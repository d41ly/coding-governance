---
slug: aHomedAnchor
node: a
opened: 2026-10-09
streams: tooling
roster: TOOL
ids: TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2
authorized-by: prompt
---

# aHomedAnchor — an unattended run authorized from local history, with no push to start it

## The problem this build exists to solve

An unattended run is authorized by its build folder only at an anchor the remote observes: the
merge-base with the remote's default branch, or, under `ANCHOR_SCOPE="published"`, the tip the
remote advertises for the run's own branch, which `slug` mode may not use at all. So an owner who
writes a build on a worktree branch, or on local `main`, cannot start `/unattended <slug>` from that
same tree: they must push first, and for `slug` mode they must land the folder on origin's default
branch. The owner's prompt, recorded in `prompts/`, asks that `slug` mode run from the tree that
wrote the build and that no push to origin be required to authorize it. Landing still pushes `main`.

## Expected improvements

- `ANCHOR_SCOPE="local"`: a build folder committed in local history, an ancestor of HEAD,
  authorizes a run in any mode, with no branch push.
- `--hold` and `--scheduled` stop asking for a published branch tip under that scope.
- The bar admits an unpublished BASE only when origin's default branch declares `local`.
- This repository opts in.

## Detriments if this is not built

- Every `slug` run from a worktree or local `main` costs a push, or a landing, before it can start.
- An owner who wrote a build locally has to publish an unfinished folder to authorize its own run.
- The prompt path keeps its push step, a commit and a network round-trip spent on nothing local.

## Build-level rules

- **The kit self-tests are NOT run** — owner, this run's prompt. Verification is hermetic probes
  built from the suites' own setup, and the plain bar at the close.
- **Owner rulings, 2026-10-09, the one opening turn**: the push dropped is the AUTHORIZATION push
  only; the switch is a NEW value `ANCHOR_SCOPE="local"`, so `published` adopters keep
  `TOOL-dNarrowedAnchor-1`'s refusal; the local anchor admits all three modes; the bar leg reads
  the scope from `.unattended.conf` at the remote's default-branch tip, never the working tree.
- **Classification**: both units MISSING at open; authored by this run, so unreviewed.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aHomedAnchor-1` | 2 | the driver's third anchor: `ANCHOR_SCOPE="local"` resolves BASE from local history |
| 2 | `TOOL-aHomedAnchor-2` | 2 | the bar leg admits a local-anchored BASE when origin's default branch declares `local` |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 2 unit(s) · node a · opened 2026-10-09 · streams tooling
ids TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aHomedAnchor-1 — the driver's third anchor: `ANCHOR_SCOPE="local"` authorizes from local history](spec/2026-10-09-spec-TOOL-aHomedAnchor-1.md) | 1 | 2 | INPROGRESS | rev-1 | 2026-10-09 |
| [TOOL-aHomedAnchor-2 — the bar leg admits a local-anchored BASE when origin's default branch declares `local`](spec/2026-10-09-spec-TOOL-aHomedAnchor-2.md) | 2 | 2 | INPROGRESS | rev-1 | 2026-10-09 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aHomedAnchor-1` | no |
| 2 | `TOOL-aHomedAnchor-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
