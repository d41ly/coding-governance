# TOOL-dTendedCadence-61 — unit 56's route set stated over the rows the siblings actually write, its evidence quoted as it stands

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 5 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-build-TOOL-dTendedCadence-61-deviation-611.md](../build/2026-11-01-build-TOOL-dTendedCadence-61-deviation-611.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 14 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 1 (TOOL-dTendedCadence-60), 27 (TOOL-dTendedCadence-62) and 35
(TOOL-dTendedCadence-63). Unit 56 §4 "The set" (:70-72) claims the rows "as specced" route `red-leg`
and `pending` to the record and route `held` elsewhere, while its own Evidence (:81-82) quotes spec-1
routing `held` to the record and no spec routes `pending`. A builder reading §4 takes the set as
settled, and its fixture plants rows already spelling `red-leg`, so nothing it says can be checked
against what unit 1 writes. This unit makes §4 state the set the corrected rows derive, row by row,
with the unit that owns each row.

## 2. Scope (IN)

- **S1** — The set. Spec-56 §4 "The set" lists the derived set as a table of row, owning unit and the
  outcomes it routes to `item.maintain.record`: `item.maintain.read` (unit 1) `in-pin`, `log`;
  `item.maintain.patch` (unit 1, with TOOL-dTendedCadence-60 S2) `filed`, `seen`, `none`, `refused`;
  `item.maintain.levels` (unit 1) `green`; `item.maintain.file` (unit 1, with TOOL-dTendedCadence-60
  S1) `filed`, `seen`, `pending`, `red-leg`, `declined`, `reported`, `none`; `item.maintain.direct`
  (units 3 and 46) `fixed`, `filed`, `seen`. The sentence "Read over the rows as specced" is not kept.
  Corrected in spec-56's text, a rev bump with a §9 line naming review id 14. Observed by AC1.
- **S2** — The evidence. Spec-56 §4 Evidence quotes spec-1's rows as TOOL-dTendedCadence-60 corrects
  them, and names that unit as the source of `red-leg`, `pending`, `declined` and `refused` on them.
  Observed by AC2.
- **S3** — The fixture note. Spec-56 §6's fixture paragraph says its planted rows are a copy, and that
  the shipped descriptor is read by TOOL-dTendedCadence-63's arm. Observed by AC2.

## 3. Non-goals (OUT)

- Unit 1's rows: TOOL-dTendedCadence-60. The arm over the shipped descriptor: TOOL-dTendedCadence-63.
- Unit 56's derivation and refusals (S1 to S3): unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-56` — §4 "The set", its Evidence and §6's fixture note, corrected here
- **consumes-from** `TOOL-dTendedCadence-60` — the corrected rows the restated set is derived from

## 4. Design

A table replaces the prose list, because the defect was a set stated with no row behind each member;
a table of row, owner and outcomes lets the next reader check each member against one spec. Written
in this unit's build pass at order 5, before unit 15 (order 7) and unit 1 (order 8) build.

### Files touched (estimate)

- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-56.md`: S1 to S3

## 5. Acceptance criteria

- **AC1** — When `grep -c "as specced" 2026-11-01-spec-TOOL-dTendedCadence-56.md` runs in the spec
  folder, it prints 0, and `grep -n '^| .item.maintain.file.'` over the same file prints a row naming
  `red-leg` and `pending` and not `held`.
  Red when: §4 still asserts a set no row carries.
- **AC2** — When `awk '/^### Evidence/,/^### Inventory/' 2026-11-01-spec-TOOL-dTendedCadence-56.md`
  runs in the spec folder, piped to `grep -c TOOL-dTendedCadence-60`, it prints at least 1; and
  `awk '/^## 6\./,/^- \*\*AC1/'` over the same file, piped to `grep -c TOOL-dTendedCadence-63`, prints
  at least 1. Both print 0 at base: the §3 mirrors this disposal writes sit outside both ranges.
  Red when: the evidence still quotes the uncorrected row, or the fixture reads as the shipped rows.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 14 (HIGH, item H1) of the round-1 spec
  audit of units 49 to 59.

## 9. Reuse audit

No code is written; the seam is spec-56's own §4, corrected in place. The same lookup unit 56 §10
ran found no reader of `[[item]]` routes, so no existing seam fits.

Recall terms used: `python tools/memory-recall/query.py "which routes may a reading carry into the
maintenance record" --terms "route set item rows outcomes routes item.maintain.record refused pending
held red-leg declined"`
