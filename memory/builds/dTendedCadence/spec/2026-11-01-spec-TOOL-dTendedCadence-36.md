# TOOL-dTendedCadence-36 — the Maintain walk refuses a key no record family admits before any item takes a side effect

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 9 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 39 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, which shares item H1 with id 1 (TOOL-dTendedCadence-35). Id 39 is the failure envelope of the
refused key: unit 1's walk reaches `item.maintain.record` last (spec-1 S2, S6), after
`item.maintain.file` has filed and `item.maintain.direct` has fixed, so a key the writer refuses
exits 2 at the record step, the walk exits 1, `run_cadence_period` releases the lease as a hand-over
(TOOL-dWellOiledMachine-13 S6 step 5), and every next wake repeats the period's filings and fixes and
writes no record. Unit 35 widens the grammar; this unit moves the key's test to the walk's first act,
so a key the record step would refuse is refused before any side effect, on every wake, and says so.

## 2. Scope (IN)

- **S1** — The test. `run_maintain(root, key, dry_run)` in `tools/drift-audit/maintain.py` calls
  `derive_record_family(key)` (TOOL-dTendedCadence-35 S2) once, before the first item of the walk and
  under `--dry-run` too. None exits 2 with `maintain — refused: key <key> is no record-key family; no
  item ran`, and no item body runs: nothing is read, filed, fixed or written. Observed by AC1 and AC2.
- **S2** — The family on the item line. `item.maintain.lease`'s `taken` line names the family,
  `maintain — <key> · item.maintain.lease · taken (<family>)`, so a run's log says which family its
  record will be written under. Observed by AC1.
- **S3** — The planted cases in the drift-audit selftest arm unit 1's §7 declares, with stub item
  bodies that record each call. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The grammar itself: TOOL-dTendedCadence-35, id 1 of the same item.
- What `run_cadence_period` does with a non-zero exit. It releases a hand-over on any non-zero exit;
  this unit makes that re-run harmless and does not change the lease.
- The node pass's own key handling: TOOL-dTendedCadence-16's `--scope node` argv calls the same
  `run_maintain`, so it takes this test unchanged.

### Edges

- **consumes-from** `TOOL-dTendedCadence-1` — `maintain.py` and `run_maintain`, the walk whose first act this unit adds; without it there is no walk to guard
- **consumes-from** `TOOL-dTendedCadence-35` — `derive_record_family`, the classifier the walk calls; without it the walk would re-type the writer's grammar
- **hands-off** `TOOL-dTendedCadence-59` — the Files touched line of the docs edit, which the minors batch repairs (review id 38)

## 4. Design

### Evidence

- Spec-1 S2 runs the items in `order_by_needs` order and exits 1 when an item body raises or refuses;
  S6 runs the writer last; spec-1 AC7 already asserts that the walk commits nothing.
- Spec-6 S6 exits 2 on a key outside its grammar "before a write", which is the record step's exit,
  not the walk's.
- TOOL-dWellOiledMachine-13 S6 step 5 releases with no `--as` on any exit other than 0.

### Inventory

Minted: nothing. The refusal line and the `(<family>)` suffix are output of existing functions.

### Files touched (estimate)

- `tools/drift-audit/maintain.py`: S1, S2
- `tools/drift-audit/selftest.py`: S3

### Alternatives rejected

- **A second copy of the families in `maintain.py`.** Two spellings of one grammar drift, which is the
  defect id 1 found between unit 6 and its siblings.
- **Test the key in `item.maintain.record` only, and skip filing on a refused key.** The record step
  runs last by its `needs`, so every earlier side effect has already run when it learns the key.

## 5. Production-readiness checklist

- security — N/A — no new write path; the change removes side effects from a refused run.
- perf / scale — one `re.fullmatch` per family per run.
- error / empty / loading states — a refused key prints one line and exits 2; no key at all keeps
  unit 1 S3's `refused: no key` line, tested first.
- observability — the `taken (<family>)` line and the refusal line.
- risks — a refused key still re-runs on every wake under the hand-over rule, now with no effect; the
  refusal line in each wake's output is how the owner sees it.
- testing — the criteria of §6, in the arm unit 1's §7 declares.
- migration — N/A — the walk is new in this build.
- user docs — `help/maintain.md`'s section "The Maintain run" names the refusal line in one sentence.

## 6. Acceptance criteria

- **AC1** — When `GOV_CADENCE_KEY=2026-11-01 python maintain.py --dry-run` runs over unit 1's walk
  fixture, its lease line reads `taken (daily)`; with `GOV_CADENCE_KEY=2026-11-01.node-a` it reads
  `taken (node)`.
  Red when: the line names no family, or names the wrong one.
- **AC2** — When `GOV_CADENCE_KEY=2026-11-01/x python maintain.py` runs over the same fixture with
  recording stub bodies for every item, it exits 2 with `no item ran`, the stubs record no call, and
  `git status --porcelain` is empty.
  Red when: any item body runs before the key is refused, or the refusal exits 1.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · the walk fixture under an admitted and a refused key with recording stubs, staged against a walk that tests the key at the record step · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 39 (HIGH, item H1) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (unit 59); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is unit 1's `run_maintain` in `tools/drift-audit/maintain.py`, and the classifier
called is unit 35's `derive_record_family`. `python tools/codebase-map/reuse_lookup.py "validate a
record key at the write boundary so no key becomes a path"` ranked name stems only (`key`, `write`,
`keys`, `write_text`), none a walk guard, and neither module exists at base, so no existing seam fits
beyond those two units. The recall probe surfaced TOOL-cMendedVintage-19, the placement ruling this
unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
