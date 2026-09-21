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
# Exit 0 + no output = clean, EXCEPT for the two announcements named below. Anything else printed
# is a violation. Exit 2 = misconfigured.
#
# THREE EXCEPTIONS, all named rather than quietly taken.
#
# ONE: a check that cannot COMPARE announces the case it could not reach, on the REPORT channel,
# which the default run does not print. Set GOV_UNATTENDED_REPORT=1 to see them. A skip that looks
# like a pass is indistinguishable from coverage, and a skip printed by default would falsify the
# contract line above — so the line keeps its meaning and the announcement gets a channel of its
# own. TOOL-dUnstalledConvoy-6.
#
# TWO: check 7's EXCLUSION notice and its UNAVAILABLE sibling print on the DEFAULT channel, and the
# contract line above is written to admit them. They are not skips. An exclusion is a positive
# finding that CHANGED THE VERDICT — a record the check stopped counting — and the reader of a green
# run is entitled to know which one and on what evidence. Routing them through REPORT was the first
# implementation and it made the exclusion invisible on every bar run, which is the check-quietly-
# deleted shape unit 4 exists to prevent; routing them to stdout without amending this paragraph
# would leave the header asserting something the code disproves. TOOL-aPrimedKeepalive-4.
#
# THREE: check 35's LANDER_MODE and SELFTESTS_OWED_PATHS lines print on the DEFAULT channel too, and
# for TWO's reason rather than by a second concession. They are not skips: they are the effective
# landing shape and the declared self-test surface, and those decide WHICH COMMIT the landing bar
# graded and whether a kit-work landing is ever told the flagged bar is owed. A reader of a green bar
# is entitled to both without setting an environment variable, and routing them through REPORT would
# make them invisible on every bar run. TOOL-dDerivedDocket-3.
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
KIT_UNATTENDED_VERSION=1.25   # gov:kit unattended@1.25 — must match unattended.sh; check-kit-versions.sh pairs them

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
MEMORY_ROOT=memory; LANDER=""; LANDER_MODE=""; SELFTESTS_OWED_PATHS=""; BYPASS_BAN=""; GATE_CMD=""; WIRING_CHECK=""
KEEPALIVE_CREATE=""; KEEPALIVE_DELETE=""; PHASES_EXTRA=""; DOD_EXTRA=""; CORE_FLOOR=""; LANDED_ANCHOR_CUTOFF=""
DISPOSITION_CUTOFF=""
# TOOL-dDerivedDocket-22 S10 - the date from which the landed fact-set arm grades a record.
LANDED_FACTS_CUTOFF=""
KICKOFF_ENGINE=""; KICKOFF_EXITS=""; DIRECTIVES_EXTRA=""; DIRECTIVES_FLOOR=""; DIRECTIVES_EXTRA_TABLE=""
HALT_CODES_EXTRA=""; HALT_FLOOR=""
HOLD_CODES_EXTRA=""; HOLD_FLOOR=""; LEASE_STALE_AFTER=""
RESUME_SCHEDULE=""; RESUME_SCHEDULE_CREATE=""; RESUME_SCHEDULE_DELETE=""
RESUME_SCHEDULE_DELAY=""; RESUME_SCHEDULE_LIMIT=""
# TOOL-dDerivedDocket-20 - condition 3's two keys, which check 38 compares with each other. The
# SENTINEL, not blank, for the driver's reason: an undeclared SHARED_RECORDS takes the kit default and
# a declared blank is the empty set, and `resolve_shared_records` in the kit library tells the two
# apart for both readers. Initialised here and admitted by the allow-list below, or this leg would read
# both keys at their defaults whatever the project declares.
SHARED_RECORDS="$SHARED_RECORDS_UNDECLARED"; GENERATED_INDEXES=""
# TOOL-dDerivedDocket-18 - the two optional declared commands the ask-mandate second opinions read.
# BOTH default to blank and blank means NOT ADOPTED, which is the register both keys already sit in
# elsewhere in this kit. They are initialised HERE and admitted by the allow-list below, or the leg
# would read them blank whatever the project declares and every arm keyed on them would announce a
# skip on an adopting repo - a check that is dark while reading green.
RECALL_CLI=""; ASKS_CMD=""
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
# ---- trap, a redefined function, an `exit`, a `set -x` - none of it crosses the boundary. What DOES
# ---- cross is a value per declared key, and the allow-list below is what bounds THAT channel: the
# ---- worst a hostile conf can do is give one of those keys a hostile value, which is the cost the
# ---- protocol concedes when it says a leg reads its subject's answer. It does not get to name a
# ---- different subject.
# ----
# ---- THE NAMES ARE READ AS TEXT AND VALIDATED, never taken from the file's own output. A key the
# ---- file spells in some other shape keeps the default initialised above, which is exactly what a
# ---- `sed`-based reader would have done with it.
_conf_names=$(sed -n 's/^[[:space:]]*\(export[[:space:]][[:space:]]*\)\{0,1\}\([A-Z][A-Z0-9_]*\)=.*/\2/p' "$CONF" | sort -u)
_conf_ok=0
while IFS= read -r -d '' _ck; do
  IFS= read -r -d '' _cv || break
  case "$_ck" in
    __CONF_IMPORT_OK__) _conf_ok=1 ;;
    # AN ALLOW-LIST, NOT A GLOB, and this half of the amendment was left standing for a round. The
    # open `[A-Z][A-Z0-9_]*` arm assigned EVERY uppercase key the conf declared, and this leg sets
    # `HERE` and `DRIVER` ABOVE the import - the file it parses every core set out of, and the
    # directory it byte-compares the playbook leg from. Reproduced twice on the live tree: a tracked
    # `DRIVER="/dev/null"` made check 1 refuse for an unreadable `AUTH_MODES`, and a decoy carrying
    # plausible declarations made checks 1, 2, 16, 26, 28 and 31 grade the decoy while the real
    # driver enforced something else. `SCOPE="skip28"` deleted the whole 28 region including 28c's
    # pinned-git-read enforcement. `.unattended.conf` is a tracked file an unattended run commits
    # itself, and this is an unguarded merge-bar leg. The two sibling importers - check-pass-order
    # and check-brief-recorded - already close it. `check-brief-recorded.sh`'s own comment names a
    # sibling that sets DRIVER above its import and evals a classifier out of it: that is
    # `check-pass-order.sh`, not this leg, which evals nothing but its own import assignment. An
    # earlier revision of this paragraph claimed that comment named THIS hole; it does not, and the
    # attribution is corrected rather than left to mislead the next reader.
    #
    # THE SET IS THE INTERSECTION of the keys initialised above with the keys the shipped
    # `.unattended.conf.example` declares, which is what "the keys this leg reads FROM THE CONF"
    # means. `UNITS_REGION_CUTOFF` is in it and is initialised nowhere above - it is read at its two
    # sites through `${UNITS_REGION_CUTOFF:-}` - so a list transcribed from the initialiser block
    # alone would have silently stopped it being configurable. `ADV_NAME` is NOT in it and is
    # initialised above: it is this leg's own derived value, parsed out of the remote's HEAD
    # advertisement, and the initialiser exists only so `set -u` survives the path where that parse
    # did not run. Assigning it from the conf is not a feature being kept, it is the same hole
    # wearing a different key.
    # THE SENTINELS BELOW NAME THIS BLOCK FOR A JOIN THAT IS NOT YET WIRED - see check 22, which
    # records why it was withdrawn. They are BARE on purpose: an anchored range over them must not be
    # able to match the extractor's own source line, which is how the first draft of that join read 38
    # keys instead of 20 and swept in heredoc markers and phase names.
    # gov:conf-allow-begin
    MEMORY_ROOT|LANDER|LANDER_MODE|SELFTESTS_OWED_PATHS|BYPASS_BAN|GATE_CMD|WIRING_CHECK|KEEPALIVE_CREATE|KEEPALIVE_DELETE|\
    PHASES_EXTRA|DOD_EXTRA|CORE_FLOOR|LANDED_ANCHOR_CUTOFF|LANDED_FACTS_CUTOFF|DISPOSITION_CUTOFF|KICKOFF_ENGINE|\
    KICKOFF_EXITS|DIRECTIVES_EXTRA|DIRECTIVES_FLOOR|DIRECTIVES_EXTRA_TABLE|HALT_CODES_EXTRA|\
    HALT_FLOOR|HOLD_CODES_EXTRA|HOLD_FLOOR|LEASE_STALE_AFTER|\
    RESUME_SCHEDULE|RESUME_SCHEDULE_CREATE|RESUME_SCHEDULE_DELETE|RESUME_SCHEDULE_DELAY|RESUME_SCHEDULE_LIMIT|\
    RECALL_CLI|ASKS_CMD|SHARED_RECORDS|GENERATED_INDEXES|\
    UNITS_REGION_CUTOFF) eval "$_ck=\$_cv" ;;
    # gov:conf-allow-end
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
# The kit default of an undeclared SHARED_RECORDS, resolved by the same library call the driver makes,
# so the two readers cannot disagree about a conf that leaves the key out.
SHARED_RECORDS=$(resolve_shared_records "$SHARED_RECORDS" "$MEMORY_ROOT")


# ====================================================================== bulk git, warmed once
# ---- THE SAME QUESTION, ABOUT THE SAME COMMIT, 127 TIMES. Measured on this tree with every git
# ---- argv logged: `rev-parse --verify <HEAD>` ran 52 times, `rev-parse HEAD` 39 and
# ---- `cat-file -e <HEAD>` 36 - all one immutable fact, each costing a process. A git process on
# ---- this platform costs ~130 ms whatever it is asked, so this leg's wall clock IS its process
# ---- count and almost nothing else: 777 of them for the leg's own checks, against 435 s of leg.
# ----
# ---- The helpers below answer those questions from tables filled by ONE query each. Every one of
# ---- them KEEPS THE ORIGINAL CALL as a fallback for a key the warm-up did not collect, so
# ---- correctness never depends on the pre-scan being complete: a miss is slow, never wrong. That
# ---- is also why the warm-ups are lazy - several checks exit before reaching a record, and a walk
# ---- nobody asks for is the same waste one process at a time was.
# ---- TOOL-aQuenchedHarness-10.

# HEAD does not move while this leg runs; it was being re-resolved once per record.
HEAD_SHA=$(GIT rev-parse HEAD 2>/dev/null || true)

# ---- every sha-shaped token in every tracked run-state file, resolved in ONE batch.
# It enumerates its own file list rather than reading `$RUNS`, because the first caller runs well
# above where `$RUNS` is built and a warm-up that ran early against an unset list would mark itself
# warmed while holding nothing - a cache that is empty and believes it is full.
# `_REV_FULL` costs nothing extra: the batch reply's first field IS the full sha, and holding it
# lets the ancestry tables answer an ABBREVIATED recorded rev, which they otherwise cannot -
# measured, 30 calls fell through to a per-call `merge-base` for exactly that reason.
declare -A _REV_OK _REV_FULL
_REV_WARMED=0
_load_rev_table() {
  [ "$_REV_WARMED" = 1 ] && return 0
  _REV_WARMED=1
  local _line _j _n
  local -a _revs=() _out=()
  while IFS= read -r _line; do
    [ -n "$_line" ] && _revs+=("$_line")
  done < <(GIT ls-files "$M/builds/*/RUN*.md" 2>/dev/null \
           | xargs -r grep -hoE '[0-9a-f]{7,40}' 2>/dev/null | sort -u)
  _n=${#_revs[@]}
  [ "$_n" -gt 0 ] || return 0
  while IFS= read -r _line; do _out+=("$_line"); done < <(
    printf '%s^{commit}\n' "${_revs[@]}" | GIT cat-file --batch-check 2>/dev/null)
  # ONE REPLY PER REQUEST, IN ORDER - which is what makes zipping them sound. Keying the table on
  # the REPLY's first field would key it by full sha and miss every abbreviated recorded fact, and
  # a short count means something went wrong: leave the table empty and let every call fall back.
  [ "${#_out[@]}" = "$_n" ] || return 0
  for ((_j = 0; _j < _n; _j++)); do
    case "${_out[$_j]}" in
      *" commit "*)
        _REV_OK[${_revs[$_j]}]=0
        _REV_FULL[${_revs[$_j]}]=${_out[$_j]%% *} ;;
      *) _REV_OK[${_revs[$_j]}]=1 ;;
    esac
  done
  return 0
}
check_rev() {  # rev -> 0 it resolves to a commit in this history · 1 it does not
  _load_rev_table
  [ -n "${_REV_OK[$1]+x}" ] && return "${_REV_OK[$1]}"
  if GIT rev-parse --verify --quiet "$1^{commit}" >/dev/null 2>&1; then _REV_OK[$1]=0; else _REV_OK[$1]=1; fi
  return "${_REV_OK[$1]}"
}

