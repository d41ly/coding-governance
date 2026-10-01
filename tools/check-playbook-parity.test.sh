#!/usr/bin/env bash
# check-playbook-parity.test.sh — self-test for <prefix>/check-playbook-parity.sh.
#
#   bash <prefix>/check-playbook-parity.test.sh
#
# Exit 0 = every arm held · 1 = an arm failed · 2 = the harness could not set up.
#
# WHY EACH ARM IS A RED PROOF. The gate under test exists to catch coverage checks that pass by
# checking nothing, so a harness that only ever watched it pass would be the very defect it gates.
# `coding-governance-agents.template.md` §7: "a new gate is not landed until its failing case has
# been observed."
#
# HOW THE ARMS WORK. Every arm builds a scratch WORKTREE-SHAPED fixture — a real git repo with its
# own <prefix>/, charter and runbook — and runs the gate inside it. Nothing here mutates the real tree,
# which matters because the gate derives its kit set from govkit's registry and `git ls-files`
# (TOOL-aRepatriatedFork-54), so every fixture carries its own registry, and would otherwise see
# this repo's own population.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
# >>> derive_self_rel — canonical copy: kit-rel.sh in gov's lib dir (byte-identical; gated)
derive_self_rel() {
  local _dsr_p _dsr_rel=""
  _dsr_p=$(cd "$1" 2>/dev/null && pwd) || return 1
  while [ ! -e "$_dsr_p/.git" ]; do
    [ "$(dirname "$_dsr_p")" = "$_dsr_p" ] && return 1
    _dsr_rel="$(basename "$_dsr_p")${_dsr_rel:+/$_dsr_rel}"
    _dsr_p=$(dirname "$_dsr_p")
  done
  printf '%s\n' "$_dsr_rel"
}
# <<< derive_self_rel
KIT_REL=$(derive_self_rel "$HERE") || { echo "check-playbook-parity.test: not inside a git repository"; exit 2; }
# PFX is the install prefix WITH its trailing slash, derived from where this file sits and empty
# at a root install: every fixture and host path below is spelled through it, never through a
# literal prefix (TOOL-aRepatriatedFork-28).
PFX="${KIT_REL:+$KIT_REL/}"
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
GATE_SRC="$ROOT/${PFX}check-playbook-parity.sh"
# TOOL-aRepatriatedFork-46: a kit is named by the name its directory has in THIS install, never
# as a literal segment: this suite's own from where it sits, a sibling's through the resolver,
# which reads the install receipt first. A fixture mirrors that layout by the resolved NAME.
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
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
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
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
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
_rkd_py=$(resolve_python) || { echo "check-playbook-parity.test: no usable python, so the sibling kits cannot be resolved"; exit 2; }
HOOKS_DIR=$(resolve_kit_dir "$_rkd_py" hooks agent-cap.js "$HERE") || exit 2
HOOKS="${HOOKS_DIR##*/}"
MT_KIT_DIR=$(resolve_kit_dir "$_rkd_py" memory-tree check-memory-hygiene.sh "$HERE") || exit 2
MT_KIT="${MT_KIT_DIR##*/}"
# TOOL-aRepatriatedFork-54: the gate reads its kit population from govkit's registry, so every
# fixture carries one and DECLARES the kits it plants; an undeclared directory is not a kit.
GK_DIR=$(resolve_kit_dir "$_rkd_py" govkit registry.toml "$HERE") || exit 2
GK="${GK_DIR##*/}"
# FX is the prefix the NEXT fixture is built at: this suite's own by default, and empty for the
# root-install arms, which every install owes whatever prefix this suite itself sits at.
FX=$PFX
fails=0
TMP=$(mktemp -d) || exit 2
trap 'rm -rf "$TMP"' EXIT

say_ok()   { printf 'arm ok    %s\n' "$1"; }
say_fail() { fails=$((fails+1)); printf 'arm FAIL  %s — %s\n' "$1" "$2"; }

