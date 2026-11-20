---
slug: dHomeGraded
node: d
opened: 2026-11-20
streams: tooling
roster: TOOL
ids: TOOL-dHomeGraded-1
---

# dHomeGraded — an adopter's bar grades the adopter, not gov's own installed kit files

## The problem this build exists to solve

Re-adopting gov 608aa364 into nicocares and inCMS left 19 and 17 red legs before either tree changed
a line of its own. Most of the reds grade files gov installed, byte-identical to gov's sources: the
shell-hygiene scans list hundreds of sites in kit scripts against an empty adopter registry, the
lexicon counts kit definitions against the adopter's pin, and check-arms asks the adopter's
DECISIONS.md for a decision gov recorded. The rest are four deployer defects: the cap census looks
for a flat-installed kit at its default path, govkit keeps a retired kit's leg row, pass_legs ignores
`[gate_runner].file`, and the lexicon grades govkit's own state dir.

## Expected improvements

- A re-adoption reds only on what the adopter wrote or edited.
- Adopters receive the fix through `govkit update`, since the scanners are kit files.

## Detriments if this is not built

- Every adopter pays for gov's kit vocabulary: registry rows, pin bumps and decision rows that
  restate gov's own records, re-done at every gov vintage.
- The real adopter findings drown among gov's, so a re-adoption stalls on noise.

## Build-level rules

- **Tier-1.** Five small mechanisms, one shared receipt reader, no receipt or manifest shape changed.
- **Merge and push on the owner's explicit ask** ("Fix gov first", 2026-11-20).

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dHomeGraded-1` | 1 | adopter scans skip gov's unmodified kit files, and four deployer defects found by the 608aa364 re-adoption close |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 1 unit(s) · node d · opened 2026-11-20 · streams tooling
ids TOOL-dHomeGraded-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dHomeGraded-1 — adopter scans skip gov's unmodified kit files, and four re-adoption defects close](spec/2026-11-20-spec-TOOL-dHomeGraded-1.md) | — | 1 | CLOSED | rev-2 | 2026-11-20 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: TOOL-dHomeGraded-1.

Ids no `spec-audit` record has ever named: TOOL-dHomeGraded-1.

Ids whose spec moved past its audited revision: none — 0 of 1 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
