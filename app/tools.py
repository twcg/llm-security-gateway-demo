from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "app" / "data"

def _load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def crm_export_all() -> Dict[str, Any]:
    # Keep this inline or move to app/data/customers.json later
    customers = [
        {"customer_id": 1, "name": "Alice", "email": "alice@example.com"},
        {"customer_id": 2, "name": "Bob", "email": "bob@example.com"},
    ]
    return {"customers": customers, "count": len(customers)}

def hr_get_employee(employee_id: int) -> Dict[str, Any]:
    employees = _load_json(DATA_DIR / "employees.json")
    emp = employees.get(str(int(employee_id)))
    if not emp:
        return {"error": f"Employee {employee_id} not found"}
    return {"employee": emp}

def finance_run_report() -> Dict[str, Any]:
    return {"report": "Q4 Summary", "status": "ok"}

def run_tool(payload: Dict[str, Any]) -> Dict[str, Any]:
    tool = payload.get("tool")

    if tool == "crm_export_all":
        return crm_export_all()

    if tool == "hr_get_employee":
        employee_id = payload.get("employee_id", 1001)
        return hr_get_employee(employee_id)

    if tool == "finance_run_report":
        return finance_run_report()

    return {"error": f"Unknown/blocked tool (mock): {tool}"}