# fixture <dir> — a minimal but VALID tree the gate passes on, so each arm breaks exactly one thing.
fixture() {
  local d=$1
  mkdir -p "$d/${FX}${MT_KIT}" "$d/${FX}${HOOKS}" "$d/${FX}lib" "$d/${FX}${GK}" "$d/.claude"
  git -C "$d" init -q 2>/dev/null
  git -C "$d" config user.email t@t; git -C "$d" config user.name t
  cp "$GATE_SRC" "$d/${FX}check-playbook-parity.sh"
  : > "$d/${FX}${MT_KIT}/engine.sh"
  printf 'const CAP = 5\nconst MAX_VERIFIERS = 5\nconst MAX_LENSES = 5\n' > "$d/${FX}${HOOKS}/agent-cap.js"
  # The registry declares the two kits this fixture plants. `lib` is declared and holds no tracked
  # file, so it is no kit; the registry's own directory is declared nowhere, so it is none either.
  printf '[[entry]]\nid = "memory-tree"\ndescriptor = "{prefix}/%s/kit.toml"\n\n[[entry]]\nid = "agent-cap"\ndescriptor = "{prefix}/%s/kit.toml"\n\n[[exempt]]\npath = "{prefix}/lib"\nwhy = "gov-internal"\n' \
    "$MT_KIT" "$HOOKS" > "$d/${FX}${GK}/registry.toml"
  printf '{ "hooks": { "PreToolUse": [ { "matcher": "Workflow|Agent" } ] } }\n' > "$d/.claude/settings.json"
  # The trio. hooks is waived; memory-tree is documented, and it is documented in the RUNBOOK.
  #
  # TWO haystack files since v3.0, and this fixture carried only one — every arm below exited 2 on
  # the gate's own two-file precondition, control included, so thirteen red proofs were proving
  # nothing but a missing file. The kit line sits in the runbook rather than the template ON PURPOSE:
  # written into the template, an empty WIRE-INTO-PROJECT.md would satisfy the precondition while no
  # arm depended on a byte of it, and a haystack half nothing reads is the green-by-absence shape
  # this gate exists to refuse. Here, emptying the runbook reds `memory-tree` as undocumented.
  #
  # Every declared pair's STATED side must appear here, or its anti-vacuity arm reds on the valid-
  # fixture control -- which is exactly what that arm is for. Three pairs were added when the
  # playbook moved under this gate's protection and out of check-agent-cap-restatement.sh's
  # population; the control failed, correctly, until the fixture carried their sentences.
  printf 'template {{ALPHA}} {{MEMORY_ROOT}}\nan array LITERAL of <=5 elements passes\nthe hook (matcher `Workflow|Agent`) denies\nat most 5 verify agents TOTAL (batch grows)\nroute through boundedParallel(thunks, 5) always\ndenies any K it cannot resolve to an integer <=5 here\n' \
    | sed 's/<=/≤/' > "$d/coding-governance-agents.template.md"
  # A root install has no root head to name a kit by, so its runbook names it the way gov's does,
  # through the `<prefix>/` token (VERIFYING repair: a bare `memory-tree/` documents nothing).
  printf 'runbook {{MEMORY_ROOT}}\nadopt '"${FX:-<prefix>/}${MT_KIT}/"' into the target repo\n' > "$d/WIRE-INTO-PROJECT.md"
  printf '# waivers\nhooks   not adopter-facing as a kit.\n' > "$d/${FX}playbook-kit-waivers.txt"
  # The stamp-rule pair (TOOL-aHonedRuleset-5) is the one row whose two homes both sit OUTSIDE
  # <prefix>/: the manifest template states the expression and manifest-check.sh owns it. The control
  # redded on a missing owning source from the day that row landed, because this fixture built no
  # skills/ tree at all.
  mkdir -p "$d/skills/session-kickoff"
  printf -- '- Stamp rule: sha = `HEAD` on any branch; the datetime always advances.\n' > "$d/skills/session-kickoff/MANIFEST-TEMPLATE.md"
  printf 'STAMP_SHA_RULE="sha = HEAD on any branch"\n' > "$d/skills/session-kickoff/manifest-check.sh"
  git -C "$d" add -A >/dev/null 2>&1
  git -C "$d" commit -qm f >/dev/null 2>&1
}

# add_kit <prefix> <kit> — a tracked kit directory the fixture's registry DECLARES. A kit planted
# without its registry row is no kit to the gate, so an arm doing that would pass for the wrong reason.
add_kit() {
  mkdir -p "$1$2" && : > "$1$2/x.sh" &&
    printf '\n[[entry]]\nid = "%s"\ndescriptor = "{prefix}/%s/kit.toml"\n' "$2" "$2" >> "$1${GK}/registry.toml"
}
add_substring_kit() { add_kit "$1" ape && printf 'the shape of a landscape\n' >> coding-governance-agents.template.md; }

