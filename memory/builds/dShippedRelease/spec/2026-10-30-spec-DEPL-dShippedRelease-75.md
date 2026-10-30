# DEPL-dShippedRelease-75 — the `codex-retrust` orders row carries the shape its readers consume

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 22 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 85 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H19, which stands beside id 14. Unit 27 S9 calls `codex-retrust` only an orders row kind,
with no `path`, file or argv. `tools/govkit/govkit.py:5655-5656` reads `order["path"]` directly,
unit 20 S4 makes a row with no `path` a red MALFORMED finding, and unit 17 S5 runs a hook's argv or
a step's `up`, and this row has neither. A Codex adopter's first update that moves a hook's bytes
reds its bar or raises KeyError. This unit sits one order above unit 20, the first reader, because
the row's order file needs unit 20's writer.

## 2. Scope (IN)

- **S1** — The row. `write_retrust_order(target, hooks)` in `tools/govkit/codex_targets.py` appends
  `{kind, id, path, argv, state}` to the receipt's `orders`: `kind` `codex-retrust`, `id`
  `codex-retrust/<first 12 hex of the hook paths' SHA-256>`, `path` the order file under
  `.governance/outbox/`, `argv` the command S9 of unit 27 prints, split, and `state` `open`.
  Observed by AC1.
- **S2** — The file. It is written by `render_attended_order("codex-retrust", argv, why)`, the one
  writer, so `check` finds `order["path"]` on disk. Observed by AC1, AC2.
- **S3** — `attend` runs a row's `argv` through `run_target_argv`, the third arm beside a hook's
  argv and a step's `up`, and sets `applied` on exit 0. Observed by AC3.
- **S4** — An offer writes the same row and file, spawning nothing, so `check_orders` reads it open
  at the adopter. Observed by AC2.

## 3. Non-goals (OUT)

- The `carries` caller: review id 14, in the minors batch.
- A declared orders-row schema shared by every writer: the audit's left-shift item, which no clause
  of this build names.

### Edges

- **consumes-from** `DEPL-dShippedRelease-27` — `derive_retrust`, the row's first mention and the command S9 prints
- **consumes-from** `DEPL-dShippedRelease-20` — `render_attended_order` and `check_orders`, the writer and the grader this row must satisfy
- **consumes-from** `DEPL-dShippedRelease-17` — `cmd_attend`, whose walk gains the row's `argv`

## 4. Design

### Evidence

- `tools/govkit/govkit.py:5655` reads `order["path"]` with no default, `:5656-5657` fail an absent file, and `:5658` reads `kind` for a hole only.
- Unit 20 S4 makes a row with no `path` the one `MALFORMED` finding; unit 17 S5 names `attended` and `codex-retrust` rows.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `write_retrust_order` | function, `tools/govkit/codex_targets.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/govkit/codex_targets.py`: S1, S2, S4
- `tools/govkit/govkit.py`: S3
- `tools/govkit/selftest.py`: the case of §6

## 5. Production-readiness checklist

- security — `argv` is gov's own printed command, written by gov into the receipt and run only by
  the owner's `attend`.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the stated repair is the unit's only change; a wrong reading reds at its own fixture.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/offers.md`'s section on what an offer leaves to an adopter gains the row,
  through unit 20's section.

## 6. Acceptance criteria

- **AC1** — When `python codex_targets.py --fixture --case trust-changed` moves one hook's bytes
  through `update`, the receipt's row holds `kind`, `id`, `path`, `argv` and `state`, and
  `python tools/run-gates/check-receipt.py <target>` counts it `open` and prints no `MALFORMED`.
  Red when: the row has no `path`, so an adopter's bar reds.
- **AC2** — When `python tools/govkit/govkit.py check --target <target>` runs on that target it
  exits 0; with the order file deleted it fails naming it.
  Red when: the row names a file nothing wrote.
- **AC3** — When `python kit_walk.py --fixture --plant attend-retrust` runs `attend` with a canary
  as the row's `argv`, the canary fires and the row reads `applied`.
  Red when: `attend` has nothing to run for this row.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · a Codex fixture target, its failing case the row with no `path` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 85 (HIGH, item H19) of the round-1 spec audit.

## 10. Reuse audit

The seams reused are unit 20's `render_attended_order` and `check_orders`.
`python tools/codebase-map/reuse_lookup.py "grade an order row of the receipt before an attended run"`
ranked `rows`, `row`, `run` and `run_arms`, name-stem hits, and a read of
`tools/govkit/govkit.py:5655` found the one reader of a row's `path`. The recall probe surfaced unit
20's brief line and report item H19, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what shape must an orders row of the receipt carry for attend and check to read it" --terms "orders row receipt path kind render_attended_order hook attended codex retrust check_orders"`
