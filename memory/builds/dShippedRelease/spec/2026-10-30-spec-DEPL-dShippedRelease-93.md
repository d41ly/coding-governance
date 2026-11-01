# DEPL-dShippedRelease-93 — A landing writes its queue exit from the lander, on either caller

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 7 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 7 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, item H5. Unit 49 re-keys `landed` without naming unit 12's queue
as a consumer. Unit 12 S2 skips only on `landed`, `withdrawn`, `superseded`, an unlanded parent or a
non-live lease, and unit 71's exit rows cover only `refused` and `owner`. After units 49 and 50 a landed
spec run reads `held`, so its entry blocks the queue while the lease is live, hides while the lease is
`released`, and heads the queue again when the build run acquires, holding every other build at exit 3
for the whole build run. This unit writes the exit where a landing is known: in the lander.

## 2. Scope (IN)

- **S1** — The verb. `python deploy_items.py queue-exit --slug <slug> --tree <tree> --why <why>` is
  `write_queue_exit`'s shell door. Observed by AC1.
- **S2** — The write. The lander's landing path, beside `write_landing_outcome`, calls it with
  `why` `landed` for a landed class, reached by a direct `--land --slug` as well as by
  `run_deploy_land`. With no loop kit it prints unit 12 S6's `no landing turn` line and writes nothing.
  A failed write prints `queue exit not written · <why>` and leaves the lander's exit as it was, since
  the landing stands. Observed by AC1, AC2, AC3.
- **S3** — The scope. An exit row with `why` `landed` passes over every earlier entry of its slug,
  whatever the tree, because the landed tree can differ from the enqueued one: the close commits
  its records in place on the prepared merge, and the lander pushes HEAD. Observed by AC2.

## 3. Non-goals (OUT)

- The exit rows of `refused` and `owner`: unit 71 and review id 108 in the minors batch.
- The key of a `refused` row: DEPL-dShippedRelease-103.
- A checklist item that a re-keying spec lists every caller: the audit's left-shift item.

### Edges

- **consumes-from** `DEPL-dShippedRelease-49` — the re-keyed `landed` read, which took the queue's skip away
- **consumes-from** `DEPL-dShippedRelease-12` — `derive_landing_queue` and `write_landing_outcome`
- **consumes-from** `DEPL-dShippedRelease-71` — `write_queue_exit` and the exit row
- **hands-off** `DEPL-dShippedRelease-103` — the `landed` row's slug-wide key, beside which that unit states the (slug, tree) key
- **hands-off** `DEPL-dShippedRelease-106` — `queue-exit`, which the minors batch also calls (review id 108)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 45, 56)

## 4. Design

### Evidence

- Unit 49 §3 names units 11 and 50 only, and unit 12 S2 reads the same function.
- Unit 12 S1 adds an entry for a new tree and takes none away; unit 71 S2 writes a row only in `run_deploy_land`, on `refused`.
- Unit 12 §4 "The turn, in order" writes the outcome at each attempt's end, so the lander knows the class before its EXIT trap.
- `tools/push-main.sh:975-977` pushes HEAD, "the SHA pushed, not the prepared one", so a landed tree need not equal an entry's `tree`.

### Supersedes

- Unit 12 S2 reads with this row: a landed slug's earlier entries leave by S3.
- Unit 12 AC2's "first lands, then the second exits 0" stands, now by the row and not by the old `landed` reading.
- Unit 71 S2's sentence that only `run_deploy_land` writes a row, for this `why`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `queue-exit` | verb of `deploy_items.py` | none |
| `landed` | a value of an exit row's `why` | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S3
- `tools/push-main.sh`: S2
- `tools/push-main.test.sh`: the lander half of §7's arm
- `tools/loop/deploy_fixture.py`: the cases of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — S2 states the three answers of the write, and AC3 plants the failed one.
- observability — each state prints the line §2 names, on green and red.
- risks — a failed exit write leaves a landed entry at the head; `admit` names it and unit 71 S4's `leave-queue` clears it.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case engine-land-direct` lands through
  `bash tools/push-main.sh --land --slug fx` with no `run_deploy_land`, the queue ref holds an exit row
  with `why` `landed`, and a second build's `admit` exits 0.
  Red when: a landing reached by the direct caller never leaves the queue.
- **AC2** — When `--case engine-two-runs-queue` lands a spec run, hands the lease over and the build run
  acquires, a second build's `python deploy_items.py admit --slug fy` exits 0 at each step.
  Red when: the old entry heads the queue again for the whole build run.
  fixture: the hand-over is unit 69's, order 11, so the main loop observes this case at the close.
- **AC3** — When `--case engine-queue-exit-fails` stubs the verb to exit 1, the lander exits 0 and prints
  `queue exit not written`.
  Red when: a landed build reports a failed landing.

## 7. Gates

`push-main self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `engine-two-runs-queue`, its failing case the exit row unread by `derive_landing_queue` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 7 (HIGH, item H5) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `write_queue_exit` (unit 71 S1), called beside `write_landing_outcome` (unit 12 S7).
`python tools/codebase-map/reuse_lookup.py "remove a landed build from a queue"`
ranked name-stem helpers (`build`, `build_commit`, `queue`, `build_fixture`) and no ref-held queue,
because unit 12's is specced and unbuilt. The recall probe surfaced scout B's row for unit 12 and
TOOL-dWellOiledMachine-60's landing push, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does a landed build leave the landing queue" --terms "landing queue exit row landed outcome write_landing_outcome write_queue_exit lander direct land slug"`
