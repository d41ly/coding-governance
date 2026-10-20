# Phase 0 builder brief: P0.1 and P0.2 from the revised text, and the bare-id predicate's opened mode

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 241 renders from this brief record through `handoff.py render --role gov-builder`, with this
file as its `input:spec`. Dispatch 234 built P0.6 and handed P0.1 and P0.2 back. Dispatch 238 verified its findings
and wrote the revised text and a build order, `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-revision.md`. The
owner then answered, verbatim (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md` `[phase0-answers]`): "Apply
all 13 (Recommended)", "List it first (Recommended)" and "Rows name the ids (Recommended)".

## The prompt

Build the revision record's `[builder]` section in its order: P0.1's rows for `deviations.py` and `asbuilt.py`, P0.2's
departures report, and finding 11's `--opened` mode of the bare-id predicate. The revision record, read with the
owner's three answers, is the spec for this unit; the execution plan's `[phase-0]` is being revised to the same text
in parallel by another dispatch.

## The brief

### Goal

`build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py`, `build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py` and
`build/2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py` carry every fix the revision record's `[builder]` section
assigns them, each seen red on its plant before its green, with finding 7 as "listed first" and finding 9 as "rows
name the ids": the approver arm holds no decision id, it looks the cited id up in `memory/DECISIONS.md`.

### Items

1. Every acceptance item of the revision record's `[builder]` section, in its order, with its command. Its plant
   names are proposals: keep or rename them, and record the final names.
2. Finding 11: `bare-ids.py --opened`, as the revision record's revised P0.7 text states it, with its red test (a bare
   chain id of an opened build planted in a record prints one line). The plain mode keeps its P0.6 verdicts.
3. Row 10's report half: every `deviations.py --report` prints each instrument's blob hash, as the revision record
   says.
4. The two population arms, `--policy report|refuse`, the departures report's sources, range, marks, ordering, names,
   byte compare and validating arm, and every P0.2 red test, as the revised text states them.

### Acceptance

- Every plant of the `[builder]` section exits as its item says, each seen on the old code first where the item names
  a before.
- On today's tree: `deviations.py` exits 0 with 0 members, `asbuilt.py --check` exits 0, and `bare-ids.py` exits 0
  printing nothing.
- `--fixture` lists each population plant, the two further arms' included.
- Append a `## P0.1 and P0.2` section to `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-deviations-instruments.md`
  listing every command you ran for a plant or a red test, in order, with its exit and the line that proves it,
  before and after each fix.

### Gates

None of the bar's legs, no suite and no kit self-test. Run each instrument's own modes and the naming lexicon
(`python tools/lexicon/lexicon.py --suggest <name> --as <cell>`) before naming a new function. The pre-commit hook
still fires on your commits; give each commit a 600000 ms timeout.

### Non-goals

- Your tree: a `git clone --shared` of `C:/projects/coding-governance/.claude/worktrees/unruffled-aryabhata-d89ede` at
  its branch `branch/unruffled-aryabhata-d89ede`, made under your scratch folder, with a linked worktree on a branch
  `p0-deviations-2` for your commits (the pre-commit isolate check refuses a feature-branch commit in a primary tree).
  The main loop fetches that branch when you return; name its tip in your return.
- No file outside `memory/builds/dClosedLoop/build/` but the `memory/builds/dClosedLoop/README.md` and
  `memory/LIVE.md` renders `gen_build_index.py --write` makes, which the pre-commit's hygiene check 9 requires.
- No change to `carries.py`, `packet.py`, `open.py`, the schedule script, the execution plan, v2 or any record but
  your instruments record.
- No product code, no chain build's folder, no decision row.
- No merge, no push, no rebase.
- Write Python to files, never through a heredoc. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Scratch work goes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d241/` only; never delete anything outside it.
