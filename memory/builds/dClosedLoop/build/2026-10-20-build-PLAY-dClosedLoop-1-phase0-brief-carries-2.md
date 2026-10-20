# Phase 0 builder brief: the carries token arm and the schedule script's row 9 note

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 242 renders from this brief record through `handoff.py render --role gov-builder`, with this
file as its `input:spec`. The revision record `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-revision.md` confirmed
findings 14 and 15, and the owner answered "Apply all 13 (Recommended)"
(`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md` `[phase0-answers]`).

## The prompt

Build the revision record's recommended fixes for finding 14 (`carries.py`'s token arm and a `**Moved:**` carrier) and
finding 15 (the schedule script's row 9 note). The revision record's two sections are the spec for this unit.

## The brief

### Goal

`build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py` no longer reds a clause's token when a `**Moved:**` line
carries it to another build whose spec holds the token, and
`build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py` prints the "claim absent from that run, left unpinned" note
its docstring promises, so P0.4's row 9 matches.

### Items

1. Finding 14, as the revision record's recommended option states it, with a plant seen red on the old code and
   green after, and every existing `carries.py` plant keeping its verdict.
2. Finding 15, as the revision record states it, with P0.4's row 9 plant re-run before and after: the note absent
   before, printed after, and every other P0.4 row's output unchanged (re-run rows 1 to 13 after the fix and compare
   with `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-schedule-redtests.md`).

### Acceptance

- Both plants exit as above; on today's tree `carries.py` exits 2 and the schedule script's plain run still prints
  makespan 271 and "a and d alone" 273.
- Append a `## Finding 14` section to `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-carries-instruments.md` and a
  `## Finding 15` section to `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-schedule-redtests.md`, each listing
  every command you ran, in order, with its exit and the line that proves it.

### Gates

None of the bar's legs, no suite and no kit self-test. Run each script's own modes and the naming lexicon (`python
tools/lexicon/lexicon.py --suggest <name> --as <cell>`) before naming a new function. The pre-commit hook still fires
on your commits; give each commit a 600000 ms timeout.

### Non-goals

- Your tree: a `git clone --shared` of `C:/projects/coding-governance/.claude/worktrees/unruffled-aryabhata-d89ede` at
  its branch `branch/unruffled-aryabhata-d89ede`, made under your scratch folder, with a linked worktree on a branch
  `p0-carries-2` for your commits (the pre-commit isolate check refuses a feature-branch commit in a primary tree).
  The main loop fetches that branch when you return; name its tip in your return.
- No file but `carries.py`, the schedule script, the two records above, and the `memory/builds/dClosedLoop/README.md`
  and `memory/LIVE.md` renders `gen_build_index.py --write` makes.
- Never run `bash tools/unattended/unattended.sh --claims` or anything that fetches, pushes or writes the real claim
  cache; plant claims in your clone, as dispatch 237 did.
- No product code, no chain build's folder, no decision row, no merge, no push, no rebase.
- Write Python to files, never through a heredoc. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Scratch work goes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d242/` only; never delete anything outside it.
