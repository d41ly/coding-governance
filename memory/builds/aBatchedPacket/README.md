---
slug: aBatchedPacket
node: a
opened: 2026-11-13
streams: tooling
roster: TOOL
ids: TOOL-aBatchedPacket-1 TOOL-aBatchedPacket-2 TOOL-aBatchedPacket-3
authorized-by: prompt
---

# aBatchedPacket — a chain build's packet is rendered and checked without one git process per spec revision

## The problem this build exists to solve

A unit of a chain build run pays tens of minutes before any code is written. The packet instrument's
coverage field runs the carries instrument, which starts one `git log` per chain spec and one
`git show` per revision of it, and the coverage report reads none of what they return. The dispatch
declaration runs that same check through the spec-token checker. The measurements and the analysis
are in `build/`, and the prompt is in `prompts/`.

## Expected improvements

- A packet check or re-render of an unchanged chain takes under a minute on node `a`.
- A dispatch declaration no longer pays the packet instrument's history walk.
- Every verdict, refusal and rendered byte is the instrument's own.

## Detriments if this is not built

- Each unit of a chain build run keeps paying the walk at every re-render and every dispatch.
- A build run of 99 units spends days on overhead that produces nothing. <!-- PINNED 2026-11-14 -->

## Build-level rules

- **Classification (M2)**: one unit, MISSING at open, Tier-2: a new shipped script and a changed
  call in the spec-token checker. A second unit, Tier-2, repairs the closing review's round 1.
- The three pinned instruments under `memory/builds/dClosedLoop/build/` keep their bytes. Editing
  one is the owner's landing and re-pin, which this build files as an ask and does not take.
- `memory/builds/dDeclaredLoop/` and its run's branch are a live run's, and are not touched.
- No full bar and no unattended self-test suite while that run is live.
- No landing: the build stops at a pushed branch, since no mandate to merge was given.
- No spec audit: not declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aBatchedPacket-1` | a front door that runs the packet instrument with its per-spec git reads answered in one process, bound to the instruments' blobs, and the spec-token checker's packet join calling it |
| 2 | `TOOL-aBatchedPacket-2` | the closing review's round 1 repaired: the suite's arms made able to fail on each read, the leg's registrations and guard, the names the lexicon grades, and the batched read under an ambient git location |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 2 unit(s) · node a · opened 2026-11-13 · streams tooling
ids TOOL-aBatchedPacket-1 TOOL-aBatchedPacket-2 TOOL-aBatchedPacket-3

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBatchedPacket-1 — a front door for the chain packet: the instrument's own `main`, its two per-spec reads answered in-process, bound to the instrument blobs it was read against](spec/2026-11-13-spec-TOOL-aBatchedPacket-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-11-13 |
| [TOOL-aBatchedPacket-2 — the closing review's round 1 repaired: each arm of the front door's suite able to fail on the read it names, the leg's owed rows, and a parent read that declines under a foreign git location](spec/2026-11-13-spec-TOOL-aBatchedPacket-2.md) | 2 | 2 | CLOSED | rev-1 | 2026-11-14 |
<!-- /gen:build-units -->

Records: 12 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aBatchedPacket-1 TOOL-aBatchedPacket-2.

Ids whose spec moved past its audited revision: none — 0 of 2 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBatchedPacket-1` | no |
| 2 | `TOOL-aBatchedPacket-2` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
