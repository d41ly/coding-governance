# DEPL-dShippedRelease-59 — the records landing takes the turn and skips the queue's order, and a slug with no entry is enqueued at the call

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 11 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 3 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`, HIGH,
item H4, which stands beside id 79. Unit 4 S7 lands the records commit with `--prepare --slug` then
`--land --slug`, and unit 12 S6 runs `check_landing_admitted` on every such call. Unit 12 never
names a records landing, a landed slug's entry is skipped, and only `deploy.land` appends one. With
a second queued build or `owner-orders` the answer is undefined, a refusal exits 5, S7 does not
route it, and unit 4 S8 holds with the mail refs unpruned.

## 2. Scope (IN)

- **S1** — The rule. `test_records_landing(slug, root)` in `tools/loop/deploy_items.py` is true when
  `git rev-list --no-merges <advertised tip>..HEAD` is one commit, carrying the `Pass: none`
  trailer, touching only paths under `memory/builds/<slug>/`, for a slug whose landing record
  `read_landing` reads. `check_landing_admitted` then exits 0 printing
  `admit — <slug> · records-only · no queue order`. The landing still takes the turn (unit 12 S4).
  Observed by AC1, AC2.
- **S2** — No entry. A slug with no entry that S1 does not admit is enqueued at the call through
  `write_queue_entry`, then answered by position, so a direct `--land --slug` neither bypasses the
  queue nor waits on a row nobody wrote. Observed by AC3.
- **S3** — The route. `run_records_landing` reads the lander's exit 5 as
  `records — held · landing turn`, exit 3, so the walk holds and a re-run lands. Observed by AC4.

## 3. Non-goals (OUT)

- A refused or dead admission: DEPL-dShippedRelease-72.
- The landing after the tombstone: DEPL-dShippedRelease-68.

### Edges

- **consumes-from** `DEPL-dShippedRelease-4` — `run_records_landing`, the records commit's shape and S8's copy probe
- **consumes-from** `DEPL-dShippedRelease-12` — `check_landing_admitted`, `write_queue_entry` and the turn
- **hands-off** `DEPL-dShippedRelease-68` — `test_records_landing`, the same test that unit's late landing passes
- **hands-off** `DEPL-dShippedRelease-78` — the no-entry rule of S2, which that unit re-reads for review id 79

## 4. Design

### Evidence

- Unit 4 S7 spells the commit `records(<slug>): landing records for <sha8>` with a `Pass: none` trailer.
- Unit 12 §5's "an empty queue admits its only entry" covers neither a non-empty queue nor a slug with no entry (report id 79).

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `test_records_landing` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2
- `tools/unattended/unattended.sh`: S3
- `tools/loop/deploy_fixture.py`: the cases of §6

### Alternatives rejected

- **Enqueuing every records landing.** It puts a build's own close behind a stranger's re-test,
  which the report's consequence names.

## 5. Production-readiness checklist

- security — the exemption reads the commit's paths and trailer, so a product change cannot pass as
  records.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a records commit touching a second folder is admitted as a landing and waits its turn, the
  safe reading.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-records-queued` runs a records landing with
  a second build queued ahead, the records commit reaches the default branch and the second build's
  entry keeps its place.
  Red when: a records landing waits behind a build, or removes its entry.
- **AC2** — When `--case engine-records-owner-orders` runs under `landing.order = "owner-orders"`
  with no order given, the records landing lands.
  Red when: a build's own close needs an owner's `land-next`.
- **AC3** — When `python deploy_items.py admit --slug fy` runs with no entry and a head queued, it
  exits 3 and the queue ref gains `fy`.
  Red when: an unqueued `--land --slug` passes the queue.
- **AC4** — When a planted lander exits 5 under `--case engine-records-held`, `run_records_landing`
  exits 3 printing `records — held`, and the mail refs stay.
  Red when: exit 5 falls through to unit 4 S8 as a done landing.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC4 · the `engine-records-` cases, their failing case `test_records_landing` answering false · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 3 (HIGH, item H4) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-4's `run_deploy_items`.
`python tools/codebase-map/reuse_lookup.py "walk ordered items stopping on the first non-zero exit and resuming by re-running"`
ranked name-stem helpers (`walk`, `build_walk`, `read_first_commit_date`) and no walker of items,
because `tools/loop/` is specced and unbuilt, so no existing seam fits outside the parent's own
module. The recall probe surfaced scout A's row for unit 4 and report items B3 and H1, which agree
with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the deploy walk resume after a held item and which items hold the lease" --terms "deploy walk idempotent held exit run_deploy_items landing record tombstone lease unlease close"`
