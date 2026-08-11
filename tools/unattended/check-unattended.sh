#!/usr/bin/env bash
# check-unattended.sh — the merge-bar leg for the unattended-run kit. THIRTEEN checks over the tree.
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
KICKOFF_ENGINE=""; KICKOFF_EXITS=""
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
RUNS=$(printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/RUN\.md$" || true)
POP=$(printf '%s\n' "$RUNS" | grep -c . || true)
if [ "$POP" = 0 ] && [ "$PRE" -gt 0 ]; then
  fail 4 "a run-state file exists under the memory root but none at the path this leg selects, so the selector is mis-segmented and every check below is silent for the wrong reason: $PRE found"
fi

phase_of() { sed -n 's/^phase: *//p' "$1" | head -1 | tr -d '\r'; }
fact_of()  { sed -n "s/^$2: *//p" "$1" | head -1 | tr -d '\r'; }
# Exactly one open, one close, CLOSE AFTER OPEN. The order clause is not decoration: a transposed
# pair satisfies a count-only check, and the driver's copy of this function truncated a file on one.
region()   { awk -v o="$2" -v c="$3" '
               index($0,o)==1 { no++; if (no==1) oat=NR; if (nc==0) inside=1; next }
               index($0,c)==1 { nc++; if (nc==1) cat=NR; inside=0; next }
               inside { print }
               END { if (no!=1 || nc!=1 || cat<oat) exit 3 }' "$1"; }

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
  # ---- AN ABSENT `base:` LINE IS THE VIOLATION, not the exemption. Wrapping this in `if [ -n ]`
  # ---- meant deleting one line from a run-writable file disarmed the only BASE check on the bar.
  rb=$(fact_of "$f" base)
  # A TERMINAL run's branch point is gone by construction: after the run merges and the branch is
  # deleted, merge-base(origin/default, HEAD) is no longer the commit it forked from. Reproducing it
  # for a landed record turns the default-branch bar permanently red on the first successful landing
  # — the pin polices a LIVE run's provenance. Reachability still holds and is what is asserted.
  # AN ABSENT `base:` IS THE VIOLATION, UNCONDITIONALLY — before any phase is consulted. This
  # refusal sat inside the non-terminal arm for exactly one commit, and in that commit a record
  # carrying a run-written TERMINAL phase with its `base:` line deleted skipped this check AND
  # check 13 below, so the leg exited 0 over a mandate that authorised itself. The terminal
  # exemption is keyed on `phase:`, which the run writes; it may buy a weaker BASE assertion, and
  # it may never buy the absence of one.
  if [ -z "$rb" ]; then
    fail 9 "a run-state file records no BASE, and the record is written by the run — an absent pin is not a satisfied one: $f"
  fi
  ph=$(fact_of "$f" phase)
  TERMINAL_REC=0
  case " $PHASES_TERMINAL " in *" $ph "*) TERMINAL_REC=1 ;; esac
  if [ -z "$rb" ]; then
    : # already refused above; fall through so check 13 still runs on whatever else is recorded
  elif [ "$TERMINAL_REC" = 1 ]; then
    # SKIPS THE MERGE-BASE REPRODUCTION ONLY. After a run lands its branch point is gone, so
    # reproducing it would red main forever. What is asserted instead is reachability — a WEAKER
    # claim, and honestly so: every commit the run authored satisfies it. The strength here comes
    # from check 13, which still reads the mandate at this same BASE and is no longer gated on
    # anything the run can delete.
    if ! git merge-base --is-ancestor "$rb" HEAD >/dev/null 2>&1; then
      fail 9 "a terminal run-state file records a BASE that is not an ancestor of HEAD, so the run it describes did not land on this history: $f"
    fi
  else
    # THE LEG DOES NOT READ GOV_DEFAULT_BRANCH. The driver may be steered by an operator; the gate
    # may not, because a leg recomputing the identical wrong value CONFIRMS the steer instead of
    # contradicting it — which is precisely how three reproduced authorization defects stayed green.
    # Derived from refs/remotes/origin/HEAD and nothing else (D3 fix 3).
    d=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null) || d=""
    d=${d#origin/}
    if [ -z "$d" ]; then
      # AND ITS ABSENCE IS THE VIOLATION. This body used to sit under `if [ -n "$d" ]` with no else,
      # so `git symbolic-ref -d refs/remotes/origin/HEAD` — exit 0, no push, no network — disarmed
      # every BASE check on the bar at once. Same shape the `base:` arm above already refuses.
      fail 9 "this leg cannot derive a default branch: refs/remotes/origin/HEAD does not resolve, so the recorded BASE cannot be checked against anything outside the run's reach — repair it with 'git remote set-head origin -a'"
    else
      lref="refs/remotes/origin/$d"
      rr=$(fact_of "$f" base-ref)
      if [ -z "$rr" ]; then
        fail 9 "a run-state file records no base-ref, so the ref its BASE was derived from cannot be re-resolved — an absent pin is not a satisfied one: $f"
      elif [ "$rr" != "$lref" ]; then
        fail 9 "a run-state file's base-ref is not the ref this leg derives from refs/remotes/origin/HEAD, which means the driver was pointed somewhere this gate is not: recorded $rr, derived $lref in $f"
      elif ! git rev-parse --verify --quiet "$rr" >/dev/null 2>&1; then
        fail 9 "a run-state file's base-ref does not resolve, so nothing can be re-derived from it: $rr in $f"
      else
        mb=$(git merge-base "$lref" HEAD 2>/dev/null) || mb=""
        if [ -z "$mb" ]; then
          fail 9 "no merge-base between $lref and HEAD, so the recorded BASE reproduces nothing: $f"
        else
          [ "$mb" = "$rb" ] || fail 9 "a recorded BASE is not the merge-base this history reproduces, and every mandate assertion hangs on that value: recorded $rb, computed $mb in $f"
          [ "$mb" != "$(git rev-parse HEAD)" ] || fail 9 "the merge-base equals HEAD, so the run authored every byte a mandate comparison would read: $f"
        fi
      fi
    fi
  fi

  # ---- 13: THE MANDATE, asserted by the BAR and not only by the driver. The leg did not contain the
  # ---- string `run:mandate` at all: it checked the driver's bookkeeping and never the thing the
  # ---- bookkeeping is about, so all three of the authorization defects reproduced against it were
  # ---- invisible here and the whole bar stayed green.
  # ----
  # ---- This is deliberately a SECOND OPINION and not a second implementation: it re-extracts both
  # ---- blocks itself, from the base commit and from the working copy, and refuses on anything that
  # ---- is not exactly one well-formed block on each side.
  if [ -n "$rb" ] && git rev-parse --verify --quiet "$rb^{commit}" >/dev/null 2>&1; then
    if bb=$(git show "$rb:$f" 2>/dev/null); then
      ma=$(printf '%s\n' "$bb" | region - '<!-- run:mandate -->' '<!-- /run:mandate -->' 2>/dev/null) && ra=0 || ra=$?
      mb2=$(region "$f" '<!-- run:mandate -->' '<!-- /run:mandate -->' 2>/dev/null) && rb2=0 || rb2=$?
      if [ "$ra" != 0 ] || [ "$rb2" != 0 ]; then
        fail 13 "a run-state file does not carry exactly one well-formed mandate block on both sides of the BASE comparison; a second block is a second authorization nobody granted: $f"
      elif [ -z "$(printf '%s' "$ma" | tr -d '[:space:]')" ]; then
        fail 13 "the mandate block is absent or empty at the recorded BASE, so nothing committed before the run authorizes it: $f"
      elif [ "$ma" != "$mb2" ]; then
        fail 13 "a run-state file's mandate differs from the one at its recorded BASE — the run edited its own authorization: $f"
      fi
    else
      fail 13 "a run-state file does not exist at its own recorded BASE, so its mandate cannot have been committed before the run: $rb in $f"
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

exit "$status"
