# DEPL-dShippedRelease-81 — A queue entry carries its own parents' answer, so the skip and `deploy.parents` read one rule

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 7 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 2 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, BLOCKER, which shares item B2 with id 87
(DEPL-dShippedRelease-82). Unit 50 S3 exempts a spec run in `run_deploy_parents` alone. Unit 12 S2's
queue still skips an entry "while a parent of it is not `landed`" under every `landing.order`, and
`run_deploy_land` and `check_landing_admitted` both admit from that queue. A spec run passes
`deploy.parents`, then `--deploy land` answers 3 and the lander exits 5 for as long as a parent is
unbuilt, the outcome unit 50 §8 F1 rejected. This unit puts the exemption where both readers meet.

## 2. Scope (IN)

- **S1** — One rule. `test_parents_admit(build, root)` in `tools/loop/deploy_items.py` is true exactly
  when `run_deploy_parents` answers `land`, by every clause of unit 11 §4 "The program" and unit 50
  S3, `test-decides` included. `run_deploy_parents` calls it for that answer, and it prints nothing
  and declares no wait. Observed by AC1.
- **S2** — The entry's key. `write_queue_entry` writes one more key, `parents-admit`, `yes` when S1 is
  true on the enqueueing node and `no` otherwise. That node alone holds the build's rows and head,
  and every other node reads the key. Observed by AC2.
- **S3** — The skip. `derive_landing_queue`'s parent clause reads: an entry is skipped, keeping its
  place, while a parent of it is not `landed` and its `parents-admit` reads `no`. An entry with no
  key reads `no`. Observed by AC2, AC3.

## 3. Non-goals (OUT)

- The first half of `test_spec_run_landing`'s definition: review ids 32, 50 and 99, in the minors
  batch, which restate the one rule.
- The end-to-end walk and the defer flip: DEPL-dShippedRelease-82, the other half of item B2.
- A re-read of `parents-admit` when a parent later withdraws: `deploy.parents` runs before the entry
  exists, and a withdrawn parent reaches `withdrawn` through unit 11's route.

### Edges

- **consumes-from** `DEPL-dShippedRelease-50` — `test_spec_run_landing`, the exemption this unit carries to the queue
- **consumes-from** `DEPL-dShippedRelease-11` — `run_deploy_parents`' answers, which S1 factors
- **consumes-from** `DEPL-dShippedRelease-12` — `write_queue_entry` and `derive_landing_queue`'s parent clause, which S2 and S3 supersede
- **hands-off** `DEPL-dShippedRelease-82` — `test_parents_admit` and the entry key, which that unit's end-to-end case walks
- **hands-off** `DEPL-dShippedRelease-106` — `test_parents_admit`, which the minors batch's one rule feeds (review ids 32, 50, 99)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 9, 55)

## 4. Design

### Evidence

- Unit 12 S2 skips "while a parent of it is not `landed`", and unit 12 S9 is enqueue, admit, land; a grep of `test_spec_run_landing` over the set prints only unit 50 (report id 2).
- Unit 11 S4's `test-decides` reads the build's head and the verdict for its tree, neither of which another node's queue read can reach; unit 12 §4 records that no cross-node reader of a verified tree exists, which is why S1 of unit 12 gives an entry its `tree`.
- Unit 50 S3 reads the landing build's own rows, which sit on its branch until the landing lands.

### The entry

```
slug: <slug>
tree: <tree>
sha: <sha>
fleet-tag: <tag>
parents-admit: yes | no
```

### Supersedes

- Unit 12 S1's key list gains `parents-admit`.
- Unit 12 S2's clause "while a parent of it is not `landed`": S3 here.
- Unit 11 §4 "The program" keeps its verdict lines; S1 only factors the read.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `test_parents_admit` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `parents-admit` | queue entry key | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `help/loop.md`: the queue's parent clause

### Alternatives rejected

- **`derive_landing_queue` calling `test_spec_run_landing` itself.** The report's first spelling. Every node runs that read, and a foreign node holds neither the landing build's rows nor its head, so the test answers on the wrong tree. Refuted by unit 11 S4 and unit 50 S3's own inputs.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — the key records the answer at enqueue, so a parent that lands later changes nothing and one that withdraws is read by the walk's own `deploy.parents`.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/loop.md` states that a queue entry carries its parents' answer.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py --fixture --plant parents-one-rule` runs a table of an
  all-landed build, a held parent, an all-DEFERRED build and a `test-decides` head, the exit of
  `parents --build fx` is 0 on exactly the rows where `test_parents_admit` is true.
  Red when: the verb and the test read two rules.
- **AC2** — When `python deploy_items.py admit --slug fx` runs on an all-DEFERRED build with a `held`
  parent, it exits 0, and the queue ref's entry reads `parents-admit: yes`.
  Red when: a spec run is never admitted, the outcome unit 50 §8 F1 rejected.
- **AC3** — When `admit --slug fy` runs on a build with one `CLOSED` unit and a `held` parent, it exits
  3, its entry reads `parents-admit: no`, and a queued build behind it exits 0 from `admit`.
  Red when: a built unit passes the skip, or a skipped entry blocks the queue.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_items.py · covers AC1 AC2 AC3 · `parents-one-rule` and the two `admit` plants, their failing case the skip reading `not landed` alone · none

## 8. Open questions

- **F1 — Where does the exemption sit?** Options: (a) a key the enqueueing node writes; (b) the test
  run by every node's queue read, the report's spelling; (c) a second exempt path in
  `check_landing_admitted`. (b) reads the wrong tree on a foreign node, and (c) leaves
  `derive_landing_queue` holding the entry for every other build. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the one form both readers can read. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 2 (BLOCKER, item B2) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `derive_landing_queue` and `write_queue_entry` (unit 12 S1, S2), and S1 factors `run_deploy_parents` (unit 11 S2).
`python tools/codebase-map/reuse_lookup.py "skip a queue entry while a parent build has not landed"`
ranked name-stem helpers (`note`, `build`, `has`, `skip`) and no queue reader, because `tools/loop/` is
specced and unbuilt, so no seam fits outside the parents. The recall probe surfaced scout B's row for
unit 11 and report item B2, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the landing queue treat a spec run with an unbuilt parent" --terms "landing queue parent skip spec run exemption deps.landing derive_landing_queue admit carry-forward DEFERRED held"`
