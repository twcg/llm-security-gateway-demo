from __future__ import annotations

import re
from typing import Any, Dict

# Very small offline redaction set (portfolio-friendly)
SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
DOB_RE = re.compile(r"\b(19|20)\d{2}-\d{2}-\d{2}\b")  # YYYY-MM-DD

def _redact_string(s: str) -> str:
    s = SSN_RE.sub("***-**-****", s)
    s = DOB_RE.sub("****-**-**", s)
    s = EMAIL_RE.sub("***@***", s)
    return s

def _walk(obj: Any) -> Any:
    if isinstance(obj, str):
        return _redact_string(obj)
    if isinstance(obj, list):
        return [_walk(x) for x in obj]
    if isinstance(obj, dict):
        # redact common key names even if value isn't a perfect regex match
        out: Dict[str, Any] = {}
        for k, v in obj.items():
            lk = str(k).lower()
            if lk in {"ssn", "social", "social_security_number"}:
                out[k] = "***-**-****"
            elif lk in {"dob", "date_of_birth"}:
                out[k] = "****-**-**"
            else:
                out[k] = _walk(v)
        return out
    return obj

def redact_result(result: Any, payload: Dict[str, Any] | None = None) -> Any:
    """
    Redact sensitive data from tool output.
    Compatible with gateway calling patterns:
      - redact_result(result)
      - redact_result(result, payload)
    """
    return _walk(result)
