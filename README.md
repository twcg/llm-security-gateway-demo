# LLM Security Gateway Demo (Offline)

A lightweight, **offline LLM security gateway** that demonstrates how to enforce **policy-as-code guardrails** in front of AI assistants and tool execution.

This project shows how teams can secure AI systems **without cloud access, model API keys, or vendor lock-in**, while still producing **deterministic decisions and audit evidence** suitable for security reviews.

The demo runs locally and in CI, and is safe to clone, review, and test.

---

## What This Demonstrates

The gateway enforces security decisions **before any AI tool is executed**:

- Allow / deny AI tool actions using policy-as-code (OPA / Rego)
- Detect and block prompt-injection attempts
- Prevent data exfiltration patterns
- Redact PII from allowed outputs
- Generate an audit log for every request and decision

### Key Properties

- ✅ Offline only
- ✅ No LLM API keys
- ✅ No cloud credentials
- ✅ Deterministic, testable decisions
- ✅ CI-safe and reviewable

---

## Request Flow

```text
User / AI Prompt
        ↓
Security Gateway
  ├─ Prompt Injection Detection
  ├─ Tool Allowlist Enforcement
  ├─ PII Redaction
  ├─ Audit Logging
        ↓
Mock Tool Execution (Local)

app/
  gateway.py        # Request handling + enforcement flow
  policy.py         # Policy evaluation via Conftest
  tools.py          # Local mock AI tools
  redact.py         # PII redaction logic
  audit.py          # Audit log writer
  data/             # Mock datasets (CRM, HR, etc.)

policies/
  tool_allowlist.rego
  prompt_injection.rego
  pii_redaction.rego

scripts/
  demo.sh            # Runs the interactive demo scenarios

tests/
  test_policies.sh   # Runs Conftest policy tests
  inputs/            # Example request payloads

tools/
  conftest           # Pinned Conftest binary (offline)
  README.md

.github/workflows/
  ci.yml             # CI pipeline (policy + demo checks)

Demo Scenarios

The demo runs three realistic scenarios:

Scenario A — Bulk Export Attempt (DENY)
	•	User attempts to export all CRM customer data
	•	Blocked by tool allowlist policy

Scenario B — Prompt Injection Attempt (DENY)
	•	User attempts to override system instructions
	•	Blocked by prompt-injection detection

Scenario C — Authorized HR Read (ALLOW + REDACT)
	•	Analyst retrieves an employee record
	•	Allowed, with SSN redacted
	•	Decision and output are audited

Quickstart

Run the Demo
chmod +x scripts/demo.sh
./scripts/demo.sh

Run Policy Tests
chmod +x tests/test_policies.sh
./tests/test_policies.sh
Both commands run fully offline and are safe to execute locally or in CI.

⸻

What This Proves
	•	AI guardrails can be enforced outside the model
	•	Policy-as-code works for AI systems, not just infrastructure
	•	Prompt injection and unsafe tool use can be blocked deterministically
	•	AI actions can produce audit-ready security evidence
	•	Teams can test AI security controls without production access

⸻

Intended Audience
	•	Security engineers
	•	Platform / infrastructure teams
	•	AI governance & risk teams
	•	Organizations evaluating AI security controls

⸻

Notes

This is a demo project, not a production gateway.
The focus is clarity, determinism, and security posture — not performance or scale.
