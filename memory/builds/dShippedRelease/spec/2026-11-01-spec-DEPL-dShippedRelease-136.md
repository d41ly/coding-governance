# DEPL-dShippedRelease-136 — the table rule keys on confirmed rows, so a header with no rows disposes nothing

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 15 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 57 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, HIGH, item H8. `parse_appendix_rows`
reads `no-appendix` only for `len(table) < 2`, so a heading, a header and a separator is an `ok` table with zero
rows, and unit 115 §4's first row passes it under any verdict. A `CLEAN WITH FIXES` report whose appendix lost
every row, with no shape line, writes `disposed · 0 finding(s)`, files nothing and passes the term, the outcome
unit 115 says it closes. A table holding only refuted rows passes the same way. This unit keys the rule on the rows.

## 2. Scope (IN)

- **S1** — No rows. `check_report_table` fails a table holding zero rows of any verdict, under every verdict, because
  `renderAppendix` returns `''` on an empty ledger and an honest harness never writes one. Observed by AC1.
- **S2** — No confirmed rows. `check_report_table` fails `CLEAN WITH FIXES` and `BLOCKED` with zero confirmed rows,
  so a refuted-only table passes only under `CLEAN`. Observed by AC2, AC3.
- **S3** — The lines. `dispose-landing` refuses each, exit 2, printing `dispose — <sha8> · table holds no row` or
  `dispose — <sha8> · no confirmed row under <verdict>`, filing nothing, and the term prints `forged · count`.
  Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The door, and a row it cannot place: DEPL-dShippedRelease-116 and -137.
- `BLOCKED` at `<n>` 0: unit 84 S2 stands, and S2 refuses it earlier.
- A checklist item that a presence test states what an empty instance reads as: the audit's left-shift item.

### Edges

- **consumes-from** `DEPL-dShippedRelease-115` — S1 and §4's table, which this unit restates
- **consumes-from** `DEPL-dShippedRelease-116` — the rows `read_report_facts` returns

## 4. Design

### Evidence

- `tools/workflows/review_replay.py:169` tests `len(table) < 2`, and rows come from `table[2:]`.
- `tools/workflows/tier2-review.js:1632` returns `''` when a ledger holds no row.
- Report id 57 scanned 246 tracked reports and found no zero-row table and no non-`CLEAN` report with zero confirmed rows. A read-only probe at this spec's writing found no zero-row table among 244 reports holding an appendix. PINNED at `e8ced8ac`.

### The empty case

Unit 115 §4's table, with its first row split by rows held.

| Verdict | Table | Rows | Confirmed rows | Shape line | S1 of unit 115 |
|---|---|---|---|---|---|
| `CLEAN` | present | at least 1 | any | any | passes, and DEPL-dShippedRelease-117 reads the compare |
| `CLEAN WITH FIXES`, `BLOCKED` | present | at least 1 | at least 1 | any | passes, and DEPL-dShippedRelease-117 reads the compare |
| `CLEAN WITH FIXES`, `BLOCKED` | present | at least 1 | 0 | any | fails |
| any | present | 0 | 0 | any | fails |
| `CLEAN` | none | - | - | none, or `confirmed=0` | passes |
| `CLEAN` | none | - | - | `confirmed` above 0, or `-` | fails |
| `CLEAN WITH FIXES`, `BLOCKED` | none | - | - | any | fails |
| any | malformed | - | - | any | fails |

### Supersedes

- Unit 115 S1's "passes a report with a table".
- Unit 115 §4's table: the table above.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3
- `tools/loop/deploy_fixture.py`: the cases of §6

## 5. Production-readiness checklist

- security — closes a green term on a report that lost its rows; no new surface.
- perf / scale — N/A — a compare on a path that already runs once per landing.
- error / empty / loading states — §4's table states each.
- observability — each state prints the line S3 names.
- risks — a `CLEAN` report keeping one refuted row and losing confirmed ones still passes; the verdict is the review's word, and DEPL-dShippedRelease-117 compares a shape line where one stands.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py dispose-landing <sha> <report>` runs on a `CLEAN WITH FIXES` report whose
  table is a header and a separator, with no shape line, it exits 2 printing `table holds no row`, `review` keeps its
  value and the intake stub's log is empty; a `CLEAN` report with the same table exits 2 too.
  Red when: a table counts as present by its header alone.
- **AC2** — When it runs on a `CLEAN WITH FIXES` report holding only refuted rows, it exits 2 printing
  `no confirmed row`.
  Red when: findings vanish on `disposed · 0 finding(s)` behind a table of refuted rows.
- **AC3** — When it runs on a `CLEAN` report holding one refuted row, it writes `disposed · 0 finding(s)`, unit 113 AC2's
  record.
  Red when: the rule refuses a review whose every finding was refuted.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · a header-only table, its failing case the rule keyed on the table's presence · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 57 (HIGH, item H8) of the round-4 spec audit.

## 10. Reuse audit

The seam extended is `check_report_table` (unit 115 S1), reading the rows of `read_report_facts` (unit 116 S3).
`python tools/codebase-map/reuse_lookup.py "refuse a table with a header and no rows"`
ranked the name-stem helpers `rows`, `row` and `extract_row` and no reader of a report table, so no existing
seam fits outside that function. The recall probe surfaced TOOL-aReplayedCard-16, TOOL-dWitnessedBar-16 and this
round's report, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what does an empty appendix table read as" --terms "header separator zero rows renderAppendix empty ledger confirmed rows table present verdict count presence"`
