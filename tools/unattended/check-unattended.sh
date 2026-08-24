#!/usr/bin/env bash
# check-unattended.sh - the merge-bar leg for the unattended-run kit. The check COUNT is written in no
# prose here, because it has now been wrong twice and a cross-build merge left this header stating two
# different totals at once. Derive it with
# `grep -oE 'fail [0-9]+' tools/unattended/check-unattended.sh | grep -oE '[0-9]+' | sort -un` -
# the second grep is load-bearing: `sort -un` on `fail 7` sorts the WORD, reads every line as 0, and
# prints exactly one.
# Contract: memory/guides/UNATTENDED-PROTOCOL.md (binding). Project layer: .unattended.conf.
#
#   bash tools/unattended/check-unattended.sh
#
# Exit 0 + no output = clean. Anything printed is a violation. Exit 2 = misconfigured.
#
# ONE EXCEPTION, and it is named rather than quietly taken: a check that cannot COMPARE announces
# the case it could not reach, on the REPORT channel, which the default run does not print. Set
# GOV_UNATTENDED_REPORT=1 to see them. A skip that looks like a pass is indistinguishable from
# coverage, and a skip printed by default would falsify the contract line above — so the line keeps
# its meaning and the announcement gets a channel of its own. TOOL-dUnstalledConvoy-6.
#
# READ-ONLY, which is what lets it run on the bar. It writes nothing, renders nothing and derives
# nothing: the run-state file's generated region is asserted EMPTY, because the unit list is derived
# from the build README at read time and lives in no second place. The README's own freshness is the
# memory-tree gate's check 9. Two legs answering one question is the class the file under test exists
# to remove — and a copy that has to be refreshed is that class wearing a different hat.
#
# THE CORE SETS ARE READ FROM THE DRIVER, never restated here. A second spelling of `PHASES_CORE` one
# file away from the thing that enforces it is the drift this leg exists to catch.
set -u
KIT_UNATTENDED_VERSION=1.8   # gov:kit unattended@1.8 — must match unattended.sh; check-kit-versions.sh pairs them

# ------------------------------------------------------------------------------ the dereference pin
# Identical to the driver's, and for the identical reason: `git replace` rewrites what a sha MEANS for
# every read, and a graft file rewrites the commit GRAPH, so check 13 could compare against the honest
# anchor and still read forged bytes. Both MEASURED with live controls, and the two suppressions are
# NOT interchangeable - only GIT_GRAFT_FILE stops the graft.
#
# The driver additionally refuses a run whose ENVIRONMENT supplies git config. This leg deliberately
# does NOT. It runs on the bar, the bar runs under the pre-push hook, and which GIT_* variables git
# exports to a hook varies by git version - measured unset for pre-push on this node, but a leg that
# reds on another node's git is a false positive on the merge bar. The levers that matter are pinned
# below rather than detected.
export GIT_GRAFT_FILE=/dev/null
# THE KIT LIBRARY, sourced before anything reads history. It holds every predicate this script and
# the gate leg must answer identically — `GIT`, the anchored id tests, path containment, and "has
# this pass committed yet". Sourced by absolute path derived from THIS file's location, because the
# `cd` to the repo root happens below and a relative source would resolve against the caller's cwd.
_LIB_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
[ -f "$_LIB_DIR/lib-unattended.sh" ] || {
  echo "unattended-check: the kit library is missing beside this script, so the predicates it shares with its own gate leg are unavailable and no answer here would be trustworthy: $_LIB_DIR/lib-unattended.sh" >&2
  exit 2
}
# shellcheck source=lib-unattended.sh
. "$_LIB_DIR/lib-unattended.sh"

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "unattended-check: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
HERE="$(cd "$(dirname "$0")" && pwd)"
DRIVER="$HERE/unattended.sh"
CONF="$ROOT/.unattended.conf"

# ---- SCOPE, so a caller can pay for the question it is asking. This leg is ~23 s and check 28 is
# ---- half of that, measured on node d 2026-08-23: 22.7 s whole, 11.7 s with the 28 region cut off.
# ---- The self-test stages a break and re-runs this script ONCE PER ARM - eighty times - and most
# ---- of those arms are asking about one check while paying for twenty-eight.
# ----
# ---- TWO DIRECTIONS, because the arms need both: `--only 28` runs the shared setup and the 28
# ---- region alone, `--skip 28` runs everything else. Anything else is REFUSED rather than
# ---- silently ignored - a scope argument nobody honours is a caller who thinks they scoped.
# ----
# ---- WHAT THIS DOES NOT DO: scope to an arbitrary check. The checks between 1 and 27 share state
# ---- freely - a later one reads a count an earlier one computed - so they are one unit until that
# ---- is untangled, and pretending otherwise would hand back wrong verdicts rather than slow ones.
SCOPE=""
case "${1:-}" in
  "")            ;;
  --only)        [ "${2:-}" = 28 ] || { echo "check-unattended: --only takes 28 and nothing else; checks 1-27 share state and are one unit"; exit 2; }; SCOPE=only28 ;;
  --skip)        [ "${2:-}" = 28 ] || { echo "check-unattended: --skip takes 28 and nothing else; checks 1-27 share state and are one unit"; exit 2; }; SCOPE=skip28 ;;
  *)             echo "check-unattended: unknown argument '${1}'; this leg takes [--only 28] or [--skip 28]"; exit 2 ;;
esac

status=0
fail() { echo "UNATTENDED check $1 FAILED — $2"; status=1; }

# DEFINED HERE, ABOVE ITS FIRST CALLER, and that placement is the whole point. It used to sit 200
# lines below the review-loop check that calls it, so at call time it was not a function yet: bash
# reported command-not-found, `2>/dev/null` hid the message, and `|| true` turned the failure into an
# empty result. The clause then compared an empty id set against the BASE roster, found no new ids,
# and reported that nothing had been promoted - dead while it was silent, and a FALSE RED the moment
# a run finally exited non-convergent. Fifth silent-skip mechanism found in this one check.
# >>> kickoff_region
region()   { awk -v o="$2" -v c="$3" '
               { ln=$0; sub(/\r$/,"",ln) }
               index(ln,o)==1 { if (ln!=o) bad=1; no++; if (no==1) oat=NR; if (nc==0) inside=1; next }
               index(ln,c)==1 { if (ln!=c) bad=1; nc++; if (nc==1) cat=NR; inside=0; next }
               inside { print }
               END { if (bad || no!=1 || nc!=1 || cat<oat) exit 3 }' "$1"; }
# <<< kickoff_region

if [ "$SCOPE" != only28 ]; then
# ---------------------------------------------------------------------------------- 1: the conf
if [ ! -f "$CONF" ]; then
  fail 1 "no .unattended.conf at the repo root, and every value this leg checks is declared there"
  exit "$status"
fi
ADV_NAME=""
MEMORY_ROOT=memory; LANDER=""; BYPASS_BAN=""; GATE_CMD=""; WIRING_CHECK=""
KEEPALIVE_CREATE=""; KEEPALIVE_DELETE=""; PHASES_EXTRA=""; DOD_EXTRA=""; CORE_FLOOR=""; LANDED_ANCHOR_CUTOFF=""
KICKOFF_ENGINE=""; KICKOFF_EXITS=""; DIRECTIVES_EXTRA=""; DIRECTIVES_FLOOR=""; DIRECTIVES_EXTRA_TABLE=""
HALT_CODES_EXTRA=""; HALT_FLOOR=""
# ---- THE CONF IS IMPORTED, NEVER SOURCED INTO THIS SHELL. Two rounds got this wrong in two ways,
# ---- and the second is why the guard is now structural rather than a probe.
# ----
# ---- Round 8: `. "$CONF"` in the main shell meant one appended `exit 0` in a tracked file - a file
# ---- the graded run can commit itself - ended the leg at status 0, which `run-gates` reads as
# ---- GATE ok. A sentinel probe was added for it.
# ----
# ---- Round 9: the probe stopped the conf ENDING the leg and not HIJACKING it, because the real
# ---- source still ran here, below `status=0` and below `fail()`. `trap 'exit 0' EXIT` satisfies the
# ---- probe - the trap fires only when the probe subshell exits, AFTER its sentinel is written - and
# ---- then fires again on this script's own `exit "$status"`: rc 0 with the FAILED line still
# ---- printed. An appended no-op `fail()` is worse: it replaces the verdict recorder itself, rc 0
# ---- with zero bytes of output, byte-indistinguishable from a clean tree.
# ----
# ---- So nothing from that file executes in this shell at all. It is sourced inside a subshell, and
# ---- the DECLARED KEYS come back as a NUL-delimited name/value stream terminated by a sentinel. A
# ---- trap, a redefined function, an `exit`, a `set -x` - none of it crosses the boundary; the worst
# ---- a hostile conf can now do is fail to deliver the sentinel, which is a refusal.
# ----
# ---- THE NAMES ARE READ AS TEXT AND VALIDATED, never taken from the file's own output: only
# ---- `[A-Z][A-Z0-9_]*` is assignable, so the stream cannot introduce a name this leg does not expect.
# ---- A key the file spells in some other shape keeps the default initialised above, which is exactly
# ---- what a `sed`-based reader would have done with it.
_conf_names=$(sed -n 's/^[[:space:]]*\(export[[:space:]][[:space:]]*\)\{0,1\}\([A-Z][A-Z0-9_]*\)=.*/\2/p' "$CONF" | sort -u)
_conf_ok=0
while IFS= read -r -d '' _ck; do
  IFS= read -r -d '' _cv || break
  case "$_ck" in
    __CONF_IMPORT_OK__) _conf_ok=1 ;;
    [A-Z][A-Z0-9_]*) eval "$_ck=\$_cv" ;;
  esac
done < <( . "$CONF" >/dev/null 2>&1 || exit 9
          for _n in $_conf_names; do eval "_cval=\${$_n:-}"; printf '%s\0%s\0' "$_n" "$_cval"; done
          printf '__CONF_IMPORT_OK__\0\0' )
# THE SENTINEL IS THE WHOLE VERDICT. `|| exit 9` catches a parse error and a `return 0`, both of which
# abort the file and RETURN rather than ending the subshell - round 9's high 2, where the probe's
# missing `|| exit 9` let a malformed `if` load only the lines above the break and hand back an empty
# `LANDED_ANCHOR_CUTOFF`, which this leg reads as "grandfather every anchor". Its absence catches the
# `exit` and `set -u` shapes, which end the subshell before the sentinel is written.
if [ "$_conf_ok" != 1 ]; then
  fail 1 "the project conf does not source cleanly, so this leg cannot read a single declared value - and sourcing it in this shell would let that file end or take over the leg rather than be graded by it: $CONF"
  exit "$status"
fi
M="$MEMORY_ROOT"
for k in LANDER BYPASS_BAN GATE_CMD WIRING_CHECK KEEPALIVE_CREATE KEEPALIVE_DELETE; do
  eval "v=\${$k}"
  [ -n "$v" ] || fail 1 "a required key is undeclared in .unattended.conf, and an undeclared value is not a defaulted one: $k"
done

# The kit's CORE sets, read from the driver — the single source. Parsed rather than sourced, because
# sourcing a script whose tail runs a verb would run the verb.
# Pure bash for the same reason as the accessors below: this runs three times per leg invocation and
# cost two processes each. Semantics preserved exactly — the line must be `KEY="…"` with only
# whitespace after the closing quote, the first such line wins, and anything else (no quotes, a
# truncated line) yields the empty string, which is the state check 1 refuses by name.
core_of() { # KEY  ->  the quoted value from $DRIVER
  local l p="$1=\"" v
  while IFS= read -r l || [ -n "$l" ]; do
    l=${l%$'\r'}
    while :; do case "$l" in *' '|*$'\t') l=${l%?} ;; *) break ;; esac; done
    case "$l" in
      "$p"*'"') v=${l#"$p"}; printf '%s\n' "${v%\"}"; return 0 ;;
    esac
  done < "$DRIVER"
  return 0
}
PHASES_CORE=$(core_of PHASES_CORE)
DOD_CORE=$(core_of DOD_CORE)
DIRECTIVES_CORE=$(core_of DIRECTIVES_CORE)
PHASES_TERMINAL=$(core_of PHASES_TERMINAL)
# TOOL-aPromptedMandate-2 - the pass-kind subset, read the SAME way as every other core set, so
# the leg never carries a second spelling of a driver declaration.
PHASES_PASSKIND=$(core_of PHASES_PASSKIND)
# the mode set, read through the SAME parse. A second spelling here is
# what this unit exists to remove.
AUTH_MODES=$(core_of AUTH_MODES)
AUTH_SCOPES="all $AUTH_MODES"
if [ -z "$AUTH_MODES" ]; then
  fail 1 "cannot read AUTH_MODES from the driver, so the mode-membership branch and the directive scope join would both pass over an empty set - an empty vocabulary makes every check keyed on it vacuously true: $DRIVER"
fi

# The parked-kind taxonomy. Read here for the same reason the four above are: a set declared in the
# driver and graded nowhere is decoration, and this one has a counter and a Definition-of-Done
# predicate hanging off it.
PARK_KINDS_OWED=$(core_of PARK_KINDS_OWED)
# The review loop's runaway backstop, read the same way. The leg holds NO copy of the number: a
# second spelling of a bound is a bound that goes wrong silently when one copy moves.
RUNAWAY_CEILING=$(core_of RUNAWAY_CEILING)
# The halt vocabulary, read the same way. The leg holds NO member token of its own: a prefix
# alternation could not tell a member from an unrelated identifier, and a sibling unit lands a
# constant whose name such an alternation would have matched.
HALT_CODES_CORE=$(core_of HALT_CODES_CORE)
HALT_CODES="$HALT_CODES_CORE $HALT_CODES_EXTRA"
if [ -z "$PHASES_CORE" ] || [ -z "$DOD_CORE" ]; then
  fail 1 "cannot read the kit's core sets from the driver, so every membership check below would pass over an empty set: $DRIVER"
  exit "$status"
fi
PHASES="$PHASES_CORE $PHASES_EXTRA"
DOD="$DOD_CORE $DOD_EXTRA"

# ---- THE REVIEW LOOP, graded from the parked region. Three clauses, and each exists because the
# ---- corpus cannot exercise it: no group may exceed the runaway ceiling; no group's blocker counts
# ---- may fail to shrink without carrying a TERMINAL LINE recording the exit; and a group that DID
# ---- exit must have been disposed of, observed as a unit row the generated region gained.
# ----
# ---- There is no round-count fact to parse. The sequence is DERIVED from the line set, and the only
# ---- grammar split here is the park helper's own output — which is why adding a round cannot make a
# ---- record disagree with itself.
if [ -z "$RUNAWAY_CEILING" ]; then
  fail 2 "the driver declares no readable RUNAWAY_CEILING, so the review-loop check below would be skipped entirely and its absence would look exactly like a clean corpus"
else
  rv_bad=""
  for rvf in $(GIT ls-files "$M/builds/*/RUN*.md" 2>/dev/null); do
    [ -f "$rvf" ] || continue
    grep -q '^[0-9][0-9-]*T[0-9:]*Z review · item ' "$rvf" 2>/dev/null || continue
    rv_readme=${rvf%/RUN*.md}/README.md
    # THE THIRD CLAUSE GRADES A DELTA, and the first cut did not — which made it the FOURTH silent
    # skip found in this one check. It tested whether the SUBJECT appeared anywhere in the units
    # region; per the spec the subject is the build slug or a spec path, and both are substrings of
    # every generated row already. Measured against the real region: the slug, the spec path and a
    # unit id were all silent, and only a fabricated id fired it. Promotion adds a NEW unit id, so
    # what has to be observed is an id present at HEAD and ABSENT at the run's own pinned BASE.
    rv_base=$(awk -F': ' '/^base: /{ sub(/\r$/,"",$2); print $2; exit }' "$rvf")
    rv_now=""; rv_then=""; rv_readable=0
    if [ -f "$rv_readme" ]; then
      rv_now=$(region "$rv_readme" '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null | grep -oE '[A-Z]+-[A-Za-z]+-[0-9]+' | sort -u || true)
      if [ -n "$rv_base" ] && GIT cat-file -e "$rv_base^{commit}" 2>/dev/null; then
        rv_then=$(GIT show "$rv_base:$rv_readme" 2>/dev/null | awk '/<!-- gen:build-units -->/{f=1;next} /<!-- \/gen:build-units -->/{f=0} f' | grep -oE '[A-Z]+-[A-Za-z]+-[0-9]+' | sort -u || true)
        rv_readable=1
      fi
    fi
    rv_new=""
    [ "$rv_readable" = 1 ] && rv_new=$(comm -23 <(printf '%s\n' "$rv_now") <(printf '%s\n' "$rv_then") | grep -c . || true)
    rv_bad="$rv_bad$(awk -v ceil="$RUNAWAY_CEILING" -v f="$rvf" -v readable="$rv_readable" -v newids="${rv_new:-0}" '
      /^[0-9][0-9-]*T[0-9:]*Z review · item / {
        line = $0; sub(/\r$/, "", line)
        i = index(line, " · item "); if (i == 0) next
        rest = substr(line, i + length(" · item "))
        j = index(rest, " · reason "); if (j == 0) next
        it = substr(rest, 1, j - 1); rs = substr(rest, j + length(" · reason "))
        n[it]++
        b = -1
        if (match(rs, /blockers [0-9]+/)) b = substr(rs, RSTART + 9, RLENGTH - 9) + 0
        if (it in last && b >= last[it]) flat[it] = flat[it] + 1; else flat[it] = 0
        last[it] = b
        if (rs ~ /CONVERGED|NON-CONVERGENT|CEILING/) term[it] = 1
        if (rs ~ /NON-CONVERGENT|CEILING/) needs[it] = 1
      }
      END {
        nneed = 0
        for (it in n) {
          if (n[it] > ceil)
            printf "\n  %s (subject %s: %d review rounds against a runaway ceiling of %d, so the loop ran past its own backstop)", f, it, n[it], ceil
          else if (flat[it] >= 1 && !(it in term))
            printf "\n  %s (subject %s: blocker counts did not shrink across consecutive rounds and no round carries an exit token, so the loop is non-convergent and nothing recorded that it stopped)", f, it
          if (it in needs) nneed++
        }
        # COUNTED ACROSS SUBJECTS, because `newids` is a per-FILE delta. Consumed inside the
        # per-subject loop it let ONE promotion satisfy every subject in the file that exited
        # without converging. A per-subject attribution is not available - the region records ids,
        # not which subject promoted them - so the honest claim is the counting one: N subjects that
        # exited owe at least N ids this run BASE lacked.
        if (nneed > 0) {
          if (readable != 1)
            printf "\n  %s (%d subject(s) EXITED without converging and the roster at this run BASE cannot be read, so whether a blocker was promoted CANNOT BE OBSERVED - a check that cannot look says so rather than passing)", f, nneed
          else if (newids + 0 < nneed)
            printf "\n  %s (%d subject(s) EXITED without converging and the generated units region gained only %d unit id(s) this run BASE lacked, so at least one blocker was neither fixed nor promoted)", f, nneed, newids + 0
        }
      }' "$rvf")"
  done
  [ -z "$(printf '%s' "$rv_bad" | tr -d '[:space:]')" ] || fail 2 "review loops that ran past the ceiling, stalled without recording it, or exited without promoting:$rv_bad"
fi

# ---- THE HALT VOCABULARY: a shrink-only floor, and every aborted record carrying a legal code.
# ---- The floor behaves like its two siblings — undeclared or malformed is a REFUSAL, never a
# ---- defaulted value, because a pin that quietly defaults is a pin nobody set.
if [ -z "$HALT_FLOOR" ]; then
  fail 2 "HALT_FLOOR is undeclared in .unattended.conf, and with no floor a deleted halt code is indistinguishable from a vocabulary that never had one"
elif ! printf '%s' "$HALT_FLOOR" | grep -qE '^[0-9]+$'; then
  fail 2 "HALT_FLOOR is not a single integer, so the shrink-only comparison below would be a string test wearing a numeric name: $HALT_FLOOR"
else
  nhalt=$(printf '%s' "$HALT_CODES_CORE" | wc -w)
  [ "$nhalt" -ge "$HALT_FLOOR" ] \
    || fail 2 "the kit's CORE halt vocabulary has shrunk below its floor, and deleting a member is a silent, reason-free override of every record that cited it: $nhalt against $HALT_FLOOR"
fi
if [ -z "$HALT_CODES_CORE" ]; then
  fail 2 "the driver declares no HALT_CODES_CORE vocabulary, so the abort verb would validate against an empty set and accept anything: $DRIVER"
fi

# ---- EVERY ABORTED RECORD CARRIES A LEGAL CODE. The population is every tracked run-state file,
# ---- ARCHIVED ONES INCLUDED — a record that could dodge this by being rotated would make the check
# ---- an honour system, and rotation is exactly what happens to a finished run.
# ---- No exemption clause and no waiver: the records that existed when this landed were migrated in
# ---- the same commit, so the check is green over the real tree on its first day rather than carrying
# ---- a grandfather list that outlives the reason for it.
if [ -n "$HALT_CODES_CORE" ]; then
  hc_bad=""
  for hcf in $(GIT ls-files "$M/builds/*/RUN*.md" 2>/dev/null); do
    [ -f "$hcf" ] || continue
    hcp=$(awk -F': ' '/^phase: /{ sub(/\r$/,"",$2); print $2; exit }' "$hcf")
    [ "$hcp" = ABORTED ] || continue
    hcv=$(awk -F': ' '/^halt-code: /{ sub(/\r$/,"",$2); print $2; exit }' "$hcf")
    if [ -z "$hcv" ]; then
      hc_bad="$hc_bad
  $hcf (phase ABORTED and no halt-code fact, so the record says a run stopped and never says why)"
    else
      case " $HALT_CODES " in
        *" $hcv "*) ;;
        *) hc_bad="$hc_bad
  $hcf (halt-code outside the effective vocabulary: $hcv)" ;;
      esac
    fi
  done
  [ -z "$(printf '%s' "$hc_bad" | tr -d '[:space:]')" ] || fail 2 "aborted run-state records whose halt code is missing or outside the effective vocabulary:$hc_bad"
