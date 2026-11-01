# DEPL-dShippedRelease-103 — An exit row is keyed by slug and tree, and an exited tree can queue again

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 8 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 91 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, item H11. An exit row hides an entry, and `write_queue_entry`
refuses a second entry for the same slug and tree. Unit 71 S1 does not say whether an exit row matches
by slug or by slug and tree, and unit 72 S1 makes every unknown admission exit `refused`, which writes
an exit row with no tree change. The re-run's `write_queue_entry` is a no-op, `derive_landing_queue`
passes over the old entry, and unit 59 S2's enqueue-at-the-call is the same no-op, so `admit` answers 3
for ever with no entry and no owner item.

## 2. Scope (IN)

- **S1** — The key. An exit row with `why` `refused` or `owner` passes over the entries of that slug and
  tree earlier on the chain, and over no others. A `landed` row keeps DEPL-dShippedRelease-93's
  slug-wide scope. Observed by AC1, AC2.
- **S2** — The re-entry. `write_queue_entry`'s "already present" test ignores an entry with a later exit
  row, so the same tree appends at the tail. Observed by AC1.
- **S3** — Who exits. Unit 71 S2's row is written on a `refused` the lander reached, and never on
  admission's exit 1 or 2. Observed by AC3.

## 3. Non-goals (OUT)

- The class of a failed admission: review ids 13 and 68, in the minors batch.
- The writer of the row on the direct caller: review id 108, in the minors batch.
- A checklist item for tombstoned keys: the audit's left-shift item is this unit's own plant.

### Edges

- **consumes-from** `DEPL-dShippedRelease-93` — the `landed` row's slug-wide scope, beside which this unit states the (slug, tree) key
- **consumes-from** `DEPL-dShippedRelease-71` — S1 and S2, whose key and caller this unit states
- **consumes-from** `DEPL-dShippedRelease-12` — `write_queue_entry`'s presence test
- **consumes-from** `DEPL-dShippedRelease-72` — S1's admission exits, which S3 keeps off the row
- **hands-off** `DEPL-dShippedRelease-59` — the re-entry rule, which that unit's enqueue-at-the-call inherits
- **hands-off** `DEPL-dShippedRelease-106` — the exit row's key, on which the minors batch rests (review ids 13, 68, 108)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 55, 56)

## 4. Design

### Evidence

- Unit 12 S1: `write_queue_entry` appends "unless one for that slug and tree is present".
- Unit 71 S1: `derive_landing_queue` "passes over every entry with a later exit row", keyed on no stated match; AC1 re-tests only a new tree.
- Unit 72 S1: "Exit 2 and every other exit stop as `refused`".

### Supersedes

- Unit 71 S1's "every entry with a later exit row".
- Unit 71 S2's "writes an exit row on `refused`", narrowed by S3.
- Unit 12 S1's presence test.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a tree refused twice appends twice, which is one more entry per refusal; each is passed over by its own row.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py --fixture --plant head-refused-same-tree` lands a head `refused`
  and re-runs `land --build fx` on the same tree, a new entry sits at the tail and `admit` answers by
  position.
  Red when: `admit` answers 3 for ever, with no entry and no owner item.
- **AC2** — When `--plant exit-key` writes an exit row for tree T1 with the slug's T2 entry queued,
  `derive_landing_queue` still holds T2.
  Red when: an exit row reads as slug-wide, so a later tree loses its place.
- **AC3** — When `--plant admit-crash` stubs `admit` to exit 2, the queue ref gains no exit commit.
  Red when: a crash in admission costs a build its queue place.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_items.py · covers AC1 AC2 AC3 · `head-refused-same-tree`, its failing case the presence test reading a tombstoned entry · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 91 (HIGH, item H11) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `write_queue_entry` and `derive_landing_queue` (unit 12 S1, S2) with `write_queue_exit` (unit 71 S1).
`python tools/codebase-map/reuse_lookup.py "re-add a key to an append only log after a tombstone row"`
ranked name-stem helpers (`rows`, `row`, `key`, `keys`) and no tombstoned log, because unit 12's is
specced and unbuilt. The recall probe surfaced unit 71 and report item H11, which agree with this
reading.

Recall terms used:
`python tools/memory-recall/query.py "how does an append only queue re-admit a tombstoned tree" --terms "write_queue_entry exit row slug tree tombstone re-enter append-only refused head key"`
