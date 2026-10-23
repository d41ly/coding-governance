# TOOL-dSafePassage-18 — the reverse walk writes no row once a down leaves the receipt below schema 4

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-18-deviation-64.md](../build/2026-10-23-build-TOOL-dSafePassage-18-deviation-64.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md`)
confirmed finding **id 2** at HIGH, merged with id 52 into its item **D-3**. TOOL-dSafePassage-4 downs
`govkit/receipt-schema-4` last (its spec, S3, lines 43-45), and that down sets schema 3 and takes
`steps` out (TOOL-dSafePassage-3 §4, lines 138-140). The reverse walk then re-reads the receipt and
records `rolled-back` through `set_step_state` (TOOL-dSafePassage-4 S4, lines 58-59 and 64-67), which
refuses below schema 4, so every rollback to before the schema step raises `Refusal` after its down
has rewritten the receipt. This unit is id 2's promotion, the reverse walk's half of D-3: a down that
leaves the re-read receipt below schema 4 writes no row, the field's absence is its rolled-back
record, and its verdict goes to the run's rollback record. Id 52's promotion,
`TOOL-dSafePassage-19`, owns what the run does after that down.

## 2. Scope (IN)

- **S1** — The question after the re-read. After each down's spawn and the re-read of the receipt
  (TOOL-dSafePassage-4 S4), `run_reverse_walk` calls `test_steps_recordable`. When it returns False,
  no `set_step_state` call is made for that row. Observed by AC1.
- **S2** — The verdict returned. `run_reverse_walk` returns its verdict list, one `(id, verdict)` per
  row it reached, in the order it reached them, a row whose record could not be written included as
  `rolled-back`. That list is what `write_rollback_record` (TOOL-dSafePassage-4 S6) names each down
  from. Observed by AC1 and AC2.
- **S3** — The walk ends there. The schema step is the reverse set's last row by TOOL-dSafePassage-4's
  order, so a down that lowers the receipt ends the reverse walk; a lowered receipt met before the
  last row is a stop naming the row, `receipt below schema 4 before the last down`, because a later
  down could not be recorded. Observed by AC3.
- **S4** — A kill during the schema step's down. Move 3's `down interrupted:` failure is persisted
  while the receipt is still at schema 4, which the writer accepts. The down is atomic, so a kill
  leaves schema 4 with that failure or schema 3 with no `steps`; the re-run reads either and
  converges, the second through a reverse set whose rows are recorded nowhere and witness-probed
  (TOOL-dSafePassage-4 S4 move 1). Observed by AC2.

## 3. Non-goals (OUT)

- The stamp, the record's last lines and a re-run from a kill after the walk: `TOOL-dSafePassage-19`.
- The forward walk's records below schema 4: `TOOL-dSafePassage-15`.
- How a down is judged reverted: `TOOL-dSafePassage-17`.

### Edges

- **consumes-from** `TOOL-dSafePassage-4` — `run_reverse_walk`, its moves, its re-read and its `rollback` fixture family; without them there is no reverse walk to change
- **consumes-from** `TOOL-dSafePassage-16` — the predicate asked after each re-read; without it the walk would copy the writer's schema test
- **hands-off** `TOOL-dSafePassage-19` — the verdict list, naming the schema step rolled back, which the record and the stamp are written from
- **hands-off** `TOOL-dSafePassage-5` — the rollback of the release-0 tree to before the schema step, which completes only through this rule

## 4. Design

### Data model

TOOL-dSafePassage-4's §4 table gains one row:

| Row before | Down result | Re-read receipt | Row after |
|---|---|---|---|
| `applied` or `failed` | exit 0, reverted | below schema 4 | none written: the field is gone, and the verdict list names it `rolled-back` |

The verdict list: `[(id, "rolled-back" | "skipped" | "STOPPED <failure>"), ...]`, the shape the
record's `down <id>:` lines print (TOOL-dSafePassage-4 §4).

### Inventory

Minted: the return value of `run_reverse_walk`, its verdict list; the stop text
`receipt below schema 4 before the last down`; the `rollback` plants `schema-step` and
`schema-step-kill`. No function, conf key, gate leg or policy key.

### Migration

None.

### Rollout

Live at landing, reached only through `--rollback`. It builds at order 3, after TOOL-dSafePassage-4
and `TOOL-dSafePassage-16` (order 2). Within order 3 it builds before `TOOL-dSafePassage-19`, which
consumes from it.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **The writer accepts a `rolled-back` row below schema 4.** The writer's refusal is the receipt's
  integrity rule; `TOOL-dSafePassage-16` keeps it whole.
- **Downing the schema step outside the reverse walk.** It would be a second spawn path for a step
  argv, which TOOL-dSafePassage-7's callers probe refuses.

## 5. Production-readiness checklist

- security: no new write; the walk writes one row fewer.
- perf / scale: one dictionary read per down.
- error / empty / loading states: a lowered receipt before the last row is a named stop.
- observability: the verdict list feeds the record's `down <id>:` lines.
- risks: a later step whose down also rewrites `schema` would meet S3's stop; none ships.
- testing: the two plants, through the arm of §7.
- migration: none.
- user docs: N/A — the "Rolling back" section TOOL-dSafePassage-4 writes already says a rollback to
  before the schema step ends with that step's down.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant schema-step` runs,
  a scratch gov whose steps file carries a copy of `govkit/receipt-schema-4` first walks a target from
  A to C and reverse-walks it to before that step: the run exits 0, the receipt reads `"schema": 3`
  with no `steps` key, and the returned verdict list names `govkit/receipt-schema-4` `rolled-back`
  last.
  Red when: `set_step_state` is called after the schema step's down and the run raises `Refusal`.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant schema-step-kill`
  runs, the fixture kills the reverse walk during the schema step's down; the receipt reads schema 4
  with that row's `down interrupted:` failure or schema 3 with no `steps`, and the re-run exits 0 with
  the receipt bytes equal to AC1's.
  Red when: the re-run refuses, or its receipt differs from AC1's.
- **AC3** — When the same family runs with `--plant schema-step-early`, a planted row after the
  schema step in walk order whose down also writes schema 3, the reverse walk stops at that row naming
  `receipt below schema 4 before the last down`, and exits 1.
  Red when: the walk downs a further row it cannot record.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the self-test calls `upgrade_steps.py fixture rollback` with the plants `schema-step`, `schema-step-kill` and `schema-step-early`, its failing case staged by a walk copy that records every row whatever the predicate reads · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit's id 2 (HIGH, item D-3,
  shared with id 52).

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-4's `run_reverse_walk`
(`memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-4.md`, S4), with the predicate
`TOOL-dSafePassage-16` exports. `python tools/codebase-map/reuse_lookup.py "skip persisting a progress
row when the receipt schema is too old to hold it"` ranked `rows`, `row`, `skip` and `extract_row`,
name-token matches; no existing seam fits beyond the two specs, which are unbuilt at the base.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
