---
slug: dPavedRoad
node: a
opened: 2026-11-10
streams: tooling
roster: TOOL
status: OPEN
ids: TOOL-dPavedRoad-1 TOOL-dPavedRoad-2 TOOL-dPavedRoad-3 TOOL-dPavedRoad-4
---

# dPavedRoad — four mechanical refusals that cost dSafePassage its rework

## The problem this build exists to solve

dSafePassage's own transcript shows where its build run lost time to mechanics, not design. About 17 of the 37 corrections sent to agents were spec-token hits a spec writer could not see, because the role may not run the checker and the checker skips a DEFERRED spec. About 33 turn ends were refused for agent or commit lines the format-guard already knew. Three writers needed context the handoff dropped. And `--staged` hygiene holds checks 12 and 23, so 6 one-way edges and 10 unjoined ledger lines surfaced only at the close. The prompt is in `prompts/`.

## Expected improvements

- A spec writer sees its own spec-token hits before it returns.
- A refused turn end carries the exact lines it asks for.
- A spec writer's Task section carries the brief's prompt.
- A commit grades check 12 and check 23 for the files it stages.

## Detriments if this is not built

- Every later build keeps paying agent round trips for spec-token hits it could catch at write time.
- Every refused turn end keeps costing a re-send.
- One-way edges and unjoined ledger lines keep surfacing at the close, as whole new units.

## Build-level rules

- **Classification (M2)**: four units, MISSING at open, Tier-2: each changes a shipped gate, hook or role file.
- No spec audit: the owner declined one at kickoff.
- `--staged` stays cheap: units 1 and 4 grade the named or staged files only, never the corpus.
- Kit versions move through the lander's `mint`, never by hand.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dPavedRoad-1` | `check-spec-tokens.py --spec <path>` grades one spec as if live, and the spec writer's gates add the spec-tokens leg |
| 2 | `TOOL-dPavedRoad-2` | format-guard's block message prints the derived agent, returned and committed lines it asks for |
| 3 | `TOOL-dPavedRoad-3` | the handoff's Task section carries the brief's prompt as a `brief:prompt` field |
| 4 | `TOOL-dPavedRoad-4` | memory hygiene `--staged` grades check 12 edges and check 23 ledger joins for the staged files only |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-10 · streams tooling
ids TOOL-dPavedRoad-1 TOOL-dPavedRoad-2 TOOL-dPavedRoad-3 TOOL-dPavedRoad-4

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
