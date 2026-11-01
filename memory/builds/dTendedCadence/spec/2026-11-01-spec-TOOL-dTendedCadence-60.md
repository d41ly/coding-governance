# TOOL-dTendedCadence-60 — unit 1's item rows route `red-leg`, `pending`, `declined` and `refused` to the record, so the derived route set holds what the walk returns

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 5 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-prompt-TOOL-dTendedCadence-60-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-60-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-60-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-60-promoted-fix-brief.md) | research | TOOL-dTendedCadence-67 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 14 (TOOL-dTendedCadence-61), 27 (TOOL-dTendedCadence-62) and 35
(TOOL-dTendedCadence-63). Unit 56 derives the record's route set from the `[[item]]` rows and renames
the red leg's hold to `red-leg` (spec-56 S1, S2). Unit 1's `item.maintain.file` row still routes
`filed`, `seen`, `held`, `reported` and `none` to `item.maintain.record` (spec-1 §4 "The rows",
:172), and no unit owes the rename, so a `red-leg` reading exits 2 before the write and the red leg
reads green while offenders stand. This unit corrects the rows unit 1 builds, before unit 1 builds
them.

## 2. Scope (IN)

- **S1** — The file row. Unit 1 §4 "The rows" gives `item.maintain.file` the outcomes `filed`, `seen`,
  `pending`, `red-leg`, `declined`, `reported` and `none`, each routed to `item.maintain.record`, and
  no `held`. `pending` is unit 17's filing (spec-17:129), `red-leg` unit 15 S3's hold as unit 56 S2
  names it, and `declined` TOOL-dTendedCadence-59 S17's decline. Corrected in spec-1's text, a rev
  bump with a §9 line naming review id 1. Observed by AC1.
- **S2** — The patch row. The same table gives `item.maintain.patch` the outcome `refused` routed to
  `item.maintain.record`, the hand-off unit 56's §3 already names toward unit 1. Observed by AC1.
- **S3** — The edge text. Spec-1's §3 edge consuming from TOOL-dTendedCadence-37 (:134) reads "the
  rule that a `red-leg` reading's `keys` are the keys the route held". Observed by AC2.

## 3. Non-goals (OUT)

- Writing the rows into `tools/drift-audit/kit.toml`: unit 1 S1, at order 8, from the corrected table.
- Unit 56's own §4 set: TOOL-dTendedCadence-61. Unit 15's text: TOOL-dTendedCadence-62. The arm over
  the shipped descriptor: TOOL-dTendedCadence-63.
- The other by-value readers of `held` (specs 16, 17, 37, 38, 43): item M7 of the same report,
  TOOL-dTendedCadence-74.

### Edges

- **consumes-from** `TOOL-dTendedCadence-56` — the derived route set and the `red-leg` hold, which unit 1's rows must route to the record
- **hands-off** `TOOL-dTendedCadence-1` — the corrected `item.maintain.file` and `item.maintain.patch` rows of §4 "The rows", which that unit writes into the kit descriptor
- **hands-off** `TOOL-dTendedCadence-61` — the corrected rows, which unit 56's §4 set is restated over
- **hands-off** `TOOL-dTendedCadence-63` — the corrected rows, whose shipped form that unit's arm reads

## 4. Design

The correction moves one table row, one cell of another and one edge sentence in spec-1; nothing
else in spec-1 changes. Written in this unit's build pass at order 5, so unit 1's builder at order 8
reads the corrected table. Unit 3's direct outcome `held` still routes to `item.maintain.file` (spec-3
S3, :69-70) and never reaches the record.

### Files touched (estimate)

- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-1.md`: S1 to S3

## 5. Acceptance criteria

- **AC1** — When `grep -n '^| .item.maintain.file.\|^| .item.maintain.patch.'
  2026-11-01-spec-TOOL-dTendedCadence-1.md` runs in the spec folder, the file row names `red-leg`,
  `pending` and `declined` and not `held`, and the patch row names `refused`.
  Red when: the row unit 1 builds still routes `held`, or a route the walk returns is absent.
- **AC2** — When `grep -c "a .held. reading" 2026-11-01-spec-TOOL-dTendedCadence-1.md` runs in the
  spec folder, it prints 0, and `grep -c "a .red-leg. reading"` over the same file prints at least 1.
  Red when: the edge text still names the old hold.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 1 (HIGH, item H1) of the round-1 spec
  audit of units 49 to 59.

## 9. Reuse audit

No code is written; the seam is spec-1's own table, corrected in place as TOOL-dTendedCadence-59
corrects its siblings. `python tools/codebase-map/reuse_lookup.py "derive the outcomes the item rows
route to one item"` ranked name stems only, as unit 56 §10 recorded, so no existing seam fits.

Recall terms used: `python tools/memory-recall/query.py "which routes may a reading carry into the
maintenance record" --terms "route set item rows outcomes routes item.maintain.record refused pending
held red-leg declined"`
