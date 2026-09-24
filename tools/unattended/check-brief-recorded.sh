#!/usr/bin/env bash
# check-brief-recorded.sh - the merge-bar leg that refuses a CLOSED unit whose build commit records
# no brief. TOOL-aHoistedPass-7. Contract: memory/guides/UNATTENDED-PROTOCOL.md. Project layer:
# .unattended.conf.
#
#   bash tools/unattended/check-brief-recorded.sh
#
# Exit 0 = clean. Exit 1 = a violation. Exit 2 = misconfigured.
#
# WHAT THIS CHECKS, in one sentence: for every unit a build README carries as CLOSED after the
# declared cutoff and BUILT WHILE A RUN WAS LIVE, the commit that BUILT that unit carries a
# `brief · item <id>` row in the run-state file whose twelve-hex hash still joins to a tracked file
# at that same commit.
#
# WHY THE BUILD COMMIT AND NOT ITS FIRST PARENT, which is where the sibling `pass-order` leg anchors.
# `--brief` STAGES its row rather than committing it, so the row lands in the same commit as the
# pass. MEASURED 2026-09-04 at `c4fcf5ad` over the three tracked builds that carried brief rows:
# twenty-six units carried a row at their build commit and exactly ONE of those also carried one at
# the first parent, so a first-parent anchor redded 25 of 26 CONFORMING units - including
# `TOOL-dBriefedPass-2`, the unit that built the verb. That is a dated snapshot of a population that
# GROWS, which is why it is stated here, once, with its commit, and nowhere else.
#
# THE TWO LEGS ARE JOINTLY SATISFIABLE, which a reader meeting them together will want to know before
# concluding otherwise: `pass-order` wants a conforming spec at the build commit's PARENT and this one
# wants a brief row AT the build commit, and one conforming pass satisfies both by writing the spec in
# an earlier commit and the brief row alongside the code. Two guards asking one question two ways is a
# recorded class in this tree; these ask two questions.
#
# ONLY A UNIT BUILT DURING A RUN IS GRADED, by the owner's ruling of 2026-09-13, recorded in build
# `dPolishedVitrine`. A brief is what a run hands the agent that builds a unit, so a unit built after
# its build's run had already finished was built outside any run and was owed none. The first
# adopter to meet this built a unit by hand the day after its run landed, and this leg redded it for
# a row no run was there to write.
#
# THE PREDICATE IS THE PHASE OF THE RUN-STATE FILE AT THE BUILD COMMIT, the commit this leg already
# reads the brief row from. That file names the record that was live, or had last finished, at that
# commit: `--preflight` retires a finished record by renaming it and scaffolds the next run's record
# in the SAME commit, so the path never names a stale run. A phase in the driver's PHASES_TERMINAL
# means the run had finished; anything else, an absent file or phase included, is graded exactly as it
# was before this unit. The terminal set is READ from the driver and spelled nowhere in this file.
#
# THE BOUNDARY IS THE COMMIT THAT WRITES THE TERMINAL PHASE. A unit whose code rides in that commit is
# outside the run, because `--landed`'s witness is a commit already on the remote and so the code in
# the commit recording it is not in what landed. The last live phase, LANDING, is still graded.
#
# A WRONGLY PICKED BUILD COMMIT MAY NOT BUY A SKIP. `build_commit` returns the EARLIEST in-range commit
# that names the id and touches a path outside the record surface, and a hand commit made between two
# runs qualifies. At that commit the record still reads the first run's terminal phase, and the second
# run's preflight retires the record only afterwards, so HEAD still bears the claim out. Round 3 of the
# closing review of build `dPolishedVitrine` reproduced a unit built during the second, live run being
# skipped exactly that way. So before a skip is honoured, every later commit that the same predicate
# accepts for the id is asked the same phase question, and the first one made while a run was live is
# where the unit is graded, announced by id with both commits and counted. This fails CLOSED: a later
# commit that names the id while a run is live grades the unit even if it only touched a file the conf
# forgot to exclude. The library is not changed, so `pass-order` keeps the pick it always had.
#
# THE CLAIM MUST STILL STAND AT HEAD, because the run authors the phase it commits. A record reading
# LANDED at one commit and BUILDING at the next would otherwise buy a unit out of this leg with two
# hand edits that leave nothing at HEAD. So the skip is honoured only while HEAD carries a record
# making the SAME claim - its base, phase and witness - at the run-state path, or in a retired
# `RUN.<phase>.<8hex>.md` that did not exist yet at the build commit. The absence test is what stops a
# run copying the claim of a record retired BEFORE the unit was built. A claim HEAD does not bear out
# is ANNOUNCED and the unit is graded as though the run were live.
#
# THE TRIPLE AND NOT THE BYTES. Finished records ARE edited after they finish: a kit migration added a
# halt code to six aborted records, two of them already retired, and a later merge fix did the same to
# a seventh. None of those edits moved the triple. MEASURED 2026-09-13 at `f1e58789` over every build
# with a pinned BASE, cutoff ignored: 25 units were built under a finished record, HEAD bears out all
# 25, and a byte comparison would have borne out 8. No unit in that tree needs the retired-record half,
# which is why a staged arm carries it. A dated snapshot of a population that grows.
#
# REACHABILITY FROM THE TERMINAL WITNESS WAS THE REJECTED PREDICATE. It needs the phase at the build
# commit anyway, to know which record's witness to read; it has no answer for an aborted run whose
# witness is not a sha, which the protocol permits; and against the two-edit forgery it adds nothing,
# because the witness at the build commit is written in the same edit as the phase.
#
# WHAT THIS DOES NOT CHECK, stated in the header because a structural check reads as a semantic one
# to everybody who did not write it:
#   - WHETHER THE BRIEF SAID ANYTHING. This leg reads a path and a hash. Whether the prose was useful,
#     accurate or even about this unit is outside it.
#   - WHETHER THE BRIEF PRECEDED THE CODE. It cannot: both land in one commit, and recovering the
#     order needs `--brief` to commit its own row, which breaks the one-commit-per-pass discipline
#     `stage_or_fail` exists to keep. Rejected in the spec's section 3 and not revisited.
#   - WHETHER A HARNESS PRODUCED THE BRIEF. An agent boundary leaves no artifact inside this repo's
#     reach: `dRetiredFork` ran without the harness and wrote 28 rows byte-identical to a harnessed
#     run's. A term claiming to see the harness would reproduce `passes-harnessed`'s exact failure.
#   - ANYTHING ABOUT a unit that is not CLOSED, a build with no pinned run BASE, or a build opened
#     before the cutoff. Those three are COUNTED on the liveness line, never silently skipped.
#   - WHETHER THE COMMITTED `opened:` OR THE COMMITTED CONF ARE HONEST. Every read below comes from
#     the graded commit, which closes the edit-and-run bypass and NOT the class: the graded run still
#     authors the values it commits, and protocol section 1 cost 2 concedes exactly that.
#   - WHETHER A FINISHED RECORD THAT STANDS AT HEAD IS HONEST. The skip above trusts a terminal claim
#     HEAD still carries. A run that forges one AND keeps it, or commits a retired record to carry it,
#     leaves that record at HEAD, where the kit gate grades it - check 15 judges a LANDED witness. This
#     leg buys the trace, not the verdict.
#   - ANYTHING ABOUT A UNIT BUILT AFTER ITS RUN FINISHED. It is announced by id and reason and graded by
#     nothing here. Whether its spec came first is still `pass-order`'s, which grades it unchanged.
#
# THE COUNT THAT PROVES TERM 1 RAN IS `graded` MINUS `unbuilt-in-range` MINUS `built after their run
# finished`, not `graded`. `graded` increments before the build-commit selection, exactly as the
# sibling's does, so a unit graded by nothing still counts as graded. That is copied deliberately and
# it is a hole; naming it here is the whole remedy, and the arms assert on the difference. The
# post-run subset joined it rather than moving the increment, which would change what the sibling's
# identically named count means.
set -u
KIT_UNATTENDED_VERSION=1.32   # gov:kit unattended@1.32 — must match unattended.sh; check-kit-versions.sh pairs them

