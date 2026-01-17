LLM Security Gateway Demo (Offline)

Overview

This repository demonstrates a lightweight, offline LLM security gateway — a policy-enforced control plane that sits in front of AI assistants and tool execution.

It shows how teams can apply policy-as-code guardrails to AI systems without requiring cloud access, model keys, or vendor lock-in.

The demo runs locally and in CI, and is safe to review, fork, and test.

⸻

What This Demonstrates

The gateway enforces security decisions before any AI tool is executed:
	•	Allow / deny AI tool actions using policy-as-code (OPA / Rego)
	•	Detect and block prompt-injection attempts
	•	Prevent data exfiltration patterns
	•	Redact PII from allowed outputs
	•	Generate an audit log for every request and decision

✔ Offline only
✔ No LLM API keys
✔ No cloud credentials
✔ Deterministic, testable decisions

User / AI Prompt
        ↓
 Security Gateway
   ├── Prompt Injection Detection
   ├── Tool Allowlist Enforcement
   ├── PII Redaction
   ├── Audit Logging
        ↓
  Mock Tool Execution (Local)

  app/
  gateway.py        # Request handling + enforcement flow
  policy.py         # Policy evaluation via Conftest
  tools.py          # Local mock AI tools (CRM / HR / Finance)
  redact.py         # PII redaction logic
  audit.py          # JSONL audit logging
  data/             # Sample local datasets
  logs/             # Audit logs (gitignored)

policies/
  tool_allowlist.rego
  prompt_injection.rego
  pii_redaction.rego

scripts/
  demo.sh           # Runs demo scenarios end-to-end

tests/
  test_policies.sh  # Policy tests via Conftest
  inputs/           # Example request inputs

.github/workflows/
  ci.yml            # CI validation (policy + demo)

  Demo Scenarios

Running the demo executes three realistic scenarios:

Scenario A — Bulk Export (DENIED)

User attempts to export all CRM customers

Result: ❌ DENIED
Reason: Requires admin role and explicit approval

⸻

Scenario B — Prompt Injection (DENIED)

Prompt attempts to override instructions and exfiltrate data

Result: ❌ DENIED
Reason: Injection + exfiltration patterns detected

⸻

Scenario C — Authorized HR Read (ALLOWED)

Analyst requests an employee record

Result: ✅ ALLOWED
Protection: SSN is automatically redacted
Audit: Decision is logged

⸻

Quick Start

Install Conftest

macOS
brew install conftest
(Linux CI installs Conftest automatically)

chmod +x scripts/demo.sh
./scripts/demo.sh

chmod +x tests/test_policies.sh
./tests/test_policies.sh
