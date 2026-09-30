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
_self_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd) || _self_dir=""  # before the cd: $0 may be relative
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
# TOOL-aRepatriatedFork-29 S3 — THE CARRIERS ARE DECLARED, THE ROOT THEY SIT UNDER IS DERIVED. Every
# row below names its carrier kit-relatively and joins it to `K`, the directory this gate sits in,
# so gov's own version gate grades gov at whatever kit root it was checked out under. The population
# stays a declaration: deriving it by glob would make a carrier that forgets its constant vanish from
# its own check. `git -C <dir> rev-parse --show-prefix` and not a string strip, because a Windows
# junction makes two spellings of one tree differ; an empty answer is the repo root, told apart from
# a failure by git's exit status.
if ! K=$(git -C "$_self_dir" rev-parse --show-prefix 2>/dev/null); then
  echo "kit-versions: cannot derive this gate's own directory from '$_self_dir' — REFUSING rather than guessing the kit root"
  exit 2
fi
# TOOL-aRepatriatedFork-46: EVERY CARRIER'S KIT IS RESOLVED, never typed. The rows below used to join
# a kit's name to `K`, which is the class the carried-prefix ban counts: a kit homed under another
# name, which the install receipt records, read as MISSING here. The sibling-kit resolver reads that
# receipt first, then probes beside this gate and one level up. A kit it cannot find is spelled
# `<no KIT kit>`, so its rows red as MISSING by name rather than disappearing from the check.
# >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
# The sibling-kit resolver (TOOL-aRepatriatedFork-2 S3), INLINED byte-identically from the
# canonical copy named on its marker line and gated by the resolve-python self-test's parity
# table. A shell consumer runs it with the python it already resolved, so the receipt rung is
# read in Python and never parsed in bash. `resolve_kit_dir <python> <home> <anchor> <here>`
# prints the kit directory REPO-RELATIVE, or the resolver's named refusal on stderr and exits 1.
resolve_kit_dir() {
  "$1" -c "$(cat <<'RKD'
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).resolve()
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
            continue
        hit = (root / str(row["path"])).resolve()
        if hit.is_file() and root in hit.parents:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir
RKD
)"'
import sys
try:
    d = resolve_kit_dir(*sys.argv[1:4])
except LookupError as e:
    sys.exit(str(e))
r = next((p for p in (d, *d.parents) if (p / ".git").exists()), d.anchor)
print(d.relative_to(r).as_posix())' "$2" "$3" "$4"
}
KV_PY=$(resolve_python) || { echo "kit-versions: no usable python, so the carriers' kits cannot be resolved — REFUSING rather than guessing the kit root"; exit 2; }
resolve_carrier_kit() { # <home> <anchor> -> the kit's repo-relative directory, or a name that resolves nowhere
  resolve_kit_dir "$KV_PY" "$1" "$2" "$_self_dir" 2>/dev/null || printf '<no %s kit>\n' "$1"
}
MT_DIR=$(resolve_carrier_kit memory-tree check-memory-hygiene.sh)
CM_DIR=$(resolve_carrier_kit codebase-map map_lib.py)
HK_DIR=$(resolve_carrier_kit hooks agent-cap.js)
WF_DIR=$(resolve_carrier_kit workflows tier2-review.js)
RG_DIR=$(resolve_carrier_kit run-gates run-gates.sh)
UN_DIR=$(resolve_carrier_kit unattended unattended.sh)
MR_DIR=$(resolve_carrier_kit memory-recall recall_conf.py)
DA_DIR=$(resolve_carrier_kit drift-audit drift_report.py)
PG_DIR=$(resolve_carrier_kit pytest-parallel-guardrails crashprobe.py)
GK_DIR=$(resolve_carrier_kit govkit govkit.py)
LX_DIR=$(resolve_carrier_kit lexicon lexicon.py)
checked=0
fails=0
V='[0-9]+\.[0-9]+'   # two-part X.Y; only monotone comparability matters to the deployer

need() { # label · file · extended-regex
  checked=$((checked+1))
  grep -qE "$3" "$2" 2>/dev/null || { echo "kit-versions: MISSING $1 in $2"; fails=$((fails+1)); }
}

