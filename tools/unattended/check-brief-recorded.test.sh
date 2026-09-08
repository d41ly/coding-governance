#!/usr/bin/env bash
# check-brief-recorded.test.sh - arms for the brief-recorded history leg. TOOL-aHoistedPass-7.
#
# EVERY ARM DRIVES A REAL FIXTURE REPOSITORY with real commits, because the whole subject of the leg
# is what a COMMIT carries and a fixture that fakes the history proves nothing about a check that
# reads it. The arms that matter are a matched pair: the same build, once with the brief row at the
# build commit and once without. An arm for the refusal alone would not distinguish a leg that reds
# correctly from one that reds on everything.
#
# THESE ARMS CARRY THE WHOLE EVIDENTIAL WEIGHT OF THE LEG, and that is a deliberate trade rather than
# an accident. `BRIEF_RECORDED_CUTOFF` is dated at the landing, so the leg grades ZERO units on the
# day it lands: every build that carries brief rows opened before that date, and five units among
# them carry no row at all, so any cutoff old enough to grade the conforming ones is old enough to
# make the leg unlandable. The bar therefore cannot fail because of this leg until the first
# unattended run lands after the cutoff. Three of the arms below are staged failures observed RED
# before the leg landed; they are what stands in for a population.
#
# NO KIT_REL SWEEP IN THIS FILE, DELIBERATELY, and the sibling suite's header says why at length:
# every path below is INSIDE the fixture tree this suite builds with `mkdir -p tools/unattended`, so
# `tools/` here is the FIXTURE's own layout and not gov's install prefix. Sweeping it to a derived
# prefix broke 14 of 19 arms in the sibling, because the `.unattended.conf` heredoc is QUOTED.
set -u
st=0; n=0
LEG="tools/unattended/check-brief-recorded.sh"
KIT="$(cd "$(dirname "$0")" && pwd)"
[ -f "$KIT/check-brief-recorded.sh" ] || { echo "FAIL cannot find check-brief-recorded.sh beside this test"; exit 2; }

same() { n=$((n+1)); if [ "$2" = "$3" ]; then echo "ok   $1"; else echo "FAIL $1 -- got '$2' want '$3'"; st=1; fi }
has()  { n=$((n+1)); case "$2" in *"$3"*) echo "ok   $1" ;; *) echo "FAIL $1 -- output did not carry '$3'"; st=1 ;; esac }
hasnt(){ n=$((n+1)); case "$2" in *"$3"*) echo "FAIL $1 -- output carried '$3' and must not"; st=1 ;; *) echo "ok   $1" ;; esac }