# The dereference pin, identical to this kit's other readers and for the identical reason: a graft
# file rewrites the commit GRAPH, so every ancestry answer below could be honest about a sha and
# wrong about what that sha means.
export GIT_GRAFT_FILE=/dev/null
# EVERY SHA DEREFERENCE BELOW GOES THROUGH `GIT`, the library's pinned wrapper, never bare `git`.
# A `git replace` ref rewrites what a sha MEANS for every read, so this leg could resolve an honest
# commit and grade forged bytes - and it grades a blob id against a twelve-hex prefix, which is
# exactly the kind of answer a substituted object would flip. The kit's own check 28c enforces it,
# and this script joins that population by being a non-test `*.sh` in this directory.

_LIB_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
[ -f "$_LIB_DIR/lib-unattended.sh" ] || {
  echo "brief-recorded: the kit library is missing beside this script, so the build-commit predicate it shares with the sibling leg is unavailable and no answer here would be trustworthy: $_LIB_DIR/lib-unattended.sh" >&2
  exit 2
}
# shellcheck source=lib-unattended.sh
. "$_LIB_DIR/lib-unattended.sh"

case "${1:-}" in "") ;; *) echo "brief-recorded: unknown argument: $1" >&2; exit 2 ;; esac

ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "brief-recorded: not a git repo"; exit 2; }
cd "$ROOT" || exit 2
HERE="$(cd "$(dirname "$0")" && pwd)"
DRIVER="$HERE/unattended.sh"
CONF="$ROOT/.unattended.conf"

