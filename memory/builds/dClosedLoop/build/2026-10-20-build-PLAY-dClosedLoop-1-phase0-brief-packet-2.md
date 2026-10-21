# Phase 0 builder brief: the packet instrument on the pinned baseline, and one roster reader

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 243 renders from this brief record through `handoff.py render --role gov-builder`, with this
file as its `input:spec`. Dispatch 241 found two defects outside its paths
(`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-deviations-instruments.md`, section `## P0.1 and P0.2`).

## The prompt

Make `packet.py` read the design baseline from `deviations.BASELINE`, the pin P0.1 row 5 puts in the deviation
instrument, and give the `roster:units` table one reader, before the opening renders any packet.

## The brief

### Goal

`build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py` no longer reads its baseline from v2's working-tree
`Baseline:` line (`packet.py:254-259`): it imports `BASELINE` from
`build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py`, the class P0.1 rows 5 and 5a close. And the `roster:units`
table has one reader: `build/2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py`'s `read_roster_units` is replaced by
`packet.py`'s `read_roster`, or both by one, whichever keeps the other callers unchanged.

### Items

1. The baseline read, with a plant: a v2 whose `Baseline:` line is moved makes the packet render from the pinned sha
   (or refuse, if `packet.py` cannot render without it; say which), where the old code followed the moved line.
2. The roster reader merged, with every existing plant of both instruments keeping its verdict, compared before and
   after, and `bare-ids.py --opened`'s two plants re-run.

### Acceptance

- The plant above seen red on the old code and green after.
- `packet.py --fixture` and every packet plant, and `bare-ids.py` plain and `--opened` with their plants, give the same
  verdicts as before the change.
- Append a `## The pinned baseline and one roster reader` section to
  `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-packet-instruments.md` listing every command, in order, with its
  exit and the line that proves it.

### Gates

None of the bar's legs, no suite and no kit self-test. Run each script's own modes and the naming lexicon before
naming a new function. The pre-commit hook still fires on your commits; give each commit a 600000 ms timeout.

### Non-goals

- Your tree: a `git clone --shared` of `C:/projects/coding-governance/.claude/worktrees/unruffled-aryabhata-d89ede` at
  its branch `branch/unruffled-aryabhata-d89ede`, made under your scratch folder, with a linked worktree on a branch
  `p0-packet-2` for your commits and `core.hooksPath=.githooks` set in the clone so the pre-commit fires. The main
  loop fetches that branch when you return; name its tip in your return.
- No file but `packet.py`, `bare-ids.py`, the record above, and the `memory/builds/dClosedLoop/README.md` and
  `memory/LIVE.md` renders `gen_build_index.py --write` makes.
- No change to `deviations.py`, `carries.py`, `asbuilt.py`, `open.py`, the schedule script, the plan, v2 or any other
  record. No product code, no chain build's folder, no decision row, no merge, no push, no rebase.
- Write Python to files, never through a heredoc. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Scratch work goes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d243/` only; never delete anything outside it.
