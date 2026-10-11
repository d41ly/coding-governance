---
slug: aHomedAnchor
node: a
opened: 2026-10-09
streams: tooling
roster: TOOL
ids: TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 TOOL-aHomedAnchor-8 TOOL-aHomedAnchor-9 TOOL-aHomedAnchor-10 TOOL-aHomedAnchor-11 TOOL-aHomedAnchor-12 TOOL-aHomedAnchor-13 TOOL-aHomedAnchor-14 TOOL-aHomedAnchor-15 TOOL-aHomedAnchor-16 TOOL-aHomedAnchor-17 TOOL-aHomedAnchor-18 TOOL-aHomedAnchor-19 TOOL-aHomedAnchor-20 TOOL-aHomedAnchor-21 TOOL-aHomedAnchor-22 TOOL-aHomedAnchor-23 TOOL-aHomedAnchor-24 TOOL-aHomedAnchor-25 TOOL-aHomedAnchor-26 TOOL-aHomedAnchor-27 TOOL-aHomedAnchor-28
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
| 6 | `TOOL-aHomedAnchor-22` | 1 | command-line entry points write UTF-8 (held asks -10, -11, -14) |
| 6 | `TOOL-aHomedAnchor-23` | 1 | the launcher arm reads only invocations (held ask -18) |
| 6 | `TOOL-aHomedAnchor-24` | 1 | `--overlaps` on both agent surfaces (held ask -20) |
| 6 | `TOOL-aHomedAnchor-25` | 1 | two suite fixtures follow other builds' carriers |
| 6 | `TOOL-aHomedAnchor-26` | 1 | the F4 harness initialises the filer's driver globals (held ask -19) |
| 6 | `TOOL-aHomedAnchor-27` | 1 | govkit reads the paths it guards as UTF-8 (held ask -12) |
| 6 | `TOOL-aHomedAnchor-28` | 1 | the unattended-build self-test's budget re-declared (held ask -21) |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 14 unit(s) · node a · opened 2026-10-09 · streams tooling
ids TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 TOOL-aHomedAnchor-8 TOOL-aHomedAnchor-9 TOOL-aHomedAnchor-10 TOOL-aHomedAnchor-11 TOOL-aHomedAnchor-12 TOOL-aHomedAnchor-13 TOOL-aHomedAnchor-14
ids TOOL-aHomedAnchor-15 TOOL-aHomedAnchor-16 TOOL-aHomedAnchor-17 TOOL-aHomedAnchor-18 TOOL-aHomedAnchor-19 TOOL-aHomedAnchor-20 TOOL-aHomedAnchor-21 TOOL-aHomedAnchor-22 TOOL-aHomedAnchor-23 TOOL-aHomedAnchor-24 TOOL-aHomedAnchor-25 TOOL-aHomedAnchor-26 TOOL-aHomedAnchor-27 TOOL-aHomedAnchor-28

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
| [TOOL-aHomedAnchor-22 — command-line entry points write UTF-8 whatever the platform default](spec/2026-10-11-spec-TOOL-aHomedAnchor-22.md) | 6 | 1 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aHomedAnchor-23 — the launcher arm reads an invocation, not a declaration, a string or a file extension](spec/2026-10-11-spec-TOOL-aHomedAnchor-23.md) | 6 | 1 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aHomedAnchor-24 — the `--overlaps` verb is named on both surfaces an agent reads](spec/2026-10-11-spec-TOOL-aHomedAnchor-24.md) | 6 | 1 | CLOSED | rev-2 | 2026-10-11 |
| [TOOL-aHomedAnchor-25 — two suite fixtures follow the carriers other builds changed](spec/2026-10-11-spec-TOOL-aHomedAnchor-25.md) | 6 | 1 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aHomedAnchor-26 — the F4 filer harness initialises the driver globals the filer appends to](spec/2026-10-11-spec-TOOL-aHomedAnchor-26.md) | 6 | 1 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aHomedAnchor-27 — govkit reads the paths it guards as UTF-8](spec/2026-10-11-spec-TOOL-aHomedAnchor-27.md) | 6 | 1 | CLOSED | rev-1 | 2026-10-11 |
| [TOOL-aHomedAnchor-28 — the unattended-build self-test's budget is re-declared from readings](spec/2026-10-11-spec-TOOL-aHomedAnchor-28.md) | 6 | 1 | CLOSED | rev-1 | 2026-10-11 |
<!-- /gen:build-units -->

Records: 12 bound to this build, across 4 record folder(s).

Ids no record names: TOOL-aHomedAnchor-26 TOOL-aHomedAnchor-27 TOOL-aHomedAnchor-28.

Ids no `spec-audit` record has ever named: TOOL-aHomedAnchor-1 TOOL-aHomedAnchor-2 TOOL-aHomedAnchor-3 TOOL-aHomedAnchor-4 TOOL-aHomedAnchor-5 TOOL-aHomedAnchor-6 TOOL-aHomedAnchor-7 TOOL-aHomedAnchor-22 TOOL-aHomedAnchor-23 TOOL-aHomedAnchor-24 TOOL-aHomedAnchor-25 TOOL-aHomedAnchor-26
TOOL-aHomedAnchor-27 TOOL-aHomedAnchor-28.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aHomedAnchor-1` | no |
| 2 | `TOOL-aHomedAnchor-2` | no |
| 3 | `TOOL-aHomedAnchor-3`, `TOOL-aHomedAnchor-5` | yes |
| 4 | `TOOL-aHomedAnchor-4` | no |
| 5 | `TOOL-aHomedAnchor-6`, `TOOL-aHomedAnchor-7` | yes |
| 6 | `TOOL-aHomedAnchor-22`, `TOOL-aHomedAnchor-23`, `TOOL-aHomedAnchor-24`, `TOOL-aHomedAnchor-25`, `TOOL-aHomedAnchor-26`, `TOOL-aHomedAnchor-27`, `TOOL-aHomedAnchor-28` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
