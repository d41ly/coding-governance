#!/usr/bin/env bash
# check-unattended.sh - the merge-bar leg for the unattended-run kit. TWENTY-THREE checks over the tree.
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
KIT_UNATTENDED_VERSION=1.7   # gov:kit unattended@1.7 — must match unattended.sh; check-kit-versions.sh pairs them

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
GIT() { git -c core.useReplaceRefs=false -c advice.graftFileDeprecated=false "$@"; }

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "unattended-check: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
HERE="$(cd "$(dirname "$0")" && pwd)"
DRIVER="$HERE/unattended.sh"
CONF="$ROOT/.unattended.conf"

status=0
fail() { echo "UNATTENDED check $1 FAILED — $2"; status=1; }

# ---------------------------------------------------------------------------------- 1: the conf
if [ ! -f "$CONF" ]; then
  fail 1 "no .unattended.conf at the repo root, and every value this leg checks is declared there"
  exit "$status"
fi
MEMORY_ROOT=memory; LANDER=""; BYPASS_BAN=""; GATE_CMD=""; WIRING_CHECK=""
KEEPALIVE_CREATE=""; KEEPALIVE_DELETE=""; PHASES_EXTRA=""; DOD_EXTRA=""; CORE_FLOOR=""
KICKOFF_ENGINE=""; KICKOFF_EXITS=""; DIRECTIVES_EXTRA=""; DIRECTIVES_FLOOR=""; DIRECTIVES_EXTRA_TABLE=""
# shellcheck disable=SC1090
. "$CONF"
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
if [ -z "$PHASES_CORE" ] || [ -z "$DOD_CORE" ]; then
  fail 1 "cannot read the kit's core sets from the driver, so every membership check below would pass over an empty set: $DRIVER"
  exit "$status"