# ---------------------------------------------------------------------------------------------
# THE FIXTURE. One build, one CLOSED unit, one build commit. What varies is the brief row that
# commit carries. The build commit must touch a path OUTSIDE the build folder, the generated indexes
# and the shared records, or `build_commit` correctly declines to call it a build commit at all --
# `tools/product.sh` is that path, and dropping it would make every arm below pass vacuously.
mkfixture() { # mode -> prints the fixture root
  local mode="$1" T
  T=$(mktemp -d) || exit 2
  ( cd "$T" || exit 2
    git init -q .
    git config user.email t@t; git config user.name t; git config commit.gpgsign false
    mkdir -p tools/unattended memory/builds/tBrief/spec memory/builds/tBrief/prompts
    cp "$KIT/lib-unattended.sh" tools/unattended/
    cp "$KIT/unattended.sh"     tools/unattended/
    cp "$KIT/check-brief-recorded.sh" tools/unattended/
    cat > .unattended.conf <<'CONF'
MEMORY_ROOT=memory
BRIEF_RECORDED_CUTOFF="2026-01-01"
GENERATED_INDEXES="memory/LIVE.md:tools/memory-tree/gen_build_index.py"
SHARED_RECORDS="memory/DECISIONS.md memory/backlog"
CONF
    cat > memory/builds/tBrief/README.md <<'RM'
---
slug: tBrief
node: t
opened: 2026-06-01
streams: tooling
roster: ARCH
ids: ARCH-tBrief-1
---
# tBrief
<!-- gen:build-index -->
<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [ARCH-tBrief-1 — the unit](spec/one.md) | 1 | 2 | CLOSED | rev-1 | 2026-06-01 |
<!-- /gen:build-units -->
<!-- /gen:build-index -->
RM
    git add -A >/dev/null; git commit -q -m "fixture base" --no-verify
    BASE=$(git rev-parse HEAD)
    printf '# tBrief — run state\n<!-- run:generated -->\n<!-- /run:generated -->\n## Run facts\nbase: %s\n## Parked\n' "$BASE" > memory/builds/tBrief/RUN.md
    git add -A >/dev/null; git commit -q -m "run state" --no-verify

    # THE BUILD PASS. The brief file is written and hashed, then the row is appended to the run-state
    # file, then the product lands -- all in ONE commit, because `--brief` STAGES its row rather than
    # committing it. That is the whole reason this leg anchors on the build commit and not on its
    # first parent.
    printf 'the brief the builder was handed\n' > memory/builds/tBrief/prompts/brief.md
    H=$(git hash-object memory/builds/tBrief/prompts/brief.md | cut -c1-12)
    case "$mode" in
      norow) ;;   # AC1's staged break: the pass records nothing about what it was handed.
      untracked)
        printf '\n2026-06-02T00:00:00Z brief · item ARCH-tBrief-1 · reason %s memory/builds/tBrief/prompts/gone.md\n' "$H" >> memory/builds/tBrief/RUN.md ;;
      emptyreason)
        # THE VACUOUS SELECTOR. The hash comparison is a PREFIX match, so an empty hash is a prefix
        # of every blob there is. Measured with the shape guard staged AWAY, this fixture still reds
        # -- `git ls-tree <commit> -- ""` REFUSES an empty pathspec -- so what the guard buys is that
        # the leg refuses on the term that is wrong instead of inheriting a refusal from git's
        # pathspec parser. The arm asserts the MESSAGE for that reason, and the message is what
        # failed when the guard was removed.
        printf '\n2026-06-02T00:00:00Z brief · item ARCH-tBrief-1 · reason \n' >> memory/builds/tBrief/RUN.md ;;
      dirpath)
        # The row names a DIRECTORY rather than a file. `ls-tree` answers with a TREE sha, which is a
        # perfectly good hex string for a prefix comparison to succeed against by luck. Measured with
        # the type filter staged away, this fixture reds anyway, because that particular tree sha does
        # not happen to share twelve hex with the brief's blob -- which is luck, not a check, and
        # filtering on the entry type is what makes the answer mean "the brief FILE".
        printf '\n2026-06-02T00:00:00Z brief · item ARCH-tBrief-1 · reason %s memory/builds/tBrief/prompts\n' "$H" >> memory/builds/tBrief/RUN.md ;;
      stale)
        # AC3's staged break: the brief is EDITED inside the same commit after the row was written,
        # so the row's twelve hex no longer describe the file it names. No unit in real history
        # exercises this -- measured, all 26 rows join -- which is why it is staged.
        printf '\n2026-06-02T00:00:00Z brief · item ARCH-tBrief-1 · reason %s memory/builds/tBrief/prompts/brief.md\n' "$H" >> memory/builds/tBrief/RUN.md
        printf 'a DIFFERENT brief, swapped under the row\n' > memory/builds/tBrief/prompts/brief.md ;;
      rebrief)
        # THE LAST ROW WINS. An earlier row carrying a dead hash must not red the unit, and must not
        # satisfy it either: the corpus re-briefs, and three real units carry two or three rows each.
        printf '\n2026-06-02T00:00:00Z brief · item ARCH-tBrief-1 · reason 000000000000 memory/builds/tBrief/prompts/brief.md\n' >> memory/builds/tBrief/RUN.md
        printf '\n2026-06-02T01:00:00Z brief · item ARCH-tBrief-1 · reason %s memory/builds/tBrief/prompts/brief.md\n' "$H" >> memory/builds/tBrief/RUN.md ;;
      stale-last)
        # The same two rows in the OTHER order, which is what a bare existential would pass. The
        # newest row is the dead one, and it must RED.
        printf '\n2026-06-02T00:00:00Z brief · item ARCH-tBrief-1 · reason %s memory/builds/tBrief/prompts/brief.md\n' "$H" >> memory/builds/tBrief/RUN.md
        printf '\n2026-06-02T01:00:00Z brief · item ARCH-tBrief-1 · reason 000000000000 memory/builds/tBrief/prompts/brief.md\n' >> memory/builds/tBrief/RUN.md ;;
      *)
        printf '\n2026-06-02T00:00:00Z brief · item ARCH-tBrief-1 · reason %s memory/builds/tBrief/prompts/brief.md\n' "$H" >> memory/builds/tBrief/RUN.md ;;
    esac
    printf 'the product\n' > tools/product.sh
    printf 'regenerated index\n' > memory/LIVE.md
    git add -A >/dev/null; git commit -q -m "ARCH-tBrief-1: build the thing" --no-verify
  ) >/dev/null 2>&1
  printf '%s' "$T"
}

