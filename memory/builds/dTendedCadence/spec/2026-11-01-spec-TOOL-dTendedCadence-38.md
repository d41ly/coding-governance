# TOOL-dTendedCadence-38 — the `[[reading]]` key `route` and its closed value set `ask | patch | file`, owned once by the registry's check

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 14 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 4 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H3. The same defect at medium is item M11, ids 21 and 49, which TOOL-dTendedCadence-48
carries; the report asks the two fixed as one change, and this unit is that change's mechanism. Three
units define `route` incompatibly: unit 8 mints it with `patch | file` and refuses anything else
(spec-8 :127, :152); unit 17 "adds" it with the one value `ask` and its AC10 refuses `file`
(spec-17 S11, AC10, :123-125, :285); unit 9 "adds" `patch` to unit 17's key (spec-9 S4, :78-79).
Built in order, unit 8's check refuses the `route = "ask"` rows of units 16 and 17, and unit 17's
AC10 refuses the `file` default unit 8 uses. This unit gives the key one owner and one closed set.

## 2. Scope (IN)

- **S1** — The set. `ROUTE_VALUES` in `tools/drift-audit/readings.py`, one row per value with its
  meaning, per §4 "The values": `ask`, `patch` and `file`, the default `file` when a row declares
  neither `route` nor `fix`. Observed by AC1.
- **S2** — The check. `check_reading_rows` reads `ROUTE_VALUES` and nothing else for `route`: a value
  outside it, or `ask` or `patch` beside a `fix`, is `<name>: route <value> …`, as unit 8's table
  states the finding; `file` beside a `fix` is refused too, since a fix decides its own route
  (TOOL-dTendedCadence-3 S2). The `route = "ask"` branch of `run_breach_route` (unit 17 S11) and the
  `patch` answer of `derive_fix_route` (unit 9 S4) read the row's value and add none. Observed by AC1
  and AC2.
- **S3** — The cases. Unit 17 AC10's refusal case becomes an unknown value, `route = "page"`; a
  `route = "ask"` row passes the check; a `route = "file"` row with no fix passes. Observed by AC1 and
  AC2.

## 3. Non-goals (OUT)

- Each value's routing at the walk: `file` is unit 15's `item.maintain.file`, `patch` unit 8's
  `item.maintain.patch` through unit 3's `derive_fix_route`, `ask` unit 17's branch of
  `run_breach_route`. This unit owns the key and the set, not the branches.
- The rows that declare a value: units 9, 16 and 17 keep their rows as written.

### Edges

- **consumes-from** `TOOL-dTendedCadence-8` — `check_reading_rows` and `readings.py`, the check whose `route` finding this unit re-keys on one set
- **consumes-from** `TOOL-dTendedCadence-17` — the `route = "ask"` row and its AC10 case, which this unit re-states against the closed set
- **hands-off** `TOOL-dTendedCadence-9` — `ROUTE_VALUES`, the set whose `patch` value that unit's sweep row declares and cites, never adds
- **hands-off** `TOOL-dTendedCadence-48` — `ROUTE_VALUES`, which that unit's S11 and S12 cite from the row comment, the README and units 17 and 9 (review ids 21, 49)
- **hands-off** `TOOL-dTendedCadence-59` — the title's pipes and the §1 citations, which the minors batch repairs (review ids 12, 23)

## 4. Design

### The values

| Value | Meaning | Beside a `fix` |
|---|---|---|
| `file` | the breach goes to `item.maintain.file` under `maintain.on-breach`; the default | refused |
| `patch` | the offender goes to `item.maintain.patch` as a keyed patch intake | refused |
| `ask` | the breach is filed as an ask under every `maintain.on-breach` value, never `held` or `reported` | refused |

A row with a `fix` declares no `route`: unit 3's `derive_fix_route` answers its fix's route when the
fix is in `maintain.fixes`, else `file`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `ROUTE_VALUES` | module constant, `readings.py` | none |

### Files touched (estimate)

- `tools/drift-audit/readings.py`: S1, S2
- `tools/drift-audit/selftest.py`: S3
- `tools/drift-audit/README.md`: the registry section's `route` row lists the three values

### Alternatives rejected

- **Each unit adds its value where it lands.** That is the defect: three specs each claim to add the
  key, and the check refuses the value the next one needs.

## 5. Production-readiness checklist

- security — N/A — a closed set read at the registration check, narrower than either spec alone.
- perf / scale — N/A — a set lookup per row.
- error / empty / loading states — a missing `route` takes `file`; an unknown one is a `# readings:`
  finding that reds `--check`.
- observability — the finding names the row and the value.
- risks — a fourth value later needs one row here and its branch where it routes.
- testing — the criteria of §6.
- migration — N/A — the registry is new in this build.
- user docs — N/A — the row grammar is the kit README's.

## 6. Acceptance criteria

- **AC1** — When `check_reading_rows` reads planted rows `route = "ask"`, `route = "patch"` and
  `route = "file"`, each with no `fix`, through `python drift_report.py --check` over a fixture
  descriptor, it prints no `# readings:` route finding.
  Red when: any of the three is refused.
- **AC2** — When the planted rows are `route = "page"` and `route = "ask"` beside `fix = "reap"`, the
  same run prints `# readings: <name>: route page …` and a route finding for the second row, and
  exits 1.
  Red when: an unknown value or a route beside a fix is admitted.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · planted rows for each value, an unknown value and a route beside a fix, staged against a check that admits `patch` and `file` only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 4 (HIGH, item H3) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (unit 59); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is unit 8's `check_reading_rows` in `tools/drift-audit/readings.py` (spec-8 §4 "The
check"), whose `route` row this unit re-keys on one table. `python tools/codebase-map/reuse_lookup.py
"validate a record key at the write boundary so no key becomes a path"` ranked name stems only and
named no row-value registry; `readings.py` does not exist at base, so no existing seam fits beyond
unit 8's own module.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
