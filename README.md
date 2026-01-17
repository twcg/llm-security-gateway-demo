# LLM Security Gateway Demo (Offline)

## What this is
A small **offline** “security control plane” that sits in front of an AI assistant and:
- Blocks unsafe tool actions (allow/deny)
- Blocks prompt-injection attempts
- Redacts PII in outputs
- Writes an audit trail for every request + decision

✅ No cloud creds  
✅ No model keys  
✅ Runs locally + in GitHub Actions safely

## Repo layout
- `app/` gateway + mock tools + redaction + audit log writer
- `policies/` OPA/Rego policies evaluated by Conftest
- `scripts/demo.sh` runs 3 demo scenarios
- `tests/test_policies.sh` runs Conftest tests against example inputs
- `.github/workflows/ci.yml` runs the checks on PRs/pushes

## Quickstart
Install conftest (mac):
- `brew install conftest`

Run demo:
- `chmod +x scripts/demo.sh`
- `./scripts/demo.sh`

Run policy tests:
- `chmod +x tests/test_policies.sh`
- `./tests/test_policies.sh`

## What this proves
- You can enforce **guardrails** (policy-as-code) in front of AI tools
- You can produce **audit evidence** for compliance/security reviews
- You can block **prompt injection** and **data exfiltration** patterns
