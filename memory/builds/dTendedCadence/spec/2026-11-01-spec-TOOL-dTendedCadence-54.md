# TOOL-dTendedCadence-54 — three cycles of one playbook through the real filing as a drift-audit arm: a closed and built cycle files again, an open one recurs

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 18 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-56 TOOL-dTendedCadence-55 TOOL-dTendedCadence-57 TOOL-dTendedCadence-53 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 40 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
BLOCKER, which shares item B2 with id 15 (TOOL-dTendedCadence-53). Unit 45's risks line covers only
an intake "closed and not built" (spec-45:77-78), and its AC2 files two cycles with no build in
between (spec-45 §6), so no criterion of the set walks a cycle whose repeat build closed and was
built. That is the main path of a cyclic playbook, and it is where the one-key text stops filing.
This unit is the arm that walks it through `write_patch_intake` and a scratch intake store, cycle
after cycle.

## 2. Scope (IN)

- **S1** — The case, in `tools/drift-audit/selftest.py`, over unit 11's `file-weekly` plant and a
  scratch intake store, run three times under `GOV_CADENCE_KEY` `2026-W44`, `2026-W45` and `2026-W46`.
  Between the first and second runs the fixture commits a build README `rB1` naming the first intake's
  content key under `**Caused-by:**`, its status CLOSED. Between the second and third it commits
  `rB2` naming the second intake's key, its status OPEN. Observed by AC1.
- **S2** — What it reads: the store's intakes and receipts, each run's line, and the filer each
  filing records. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- The text and the reader themselves: TOOL-dTendedCadence-53.
- Placing an intake as `repeat`: Entry's, outside this kit.

### Edges

- **consumes-from** `TOOL-dTendedCadence-45` — the repeat filing over unit 11's plant, whose AC2 this arm extends past a built cycle
- **consumes-from** `TOOL-dTendedCadence-53` — `derive_repeat_text` and `read_caused_by_build`, which the arm drives through the real filing
- **hands-off** `TOOL-dTendedCadence-74` — the three-cycle case, which the minors batch re-runs after unit 59 S13 is corrected (review id 40)

## 4. Design

The store is `intake.py`'s, TOOL-dWellOiledMachine-27's, under a scratch git common dir; where it is
absent from the build run's tree the case reports itself not run with that reason, as unit 45 AC2's
fixture line says, and never green. The READMEs are committed in the fixture repository, since
`read_caused_by_build` reads `HEAD`'s tracked files.

### Files touched (estimate)

- `tools/drift-audit/selftest.py`: S1, S2

## 5. Acceptance criteria

- **AC1** — When the case runs, the store holds two intakes for the playbook: the first with one
  receipt, from `2026-W44`; the second, whose text ends `after: rB1`, with two receipts, from
  `2026-W45` and `2026-W46`. The three run lines print `filed`, `filed` and `seen 2026-W46`.
  Red when: the second cycle is absorbed as a receipt on the first intake, or the third, whose build
  is open, files a third intake.
  fixture: `intake.py` is TOOL-dWellOiledMachine-27's, absent at `f4597719`.
- **AC2** — When the case runs, every recorded filer is `playbook-cycle-weekly`, and the count of
  filings recorded under `item.maintain.file` is 0, out of a population of three runs.
  Red when: a repeat cycle is handed on as a survivor breach.

## 6. Gates

`drift-audit selftest` · `memory hygiene`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · three cycles over one plant with a CLOSED then an OPEN committed README, staged against the four-line text with no `after:` line · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 40 (BLOCKER, item B2) of the round-1
  spec audit of units 35 to 48.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 49 to 59 declare toward this unit (units 74); no scope, design or criterion moved.

## 9. Reuse audit

The seam is unit 11's `file-weekly` plant and the drift-audit selftest arm; the case calls unit 53's
functions and unit 8's filing by name. `python tools/codebase-map/reuse_lookup.py "find the build a
request caused and whether it closed"` named no cycle fixture, so no existing seam fits beyond that
plant.

Recall terms used: `python tools/memory-recall/query.py "how does a cyclic playbook file one repeat
intake per cycle once a cycle's build closed" --terms "repeat intake cycle playbook content key
survivor seen Caused-by build closed period-free"`