# ---- ancestry is set membership, and one walk answers every record.
# `merge-base --is-ancestor A B` is true exactly when A is reachable from B, which is what
# `rev-list B` enumerates - same relation, same reflexive case. An abbreviated rev cannot be looked
# up in a table of full shas, so it falls back to the original call.
declare -A _HEAD_REACH
_HEAD_WARMED=0
_load_head_reach() {
  [ "$_HEAD_WARMED" = 1 ] && return 0
  _HEAD_WARMED=1
  local _h
  while IFS= read -r _h; do [ -n "$_h" ] && _HEAD_REACH[$_h]=1; done < <(GIT rev-list HEAD 2>/dev/null)
  return 0
}
check_head_reaches() {  # rev -> 0 an ancestor of HEAD, HEAD itself included · 1 not
  _load_head_reach
  local _r=$1
  if [ ${#_r} != 40 ]; then _load_rev_table; _r=${_REV_FULL[$1]:-$1}; fi
  if [ ${#_r} = 40 ]; then
    [ -n "${_HEAD_REACH[$_r]+x}" ]
    return $?
  fi
  GIT merge-base --is-ancestor "$1" HEAD 2>/dev/null
}

# The same, against the tip the remote advertises for its own default branch. It is a DIFFERENT set
# from the union `is_published` holds: reachable-from-any-advertised-tip does not imply
# reachable-from-ADV_HEAD, and this asks the narrower question.
declare -A _ADVH_REACH
_ADVH_WARMED=0
_load_adv_reach() {
  [ "$_ADVH_WARMED" = 1 ] && return 0
  _ADVH_WARMED=1
  [ "${ADV_HEAD_OK:-0}" = 1 ] || return 0
  local _h
  while IFS= read -r _h; do [ -n "$_h" ] && _ADVH_REACH[$_h]=1; done < <(GIT rev-list "$ADV_HEAD" 2>/dev/null)
  return 0
}
check_adv_reaches() {  # rev -> 0 an ancestor of the advertised HEAD · 1 not
  _load_adv_reach
  local _r=$1
  if [ ${#_r} != 40 ]; then _load_rev_table; _r=${_REV_FULL[$1]:-$1}; fi
  if [ "${ADV_HEAD_OK:-0}" = 1 ] && [ ${#_r} = 40 ]; then
    [ -n "${_ADVH_REACH[$_r]+x}" ]
    return $?
  fi
  GIT merge-base --is-ancestor "$1" "${ADV_HEAD:-}" 2>/dev/null
}
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

# TOOL-dNarrowedAnchor-1 - the partition of that vocabulary by which modes may reach the SECOND
# anchor, read through the same parse for the same reason: a second spelling of a set is how two
# files come to disagree about it silently.
#
# EMPTY IS A REFUSAL, and the direction matters more here than it does for AUTH_MODES. An empty
# AUTH_MODES makes checks keyed on it vacuously TRUE; an empty SECOND_ANCHOR_MODES makes check 29
# fire on EVERY mode, so a failed read would red a fleet of legitimate prompt runs rather than
# silently pass them. Both failure modes are wrong and this one is louder, which is why it refuses
# rather than defaulting to the driver's pair.
SECOND_ANCHOR_MODES=$(core_of SECOND_ANCHOR_MODES)
if [ -z "$SECOND_ANCHOR_MODES" ]; then
  fail 1 "cannot read SECOND_ANCHOR_MODES from the driver, so check 29 would treat every declared mode as inadmissible on the second anchor and red every branch-anchored run in the tree: $DRIVER"
fi

# The parked-kind taxonomy. Read here for the same reason the four above are: a set declared in the
# driver and graded nowhere is decoration, and this one has a counter and a Definition-of-Done
# predicate hanging off it.
PARK_KINDS_OWED=$(core_of PARK_KINDS_OWED)
# The ACT axis of the same taxonomy, read for the reason the kind axis is: it has a `--status`
# counter and a Definition-of-Done predicate hanging off it, and a set declared in the driver and
# graded nowhere is decoration. A SEPARATE read rather than a widened one, because these are acts and
# that is kinds.
PARK_ACTS_OWED=$(core_of PARK_ACTS_OWED)
# The non-overridable Definition-of-Done set, read for arm 16d below.
DOD_NO_OVERRIDE=$(core_of DOD_NO_OVERRIDE)
# The review loop's runaway backstop, read the same way. The leg holds NO copy of the number: a
# second spelling of a bound is a bound that goes wrong silently when one copy moves.
RUNAWAY_CEILING=$(core_of RUNAWAY_CEILING)
# READ FROM THE DRIVER, never restated — this file's own rule, and fifteen other closed sets
# already obey it. A restatement drifts silently: widen the driver's set and this leg tells a
# record it was hand-edited when the driver itself wrote the value.
REVIEW_DISPOSITIONS=$(core_of REVIEW_DISPOSITIONS)
# THE FOLD RULE'S OWN CUTOFF, read the same way (closing review of aProbedUnit, round 2, cluster A).
# DISPOSITION_CUTOFF dates the FIELD; this dates the later rule about the field's VALUE, and a ratchet
# that grades history needs one per rule it grades — the fold-beside-blockers clause under the
# field's cutoff alone redded sixteen tracked records the driver itself wrote under the contract that
# accepted them. Unreadable is named inside check 2 rather than at a `fail` site of its own, because
# the three pinned check-2 ordinals in memory/project/unarmed-branches.txt sit below this line.
FOLD_CUTOFF=$(core_of FOLD_CUTOFF)
# The halt vocabulary, read the same way. The leg holds NO member token of its own: a prefix
# alternation could not tell a member from an unrelated identifier, and a sibling unit lands a
# constant whose name such an alternation would have matched.
HALT_CODES_CORE=$(core_of HALT_CODES_CORE)
# The HOLD vocabulary, read for the reason the halt one is: a set the driver validates against and
# nothing grades is a vocabulary with a floor nobody enforces.
HOLD_CODES_CORE=$(core_of HOLD_CODES_CORE)
HALT_CODES="$HALT_CODES_CORE $HALT_CODES_EXTRA"

# ---- TOOL-dDerivedDocket-18 — the driver's UNQUOTED numeric constants. `core_of` above matches
# ---- `KEY="value"` and nothing else, by a contract check 1 refuses on, so a constant the driver
# ---- declares BARE is invisible to it and reads as the empty string. Two ways out were rejected:
# ---- quoting the driver's declaration is a kit file edited to suit its reader, and restating the
# ---- number here is the drift this whole file exists to catch. This reads the bare form instead.
# ---- DIGITS ONLY. A bare value that is not a plain integer is NOT an answer — it comes back empty,
# ---- exactly as `core_of` does on an unreadable line, and the caller names its own skip. Widening
# ---- this to "anything after the `=`" would import an unquoted expression, a trailing comment and
# ---- a `$(…)` as though they were constants.
read_bare_const() { # KEY  ->  the unquoted integer from $DRIVER, or nothing
  local l p="$1=" v
  while IFS= read -r l || [ -n "$l" ]; do
    l=${l%$'\r'}
    while :; do case "$l" in *' '|*$'\t') l=${l%?} ;; *) break ;; esac; done
    case "$l" in
      "$p"*) v=${l#"$p"}
             case "$v" in ""|*[!0-9]*) ;; *) printf '%s\n' "$v"; return 0 ;; esac ;;
    esac
  done < "$DRIVER"
  return 0
}
# ---- The declared shape of the ask generator's projection, read from the driver for the reason
# ---- every other closed set here is: the leg re-runs the SAME two call shapes the driver runs
# ---- (S8) and a second spelling of the column contract is how the two come to read different
# ---- fields of one row. An unreadable value is a NAMED SKIP at the arm, never a guessed width.
# ---- READ LAZILY, on the first producer call and never before it. The three keys sit ~2700 lines
# ---- into the driver, so the pure-bash scan costs about a third of a second each - measured on
# ---- node d 2026-09-21, a second a leg run, paid by every run of this leg and every arm of its
# ---- suite for records that do not exist yet. Only a mandated, unpublished record reaches a call.
ASK_TSV_HEAD=""; ASK_TSV_EXAMINED=""; ASK_TSV_FIELDS=""; ASK_TSV_READ=0
read_ask_tsv_contract() {
  [ "$ASK_TSV_READ" = 1 ] && return 0
  ASK_TSV_READ=1
  ASK_TSV_HEAD=$(core_of ASK_TSV_HEAD)
  ASK_TSV_EXAMINED=$(core_of ASK_TSV_EXAMINED)
  ASK_TSV_FIELDS=$(read_bare_const ASK_TSV_FIELDS)
}

# ---- TOOL-dDerivedDocket-18 — THE PYTHON LAUNCHER, RESOLVED. The anchor ban below reaches the
# ---- recall kit's own extractor through an interpreter, and this leg is the first thing in the kit
# ---- to spawn one. The block between the markers is byte-identical to the canonical copy its own
# ---- marker line names, and its parity gate reds if it drifts; it is carried INLINE because a
# ---- copy-installed kit has
# ---- no shared library to source, which is the same reason the driver has carried it since
# ---- aDeferredBar. A resolver that finds no usable launcher is a NAMED SKIP at the arm, never a
# ---- silent pass: being on PATH is not evidence, so the candidate is RUN.
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
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
_disp_ok=1
# ---- THE SET MUST BE READABLE, or the two clauses that compare against it grade every value as
# ---- illegal or none as illegal, and both look like a working check. Same liveness shape as
# ---- RUNAWAY_CEILING and AUTH_MODES above.
if [ -z "$REVIEW_DISPOSITIONS" ]; then
  fail 2 "the driver declares no readable REVIEW_DISPOSITIONS, so the clause that grades a recorded disposition would compare every value against an empty set and report whatever that produces as a verdict"
  _disp_ok=0
fi
# ---- DISPOSITION_CUTOFF: malformed is a REFUSAL, never a defaulted value, because a cutoff that
# ---- quietly defaults grades every record or none and nobody can tell which. Same shape as the
# ---- RUNAWAY_CEILING refusal below it and as check-pass-order.sh's own cutoff guard.
if [ -n "$DISPOSITION_CUTOFF" ]; then
  case "$DISPOSITION_CUTOFF" in
    [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
    *) fail 2 "DISPOSITION_CUTOFF is declared and is not an ISO date, and a cutoff nothing can compare grades every record or none: $DISPOSITION_CUTOFF"; _disp_ok=0 ;;
  esac
else
  # ---- ANNOUNCED UNCONDITIONALLY, on stdout, once per run. NOT through report(), which is gated on
  # ---- GOV_UNATTENDED_REPORT and would make a disabled term invisible on a default bar run — a
  # ---- silently disabled clause reads exactly like a clause finding nothing wrong.
  echo "unattended: DISPOSITION_CUTOFF is blank or undeclared, so check 2 clause 3 grades EVERY record on the id-delta proxy and reads no recorded disposition — a run that folded correctly is still graded as though it had promoted"
fi
if [ "$_disp_ok" != 1 ]; then
  # ---- AND THE LOOP BELOW IS SKIPPED ENTIRELY. An unreadable cutoff means this leg cannot decide
  # ---- WHICH predicate applies, and grading every record on the other one is precisely the silent
  # ---- choice the refusal above exists to prevent. Same shape as the RUNAWAY_CEILING arm beside it:
  # ---- a term that cannot be read says so instead of quietly picking a default.
  echo "unattended: check 2 graded NO record and skipped ALL THREE of its review-loop clauses — the runaway-ceiling and stalled-loop arms as well as the disposition one. A term this check cannot read leaves it unable to decide which predicate applies, and choosing one silently would be the fault the refusal above names"
elif [ -z "$RUNAWAY_CEILING" ]; then
  fail 2 "the driver declares no readable RUNAWAY_CEILING, so the review-loop check below would be skipped entirely and its absence would look exactly like a clean corpus"
else
  rv_bad=""
  # ---- A CUTOFF NOTHING CAN COMPARE grades every record or none: an empty one sorts before every
  # ---- date and reds the whole grandfathered population, a malformed one sorts after and disarms
  # ---- the clause silently. Named once, into the same failure the clauses below feed.
  case "$FOLD_CUTOFF" in
    [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
    *) rv_bad="$rv_bad
  (the driver declares no readable ISO-date FOLD_CUTOFF, so the fold-beside-blockers clause cannot tell a record written under the old contract from one graded by the severity rule and would red every record or none: '$FOLD_CUTOFF')" ;;
  esac
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
    rv_new=""; rv_readable=0
    if [ -f "$rv_readme" ]; then
      # NON-WONTDO ONLY. The promotion clause discharges an exited loop by counting NEW unit ids,
      # and it never looked at their status - so three thin specs flipped to `WONTDO` satisfied it,
      # and `build-complete` saw no non-terminal row either. A promoted blocker that was retired is
      # not a promotion. The status predicate is spelled EXACTLY as check 24's retire loop spells it,
      # so the two clauses cannot disagree about what a retired unit looks like.
      #
      # SEVEN PROCESSES PER RECORD BECAME ZERO. This was `grep -vE | grep -oE | sort -u` on the HEAD
      # side, `grep -oE | sort -u` on the BASE side, and `comm -23 | grep -c` to difference them --
      # ten spawns a record, of which only the COUNT is consumed, by the awk below via `-v newids`.
      # Two associative arrays do `sort -u`'s dedupe and `comm -23`'s difference, and unlike `comm`
      # they need no sorted input at all, so the ordering coupling between the three goes with them.
      #
      # THE MATCH IS A LOOP, NOT ONE `[[ =~ ]]`, and that is the whole correctness of it. `grep -oE`
      # emits EVERY id on a line while a bare match takes only the first, so a units row naming two
      # ids would under-count -- and this count feeds the promotion clause, where under-counting
      # reads as "no promotion happened": a FALSE GREEN, the one direction that must not be possible.
      # Both sides use the identical loop, because two spellings would manufacture phantom ids.
      declare -A _rv_h=() _rv_b=()
      _rv_blob=$(region "$rv_readme" '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null || true)
      while IFS= read -r _rv_l || [ -n "$_rv_l" ]; do
        case $_rv_l in *'| WONTDO |'*) continue ;; esac
        while [[ $_rv_l =~ [A-Z]+-[A-Za-z]+-[0-9]+ ]]; do
          _rv_h[${BASH_REMATCH[0]}]=1; _rv_l=${_rv_l#*"${BASH_REMATCH[0]}"}
        done
      done <<< "$_rv_blob"
      if [ -n "$rv_base" ] && check_rev "$rv_base"; then
        _rv_blob=$(GIT show "$rv_base:$rv_readme" 2>/dev/null | awk '/<!-- gen:build-units -->/{f=1;next} /<!-- \/gen:build-units -->/{f=0} f' || true)
        while IFS= read -r _rv_l || [ -n "$_rv_l" ]; do
          while [[ $_rv_l =~ [A-Z]+-[A-Za-z]+-[0-9]+ ]]; do
            _rv_b[${BASH_REMATCH[0]}]=1; _rv_l=${_rv_l#*"${BASH_REMATCH[0]}"}
          done
        done <<< "$_rv_blob"
        rv_readable=1
      fi
      if [ "$rv_readable" = 1 ]; then
        _rv_n=0
        for _rv_k in "${!_rv_h[@]}"; do [ -n "${_rv_b[$_rv_k]:-}" ] || _rv_n=$((_rv_n + 1)); done
        rv_new=$_rv_n
      fi
    fi
    # GRADED ON THE RECORD'S OWN FIRST-COMMIT DATE, the idiom LANDED_ANCHOR_CUTOFF already uses. A
    # record whose first commit is at or after the cutoff is read for its dispositions; one before it
    # keeps the id-delta proxy verbatim, messages included.
    rv_graded=0
    if [ -n "$DISPOSITION_CUTOFF" ]; then
      # --follow OR THE ROTATION RE-DATES THE RECORD. `--preflight` moves a terminal RUN.md to
      # RUN.<phase>.<blob8>.md, a NEW path whose first `A` is the rotation commit, so a record
      # created before the cutoff becomes GRADED the moment any later run rotates it — and its rows
      # predate the flag, so it reds forever on an append-only archive. Measured on
      # RUN.ABORTED.fc79c21d.md: 2026-08-20 without, 2026-08-19 with.
      rv_fc=$(GIT log --follow --diff-filter=A --format=%cs -- "$rvf" 2>/dev/null | tail -1)
      # AN EMPTY DATE GRADES. The record is staged and uncommitted, which is the IN-FLIGHT run — the
      # one case that can still record a disposition, and so the last one to hand the id proxy to.
      # The sibling cutoff this was copied from grandfathers an empty date; the spec said to invert
      # that and the first cut took the sibling's clause verbatim.
      if [ -z "$rv_fc" ] || printf '%s\n%s\n' "$DISPOSITION_CUTOFF" "$rv_fc" | sort -C; then rv_graded=1; fi
    fi
    # THE FOLD RULE HAS ITS OWN CUTOFF, from the SAME first-commit date by the same idiom. A record
    # before it was written when the driver accepted `fold` at a blocker-bearing exit, and reading it
    # by today's rule redded sixteen tracked append-only records no verb can rewrite. An empty date
    # grades here too, for the reason the sibling gives: it is the in-flight run.
    rv_foldgraded=0
    if [ "$rv_graded" = 1 ] && { [ -z "$rv_fc" ] || printf '%s\n%s\n' "$FOLD_CUTOFF" "$rv_fc" | sort -C; }; then rv_foldgraded=1; fi
    rv_bad="$rv_bad$(awk -v ceil="$RUNAWAY_CEILING" -v f="$rvf" -v readable="$rv_readable" -v newids="${rv_new:-0}" -v graded="$rv_graded" -v foldgraded="$rv_foldgraded" -v disps="|$REVIEW_DISPOSITIONS|" '
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
        if (rs ~ /CONVERGED|NON-CONVERGENT|CEILING|BOUNDED/) term[it] = 1
        nf = split(rs, fld, " · ")
        if (rs ~ /NON-CONVERGENT|CEILING|BOUNDED/) {
          needs[it] = 1; bl[it] = b
          disp[it] = (nf > 0 && fld[nf] ~ /^disposition /) ? substr(fld[nf], length("disposition ") + 1) : ""
        }
        # A CONVERGED ROW CARRYING A DISPOSITION IS READ TOO (closing review of aProbedUnit, cluster
        # C). The severity rule disposes the HIGHS that stood at zero blockers, and the driver
        # records `CONVERGED · disposition promote` when it did; a promotion this clause never
        # counted was a promotion the bar could not see. Only under the graded path: the id-delta
        # proxy predates the field and never read a converged row, and a converged subject is not
        # one that "EXITED without converging".
        else if (rs ~ /CONVERGED/ && graded == 1 && nf > 0 && fld[nf] ~ /^disposition /) {
          needs[it] = 1; bl[it] = b
          disp[it] = substr(fld[nf], length("disposition ") + 1)
        }
      }
      END {
        nneed = 0; nomiss = ""; illegal = ""; foldbad = ""
        for (it in n) {
          if (n[it] > ceil)
            printf "\n  %s (subject %s: %d review rounds against a runaway ceiling of %d, so the loop ran past its own backstop)", f, it, n[it], ceil
          else if (flat[it] >= 1 && !(it in term))
            printf "\n  %s (subject %s: blocker counts did not shrink across consecutive rounds and no round carries an exit token, so the loop is non-convergent and nothing recorded that it stopped)", f, it
          if (it in needs) {
            if (graded != 1) nneed++
            else if (disp[it] == "") nomiss = nomiss " " it
            else if (index(disps, "|" disp[it] "|") == 0) illegal = illegal " " it "=" disp[it]
            else if (disp[it] == "promote") nneed++
            else if (bl[it] > 0 && foldgraded == 1) foldbad = foldbad " " it "=" bl[it]
            # a subject recording `fold` beside ZERO blockers demands NOTHING, which is the entire
            # point of reading the field instead of inferring an answer from ids; beside a non-zero
            # count it is a blocker left standing under a field that says nothing was — from
            # FOLD_CUTOFF on. Before it the driver accepted the row, and it demands what it demanded
            # when it was written: nothing
          }
        }
        if (graded == 1) {
          if (nomiss != "")
            printf "\n  %s (exited subject(s)%s record NO disposition while this record is graded against DISPOSITION_CUTOFF, so which of fold or promote the run took cannot be read - and with nothing to read this clause would demand nothing and pass by finding nothing)", f, nomiss
          if (illegal != "")
            printf "\n  %s (exited subject(s)%s carry a disposition outside the closed set %s - the driver validates the flag at write time, so an illegal value reached this record by HAND, and reading it as absent would name the wrong cause)", f, illegal, substr(disps, 2, length(disps) - 2)
          if (foldbad != "")
            printf "\n  %s (exited subject(s)%s record disposition fold beside a NON-ZERO blocker count in a record first-committed on or after FOLD_CUTOFF, after which the driver refuses this at write time, and the severity rule promotes every blocker, so a fold there is a blocker left standing under a field that says nothing was)", f, foldbad
          if (nneed > 0) {
            if (readable != 1)
              printf "\n  %s (%d subject(s) EXITED recording disposition promote and the roster at this run BASE cannot be read, so whether a blocker was promoted CANNOT BE OBSERVED - a check that cannot look says so rather than passing)", f, nneed
            else if (newids + 0 < nneed)
              printf "\n  %s (%d subject(s) EXITED recording disposition promote and the generated units region gained only %d non-WONTDO unit id(s) this run BASE lacked, so at least one promoted blocker or high has no unit. A subject recording disposition fold beside zero blockers demands nothing here)", f, nneed, newids + 0
          }
        }
        else {
        # COUNTED ACROSS SUBJECTS, because `newids` is a per-FILE delta. Consumed inside the
        # per-subject loop it let ONE promotion satisfy every subject in the file that exited
        # without converging. A per-subject attribution is not available - the region records ids,
        # not which subject promoted them - so the honest claim is the counting one: N subjects that
        # exited owe at least N ids this run BASE lacked.
        if (nneed > 0) {
          if (readable != 1)
            printf "\n  %s (%d subject(s) EXITED without converging and the roster at this run BASE cannot be read, so whether a blocker was promoted CANNOT BE OBSERVED - a check that cannot look says so rather than passing)", f, nneed
          else if (newids + 0 < nneed)
            printf "\n  %s (%d subject(s) EXITED without converging and the generated units region gained only %d non-WONTDO unit id(s) this run BASE lacked, so at least one blocker was neither fixed nor promoted. This is a LOWER BOUND: it demands one surviving id per exited SUBJECT, not one per standing BLOCKER, because the region records ids and not which subject promoted them)", f, nneed, newids + 0
        }
        }
      }' "$rvf")"
  done
  [ -z "${rv_bad//[[:space:]]/}" ] || fail 2 "review loops that ran past the ceiling, stalled without recording it, or exited without accounting for their blockers:$rv_bad"
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

# ---- THE HOLD VOCABULARY, graded exactly as the halt one above it and never merged with it: a
# ---- halt code ENDS a run and a hold code PAUSES one, and one list would let a pause be recorded
# ---- as an ending. Its floor behaves the same way — undeclared or malformed is a REFUSAL, never a
# ---- defaulted value, because a pin that quietly defaults is a pin nobody set.
if [ -z "$HOLD_FLOOR" ]; then
  fail 2 "HOLD_FLOOR is undeclared in .unattended.conf, and with no floor a deleted hold code is indistinguishable from a vocabulary that never had one"
elif ! printf '%s' "$HOLD_FLOOR" | grep -qE '^[0-9]+$'; then
  fail 2 "HOLD_FLOOR is not a single integer, so the shrink-only comparison below would be a string test wearing a numeric name: $HOLD_FLOOR"
else
  nhold=$(printf '%s' "$HOLD_CODES_CORE" | wc -w)
  [ "$nhold" -ge "$HOLD_FLOOR" ] \
    || fail 2 "the kit's CORE hold vocabulary has shrunk below its floor, and deleting a member is a silent, reason-free override of every record and every sibling unit that routes to it: $nhold against $HOLD_FLOOR"
fi
if [ -z "$HOLD_CODES_CORE" ]; then
  fail 2 "the driver declares no HOLD_CODES_CORE vocabulary, so the hold verb would validate against an empty set and record a pause under any word at all: $DRIVER"
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
  [ -z "${hc_bad//[[:space:]]/}" ] || fail 2 "aborted run-state records whose halt code is missing or outside the effective vocabulary:$hc_bad"
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
  # THE ACT AXIS, joined to its WRITER the way the kind axis is joined to `park`. `verb_rescope`'s
  # act argument is a closed `case` alternation and is the only thing that can put an act into a row,
  # so an owed act outside it is a member no row can ever carry: the surfaced count silently returns
  # to what it was, the split's whole purpose reverts, and every gate and every criterion stays green.
  # A typo like `supercede` is exactly that, and is what this arm exists to catch.
  if [ -n "$PARK_ACTS_OWED" ]; then
    pa_case=$(grep -oE '^[[:space:]]*retire\|supersede\|add\)' "$DRIVER" | head -1)
    if [ -z "$pa_case" ]; then
      fail 2 "the driver declares owed rescope ACTS but this leg cannot find the closed act alternation --rescope validates against, so the act axis would be graded against nothing: $DRIVER"
    else
      pa_dead=""
      for pa in $PARK_ACTS_OWED; do
        printf '%s' "$pa_case" | grep -qE "(^|\|)[[:space:]]*$pa(\||\))" || pa_dead="$pa_dead $pa"
      done
      [ -z "$pa_dead" ] || fail 2 "the parked-ACT taxonomy names an act --rescope's own closed case cannot accept, so no row can ever carry it and the surfaced count is silently narrower than the set says:$pa_dead"
    fi
  else
    fail 2 "the driver declares no readable PARK_ACTS_OWED, so the act axis of the surfaced count would range over an empty set and a retirement would silently stop being owed: $DRIVER"
  fi
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
[ -n "${PHASES//[[:space:]]/}" ] \
  || fail 2 "the effective phase vocabulary is empty, which makes every phase check below vacuously true"
nphase=$(_wc=(${PHASES_CORE}); echo ${#_wc[@]})
if [ -n "${pfloor:-}" ] && [ "$nphase" -lt "$pfloor" ]; then
  fail 2 "the kit's CORE phase vocabulary has shrunk below its floor, and deleting a core member is a silent, reason-free override of everything keyed on it: $nphase against $pfloor"
fi
# A TERMINAL phase outside the vocabulary is unreachable, so no run could ever finish. Same vacuity
# from the other side — and this one IS falsifiable, because the two sets are declared independently.
for t in $PHASES_TERMINAL; do
  case " $PHASES " in *" $t "*) ;;
    *) fail 2 "a TERMINAL phase is not in the effective vocabulary, so no run could ever reach it: $t";; esac
done
[ -n "${DOD//[[:space:]]/}" ] \
  || fail 3 "the effective Definition-of-Done set is empty, so --close would block on nothing"
ndod=$(_wc=(${DOD_CORE}); echo ${#_wc[@]})
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

# ---- 38: NO PATH IS BOTH A SHARED RECORD AND A GENERATED INDEX. TOOL-dDerivedDocket-20 S1. The two
# ---- keys are condition 3's two halves and `--dispatch` answers each by its own rule, so one path
# ---- under both is answered by whichever rule the verb reaches first and the other declaration means
# ---- nothing. The driver refuses such a conf at load; this is the same library predicate on the bar,
# ---- which is what reaches a conf no run has read yet. CONTAINMENT in either direction, never string
# ---- equality, because `memory` beside a `memory/LIVE.md` index is the same contradiction.
# ----
# ---- WHAT THIS DOES NOT CHECK: that either key names the RIGHT paths. It compares the kit's own two
# ---- keys with each other and nothing else - no memory-tree state, no index on disk - which is what
# ---- lets it land unchanged in any adopter.
_c38=$(scan_shared_index_overlaps "$SHARED_RECORDS" "$GENERATED_INDEXES")
# A PROBE THAT CANNOT MOVE SAYS SO: over an empty index set this comparison passes by finding
# nothing, so the report channel names both populations it was handed.
read -ra _c38_s <<<"$SHARED_RECORDS"; read -ra _c38_g <<<"$GENERATED_INDEXES"
report "check 38 compared ${#_c38_s[@]} shared record(s) against ${#_c38_g[@]} index half(s)"
if [ -n "$_c38" ]; then
  # Formatted OUTSIDE the message: the arm meta-gate reads a branch's signature up to the message's
  # first closing quote, so a substitution quoting its own argument inside it would end the signature
  # on shell source no assertion can emit.
  _c38_pairs=$(printf '%s\n' "$_c38" | awk -F'\t' '{ printf "%sSHARED_RECORDS %s overlaps the index %s", (NR > 1 ? "; " : ""), $1, $2 }')
  fail 38 "a path is declared under both SHARED_RECORDS and GENERATED_INDEXES, so --dispatch answers it by whichever of condition 3's two rules it reaches first and the other declaration means nothing: $_c38_pairs"
fi

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
# THE BOUND IS 10 s AND IT IS NOT A TIMEOUT, IT IS A CAPABILITY PROBE. `true` returns instantly, so
# the only thing a bound can add here is a FALSE NEGATIVE: at the shipped `1` it was process-creation
# latency that tripped it, not a missing binary. MEASURED node `a` 2026-08-28, `timeout -k 1s 1 true`
# 0/40 failures quiet and 7/40 under eight concurrent spawn loops, while `timeout -k 1s 10 true` was
# 0/40 under that same load. That 17% is the whole of the run-gates canary's flakiness: the suite
# probes once while the box is quiet, the runner probes again under a full bar, they disagree, and an
# arm then blames `GATE_JOBS` or the clamp for a binary that was there the entire time. Raising the
# bound costs nothing -- it is only ever reached if `timeout` genuinely hangs. TOOL-aSiftedFork-7.
timeout -k 1s 10 true >/dev/null 2>&1 || REMOTE_BOUND_LIVE=0
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
# ---- TWO GIT PROCESSES FOR THE WHOLE FUNCTION, however many commits it judges.
# ---- TOOL-aQuenchedHarness-10.
#
# `is_published` asks one question — is this commit an ancestor of ANY tip the remote advertises —
# and it used to answer it with two processes per commit per tip: `cat-file -e` to see whether the
# tip is readable, then `merge-base --is-ancestor`. Measured on this repo: 87 identical `cat-file -e`
# calls for `$ADV_HEAD` alone and 121 ancestry calls, every one of them against that same tip.
#
# ANCESTOR-OF-ANY IS A UNION, so it is ONE walk and not one per tip. `merge-base --is-ancestor A B`
# is true exactly when A is reachable from B, and `git rev-list B C D` enumerates everything
# reachable from B or C or D — so the union set answers the disjunction directly. A first attempt at
# this warmed one set per tip and cost 8.88 s against 1.31 s for the union, on the 28 heads this
# origin advertises; that mistake is recorded here because the per-tip shape looks more careful and
# is strictly worse.
#
# THE `miss` LIMB IS WHY EXISTENCE IS STILL ASKED SEPARATELY. The function must return 2 —
# CANNOT TELL — when any advertised tip is unreadable, and a union walk cannot distinguish "absent
# from the union" from "a tip we could not read". One `cat-file --batch-check` answers existence for
# every tip in one process, and it NORMALISES too: the reply's first field is the full 40-hex sha,
# which is what makes an abbreviated record fact like `witness: a9560632` comparable against a set
# of full shas instead of silently missing it.
# Whether the advertised HEAD is readable here is fixed for the run; it was being re-asked once
# per record, 36 times, always about the same sha.
ADV_HEAD_OK=0
if [ -n "$ADV_HEAD" ] && GIT cat-file -e "$ADV_HEAD^{commit}" 2>/dev/null; then ADV_HEAD_OK=1; fi

declare -A _PUB_REACH
_PUB_WARMED=0
_PUB_MISS=0
_load_pub_reach() {
  [ "$_PUB_WARMED" = 1 ] && return 0
  _PUB_WARMED=1
  local _t _h _present="" _sha _ty
  # ---- ONE PROCESS: which advertised tips are readable, and what their full shas are.
  # `cat-file --batch-check` prints `<oid> <type> <size>` and does NOT echo its input, so the
  # TYPE IS THE SECOND FIELD. Reading it as the third made every tip look unreadable and turned
  # every answer into CANNOT TELL, which reds check 9 on every record in the tree. The A/B that
  # should have caught it ran against a clone with the remote detached, so `$ADV_TIPS` was empty
  # and this function never ran at all. A fixture that disables the path under test measures the
  # other paths twice. TOOL-aQuenchedHarness-10.
  while read -r _sha _ty _; do
    case "$_ty" in
      commit) _present="$_present $_sha" ;;
      *)      _PUB_MISS=1 ;;
    esac
  done < <(for _t in $ADV_HEAD $ADV_TIPS; do [ -n "$_t" ] && printf '%s^{commit}\n' "$_t"; done \
           | GIT cat-file --batch-check 2>/dev/null)
  # ---- one process: everything reachable from any of them
  [ -n "$_present" ] || return 0
  while IFS= read -r _h; do
    [ -n "$_h" ] && _PUB_REACH[$_h]=1
  done < <(GIT rev-list $_present 2>/dev/null)
  return 0
}

# Full sha for a rev, through the same batch, so an abbreviation is comparable. Falls back to the
# rev itself when nothing resolves, which keeps the caller's own miss handling in charge.
declare -A _PUB_FULL
resolve_full_sha() {  # rev -> full sha, or empty
  [ -n "${_PUB_FULL[$1]+x}" ] && { printf '%s' "${_PUB_FULL[$1]}"; return 0; }
  local _r
  # The batch above has already resolved every rev recorded in a run-state file, which is where
  # every abbreviated fact this leg judges comes from. Only something outside that set costs a
  # process here.
  _load_rev_table
  _r=${_REV_FULL[$1]:-}
  [ -n "$_r" ] || _r=$(GIT rev-parse --verify --quiet "$1^{commit}" 2>/dev/null) || _r=""
  _PUB_FULL[$1]=$_r
  printf '%s' "$_r"
}

is_published() { # commit -> 0 published · 1 not published · 2 CANNOT TELL, a tip could not be read
  # THE INVARIANT IS "EVERY TIP WAS READABLE", not "at least one was". The first cut tracked PRESENCE
  # and returned 2 only when ALL advertised tips were absent, so a single stale locally-present branch
  # restored the forgery-shaped false red for every record. Reproduced against this clone: three tips
  # advertised, one present and two absent, so `have` was 1 and the answer came back a definite
  # "not published" computed from a third of the evidence. Sound form: not-published requires that no
  # present tip contains the commit AND that nothing was unreadable; anything less is cannot-tell.
  # ---- THE TIPS ARE RESOLVED ONCE, NOT ONCE PER COMMIT. TOOL-aQuenchedHarness-10.
  #
  # `$ADV_HEAD` and `$ADV_TIPS` are fixed for the whole run: they come from one `ls-remote`
  # observation before any record is read. This function was re-asking git whether each of them
  # EXISTS on every call, and it is called once per commit under judgement — measured at 87
  # `cat-file -e` calls for `$ADV_HEAD` alone in a single run of this leg, all of them the same
  # question with the same answer.
  #
  # AND ANCESTOR-OF-ANY IS ONE UNION WALK, not 121 processes and not one walk per tip.
  # `merge-base --is-ancestor A B` is true exactly when A is reachable from B, and
  # `git rev-list B C D` enumerates everything reachable from B or C or D — so the union answers the
  # disjunction directly. Same reachability relation, same reflexive case: rev-list emits B itself,
  # and B is an ancestor of itself. A first cut warmed one set PER TIP and cost 8.88 s against
  # 1.31 s for the union over the 28 heads this origin advertises, so the per-tip shape looks more
  # careful and is strictly worse.
  #
  # AN ABBREVIATED COMMIT IS NORMALISED rather than missed. A 40-char set cannot answer an 8-char
  # argument, and answering "not published" there would turn a real publication into a red.
  _load_pub_reach
  local c="$1" _full
  # A FULL SHA COSTS NO PROCESS AT ALL: it is a table lookup. Only an abbreviation needs
  # resolving, and this tree holds very few, so the fallback runs a handful of times rather than
  # once per record. Normalising unconditionally would have put a `rev-parse` back on every
  # record and given back most of what the union walk just bought.
  if [ ${#c} = 40 ]; then
    [ -n "${_PUB_REACH[$c]+x}" ] && return 0
  else
    _full=$(resolve_full_sha "$c")
    [ -n "$_full" ] && [ -n "${_PUB_REACH[$_full]+x}" ] && return 0
  fi
  # Not reachable. Whether that means NOT PUBLISHED or CANNOT TELL is the same question it always
  # was: it is only a definite answer when every advertised tip was readable.
  [ "$_PUB_MISS" = 0 ] || return 2
  return 1
}

# ------------------------------------------ which commit INTRODUCED a line in a run-state record
# TOOL-dDerivedDocket-52. Unit 18's S2 re-derives a run's `m-base:` from the commit that first
# recorded it, and its S8 does the same for `asks-at-landing:`. Both need ONE answer to "which
# commit introduced this line in this record", and both need to be told when there is no answer
# rather than handed a plausible wrong one.
#
# WHAT THIS DOES NOT ANSWER, first, because a resolver read as a guarantee is worse than none: it
# answers only inside the queried record's own tenancy of that path, says nothing about an earlier
# run's copy at the same path, and does not follow a record moved out of its build folder.
#
# WHY A PATH-SCOPED SEARCH IS NOT THE ANSWER. `--preflight` retires a terminal record by renaming it
# INSIDE its own folder and writing a fresh live record in the same commit, so the archived path
# exists and a search scoped to it answers with the ROTATION commit - a wrong sha, not a missing one.
# Measured on this tree 2026-09-20 over `RUN.LANDED.a1fd98d8.md`: the archived path alone answers the
# rotation (2026-08-20), the two paths together answer the run's own preflight (2026-08-18).
#
# WHY NOT `--diff-filter=A`, the obvious spelling for both ends of the window. A rotation is not a
# rename and not a delete-and-add to git - it records `A` the archived record and `M` the live one -
# so the newest ADD at a path is the FIRST run's add and not the current tenant's. Worse, and
# measured in a scratch repo on 2026-09-21: when the rotation lands inside a MERGE commit, an add
# search over the archived path answers NOTHING, under the plain spelling AND under
# `--full-history`, because git computes no diff for a merge. That is the class
# `tools/memory-tree/row_grammar.py:335-340` records for two of this repo's own archives. Both ends
# of the window are therefore resolved by FIRST TOUCH, which a merge cannot hide.
#
# WHY `--full-history` EVERYWHERE. A path-restricted walk drops a commit TREESAME with a parent, and
# a merge that resolves the record to its first parent's side prunes the whole branch that touched
# it. Measured in a scratch repo on 2026-09-21 with an `-s ours` merge: the plain walk loses the
# commit that introduced the line and answers nothing at all; the unsimplified walk keeps it.
# `tools/drift-audit/drift_report.py:806-818` reproduced the same class for the same flag.
#
# THE TENANCY FLOOR IS THE MECHANISM, not a refinement. Two runs share one path, and their records
# share whole lines - `memory/builds/aBoundedVerdict/RUN.md` and its ABORTED sibling carry thirteen
# identical non-blank lines today. Unfloored, a search for one of them answers the FIRST run's
# preflight (`e8be30e9`, 40 commits walked) instead of the queried record's own (`9ea808cf`, 24).
# The verification below cannot catch that and is not asked to: `e8be30e9`'s first parent carries no
# record at all, so "the parent does not have the line" is true of a commit made the day before the
# queried record existed. A boundary is where one run's tenancy of a path ends and the next begins -
# the first touch of the live record, and the first touch of every archived sibling beside it.
#
# THE CAP DETECTS A WINDOW, it never SELECTS one, and the direction is why. The answer sits at the
# OLDEST end, while `--max-count` applies during a newest-first traversal - so `--reverse
# --max-count=N` keeps the N NEWEST commits and discards the only end that can hold the answer. That
# is the defect `tools/unattended/lib-unattended.sh:266-279` records against its own sibling walk.
# So `cap+1` is FETCHED, the verdict is reached from the whole emitted list BEFORE any candidate is
# graded, and a window deeper than the cap is announced rather than answered. A sentinel met
# mid-walk would return a RE-introduction among the retained newest commits, which is a wrong sha
# wearing the face of an answer.
#
# THE CAP LIVES IN THIS FUNCTION, not beside it, and that is an arming decision: the bound arms
# extract this function with `sed` and source it, so a constant one line up would have to be
# re-declared by the suite, and the arms would then grade a cap they wrote themselves. THE VALUE IS
# NOT REPEATED IN THIS PARAGRAPH, it is the default two lines down: it is the sibling bound's own
# (`PASS_ORDER_PREANCHOR_CAP`, in this kit's pass-order leg). The floor under any value is measured:
# the deepest floored window on this tree at HEAD is 60 commits, on
# `memory/builds/dRetiredFork/RUN.md`, so a cap at or below that announces on this repo's own
# deepest record.
#
# A NAMED EMPTY, NEVER SILENCE. Four reasons are distinguished by text, on stderr - the channel
# `pass_commit` already uses for the same shape, and the one that leaves this leg's "exit 0 and no
# output is clean" contract on stdout untouched. An empty answer is the caller's cue to take the
# weaker ancestry reading; an empty answer with no reason is indistinguishable from a clean one.
resolve_introducing_commit() { # run-state path · literal line -> the introducing sha, or a NAMED empty
  local _rel=$1 _line=$2
  local _cap=${INTRODUCING_WALK_CAP:-400}
  local _why="unattended-check: resolve_introducing_commit cannot name the commit that introduced a line in"
  local _dir _base _tip _ceil _floor _sib _b _bn _bestn _p _par _c _own _phas _n _i
  local _paths=() _all=()

  _tip=$(GIT rev-parse --verify --quiet 'HEAD^{commit}' 2>/dev/null) || _tip=""
  if [ -z "$_tip" ]; then
    printf '%s %s: the range could not be resolved - this checkout has no HEAD commit to walk back from\n' "$_why" "$_rel" >&2
    return 1
  fi
  case $_rel in */*) _dir=${_rel%/*} ;; *) _dir=. ;; esac
  _base=${_rel##*/}

  # ---- THE PATH SET. The record's own path, plus - where that path is an archived name - the live
  # ---- record beside it, DERIVED the way the rotation builds its name (the record's own folder,
  # ---- then the live basename) rather than by re-spelling the archived name's grammar.
  if [ "$_base" = RUN.md ]; then _paths=("$_rel"); else _paths=("$_rel" "$_dir/RUN.md"); fi

  # ---- THE CEILING. For the live record it is HEAD. For an archived one it is that path's own first
  # ---- touch - the rotation - because the record's bytes lived at the live path for exactly the
  # ---- span ending there, and everything after it at that path belongs to the next run.
  if [ "$_base" = RUN.md ]; then
    _ceil=$_tip
  else
    _ceil=$(GIT rev-list --full-history "$_tip" -- "$_rel" 2>/dev/null | tail -1)
    if [ -z "$_ceil" ]; then
      printf '%s %s: the range could not be resolved - no commit reachable from HEAD touches this archived record\n' "$_why" "$_rel" >&2
      return 1
    fi
  fi

  # ---- THE FLOOR: the NEWEST tenancy boundary at or before the ceiling. Distance to the ceiling
  # ---- decides which is newest, because a boundary's ancestor set is what orders it - commit dates
  # ---- do not, and this repo's own nodes disagree about the clock.
  _floor=""; _bestn=""
  for _sib in $(GIT ls-tree --name-only "$_ceil" "$_dir/" 2>/dev/null); do
    case ${_sib##*/} in RUN*.md) ;; *) continue ;; esac
    # THE QUERIED ARCHIVED PATH IS NOT ITS OWN BOUNDARY - its first touch IS the ceiling, and a
    # window cannot be floored at its own top. The LIVE record must NOT take this branch: its own
    # first touch is a boundary, and in a folder that has never rotated it is the only one. Keying
    # this on `first touch == ceiling` instead read a record whose only touch is the tip as having
    # no floor at all, which is every record in a shallow clone - measured 2026-09-21, and the
    # reason that spelling is written down here rather than left as a diff.
    if [ "$_base" != RUN.md ] && [ "$_sib" = "$_rel" ]; then continue; fi
    _b=$(GIT rev-list --full-history "$_ceil" -- "$_sib" 2>/dev/null | tail -1)
    [ -n "$_b" ] || continue
    _bn=$(GIT rev-list --count "$_b..$_ceil" 2>/dev/null) || continue
    case ${_bn:-x} in ''|*[!0-9]*) continue ;; esac
    if [ -z "$_bestn" ] || [ "$_bn" -lt "$_bestn" ]; then _bestn=$_bn; _floor=$_b; fi
  done
  if [ -z "$_floor" ]; then
    printf '%s %s: the tenancy floor could not be resolved, so the only walk left would cross into an earlier run copy of this path\n' "$_why" "$_rel" >&2
    return 1
  fi

  # ---- A GRAFTED OLDEST END IS NOT AN OLDEST END. In a shallow clone the boundary commit has no
  # ---- parents present, so every file in it reads as introduced there - measured 2026-09-21, an
  # ---- add search in a `--depth 2` clone answers the graft commit for a record created long before
  # ---- it. The floor is exactly where this function stops applying the parent test, so a graft at
  # ---- the floor turns the one unverified candidate into a confident wrong answer.
  for _p in $(GIT cat-file commit "$_floor" 2>/dev/null | sed -n '/^$/q; s/^parent //p'); do
    GIT cat-file -e "$_p^{commit}" 2>/dev/null && continue
    printf '%s %s: the range could not be resolved - the oldest end of the window names a parent this repository does not have, which is a shallow or grafted history\n' "$_why" "$_rel" >&2
    return 1
  done

  # ---- THE CANDIDATES, newest-first and bounded at cap+1 so the traversal is bounded and the
  # ---- truncation verdict is EXACT: with `--max-count=$_cap` a complete walk of an exactly-cap-deep
  # ---- window is indistinguishable from a truncated one. `--not <floor>^@` includes the floor
  # ---- itself, which `<floor>..<ceiling>` would drop - and the floor is usually the preflight
  # ---- commit the search is looking for.
  _all=( $(GIT rev-list --full-history --max-count=$((_cap + 1)) "$_ceil" --not "$_floor^@" -- "${_paths[@]}" 2>/dev/null) )
  _n=${#_all[@]}
  if [ "$_n" -gt "$_cap" ]; then
    printf '%s %s: the tenancy window is deeper than the %s-commit walk cap, so its oldest end - where an introduction lives - was never fetched and the answer is UNKNOWN rather than absent\n' "$_why" "$_rel" "$_cap" >&2
    return 1
  fi

  # ---- GRADED OLDEST FIRST, over the list reversed HERE rather than by `--reverse`, which reverses
  # ---- after the cap has already discarded the oldest end.
  _i=$((_n - 1))
  while [ "$_i" -ge 0 ]; do
    _c=${_all[$_i]}
    _i=$((_i - 1))
    # The record at this commit, read at the first path of the set that exists there: the queried
    # path where it is already the record's home, the live path before the rotation moved it.
    _own=""
    for _p in "${_paths[@]}"; do
      GIT cat-file -e "$_c:$_p" 2>/dev/null || continue
      GIT show "$_c:$_p" 2>/dev/null | tr -d '\r' | grep -qxF -- "$_line" && _own=1
      break
    done
    [ -n "$_own" ] || continue
    # AT THE FLOOR THE PARENT TEST IS NOT APPLIED, and this is the one exception rather than an
    # escape hatch: the parent's copy there is ANOTHER run's record at the same path, so comparing
    # them is the collision the floor exists to close. Everywhere else, "introduced" means the first
    # parent's copy did NOT carry the line - including the case where the record does not exist at
    # the first parent, which is what a preflight commit looks like.
    if [ "$_c" = "$_floor" ]; then printf '%s' "$_c"; return 0; fi
    _par=$(GIT rev-parse --verify --quiet "$_c^1^{commit}" 2>/dev/null) || _par=""
    if [ -z "$_par" ]; then printf '%s' "$_c"; return 0; fi
    _phas=""
    for _p in "${_paths[@]}"; do
      GIT cat-file -e "$_par:$_p" 2>/dev/null || continue
      GIT show "$_par:$_p" 2>/dev/null | tr -d '\r' | grep -qxF -- "$_line" && _phas=1
      break
    done
    [ -n "$_phas" ] && continue
    printf '%s' "$_c"; return 0
  done
  printf '%s %s: the whole tenancy window was walked and no commit in it introduced that line\n' "$_why" "$_rel" >&2
  return 1
}


# ================ THE ASK MANDATE, SECOND-OPINIONED — TOOL-dDerivedDocket-18 ======================
# Unit 16 pins `asks:`, `m-base:` and `asks-ready:` at preflight and unit 17 freezes
# `asks-at-landing:` at the landing. Every one of those facts is written into a run-state file BY
# THE RUN BEING GRADED, so the bar needs its own reading of each, re-derived from inputs the run
# cannot move. That is the pattern check 19 already applies to `authorized-by:`, `playbook:` and
# `pieces:`, extended to the four facts the ask path adds.
#
# A SECOND OPINION AND NOT A SECOND IMPLEMENTATION. Nothing here re-implements the READY rule or
# the status fold: the arm below re-RUNS the project's own declared producer over the inputs the
# record pinned and compares. The independence is in the INPUTS, never in a second grammar — which
# is why the ask-row match, the id-range expander and the filing home are the kit library's,
# shared with the driver, rather than spelled a second time here.
#
# WHAT THESE ARMS DO NOT CHECK, said here because a structural check reads as a semantic one to
# everybody who did not write it:
#   * a declared producer that cannot be run, breaches the bound, or answers in a shape this leg
#     refuses is reported UNANSWERED and never red. "This pin is forged" and "nobody could ask" are
#     different claims, and a bar that reds on a broken external command sends its reader at the
#     wrong thing. A forged pin behind a broken producer is therefore invisible here.
#   * a record whose preflight commit is already reachable from the advertised default tip is
#     counted and NOT re-derived, so a pin that was wrong when written and has since landed is out
#     of reach here for ever. That is the price of never grading an archived record against a
#     producer whose rules moved after it landed.
#   * the freeze is re-derived at the FIRST PARENT of the commit that introduced it, which is the
#     tree the landing verb examined under both lander modes. A project whose lander commits the
#     record somewhere else gets a re-derivation of a different tree — and that is a RED here, not
#     a skip, because the leg cannot tell it from a forged freeze.
#   * `anchor-sha:` and the recorded BASE are themselves written by the run. S2 grades `m-base:`
#     against the anchor the record pins and does not re-observe that anchor; what grades the pin
#     is check 9's reading of the remote's own advertisement, and in the end the same leg re-run in
#     a clone the run never touched - check 13's honest limit, and it applies here unchanged.
#   * none of it says the asks were answered WELL. It says the facts on the record are the ones its
#     own declared inputs produce.

# The `asks:` value out of a build README blob's front matter, parsed HERE rather than read back
# from the record — the same shape as the `authorized-by:` and `playbook:` reads in check 19 above.
# FRONT MATTER ONLY, closing on the first `---` after line 1, for the reason that parse gives: `---`
# is also a horizontal rule, so a scan running to the end of the file could take an `asks:` line out
# of the body and read a sentence as a mandate.
read_asks_of() { # README blob text -> the asks: value, or nothing
  printf '%s\n' "$1" | awk '
    NR == 1 { next }
    /^---[[:space:]]*\r?$/ { exit }
    /^asks:/ { v = $0; sub(/^asks:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print v; exit }'
}

# ---- TOOL-dDerivedDocket-19 - THE GRANT LINE, read the way `read_asks_of` reads the mandate: an
# ---- independent parse of the same blob, first line of the key, front matter only. It returns
# ---- `may=<value>` rather than the bare value, because PRESENCE is the fact the grant arms turn on:
# ---- an absent key means `none` and an empty one is a malformed grant, and a bare empty string
# ---- cannot tell them apart.
read_may_of() { # README blob text -> `may=<value>` when the front matter carries the key, or nothing
  printf '%s\n' "$1" | awk '
    NR == 1 { if ($0 !~ /^---[[:space:]]*\r?$/) exit; next }
    /^---[[:space:]]*\r?$/ { exit }
    /^may:/ { v = $0; sub(/^may:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print "may=" v; exit }'
}

# ---- TOOL-dDerivedDocket-19 S4, the cross-run arm's reader. Given a run's OWN commits on stdin, one
# ---- per line: every commit that WRITES a `may:` front-matter line into a build README, printed as
# ---- `<commit> <README>`. ANY build README, the run's own included: a README a run lands on the
# ---- default branch is one the NEXT run is authorized by, so a grant there is a grant between runs.
# ----
# ---- A TWO-PARENT COMMIT ANSWERS ONLY FOR THE LINES NEITHER PARENT HOLDS. Its first-parent diff
# ---- carries everything the other parent brought in, which for a reconcile is default-branch
# ---- content - an owner's hand-typed grant among it, the one channel ruling D12-j keeps open. So a
# ---- merge is read by its COMBINED diff, and a line counts only where every prefix column is `+`;
# ---- each parent's own commits in the range are graded where they were made.
# ----
# ---- TWO STAGES, and the second is what makes the first safe to be generous. ONE `diff-tree --stdin`
# ---- over the whole list, restricted to README paths, names the candidates; each is then settled by
# ---- reading the key out of the FRONT MATTER at the commit and at every parent, and it is a write
# ---- only when the key is present at the commit and differs from what every parent carries. A body
# ---- line that happens to start `may:` is therefore no grant, and a merge that took one side's line
# ---- verbatim wrote nothing. The comparison is RAW: rewriting a grant's spelling is a write.
# ----
# ---- WHAT IT DOES NOT SEE: a README under a path other than `<MEMORY_ROOT>/builds/<slug>/README.md`,
# ---- and a grant a run carries in some other file. Neither is a place the driver reads a grant from.
scan_grant_writes() { # stdin: commit ids -> `<commit> <README>` per commit that writes a may: line into one
  local _sg_c _sg_p _sg_new _sg_par _sg_hit
  GIT diff-tree --stdin -r -p --cc --no-renames --no-ext-diff --no-textconv --format='commit %H %P' \
      -- "$M/builds/*/README.md" 2>/dev/null \
    | awk -v pre="$M/builds/" '
        /^commit [0-9a-f]+/ { c = $2; np = NF - 2; f = ""; inh = 0; next }
        /^diff --git / { f = $NF; sub(/^b\//, "", f); inh = 0; next }
        /^diff --(cc|combined) / { f = $NF; inh = 0; next }
        /^@@/ { inh = 1; next }
        inh == 1 {
          w = (np > 1) ? np : 1
          lead = substr($0, 1, w); body = substr($0, w + 1)
          if (body ~ /^may:/ && lead !~ /[^+]/ && index(f, pre) == 1 \
              && substr(f, length(pre) + 1) ~ /^[^\/]+\/README\.md$/) print c " " f
        }' | sort -u \
    | while read -r _sg_c _sg_p; do
        [ -n "$_sg_p" ] || continue
        _sg_new=$(read_may_of "$(GIT show "$_sg_c:$_sg_p" 2>/dev/null)")
        [ -n "$_sg_new" ] || continue
        _sg_hit=1
        for _sg_par in $(GIT rev-list --parents -n 1 "$_sg_c" 2>/dev/null | cut -d' ' -f2-); do
          [ "$(read_may_of "$(GIT show "$_sg_par:$_sg_p" 2>/dev/null)")" = "$_sg_new" ] && _sg_hit=0
        done
        [ "$_sg_hit" = 1 ] && printf '%s %s\n' "$_sg_c" "$_sg_p"
      done
}

# ---- THE DECLARED PRODUCER, RUN BOUNDED. S8 re-runs the driver's own two call shapes —
# ---- `<ASKS_CMD> --tsv --ready <ids> --target <slug> --at <rev>` — over the inputs a record pinned.
# ---- `$ASKS_CMD` IS UNQUOTED, exactly as `$WIRING_CHECK`, `$LANDER` and `$GATE_CMD` are in the
# ---- driver, so a project may declare a launcher and a script rather than one word.
# ----
# ---- CAPTURED THROUGH A FILE AND NOT A SUBSTITUTION. `out=$(timeout N cmd)` reads until EOF and a
# ---- surviving descendant holds the pipe, so the verdict would be bounded while the clock is not —
# ---- the defect this leg already records against its own remote observation.
# ----
# ---- THE BOUND IS THE ONE THIS LEG ALREADY READS FROM THE DRIVER. A second number declared here
# ---- would be a bound that goes wrong silently when the driver's moves, and the driver's own
# ---- `GATE_BOUND` is an hour — a figure written for a whole merge bar and not for one leg of one.
# ---- A BREACH IS UNANSWERED, NEVER A RED: "this ask is not ready" and "nobody asked" are not the
# ---- same claim, and this leg says which it observed.
AQ_ROWS=""; AQ_WHY=""
run_ask_query() { # target slug · rev · ids… -> 0 and AQ_ROWS (id TAB status TAB ready), or 1 and AQ_WHY
  local _tgt="$1" _rev="$2" _rc _aqd _id _bad
  shift 2
  AQ_ROWS=""; AQ_WHY=""
  if [ -z "$ASKS_CMD" ]; then
    AQ_WHY="this project declares no ASKS_CMD, so there is no producer to re-run and nothing here could grade a pinned mandate"
    return 1
  fi
  read_ask_tsv_contract
  if [ -z "$ASK_TSV_HEAD" ] || [ -z "$ASK_TSV_EXAMINED" ] || [ -z "$ASK_TSV_FIELDS" ]; then
    AQ_WHY="the driver declares no readable projection contract — its row keyword, its examined keyword or its field count — so a positional read of the producer's rows here would report columns nobody printed"
    return 1
  fi
  _aqd=$(mktemp -d) || { AQ_WHY="cannot create a capture directory, so this leg observed NOTHING of the declared producer; that is a fault on THIS side rather than an answer about any pin"; return 1; }
  if [ "$REMOTE_BOUND_LIVE" = 1 ]; then
    timeout -k 5s "$REMOTE_BOUND" $ASKS_CMD --tsv --ready "$@" --target "$_tgt" --at "$_rev" \
      </dev/null >"$_aqd/out" 2>"$_aqd/err"
    _rc=$?
  else
    $ASKS_CMD --tsv --ready "$@" --target "$_tgt" --at "$_rev" \
      </dev/null >"$_aqd/out" 2>"$_aqd/err"
    _rc=$?
  fi
  # ONE AWK over the whole stream, in the driver's own projection order, keeping the three columns
  # every caller here reads. Anything that is neither a row of the declared width nor the declared
  # `examined` line emits a `BAD` line and stops, so the refusal can quote what it refused.
  # STDOUT ONLY. The producer's notices are on stderr by contract (TOOL-dDerivedDocket-48), and a
  # parse that refused any line not leading with the row keyword would read a HEALTHY producer as a
  # malformed one.
  AQ_ROWS=$(ASK_HEAD="$ASK_TSV_HEAD" ASK_EX="$ASK_TSV_EXAMINED" ASK_N="$ASK_TSV_FIELDS" awk -F'\t' '
      BEGIN { h = ENVIRON["ASK_HEAD"]; ex = ENVIRON["ASK_EX"]; want = ENVIRON["ASK_N"] + 0 }
      $0 == "" { next }
      $1 == ex { next }
      $1 == h && NF == want { print $2 "\t" $3 "\t" $7; next }
      { print "BAD\t" $0; exit }' "$_aqd/out")
  _bad=$(printf '%s\n' "$AQ_ROWS" | sed -n 's/^BAD\t//p' | sed -n 1p)
  rm -rf "$_aqd" 2>/dev/null
  if [ "$_rc" = 124 ]; then
    AQ_ROWS=""
    AQ_WHY="the declared producer was KILLED by this leg's wall-clock bound of ${REMOTE_BOUND}s rather than answering, so the pin was NEVER ANSWERED here; that is a stalled or absent generator and not a statement about the pin"
    return 1
  fi
  if [ -n "$_bad" ]; then
    AQ_ROWS=""
    AQ_WHY="the declared producer printed a line that is not the $ASK_TSV_FIELDS-field $ASK_TSV_HEAD projection, so a positional read of it would report fields nobody printed — the line: $_bad"
    return 1
  fi
  if [ "$_rc" != 0 ]; then
    AQ_ROWS=""
    AQ_WHY="the declared producer exited $_rc, so the rows it printed are not an answer this leg may grade a pin against"
    return 1
  fi
  # THE MANDATE IS ITERATED, NEVER THE ROWS. A loop over what came back can only confirm what came
  # back: a producer that dropped an id would be graded on the ids it did return, and the missing
  # one would never be mentioned at all.
  for _id in "$@"; do
    printf '%s\n' "$AQ_ROWS" | cut -f1 | grep -qxF -- "$_id" && continue
    AQ_ROWS=""
    AQ_WHY="DEAD PROBE — the declared producer answered for fewer asks than it was asked about, and an id it never graded is an id nothing here can compare: $_id is missing from its rows"
    return 1
  done
  return 0
}
# One projected row's field, BY NAME, so no caller here counts tabs.
read_ask_row() { # ask id · status|ready -> the value, or nothing
  local _n
  case "$2" in status) _n=2 ;; ready) _n=3 ;; *) return 0 ;; esac
  printf '%s\n' "$AQ_ROWS" | awk -F'\t' -v i="$1" -v n="$_n" '$1 == i { print $n; exit }'
}

# ---- S3's ANCHOR JUDGEMENT, THROUGH THE RECALL KIT'S OWN EXTRACTOR. Whether a line ANCHORS an id
# ---- (defines the record) or merely cites one is that kit's `anchor_at`, and a local list of the
# ---- shapes it admits is two copies of one grammar: they disagree silently, and the copy is always
# ---- the one that rots. The extractor is reached through the DECLARED `RECALL_CLI`, whose
# ---- directory holds it — a kit file may name nothing outside itself by literal, and a
# ---- `tools/<kit>/` spelling resolves to nothing in an adopter installed at another prefix.
# ----
# ---- A BLANK KEY, A MISSING EXTRACTOR AND AN UNRESOLVABLE INTERPRETER ARE THREE NAMED SKIPS. None
# ---- of them is zero anchors found, and the caller prints which one it took.
ASK_ANCHOR_PY='
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, sys.argv[1])
try:
    import extract
except Exception as exc:
    sys.stderr.write("the anchor extractor did not import: %s\n" % exc)
    raise SystemExit(3)
try:
    g = extract.grammar_for(sys.argv[2])
except Exception as exc:
    sys.stderr.write("the anchor extractor could not bind a grammar: %s\n" % exc)
    raise SystemExit(3)
slug = sys.argv[3]
for raw in sys.stdin.read().split("\n"):
    path = raw.rstrip("\r")
    if not path:
        continue
    try:
        with open(path, "rb") as fh:
            body = fh.read().decode("utf-8", "replace")
    except OSError:
        continue
    for i, line in enumerate(body.replace("\r\n", "\n").split("\n"), 1):
        got = extract.anchor_at(line, g)
        if not got:
            continue
        home = got.split("-", 1)[1].rsplit("-", 1)[0]
        if home != slug:
            sys.stdout.write("%s\t%d\t%s\n" % (path, i, got))
'
ASK_ANCHORS=""; ASK_ANCHOR_WHY=""
scan_foreign_anchors() { # build folder · slug -> 0 and ASK_ANCHORS, or 1 and ASK_ANCHOR_WHY
  local _dir="$1" _slug="$2" _rdir _ext _py _rc _askd
  ASK_ANCHORS=""; ASK_ANCHOR_WHY=""
  if [ -z "$RECALL_CLI" ]; then
    ASK_ANCHOR_WHY="RECALL_CLI is blank in this project, so the recall kit is not adopted here and the anchor grammar this arm judges by is absent — which is NOT the same answer as no foreign anchor found"
    return 1
  fi
  case "$RECALL_CLI" in */*) _rdir="${RECALL_CLI%/*}" ;; *) _rdir="." ;; esac
  _ext="$_rdir/extract.py"
  if [ ! -f "$_ext" ]; then
    ASK_ANCHOR_WHY="the declared RECALL_CLI names a directory that holds no anchor extractor, so there is no grammar to read and a local copy of its shapes would be a second one: $_ext"
    return 1
  fi
  _py=$(resolve_python 2>/dev/null) || _py=""
  if [ -z "$_py" ]; then
    ASK_ANCHOR_WHY="no python launcher on this node RAN, so the anchor extractor could not be reached; every candidate is executed rather than looked up, because being on PATH is not evidence"
    return 1
  fi
  _askd=$(mktemp -d) || { ASK_ANCHOR_WHY="cannot create a capture directory, so the anchor extractor was never run and this folder went unjudged"; return 1; }
  GIT ls-files -- "$_dir" >"$_askd/files" 2>/dev/null
  if [ "$REMOTE_BOUND_LIVE" = 1 ]; then
    timeout -k 5s "$REMOTE_BOUND" "$_py" -c "$ASK_ANCHOR_PY" "$_rdir" "$ROOT" "$_slug" \
      <"$_askd/files" >"$_askd/out" 2>"$_askd/err"
    _rc=$?
  else
    "$_py" -c "$ASK_ANCHOR_PY" "$_rdir" "$ROOT" "$_slug" \
      <"$_askd/files" >"$_askd/out" 2>"$_askd/err"
    _rc=$?
  fi
  ASK_ANCHORS=$(cat "$_askd/out" 2>/dev/null)
  ASK_ANCHOR_WHY=$(sed -n 1p "$_askd/err" 2>/dev/null)
  rm -rf "$_askd" 2>/dev/null
  if [ "$_rc" != 0 ]; then
    ASK_ANCHORS=""
    [ -n "$ASK_ANCHOR_WHY" ] || ASK_ANCHOR_WHY="the anchor extractor exited $_rc without saying why"
    return 1
  fi
  ASK_ANCHOR_WHY=""
  return 0
}
# ---- TOOL-dDerivedDocket-22 S10 - THE LANDED FACT-SET ARM'S SWITCH, and the landing shape it grades
# ---- under. A malformed cutoff is a REFUSAL rather than a default, for DISPOSITION_CUTOFF's reason: a
# ---- string compared against a date grades every record or none and nobody can tell which. A BLANK
# ---- one turns the arm off and says so on the report channel, where this leg announces every case
# ---- it could not reach, so a disabled arm never reads as one that found nothing.
LFC_ON=0; LFC_MODE=${LANDER_MODE:-primary}; lfc_n_landed=0; lfc_n_derived=0; lfc_n_landing=0
if [ -n "$LANDED_FACTS_CUTOFF" ]; then
  case "$LANDED_FACTS_CUTOFF" in
    [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) LFC_ON=1 ;;
    *) fail 15 "LANDED_FACTS_CUTOFF is declared and is not an ISO date, and a cutoff nothing can compare would grade every landed record or none while reading as configured: $LANDED_FACTS_CUTOFF" ;;
  esac
else
  report "the landed fact-set arm of check 15 is OFF - LANDED_FACTS_CUTOFF is blank or undeclared, so no landed or committed LANDING record is graded for the facts its landing verb writes"
fi
live=""; nlive=0
# TOOL-dDerivedDocket-18 - how many records pin an asks: fact, and how many of those were already
# published and so deliberately not re-derived. Counted here rather than derived after the loop,
# because the population is the loop's own and a second selection would be a second answer.
asks_n=0; asks_pub=0
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

  # AN ARCHIVED RECORD MUST BE TERMINAL. Since TOOL-aUnblockedFleet-2 this is the ONLY check in this
  # leg that still refuses on a run-state phase, and its importance rose accordingly: check 7 now
  # REPORTS the concurrent count rather than failing on it, so nothing else keeps a build folder to
  # one live record. That property is this branch's alone. It was already its own branch rather than
  # a consequence of the count — a `RUN.md` at LANDED plus one archived record edited back to RUNNING
  # left the old `nlive <= 1` silent, which was the steady state after every completed second run.
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
        check_rev "$w" \
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

  # ---- 15, THE LANDED FACT SET - TOOL-dDerivedDocket-22 S10, the weak form of
  # ---- TOOL-aBoundedCeiling-11. GRADED BY MODE over three populations, because the facts are due at a
  # ---- different verb in each: a recorded LANDED that `--landed` wrote, a recorded LANDED the rotation
  # ---- wrote with `landed-derived`, and under in-place landing a COMMITTED LANDING, whose roster
  # ---- `--close` froze beside the phase. The predicate and the dating are the kit library's, shared
  # ---- with `--preflight`, which refuses to retire a record this arm would then red for ever.
  # ----
  # ---- WHAT IT DOES NOT CHECK: that a fact is TRUE, or that the roster names the units the run built.
  # ---- It grades PRESENCE, on records first committed on or after the cutoff, dated with `--follow`
  # ---- and floored at a rotated folder's tenancy - `read_first_commit_date` states the direction of
  # ---- its own error. `asks-at-landing` is the freeze-presence arm's, below, and not graded twice.
  # ----
  # ---- UNDER `primary` A COMMITTED LANDING THE REMOTE ALREADY CARRIES is REPORTED and never graded:
  # ---- `--landed` writes its facts and is the verb that completes it, so a red here would be asking
  # ---- a record for facts its own next verb has not been run to write.
  if [ "$LFC_ON" = 1 ]; then
    lfc_pop=""
    case "$ph" in
      LANDED) if grep -q '^landed-derived:' "$f" 2>/dev/null; then lfc_pop=derived; else lfc_pop=landed; fi ;;
      LANDING)
        if lfc_c=$(read_landing_commit "$f"); then
          if [ "$LFC_MODE" = in-place ]; then
            lfc_pop=landing
          elif check_adv_reaches "$lfc_c"; then
            lfc_s=${f#"$M/builds/"}; lfc_s=${lfc_s%%/*}
            report "check 15 did not grade the landed facts of $f - it is a committed LANDING the remote already carries, so it derives LANDED, and under primary landing the verb that writes those facts has not run yet: --landed $lfc_s"
          fi
        fi ;;
    esac
    if [ -n "$lfc_pop" ] && check_landed_facts_due "$f" "$LANDED_FACTS_CUTOFF"; then
      case "$lfc_pop" in
        landed) lfc_n_landed=$((lfc_n_landed + 1)) ;;
        derived) lfc_n_derived=$((lfc_n_derived + 1)) ;;
        landing) lfc_n_landing=$((lfc_n_landing + 1)) ;;
      esac
      lfc_miss=$(read_missing_landed_facts "$f" "$lfc_pop")
      [ -z "$lfc_miss" ] \
        || fail 15 "a landed record first committed on or after LANDED_FACTS_CUTOFF is missing a fact its landing verb writes, so what that landing covered cannot be read from the record it left, and no verb adds a fact to a record once it is terminal or pushed - population $lfc_pop, missing [$lfc_miss] in $f"
    fi
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
  [ "$term" = 1 ] || [ -z "${a//[[:space:]]/}" ] || \
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
      [ "$ADV_HEAD_OK" = 1 ] || b=""
        # ANCESTRY, NOT EQUALITY — and the reason is the kit's own first success. Equality wedged the
        # bar permanently: merging then pushing, the two acts an authorization grants, move the
        # merge-base past the pin forever, so a LANDED record red every later default-branch push.
        # Reproduced on an honest fixture with no attacker. A phase-keyed carve-out is not the fix
        # either — the run writes `phase:`, so it would be a one-line escape from this check.
        # What actually matters, and what survives landing: the recorded BASE lies on the history the
        # ANCHOR names rather than on the branch the run authored.
        if ! check_rev "$rb"; then
          fail 9 "a recorded BASE does not resolve to a commit in this history, and the record is written by the run: $rb in $f"
        else
          # CAPTURED, not read off $? two conditions later. Threading a three-way status through an
          # elif chain makes the second branch read the status of the first TEST rather than of the
          # call, which is the guard-shares-state-with-what-it-guards shape this kit refuses.
          is_published "$rb"; _pubrc=$?
          if [ "$_pubrc" = 0 ]; then
            if ! check_head_reaches "$rb"; then
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
            [ "$rb" != "$HEAD_SHA" ] || fail 9 "the recorded BASE equals HEAD at a phase that claims work was done, so the run authored every byte an authorization comparison would read: $f" ;;
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
            if [ "$ph" = LANDED ] && [ -n "$b" ] && check_rev "$w"; then
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
              # TOOL-dDerivedDocket-22 S9 - A `landed-derived` FACT IS THIS RECORD'S ANCHOR EVIDENCE.
              # Only the rotation writes it, beside `phase: LANDED`, when `--preflight` derived the
              # landing from the advertised tip; no in-place verb writes `landed-anchor`, so asking
              # for one would red every rotated record. What it names is TESTED rather than trusted:
              # the landing commit must be on the tip this remote advertises, or a hand-written
              # archive would meet the anchor rule without ever having landed.
              lfd=$(fact_of "$f" landed-derived)
              if [ -z "$ak" ] && [ -n "$lfd" ]; then
                lfd_c=${lfd%% *}
                check_adv_reaches "$lfd_c" \
                  || fail 15 "a record claims LANDED on derived evidence and the landing commit its landed-derived: names is not on the tip the remote advertises, so the derivation it records is one this remote does not support: $lfd_c against $b in $f"
                ak=remote
              elif [ -z "$ak" ]; then
                # GRANDFATHERED BY DATE, the same idiom this kit's other cutoffs use. Every LANDED
                # record written before this unit carries no anchor kind and every one of them is in
                # fact remote-anchored; a record dated at or after the cutoff has no such excuse.
                # DATED WITH `--follow` (TOOL-dDerivedDocket-22 S9), as DISPOSITION_CUTOFF is: without
                # it a rotation re-dates a pre-cutoff record to the commit that added its archived
                # name and moves it into the graded set, where it reds for an anchor kind no verb may
                # now write. `read_first_commit_date` states the direction of its own error.
                # UNFLOORED, and deliberately: the tenancy floor would date
                # `memory/builds/dUnstalledConvoy/RUN.md` to its second run's rotation, 2026-08-24,
                # past this cutoff, and that LANDED record carries no anchor kind and is terminal -
                # a red no verb could clear. The fact-set arm, whose key is new, floors.
                fcommit=$(read_first_commit_date "$f" nofloor)
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
                elif check_adv_reaches "$w"; then
                  : # ...or it reached the remote afterwards, which is an UPGRADE and not a defect
                else
                  report "check 15 skipped for $f — a local-anchored LANDED names a witness this clone does not carry on its own default branch, and a local anchor is a record of a merge rather than an observation of one, so this clone cannot judge it"
                fi
              elif ! check_adv_reaches "$w"; then
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
  if [ -n "$rb" ] && check_rev "$rb"; then
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
      # HOISTED out of the presence guard below (TOOL-dNarrowedAnchor-1). Check 29 needs the DECLARED
      # mode for every run-state file, not only the ones carrying a `mode:` line of their own: a
      # record written before that key existed still has a recorded BASE, and whether that base sits
      # off the default branch is answerable without it. Leaving the derivation inside the guard
      # would have scoped the new check to the best-recorded half of the population, which is the
      # half least likely to need it.
      dmode=$(printf '%s\n' "$bb" | awk '
        NR == 1 { next }
        /^---[[:space:]]*\r?$/ { exit }
        /^authorized-by:/ { v = $0; sub(/^authorized-by:[[:space:]]*/, "", v); sub(/[[:space:]]*\r?$/, "", v); print v; exit }')
      [ -n "$dmode" ] || dmode=slug

      # ---- 29: THE SECOND ANCHOR IS ADMISSIBLE PER MODE. The driver refuses this at preflight; this
      # ---- is the merge bar's own opinion of the same question, and it is DERIVED rather than read
      # ---- back. `anchor-kind` is recorded in the very file under inspection, so reading it would
      # ---- be asking the subject to grade itself - the rule this leg already keeps for the base.
      # ----
      # ---- THE DISCRIMINATOR IS `ADV_HEAD`, NOT `is_published`. That helper answers "ancestor of ANY
      # ---- advertised tip", which is true under BOTH anchors and would therefore never separate
      # ---- them - it would be a check that cannot fail. Ancestry of the advertised DEFAULT-BRANCH
      # ---- tip is the question: a base the first anchor could have produced is one that sits on it.
      # ----
      # ---- CANNOT TELL STAYS SILENT, exactly as `is_published` does. An unreadable or unadvertised
      # ---- default-branch tip means the remote could not be observed, and a leg that reds a whole
      # ---- fleet on a network fault is worse than one that waits for the next run.
      case " $SECOND_ANCHOR_MODES " in
        *" $dmode "*) ;;
        *)
          if [ "$ADV_HEAD_OK" = 1 ] \
             && check_rev "$rb" \
             && ! check_adv_reaches "$rb"; then
            fail 29 "a run's recorded BASE is not on the branch the remote calls its default, so it came from the second anchor, while the build README there declares a mode whose discipline is that the folder already existed: mode $dmode, admissible on that anchor are $SECOND_ANCHOR_MODES, base $rb in $f"
          fi ;;
      esac

      if [ -n "$recmode" ]; then
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

      # ---- 19: THE GRANT, re-derived here rather than believed - TOOL-dDerivedDocket-19 S4. The
      # ---- driver pins `may:` from the README at BASE, normalised by the library's `parse_grants`;
      # ---- this re-reads that same blob with its own parse and normalises it with the SAME function,
      # ---- so a backticked grant and a bare one agree and the comparison does not turn on how the
      # ---- owner copied it. AT BASE, never at HEAD: a README the run edited after its preflight is
      # ---- not the authorization it ran under. The residual is that SHARED normaliser: a grammar wrong
      # ---- the same way for both callers agrees with itself here, and what catches that is the
      # ---- driver suite's one refused fixture per negative the grammar declares, not this arm.
      # ----
      # ---- PRESENCE-GUARDED in the direction check 19's mode arm is: a record written before this
      # ---- unit carries no `may:` fact, and over a README declaring nothing that is an honest
      # ---- absence. A record carrying no fact while its README at BASE DOES declare a grant is not
      # ---- one, and reds - the pin the driver writes for that README is not there.
      # ----
      # ---- ...and a `may:` other than `none` on a record whose mode is not `slug` reds whatever its
      # ---- README says: the driver refuses the key under every other mode, so such a record was
      # ---- written around it, and a grant a second-anchor run pinned is one it could have authored.
      recmay=$(fact_of "$f" may)
      dmayl=$(read_may_of "$bb")
      if [ -z "$dmayl" ]; then
        dmay=none
      elif ! dmay=$(parse_grants "${dmayl#may=}"); then
        dmay="refused by the grant grammar at token ${dmay:-(an empty value)}"
      fi
      if [ -n "$recmay" ] || [ "$dmay" != none ]; then
        [ "$recmay" = "$dmay" ] || fail 19 "a run-state file pins a may: grant the build README at its own recorded BASE does not declare, so the authority the run says its owner committed is not the authority that README carries - pinned against declared follow: [${recmay:-(no may: fact)}] against [$dmay] in $f"
      fi
      if [ -n "$recmay" ] && [ "$recmay" != none ] && [ "${recmode:-$dmode}" != slug ]; then
        fail 19 "a run-state file pins a may: grant while recording an authorization mode that resolves at the second anchor, so the grant could be one the run wrote for itself - ruling D12-j honours a grant only under slug: mode [${recmode:-$dmode}], may: [$recmay] in $f"
      fi
    else
      fail 13 "no build README at a run's recorded BASE, so nothing committed before that run branched authorizes it: $rb in $bre"
    fi

    # ---- 19: NO RUN COMMIT WRITES A GRANT INTO ANY BUILD README - TOOL-dDerivedDocket-19 S4, the
    # ---- cross-run arm. A README a run lands on the default branch authorizes the next run, so
    # ---- without this one run could grant another (TOOL-aStandingWrit-1). It reads each run's OWN
    # ---- commits, never `base..HEAD` or `base..witness`: both hold every default-branch commit
    # ---- landed since BASE, so the owner's hand-typed grant - the channel ruling D12-j keeps open -
    # ---- would red the run that then could not land, and once archived would red the bar for ever.
    # ----
    # ---- THE RANGE PER RECORDED STATE. A working, HELD or LANDING record walks to HEAD and excludes
    # ---- the advertised default-branch tip, the one check 7 observes; with that tip absent from this
    # ---- clone, the local ref of the advertised name, announced as the weaker reading. A terminal
    # ---- record walks from its WITNESS and excludes what `read_run_exclusions` reads off the merges
    # ---- on that witness's tail - by which parent reaches the record's own commits, never by parent
    # ---- order and never from a tip - so a landed or aborted record keeps one range for ever. A
    # ---- DERIVED-LANDED record - a LANDING whose landing commit C the advertised tip holds - walks
    # ---- from C with the same exclusions (TOOL-dDerivedDocket-22 S17), so it keeps the range its
    # ---- rotated archive will have. Read as live instead, its range would be whatever this tree has
    # ---- not pushed, which after a landing is nothing at all.
    # ----
    # ---- A SKIP ANNOUNCES ITSELF. A terminal record with no witness, a witness this clone cannot
    # ---- resolve, or a live one with no tip to exclude is named on the report channel, never passed.
    # ----
    # ---- WHAT IT TRUSTS, because its inputs are the graded record's own. The witness and the BASE
    # ---- bound the range and the run writes both, so a forged pair moves the range: check 9 grades
    # ---- the BASE and checks 6 and 15 the witness, and this arm reads them as those checks leave them.
    # ---- A TERMINAL RECORD IS SCANNED OVER `base..witness` FIRST, and walked only on a hit. That range
    # ---- is a SUPERSET of the run's own commits, so a superset writing no grant settles the subset
    # ---- with no walk at all - the ordinary case, since no build README in this tree has ever carried
    # ---- the key. Measured before this was added: the walk over every terminal record here cost some
    # ---- twenty seconds a bar to reach the same empty answer the one superset scan reaches.
    mayend=""; mayex=""; maywhy=""; maywalk=0
    case " $PHASES_TERMINAL " in
      *" $ph "*)
        if [ -z "$w" ]; then
          maywhy="it is $ph and names no witness, so there is no endpoint to walk its own commits from"
        elif ! check_rev "$w"; then
          maywhy="its witness $w does not resolve to a commit in this clone"
        else
          mayend=$w; maywalk=1
        fi ;;
      *)
        mayend=HEAD
        maylc=""
        [ "$ph" = LANDING ] && maylc=$(read_landing_commit "$f" 2>/dev/null)
        if [ -n "$maylc" ] && check_adv_reaches "$maylc"; then
          mayend=$maylc; maywalk=1
        elif [ "$ADV_HEAD_OK" = 1 ]; then
          mayex=$ADV_HEAD
        elif [ -n "$ADV_NAME" ] && GIT rev-parse --verify --quiet "refs/heads/$ADV_NAME^{commit}" >/dev/null 2>&1; then
          mayex="refs/heads/$ADV_NAME"
          report "check 19 excludes the LOCAL ref $ADV_NAME from the own commits of $f - the advertised default-branch tip is not in this clone, and a local ref is the weaker reading: a run that merged into it hides its own commits from the grant-write arm"
        else
          maywhy="it is live and neither the advertised default-branch tip nor a local ref of the advertised name can be read, so its own commits cannot be told from the default branch's"
        fi ;;
    esac
    if [ -n "$maywhy" ]; then
      report "check 19 SKIPPED the grant-write arm for $f - $maywhy"
    elif ! maycs=$(read_run_commits "$mayend" "$rb" $mayex); then
      report "check 19 SKIPPED the grant-write arm for $f - its own commits could not be enumerated from $mayend over base $rb, and an empty list here would read as a run that wrote nothing"
    else
      maywr=$(printf '%s\n' "$maycs" | scan_grant_writes)
      if [ -n "$maywr" ] && [ "$maywalk" = 1 ]; then
        mayex=$(read_run_exclusions "$mayend" "$rb" "$M/builds/$bslug/RUN.md" 2>/dev/null)
        [ $? = 0 ] || report "check 19 read the terminal exclusions of $f only in part - the walk or a reachability probe could not answer, so its range keeps commits an exclusion would have removed, which is the fail-closed direction"
        if maycs=$(read_run_commits "$mayend" "$rb" $mayex); then
          maywr=$(printf '%s\n' "$maycs" | scan_grant_writes)
        else
          report "check 19 graded the WHOLE base..witness range of $f - its own commits could not be enumerated past the exclusions the walk read, and the superset is the fail-closed reading"
        fi
      fi
      # AN EMPTY RANGE IS SAID OUT LOUD. It is honest for a run that has committed nothing past its
      # BASE, and it is what a live record reads as once everything it wrote is on the advertised
      # tip without a committed LANDING to walk from - a skip that looks like a pass otherwise.
      [ -n "$maycs" ] || report "check 19's grant-write arm examined NO own commit of $f - the range from $mayend over base $rb past its exclusions is empty"
      while read -r maysha mayrd; do
        [ -n "$maysha" ] || continue
        fail 19 "a commit among a run's own commits writes a may: line into a build README, so a run could land the grant the next run would be authorized by - commit and README follow: $maysha in $mayrd, run $f"
      done <<MAYWRITES
$maywr
MAYWRITES
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

  # ---- THE ASK MANDATE, SECOND-OPINIONED — TOOL-dDerivedDocket-18. The helpers and the honest
  # ---- limits are at the head of this file; what follows is the six arms, keyed on the ONE fact
  # ---- that makes a record mandated. Every one of them is VACUOUS on a record with no `asks:`
  # ---- fact, which is every record in this tree today, so the count is announced after the loop:
  # ---- a skip that looks like a pass is indistinguishable from coverage.
  recasks=$(fact_of "$f" asks)
  if [ -n "$recasks" ]; then
    asks_n=$((asks_n + 1))
    askslug=${f#"$M/builds/"}; askslug=${askslug%%/*}
    asksre="$M/builds/$askslug/README.md"
    askids=$(printf '%s\n' "$recasks" | expand_id_runs)

    # ---- S5: ONE AUTHORIZATION PATH (owner ruling D12-a). A mandate is admissible on the FIRST
    # ---- anchor's discipline alone — mode `slug`, where the owner landed the folder before the run
    # ---- existed. The driver refuses the rest at preflight, so a record reaching this arm was
    # ---- written around the driver rather than by it. The blank-conf half is its own refusal and
    # ---- not a consequence of the mode one: a `slug` record pinning a mandate with no declared
    # ---- producer is a pinned set nothing ever graded.
    askmode=$(fact_of "$f" mode)
    [ "$askmode" = slug ] \
      || fail 19 "a run-state file pins an asks: mandate while recording an authorization mode whose discipline lets the run reach the anchor it writes, so the mandate and the tree it is asserted against could both be this run's own: mode [${askmode:-(none)}] in $f"
    [ -n "$ASKS_CMD" ] \
      || fail 19 "a run-state file pins an asks: mandate while this project declares no ASKS_CMD, so nothing here or in the driver ever said whether any of that mandate is executable and every check keyed on it passes over an ungraded list: $f"

    # ---- S1: THE `asks:` FACT AGAINST THE BUILD README ITSELF — at the recorded BASE, and while
    # ---- the run is still live at HEAD too. Two halves catching two different things: a fact that
    # ---- never matched its authorization, and an authorization edited underneath a live run
    # ---- (property P6). A record at LANDING or at a terminal phase is PAST ITS CLOSE and the HEAD
    # ---- half does not touch it — otherwise the owner's next edit to that README reds a landed
    # ---- record for ever, and under the in-place lander it does so through a record that never
    # ---- rotates.
    if [ -n "$rb" ] && check_rev "$rb" && askbb=$(GIT show "$rb:$asksre" 2>/dev/null); then
      askdecl=$(read_asks_of "$askbb")
      [ "$recasks" = "$askdecl" ] \
        || fail 19 "a run-state file pins an asks: mandate the build README at its own recorded BASE does not declare, so the set the run says authorized it is not the set its authorization asked for - pinned against declared follow: [$recasks] against [${askdecl:-(none)}] in $f"
      case " LANDING $PHASES_TERMINAL " in
        *" $ph "*)
          report "check 19 did not re-read $asksre at HEAD for $f - the record is at $ph, which is past its close, and the pinned-mandate property binds a LIVE run" ;;
        *)
          askhead=$(read_asks_of "$(GIT show "HEAD:$asksre" 2>/dev/null)")
          [ "$recasks" = "$askhead" ] \
            || fail 19 "a LIVE run's build README carries an asks: line at HEAD that is not the one the run pinned, so the mandate this run will be measured against was edited underneath it - pinned against HEAD follow: [$recasks] against [${askhead:-(none)}] in $f" ;;
      esac
    else
      report "check 19 could not read the build README at the recorded BASE for $f, so its asks: fact was not compared against the authorization here; check 13 owns that refusal"
    fi

    # ---- S2: PROPERTY P5 RE-DERIVED. Every mandated ask has a filed row in its HOME build's
    # ---- BACKLOG at the tree the mandate was asserted against — the blob at `m-base:`, never the
    # ---- working tree, because a row filed after the run began would otherwise satisfy a property
    # ---- about provenance. The line match is the kit library's, shared with the driver's own P5:
    # ---- the independence of a second opinion is in its INPUTS, never in a second grammar.
    # ----
    # ---- ...and `m-base:` ITSELF is graded against the pinned `anchor-sha:` and never against
    # ---- `base:`, because a forged pair that agrees with itself is the whole hazard. Equality is
    # ---- safe here in a way it is not for check 9: this is the merge-base of two FROZEN commits,
    # ---- and a merge-base of two frozen commits never moves.
    askmb=$(fact_of "$f" m-base)
    askash=$(fact_of "$f" anchor-sha)
    askpf=""
    if [ -z "$askmb" ] || ! check_rev "$askmb"; then
      fail 19 "a run-state file pins an asks: mandate and no m-base: this clone can read, so every property about the tree that mandate was asserted against would be graded over an empty blob or, worse, over the index the run itself staged: m-base [${askmb:-(none)}] in $f"
    else
      askhomeseen=""; askhomeblob=""
      for askid in $askids; do
        askhome=$(ask_home_of "$askid")
        if [ "$askhome" != "$askhomeseen" ]; then
          askhomeseen=$askhome
          askhomeblob=$(GIT show "$askmb:$M/builds/$askhome/BACKLOG.md" 2>/dev/null || true)
        fi
        ask_filed_in "$askhomeblob" "$askid" \
          || fail 19 "a mandated ask has no filed row in the tree this run pinned its mandate against, so the run was authorized by a record that tree does not carry and could have written the row itself: $askid, wanted in $M/builds/$askhome/BACKLOG.md at $askmb"
      done
      # HEAD AT PREFLIGHT is the FIRST PARENT of the earliest commit whose copy of this record
      # carries the `m-base:` line: preflight refuses a dirty tree and stages the record, so the
      # next commit carries it. `resolve_introducing_commit` says when it cannot name that commit
      # rather than handing back a plausible wrong one.
      askpf=$(resolve_introducing_commit "$f" "m-base: $askmb" 2>/dev/null) || askpf=""
      askpar=""
      [ -n "$askpf" ] && askpar=$(GIT rev-parse --verify --quiet "$askpf^1^{commit}" 2>/dev/null)
      askwant=""
      [ -n "$askpar" ] && [ -n "$askash" ] && check_rev "$askash" \
        && askwant=$(GIT merge-base "$askash" "$askpar" 2>/dev/null)
      if [ -n "$askwant" ]; then
        askgot=$(resolve_full_sha "$askmb"); [ -n "$askgot" ] || askgot=$askmb
        [ "$askgot" = "$askwant" ] \
          || fail 19 "a run-state file's m-base: is not the merge-base of the anchor it pinned and the tree its own preflight stood on, so the tree its mandate was asserted against was chosen rather than derived - recorded against re-derived follow: [$askmb] against [$askwant] in $f"
      else
        report "check 19 FELL BACK TO ANCESTRY for the m-base: of $f - the commit that introduced that line, or its first parent, could not be named, so this is the weaker reading and a pin moved to any older common commit passes it"
        askfb=1
        { [ -n "$askash" ] && check_rev "$askash" \
          && GIT merge-base --is-ancestor "$askmb" "$askash" 2>/dev/null; } || askfb=0
        check_head_reaches "$askmb" || askfb=0
        [ "$askfb" = 1 ] \
          || fail 19 "a run-state file's m-base: is not an ancestor of both the anchor it pinned and this working history, so the tree its mandate was asserted against does not lie on the history that authorized the run: m-base [$askmb] against anchor [${askash:-(none)}] in $f"
      fi
    fi

    # ---- S3: THE FOLDER-WIDE ANCHOR BAN. No tracked file under a mandated run's own build folder
    # ---- may ANCHOR an id whose slug is not this build's. Both a foreign ask id and a foreign unit
    # ---- id anchored here make this build a SECOND CLAIMANT for a record it does not own, and the
    # ---- narrower predicate — "an id whose ask row is filed elsewhere" — would need the witness,
    # ---- which this arm deliberately does not read.
    if scan_foreign_anchors "$M/builds/$askslug" "$askslug"; then
      if [ -n "$ASK_ANCHORS" ]; then
        askhit=$(printf '%s\n' "$ASK_ANCHORS" | sed -n 1p | tr '\t' ':')
        askhitn=$(printf '%s\n' "$ASK_ANCHORS" | grep -c . || true)
        fail 37 "a mandated run's own build folder ANCHORS a record id belonging to another build, so this folder is a second claimant for an id it does not own and the two builds' records can no longer be told apart: $askhit ($askhitn in all) under $M/builds/$askslug"
        printf '%s\n' "$ASK_ANCHORS" | tr '\t' ':' | while IFS= read -r askline; do
          [ -n "$askline" ] && report "check 37 foreign anchor under $M/builds/$askslug: $askline"
        done
      else
        report "check 37 found no foreign anchor under $M/builds/$askslug"
      fi
    else
      report "check 37 SKIPPED for $M/builds/$askslug - $ASK_ANCHOR_WHY"
    fi

    # ---- S4: THE FREEZE IS PRESENT ON A LANDED RECORD, and it names every mandated id. Ruling D4
    # ---- makes CLOSED non-absorbing, so a later REOPEN would retroactively change what a landed
    # ---- record appears to have answered: the answer is pinned at the moment of landing or it is
    # ---- not an answer about this run at all. A freeze missing one mandated id loses that ask's
    # ---- frozen answer, which is why PRESENCE alone is not the check.
    # ---- TOOL-dDerivedDocket-22 S15 - UNDER in-place LANDING THE FREEZE IS DUE AT THE CLOSE, which
    # ---- writes it beside LANDING in the record it commits, so a COMMITTED LANDING record is graded
    # ---- too. Graded on the recorded LANDED alone, this arm would examine nothing in gov's own mode
    # ---- until a rotation, and the second opinion would never fire. Under primary it is due at
    # ---- `--landed`, and only a recorded LANDED is graded, exactly as before.
    askfz=$(fact_of "$f" asks-at-landing)
    askfzdue=0
    if [ "$ph" = LANDED ]; then
      askfzdue=1
    elif [ "$ph" = LANDING ] && [ "$LFC_MODE" = in-place ] && read_landing_commit "$f" >/dev/null; then
      askfzdue=2
    fi
    if [ "$askfzdue" != 0 ]; then
      if [ -z "$askfz" ] && [ "$askfzdue" = 2 ]; then
        fail 15 "a committed LANDING record under an asks: mandate carries no asks-at-landing:, and under in-place landing --close writes that freeze beside the phase, so the record the push carries answers nothing about the question the run was authorized by: $f"
      elif [ -z "$askfz" ]; then
        fail 15 "a record claims LANDED under an asks: mandate and freezes no answer to it, so what that run actually answered is whatever the tree says today rather than what it said at landing: $f"
      else
        for askid in $askids; do
          case " $askfz " in
            *" $askid="*) ;;
            *) fail 15 "a landed record's asks-at-landing: omits an ask its own mandate names, so that ask's answer at landing is lost and the freeze covers less than the question the run was authorized by: $askid in $f" ;;
          esac
        done
      fi
    fi

    # ---- S8: THE PINS RE-DERIVED, BEFORE PUBLICATION. `asks-ready:` and the freeze are the two
    # ---- ask facts nothing above can re-derive from a blob, because their content is the declared
    # ---- producer's answer and not a line in a file. So the producer is RE-RUN over the inputs the
    # ---- record pinned and its answer compared — bounded to records whose preflight commit is not
    # ---- yet reachable from the advertised default tip. A published record is counted and left
    # ---- alone: re-deriving one would grade an archived pin against a producer whose rules moved
    # ---- after it landed, and it would cost one generator run per mandated record per bar for ever.
    if [ -z "$ASKS_CMD" ]; then
      report "check 19 did not re-derive the pins of $f - this project declares no ASKS_CMD, and S5 above has already refused the record for exactly that"
    elif [ -z "$askpf" ]; then
      report "check 19 SKIPPED the pin re-derivation for $f - the commit that introduced its m-base: could not be named, so whether this record is published cannot be asked at all"
    else
      askrederive=1
      if [ "$ADV_HEAD_OK" != 1 ]; then
        report "check 19 is re-deriving the pins of EVERY mandated record because this run observed no readable default-branch tip, so no record can be shown published: $f"
      elif check_adv_reaches "$askpf"; then
        askrederive=0
        asks_pub=$((asks_pub + 1))
        report "check 19 - $f is published, not re-derived: its preflight commit $askpf is an ancestor of the advertised default tip"
      fi
      if [ "$askrederive" = 1 ]; then
        askready=$(fact_of "$f" asks-ready)
        if run_ask_query "$askslug" "$askmb" $askids; then
          askpairs=""
          for askid in $askids; do askpairs="$askpairs $askid=$(read_ask_row "$askid" ready)"; done
          askpairs=${askpairs# }
          [ "$askready" = "$askpairs" ] \
            || fail 19 "a run-state file's asks-ready: is not what the declared producer says at the very tree the run pinned, so the grades that mandate was admitted on are not the producer's - recorded against re-derived follow: [${askready:-(none)}] against [$askpairs] in $f"
        else
          report "check 19 reports the asks-ready: of $f UNANSWERED rather than red - $AQ_WHY"
        fi
        # THE FREEZE, at the FIRST PARENT of the commit that introduced it, which is the tree the
        # landing verb examined. Its scope is the mandate THEN this build's own filings at that same
        # commit, deduplicated, and the pairs are emitted in the driver's own stable order - slug
        # then numeric sequence, never a string sort, which puts `-10` before `-2`.
        if [ -n "$askfz" ]; then
          askfzc=$(resolve_introducing_commit "$f" "asks-at-landing: $askfz" 2>/dev/null) || askfzc=""
          askfzp=""
          [ -n "$askfzc" ] && askfzp=$(GIT rev-parse --verify --quiet "$askfzc^1^{commit}" 2>/dev/null)
          if [ -z "$askfzp" ]; then
            report "check 15 SKIPPED the freeze re-derivation for $f - the commit that introduced its asks-at-landing: line, or that commit's first parent, could not be named, so the tree the landing verb examined cannot be reached"
          else
            askscope=""
            for askid in $askids; do
              case " $askscope " in *" $askid "*) continue ;; esac
              askscope="$askscope $askid"
            done
            for askid in $(asks_filed_in "$(GIT show "$askfzp:$M/builds/$askslug/BACKLOG.md" 2>/dev/null)"); do
              [ "$(ask_home_of "$askid")" = "$askslug" ] || continue
              case " $askscope " in *" $askid "*) continue ;; esac
              askscope="$askscope $askid"
            done
            askscope=${askscope# }
            if [ -z "$askscope" ]; then
              report "check 15 SKIPPED the freeze re-derivation for $f - its mandate expands to no id and its folder files none at that tree, so the scope the freeze covers is empty and there is nothing to compare"
            elif run_ask_query "$askslug" "$askfzp" $askscope; then
              askpairs=""
              for askid in $(printf '%s\n' $askscope | sort -t- -k2,2 -k3,3n); do
                askst=$(read_ask_row "$askid" status)
                askpairs="$askpairs$askid=${askst:--} "
              done
              askpairs=${askpairs% }
              [ "$askfz" = "$askpairs" ] \
                || fail 15 "a landed record's asks-at-landing: is not what the declared producer says at the tree its landing verb examined, so the answer frozen into a terminal record is not the one that tree gives - recorded against re-derived follow: [$askfz] against [$askpairs] in $f"
            else
              report "check 15 reports the asks-at-landing: of $f UNANSWERED rather than red - $AQ_WHY"
            fi
          fi
        fi
      fi
    fi
  fi
done <<EOF
$RUNS
EOF

# ---- TOOL-dDerivedDocket-18 — THE ASK-MANDATE SECOND OPINIONS, COUNTED. One line per run, and it
# ---- is emitted whether the count is zero or not: a check that quantifies over an empty population
# ---- is silent for exactly the same reason a passing one is, and "no record pins an asks: fact" is
# ---- a finding about the tree rather than a verdict about a record. On the REPORT channel with
# ---- every other announcement of a case a check could not reach, so the contract at the head of
# ---- this file — exit 0 and no output is clean — keeps its meaning.
# ---- TOOL-dDerivedDocket-22 S10 - THE FACT-SET ARM, COUNTED PER POPULATION on one line, and a zero
# ---- says so: in gov's own in-place mode no record says LANDED until a rotation, so an arm grading
# ---- recorded LANDED alone would pass on nothing, and the count is what shows which one it graded.
if [ "$LFC_ON" = 1 ]; then
  lfc_tot=$((lfc_n_landed + lfc_n_derived + lfc_n_landing))
  lfc_zero=""
  [ "$lfc_tot" = 0 ] && lfc_zero=" - a count of 0, so this arm graded nothing on this tree and its green is coverage of an empty population"
  report "the landed fact-set arm of check 15 graded, at LANDED_FACTS_CUTOFF $LANDED_FACTS_CUTOFF under LANDER_MODE $LFC_MODE: recorded LANDED $lfc_n_landed · rotated derived LANDED $lfc_n_derived · committed LANDING $lfc_n_landing$lfc_zero"
fi
if [ "$asks_n" = 0 ]; then
  report "the ask-mandate second opinions (checks 19, 15 and 37) are VACUOUS on this tree: 0 run-state records pin an asks: fact, so every arm examined nothing and a green verdict here is coverage of an empty population"
else
  report "the ask-mandate second opinions examined $asks_n run-state record(s) pinning an asks: fact, of which $asks_pub were already published on the advertised default tip and so were not re-derived"
fi

# ---- 7: REPORT the concurrent unattended runs. This check no longer asserts anything about how many
# ---- are live, and it cannot fail. TOOL-aUnblockedFleet-2.
# ----
# ---- WHAT IT NO LONGER CHECKS, first, because a gate's own header owes its gaps. It does not bound
# ---- the live count. It does not detect an ABANDONED record — one is now reported forever, with no
# ---- staleness bound, and an operator has to read the report; TOOL-aReapedTicket-5 keeps that scope.
# ---- The one property still enforced over run-state phases is check 4's, that an ARCHIVED record is
# ---- terminal, and that is what keeps a build folder to one live record now that this one does not.
# ----
# ---- It refused, until this unit, whenever more than one tracked record was non-terminal, on the
# ---- ground that "the run" would otherwise be ill-defined for anything keyed on it. Nothing is keyed
# ---- on it: measured by construction with this check and the driver's refusal 5 both neutered over
# ---- two genuinely live records, where the whole leg exited 0 and every driver verb resolved its own
# ---- build. What the refusal cost is on the record three times — TOOL-aFusedCharter-4,
# ---- TOOL-aBoundedVerdict-24 and TOOL-aReapedTicket-5 — twice cleared only by marking honest runs
# ---- ABORTED.
# ----
# ---- THE `LANDING`-ALREADY-ON-THE-REMOTE EXCLUSION. A record at `LANDING` whose OWN commit - the one
# ---- that last wrote its committed bytes - is an ancestor of the tip the remote advertises is NOT a
# ---- competing run: by owner ruling D12-i2 it derives LANDED (TOOL-dDerivedDocket-22). Nothing keyed
# ---- on "the run" could ever resolve to it, because the record the push carried is already on the
# ---- branch every later run measures against. Without this, such a record counts forever and reds
# ---- the bar for every later run on every node, which is the deadlock `TOOL-aBoundedVerdict-24` and
# ---- `TOOL-aFusedCharter-4` both record and which the fleet previously cleared only by marking
# ---- honest runs ABORTED.
# ----
# ---- WHAT THIS DOES NOT CLAIM, and the header says so because a structural check reads as a semantic
# ---- one to everybody who did not write it. It does NOT say the run finished correctly, that its
# ---- Definition of Done was met, or that anything reviewed it. It says one thing: the commit carrying
# ---- this record's LANDING is on the branch the remote calls its default. The derivation is a
# ---- READING and this leg writes nothing, so every other check keyed on the recorded phase grades
# ---- this record exactly as before.
# ----
# ---- SCOPED TO `LANDING` AND NOTHING ELSE. A `BUILDING` record whose commits happen to be on the
# ---- remote is a genuinely live run and keeps counting: `LANDING` is the one phase that means
# ---- `--close` already evaluated the Definition of Done, so it is the one phase where "on the
# ---- remote" is the whole remaining difference.
# ----
# ---- IT FAILS CLOSED AND IT SAYS SO. No advertisement, an uncommitted record, or a tip this clone
# ---- has not fetched leaves the record counted, with the reason reported. A check that silently
# ---- stops excluding is indistinguishable from one that found nothing to exclude, which is this
# ---- repo's own green-by-absence class.
c7anchor="$ADV_HEAD"
[ -n "$c7anchor" ] && { GIT rev-parse --verify --quiet "$c7anchor^{commit}" >/dev/null 2>&1 || c7anchor=""; }
# ---- UNCONDITIONAL, not `report`. `report` is gated on REPORT=1, so routing either line through it
# ---- would make the exclusion invisible on every default bar run — a check quietly deleted, which is
# ---- the exact shape this exclusion must not have. Caught by verifying it rather than by reading it.
if [ "$nlive" -gt 1 ] && [ -z "$c7anchor" ]; then
  printf 'unattended: check 7 exclusion UNAVAILABLE — no advertised default-branch tip resolves in this clone, so a LANDING record already on the remote cannot be told from a competing run; every non-terminal record is counted
'
fi
c7keep=""; c7drop=""; c7n=0
for c7f in $live; do
  c7ph=$(phase_of "$c7f")
  # TOOL-dDerivedDocket-22 S9 - THE LANDING COMMIT, NOT THE WITNESS. The witness answers whether
  # the WORK is on the remote; the question is whether the RECORD is, because a run that pushed its
  # work before committing its LANDING record has a witness on the remote and a record nobody
  # pushed. `read_landing_commit` is the kit library's, so the driver's `check_single_live` and
  # `--status` read exactly this commit, and the leg and the driver agree about one record. It is a
  # commit this leg FOUND - the one that last wrote the record's committed bytes - so no field the
  # run authors can disarm it, which is what the witness's sha-shape clause used to guard against.
  c7c=""
  [ "$c7ph" = LANDING ] && c7c=$(read_landing_commit "$c7f" 2>/dev/null)
  if [ -n "$c7c" ] && [ -n "$c7anchor" ] && GIT merge-base --is-ancestor "$c7c" "$c7anchor" 2>/dev/null; then
    c7drop="$c7drop $c7f"
    printf 'unattended: check 7 EXCLUDED %s — derived LANDED: its landing commit %s is an ancestor of the advertised default-branch tip %s, so the record the push carried is on the remote and it is a finished run rather than a second live one\n' "$c7f" "$c7c" "$c7anchor"
  else
    c7keep="$c7keep $c7f"; c7n=$((c7n+1))
  fi
done
[ -z "$c7drop" ] || live="$c7keep"
[ -z "$c7drop" ] || nlive="$c7n"
# REPORTED, NEVER FAILED. TOOL-aUnblockedFleet-2. Silent at one or fewer.
#
# WHERE THIS OUTPUT ACTUALLY LANDS, stated because the first version of this comment got it wrong and
# the closing diff review caught it. It goes to the DEFAULT channel rather than through `report`,
# which is right as far as it goes -- but `run-gates.sh` echoes a leg's captured stdout ONLY from
# report_one's FAIL branch, and an rc=0 leg prints one line and nothing else. So on a GREEN bar
# nobody sees this. The bytes are persisted, redacted, to <git-dir>/gate-logs/ and are fully visible
# on a direct run of this script; the operator-facing half is the DRIVER's --preflight announcement,
# which an agent does read. Do not restate the old claim that the default channel makes it visible.
if [ "$nlive" -gt 1 ]; then
  printf 'unattended: %d concurrent unattended run(s) — none of them blocks another, and this leg does not fail on the count:
' "$nlive"
  for c7r in $live; do printf '  %s · phase %s
' "$c7r" "$(phase_of "$c7r")"; done
fi

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
VERBSHIP="$HERE/VERBS.template.md"
VERBDOC="$M/guides/UNATTENDED-VERBS.md"
KITREL=${HERE#"$(cd "$ROOT" && pwd)"/}
PREFIX=${KITREL%/*}; [ "$PREFIX" = "$KITREL" ] && PREFIX="" || PREFIX="$PREFIX/"
# ---- TWO PAIRS as of TOOL-dFoldedVerdict-5, iterated rather than copied. The second exists because
# ---- the protocol had reached its byte cap EXACTLY and section 7 moved out to make the contract
# ---- amendable again. A ROW here and not a new check number: this check already carries the
# ---- both-halves refusal the second pair needs, so a new number would only have to be added
# ---- everywhere check numbers are enumerated. The pair NAME is a parameter because with one message
# ---- for both pairs a reader has to open the paths to learn which half of the kit drifted.
# ---- The COMPARISON is shared and the MESSAGES are not, which is deliberate rather than clumsy.
# ---- `check-arms.py` arms a branch by finding a test assertion that names the branch's own failure
# ---- text, and its signature is the longest LITERAL run between interpolations. A message reading
# ---- "the shipped $1 ... drifted" therefore has no assertable literal at all — every arm for it
# ---- would have to name a `$1` no run ever emits. So each pair states its own sentence.
_c10_cmp() { # shipped half · installed half -> 0 identical · 1 drifted · 2 a half is missing
  [ -f "$1" ] && [ -f "$2" ] || return 2
  if [ -n "$PREFIX" ]; then nl=$(sed -e 's/\r$//' -e "s|$PREFIX||g" "$2"); else nl=$(sed -e 's/\r$//' "$2"); fi
  ns=$(sed -e 's/\r$//' "$1")
  [ "$nl" = "$ns" ]
}
_c10_cmp "$SHIP" "$LIVEDOC"; _c10rc=$?
if [ "$_c10rc" -eq 2 ]; then
  fail 10 "one half of the protocol pair is missing, and a parity check with one file is a check that cannot fail: $SHIP / $LIVEDOC"
elif [ "$_c10rc" -ne 0 ]; then
  fail 10 "the shipped protocol and this repo's installed copy have drifted, so the kit ships something other than what it runs on: $SHIP vs $LIVEDOC"
  diff <(printf '%s\n' "$nl") <(printf '%s\n' "$ns") | head -10 | sed 's/^/    /'
fi
# ---- THE SECOND PAIR, added when TOOL-dFoldedVerdict-5 moved section 7 out of a protocol that had
# ---- reached its byte cap exactly. A row here and not a new check number: this check already owns
# ---- the both-halves refusal the second pair needs.
_c10_cmp "$VERBSHIP" "$VERBDOC"; _c10rc=$?
if [ "$_c10rc" -eq 2 ]; then
  fail 10 "one half of the verb-carrier pair is missing, and a parity check with one file is a check that cannot fail: $VERBSHIP / $VERBDOC"
elif [ "$_c10rc" -ne 0 ]; then
  fail 10 "the shipped verb carrier and this repo's installed copy have drifted, so the kit ships something other than what it runs on: $VERBSHIP vs $VERBDOC"
  diff <(printf '%s\n' "$nl") <(printf '%s\n' "$ns") | head -10 | sed 's/^/    /'
fi
# ---- THE THIRD PAIR, the ask guide. TOOL-dDerivedDocket-20 S4 moved the ask contract - routes,
# ---- orientation, parking, discovery filing and the asks-disposed terms - out to its own carrier,
# ---- because the protocol stood a kilobyte under its cap with five units still owing it text. The
# ---- same two refusals, each in its own sentence for the arm meta-gate's reason above.
ASKSHIP="$HERE/ASKS.template.md"
ASKSDOC="$M/guides/UNATTENDED-ASKS.md"
_c10_cmp "$ASKSHIP" "$ASKSDOC"; _c10rc=$?
if [ "$_c10rc" -eq 2 ]; then
  fail 10 "one half of the ask-guide pair is missing, and a parity check with one file is a check that cannot fail: $ASKSHIP / $ASKSDOC"
elif [ "$_c10rc" -ne 0 ]; then
  fail 10 "the shipped ask guide and this repo's installed copy have drifted, so the kit ships something other than what it runs on: $ASKSHIP vs $ASKSDOC"
  diff <(printf '%s\n' "$nl") <(printf '%s\n' "$ns") | head -10 | sed 's/^/    /'
fi
# THE PAIR COUNT, on the report channel, so a reader can tell which pairs this check actually compared
# without opening this file. Derived from the three pairs above rather than typed: a pair added without
# a row here is a pair the count does not name, which is visible in one run.
_c10_names=(protocol verbs asks); _c10_ship=("$SHIP" "$VERBSHIP" "$ASKSHIP"); _c10_live=("$LIVEDOC" "$VERBDOC" "$ASKSDOC")
_c10_n=0
for _c10_i in "${!_c10_names[@]}"; do
  [ -f "${_c10_ship[$_c10_i]}" ] && [ -f "${_c10_live[$_c10_i]}" ] && _c10_n=$((_c10_n + 1))
done
report "check 10 byte-compared $_c10_n of its ${#_c10_names[@]} pairs: ${_c10_names[*]}"

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
  # THE FOURTH SPELLING IS NOT JOINED, AND THAT IS A KNOWN GAP RATHER THAN AN OVERSIGHT.
  # The import's allow-list at the top of this file is a fourth hand-typed spelling of this leg's
  # conf key set - beside the initialiser block, this example and section 8's table - and it is the
  # only one of the four nothing reads. A key added to the other three and forgotten there is dropped
  # SILENTLY: it keeps its initialised default and every gate stays green.
  #
  # The join was WRITTEN and then WITHDRAWN unlanded, for a reason worth more than the check: its two
  # refusal branches each owe an arm under the harness meta-gate, the only suite that can carry one is
  # on no bar and could not complete a run on the node that wrote this, and a refusal whose failing
  # case nobody has observed is exactly what this leg's own header calls an assertion about nothing.
  # The predicate itself WAS measured over the tracked tree before it was withdrawn - the keys this
  # example declares AND this file initialises, minus the allow-list, is EMPTY, with no near-miss in
  # either direction - so there is no live instance today and the hazard is the next key, not this
  # tree. TOOL-aHoistedPass-40 carries the predicate, the sentinel design and that measurement.
  if [ -n "$(printf '%s' "$undocumented$phantom$proj_extra" | tr -d '[:space:]')" ]; then
    fail 22 "the protocol's binding key table and the declared conf disagree, so a key is either configurable and undocumented or documented and dead. undocumented in the protocol: ${undocumented:-none} | documented but in no example: ${phantom:-none} | set by this project and undocumented: ${proj_extra:-none}"
  fi
fi

# ---- 35: THE LANDING SHAPE, GRADED AND ANNOUNCED. TOOL-dDerivedDocket-3 S1. The announcement is as
# ---- load-bearing as the refusals beside it: `LANDER_MODE` decides which commit the landing bar
# ---- grades and which verb commits the record, so a reader of a green bar who cannot tell
# ---- `in-place` from a blank line is reading a verdict about a different landing.
# ----
# ---- THE CLOSED SET AND ITS DEFAULT COME FROM THE DRIVER, off the two marked lines, never retyped
# ---- here. That is this file's own header rule for the phase and DoD sets, and a landing mode is
# ---- the same kind of thing. A marker that stops resolving is a REFUSAL, because a set read as
# ---- empty would make every declared value legal.
_c35_line=$(grep -A1 -F 'gov:lander-mode-set' "$DRIVER" 2>/dev/null | tail -1)
_c35_set=$(printf '%s' "$_c35_line" | sed 's/[^a-z|-]//g' | tr '|' ' ')
_c35_def=$(grep -F 'gov:lander-mode-default' "$DRIVER" 2>/dev/null | sed -n 's/.*LANDER_MODE=\([a-z-]*\).*/\1/p' | head -1)
if [ -z "${_c35_set// /}" ] || [ -z "$_c35_def" ]; then
  fail 35 "this leg cannot read the closed LANDER_MODE set and its default off the driver's own marked lines, so the declared mode would be graded against an empty set and every value, including a misspelling, would read as legal: $DRIVER"
else
  _c35_eff="$LANDER_MODE"; _c35_src=declared
  [ -n "$_c35_eff" ] || { _c35_eff="$_c35_def"; _c35_src=defaulted; }
  case " $_c35_set " in
    *" $_c35_eff "*)
      echo "unattended: LANDER_MODE $_c35_eff ($_c35_src) — the landing shape every run in this project takes, graded against the driver's own set: $_c35_set" ;;
    *)
      fail 35 "LANDER_MODE is declared outside the driver's closed set, so every run in this project refuses at conf load and no landing is reachable at all, declared $LANDER_MODE against the set $_c35_set" ;;
  esac
fi
# ---- 36: THE DURABLE RESTART CARRIER, GRADED AND ANNOUNCED. TOOL-dDerivedDocket-5 S1 and S2.
# ---- Three questions, and the first is the one a project gets wrong silently: the switch's value.
# ----
# ---- THE CLOSED SET AND THE DEFAULT COME FROM THE DRIVER, off its two marked lines, never retyped
# ---- here — check 35's own rule for LANDER_MODE, applied to the sibling switch beside it. A marker
# ---- that stops resolving is a REFUSAL, because a set read as empty makes every value legal.
# ----
# ---- WHAT THIS DOES NOT CHECK: that the declared tools EXIST, that the carrier is really durable,
# ---- or that any restart was ever filed. No script reaches a harness scheduler store — that is the
# ---- premise the whole feature rests on — so filing and reaping stay agent-attested, exactly as the
# ---- keepalive's are. This grades the DECLARATION and nothing beyond it.
_c36_line=$(grep -A1 -F 'gov:resume-schedule-set' "$DRIVER" 2>/dev/null | tail -1)
_c36_set=$(printf '%s' "$_c36_line" | sed 's/[^a-z|]//g' | tr '|' ' ')
_c36_def=$(grep -F 'gov:resume-schedule-default' "$DRIVER" 2>/dev/null | sed -n 's/.*RESUME_SCHEDULE=\([a-z]*\).*/\1/p' | head -1)
if [ -z "${_c36_set// /}" ] || [ -z "$_c36_def" ]; then
  fail 36 "this leg cannot read the closed RESUME_SCHEDULE set and its default off the driver's own marked lines, so the declared switch would be graded against an empty set and every value, a misspelling included, would read as legal: $DRIVER"
else
  _c36_eff="$RESUME_SCHEDULE"; _c36_src=declared
  [ -n "$_c36_eff" ] || { _c36_eff="$_c36_def"; _c36_src=defaulted; }
  case " $_c36_set " in
    *" $_c36_eff "*)
      echo "unattended: RESUME_SCHEDULE $_c36_eff ($_c36_src) — whether a hold that owes a restart prints one for the agent to file, graded against the driver's own set: $_c36_set" ;;
    *)
      fail 36 "RESUME_SCHEDULE is declared outside the driver's closed set, so every run in this project refuses at conf load and no verb is reachable at all, declared $RESUME_SCHEDULE against the set $_c36_set"
      _c36_eff=refused ;;
  esac
  if [ "$_c36_eff" = on ]; then
    # ---- THE PAIR IS REQUIRED WHILE THE SWITCH IS ON, and undeclared is not defaulted: a hold then
    # ---- records `none · no carrier` and the run pauses with nothing filed to restart it. --hold
    # ---- itself never refuses for this — the hold is the safe state — so the refusal lives here.
    for _c36_k in RESUME_SCHEDULE_CREATE RESUME_SCHEDULE_DELETE; do
      eval "_c36_v=\${$_c36_k}"
      [ -n "$_c36_v" ] || fail 36 "RESUME_SCHEDULE is $_c36_eff ($_c36_src) and this key is undeclared, so every hold this project takes records 'none · no carrier' and pauses with nothing filed to restart it; declare the pair, or write RESUME_SCHEDULE=\"off\": $_c36_k"
    done
    # ---- THE CARRIER MAY NOT BE THE KEEPALIVE'S. Graded on the CREATE half, which is the one that
    # ---- files the task: this project's own conf declares that store session-scoped, so a restart
    # ---- filed there dies with the session it exists to outlive and every hold then reads as owing
    # ---- a restart that can never fire.
    if [ -n "$RESUME_SCHEDULE_CREATE" ] && [ "$RESUME_SCHEDULE_CREATE" = "$KEEPALIVE_CREATE" ]; then
      fail 36 "the declared durable restart carrier is the keepalive's own create tool, and that store is session-scoped, so every restart filed there dies with the session it exists to outlive: RESUME_SCHEDULE_CREATE and KEEPALIVE_CREATE are both $RESUME_SCHEDULE_CREATE"
    fi
  elif [ "$_c36_eff" = off ]; then
    echo "unattended: RESUME_SCHEDULE is off — no hold in this project owes a durable restart, and every held run waits for a person to type --resume"
  fi
