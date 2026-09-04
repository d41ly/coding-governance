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
#   - whether the WAIVER REGISTRY's rows deserve their waivers. It grades that each waived unit is
#     still a violation (a stale row REDS) and never why the waiver was granted.
#   - whether a build's COMMITTED `opened:` is honest. TOOL-aStagedLane-1 S6 moved the read from the
#     working tree to the graded commit, which closes the edit-and-run bypass and NOT the class: the
#     graded run still authors the value it commits. Narrowing, not removal, and it is said here
#     because a gate's header states what it does not check.
#
# TOOL-aStagedLane-1 WIDENED THE POPULATION to builds with no run-state file. The range for those is
# derived from the build FOLDER's own first commit instead of a run's pinned BASE; see THE RANGE
# below. `--preview` grades the live tree and prints violations without setting exit status, which is
# how a candidate predicate gets run over the real tree before it is wired.
set -u
KIT_UNATTENDED_VERSION=1.17   # gov:kit unattended@1.17 — must match unattended.sh; check-kit-versions.sh pairs them

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

# S2f - `--preview` grades the live tree and prints everything it finds WITHOUT setting exit status.
# AGENTS.md section 7 requires a candidate gate predicate to be run over the real tree before it is
# wired, printing hits AND near-misses; without a mode that does not red, doing so means editing the
# script or reading a failing bar. The blocker this leg's own build met at round 3 - two units
# already on the default branch that the widened predicate reds - was found exactly this way.
PREVIEW=0
case "${1:-}" in --preview) PREVIEW=1 ;; "") ;; *) echo "pass-order: unknown argument: $1" >&2; exit 2 ;; esac

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "pass-order: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
HERE="$(cd "$(dirname "$0")" && pwd)"
DRIVER="$HERE/unattended.sh"
CONF="$ROOT/.unattended.conf"

[ -f "$CONF" ] || { echo "pass-order: no .unattended.conf at the repo root, and every value this leg needs is a declaration"; exit 2; }
[ -f "$DRIVER" ] || { echo "pass-order: no driver beside this script, and the classifier below is sliced out of it"; exit 2; }

MEMORY_ROOT=""; PASS_ORDER_CUTOFF=""; GENERATED_INDEXES=""; SHARED_RECORDS=""
PASS_ORDER_PREANCHOR_CAP=""
# ---- THE CONF IS IMPORTED, NEVER SOURCED INTO THIS SHELL, and this block is `check-unattended.sh`'s
# ---- verbatim rather than a third hand-written reader. `$CONF` is a TRACKED file the graded run
# ---- commits, so sourcing it here executes it, and both siblings hardened this one recorded
# ---- incident at a time. Reproduced against THIS leg before the fix, on a fixture that reds
# ---- honestly: an appended `exit 0` gave rc 0 with zero bytes of output, byte-indistinguishable
# ---- from a clean tree; `trap 'exit 0' EXIT` was worse — the leg PRINTED its own FAILED line and
# ---- still exited 0. The conf loads AFTER the library here, so it could also redefine the pinned
# ---- `GIT` wrapper this file's header spends nine lines insisting on.
# ----
# ---- PROTOCOL §1 cost 2 concedes that a leg reading this conf reads its subject's ANSWER. It does
# ---- not concede code execution that suppresses the leg's own return code and output.
# ----
# ---- So nothing from that file executes in this shell. It is sourced inside a SUBSHELL and the
# ---- declared keys come back as a NUL-delimited name/value stream terminated by a sentinel; a trap,
# ---- a redefined function or an `exit` cannot cross that boundary, and the worst a hostile conf can
# ---- do is fail to deliver the sentinel, which is a refusal. Only `[A-Z][A-Z0-9_]*` names are
# ---- assignable, so the stream cannot introduce a name this leg does not expect.
_conf_names=$(sed -n 's/^[[:space:]]*\(export[[:space:]][[:space:]]*\)\{0,1\}\([A-Z][A-Z0-9_]*\)=.*/\2/p' "$CONF" | sort -u)
_conf_ok=0
while IFS= read -r -d '' _ck; do
  IFS= read -r -d '' _cv || break
  case "$_ck" in
    __CONF_IMPORT_OK__) _conf_ok=1 ;;
    # AN ALLOW-LIST, NOT A GLOB, and this is where the spliced block had to be adapted rather than
    # copied. The sibling assigns EVERY uppercase key it sees, which is safe THERE because that
    # script sets nothing it cares about above the import. This one sets DRIVER at :51 — the path it
    # eval's the classifier out of — so one tracked conf line `DRIVER="tools/unattended/evil.sh"`
    # made the leg eval an attacker-chosen file and exit 0 with its own FAILED line printed.
    # Reproduced end to end before this line existed. Only the keys this leg DECLARES are assignable,
    # so the stream cannot reach a name the leg did not ask for.
    MEMORY_ROOT|PASS_ORDER_CUTOFF|GENERATED_INDEXES|SHARED_RECORDS|PASS_ORDER_PREANCHOR_CAP) eval "$_ck=\$_cv" ;;
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
  echo "pass-order: the project conf does not source cleanly, so this leg cannot read a declared value - and sourcing it in this shell would let that file end or take over the leg rather than be graded by it: $CONF"
  exit 2
