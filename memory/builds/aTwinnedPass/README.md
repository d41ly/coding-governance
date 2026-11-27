---
slug: aTwinnedPass
node: a
opened: 2026-11-15
streams: tooling
roster: TOOL
ids: TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 TOOL-aTwinnedPass-4 TOOL-aTwinnedPass-5 TOOL-aTwinnedPass-6 TOOL-aTwinnedPass-7 TOOL-aTwinnedPass-8 TOOL-aTwinnedPass-9 TOOL-aTwinnedPass-10 TOOL-aTwinnedPass-11 TOOL-aTwinnedPass-12 TOOL-aTwinnedPass-13
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

- **Classification (M2)**: three units, MISSING at open, and two promoted from the closing review's round 1, Tier-2: a changed kit contract (the unit
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
| 1 | `TOOL-aTwinnedPass-1` | the unit harness's optional `passBase` key: the builder runs in the runtime's own worktree reset to that commit, and its write set and brief are the main loop's |
| 2 | `TOOL-aTwinnedPass-2` | the pass-tree tool: merge a pass's branch back `--no-ff` with generated outputs re-rendered, or remove an uncommitted one |
| 3 | `TOOL-aTwinnedPass-3` | `--dispatch` condition 1 leaves a path every pass may share, an effective generated output, out of the sibling overlap |
| 4 | `TOOL-aTwinnedPass-4` | the pass's branch, worktree and fork sha cross every handoff only in the runtime's own spelling (review round 1: H1, H2, M1, M3) |
| 5 | `TOOL-aTwinnedPass-5` | every arm of the build's three suites can go red on the regression it names (review round 1: H3, M2, M4, M5, M6, L1, L2) |
| 11 | `TOOL-aTwinnedPass-11` | the Workflow runtime's worktree spelling, `wf_<run>-<n>`, admitted beside the Agent tool's `agent-<id>` at both ends of the handoff (the measurement's finding) |
| 13 | `TOOL-aTwinnedPass-13` | the reconcile with local main at `a76c6afe7`: its four conflicts resolved so the landing merge is clean (the owner's "merge to local main") |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 7 unit(s) · node a · opened 2026-11-15 · streams tooling
ids TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 TOOL-aTwinnedPass-4 TOOL-aTwinnedPass-5 TOOL-aTwinnedPass-6 TOOL-aTwinnedPass-7 TOOL-aTwinnedPass-8 TOOL-aTwinnedPass-9 TOOL-aTwinnedPass-10 TOOL-aTwinnedPass-11 TOOL-aTwinnedPass-12 TOOL-aTwinnedPass-13

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTwinnedPass-1 — the unit harness builds one pass in a worktree of its own, on a write set the main loop declared](spec/2026-11-15-spec-TOOL-aTwinnedPass-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aTwinnedPass-3 — `--dispatch` condition 1 leaves an effective generated output out of the sibling comparison](spec/2026-11-15-spec-TOOL-aTwinnedPass-3.md) | 1 | 2 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aTwinnedPass-2 — the pass-tree tool: merge a pass's own branch back `--no-ff` with generated outputs re-rendered, or take it away](spec/2026-11-15-spec-TOOL-aTwinnedPass-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aTwinnedPass-4 — a pass's branch, worktree and fork sha cross every handoff only in the runtime's own spelling](spec/2026-11-15-spec-TOOL-aTwinnedPass-4.md) | 3 | 2 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aTwinnedPass-5 — every arm of the build's three suites can go red on the regression it names](spec/2026-11-15-spec-TOOL-aTwinnedPass-5.md) | 4 | 2 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aTwinnedPass-11 — the Workflow runtime's worktree spelling, admitted beside the Agent tool's at both ends of the handoff](spec/2026-11-15-spec-TOOL-aTwinnedPass-11.md) | 5 | 2 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aTwinnedPass-13 — the reconcile with local main at a76c6afe7: its four conflicts resolved so the landing merge is clean](spec/2026-11-15-spec-TOOL-aTwinnedPass-13.md) | 6 | 2 | CLOSED | rev-1 | 2026-11-15 |
<!-- /gen:build-units -->

Records: 40 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aTwinnedPass-1 TOOL-aTwinnedPass-11 TOOL-aTwinnedPass-13 TOOL-aTwinnedPass-2 TOOL-aTwinnedPass-3 TOOL-aTwinnedPass-4 TOOL-aTwinnedPass-5.

Ids whose spec moved past its audited revision: none — 0 of 7 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aTwinnedPass-1`, `TOOL-aTwinnedPass-3` | yes |
| 2 | `TOOL-aTwinnedPass-2` | no |
| 3 | `TOOL-aTwinnedPass-4` | no |
| 4 | `TOOL-aTwinnedPass-5` | no |
| 5 | `TOOL-aTwinnedPass-11` | no |
| 6 | `TOOL-aTwinnedPass-13` | no |

A step's `Parallel` yes means its units share an order; `doc.build-method#m6-passes-commits-parallelism` still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| the units | the units table above |
| briefs | `2026-11-15-prompt-TOOL-aTwinnedPass-5-pass-brief.md`, `2026-11-15-prompt-TOOL-aTwinnedPass-5-2-builder.md` and 27 more under prompts/ |
| reviews | `2026-11-15-review-TOOL-aTwinnedPass-4-5-closing-diff-round2.md` (CLEAN WITH FIXES), `2026-11-15-review-TOOL-aTwinnedPass-11-closing-diff-round3.md` (CLEAN WITH FIXES) and 1 more under reviews/ |
| research | `2026-11-15-build-TOOL-aTwinnedPass-2-measurement.md` |
| logs | `2026-11-15-build-TOOL-aTwinnedPass-5-1-acceptance-ledger.md`, `2026-11-15-build-TOOL-aTwinnedPass-4-1-acceptance-ledger.md` and 5 more under build/ |
| open asks | `BACKLOG.md`, 6 open |
| card ref | `refs/gov/builds/aTwinnedPass/card` |
<!-- /gen:build-routes -->
