---
slug: dLandedOwners
node: d
opened: 2026-11-19
streams: tooling
roster: TOOL
status: OPEN
ids: TOOL-dLandedOwners-1 TOOL-dLandedOwners-2 TOOL-dLandedOwners-3
---

# dLandedOwners — the policy kit counts a carried-forward build run as landed, and its reader scan sees every real reader

## The problem this build exists to solve

The policy kit's `derive_landed_owners` counts a build as landed only when every spec reads CLOSED or
WONTDO, so a build run that carried one unit forward, DEFERRED against an ask, reads unlanded:
dDeclaredLoop and dSafePassage at `51971579a`. The reader-coverage arm and the loop's termination read
skip their keys. Counting them landed reds reader coverage on eight dDeclaredLoop keys: seven are read by
the loop kit through a module constant the reader scan does not see, and one is read only by a dClosedLoop
instrument the scan excludes. The owner's words are recorded under `prompts/`.

## Expected improvements

- The policy kit reads every landed build run as landed, a carried-forward unit included.
- The reader scan sees a key read through a module constant.
- Reader coverage grades every landed owner's keys and reports no false finding.

## Detriments if this is not built

- Policy keys owned by landed builds go ungraded for a missing reader.
- The loop's termination read treats landed builds as open.
- Ask TOOL-dTrackedAtlas-5 stays open against a defect the schedule no longer has.

## Build-level rules

- Attended, through `/build`; the owner chose the scope on 2026-11-19: "Predicate + scan".
- Every unit is a shipped-kit edit under `tools/policy/`, so Tier-2.
- No spec audit: the owner was not asked for one and the scope is three small mechanisms.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dLandedOwners-1` | the landed-owner predicate counts a build run that landed with units carried forward as landed |
| 2 | `TOOL-dLandedOwners-2` | the reader scan reads a key passed to a reader through a module constant |
| 3 | `TOOL-dLandedOwners-3` | a key read only outside the scanned code takes a declared, reasoned disposition in reader coverage |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-11-19 · streams tooling
ids TOOL-dLandedOwners-1 TOOL-dLandedOwners-2 TOOL-dLandedOwners-3

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