need "KIT_MEMORY_TREE_VERSION"    ${MT_DIR}/check-memory-hygiene.sh "^KIT_MEMORY_TREE_VERSION=$V([[:space:]]|\$)"
need "KIT_CODEBASE_MAP_VERSION"   ${CM_DIR}/map_lib.py             "^KIT_CODEBASE_MAP_VERSION = \"$V\""
need "KIT_AGENT_CAP_VERSION"      ${HK_DIR}/agent-cap.js                  "KIT_AGENT_CAP_VERSION = '$V'"
# The harness path, bound ONCE. It was spelled at three sites after TOOL-dRetiredFork-7 and the
# install-prefix ratchet is shrink-only, so a literal per use is a regression an adopter pays
# for: apply ships these bytes verbatim and a carried `tools/` path resolves to nothing at
# another prefix.
T2R="${WF_DIR}/tier2-review.js"
need "tier2-review meta.version"  "$T2R"                                   "version: '$V'"
need "KIT_MANIFEST_VERSION"       skills/session-kickoff/manifest-check.sh  "^KIT_MANIFEST_VERSION=\"$V\""

# tier2-review.js carries THREE version tokens on one line: `meta.version`, a `gov:kit tier2-review@`
# marker and a `gov:kit review-harness@` marker — BOTH ids, because the file ships under two kit
# names. Only the first was paired. Found by TOOL-dRetiredFork-7's AC5, which required the gate to go
# RED with the marker reverted rather than accepting a bare post-bump green: reverting
# `review-harness@` alone left this gate at exit 0, so that carrier could drift a whole release
# without anything noticing. An unpaired version marker is not a version carrier; it is a comment.
for id in tier2-review review-harness; do
  mk=$(grep -oE "gov:kit $id@$V" "$T2R" | head -1 | grep -oE "$V")
  tv=$(grep -oE "version: '$V'" "$T2R" | head -1 | grep -oE "$V")
  if [ -z "$mk" ] || [ "$mk" != "$tv" ]; then
    echo "kit-versions: $T2R gov:kit $id@ marker (${mk:-unreadable}) != its meta.version (${tv:-unreadable})"
    fails=$((fails+1))
  fi
done

# The kickoff manifest format: the constant in the checker, and the marker in the SEED an adopter
# instantiates from. Nothing forced these to agree before — this file had no entry for the constant
# and the verdict-epoch gate is hardcoded to the memory-tree engine — so the checker could demand a
# key the shipped template did not carry, with the full bar green. That is the same hole this file's
# own header describes for the doc templates, which went three bumps behind and shipped the wrong
# number into every adopting tree.
# TOOL-aRepatriatedFork-15 S4: the seed is compared with MANIFEST_FORMAT, not with the kit vintage.
# The two were one number, so a vintage bump forced a seed marker bump and told every adopter their
# manifest format was stale when only the kit's bytes had moved. Both are still required to parse.
need "MANIFEST_FORMAT"            skills/session-kickoff/manifest-check.sh  "^MANIFEST_FORMAT=\"$V\""
mv_c=$(grep -oE "^MANIFEST_FORMAT=\"$V\"" skills/session-kickoff/manifest-check.sh | head -1 | grep -oE "$V")
mv_t=$(grep -oE "kickoff-manifest: v$V" skills/session-kickoff/MANIFEST-TEMPLATE.md | head -1 | grep -oE "$V")
if [ -z "$mv_c" ]; then
  echo "kit-versions: MANIFEST_FORMAT is unreadable, so the shipped manifest seed cannot be compared against it"
  fails=$((fails+1))
elif [ "$mv_c" != "$mv_t" ]; then
  echo "kit-versions: MANIFEST-TEMPLATE.md marker (${mv_t:-unreadable}) != MANIFEST_FORMAT ($mv_c) — an adopter would instantiate a seed the checker rejects"
  fails=$((fails+1))
fi
# ...and the vintage's same-line marker agrees with the vintage. Same line is not same value.
mv_k=$(grep -oE "^KIT_MANIFEST_VERSION=\"$V\"" skills/session-kickoff/manifest-check.sh | head -1 | grep -oE "$V")
if [ -z "$mv_k" ] || ! grep -qE "gov:kit kickoff-manifest@$mv_k([^0-9.]|\$)" skills/session-kickoff/manifest-check.sh; then
  echo "kit-versions: manifest-check.sh gov:kit kickoff-manifest@ marker != KIT_MANIFEST_VERSION (${mv_k:-unreadable})"
  fails=$((fails+1))
