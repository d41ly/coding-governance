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

# agent-cap: constant and marker sit on ONE line, which is why this pair was presence-checked only —
# and a half-bumped pair therefore passed. Assert they agree like every other pair; "same line" is
# not "same value", and the marker is what a deployer greps in an adopting tree.
ac=$(grep -oE "KIT_AGENT_CAP_VERSION = '$V'" tools/hooks/agent-cap.js | head -1 | grep -oE "$V")
if [ -z "$ac" ] || ! grep -qE "gov:kit agent-cap@$ac([^0-9.]|\$)" tools/hooks/agent-cap.js; then
  echo "kit-versions: agent-cap.js gov:kit marker != KIT_AGENT_CAP_VERSION (${ac:-unreadable})"
  fails=$((fails+1))
fi
need "KIT_SETTINGS_MERGE_VERSION" tools/settings-merge.py                   "KIT_SETTINGS_MERGE_VERSION = \"$V\""

# settings-merge: constant plus the marker in its own module docstring, which is where a deployer
# reads the version of a single-file kit. Presence-only left a half-bumped pair passing, same as
# agent-cap's.
sm=$(grep -oE "^KIT_SETTINGS_MERGE_VERSION = \"$V\"" tools/settings-merge.py | head -1 | grep -oE "$V")
if [ -z "$sm" ] || [ "$(grep -cE "gov:kit settings-merge@$sm([^0-9.]|\$)" tools/settings-merge.py)" -lt 2 ]; then
  echo "kit-versions: settings-merge.py gov:kit markers != KIT_SETTINGS_MERGE_VERSION (${sm:-unreadable})"
  fails=$((fails+1))
fi

# memory-tree is the only kit whose version lives in TWO hand-kept literals (engine constant + the
# marker in HYGIENE.template.md it ships verbatim). Assert they agree — a stale marker makes the
# deployer read the wrong installed version. (Token is mid-line, so CRLF working trees are fine.)
c=$(grep -oE "^KIT_MEMORY_TREE_VERSION=$V" tools/memory-tree/check-memory-hygiene.sh | head -1 | cut -d= -f2)
if [ -z "$c" ] || ! grep -qE "gov:kit memory-tree@$c([^0-9.]|\$)" tools/memory-tree/HYGIENE.template.md; then
  echo "kit-versions: HYGIENE.template.md marker != KIT_MEMORY_TREE_VERSION (${c:-unreadable})"
  fails=$((fails+1))
fi

need "KIT_UNATTENDED_VERSION"     tools/unattended/unattended.sh            "^KIT_UNATTENDED_VERSION=$V([[:space:]]|\$)"
# The unattended kit carries its version in TWO hand-kept literals — the driver and the leg — and the
# leg's own comment claimed this gate paired them while nothing did. Same shape as memory-tree below.
u=$(grep -oE "^KIT_UNATTENDED_VERSION=$V" tools/unattended/unattended.sh | head -1 | cut -d= -f2)
if [ -z "$u" ] || ! grep -qE "^KIT_UNATTENDED_VERSION=$u([^0-9.]|\$)" tools/unattended/check-unattended.sh; then
  echo "kit-versions: check-unattended.sh KIT_UNATTENDED_VERSION != unattended.sh (${u:-unreadable})"
  fails=$((fails+1))
fi
need "KIT_MEMORY_RECALL_VERSION"  tools/memory-recall/recall_conf.py         "^KIT_MEMORY_RECALL_VERSION = \"$V\""

# memory-recall: constant in recall_conf.py, marker in the README the adopter keeps. Same pair
# assertion as memory-tree — a stale marker makes the deployer read the wrong installed version.
r=$(grep -oE "^KIT_MEMORY_RECALL_VERSION = \"$V\"" tools/memory-recall/recall_conf.py | head -1 | grep -oE "$V")
if [ -z "$r" ] || ! grep -qE "gov:kit memory-recall@$r([^0-9.]|\$)" tools/memory-recall/README.md; then
  echo "kit-versions: memory-recall README marker != KIT_MEMORY_RECALL_VERSION (${r:-unreadable})"
  fails=$((fails+1))
fi

need "KIT_DRIFT_AUDIT_VERSION"    tools/drift-audit/drift_report.py          "^KIT_DRIFT_AUDIT_VERSION = \"$V\""

# drift-audit: constant in drift_report.py, marker in the README the adopter keeps. Same pair
# assertion as memory-tree/memory-recall — a stale marker makes the deployer read the wrong version.
da=$(grep -oE "^KIT_DRIFT_AUDIT_VERSION = \"$V\"" tools/drift-audit/drift_report.py | head -1 | grep -oE "$V")
if [ -z "$da" ] || ! grep -qE "gov:kit drift-audit@$da([^0-9.]|\$)" tools/drift-audit/README.md; then
  echo "kit-versions: drift-audit README marker != KIT_DRIFT_AUDIT_VERSION (${da:-unreadable})"
  fails=$((fails+1))
fi

need "drift-audit-code meta.version"  tools/workflows/drift-audit-code.js  "version: '$V'"
need "drift-audit-state meta.version" tools/workflows/drift-audit-state.js "version: '$V'"

# ...and each harness's meta.version agrees with the kit constant AND with its own gov:kit marker.
# The harnesses ship the kit's `args` contract, so a contract narrowing that moves the engine version
# and leaves a harness at the old one tells an adopter the wrong thing about the file they actually run.
for h in code state; do
  hv=$(grep -oE "version: '$V'" "tools/workflows/drift-audit-$h.js" | head -1 | grep -oE "$V")
  if [ -z "$hv" ] || [ "$hv" != "$da" ]; then
    echo "kit-versions: drift-audit-$h.js meta.version (${hv:-unreadable}) != KIT_DRIFT_AUDIT_VERSION (${da:-unreadable})"
    fails=$((fails+1))
  elif ! grep -qE "gov:kit drift-audit@$hv([^0-9.]|\$)" "tools/workflows/drift-audit-$h.js"; then
    echo "kit-versions: drift-audit-$h.js gov:kit marker != its own meta.version ($hv)"
    fails=$((fails+1))
  fi
done

need "KIT_PYTEST_GUARDRAILS_VERSION" tools/pytest-parallel-guardrails/crashprobe.py "^KIT_PYTEST_GUARDRAILS_VERSION = \"$V\""
need "KIT_GOVKIT_VERSION"          tools/govkit/govkit.py                    "^KIT_GOVKIT_VERSION = \"$V\""

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