[ -f "$CONF" ] || { echo "brief-recorded: no .unattended.conf at the repo root, and every value this leg needs is a declaration"; exit 2; }
[ -f "$DRIVER" ] || { echo "brief-recorded: no driver beside this script, and the row grammar this leg matches is written by exactly one function in that file, so there would be nothing to assert the grammar against"; exit 2; }

MEMORY_ROOT=""; BRIEF_RECORDED_CUTOFF=""; GENERATED_INDEXES=""; SHARED_RECORDS=""
# ---- THE CONF IS IMPORTED, NEVER SOURCED INTO THIS SHELL, and this block is `check-pass-order.sh`'s
# ---- rather than a third hand-written reader. `$CONF` is a TRACKED file the graded run commits, so
# ---- sourcing it here executes it. Both siblings hardened this one recorded incident at a time: an
# ---- appended `exit 0` gives rc 0 with zero bytes of output, byte-indistinguishable from a clean
# ---- tree, and `trap 'exit 0' EXIT` is worse - the leg PRINTS its own FAILED line and still exits 0.
# ---- The conf loads AFTER the library here, so it could also redefine the pinned `GIT` wrapper this
# ---- file's header spends six lines insisting on.
# ----
# ---- PROTOCOL section 1 cost 2 concedes that a leg reading this conf reads its subject's ANSWER. It
# ---- does not concede code execution that suppresses the leg's own return code and output.
# ----
# ---- So nothing from that file executes in this shell. It is sourced inside a SUBSHELL and the
# ---- declared keys come back as a NUL-delimited name/value stream terminated by a sentinel; a trap,
# ---- a redefined function or an `exit` cannot cross that boundary, and the worst a hostile conf can
# ---- do is fail to deliver the sentinel, which is a refusal.
_conf_names=$(sed -n 's/^[[:space:]]*\(export[[:space:]][[:space:]]*\)\{0,1\}\([A-Z][A-Z0-9_]*\)=.*/\2/p' "$CONF" | sort -u)
_conf_ok=0
while IFS= read -r -d '' _ck; do
  IFS= read -r -d '' _cv || break
  case "$_ck" in
    __CONF_IMPORT_OK__) _conf_ok=1 ;;
    # AN ALLOW-LIST, NOT A GLOB, and it is THIS leg's own declared four rather than the sibling's
    # five. The sibling assigns every uppercase key it sees and had to stop: it sets `DRIVER` above
    # its import - the path it eval's a classifier out of - so one tracked conf line
    # `DRIVER="tools/unattended/evil.sh"` made that leg eval an attacker-chosen file and exit 0 with
    # its own FAILED line printed. This leg sets `DRIVER` and `CONF` above its import too. Only the
    # keys declared on the line above are assignable, so the stream cannot reach a name this leg did
    # not ask for.
    MEMORY_ROOT|BRIEF_RECORDED_CUTOFF|GENERATED_INDEXES|SHARED_RECORDS) eval "$_ck=\$_cv" ;;
  esac
done < <( . "$CONF" >/dev/null 2>&1 || exit 9
          for _n in $_conf_names; do eval "_cval=\${$_n:-}"; printf '%s\0%s\0' "$_n" "$_cval"; done
          printf '__CONF_IMPORT_OK__\0\0' )
# THE SENTINEL IS THE WHOLE VERDICT. `|| exit 9` catches a parse error and a `return 0`, both of
# which abort the file and RETURN rather than ending the subshell; its absence catches the `exit` and
# `set -u` shapes, which end the subshell before the sentinel is written.
if [ "$_conf_ok" != 1 ]; then
  echo "brief-recorded: the project conf does not source cleanly, so this leg cannot read a declared value - and sourcing it in this shell would let that file end or take over the leg rather than be graded by it: $CONF"
  exit 2
fi
MEMORY_ROOT="${MEMORY_ROOT:-memory}"

