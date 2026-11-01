# DEPL-dShippedRelease-80 — `run_deploy_review` branches on `unfired` before it reads a row, so a first walk fires or says not placed

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 13 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 28 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, BLOCKER, which shares item B1 with id 1
(DEPL-dShippedRelease-79). Unit 60 S1's new first step reads the field before unit 14 S1's row check,
so a landing with no `landing review` row takes the `pending` arm and never writes `not-placed`. That
reaches the default `review.deploy = opt-in`, so every landing holds at exit 3 and `dispose-landing`
has nothing to dispose. This unit states the arms in their one order and proves each from a record
nobody planted.

## 2. Scope (IN)

- **S1** — The arms. `run_deploy_review` reads `review` through `read_landing` and branches on the
  value alone: `disposed · …` and `not-placed · …` print it and exit 0; `pending` prints the pin and
  exits 3 with no `--trigger`; `unfired` goes on to unit 14 S1's `derive_breakpoints` read, which
  writes `not-placed` on no row and fires on a row. Observed by AC1, AC2.
- **S2** — Every other value exits 2 naming it and fires nothing, so a corrupt field never reads as
  unfired. Observed by AC3.
- **S3** — A read that answers no value. `read_landing`'s `absent` exit 1, `refused` exit 1 and dead
  probe exit 2 each stop the verb with that exit, firing nothing. Observed by AC4.
- **S4** — The first-walk fixture. `--case review-first-walk` walks `--deploy record` then
  `--deploy review` with no planted field under `opt-in` and under `owed`, so each arm of the value
  table is reached from the record's initial value. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The initial value: DEPL-dShippedRelease-79, the other half of item B1.
- A review that dies after its trigger: review id 97, in the minors batch.
- A lint over every field's value table: the audit's left-shift item, and this unit's fixture is its
  one instance.

### Edges

- **consumes-from** `DEPL-dShippedRelease-79` — `unfired`, the initial value this unit's arm order branches on
- **consumes-from** `DEPL-dShippedRelease-60` — the first step, whose arm order this unit restates
- **consumes-from** `DEPL-dShippedRelease-14` — S1's row read, which becomes the body of the `unfired` arm
- **hands-off** `DEPL-dShippedRelease-106` — the arms, which the minors batch reads for review id 97

## 4. Design

### Evidence

- Unit 60 S1 places the field read "as a first step", ahead of unit 14 S1's two arms, and report id 28 records that a landing with no row reaches the `pending` arm.
- `read_landing`'s exits are unit 1 S4's: 1 for `absent` and `refused`, 2 for a dead probe.
- Unit 14 AC1's `review-not-placed` and AC3's `review-values` expect exactly the two arms S1 reaches.

### The arms, in order

| Field value | Row read | `--trigger` | Exit |
|---|---|---|---|
| `disposed · …`, `not-placed · …` | no | no | 0, value printed |
| `pending` | no | no | 3, pin printed |
| `unfired`, no row | yes | no | 0, `not-placed · review.deploy=<value>` written |
| `unfired`, a row | yes | once | 3, `pending` written after exit 0 |
| any other | no | no | 2, naming it |

### Supersedes

- Unit 60 S1's sentence order: its `pending` and `disposed` arms stand, and `unfired` joins them as the one arm that reaches unit 14 S1.
- Unit 60's AC1 and AC2 stand as written, since each reaches `pending` by this verb's own write.
- Unit 78 S53's re-read of the `pending` arm stands.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/loop/deploy_fixture.py`: S4's case

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — §4's table states each value, and AC3 and AC4 plant the two that answer nothing.
- observability — each state prints the line §2 names, on green and red.
- risks — unit 60 §5's duplicate trigger on a kill between `--trigger` and the write stands, since the field still reads `unfired` there.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-first-walk` runs at the default
  `review.deploy`, `read-landing` prints `review<TAB>not-placed · review.deploy=opt-in`, the verb
  exits 0 and the stub's log holds no `--trigger`.
  Red when: a landing with no row takes the `pending` arm and holds at exit 3.
- **AC2** — When the same case runs under `review.deploy = "owed"`, the first `--deploy review` exits
  3 and the log holds one `--trigger`, and a second run exits 3 with the log unchanged.
  Red when: no landing review ever fires, or a re-walk fires a second.
- **AC3** — When `--case review-field-corrupt` plants `review: lgtm`, `--deploy review` exits 2 naming
  `lgtm` and the log holds no `--trigger`.
  Red when: an unknown value reads as unfired and fires a review.
- **AC4** — When `--case review-no-record` runs with no ref, `--deploy review` exits 1 printing
  `absent`, and with a dead remote it exits 2; the log holds no `--trigger` in either.
  Red when: a landing with no record fires a review about nothing.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC4 · `review-first-walk`, its failing case the `pending` arm read ahead of `unfired` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 28 (BLOCKER, item B1) of the round-2 spec audit.

## 10. Reuse audit

The seam extended is `run_deploy_review` (unit 14 S1, unit 60 S1), and `read_landing`'s exits are unit 1 S4's.
`python tools/codebase-map/reuse_lookup.py "read a report path from a field before firing a review"`
ranked name-stem helpers (`read`, `read_text`, `before`, `report`) and no breakpoint reader, because
`tools/loop/` is specced and unbuilt, so no seam fits outside the parent's module. The recall probe
surfaced TOOL-dPlacedRequest-5 and report item B1, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what value does the landing record hold for a review that never fired" --terms "landing review field pending trigger not-placed unfired disposed run_deploy_review breakpoint walk record"`
