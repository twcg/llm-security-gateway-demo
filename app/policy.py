from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFTEST = REPO_ROOT / "tools" / "conftest"
POLICY_DIR = REPO_ROOT / "policies"
TMP_INPUT = REPO_ROOT / "app" / "logs" / "_input_tmp.json"

ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def _strip_ansi(s: str) -> str:
    return ANSI_RE.sub("", s)


def _extract_denies(stdout: str) -> List[str]:
    """
    Conftest prints deny messages like:
      FAIL - <file> - <namespace> - DENY: <message>
    We normalize those into just the message strings.
    """
    reasons: List[str] = []
    for line in _strip_ansi(stdout).splitlines():
        m = re.search(r"DENY:\s*(.*)$", line)
        if m:
            reasons.append(m.group(1).strip())
    return reasons


def evaluate_policies(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Returns: {"allow": bool, "reasons": [str, ...]}
    allow=True when conftest exits 0 (no deny rules fired).
    allow=False when conftest exits non-zero (one or more deny rules fired).
    """
    TMP_INPUT.parent.mkdir(parents=True, exist_ok=True)
    TMP_INPUT.write_text(json.dumps(payload, indent=2))

    cmd = [
        str(CONFTEST),
        "test",
        str(TMP_INPUT),
        "-p",
        str(POLICY_DIR),
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True)
    stdout = proc.stdout or ""
    stderr = proc.stderr or ""
    combined = (stdout + "\n" + stderr).strip()

    if proc.returncode == 0:
        return {"allow": True, "reasons": ["All policies passed"]}

    reasons = _extract_denies(combined)
    if not reasons:
        # Fallback if output format changes
        reasons = [_strip_ansi(combined)] if combined else ["Policy denied (no details)"]

    return {"allow": False, "reasons": reasons}