# --------------------------------------------------------------------------- THE GRAMMAR PROBE
# A PROBE THAT CANNOT MOVE SAYS SO. The sibling leg's DEAD PROBE guards a classifier it slices out of
# the driver by line span; this leg slices nothing, so that probe has no counterpart here. What it
# has instead is a GRAMMAR coupling, and it is exactly as load-bearing.
#
# The row this leg matches is written by ONE function in ONE file - `verb_brief`, through `park()`,
# whose own header pins the reason field as LINE-FINAL because two other readers depend on it. If the
# driver stops spelling that grammar, every graded unit reds with "no brief row" and the leg reports a
# corpus of false accusations wearing a finding's clothes. Two greps convert all of them into one
# honest refusal.
#
# TWO LITERALS AND NOT ONE, which is a correction to the spec. ` brief · item ` with a LEADING space
# appears in the driver only as an argument to its own `grep -F`, so asserting that alone couples this
# leg to the driver's READER and not to its writer. `brief · item ` glued is `verb_brief`'s own
# spelling of the row it is about to write, and ` · reason ` is `park()`'s line-final reason field -
# the one the hash and the path ride on. Both halves of what this leg parses, and both from the
# writing side.
#
# GRADED BEFORE THE CUTOFF, deliberately: a probe that cannot move must say so whether or not the term
# it guards is switched on, and a blank cutoff below exits 0 with an announcement that would otherwise
# be indistinguishable from a leg whose grammar had rotted away.
if ! grep -qF -- 'brief · item ' "$DRIVER" || ! grep -qF -- ' · reason ' "$DRIVER"; then
  echo "brief-recorded: DEAD PROBE — the driver no longer spells the 'brief · item ' / ' · reason ' row grammar this leg matches, so every unit below would red for a row nothing can write any more, which is a corpus of false accusations rather than a finding: $DRIVER"
  exit 2
fi

# ----------------------------------------------------------------------------- THE TERMINAL SET
# WHICH PHASES MEAN "THIS RUN HAS FINISHED" IS THE DRIVER'S `PHASES_TERMINAL`, and this file does not
# spell it a second time. It is PARSED, never sourced, with the kit gate's grammar for a core
# declaration: the first line that is exactly `PHASES_TERMINAL="…"`, trailing whitespace allowed.
#
# A SET THIS LEG CANNOT READ IS A DEAD PROBE, never an empty set. An empty set grades every unit as
# though every run were still live, which is the verdict this unit exists to correct, delivered
# silently. Checked before the cutoff for the grammar probe's reason.
TERMINAL_PHASES=""
while IFS= read -r _dl || [ -n "$_dl" ]; do
  _dl=${_dl%$'\r'}
  while :; do case "$_dl" in *' '|*$'\t') _dl=${_dl%?} ;; *) break ;; esac; done
  case "$_dl" in
    'PHASES_TERMINAL="'*'"') _dl=${_dl#'PHASES_TERMINAL="'}; TERMINAL_PHASES=${_dl%'"'}; break ;;
  esac
done < "$DRIVER"
_tp_ok=0
for _tp in $TERMINAL_PHASES; do
  case "$_tp" in *[!A-Z]*) _tp_ok=0; break ;; *) _tp_ok=1 ;; esac
done
if [ "$_tp_ok" != 1 ]; then
  echo "brief-recorded: DEAD PROBE — the driver's PHASES_TERMINAL cannot be read as a set of phase tokens, so this leg cannot tell a unit built after its run finished from one built during it, and an empty set would grade them all as though the run were live: [$TERMINAL_PHASES] in $DRIVER"
  exit 2
fi

# ONE AWK PROGRAM READS A RECORD'S CLAIM, so the build commit's record and HEAD's are read the same way.
# The claim is the record's base, phase and witness, one per line and in that order: each value is one
# line of the record, so a newline cannot occur inside one and the joined claim cannot be ambiguous.
# The field grammar is the driver's `fact`: the FIRST line opening with the key and a colon, a trailing
# CR dropped, leading SPACES dropped and nothing else touched.
#
# A DOT CLOSES THE CLAIM, and it is load-bearing. Command substitution strips trailing newlines, so
# without a terminator a record carrying a base and nothing else collapses to one line, and the phase
# read below returns the BASE: a record reading `base: LANDED` would be a finished run. The first
# draft had exactly that shape and an arm now pins it.
CLAIM_AWK='
  { sub(/\r$/, "") }
  !hb && /^base:/    { v = $0; sub(/^base: */, "", v);    b = v; hb = 1 }
  !hp && /^phase:/   { v = $0; sub(/^phase: */, "", v);   p = v; hp = 1 }
  !hw && /^witness:/ { v = $0; sub(/^witness: */, "", v); w = v; hw = 1 }
  END { printf "%s\n%s\n%s\n.", b, p, w }'

