#!/usr/bin/env bash
# check-pass-order.sh - the merge-bar leg that refuses a unit BUILT BEFORE IT WAS SPECCED.
# TOOL-dBriefedPass-3. Contract: memory/guides/UNATTENDED-PROTOCOL.md. Project layer: .unattended.conf.
#
#   bash tools/unattended/check-pass-order.sh
#
# Exit 0 = clean. Exit 1 = a violation. Exit 2 = misconfigured.
#
# WHAT THIS CHECKS, in one sentence: for every unit a build README carries as CLOSED, the commit that
# BUILT that unit had a conforming, non-THIN spec for it at its first parent.
#
# WHY IT IS A HISTORY CHECK AND NOT A STATE CHECK. `--dispatch` refuses a build pass on a MISSING or
# THIN unit at the moment of the act, and that refusal is bypassable by simply not calling the verb.
# `--close`'s `build-complete` term grades the spec at CLOSE time, by which point a run that built
# first and specced afterwards has a spec that is neither missing nor thin. Only the commit graph
# remembers the ORDER, so only a history check can tell the two apart.
#
# WHAT THIS DOES NOT CHECK, stated in the header because a structural check reads as a semantic one to
# everybody who did not write it:
#   - whether the spec was GOOD, whether it was reviewed, or whether the code followed it.
#     `specs-audited` measures that a pre-code audit left evidence; this measures ORDER and nothing else.
#   - whether a build pass was DISPATCHED. That is a different join over the same range.
#   - anything about a unit that is not CLOSED. An OPEN unit legitimately has no build commit yet, so
#     grading one would red mid-build on every run including the one that must land it.
#   - anything about a build with no run-state file. The range this walks is a RUN's pinned BASE, and a
#     build that was never carried by an unattended run has no such pin. Those are COUNTED and
#     announced, never silently skipped.
set -u
KIT_UNATTENDED_VERSION=1.14   # gov:kit unattended@1.14 — must match unattended.sh; check-kit-versions.sh pairs them

# The dereference pin, identical to this kit's other two readers and for the identical reason: a graft
# file rewrites the commit GRAPH, so every ancestry answer below could be honest about a sha and wrong
# about what that sha means.
export GIT_GRAFT_FILE=/dev/null
# EVERY SHA DEREFERENCE BELOW GOES THROUGH `GIT`, the library's pinned wrapper, never bare `git`.
# A `git replace` ref rewrites what a sha MEANS for every read, so this leg could resolve an honest
# commit and grade forged bytes — and it grades whether a spec existed at a PARENT, which is exactly
# the kind of answer a substituted object would flip. The kit's own check 28 enforces it; the first
# cut of this file used bare `git` at nine sites and the gate named all nine.

_LIB_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
[ -f "$_LIB_DIR/lib-unattended.sh" ] || {
  echo "pass-order: the kit library is missing beside this script, so the predicates it shares with the driver are unavailable and no answer here would be trustworthy: $_LIB_DIR/lib-unattended.sh" >&2
  exit 2
}
# shellcheck source=lib-unattended.sh
. "$_LIB_DIR/lib-unattended.sh"

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "pass-order: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
HERE="$(cd "$(dirname "$0")" && pwd)"
DRIVER="$HERE/unattended.sh"
CONF="$ROOT/.unattended.conf"

[ -f "$CONF" ] || { echo "pass-order: no .unattended.conf at the repo root, and every value this leg needs is a declaration"; exit 2; }
[ -f "$DRIVER" ] || { echo "pass-order: no driver beside this script, and the classifier below is sliced out of it"; exit 2; }

MEMORY_ROOT=""; PASS_ORDER_CUTOFF=""
# shellcheck disable=SC1090
. "$CONF"
MEMORY_ROOT="${MEMORY_ROOT:-memory}"

