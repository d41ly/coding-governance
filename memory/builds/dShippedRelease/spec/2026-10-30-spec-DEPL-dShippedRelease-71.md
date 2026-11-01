# DEPL-dShippedRelease-71 — a queue entry leaves by a written exit, so a refused or held head blocks no other landing

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 7 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md](../reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-70 DEPL-dShippedRelease-72 DEPL-dShippedRelease-53 DEPL-dShippedRelease-56 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-60 DEPL-dShippedRelease-73 DEPL-dShippedRelease-55 DEPL-dShippedRelease-77 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-76 DEPL-dShippedRelease-75 DEPL-dShippedRelease-67 DEPL-dShippedRelease-54 DEPL-dShippedRelease-57 DEPL-dShippedRelease-74 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 77 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H15. Unit 12 S2 skips an entry only for a landed, withdrawn or superseded slug, an
unlanded parent, or a lease reading neither `live` nor `held`. A `refused` landing routes to Test
with its lease live, a paused build reads `held`, and S1 adds a new entry for a new tree and takes
none away, so every other build on every node gets exit 3 for the length of a re-test, or
indefinitely. The `landing-turn` owner item names no action that clears it.

## 2. Scope (IN)

- **S1** — The exit row. `write_queue_exit(slug, tree, why)` in `tools/loop/deploy_items.py` appends
  one commit to `refs/gov/landing-queue/<branch>` with keys `exit`, `slug`, `tree`, `why`.
  `derive_landing_queue` passes over every entry with a later exit row. Observed by AC1, AC3.
- **S2** — The class. `run_deploy_land` writes an exit row on `refused`, `why` `refused`, so the
  head leaves as its build returns to Test, and a re-test's new tree queues anew at the tail.
  Observed by AC1.
- **S3** — A held build. S2's skip reads `held` too: a `held` lease keeps its place and is passed
  over. Observed by AC2.
- **S4** — The owner's action. The `landing-turn` item gains the option `leave-queue`, which writes
  an exit row for the head with `why` `owner`. Observed by AC3.

## 3. Non-goals (OUT)

- The tree comparison across nodes: no cross-node reader exists, by unit 12 §4's evidence line, so
  an entry's tree is not compared.
- The wait's own observation: review id 21, in the minors batch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-12` — `derive_landing_queue`, `run_deploy_land` and the `landing-turn` item
- **hands-off** `DEPL-dShippedRelease-93` — `write_queue_exit`, which that unit calls with `why` `landed` (review id 7)
- **hands-off** `DEPL-dShippedRelease-103` — S1's match and S2's caller, which that unit states (review id 91)
- **hands-off** `DEPL-dShippedRelease-106` — the text and code which the round-2 minors batch repairs (review ids 46, 53, 68, 84, 108)
- **consumes-from** `DEPL-dShippedRelease-72` — S1's admission exits, the `admission-error` class, which stay off this unit's exit row (review id 68)

## 4. Design

### Evidence

- Unit 12 §4 routes `refused` to `transition`, to Test, with no lease change, and its S2 keeps `held` in the queue's way (report id 77).
- `build_gov_commit` and `write_gov_ref` (TOOL-dPlacedRequest-11) already carry an entry, so an exit is one more commit on one chain.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `write_queue_exit` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `leave-queue` | owner-item option | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/runtime/owner_items.py`: the option

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each exit row names its `why` on the chain, and `admit` prints the skip.
- risks — a head that leaves on `refused` and re-tests goes behind later arrivals, the cost of a
  re-test by design.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py --fixture --plant head-refused` runs a head that lands
  `refused`, the queue's second build then exits 0 from `admit`, and the head's re-test appends at
  the tail.
  Red when: a refused head holds every landing on every node.
- **AC2** — When `--plant head-held` holds the head's lease, the second build exits 0 from `admit`,
  and on resume the head is admitted ahead of the tail.
  Red when: a paused build stops the fleet of builds behind it, or loses its place.
- **AC3** — When `--plant owner-leave` disposes `leave-queue` on a head reading `live`, an exit row
  names `owner`, and the second build exits 0.
  Red when: the owner item names no action that clears the head.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_items.py · covers AC1 AC2 AC3 · the three plants, their failing case an exit row unread by `derive_landing_queue` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 77 (HIGH, item H15) of the round-1 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-2 spec audit's promoted units declare toward this unit (units 72, 93, 103, 106); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-12's outcome and queue code.
`python tools/codebase-map/reuse_lookup.py "append an entry to a ref chain and skip or tombstone an entry"`
ranked name-stem helpers (`skip`, `build_self_chain`, `resolve_entry`, `read_chain_clauses`) and no
ref-held queue, since unit 12's is specced and unbuilt, so no existing seam fits outside it. The
recall probe surfaced scout B's queue row and report item H15, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does a queue ref let a refused or held head leave so other builds land" --terms "landing queue entry tombstone refused held admission fail closed exit turn lease"`