fi
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

# ------------------------------------------------------------------------- THE WAIVER REGISTRY
# S2e. The widening reds two units already landed on the default branch, and history is append-only,
# so the leg could not otherwise be wired at all. The registry is a DECLARED population: one row per
# waived unit, `<unit-id><TAB><reason>`, comments and blanks ignored.
#
# AN ABSENT FILE MEANS AN EMPTY WAIVER SET, never a blanket one. An exemption list that exempts
# everything when it goes missing is the vacuous-selector class on the one path this leg reports a
# hard violation, so the default direction is the one that REDS.
#
# AND A STALE ROW REDS. A waiver naming a unit this leg no longer reports is an exemption that has
# outlived its reason, and leaving it silently widens the surface it was written to narrow - the same
# posture every other declared population in this repo takes.
WAIVER_FILE="$MEMORY_ROOT/project/pass-order-waiver.txt"
waived_ids=""
if [ -f "$WAIVER_FILE" ]; then
  # FLATTENED TO ONE SPACE-SEPARATED LINE, and the unquoted expansion doing it is load-bearing rather
  # than sloppy. The membership tests below are `case " $waived_ids " in *" $id "*`, which needs a
  # SPACE on both sides of every id. Left as grep's newline-separated output, the first row matches
  # only if it is also the last — so a ONE-ROW registry works and a two-row one silently waives
  # nothing. Found by running the wired leg over the real tree, which has two rows, AFTER a self-test
  # arm carrying one row had passed: the instance was covered and the class was not.
  waived_ids=$(sed -e 's/#.*//' -e 's/[[:space:]].*$//' "$WAIVER_FILE" | grep -E '^[A-Z]+-[A-Za-z]+-[0-9]+$' || true)
  waived_ids=$(echo $waived_ids)
fi

graded=0; skipped_cutoff=0; norun_graded=0; unbuilt=0; preanchor_hits=0; waived_n=0; truncated=0
violations=""; waived_seen=""; previews=""

