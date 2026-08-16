#!/usr/bin/env bash
# check-unattended.sh — the merge-bar leg for the unattended-run kit. FIFTEEN checks over the tree.
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
KIT_UNATTENDED_VERSION=1.4   # gov:kit unattended@1.4 — must match unattended.sh; check-kit-versions.sh pairs them

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

  # ---- 8: the generated region is a COPY. If it drifts from its source the file is answering a
  # ---- question the README already answers, differently — the whole class this build removes.
  rd=${f%/RUN.md}/README.md
  if [ -f "$rd" ]; then
    a=$(region "$f" '<!-- run:generated -->' '<!-- /run:generated -->' 2>/dev/null) || \
      fail 8 "a run-state file's generated markers are malformed, so the copy cannot be compared with its source: $f"
    b=$(region "$rd" '<!-- gen:build-index -->' '<!-- /gen:build-index -->' 2>/dev/null) || \
      fail 8 "a build README's generated markers are malformed, so the copy has no source to be compared with: $rd"
    # THE EQUALITY REFUSAL IS SCOPED TO A NON-TERMINAL RUN. Both malformed-marker refusals above
    # still fire on every phase: a terminal run's file must still be READABLE, and skipping those
    # would let a file rot into unparseability once it landed.
    #
    # Why the equality cannot bind a terminal run: the copy is refreshed by `--preflight` and by
    # nothing else, and `verb_preflight` calls `refuse_if_terminal` before it reaches that splice.
    # So a LANDED run has no supported route back to equality — the driver refuses to re-copy, and
    # the check's own message ("re-run the driver") names a remedy that does not exist for it. The
    # only ways to satisfy it were to hand-edit a file this same message calls generated, or to
    # freeze the README the copy was taken from, which would have made the corpus permanently
    # unrenderable.
    #
    # What the copy MEANS also differs by phase. For a live run it is a mirror, and drift means the
    # run is working from a stale roster — a real defect. For a landed one it is a historical record
    # of what the README said when the run finished, and the README moving afterwards is ordinary.
    # Judging a record against a source that legitimately moved is not a check, it is a countdown.
    #
    # Section 9 of the protocol governs what a check running under the run's own uid can buy; this
    # carve-out narrows a check that could not be satisfied rather than one that was inconvenient.
    case " $PHASES_TERMINAL " in
      *" $ph "*) ;;
      *) [ "$a" = "$b" ] || fail 8 "a run-state file's generated region differs from the build README slice it is a COPY of; re-run the driver rather than hand-editing it: $f" ;;
    esac
  fi

  # ---- 9: the recorded BASE must be the merge-base git reproduces. A pin the run can quietly move
  # ---- is not a pin, and every mandate assertion hangs on this value.
  # ---- AN ABSENT `base:` LINE IS THE VIOLATION, not the exemption. Wrapping this in `if [ -n ]`
  # ---- meant deleting one line from a run-writable file disarmed the only BASE check on the bar.
  rb=$(fact_of "$f" base)
  if [ -z "$rb" ]; then
    fail 9 "a run-state file records no BASE, and the record is written by the run — an absent pin is not a satisfied one: $f"
  else
    d=${GOV_DEFAULT_BRANCH:-}
    [ -n "$d" ] || { d=$(git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null) || d=""; d=${d#origin/}; }
    if [ -n "$d" ]; then
      # REMOTE-TRACKING ONLY, matching the driver: a bare local branch is a ref the run can move
      # with `git branch -f`, which is how BASE was made to equal HEAD.
      for b in "refs/remotes/origin/$d" "refs/remotes/$d"; do
        GIT rev-parse --verify --quiet "$b" >/dev/null 2>&1 || continue
        # ANCESTRY, NOT EQUALITY — and the reason is the kit's own first success. Equality wedged the
        # bar permanently: merging then pushing, the two acts an authorization grants, move the
        # merge-base past the pin forever, so a LANDED record red every later default-branch push.
        # Reproduced on an honest fixture with no attacker. A phase-keyed carve-out is not the fix
        # either — the run writes `phase:`, so it would be a one-line escape from this check.
        # What actually matters, and what survives landing: the recorded BASE lies on the history the
        # ANCHOR names rather than on the branch the run authored.
        if ! GIT rev-parse --verify --quiet "$rb^{commit}" >/dev/null 2>&1; then
          fail 9 "a recorded BASE does not resolve to a commit in this history, and the record is written by the run: $rb in $f"
        elif ! GIT merge-base --is-ancestor "$rb" "$b" 2>/dev/null; then
          fail 9 "a recorded BASE is not an ancestor of the anchor, so it names a commit off the history the anchor blesses — which is where a run's own commits live: recorded $rb against $b in $f"
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
            if [ "$ph" = LANDED ] && GIT rev-parse --verify --quiet "$w^{commit}" >/dev/null 2>&1                && ! GIT merge-base --is-ancestor "$w" "$b" 2>/dev/null; then
              fail 15 "a record claims LANDED with a witness that is not an ancestor of the anchor, so the work it says reached the remote is not on the branch the remote calls its default: $w against $b in $f"
            fi ;;
        esac
        break
      done
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
    else
      fail 13 "no build README at a run's recorded BASE, so nothing committed before that run branched authorizes it: $rb in $bre"
    fi
  fi

  # ---- 11: the landing rule, checked where the record is. A run that wrote the bypass flag into its
  # ---- own state file is a run that considered using it.
  if [ -n "$BYPASS_BAN" ] && grep -qF -- "$BYPASS_BAN" "$f"; then
    fail 11 "a run-state file names the declared bypass flag, and bypassing the lander discards the whole bar the mandate leaned on: $BYPASS_BAN in $f"
  fi
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
