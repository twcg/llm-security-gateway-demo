# LLM Security Gateway Demo (Offline)

A lightweight, **offline LLM security gateway** that demonstrates how to enforce **policy-as-code guardrails** in front of AI assistants and tool execution.

This project shows how teams can secure AI systems **without cloud access, model API keys, or vendor lock-in**, while still producing **deterministic decisions and audit evidence** suitable for security and compliance reviews.

> ✔ Runs locally  
> ✔ Runs in CI  
> ✔ Safe to fork, test, and review  

---

## Why This Exists

Most AI security discussions focus on *model behavior*.  
This project demonstrates **control-plane enforcement** — security decisions made **outside the model**, before tools are executed.

It answers the question:

> *“How do we apply the same guardrails we use for infrastructure to AI systems?”*

---

## What This Gateway Enforces

Before **any AI tool executes**, the gateway enforces:

- **Tool allow / deny decisions** (OPA / Rego)
- **Prompt-injection detection**
- **Data exfiltration prevention**
- **PII redaction on allowed outputs**
- **Audit logging for every request**

### Design Principles

- ✅ Offline-first  
- ✅ No LLM API keys  
- ✅ No cloud credentials  
- ✅ Deterministic, testable decisions  
- ✅ CI-safe execution  

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