# ------------------------------------------------------------------------------------ THE CUTOFF
# DATE-GATED on the build README's `opened:` date, the idiom PASS_ORDER_CUTOFF, SPEC_THIN_CUTOFF,
# UNITS_REGION_CUTOFF, LANDED_ANCHOR_CUTOFF and DISPOSITION_CUTOFF already share. BLANK turns the term
# OFF and the leg ANNOUNCES that rather than passing silently, because a check grading nothing and a
# check finding nothing print the same thing otherwise.
#
# ITS VALUE IS THE LANDING DATE AND THE CONSEQUENCE IS STATED RATHER THAN BURIED: this leg grades ZERO
# units on the day it lands. All three builds carrying brief rows opened on 2026-09-01, -02 and -03,
# and five units among them carry no row at all, so any cutoff old enough to grade the conforming ones
# is old enough to make the leg unlandable, and a per-build cutoff cannot admit one unit without its
# siblings. The evidential weight therefore sits in the staged arms of check-brief-recorded.test.sh,
# observed RED before this landed - not in a waiver registry, because an exemption is not coverage.
if [ -z "$BRIEF_RECORDED_CUTOFF" ]; then
  echo "brief-recorded: the project declares no BRIEF_RECORDED_CUTOFF, so the BRIEF term is OFF and no unit is graded on whether its build commit recorded the brief it was built from"
  exit 0
fi
case "$BRIEF_RECORDED_CUTOFF" in
  [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
  *) echo "brief-recorded: BRIEF_RECORDED_CUTOFF is not an ISO date, and a cutoff nothing can compare grades every build or none: $BRIEF_RECORDED_CUTOFF"; exit 2 ;;
esac

# ---- THE SUBJECT CACHE, which this leg was built WITHOUT. TOOL-aQuenchedHarness-13.
#
# `build_commit` walks the whole in-range history ONCE PER UNIT, and for every commit it needs that
# commit's subject. Its own header says the cache is not an optimisation a caller may drop, and
# prices the sibling leg at 591 s cached against 3977-5401 s uncached. This leg declared no `_SUBJ`
# at all - `grep -c _SUBJ` returned ZERO - so every unit paid a `git log -1` plus a `tr` on every
# commit in range. Measured at main tip d499258d: 1760 s against a 900 s ceiling, ALREADY RED before
# this build merged anything, and rising with each landed unit.
#
# This is the sibling's block, ported rather than re-derived, INCLUDING its size assertion. That
# assertion is the load-bearing half: a read loop that truncates leaves a cache answering "no such
# commit" for every id, every unit grades unbuilt-in-range, and the leg exits 0 - a silent green of
# exactly the shape this kit refuses. Equality is exact because shas are unique.
declare -A _SUBJ=()
while IFS= read -r _cl; do
  _SUBJ[${_cl%% *}]=" ${_cl#* } "
done < <(GIT log --format='%H %s' HEAD 2>/dev/null | tr -c 'A-Za-z0-9\n-' ' ')
_n_hist=$(GIT rev-list --count HEAD 2>/dev/null)
case "$_n_hist" in ''|*[!0-9]*) _n_hist=-1 ;; esac
if [ "${#_SUBJ[@]}" -ne "$_n_hist" ]; then
  echo "brief-recorded: the subject cache holds ${#_SUBJ[@]} commit(s) where history has $_n_hist, so the build-commit walk below would miss commits and report every unit unbuilt-in-range - which is a clean bill this leg has not earned"
  exit 2
fi

graded=0; skipped_cutoff=0; nobase=0; unbuilt=0; postrun=0; unborne=0; regraded=0
violations=""; announced=""

