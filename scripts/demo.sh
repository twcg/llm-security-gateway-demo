#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "=== Repo root ==="
echo "$REPO_ROOT"
echo ""

echo "=== Conftest version (offline pinned) ==="
"$REPO_ROOT/tools/conftest" --version
echo ""

# Generate/refresh test inputs, but keep output quiet for an "executive clean" demo
"$REPO_ROOT/tests/test_policies.sh" >/dev/null

echo ""
echo "=== Running demo scenarios ==="
echo ""

echo "=== Scenario A — Bulk export attempt (should DENY) ==="
python3 "$REPO_ROOT/app/gateway.py" --scenario a
echo ""

echo "=== Scenario B — Prompt injection attempt (should DENY) ==="
python3 "$REPO_ROOT/app/gateway.py" --scenario b
echo ""

echo "=== Scenario C — Authorized HR read (should ALLOW + redact) ==="
python3 "$REPO_ROOT/app/gateway.py" --scenario c
echo ""

# Optional: show audit log only when explicitly requested
if [[ "${SHOW_AUDIT:-0}" == "1" ]]; then
  echo "=== Audit log (last 20 lines) ==="
  tail -n 20 "$REPO_ROOT/app/logs/audit.jsonl" 2>/dev/null || true
fi