# ------------------------------------------------------------------------------- THE CLASSIFIER
# SLICED OUT OF THE DRIVER'S SHIPPED BYTES, never re-implemented. `plan_state` is the M2 classifier
# and a second copy here would be two answers to one question about what THIN means - which is the
# exact class this kit's own marker-contract harness exists to forbid across its two readers.
# The end line is DERIVED from the closing brace, never counted: a magic span over a live function
# silently truncates as the function grows, and a truncated body still defines the function, so the
# liveness probe below would pass while every verdict came back empty.
_ps_start=$(grep -n '^plan_state()' "$DRIVER" | cut -d: -f1)
_ps_end=$(awk -v s="${_ps_start:-0}" 'NR>s && /^}/ {print NR; exit}' "$DRIVER")
if [ -z "$_ps_start" ] || [ -z "$_ps_end" ] || [ "$_ps_end" -le "$_ps_start" ]; then
  echo "pass-order: cannot slice plan_state out of the driver, so every unit below would be graded by nothing: $DRIVER"; exit 2
fi
eval "$(sed -n "${_ps_start},${_ps_end}p" "$DRIVER")"
declare -F plan_state >/dev/null || { echo "pass-order: plan_state did not survive the slice, so this leg would grade nothing and report clean"; exit 2; }

# ------------------------------------------------------------------------------- THE LIVENESS PROBE
# A PROBE THAT CANNOT MOVE SAYS SO. The classifier must return a real token on a real spec before a
# single verdict is trusted; without this the whole leg reports a clean bill when the slice breaks,
# which is indistinguishable from a clean run and is how a green bar stops meaning anything.
_probe=$(git ls-files "$MEMORY_ROOT/builds/*/spec/*.md" 2>/dev/null | head -1)
if [ -n "$_probe" ]; then
  case "$(plan_state "$_probe")" in
    MISSING|THIN|FORKED|READY) ;;
    *) echo "pass-order: DEAD PROBE — the sliced classifier returned no known state on $_probe, so no verdict below would mean anything"; exit 2 ;;
  esac
fi

# ------------------------------------------------------------------------------------ THE CUTOFF
# DATE-GATED on the build README's `opened:` date, the same idiom UNITS_REGION_CUTOFF and
# SPEC_THIN_CUTOFF use and for the same reason: every build that landed before this check existed
# cannot be rewritten, and a term that reds them is unlandable by any run. BLANK turns the term OFF
# and the leg ANNOUNCES that rather than passing silently, because a check grading nothing and a
# check finding nothing print the same thing otherwise.
if [ -z "$PASS_ORDER_CUTOFF" ]; then
  echo "pass-order: the project declares no PASS_ORDER_CUTOFF, so the ORDER term is OFF and no unit is graded on whether its spec predated its build commit"
  exit 0
fi
case "$PASS_ORDER_CUTOFF" in
  [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
  *) echo "pass-order: PASS_ORDER_CUTOFF is not an ISO date, and a cutoff nothing can compare grades every build or none: $PASS_ORDER_CUTOFF"; exit 2 ;;
esac

graded=0; skipped_cutoff=0; skipped_norun=0; unbuilt=0; violations=""

