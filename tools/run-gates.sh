#!/usr/bin/env bash
# run-gates.sh — the coding-governance merge bar: run every gate this repo dogfoods, report per leg.
# All green before any merge. Exit 0 = all passed · 1 = one or more failed · 2 = must run from the repo.
#   bash tools/run-gates.sh
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "run-gates: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
PYBIN=python3; command -v python3 >/dev/null 2>&1 || PYBIN=python
fails=0; n=0

leg() { # name · command...
  local name=$1; shift; n=$((n+1))
  local out; out=$("$@" 2>&1); local rc=$?
  if [ "$rc" = 0 ]; then printf 'GATE ok    %s\n' "$name"
  else fails=$((fails+1)); printf 'GATE FAIL  %s (exit %d)\n' "$name" "$rc"; printf '%s\n' "$out" | sed 's/^/    /'; fi
}

leg "memory hygiene (12 checks)"      bash tools/memory-tree/check-memory-hygiene.sh
leg "kickoff-manifest ratchet"        bash skills/session-kickoff/manifest-check.sh
leg "template size <=32KiB"           bash tools/check-template-size.sh
leg "kit version markers"             bash tools/check-kit-versions.sh
leg "agent-instructions wiring"       bash tools/agent-instructions/adopt-agent-instructions.sh --check --aliases claude
leg "manifest-check self-test"        bash skills/session-kickoff/manifest-check.test.sh
leg "agent-cap self-test"             bash tools/hooks/agent-cap.test.sh
leg "agent-instructions self-test"    bash tools/agent-instructions/adopt-agent-instructions.test.sh
leg "memory-hygiene self-test"        bash tools/memory-tree/check-memory-hygiene.test.sh
leg "branch-guard self-test"          bash .githooks/pre-commit.test.sh
leg "check-wiring self-test"          bash tools/check-wiring.test.sh
leg "pytest-guardrails self-test"     bash tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh
leg "codebase-map kit selftest"       "$PYBIN" tools/codebase-map/selftest.py
leg "settings-merge selftest"         "$PYBIN" tools/settings-merge.py --selftest

echo "----"
if [ "$fails" = 0 ]; then echo "gates GREEN — $n/$n legs passed"; exit 0
else echo "gates RED — $fails/$n legs failed"; exit 1; fi