for readme in $(git ls-files "$MEMORY_ROOT/builds/*/README.md" 2>/dev/null); do
  bdir=${readme%/README.md}
  slug=${bdir##*/}
  # S6 - THE CUTOFF IS READ FROM THE COMMIT BEING GRADED, not the working tree. Reading it from disk
  # let one uncommitted character exempt a build from this leg, and the widening multiplies the
  # population that field governs. One object read per build, none per unit. The residual - the run
  # still authors the value it COMMITS - is in this file's header rather than left to be discovered.
  opened=$(GIT show "HEAD:$readme" 2>/dev/null | sed -n 's/^opened:[[:space:]]*//p' | head -1)
  case "$opened" in [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;; *) skipped_cutoff=$((skipped_cutoff+1)); continue ;; esac
  # `sort -C` over the pair is the same date comparison the driver's THIN term uses; a build opened
  # BEFORE the cutoff keeps the grandfathering.
  if ! printf '%s\n%s\n' "$PASS_ORDER_CUTOFF" "$opened" | sort -C; then
    skipped_cutoff=$((skipped_cutoff+1)); continue
  fi

  # ------------------------------------------------------------------------------- THE RANGE
  # S1/S2/S2b. A run's pinned BASE where one is readable; otherwise the build FOLDER's own first
  # commit. `norun` marks which, because the pre-anchor probe below is scoped to the derived-range
  # population - an unattended build's BASE is pinned before its run starts and has no such hole.
  #
  # THE ANCHOR IS `<first>^`, so the range INCLUDES `<first>` itself: `rev-list A..HEAD` excludes A,
  # and a commit that creates the build folder and writes product code in one act is precisely the
  # violation this widening exists to catch. A root commit has no parent, so the walk starts there.
  #
  # S2b - AN UNUSABLE `base:` FALLS BACK rather than skipping. Otherwise a build with a garbage
  # RUN.md would be MORE exempt than a build with none, which is one committed line away from any
  # run that wants out of this leg.
  run="$bdir/RUN.md"
  base=""; norun=1
  if [ -f "$run" ]; then
    base=$(sed -n 's/^base:[[:space:]]*//p' "$run" | head -1)
    case "$base" in
      [0-9a-f][0-9a-f][0-9a-f][0-9a-f]*) GIT cat-file -e "$base^{commit}" 2>/dev/null && norun=0 || base="" ;;
      *) base="" ;;
    esac
  fi
  first=""
  if [ "$norun" = 1 ]; then
    first=$(GIT rev-list --reverse HEAD -- "$bdir" 2>/dev/null | head -1)
    [ -n "$first" ] || { skipped_cutoff=$((skipped_cutoff+1)); continue; }
    base=$(GIT rev-parse "$first^" 2>/dev/null) || base=""
    norun_graded=$((norun_graded+1))
  fi

  # The CLOSED units, from the generated region. A row's id is spelled twice, so `match` takes the
  # first occurrence per row rather than a `grep -o` that would emit each unit twice.
  ids=$(awk -v s="$slug" '
      /<!-- gen:build-units -->/ { inr=1; next }
      /<!-- \/gen:build-units -->/ { inr=0 }
      inr && / CLOSED / { if (match($0, "[A-Z]+-" s "-[0-9]+")) print substr($0, RSTART, RLENGTH) }' "$readme" | sort -u)

  for id in $ids; do
    graded=$((graded+1))
    # STEP 1 - the BUILD commit: the earliest commit in BASE..HEAD whose SUBJECT carries this id as a
    # WHOLE TOKEN and which touched a path outside the RECORD SURFACE below. The whole-token match is
    # `memory/gotchas/id-matched-as-a-substring`: every id ending in a 1-up sequence is a prefix of
    # nine others, so an unanchored `TOOL-x-1` matches `TOOL-x-19`'s commit.
    #
    # THE EXCLUSION IS THE BUILD'S WHOLE FOLDER PLUS THE GENERATED INDEXES, and getting this wrong
    # made a CONFORMING run unlandable. It was `spec/` and `reviews/` alone, and a spec pass
    # legitimately writes more than those two: the regenerated index, the build README, the run-state
    # file and the month ledger all sit outside them. So a SPEC commit naming the unit id won the
    # selection and step 2 then graded ITS parent — where, correctly, no spec exists yet — and the leg
    # reported "the spec was written after the code" about a run that did the opposite. Reproduced on
    # the spec-first fixture. The shape is this corpus's norm rather than a corner: `spec(<slug>):
    # <id> ...` subjects are everywhere, and this build escaped only because its own spec commit
    # named the slug and no unit id. With `red_after_land = true` and history append-only, the next
    # conforming run would have been unlandable short of a bypass.
    #
    # `GENERATED_INDEXES` is read from the conf as `index:generator` pairs; only the index half is an
    # excluded path, because a commit touching the GENERATOR is touching product code.
    # THE RECORD SURFACE a spec pass legitimately writes: this build's folder, the generated indexes,
    # AND the SHARED RECORDS. The last was omitted at first and it is not a corner — template section
    # 1 MANDATES a backlog row, so a conforming spec-first run writes `memory/backlog/<FAMILY>.md`
    # in the same commit, which put the commit back outside the exclusion and redded the run that
    # followed the method exactly. Reproduced on this kit's own fixture.
    _gen_ex=""
    for _gi in $GENERATED_INDEXES; do
      _gp=${_gi%%:*}
      [ -n "$_gp" ] && _gen_ex="$_gen_ex -e ^$_gp"
    done
    for _sr in $SHARED_RECORDS; do
      [ -n "$_sr" ] && _gen_ex="$_gen_ex -e ^$_sr"
    done
    # ONE PREDICATE, TWO WINDOWS. `_find_build_commit <rev-range>` is the whole build-commit
    # definition and both the in-range walk and the pre-anchor probe call it. A second copy would be
    # two answers to one question, and the copy would be the one that drifts.
    _find_build_commit() {
      local _range="$1" _cap="$2" _c _subj _n=0
      for _c in $(GIT rev-list --reverse $_range 2>/dev/null); do
        if [ -n "$_cap" ] && [ "$_n" -ge "$_cap" ]; then printf 'TRUNCATED'; return 0; fi
        _n=$((_n+1))
        _subj=$(GIT log -1 --format=%s "$_c" 2>/dev/null)
        case " $(printf '%s' "$_subj" | tr -c 'A-Za-z0-9-' ' ') " in *" $id "*) ;; *) continue ;; esac
        # Did it touch anything outside this build's own record surface?
        if GIT show --pretty=format: --name-only "$_c" 2>/dev/null \
           | grep -v '^$' | grep -qv -e "^$bdir/" $_gen_ex; then
          printf '%s' "$_c"; return 0
        fi
      done
      return 0
    }
    build_c=$(_find_build_commit "${base:+$base..}HEAD" "")
    if [ -z "$build_c" ]; then
      # S2c - THE PRE-ANCHOR PROBE, and it runs ONLY for the derived-range population. A commit that
      # writes product code for a unit touches nothing under the build folder, so it sits STRICTLY
      # EARLIER than that folder's first commit and outside the derived range entirely - the most
      # flagrant instance of the violation, landing in a tally this file's own liveness block warns
      # must not be read as benign. The window is INCLUSIVE of the anchor `<first>^`, which the range
      # above excludes, so `rev-list <anchor>` and never `<anchor>^`.
      #
      # SAME PREDICATE, exclusion included. Without it a `backlog(<id>): open the row` commit - which
      # ordinarily lands before the build folder exists - reads as a violation and reds a conforming
      # build. This script's own comment above records that dropping the exclusion once made a
      # conforming run unlandable.
      #
      # S2d - BOUNDED BY CONSTRUCTION, because the miss rate over the widened population could not be
      # measured before this landed. A probe that gives up is COUNTED, never reported as a miss.
      if [ "$norun" = 1 ] && [ -n "$base" ]; then
        pre_c=$(_find_build_commit "$base" "${PASS_ORDER_PREANCHOR_CAP:-400}")
        if [ "$pre_c" = TRUNCATED ]; then
          truncated=$((truncated+1))
        elif [ -n "$pre_c" ]; then
          preanchor_hits=$((preanchor_hits+1))
          _v="  $id — BUILT at $(GIT rev-parse --short "$pre_c") BEFORE this build's folder existed, so no spec for it can have existed either"
          case " $waived_ids " in
            *" $id "*) waived_n=$((waived_n+1)); waived_seen="$waived_seen $id" ;;
            *) violations="$violations