# ---- AC1, THE PASSING CASE FIRST. A refusal with no observed passing case is a gate that cannot be
# ---- satisfied, and it is the arm most often missing.
T=$(mkfixture ok)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "brief recorded at the build commit: the leg is green" "$rc" "0"
has  "brief recorded: the unit was GRADED, not skipped" "$o" "graded 1 closed unit"
hasnt "brief recorded: nothing is reported as a violation" "$o" "FAILED"
rm -rf "$T"

# ---- AC1, THE FAILING CASE, OBSERVED. This is the arm the whole leg exists for, and until it has
# ---- been seen RED the leg is an assertion about nothing.
T=$(mkfixture norow)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "no brief row at the build commit: the leg REDS" "$rc" "1"
has  "no brief row: the message names the unit" "$o" "ARCH-tBrief-1"
has  "no brief row: the message names the build commit" "$o" "BUILT at"
has  "no brief row: the unit was graded, not skipped" "$o" "graded 1 closed unit"
rm -rf "$T"

# ---- AC3: the brief was EDITED inside the build commit and no re-brief row recorded it. Staged,
# ---- because no unit in real history exercises it -- all 26 tracked rows join their blobs.
T=$(mkfixture stale)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "hash no longer joins: the leg REDS" "$rc" "1"
has  "stale hash: the ROW's twelve hex are named" "$o" "carries hash"
has  "stale hash: the BLOB's id is named beside it" "$o" "blob at the same commit is"
rm -rf "$T"

# ---- The row names a path that is not tracked at that commit. A row recording that a brief existed
# ---- and joining to nothing is the same defect one step earlier.
T=$(mkfixture untracked)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "row names an untracked path: the leg REDS" "$rc" "1"
has  "untracked path: the message says it joins to nothing" "$o" "joins to nothing"
rm -rf "$T"

# ---- THE VACUOUS SELECTOR, both shapes, and what these two arms actually demonstrate is stated
# ---- rather than assumed. Both fixtures were run against the leg with its guards STAGED AWAY: both
# ---- still redded, one because git refuses an empty pathspec and one because a tree sha happened not
# ---- to share twelve hex with a blob. So neither guard closed an open green. What they buy is that
# ---- the refusal comes from the term that is wrong, on this leg's own message, instead of from a
# ---- neighbouring tool's error and a coincidence -- which is why the message assertion below is the
# ---- one that failed when the guard was removed, and the exit-status assertion was not.
T=$(mkfixture emptyreason)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "empty reason field: REDS rather than matching every blob there is" "$rc" "1"
has  "empty reason: the message says what the comparison would have done" "$o" "match every blob"
rm -rf "$T"
T=$(mkfixture dirpath)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "row names a directory: REDS rather than comparing against a tree sha" "$rc" "1"
rm -rf "$T"

# ---- THE QUANTIFIER, both directions, and one arm alone would decide neither. A stale FIRST row must
# ---- not red a re-briefed unit; a stale LAST row must not be rescued by a live earlier one, which is
# ---- exactly what a bare existential would do.
T=$(mkfixture rebrief)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "re-briefed, newest row joins: green" "$rc" "0"
rm -rf "$T"
T=$(mkfixture stale-last)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "re-briefed, newest row is DEAD: REDS rather than being rescued by the older one" "$rc" "1"
rm -rf "$T"

# ---- AC5: the cutoff, both directions. Blank ANNOUNCES rather than passing silently; malformed is a
# ---- REFUSAL, because a cutoff nothing can compare grades every build or none.
T=$(mkfixture norow)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "cutoff control: the fixture REDS before the cutoff is touched" "$rc" "1"
( cd "$T" && sed -i 's/^BRIEF_RECORDED_CUTOFF=.*/BRIEF_RECORDED_CUTOFF=""/' .unattended.conf )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "cutoff BLANK: exits 0 over a tree that would otherwise RED" "$rc" "0"
has  "cutoff BLANK: the skip ANNOUNCES itself and names the key" "$o" "BRIEF_RECORDED_CUTOFF"
( cd "$T" && sed -i 's/^BRIEF_RECORDED_CUTOFF=.*/BRIEF_RECORDED_CUTOFF="last tuesday"/' .unattended.conf )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "cutoff MALFORMED: refuses rather than grading everything or nothing" "$rc" "2"
has  "cutoff MALFORMED: the refusal names the value" "$o" "last tuesday"
# The grandfathering direction: a build OPENED before the cutoff is skipped and COUNTED.
( cd "$T" && sed -i 's/^BRIEF_RECORDED_CUTOFF=.*/BRIEF_RECORDED_CUTOFF="2026-12-01"/' .unattended.conf )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "cutoff AFTER the build opened: grandfathered, exits 0" "$rc" "0"
has  "cutoff AFTER: the skipped build is COUNTED, not silent" "$o" "1 build(s) skipped by the"
rm -rf "$T"