fi
PHASES="$PHASES_CORE $PHASES_EXTRA"
DOD="$DOD_CORE $DOD_EXTRA"

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
# >>> kickoff_region
region()   { awk -v o="$2" -v c="$3" '
               { ln=$0; sub(/\r$/,"",ln) }
               index(ln,o)==1 { if (ln!=o) bad=1; no++; if (no==1) oat=NR; if (nc==0) inside=1; next }
               index(ln,c)==1 { if (ln!=c) bad=1; nc++; if (nc==1) cat=NR; inside=0; next }
               inside { print }
               END { if (bad || no!=1 || nc!=1 || cat<oat) exit 3 }' "$1"; }
# <<< kickoff_region

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
# ---- hook with no tty, and a credential prompt would hang the push rather than refuse it.
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
  adv_remote=""   # left empty on purpose: the fail-closed branch in check 9 reports it
fi
# GUARDED on the population too: with no run-state file there is nothing whose BASE could be
# checked, and two network round-trips per bar run bought exactly nothing. POP is computed above.
if [ -n "$adv_remote" ] && [ "$POP" != 0 ]; then
  adv_raw=$(GIT_TERMINAL_PROMPT=0 GIT ls-remote --symref --exit-code "$adv_remote" HEAD 2>/dev/null) \
    && ADV_HEAD=$(printf '%s\n' "$adv_raw" | awk -F'\t' '{ sub(/\r$/,"",$2) } $2=="HEAD" && $1 ~ /^[0-9a-f]+$/ { print $1; exit }')
  ADV_TIPS=$(GIT_TERMINAL_PROMPT=0 GIT ls-remote --heads "$adv_remote" 2>/dev/null \
    | awk -F'\t' '$1 ~ /^[0-9a-f]+$/ { print $1 }')
fi

# PUBLISHED = an ancestor of a tip the remote advertises. Ancestry and NOT equality, and the
# distinction is the whole of S6: under the second anchor the BASE is pinned to the advertised branch
# tip, the run then commits and pushes that same branch again — which is exactly what the Skill tells
# it to do — and the advertised tip moves PAST the pin. Equality reds from that moment on, forever,
# and worse after a branch delete or a squash-merge landing. This file already records being moved
# off equality once for that reason; writing it back in a second place would re-earn the same wedge.
is_published() { # commit -> 0 if it is an ancestor of any advertised tip
  local c="$1" t
  [ -n "$ADV_HEAD" ] && GIT merge-base --is-ancestor "$c" "$ADV_HEAD" 2>/dev/null && return 0
  for t in $ADV_TIPS; do
    GIT merge-base --is-ancestor "$c" "$t" 2>/dev/null && return 0
  done
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
  rd=${f%/RUN.md}/README.md
  case " $PHASES_TERMINAL " in *" $ph "*) rd="" ;; esac
  if [ -n "$rd" ] && [ -f "$rd" ]; then
    a=$(region "$f" '<!-- run:generated -->' '<!-- /run:generated -->' 2>/dev/null) || \
      fail 8 "a run-state file's generated markers are malformed: $f"
    [ -z "$(printf '%s' "$a" | tr -d '[:space:]')" ] || \
      fail 8 "a run-state file's generated region carries a COPY of the unit list; that list is DERIVED from the build README on every read, so a copy here is a second answer waiting to go stale. Empty the region between its markers: $f"
  fi

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
      fail 9 "the remote advertised no tips, so the recorded BASE cannot be shown to be published and this leg will not pass a run it could not check; the bar's authoritative run is the pre-push hook, which has the network by construction: $f"
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
        elif ! is_published "$rb"; then
          fail 9 "a recorded BASE is not published on the remote — it is an ancestor of no tip the remote advertises, so it names a commit that exists only where this run could have authored it: recorded $rb in $f"
        elif ! GIT merge-base --is-ancestor "$rb" HEAD 2>/dev/null; then
          fail 9 "a recorded BASE is not an ancestor of HEAD, so the run-state file pins a commit this working history does not build on: $rb in $f"
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
            if [ "$ph" = LANDED ] && [ -n "$b" ] && GIT rev-parse --verify --quiet "$w^{commit}" >/dev/null 2>&1                && ! GIT merge-base --is-ancestor "$w" "$b" 2>/dev/null; then
              fail 15 "a record claims LANDED with a witness that is not an ancestor of the anchor, so the work it says reached the remote is not on the branch the remote calls its default: $w against $b in $f"
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
        [ "$recmode" = "$dmode" ] || fail 19 "a run-state file records an authorization mode the build README at its own recorded BASE does not declare, so the discipline the run says bound it is not the one its authorization asked for: $recmode against $dmode"
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
  # ---- Only the waiver kind is joined. `park()` writes four, and the other three legitimately
  # ---- arrive late — an `override` is written at `--close`, an `abort` reason later still — so
  # ---- joining them to the first blob would red every honest run. The waiver's whole claim is that
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
    tblscope=$(tr -d '\r' < "$tmpl" | awk -F'|' '
      /^[[:space:]]*\|[[:space:]]*`[a-z][a-z-]*`[[:space:]]*\|/ {
        h = ""; sc = ""
        for (i = 2; i <= NF; i++) {
          cell = $i
          gsub(/^[[:space:]]+|[[:space:]]+$/, "", cell)
          if (h == "" && cell ~ /^`[a-z][a-z-]*`$/) { gsub(/`/, "", cell); h = cell; continue }
          if (cell == "all" || cell == "prompt") sc = cell
        }
        if (h != "" && sc != "") print h ":" sc
      }' | sort -u)
    if [ -z "$tblscope" ]; then
      fail 16 "the Skill's directive table carries no scope cell this leg can read, so the scope join would compare the registry against nothing and pass by finding nothing; the cell it looks for holds exactly all or prompt"
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
      ndod=$(printf '%s
' "$dcore" | grep -c . || true)
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
  rsbase=""
  for rsc in $(GIT log --reverse --format=%H -- "$f" 2>/dev/null); do
    case "$(GIT show "$rsc:$f" 2>/dev/null | grep -m1 '^phase:')" in
      *BUILDING*|*RUNNING*|*VERIFYING*|*LANDING*|*LANDED*) rsbase="$rsc"; break ;;
    esac
  done
  [ -n "$rsbase" ] || rsbase="$rb"
  rsb=$(GIT show "$rsbase:$bre" 2>/dev/null || true)
  rs_cut=${UNITS_REGION_CUTOFF:-}
  rs_date=$(GIT show -s --format=%cs "$rsbase" 2>/dev/null || true)
  if [ -z "$rsb" ]; then
    report "check 22 skipped for $f — no build README at the baseline commit, so there is no authorized roster to compare against"
  elif ! printf '%s\n' "$rsb" | grep -qxF -- '<!-- gen:build-units -->'; then
    report "check 22 skipped for $f — the baseline build README carries no units region, so the comparison would be vacuous over an empty set"
  elif [ -n "$rs_cut" ] && [ -n "$rs_date" ] && ! printf '%s\n%s\n' "$rs_cut" "$rs_date" | sort -C; then
    report "check 22 skipped for $f — the baseline predates UNITS_REGION_CUTOFF, so its absent region is grandfathered rather than a defect"
  elif ! rs_was=$(printf '%s\n' "$rsb" | region - '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null); then
    report "check 22 skipped for $f — the baseline build README carries a units marker but not exactly one well-formed pair, so there is no single roster to compare"
  elif ! rs_now=$(region "$bre" '<!-- gen:build-units -->' '<!-- /gen:build-units -->' 2>/dev/null); then
    report "check 22 skipped for $f — the working build README does not carry exactly one well-formed units pair, so the executing roster cannot be read"
  elif ! printf '%s
  ' "$rs_was" | grep -qE '[A-Z]+-[A-Za-z0-9]+-[0-9]+'; then
    # AN EMPTY BASELINE ROSTER IS NOT A COMPARISON, and it is not vacuously TRUE either — it is
    # vacuously ACCUSATORY: every unit the build has would read as added. MEASURED by this unit's
    # own fixture, whose run carries a live phase from its first commit, so the baseline predates
    # every spec. That is exactly the prompt-authorized shape, where a run legitimately authors
    # its whole roster after preflight. Skipping is the honest answer and it says so out loud.
    report "check 22 skipped for $f — the baseline roster names no unit, so every unit this build has would read as added and the comparison would accuse rather than check"
  else
    rs_rows=$(grep -F -- ' rescope · item ' "$f" 2>/dev/null || true)
    # ADDED ids: accounted for by an `add` naming it, OR a `supersede` naming it as the successor.
    # An `add` alone would red a correctly performed supersession, whose successor is present now
    # and absent then with no `add` row that the sibling verb would even accept.
    for rsid in $(printf '%s\n' "$rs_now" | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u); do
      printf '%s\n' "$rs_was" | grep -qF -- "$rsid" && continue
      printf '%s\n' "$rs_rows" | grep -qE "item add $rsid( |\$)" && continue
      printf '%s\n' "$rs_rows" | grep -qE "item supersede [A-Za-z0-9-]+ -> $rsid( |\$)" && continue
      fail 22 "a unit is in the roster this run is executing and was not in the roster it entered BUILDING with, and no rescope row adds or supersedes into it, so the scope moved with nothing on the record saying so: $rsid in $f"
    done
    # RETIRED units: a status that is WONTDO now and was not then owes a retire or a supersede.
    for rsid in $(printf '%s\n' "$rs_now" | grep -E '\| WONTDO \|' | grep -oE '[A-Z]+-[A-Za-z0-9]+-[0-9]+' | sort -u); do
      printf '%s\n' "$rs_was" | grep -F -- "$rsid" | grep -q '| WONTDO |' && continue
      printf '%s\n' "$rs_rows" | grep -qE "item (retire|supersede) $rsid( |\$)" && continue
      fail 22 "a unit went WONTDO after this run entered BUILDING and no rescope row retires or supersedes it, so a unit was dropped with nothing on the record saying so: $rsid in $f"
    done
    # A SUPERSESSION THAT NEVER LANDED ITS REPLACEMENT is a retirement wearing a better name.
    printf '%s\n' "$rs_rows" | grep -oE 'item supersede [A-Za-z0-9-]+ -> [A-Za-z0-9-]+' | awk '{print $NF}' | sort -u \
    | while IFS= read -r rssucc; do
        [ -n "$rssucc" ] || continue
        printf '%s\n' "$rs_now" | grep -qF -- "$rssucc" && continue
        fail 22 "a rescope row supersedes into a successor the executing roster does not carry, so the replacement never landed and the row records a retirement wearing a better name: $rssucc in $f"
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
  dsrows=$(grep -F -- ' dispatch · item ' "$f" 2>/dev/null || true)
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
    dshit=""
    for dsc in $(GIT log --reverse --format=%H "$dsgrp"..HEAD 2>/dev/null); do
      case "$(GIT log -1 --format=%s "$dsc" 2>/dev/null)" in *"$dsunit"*) ;; *) continue ;; esac
      case "$(GIT diff-tree --no-commit-id --name-only -r "$dsc" 2>/dev/null | grep -v -x -F "$f")" in
        "") continue ;;
      esac
      dshit="$dsc"; break
    done
    if [ -z "$dshit" ]; then
      # NO COMMIT NAMES THE PASS. Legal when the pass produced no change - M6 says a pass that
      # changed nothing commits nothing. NOT legal when the declared paths moved anyway: that is the
      # declared work happening while the join is dodged, and it is the only reading of this state
      # that is a defect. Keyed on the PATHS and not on a subject naming no id at all, because the
      # latter reds on every witness commit a run makes between passes.
      dsmoved=""
      for dsp in $dsdecl; do
        GIT log --format=%H "$dsgrp"..HEAD -- "$dsp" 2>/dev/null | grep -q . && dsmoved="$dsmoved $dsp"
      done
      # ...and the run-state file is excluded from the OUTSIDE test too, for the same reason.
      if [ -n "$dsmoved" ]; then
        fail 23 "a declared path of a dispatched pass moved after the group anchor while no commit names that pass, so the declared work happened and the only join this check has was dodged: $dsunit wrote$dsmoved in $f"
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
      case "$(GIT log -1 --format=%s "$dshit" 2>/dev/null)" in *"$dssunit"*) dsother="$dssunit" ;; esac
    done <<DSSIBS
$(grep -F -- " dispatch · item $dsgrp " "$f" 2>/dev/null)
DSSIBS
    if [ -n "$dsother" ]; then
      fail 23 "one commit names two passes of the same dispatch group, so a subset test over it cannot say which pass wrote what and the attribution this check rests on is not available: $dsunit and $dsother in $f"
      continue
    fi
    # THE SUBSET TEST. Declaring MORE than you use is conservative and fine; writing outside the
    # declaration is the defect.
    dsout=""
    for dsq in $(GIT diff-tree --no-commit-id --name-only -r "$dshit" 2>/dev/null | grep -v -x -F "$f"); do
      dsok=0
      for dsp in $dsdecl; do
        case "$dsq" in "$dsp"|"$dsp"/*) dsok=1; break ;; esac
      done
      [ "$dsok" = 1 ] || dsout="$dsout $dsq"
    done
    [ -z "$dsout" ] || fail 23 "a dispatched pass committed a path outside the set it declared before dispatch, which is the disjointness proof failing at the only moment it could be checked: $dsunit at $dshit wrote$dsout in $f"
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

exit "$status"
