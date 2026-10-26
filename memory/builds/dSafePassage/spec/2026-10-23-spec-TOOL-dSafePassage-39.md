# TOOL-dSafePassage-39 — the step row's `via` mark survives every rewrite that keeps the row `applied`, so the reverse walk's own records cannot erase it

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 3708a705 · streams tooling · order 6 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-39-deviation-85.md](../build/2026-10-23-build-TOOL-dSafePassage-39-deviation-85.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-23-prompt-TOOL-dSafePassage-42-hygiene-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-42-hygiene-fix.md) | research | TOOL-dSafePassage-38 TOOL-dSafePassage-42 |
| [2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-31-tokens-b-1-spec-writer.md) | research | TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-39-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-39-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-38 TOOL-dSafePassage-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 27 to 35
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md`)
confirmed finding **id 23** at HIGH, its item **D-4**. TOOL-dSafePassage-33 S1 has `set_step_state`
write `via` only when given, and S2 names only the forward walk's moves 1 and 5 as callers.
TOOL-dSafePassage-4 S4 move 3 rewrites the row through `set_step_state` before every down spawns,
keeping its state and setting `failure` to `down interrupted: …`, and passes no `via`;
TOOL-dSafePassage-3 §4 "Data model" says the writer replaces the row and keeps only a known
`introduced`. So on every rollback of a row the forward walk applied by witness alone, the mark is
gone before the down runs, TOOL-dSafePassage-33 S3 takes the witness branch, and a legacy-home row
whose witness still holds after its no-op down stops with
`witness still holds after down; before-image <path> absent`. That re-blocks the rollback
TOOL-dSafePassage-17 exists to unblock. This unit is id 23's promotion: the one writer carries the mark
across every rewrite that keeps the row `applied`, and the reverse walk's move 3 marks a row it finds
applied with no record and no image the same way.

## 2. Scope (IN)

- **S1** — The carry. `set_step_state`, called with no `via` for a step whose existing row is
  `applied` with `via` `witness`, keeps `via` when the new state is `applied`, and writes the row
  without it when the state changes. Called with `via="witness"`, it writes the mark under TOOL-dSafePassage-33 S1's rules.
  Every caller inherits the carry through the one writer, so no caller passes the mark back by hand.
  Observed by AC1 and AC2.
- **S2** — The callers, named. §4 "The writer's callers" lists every call of `set_step_state` the
  build's specs declare, found by `git grep -n "set_step_state" -- memory/builds/dSafePassage/spec/`
  on 2026-10-23, with the state it writes and what happens to `via`. Observed by AC2.
- **S3** — Move 3 over an unrecorded row. When TOOL-dSafePassage-4 S4 move 1 finds a row the receipt
  records nowhere with its witness holding, and no before-image exists at the row's image path
  (TOOL-dSafePassage-1 §4 "The before-image"), move 3 records it `applied` with `via="witness"`: no up
  is on record and no image says one wrote, which is the judgement TOOL-dSafePassage-33 S4 makes of
  such a row. A kill between move 3 and the down's verdict then leaves the mark the re-run needs.
  Observed by AC3.

## 3. Non-goals (OUT)

- When move 1 of the forward walk may set the mark: finding 29, `TOOL-dSafePassage-40`.
- Whether an `applied` row may carry a `failure`. TOOL-dSafePassage-3's AC7 refuses one and
  TOOL-dSafePassage-4 §4's table writes one at move 3; this unit keys the carry on the state alone, and
  `TOOL-dSafePassage-43` owns the answer.
- A second record of the mark beside the receipt's row.

### Edges

- **consumes-from** `TOOL-dSafePassage-33` — the optional `via` mark, its writer rules and the down's verdict that reads it; without them there is no mark to carry
- **consumes-from** `TOOL-dSafePassage-3` — `set_step_state`, the one writer that replaces a row whole; without it there is no rewrite to carry the mark across
- **consumes-from** `TOOL-dSafePassage-4` — the reverse walk's move 1 and move 3 and the `rollback` fixture family; without them there is no rewrite before the down and no plant to kill it
- **consumes-from** `TOOL-dSafePassage-43` — the answer to the second non-goal: an `applied` row may carry a `failure` that opens with an entry of `DOWN_STOP_PREFIXES`, so AC1 and AC3 write rows the writer admits
- **hands-off** `TOOL-dSafePassage-45` — S2's caller table read as a recorded reading, its `pending` as "none, or `failed` / `rolled-back`", finding 5 of the spec audit of units 36 to 42

## 4. Design

### The writer's callers

| Caller | Row before | Row after | `via` |
|---|---|---|---|
| TOOL-dSafePassage-2 S2 move 1 | pending | `applied` | written as `TOOL-dSafePassage-40` allows |
| TOOL-dSafePassage-2 S2 moves 2 to 5, any failure | any | `failed` | dropped, a state change |
| TOOL-dSafePassage-2 S2 move 5 | `failed`, set at move 3 | `applied` | none, a state change from `failed` |
| TOOL-dSafePassage-4 S4 move 3 | `applied` | `applied`, `failure` set | carried |
| TOOL-dSafePassage-4 S4 move 3, unrecorded row | none | `applied` | `witness` when no image exists (S3) |
| TOOL-dSafePassage-4 S4 moves 4 and 5, a stop | `applied` | `applied`, `failure` set | carried |
| TOOL-dSafePassage-4 S4 move 5, reverted | `applied` | `rolled-back` | dropped, a state change |
| TOOL-dSafePassage-8 §4 source-mode step 5 | `applied` | `applied` | carried |
| TOOL-dSafePassage-19 S4's re-run | through TOOL-dSafePassage-4's moves | as those rows | as those rows |
| TOOL-dSafePassage-20 S3's self-test arm | a scratch receipt | any | no shipped mark |

TOOL-dSafePassage-18 writes no row once a down leaves the receipt below schema 4, so it calls the
writer for no row this table could carry.

### Inventory

Minted: the `rollback` plants `witness-only-down-killed` and `unrecorded-witness-down-killed`. No
function, conf key, gate leg or policy key. No new `raise Refusal` site, so
`tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

