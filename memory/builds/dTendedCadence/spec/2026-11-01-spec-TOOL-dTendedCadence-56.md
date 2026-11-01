# TOOL-dTendedCadence-56 — the record's route set derived from the outcomes the item rows route to `item.maintain.record`, and the red leg's hold spelled `red-leg`

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 4 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-55 TOOL-dTendedCadence-57 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 16 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
HIGH, item H2. Unit 37 S2 closes the stdin route set at ten typed values and calls it "the union of
the outcomes the siblings already name" (spec-37 S2, §4 Inventory, :31-35, :65). It omits `refused`,
which unit 8's `write_patch_intake` returns, and `none`, which unit 1's item table routes from
`item.maintain.patch` and `item.maintain.file` to the record (spec-1 §4 "The rows"). A route outside
the set exits 2 before the write, so one refused patch filing stops every later wake's record. The set
also reuses `held`, unit 3's owner-gated direct outcome (spec-3 S3, :69-70). This unit derives the set
from the item rows, never types it, and gives the red leg's hold a name of its own.

## 2. Scope (IN)

- **S1** — The derivation. `derive_record_routes(kit_dir)` in `tools/drift-audit/maintenance.py`
  reads the `[[item]]` rows of `<kit_dir>/kit.toml` with `tomllib` and returns every outcome whose
  `routes` entry names `item.maintain.record`, the row schema TOOL-dDeclaredLoop-12 §4 "Data model"
  gives. Unit 37 S2's typed set is not written; `render_maintenance_record` refuses a reading whose
  `route` is outside the derived set, exit 2 before a write, naming the route and the set. Observed by
  AC1 and AC2.
- **S2** — The red leg's hold. The route under which a breach reaches the record as an `over-pin:`
  line is `red-leg`, the `maintain.on-breach` value that holds it, and unit 37 S1's derivation keys
  on `red-leg`. `held` stays unit 3's direct outcome alone, which routes to `item.maintain.file` and
  so never reaches the record. Observed by AC1.
- **S3** — The dead derivation. A readings list that is not empty, read beside no `[[item]]` row
  routing to `item.maintain.record`, exits 2 with `maintenance — refused: no item row routes to
  item.maintain.record in <kit_dir>/kit.toml`, never a write that admits every route. An empty
  readings list, the security review's, needs no route. Observed by AC3.
- **S4** — The docs. The drift-audit README's maintenance record section says the route set is the
  item rows' and names `red-leg`. Observed by AC4.

## 3. Non-goals (OUT)

- The item rows themselves: unit 1 S1, unit 3 S3 and unit 46 S2 write them; S1 reads them.
- Returning `red-leg` from `run_breach_route`: unit 15 S3's, handed off below.
- Declaring `refused` on `item.maintain.patch`: unit 1's row, handed off below.
- Which readings take `red-leg`: unit 15 S1 to S3 and unit 17 S11, unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-37` — `render_maintenance_record`'s typed route set and its `held` derivation, which this unit derives from the item rows and keys on `red-leg`
- **hands-off** `TOOL-dTendedCadence-15` — `run_breach_route`'s hold under `maintain.on-breach: red-leg`, whose route that unit returns as `red-leg`
- **hands-off** `TOOL-dTendedCadence-1` — the `[[item]]` rows, whose `item.maintain.patch` row declares `refused` routed to `item.maintain.record`, so a refused filing reaches the record
- **hands-off** `TOOL-dTendedCadence-51` — the route `red-leg`, whose readings' keys that unit's round trip compares as `over-pin:` lines
- **hands-off** `TOOL-dTendedCadence-60` — the derived route set and the `red-leg` hold, which that unit makes unit 1's rows route to the record (review id 1)
- **hands-off** `TOOL-dTendedCadence-61` — §4 "The set", its Evidence and §6's fixture note, which that unit corrects in place (review id 14)
- **hands-off** `TOOL-dTendedCadence-62` — the hold's name `red-leg`, which that unit makes unit 15's text return throughout (review id 27)
- **hands-off** `TOOL-dTendedCadence-63` — `derive_record_routes`, which that unit's case calls over the shipped descriptor (review id 35)
- **hands-off** `TOOL-dTendedCadence-74` — `derive_record_routes` over the one row reader, and §10, repaired by the minors batch (review ids 2, 3, 15, 23)

## 4. Design

### The set

```
derive_record_routes(kit_dir):
    rows = tomllib.load(<kit_dir>/kit.toml).get("item", [])
    return { outcome for row in rows for outcome, target in row["routes"].items()
             if target == "item.maintain.record" }