fi

# ---- THE PARKED-KIND TAXONOMY, joined against the code that WRITES those kinds. One direction only,
# ---- and the asymmetry is deliberate rather than an oversight:
# ----
# ----   ASSERTED — every token in the surfaced set is a kind some `park` call site can actually write.
# ----   That catches a STALE MEMBER: a kind deleted from the driver and left behind in the taxonomy,
# ----   which silently widens a count that exists to be narrow. Same shape as an exemption naming a
# ----   path that no longer exists, which this repo reds in both directions elsewhere.
# ----
# ----   NOT ASSERTED — the converse, that every written kind is in the set. It is FALSE BY DESIGN:
# ----   `history` is the complement and is declared nowhere, so the first history kind would red a
# ----   check that demanded it. Writing that assertion would force a future unit to weaken this leg
# ----   in the same commit that adds a legitimate kind, which is worse than not having it.
# ----
# ---- So a NEW kind arrives unclassified and this leg stays silent about it. Said plainly because a
# ---- reader who assumes both directions are covered would be wrong, and the gap is in the design.
if [ -n "$PARK_KINDS_OWED" ]; then
  pk_dead=""
  for pk in $PARK_KINDS_OWED; do
    grep -qE "^[[:space:]]*park \"\\\$rel\" $pk " "$DRIVER" || pk_dead="$pk_dead $pk"
  done
  [ -z "$pk_dead" ] || fail 2 "the parked-kind taxonomy names a kind no park call site in the driver writes, so a count that exists to be narrow is silently wider than the code it measures:$pk_dead"
else
  fail 2 "the driver declares no PARK_KINDS_OWED taxonomy, so the surfaced count and the parked-decisions Definition-of-Done item both range over a set this leg cannot read: $DRIVER"
fi

# ---------------------------------------------------------------------- 2 + 3: the core-set floors
# WHY A COUNT AND NOT A MEMBERSHIP LIST. The first cut asserted "every CORE member is present in the
# effective set" — and the effective set is composed HERE as core plus the project's extras, so core
# is a subset BY CONSTRUCTION and the check could not fail. It armed cleanly and tested nothing:
# this repo's own vacuous-selector class, one level up. Caught by writing the red fixture and
# watching it stay green.
#
# The names stay in ONE place, the driver. What is pinned is a shrink-only COUNT — the shape
# `ARMS_FLOORS` and `baseline.toml` already use: deleting a core member drops the count below the
# floor and reds, adding one is free, and RAISING the floor is a deliberate edit that says why. The
# project layer can reach neither number, which is the property F3 asked for.
[ -n "$CORE_FLOOR" ] \
  || fail 1 "CORE_FLOOR is undeclared in .unattended.conf, and with no floor a deleted core member is indistinguishable from a set that never had one"
# A MALFORMED floor is a refusal, not a skip. `case *:*` accepted only the well-formed shape and
# left both floors EMPTY otherwise, so `CORE_FLOOR="6"` or `"six:six"` disarmed both shrink-only
# pins while the conf still looked configured. Only the wholly UNDECLARED case was being caught,
# which is the easier half of the same mistake.
pfloor=""; dfloor=""
if [ -n "$CORE_FLOOR" ]; then
  case "$CORE_FLOOR" in
    *[!0-9:]* | *:*:* | :* | *: | *[!0-9]) ;;
    *:*) pfloor=${CORE_FLOOR%%:*}; dfloor=${CORE_FLOOR##*:} ;;
  esac
  [ -n "$pfloor" ] && [ -n "$dfloor" ] \
    || fail 1 "CORE_FLOOR is malformed and both shrink-only floors are therefore unenforced; want two integers separated by a colon: $CORE_FLOOR"
fi
[ -n "$(printf '%s' "$PHASES" | tr -d '[:space:]')" ] \
  || fail 2 "the effective phase vocabulary is empty, which makes every phase check below vacuously true"
nphase=$(printf '%s\n' $PHASES_CORE | grep -c . || true)
if [ -n "${pfloor:-}" ] && [ "$nphase" -lt "$pfloor" ]; then
  fail 2 "the kit's CORE phase vocabulary has shrunk below its floor, and deleting a core member is a silent, reason-free override of everything keyed on it: $nphase against $pfloor"
fi
# A TERMINAL phase outside the vocabulary is unreachable, so no run could ever finish. Same vacuity
# from the other side — and this one IS falsifiable, because the two sets are declared independently.
for t in $PHASES_TERMINAL; do
  case " $PHASES " in *" $t "*) ;;
    *) fail 2 "a TERMINAL phase is not in the effective vocabulary, so no run could ever reach it: $t";; esac
done
[ -n "$(printf '%s' "$DOD" | tr -d '[:space:]')" ] \
  || fail 3 "the effective Definition-of-Done set is empty, so --close would block on nothing"
ndod=$(printf '%s\n' $DOD_CORE | grep -c . || true)
if [ -n "${dfloor:-}" ] && [ "$ndod" -lt "$dfloor" ]; then
  fail 3 "the kit's CORE Definition-of-Done set has shrunk below its floor, and deleting an item is a silent, reason-free override of everything keyed on it: $ndod against $dfloor"
fi
# THE SLACK ARM, the mirror of the one above. A floor BELOW the kit's own core count is not a pin
# at all: the set grew and the declaration did not, so the pin sits under the value it guards and
# would not notice a later deletion. The DIRECTIVES half has carried this arm; the two CORE halves
# did not, which is how a core set grows in the shipped example and not in a project's own conf
# while every check stays green.
nph=$(printf '%s
' $PHASES_CORE | grep -c . || true)
if [ -n "${pfloor:-}" ] && [ "$pfloor" -lt "$nph" ]; then
  fail 3 "the declared PHASE floor sits below the kit's own core count, so the pin guards nothing and a later deletion would pass it - declared against core: $pfloor against $nph"
fi
if [ -n "${dfloor:-}" ] && [ "$dfloor" -lt "$ndod" ]; then
  fail 3 "the declared Definition-of-Done floor sits below the kit's own core count, so the pin guards nothing and a later deletion would pass it - declared against core: $dfloor against $ndod"
fi

# --------------------------------------------------------------- the population, two granularities
FILES=$(git ls-files "$M/")
# PRECONDITION: a run-state file ANYWHERE under the memory root. POPULATION: one at the exact path
# this leg selects. Equal-and-zero is a young tree and is SILENT — a repo with no unattended run yet
# is not a violation, and a guard that cannot tell that from a mis-segmented selector reds every
# fresh adopter on install. Precondition non-zero with an empty population is the mis-segmentation.
PRE=$(printf '%s\n' "$FILES" | grep -cE '(^|/)RUN\.md$' || true)
# THE POPULATION IS THE LIVE RECORD PLUS EVERY ARCHIVED ONE (kit 1.6). Rotation retires a finished
# record to `RUN.<phase>.<blob8>.md` beside the live one, so every per-file check below now
# quantifies over both — checks 9, 13 and 15 included, which is what keeps an archived LANDED
# record's witness answerable to the anchor.
#
# `PRE` above is deliberately NOT widened: it is the mis-segmentation PRECONDITION, not the
# population. An archives-only tree reading PRE=0 with POP>0 is silent by design.
RUNS=$(printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/RUN(\.[A-Z]+\.[0-9a-f]{8})?\.md$" || true)
POP=$(printf '%s\n' "$RUNS" | grep -c . || true)
if [ "$POP" = 0 ] && [ "$PRE" -gt 0 ]; then
  fail 4 "a run-state file exists under the memory root but none at the path this leg selects, so the selector is mis-segmented and every check below is silent for the wrong reason: $PRE found"
fi

# PURE BASH, no forks. These were `sed … | head -1 | tr -d '\r'` — THREE processes per call, and they
# are called per run-state file per check, so the leg paid them dozens of times per invocation and
# its self-test paid them thousands of times per run. Process spawn dominates on Windows: the suite
# ran 77s for ~1.4s of CPU, and it was never the git calls (885 of those, ~24s), it was the forks
# around them. Same semantics: first matching line wins, `key:` followed by any run of spaces, a
# valueless key yields the empty string, and a trailing CR is stripped.
fact_of() { # file · key
  local l p="$2:"
  while IFS= read -r l || [ -n "$l" ]; do
    l=${l%$'\r'}
    case "$l" in
      "$p"*) l=${l#"$p"}; while [ "${l# }" != "$l" ]; do l=${l# }; done; printf '%s\n' "$l"; return 0 ;;
    esac
  done < "$1"
  return 0
}
phase_of() { fact_of "$1" phase; }
# Exactly one open, one close, CLOSE AFTER OPEN. The order clause is not decoration: a transposed
# pair satisfies a count-only check, and the driver's copy of this function truncated a file on one.
# A marker line is the marker or it is malformed — the prefix test IDENTIFIES the line, equality
# judges it. The old form let a run append its own authorization to the `<!-- run:mandate -->` line:
# both slices dropped the whole line, compared byte-equal, and the injected sentence sat inside the
# block a human reads. Reproduced at gate exit 0 with no output. CR-normalised before comparing,
# because the prefix test tolerated a CRLF worktree by accident and an equality test does not.

# THE REPORT CHANNEL. Silent by default, so the contract above holds byte for byte and the three
# green-control arms in the sibling test keep their meaning. A check that cannot compare says which
# arm went unexercised and why, and an operator asks for those by setting the variable. Liveness is
# not left to the default run: the sibling test asserts the channel EMITS, which is the arm that
# would notice this going quiet.
REPORT=${GOV_UNATTENDED_REPORT:-0}
report() { [ "$REPORT" = 1 ] && printf 'unattended-report: %s\n' "$1"; return 0; }

# ---- 14: a replace ref or a graft file in a repo running an unattended run IS the violation, not
# ---- only a mechanism to suppress. The `GIT()` pin makes THIS leg's reads honest; nothing binds the
# ---- next tool that reads the same objects, and the run can add one at any moment.
if [ "$POP" -gt 0 ]; then
  rr=$(git for-each-ref --format='%(refname)' refs/replace/ 2>/dev/null | grep -c . || true)
  [ "$rr" = 0 ] \
    || fail 14 "a repo carrying an unattended run-state file also carries replace refs, and a replace ref rewrites what a sha MEANS for every read that is not pinned: $rr found"
  gf="$(git rev-parse --git-common-dir 2>/dev/null)/info/grafts"
  [ ! -f "$gf" ] \
    || fail 14 "a repo carrying an unattended run-state file also carries a grafts file, which rewrites the commit GRAPH underneath every ancestry read: $gf"
fi

# ITERATED WITH `read`, NOT WORD-SPLIT. `for f in $RUNS` split a tracked path containing a space into
# two non-existent paths, both swallowed by the `[ -f ]` guard — so every per-file check below never
# ran on that file and the gate exited 0 without ever naming it. The mis-segmentation guard at check
# 4 above could not see it either: the path matches the selector, it is the LOOP that loses it.
# ---- S6c: ONE advertisement per leg RUN, never per record. This leg made ZERO network calls before
# ---- this unit. Check 9's predicate is now stated against what the REMOTE advertises, and AC8
# ---- forbids the leg from reading `anchor-kind` — a value its own subject writes — so it cannot
# ---- know which records need the observation and must hold it for all of them.
# ----
# ---- FAIL-CLOSED, decided rather than left open, and the cost is smaller than it first looks. The
# ---- AUTHORITATIVE run of this bar is `.githooks/pre-push`, and a push has the network by
# ---- construction, so the run that actually decides a landing never pays this. An offline
# ---- diff-scoped run pays it LOUDLY, which is the whole point: failing open would disarm the only
# ---- BASE check on the bar, and that is the silent-skip shape this file refuses by name elsewhere.
# ---- GIT_TERMINAL_PROMPT=0 is carried HERE rather than left to the driver: this leg runs under a
# ---- hook with no tty. WHAT IT ACTUALLY DOES, corrected: it bounds git's OWN prompt and says
# ---- nothing about a configured credential HELPER, which is a separate process — a helper that
# ---- opens a GUI dialog blocks with nothing on stdout and the variable never reaches it. That is
# ---- why the observation below also passes `credential.interactive=never`, which is the setting a
# ---- helper reads, and why it is passed with `-c` so it cannot reach the landing push. This comment
# ---- previously claimed the variable made a prompt "refuse rather than hang"; it does not, and a
# ---- comment asserting a bound nothing provides is worse than no comment, because it stops the next
# ---- reader looking.
# ---- BOUNDED. These two calls run inside $GATE_CMD, which runs inside .githooks/pre-push, so an
# ---- unbounded one HANGS THE PUSH instead of reddening it — strictly worse than the driver's case,
# ---- where at least an operator is watching. Both go through the same three-part bound the driver
# ---- uses, spelled once in the helper below, and both capture through a FILE: a command
# ---- substitution around `timeout` reads until EOF and a surviving descendant holds the pipe, so
# ---- the verdict is bounded while the clock is not. Measured, on this node and in the gate runner.
ADV_HEAD=""; ADV_TIPS=""
# EXACTLY ONE remote, matching the driver's check 24. `| head -1` blessed whichever name sorted
# first, with none of the endpoint guards the driver applies — so a run that adds a second
# remote it controls could have the leg measure "published" against an endpoint the landing push
# never reaches. A clone with several remotes is refused rather than guessed at.
adv_nrem=$(GIT remote 2>/dev/null | grep -c . || true)
adv_remote=""
if [ "$adv_nrem" = 1 ]; then
  adv_remote=$(GIT remote 2>/dev/null | head -1)
elif [ "$adv_nrem" != 0 ]; then
  adv_remote=""
fi
# CARRIED AS ITS OWN CAUSE. Both remote-count states used to arrive downstream as an empty
# advertisement and print "the remote advertised no tips" - a message about the REMOTE for a fault in
# this clone's own configuration. The split above already existed; only the reporting was missing.
ADV_NREM_RC=0
[ "$adv_nrem" = 0 ] && ADV_NREM_RC=96
{ [ "$adv_nrem" != 0 ] && [ "$adv_nrem" != 1 ]; } && ADV_NREM_RC=97
# GUARDED on the population too: with no run-state file there is nothing whose BASE could be
# checked, and two network round-trips per bar run bought exactly nothing. POP is computed above.
# The bound, and the pins, in ONE place shared with the driver's helper. The leg cannot source the
# driver — it reads it as data — so the constants are read FROM it the same way every other core set
# is, through core_of, rather than spelled a second time here. A leg that carried its own copy of the
# bound would be the two-answers class, and this file already refuses that shape elsewhere.
REMOTE_BOUND=$(core_of REMOTE_BOUND)
REMOTE_CONNECT_BOUND=$(core_of REMOTE_CONNECT_BOUND)
REMOTE_LOWSPEED_BYTES=$(core_of REMOTE_LOWSPEED_BYTES)
# NO FALLBACK. A `${x:-60}` made an unreadable bound indistinguishable from a successful read, and
# that is exactly how this went green while reading nothing: the driver declared all three UNQUOTED,
# core_of matches only KEY="value", and every read returned empty. The defaults then restated the
# driver's numbers from memory, so the single-source comment above described something the code did
# not do and tuning the driver moved nothing here. An unreadable bound now refuses, the way
# RUNAWAY_CEILING already does.
if [ -z "$REMOTE_BOUND" ] || [ -z "$REMOTE_CONNECT_BOUND" ] || [ -z "$REMOTE_LOWSPEED_BYTES" ]; then
  fail 2 "the driver declares no readable REMOTE_BOUND, REMOTE_CONNECT_BOUND or REMOTE_LOWSPEED_BYTES, so this leg would observe the remote under bounds it invented rather than the ones the driver uses; core_of reads a double-quoted value only, so an unquoted constant reads as absent"
  REMOTE_BOUND=60; REMOTE_CONNECT_BOUND=20; REMOTE_LOWSPEED_BYTES=1000
fi
REMOTE_BOUND_LIVE=1
timeout -k 1s 1 true >/dev/null 2>&1 || REMOTE_BOUND_LIVE=0
# IT MUST SAY SO. The flag's only reader used to be the `if` below, so on a node with no working
# `timeout -k` every observation ran with the wall-clock bound silently absent and byte-identical
# output — a skip that looks like a pass. The transport options still apply on that path; it is the
# wall clock specifically that is gone, and the line says which. TO STDERR: fail() writes to
# stdout, so an advisory sharing that channel is indistinguishable from a violation.
[ "$REMOTE_BOUND_LIVE" = 1 ] || echo "unattended-check: NOTE - this node has no working 'timeout -k', so the ${REMOTE_BOUND}s wall-clock bound on remote observation is INERT; http.lowSpeed and ssh ConnectTimeout still apply" >&2
# WRITES TO `$adv_f` BY NAME, not to a parameter, and that is deliberate. This leg has a source-level
# arm asserting it performs no write into the tree it judges, and that arm allows a redirect only when
# its target variable is assigned from `mktemp` in this same file — a property check rather than a
# blessed spelling. A parameter would defeat it, and with exactly ONE caller here the parameter bought
# nothing anyway. `adv_f` is set by that caller before this runs.
# THE NAMED PINS, sourced from the kit library above. Moving GIT() into that library gave the
# DRIVER the constants and left these two sites spelling the values literally, which is exactly
# the drift naming them was meant to prevent: this helper cannot call GIT(), because it needs
# the pins as argv to `timeout`, so it is the one caller that must spell them and the one that
# silently goes stale when they change.
observe_remote() { # <git args…> -> rc (124 = the bound fired); output lands in $adv_f
  local rc
  if [ "$REMOTE_BOUND_LIVE" = 1 ]; then
    timeout -k 5s "$REMOTE_BOUND" \
      env GIT_TERMINAL_PROMPT=0 \
          "GIT_SSH_COMMAND=ssh -o ConnectTimeout=$REMOTE_CONNECT_BOUND -o BatchMode=yes" \
      git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV" \
          -c credential.interactive=never \
          -c "http.lowSpeedLimit=$REMOTE_LOWSPEED_BYTES" -c "http.lowSpeedTime=$REMOTE_BOUND" \
          "$@" >"$adv_f" 2>/dev/null
    rc=$?
  else
    env GIT_TERMINAL_PROMPT=0 \
        "GIT_SSH_COMMAND=ssh -o ConnectTimeout=$REMOTE_CONNECT_BOUND -o BatchMode=yes" \
    git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV" \
        -c credential.interactive=never \
        -c "http.lowSpeedLimit=$REMOTE_LOWSPEED_BYTES" -c "http.lowSpeedTime=$REMOTE_BOUND" \
        "$@" >"$adv_f" 2>/dev/null
    rc=$?
  fi
  return "$rc"
}
# THE THREE OUTCOMES ARE KEPT APART. They used to collapse into one message: `mktemp` failing skipped
# both observations SILENTLY, observe_remote's status was discarded by an `&&`, and the only branch
# left downstream said "the remote advertised no tips" - so a dead TMPDIR and a fired wall-clock bound
# both reported as a remote that answered nothing. The driver separates the same three one file over;
# the fix was made there and not carried across.
ADV_RC=0
if [ -n "$adv_remote" ] && [ "$POP" != 0 ]; then
  adv_f=$(mktemp) || adv_f=""
  if [ -z "$adv_f" ]; then
    ADV_RC=98
  else
    observe_remote ls-remote --symref --exit-code "$adv_remote" HEAD; _rc1=$?
    [ "$_rc1" = 0 ] && ADV_HEAD=$(awk -F'\t' '{ sub(/\r$/,"",$2) } $2=="HEAD" && $1 ~ /^[0-9a-f]+$/ { print $1; exit }' "$adv_f")
    # THE SYMREF NAME, beside the sha — TOOL-dUnstalledConvoy-2 needs it for the local landing arm,
    # and the advertisement is the only admissible source: GOV_DEFAULT_BRANCH and every
    # `refs/remotes/*` read were purged from this path because the run can write both.
    #
    # READ FROM THE CAPTURE FILE, not from a command substitution. The version that introduced this
    # parse fetched the advertisement again through `$(GIT ls-remote ...)` with NO timeout, which
    # un-bounds the observation this leg spent a build bounding: a substitution reads until EOF, EOF
    # waits on the last inherited write end, and a surviving descendant holds it while `timeout`
    # reports on schedule. The name was in the bytes already captured, so it costs no second call.
    [ "$_rc1" = 0 ] && ADV_NAME=$(awk -F'	' '{ sub(/$/,"",$2) } $2=="HEAD" && $1 ~ /^ref: / { sub(/^ref: /,"",$1); sub(/^refs\/heads\//,"",$1); print $1; exit }' "$adv_f")
    observe_remote ls-remote --heads "$adv_remote"; _rc2=$?
    [ "$_rc2" = 0 ] && ADV_TIPS=$(awk -F'\t' '$1 ~ /^[0-9a-f]+$/ { print $1 }' "$adv_f")
    # 124 is the bound firing. Either call hitting it means this leg observed nothing it can trust.
    { [ "$_rc1" = 124 ] || [ "$_rc2" = 124 ]; } && ADV_RC=124
    # ...and ANY OTHER non-zero is a transport failure, which is also not an answer. Splitting 124 out
    # left every other failure - auth refused, DNS gone, the endpoint 404ing - landing on a message
    # about what the remote ADVERTISED, which is a claim this leg never got close enough to make.
    # `--exit-code` makes 2 mean "answered, advertised nothing", so 2 is a real answer and stays.
    if [ "$ADV_RC" = 0 ]; then
      case "$_rc1:$_rc2" in
        0:0|0:2|2:0|2:2) ;;
        *) ADV_RC=95 ;;
      esac
    fi
    rm -f "$adv_f"
  fi
