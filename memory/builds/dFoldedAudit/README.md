---
slug: dFoldedAudit
node: d
opened: 2026-11-01
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8
---

# dFoldedAudit — a spec audit folds local fixes, promotes only new mechanisms, and its chain stops itself

## The problem this build exists to solve

M4 binds a spec audit to PROMOTE every confirmed finding into a new unit and refuses `fold` at every
exit. A one-line correction therefore becomes a unit that overrides its target from outside while
the target stays wrong, and that unit is audited as new surface, so each round mints the next. The
chain is bounded only by a precision floor no round reached: dMindYourWords ran highs 7, 7, 13 at
precision 0.97, 0.90, 0.89 until the owner stopped it by hand. The owner's prompt is recorded
verbatim under `prompts/`.

## Expected improvements

- A spec audit's local findings fold into their specs, revisions bumped.
- Only a finding that needs a new mechanism mints a unit.
- A repair unit edits its unbuilt sibling's spec instead of superseding it from outside.
- A chain stops on a derived verdict, with a ceiling that holds for the owner.
- dClosedLoop's unbuilt specs carry the same rules.

## Detriments if this is not built

- Every spec run keeps paying about 1.8M tokens a round to audit its own promotions.
- Corrected specs stay wrong beside the units that override them.
- A chain keeps ending only when the owner stops it by hand.
- The closed-loop design ships the promote-everything rule into `tools/loop/`.

## Build-level rules

- **Classification (M2)**: eight units, MISSING at open, Tier-2: shipped kit edits.
- **Scope**: spec audits only. Closing diff reviews stay exactly as they are.
- Owner, 2026-11-01: at an R5 stop a local HIGH folds, and a HIGH needing a new mechanism is
  promoted once more and built from its spec under a recorded `specs-audited` override.
- Owner, 2026-11-01: a round whose HIGHs all fold and that promotes nothing re-audits only the specs
  it folded, and a round whose HIGHs all sit in the prior round's folds also stops.
- Owner, 2026-11-01: the precision bound retires; a chain-level round ceiling, a policy key
  defaulting to 4, holds the run for the owner when neither stop has fired.
- Brief, accepted by the owner 2026-11-01: not retroactive, so promoted minor batches stand. R4
  reaches an unbuilt sibling only. A budget does not outrank R1 for spec audits. dSafePassage and
  every live run stay untouched.
- No `spec-audit:` key: the owner's prompt does not ask for one, so none is owed here.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-dFoldedAudit-1` | M4 and its carriers state the spec-audit disposal and chain stop |
| 2 | `TOOL-dFoldedAudit-2` | `--review` and check 2 record and grade a spec exit that folds |
| 3 | `TOOL-dFoldedAudit-3` | the DISPOSAL stage disposes by nature and reconciles folds to their specs |
| 4 | `TOOL-dFoldedAudit-4` | a repair unit edits its unbuilt sibling's spec with a rev bump |
| 5 | `TOOL-dFoldedAudit-5` | each HIGH records its specs and a verb derives the chain's stop verdict |
| 6 | `TOOL-dFoldedAudit-6` | an audit's own fold owes no hand `spec-revised` deviation record |
| 7 | `TOOL-dFoldedAudit-7` | policy keys switch the disposal, the stop and the ceiling |
| 8 | `TOOL-dFoldedAudit-8` | dClosedLoop's unbuilt specs and its frozen design take the same rules |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 8 unit(s) · node d · opened 2026-11-01 · streams tooling
ids TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dFoldedAudit-7 — policy keys switch the disposal, the stop and the ceiling](spec/2026-11-01-spec-TOOL-dFoldedAudit-7.md) | 10 | 2 | OPEN | rev-3 | 2026-11-01 |
| [TOOL-dFoldedAudit-2 — --review and check 2 record and grade a spec exit that folds](spec/2026-11-01-spec-TOOL-dFoldedAudit-2.md) | 20 | 2 | OPEN | rev-2 | 2026-11-01 |
| [TOOL-dFoldedAudit-3 — the DISPOSAL stage disposes by nature and reconciles folds to their specs](spec/2026-11-01-spec-TOOL-dFoldedAudit-3.md) | 30 | 2 | OPEN | rev-2 | 2026-11-01 |
| [TOOL-dFoldedAudit-4 — a repair unit edits its unbuilt sibling's spec with a rev bump](spec/2026-11-01-spec-TOOL-dFoldedAudit-4.md) | 40 | 2 | OPEN | rev-3 | 2026-11-01 |
| [TOOL-dFoldedAudit-5 — each HIGH records its specs and a verb derives the chain's stop verdict](spec/2026-11-01-spec-TOOL-dFoldedAudit-5.md) | 50 | 2 | OPEN | rev-2 | 2026-11-01 |
| [TOOL-dFoldedAudit-6 — an audit's own fold owes no hand `spec-revised` deviation record](spec/2026-11-01-spec-TOOL-dFoldedAudit-6.md) | 60 | 2 | OPEN | rev-3 | 2026-11-01 |
| [TOOL-dFoldedAudit-1 — M4 and its carriers state the spec-audit disposal and chain stop](spec/2026-11-01-spec-TOOL-dFoldedAudit-1.md) | 70 | 2 | OPEN | rev-3 | 2026-11-01 |
| [TOOL-dFoldedAudit-8 — dClosedLoop's unbuilt specs and its frozen design take the same rules](spec/2026-11-01-spec-TOOL-dFoldedAudit-8.md) | 80 | 2 | OPEN | rev-1 | 2026-11-01 |
<!-- /gen:build-units -->

Records: 29 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8.

Ids whose spec moved past its audited revision: none — 0 of 8 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 10 | `TOOL-dFoldedAudit-7` | no |
| 20 | `TOOL-dFoldedAudit-2` | no |
| 30 | `TOOL-dFoldedAudit-3` | no |
| 40 | `TOOL-dFoldedAudit-4` | no |
| 50 | `TOOL-dFoldedAudit-5` | no |
| 60 | `TOOL-dFoldedAudit-6` | no |
| 70 | `TOOL-dFoldedAudit-1` | no |
| 80 | `TOOL-dFoldedAudit-8` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