fi

# agent-cap: constant and marker sit on ONE line, which is why this pair was presence-checked only —
# and a half-bumped pair therefore passed. Assert they agree like every other pair; "same line" is
# not "same value", and the marker is what a deployer greps in an adopting tree.
ac=$(grep -oE "KIT_AGENT_CAP_VERSION = '$V'" ${HK_DIR}/agent-cap.js | head -1 | grep -oE "$V")
if [ -z "$ac" ]; then
  echo "kit-versions: KIT_AGENT_CAP_VERSION is unreadable in ${HK_DIR}/agent-cap.js"
  fails=$((fails+1))
else
  # The population is DERIVED, and naming one file is exactly how a half-bumped pair passed here for
  # the THIRD time. `TOOL-dTieredTribunal-14` took the kit to 1.8 in both agent-cap copies and left
  # both scratch-guard copies at 1.7; this block greped agent-cap.js alone and exited 0 over one kit
  # advertising two versions. The population is every tracked `*.js` and NOT every tracked file:
  # that pathspec is load-bearing rather than decorative, because this checker's own source carries
  # the marker string in the grep below and a tree-wide sweep would grade the checker by its own
  # predicate. A carrier introduced in another language would go unseen, which is the honest limit.
  # Asserting a marker EXISTS somewhere is not asserting the carriers
  # agree. Every tracked carrier of the marker is compared to the constant now.
  accarriers=$(git grep -lE "gov:kit agent-cap@" -- '*.js' | sort)
  if [ -z "$accarriers" ]; then
    echo "kit-versions: no tracked file carries a gov:kit agent-cap@ marker — the probe cannot move, which is not a pass"
    fails=$((fails+1))
  fi
  for acf in $accarriers; do
    if ! grep -qE "gov:kit agent-cap@$ac([^0-9.]|\$)" "$acf"; then
      echo "kit-versions: $acf carries a gov:kit agent-cap@ marker that is not $ac (KIT_AGENT_CAP_VERSION)"
      fails=$((fails+1))
    fi
  done
fi
need "KIT_SETTINGS_MERGE_VERSION" ${K}settings-merge.py                   "KIT_SETTINGS_MERGE_VERSION = \"$V\""
need "KIT_RUN_GATES_VERSION"      ${RG_DIR}/run-gates.sh              "^KIT_RUN_GATES_VERSION=$V([[:space:]]|\$)"

# run-gates: the constant in the runner, the marker on that same line, and the marker in the kit
# README a deployer greps. Asserted EQUAL rather than merely present, because this file has twice
# recorded a half-bumped pair passing a presence-only check (agent-cap, settings-merge).
rg=$(grep -oE "^KIT_RUN_GATES_VERSION=$V([[:space:]]|$)" ${RG_DIR}/run-gates.sh | head -1 | grep -oE "$V")
if [ -z "$rg" ]; then
  echo "kit-versions: KIT_RUN_GATES_VERSION is unreadable in ${RG_DIR}/run-gates.sh"
  fails=$((fails+1))
else
  grep -qE "gov:kit run-gates@$rg([^0-9.]|\$)" ${RG_DIR}/run-gates.sh     || { echo "kit-versions: run-gates.sh gov:kit marker != KIT_RUN_GATES_VERSION ($rg)"; fails=$((fails+1)); }
  grep -qE "gov:kit run-gates@$rg([^0-9.]|\$)" ${RG_DIR}/README.md     || { echo "kit-versions: ${RG_DIR}/README.md gov:kit marker != KIT_RUN_GATES_VERSION ($rg) — the README is where a deployer reads a kit's version in an adopting tree"; fails=$((fails+1)); }
fi

# settings-merge: constant plus the marker in its own module docstring, which is where a deployer
# reads the version of a single-file kit. Presence-only left a half-bumped pair passing, same as
# agent-cap's.
sm=$(grep -oE "^KIT_SETTINGS_MERGE_VERSION = \"$V\"" ${K}settings-merge.py | head -1 | grep -oE "$V")
if [ -z "$sm" ] || [ "$(grep -cE "gov:kit settings-merge@$sm([^0-9.]|\$)" ${K}settings-merge.py)" -lt 2 ]; then
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
c=$(grep -oE "^KIT_MEMORY_TREE_VERSION=$V" ${MT_DIR}/check-memory-hygiene.sh | head -1 | cut -d= -f2)
if [ -z "$c" ]; then
  echo "kit-versions: KIT_MEMORY_TREE_VERSION is unreadable, so no marker can be compared against it"
  fails=$((fails+1))
