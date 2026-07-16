#!/usr/bin/env bash
# check-kit-versions.sh — the govkit Phase-0 contract gate. Every kit carries a well-formed version
# constant a deployer can grep in a target repo, and the one hand-kept marker/constant PAIR
# (memory-tree: engine constant + the marker in the doc it ships) agrees. Version format is the
# house two-part X.Y (matching KIT_MANIFEST_VERSION). Drift here silently defeats deployer version
# detection, so it rides the merge bar.
# Deliberate: no consumer reads these constants until the Phase-1 govkit deployer — this gate is the
# executable acceptance check for THIS unit's deliverable (version-detectability), guarding the
# constants from silent deletion/malformation, not scaffolding for a speculative feature.
#   Exit 0 = all present + consistent · 1 = a constant is missing/malformed or a marker drifted · 2 = not a repo.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
fails=0
V='[0-9]+\.[0-9]+'   # two-part X.Y; only monotone comparability matters to the deployer

need() { # label · file · extended-regex
  grep -qE "$3" "$2" 2>/dev/null || { echo "kit-versions: MISSING $1 in $2"; fails=$((fails+1)); }
}

need "KIT_MEMORY_TREE_VERSION"    tools/memory-tree/check-memory-hygiene.sh "^KIT_MEMORY_TREE_VERSION=$V([[:space:]]|\$)"
need "KIT_CODEBASE_MAP_VERSION"   tools/codebase-map/map_lib.py             "^KIT_CODEBASE_MAP_VERSION = \"$V\""
need "KIT_AGENT_CAP_VERSION"      tools/hooks/agent-cap.js                  "KIT_AGENT_CAP_VERSION = '$V'"
need "tier2-review meta.version"  tools/workflows/tier2-review.js           "version: '$V'"
need "KIT_SETTINGS_MERGE_VERSION" tools/settings-merge.py                   "KIT_SETTINGS_MERGE_VERSION = \"$V\""

# memory-tree is the only kit whose version lives in TWO hand-kept literals (engine constant + the
# marker in HYGIENE.template.md it ships verbatim). Assert they agree — a stale marker makes the
# deployer read the wrong installed version. (Token is mid-line, so CRLF working trees are fine.)
c=$(grep -oE "^KIT_MEMORY_TREE_VERSION=$V" tools/memory-tree/check-memory-hygiene.sh | head -1 | cut -d= -f2)
if [ -z "$c" ] || ! grep -qE "gov:kit memory-tree@$c([^0-9.]|\$)" tools/memory-tree/HYGIENE.template.md; then
  echo "kit-versions: HYGIENE.template.md marker != KIT_MEMORY_TREE_VERSION (${c:-unreadable})"
  fails=$((fails+1))
fi

need "KIT_PYTEST_GUARDRAILS_VERSION" tools/pytest-parallel-guardrails/crashprobe.py "^KIT_PYTEST_GUARDRAILS_VERSION = \"$V\""

# pytest-parallel-guardrails: the constant lives in crashprobe.py, but the probe is a
# hunt-then-remove diagnostic — the DEPLOYER-side version signal is the gov:kit marker in each
# artifact adopters KEEP. Assert the constant and every marker agree (memory-tree-pair style).
g=$(tr -d '\r' < tools/pytest-parallel-guardrails/crashprobe.py | grep -oE "^KIT_PYTEST_GUARDRAILS_VERSION = \"$V\"" | head -1 | grep -oE "$V")
for kept in README.md pyproject-snippet.toml aiosqlite-seam-conftest.py aiosqlite_worker_resilience.test-template.py; do
  if [ -z "$g" ] || ! grep -qE "gov:kit pytest-parallel-guardrails@$g([^0-9.]|\$)" "tools/pytest-parallel-guardrails/$kept"; then
    echo "kit-versions: pytest-parallel-guardrails marker in $kept != constant (${g:-unreadable})"
    fails=$((fails+1))
  fi
done

[ "$fails" = 0 ] && exit 0
echo "kit-versions: $fails problem(s)"
exit 1
