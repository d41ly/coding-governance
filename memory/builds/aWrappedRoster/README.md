---
slug: aWrappedRoster
node: a
opened: 2026-11-22
streams: tooling
roster: TOOL
ids: TOOL-aWrappedRoster-1
---

# aWrappedRoster — the kit's leg-manifest parser reads an object-wrapped manifest

## The problem this build exists to solve

`tree_lib.parse_leg_names` accepts only a top-level JSON list of leg rows. inCMS commits its
`scripts/gate-legs.json` as `{"_doc": ..., "legs": [...]}`, so the parser raises on every blob of
it. The red-fix lane reads that as "no leg manifest", and every `Red-fix:` commit in inCMS reds the
`routed commits name a specced unit` leg as uncheckable. It held inCMS's bPliantViewport landing.

## Expected improvements

- A `Red-fix:` commit in an adopter with an object-wrapped manifest grades against its legs.

## Detriments if this is not built

- Every adopter with a wrapped manifest carries a permanent routed-commits red nobody can clear.

## Build-level rules

- Owner go, 2026-11-22, in the bPliantViewport session on node `a`: "Fix it upstream".

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aWrappedRoster-1` | `parse_leg_names` unwraps a top-level object's `legs` list |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node a · opened 2026-11-22 · streams tooling
ids TOOL-aWrappedRoster-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aWrappedRoster-1 — the leg-manifest parser reads an object-wrapped manifest](spec/2026-11-22-spec-TOOL-aWrappedRoster-1.md) | — | 1 | CLOSED | rev-2 | 2026-11-22 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-aWrappedRoster-1.

Ids no `spec-audit` record has ever named: TOOL-aWrappedRoster-1.

Ids whose spec moved past its audited revision: none — 0 of 1 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| the units | the units table above |
| card ref | `refs/gov/builds/aWrappedRoster/card` |
<!-- /gen:build-routes -->
