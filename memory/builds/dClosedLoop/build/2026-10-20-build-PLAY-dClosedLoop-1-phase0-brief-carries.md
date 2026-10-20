# Phase 0 builder brief: the carries join hardened

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 235 renders its goal, items, acceptance, gates and non-goals from this brief record, through
`handoff.py render --role gov-builder --input prompt=<this file>`. Phase 0 is the unit's remaining work, S4 of
`spec/2026-10-20-spec-PLAY-dClosedLoop-1.md`, and the owner approved it (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`
`[walk]`, `[handoff]`).

## The prompt

Build P0.1's two rows whose fix lives in `carries.py`, rows 1 and 2 of the table in
`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]`. The plan is the spec for this unit: follow
it as written.

## The brief

### Goal

`build/2026-10-19-build-PLAY-dClosedLoop-1-carries.py` no longer counts a clause another build's spec carries as
carried for its owner (unless a `**Moved:** … to <this build> by <decision>` line names it), and no longer lets a
dropped clause escape after a later edit, because the drop arm compares against every revision of the spec since its
first commit. Each fix is seen red on its plant first.

### Items

1. Row 1, `crossbuild`: the plant reds after the fix and is green before it.
2. Row 2, `drop` then `typo`: red after the fix.
3. Each plant is ported into the instrument's own `--fixture --plant <name>` from IR:754-838 (IR is
   `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-instruments.md`). Existing plants keep their verdicts,
   compared before and after.

### Acceptance

- Both plants exit as their rows say, each seen on the old code first.
- On today's tree `carries.py` exits 2 (no spec measured), as before.
- `carries.py --report <slug>` keeps its current interface: another unit's departures report calls it as a
  subprocess.
- A record `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-carries-instruments.md` (first line
  `**Serves:** research PLAY-dClosedLoop-1`) lists every command you ran for a plant, in order, with its exit code and
  the line that proves it, before and after each fix. Commit it.

### Gates

None of the bar's legs, no suite and no kit self-test. Run the instrument's own `--fixture` and `--plant` modes and
the naming lexicon (`python tools/lexicon/lexicon.py --suggest <name> --as <cell>`) before naming a new function. The
pre-commit hook still fires on your commits; give each commit a 600000 ms timeout.

### Non-goals

- Your tree is the worktree `C:/projects/coding-governance/.claude/worktrees/p0-carries`, on branch `branch/p0-carries`, cut from the main loop's branch with this brief committed. Run every command there (`git -C` with that forward-slash path, or `cd` into it first) and commit only there. This brief is your spec input: read it there whole, then the plan sections it names.
- No file but `carries.py` and the record above. In particular not `deviations.py`, `asbuilt.py` or any record that
  holds a bare dTrueNorth id: another unit owns those in parallel.
- No change to v2, the execution plan or any other record. No product code, no chain build's folder, no decision row.
- An id in a fixture string that names a dTrueNorth unit or a dClosedLoop decision not yet minted is written in the
  `missing:` form, so the build-index generator joins nothing.
- No merge, no push, no rebase onto another branch.
- Write Python to files, never through a heredoc. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Scratch work goes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d235/` only; never delete anything outside it.
