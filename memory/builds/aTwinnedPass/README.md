---
slug: aTwinnedPass
node: a
opened: 2026-11-15
streams: tooling
roster: TOOL
ids: TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3
authorized-by: prompt
---

# aTwinnedPass — two unit passes of one build at once, each in its own worktree, merged back by the main loop

## The problem this build exists to solve

The unit harness builds every pass in the run's one worktree, so two builders would share one git
index and stage into each other's commits. `--dispatch` also refuses two open passes that both
declare a generated output every pass rewrites. So the method's parallel-when-disjoint rule (M6) is
unreachable, and a 99-unit run builds one unit at a time. Asks `TOOL-dDerivedDocket-55` and `-57`
filed both halves; the prompt is in `prompts/`.

## Expected improvements

- Two disjoint units of one build are built at once, each in its own worktree and branch.
- The main loop merges each pass back `--no-ff` and re-renders the generated outputs once per merge.
- Two passes declaring one generated output are no longer siblings colliding on it.

## Detriments if this is not built

- Every unit waits for the one before it, builder and commit hooks included.
- A run's wall clock grows with its unit count even where the build order marks a group parallel.

## Build-level rules

- **Classification (M2)**: three units, MISSING at open, Tier-2: a changed kit contract (the unit
  harness's args), a new kit tool, and a changed behaviour of `--dispatch`.
- `memory/builds/dDeclaredLoop/`, its run's worktree, its branch and its run-state file are a live
  run's, and are not touched. `pass_commit`, `read_attribution_tokens`, `check_pass_open` and
  `read_open_passes` are left alone, because that run's branch rewrote them.
- No unattended self-test suite while that run is live, beyond the arms this build adds or moves.
- No landing without the owner's explicit ask.
- No spec audit: not declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aTwinnedPass-1` | the unit harness's optional `tree` key: the builder works and commits in the pass's own worktree, and its write set and brief are the main loop's |
| 2 | `TOOL-aTwinnedPass-2` | the pass-tree tool: cut a pass's worktree from the run's tip, and merge it back `--no-ff` with generated outputs re-rendered |
| 3 | `TOOL-aTwinnedPass-3` | `--dispatch` condition 1 leaves a path every pass may share, an effective generated output, out of the sibling overlap |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node a · opened 2026-11-15 · streams tooling
ids TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTwinnedPass-1 — the unit harness builds one pass in a worktree of its own, on a write set the main loop declared](spec/2026-11-15-spec-TOOL-aTwinnedPass-1.md) | 1 | 2 | SPECCED | rev-1 | 2026-11-15 |
| [TOOL-aTwinnedPass-3 — `--dispatch` condition 1 leaves an effective generated output out of the sibling comparison](spec/2026-11-15-spec-TOOL-aTwinnedPass-3.md) | 1 | 2 | SPECCED | rev-1 | 2026-11-15 |
| [TOOL-aTwinnedPass-2 — the pass-tree tool: cut a pass's worktree from the run's tip, and merge it back `--no-ff` with generated outputs re-rendered](spec/2026-11-15-spec-TOOL-aTwinnedPass-2.md) | 2 | 2 | SPECCED | rev-1 | 2026-11-15 |
<!-- /gen:build-units -->

Records: 4 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3.

Ids whose spec moved past its audited revision: none — 0 of 3 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aTwinnedPass-1`, `TOOL-aTwinnedPass-3` | yes |
| 2 | `TOOL-aTwinnedPass-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
