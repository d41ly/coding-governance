# TOOL-dSafePassage-15 — the walk persists no step row below schema 4, so a schema-3 receipt reaches the schema step

**Status:** DEFERRED · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-15-deviation-61.md](../build/2026-10-23-build-TOOL-dSafePassage-15-deviation-61.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-16 TOOL-dSafePassage-20 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-22 TOOL-dSafePassage-24 TOOL-dSafePassage-17 TOOL-dSafePassage-23 TOOL-dSafePassage-25 TOOL-dSafePassage-21 TOOL-dSafePassage-26 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 1** at BLOCKER, merged with id 50 into its item **D-1**. TOOL-dSafePassage-2's
walk persists an `interrupted:` `failed` row before every spawn (its spec, S2 move 3, lines 44-45) and
routes every record through `set_step_state` (S3, lines 52-53), which refuses on any receipt below
schema 4. Every existing adopter receipt is at schema 3, and the first pending step on it is
`govkit/receipt-schema-4`, so the walk's first move refuses before that step's up runs and no adopter
reaches schema 4 through `update`. This unit is id 1's promotion, the walk's half of D-1: the walk
asks `TOOL-dSafePassage-16`'s predicate before each record and persists no row while the receipt is
below schema 4. The schema step's own `applied` row is written after its post-spawn re-read, once the
receipt is at schema 4.

## 2. Scope (IN)

- **S1** — The question before each record. `run_step_walk` calls `test_steps_recordable` on its
  in-memory receipt before each of the walk's persists: move 1's and move 5's `applied`, move 2's
  `attended`, move 3's `interrupted:`, move 4's `exit <rc>:` and move 5's `witness does not hold
  after up`. When it returns False, no `set_step_state` call is made and the receipt is not
  rewritten. Observed by AC1 and AC2.
- **S2** — Where an unrecorded verdict goes. A record the walk does not persist prints its step line
  with the suffix `(not recorded: receipt below schema 4)`. A failed or attended verdict is still a
  stop and still a finding of `update`, so the `gov_commit` stamp is withheld as for any stopped walk
  (TOOL-dSafePassage-2 S4). Observed by AC2.
- **S3** — The schema step's row. After `govkit/receipt-schema-4`'s up, the walk's post-spawn re-read
  (TOOL-dSafePassage-2 S3) brings schema 4 and `"steps": []` into memory, the predicate holds, and
  move 5 records the step `applied` through `set_step_state`, with no special case for its id. Every
  later step records as TOOL-dSafePassage-2 specifies. Observed by AC1 and AC4.
- **S4** — A kill during the schema step. Move 3 writes no `interrupted:` row on a schema-3 receipt,
  so a kill there leaves no row. The step's up is `atomic` (TOOL-dSafePassage-3's row), so the
  receipt reads schema 3 or schema 4 whole, and the re-run's move 1 witness decides: schema 4 records
  `applied` without a spawn, schema 3 runs the up again. Observed by AC3.
- **S5** — The fixtures. The `walk` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains the plants `schema-3`, `schema-3-fail` and `schema-3-kill`, whose scratch gov carries a copy
  of `tools/govkit/steps/receipt_schema_4.py` and its row first, and whose target receipt is the one
  `apply` writes forced to schema 3 with `steps` taken out. The `update` family gains
  `schema-3-update`. Observed by AC1 to AC4.

## 3. Non-goals (OUT)

- The predicate and the writer's refusal: `TOOL-dSafePassage-16` and TOOL-dSafePassage-3.
- The reverse walk's records below schema 4: `TOOL-dSafePassage-18`.
- A row for a step that ran on a schema-3 receipt and failed. The receipt cannot hold one, so the
  verdict is output and a finding only; the next run's witness is its recovery.
- The step program's up, down and witness, which stay TOOL-dSafePassage-3's.

### Edges

- **consumes-from** `TOOL-dSafePassage-2` — `run_step_walk`, its five moves, its post-spawn re-read and its `walk` and `update` fixture families; without them there is no walk to change
- **consumes-from** `TOOL-dSafePassage-16` — the predicate the walk asks before each record; without it the walk would copy the writer's schema test
- **hands-off** `TOOL-dSafePassage-5` — the release-0 walk from a schema-3 receipt, which reaches the schema step's up only through this rule
- **hands-off** `TOOL-dSafePassage-11` — its walk from a scratch adopter's receipt to the floor step, which passes the schema step first only through this rule

## 4. Design

### Data model

No new field. The walk's verdict table, beside TOOL-dSafePassage-2's §4 "Data model":

| Receipt in memory before the record | What the walk does |
|---|---|
| the predicate holds | `set_step_state`, then one atomic write, as TOOL-dSafePassage-2 S3 |
| the predicate does not hold | no call, no write, the step line suffixed `(not recorded: receipt below schema 4)` |

A failure the walk could not record is still a stop: the run's findings carry it, so the exit is 1
and `gov_commit` does not move.

### The order on a schema-3 receipt

1. Move 1 runs the schema step's witness, which exits 1 at schema 3 (TOOL-dSafePassage-3 AC5).
2. Move 3 asks the predicate, which is False, and persists nothing.
3. Move 4 runs the up, which writes schema 4 with `"steps": []`.
4. The post-spawn re-read brings that receipt into memory.
5. Move 5 runs the witness, which exits 0, asks the predicate, which is now True, and records
   `govkit/receipt-schema-4` `applied`.

### Inventory

Minted: the step-line suffix `(not recorded: receipt below schema 4)`; the plants `schema-3`,
`schema-3-fail` and `schema-3-kill` of the `walk` family and `schema-3-update` of the `update`
family. No function, conf key, gate leg or policy key.

### Migration

None beyond TOOL-dSafePassage-2's: a schema-3 receipt now walks.

### Rollout

Live at landing. It builds at order 3, after TOOL-dSafePassage-2 and `TOOL-dSafePassage-16` (order 2).
Within order 3 it builds before TOOL-dSafePassage-11, which consumes from it, and it shares
`tools/govkit/upgrade_steps.py` with `TOOL-dSafePassage-18`, `-19`, `-22` and `-24`, so the build run
sequences those passes by M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **The writer's exception for the schema step's row**, offered by id 1's sound fix and rejected by
  id 50's skeptic; see `TOOL-dSafePassage-16` §4.
- **Running the schema step outside the walk**, in `update`'s preamble. It would be a second way to
  run a step, outside TOOL-dSafePassage-7's one spawn site, and a step the walk did not run is not
  recorded by the walk's rules.

## 5. Production-readiness checklist

- security: no new spawn path and no new write; the walk writes less.
- perf / scale: one dictionary read per record.
- error / empty / loading states: an unrecorded failure prints its step line and stops the walk; the
  next run's witness is its recovery.
- observability: the suffix names why a verdict was not recorded.
- risks: a schema step whose up is not atomic would leave a half receipt on a kill; its row declares
  `resume = "atomic"`, and AC3 observes the kill.
- testing: the four plants, through the arm of §7.
- migration: none.
- user docs: N/A — `TOOL-dSafePassage-16` writes the help page's bootstrap rule, and this unit adds
  no operator-visible verb.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant schema-3` runs from a
  schema-3 receipt with no `steps`, it prints `govkit/receipt-schema-4` `applied` after its up and
  every later step `applied`, the receipt reads `"schema": 4` with `steps` whose first row is
  `govkit/receipt-schema-4` `applied`, and it exits 0.
  Red when: a pre-spawn write raises `Refusal`, so the run exits 2 before the up, or the schema
  step's row is missing.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant schema-3-fail` runs
  with the schema step's up planted to exit 1, the run exits 1, prints the step line with
  `(not recorded: receipt below schema 4)`, and the receipt's bytes equal its bytes before the run.
  Red when: the walk attempts any write on the schema-3 receipt, or the receipt changes.
- **AC3** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant schema-3-kill` runs,
  the fixture kills the walk and the step after the up's temporary file is written; the receipt then
  reads schema 3 or schema 4 whole, and the re-run walk exits 0 with the receipt and target bytes
  equal to AC1's.
  Red when: the re-run refuses, or its bytes differ from an uninterrupted walk's.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture update --plant schema-3-update`
  runs, the scratch gov's `govkit.py update --target <t> --write` over a target whose receipt `apply`
  wrote and the fixture forced to schema 3 exits 0, and the receipt reads schema 4 with the schema
  step `applied`; run again with the schema step killed during its up, the re-run exits 0 with the
  same receipt bytes.
  Red when: any pre-spawn write refuses on the schema-3 receipt.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 · the self-test calls `upgrade_steps.py fixture` for the `walk` plants `schema-3`, `schema-3-fail`, `schema-3-kill` and the `update` plant `schema-3-update`, its failing case staged by a walk copy that skips the predicate · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 1 (BLOCKER, item
  D-1, shared with id 50).

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-2's `run_step_walk` and its post-spawn re-read
(`memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-2.md`, S2 and S3), with the
predicate `test_steps_recordable` that `TOOL-dSafePassage-16` exports beside the writer. `python
tools/codebase-map/reuse_lookup.py "skip persisting a progress row when the receipt schema is too old
to hold it"` ranked `rows`, `row`, `skip` and `extract_row`, name-token matches; the walk is unbuilt
at the base, so no existing seam fits beyond the two specs named. The recall probe found
`TOOL-cMendedVintage-19`, which places this repair at order 3, one above the walk it repairs.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
