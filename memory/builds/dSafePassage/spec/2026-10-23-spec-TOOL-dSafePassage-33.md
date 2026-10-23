# TOOL-dSafePassage-33 — a missing before-image means "never ran" only for a row the forward walk applied by witness alone, recorded as such

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-33-deviation-79.md](../build/2026-10-23-build-TOOL-dSafePassage-33-deviation-79.md) | deviation | — |
| [2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-32 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-31 TOOL-dSafePassage-34 TOOL-dSafePassage-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 15 to 26
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`)
confirmed finding **id 40** at HIGH, its item **D-6**. TOOL-dSafePassage-17 S2's fourth bullet and its
S3 read "no before-image at the down's spawn" as reverted on the down's exit 0, and
`write_from_before_image` then exits 0 having written nothing. Its §5 risks line asserts that such a
down "wrote nothing on the up side either". The image can be absent after an up that wrote:
TOOL-dSafePassage-2 S11 stages the image and never commits it, so a discarded index loses it, and
TOOL-dSafePassage-26 S23 deletes gov's own template-size image once its witness holds. TOOL-dSafePassage-1
§4 "The before-image" says each up writes its image first, so "absent" means "never ran" only for a
row applied by witness alone. A rollback over a row whose image went missing then records
`rolled-back` and reports success while the up's writes remain. This unit is id 40's promotion: the
forward walk records which rows it applied by witness alone, and only those rows, or rows the receipt
records nothing for, take the no-image rule.

## 2. Scope (IN)

- **S1** — The mark. TOOL-dSafePassage-3's step row gains an optional `"via": "witness"`, legal only
  on an `applied` row, meaning the forward walk recorded the step `applied` at move 1 of
  TOOL-dSafePassage-2 S2, its `up` never spawned. `set_step_state` takes `via=None`, raises `Refusal`
  on any other value and on a `via` with a state other than `applied`, and writes the key only when
  given. `read_step_states` refuses the same rows. Observed by AC1.
- **S2** — The writer's callers. `run_step_walk`'s move 1 passes `via="witness"`; its move 5, after
  an up, passes nothing, so a row rewritten by a later walk carries the mark only when that walk
  applied it by witness. The source-mode walk of TOOL-dSafePassage-8 calls the same moves. Observed
  by AC1.
- **S3** — The scoped rule. `derive_down_verdict` (TOOL-dSafePassage-17 S2) reads the row's last record
  beside `image_present`. With no `reverted` and no image, the down's exit 0 decides only when the
  record is `applied` with `via` `witness`, or the receipt holds no row for the step. With no
  `reverted`, no image, and an `applied` record without `via`, the witness decides, as it does with an
  image present. When it still holds, the row stops with the failure
  `witness still holds after down; before-image <path> absent`, naming the image path. Observed by
  AC2, AC3 and AC4.
- **S4** — Why a row with no record takes the rule. TOOL-dSafePassage-19 S4's re-run after a kill
  reads a receipt the schema step's down left with no `steps`. In the reverse order every other down
  ran before that one and cleared its own image, so a row with no record and no image is one already
  downed or one applied by witness, and its down writes nothing either way. Observed by AC4.
- **S5** — The docs. The receipt section of `help/upgrade-steps.md`, which TOOL-dSafePassage-3 S8
  writes, names `via`; its "Rolling back" section says a row whose up ran and whose image is missing
  stops the rollback, naming the image. Observed by AC5.

## 3. Non-goals (OUT)

- Writing an image for every up, an empty one included. TOOL-dSafePassage-3 §8 F5 resolved that the
  schema step writes none, so the rule cannot rest on every up having one.
- Restoring a lost image. The stop names it, and an operator decides.
- The re-run's second downs over the shipped rows and their criterion: findings 42 and 11, carried by
  the minors batch `TOOL-dSafePassage-35`.

### Edges

- **consumes-from** `TOOL-dSafePassage-17` — `derive_down_verdict` and its no-image rule, which this unit scopes; without them there is no rule to narrow
- **consumes-from** `TOOL-dSafePassage-3` — `set_step_state`, `read_step_states` and the step row grammar, which gain the optional mark; without them the walk has nowhere to record how a row was applied
- **consumes-from** `TOOL-dSafePassage-2` — `run_step_walk` and its move 1, the one place a row is applied by witness alone; without it no caller passes the mark
- **hands-off** `TOOL-dSafePassage-35` — the re-run's second downs over the shipped row shapes, which take this unit's no-record branch
- **hands-off** `TOOL-dSafePassage-39` — the mark carried by the one writer across every rewrite that keeps a row `applied`, and the reverse walk's move 3 marking an unrecorded row, the repair of finding 23 of the spec audit of units 27 to 35
- **hands-off** `TOOL-dSafePassage-40` — move 1's mark set only when the walk-start receipt holds no record for the step and no before-image is on disk, the repair of finding 29 of the spec audit of units 27 to 35

## 4. Design

### Data model

The step row after this unit:

```json
{"id": "agent-cap/fanout-cap-to-agents-in-flight", "introduced": "<sha>", "state": "applied", "via": "witness"}
```

The down's verdict, TOOL-dSafePassage-17 §4's table with this unit's split of its last row:

| Row | Image at spawn | Last record | Down | Judged by | Row after |
|---|---|---|---|---|---|
| `reverted = "down-exit"` | either | any | exit 0 | the down | `rolled-back` |
| `reverted` an argv | either | any | exit 0 | that argv | `rolled-back` on its exit 0 |
| no `reverted` | present | any | exit 0 | the witness | `rolled-back` when it does not hold |
| no `reverted` | absent | `applied`, `via` `witness`, or none | exit 0 | the down | `rolled-back` |
| no `reverted` | absent | `applied`, no `via` | exit 0 | the witness | `rolled-back` when it does not hold, else stop naming the image |

### Inventory

Minted: the row key `via` and its one value `witness`; the failure text
`witness still holds after down; before-image <path> absent`; the `rollback` plant `image-lost`. No
function, conf key, gate leg or policy key. `set_step_state`'s new refusal joins its existing
`raise Refusal` branch, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

Additive: the key is optional, and no receipt at the base records a step.

### Rollout

Live at landing. It builds at order 5, after TOOL-dSafePassage-17 (order 4), the last of the three
units whose code it amends.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **An empty before-image for every up.** It contradicts TOOL-dSafePassage-3 §8 F5's resolved fork
  for the schema step.
- **Reading a missing image as a stop for every row.** The two legacy-home rows on an adopter that
  never held the file could never roll back, the blocker TOOL-dSafePassage-17 exists to close.

## 5. Production-readiness checklist

- security: no new write path; the receipt gains one optional key through its one writer.
- perf / scale: unchanged.
- error / empty / loading states: a lost image now stops the rollback by name instead of passing.
- observability: the failure names the image path.
- risks: a row applied by its up whose image was lost cannot roll back until an operator restores the
  image or reverts the up's writes by hand; that is the price of never recording a false
  `rolled-back`.
- testing: the plant of §6 beside TOOL-dSafePassage-17's, through §7.
- migration: additive.
- user docs: `help/upgrade-steps.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture walk --plant witness-holds` runs,
  the receipt's row for the planted step reads `"via": "witness"`; after `--plant fail-k`'s rows that
  ran their up, none carries `via`; and a `python -c` probe calling `set_step_state` with
  `via="witness"` and state `failed` raises `Refusal`.
  Red when: a row applied by its up carries the mark, or the writer accepts a mark off `applied`.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant image-lost` runs,
  a row whose up wrote a file and its image is recorded `applied` with no `via`, the image is then
  deleted, and the reverse walk stops on the row with the failure naming the image path, leaving the
  up's file in place, and exits 1.
  Red when: the walk records `rolled-back` while the up's file remains.
- **AC3** — When the same family runs with TOOL-dSafePassage-17's `--plant witness-only`, the row is
  recorded `applied` with `via` `witness`, and the reverse walk downs it with no image, records
  `rolled-back` and exits 0.
  Red when: the scoped rule stops a row the forward walk applied by witness.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback-update --plant schema-step-kill-before-stamp`
  runs, TOOL-dSafePassage-19's plant, the re-run downs its rows that have no record and no image by
  their exit and exits 0.
  Red when: a row with no record is judged by its witness and the re-run stops.
- **AC5** — When `git grep -n -e "via" -e "before-image" -- help/upgrade-steps.md` runs, the receipt
  section names `via` and the "Rolling back" section says a missing image stops a row whose up ran.
  Red when: the page still says a missing image always means the step never ran.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 · the self-test calls `upgrade_steps.py fixture rollback` with `image-lost` beside `witness-only`, the walk's `witness-holds` record and the writer's refusal, its failing case staged by a verdict copy that applies the no-image rule to every row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit of units 15 to 26's
  id 40 (HIGH, item D-6).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-39`, `TOOL-dSafePassage-40`; no other section moved.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-3's one writer and reader of the step rows, TOOL-dSafePassage-2's
move 1 and TOOL-dSafePassage-17's `derive_down_verdict`, all specced and unbuilt at the base.
`python tools/codebase-map/reuse_lookup.py "record how a step was applied in the receipt"` ranked
`records`, `step` and `extract_records`, name-token matches, so no existing seam fits beyond the
three specs.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