# arm <label> <expect: ok|red|refuse> <expected-substring-when-red> <mutator…>
# `refuse` is a red that must ALSO exit 2: the gate could not run, which is not a finding.
arm() {
  local label=$1 expect=$2 want=$3; shift 3
  local d="$TMP/$(printf '%s' "$label" | tr -c 'a-zA-Z0-9' '_')"
  fixture "$d"
  ( cd "$d" && "$@" >/dev/null 2>&1 )
  git -C "$d" add -A >/dev/null 2>&1
  local out rc
  out=$(cd "$d" && bash ${FX}check-playbook-parity.sh 2>&1); rc=$?
  if [ "$expect" = ok ]; then
    if [ "$rc" -eq 0 ]; then say_ok "$label"
    else say_fail "$label" "expected the gate to PASS, it exited $rc"; printf '%s\n' "$out" | sed 's/^/      /'; fi
    return
  fi
  if [ "$rc" -eq 0 ]; then
    say_fail "$label" "expected the gate to RED, it exited 0 — the mutation was not caught"
    printf '%s\n' "$out" | sed 's/^/      /'; return
  fi
  if [ "$expect" = refuse ] && [ "$rc" -ne 2 ]; then
    say_fail "$label" "expected the gate to REFUSE with exit 2, it exited $rc"
    printf '%s\n' "$out" | sed 's/^/      /'; return
  fi
  case "$out" in
    *"$want"*) say_ok "$label" ;;
    *) say_fail "$label" "reds, but not naming: $want"; printf '%s\n' "$out" | sed 's/^/      /' ;;
  esac
}

# --- the control. Without it, every red proof below could be redding for an unrelated reason. -----
arm "control · a valid fixture passes" ok "" true
# FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]; then echo "foreign-prefix-probe: stopped after 1 arm"; [ "${fails:-0}" = 0 ] && echo "PASS (${probe_n:-1} assertions)" || echo "FAIL (${probe_n:-1} assertions)"; [ "${fails:-0}" = 0 ] && exit 0; exit 1; fi

# --- the anchored matcher itself ---------------------------------------------------------------
# The gate's header calls a bare substring match "the vacuous-selector shape this gate exists to
# prevent, committed by the gate itself" — and nothing pinned it: loosening `named_in_playbook`
# to `grep -qF` left every other arm green. This fixture names a kit ONLY as a substring inside an
# unrelated word, so a loosened matcher certifies it documented and the arm goes red.
arm "S1 a kit named only as a substring is NOT documented" red \
  "a kit ships and the playbook never names it, with no waiver row to excuse it: ape" \
  add_substring_kit "$PFX"

# --- AC1 · a kit named nowhere and waived nowhere --------------------------------------------------
arm "AC1 an undocumented kit reds by name" red \
  "a kit ships and the playbook never names it, with no waiver row to excuse it: orphankit" \
  add_kit "$PFX" orphankit

# --- TOOL-aRepatriatedFork-54 · the population is the registry's, at this prefix and at the root --------
# Each root arm builds its fixture at the repository root whatever prefix this suite sits at. The
# first is the red-first control of the unit: the listing gate reds on it naming `.claude`.
REGISTRY_REFUSAL="cannot read the kit population from govkit's registry.toml"
arm "AC3 an unresolvable registry REFUSES rather than reading as an empty population" refuse \
  "$REGISTRY_REFUSAL" sh -c 'rm -f '"${PFX}${GK}/registry.toml"''
FX=""
arm "AC2 at a root install .claude/, skills/ and an undeclared dir are not kits" ok "" \
  sh -c 'mkdir -p stray && : > stray/x.sh'
arm "AC3 at a root install an unresolvable registry REFUSES" refuse \
  "$REGISTRY_REFUSAL" sh -c 'rm -f '"${GK}/registry.toml"''
arm "AC3 at a root install a declared kit the playbook never names reds by name" red \
  "a kit ships and the playbook never names it, with no waiver row to excuse it: orphankit" \
  add_kit "" orphankit
FX=$PFX

# --- AC2 · the unit's central proof: a stated value drifting from the source that owns it ----------
arm "AC2 MAX_LENSES drifts from the template's stated bound" red \
  "a declared value pair disagrees with the source that owns it. Pair lens-array bound" \
  sh -c 'printf "const MAX_LENSES = 6\n" > '"${PFX}${HOOKS}/agent-cap.js"''
