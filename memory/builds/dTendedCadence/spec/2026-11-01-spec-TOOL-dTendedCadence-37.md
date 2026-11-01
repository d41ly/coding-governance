# TOOL-dTendedCadence-37 — the maintenance record's `over-pin:` lines derived from the route a reading reached, never from its `over` flag

**Status:** DEFERRED · rev-3 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 3 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 2 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H2. Unit 6 writes `over-pin:` as "the `keys` of every reading with `over` true"
(spec-6 §4, :224-225). Unit 8 S5 sets `over` on every live pinned reading over its pin, which includes
unit 14's log band, `route = "ask"` readings already filed (unit 17 S11, unit 16 S8) and offenders a
direct fix just cleared. Unit 15's red leg counts every `over-pin:` line, so under
`maintain.on-breach: red-leg` it reds on readings the bands absorbed, and the AC7 of units 16 and 17
("the red leg stays green") cannot pass. The stdin already carries each reading's `route`
(spec-6:222); this unit derives the lines from it.

## 2. Scope (IN)

- **S1** — The derivation. `render_maintenance_record` in `tools/drift-audit/maintenance.py` writes
  one `over-pin:` line per key of each stdin reading whose `route` is `held`, and none for any other
  route, `over` true or not. Observed by AC1 and AC2.
- **S2** — The contract the line rests on, stated in unit 6's stdin grammar beside `route`: `route` is
  the outcome the walk reached for that reading, one of `in-pin`, `log`, `fixed`, `survived`, `filed`,
  `seen`, `pending`, `held`, `reported` or `survivor`, and the `keys` of a `held` reading are the
  keys the route held, never the keys read before a fix ran. A `route` outside that set exits 2 before a write, as a line
  value carrying a break does. Observed by AC2.
- **S3** — `on-finding` keeps reading `over` and `live` (unit 6 §8 F5): a finding is still a reading
  over its pin or not live, so a log-band run is recorded, and its record carries no `over-pin:` line.
  Observed by AC1.

## 3. Non-goals (OUT)

- Which route a breach takes: TOOL-dTendedCadence-15 S1 to S3 (`held` under `red-leg`) and
  TOOL-dTendedCadence-17 S11 (`route = "ask"` never `held`).
- Which record the red leg reads: TOOL-dTendedCadence-43.
- The Readings table's Route column: it already prints the stdin `route` and is unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-6` — `render_maintenance_record` and its stdin grammar, whose `over-pin:` derivation this unit replaces
- **hands-off** `TOOL-dTendedCadence-1` — the stdin `route` set and the rule that a `held` reading's `keys` are the keys the route held, which `item.maintain.record`'s input must carry
- **hands-off** `TOOL-dTendedCadence-56` — `render_maintenance_record`'s typed route set and its `held` derivation, which that unit derives from the item rows and keys on `red-leg` (review id 16)
- **hands-off** `TOOL-dTendedCadence-59` — the stdin `route` naming, which the minors batch repairs (review id 3)
- **hands-off** `TOOL-dTendedCadence-74` — AC1, its arm and the hold's spelling, corrected to `red-leg` by the minors batch (review ids 2, 3, 15)

## 4. Design

### Evidence

- Spec-6:221-225 gives stdin `{"read", "readings": [{"reading", "value", "of", "live", "over",
  "route", "keys"}], "fields"}` and derives `over-pin:` from `over`.
- Spec-15 S3: under `red-leg` "nothing is filed, route `held`; the offender reaches the record as an
  `over-pin:` line". Spec-15 S1 names the four routes `filed`, `seen`, `held`, `reported`.
- Spec-1 S4 and S6: `in-pin` and `log` route to the record; spec-3 S3 adds `fixed` and `survived`,
  spec-8 S7 adds `survivor`, and spec-17 S11 adds `pending`.

### Inventory

Minted: nothing. The route set is the union of the outcomes the siblings already name.

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1, S2
- `tools/drift-audit/selftest.py`: the cases of §6
- `tools/drift-audit/README.md`: the maintenance record section states the derivation

### Alternatives rejected

- **Keep `over` and subtract the log band and `ask` rows in the leg.** The leg would re-derive two
  siblings' routing from row keys, a second copy of a decision the walk already made and recorded.

## 5. Production-readiness checklist

- security — N/A — no new write path; the route set narrows what stdin may carry.
- perf / scale — N/A — one string compare per reading.
- error / empty / loading states — an unknown route exits 2 before a write; a reading with no keys
  and route `held` writes no line.
- observability — the Readings table still shows every route, so a held reading is visible beside
  the lines it wrote.
- risks — a walk that passes `held` for a cleared offender writes a false line; S2's contract on
  `keys` is the guard, and unit 1's AC7 fixture is where it is observed.
- testing — the criteria of §6, in the arm unit 6's §7 declares.
- migration — N/A — no record exists at base.
- user docs — N/A — the record's grammar is the kit README's.

## 6. Acceptance criteria

- **AC1** — When `python maintenance.py write --key 2026-11-01 --base <sha>` runs with stdin holding
  one reading `over` true with route `log`, one `over` true with route `filed`, and one with route
  `held` and one key, under `record-when = "on-finding"`, it writes the record, and `grep -c
  '^over-pin:'` over it prints 1, the held key.
  Red when: a log-band or filed reading writes an `over-pin:` line, or a held one writes none.
- **AC2** — When the same command runs with one reading whose route is `page`, it exits 2 naming
  the route, and no file is written.
  Red when: an unknown route is written through.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · stdin planting `log`, `filed` and `held` readings and one unknown route, staged against the `over`-derived lines · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 2 (HIGH, item H2) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (units 56 and 59); no scope, design or criterion moved.
- rev-3 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 49 to 59 declare toward this unit (units 74); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is unit 6's `render_maintenance_record` in `tools/drift-audit/maintenance.py` and
its stdin grammar (spec-6:221-225); the route values are the siblings' own (spec-15 S1, spec-3 S3,
spec-8 S7). `python tools/codebase-map/reuse_lookup.py "file a records-only intake so a written record
is committed and landed"` ranked `records`, `corpus_files`, `extract_records` and `read_records`, none
a route-aware record writer, so no existing seam fits beyond unit 6's own module, absent at base.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
