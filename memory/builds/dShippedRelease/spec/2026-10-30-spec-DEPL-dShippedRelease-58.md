# DEPL-dShippedRelease-58 — every `step.deploy` item has a verb and an adapter row, and the documented order reaches `run_deploy_land`

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 11 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 2 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`, HIGH,
item H3. Unit 4 S1 runs each item through its own `--deploy <item>`, yet the set defines no
`--deploy parents`, `--deploy land` or `--deploy recommend`. S14 registers nine adapters where
TOOL-dWellOiledMachine-6 S8 runs a command item only through its row, and S15's order never reaches
`run_deploy_land`, so `deps.landing` is not enforced on the walk and `write_queue_entry` never runs.
This unit wires the population and proves it by a join.

## 2. Scope (IN)

- **S1** — The verbs, in `tools/unattended/unattended.sh`: `--deploy parents <slug>` over
  `python deploy_items.py parents --build <slug>`, `--deploy land <slug>` over
  `python deploy_items.py land --build <slug>`, and `--deploy recommend <slug>` over
  `--recommend <slug> --stage deploy` (TOOL-dDeclaredLoop-22 S3). Each exits as its callee does.
  Observed by AC1, AC2.
- **S2** — The adapters. S14's `[[adapter]]` rows at `point.command-adapters` in
  `tools/runtime/points.toml` cover every command item of `read_items(step="step.deploy")`, these
  three and `deploy.released` among them. Unit 4's AC12 reads that count from `read_items`, never a
  typed nine. The `deploy.released` row is inert until `item.deploy.released` leaves its
  `[[stand-in]]` row. Observed by AC3.
- **S3** — The order. `tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`, states `--deploy run <slug> --to-land`, `--close`,
  `--deploy land <slug>`, `--landed`, `--deploy run <slug>`, so a landing goes through
  `run_deploy_land`. Observed by AC2.
- **S4** — The join. `check_deploy_items_wired(root)` in `tools/loop/deploy_items.py`, reached as
  `python deploy_items.py check-wired`, reads every `[[item]]` of `step.deploy` and fails on one
  that is on no `[[stand-in]]` row and has no `--deploy` verb in `unattended.sh` or no adapter row.
  Observed by AC4.

## 3. Non-goals (OUT)

- `--deploy released`'s body: DEPL-dShippedRelease-5, which this unit hands the adapter row.
- The recommendation's scoring: TOOL-dDeclaredLoop-22.

### Edges

- **consumes-from** `DEPL-dShippedRelease-4` — `run_deploy_items`, S14's adapter rows and S15's order, each of which this unit completes
- **consumes-from** `DEPL-dShippedRelease-11` — `run_deploy_parents`, under `--deploy parents`
- **consumes-from** `DEPL-dShippedRelease-12` — `run_deploy_land` and `write_queue_entry`, under `--deploy land`
- **hands-off** `DEPL-dShippedRelease-5` — the `deploy.released` adapter row, inert until that unit lifts the stand-in, and `--deploy released`, the verb the row runs

## 4. Design

### Evidence

- A grep of `--deploy <verb>` over the set lists carries, close, core, current, distill, field, mandate, notify, record, released,
  review, run, snapshot and unlease (report id 2's reason), with no `parents`, `land` or `recommend`.
- Unit 11 S2 and unit 12 S9 define `deploy_items.py parents` and `deploy_items.py land`, and unit 5 S1 defines `--deploy released`.
- Unit 4 S1 prints `stand-in <owner>` for an item on a `[[stand-in]]` row and goes on.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `check_deploy_items_wired` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `--deploy parents`, `land`, `recommend`, `check-wired` | verbs | none |

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1, `KIT_UNATTENDED_VERSION`
- `tools/runtime/points.toml`: S2
- `tools/loop/deploy_items.py`: S4
- `tools/loop/deploy_fixture.py`: the cases of §6
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`: S3

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — an operator's habit of `--land` still lands; it skips the queue as it does with no
  `--slug`, and the walk's `deploy.land` then reads `nothing-pushed`.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `memory/guides/UNATTENDED-VERBS.md`, rendered from its template, states the order.

## 6. Acceptance criteria

- **AC1** — When `unattended.sh --deploy parents fx` runs on a fixture with one held parent it exits
  3 printing `awaiting`, and `python deploy_fixture.py --case engine-to-land` runs that verb through
  the walk.
  Red when: `deps.landing` is unenforced on the walk.
- **AC2** — When `python deploy_fixture.py --case engine-land-order` follows the documented order on
  a fixture build, the queue ref holds its entry.
  Red when: the order bypasses `run_deploy_land`, so the queue stays empty.
- **AC3** — When `python supervise.py --check-adapters` runs at the pass, it exits 0, and the count
  it prints equals the command items of `read_items(step="step.deploy")`.
  Red when: a command item has no adapter, the state unit 4's AC12 named and could not see.
- **AC4** — When `python deploy_items.py check-wired` runs at the pass it exits 0; with one adapter
  row taken out of a scratch copy it exits 1 naming the item.
  Red when: a new item with neither a verb nor an adapter passes.

## 7. Gates

`recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC4 · `engine-land-order`, its failing case the documented order with plain `--land` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 2 (HIGH, item H3) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-4's `run_deploy_items`.
`python tools/codebase-map/reuse_lookup.py "walk ordered items stopping on the first non-zero exit and resuming by re-running"`
ranked name-stem helpers (`walk`, `build_walk`, `read_first_commit_date`) and no walker of items,
because `tools/loop/` is specced and unbuilt, so no existing seam fits outside the parent's own
module. The recall probe surfaced scout A's row for unit 4 and report items B3 and H1, which agree
with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the deploy walk resume after a held item and which items hold the lease" --terms "deploy walk idempotent held exit run_deploy_items landing record tombstone lease unlease close"`
