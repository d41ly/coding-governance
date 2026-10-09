---
slug: aHomedAnchor
node: a
opened: 2026-10-09
streams: tooling
roster: TOOL
ids: TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 TOOL-aHomedAnchor-8 TOOL-aHomedAnchor-9 TOOL-aHomedAnchor-10 TOOL-aHomedAnchor-11 TOOL-aHomedAnchor-12 TOOL-aHomedAnchor-13 TOOL-aHomedAnchor-14 TOOL-aHomedAnchor-15 TOOL-aHomedAnchor-16 TOOL-aHomedAnchor-17 TOOL-aHomedAnchor-18 TOOL-aHomedAnchor-19 TOOL-aHomedAnchor-20 TOOL-aHomedAnchor-21
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
- **Classification**: units 1 and 2 MISSING at open; 3 to 7 promoted by the closing review's round 1
  (CONVERGED, no blocker). All seven authored by this run; no spec audit was declared.

## Parked decisions

None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aHomedAnchor-1` | 2 | the driver's third anchor: `ANCHOR_SCOPE="local"` resolves BASE from local history |
| 2 | `TOOL-aHomedAnchor-2` | 2 | the bar leg admits a local-anchored BASE when origin's default branch declares `local` |
| 3 | `TOOL-aHomedAnchor-3` | 1 | re-render the Skill (review round 1, HIGH id 7) |
| 3 | `TOOL-aHomedAnchor-5` | 1 | an adopter arm proves the `local` render (HIGH id 28, M9) |
| 4 | `TOOL-aHomedAnchor-4` | 1 | the pre-commit hook runs the wiring check on its inputs (HIGH id 17) |
| 5 | `TOOL-aHomedAnchor-6` | 2 | the driver and doc minors, batched |
| 5 | `TOOL-aHomedAnchor-7` | 2 | the leg minors, batched |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 7 unit(s) · node a · opened 2026-10-09 · streams tooling
ids TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 TOOL-aHomedAnchor-8 TOOL-aHomedAnchor-9 TOOL-aHomedAnchor-10 TOOL-aHomedAnchor-11 TOOL-aHomedAnchor-12 TOOL-aHomedAnchor-13 TOOL-aHomedAnchor-14
ids TOOL-aHomedAnchor-15 TOOL-aHomedAnchor-16 TOOL-aHomedAnchor-17 TOOL-aHomedAnchor-18 TOOL-aHomedAnchor-19 TOOL-aHomedAnchor-20 TOOL-aHomedAnchor-21

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aHomedAnchor-1 — the driver's third anchor: `ANCHOR_SCOPE="local"` authorizes from local history](spec/2026-10-09-spec-TOOL-aHomedAnchor-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aHomedAnchor-2 — the bar leg admits a local-anchored BASE when origin's default branch declares `local`](spec/2026-10-09-spec-TOOL-aHomedAnchor-2.md) | 2 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aHomedAnchor-3 — re-render the unattended Skill from its template](spec/2026-10-09-spec-TOOL-aHomedAnchor-3.md) | 3 | 1 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aHomedAnchor-5 — an adopter arm proves the render of `ANCHOR_SCOPE="local"`](spec/2026-10-09-spec-TOOL-aHomedAnchor-5.md) | 3 | 1 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aHomedAnchor-4 — the pre-commit hook runs the Skill wiring check when its inputs are staged](spec/2026-10-09-spec-TOOL-aHomedAnchor-4.md) | 4 | 1 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aHomedAnchor-6 — the closing review's driver and doc minors, batched](spec/2026-10-09-spec-TOOL-aHomedAnchor-6.md) | 5 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aHomedAnchor-7 — the closing review's leg minors, batched](spec/2026-10-09-spec-TOOL-aHomedAnchor-7.md) | 5 | 2 | CLOSED | rev-1 | 2026-10-09 |
<!-- /gen:build-units -->

Records: 11 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aHomedAnchor-1` | no |
| 2 | `TOOL-aHomedAnchor-2` | no |
| 3 | `TOOL-aHomedAnchor-3`, `TOOL-aHomedAnchor-5` | yes |
| 4 | `TOOL-aHomedAnchor-4` | no |
| 5 | `TOOL-aHomedAnchor-6`, `TOOL-aHomedAnchor-7` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