# THE POPULATION COMES FROM THE GRADED COMMIT, selector included. `git ls-files` enumerates the INDEX,
# so one `git rm --cached` of a build README - staged, nothing committed - would drop that whole build
# from grading, and doing it across the tree would silence the leg while it reported a clean bill.
# The sibling met that as a closing-review blocker; this leg is written past it rather than into it.
for readme in $(GIT ls-tree -r --name-only HEAD -- "$MEMORY_ROOT/builds" 2>/dev/null | grep -E "/README\.md$"); do
  bdir=${readme%/README.md}
  slug=${bdir##*/}
  opened=$(GIT show "HEAD:$readme" 2>/dev/null | sed -n 's/^opened:[[:space:]]*//p' | head -1)
  case "$opened" in [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;; *) skipped_cutoff=$((skipped_cutoff+1)); continue ;; esac
  # `sort -C` over the pair is the same date comparison every sibling cutoff uses; a build opened
  # BEFORE the cutoff keeps the grandfathering.
  if ! printf '%s\n%s\n' "$BRIEF_RECORDED_CUTOFF" "$opened" | sort -C; then
    skipped_cutoff=$((skipped_cutoff+1)); continue
  fi

  # THE RANGE IS THE RUN'S PINNED BASE, and a build without one is COUNTED rather than graded. The
  # sibling leg falls back to the build folder's own first commit; this leg deliberately does not,
  # because the brief row lives in the run-state file and a build with no readable run-state file has
  # no run-state file to carry one. Announcing that population is the whole of the answer: a build
  # that cannot be graded and a build that graded clean must not print the same thing.
  run="$bdir/RUN.md"
  base=""
  _runblob=$(GIT show "HEAD:$run" 2>/dev/null || true)
  if [ -n "$_runblob" ]; then
    base=$(printf '%s\n' "$_runblob" | sed -n 's/^base:[[:space:]]*//p' | head -1)
    case "$base" in
      [0-9a-f][0-9a-f][0-9a-f][0-9a-f]*) GIT cat-file -e "$base^{commit}" 2>/dev/null || base="" ;;
      *) base="" ;;
    esac
  fi
  if [ -z "$base" ]; then nobase=$((nobase+1)); continue; fi
  # The claim HEAD's own record makes, read once per build from the blob already in hand.
  _head_claim=$(printf '%s\n' "$_runblob" | awk "$CLAIM_AWK")

  # The CLOSED units, from the generated region at the graded commit. A row's id is spelled twice, so
  # `match` takes the first occurrence per row rather than a `grep -o` that would emit each unit twice.
  ids=$(GIT show "HEAD:$readme" 2>/dev/null | awk -v s="$slug" '
      /<!-- gen:build-units -->/ { inr=1; next }
      /<!-- \/gen:build-units -->/ { inr=0 }
      inr && / CLOSED / { if (match($0, "[A-Z]+-" s "-[0-9]+")) print substr($0, RSTART, RLENGTH) }' | sort -u)

  for id in $ids; do
    graded=$((graded+1))
    # STEP 1 - the BUILD commit, through the kit library's `build_commit`, which is the sibling leg's
    # own selection rather than a second copy of it. A copy would be two answers to one question, and
    # this half is the one that has already been wrong twice: its exclusion set made a CONFORMING run
    # unlandable, twice over. The default window is the in-range `--reverse` walk.
    build_c=$(build_commit "$base..HEAD" "$id" "$bdir" "$GENERATED_INDEXES" "$SHARED_RECORDS")
    if [ -z "$build_c" ]; then unbuilt=$((unbuilt+1)); continue; fi

    # TERM 1 - the run-state blob AT THAT COMMIT carries a row for this unit. Matched on the whole
    # field including both separators, which makes the id a whole token by construction: without the
    # trailing ` · reason ` an id is a prefix of nine others every build with ten units will mint.
    _sb=$(GIT show "$build_c:$run" 2>/dev/null || true)

    # TERM 0 - WAS A RUN LIVE WHEN THIS UNIT WAS BUILT. The header's section on units built during a
    # run is the argument; this is the mechanism. The phase is one token or it is not terminal, so a
    # value carrying a space cannot match two members of the set at once.
    _claim=$(printf '%s\n' "$_sb" | awk "$CLAIM_AWK")
    _ph=${_claim#*$'\n'}; _ph=${_ph%%$'\n'*}
    _fin=0
    case "$_ph" in
      ''|*[!A-Z]*) ;;
      *) case " $TERMINAL_PHASES " in *" $_ph "*) _fin=1 ;; esac ;;
    esac
    # THE PICK IS CHECKED BEFORE IT BUYS A SKIP. The header's section on a wrongly picked build commit
    # is the argument. Every later commit that `build_commit`'s own predicate accepts for this id is
    # asked the same phase question, the subject cache filtering first so the predicate runs only on a
    # commit that names the id. The first one made while a run was live is where the unit is graded.
    if [ "$_fin" = 1 ]; then
      _live_c=""; _live_ph=""
      for _lc in $(GIT rev-list --reverse "$build_c..HEAD" 2>/dev/null); do
        case "${_SUBJ[$_lc]-}" in ''|*" $id "*) ;; *) continue ;; esac
        [ -n "$(build_commit "$_lc^!" "$id" "$bdir" "$GENERATED_INDEXES" "$SHARED_RECORDS")" ] || continue
        _lph=$(GIT show "$_lc:$run" 2>/dev/null | awk "$CLAIM_AWK")
        _lph=${_lph#*$'\n'}; _lph=${_lph%%$'\n'*}
        case "$_lph" in ''|*[!A-Z]*) ;; *) case " $TERMINAL_PHASES " in *" $_lph "*) continue ;; esac ;; esac
        _live_c=$_lc; _live_ph=$_lph; break
      done
      if [ -n "$_live_c" ]; then
        regraded=$((regraded+1))
        announced="$announced
