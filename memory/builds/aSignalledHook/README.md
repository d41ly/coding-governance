---
slug: aSignalledHook
node: a
opened: 2026-10-11
streams: tooling
roster: TOOL
ids: TOOL-aSignalledHook-1
---

# aSignalledHook — a signal-killed pre-push hook refuses the push instead of landing it

## The problem this build exists to solve

On Git for Windows a pre-push hook that dies by a signal is read by git as success, so the push lands
with no bar. 69e0ff0f landed that way on 2026-10-11 while its bar sat queued in the turnstile: the
hook's run-log END reads `rc=0 exit=unclean` five seconds before the push. The hook had no signal trap
by design, and nothing downstream could tell that landing from a gated one.

## Expected improvements

- A catchable signal to the hook refuses the push on every platform, and stops the bar it was waiting on.
- A push git calls successful with no hook verdict is reported as `landed UNGATED`, with no lander marker.

## Detriments if this is not built

- Any session that stops a lander mid-bar can land an ungated default branch, silently.
- An unattended run reads that landing as gated, because the lander marker is written regardless.

## Build-level rules

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aSignalledHook-1` | INPROGRESS | trap the hook's catchable signals into a refusal; the lander requires the hook's allow record |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 1 unit(s) · node a · opened 2026-10-11 · streams tooling
ids TOOL-aSignalledHook-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aSignalledHook-1 — a signal-killed pre-push hook refuses the push, and a success with no hook verdict is caught by the lander](spec/2026-10-11-spec-TOOL-aSignalledHook-1.md) | 1 | 2 | INPROGRESS | rev-1 | 2026-10-11 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aSignalledHook-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aSignalledHook-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
