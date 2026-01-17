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
