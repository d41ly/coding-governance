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
need "KIT_MANIFEST_VERSION"       skills/session-kickoff/manifest-check.sh  "^KIT_MANIFEST_VERSION=\"$V\""

# The kickoff manifest format: the constant in the checker, and the marker in the SEED an adopter
# instantiates from. Nothing forced these to agree before — this file had no entry for the constant
# and the verdict-epoch gate is hardcoded to the memory-tree engine — so the checker could demand a
# key the shipped template did not carry, with the full bar green. That is the same hole this file's
# own header describes for the doc templates, which went three bumps behind and shipped the wrong
# number into every adopting tree.
mv_c=$(grep -oE "^KIT_MANIFEST_VERSION=\"$V\"" skills/session-kickoff/manifest-check.sh | head -1 | grep -oE "$V")
mv_t=$(grep -oE "kickoff-manifest: v$V" skills/session-kickoff/MANIFEST-TEMPLATE.md | head -1 | grep -oE "$V")
if [ -z "$mv_c" ]; then
  echo "kit-versions: KIT_MANIFEST_VERSION is unreadable, so the shipped manifest seed cannot be compared against it"
  fails=$((fails+1))
elif [ "$mv_c" != "$mv_t" ]; then
  echo "kit-versions: MANIFEST-TEMPLATE.md marker (${mv_t:-unreadable}) != KIT_MANIFEST_VERSION ($mv_c) — an adopter would instantiate a seed the checker rejects"
  fails=$((fails+1))
fi

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

# memory-tree's version lives in the engine constant AND in a marker on every doc the kit SHIPS and
# an adopter RENDERS. Assert they all agree — a stale marker makes the deployer, and the adopter
# reading its own installed rule-set, believe a version the kit disagrees with.
#
# ENUMERATED, NOT NAMED. This block used to name HYGIENE.template.md alone, and the two siblings it
# did not name drifted exactly as you would expect: BUILD-METHOD.template.md sat three bumps behind
# and shipped that number into every adopting tree, and SPEC-TEMPLATE.template.md carried no marker
# at all, which is the same hole one level down — a shipped doc that self-identifies as nothing
# cannot be caught by any comparison. Naming one file is why the hole reopened at every bump. The
# population is DERIVED from the tree, so the next shipped template is covered by existing.
#
# The decoy fixtures in check-verdict-epoch.test.sh are excluded by construction rather than by a
# special case: they are not `*.template.md`, so this glob never sees them.
# (The token is mid-line, so a CRLF working tree is fine.)
c=$(grep -oE "^KIT_MEMORY_TREE_VERSION=$V" tools/memory-tree/check-memory-hygiene.sh | head -1 | cut -d= -f2)
if [ -z "$c" ]; then
  echo "kit-versions: KIT_MEMORY_TREE_VERSION is unreadable, so no marker can be compared against it"
  fails=$((fails+1))
else
  mt_templates=$(git ls-files 'tools/memory-tree/*.template.md' 2>/dev/null)
  if [ -z "$mt_templates" ]; then
    # An empty population would make every assertion below vacuously true, which is the failure this
    # repo names `vacuous-selector-empty-population`. It is a refusal, not a pass.
    echo "kit-versions: no tracked tools/memory-tree/*.template.md — the marker assertion would be vacuous"
    fails=$((fails+1))
  fi
  for t in $mt_templates; do
    if ! grep -qE "gov:kit memory-tree@$V" "$t"; then
      echo "kit-versions: $t ships with NO gov:kit memory-tree@ marker — an adopter renders it and cannot tell which kit version they hold"
      fails=$((fails+1))
    elif ! grep -qE "gov:kit memory-tree@$c([^0-9.]|\$)" "$t"; then
      echo "kit-versions: $t marker != KIT_MEMORY_TREE_VERSION ($c)"
      fails=$((fails+1))
    fi
  done
fi

# unattended's version lives in TWO engine constants and in a marker on every doc the kit SHIPS.
# check-kit-versions paired the two CONSTANTS and not the shipped docs, which is how
# PROTOCOL.template.md sat at @1.2 against 1.3 unnoticed — the exact hole memory-tree's block above
# was widened to close, one kit over. Filed as TOOL-cFinalBerth-3; this is that row.
#
# ENUMERATED, NOT NAMED, for the reason the block above records: naming one file is why the hole
# reopens at every bump. The population is DERIVED, so the next shipped template is covered already.
#
# The two INLINE markers that share a line with each constant are paired too. Same line is NOT same
# value: agent-cap's same-line pair is the recorded case where a half-bumped constant and marker
# passed because nothing compared them to each other.
uc=$(grep -oE "^KIT_UNATTENDED_VERSION=$V" tools/unattended/unattended.sh | head -1 | cut -d= -f2)
if [ -z "$uc" ]; then
  echo "kit-versions: KIT_UNATTENDED_VERSION is unreadable in unattended.sh, so no marker can be compared against it"
  fails=$((fails+1))
else
  for s in tools/unattended/unattended.sh tools/unattended/check-unattended.sh; do
    if ! grep -qE "^KIT_UNATTENDED_VERSION=$uc([^0-9.]|\$)" "$s"; then
      echo "kit-versions: $s KIT_UNATTENDED_VERSION != $uc — the driver and its leg disagree about which kit this is"
      fails=$((fails+1))
    fi
    if ! grep -qE "gov:kit unattended@$uc([^0-9.]|\$)" "$s"; then
      echo "kit-versions: $s carries a same-line gov:kit unattended@ marker that disagrees with $uc — same line is not same value"
      fails=$((fails+1))
    fi
  done
  un_templates=$(git ls-files 'tools/unattended/*.template.md' 2>/dev/null)
  if [ -z "$un_templates" ]; then
    echo "kit-versions: no tracked tools/unattended/*.template.md — the marker assertion would be vacuous"
    fails=$((fails+1))
  fi
  for t in $un_templates; do
    if ! grep -qE "gov:kit unattended@$V" "$t"; then
      echo "kit-versions: $t ships with NO gov:kit unattended@ marker — an adopter renders it and cannot tell which kit version they hold"
      fails=$((fails+1))
    elif ! grep -qE "gov:kit unattended@$uc([^0-9.]|\$)" "$t"; then
      echo "kit-versions: $t marker != KIT_UNATTENDED_VERSION ($uc)"
      fails=$((fails+1))
    fi
  done
fi

need "KIT_UNATTENDED_VERSION"     tools/unattended/unattended.sh            "^KIT_UNATTENDED_VERSION=$V([[:space:]]|\$)"
# The driver/leg constant pairing that used to sit here is SUBSUMED by the unattended block below,
# which derives the same $uc from the same file and asserts the same regex against the same second
# file — one defect, two messages, two increments, and two copies to keep in step. Deleted rather
# than kept as a second opinion, because a re-implementation of an assertion is not one.
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