fi

# PUBLISHED = an ancestor of a tip the remote advertises. Ancestry and NOT equality, and the
# distinction is the whole of S6: under the second anchor the BASE is pinned to the advertised branch
# tip, the run then commits and pushes that same branch again — which is exactly what the Skill tells
# it to do — and the advertised tip moves PAST the pin. Equality reds from that moment on, forever,
# and worse after a branch delete or a squash-merge landing. This file already records being moved
# off equality once for that reason; writing it back in a second place would re-earn the same wedge.
# THREE ANSWERS, NOT TWO, and the third is the one that cost a red bar. `--is-ancestor` fails both
# when the commit is NOT an ancestor and when the tip is not in this clone's object store, and this
# function used to collapse those into "not published". A clone that has not fetched since the remote
# advanced therefore reported EVERY record as naming a commit that exists only locally - measured
# here on 2026-08-21: sixteen records, every one of them honest, all sixteen red, and the same leg
# green minutes later once the tip had been fetched. A bar that reds on network timing rather than on
# the tree is worse than one that reds stably, because the fix people reach for is a re-run.
#
# The driver has carried the distinction for longer (its check 30, "the remote advertises a tip this
# clone does not have"); this side had not been given it.
is_published() { # commit -> 0 published · 1 not published · 2 CANNOT TELL, a tip could not be read
  # THE INVARIANT IS "EVERY TIP WAS READABLE", not "at least one was". The first cut tracked PRESENCE
  # and returned 2 only when ALL advertised tips were absent, so a single stale locally-present branch
  # restored the forgery-shaped false red for every record. Reproduced against this clone: three tips
  # advertised, one present and two absent, so `have` was 1 and the answer came back a definite
  # "not published" computed from a third of the evidence. Sound form: not-published requires that no
  # present tip contains the commit AND that nothing was unreadable; anything less is cannot-tell.
  local c="$1" t miss=0
  if [ -n "$ADV_HEAD" ]; then
    if GIT cat-file -e "$ADV_HEAD^{commit}" 2>/dev/null; then
      GIT merge-base --is-ancestor "$c" "$ADV_HEAD" 2>/dev/null && return 0
    else
      miss=1
    fi
  fi
  for t in $ADV_TIPS; do
    if GIT cat-file -e "$t^{commit}" 2>/dev/null; then
      GIT merge-base --is-ancestor "$c" "$t" 2>/dev/null && return 0
    else
      miss=1
    fi
  done
  [ "$miss" = 0 ] || return 2
  return 1
}

