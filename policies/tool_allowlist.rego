package main

deny[msg] {
  input.tool == "crm_export_all"
  input.action == "bulk_export"
  not admin_approved
  msg := "DENY: bulk export requires role=admin AND approval=true"
}

deny[msg] {
  input.action == "exfiltrate"
  msg := "DENY: suspected exfiltration action"
}

admin_approved {
  input.role == "admin"
  input.approval == true
}