```

Read over the rows as specced, the set is `in-pin`, `log`, `green`, `fixed`, `filed`, `seen`, `none`,
`pending`, `reported`, `refused` and `red-leg`. `survived`, `survivor` and `held` route to
`item.maintain.file`, whose own outcome is the one the record sees, so none of them is a record route.
A sibling that adds an outcome routed to the record adds it to the set by adding it to its row.

The rename of the hold touches no code in the tree: unit 15's route and unit 37's derivation are both
unbuilt at base, so every reader of the name is a spec of this build, and each is joined by an edge
above or by unit 37's own.

### Evidence

- Spec-1 §4 "The rows": `item.maintain.patch` routes `filed`, `seen`, `none` and `item.maintain.file`
  routes `filed`, `seen`, `held`, `reported`, `none` to `item.maintain.record`.
- Spec-8 §4 returns `refused` from `write_patch_intake`, and finding id 16's skeptic confirmed it.
- Spec-3 S3 gives `item.maintain.direct` the outcomes `fixed`, `survived` and `held`, `held` routed to
  `item.maintain.file`; spec-46 S2 adds `filed` and `seen`, routed to the record.
- Refuted finding 4 of the same report: no reading reaches the record with route `none` today. The
  derivation admits it anyway, because the rows route it there.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_record_routes` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `red-leg` | record route, the red leg's hold | none |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1, S2, S3
- `tools/drift-audit/selftest.py`: the cases of §6
- `tools/drift-audit/README.md`: S4

### Alternatives rejected

- **Add `refused` and `none` to unit 37's typed set.** The next sibling outcome reds the record again;
  the rows already hold the answer.
- **Map every item outcome to a record route in `run_maintain`.** A second table beside the rows'
  `routes`, two answers to one question.

## 5. Production-readiness checklist

- security — the write boundary keeps its deny-by-default shape: a route outside the derived set, and
  any route read beside no row, exits 2 before a write.
- perf / scale — one `tomllib` read of the kit descriptor per write.
- error / empty / loading states — an unknown route and a dead derivation each exit 2 naming
  themselves; an empty readings list writes as before.
- observability — the refusal names the route and the derived set.
- risks — the descriptor holds no `[[item]]` row until unit 1 lands at order 8, so a write between
  orders 4 and 8 with readings refuses; only fixtures write then, and they plant rows.
- testing — the criteria of §6, in the arm unit 6's §7 declares.
- migration — N/A — no record exists at base.
- user docs — N/A — the record's grammar is the kit README's, S4.

## 6. Acceptance criteria

The fixture is unit 37's, its kit descriptor copied with three planted `[[item]]` rows: `item.maintain.read`
routing `in-pin` and `log`, `item.maintain.patch` routing `filed` and `refused`, and
`item.maintain.file` routing `red-leg` and `filed` to `item.maintain.record`, and `survivor` to
`item.maintain.file`.

- **AC1** — When `python maintenance.py write --key 2026-11-01 --base <sha>` runs with stdin holding
  one reading routed `log`, one `refused` and one `red-leg` with one key, it writes the record, and
  `grep -c '^over-pin:'` over it prints 1.
  Red when: a refused filing exits 2, or a reading routed other than `red-leg` writes an `over-pin:`
  line.
- **AC2** — When the same command runs with one reading routed `survivor`, and then one routed
  `held`, it exits 2 each time naming the route, and no file is written.
  Red when: a route no row sends to the record is written through.
- **AC3** — When the same command runs with the planted rows removed and one reading routed `log`, it
  exits 2 with `no item row routes to item.maintain.record`; with `"readings": []` it writes.
  Red when: an empty derivation admits every route, or refuses a record with no readings.
- **AC4** — When `grep -n "red-leg" README.md` runs in `tools/drift-audit/`, it matches inside the
  maintenance record section.
  Red when: the README still names a typed route set.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 AC3 · planted item rows and stdin routes `log`, `refused`, `red-leg`, `survivor` and `held`, staged against unit 37's typed set · none

## 8. Open questions

- **F1 — Which hold gets the new name?** Options: (a) the red leg's, `red-leg`; (b) unit 3's
  owner-gated direct outcome. (b) renames an outcome unit 3 S3 and unit 46 S1 both spell, and the
  record never sees it; (a) renames the one route the record reads. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the narrower change. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 16 (HIGH, item H2) of the round-1 spec
  audit of units 35 to 48.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 49 to 59 declare toward this unit (units 60, 61, 62, 63, 74); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is unit 6's `render_maintenance_record` with unit 37's derivation, and the row
schema of TOOL-dDeclaredLoop-12, read rather than restated. `python tools/codebase-map/reuse_lookup.py
"derive the outcomes the item rows route to one item"` ranked name stems only, `rows`, `row`,
`extract_row` (`tools/memory-tree/backlog.py`) and `derive_scope`, none a reader of `[[item]]`
routes; the loop kit's `read_items` is specced and unbuilt at base and reads `tools/loop/loop.toml`
only (unit 1 §8 F1, :279), so no existing seam fits and the read is one `tomllib` comprehension.

Recall terms used: `python tools/memory-recall/query.py "which routes may a reading carry into the
maintenance record" --terms "route set item rows outcomes routes item.maintain.record refused none
held red-leg over-pin derive"`