live=""; nlive=0
while IFS= read -r f; do
  [ -n "$f" ] || continue
  if [ ! -f "$f" ]; then
    fail 4 "a run-state file is tracked at a path this leg cannot read, and skipping it silently removes it from every check below: $f"
    continue
  fi
  ph=$(phase_of "$f")

  # ---- 4: the phase token is IN the declared vocabulary. Unit 1 kept the run-state file out of the
  # ---- status-vocabulary check on purpose, so this is the ONLY place a phase is validated.
  if [ -z "$ph" ]; then
    fail 4 "a run-state file declares no phase, and a file with no phase is outside every check keyed on one: $f"
    continue
  fi
  case " $PHASES " in *" $ph "*) ;;
    *) fail 4 "a run-state file declares a phase outside the effective vocabulary: $ph in $f (legal: $PHASES)";; esac

  case " $PHASES_TERMINAL " in *" $ph "*) ;; *) nlive=$((nlive+1)); live="$live $f";; esac

  # AN ARCHIVED RECORD MUST BE TERMINAL, and this is its own branch rather than a consequence of the
  # live-run rule below. Check 7 is `nlive <= 1`, which fires at TWO — so a `RUN.md` that has reached
  # LANDED plus one archived record hand-edited back to RUNNING gives nlive=1 and the leg says
  # nothing. That is the steady state after every completed second run, which makes it the one window
  # where the widened population would otherwise buy less than it looks like it does.
  case "$f" in
    */RUN.md) ;;
    *) case " $PHASES_TERMINAL " in *" $ph "*) ;;
         *) fail 4 "an ARCHIVED run-state file carries a non-terminal phase, so a finished record was retired while still claiming to be live, or was edited after retirement: $ph in $f";; esac;;
  esac

  # ---- 5: witness PRESENCE, its own branch. Check 6 below reuses the drift oracle's judgeability
  # ---- discipline, which SKIPS a claim carrying no sha — so folding presence into resolution makes
  # ---- naming no witness the cheapest way for a run to say nothing, and it is the sole author here.
  w=$(fact_of "$f" witness)
  if [ -z "$w" ]; then
    fail 5 "a phase claim carries no witness, and presence is its own refusal because an oracle that skips an unwitnessed claim can never fire on one: $ph in $f"
  else
    # ---- 6: a PRESENT witness must resolve. Unjudgeable shapes (a workflow id, a tag this clone has
    # ---- not fetched) are skipped, which is legal ONLY because check 5 already refused absence.
    case "$w" in
      [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]*)
        GIT rev-parse --verify --quiet "$w^{commit}" >/dev/null 2>&1 \
          || fail 6 "a witness looks like a sha and resolves to no commit in this history: $w in $f" ;;
      *) ;;   # not sha-shaped: unjudgeable, and skipping it is the discipline, not an omission
    esac
  fi

  # ---- 15, FIRST HALF: a claim of LANDED carries a SHA. The protocol permits a sha, a tag or a
  # ---- workflow id for a phase claim generally, and section 3 now narrows that for the TERMINAL
  # ---- phases, because here the ancestry assertion below IS the claim — an unjudgeable witness at
  # ---- LANDED is a landing nothing can check, which is the whole thing this check exists for.
  # ----
  # ---- OUTSIDE the anchor loop, deliberately. This half needs no anchor, no recorded BASE and no
  # ---- remote-tracking ref; folding it in with the ancestry half below would gate it on three
  # ---- preconditions it does not need, and on a clone with no default branch resolvable it would
  # ---- run zero times while looking like coverage.
  if [ "$ph" = LANDED ]; then
    case "$w" in
      [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]*) ;;
      *) fail 15 "a record claims LANDED with a witness that is not sha-shaped, so the claim that the work reached the remote cannot be judged at all, and a terminal claim is exactly where an unjudgeable witness costs the most: $w in $f" ;;
    esac
  fi

  # ---- 8: the generated region holds NO COPY of the unit list. It is DERIVED from the build README
  # ---- on every read, so there is nothing here to keep fresh.
  #
  # This check used to assert the opposite — that the region EQUALS the README slice — and the
  # equality was unmaintainable in the ordinary case: a spec rev bump moves the build index, and the
  # region's only writer was `--preflight`, which refuses once a run is live. The refusal told the
  # reader to "re-run the driver", naming a path no verb walks. Asserting EMPTINESS is the same
  # invariant with the copy removed: one fact, one home, and nothing to go stale between reads.
  # THE TERMINAL EXEMPTION IS SCOPED TO EMPTINESS, and only emptiness. It used to clear `rd`, which
  # skipped BOTH refusals below — so a terminal record with MALFORMED generated markers was exempt from
  # a shape check that has nothing to do with why the exemption exists. The exemption is for a finished
  # run whose region legitimately holds a frozen roster; a marker pair is either well-formed or it is
  # not, in every phase.
  # MEASURED 2026-08-20: unexempting the marker-shape branch reds NOTHING — every tracked record has a
  # well-formed pair. That is why this is safe to tighten and also why it needs a RED FIXTURE in the
  # sibling test: a check whose only evidence is a corpus that cannot trigger it is the
  # fixture-passes-by-finding-nothing class, which is this whole unit's subject.
  # THE README GUARD IS GONE, AND IT WAS SKIPPING THE WHOLE CHECK ON EVERY ARCHIVED RECORD. `rd` was
  # `${f%/RUN.md}/README.md`, but the selector above deliberately admits `RUN.<PHASE>.<8hex>.md`, where
  # that suffix strip is a NO-OP - so `rd` named a path INSIDE the record file, the guard was always
  # false, and three tracked archived records were silently exempt. That also took the measurement
  # above over a population three records short. Nothing else read `rd`; the block reads only `$f`.
  term=0
  case " $PHASES_TERMINAL " in *" $ph "*) term=1 ;; esac
  a=$(region "$f" '<!-- run:generated -->' '<!-- /run:generated -->' 2>/dev/null) || \
    fail 8 "a run-state file's generated markers are malformed: $f"
  [ "$term" = 1 ] || [ -z "$(printf '%s' "$a" | tr -d '[:space:]')" ] || \
    fail 8 "a run-state file's generated region carries a COPY of the unit list; that list is DERIVED from the build README on every read, so a copy here is a second answer waiting to go stale. Empty the region between its markers: $f"

  # ---- 9: the recorded BASE must be the merge-base git reproduces. A pin the run can quietly move
  # ---- is not a pin, and every mandate assertion hangs on this value.
  # ---- AN ABSENT `base:` LINE IS THE VIOLATION, not the exemption. Wrapping this in `if [ -n ]`
  # ---- meant deleting one line from a run-writable file disarmed the only BASE check on the bar.
  rb=$(fact_of "$f" base)
  if [ -z "$rb" ]; then
    fail 9 "a run-state file records no BASE, and the record is written by the run — an absent pin is not a satisfied one: $f"
  else
    # S6/S6b: the ADVERTISEMENT replaces the remote-tracking loop, and with it goes the last place
    # this leg read GOV_DEFAULT_BRANCH or a `refs/remotes/*` ref on the BASE path — both of which the
    # run can write, which is what TOOL-aStandingWrit-6 records. The loop carried five things and
    # each is disposed of explicitly rather than left to fall out of the rewrite:
    #   1 the not-a-commit refusal      — kept, below, and it needs no anchor
    #   2 ancestor-of-anchor            — REPLACED by is_published (this is S6 itself)
    #   3 ancestor-of-HEAD              — KEPT. Clause 2 has no relation to this run's history, so a
    #                                     BASE published on a wholly unrelated ref would otherwise
    #                                     satisfy the check; this is what ties it to this tree
    #   4 the phase-keyed `rb != HEAD`  — kept, below, and it needs no anchor
    #   5 check 15's second half        — kept, RE-ANCHORED to the advertised HEAD tip, which is the
    #                                     same commit the old `$b` resolved to on an honest tree
    if [ -z "$ADV_HEAD" ] && [ -z "$ADV_TIPS" ]; then
      # FAIL CLOSED, and this branch is the whole of that claim. Without it the block below was
      # simply SKIPPED when the remote did not answer — every check-9 BASE predicate, check 15's
      # second half, and (through the rb gate) the check-13 mandate assertion, silently absent on
      # a forged base. That is fail-OPEN under a comment promising the opposite, and a REGRESSION:
      # before this unit the leg read local refs and still checked something.
      # THREE OUTCOMES, THREE MESSAGES. "The remote answered nothing" is kept for the case where git
      # actually answered; a fired bound and a dead scratch dir are different faults with different
      # remedies, and one message for all three sent the reader at the network every time.
      if [ "$ADV_NREM_RC" = 96 ]; then
        fail 9 "this clone declares NO remote, so there is no endpoint to observe and whether a recorded BASE is published was never asked; that is a fault in this clone rather than an answer about any remote: recorded $rb in $f"
      elif [ "$ADV_NREM_RC" = 97 ]; then
        fail 9 "this clone declares more than one remote, so which endpoint published would even mean is a guess; the leg refuses to pick one rather than measuring the BASE against whichever name sorts first: recorded $rb in $f"
      elif [ "$ADV_RC" = 95 ]; then
        fail 9 "the remote could not be reached to observe its tips, so whether a recorded BASE is published is UNKNOWN rather than answered no; that is a transport or credential fault and not a statement about what the remote holds: recorded $rb in $f"
      elif [ "$ADV_RC" = 98 ]; then
        fail 9 "cannot create a scratch file to capture the remote advertisement, so this leg observed NOTHING and the BASE predicates below would be graded against an empty answer; this is a fault on THIS side, not the remote's: $f"
      elif [ "$ADV_RC" = 124 ]; then
        fail 9 "the remote observation was KILLED by this kit's own wall-clock bound rather than answered, so the recorded BASE could not be checked; that is a partition or a stalled server, not a remote that advertises nothing: $f"
      else
        fail 9 "the remote advertised no tips, so the recorded BASE cannot be shown to be published and this leg will not pass a run it could not check; the bar's authoritative run is the pre-push hook, which has the network by construction: $f"
      fi
    else
      # D3: PROVED PRESENT, not merely non-empty. `$b` is the advertised HEAD tip, which a clone
      # that has not fetched does not have — and `--is-ancestor` against a missing object fails,
      # which red three honest LANDED records. An absent tip disables the ancestry half only.
      b="$ADV_HEAD"
      GIT rev-parse --verify --quiet "$b^{commit}" >/dev/null 2>&1 || b=""
        # ANCESTRY, NOT EQUALITY — and the reason is the kit's own first success. Equality wedged the
        # bar permanently: merging then pushing, the two acts an authorization grants, move the
        # merge-base past the pin forever, so a LANDED record red every later default-branch push.
        # Reproduced on an honest fixture with no attacker. A phase-keyed carve-out is not the fix
        # either — the run writes `phase:`, so it would be a one-line escape from this check.
        # What actually matters, and what survives landing: the recorded BASE lies on the history the
        # ANCHOR names rather than on the branch the run authored.
        if ! GIT rev-parse --verify --quiet "$rb^{commit}" >/dev/null 2>&1; then
          fail 9 "a recorded BASE does not resolve to a commit in this history, and the record is written by the run: $rb in $f"
        else
          # CAPTURED, not read off $? two conditions later. Threading a three-way status through an
          # elif chain makes the second branch read the status of the first TEST rather than of the
          # call, which is the guard-shares-state-with-what-it-guards shape this kit refuses.
          is_published "$rb"; _pubrc=$?
          if [ "$_pubrc" = 0 ]; then
            if ! GIT merge-base --is-ancestor "$rb" HEAD 2>/dev/null; then
              fail 9 "a recorded BASE is not an ancestor of HEAD, so the run-state file pins a commit this working history does not build on: $rb in $f"
            fi
          elif [ "$_pubrc" = 2 ]; then
            fail 9 "the remote advertised tips this clone does not have, so whether a recorded BASE is published CANNOT BE OBSERVED and this leg will not answer a question it could not ask; fetch and re-run: recorded $rb in $f"
          else
            fail 9 "a recorded BASE is not published on the remote — it is an ancestor of no tip the remote advertises, so it names a commit that exists only where this run could have authored it: recorded $rb in $f"
          fi
        fi
        # ONLY once the run claims to have built something. At PREFLIGHT and through the pass
        # phases the base legitimately equals HEAD - that is a run that has correctly built
        # nothing yet, and the driver blesses it there. Refusing it here made the two halves of one
        # kit disagree, each with its own green test.
        # ABORTED IS NOT A WORK-CLAIMING PHASE, and it used to be listed here. An aborted run
        # authorizes no landing, so the clause buys nothing on it — while a run that aborts before its
        # first commit records a base equal to HEAD (the pin is taken through the degenerate path at
        # preflight) and red the bar with its own abort record, on the one exit that exists for a run
        # which cannot meet its obligations. Reachable for the first time now that a verb writes it.
        case "$ph" in
          LANDING|LANDED|VERIFYING)
            [ "$rb" != "$(GIT rev-parse HEAD)" ] || fail 9 "the recorded BASE equals HEAD at a phase that claims work was done, so the run authored every byte an authorization comparison would read: $f" ;;
        esac
        # ---- 15, SECOND HALF: the LANDED witness lies on the history the ANCHOR blesses. The first
        # ---- half above already refused a witness that is not sha-shaped, so reaching this with an
        # ---- unjudgeable one is impossible and no skip is needed. This half is INSIDE the loop
        # ---- because it needs the anchor, and it therefore inherits check 9's silent skip where no
        # ---- default branch resolves — stated in the unit's own non-goals rather than implied.
        # SHA-SHAPED ONLY, and RESOLVING only. `fail` does not `continue`, so without the shape guard
        # this ran on the very witness the first half had just rejected and the record red TWICE with
        # two sentences that contradict each other - one saying the witness is not a sha, the next
        # reasoning about its ancestry. And resolvability is check 6's question, asked one loop up for
        # every sha-shaped witness at any phase; asking it again here is a second answer to it, so this
        # half stays silent on an unresolvable witness and lets check 6 own it.
        case "$w" in
          [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]*)
            # GUARDED on a non-empty anchor. `$b` is the ADVERTISED HEAD tip now, and a remote that answers
            # with heads but no HEAD symref leaves it empty — `--is-ancestor "$w" ""` then fails, and this
            # fired on an honest LANDED record. The old `$b` was a loop variable that could not be empty.
            if [ "$ph" = LANDED ] && [ -n "$b" ] && GIT rev-parse --verify --quiet "$w^{commit}" >/dev/null 2>&1; then
              # THE RECORDED ANCHOR KIND DECIDES WHICH HISTORY BLESSES THE WITNESS. A `local` record is
              # a claim about ONE clone: the protocol says plainly it is a RECORD of a merge and not an
              # OBSERVATION of one, so a clone that never had that merge cannot judge it and says so
              # rather than redding. Without that, a run lands locally on one node and the same leg
              # reds on every other node that has not fast-forwarded its own default branch.
              #
              # THIS GRADES THE RECORDED CLAIM, it does not re-derive the driver's pick. The driver
              # chose an anchor by testing ancestry; this asks whether the claim is well-formed and
              # whether history still supports it — two questions the driver never asked, both of which
              # can fail on a record the driver wrote happily.
              ak=$(fact_of "$f" landed-anchor)
              case "$ak" in
                remote|"") ;;
                local) ;;
                *) fail 15 "a record claims LANDED with an anchor kind outside the closed set of remote and local, and defaulting an unrecognised one would promote the record to whichever claim the reader assumed: $ak in $f" ;;
              esac
              if [ -z "$ak" ]; then
                # GRANDFATHERED BY DATE, the same idiom this kit's other cutoffs use. Every LANDED
                # record written before this unit carries no anchor kind and every one of them is in
                # fact remote-anchored; a record dated at or after the cutoff has no such excuse.
                fcommit=$(GIT log --diff-filter=A --format=%cs -- "$f" 2>/dev/null | tail -1)
                if [ -n "$LANDED_ANCHOR_CUTOFF" ] && [ -n "$fcommit" ] \
                   && printf '%s\n%s\n' "$LANDED_ANCHOR_CUTOFF" "$fcommit" | sort -C; then
                  fail 15 "a record claims LANDED and names no anchor kind while its own first commit is at or after the declared cutoff, so which history was meant to bless its witness cannot be read at all: $f"
                else
                  ak=remote
                fi
              fi
              if [ "$ak" = local ]; then
                if [ -n "$ADV_NAME" ] && GIT rev-parse --verify --quiet "refs/heads/$ADV_NAME" >/dev/null 2>&1 \
                   && GIT merge-base --is-ancestor "$w" "refs/heads/$ADV_NAME" 2>/dev/null; then
                  : # the local default branch carries it, which is the claim
                elif GIT merge-base --is-ancestor "$w" "$b" 2>/dev/null; then
                  : # ...or it reached the remote afterwards, which is an UPGRADE and not a defect
                else
                  report "check 15 skipped for $f — a local-anchored LANDED names a witness this clone does not carry on its own default branch, and a local anchor is a record of a merge rather than an observation of one, so this clone cannot judge it"
                fi
              elif ! GIT merge-base --is-ancestor "$w" "$b" 2>/dev/null; then
                fail 15 "a record claims LANDED with a witness that is not an ancestor of the anchor, so the work it says reached the remote is not on the branch the remote calls its default: $w against $b in $f"
              fi
            fi ;;
        esac
    fi
  fi

  # ---- 13: THE AUTHORIZATION, asserted by the BAR and not only by the driver. This leg once did not
  # ---- contain the marker string at all: it checked the driver's bookkeeping and never the thing the
  # ---- bookkeeping was about, so all three authorization defects reproduced against it were invisible
  # ---- here and the whole bar stayed green. The subject moved from a mandate block inside the
  # ---- run-state file to the BUILD FOLDER itself; the obligation to assert it here did not.
  # ----
  # ---- A SECOND OPINION, not a second implementation: it derives the build README path from the
  # ---- run-state file's own location and reads it at the recorded BASE itself.
  # ----
  # ---- Honest limit, and it belongs next to the code rather than in a document nobody reads at the
  # ---- same time: `rb` is read from a file the run writes. This is an internal-consistency assertion
  # ---- over run-written facts, stable and offline and deterministic - not an authorization verdict.
  # ---- What makes it one is running this same leg in a clone the run never touched.
  if [ -n "$rb" ] && GIT rev-parse --verify --quiet "$rb^{commit}" >/dev/null 2>&1; then
    bslug=${f#"$M/builds/"}; bslug=${bslug%%/*}
    bre="$M/builds/$bslug/README.md"
    if bb=$(GIT show "$rb:$bre" 2>/dev/null); then
      bad_fm=0
      case "$bb" in
        "---"*) ;;
        *) fail 13 "the build README at a run's recorded BASE is not a build README - front matter opens at line 1 and this does not, so the authorization names something that is not a build: $bre"
           bad_fm=1 ;;
      esac
      # The slug comparison PRESUMES line 1 is the front-matter opener. Falling through emitted a
      # second, false "declares a different slug" for a file that is simply not a README - and the
      # driver this leg second-opinions returns after the first refusal.
      [ "$bad_fm" = 0 ] || continue
      dslug=$(printf '%s\n' "$bb" | awk '
        NR == 1 { next }
        /^---[[:space:]]*\r?$/ { exit }
        /^slug:/ { sub(/^slug:[[:space:]]*/, ""); sub(/[[:space:]]*\r?$/, ""); print; exit }')
      [ "$dslug" = "$bslug" ] || fail 13 "a build README at its run's recorded BASE declares a different slug, so the folder was renamed or its README copied from another build: declared $dslug, folder $bslug"
      # ---- 19: THE AUTHORIZATION MODE, re-derived here rather than believed. TOOL-aPromptedMandate-1.
      # ---- A SECOND OPINION in check 13's own shape: the same blob, an independent parse, compared
      # ---- against what the run recorded. The driver reads this key to DECIDE which discipline binds
      # ---- a run; a value only the driver ever reads is a value only the driver can be wrong about.
      # ----
      # ---- PRESENCE-GUARDED, deliberately. Every run-state file written before this unit carries no
      # ---- `mode:` line at all, and the leg's documented idiom is silence on absence - so a legacy
      # ---- record is outside this arm by construction rather than by a waiver. What is NOT guarded
      # ---- is the other direction: a record that HAS a mode must agree with the README, and an
      # ---- absent key at BASE means `slug`, which is what the driver writes for it.
      # ----
      # ---- WHAT THIS IS NOT, against `second-implementation-is-not-a-second-opinion`. It does not
      # ---- recompute the driver's answer from the driver's inputs: it compares the driver's OUTPUT
      # ---- (the recorded `mode:`) against the driver's INPUT (the README at BASE), which is a
      # ---- provenance question and not an arithmetic one. The residual is the SHARED PARSE: both
      # ---- sides read the key with an awk of the same shape, so a parse that is wrong the same way
      # ---- twice agrees wrongly. That is smaller than the class it belongs to - a forged RECORD is
      # ---- still caught, which is the threat - and it is stated here rather than left to be found.
      recmode=$(fact_of "$f" mode)
      if [ -n "$recmode" ]; then
        dmode=$(printf '%s\n' "$bb" | awk '
          NR == 1 { next }
          /^---[[:space:]]*\r?$/ { exit }
          /^authorized-by:/ { v = $0; sub(/^authorized-by:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print v; exit }')
        [ -n "$dmode" ] || dmode=slug
        # ---- MEMBERSHIP first, then agreement, and they are two
        # ---- questions. This arm compared the two recorded values and had no opinion about
        # ---- whether either was LEGAL, so a README and a record carrying the SAME misspelling
        # ---- AGREED and passed - an assertion between two values one typo produced. Membership
        # ---- is the half that can see it, and it is why the agreement arm alone was not enough.
        case " $AUTH_MODES " in
          *" $recmode "*) ;;
          *) fail 19 "a run-state file records an authorization mode outside the kit's published set, so the discipline it names is one no kit member defines - legal values are $AUTH_MODES, recorded: $recmode" ;;
        esac
        case " $AUTH_MODES " in
          *" $dmode "*) ;;
          *) fail 19 "the build README at a run's recorded BASE declares an authorization mode outside the kit's published set, so the authorization names a discipline no kit member defines - legal values are $AUTH_MODES, declared: $dmode" ;;
        esac
        [ "$recmode" = "$dmode" ] || fail 19 "a run-state file records an authorization mode the build README at its own recorded BASE does not declare, so the discipline the run says bound it is not the one its authorization asked for: $recmode against $dmode"
        # ---- the DECLARATION SEAM, second-opinioned the same way the
        # ---- mode is. The leg re-derives the binding from the same blob and compares it against
        # ---- what the run RECORDED - never reading the driver's answer, which would confirm it
        # ---- rather than check it. Scoped to recipe runs because no other mode has a binding.
        if [ "$dmode" = recipe ]; then
          dpb=$(printf '%s\n' "$bb" | awk '
            NR == 1 { next }
            /^---[[:space:]]*\r?$/ { exit }
            /^playbook:/ { v = $0; sub(/^playbook:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print v; exit }')
          dn=$(printf '%s\n' "$bb" | awk '
            NR == 1 { next }
            /^---[[:space:]]*\r?$/ { exit }
            /^pieces:/ { v = $0; sub(/^pieces:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print v; exit }')
          recpb=$(fact_of "$f" playbook)
          recn=$(fact_of "$f" pieces)
          [ "$recpb" = "$dpb" ] || fail 19 "a run-state file records a playbook the build README at its own recorded BASE does not name, so the instructions the run says bound it are not the ones its authorization pointed at - recorded against declared follow: $recpb against $dpb"
          [ "$recn" = "$dn" ] || fail 19 "a run-state file records a piece count the build README at its own recorded BASE does not declare, so the number the run will be measured against is not the number it was asked for - recorded against declared follow: $recn against $dn"
        fi
      fi
    else
      fail 13 "no build README at a run's recorded BASE, so nothing committed before that run branched authorizes it: $rb in $bre"
    fi
  fi

  # ---- 11: the landing rule, checked where the record is. A run that wrote the bypass flag into its
  # ---- own state file is a run that considered using it.
  if [ -n "$BYPASS_BAN" ] && grep -qF -- "$BYPASS_BAN" "$f"; then
    fail 11 "a run-state file names the declared bypass flag, and bypassing the lander discards the whole bar the mandate leaned on: $BYPASS_BAN in $f"
  fi
  # ---- 17: a parked WAIVER names a declared handle, carries a reason, and was in the run-state
  # ---- file's FIRST committed blob. Unit 3 refuses a bad waiver at the moment of writing; this is
  # ---- the SECOND OPINION over what actually landed.
  # ----
  # ---- Only the waiver kind is joined. `park()` writes every declared kind, and the others
  # ---- legitimately arrive late — an `override` at `--close`, an `abort` reason later still, a
  # ---- `proposal` at any point at all — so joining them to the first blob would red every honest
  # ---- run. The waiver's whole claim is that
  # ---- it was taken at preflight, which is exactly why the join means something on it alone.
  # ----
  # ---- HONEST LIMIT, in source rather than in a document read at a different time (check 13's
  # ---- precedent): run locally this proves little, because the run writes BOTH sides — it can
  # ---- commit a waiver at pass 4 and the blob it is compared against is one it also authored.
  # ---- What changes is that the same leg re-run in a clone the run never touched now has something
  # ---- to catch here. This is not an authorization verdict and does not claim to be.
  while IFS= read -r wl; do
    [ -n "$wl" ] || continue
    # Free text LAST, so nothing after the reason is ever read: a reason that could contain the
    # separator would make this parse ambiguous, which is why unit 3 refuses a newline in one.
    wh=${wl#* waiver · item }; wh=${wh%% · reason *}
    wr=${wl#* · reason }
    case " $PHASES_TERMINAL " in *" $ph "*) ;;
      *) case " $DIRECTIVES_CORE $DIRECTIVES_EXTRA " in
           *" $wh:"*) ;;
           *) fail 17 "a parked waiver names a handle outside the effective directive set, so the record claims a relaxation of a rule no verb would have accepted: $wh in $f" ;;
         esac ;;
    esac
    [ -n "$wr" ] \
      || fail 17 "a parked waiver carries an empty reason, and a waiver recording no reason is indistinguishable from one nobody meant: $wh in $f"
    # --diff-filter=A with `tail -1` takes the OLDEST add, so a file deleted and re-added is still
    # judged against its original commit. Rename following is off on purpose: this leg selects its
    # population at an exact path, so a renamed run-state file is a different file to every check.
    # SILENT when the file has no committed blob at all — that is the honest preflight-to-first-
    # commit window, and reddening it would red a correct run with nobody present to read it.
    wfirst=$(GIT log --diff-filter=A --format=%H -- "$f" 2>/dev/null | tail -1)
    if [ -n "$wfirst" ]; then
      GIT show "$wfirst:$f" 2>/dev/null | grep -qF -- "$wl" \
        || fail 17 "a parked waiver line is absent from the run-state file's FIRST committed blob, so it was appended after the record was created and the claim that the owner took it at preflight is not what landed: $wh in $f"
    fi
  done <<WAIVERS
$(tr -d '' < "$f" 2>/dev/null | grep -E '^[0-9][0-9-]*T[0-9:]*Z waiver · item [^ ]* · reason ' || true)
WAIVERS
done <<EOF
$RUNS
EOF

# ---- 7: at most ONE non-terminal run-state file, or "the run" is not well-defined and anything
# ---- keying on it must either OR the phases together or pick one arbitrarily.
[ "$nlive" -le 1 ] || fail 7 "more than one run-state file is non-terminal, so 'the run' is not well-defined for anything keyed on it:$live"

# ---- 10: the kit ships what this repo runs. ONE pair. The comparison is written here rather than
# ---- borrowed from the memory-tree harness because each kit is copy-installed standalone and an
# ---- adopter may hold one and not the other; the normalisation is copied deliberately.
# ----
# ---- WHAT THIS CHECK DOES NOT DO, stated here because the omission has cost real defects. It compares
# ---- the two COPIES to each other. It says nothing about whether either one is TRUE. A sentence that
# ---- is wrong in both halves is green, forever, and three defects in that document survived exactly
# ---- that way: a Definition-of-Done cell describing a comparison the driver never makes, an override
# ---- rule stated only at run start, and an acceptance criterion that was never met at the close it was
# ---- claimed at. A parity leg is a copy check; the only thing that grades a sentence against the code
# ---- is a reader, and a check whose header does not say so reads as a semantic guarantee to everybody
# ---- who did not write it.
SHIP="$HERE/PROTOCOL.template.md"
LIVEDOC="$M/guides/UNATTENDED-PROTOCOL.md"
KITREL=${HERE#"$(cd "$ROOT" && pwd)"/}
PREFIX=${KITREL%/*}; [ "$PREFIX" = "$KITREL" ] && PREFIX="" || PREFIX="$PREFIX/"
if [ -f "$SHIP" ] && [ -f "$LIVEDOC" ]; then
  if [ -n "$PREFIX" ]; then nl=$(sed -e 's/\r$//' -e "s|$PREFIX||g" "$LIVEDOC"); else nl=$(sed -e 's/\r$//' "$LIVEDOC"); fi
  ns=$(sed -e 's/\r$//' "$SHIP")
  if [ "$nl" != "$ns" ]; then
    fail 10 "the shipped protocol and this repo's installed copy have drifted, so the kit ships something other than what it runs on: $SHIP vs $LIVEDOC"
    diff <(printf '%s\n' "$nl") <(printf '%s\n' "$ns") | head -10 | sed 's/^/    /'
  fi
elif [ ! -f "$SHIP" ] || [ ! -f "$LIVEDOC" ]; then
  fail 10 "one half of the protocol pair is missing, and a parity check with one file is a check that cannot fail: $SHIP / $LIVEDOC"
fi

# ---- 16: the INSTALLED protocol describes the rotation it is the rules for. Check 10 above cannot
# ---- see this: it is a byte-diff of the pair, and it is green whatever BOTH of them say. A rotation
# ---- shipped with a protocol that does not name the archive grammar is a mechanism an operator
# ---- meets for the first time in a directory listing.
if [ -f "$LIVEDOC" ] && ! grep -qF 'RUN.<phase>.<blob8>.md' "$LIVEDOC"; then
  fail 16 "the installed protocol does not spell the archive filename grammar 'RUN.<phase>.<blob8>.md', so the rules a run is measured against do not describe what --preflight does to a finished record: $LIVEDOC"
fi

# ---- 22: EVERY DECLARED CONF KEY IS DOCUMENTED, and every documented key is real. Joined in BOTH
# ---- directions against section 8's table, which the protocol calls BINDING. Three keys this kit
# ---- added reached the tree undocumented, one of them MANDATORY: `HALT_FLOOR` reds this leg when
# ---- undeclared, so an adopter configuring from the contract got a red bar naming a key the
# ---- contract never mentioned. Check 10 above cannot see it — it is a byte-diff of the pair, and
# ---- both copies were identically incomplete, which is the whole limitation its own header states.
# ----
# ---- WHAT THIS DOES NOT CHECK: that a row DESCRIBES its key correctly. It grades presence of the
# ---- key name in the table region, nothing more. A row whose prose is wrong is green here, and only
# ---- a reader catches that.
EXAMPLE_CONF="$HERE/.unattended.conf.example"
# A MISSING EXAMPLE IS A REFUSAL, not a skip. Guarding the whole check on `[ -f ]` made it vanish
# silently wherever the kit ships without its example - which is exactly where a documentation join
# is worth most - and a check that says nothing is indistinguishable from a check that passed. The
# example is a tracked kit file, so its absence is a broken install rather than a configuration.
if [ ! -f "$EXAMPLE_CONF" ]; then
  fail 22 "the kit ships no .unattended.conf.example, so the key table below can be joined against nothing and this check would pass by grading an empty set: $EXAMPLE_CONF"
elif [ -f "$LIVEDOC" ]; then
  # SCOPED TO SECTION 8's OWN REGION. Read over the whole file it also collects the phase
  # vocabulary, whose table has the same row shape - eleven phase names arriving as "documented
  # but declared nowhere" is a checker grading the wrong population, and muting them would take an
  # exclusion list that then hides a real dead key.
  sec8=$(awk '/^## 8[.] /{f=1;next} f&&/^## /{f=0} f' "$LIVEDOC")
  # THE FIRST TABLE CELL, not the whole section. The extractor read every backticked ALL-CAPS token in
  # section 8, so a PROSE mention of a phase name - main's `LANDED` - entered the key set as a phantom
  # and red this leg on the merged tree. Neither parent had both the prose and the check. Reading the
  # key column keeps the `·`-joined KEEPALIVE_CREATE/KEEPALIVE_DELETE row, which yields both keys.
  doc_keys=$(printf '%s\n' "$sec8" | awk -F'|' 'NF>2 {print $2}' | grep -oE '`[A-Z_]+`' | tr -d '`' | sort -u)
  # THE KIT'S EXAMPLE CONF IS THE REVERSE POPULATION, not the adopting project's. A project declares
  # the keys it needs and leaves the optional ones out, so "documented but not declared here" is the
  # NORMAL state of any real conf - graded against one, this check red six keys on a conforming
  # fixture tree, which is a checker measuring the wrong set rather than a repo with a fault. The
  # example is the kit's own full declaration and is what makes the reverse direction meaningful:
  # a documented key absent from it is a row describing something no adopter can copy.
  ex_keys=$(grep -oE '^[A-Z_]+=' "$EXAMPLE_CONF" | tr -d '=' | sort -u)
  undocumented=$(comm -23 <(printf '%s\n' "$ex_keys") <(printf '%s\n' "$doc_keys") | tr '\n' ' ')
  phantom=$(comm -13 <(printf '%s\n' "$ex_keys") <(printf '%s\n' "$doc_keys") | tr '\n' ' ')
  # ...and the ADOPTING project may declare nothing the table does not carry. One direction only,
  # because an optional key it never sets is not a fault.
  if [ -f "$ROOT/.unattended.conf" ]; then
    proj_extra=$(comm -23 <(grep -oE '^[A-Z_]+=' "$ROOT/.unattended.conf" | tr -d '=' | sort -u) <(printf '%s\n' "$doc_keys") | tr '\n' ' ')
  else
    proj_extra=""
  fi
  if [ -n "$(printf '%s' "$undocumented$phantom$proj_extra" | tr -d '[:space:]')" ]; then
    fail 22 "the protocol's binding key table and the declared conf disagree, so a key is either configurable and undocumented or documented and dead. undocumented in the protocol: ${undocumented:-none} | documented but in no example: ${phantom:-none} | set by this project and undocumented: ${proj_extra:-none}"
  fi
fi

# ---- 12: the kickoff engine's hand-back. BLANK KICKOFF_ENGINE turns this off — an adopter may not
# ---- use the kickoff skill at all. This is the one check that reads a file outside the kit, and it
# ---- exists because nothing else does: the manifest ratchet watches the project layer, and the
# ---- coverage gate enumerates the skill's PATH, so the engine's TEXT was read by no leg.
if [ -n "$KICKOFF_ENGINE" ]; then
  if [ ! -f "$KICKOFF_ENGINE" ]; then
    fail 12 "KICKOFF_ENGINE names a file that does not exist, so the hand-back check reads nothing and passes: $KICKOFF_ENGINE"
  else
    # CR-STRIPPED, and not because today's patterns need it. Every assertion below happens to match
    # mid-line, so a CRLF worktree passes them by luck rather than by design — and the engine is NOT
    # `eol=lf`-pinned repo-wide, so CRLF here is the normal state of a linked worktree. The first
    # pattern anchored to a line END would break silently on the node that wrote it. Strip once.
    eng=$(tr -d '\r' < "$KICKOFF_ENGINE")
    grep -qF 'Step 5b' <<<"$eng" \
      || fail 12 "the kickoff engine declares no unattended hand-back, so a mandated run still halts at the READY card with nobody to answer it: $KICKOFF_ENGINE"
    # BOTH DIRECTIONS. The hand-back is the exception; the stop is the default, and a change that
    # deleted the stop would make every ATTENDED kickoff run on without asking. The literal prompt
    # string is asserted, not the section heading — a heading survives a gutted body.
    grep -qF "Ready — say go and I'll start, or adjust any field." <<<"$eng" \
      || fail 12 "the kickoff engine no longer carries the READY prompt string, so the DEFAULT stop is gone and every attended kickoff would run on unasked: $KICKOFF_ENGINE"
    if [ -n "$KICKOFF_EXITS" ]; then
      nex=$(grep -cE '^[0-9]+\. \*\*Step ' <<<"$eng" || true)
      [ "$nex" -ge "$KICKOFF_EXITS" ] \
        || fail 12 "the kickoff engine enumerates fewer interactive exits than the floor, and a dropped exit is a place an unattended run silently regains to stop: $nex against $KICKOFF_EXITS"
    fi
  fi
fi


# ---- 16: the DIRECTIVE REGISTRY, joined to the table an agent actually reads. Three arms.
# ----
# ---- Arm A is a SECOND OPINION, not a recomputation. The driver's constant and the Skill's
# ---- hand-authored table are two different artifacts in two different languages; joining them
# ---- catches a handle added to one and forgotten in the other, which is the drift this build's
# ---- whole pointer-not-copy design depends on not happening. A generator would make the two agree
# ---- by construction and check nothing.
tmpl="$HERE/SKILL.template.md"
# Bound BEFORE either guard, because arm B reads it from outside the branch that used to assign it.
# A template present but carrying no readable row left `core` unset, and under `set -u` arm B then
# died on it — so the refusal for an unreadable table took arm C and this leg's own exit code down
# with it, reporting one problem where there were two.
# TOOL-cSettledDocket-2: the EFFECTIVE set, core plus whatever the project declared. `--waive` has
# always accepted an extra handle — the driver composes both — while this join covered CORE alone,
# so an extra was waivable by a verb and invisible to the agent, and the project could not fix that
# by adding a table row because the Skill is rendered from a kit template. It has a row source now.
# TOOL-aPromptedMandate-4 - a registry entry is now `<handle>:<section>[:<scope>]`, and everything
# below consumes the TWO-field form: arm A comms `core` against the table's `handle:M<n>` pairs, and
# arm B resolves the section as ${pair#*:}. Fed whole entries, both read `M12:prompt` as a section
# and red on a CORRECT implementation - measured, four refusals, before this split existed.
#
# ONE splitter, here, rather than one per consumer. `corescope` is built from the CORE set alone: a
# project's DIRECTIVES_EXTRA_TABLE rows are hand-authored and carry no scope column, and the join
# below must not red an adopter for a column the kit never asked them to write.
core=""; corescope=""
for _de in $DIRECTIVES_CORE $DIRECTIVES_EXTRA; do
  _dh=${_de%%:*}; _dr=${_de#*:}; _ds=${_dr%%:*}; _dc=${_dr#*:}
  [ "$_dc" = "$_dr" ] && _dc=all
  core="$core$_dh:$_ds
"
done
for _de in $DIRECTIVES_CORE; do
  _dh=${_de%%:*}; _dr=${_de#*:}; _dc=${_dr#*:}
  [ "$_dc" = "$_dr" ] && _dc=all
  corescope="$corescope$_dh:$_dc
"
done
core=$(printf '%s' "$core" | grep . | sort -u)
corescope=$(printf '%s' "$corescope" | grep . | sort -u)
if [ ! -f "$tmpl" ]; then
  fail 16 "the kit ships no SKILL.template.md, so the directive table an agent reads cannot be joined to the registry it is supposed to mirror; a shipped kit always has one, so this is a broken install rather than a project choice"
else
  # The handle must be the row's FIRST cell; the carrier is its M<n> token wherever it sits, so the
  # M<n> column may move but the handle column may not. A `tbl` sed used to sit here duplicating this
  # awk's row filter in BRE — non-empty in exactly the same cases, readable only by the emptiness
  # test below. Two grammars over one row shape, and no input could tell them apart, so one is gone.
  tblpairs=$(tr -d '\r' < "$tmpl" | awk -F'|' '
    /^[[:space:]]*\|[[:space:]]*`[a-z][a-z-]*`[[:space:]]*\|/ {
      h = ""; c = ""; n = 0
      for (i = 2; i <= NF; i++) {
        cell = $i
        gsub(/^[[:space:]]+|[[:space:]]+$/, "", cell)
        if (h == "" && cell ~ /^`[a-z][a-z-]*`$/) { gsub(/`/, "", cell); h = cell; continue }
        if (cell ~ /^M[0-9]+$/) { c = cell; n++ }
      }
      if (h != "" && n == 1) print h ":" c
      else if (h != "" && n != 1) print h ":AMBIGUOUS"
    }' | sort -u)
  # TOOL-cSettledDocket-2 — the PROJECT's own rows, if it declared a source. Same row grammar as the
  # kit table, read with the same awk, so the two cannot disagree about what a row IS.
  #
  # A declared path that does not EXIST is a named refusal, never an empty union: silent, every
  # project-declared directive would land back on the "declared and absent from the table" branch
  # with nothing saying why. Undeclared is the empty set, which is every adopter today.
  if [ -n "$DIRECTIVES_EXTRA_TABLE" ]; then
    if [ ! -f "$ROOT/$DIRECTIVES_EXTRA_TABLE" ]; then
      fail 16 "DIRECTIVES_EXTRA_TABLE names a file that does not exist, so every project-declared directive would read as absent from the table it is supposed to be in: $DIRECTIVES_EXTRA_TABLE"
    else
      xtra=$(tr -d '\r' < "$ROOT/$DIRECTIVES_EXTRA_TABLE" | awk -F'|' '
        /^[[:space:]]*\|[[:space:]]*`[a-z][a-z-]*`[[:space:]]*\|/ {
          h = ""; c = ""; nm = 0
          for (i = 2; i <= NF; i++) {
            cell = $i
            gsub(/^[[:space:]]+|[[:space:]]+$/, "", cell)
            if (h == "" && cell ~ /^`[a-z][a-z-]*`$/) { gsub(/`/, "", cell); h = cell; continue }
            if (cell ~ /^M[0-9]+$/) { c = cell; nm++ }
          }
          if (h != "" && nm == 1) print h ":" c
          else if (h != "" && nm != 1) print h ":AMBIGUOUS"
        }' | sort -u)
      if [ -z "$xtra" ]; then
        fail 16 "DIRECTIVES_EXTRA_TABLE names a file carrying no readable directive row, so the project declared a row source and the union it contributes is empty: $DIRECTIVES_EXTRA_TABLE"
      else
        tblpairs=$(printf '%s\n%s\n' "$tblpairs" "$xtra" | grep . | sort -u)
      fi
    fi
  fi
  if [ -z "$tblpairs" ]; then
    fail 16 "the Skill template carries no directive table row this leg can read, so arm A would join the registry against nothing and pass by finding nothing; the row shape it looks for is a leading pipe then a backticked lowercase handle"
  else
    case "$tblpairs" in *":AMBIGUOUS"*)
      fail 16 "a directive row cites more than one build-method section, so the join has no single answer to read for that handle" ;;
    esac
    only_reg=$(comm -23 <(printf '%s\n' "$core") <(printf '%s\n' "$tblpairs"))
    only_tbl=$(comm -13 <(printf '%s\n' "$core") <(printf '%s\n' "$tblpairs"))
    [ -z "$only_reg" ] || fail 16 "a directive is declared in the registry and absent from the Skill's table, so the agent that reads the table is bound by a set it was never shown: $only_reg"
    [ -z "$only_tbl" ] || fail 16 "the Skill's table names a directive the registry does not declare, so the agent is told about a handle no verb will accept: $only_tbl"
    # TOOL-aPromptedMandate-6 fold, review L2 - the scope is KIT-OWNED, and two carriers say so. It
    # was enforceable only by convention: `scope_of` composes core PLUS extra, so a project could
    # declare `house-style:M9:prompt` and select a binding the protocol says it may not. Refused here
    # rather than silently honoured, which keeps the documents true.
    for _xe in $DIRECTIVES_EXTRA; do
      case "${_xe#*:}" in *:*)
        fail 16 "a project-declared directive carries a SCOPE, and the scope is kit-owned because a project-selectable one is a narrowing of the core wearing another name: $_xe" ;;
      esac
    done
    # TOOL-aPromptedMandate-4 - the SCOPE column, joined to the registry's third field. Scoped to the
    # KIT table's rows: the handle set compared is the CORE set, so a project's own extra rows are
    # outside this arm and an adopter is never redded for a column the kit did not ask them to write.
    #
    # ANTI-VACUITY FIRST. If the column is absent from every row the extraction is empty, and an
    # empty-against-empty comparison is green - which is the shape this repo reds elsewhere by name.
    # The guard is ordered ahead of the comparison for the reason arm A's and D's are.
    tblscope=$(tr -d '\r' < "$tmpl" | awk -F'|' -v legal="$AUTH_SCOPES" '
      /^[[:space:]]*\|[[:space:]]*`[a-z][a-z-]*`[[:space:]]*\|/ {
        h = ""; sc = ""
        for (i = 2; i <= NF; i++) {
          cell = $i
          gsub(/^[[:space:]]+|[[:space:]]+$/, "", cell)
          if (h == "" && cell ~ /^`[a-z][a-z-]*`$/) { gsub(/`/, "", cell); h = cell; continue }
          if (index(" " legal " ", " " cell " ")) sc = cell
        }
        if (h != "" && sc != "") print h ":" sc
      }' | sort -u)
    if [ -z "$tblscope" ]; then
      fail 16 "the Skill's directive table carries no scope cell this leg can read, so the scope join would compare the registry against nothing and pass by finding nothing; the cell it looks for holds one of: $AUTH_SCOPES"
    else
      # ONE branch, not a comm PAIR. Measured: changing a single scope cell puts the same handle in
      # BOTH differences, so an only-in-table second branch cannot fire ALONE - it is reachable only
      # alongside this one, or alongside arm A which already covers the handle set. A branch no
      # fixture can isolate is a branch whose arm proves nothing, so there is one.
      _cs=$(printf '%s' "$corescope" | tr '\n' ' ')
      _ts=$(printf '%s' "$tblscope" | tr '\n' ' ')
      [ "$corescope" = "$tblscope" ] || fail 16 "the directive scopes the registry declares are not the scopes the Skill's table shows, so the agent is told which runs a rule binds by a table that disagrees with the verb enforcing it: $_cs against $_ts"
    fi
  fi
  # Arm B: every cited section RESOLVES. SILENT when the carrier is absent — the leg grades the
  # TREE and an adopter may install this kit without the memory-tree one; the DRIVER is what grades
  # the RUN, and unit 4's refusal is where a missing carrier actually stops something.
  if [ -f "$M/guides/BUILD-METHOD.md" ]; then
    for pair in $core; do
      sec=${pair#*:}
      grep -qE "^## $sec( |\$)" "$M/guides/BUILD-METHOD.md" \
        || fail 16 "a directive points at a build-method section that does not exist, so the handle names a rule no reader can reach: $pair"
    done
  fi
fi
# Arm C: the floor. Mirrors CORE_FLOOR's two branches — undeclared and malformed are both refusals,
# because either one leaves the pin unenforced while the conf still looks configured.
# TOOL-aPromptedMandate-6 fold, review H1 - a floor BELOW the kit's own core count is SLACK BY
# CONSTRUCTION and cannot fire on the deletion it exists to catch. This build shipped exactly that:
# the bump to 13 was reverted by a `git checkout --` during an unrelated probe, and arm C passed
# because it only ever asked whether the count met the floor, never whether the floor met the kit.
_ndc=$(printf '%s\n' $DIRECTIVES_CORE | grep -c . || true)
if [ -n "$DIRECTIVES_FLOOR" ] && [ "$DIRECTIVES_FLOOR" -lt "$_ndc" ] 2>/dev/null; then
  fail 16 "DIRECTIVES_FLOOR is declared below the kit's own core directive count, so the shrink-only pin is slack by construction and a deleted core handle would pass it: $DIRECTIVES_FLOOR against $_ndc"
fi
if [ -z "$DIRECTIVES_FLOOR" ]; then
  fail 16 "DIRECTIVES_FLOOR is undeclared in .unattended.conf, and with no floor a deleted directive is indistinguishable from a set that never had one"
else
  case "$DIRECTIVES_FLOOR" in
    ''|*[!0-9]*) fail 16 "DIRECTIVES_FLOOR is not a plain integer, so the shrink-only pin on the directive set is unenforced while the conf still looks configured: $DIRECTIVES_FLOOR" ;;
    *) ndir=$(printf '%s\n' $DIRECTIVES_CORE | grep -c . || true)
       [ "$ndir" -ge "$DIRECTIVES_FLOOR" ] \
         || fail 16 "the kit's CORE directive set has shrunk below its floor, and deleting a directive is a silent, reason-free relaxation of everything keyed on it: $ndir against $DIRECTIVES_FLOOR" ;;
  esac
fi
# Arms D and E: the CONTRACT's own two tables joined to the constants the driver enforces. Same
# shape as arm A one document over — a shell constant against a hand-authored markdown table — and
# the same reason: the protocol is what an outside reader is told, and a contract that publishes a
# vocabulary the kit does not use is worse than one that publishes none.
# The SHIPPED template is the side read. Check 10 already asserts the installed copy equals it after
# prefix substitution, so reading both here would be a second answer to a question that check owns.
proto="$HERE/PROTOCOL.template.md"
if [ -f "$proto" ]; then
  # §3's run-order PARAGRAPH, not the whole file. Measured: the same pattern over the document also
  # returns `LANDER`, which is a conf key — the paragraph scope is load-bearing, not tidy.
  pph=$(tr -d '\r' < "$proto" | awk '
    /in run order:$/ { f = 1; next }
    f && /^$/        { if (seen) exit; next }
    f                { seen = 1; print }' | grep -oE '`[A-Z][A-Z_]*`' | tr -d '`' | sort -u)
  # An EMPTY extraction is its own NAMED refusal, as arm A's is: a prose anchor that gets reworded
  # otherwise empties the comparison and the join passes by finding nothing.
  if [ -z "$pph" ]; then
    fail 16 "the protocol's run-order paragraph yields no phase token, so the phase join would compare the driver's vocabulary against nothing and pass by finding nothing; the anchor is the line ending 'in run order:'"
  else
    pcore=$(printf '%s\n' $PHASES_CORE | sort -u)
    pd1=$(comm -23 <(printf '%s\n' "$pcore") <(printf '%s\n' "$pph"))
    pd2=$(comm -13 <(printf '%s\n' "$pcore") <(printf '%s\n' "$pph"))
    [ -z "$pd1" ] || fail 16 "a CORE phase is enforced by the driver and absent from the protocol's run-order list, so the contract publishes a vocabulary the kit does not use: $pd1"
    [ -z "$pd2" ] || fail 16 "the protocol's run-order list names a phase the driver does not carry, so the contract promises a position no run can ever occupy: $pd2"
    # TOOL-aPromptedMandate-2 - ...and the PASS-KIND subset, joined the same way. Adding a phase and
    # calling it a pass kind is a claim about the build method, and the row join above cannot see it:
    # the rows were right and only the prose was wrong is exactly how the DoD count sentence went
    # stale in both copies while its leg stayed green.
    ppk=$(tr -d '\r' < "$proto" | awk '
      /PASS kinds:$/ { f = 1; next }
      f && /^$/      { if (seen) exit; next }
      f              { seen = 1; print }' | grep -oE '`[A-Z][A-Z_]*`' | tr -d '`' | sort -u)
    if [ -z "$ppk" ]; then
      fail 16 "the protocol names no phase as a build-method pass kind, so the pass-kind join would compare the driver's subset against nothing and pass by finding nothing; the anchor is the line ending 'PASS kinds:'"
    else
      # TOOL-aPromptedMandate-6 fold, review L3 - the subset relation, never asserted. A pass-kind
    # naming a phase no run can occupy publishes a position the vocabulary does not carry, and the
    # both-ways join to the protocol cannot see it: both sides would agree on the same wrong token.
    for _pk in $PHASES_PASSKIND; do
      case " $PHASES_CORE " in *" $_pk "*) ;;
        *) fail 16 "a phase is published as a build-method pass kind and is not in the core vocabulary, so the contract names a position no run can ever occupy: $_pk" ;;
      esac
    done
    pkcore=$(printf '%s\n' $PHASES_PASSKIND | sort -u)
      kd1=$(comm -23 <(printf '%s\n' "$pkcore") <(printf '%s\n' "$ppk"))
      kd2=$(comm -13 <(printf '%s\n' "$pkcore") <(printf '%s\n' "$ppk"))
      [ -z "$kd1" ] || fail 16 "the driver publishes a phase as a build-method pass kind and the protocol does not list it, so the contract understates which positions the method names: $kd1"
      [ -z "$kd2" ] || fail 16 "the protocol lists a phase as a build-method pass kind that the driver does not publish as one, so the contract claims the method names a position it does not: $kd2"
    fi
  fi
  # Item NAMES only. The checker column is deliberately not joined: measured today three cells read
  # `machine, PRE-LANDING` or `agent-attested` against the constant's `machine`/`agent`, and those
  # spellings say something true the constant has no room for. Joining them would need a
  # normalisation table, which is a third spelling of a two-value fact.
  pdod=$(tr -d '\r' < "$proto" | sed -n 's/^| `\([a-z][a-z-]*\)` |.*/\1/p' | sort -u)
  if [ -z "$pdod" ]; then
    fail 16 "the protocol's Definition-of-Done table yields no item row, so the DoD join would compare the driver's set against nothing and pass by finding nothing"
  else
    dcore=$(printf '%s\n' $DOD_CORE | sed 's/:.*//' | sort -u)
    ed1=$(comm -23 <(printf '%s\n' "$dcore") <(printf '%s\n' "$pdod"))
    ed2=$(comm -13 <(printf '%s\n' "$dcore") <(printf '%s\n' "$pdod"))
    [ -z "$ed1" ] || fail 16 "a CORE Definition-of-Done item is enforced by --close and absent from the protocol's table, so a run is blocked by an item the contract never told anyone about: $ed1"
    [ -z "$ed2" ] || fail 16 "the protocol's Definition-of-Done table names an item the driver does not carry, so the contract publishes a gate nothing evaluates: $ed2"
    # ...and the COUNT SENTENCE above the table, joined to the same set. This is the finding that
    # earned the arm: the table grew to eight rows while the sentence directly above it still said
    # six, in BOTH copies, so the parity leg was green over a document contradicting itself. A row
    # join cannot see a miscount, because the rows were right and only the prose was wrong.
    cw=$(tr -d '\r' < "$proto" | sed -n 's/^\([A-Za-z]*\) kit-owned core items\..*/\1/p' | head -1)
    if [ -z "$cw" ]; then
      fail 16 "the protocol states no count of kit-owned core Definition-of-Done items, so the sentence that summarises the table cannot be joined to the table or to the driver"
    else
      case "$(printf '%s' "$cw" | tr 'A-Z' 'a-z')" in
        one) cn=1 ;; two) cn=2 ;; three) cn=3 ;; four) cn=4 ;; five) cn=5 ;; six) cn=6 ;;
        seven) cn=7 ;; eight) cn=8 ;; nine) cn=9 ;; ten) cn=10 ;; eleven) cn=11 ;; twelve) cn=12 ;;
        *) cn=-1 ;;
      esac
      ndod=$(printf '%s\n' "$dcore" | grep -c . || true)
      [ "$cn" = "$ndod" ]         || fail 16 "the protocol's stated count of core Definition-of-Done items disagrees with the set the driver enforces, and that sentence sits directly above the table it miscounts: says '$cw', driver carries $ndod"
    fi
  fi
