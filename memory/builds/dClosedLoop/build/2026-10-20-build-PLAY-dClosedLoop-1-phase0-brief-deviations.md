# Phase 0 builder brief: the bare-id fix, the deviation and as-built instruments hardened, and the departures report

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 234 renders its goal, items, acceptance, gates and non-goals from this brief record, through
`handoff.py render --role gov-builder --input prompt=<this file>`. Phase 0 is the unit's remaining work, S4 of
`spec/2026-10-20-spec-PLAY-dClosedLoop-1.md`, and the owner approved it (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`
`[walk]`, `[handoff]`).

## The prompt

Build P0.6's bare-id fix, then P0.1's rows for `deviations.py` and `asbuilt.py`, then P0.2's departures report, as
`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]` states them. The plan is the spec for this
unit: follow it as written.

## The brief

### Goal

`build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py` and `build/2026-10-19-build-PLAY-dClosedLoop-1-asbuilt.py`
carry every P0.1 fix that names them, each seen red on its plant before its green, and `deviations.py` carries P0.2's
`--report <slug> [--write|--check]` mode with its validating arm and red tests. No tracked file under `memory/` holds
a bare dTrueNorth id that the build-index generator would join.

### Items

1. **P0.6, first.** Run the generator-grammar predicate the plan names (`tree_lib.scan_missing_citations` through
   `gen_build_index.build_roster_id_re` and `extract_roster_ids`, over tracked files under `memory/`, filtered to
   v2's 22 chain slugs). Commit the predicate as `build/2026-10-20-build-PLAY-dClosedLoop-1-bare-ids.py` (exit 1 and
   one line per hit; exit 0 and nothing on a clean tree), since P0.7 re-runs it. Mark every hit `missing:`, in the
   fixture strings and in the verbatim copies alike; the plan counted 25 in 7 files and later records may add more.
   Every instrument's `--fixture` and every `--plant` keeps its verdict, compared before and after. Run P0.6's red
   test in a scratch clone (a `memory/builds/dTrueNorth/README.md` plus `gen_build_index.py --write`, before and after
   the fix; a planted bare id and a planted `x:`-prefixed id each print one line).
2. **P0.1**, every row whose fix lives in `deviations.py` or `asbuilt.py`: rows 3 to 8 and 11, the two further
   population arms, and `--policy report|refuse` (default `report`). Each plant is ported into the instrument's own
   `--fixture --plant <name>` from IR:754-838 (IR is `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-instruments.md`).
   Row 6's approver arm reads the decision ids below. Row 9 is a placement rule: write it into the instrument's
   docstring. Rows 1, 2 and 10 are other units' (`carries.py` and the packet instrument); do not touch `carries.py`.
3. **P0.2**, the departures report, in `deviations.py`, with every source, the run's range `P..HEAD`, the marks, the
   ordering, the file names (`-departures-spec.md` / `-departures-build.md`), the byte compare and the separate
   validating arm, and every red test the plan lists, each planted into the sources or a renderer stub, never into a
   written report. Where the report reads `carries.py --report <slug>`, call it as a subprocess and tolerate its exit
   2 on a build with no spec.

**Decision ids, fixed for Phase 0** (P0.8 mints them under dClosedLoop's slug; the rows themselves are the main
loop's, written after this unit): row 1 `PLAY-dClosedLoop-2`, row 2 (the grant) `PLAY-dClosedLoop-3`, row 3
`PLAY-dClosedLoop-4`, row 4 `PLAY-dClosedLoop-5`, row 5 `PLAY-dClosedLoop-6`, row 6 `PLAY-dClosedLoop-7`, row 7
`PLAY-dClosedLoop-8`, row 8 `PLAY-dClosedLoop-9`, row 9 `PLAY-dClosedLoop-10`. In any instrument string or fixture
they appear in the `missing:` form until the rows land, so the generator joins nothing early.

### Acceptance

- Every P0.1 plant this unit owns exits as its row says, and each fix was seen red on its plant before the fix and
  green after (or, for a false-red row, red before and green after).
- On today's tree: `deviations.py` exits 0 with 0 members and `asbuilt.py --check` exits 0.
- P0.2: `--fixture` lists each population plant of P0.1, the two further arms' included, and every P0.2 red test gives
  the result its line states, each arm-removed control green where the plan names one.
- P0.6: the predicate prints nothing on your tip, and its red test gave the four results the plan names.
- A record `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-deviations-instruments.md` (first line
  `**Serves:** research PLAY-dClosedLoop-1`) lists every command you ran for a plant or a red test, in order, with its
  exit code and the line that proves it, before and after each fix. Commit it.

### Gates

None of the bar's legs, no suite and no kit self-test. Run each instrument's own `--fixture` and `--plant` modes and
the naming lexicon (`python tools/lexicon/lexicon.py --suggest <name> --as <cell>`) before naming a new function. The
pre-commit hook still fires on your commits; give each commit a 600000 ms timeout.

### Non-goals

- Your tree is the worktree `C:/projects/coding-governance/.claude/worktrees/p0-deviations`, on branch `branch/p0-deviations`, cut from the main loop's branch with this brief committed. Run every command there (`git -C` with that forward-slash path, or `cd` into it first) and commit only there. This brief is your spec input: read it there whole, then the plan sections it names.
- No file outside `memory/builds/dClosedLoop/`, except the `missing:` marks P0.6 makes in tracked records under
  `memory/` that hold a hit.
- No change to `carries.py`, the schedule script, v2, the execution plan or any other record's substance.
- No product code (`tools/`, `skills/`, the template, the runbook), no chain build's folder, no decision row.
- No merge, no push, no rebase onto another branch.
- Write Python to files, never through a heredoc. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Scratch work goes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d234/` only; never delete anything outside it.
