# DEPL-dShippedRelease-110 — `dispose-landing` writes nothing into a report and refuses one stating another range

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 29 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, which shares item H1
with ids 2, 38 and 48 (DEPL-dShippedRelease-109, -111, -112). Unit 90 S1 refuses only a report already
holding its one spelling, so a real report of another range, spelled otherwise, gets this landing's
range stamped on and passes all four terms. The `landing` term then grades the disposal's own write,
the forgery it exists to stop. This unit takes the write out, so the term grades only what the review
wrote.

## 2. Scope (IN)

- **S1** — No write. `dispose-landing <sha> <report>` writes no byte into the report: unit 90 S1's stamp
  is not built. Observed by AC1.
- **S2** — The refusal. A report whose `range` differs from `read_pin_range` is refused, exit 2, printing
  `dispose — <sha8> · report states <base8>...<head8>`, and `review` keeps its value. A `range` of `none`
  or `ambiguous` is refused the same way, printing that word. Observed by AC1, AC2.
- **S3** — The order. S2 runs ahead of `write_review_patches`, so a refused report files nothing.
  Observed by AC2.
- **S4** — The binding is the review's. With no write, the `landing` term reads bytes the review agent
  wrote, and `dispose-landing` over the same report twice leaves it unchanged. Observed by AC3.

## 3. Non-goals (OUT)

- The read and the compare: DEPL-dShippedRelease-109.
- A report whose pin refuses: review id 53, in the minors batch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-109` — `read_report_range` and `read_pin_range`, which S2 reads
- **consumes-from** `DEPL-dShippedRelease-90` — S1 and AC2, which this unit supersedes
- **consumes-from** `DEPL-dShippedRelease-14` — `dispose-landing` and S4's order
- **hands-off** `DEPL-dShippedRelease-111` — the unchanged bytes, which that unit's honest case asserts
- **hands-off** `DEPL-dShippedRelease-112` — S2's refusal, beside which that unit states the unreadable spellings
- **hands-off** `DEPL-dShippedRelease-113` — S2, which the minimal record's range line must pass
- **hands-off** `DEPL-dShippedRelease-106` — S2, which S49's `dispose-with-reason` report must pass, so the edge naming the stamp reads this unit

## 4. Design

### Evidence

- Unit 90 S1: "writes `**Reviewed range:**` under the report's `**Serves:**` line. A report already holding that line with a different range is refused".
- Report id 29 tallied 12 diff-review records from 2026-10 on, each stating a range under some label, and read a real report of another range through S1. PINNED at the audit.
- Unit 106 S49's `dispose-with-reason` writes a report and runs `dispose-landing` over it.

### Supersedes

- Unit 90 S1 whole, S3's "through `dispose-landing`" stands, and AC2 whole: AC1 and AC3 here take its place.
- Unit 90 §5's risks line on a stamped report: a report is not rewritten.
- Unit 14 S4's stamp, which unit 90's Supersedes added.
- Unit 106 S49's report states this landing's range in its opening, the line DEPL-dShippedRelease-113 writes.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/loop/deploy_fixture.py`: the cases of §6

### Alternatives rejected

- **Stamping a report that states no range.** It hands a report of an unknown range this landing's binding, id 29's forgery by another door.

## 5. Production-readiness checklist

- security — the disposal stops writing into the record it certifies, so a report's binding is what the review wrote. A session able to land a new report stating this range passes, in the open, as unit 90 §5 states.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — S2 names each refused state, and each has its plant.
- observability — each state prints the line §2 names, on green and red.
- risks — a report from before the harness's opening rule states no range and is refused; a landing review is always newer than that rule.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py dispose-landing <sha> <report>` runs on a real diff-review stating
  another range, spelled unlike unit 90's line, it exits 2 naming the range, `review` keeps its value and
  `git status --porcelain` lists no change to the report.
  Red when: a foreign report gets this landing's range and passes every term.
- **AC2** — When it runs on a report stating no range, and on one stating two, it exits 2 printing `none`
  and `ambiguous`, and the intake stub's log is empty.
  Red when: a refused report files findings, or an unbound report is disposed.
- **AC3** — When it runs twice on an honest report, `git hash-object <report>` prints one value before
  and after.
  Red when: the disposal writes into the record the term reads.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · a real report of another range, its failing case the stamp restored · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 29 (HIGH, item H1) of the round-3 spec audit.

## 10. Reuse audit

The seam extended is `dispose-landing` (unit 14 S4), reading DEPL-dShippedRelease-109's read.
`python tools/codebase-map/reuse_lookup.py "refuse a report that names a different range without rewriting it"`
ranked the name-stem helper `report` and no reader of a binding, because `tools/loop/` is specced and
unbuilt, so no existing seam fits outside the parent's own module. The recall probe surfaced unit 90
and DEPL-dCarriedReceipt-2, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "may a disposal write into the report it certifies" --terms "dispose-landing stamp report range forged landing term binding guard own write"`