fi

# ---- 18: the kickoff step comes AFTER preflight in the Skill an agent reads. Invoked first,
# ---- /session-kickoff halts at its READY card, which under a mandate nobody is present to answer.
# ---- Two line numbers and a comparison — the shape region() already uses here and in the driver,
# ---- for the reason recorded there: a TRANSPOSED pair satisfies a count-only check, and the
# ---- driver's copy of that function truncated a file on exactly that.
# ---- Keyed on a non-blank KICKOFF_ENGINE, matching check 12: an adopter may not ship the kickoff
# ---- skill at all. ABSENCE IS A REFUSAL rather than the safe side, because a template that never
# ---- names kickoff and a template that names it too early read identically on any count.
# ---- It asserts the ORDER OF TWO LINES in a document and nothing more. Whether the sequence WORKS
# ---- is unexecuted and is carried as a residual in the build README, not implied away here.
if [ -n "$KICKOFF_ENGINE" ] && [ -f "$tmpl" ]; then
  # First match of each, so a template naming either twice is judged on the occurrence the agent
  # reads first. Anchored on the fenced invocation and the literal skill name — neither is a
  # heading, which a reword survives while gutting the body.
  pfl=$(awk '{ sub(/$/,"") } index($0, "unattended.sh --preflight") { print NR; exit }' "$tmpl")
  kol=$(awk '{ sub(/$/,"") } index($0, "/session-kickoff") { print NR; exit }' "$tmpl")
  if [ -z "$pfl" ]; then
    fail 18 "the Skill template names no --preflight invocation, so there is no anchor to order the kickoff step against and the sequence this check exists to hold is unstated: $tmpl"
  elif [ -z "$kol" ]; then
    fail 18 "the Skill template never names /session-kickoff while this project declares a kickoff engine, and a missing step reads exactly like a deadlocked one on any count-based check: $tmpl"
  elif [ "$kol" -lt "$pfl" ]; then
    fail 18 "the Skill template puts the kickoff step BEFORE --preflight, and kickoff invoked first halts at its READY card with nobody under a mandate to answer it: /session-kickoff at line $kol, --preflight at line $pfl in $tmpl"
  fi
