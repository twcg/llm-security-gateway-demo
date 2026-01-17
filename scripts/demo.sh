#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Use CI-installed conftest if present, otherwise local offline binary
CONFTEST_BIN="${CONFTEST_BIN:-"$REPO_ROOT/tools/conftest"}"

echo "=== Repo root ==="
echo "$REPO_ROOT"
echo ""

echo "=== Conftest version (offline pinned) ==="
$CONFTEST_BIN --version
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