# ---- AC6: THE DEAD PROBE. When the driver no longer spells the row grammar, every unit would red for
# ---- a row nothing can write any more. That is a corpus of false accusations wearing a finding's
# ---- clothes, and the leg must refuse INSTEAD of reporting any of them. Staged on the conforming
# ---- fixture, so the only thing that changed is the grammar.
T=$(mkfixture ok)
( cd "$T" && sed -i 's/brief · item/brief-item/g' tools/unattended/unattended.sh )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "driver grammar gone: exits 2 rather than accusing every unit" "$rc" "2"
has  "driver grammar gone: it says DEAD PROBE" "$o" "DEAD PROBE"
hasnt "driver grammar gone: it printed no violation and no liveness line" "$o" "graded"
rm -rf "$T"

# ---- AC4: THE LIVENESS LINE. Four counts, every one of them present, and `graded` minus
# ---- `unbuilt-in-range` is what proves term 1 actually ran -- `graded` alone increments before the
# ---- build-commit selection, so a unit graded by nothing still counts as graded.
T=$(mkfixture ok)
o=$(cd "$T" && bash "$LEG" 2>&1)
has   "liveness: the graded population is named" "$o" "graded 1 closed unit"
has   "liveness: the cutoff population is named" "$o" "skipped by the"
has   "liveness: the no-BASE population is named" "$o" "with no pinned run BASE"
has   "liveness: the unbuilt population is named" "$o" "0 unit(s) unbuilt-in-range"
has   "liveness: the exclusion set is printed beside the counts" "$o" "the record surface excluded from build-commit selection was"
hasnt "liveness: it never claims a bare 'clean'" "$o" "clean"
rm -rf "$T"

# ---- THE HOSTILE CONF. `$CONF` is a TRACKED file the graded run commits, so a leg that SOURCES it
# ---- lets its own subject end or hijack it. Both shapes were reproduced against the sibling leg
# ---- before its import was hardened: `exit 0` gave rc 0 with zero output, byte-indistinguishable
# ---- from a clean tree, and `trap` was worse -- the leg PRINTED its own FAILED line and exited 0.
# ---- This block was copied from that leg with its allow-list narrowed, so the arms come too.
T=$(mkfixture norow)
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "hostile-conf control: the fixture reds BEFORE the conf is touched" "$rc" "1"
( cd "$T" && printf '\nexit 0\n' >> .unattended.conf )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
n=$((n+1)); [ "$rc" != 0 ] && echo "ok   hostile conf: an appended \`exit 0\` cannot end the leg at 0" || { echo "FAIL an appended exit 0 ended the leg at 0 -- the subject silenced its own gate"; st=1; }
rm -rf "$T"
T=$(mkfixture norow)
( cd "$T" && printf "\ntrap 'exit 0' EXIT\n" >> .unattended.conf )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
n=$((n+1)); [ "$rc" != 0 ] && echo "ok   hostile conf: an appended EXIT trap cannot force rc 0" || { echo "FAIL an appended EXIT trap forced rc 0 -- the worse shape, where the leg prints FAILED and exits green"; st=1; }
# THE VECTOR THE SPLICE MISSED. This leg sets DRIVER above its import, exactly as the sibling does,
# and the sibling's blanket uppercase assignment let one tracked conf line redirect that path.
( cd "$T" && printf '\nDRIVER="tools/unattended/evil.sh"\n' >> .unattended.conf )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
hasnt "hostile conf: DRIVER is not assignable from the conf" "$o" "evil.sh"
rm -rf "$T"

