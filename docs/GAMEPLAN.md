# LLM Security Gateway Demo — Game Plan (Offline)

Goal: Build an offline security gateway that:
- Denies unsafe tool actions (allowlist)
- Denies prompt-injection attempts
- Redacts PII in outputs
- Logs every request/decision/result to audit JSONL

Scenarios:
A) Export all CRM customers -> DENY
B) Prompt injection tries to force tool execution -> DENY
C) Read employee record -> ALLOW but redact SSN