brief-recorded: GRADED AT A LATER COMMIT — $id: the earliest commit naming it, $(GIT rev-parse --short "$build_c"), was made while $run read $_ph, but $(GIT rev-parse --short "$_live_c") also names it and touches a path outside the record surface while $run read ${_live_ph:-no phase}, so the unit was worked on during a live run and is graded there"
        build_c=$_live_c
        _sb=$(GIT show "$build_c:$run" 2>/dev/null || true)
        _fin=0
      fi
    fi
    if [ "$_fin" = 1 ]; then
      # WHO STILL MAKES THIS CLAIM AT HEAD: the run-state file itself, or a retired record that was
      # not yet retired at the build commit. The name is shape-checked against the one grammar the
      # driver writes, `RUN.<phase>.<8hex>.md`, and never against its own blob: a migrated retired
      # record keeps its name and changes its bytes, so that equality is already false in this tree.
      _stands=""
      if [ "$_claim" = "$_head_claim" ]; then
        _stands="$run"
      else
        for _ar in $(GIT ls-tree --name-only HEAD -- "$bdir/" 2>/dev/null); do
          _an=${_ar#"$bdir/"}
          case "$_an" in RUN.*.md) ;; *) continue ;; esac
          _am=${_an#RUN.}; _am=${_am%.md}
          case "${_am%.*}" in ''|*[!A-Z]*) continue ;; esac
          case "${_am##*.}" in [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]) ;; *) continue ;; esac
          [ -z "$(GIT ls-tree "$build_c" -- "$_ar" 2>/dev/null)" ] || continue
          [ "$(GIT show "HEAD:$_ar" 2>/dev/null | awk "$CLAIM_AWK")" = "$_claim" ] || continue
          _stands="$_ar"; break
        done
      fi
      if [ -n "$_stands" ]; then
        postrun=$((postrun+1))
        announced="$announced
brief-recorded: NOT GRADED — $id was BUILT at $(GIT rev-parse --short "$build_c") while $run read $_ph, so its run had already finished and the unit was built outside any run; $_stands still makes that claim at HEAD"
        continue
      fi
      unborne=$((unborne+1))
      announced="$announced