# ---- AN UNCOMMITTED EDIT MUST NOT CHANGE THE VERDICT. Every read in this leg comes from the graded
# ---- commit; the sibling met the working-tree version of this as a closing-review blocker at three
# ---- separate reads, so the class is asserted here rather than inherited on trust.
T=$(mkfixture norow)
( cd "$T" && sed -i 's/ CLOSED / OPEN /' memory/builds/tBrief/README.md \
    && sed -i 's/^opened: .*/opened: 2020-01-01/' memory/builds/tBrief/README.md )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "uncommitted README edits do not exempt the unit" "$rc" "1"
has  "uncommitted README edits: still graded from the commit" "$o" "graded 1 closed unit"
# The INDEX mutation, which a content edit cannot reach: the selector that decides which builds are
# read at all was the sibling's round-2 blocker, and `git rm --cached` is the only staging for it.
( cd "$T" && git checkout -q -- memory/builds/tBrief/README.md && git rm -q --cached memory/builds/tBrief/README.md >/dev/null )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "an UNCOMMITTED index removal does not drop the build" "$rc" "1"
rm -rf "$T"

# ---- A BUILD WITH NO PINNED RUN BASE IS COUNTED, never silently skipped. The brief row lives in the
# ---- run-state file, so a build with no readable one cannot be graded -- and a build that cannot be
# ---- graded must not print what a build that graded clean prints.
T=$(mkfixture ok)
( cd "$T" && sed -i 's/^base: .*/base: not-a-sha/' memory/builds/tBrief/RUN.md \
    && git add -A >/dev/null && git commit -q -m 'break the base' --no-verify )
o=$(cd "$T" && bash "$LEG" 2>&1); rc=$?
same "unusable run BASE: exits 0" "$rc" "0"
has  "unusable run BASE: the build is COUNTED as ungradeable" "$o" "1 build(s) with no pinned run BASE"
has  "unusable run BASE: and nothing was graded" "$o" "graded 0 closed unit"
rm -rf "$T"

# ---- THE SUBJECT CACHE MUST BE COMPLETE, and a truncated one must REFUSE rather than grade.
# ---- TOOL-aQuenchedHarness-13. The cache is what makes this leg affordable: without it every unit
# ---- re-walks the in-range history reading one subject per commit, measured at 1760 s on main tip
# ---- against a 900 s ceiling. With it, 255 s and byte-identical output.
# ---- The DANGEROUS failure is not slowness, it is a cache that reads SHORT: it then answers "no
# ---- such commit" for every id, every unit grades unbuilt-in-range, and the leg exits 0 with a
# ---- clean bill it never earned. The size assertion is what makes that impossible, so it is armed
# ---- here rather than trusted. The break is staged into a COPY of the leg beside a copy of the
# ---- library, because the leg refuses to run without one.
T=$(mkfixture ok)
D="$T/.brk"; mkdir -p "$D"
cp "$LEG" "$KIT/lib-unattended.sh" "$KIT/unattended.sh" "$D/" 2>/dev/null
# `#` as the delimiter, because the thing being inserted IS a pipe. The first spelling used `|`
# and `&`, which re-inserts the match and produced `2>/dev/null head -5 |` - making `head` an
# argument to `git log` rather than a stage after it. The fixture guard below is what catches that.
# TRUNCATE BY EXACTLY ONE COMMIT, not to a fixed count. The first spelling used `head -5`, and the
# fixture's history is shorter than five - so it truncated NOTHING, the cache matched history, the
# leg exited 0 and this arm asserted a refusal that had no reason to happen. `head -n -1` drops the
# last line whatever the length, which is also the sharper test: off-by-one is the realistic way a
# cache reads short, and it must refuse just as loudly as an empty one.
sed -i 's#| tr -c#| head -n -1 | tr -c#' "$D/$(basename "$LEG")"
# THE GUARD ASSERTS THE EFFECT, not the edit. Checking that the text was inserted is what let the
# no-op through: the pipeline was patched and changed nothing. Two commits are what make a
# one-line truncation observable.
_nc=$(cd "$T" && git rev-list --count HEAD 2>/dev/null || echo 0)
n=$((n+1)); [ "${_nc:-0}" -ge 2 ] || { echo "FAIL fixture no-op: history is $_nc commit(s), so dropping one leaves nothing to detect"; st=1; }
o=$(cd "$T" && bash "$D/$(basename "$LEG")" 2>&1); rc=$?
same "a truncated subject cache REFUSES" "$rc" "2"
has  "a truncated subject cache names the shortfall" "$o" "so the build-commit walk below would miss commits and report every unit unbuilt-in-range"
rm -rf "$T"

echo "--- $n arms, exit $st"
exit $st
