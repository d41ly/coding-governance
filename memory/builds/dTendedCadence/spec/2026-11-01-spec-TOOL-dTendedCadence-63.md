# TOOL-dTendedCadence-63 — a drift-audit selftest case derives the record's route set from the shipped kit descriptor, never a planted copy

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 5 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 35 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 1 (TOOL-dTendedCadence-60), 14 (TOOL-dTendedCadence-61) and 27
(TOOL-dTendedCadence-62). Unit 56's criteria plant their own `[[item]]` rows, already spelling
`red-leg` (spec-56 §6, :125-128), so no criterion reads `tools/drift-audit/kit.toml` as shipped, and a
descriptor that admits `held` and refuses `red-leg` passes every one. This unit adds the one case that
reads the shipped rows.

## 2. Scope (IN)

- **S1** — The case. `tools/drift-audit/selftest.py` gains one case that calls
  `derive_record_routes(<the kit's own directory>)` (unit 56 S1), the directory `selftest.py` sits in,
  with no copy, and asserts the set contains `in-pin`, `log`, `green`, `filed`, `seen`, `none`,
  `refused`, `pending`, `red-leg`, `declined` and `reported`, and contains none of `held`, `survivor`
  and `survived`. The expected members are the outcomes TOOL-dTendedCadence-61 S1 tabulates, typed
  in the case as its oracle. Observed by AC1.
- **S2** — The failure line. A miss prints the missing and the unexpected members and the descriptor
  path read, so a red names the row to fix. Observed by AC1.

## 3. Non-goals (OUT)

- Writing the rows: unit 1 S1 from TOOL-dTendedCadence-60's corrected table.
- Deriving the oracle from the bodies' return values: no reader of those exists, and the typed set is
  the test's expectation, not a second source the code reads.

### Edges

- **consumes-from** `TOOL-dTendedCadence-56` — `derive_record_routes`, the function the case calls
- **consumes-from** `TOOL-dTendedCadence-60` — the corrected rows, the members the case expects
- **consumes-from** `TOOL-dTendedCadence-1` — the shipped `[[item]]` rows in `tools/drift-audit/kit.toml`, which the case reads at the close

## 4. Design

The case passes `pathlib.Path(__file__).resolve().parent`, the kit's own directory, and builds no
fixture, which is the whole point: every other case of unit 56 reads a copy. Before unit 1 lands its
rows at order 8 the case is red, by S3 of unit 56 (no row routes to the record) or by the missing
members; the close observes it once every unit is built.

### Files touched (estimate)

- `tools/drift-audit/selftest.py`: S1, S2

## 5. Acceptance criteria

- **AC1** — When `python -c "import maintenance; print(sorted(maintenance.derive_record_routes('.')))"`
  runs in `tools/drift-audit/` at the close, its output holds `red-leg`, `refused`, `pending` and
  `declined` and not `held`; and the selftest case of S1, run against a descriptor copy whose
  `item.maintain.file` row routes `held` in place of `red-leg`, fails naming both members and the path.
  Red when: the shipped descriptor admits `held` or refuses a route the walk returns, and no case reads
  it.
  cost: observed at the close, after unit 1 lands the rows.

## 6. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 · the shipped descriptor read in place, staged against an `item.maintain.file` row routing `held` as spec-1 specced it at base · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 35 (HIGH, item H1) of the round-1 spec
  audit of units 49 to 59.

## 9. Reuse audit

The seam extended is unit 56's `derive_record_routes`, called over the real kit directory, and the
drift-audit selftest's case list. `python tools/codebase-map/reuse_lookup.py "derive the outcomes the
item rows route to one item"` named no reader of `[[item]]` routes at base, so no existing seam fits
beyond unit 56's function.

Recall terms used: `python tools/memory-recall/query.py "which routes may a reading carry into the
maintenance record" --terms "route set item rows shipped kit descriptor selftest derive_record_routes
red-leg held"`
