# DEPL-dShippedRelease-53 — `deploy.record` copies the core verdict at its write, and `deploy.core` never writes to an absent ref

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 10 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
BLOCKER, item B3, which stands beside id 74 (DEPL-dShippedRelease-56) on one order. Unit 13 S7 sets
`core` and `patch-key` through `set_landing_field` at `deploy.core`, and `deploy.record` runs after
it (flow-steps:438-439). Unit 1 S6 has no absent arm and S2 then writes `core: pending`, so the walk
dies on its first verdict or the verdict is lost with no later setter. This unit settles the order:
the record reads the verdict when it writes.

## 2. Scope (IN)

- **S1** — The copy. `--deploy record` calls `derive_core_fields(sha, root)` in
  `tools/loop/deploy_items.py`, over `read_core_verdict`, for the two fields S2 of unit 1 wrote as
  constants. `GREEN` gives `core: green`, `RED` gives `core: red` and `patch-key` from
  `derive_red_key(sha)`, `REFUSED` gives `core: refused`, and any other answer keeps `core: pending`
  and `patch-key: -`. Observed by AC1, AC2.
- **S2** — The absent arm. `set_landing_field` reads the tip first, and an absent ref exits 1
  printing `landing — <sha8> · absent` and writes nothing. It never creates a record. Observed by
  AC3.
- **S3** — `deploy.core` before the record. `run_deploy_core` reads that exit 1 as settled by S1: it
  prints `core — <sha8> · <verdict> · record pending` and exits by its route, so a first verdict
  reaches `deploy.record` and is not lost. Unit 13 S7's write stands for every read after the record
  exists. Observed by AC1, AC2.
- **S4** — The patch. Filing stays at `deploy.core` (unit 13 S8). A filed receipt ratifies once a
  landing record names its SHA, which S1's `patch-key` makes true on the same walk, so unit 13 §8
  F3's accept line holds on the first red. Observed by AC2.
- **S5** — The fixture. `--case core-walk-unplanted` walks a landing with no planted record from
  `deploy.core` to `read-landing`, once green and once red, and asserts `core` is not `pending`.
  Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The walk's handling of a `running` first answer: DEPL-dShippedRelease-56, which reads the same two
  items.
- Swapping the two items' `needs`: §8 F1.

### Edges

- **consumes-from** `DEPL-dShippedRelease-13` — `read_core_verdict`, `derive_red_key` and `run_deploy_core`, the verdict this unit copies and the write it guards
- **consumes-from** `DEPL-dShippedRelease-1` — `--deploy record`, `render_landing_body` and `set_landing_field`, whose absent arm S2 states
- **hands-off** `DEPL-dShippedRelease-56` — `derive_core_fields` and the `absent` exit, on which the walk's pass of a `running` answer rests

## 4. Design

### Evidence

- flow-steps:438 routes green and red to `deploy.record`, and flow-steps:439 has the record hold the core re-check's verdict
  and, on a red, the patch intake's key.
- Unit 13 §4 "The routes" says a `running` first answer does not hold the record; unit 1 S2 writes `core: pending` and S7
  makes a second `--deploy record` a no-op, so nothing else sets the field through that verb.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_core_fields` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S3
- `tools/unattended/unattended.sh`: S2
- `tools/loop/deploy_fixture.py`: S5's case

### Alternatives rejected

- **`set_landing_field` creating the ref.** Two writers of one record, and S7's idempotence would
  then read a stub.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a verdict arriving between `derive_core_fields` and the write lands at the next read
  through unit 13 S7, so the window costs one beat.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — the field's meaning on `help/deploy.md` does not change.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case core-walk-unplanted` runs with a planted green
  verdict, `python deploy_items.py read-landing <sha>` prints `core<TAB>green` and
  `patch-key<TAB>-`.
  Red when: `core` reads `pending`, so the verdict was lost at the first write.
- **AC2** — When the same case runs with a planted red verdict, `read-landing` prints
  `core<TAB>red`, `patch-key` equal to `derive_red_key(sha)`, and `python intake.py ratifies <key>`
  ratifies.
  Red when: a first red's patch names no record, or `patch-key` stays `-`.
- **AC3** — When `unattended.sh --deploy field <sha> core green` runs with no ref, it exits 1
  printing `absent` and the ref stays absent.
  Red when: the setter mints a record no writer owns.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `core-walk-unplanted`, its failing case the record writing `core: pending` as a constant · none

## 8. Open questions

- **F1 — One order for the core verdict and the record.** Options: (a) keep `deploy.core` then
  `deploy.record`, the record reading the verdict at its write; (b) swap the `needs` and ask
  dDeclaredLoop to move the row. (b) contradicts flow-steps:438-439 and owes a parent change.
  RESOLVED (agent, 2026-10-30, delegated): (a), rung 1, flow-steps:439. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 1 (BLOCKER, item B3) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-4's `run_deploy_items`.
`python tools/codebase-map/reuse_lookup.py "walk ordered items stopping on the first non-zero exit and resuming by re-running"`
ranked name-stem helpers (`walk`, `build_walk`, `read_first_commit_date`) and no walker of items,
because `tools/loop/` is specced and unbuilt, so no existing seam fits outside the parent's own
module. The recall probe surfaced scout A's row for unit 4 and report items B3 and H1, which agree
with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the deploy walk resume after a held item and which items hold the lease" --terms "deploy walk idempotent held exit run_deploy_items landing record tombstone lease unlease close"`
