---
slug: dSweptScratch
node: d
opened: 2026-11-19
streams: tooling
roster: TOOL
ids: TOOL-dSweptScratch-1
---

# dSweptScratch — selftest scratch that a Windows run actually removes

## The problem this build exists to solve

Node `d` held ~1M leftover dirs (~50 GB) in `%TEMP%` on 2026-11-19, enough to stall the disk. The
gov share was scratch the code believed it removed: `rmtree(ignore_errors=True)` over a scratch git
repo, whose objects git writes read-only, so on Windows the tree survives. TOOL-aBranchedMandate-6
fixed this in the memory-recall selftest alone. The bar's trapped `TMPDIR` hides it; a direct run
does not.

## Expected improvements

- A suite run directly on Windows leaves its temp dir as it found it.
- Adopters receive the same through re-adoption, since their copies are these files.

## Detriments if this is not built

- Every direct run keeps adding git trees to `%TEMP%`, hundreds per run for the larger suites.
- A machine that runs them all day fills its disk and stalls on metadata, as node `d` did.

## Build-level rules

- **Tier-1.** One mechanism applied at many call sites, no kit contract changed.
- **Merge and push on the owner's explicit ask** ("land everything", 2026-11-19).

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dSweptScratch-1` | 1 | every selftest and fixture removes the scratch it made, read-only git objects included |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node d · opened 2026-11-19 · streams tooling
ids TOOL-dSweptScratch-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSweptScratch-1 — every selftest and fixture removes the scratch it made, read-only git objects included](spec/2026-11-19-spec-TOOL-dSweptScratch-1.md) | — | 1 | CLOSED | rev-2 | 2026-11-19 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-dSweptScratch-1.

Ids no `spec-audit` record has ever named: TOOL-dSweptScratch-1.

Ids whose spec moved past its audited revision: none — 0 of 1 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