fi

# ---- ...and the self-test surface the in-place close derives its announcement from. A DECLARED
# ---- prefix matching no tracked path is a refusal: it reads as coverage of a surface that is not
# ---- there, and the landing of kit work under it is then never told the flagged bar is owed. A
# ---- BLANK key is not a refusal - an adopter may owe no such bar at all - but it is ANNOUNCED,
# ---- because a term that silently un-owes a Definition-of-Done clause is indistinguishable from
# ---- one that found nothing to owe.
if [ -z "$SELFTESTS_OWED_PATHS" ]; then
  echo "unattended: SELFTESTS_OWED_PATHS is blank — no landing range in this project can ever be told the kit Definition of Done owes the flagged bar, so that clause has no declared surface to be read against"
else
  _c35_dead=""
  for _c35_p in $SELFTESTS_OWED_PATHS; do
    if [ -n "$(GIT ls-files -- "$_c35_p" 2>/dev/null | head -1)" ]; then
      echo "unattended: SELFTESTS_OWED_PATHS entry $_c35_p — resolves to tracked paths"
    else
      _c35_dead="$_c35_dead $_c35_p"
    fi
  done
  [ -z "${_c35_dead// /}" ] \
    || fail 35 "SELFTESTS_OWED_PATHS declares a prefix that matches no tracked path, so it reads as coverage of a surface that is not in this tree and an in-place landing of kit work under it would never be told the flagged bar is owed:$_c35_dead"
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
#
# THREE lists, not two, and the third is `coresec` - the CORE handle:section pairs. The body term
# below is the strictest thing in this leg and it iterated `core`, which is core PLUS extra, while
# its own rationale promised core-only. An adopter declaring the documented `DIRECTIVES_EXTRA`
# knob then got a permanent `fail 16` on a rendered carrier they cannot edit, because the
# memory-tree kit ships BUILD-METHOD.md with `role = "rendered"` and the doc-parity leg
# byte-compares it. No route to green, on an unguarded merge-bar leg. Closing-review F3.
core=""; corescope=""; coresec=""
for _de in $DIRECTIVES_CORE $DIRECTIVES_EXTRA; do
  _dh=${_de%%:*}; _dr=${_de#*:}; _ds=${_dr%%:*}; _dc=${_dr#*:}
  [ "$_dc" = "$_dr" ] && _dc=all
  core="$core$_dh:$_ds
"
done
for _de in $DIRECTIVES_CORE; do
  _dh=${_de%%:*}; _dr=${_de#*:}; _ds=${_dr%%:*}; _dc=${_dr#*:}
  [ "$_dc" = "$_dr" ] && _dc=all
  corescope="$corescope$_dh:$_dc
"
  coresec="$coresec$_dh:$_ds
"
done
core=$(printf '%s' "$core" | grep . | sort -u)
corescope=$(printf '%s' "$corescope" | grep . | sort -u)
coresec=$(printf '%s' "$coresec" | grep . | sort -u)
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
    # ---- THE BODY TERM (TOOL-aHoistedPass-2). Existence is not a route. Arm B above asserts the
    # ---- cited section EXISTS and never opens it, so 17 of 17 handles pointed at real sections
    # ---- that stated no rule about them — measured, and it is the defect this term closes: a run
    # ---- resolving `passes-harnessed` read M6, found nothing, and built inline.
    # ----
    # ---- CORE-ONLY, on `corescope`'s own principle, and it iterates `coresec` rather than `core`
    # ---- because `core` is core PLUS extra. A project's DIRECTIVES_EXTRA rows are hand-authored
    # ---- and must not red an adopter for prose the kit never asked them to write — and the rendered
    # ---- carrier is byte-compared by the doc-parity leg, so an adopter redded here has no route to
    # ---- green at all. This paragraph said CORE-ONLY for a round while the loop below said
    # ---- otherwise; the arm under `an extra handle is graded for EXISTENCE and not for BODY` is
    # ---- what now decides which of the two is true. Closing-review F3.
    # ----
    # ---- `coresec` is split from the SAME registry parse as `core` and `corescope`, so no second
    # ---- spelling of the handle set exists to drift — which is the class this whole build is about.
    # ----
    # ---- BACKTICKS, NOT A WORD BOUNDARY, and that closes two holes with one token shape. A bare
    # ---- `<!-- anchors: … -->` satisfies a naive term while the section states no rule, and
    # ---- `researched` is an ordinary English past participle a future prose edit would satisfy by
    # ---- accident, certifying a section that says nothing.
    # ----
    # ---- THE COMMENT STRIP IS BLOCK-WISE, SPANNING LINES, and that is the whole point of the term
    # ---- rather than a detail of it. A filter dropping lines that MATCH `^[[:space:]]*<!--` drops
    # ---- only a comment's FIRST line, so a multi-line comment carrying the anchor on line two
    # ---- satisfies it. Measured on four fixtures built from the real file: the naive form PASSES
    # ---- that evasion and this form REDS it, with an honest rule sentence green in both.
    # ----
    # ---- WHAT IT DOES NOT CHECK, said here because a structural check reads as a semantic one to
    # ---- everybody who did not write it: it grades that the section NAMES its handle in a form a
    # ---- comment cannot fake. It does not grade that the sentence around the name states the rule,
    # ---- so a dead anchor inside a real sentence still passes. Strictly stronger than
    # ---- existence-only, strictly weaker than semantics.
    for pair in $coresec; do
      hnd=${pair%%:*}; sec=${pair#*:}
      _body=$(awk -v s="^## $sec( |\$)" '
        $0 ~ s { inb = 1; next }
        inb && /^## / { exit }
        inb {
          line = $0
          while (1) {
            if (incm) { i = index(line, "-->"); if (i == 0) { line = ""; break }
                        line = substr(line, i + 3); incm = 0; continue }
            i = index(line, "<!--"); if (i == 0) break
            pre = substr(line, 1, i - 1); rest = substr(line, i + 4)
            j = index(rest, "-->")
            if (j == 0) { line = pre; incm = 1; break }
            line = pre substr(rest, j + 3)
          }
          print line
        }' "$M/guides/BUILD-METHOD.md")
      printf '%s' "$_body" | grep -qF -- "\`$hnd\`" \
        || fail 16 "a directive's cited build-method section states nothing about it, so a run resolving the handle reads that section and finds no rule — absent in backticks outside every HTML comment: $pair"
    done
  fi
fi
# ---- 16d: the NON-OVERRIDABLE Definition-of-Done set, joined to the Skill an agent reads, in BOTH
# ---- directions. The same shape as arm A one block up and for the same reason: the driver's
# ---- constant and the Skill's hand-authored paragraph are two artifacts in two languages, and a
# ---- member added to one and forgotten in the other is a run told it may override an item the verb
# ---- will refuse - or worse, told the refusal has an override route it does not have. The Skill
# ---- said ONE item where the driver held TWO for as long as the second existed, and nothing saw it.
# ----
# ---- WHAT THIS DOES NOT CHECK: whether the paragraph's PROSE is correct, only that the member SET
# ---- matches. A paragraph naming both items and describing them backwards passes.
if [ -z "$DOD_NO_OVERRIDE" ]; then
  fail 16 "cannot read DOD_NO_OVERRIDE from the driver, so the join below would compare the Skill against an empty set and pass by finding nothing: $DRIVER"
elif [ ! -f "$tmpl" ]; then
  fail 16 "the kit ships no SKILL.template.md, so the non-overridable set an agent reads cannot be joined to the constant the verb enforces"
else
  # The PARAGRAPH, selected by its own sentence and terminated by the first blank line. Item names
  # are backticked and lowercase-hyphen shaped, which is what excludes the `--abort` route named in
  # the same paragraph without excluding a member the Skill invented.
  _no_tbl=$(awk '
      /items? (has|have) NO override/ { p = 1 }
      p && /^[[:space:]]*$/ { exit }
      p { print }' "$tmpl"     | grep -oE '`[a-z][a-z-]*`' | tr -d '`' | sort -u)
  if [ -z "$_no_tbl" ]; then
    fail 16 "the Skill template carries no non-overridable paragraph this leg can read, so the join would compare the driver's set against nothing and pass by finding nothing; the sentence it looks for names the items and the item names are backticked"
  else
    # The MEMBERS, one per line and deduplicated. A first cut also computed a count here and threw
    # it away to /dev/null, taking the status with it: plumbing that ran, decided nothing, and read
    # as a guard.
    _no_core=$(printf '%s
' $DOD_NO_OVERRIDE | sort -u)
    _no_only_drv=$(comm -23 <(printf '%s
' "$_no_core") <(printf '%s
' "$_no_tbl") | tr '
' ' ')
    _no_only_tbl=$(comm -13 <(printf '%s
' "$_no_core") <(printf '%s
' "$_no_tbl") | tr '
' ' ')
    [ -z "${_no_only_drv//[[:space:]]/}" ] || fail 16 "the driver refuses an override on an item the Skill's non-overridable paragraph does not name, so a run meets a refusal its own instructions said could not happen:$_no_only_drv"
    [ -z "${_no_only_tbl//[[:space:]]/}" ] || fail 16 "the Skill's non-overridable paragraph names an item the driver does not refuse an override on, so a run is told a route is closed that is open:$_no_only_tbl"
  fi
fi

# Arm C: the floor. Mirrors CORE_FLOOR's two branches — undeclared and malformed are both refusals,
# because either one leaves the pin unenforced while the conf still looks configured.
# TOOL-aPromptedMandate-6 fold, review H1 - a floor BELOW the kit's own core count is SLACK BY
# CONSTRUCTION and cannot fire on the deletion it exists to catch. This build shipped exactly that:
# the bump to 13 was reverted by a `git checkout --` during an unrelated probe, and arm C passed
# because it only ever asked whether the count met the floor, never whether the floor met the kit.
_ndc=$(_wc=(${DIRECTIVES_CORE}); echo ${#_wc[@]})
if [ -n "$DIRECTIVES_FLOOR" ] && [ "$DIRECTIVES_FLOOR" -lt "$_ndc" ] 2>/dev/null; then
  fail 16 "DIRECTIVES_FLOOR is declared below the kit's own core directive count, so the shrink-only pin is slack by construction and a deleted core handle would pass it: $DIRECTIVES_FLOOR against $_ndc"
fi
if [ -z "$DIRECTIVES_FLOOR" ]; then
  fail 16 "DIRECTIVES_FLOOR is undeclared in .unattended.conf, and with no floor a deleted directive is indistinguishable from a set that never had one"
else
  case "$DIRECTIVES_FLOOR" in
    ''|*[!0-9]*) fail 16 "DIRECTIVES_FLOOR is not a plain integer, so the shrink-only pin on the directive set is unenforced while the conf still looks configured: $DIRECTIVES_FLOOR" ;;
    *) ndir=$(_wc=(${DIRECTIVES_CORE}); echo ${#_wc[@]})
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
        # THE TABLE RUNS PAST THE SET IT GRADES, deliberately. It used to stop at `twelve`, which is
        # exactly where the core set stood - so the FIRST correct sentence written after the
        # thirteenth item landed mapped to -1 and red the leg for naming the right number. A count
        # word this table cannot read is indistinguishable from a miscount, and the cheap half of
        # that is the table. TOOL-dDerivedDocket-17.
        thirteen) cn=13 ;; fourteen) cn=14 ;; fifteen) cn=15 ;; sixteen) cn=16 ;;
        seventeen) cn=17 ;; eighteen) cn=18 ;; nineteen) cn=19 ;; twenty) cn=20 ;;
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

# ---- 34: THE LAND SECTION CARRIES BOTH LANDING SHAPES. TOOL-dDerivedDocket-3 S6, AC4. The Skill is
# ---- ONE render shared by every adopter and the mode is a conf value, so this section is graded
# ---- unconditionally rather than under `LANDER_MODE`: an adopter who switches the key must not have
# ---- to re-render a document that never described the mode they switched to.
# ----
# ---- SECTION-SCOPED, for check 18's recorded reason: a file-wide locator goes green the moment the
# ---- literal appears in any other section, and `--prepare` legitimately appears in the Close
# ---- section too. An EMPTY section is its own refusal — an arm reading a section the render never
# ---- emits passes over nothing, which is this leg's own could-not-fail shape.
# ----
# ---- WHAT THIS DOES NOT CHECK: that the sequence WORKS, or that the steps are in the right order.
# ---- It grades presence of the two verbs and ABSENCE of a merge into the node's own default branch.
# ---- The order is protocol section 6's sentence and a reader's job.
if [ -f "$tmpl" ]; then
  _c34_land=$(tr -d '\r' < "$tmpl" | awk '/^## Land[ \t]*$/ { f = 1; next } f && /^## / { f = 0 } f')
  if [ -z "${_c34_land//[[:space:]]/}" ]; then
    fail 34 "the Skill template carries no Land section body, so every assertion about the landing an agent is told to perform would be graded over nothing and would pass by finding nothing: $tmpl"
  else
    _c34_miss=""
    for _c34_f in "--prepare" "--land"; do
      printf '%s\n' "$_c34_land" | grep -qF -- "$_c34_f" || _c34_miss="$_c34_miss $_c34_f"
    done
    [ -z "${_c34_miss// /}" ] \
      || fail 34 "the Skill's Land section names neither landing shape in full - an in-place landing prepares the merge and then pushes exactly it, and a section missing either verb sends an agent to a landing it cannot complete:$_c34_miss in $tmpl"
    # A MERGE INTO THE NODE'S OWN DEFAULT BRANCH is the primary path's fallback text, and it is what
    # survives a half-finished edit of this section. In `in-place` it is wrong twice over: that ref
    # is one this session can move, and it carries whatever else on this node has not been pushed.
    _c34_local=$(printf '%s\n' "$_c34_land" | grep -niE '(merge|merged|merging|merges)[^.]*(local main|local default branch|into main)' || true)
    [ -z "$_c34_local" ] \
      || fail 34 "the Skill's Land section directs a merge into the node's own default branch, which is a ref this session can move and which carries whatever else here is unpushed, so the landing it describes is not the one the bar graded: $_c34_local"
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
  if ! rs_now=$(region "$bre" '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null); then
    report "check 24 skipped for $f — the working build README does not carry exactly one well-formed units pair, so the executing roster cannot be read"
  else
    # THE RETIRE ARM'S BASELINE IS THE PINNED BASE, and the ADD ARM'S IS NOT. `baseline_units` stops
    # at the first commit carrying BUILDING, RUNNING, VERIFYING, LANDING or LANDED - so SPECCING,
    # REVIEWING, FOLDING, RESEARCHING and TESTING are all BEFORE it, and a unit authored `WONTDO`
    # while speccing is already retired at that baseline and owes no row. That window is exactly
    # where a prompt-authorized run does its speccing.
    #
    # The ADD arm keeps the live-phase baseline for the reason its own header states: M2 MANDATES
    # authoring an absent spec, so an addition between BASE and BUILDING is the case that arm exists
    # to PERMIT. A retirement between the same two points is not, and the asymmetry is the point
    # rather than an inconsistency.
    rs_pinned=""; rs_pwhy=""
    if ! rs_pinned=$(pinned_units "$rb" "$bre" "${UNITS_REGION_CUTOFF:-}"); then
      rs_pwhy=$rs_pinned; rs_pinned=""
    fi
    rs_rows=$(grep -F -- ' rescope · item ' "$f" 2>/dev/null || true)
    # ADDED ids: accounted for by an `add` naming it, OR a `supersede` naming it as the successor.
    # An `add` alone would red a correctly performed supersession, whose successor is present now
    # and absent then with no `add` row that the sibling verb would even accept.
    #
    # SKIPPED SEPARATELY, and the message says which question could not be asked. Its two siblings
    # below keep running on their own baseline.
    if [ -n "$rs_why" ]; then
      report "check 24's ADD arm skipped for $f — $rs_why (the RETIRE and supersession arms still ran)"
    else
    for rsid in $(printf '%s\n' "$rs_now" | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u); do
      id_in "$rs_was" "$rsid" && continue
      printf '%s\n' "$rs_rows" | grep -qE "item add $rsid( |\$)" && continue
      printf '%s\n' "$rs_rows" | grep -qE "item supersede [A-Za-z0-9-]+ -> $rsid( |\$)" && continue
      fail 24 "a unit is in the roster this run is executing and was not in the roster it entered BUILDING with, and no rescope row adds or supersedes into it, so the scope moved with nothing on the record saying so: $rsid in $f"
    done
    fi
    # RETIRED units: a status that is WONTDO now and was not so at the PINNED BASE owes a retire or
    # a supersede. Reported SEPARATELY when its own baseline is unreadable, because the whole-check
    # skip this replaces took the ADD arm and the supersession arm down with it.
    if [ -n "$rs_pwhy" ]; then
      report "check 24's RETIRE arm skipped for $f — $rs_pwhy (the ADD arm still ran)"
    else
      # ABSENCE FROM THE PINNED ROSTER IS NOT AN EXEMPTION, and a first cut of this arm made it one.
      # A unit ADDED after the pinned BASE and flipped to WONTDO during the run would then owe a row
      # nowhere: the ADD arm exempts it because `baseline_units`' roster already carries it, and
      # `check_authorization` is a subset test that refuses only REMOVALS, which a status flip is
      # not. Added-then-retired would have been silent — the exact drop units 5 and 6 exist to close,
      # reintroduced by the fix for it.
      #
      # So absence falls back to the LIVE-PHASE baseline instead: a unit that was already WONTDO
      # there was retired before building and owes nothing, and one that was not owes its row. When
      # that baseline is unreadable the fallback is unavailable and the arm asks for the row, which
      # is the strict direction and is the behaviour this arm had before the rekey.
      for rsid in $(printf '%s\n' "$rs_now" | grep -E '\| WONTDO \|' | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u); do
        if id_in "$rs_pinned" "$rsid"; then
          id_rows "$rs_pinned" "$rsid" | grep -q '| WONTDO |' && continue
        elif [ -z "$rs_why" ]; then
          id_rows "$rs_was" "$rsid" | grep -q '| WONTDO |' && continue
        fi
        printf '%s\n' "$rs_rows" | grep -qE "item (retire|supersede) $rsid( |\$)" && continue
        fail 24 "a unit is WONTDO now and was not at the BASE this run pinned, and no rescope row retires or supersedes it, so declared scope was dropped with nothing on the record saying so: $rsid in $f"
      done
    fi
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
# ----
# ---- THE BRIEF LEAVES THE POPULATION (TOOL-aLeakedHandle-7). `--brief` records the brief a pass was
# ---- handed and stages only the run-state file; the brief is already tracked, so the pass's one
# ---- commit carries it, and the pass never declared it because the pass never wrote it. Two
# ---- boundaries, both load-bearing: the PATH the row names and not its directory — a row naming
# ---- `prompts/` excludes nothing under it, or a pass could hide any write there — and the rows in the
# ---- PASS COMMIT'S TREE and not the working copy, so a row appended after the commit hides nothing.
# ---- THE SET IS THE LIBRARY'S (`read_brief_paths`), AND `pass_commit` SUBTRACTS IT FIRST. When only
# ---- this check forgave the brief, a `{run-state, brief}` bookkeeping commit naming the unit was
# ---- selected as the pass commit, graded clean, and the real pass commit was never read — silent on
# ---- the ordinary shape. Now that commit is skipped as bookkeeping and the walk reaches the commit
# ---- that wrote something; the exclusion stays here because that commit still carries the brief
# ---- when the run makes one commit (arm A), and forgiving it there is this check's job.
# ---- What that does NOT buy: a run that writes the brief row and a stray file into the same pass
# ---- commit still hides the stray file — both artifacts are the run's, the limit stated above for
# ---- dispatch rows — and a row naming a path no brief was handed at is excluded here and joined by
# ---- NOTHING: `brief-recorded` grades CLOSED units only, at the BUILD commit and not the pass
# ---- commit, reads the LAST row per unit where this check takes the union, and proves only that the
# ---- row's hash still names the blob at that path. Nothing asserts the path was a brief.
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
    if ! check_rev "$dsgrp"; then
      report "check 23 skipped for $dsunit in $f — the recorded group anchor does not resolve in this clone, so the commit window cannot be opened"
      continue
    fi
    if ! check_head_reaches "$dsgrp"; then
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
    # LOOP-INVARIANT, HOISTED. `$dshit` does not change inside this loop, so reading its
    # subject once per SIBLING was a git spawn per sibling to answer the same question.
    # TOOL-aQuenchedHarness-7.
    dshitsub=$(GIT log -1 --format=%s "$dshit" 2>/dev/null)
    while IFS= read -r dssib; do
      [ -n "$dssib" ] || continue
      dssitem=${dssib#* dispatch · item }; dssitem=${dssitem%% · reason *}
      dssunit=${dssitem#* }
      [ "$dssunit" = "$dsunit" ] && continue
      # ANCHORED, like every other id test in this file. Left as a substring, a group holding a
      # `-1` and a `-10` reports the pair as ambiguous on the `-1` commit and reds a correct run.
      id_in "$dshitsub" "$dssunit" && dsother="$dssunit"
    done <<DSSIBS
$(printf '%s\n' "$dsrows" | grep -F -- " dispatch · item $dsgrp ")
DSSIBS
    if [ -n "$dsother" ]; then
      printf 'unattended: check 23 — one commit names two passes of the same dispatch group, so a subset test over it cannot say which pass wrote what and the attribution this comparison rests on is not available: %s and %s in %s\n' "$dsunit" "$dsother" "$f"
      continue
    fi
    # THE EXCLUSION SET: every path a ` brief · item <unit> · reason ` row names for THIS unit, read
    # from the run-state file AT THE PASS COMMIT by the kit library — the same `read_brief_paths`
    # that `pass_commit` subtracted before it selected `$dshit`, so the selector and this grader
    # cannot forgive different paths. Only the row's side is normalised: `diff-tree` already prints
    # git's canonical spelling. Newline-delimited with a newline at both ends, so the membership test
    # below is an exact match and never a prefix or a containment.
    dsnl=$'\n'; dsbrief="$dsnl$(read_brief_paths "$dshit" "$dsunit" "$f")$dsnl"
    # THE SUBSET TEST. Declaring MORE than you use is conservative and fine; writing outside the
    # declaration is the defect.
    dsout=""
    for dsq in $(GIT diff-tree --no-commit-id --name-only -r "$dshit" 2>/dev/null | grep -v -x -F "$f"); do
      # EXACT membership, deliberately not `covers`: that is a containment test, and a row naming a
      # directory would then hide everything under it.
      case "$dsbrief" in *"$dsnl$dsq$dsnl"*)
        report "check 23 excluded $dsq for $dsunit in $f — the path its brief row names, staged by --brief rather than written by the pass"
        continue ;;
      esac
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
# BATCHED: two greps over the whole population, not two per file. Absorbed from inCMS, which
# measured 132.2 s -> 2.795 s on its own corpus with the verdict asserted IDENTICAL. The verdict is
# what matters and the equality is fixtured, because a speed-up that changes a verdict is not an
# optimisation.
#
# `/dev/null` IS LOAD-BEARING. `grep -c` omits the filename when handed ONE file and prefixes it when
# handed several, so a corpus that happens to hold a single build README would silently change the
# output shape and this parse would read nothing — passing by finding no rows. The extra argument
# forces the prefix in both cases, and /dev/null contributes a `0` row that names a path no build
# ever has.
bad_units=""
_c21_files=$(GIT ls-files "$M/builds/*/README.md" 2>/dev/null)
if [ -n "$_c21_files" ]; then
  # TWO greps and ONE awk for the whole population — THREE processes, not 2N.
  #
  # THE FIRST CUT OF THIS WAS NOT AN OPTIMISATION AND THE MEASUREMENT SAID SO. It batched the greps
  # and then parsed their output with a `sed` PER FILE, trading 176 greps for 2 greps plus 176 seds:
  # measured over 88 build READMEs, 109 ms became 116 ms. Process creation is the cost on this node,
  # so the join has to happen in ONE pass or the batching buys nothing.
  #
  # `/dev/null` IS LOAD-BEARING. `grep -c` omits the filename when handed ONE file and prefixes it
  # when handed several, so a corpus holding a single build README would silently change the output
  # shape and this parse would read nothing — passing by finding no rows. The extra argument forces
  # the prefix in both cases and contributes a `0` row for a path no build ever has.
  bad_units=$(grep -cxF -- '<!-- gen:build-units -->' /dev/null $_c21_files 2>/dev/null \
    | awk -F: -v closes="$(grep -cxF -- '<!-- /gen:build-units -->' /dev/null $_c21_files 2>/dev/null)" '
        BEGIN { n = split(closes, L, "\n")
                for (i = 1; i <= n; i++) { p = L[i]; sub(/:[0-9]*$/, "", p)
                                           c = L[i]; sub(/^.*:/, "", c); CL[p] = c } }
        $0 !~ /^\/dev\/null:/ {
          path = $0; sub(/:[0-9]*$/, "", path)
          open = $0; sub(/^.*:/, "", open)
          if (open != 1 || CL[path] != 1) printf " %s", path
        }')
fi
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

    # ---- TOOL-aGroundedOrientation-2 - the ORIENTATION PROBES precede the build-folder write.
    # ---- Same slice, same shape, fourth locator. The defect: step 1 said "in the /session-kickoff
    # ---- manner", which is a posture a reader satisfies without running anything, while the engine
    # ---- that runs the probes is invoked at step 6 - after step 3 has authored the ROSTER and step 4
    # ---- has pushed it. Under a published anchor that roster IS the authorization, so a seam found
    # ---- late costs a commit and a push. Measured on the run that added this check: its own roster
    # ---- grew after BASE and check 24 caught it.
    # ----
    # ---- It does NOT assert WHICH probes run. The kickoff engine's Step 4 owns that list and a gate
    # ---- enumerating it becomes a third carrier that reds when that engine legitimately changes.
    # ---- SECTION-scoped, never file-scoped, for check 18's own recorded reason: a file-wide locator
    # ---- goes green when the literal sits in any other section, and is blind to a third start path.
    prbl=$(printf '%s\n' "$psec" | awk -F'\t' 'index($2, "RUN the orientation probes") { print $1; exit }')
    wrtl=$(printf '%s\n' "$psec" | awk -F'\t' 'index($2, "Write the build folder") { print $1; exit }')
    if [ -z "$prbl" ] || [ -z "$wrtl" ]; then
      fail 20 "the Skill's prompt path does not name both its orientation-probe step and its build-folder write, so the ordering that puts the probes before the roster cannot be checked at all and would compare against an empty string; it looks for 'RUN the orientation probes' and 'Write the build folder'"
    else
      [ "$prbl" -lt "$wrtl" ] || fail 20 "the Skill's prompt path runs its orientation probes AFTER it writes the build folder, so the roster is authored and pushed before the probes that inform it, and correcting it costs a commit and a push: $prbl against $wrtl"
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
nverbs=$(_wc=(${VERBS_ALL}); echo ${#_wc[@]})
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
  # ---- THE CONTRACT ARM READS THE VERB CARRIER AND NOTHING ELSE (TOOL-dFoldedVerdict-5). Accepting
  # ---- a hit in either that file or the protocol would pass a HALF-COMPLETED move — the state that
  # ---- leaves the verbs in both places — so the fallback is deliberately absent. A missing carrier
  # ---- is its own named refusal and not a skipped arm: a guard of the form `[ -f X ] && read X`
  # ---- with no else is the shape check 10's own header calls a check that cannot fail.
  [ -f "$VERBSHIP" ] || fail 26 "the verb carrier is absent, so the arm that joins every declared verb to the contract cannot run and would otherwise skip in silence: $VERBSHIP"
  _c26_ship=""; [ -f "$VERBSHIP" ] && _c26_ship=$'
'$(cat "$VERBSHIP")$'
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
    if [ -f "$VERBSHIP" ]; then
      case "$_c26_ship" in
        *$'
'"- "?"$v"?" — "*) : ;;
        *) fail 26 "a declared verb has no entry in the verb carrier, so the contract a run is measured against does not describe a verb that run can call: $v in $VERBSHIP" ;;
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
    # THE EXEMPTION IS A CLASS, NOT A SPELLING. `grep -q` was the only form excluded here, and the
    # property that earns the exclusion is that a PRESENCE TEST cannot yield the key's value and so
    # cannot be a second answer to it. `grep -l` has exactly that property — it returns FILENAMES —
    # and was not excluded, so batching a per-file `grep -q` discovery into one `grep -l` tripped
    # this check while changing nothing it grades. Found when `TOOL-aScouredKit-6` did precisely
    # that in check-playbook.sh.
    #
    # `-l` and `-q` only. NOT `-c`, which yields a count that a caller can branch on, and not the
    # bare form, which yields the matching LINE — that is the read this check exists to catch. The
    # widening is deliberately the narrowest one that covers the class.
    KB_CARETS="$KB_CARETS$(grep -nE '\^[A-Za-z_]' "$_f" | grep -vE '^[0-9]+:[[:space:]]*#' | grep -vE 'grep [^|]*-[A-Za-z]*[ql]' | sed "s|^|$_f	|" || true)
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


# ---- check 30 - a --plan run may never claim terminality over a build it graded nothing on.
# TOOL-dHonouredPark, closing review round 3. A CORPUS check rather than a fixture one, and
# deliberately: the blocker it gates was live on FIVE tracked builds while every fixture arm in
# this kit was green. The predicate is the SHAPE, not the branch - any output carrying both a
# NOT A UNIT row and the terminal verdict is a build being told it is finished by a verb that
# graded nothing on it. It redded on those five the day it was written, which is the failing case
# observed before landing.
#
# A build whose --plan REFUSES is skipped: a refusal is a verdict this check has no opinion about.
if [ -d "$MEMORY_ROOT/builds" ]; then
  _pv_seen=0; _pv_bad=""; _pv_drv="$(cd "$(dirname "$0")" && pwd)/unattended.sh"
  # ---- THE DRIVER IS ASKED ABOUT THE BUILDS THAT CAN POSSIBLY RED, not about all of them.
  # TOOL-aQuenchedHarness-10.
  #
  # Getting the verdict from the driver is the right shape and is unchanged: deciding it here would
  # be a second implementation of the driver's predicate rather than a second opinion on its output.
  # What was wrong was the POPULATION. Every tracked build got its own `--plan`, and one `--plan`
  # costs 3.8 s on this tree - 29 spawned processes, 13 awk and 9 grep of them, re-reading spec files
  # this leg can read once for the whole corpus. Over 102 builds that was ~390 s, the largest single
  # item on the longest leg of the bar, spent almost entirely on builds that cannot produce the row
  # this check looks for.
  #
  # THE FILTER IS A NECESSARY CONDITION AND NEVER THE VERDICT. A `NOT A UNIT` row is emitted at
  # exactly two places in the driver, and both are keyed on one spec: its status header did not
  # parse, or its heading id did not. A build with no such spec cannot emit the row, so passing over
  # it cannot hide a red. A build WITH one is handed to the driver, which decides both halves of the
  # conjunction - this filter says nothing at all about the terminal half, and over-selecting is
  # free. On this tree it selects five builds, which are the same five the check redded on the day
  # it was written.
  #
  # THE PATTERNS ARE THE DRIVER'S OWN AND ARE ASSERTED AGAINST IT. A filter keyed on a predicate
  # spelled twice is a filter that silently stops selecting when one copy moves, and a check whose
  # population quietly empties reports clean forever. If `spec_facts` stops spelling either pattern
  # this way, this REFUSES instead.
  #
  # AN UNREADABLE OR EMPTY SPEC SELECTS ITS BUILD, because that is what the driver does with one:
  # `spec_facts` emits an empty row for a path it cannot read, and awk's `FNR==1` never fires for a
  # zero-length file, so neither yields an id or a status and both become `NOT A UNIT`.
  _pv_pid='^# [A-Za-z0-9][A-Za-z0-9-]* '
  _pv_pst='^\*\*Status:\*\* [A-Z]+ '
  if ! grep -qF "$_pv_pid" "$_pv_drv" 2>/dev/null || ! grep -qF "$_pv_pst" "$_pv_drv" 2>/dev/null; then
    fail 30 "the driver no longer spells one of the two patterns this check selects its population with, so the selection below is keyed on a predicate the driver has moved away from and would quietly grade nothing: $_pv_drv"
  else
    _pv_ok=""; _pv_cand=""; _pv_n=0; _pv_seed=""; _pv_nseed=0
    # `drop_working_specs` spelled as the driver spells it: a path under `spec/_<dir>/` is scratch,
    # not a spec, and enumerating one produced a NOT A UNIT row for a notes file.
    for _pv_f in $(GIT ls-files "$MEMORY_ROOT/builds/*/spec/*.md" 2>/dev/null | grep -vE '/spec/_[^/]*/'); do
      _pv_n=$((_pv_n+1))
      _pv_s=${_pv_f#"$MEMORY_ROOT/builds/"}; _pv_s=${_pv_s%%/*}
      # THE CANARY SAMPLE, collected here because this is the only pass over the build slugs.
      case " $_pv_seed " in
        *" $_pv_s "*) ;;
        *) [ "$_pv_nseed" -ge 3 ] || { _pv_seed="$_pv_seed $_pv_s"; _pv_nseed=$((_pv_nseed+1)); } ;;
      esac
      if [ -r "$_pv_f" ] && [ -s "$_pv_f" ]; then
        _pv_ok="$_pv_ok$_pv_f
"
      else
        _pv_cand="$_pv_cand $_pv_s"
      fi
    done
    # ONE AWK PASS OVER THE WHOLE CORPUS, chunked by xargs because 551 spec paths are 41 KB of argv
    # and Windows caps a command line at 32 KB - a single invocation would fail on the platform this
    # leg is most often run on, and it would fail by not running rather than by reporting.
    if [ -n "$_pv_ok" ]; then
      while IFS= read -r _pv_f; do
        [ -n "$_pv_f" ] || continue
        _pv_s=${_pv_f#"$MEMORY_ROOT/builds/"}; _pv_cand="$_pv_cand ${_pv_s%%/*}"
      done < <(printf '%s' "$_pv_ok" | xargs -s 20000 awk '
        { sub(/\r$/,"") }
        FNR==1 { if (f != "" && (id == "" || st == "")) print f; f=FILENAME; id=""; st="" }
        /^# [A-Za-z0-9][A-Za-z0-9-]* / { if (id == "") id=$2 }
        /^\*\*Status:\*\* [A-Z]+ / { if (st == "") st=$2 }
        END { if (f != "" && (id == "" || st == "")) print f }' 2>/dev/null)
    fi
    _pv_slugs=""
    for _pv_s in $_pv_cand; do
      case " $_pv_slugs " in *" $_pv_s "*) ;; *) _pv_slugs="$_pv_slugs $_pv_s" ;; esac
    done
    # THE ASK ALWAYS CARRIES A CANARY SAMPLE, and it is a SAMPLE rather than one build.
    # The liveness assertion below exists because the first cut of this check resolved the driver
    # path wrongly and walked zero builds; on a corpus that selects nothing, that assertion would
    # pass over an empty ask and stop meaning anything. So the driver is always asked about
    # something.
    #
    # ONE canary was not enough, and the kit's own cross-component fixture proved it: a single
    # build refusing for its own reasons - a broken units region, in that arm deliberately - drove
    # `_pv_seen` to zero and RED a check that the old whole-corpus walk left silent, because some
    # OTHER build there still graded. A refusal is a verdict this check has no opinion about, so
    # liveness must not be hostage to which build happens to sort first. Three is enough to make
    # that accident unlikely and is ~11 s, and the assertion stays honest: if all three refuse,
    # something is wrong with the driver path and saying so is the whole point.
    for _pv_s in $_pv_seed; do
      case " $_pv_slugs " in *" $_pv_s "*) ;; *) _pv_slugs="$_pv_slugs $_pv_s" ;; esac
    done
    if [ -n "$_pv_slugs" ]; then
      # ONE DRIVER PROCESS FOR THE WHOLE SELECTION. `--plan` takes several slugs and frames each
      # one's output with its own rc; each still runs in its own subshell, so one build's refusal
      # cannot colour the next. The frames are read with a state machine rather than split on, so a
      # build whose plan output happens to contain the marker text cannot merge two verdicts.
      _pv_cur=""; _pv_buf=""
      while IFS= read -r _pv_l || [ -n "$_pv_l" ]; do
        case "$_pv_l" in
          "unattended-plan-open: "*) _pv_cur=${_pv_l#unattended-plan-open: }; _pv_buf="" ;;
          "unattended-plan-rc: "*)
            _pv_rest=${_pv_l#unattended-plan-rc: }
            _pv_s=${_pv_rest%% *}; _pv_rc=${_pv_rest##* }
            # A build whose --plan REFUSES is skipped: a refusal is a verdict this check has no
            # opinion about, which is what the old `|| continue` said.
            if [ "$_pv_s" = "$_pv_cur" ] && [ "$_pv_rc" = 0 ]; then
              _pv_seen=$((_pv_seen+1))
              case "$_pv_buf" in
                *"NOT A UNIT"*)
                  case "$_pv_buf" in
                    *"every tracked spec is terminal"*) _pv_bad="$_pv_bad $_pv_s" ;;
                  esac ;;
              esac
            fi
            _pv_cur=""; _pv_buf="" ;;
          *) [ -n "$_pv_cur" ] && _pv_buf="$_pv_buf
$_pv_l" ;;
        esac
      # `--framed` UNCONDITIONALLY: the loop below reads frames, so it must never be handed the
    # unframed form. Letting the driver decide by arity meant a corpus of one build produced no
    # frames, the loop counted no verdicts, and the liveness branch red a healthy tree.
    done < <(bash "$_pv_drv" --plan --framed $_pv_slugs 2>/dev/null)
    fi
    # LIVENESS, IN TWO PARTS, because the check now has two stages and either can empty out. The
    # scan must have read specs - a selector over nothing selects nothing and looks clean - and the
    # driver must have returned a verdict for something it was asked about.
    [ "$_pv_n" -gt 0 ] || fail 30 "the spec scan that selects this check's population read no tracked spec at all, so both the selection and the clean result below are about an empty corpus rather than about the builds: $MEMORY_ROOT/builds"
    [ "$_pv_seen" -gt 0 ] || fail 30 "the driver returned no verdict for any build this check asked it about, so a clean result here is about a driver path that answered nothing rather than about the corpus:$_pv_slugs"
    [ -z "$_pv_bad" ] || fail 30 "a build's --plan reports NOT A UNIT rows AND claims every tracked spec is terminal, so a reader picking up work is told a build is finished by a verb that graded nothing on it:$_pv_bad"
  fi
fi


# ---- check 31 - the adopter whose ROUTE does not resolve is TOLD, on every bar. TOOL-aHoistedPass-9,
# the gate-time half of ruling D4: `govkit apply` refuses the same gap at the act that CREATES it and
# only for installs made after it lands, while this runs on every bar of every adopter forever -
# including the whole population that arm can never reach. Neither subsumes the other.
#
# THE SECTION COMES OUT OF THE REGISTRY, never typed here. `passes-harnessed` names its carrier
# section in the driver's DIRECTIVES_CORE, and a literal section token in this block would go on
# grading a section the directive no longer names the day the handle is re-pointed.
#
# ONE ANNOUNCED SKIP PER CASE this check cannot COMPARE, each naming its OWN subject. The BRANCHES
# are the count and no numeral is typed beside them: F6 added the two Skill cases and left a `FIVE`
# here that was two short, in a header whose enumeration is load-bearing. A guard
# that a binding pair EXISTS is not a guard that it COVERS, and an absence-only assertion passes when
# the subject was never there - so a check that cannot compare SAYS so rather than reporting a
# reassuring zero. The announcement is therefore this check's liveness assertion and no separate
# vacuity branch is owed. ONE LINE PER UNRESOLVED PATH: a skip whose subject is a SET leaves a reader
# unable to say which path it was about, which is the shape this build exists to remove.
#
# SKIP, NOT FAIL, ON AN ABSENT DIRECTORY, and that split IS the ruling. An absent directory means the
# route's kit was never installed here - an install decision a standing bar cannot undo, and redding
# it punishes the wrong act on the wrong day. A missing FILE inside a present directory means the kit
# WAS taken and its route is broken, which is a defect in that tree and theirs to fix.
#
# NOT A WHOLE-LEG SKIP. None of the other numbered checks needs the route to exist, so skipping the
# leg would discard every one of their verdicts to announce this one - green-by-absence, one level up.
#
# WHAT THIS DOES NOT CHECK, said here because a structural check reads as a semantic one to everybody
# who did not write it: whether the route script WORKS, or whether the sentence around it is true
# about it. It grades that a path the section names IN BACKTICKS resolves in this tree, and a present
# but broken script passes. Check 16's body term - not this one - grades the section for stating a
# rule at all. Backticks rather than bare tokens, because a bare match would take a prose mention or
# a fenced example as a subject to grade.
#
# `${core:-}` AND `${M:-}` ARE DELIBERATE. Both are assigned inside the `only28` guard, so under
# `--only 28` they are unset and `set -u` would kill the script right here. That flag does not reach
# this block today for an unrelated reason - check 30 above reads `$MEMORY_ROOT` under the same guard
# and dies first, measured at e828f778 and filed as TOOL-aHoistedPass-37 - and these two spellings
# are what stop this check becoming the SECOND crash on that path the day the first one is fixed.
#
# TWO CARRIERS, and the second half is the closing review's F6. This check read the build-method
# render alone while the SKILL - the carrier an agent actually reads, and the one that mandates
# `scriptPath` calls - spelled the same two scripts as install-prefix LITERALS. At a root install
# those resolve to nothing, and this check passed over exactly that half: it certified the carrier
# that was already right. `_c31_hit` is ONE resolver called twice rather than two loops, so the two
# carriers cannot be graded on different terms.
_c31_hit() { # <carrier> <path>...
  local _c31_who="$1" _c31_p; shift
  for _c31_p in "$@"; do
    [ -f "$_c31_p" ] && continue
    if [ -d "$(dirname "$_c31_p")" ]; then
      fail 31 "a carrier of the harnessed-pass route names a script this tree does not carry while the directory that holds it IS present, so the route's kit was taken and its route is broken: $_c31_p named by $_c31_who"
    else
      report "check 31 skipped for $_c31_p — the directory that would hold it is absent, so the route's kit was never installed in this tree and a standing bar cannot undo an install decision"
    fi
  done
}
# The backticked tokens with a route script's shape. Both greps exit non-zero on no match and that
# is an ANSWER here rather than a failure - the empty branches below are what say so, and neither
# grep sits in an `&&` chain that could read it as one.
_c31_routes() { grep -oE '`[^`]+`' | tr -d '`' | grep -E '(^|/)workflows/[A-Za-z0-9_.-]+\.js$' | sort -u; }
_c31_sec=$(printf '%s\n' ${core:-} | awk -F: -v h=passes-harnessed '$1 == h { print $2; exit }')
_c31_bm="${M:-}/guides/BUILD-METHOD.md"
# THE SKILL'S PATH IS THE ADOPTER'S, spelled the one way `adopt-unattended.sh` writes it. It is not a
# kit path and carries no install prefix: `.claude/skills/` is the harness's own convention and is
# the same at every prefix, which is why it can be named here at all.
_c31_skill=".claude/skills/unattended/SKILL.md"
if [ ! -f "$_c31_skill" ]; then
  report "check 31 skipped for $_c31_skill — this tree carries no rendered Skill, so the carrier an agent actually reads states no route to resolve; the adopter renders it, and a tree without one has taken this kit only halfway"
else
  _c31_spaths=$(_c31_routes < "$_c31_skill")
  if [ -z "$_c31_spaths" ]; then
    report "check 31 skipped for $_c31_skill — the rendered Skill names no backticked route script, so this carrier states no route for a run to resolve and there is nothing to test"
  else
    _c31_hit "$_c31_skill" $_c31_spaths
  fi
fi
if [ -z "$_c31_sec" ]; then
  report "check 31 skipped for $DRIVER — the directive registry names no passes-harnessed handle this leg can read, so the section holding the route is unnamed and there is nothing to resolve"
elif [ ! -f "$_c31_bm" ]; then
  report "check 31 skipped for $_c31_bm — this tree carries no build-method carrier, so the section naming the route cannot be opened; check 16 arm B is silent on the same absence and this line is the announcement it does not make"
elif ! grep -qE "^## $_c31_sec( |\$)" "$_c31_bm"; then
  report "check 31 skipped for $_c31_bm — it carries no $_c31_sec heading, so the route cannot be read out of it; check 16 arm B owns that refusal and two legs answering one question is what this file's header exists to remove"
else
  # The section slice, then its route tokens through the same extractor the Skill arm uses.
  _c31_paths=$(awk -v s="^## $_c31_sec( |\$)" '
      $0 ~ s { inb = 1; next }
      inb && /^## / { exit }
      inb' "$_c31_bm" | _c31_routes)
  if [ -z "$_c31_paths" ]; then
    report "check 31 skipped for $_c31_bm — $_c31_sec names no backticked route script, so this tree states no route for a run to resolve and there is nothing to test; an adopter whose render predates the route sentence is in exactly this state"
  else
    # PER PATH, so a tree carrying one of two named scripts fails on the one it lacks and says
    # nothing about the one it has. The directory under test is `dirname` of the path the carrier
    # ITSELF names: TOOL_ROOT renders to the empty string at a root install, so an install-prefix
    # literal here would be wrong in an adopter tree in both directions.
    _c31_hit "$_c31_bm" $_c31_paths
  fi
fi

# ---- 32: EVERY READ OF THE `phase` FACT GOES THROUGH ONE OF THE TWO READERS (S8). Two readers, a
# ---- call-site classification, and a structural arm that grades it — because a classification
# ---- nothing enforces is a comment. The rules, stated once here and nowhere else:
# ----
# ----   * outside `read_derived_phase` and `read_recorded_phase`, a direct read of the fact REDS, whatever
# ----     function contains it — including a function that also WRITES the phase, which is where the
# ----     one live instance at BASE sat;
# ----   * the exemption is a LINE, never a function: a read that shares its line with the
# ----     `set_fact <file> phase` it guards is that writer's own guard;
# ----   * a `read_recorded_phase` call REDS unless the allow-list below names its function;
# ----   * an allow-list entry naming a function that no longer calls `read_recorded_phase` REDS too,
# ----     because a stale row silently widens the very set it was written to narrow.
# ----
# ---- DECLARED, so a fixture can move it. A list typed inside the awk program could not be broken by
# ---- a staged edit, and an arm whose failing case cannot be staged is an assertion about nothing.
PHASE_RECORDED_FNS="refuse_if_terminal archive_name_of verb_landed"
if [ ! -f "$DRIVER" ]; then
  fail 32 "the driver is not where this leg reads it, so the phase-read routing below would be graded over no lines at all and would pass by finding nothing: $DRIVER"
else
  _c32=$(PRF="$PHASE_RECORDED_FNS" awk '
    BEGIN { n = split(ENVIRON["PRF"], a, /[ \t]+/); for (i = 1; i <= n; i++) if (a[i] != "") allow[a[i]] = 1 }
    /^[a-z_][A-Za-z0-9_]*\(\)/ { fn = $0; sub(/\(\).*/, "", fn) }
    /^[ \t]*#/ { next }
    {
      ln = $0; sub(/\r$/, "", ln)
      isread = (ln ~ /(^|[^A-Za-z0-9_])fact[ \t]+[^ \t]+[ \t]+phase([^A-Za-z0-9_-]|$)/) \
            || (ln ~ /s\/\^phase: \/\/p/)
      iswrite = (ln ~ /set_fact[ \t]+[^ \t]+[ \t]+phase([^A-Za-z0-9_-]|$)/)
      if (isread && !iswrite && fn != "read_derived_phase" && fn != "read_recorded_phase")
        printf "\n  %s:%d reads the phase fact directly inside %s(), which is neither reader", FILENAME, NR, fn
      if (ln ~ /(^|[^A-Za-z0-9_])read_recorded_phase[ \t]+"/) {
        seen[fn] = 1
        if (!(fn in allow))
          printf "\n  %s:%d calls read_recorded_phase() inside %s(), which the allow-list does not name", FILENAME, NR, fn
      }
    }
    END { for (k in allow) if (!(k in seen)) printf "\n  the allow-list names %s(), which no longer calls read_recorded_phase()", k }
  ' "$DRIVER")
  [ -z "${_c32//[[:space:]]/}" ] \
    || fail 32 "the phase fact is read outside the two readers, or the recorded-phase allow-list disagrees with the source, so the effective phase and the recorded one can differ at a call site nobody classified:$_c32"
fi

# ---- 33: A PHASE ANOTHER VERB PRODUCES IS NOT REACHABLE THROUGH `--phase`. Vocabulary membership is
# ---- not permission: every literal phase a `set_fact … phase` site writes is a PRODUCER's, written
# ---- with the facts that make it mean something, and a phase move into it would be that record with
# ---- none of them. The terminals are covered by `verb_phase`'s own `is_terminal` branch, and
# ---- `--preflight`'s initial RUNNING is the one literal that is a starting position rather than a
# ---- produced claim, so both are excluded.
if [ -f "$DRIVER" ]; then
  _c33_body=$(awk '/^verb_phase\(\)/ { inb = 1 } inb { print } inb && /^}/ { exit }' "$DRIVER")
  _c33_lits=$(grep -oE 'set_fact[ \t]+[^ \t]+[ \t]+phase[ \t]+[A-Z]+' "$DRIVER" | awk '{ print $NF }' | sort -u)
  _c33=""
  for _c33_p in $_c33_lits; do
    [ "$_c33_p" = RUNNING ] && continue
    case " $PHASES_TERMINAL " in *" $_c33_p "*) continue ;; esac
    printf '%s\n' "$_c33_body" | grep -qF "\"\$want\" = $_c33_p" \
      || _c33="$_c33 $_c33_p"
  done
  [ -z "${_c33//[[:space:]]/}" ] \
    || fail 33 "a phase another verb PRODUCES is reachable through --phase, so one phase move would write that phase with none of the facts its producer writes beside it, and the verb that releases it would have nothing to read:$_c33"
fi

# ---- 15, THE DATING SELF-SCAN - TOOL-dDerivedDocket-22 section 7. A FIRST-COMMIT DATE read with
# ---- `--diff-filter=A` and no `--follow` anywhere in this kit's own shell. That spelling dates an
# ---- archived record to the rotation that added its name, which moves a grandfathered record into a
# ---- cutoff's graded set where no verb may repair it; check 15's anchor cutoff carried exactly that
# ---- line until this unit. The CLASS is gated, not the one instance.
# ----
# ---- THE PREDICATE, run over the tree with hits and near-misses printed before it was wired: a
# ---- non-comment line carrying `--diff-filter=A` AND a date placeholder (`%cs`, `%ad` and their
# ---- kin) AND no `--follow`. Near-misses it deliberately passes: a SHA read (`--format=%H`), which
# ---- the rotation-aware introducing-commit resolver answers and which must not follow, and a line
# ---- that already follows. WHAT IT DOES NOT CATCH: a date read split across two lines, a date read
# ---- by a language other than shell, or a first commit dated without `--diff-filter=A` at all.
_c15s=$(for _c15f in "$HERE"/*.sh; do
          [ -f "$_c15f" ] || continue
          awk '/^[ \t]*#/ { next }
               /--diff-filter=A/ && /%[ac][sdiIt]/ && !/--follow/ { printf "\n  %s:%d", FILENAME, FNR }' "$_c15f"
        done)
[ -z "${_c15s//[[:space:]]/}" ] \
  || fail 15 "a first-commit DATE is read with --diff-filter=A and no --follow in this kit's own shell, so a rotation re-dates an archived record to the commit that added its name and a cutoff grades a record it was written to grandfather:$_c15s"


exit "$status"
