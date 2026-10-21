# Phase 0 builder brief: the packet instrument

**Serves:** research PLAY-dClosedLoop-1

The handoff for dispatch 236 renders its goal, items, acceptance, gates and non-goals from this brief record, through
`handoff.py render --role gov-builder --input prompt=<this file>`. Phase 0 is the unit's remaining work, S4 of
`spec/2026-10-20-spec-PLAY-dClosedLoop-1.md`, and the owner approved it (`build/2026-10-20-build-PLAY-dClosedLoop-1-execution.md`
`[walk]`, `[handoff]`).

## The prompt

Build P0.3, the packet instrument, with P0.1 row 10's pin arm, as
`build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]` and `[handoffs]` state them. The plan is the
spec for this unit: follow it as written.

## The brief

### Goal

`build/2026-10-20-build-PLAY-dClosedLoop-1-packet.py` renders one packet per chain build, written as
`memory/builds/<slug>/prompts/<date>-prompt-<first unit>-packet.md`, carrying `## The prompt` and `## The brief` so
`tools/roles/handoff.py render --input prompt=<packet>` reads its `brief:*`. It has `--write`, `--check <slug>` with
its completeness arms and the separate pin arm, and `--repin <instrument>`. It exposes a function the opening script
(a later unit) imports to render every packet at the opening, and it writes no chain build's folder itself in this
unit.

### Items

1. The twelve fields of P0.3, from the handoffs return's probe (IR:197-283; IR is
   `build/2026-10-20-build-PLAY-dClosedLoop-1-research-exec-instruments.md`), `carries.py`'s `design()` and
   `asbuilt.py`'s view. Import from the sibling instruments by path rather than copying their parsers.
2. Field 1's pins cover v2, the as-built view and each instrument: `carries.py`, `deviations.py`, `asbuilt.py`,
   `packet.py` itself, the schedule script, and the opening script `build/2026-10-20-build-PLAY-dClosedLoop-1-open.py`
   once it exists (pin only the tracked ones present at render time).
3. Field 9 reads the opened README's roster when one exists (none does in this unit) and every open ask in
   dClosedLoop's `BACKLOG.md` naming a chain build (none exists yet: the file is absent, which the arm reads as empty,
   never as an error). dTrueNorth's packet carries its extra unit and the decision row it derives from, P0.8 row 1,
   whose id is fixed for Phase 0 as `PLAY-dClosedLoop-2` (written in the `missing:` form until the row lands, so the
   build-index generator joins nothing early).
4. `--check`'s completeness arms, each red on a planted omission; the pin arm, red on a moved blob whatever the byte
   compare says, with the plan's two controls; `--repin` refusing inside a chain run (a live `RUN.md` in the tree).
   Each plant goes into the instrument's own `--fixture --plant <name>`.

### Acceptance

- dTrueNorth's packet reproduces the handoffs return's worked example: six clauses, `cl-dClosedLoop-0001@83b6b117`
  through `cl-dClosedLoop-0006@06ceb3cc`; the node `record-kind.deviation`; the gaps gap-design-13, gap-build-07 and
  gap-mem-47; field 9's extra unit and its decision row.
- In a scratch clone with a minimal `memory/builds/dTrueNorth/README.md` and dTrueNorth's packet written,
  `handoff.py render --build dTrueNorth --unit <a placeholder first unit> --input prompt=<packet>` renders and
  `handoff.py check` is green on the result. Say which placeholder you used; the main loop re-observes this on the
  real opening.
- Every completeness arm and the pin arm seen red on its plant, and the two pin-arm controls green on the same plant.
- A record `build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-packet-instruments.md` (first line
  `**Serves:** research PLAY-dClosedLoop-1`) lists every command you ran for a plant or acceptance check, in order,
  with its exit code and the line that proves it. Commit it with the instrument.

### Gates

None of the bar's legs, no suite and no kit self-test. Run the instrument's own modes and the naming lexicon
(`python tools/lexicon/lexicon.py --suggest <name> --as <cell>`) before naming a new function. The pre-commit hook
still fires on your commits; give each commit a 600000 ms timeout.

### Non-goals

- Your tree is the worktree `C:/projects/coding-governance/.claude/worktrees/p0-packet`, on branch `branch/p0-packet`, cut from the main loop's branch with this brief committed. Run every command there (`git -C` with that forward-slash path, or `cd` into it first) and commit only there. This brief is your spec input: read it there whole, then the plan sections it names.
- No file but `packet.py` and the record above. In particular not `carries.py`, `deviations.py` or `asbuilt.py`,
  which other units change in parallel: if `packet.py` needs a change there, name it in your return.
- No chain build's folder or packet committed, no decision row, no change to v2 or the execution plan, no product
  code.
- No merge, no push, no rebase onto another branch.
- Write Python to files, never through a heredoc. Commits end with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
- Scratch work goes under `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unruffled-aryabhata-d89ede/1cef2554-91c7-4cd1-9950-7f33d1289103/scratchpad/d236/` only; never delete anything outside it.
