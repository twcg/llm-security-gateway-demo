from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

DEFAULT_AUDIT_PATH = Path(__file__).resolve().parent / "logs" / "audit.jsonl"

def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

def write_audit(entry: Dict[str, Any], path: Optional[str] = None) -> None:
    """
    Write a single JSONL audit record.

    Supports:
      - write_audit(entry)  -> writes to default app/logs/audit.jsonl
      - write_audit(entry, path=".../audit.jsonl") -> custom path
    """
    audit_path = Path(path) if path else DEFAULT_AUDIT_PATH
    _ensure_parent(audit_path)

    # Ensure we always have a timestamp
    if "ts" not in entry:
        entry["ts"] = _now_iso()

    with audit_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
