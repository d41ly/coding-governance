#!/usr/bin/env bash
# run-gates.sh — the coding-governance merge bar: run every gate this repo dogfoods, report per leg.
# The full bar green at the push boundary; earlier runs scoped. Exit 0 = all passed · 1 = one or more failed · 2 = must run from the repo.
#   bash tools/run-gates.sh
set -u
ROOT=$(git rev-parse --show-toplevel 2>/dev/null) || { echo "run-gates: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
PYBIN=python3; command -v python3 >/dev/null 2>&1 || PYBIN=python
fails=0; n=0; skips=0

# Baseline for conditional legs: the mainline tip we gate against. Override with GATE_BASE.
# Unresolvable (no remote / shallow / detached) → empty, and changed() fails safe to "run".
DEFBR=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null); DEFBR=${DEFBR#origin/}
BASE=$(git rev-parse --verify -q "${GATE_BASE:-origin/${DEFBR:-main}}" 2>/dev/null) || BASE=
changed() { [ -z "$BASE" ] && return 0; ! git diff --quiet "$BASE" -- "$@" 2>/dev/null; }

leg() { # name · command...
  local name=$1; shift; n=$((n+1))
  local out; out=$("$@" </dev/null 2>&1); local rc=$?   # legs never read stdin — deny it so a stray reader can't hang the bar
  if [ "$rc" = 0 ]; then printf 'GATE ok    %s\n' "$name"
  else fails=$((fails+1)); printf 'GATE FAIL  %s (exit %d)\n' "$name" "$rc"; printf '%s\n' "$out" | sed 's/^/    /'; fi
}

leg_if_changed() { # guard-path[,guard-path...] · name · command...  (leg() counts n on run; skip counts here)
  local guard=$1 name=$2; shift 2
  local paths; IFS=, read -ra paths <<<"$guard"
  if changed "${paths[@]}"; then leg "$name" "$@"
  else n=$((n+1)); skips=$((skips+1)); printf 'GATE skip  %s (unchanged vs %s)\n' "$name" "${DEFBR:-baseline}"; fi
}

leg "memory hygiene (12 checks)"      bash tools/memory-tree/check-memory-hygiene.sh
leg "kickoff-manifest ratchet"        bash skills/session-kickoff/manifest-check.sh
leg "template size <=32KiB"           bash tools/check-template-size.sh
leg "kit version markers"             bash tools/check-kit-versions.sh
leg "agent-instructions wiring"       bash tools/agent-instructions/adopt-agent-instructions.sh --check --aliases claude
leg_if_changed "skills/session-kickoff/manifest-check.sh,skills/session-kickoff/manifest-check.test.sh" \
      "manifest-check self-test"        bash skills/session-kickoff/manifest-check.test.sh
leg "agent-cap self-test"             bash tools/hooks/agent-cap.test.sh
leg "agent-instructions self-test"    bash tools/agent-instructions/adopt-agent-instructions.test.sh
leg "memory-hygiene self-test"        bash tools/memory-tree/check-memory-hygiene.test.sh
leg "branch-guard self-test"          bash .githooks/pre-commit.test.sh
leg "check-wiring self-test"          bash tools/check-wiring.test.sh
leg "pytest-guardrails self-test"     bash tools/pytest-parallel-guardrails/pytest-parallel-guardrails.test.sh
leg "codebase-map kit selftest"       "$PYBIN" tools/codebase-map/selftest.py
leg "settings-merge selftest"         "$PYBIN" tools/settings-merge.py --selftest

echo "----"
skipnote=""; [ "$skips" -gt 0 ] && skipnote=" ($skips skipped)"
if [ "$fails" = 0 ]; then echo "gates GREEN — $((n-skips))/$((n-skips)) legs passed$skipnote"; exit 0
else echo "gates RED — $fails/$n legs failed$skipnote"; exit 1; fi
