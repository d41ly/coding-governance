# Phase 0 builder brief: the schedule script's red tests re-run

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 237 renders its goal, items, acceptance, gates and non-goals from this brief record, through
`handoff.py render --role gov-builder --input prompt=<this file>`. Phase 0 is the unit's remaining work, S4 of
`spec/2026-10-20-spec-PLAY-dClosedLoop-1.md`, and the owner approved it (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`
`[walk]`, `[handoff]`).

## The prompt

Re-run P0.4's red tests against `build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py`, as
`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]` P0.4 states them, and record each result.
The plan is the spec for this unit.

## The brief

### Goal

Every row of P0.4's red-test table observed again at this branch's tip, each result compared with the row, and the
plain run's output recorded, so the owner's opening read can trust the script the nodes run at every landing.

### Items

1. A `git clone --shared` scratch clone of this worktree, under your scratch folder. Each plant is made there, never in
   the worktree.
2. Each of the thirteen rows, plus the plain run `python <script> --ref HEAD` on the unplanted clone, and the
   `tree_state` done rule the plan's last paragraph states.
3. Cached claims are planted where the script reads them; read the script's docstring for where that is.

### Acceptance

- A record `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-schedule-redtests.md` (first line
  `**Serves:** research PLAY-dClosedLoop-1`) holds, per row: the plant as made (the exact edit or file written), the
  command, the exit code, the output lines that decide it, and MATCH or DIFFERS against the row. Then the plain run's
  output whole. Commit it.
- Where a row DIFFERS, do not change the script: the record says what differs and why, and your return names it, so
  the main loop raises it with the owner.

### Gates

None of the bar's legs, no suite and no kit self-test. The pre-commit hook still fires on your commit; give it a
600000 ms timeout.

### Non-goals

- Your tree is the worktree `C:/projects/coding-governance/.claude/worktrees/p0-schedule`, on branch `branch/p0-schedule`, cut from the main loop's branch with this brief committed. Run every command there (`git -C` with that forward-slash path, or `cd` into it first) and commit only there. This brief is your spec input: read it there whole, then the plan sections it names.
- No file but the record above. No change to the schedule script, v2, the execution plan or any other record.
- Never run `bash tools/unattended/unattended.sh --claims` against the remote or any command that writes the real
  claim cache, pushes or fetches: plant the cache in the scratch clone instead.
- No merge, no push, no rebase onto another branch.
- Write Python to files, never through a heredoc. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Scratch work goes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d237/` only; never delete anything outside it.
