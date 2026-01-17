from __future__ import annotations

import os
import subprocess
from pathlib import Path
import shutil
from typing import Dict, List, Any, Tuple


REPO_ROOT = Path(__file__).resolve().parents[1]


def _pick_conftest_bin() -> str:
    """
    Prefer CI/system conftest on GitHub Actions, but keep local offline support.

    Order:
      1) CONFTEST_BIN env var (e.g., "conftest" or "/usr/local/bin/conftest")
      2) system PATH lookup (shutil.which("conftest"))
      3) repo-pinned binary at ./tools/conftest (your offline Mac setup)
    """
    env_bin = os.environ.get("CONFTEST_BIN")
    if env_bin:
        return env_bin

    which_bin = shutil.which("conftest")
    if which_bin:
        return which_bin

    return str(REPO_ROOT / "tools" / "conftest")


def _clean_conftest_output(stdout: str) -> List[str]:
    """
    conftest outputs lines like:
      FAIL - file - namespace - message
    We want just the message part, clean and executive-friendly.
    """
    reasons: List[str] = []
    for line in (stdout or "").splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("FAIL - "):
            # Keep only the last " - " segment as the message
            parts = line.split(" - ")
            reasons.append(parts[-1].strip())
        elif line.startswith("WARN - "):
            # Optional: include warnings if you want
            parts = line.split(" - ")
            reasons.append(f"WARNING: {parts[-1].strip()}")
    return reasons


def evaluate_policies(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Uses Conftest: if policies produce any deny messages, conftest exits non-zero.

    Returns:
      {
        "allow": bool,
        "reasons": [str, ...]
      }
    """
    conftest_bin = _pick_conftest_bin()

    # Write payload to a temp input file under app/logs (exists in repo)
    logs_dir = REPO_ROOT / "app" / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    input_path = logs_dir / "_input_tmp.json"
    input_path.write_text(__import__("json").dumps(payload, indent=2))

    cmd = [
        conftest_bin,
        "test",
        str(input_path),
        "-p",
        str(REPO_ROOT / "policies"),
        "--all-namespaces",
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True)

    # conftest exit code:
    #   0 => allow (no deny rules fired)
    #   non-zero => deny (one or more deny rules fired)
    if proc.returncode == 0:
        return {"allow": True, "reasons": ["All policies passed"]}

    reasons = _clean_conftest_output(proc.stdout)
    if not reasons:
        # Fallback if formatting changes
        reasons = [proc.stdout.strip() or "Policy denied (no details)"]

    return {"allow": False, "reasons": reasons}
