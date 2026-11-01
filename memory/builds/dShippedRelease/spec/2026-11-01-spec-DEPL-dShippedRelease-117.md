# DEPL-dShippedRelease-117 — a report's shape line is compared with its rows where that line exists

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 49 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, which shares item H3 with
ids 4 and 30 (DEPL-dShippedRelease-115, -116). The harness says its appendix copy is not verified, and
unit 85's writer and term read the same rows, so a copy that lost rows agrees with itself. Unit 85 §3
rejected the `review-shape` line as the count source, and that stands, but the line is the one number the
report states apart from its table. This unit reads it as a guard, only where it exists.

## 2. Scope (IN)

- **S1** — The read. `read_shape_confirmed(text)` in `tools/workflows/review_replay.py` returns the
  `confirmed=` value of a `review-shape … at=synth …` line as an integer or `-`, or None with no such
  line. It rides the `--facts` door as the key `shape`. Observed by AC3.
- **S2** — The compare. Where `shape` is an integer and a table stands, a value differing from the
  confirmed rows fails. `dispose-landing` refuses, exit 2, printing
  `dispose — <sha8> · <rows> row(s) against confirmed=<n>`, and the term prints `forged · count`. Observed
  by AC1.
- **S3** — Where it does not exist. A report with a table and no shape line, or with `confirmed=-`, takes
  its rows with no compare. Observed by AC2.
- **S4** — Rows stay the count. `<n>` is DEPL-dShippedRelease-116's count on every path, and the shape line
  decides only whether a report passes. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The empty case, which also reads `shape`: DEPL-dShippedRelease-115.
- A comparison with the prose's stated count: `parse_appendix_rows`' refusal stays the replay benchmark's,
  by DEPL-dShippedRelease-116 §4.

### Edges

- **consumes-from** `DEPL-dShippedRelease-116` — the `--facts` door and the confirmed rows
- **consumes-from** `DEPL-dShippedRelease-85` — §3's non-goal and §4's alternative, which this unit amends
- **hands-off** `DEPL-dShippedRelease-115` — the key `shape`, which the empty case reads

## 4. Design

### Evidence

- `tools/workflows/tier2-review.js:1902` says the copy is not verified, and `:1904` orders the shape line copied above the appendix heading.
- `tools/workflows/tier2-review.js:79-83` renders `review-shape kind=… round=… intensity=… at=… raw=… confirmed=… …`, a count not yet produced printing `-`.
- Report item H3 records that 26 of 245 tracked reports with an appendix hold no shape line, and that unit 106 S49's report and the planted fixtures hold none. PINNED at the audit.
- This round's own report ends `review-shape kind=spec-audit round=1 intensity=full at=synth raw=73 confirmed=69 …`, and its appendix holds 69 `confirmed` rows, the real pair AC3 reads.

### Supersedes

- Unit 85 §3's non-goal "Reading the `review-shape` line's `confirmed=`" and §4's alternative: the line stays no count source, and it is a guard here.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_shape_confirmed` | function, `tools/workflows/review_replay.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/workflows/review_replay.py`: S1
- `tools/loop/deploy_items.py`: S2, S3, S4
- `tools/loop/deploy_fixture.py`: the cases of §6

### Alternatives rejected

- **The shape line as the count.** Unit 85 §4's reason stands: the rows are what gets filed.
- **Refusing a report with no shape line.** 26 tracked reports hold none, and unit 106 S49's writer and DEPL-dShippedRelease-113's write none.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — the key rides one spawn DEPL-dShippedRelease-116 already makes.
- error / empty / loading states — S3 names the two states with no compare, and §6 plants each.
- observability — the refusal names both numbers.
- risks — a shape line edited with its table agrees; the copy is the agent's, and the compare catches only a copy that diverged.
- testing — the criteria of §6 and the arms of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-shape-mismatch` plants a table of two confirmed
  rows under `confirmed=3`, `dispose-landing` exits 2 naming both numbers, the intake stub's log is
  empty, and `--deploy close` on a field set by hand exits 3 printing `forged · count`.
  Red when: a table that lost a row disposes at the lower count.
- **AC2** — When the case plants a table of two confirmed rows with no shape line, and again under
  `confirmed=-`, `dispose-landing` writes `disposed · 2 finding(s)`.
  Red when: the guard refuses the report unit 106 S49 writes.
- **AC3** — When `python tools/workflows/review_replay.py --facts memory/builds/dShippedRelease/reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`
  runs, it prints `shape` 69 and 69 rows reading `confirmed`.
  Red when: the read misses the harness's real line, so the guard never fires.
  figure: 69 is PINNED by that tracked report.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/workflows/review_replay.py · covers AC3 · the tracked report, its failing case the line matched without `at=synth` · none

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · `review-shape-mismatch`, its failing case the compare cut out · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 49 (HIGH, item H3) of the round-3 spec audit.

## 10. Reuse audit

The seam extended is the `--facts` door (DEPL-dShippedRelease-116), reading the line `renderShapeLine` writes at `tools/workflows/tier2-review.js:79`.
`python tools/codebase-map/reuse_lookup.py "cross check a stated confirmed count against the table rows"`
ranked the name-stem helper `rows` and no reader of the shape line in Python, so no existing seam reads
it and S1 is new beside `extract_stated_count`. The recall probe surfaced TOOL-dTotalRecall-11 and
TOOL-aQuotedBrief-3, which do not touch this line, so it answered nothing here.

Recall terms used:
`python tools/memory-recall/query.py "what does the review-shape line state" --terms "review-shape at=synth confirmed raw blocker high shape line appendix copy not verified"`
