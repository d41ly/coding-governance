# DEPL-dShippedRelease-143 — `read_appendix_table` reads `malformed` on a table with no separator line

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 16 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md) | research | DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 41 of `reviews/2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md`, HIGH, item H5. Unit 137 promises
each row is returned or the table reads `malformed`, and names two damaged shapes. `tools/workflows/review_replay.py:175`
discards `table[1]` by position and never tests that it is a separator. A plant holding a header, two confirmed rows
and no separator, stated count 1, returned only row 2 with error None. Unit 137 S1's cell count cannot see it, because
the swallowed row has the header's cell count. On a report with no shape line, or with `confirmed=-`, one confirmed
finding goes unfiled and writer and term agree. This unit tests the line it discards, and repairs unit 137, order
15, at the next step.

## 2. Scope (IN)

- **S1** — The test. `read_appendix_table` reads `malformed` unless every cell of `table[1]` matches `:?-+:?` whole, the
  error reading `malformed: the appendix has no separator line`. The `len(table) < 2` no-appendix reading stands.
  Observed by AC1.
- **S2** — Unit 115 S4 reads the rest, as it does for unit 137 S3: `check_report_table` fails a `malformed` table under
  any verdict, so `dispose-landing` refuses, exit 2, filing nothing. Observed by AC2.
- **S3** — The replay stands. `parse_appendix_rows` carries this error as unit 137 S4 carries the other two.
  Observed by AC3.
- **S4** — No reader breaks. The walk of §4's Evidence holds on every tracked report, and on each inline fixture of
  `tools/workflows/review_replay.py`. Observed by AC4.

## 3. Non-goals (OUT)

- A table truncated at its last row: §5 states it, and only unit 117's shape line can catch that.
- Which row shapes are `malformed` otherwise: DEPL-dShippedRelease-137.
- A checklist item that a parser test each positional line it discards: the audit's left-shift item.

### Edges

- **consumes-from** `DEPL-dShippedRelease-116` — S1's `read_appendix_table` and S2's `malformed`
- **consumes-from** `DEPL-dShippedRelease-137` — S1, S2 and §4's first Supersedes bullet, whose promise this unit completes

## 4. Design

### Evidence

- `tools/workflows/review_replay.py:175` builds rows from `table[2:]`, and `:169-170` is the two-line floor.
- `tools/workflows/tier2-review.js:1902` says the appendix copy is not verified, and unit 116 leaves the stated-count check in `parse_appendix_rows`, out of `read_appendix_table`.
- A read-only walk of `git ls-files 'memory/**/reviews/*.md'` found 245 appendix tables and 0 whose second line is not a separator. PINNED at `e4c33972`, re-derivable by AC4.

### Supersedes

- Unit 137 §4's "each row is returned, or the table reads `malformed`": it reads with S1.
- Unit 137 §5's "S1 and S2 name the two damaged shapes": three, with S1 here.
- Unit 115 S4's "a missing column" reads with this state too, as unit 137 restates it.

### Files touched (estimate)

- `tools/workflows/review_replay.py`: S1, S3 and the inline plant
- `tools/loop/deploy_fixture.py`: the case of §6

### Alternatives rejected

- **Reading `table[1]` as a row when it fails the test.** It files a finding from a table the harness did not write, and its header may be the damaged line.
- **Comparing the row count with the stated count here.** Unit 116 keeps that check in `parse_appendix_rows`, and a report with `confirmed=-` states none.

## 5. Production-readiness checklist

- security — closes a count that agrees with itself on a damaged report; no new surface.
- perf / scale — N/A — one regex over one line per report.
- error / empty / loading states — S1 names the third damaged shape, and AC1 plants it.
- observability — `--facts` prints `malformed`, and the error names the line.
- risks — what stays unseen is a copy truncated at the last row: every line left has its place, so only unit 117's shape line can catch it.
- testing — the criteria of §6 and the arms of §7.
- migration — N/A — no tracked report holds this shape, as §4's walk shows.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/workflows/review_replay.py --facts <plant>` reads a table of a header and two confirmed
  rows with no separator line, it prints `table` `malformed` and exits 0.
  Red when: `table[2:]` stands, and the first body row vanishes with no error.
- **AC2** — When `python deploy_items.py dispose-landing <sha> <report>` runs on that plant, it exits 2, `review` keeps its
  value and the intake stub's log is empty.
  Red when: a confirmed finding goes unfiled and writer and term agree on a low count.
- **AC3** — When `python tools/workflows/review_replay.py --known <plant> --candidate <record>` reads that plant, it exits 2
  printing `malformed`.
  Red when: the replay benchmark scores a table the door refuses.
- **AC4** — When `python -c` walks `git ls-files 'memory/**/reviews/*.md'` and calls `read_appendix_table` on each report
  holding an appendix, no table reads `malformed` on this error, and the count of tables read is above 0.
  Red when: the test refuses a landed report, or the walk reads nothing.
  figure: DERIVED at observation; 245 at `e4c33972`.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `review-replay selftest` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/workflows/review_replay.py · covers AC1 AC3 · the inline plant, its failing case the existing `table[2:]` · `ARMS_DECLARED` rises by one

New arm: tools/loop/deploy_fixture.py · covers AC2 · a report holding that plant, its failing case `malformed` meaning unit 137's two states alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 41 (HIGH, item H5) of the round-5 spec audit.

## 10. Reuse audit

The seam extended is `read_appendix_table` (units 116 and 137), the loop at `tools/workflows/review_replay.py:164`.
`python tools/codebase-map/reuse_lookup.py "table separator line discarded by position in a markdown parser"`
ranked the name-stem helper `parse` and no table reader, so no existing seam fits outside that function. The recall
probe surfaced unit 137 and this round's report, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what does a table parser do with a line it discards by position" --terms "separator line header table appendix positional discard malformed parse_appendix_rows read_appendix_table rows cell"`
