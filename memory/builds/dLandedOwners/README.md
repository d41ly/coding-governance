---
slug: dLandedOwners
node: d
opened: 2026-11-19
streams: tooling
roster: TOOL
ids: TOOL-dLandedOwners-1 TOOL-dLandedOwners-2 TOOL-dLandedOwners-3 TOOL-dLandedOwners-4 TOOL-dLandedOwners-5 TOOL-dLandedOwners-6
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
- Every unit is a shipped-kit edit, so Tier-2: all four under `tools/policy/`, unit 2 also in `tools/loop/budget.py`,
  unit 4 also in `tools/govkit/`.
- No spec audit: the owner was not asked for one and the scope opened as three small mechanisms. Unit 4 is the
  closing review's promoted findings, batched as the diff-exit rule orders.
- Fork F1 of unit 1, the owner's pick (a): dDeclaredLoop's pending review cycle row is carried by ask
  `TOOL-dLandedOwners-5`, and the held `loop termination` leg reads it stale until a later build bounds the cycle.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dLandedOwners-1` | the landed-owner predicate counts a build run that landed with units carried forward as landed |
| 2 | `TOOL-dLandedOwners-2` | the reader scan reads a key passed to a reader through a module constant |
| 3 | `TOOL-dLandedOwners-3` | a key read only outside the scanned code takes a declared, reasoned disposition in reader coverage |
| 4 | `TOOL-dLandedOwners-4` | the closing review's promoted findings: the kit threaded to every resolver, failing cases for each landed-predicate arm, the withheld list checked, one git-read refusal and the docs aligned (M1-M5, L1-L4, promoted) |
| 5 | `TOOL-dLandedOwners-6` | the two legs the close's bar read red: the policy-fixtures guard covers its import closure, and the unscanned-readers row stops reading as a spec citation |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 5 unit(s) · node d · opened 2026-11-19 · streams tooling
ids TOOL-dLandedOwners-1 TOOL-dLandedOwners-2 TOOL-dLandedOwners-3 TOOL-dLandedOwners-4 TOOL-dLandedOwners-5 TOOL-dLandedOwners-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dLandedOwners-1 — the policy kit's landed predicate counts a build run that carried a unit forward](spec/2026-11-19-spec-TOOL-dLandedOwners-1.md) | 1 | 2 | CLOSED | rev-3 | 2026-11-19 |
| [TOOL-dLandedOwners-2 — the reader scan reads a key passed to a reader through a module constant](spec/2026-11-19-spec-TOOL-dLandedOwners-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-11-19 |
| [TOOL-dLandedOwners-3 — a key read only outside the scanned code takes a declared, reasoned disposition in reader coverage](spec/2026-11-19-spec-TOOL-dLandedOwners-3.md) | 3 | 2 | CLOSED | rev-1 | 2026-11-19 |
| [TOOL-dLandedOwners-4 — the closing review's promoted findings: the kit threaded to every resolver, a failing case for each landed-predicate arm, every withheld file checked, one git-read refusal and the docs aligned](spec/2026-11-19-spec-TOOL-dLandedOwners-4.md) | 4 | 2 | CLOSED | rev-2 | 2026-11-19 |
| [TOOL-dLandedOwners-6 — the two legs the close's bar read red: the policy-fixtures guard covers its import closure, and the unscanned-readers row stops reading as a spec citation](spec/2026-11-19-spec-TOOL-dLandedOwners-6.md) | 5 | 2 | CLOSED | rev-1 | 2026-11-19 |
<!-- /gen:build-units -->

Records: 27 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dLandedOwners-1 TOOL-dLandedOwners-2 TOOL-dLandedOwners-3 TOOL-dLandedOwners-4 TOOL-dLandedOwners-6.

Ids whose spec moved past its audited revision: none — 0 of 5 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dLandedOwners-1` | no |
| 2 | `TOOL-dLandedOwners-2` | no |
| 3 | `TOOL-dLandedOwners-3` | no |
| 4 | `TOOL-dLandedOwners-4` | no |
| 5 | `TOOL-dLandedOwners-6` | no |

A step's `Parallel` yes means its units share an order; `doc.build-method#m6-passes-commits-parallelism` still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| the units | the units table above |
| briefs | `2026-11-19-prompt-TOOL-dLandedOwners-6-spec-brief.md`, `2026-11-19-prompt-TOOL-dLandedOwners-6-build-brief.md` and 18 more under prompts/ |
| reviews | `2026-11-19-review-TOOL-dLandedOwners-1-3-closing-diff-round1.md` (CLEAN WITH FIXES) |
| logs | `2026-11-20-build-TOOL-dLandedOwners-1-agent-ledger.md`, `2026-11-19-build-TOOL-dLandedOwners-6-ledger.md` and 4 more under build/ |
| open asks | `BACKLOG.md`, 1 open |
| card ref | `refs/gov/builds/dLandedOwners/card` |
<!-- /gen:build-routes -->