for readme in $(git ls-files "$MEMORY_ROOT/builds/*/README.md" 2>/dev/null); do
  bdir=${readme%/README.md}
  slug=${bdir##*/}
  opened=$(sed -n 's/^opened:[[:space:]]*//p' "$readme" | head -1)
  case "$opened" in [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;; *) skipped_cutoff=$((skipped_cutoff+1)); continue ;; esac
  # `sort -C` over the pair is the same date comparison the driver's THIN term uses; a build opened
  # BEFORE the cutoff keeps the grandfathering.
  if ! printf '%s\n%s\n' "$PASS_ORDER_CUTOFF" "$opened" | sort -C; then
    skipped_cutoff=$((skipped_cutoff+1)); continue
  fi
  run="$bdir/RUN.md"
  if [ ! -f "$run" ]; then skipped_norun=$((skipped_norun+1)); continue; fi
  base=$(sed -n 's/^base:[[:space:]]*//p' "$run" | head -1)
  case "$base" in [0-9a-f][0-9a-f][0-9a-f][0-9a-f]*) ;; *) skipped_norun=$((skipped_norun+1)); continue ;; esac
  GIT cat-file -e "$base^{commit}" 2>/dev/null || { skipped_norun=$((skipped_norun+1)); continue; }

  # The CLOSED units, from the generated region. A row's id is spelled twice, so `match` takes the
  # first occurrence per row rather than a `grep -o` that would emit each unit twice.
  ids=$(awk -v s="$slug" '
      /<!-- gen:build-units -->/ { inr=1; next }
      /<!-- \/gen:build-units -->/ { inr=0 }
      inr && / CLOSED / { if (match($0, "[A-Z]+-" s "-[0-9]+")) print substr($0, RSTART, RLENGTH) }' "$readme" | sort -u)

  for id in $ids; do
    graded=$((graded+1))
    # STEP 1 - the BUILD commit: the earliest commit in BASE..HEAD whose SUBJECT carries this id as a
    # WHOLE TOKEN and which touched a path outside this build's spec/ and reviews/ folders. The
    # whole-token match is `memory/gotchas/id-matched-as-a-substring`: every id ending in a 1-up
    # sequence is a prefix of nine others, so an unanchored `TOOL-x-1` matches `TOOL-x-19`'s commit.
    build_c=""
    for c in $(GIT rev-list --reverse "$base..HEAD" 2>/dev/null); do
      subj=$(GIT log -1 --format=%s "$c" 2>/dev/null)
      case " $(printf '%s' "$subj" | tr -c 'A-Za-z0-9-' ' ') " in *" $id "*) ;; *) continue ;; esac
      # Did it touch anything that is not this build's own spec or review prose?
      if GIT show --pretty=format: --name-only "$c" 2>/dev/null \
         | grep -v '^$' | grep -qv -e "^$bdir/spec/" -e "^$bdir/reviews/"; then
        build_c="$c"; break
      fi
    done
    if [ -z "$build_c" ]; then unbuilt=$((unbuilt+1)); continue; fi

    # STEP 2 - at the build commit's FIRST PARENT, a tracked spec under this build must carry the id
    # in a conforming status header and must not grade MISSING or THIN. The first parent and not the
    # BASE: the build method REQUIRES a run to author a missing spec, so a BASE-anchored test would
    # refuse the shape the method mandates. What this anchor refuses is authoring it AFTERWARDS.
    parent=$(GIT rev-parse "$build_c^" 2>/dev/null) || { unbuilt=$((unbuilt+1)); continue; }
    found=""; state=""
    for sp in $(GIT ls-tree -r --name-only "$parent" -- "$bdir/spec/" 2>/dev/null); do
      blob=$(GIT show "$parent:$sp" 2>/dev/null) || continue
      case " $(printf '%s' "$blob" | head -5 | tr -c 'A-Za-z0-9-' ' ') " in *" $id "*) ;; *) continue ;; esac
      tmp=$(mktemp) || exit 2
      printf '%s\n' "$blob" > "$tmp"
      state=$(plan_state "$tmp"); rm -f "$tmp"
      found="$sp"; break
    done
    if [ -z "$found" ]; then
      violations="$violations
  $id — BUILT at $(GIT rev-parse --short "$build_c") with NO tracked spec at that commit's parent $(GIT rev-parse --short "$parent"); the spec was written after the code, which is the same act with the record written last"
      continue
    fi
    case "$state" in
      MISSING|THIN)
        violations="$violations
  $id — BUILT at $(GIT rev-parse --short "$build_c") against a spec that graded $state at the parent $(GIT rev-parse --short "$parent") ($found); nothing stated what done meant for it before it was built"
        ;;
    esac
  done
done

# ------------------------------------------------------------------------------- THE LIVENESS LINE
# THREE COUNTS, one per population this leg WALKS, because a liveness line naming fewer populations
# than the check walks is a partial probe reporting as a whole one. `unbuilt` is the population step
# 1 drops - a unit whose build commit is outside its run's own range, which is the ordinary shape for
# a resumed build - and omitting it would let a run whose every unit fell outside the range print a
# clean two-count line while grading nothing.
echo "pass-order: graded $graded closed unit(s) · $skipped_cutoff build(s) skipped by the $PASS_ORDER_CUTOFF cutoff · $skipped_norun with no pinned run BASE · $unbuilt unit(s) unbuilt-in-range"

if [ -n "$violations" ]; then
  echo "pass-order FAILED — a unit was BUILT before a conforming spec for it existed:$violations"
  exit 1
fi
exit 0