arm "AC2b the hook matcher drifts from .claude/settings.json" red \
  "a declared value pair disagrees with the source that owns it. Pair agent-cap hook matcher" \
  sh -c 'printf "{ \"hooks\": { \"PreToolUse\": [ { \"matcher\": \"Workflow\" } ] } }\n" > .claude/settings.json'

# --- AC3 · a placeholder added and the catalogue counts not updated ---------------------------------

# --- AC4 · an extraction that matches nothing must never compare empty to empty ----------------------
arm "AC4 an unresolvable pair reds rather than passing" red \
  "an extraction matched NOTHING, so the pair was never compared" \
  sh -c 'sed -i "s/an array LITERAL of ≤5 elements passes//" coding-governance-agents.template.md'

# --- AC5 · the derivation broken to lose its sentinel -------------------------------------------------
arm "AC5 a derivation missing its sentinel reds" red \
  "the kit derivation lost its frozen sentinel member, so the derivation is broken rather than the tree being empty: expected to find " \
  sh -c 'git rm -q -r --cached '"${PFX}${MT_KIT}"' >/dev/null 2>&1; rm -rf '"${PFX}${MT_KIT}"''

# --- AC6 · both waiver-drain arms ----------------------------------------------------------------------
arm "AC6a a waiver for a kit that is gone reds as stale" red \
  "a waiver row names a kit that no longer exists, so the row excuses nothing and is stale" \
  sh -c 'printf "ghostkit  gone\n" >> '"${PFX}playbook-kit-waivers.txt"''
arm "AC6b a waiver for a kit the playbook DOES name reds" red \
  "a waiver row names a kit the playbook DOES document, so the row excuses nothing" \
  sh -c 'printf "memory-tree  redundant\n" >> '"${PFX}playbook-kit-waivers.txt"''

# --- AC9 · the registry absent: red and STOP, never create one -------------------------------------------
arm "AC9 an absent waiver registry reds and stops" red \
  "the kit waiver registry is absent and this gate never creates it: expected " \
  sh -c 'git rm -q --cached '"${PFX}playbook-kit-waivers.txt"' >/dev/null 2>&1; rm -f '"${PFX}playbook-kit-waivers.txt"''

# --- the two S2-stage integrity guards ----------------------------------------------------------
# Both mutate the fixture's OWN copy of the gate, which is what a red proof of THIS kind of guard
# looks like: the guard exists to notice that the stage did not run, so the fixture has to be a
# stage that did not run.
arm "S2 an uncreatable results file reds instead of reporting agreement" red \
  "the value-parity stage could not create its results file, so no pair was compared and this gate must not report agreement" \
  sh -c 'sed -i "s|^PPTMP=.*|PPTMP=/nonexistent-dir-for-the-arm/pp|" '"${PFX}check-playbook-parity.sh"''
arm "S2 a lost results file reds rather than reading as no-disagreement" red \
  "the value-parity stage produced no completion sentinel, so its results were lost rather than empty and no pair was actually compared" \
  sh -c "sed -i \"/^printf 'PAIRSTAGE-RAN/d\" ${PFX}check-playbook-parity.sh"

# --- the structural intersection check must not pass vacuously ---------------------------------------------

# --- the remaining five branches, armed rather than pinned as exceptions -------------------------
# check-arms refuses an unarmed branch that is not written into memory/project/unarmed-branches.txt,

# check 1 · the kit derivation returns an EMPTY set. Distinct from AC5, where the set is non-empty
# and merely lost its sentinel: here coverage would be vacuously true over nothing at all.
arm "S1 an empty kit derivation reds before reporting coverage" red \
  "the kit derivation returned an empty set, so coverage would pass by checking nothing" \
  sh -c 'git rm -q -r --cached '"${PFX%/}"' >/dev/null 2>&1; rm -rf '"${PFX}${MT_KIT}"' '"${PFX}${HOOKS}"' '"${PFX}lib"''

# check 8 · a stated count that cannot be extracted at all. Without this the arithmetic block would
# compare three empty strings and report ok — the same vacuity the pair loop guards against.

# check 13 · the catalogue NAMES a shared placeholder that is not the measured intersection. The
# structural half of S3: check 12 catches naming none, this catches naming the wrong one.

if [ "$fails" -ne 0 ]; then
  printf 'check-playbook-parity.test.sh FAILED — %d arm(s)\n' "$fails"
  exit 1
fi
printf 'PASS — check-playbook-parity.test.sh: every arm held\n'