fi
# ---- 22 runs in its OWN loop over the run population, NOT inside the BASE-blob block. That block
# ---- is entered only when the build README exists AT THE PINNED BASE, and a build folder created
# ---- after the run's BASE has no blob there — measured: the fixture's own run never reached the
# ---- check, and every arm read as green over a check that had not run. This one needs the RUN-STATE
# ---- file's own history and the working README, never the pinned BASE, so it has no business behind
# ---- that gate.
for f in $RUNS; do
  [ -f "$f" ] || continue
  case "$f" in *"/RUN.md") ;; *) continue ;; esac   # frozen retired records are not amendable
  ph=$(fact_of "$f" phase); case "$ph" in LANDED|ABORTED) continue ;; esac
  rb=$(fact_of "$f" base)
  bslug=${f#"$M/builds/"}; bslug=${bslug%%/*}
  bre="$M/builds/$bslug/README.md"
  [ -f "$bre" ] || continue
  # ---- 22: an AMENDMENT with no record. TOOL-dUnstalledConvoy-6.
  # ---- M3 delegates this build's own scope and M2 names the three acts, so the failure mode moved
  # ---- from STALLING to DRIFTING: a unit quietly retired because it was inconvenient, with
  # ---- nothing in the record saying so. This compares the roster the run was authorized for
  # ---- against the roster it is executing, and asks the run-state file to account for the
  # ---- difference.
  # ----
  # ---- WHAT IT CANNOT BUY. Both inputs are inside the run's reach — the run wrote the rows and
  # ---- the run made the edits. It catches the CHEAP failure, an amendment made with NO record.
  # ---- It does not catch a truthful-looking row attached to a different edit, which takes a
  # ---- deliberate lie. A green here is not proof an amendment was honest, and the two artifacts
  # ---- are produced by different acts at different times, which is the whole of why it is worth
  # ---- having anyway.
  # ----
  # ---- IT DOES NOT RE-IMPLEMENT THE REMOVAL REFUSAL. `check_authorization` refuses a narrowed id
  # ---- set and `authorization-reachable` has no override; a second copy here would recompute the
  # ---- driver's answer from the driver's inputs, which confirms rather than checks.
  # ----
  # ---- THE BASELINE IS THE COMMIT THE RUN ENTERED `BUILDING` AT, not the pinned BASE. A run that
  # ---- classifies a unit MISSING and authors its spec is doing what M2 MANDATES, and every such
  # ---- spec is absent at BASE — keying on BASE would red a run for obeying the method, and the
  # ---- prompt-authorized mode makes it sharper still, since such a run starts with an empty
  # ---- region. Using the REGION at that commit rather than per-id spec archaeology is equivalent
  # ---- here because hygiene check 9 refuses a stale index, so a spec committed by then is in the
  # ---- region by then; that dependency is the reason this shortcut is sound and is stated rather
  # ---- than assumed.
  # ONE DERIVATION, in lib-unattended.sh, called by the driver too. Deciding "what roster did this
  # run start with" separately in each is what made check 24 and check 48 unsatisfiable together:
  # this file asked whether a unit was in the BASELINE roster, and the driver asked whether it was
  # in the CURRENT one — a different question with a different answer, and a run whose roster grew
  # before anybody recorded it was wedged between the two. TOOL-dUnstalledConvoy-33.
  rs_why=""
  if ! rs_was=$(baseline_units "$f" "$bre" "${UNITS_REGION_CUTOFF:-}" "$rb"); then
    rs_why=$rs_was; rs_was=""
  fi
  if [ -n "$rs_why" ]; then
    report "check 24 skipped for $f — $rs_why"
  elif ! rs_now=$(region "$bre" '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null); then
    report "check 24 skipped for $f — the working build README does not carry exactly one well-formed units pair, so the executing roster cannot be read"
  else
    rs_rows=$(grep -F -- ' rescope · item ' "$f" 2>/dev/null || true)
    # ADDED ids: accounted for by an `add` naming it, OR a `supersede` naming it as the successor.
    # An `add` alone would red a correctly performed supersession, whose successor is present now
    # and absent then with no `add` row that the sibling verb would even accept.
    for rsid in $(printf '%s\n' "$rs_now" | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u); do
      id_in "$rs_was" "$rsid" && continue
      printf '%s\n' "$rs_rows" | grep -qE "item add $rsid( |\$)" && continue
      printf '%s\n' "$rs_rows" | grep -qE "item supersede [A-Za-z0-9-]+ -> $rsid( |\$)" && continue
      fail 24 "a unit is in the roster this run is executing and was not in the roster it entered BUILDING with, and no rescope row adds or supersedes into it, so the scope moved with nothing on the record saying so: $rsid in $f"
    done
    # RETIRED units: a status that is WONTDO now and was not then owes a retire or a supersede.
    for rsid in $(printf '%s\n' "$rs_now" | grep -E '\| WONTDO \|' | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u); do
      id_rows "$rs_was" "$rsid" | grep -q '| WONTDO |' && continue
      printf '%s\n' "$rs_rows" | grep -qE "item (retire|supersede) $rsid( |\$)" && continue
      fail 24 "a unit went WONTDO after this run entered BUILDING and no rescope row retires or supersedes it, so a unit was dropped with nothing on the record saying so: $rsid in $f"
    done
    # A SUPERSESSION THAT NEVER LANDED ITS REPLACEMENT is a retirement wearing a better name.
    # A `for`, never a `| while`: `fail` in a pipeline subshell sets a status the parent never
    # sees, so the leg reports the violation and exits 0 — the shape this whole build is about.
    for rssucc in $(printf '%s\n' "$rs_rows" | grep -oE 'item supersede [A-Za-z0-9-]+ -> [A-Za-z0-9-]+' | awk '{print $NF}' | sort -u); do
        [ -n "$rssucc" ] || continue
        id_in "$rs_now" "$rssucc" && continue
        fail 24 "a rescope row supersedes into a successor the executing roster does not carry, so the replacement never landed and the row records a retirement wearing a better name: $rssucc in $f"
      done
  fi

done

# ---- 23: a DECLARED write set against what the pass actually committed. TOOL-dUnstalledConvoy-10.
# ---- The sibling verb records what a concurrently dispatched pass SAID it would write; this is the
# ---- half that can catch the declaration out. The two artifacts are produced by different acts at
# ---- different times, which is the whole of why the comparison is worth making.
# ----
# ---- WHAT IT CANNOT BUY: both artifacts are authored by the run — it wrote the rows and it made the
# ---- commits — so a run determined to hide a collision can simply declare the wider set up front.
# ---- That is a more expensive lie than the failure this catches, and this check does not claim to
# ---- reach it. A green row here is not proof two passes were disjoint.
# ----
# ---- THE JOIN is the unit id in the commit subject, which the build method already requires of every
# ---- pass commit for its own reasons. This check consumes that rule rather than inventing an
# ---- attribution mechanism, and refuses an ambiguous subject rather than guessing which pass a
# ---- commit belongs to.
# ----
# ---- THE WINDOW is the FIRST commit after the group anchor naming the unit, and nothing later. A
# ---- pass's own review fold or spec bump lands after its group has ended and is outside it by
# ---- construction; grading those would red an ordinary sequential fold with no in-band repair.
for f in $RUNS; do
  [ -f "$f" ] || continue
  case "$f" in *"/RUN.md") ;; *) continue ;; esac
  ph=$(fact_of "$f" phase); case "$ph" in LANDED|ABORTED) continue ;; esac
  # ONE ROW PER (anchor, unit), AND ITS PATHS ARE THE UNION OF EVERY ROW UNDER THAT KEY. The key
  # already carries the anchor, so rows at DIFFERENT anchors stay separate — they are different passes
  # with different windows. What changes is same-anchor rows: `row[k] = $0` overwrote, so a run that
  # took the driver's own published repair ("a pass that needs more paths declares again") had its
  # first declaration silently discarded and was reported against the second alone.
  dsrows=$(grep -F -- ' dispatch · item ' "$f" 2>/dev/null | awk '
      { k = $0; sub(/^.* dispatch · item /, "", k); sub(/ · reason .*$/, "", k)
        pth = $0; sub(/^.* · reason /, "", pth)
        pre = $0; sub(/ dispatch · item .*$/, "", pre)
        if (!(k in seen)) { seen[k] = 1; ord[++n] = k; head[k] = pre; paths[k] = pth }
        else {
          split(paths[k], have, " "); dup = 0
          split(pth, add, " ")
          for (a in add) { dup = 0
            for (h in have) if (have[h] == add[a]) dup = 1
            if (!dup) paths[k] = paths[k] " " add[a] }
        } }
      END { for (i = 1; i <= n; i++) { k = ord[i]
              print head[k] " dispatch · item " k " · reason " paths[k] } }' || true)
  if [ -z "$dsrows" ]; then
    report "check 23 skipped for $f — this run declared no concurrent dispatch, so there is no declaration to compare and a green verdict here would be coverage of nothing"
    continue
  fi
  while IFS= read -r dsrow; do
    [ -n "$dsrow" ] || continue
    dsitem=${dsrow#* dispatch · item }; dsitem=${dsitem%% · reason *}
    dsgrp=${dsitem%% *}; dsunit=${dsitem#* }
    dsdecl=${dsrow#* · reason }
    if ! GIT rev-parse --verify --quiet "$dsgrp^{commit}" >/dev/null 2>&1; then
      report "check 23 skipped for $dsunit in $f — the recorded group anchor does not resolve in this clone, so the commit window cannot be opened"
      continue
    fi
    if ! GIT merge-base --is-ancestor "$dsgrp" HEAD 2>/dev/null; then
      report "check 23 skipped for $dsunit in $f — the group anchor is not an ancestor of HEAD, so this clone does not carry the history the declaration was made against"
      continue
    fi
    # THE FIRST commit naming the unit, oldest-first, and nothing after it.
    # A RUN-STATE BOOKKEEPING COMMIT IS NOT A PASS COMMIT, and skipping it is not a convenience.
    # `--dispatch` STAGES the run-state file, so the run commits the declaration itself — and that
    # commit's subject names the unit, being about it. Without this skip the DECLARATION is read as
    # the pass's own commit, the subset test runs against a diff touching only the run-state file, and
    # the check reds on every correctly declared pass. Measured on this unit's own fixture.
    # THE KIT LIBRARY ANSWERS THIS, not a loop written here. The driver's condition 1 asks the same
    # question, and when the two were written separately the driver's copy omitted the run-state skip
    # below and closed every pass on its own declaration commit.
    # S3 — THE WINDOW'S UPPER BOUND. A unit legitimately owns several rows at several anchors, and
    # an unbounded window grades row one against row two's commit, which is another pass's work. The
    # bound is the unit's NEXT anchor by ancestry, and the window is (own, next] — inclusive at the
    # top, because `pass_commit` is exclusive at the bottom and a commit sitting exactly on the next
    # anchor must belong to exactly one of the two rows rather than to neither.
    dsanchors=$(printf '%s\n' "$dsrows" | while IFS= read -r _r; do
        [ -n "$_r" ] || continue
        _i=${_r#* dispatch · item }; _i=${_i%% · reason *}
        [ "${_i#* }" = "$dsunit" ] && printf '%s\n' "${_i%% *}"
      done)
    dstop=$(next_anchor "$dsgrp" "$dsanchors")
    [ -n "$dstop" ] || dstop=HEAD
    dshit=$(pass_commit "$dsgrp" "$dsunit" "$f" "$dstop" || true)
    if [ -z "$dshit" ]; then
      # NO COMMIT NAMES THE PASS. Legal when the pass produced no change - M6 says a pass that
      # changed nothing commits nothing. NOT legal when the declared paths moved anyway: that is the
      # declared work happening while the join is dodged, and it is the only reading of this state
      # that is a defect. Keyed on the PATHS and not on a subject naming no id at all, because the
      # latter reds on every witness commit a run makes between passes.
      dsmoved=""
      for dsp in $dsdecl; do
        # S4 — THE SAME UPPER BOUND. This scan asks whether a declared path moved while no commit
        # named the pass; unbounded it sees the NEXT pass's writes and reports them against this row.
        GIT log --format=%H "$dsgrp".."$dstop" -- "$dsp" 2>/dev/null | grep -q . && dsmoved="$dsmoved $dsp"
      done
      # ...and the run-state file is excluded from the OUTSIDE test too, for the same reason.
      if [ -n "$dsmoved" ]; then
        printf 'unattended: check 23 — a declared path of a dispatched pass moved inside its window while no commit names that pass, so the declared work happened and the only join this check has was dodged: %s wrote%s in %s\n' "$dsunit" "$dsmoved" "$f"
      else
        report "check 23 observed for $dsunit in $f — no commit names this pass and none of its declared paths moved, which is a pass that produced no change"
      fi
      continue
    fi
    # AMBIGUOUS ATTRIBUTION is a refusal, never a guess: a subset test over a commit that could
    # belong to either of two passes proves nothing about either.
    dsother=""
    while IFS= read -r dssib; do
      [ -n "$dssib" ] || continue
      dssitem=${dssib#* dispatch · item }; dssitem=${dssitem%% · reason *}
      dssunit=${dssitem#* }
      [ "$dssunit" = "$dsunit" ] && continue
      # ANCHORED, like every other id test in this file. Left as a substring, a group holding a
      # `-1` and a `-10` reports the pair as ambiguous on the `-1` commit and reds a correct run.
      id_in "$(GIT log -1 --format=%s "$dshit" 2>/dev/null)" "$dssunit" && dsother="$dssunit"
    done <<DSSIBS
$(printf '%s\n' "$dsrows" | grep -F -- " dispatch · item $dsgrp ")
DSSIBS
    if [ -n "$dsother" ]; then
      printf 'unattended: check 23 — one commit names two passes of the same dispatch group, so a subset test over it cannot say which pass wrote what and the attribution this comparison rests on is not available: %s and %s in %s\n' "$dsunit" "$dsother" "$f"
      continue
    fi
    # THE SUBSET TEST. Declaring MORE than you use is conservative and fine; writing outside the
    # declaration is the defect.
    dsout=""
    for dsq in $(GIT diff-tree --no-commit-id --name-only -r "$dshit" 2>/dev/null | grep -v -x -F "$f"); do
      dsok=0
      for dsp in $dsdecl; do
        # THROUGH THE LIBRARY, which normalises. A bare `case` graded the recorded spelling as a
        # literal, so a declaration the driver accepted as `work/sub/` matched nothing the commit
        # touched and redded this leg permanently, with narrowing refused and no in-band repair.
        covers "$dsp" "$dsq" && { dsok=1; break; }
      done
      [ "$dsok" = 1 ] || dsout="$dsout $dsq"
    done
    [ -z "$dsout" ] || printf 'unattended: check 23 — a dispatched pass committed a path outside the set it declared before dispatch: %s at %s wrote%s in %s\n' "$dsunit" "$dshit" "$dsout" "$f"
  done <<DSROWS
$dsrows
DSROWS
done

# ---- 21 (TOOL-aBoundedVerdict-11 S5): every tracked build README carries EXACTLY ONE well-formed
# ---- `gen:build-units` pair. The driver reads its unit list from that region for four questions -
# ---- the authorization scope, `--plan`'s roster join, `--status`'s next unit and `build-complete`'s
# ---- terms - so a README without it is a build no run can close, and one with a duplicated or
# ---- transposed pair is worse: `region` conflates absent with malformed.
# ----
# ---- POPULATION IS DERIVED, never listed: `git ls-files` over the memory root's build READMEs. A
# ---- hand-kept list goes stale the first time a build folder lands. This check exists because
# ---- nothing gated the markers' PRESENCE - only their well-formedness once present - which another
# ---- node reported independently from a live run.
# ----
# ---- That report named the AUTHORED `roster:units` pair, and S5's answer was to make the GENERATED
# ---- pair mandatory instead - so this gates a DIFFERENT pair from the one reported missing, and
# ---- reading it as the report's own fix is wrong. The report is a live row in the tooling backlog
# ---- shard, filed from the aPacedTurnstile run. Its id is deliberately NOT spelled here: it now
# ---- names a non-terminal spec, and drift-audit's oracle reads a shipped-source citation of one as
# ---- proof that its work shipped. Re-adding the id reds `drift-audit records` on the next bar.
# ----
# ---- The generator CREATES a missing pair on --write, so the repair is one render and the refusal
# ---- names it: the SCRIPT and its mode, never a launcher, because this repo cannot assume a bare
# ---- `python` exists and the driver's own resolver ban refuses one in source.
bad_units=""
for bmd in $(GIT ls-files "$M/builds/*/README.md" 2>/dev/null); do
  no=$(grep -cxF -- '<!-- gen:build-units -->' "$bmd" 2>/dev/null || true)
  nc=$(grep -cxF -- '<!-- /gen:build-units -->' "$bmd" 2>/dev/null || true)
  [ "${no:-0}" = 1 ] && [ "${nc:-0}" = 1 ] && continue
  bad_units="$bad_units $bmd"
done
if [ -n "$bad_units" ]; then
  fail 21 "a tracked build README does not carry exactly one well-formed generated-units marker pair, so the driver cannot read its unit list and no run against it can close; repair with the --write mode of tools/memory-tree/gen_build_index.py:$bad_units"
fi

# ---- 20: the PROMPT path's own ordering, PER PATH. TOOL-aPromptedMandate-5.
# ---- Check 18 above orders the FIRST --preflight against the FIRST /session-kickoff across the
# ---- whole template. Once a second start path exists that check keeps grading the FIRST one and is
# ---- SILENTLY BLIND to the other - which is the failure direction nobody notices, as against a
# ---- false red, which somebody fixes in a minute. So the prompt path is ordered inside its OWN
# ---- section rather than against the file.
# ----
# ---- What it holds: the single owner turn precedes the push, and the push precedes preflight. That
# ---- ordering is the whole provenance argument - everything written before the push is older than
# ---- the commit that authorizes the run, and an ask after it is an ask nobody is present for.
if [ -f "$tmpl" ]; then
  # The section, sliced heading-to-heading. A template with no prompt path at all is LEGAL and
  # silent: this kit shipped without one, and an adopter reading an older copy is not in error.
  psec=$(awk '
    /^## Start a run from a PROMPT/ { f = 1; n = 0; next }
    f && /^## / { exit }
    f { n++; print n "\t" $0 }' "$tmpl")
  if [ -n "$psec" ]; then
    askl=$(printf '%s\n' "$psec" | awk -F'\t' 'index($2, "AskUserQuestion") { print $1; exit }')
    pshl=$(printf '%s\n' "$psec" | awk -F'\t' 'index($2, "PUSH THE BRANCH") { print $1; exit }')
    pfl2=$(printf '%s\n' "$psec" | awk -F'\t' 'index($2, "**Preflight**") { print $1; exit }')
    if [ -z "$askl" ] || [ -z "$pshl" ] || [ -z "$pfl2" ]; then
      fail 20 "the Skill's prompt path does not name all three of its ordered steps, so the order that makes the owner turn provably older than the authorization cannot be checked at all; it looks for AskUserQuestion, PUSH THE BRANCH and a bolded Preflight"
    else
      [ "$askl" -lt "$pshl" ] || fail 20 "the Skill's prompt path puts its owner turn AFTER the branch push, so the one question it is allowed to ask would be asked by a run that is already authorized and has nobody to answer it: $askl against $pshl"
      [ "$pshl" -lt "$pfl2" ] || fail 20 "the Skill's prompt path puts the branch push AFTER preflight, and preflight run first meets the refusal that nothing published authorizes the run: $pshl against $pfl2"
    fi
  fi
fi

# ---- 26: THE VERB SET, joined across the documents that spell it. the verb-carrier unit.
# ----
# ---- The driver DERIVES its own two prose carriers now - refusal 14 from the declaration, the usage
# ---- text from the header - so this leg re-checks neither. What no runtime derivation can reach is a
# ---- carrier in ANOTHER FILE: the protocol's verb section is what an owner reads, the Skill's
# ---- invocations are what an agent reads, and a verb missing from either is a verb nobody knows
# ---- exists. Three of the five carriers were stale the day this check was written, and the previous
# ---- fix for exactly that drift was a hand-resynchronisation that lasted one verb.
# ----
# ---- WHAT THIS DOES NOT CHECK: whether a verb's DESCRIPTION anywhere is true. It joins names.
VERBS_SLUG=$(core_of VERBS_SLUG)
VERBS_INLINE=$(core_of VERBS_INLINE)
VERBS_ALL="$VERBS_SLUG $VERBS_INLINE"
nverbs=$(printf '%s\n' $VERBS_ALL | grep -c . || true)
if [ "$nverbs" -lt 10 ]; then
  fail 26 "cannot read the driver's verb declarations, so every carrier below would be joined against an empty set and this check would pass over nothing: $DRIVER"
else
  # ---- THE THREE CARRIERS ARE READ ONCE, not re-grepped once per verb. Same reason `core_of` above
  # ---- is pure bash: a grep per (verb, carrier) is three processes per verb and the verb set is the
  # ---- driver's whole vocabulary, so this one loop was 51 of this leg's 469 process spawns. The
  # ---- predicates below are the same predicates - `( |$)` becomes the two line-terminator cases, the
  # ---- protocol's `^- .VERB. — ` keeps its one-character sentinels as `?`, and the Skill's is still a
  # ---- fixed substring. A quoted expansion inside a `case` pattern is literal, so a verb is never
  # ---- read as a glob.
  _c26_drv=$'
'$(cat "$DRIVER")$'
'
  _c26_ship=""; [ -f "$SHIP" ] && _c26_ship=$'
'$(cat "$SHIP")$'
'
  _c26_tmpl=""; [ -f "$tmpl" ] && _c26_tmpl=$(cat "$tmpl")
  for v in $VERBS_ALL; do
    case "$_c26_drv" in
      *$'
'"#   unattended.sh $v "*|*$'
'"#   unattended.sh $v"$'
'*) : ;;
      *) fail 26 "a declared verb is absent from the driver's own header, and the usage text is RENDERED from that header, so the verb has no documented arguments anywhere a reader looks: $v in $DRIVER" ;;
    esac
    if [ -f "$SHIP" ]; then
      case "$_c26_ship" in
        *$'
'"- "?"$v"?" — "*) : ;;
        *) fail 26 "a declared verb has no entry in the protocol's verb section, so the contract a run is measured against does not describe a verb that run can call: $v in $SHIP" ;;
      esac
    fi
    if [ -f "$tmpl" ]; then
      case "$_c26_tmpl" in
        *"unattended.sh $v "*) : ;;
        *) fail 26 "a declared verb is never invoked in the Skill an agent actually reads, so nothing an agent follows would ever call it: $v in $tmpl" ;;
      esac
    fi
  done
fi

# ---- 27: every park() CALL SITE names a DECLARED kind. The parked region is parsed by kind - by
# ---- --status, by check 17 and by the build method's own wrap-up derivation - so a row whose kind is
# ---- outside the set is a row nothing counts and nothing surfaces. It fails SILENTLY and in the
# ---- direction that loses: the entry is written, the file looks right, and the owner never hears it.
# ----
# ---- Source-level, because every call site passes a literal and no invocation of this driver can
# ---- reach a mistyped one. A runtime guard inside park() would be a branch nothing can fire.
PARK_KINDS=$(core_of PARK_KINDS)
PARK_KINDS_OWED=$(core_of PARK_KINDS_OWED)
# SPACE-SEPARATED, because both joins below are ' word ' membership tests and a newline inside the
# haystack makes every one of them miss - which reds five correct call sites and would be read as
# the check being wrong rather than the shell being literal.
pk_sites=$(grep -oE '^[[:space:]]*park "[$][a-zA-Z_]+" [a-zA-Z-]+' "$DRIVER" | awk '{print $3}' | sort -u | tr '\n' ' ')
npk=$(printf '%s' "$pk_sites" | wc -w)
if [ -z "$PARK_KINDS" ] || [ "$npk" -eq 0 ]; then
  fail 27 "cannot read the parked-kind vocabulary or cannot find a single park() call site, so the membership join below would pass over an empty set - declared and found follow: [$PARK_KINDS] and [$pk_sites]"
else
  for k in $pk_sites; do
    case " $PARK_KINDS " in *" $k "*) ;;
      *) fail 27 "a park() call site writes a kind the driver does not declare, and every reader of that region parses BY kind, so the row would be written and then counted by nothing: $k against [$PARK_KINDS]" ;;
    esac
  done
  # BOTH DIRECTIONS. A declared kind with no writer is the other half of the same defect, and it is
  # the half this kit has a recorded case of: the protocol declared DECISION for as long as it had
  # instructed a run to park one, and no verb wrote it, so the instruction could not be obeyed.
  for k in $PARK_KINDS; do
    case " $pk_sites " in *" $k "*) ;;
      *) fail 27 "the driver declares a parked kind that no park() call site ever writes, so the vocabulary names a row nothing can produce and the instruction to record one cannot be obeyed: $k" ;;
    esac
  done
  # The OWED subset is a subset. A kind owed to the owner but absent from the full set is counted by
  # --status's first alternation and by nothing else, which is a row that exists in one reader only.
  for k in $PARK_KINDS_OWED; do
    case " $PARK_KINDS " in *" $k "*) ;;
      *) fail 27 "a kind the owner is owed an answer to is not in the declared parked-kind set, so the status split and the vocabulary disagree about which rows exist: $k against [$PARK_KINDS]" ;;
    esac
  done
fi