else
  mt_templates=$(git ls-files "${MT_DIR}/*.template.md" 2>/dev/null)
  if [ -z "$mt_templates" ]; then
    # An empty population would make every assertion below vacuously true, which is the failure this
    # repo names `vacuous-selector-empty-population`. It is a refusal, not a pass.
    echo "kit-versions: no tracked ${MT_DIR}/*.template.md — the marker assertion would be vacuous"
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
uc=$(grep -oE "^KIT_UNATTENDED_VERSION=$V" ${UN_DIR}/unattended.sh | head -1 | cut -d= -f2)
if [ -z "$uc" ]; then
  echo "kit-versions: KIT_UNATTENDED_VERSION is unreadable in unattended.sh, so no marker can be compared against it"
  fails=$((fails+1))
else
  for s in ${UN_DIR}/unattended.sh ${UN_DIR}/check-unattended.sh ${UN_DIR}/check-pass-order.sh ${UN_DIR}/check-brief-recorded.sh; do
    if ! grep -qE "^KIT_UNATTENDED_VERSION=$uc([^0-9.]|\$)" "$s"; then
      echo "kit-versions: $s KIT_UNATTENDED_VERSION != $uc — the driver and its leg disagree about which kit this is"
      fails=$((fails+1))
    fi
    if ! grep -qE "gov:kit unattended@$uc([^0-9.]|\$)" "$s"; then
      echo "kit-versions: $s carries a same-line gov:kit unattended@ marker that disagrees with $uc — same line is not same value"
      fails=$((fails+1))
    fi
  done
  un_templates=$(git ls-files "${UN_DIR}/*.template.md" 2>/dev/null)
  if [ -z "$un_templates" ]; then
    echo "kit-versions: no tracked ${UN_DIR}/*.template.md — the marker assertion would be vacuous"
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

need "KIT_UNATTENDED_VERSION"     ${UN_DIR}/unattended.sh            "^KIT_UNATTENDED_VERSION=$V([[:space:]]|\$)"
# The driver/leg constant pairing that used to sit here is SUBSUMED by the unattended block below,
# which derives the same $uc from the same file and asserts the same regex against the same second
# file — one defect, two messages, two increments, and two copies to keep in step. Deleted rather
# than kept as a second opinion, because a re-implementation of an assertion is not one.
need "KIT_MEMORY_RECALL_VERSION"  ${MR_DIR}/recall_conf.py         "^KIT_MEMORY_RECALL_VERSION = \"$V\""

# memory-recall: constant in recall_conf.py, marker in the README the adopter keeps. Same pair
# assertion as memory-tree — a stale marker makes the deployer read the wrong installed version.
r=$(grep -oE "^KIT_MEMORY_RECALL_VERSION = \"$V\"" ${MR_DIR}/recall_conf.py | head -1 | grep -oE "$V")
if [ -z "$r" ] || ! grep -qE "gov:kit memory-recall@$r([^0-9.]|\$)" ${MR_DIR}/README.md; then
  echo "kit-versions: memory-recall README marker != KIT_MEMORY_RECALL_VERSION (${r:-unreadable})"
  fails=$((fails+1))
fi

need "KIT_DRIFT_AUDIT_VERSION"    ${DA_DIR}/drift_report.py          "^KIT_DRIFT_AUDIT_VERSION = \"$V\""

# drift-audit: constant in drift_report.py, marker in the README the adopter keeps. Same pair
# assertion as memory-tree/memory-recall — a stale marker makes the deployer read the wrong version.
da=$(grep -oE "^KIT_DRIFT_AUDIT_VERSION = \"$V\"" ${DA_DIR}/drift_report.py | head -1 | grep -oE "$V")
if [ -z "$da" ] || ! grep -qE "gov:kit drift-audit@$da([^0-9.]|\$)" ${DA_DIR}/README.md; then
  echo "kit-versions: drift-audit README marker != KIT_DRIFT_AUDIT_VERSION (${da:-unreadable})"
  fails=$((fails+1))
