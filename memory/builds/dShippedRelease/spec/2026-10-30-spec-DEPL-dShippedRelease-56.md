# DEPL-dShippedRelease-56 — a `running` core passes to `deploy.record`, so a landing record exists for the length of the bar

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 11 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 74 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H1, which stands beside id 1 (DEPL-dShippedRelease-53). Unit 4 S1 stops the walk at the
first non-zero exit and unit 13 S7 exits 3 on `running`, while unit 13 §4 says a `running` answer
does not hold `deploy.record`. For the 16 to 65 minutes of a bar no landing record exists, and a
killed supervisor leaves none, the state unit 1 §8 F2 refused.

## 2. Scope (IN)

- **S1** — The pass. `WALK_RECORD_ON_HOLD` in `tools/loop/deploy_items.py` maps `item.deploy.core`
  to `item.deploy.record`. When `run_deploy_items` reads exit 3 from a key of that map, it runs the
  value's item and then stops with exit 3. Every other non-zero exit stops as unit 4 S1 says.
  Observed by AC1.
- **S2** — The resume. A re-run re-enters at `deploy.core`; a verdict read then sets `core` and
  `patch-key` through `set_landing_field`, since the ref now exists, and `deploy.record` prints
  `already recorded`. Observed by AC2.
- **S3** — The killed supervisor. A case kills the walk after the record's write, with the core
  reading `running`, and a second node's walk finds one record and finishes it. Observed by AC3.

## 3. Non-goals (OUT)

- The record's copy of a verdict already read: DEPL-dShippedRelease-53.
- A `running` wait of its own: unit 13 S7's ceiling stands.

### Edges

- **consumes-from** `DEPL-dShippedRelease-4` — `run_deploy_items` and its stop rule, which this unit gives its one exception
- **consumes-from** `DEPL-dShippedRelease-13` — `--deploy core`'s exit 3 on `running`, the one hold this unit passes
- **consumes-from** `DEPL-dShippedRelease-53` — `derive_core_fields` and the `absent` exit, which make the first read safe

## 4. Design

### Evidence

- Unit 4 §4 "The one commit" orders `core · record · distill`; S1 stops on the first non-zero exit, 3 meaning held.
- A bar runs 16 to 65 minutes (`tools/push-main.sh:231-233`, cited by unit 12 §4).
- Unit 1 §8 F2 rejected a landing with no record for a killed supervisor.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `WALK_RECORD_ON_HOLD` | module constant, `tools/loop/deploy_items.py` | `py.constant`, screaming |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1
- `tools/loop/deploy_fixture.py`: the cases of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — the record itself reads `core: pending`, so a reader sees the bar is out.
- risks — a walk that passes one hold could pass others; the map names one pair and a second pair is
  a spec change.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-core-running` walks a landing whose core
  reads `running`, the walk exits 3 and `read-landing` prints `core<TAB>pending`.
  Red when: no landing record exists while the bar runs.
- **AC2** — When the verdict turns red and the walk re-runs, `read-landing` prints `core<TAB>red`
  with a `patch-key`, and exactly one ref exists under `refs/gov/landing/`.
  Red when: the verdict stays in the bar's record and never reaches the landing record.
- **AC3** — When `--case engine-core-killed` stops the walk after the write and a second clone's
  `--deploy run` follows, the second walk prints `already recorded` and finishes.
  Red when: a killed supervisor leaves a landing no second node can read.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `engine-core-running`, its failing case the map emptied · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 74 (HIGH, item H1) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-4's `run_deploy_items`.
`python tools/codebase-map/reuse_lookup.py "walk ordered items stopping on the first non-zero exit and resuming by re-running"`
ranked name-stem helpers (`walk`, `build_walk`, `read_first_commit_date`) and no walker of items,
because `tools/loop/` is specced and unbuilt, so no existing seam fits outside the parent's own
module. The recall probe surfaced scout A's row for unit 4 and report items B3 and H1, which agree
with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the deploy walk resume after a held item and which items hold the lease" --terms "deploy walk idempotent held exit run_deploy_items landing record tombstone lease unlease close"`