Additive: no receipt at the base records a step.

### Rollout

Live at landing. It builds at order 6, after TOOL-dSafePassage-33 (order 5), whose mark it keeps. It
shares `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with `TOOL-dSafePassage-40` and
TOOL-dSafePassage-26 at order 6, so the build run sequences those passes by M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Having the down's verdict read the row as it stood before move 3.** It keeps the mark for one
  walk only: after a kill, the re-run's first read is the row move 3 already rewrote, and the mark is
  gone.
- **Having each caller pass `via` back.** Every future caller would owe it, and one that forgot would
  erase the mark silently, the class this finding is.

## 5. Production-readiness checklist

- security: no new write path; the receipt's one writer gains a carry rule.
- perf / scale: unchanged.
- error / empty / loading states: a killed rollback leaves the mark in place for its re-run.
- observability: the receipt row shows `via` beside the down's `failure` text.
- risks: a row that was applied by witness and later changed by hand keeps the mark; its down is then
  judged by its exit, as TOOL-dSafePassage-33 judges every such row.
- testing: the two plants and the probe, through §7.
- migration: additive.
- user docs: N/A — `help/upgrade-steps.md`'s receipt section, which TOOL-dSafePassage-33 S5 writes,
  already names the mark and its meaning; the carry changes neither.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture rollback --plant witness-only-down-killed`
  runs, TOOL-dSafePassage-17's `witness-only` row is applied by witness, the rollback is killed after
  move 3 and before the down's verdict, the receipt row then reads `applied` with `via` `witness` and
  the `down interrupted:` failure, and the re-run downs it, records `rolled-back` and exits 0.
  Red when: move 3 erases the mark and the re-run stops naming a before-image.
- **AC2** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `set_step_state` on a schema-4 receipt whose row is `applied` with `via` `witness`, a call with state
  `applied` and no `via` keeps the mark, and calls with state `failed` and `rolled-back` drop it.
  Red when: a same-state rewrite drops the mark, or a state change keeps it.
- **AC3** — When the same family runs with `--plant unrecorded-witness-down-killed`, a schema-4
  receipt holding no row for a step whose witness holds and whose image is absent is rolled back and
  killed after move 3; the row reads `applied` with `via` `witness`, and the re-run records
  `rolled-back` and exits 0.
  Red when: move 3 records the unrecorded row without the mark, so the re-run judges it by its witness.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the self-test calls `upgrade_steps.py fixture rollback` with the two killed plants and runs the writer probe, its failing case staged by a writer copy that replaces the row whole with no carry · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 27 to 35's id 23
  (HIGH, item D-4).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 36 to 42, written by the disposal stage: `TOOL-dSafePassage-43`, `TOOL-dSafePassage-45`; the second non-goal names its owner, `TOOL-dSafePassage-43`; no other section moved.
- rev-3 · 2026-10-26 · §7 · the §7 leg line gains `policy fixtures`, whose guard a §4 Files touched path
  trips, per the spec-tokens repair handoff
  `memory/builds/dSafePassage/prompts/2026-10-26-prompt-TOOL-dSafePassage-31-1-spec-writer.md`; no
  criterion's meaning moved.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-3's writer `set_step_state`, TOOL-dSafePassage-4's move 3 and
TOOL-dSafePassage-33's mark, all specced and unbuilt at the base. `python tools/codebase-map/reuse_lookup.py
"carry a row field forward when its writer rewrites the row"` ranked `rows`, `row`, `write` and
`write_text`, name-token matches in test and generator files, so no existing seam fits beyond the three
specs. The caller table was derived by grep over this build's specs, not from a record.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's promoted repairs are placed and sequenced after the unit they repair" --terms "spec audit promoted repair unit order edges hands-off consumes-from minors batch disposal rescope"`
