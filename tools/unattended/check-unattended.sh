#!/usr/bin/env bash
# check-unattended.sh — the merge-bar leg for the unattended-run kit. Eleven checks over the tree.
# Contract: memory/guides/UNATTENDED-PROTOCOL.md (binding). Project layer: .unattended.conf.
#
#   bash tools/unattended/check-unattended.sh
#
# Exit 0 + no output = clean. Anything printed is a violation. Exit 2 = misconfigured.
#
# READ-ONLY, which is what lets it run on the bar. It writes nothing, renders nothing and derives
# nothing: the run-state file's generated region is COMPARED against the build README's slice, whose
# freshness the memory-tree gate's check 9 already owns. Two legs answering one question is the class
# the file under test exists to remove.
#
# THE CORE SETS ARE READ FROM THE DRIVER, never restated here. A second spelling of `PHASES_CORE` one
# file away from the thing that enforces it is the drift this leg exists to catch.
set -u
KIT_UNATTENDED_VERSION=1.0   # gov:kit unattended@1.0 — must match unattended.sh; check-kit-versions.sh pairs them

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
# shellcheck disable=SC1090
. "$CONF"
M="$MEMORY_ROOT"
for k in LANDER BYPASS_BAN GATE_CMD WIRING_CHECK KEEPALIVE_CREATE KEEPALIVE_DELETE; do
  eval "v=\${$k}"
  [ -n "$v" ] || fail 1 "a required key is undeclared in .unattended.conf, and an undeclared value is not a defaulted one: $k"
done

# The kit's CORE sets, read from the driver — the single source. Parsed rather than sourced, because
# sourcing a script whose tail runs a verb would run the verb.
core_of() { sed -n "s/^$1=\"\\(.*\\)\"[[:space:]]*$/\\1/p" "$DRIVER" | head -1; }
PHASES_CORE=$(core_of PHASES_CORE)
DOD_CORE=$(core_of DOD_CORE)
PHASES_TERMINAL=$(core_of PHASES_TERMINAL)
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
pfloor=""; dfloor=""
case "$CORE_FLOOR" in *:*) pfloor=${CORE_FLOOR%%:*}; dfloor=${CORE_FLOOR##*:} ;; esac
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
RUNS=$(printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/RUN\.md$" || true)
POP=$(printf '%s\n' "$RUNS" | grep -c . || true)
if [ "$POP" = 0 ] && [ "$PRE" -gt 0 ]; then
  fail 4 "a run-state file exists under the memory root but none at the path this leg selects, so the selector is mis-segmented and every check below is silent for the wrong reason: $PRE found"
fi

phase_of() { sed -n 's/^phase: *//p' "$1" | head -1 | tr -d '\r'; }
fact_of()  { sed -n "s/^$2: *//p" "$1" | head -1 | tr -d '\r'; }
region()   { awk -v o="$2" -v c="$3" '
               index($0,o)==1 { no++; if (nc==0) inside=1; next }
               index($0,c)==1 { nc++; inside=0; next }
               inside { print }
               END { if (no!=1 || nc!=1) exit 3 }' "$1"; }

live=""; nlive=0
for f in $RUNS; do
  [ -f "$f" ] || continue
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
        git rev-parse --verify --quiet "$w^{commit}" >/dev/null 2>&1 \
          || fail 6 "a witness looks like a sha and resolves to no commit in this history: $w in $f" ;;
      *) ;;   # not sha-shaped: unjudgeable, and skipping it is the discipline, not an omission
    esac
  fi

  # ---- 8: the generated region is a COPY. If it drifts from its source the file is answering a
  # ---- question the README already answers, differently — the whole class this build removes.
  rd=${f%/RUN.md}/README.md
  if [ -f "$rd" ]; then
    a=$(region "$f" '<!-- run:generated -->' '<!-- /run:generated -->' 2>/dev/null) || \
      fail 8 "a run-state file's generated markers are malformed, so the copy cannot be compared with its source: $f"
    b=$(region "$rd" '<!-- gen:build-index -->' '<!-- /gen:build-index -->' 2>/dev/null) || \
      fail 8 "a build README's generated markers are malformed, so the copy has no source to be compared with: $rd"
    [ "$a" = "$b" ] || fail 8 "a run-state file's generated region differs from the build README slice it is a COPY of; re-run the driver rather than hand-editing it: $f"
  fi

  # ---- 9: the recorded BASE must be the merge-base git reproduces. A pin the run can quietly move
  # ---- is not a pin, and every mandate assertion hangs on this value.
  rb=$(fact_of "$f" base)
  if [ -n "$rb" ]; then
    d=${GOV_DEFAULT_BRANCH:-}
    [ -n "$d" ] || { d=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null) || d=""; d=${d#origin/}; }
    if [ -n "$d" ]; then
      for b in "origin/$d" "$d"; do
        git rev-parse --verify --quiet "$b" >/dev/null 2>&1 || continue
        mb=$(git merge-base "$b" HEAD 2>/dev/null) || continue
        [ "$mb" = "$rb" ] || fail 9 "a recorded BASE is not the merge-base this history reproduces, and every mandate assertion hangs on that value: recorded $rb, computed $mb in $f"
        break
      done
    fi
  fi

  # ---- 11: the landing rule, checked where the record is. A run that wrote the bypass flag into its
  # ---- own state file is a run that considered using it.
  if [ -n "$BYPASS_BAN" ] && grep -qF -- "$BYPASS_BAN" "$f"; then
    fail 11 "a run-state file names the declared bypass flag, and bypassing the lander discards the whole bar the mandate leaned on: $BYPASS_BAN in $f"
  fi
done

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

exit "$status"