brief-recorded: GRADED ANYWAY — $id was BUILT at $(GIT rev-parse --short "$build_c") while $run read $_ph, but no record at HEAD still makes that claim, neither $run nor one retired after that commit, so the finished run is not taken on its word"
    fi

    _rows=$(printf '%s\n' "$_sb" | grep -F " brief · item $id · reason " || true)
    if [ -z "$_rows" ]; then
      violations="$violations
  $id — BUILT at $(GIT rev-parse --short "$build_c") with NO brief row in $run at that commit; nothing on disk records what the agent that built it was handed"
      continue
    fi
    # TERM 2 - the LAST row wins, and the writer is why it can. A unit can be re-briefed and the
    # corpus does it: three units carry two or three rows each, naming ONE path with different hashes.
    # A universal reading over rows reds all three, because the earlier hashes no longer describe the
    # file; a bare existential lets a stale row satisfy this term forever after an edit. `verb_brief`
    # compares the WHOLE line before writing and returns without writing when it is unchanged, so a
    # new row exists only when the hash CHANGED - which makes the last row the newest hash, which is
    # the file the builder was handed.
    _row=$(printf '%s\n' "$_rows" | tail -1)
    _rest=${_row#* · reason }
    _hash=${_rest%% *}
    _path=${_rest#* }
    # THE HASH IS SHAPE-CHECKED BEFORE IT IS COMPARED, because the comparison below is a PREFIX
    # match and an EMPTY hash is a prefix of every blob in the repository. What stops that today is
    # NOT this leg: `git ls-tree <commit> -- ""` REFUSES an empty pathspec — measured, it prints
    # `fatal: empty string is not a valid pathspec` — so the empty row currently reds one branch
    # further down, on the path rather than on the hash. That is protection this file does not own
    # and did not ask for. Stated rather than claimed: this guard did not close an open green, it
    # moved the refusal onto the term that is actually wrong and off a neighbouring tool's error
    # message. The arm for it in `check-brief-recorded.test.sh` says the same thing.
    case "$_hash" in
      [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]) ;;
      *) violations="$violations
  $id — its brief row at $(GIT rev-parse --short "$build_c") carries no twelve-hex hash in its reason field, so the join it claims to record cannot be made and a prefix comparison against it would match every blob in the repository: [$_rest]"
         continue ;;
    esac
    # `ls-tree` AND NOT `rev-parse <commit>:<path>`: the latter is mangled by POSIX-emulation shells
    # on Windows for a path with a leading dot segment and reports ABSENT rather than failing, which
    # is a wrong verdict wearing a clean one's clothes (memory/gotchas/msys-mangles-rev-colon-dotpath).
    _blob=$(GIT ls-tree "$build_c" -- "$_path" 2>/dev/null | awk '$2 == "blob" { print $3 }' | head -1)
    if [ -z "$_blob" ]; then
      violations="$violations
  $id — its brief row at $(GIT rev-parse --short "$build_c") names $_path, which is not a tracked file at that commit, so the row records that a brief existed and joins to nothing"
      continue
    fi
    case "$_blob" in
      "$_hash"*) ;;
      *) violations="$violations
  $id — its brief row at $(GIT rev-parse --short "$build_c") carries hash $_hash for $_path, but that path's blob at the same commit is $_blob; the file moved under the row and no re-brief recorded it" ;;
    esac
  done
done

# ------------------------------------------------------------------------------- THE LIVENESS LINE
# ONE COUNT PER POPULATION THIS LEG WALKS. Do not write the number of them here: the line is two
# inches below and cannot go stale, and the sibling's comment saying "THREE COUNTS" above a line
# printing four is what taught this file not to.
#
# DO NOT READ A NON-ZERO `unbuilt-in-range` AS BENIGN. It is the ordinary shape for a resumed build,
# and it is ALSO what a widened exclusion set looks like - every commit falls inside the excluded
# surface, no build commit is found, and the leg reports a clean bill with a count a reader has been
# taught to ignore. `graded` minus `unbuilt-in-range` is the count that proves term 1 ran at all.
#
# THE EXCLUSION SET IS PRINTED, and that is not decoration. It is composed from two conf keys the
# GRADED RUN can commit, so widening `GENERATED_INDEXES` turns a real violation green and the only
# other trace is the count above. Naming the set makes a widened one visible in the one line an
# operator actually reads. It does not PREVENT the widening - the conf is inside the run's reach and
# protocol section 1 cost 2 concedes that - so what this buys is a trace, not a guard, and saying
# which is the point.
#
# THE THREE POST-RUN COUNTS ARE SUBSETS OF `graded`, like `unbuilt-in-range`. The first is the population
# this leg does NOT grade, and a skip must announce itself: every such unit also gets its own line below
# naming it, the commit and the phase. The second is graded as though its run were live, and it is
# counted because a terminal claim HEAD does not bear out is either a hand edit or a forgery, and both
# are worth a reader's eye whether or not the unit also carries a brief. The third is graded at a later
# commit than the one `build_commit` picked, and it is counted because each is a pick the library got
# wrong, which the sibling leg still trusts.
echo "brief-recorded: graded $graded closed unit(s) · $skipped_cutoff build(s) skipped by the $BRIEF_RECORDED_CUTOFF cutoff · $nobase build(s) with no pinned run BASE · $unbuilt unit(s) unbuilt-in-range · $postrun unit(s) built after their run finished, not graded · $unborne unit(s) built under a finished claim HEAD does not bear out, graded · $regraded unit(s) whose earliest commit fell after their run finished and a later one inside a live run, graded at the later"
echo "brief-recorded: the record surface excluded from build-commit selection was: <build folder> $(printf '%s ' $GENERATED_INDEXES $SHARED_RECORDS)"
if [ -n "$announced" ]; then
  printf '%s\n' "${announced#?}"
fi

if [ -n "$violations" ]; then
  echo "brief-recorded FAILED — a CLOSED unit's build commit records no usable brief:$violations"
  exit 1
fi
exit 0