# ---- 24: the MODE SET, joined to the ROUTING TABLE an agent reads, in both directions. This closes
# ---- the fork the mode vocabulary left open: the driver publishes `AUTH_MODES` so nothing has to
# ---- spell it twice, and the one document that has to spell it anyway — the Skill, because a reader
# ---- choosing a path is choosing a mode — was joined to nothing.
# ----
# ---- The extraction takes the LAST backticked lowercase cell of each routing row, so the table's
# ---- prose columns may be rewritten freely and the mode column may not move to the middle without
# ---- this noticing. WHAT IT DOES NOT CHECK: whether the row's PROSE describes the mode correctly.
if [ -f "$tmpl" ]; then
  modesec=$(tr -d '\r' < "$tmpl" | awk '/^## Which path/{f=1;next} f&&/^## /{exit} f')
  if [ -z "$modesec" ]; then
    fail 24 "the Skill template carries no routing section, so a reader holding a build to start is never told which mode their path declares and every join below would have nothing to read; the heading this looks for is '## Which path'"
  else
    tblmodes=$(printf '%s\n' "$modesec" | awk -F'|' '
      /^[[:space:]]*[|]/ {
        m = ""
        for (i = 2; i <= NF; i++) {
          cell = $i; gsub(/^[[:space:]]+|[[:space:]]+$/, "", cell)
          if (cell ~ /^`[a-z][a-z-]*`$/) { gsub(/`/, "", cell); m = cell }
        }
        if (m != "") print m
      }' | sort -u | tr '\n' ' ')
    if [ -z "$tblmodes" ]; then
      fail 24 "the Skill's routing section carries no row naming an authorization mode, so both joins below would compare the driver's mode set against an empty one and pass by finding nothing"
    else
      for _m in $AUTH_MODES; do
        case " $tblmodes " in *" $_m "*) ;;
          *) fail 24 "the driver declares an authorization mode that no routing row names, so a build may legally declare a mode the Skill never tells anyone how to start: $_m against [$tblmodes]" ;;
        esac
      done
      for _m in $tblmodes; do
        case " $AUTH_MODES " in *" $_m "*) ;;
          *) fail 24 "the Skill's routing table names an authorization mode the driver does not declare, so a reader following that row writes a build README preflight will refuse: $_m against [$AUTH_MODES]" ;;
        esac
      done
    fi
  fi
fi

# ---- 25: the content-scope rule is labelled a CHECK and denies its own machine half. A prose rule
# ---- that reads like enforcement is worse than no rule: the reader stops looking for the gate.
# ---- This one has NO gate on either entry point — the refusal that was to provide it was withdrawn
# ---- unbuilt on the unattended path, and on the attended path its two inputs do not exist at all.
# ----
# ---- Grepped as LITERALS, which is what check 12 does to the kickoff engine and for its reason: a
# ---- heading survives a gutted body, and the sentence that has to be there is the qualifier, not
# ---- the section. WHAT THIS DOES NOT CHECK: that the surrounding paragraph is true.
if [ -f "$tmpl" ]; then
  pbsec=$(tr -d '\r' < "$tmpl" | awk '/^## Start a PLAYBOOK run/{f=1;next} f&&/^## /{exit} f')
  if [ -z "$pbsec" ]; then
    fail 25 "the Skill template carries no playbook-run section, so the mode the driver accepts has no start path an agent can follow: $tmpl"
  else
    printf '%s\n' "$pbsec" | grep -qF 'there is no machine half' \
      || fail 25 "the Skill's playbook-run path does not deny its own machine half, and a prose rule that reads like enforcement stops the reader looking for the gate that is not there: $tmpl"
    printf '%s\n' "$pbsec" | grep -qF 'ordinary code build' \
      || fail 25 "the Skill's playbook-run path does not say what this mode is NOT for, so the one refusal it is supposed to carry in prose is absent from the prose: $tmpl"
  fi
fi

# ---- 28: THE INLINED PARSER, one answer in two files. `declared_list` is copy-inlined in the driver
# ---- and in the playbook leg because each kit script is installed standalone and cannot import — so
# ---- the only thing keeping two copies one answer is this check.
# ----
# ---- It exists because the copies ALREADY desynchronised once, silently and expensively. Round 1
# ---- found a trailing-comment strip missing from the `set_checks` parse; the fold added it there and
# ---- wrote a THIRD spelling for `piece_checks` seventy-five lines away without it, and the kit's own
# ---- template line then graded every piece `unchecked` on an item that takes no override. A byte
# ---- comparison is the cheapest thing that could have caught that.
# ----
# ---- WHAT IT DOES NOT CHECK: whether the shared parse is CORRECT. Two identical wrong copies pass.
# ---- The template arm below is what checks the answer.
fi

if [ "$SCOPE" != skip28 ]; then
dl_a=$(awk '/^declared_list\(\) \{/{f=1} f{print} f&&/^\}/{exit}' "$DRIVER")
dl_b=$(awk '/^declared_list\(\) \{/{f=1} f{print} f&&/^\}/{exit}' "$HERE/check-playbook.sh" 2>/dev/null)
# THE SCALAR SIBLING, on the same terms. Round 3, HIGH 6: `declared_list` was consolidated and
# byte-compared while the FIVE scalar reads stayed ad-hoc, so this check generalised the parse across
# list keys and the gate across `*_checks` only - two of the block's ten declaration keys.
ds_a=$(awk '/^declared_scalar\(\) \{/{f=1} f{print} f&&/^\}/{exit}' "$DRIVER")
ds_b=$(awk '/^declared_scalar\(\) \{/{f=1} f{print} f&&/^\}/{exit}' "$HERE/check-playbook.sh" 2>/dev/null)
tpl="$HERE/PLAYBOOK-TEMPLATE.template.md"

# ---- THE KIT'S OWN SOURCE POPULATION, derived once for the three rules below. A hand-typed file list
# ---- is a declaration that rots: round 5 found 28c scanning three names while the kit had seven, and
# ---- the ones it did not name held thirty of the thirty-two sha reads.
KIT_SH=""
for _f in "$HERE"/*.sh; do
  case "$_f" in *.test.sh) continue ;; esac
  [ -f "$_f" ] || continue
  KIT_SH="$KIT_SH $_f"
done
# LIVENESS BY MEMBERSHIP, not by count. A count floor is unreachable here - this script and the
# adopter are themselves non-test `*.sh` in this directory, so the population is never empty and a
# branch guarding emptiness could be reached by no fixture, which is the shape round 3 filed against
# this very check. What the three rules below actually need is that the file they exist to police is
# IN the population. There is no branch for the DRIVER: check 1 exits the whole leg when its core sets
# are unreadable, nine hundred lines above here, so a driver-missing branch could not be reached
# either. The leg CAN go missing without stopping the run.
case " $KIT_SH " in
  *" $HERE/check-playbook.sh "*) ;;
  *) fail 28 "the playbook leg is not in the source population these three rules scan, so the census reader - the one that dereferences the BASE blob every DoD verdict rests on - would go unexamined: $HERE/check-playbook.sh" ;;
esac

# ---- 28a - THE REFUSAL MUST BE READ, AT EVERY CALL SITE, and the rule ENUMERATES WHAT IS COMPLIANT
# ---- rather than what is not. Four rounds have broken here. Round 3 gave `declared_list` a
# ---- `return 2`; round 4 found two of three call sites branching on it; round 5 found this rule
# ---- whitelisting any line containing `||`, so `… || true` graded compliant; round 6 found the
# ---- replacement enumerating three discard spellings while `|| return 0` and `|| _x=""` walked past,
# ---- and an honest refusal whose PROSE contained the word `true` matched the discard arm and red.
# ----
# ---- Enumerating discards is unwinnable: every new spelling widens the hole, and the default is pass.
# ---- Enumerating the compliant set inverts that - the default is FAIL, and a new spelling has to be
# ---- added deliberately. The compliant set is exactly two shapes: a negated conditional around the
# ---- call, or a `||` whose right-hand side provably refuses.
# ----
# ---- AND THE DECISION IS TAKEN ON A TOKEN, NEVER ON A LINE. The line is split at the call, the part
# ---- BEFORE it is asked about the conditional and the part AFTER it about the refusal, so prose
# ---- anywhere else on the line cannot vote. That is round 6's own diagnosis of seven of its ten
# ---- defects, applied here first.
# ----
# ---- The rule binds a parser that CAN refuse, and that property is DERIVED from the parser's own
# ---- body: a `return <nonzero>` in the extracted text. Give `declared_scalar` one tomorrow and its
# ---- call sites start being policed without a byte of this check changing.
# ----
# ---- WHAT THIS DOES NOT CHECK: whether the refusal a caller takes is the RIGHT one for the item.
rc_refusers=0
for _p in declared_list declared_scalar; do
  case "$_p" in declared_list) _body=$dl_a ;; *) _body=$ds_a ;; esac
  printf '%s\n' "$_body" | grep -qE '(^|[^[:alnum:]_])return[[:space:]]+[1-9]' || continue
  rc_refusers=$((rc_refusers + 1))
  _p_sites=0
  for _f in $KIT_SH; do
    _f_named=0
    grep -q "$_p" "$_f" && _f_named=1
    _f_sites=0
    while IFS= read -r _cs; do
      [ -n "$_cs" ] || continue
      _f_sites=$((_f_sites + 1)); _p_sites=$((_p_sites + 1))
      _ln=${_cs%%:*}; _txt=${_cs#*:}
      _head=${_txt%%"\$($_p"*}
      _tail=${_txt#*"\$($_p"}
      _tail=${_tail#*)}
      case "$_head" in
        *'if !'*|*'while !'*|*'until !'*|*'if ! '*) continue ;;
      esac
      # A `||` COUNTS ONLY IF ITS RIGHT-HAND SIDE REFUSES. `return 0`, an assignment and `true` are
      # not refusals; `return <nonzero>`, `exit <nonzero>`, `fail ` and `bad ` are.
      case "$_tail" in
        *'||'*)
          case "$_tail" in
            *'return '[1-9]*|*'exit '[1-9]*|*'fail '*|*'bad '*|*'continue'*) continue ;;
          esac ;;
      esac
      fail 28 "a parser that can REFUSE is called at a site that does not act on its exit status, so the refusal arrives as the empty string every caller reads as the declared null and the item it guards grades met with nothing recorded - parser, site and call follow: $_p at $_f:$_ln spells [$_txt]"
    done <<RCEOF
$(grep -nE '\$\('"$_p"'[[:space:]]' "$_f" | grep -vE '^[0-9]+:[[:space:]]*#' || true)
RCEOF
    # PER FILE, for a file that NAMES the parser. A file that never mentions it legitimately has no
    # call sites; a file that mentions it and has none this pattern can see is a call spelling that
    # drifted, which is the masking direction the per-parser counter alone cannot see. The adopter and
    # this checker mention the names in prose, so the assertion is scoped to files holding a `$(`-call.
    # DETECTED BROADLY, ENUMERATED NARROWLY, and the gap between the two is the finding. The
    # enumerator wants `$(<parser><space>`; this detector accepts any whitespace after the `$(` too,
    # so a call written with a space after the substitution is seen here and missed there - which is
    # exactly the drift this branch exists to report rather than to silently tolerate. COMMENTS ARE
    # FILTERED, because the first cut of this detector matched the sentence above describing it.
    if [ "$_f_named" = 1 ] && [ "$_f_sites" -eq 0 ] && grep -E "[$][(][[:space:]]*$_p" "$_f" | grep -qvE '^[[:space:]]*#'; then
      fail 28 "a file spells a call to a refusing parser in a shape this rule cannot enumerate, so its call sites go unpoliced while the rule reports nothing about them - parser and file follow: $_p in $_f"
    fi
  done
  [ "$_p_sites" -gt 0 ] || fail 28 "a refusing parser has NO call site this rule can see, so it was asserted over an empty population and would stay green with every caller discarding the status - the enumeration pattern has stopped matching the way this kit calls this parser: $_p"
done
[ "$rc_refusers" -gt 0 ] || fail 28 "neither inlined parser carries a nonzero return any more, so the rule that a refusal must be read now binds nothing - either the refusal round 3 added was removed, in which case a legal multi-line declaration parses to the declared null again, or this check's derivation of which parsers can refuse has stopped matching them"

# ---- 28b - EVERY DECLARATION KEY IS BOUND TO THE PARSER ITS REAL READER CALLS, asserted POSITIVELY.
# ---- Round 5 found the first cut vacuous; round 6 found the second cut's EXEMPTION TABLE destroyed by
# ---- word-splitting - `for _e in $KEY_EXEMPT` over a record containing spaces yields its first field
# ---- and the literal resolved to the 4-byte string `grep`, present nineteen times in the file it
# ---- names, so the freshness half had no failing input at all. The table is newline-separated and
# ---- read without splitting now, which is the only shape that survives a value with spaces in it.
KEY_EXEMPT=$(cat <<'EXEMPTEOF'
legs|check-playbook.sh|ent=$(printf '%s\n' "$body" | grep -oE
EXEMPTEOF
)
kb_keys=0
if [ -f "$tpl" ]; then
  # ---- THE TWO CORPORA THE KEY LOOP READS, one pass per file instead of one per (key, file). Each
  # ---- record is `<file>TAB<lineno>:<text>`, split on its FIRST tab so a tab inside the text is
  # ---- carried through untouched. The comment filter is the one the two greps used to apply, moved
  # ---- one level out; `grep -q` lines are still dropped from the caret corpus, for the reason the
  # ---- original filter names.
  KB_CALLS=""
  KB_CARETS=""
  for _f in $KIT_SH; do
    KB_CALLS="$KB_CALLS$(grep -nE 'declared_(list|scalar) ' "$_f" | grep -vE '^[0-9]+:[[:space:]]*#' | sed "s|^|$_f	|" || true)
"
    KB_CARETS="$KB_CARETS$(grep -nE '\^[A-Za-z_]' "$_f" | grep -vE '^[0-9]+:[[:space:]]*#' | grep -v 'grep -q' | sed "s|^|$_f	|" || true)
"
  done
  while IFS= read -r _k; do
    [ -n "$_k" ] || continue
    kb_keys=$((kb_keys + 1))
    _reads=0
    for _f in $KIT_SH; do
      # THE COMMENT FILTER ON THE POSITIVE HALF TOO. Its negative half has had one since round 5, and
      # a key whose only "read" is a commented-out call is a key nothing reads. It is applied in the
      # per-file corpora above, before either key test, which is where the two greps used to apply it.
      #
      # THE GREPS MOVED OUT OF THIS LOOP AND NOTHING ELSE MOVED. They ran once per (key, file) - 200 of
      # this leg's 469 process spawns, the single largest population in it - and their patterns are
      # key-specific only in the tail, so the file half is now read once and the key half is matched
      # here. The corpora are SUPERSETS by construction: a line matching `declared_(list|scalar) .*
      # KEY)` contains `declared_list ` or `declared_scalar `, and a line matching `\^KEY(...)` contains
      # a caret followed by a letter or underscore, because every key the template declares starts with
      # one. The exact predicate is re-applied per key below, so the prefilter can only ever be wider.
      while IFS= read -r _rec; do
        [ -n "$_rec" ] || continue
        [ "${_rec%%	*}" = "$_f" ] || continue
        _hit=${_rec#*	}
        case "$_hit" in
          *"declared_list "*" $_k)"*|*"declared_scalar "*" $_k)"*) _reads=$((_reads + 1)); break ;;
        esac
      done <<KBCEOF
$KB_CALLS
KBCEOF
      while IFS= read -r _rec; do
        [ -n "$_rec" ] || continue
        [ "${_rec%%	*}" = "$_f" ] || continue
        _hit=${_rec#*	}
        # `( |$)` in the original ERE, as its two cases: a non-word character after the key, or the
        # end of the line. Anything else is a longer identifier that merely starts with the key.
        case "$_hit" in
          *"^$_k") : ;;
          *"^$_k"[!A-Za-z_]*) : ;;
          *) continue ;;
        esac
        fail 28 "a declaration key the shipped template ships is read by an ad-hoc pipeline rather than by the parser this check certifies it through, so the answer this gate blesses and the answer its consumer actually gets are two answers to one question - key, site and read follow: $_k at $_f:${_hit%%:*} spells [${_hit#*:}]"
      done <<KBEOF
$KB_CARETS
KBEOF
    done
    [ "$_reads" -gt 0 ] && continue
    _ex=""
    while IFS= read -r _e; do
      [ -n "$_e" ] || continue
      case "$_e" in "$_k|"*) _ex=$_e ;; esac
    done <<EXEOF
$KEY_EXEMPT
EXEOF
    if [ -z "$_ex" ]; then
      fail 28 "the shipped template declares a key no inlined parser ever reads, so this check certifies a parse nothing consumes while whatever does consume it is unexamined - declare a parser read for it, or an exemption naming the reader that owns it: $_k in $tpl"
      continue
    fi
    _exrest=${_ex#*|}
    _exf=${_exrest%%|*}
    _exlit=${_exrest#*|}
    grep -qF -- "$_exlit" "$HERE/$_exf" \
      || fail 28 "a key exemption names a reader whose signature is no longer in that file, so the key is unread by any parser AND unaccounted for by the exemption that excused it - key, file and missing literal follow: $_k in $_exf wants [$_exlit]"
  done <<KEYEOF
$(awk '/^```toml/{f=1;next} f&&/^```/{exit} f&&/^[a-z_]+[[:space:]]*=/{sub(/[[:space:]]*=.*$/,"");print}' "$tpl" || true)
KEYEOF
  [ "$kb_keys" -gt 0 ] || fail 28 "the shipped template yielded no declaration key to bind to a reader, so every key in it could be read by an ad-hoc pipeline and this rule would stay green over the empty set: $tpl"
fi

# ---- 28c - EVERY SHA DEREFERENCE IN THIS KIT GOES THROUGH A PINNED READ. A forced replace ref
# ---- rewrites what a dereference returns without touching one tracked byte, and ONLY
# ---- `-c core.useReplaceRefs=false` suppresses it. The exported `GIT_GRAFT_FILE` a child inherits
# ---- does not, and a `-c` is per-invocation, so nothing propagates it to a spawned leg. The committed
# ---- BASE blob is one of exactly two inputs outside the run's own reach; an unpinned read puts it
# ---- back inside, on the item that takes no override.
# ----
# ---- EACH LINE IS GRADED TWICE AND INDEPENDENTLY. Round 6: classifying a whole line as
# ---- wrapper-routed on the substring `GIT ` meant a trailing comment mentioning the wrapper excused a
# ---- bare unpinned read on the same line. A line carrying both is graded on its raw half.
# ----
# ---- THE VERB SET IS WIDE, and the exemptions are PROPERTIES rather than a list of lines. Measured
# ---- over this tree before wiring, per §7: the wide set surfaces eight bare invocations, seven of
# ---- which name no revision at all (`rev-parse --show-toplevel` and friends) or enumerate refs. Those
# ---- two properties are why they are exempt, and both are derived per invocation:
# ----   * every argument after the verb is a flag  -> the invocation cannot name a revision;
# ----   * the verb is `for-each-ref`               -> it enumerates refs, and the kit's own
# ----     replace-ref DETECTOR is one of these: pinning it would blind the check that finds them.
GITV='show|cat-file|ls-tree|archive|rev-list|rev-parse|log|grep|diff|diff-tree|merge-base|for-each-ref|describe|blame'
# THE INVOCATION HAS TO BE IN COMMAND POSITION, which is the difference between code and prose about
# code. The first cut boundaried on "not a word character", so the sentence "every bare git invocation
# ... or for-each-ref property" - inside this check's OWN refusal message - matched as a bare unpinned
# dereference and the gate red on itself. A `git` preceded by an ordinary word is being TALKED ABOUT;
# a `git` preceded by a separator or a command substitution is being RUN. Same lesson as everywhere
# else in this check: decide on the token, never on the line.
GITPOS='(^|[|&;(){}!]|[$][(])[[:space:]]*'
_wrapdef=0
for _f in $KIT_SH; do
  while IFS= read -r _hit; do
    [ -n "$_hit" ] || continue
    _wrapdef=$((_wrapdef + 1))
    # THE PIN MAY BE SPELLED OR EXPANDED, and this predicate has to see both. The merge that brought
    # `aBoundedVerdict` in redefined the wrapper as `git -c "$GIT_PIN_REPLACE" -c "$GIT_PIN_GRAFTADV"`,
    # moving the setting into a constant beside it - a strictly better shape, and one a grep for the
    # literal reads as an unpinned wrapper. So a wrapper line naming a variable is accepted only when
    # THAT variable is assigned the pin in the same file: the indirection is followed rather than
    # trusted, which is the difference between reading a name and reading a value.
    _wl=${_hit#*:}
    _pinned=0
    case "$_wl" in *'core.useReplaceRefs=false'*) _pinned=1 ;; esac
    if [ "$_pinned" -eq 0 ]; then
      for _pv in $(printf '%s\n' "$_wl" | grep -oE '[$]\{?[A-Za-z_][A-Za-z0-9_]*' | tr -d '${'); do
        grep -qE "^[[:space:]]*$_pv=core\.useReplaceRefs=false" "$_f" && { _pinned=1; break; }
      done
    fi
    [ "$_pinned" -eq 1 ] && continue
    fail 28 "the kit's own git wrapper is defined without the replace-ref pin, so every read routed through it is unpinned at once - and this kit routes its BASE-blob authorization read through it. Site follows: $_f:${_hit%%:*} spells [${_hit#*:}]"
  done <<WDEOF
$(grep -nE '^[[:space:]]*GIT\(\)[[:space:]]*\{' "$_f" || true)
WDEOF
done
[ "$_wrapdef" -gt 0 ] || fail 28 "no git wrapper definition was found anywhere in this kit, so the GIT-spelled reads below are accepted on the strength of a definition this check cannot see - which is the same as not checking them"
sha_raw=0
sha_raw_graded=0
sha_wrapped=0
for _f in $KIT_SH; do
  # THE RAW ARM.
  while IFS= read -r _hit; do
    [ -n "$_hit" ] || continue
    sha_raw=$((sha_raw + 1))
    _inv=$(printf '%s\n' "${_hit#*:}" | grep -oE "${GITPOS}git[[:space:]]+[^|;&)]*" | head -1)
    _inv="git ${_inv#*git }"
    # THE VERB IS THE FIRST TOKEN THAT IS NEITHER A FLAG NOR A FLAG'S ARGUMENT. `-C <dir>` and
    # `-c <name>=<value>` each take one, and skipping the flag while grading its argument is how
    # `git -C "$ROOT" rev-parse` came out with a verb of `"$ROOT"`.
    _verb=""; _skip=0
    for _tok in $_inv; do
      [ "$_skip" = 1 ] && { _skip=0; continue; }
      case "$_tok" in
        git) continue ;;
        -c|-C) _skip=1; continue ;;
        -*|*=*) continue ;;
        *) _verb=$_tok; break ;;
      esac
    done
    [ "$_verb" = for-each-ref ] && continue
    _args=${_inv#*"$_verb"}; _args=${_args%%2>*}
    _names_rev=0
    for _tok in $_args; do
      case "$_tok" in -*|'') continue ;; *) _names_rev=1; break ;; esac
    done
    [ "$_names_rev" = 1 ] || continue
    sha_raw_graded=$((sha_raw_graded + 1))
    case "$_inv" in
      *'core.useReplaceRefs=false'*) continue ;;
    esac
    fail 28 "a sha is dereferenced without the replace-ref pin, so a replace ref this run may install at any moment substitutes the committed bytes the census grades - and the run then supplies the playbook it is measured against, on an item no waiver can move. Site and read follow: $_f:${_hit%%:*} spells [${_hit#*:}]"
  done <<RAWEOF
$(grep -nE "${GITPOS}git[[:space:]]+([^|;&]*[[:space:]])?($GITV)([[:space:]]|\$)" "$_f" | grep -vE '^[0-9]+:[[:space:]]*#' || true)
RAWEOF
  # THE WRAPPED ARM, counted independently of whether the same line also matched the raw one.
  # `grep -c` prints 0 and exits 1 on no match, so the count is taken FIRST and the status swallowed
  # after it - `|| echo 0` appended a second line and the arithmetic below silently failed on it.
  _wn=$(grep -cE "${GITPOS}GIT[[:space:]]+([^|;&]*[[:space:]])?($GITV)([[:space:]]|\$)" "$_f" 2>/dev/null || true)
  sha_wrapped=$((sha_wrapped + ${_wn:-0}))
done
# LIVENESS ON EACH SPELLING SEPARATELY, and on the raw arm's GRADED population rather than its
# candidate one. Round 5's cut counted a candidate it then exempted and called that coverage; a raw
# arm whose every candidate is excused has reached nothing, and the two states must not look alike.
# NO ASSERTION ON THE RAW CANDIDATE COUNT, and the reason is reachability rather than confidence.
# Every kit script bootstraps with `ROOT=$(git rev-parse --show-toplevel)`, which is a bare invocation
# on this scan's verb list, so `sha_raw` cannot be zero in any run that gets this far - neutralise
# those and the checker exits at its own root resolution long before check 28. A branch no fixture can
# reach is the shape round 3 filed against this check and round 5 filed against the count floor that
# preceded this one, so it is stated here instead of being written as a gate that always passes.
#
# The GRADED count below is the live one: it is the candidates that survived the two exemptions, and
# routing the kit's last real dereference through the wrapper takes it to zero. That arm exists.
[ "$sha_raw_graded" -gt 0 ] || fail 28 "every bare git invocation in the kit was excused by the flags-only or for-each-ref property, so the raw arm graded nothing at all this run - it is reporting a clean nothing rather than a pass, and the two are not the same claim"
# AND NONE ON THE WRAPPED COUNT EITHER, for the same reason and it was measured: renaming every
# wrapper-routed verb in the kit takes `sha_wrapped` to zero and ALSO stops this checker before it can
# say so, because the checker is one of the scripts being renamed. There is no fixture that empties
# the population and still reaches the report.
#
# WHAT THIS RULE THEREFORE ASSERTS, stated plainly because a reader will assume more: that every bare
# invocation naming a revision carries the pin, that the wrapper's own definition carries it, and that
# at least one bare candidate survived the exemptions to be graded. It does NOT assert that either
# spelling still appears anywhere - a predicate that silently stopped matching both would pass, and
# the two deleted branches are where that gap used to be papered over with a check nothing could fail.

if [ -z "$ds_a" ] || [ -z "$ds_b" ]; then
  fail 28 "the declared-scalar parser is missing from one of the two scripts that inline it, so the comparison that keeps the copies one answer would pass over an empty pair - driver and leg follow: $DRIVER and $HERE/check-playbook.sh"
elif [ "$ds_a" != "$ds_b" ]; then
  fail 28 "the two inlined copies of the declared-scalar parser have drifted, and a declaration parsed two ways is two answers to one question - they are copy-inlined because each kit script installs standalone, so this comparison is the only thing holding them together"
  diff <(printf '%s\n' "$ds_a") <(printf '%s\n' "$ds_b") | head -8 | sed 's/^/    /'
fi
if [ -z "$dl_a" ] || [ -z "$dl_b" ]; then
  fail 28 "the declared-list parser is missing from one of the two scripts that inline it, so the comparison that keeps the copies one answer would pass over an empty pair - driver and leg follow: $DRIVER and $HERE/check-playbook.sh"
elif [ "$dl_a" != "$dl_b" ]; then
  fail 28 "the two inlined copies of the declared-list parser have drifted, and a declaration parsed two ways is two answers to one question - they are copy-inlined because each kit script installs standalone, so this comparison is the only thing holding them together"
  diff <(printf '%s\n' "$dl_a") <(printf '%s\n' "$dl_b") | head -8 | sed 's/^/    /'
else
  # THE ANSWER, not just the agreement. Every key the SHIPPED TEMPLATE declares is fed to the parser
  # its reader calls, exactly as an adopter would copy it - comment and all. The template is the one
  # input every adopter starts from, and no hand-written fixture keeps carrying its comment.
  if [ ! -f "$tpl" ]; then
    fail 28 "the shipped playbook template is missing, so the parser cannot be run over the line every adopter actually copies and this check would grade agreement alone: $tpl"
  else
    # THE REAL PARSER, EXECUTED - not a third spelling of it. Writing the pipeline out here is the
    # exact defect this check exists to catch, one level up: a checker that re-implements its subject
    # confirms the re-implementation. The extracted function text is defined and called.
    #
    # AND THE EXIT STATUS IS THE FIRST THING ASSERTED. Round 3, HIGH 4: this ran the parser under
    # `2>/dev/null` and asserted only that the output was EMPTY - so a syntax error, a truncated
    # extraction and a correct parse of `[]` were one observation, and replacing both parser bodies
    # with an empty printf left this check silent and green while the census went verified-over-unchecked.
    # A dead harness must not be byte-indistinguishable from a working one.
    # ONE PROCESS PER PARSER PER LOOP, not one per specimen. Measured on node d, 2026-08-23, with
    # per-region timestamps taken inside the suite's own fixture: the 34 `bash -c` spawns this block
    # used to make were 5.0 s of a 10.7 s invocation, and the fixture suite runs this leg 243 times.
    # The parser body, the function called and the specimens are unchanged - what changed is that they
    # are fed to one shell instead of one shell each.
    #
    # THE FALLBACK KEEPS THIS BYTE-IDENTICAL FOR ONE DEGRADED SHAPE AND REDS ON THE OTHER, and the
    # distinction is round 7's blocker 1. A body that will not parse makes `bash -c` print nothing and
    # exit nonzero, so the reply is EMPTY; every slot is filled with that exit status and an empty
    # answer, which is exactly what the per-specimen wrapper handed each caller before, so the rc
    # branches below fire with the same text the same number of times. A body that RAN and returned a
    # reply that will not split per specimen is a different fact and gets its own refusal, because the
    # value that would otherwise be fabricated - rc 0 and the empty string - is what both template
    # arms read as a clean parse. A dead harness must not be byte-indistinguishable from a working
    # one, it must not be text-distinguishable from the unbatched one, and its degraded mode must not
    # be spelled with the passing value.
    # _PB_DEAD says the harness answered NOTHING, which the fill alone cannot say. Round 8's low 2:
    # `bash -c` exits 2 on a syntax error, the empty-reply branch faithfully fills every slot with
    # that 2 - and 2 is exactly the value the multi-line REFUSAL arm asserts, so a parser that will
    # not parse reported a correct refusal from a harness that ran nothing. The equivalence with the
    # old per-specimen wrapper is worth keeping; the arm reading it as an answer is not.
    _PB_RC=(); _PB_OUT=(); _PB_DEAD=0
    _pbatch() { # parser-body - fn - body key [body key ...]  ->  fills _PB_RC / _PB_OUT, one per pair
      local _body=$1 _fn=$2 _pairs _res _rc _line _i
      shift 2
      _PB_DEAD=0
      _pairs=$(( $# / 2 ))
      _PB_RC=(); _PB_OUT=()
      _res=$(bash -c "$_body
while [ \$# -gt 0 ]; do
  _pb_o=\$($_fn \"\$1\" \"\$2\"); _pb_r=\$?
  printf '%s\t%s\n' \"\$_pb_r\" \"\$_pb_o\"
  shift 2
done" _ "$@")
      _rc=$?
      if [ -n "$_res" ]; then
        while IFS= read -r _line; do
          _PB_RC+=("${_line%%$'\t'*}")
          _PB_OUT+=("${_line#*$'\t'}")
        done <<PBEOF
$_res
PBEOF
      fi
      [ "${#_PB_RC[@]}" -eq "$_pairs" ] && return 0
      # ---- TWO DEGRADED SHAPES, AND THEY ARE NOT THE SAME SHAPE. Round 7's blocker 1 was one branch
      # ---- for both, filling every slot with the batch's own `$_rc` - which is 0 when the batch RAN
      # ---- and merely misaligned, and `(rc 0, "")` is the PASSING pair in both template arms below.
      # ---- A parser broken only for multi-line input therefore took the leg to rc 0 with no output,
      # ---- in the loop that is the shipped template's ONLY grader. A degraded-mode substitute must
      # ---- never be a value some assertion reads as clean.
      if [ -z "$_res" ]; then
        # THE BODY DID NOT RUN. `bash -c` printed nothing and exited nonzero, which is byte-for-byte
        # what the per-specimen wrapper handed each caller before this was batched, so the rc branches
        # below fire with the same text the same number of times. This is the equivalence the comment
        # above claims, and it is true of THIS branch only.
        _PB_RC=(); _PB_OUT=(); _PB_DEAD=1
        _i=0
        while [ "$_i" -lt "$_pairs" ]; do _PB_RC+=("$_rc"); _PB_OUT+=(""); _i=$((_i + 1)); done
        return 0
      fi
      # THE BODY SPOKE AND THE REPLY DOES NOT LINE UP: one answer carried a newline, or the parser
      # emitted a line of its own. There is no honest per-specimen answer to hand back, so this says
      # so ONCE and then poisons every slot with a nonzero sentinel, which reaches each arm's rc
      # branch. 125 is not a status any parser here returns.
      fail 28 "the batched parser harness got a reply it cannot split per specimen, so no assertion below is answering about the input it names - parser, specimens sent and answer lines received follow: $_fn wanted $_pairs got ${#_PB_RC[@]}"
      _PB_RC=(); _PB_OUT=()
      _i=0
      while [ "$_i" -lt "$_pairs" ]; do _PB_RC+=(125); _PB_OUT+=(""); _i=$((_i + 1)); done
      return 0
    }
    tpl_block=$(awk '/^```toml/{f=1;next} f&&/^```/{exit} f' "$tpl")
    # THE POSITIVE DIRECTION, FIRST AND FIXED, FOR BOTH PARSERS. The template declares every key as a
    # declared null of its own type, so neither template loop below has an input whose expected parse
    # is non-empty - each is structurally incapable of telling a working parser from one that answers
    # nothing, which is the answer that disables every consumer. These specimens are this check's only
    # non-empty expectation.
    #
    # ROUND 4, HIGH 5: the list half got these and the scalar half did not, in the same commit. Gutting
    # `declared_scalar` to an empty printf visited seven template keys with zero failures, and swapping
    # its comment strip for a delete-the-whole-line sed - which empties every commented declaration,
    # the mirror image of the leak this arm exists to catch - left the whole kit green.
    _dl_specs=('Xk = ["a", "b#c"]    # trailing commentX|Xa b#cX' 'Xk = [ "solo" ]X|XsoloX' 'Xk = []X|XX' 'Xk = # globs. Where pieces land [see 7]X|XX' 'Xk =X|XX' 'Xk = ["a", "b"] X|Xa bX' 'Xk = ["a"]	X|XaX' 'Xk =# globsX|XX' 'Xk =#globsX|XX' 'Xk = [ ]X|XX')
    _argv=()
    for spec in "${_dl_specs[@]}"; do
      _in=${spec%%|*}; _in=${_in#X}; _in=${_in%X}
      _argv+=("$_in" k)
    done
    _pbatch "$dl_a" declared_list "${_argv[@]}"
    _ix=-1
    for spec in "${_dl_specs[@]}"; do
      _ix=$((_ix + 1))
      _in=${spec%%|*}; _want=${spec#*|}
      _in=${_in#X}; _in=${_in%X}; _want=${_want#X}; _want=${_want%X}
      _got=${_PB_OUT[$_ix]}; _rc=${_PB_RC[$_ix]}
      if [ "$_rc" -ne 0 ]; then
        fail 28 "the extracted declared-list parser could not be executed, so every parse assertion in this check would read its silence as the declared null and pass - specimen and exit status follow: [$_in] exited $_rc"
      elif [ "$_got" != "$_want" ]; then
        fail 28 "the extracted declared-list parser does not return the members of a NON-EMPTY declaration, which is the only direction that tells a working parser from one answering nothing - specimen, wanted and got follow: [$_in] wanted [$_want] got [$_got]"
      fi
    done
    _ds_specs=('Xk = "v"    # trailing commentX|XvX' 'Xk = 0X|X0X' 'Xk = {}    # noteX|X{}X' 'Xk = memory/records    # where they landX|Xmemory/recordsX' 'Xk = # who ratified and whenX|XX' 'Xk =    # TBDX|XX' 'Xk =# who ratifiedX|XX' 'Xk =#whoX|XX' 'Xk = "v" X|XvX')
    _argv=()
    for spec in "${_ds_specs[@]}"; do
      _in=${spec%%|*}; _in=${_in#X}; _in=${_in%X}
      _argv+=("$_in" k)
    done
    _pbatch "$ds_a" declared_scalar "${_argv[@]}"
    _ix=-1
    for spec in "${_ds_specs[@]}"; do
      _ix=$((_ix + 1))
      _in=${spec%%|*}; _want=${spec#*|}
      _in=${_in#X}; _in=${_in%X}; _want=${_want#X}; _want=${_want%X}
      _got=${_PB_OUT[$_ix]}; _rc=${_PB_RC[$_ix]}
      if [ "$_rc" -ne 0 ]; then
        fail 28 "the extracted declared-scalar parser could not be executed, so every parse assertion in this check would read its silence as the declared null and pass - specimen and exit status follow: [$_in] exited $_rc"
      elif [ "$_got" != "$_want" ]; then
        fail 28 "the extracted declared-scalar parser does not return the VALUE of a non-empty declaration, which is the only direction that tells a working parser from one answering nothing - a parser that empties every commented line passes every other assertion here. Specimen, wanted and got follow: [$_in] wanted [$_want] got [$_got]"
      fi
    done
    # THE MULTI-LINE ARRAY, which is round 3's blocker and round 4's. A legal TOML array spread over
    # lines used to yield the bare `[`, parse to the declared null, and grade every verdict-less piece
    # `verified` on the one item that takes no override - and this check CERTIFIED that output, because
    # empty was all it ever asserted. Round 4 then found the refusal testing the RAW line, so a `]`
    # inside a trailing comment satisfied the terminator arm and restored the whole defect. BOTH
    # spellings are specimens here, and the commented one is the reason the first was not enough.
    _ml_specs=('k = [' 'k = [   # one per piece [see section 7]' 'k = [ # note ]' 'k = ["a[0]",' 'k = ["content/pieces/[0-9]*/**",')
    _argv=()
    for _ml in "${_ml_specs[@]}"; do
      _argv+=("$(printf '%s\n  "a",\n]\n' "$_ml")" k)
    done
    _pbatch "$dl_a" declared_list "${_argv[@]}"
    _ix=-1
    for _ml in "${_ml_specs[@]}"; do
      _ix=$((_ix + 1))
      _got=${_PB_OUT[$_ix]}; _rc=${_PB_RC[$_ix]}
      # THE ONLY ARM HERE WHOSE EXPECTED VALUE IS A NONZERO STATUS, so it is the only one a dead
      # harness can satisfy by accident. It grades the harness first.
      [ "$_PB_DEAD" -eq 0 ] || { fail 28 "the multi-line refusal is graded against a harness that answered nothing, so a parser that will not parse would report the refusal this arm is looking for: specimen [$_ml]"; continue; }
      [ "$_rc" -eq 2 ] || fail 28 "the extracted declared-list parser does not REFUSE an array left open at the end of its line, so a legal multi-line declaration parses to the declared null and every piece carrying no verdict grades verified - specimen, exit status and answer follow: [$_ml] exited $_rc with [$_got]"
    done
    # THE TWO TEMPLATE LOOPS COUNT SEPARATELY. Round 4, MEDIUM 6: one shared counter meant either half
    # could go dark while the other satisfied the liveness assertion - the list awk matches three keys
    # and the scalar awk seven, so neutering either left the check green under a message claiming the
    # template half had covered something. That is round 3's HIGH 6 restored one level up: the
    # population became derived and the assertion that the derivation found anything stayed blind to
    # half of it.
    tpl_list=0
    tpl_scalar=0
    _tl_rows=(); _argv=()
    while IFS= read -r tl; do
      [ -n "$tl" ] || continue
      _tl_rows+=("$tl"); _argv+=("$tpl_block" "${tl%%[[:space:]]*}")
    done <<TPLKEOF
$(awk '/^```toml/{f=1;next} f&&/^```/{exit} f&&/^[a-z_]+[[:space:]]*=[[:space:]]*\[/' "$tpl" || true)
TPLKEOF
    [ "${#_tl_rows[@]}" -eq 0 ] || _pbatch "$dl_a" declared_list "${_argv[@]}"
    _ix=-1
    for tl in ${_tl_rows[@]+"${_tl_rows[@]}"}; do
      _ix=$((_ix + 1))
      tpl_list=$((tpl_list + 1))
      got=${_PB_OUT[$_ix]}; rc=${_PB_RC[$_ix]}
      # THE rc BRANCH IS BACK, and the comment that removed it was wrong. It read: a branch here could
      # be reached by no fixture, because the specimens above already assert the parser executes. A
      # template list key written MULTI-LINE reaches it exactly - rc 2, empty stdout, the -n test
      # false, silent pass. That matters more than it looks: `check-playbook.sh` excludes this template
      # from its own population, so this loop is the ONLY grader of the shipped template's declarations.
      if [ "$rc" -ne 0 ]; then
        fail 28 "the shipped template's own list declaration is REFUSED by the parser that reads it, so an adopter who copies the template inherits a declaration the driver cannot parse - and this check is the template's only grader, so nothing else would say so. Key and exit status follow: ${tl%%=*} exited $rc"
      elif [ -n "$got" ]; then
        fail 28 "the shipped template's own declaration line does not parse to the declared null, so an adopter who copies the template verbatim inherits phantom check names and every piece grades unchecked - key and parse follow: ${tl%%=*} yields [$got]"
      fi
    done

    # EVERY OTHER KEY IN THE FENCE, through the scalar parser. The population is DERIVED from the
    # template's own toml block rather than from a hand-typed pattern, so a key added there reds until
    # a parse assertion claims it. The old pattern matched `*_checks` - two keys of ten - while the
    # failure text made the key-independent claim "an adopter who copies the template verbatim".
    #
    # WHAT IS ASSERTED is that the COMMENT does not survive the parse. Every value in the shipped
    # block is a declared null of its own type, so a `#` in the parsed result is the leak signature and
    # it is the same signature for every key.
    _ts_rows=(); _argv=()
    while IFS= read -r tl; do
      [ -n "$tl" ] || continue
      _ts_rows+=("$tl"); _argv+=("$tpl_block" "${tl%%[[:space:]]*}")
    done <<TPLSKEOF
$(awk '/^```toml/{f=1;next} f&&/^```/{exit} f&&/^[a-z_]+[[:space:]]*=/ && !/^[a-z_]+[[:space:]]*=[[:space:]]*\[/' "$tpl" || true)
TPLSKEOF
    [ "${#_ts_rows[@]}" -eq 0 ] || _pbatch "$ds_a" declared_scalar "${_argv[@]}"
    _ix=-1
    for tl in ${_ts_rows[@]+"${_ts_rows[@]}"}; do
      _ix=$((_ix + 1))
      tpl_scalar=$((tpl_scalar + 1))
      got=${_PB_OUT[$_ix]}; rc=${_PB_RC[$_ix]}
      if [ "$rc" -ne 0 ]; then
        fail 28 "the extracted declared-scalar parser could not be executed over the shipped template's own line, and an unexecutable parser returns the empty string every assertion here reads as clean - key and exit status follow: ${tl%%=*} exited $rc"
      else
        case "$got" in
          *'#'*) fail 28 "the shipped template's own declaration line parses with its COMMENT still attached, so an adopter who fills the template in place and keeps the comments gets that prose as the value - key and parse follow: ${tl%%=*} yields [$got]" ;;
        esac
      fi
    done

    # LIVENESS, PER LOOP, and DELIBERATELY NOT A COUNT COMPARISON. The first cut asserted that the
    # number of keys parsed equalled the number the fence declares - but both sides are derived from
    # that same fence by the same awk, so they cannot disagree whatever either does. That is this
    # project's own `assertion-between-two-derived-values` class, written into the check that exists to
    # stop a parser going quiet.
    #
    # The second cut asserted the UNION was non-empty, which is true of either half alone. Each half
    # now answers for itself, and the refusals name which one covered nothing - because "the template
    # half ran" was never the claim worth making about two independent populations.
    [ "$tpl_list" -gt 0 ] || fail 28 "the shipped template's declaration block yielded no LIST key this check could parse, so the list half of the template assertion covered nothing and a parser that answers nothing for every array would pass it: $tpl"
    [ "$tpl_scalar" -gt 0 ] || fail 28 "the shipped template's declaration block yielded no SCALAR key this check could parse, so the scalar half of the template assertion covered nothing and a comment leak on every scalar key would pass it: $tpl"
  fi
fi

fi

exit "$status"