$_v" ;;
          esac
          previews="$previews
$_v"
          continue
        fi
      fi
      unbuilt=$((unbuilt+1)); continue
    fi

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
    # EVERY VIOLATION ROUTES THROUGH THE WAIVER, and one helper does it so a future violation class
    # cannot be added on a path that forgets to consult the registry.
    _report() {
      previews="$previews
$1"
      case " $waived_ids " in
        *" $id "*) waived_n=$((waived_n+1)); waived_seen="$waived_seen $id" ;;
        *) violations="$violations
$1" ;;
      esac
    }
    if [ -z "$found" ]; then
      _report "  $id — BUILT at $(GIT rev-parse --short "$build_c") with NO tracked spec at that commit's parent $(GIT rev-parse --short "$parent"); the spec was written after the code, which is the same act with the record written last"
      continue
    fi
    case "$state" in
      MISSING|THIN)
        _report "  $id — BUILT at $(GIT rev-parse --short "$build_c") against a spec that graded $state at the parent $(GIT rev-parse --short "$parent") ($found); nothing stated what done meant for it before it was built"
        ;;
    esac
  done
done

# ------------------------------------------------------------------------------- THE LIVENESS LINE
# THREE COUNTS, one per population this leg WALKS, because a liveness line naming fewer populations
# than the check walks is a partial probe reporting as a whole one. `unbuilt` is the population step
# 1 drops: a unit whose build commit is outside its run's own range.
#
# DO NOT READ A NON-ZERO `unbuilt` AS BENIGN. It is the ordinary shape for a RESUMED build, and it is
# ALSO what a widened exclusion set looks like — every commit falls inside the excluded surface, no
# build commit is found, and the leg reports a clean bill with a count a reader has been taught to
# ignore. An earlier revision of this comment said only the benign half, which is why the exclusion
# set is now printed beside it.
# THE EXCLUSION SET IS PRINTED, and that is not decoration. It is composed from two conf keys the
# GRADED RUN can commit, so widening `GENERATED_INDEXES` to something like `tools:g memory:g` turns a
# real violation green — and the only trace was the `unbuilt-in-range` count, which this file's own
# comment teaches a reader is the ordinary shape for a resumed build. Naming the set makes a widened
# one visible in the one line an operator actually reads. It does not PREVENT the widening: the conf
# is inside the run's reach and protocol section 1 cost 2 concedes exactly that, so what this buys is
# a trace, not a guard, and saying which is the point.
# SIX COUNTS, one per population this leg walks, and `skipped_norun` is GONE rather than pinned at
# zero: S1 grades those builds and S2b routes an unusable base to the folder anchor, so every path
# that once incremented it is closed. A field that can only ever print 0 is a dead probe whatever
# value it shows, and this file's own doctrine is that a probe which cannot move says so.
echo "pass-order: graded $graded closed unit(s) · $skipped_cutoff build(s) skipped by the $PASS_ORDER_CUTOFF cutoff · $norun_graded build(s) graded with no run-state file · $unbuilt unit(s) unbuilt-in-range · $preanchor_hits pre-anchor violation(s) · $waived_n waived by $WAIVER_FILE · $truncated probe(s) truncated at the ${PASS_ORDER_PREANCHOR_CAP:-400}-commit cap"
echo "pass-order: the record surface excluded from build-commit selection was: <build folder> $(printf '%s ' $GENERATED_INDEXES $SHARED_RECORDS)"

# A STALE WAIVER REDS. A row naming a unit this leg no longer reports has outlived its reason, and an
# exemption nobody re-checks silently widens the surface it was written to narrow.
stale=""
for _w in $waived_ids; do
  case " $waived_seen " in *" $_w "*) ;; *) stale="$stale $_w" ;; esac
done

if [ "$PREVIEW" = 1 ]; then
  echo "pass-order --preview: every violation the predicate finds, waived or not:${previews:-
  (none)}"
  [ -n "$stale" ] && echo "pass-order --preview: waiver rows matching nothing:$stale"
  echo "pass-order --preview: exit status is NOT set in this mode"
  exit 0
fi

if [ -n "$stale" ]; then
  echo "pass-order FAILED — $WAIVER_FILE waives unit(s) this leg no longer reports as a violation, and a stale exemption widens the surface it was written to narrow:$stale"
  exit 1
fi

if [ -n "$violations" ]; then
  echo "pass-order FAILED — a unit was BUILT before a conforming spec for it existed:$violations"
  exit 1
fi
exit 0