fi

need "drift-audit-code meta.version"  ${WF_DIR}/drift-audit-code.js  "version: '$V'"
need "drift-audit-state meta.version" ${WF_DIR}/drift-audit-state.js "version: '$V'"

# ...and each harness's meta.version agrees with the kit constant AND with its own gov:kit marker.
# The harnesses ship the kit's `args` contract, so a contract narrowing that moves the engine version
# and leaves a harness at the old one tells an adopter the wrong thing about the file they actually run.
for h in code state; do
  hv=$(grep -oE "version: '$V'" "${WF_DIR}/drift-audit-$h.js" | head -1 | grep -oE "$V")
  if [ -z "$hv" ] || [ "$hv" != "$da" ]; then
    echo "kit-versions: drift-audit-$h.js meta.version (${hv:-unreadable}) != KIT_DRIFT_AUDIT_VERSION (${da:-unreadable})"
    fails=$((fails+1))
  elif ! grep -qE "gov:kit drift-audit@$hv([^0-9.]|\$)" "${WF_DIR}/drift-audit-$h.js"; then
    echo "kit-versions: drift-audit-$h.js gov:kit marker != its own meta.version ($hv)"
    fails=$((fails+1))
  fi
done

need "KIT_PYTEST_GUARDRAILS_VERSION" ${PG_DIR}/crashprobe.py "^KIT_PYTEST_GUARDRAILS_VERSION = \"$V\""
need "KIT_GOVKIT_VERSION"          ${GK_DIR}/govkit.py                    "^KIT_GOVKIT_VERSION = \"$V\""
# The kit dir, bound ONCE for the same reason `T2R` above is: a literal per use is a regression an
# adopter pays for, and the carried-prefix ban counts every one of them.
LXD="$LX_DIR"
need "KIT_LEXICON_VERSION"         "$LXD/lexicon.py"                         "^KIT_LEXICON_VERSION = \"$V\""

# lexicon: the constant was PRESENCE-checked alone, which is how a bump to 1.2 shipped with all four
# `gov:kit lexicon@` markers left at 1.1 and only `govkit selfcheck` — at the push boundary — noticing.
# Two checkers, one question, and the weaker one is the one a session reaches for. Paired here in the
# shape the guardrails block below already uses, so the cheap branch-local run reds on this class.
# The Skill is deliberately absent from the list: it is RENDERED from the constant and cannot drift.
# TOOL-aSurfacedLexicon-10, round-2 review F1.
lx=$(grep -oE "^KIT_LEXICON_VERSION = \"$V\"" "$LXD/lexicon.py" | head -1 | grep -oE "$V")
for kept in lexicon.py canon.py README.md LEXICON.md; do
  if [ -z "$lx" ] || ! grep -qE "gov:kit lexicon@$lx([^0-9.]|\$)" "$LXD/$kept"; then
    echo "kit-versions: lexicon gov:kit marker in $kept != the constant (${lx:-unreadable})"
    fails=$((fails+1))
  fi
done

# pytest-parallel-guardrails: the constant lives in crashprobe.py, but the probe is a
# hunt-then-remove diagnostic — the DEPLOYER-side version signal is the gov:kit marker in each
# artifact adopters KEEP. Assert the constant and every marker agree (memory-tree-pair style).
g=$(tr -d '\r' < ${PG_DIR}/crashprobe.py | grep -oE "^KIT_PYTEST_GUARDRAILS_VERSION = \"$V\"" | head -1 | grep -oE "$V")
for kept in README.md pyproject-snippet.toml aiosqlite-seam-conftest.py aiosqlite_worker_resilience.test-template.py; do
  if [ -z "$g" ] || ! grep -qE "gov:kit pytest-parallel-guardrails@$g([^0-9.]|\$)" "${PG_DIR}/$kept"; then
    echo "kit-versions: pytest-parallel-guardrails marker in $kept != constant (${g:-unreadable})"
    fails=$((fails+1))
  fi
done

[ "$fails" = 0 ] && { echo "kit-versions: clean — $checked declared carrier(s) under ${K:-the repo root}"; exit 0; }
echo "kit-versions: $fails problem(s)"
exit 1
