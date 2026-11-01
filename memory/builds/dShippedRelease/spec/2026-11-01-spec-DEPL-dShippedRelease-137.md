# DEPL-dShippedRelease-137 — `read_appendix_table` reads `malformed` on a row it cannot place

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 15 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-138 |
| [2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-134 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-131 DEPL-dShippedRelease-138 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 58 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, HIGH, item H9. Unit 116 S1 promises
every table row, and `malformed` means only a missing column. The kept loop holds `elif table: break` and
`zip(header, cells)`, so one stray blank or wrapped line ends the table with `table` still `ok`, and every later row
is gone. Confirmed rows vanish, `<n>` is low, fewer patches are filed, and the term agrees, because writer and term
read one door. This is the class `memory/gotchas/parser-drops-rows-it-cannot-place.md` names.

## 2. Scope (IN)

- **S1** — A row it cannot place. `read_appendix_table` reads `malformed` on a body row whose cell count differs from
  the header's, so `zip` never truncates a row. Observed by AC1.
- **S2** — A table cut in two. Any `|` line after the table ended reads `malformed`, so the `break` never hides a row.
  Observed by AC1.
- **S3** — Unit 115 S4 reads the rest. A `malformed` table fails `check_report_table` under any verdict, so
  `dispose-landing` refuses, exit 2, and the term prints `forged · count`. Observed by AC2.
- **S4** — The replay stands. `parse_appendix_rows` carries the `malformed:` error to its callers, the refusal shape
  `parse_record_findings` already reports. Observed by AC3.

## 3. Non-goals (OUT)

- A `verdict` cell outside the set: DEPL-dShippedRelease-118 S1.
- A table with no rows: DEPL-dShippedRelease-136.
- Stdin and the door's failures: review ids 24 and 61, in the minors batch.

### Edges

- **consumes-from** `DEPL-dShippedRelease-116` — S1's `read_appendix_table` and S2's `malformed`
- **consumes-from** `DEPL-dShippedRelease-115` — S4, which fails a `malformed` table under any verdict
- **hands-off** `DEPL-dShippedRelease-143` — S1, S2 and §4's first Supersedes bullet, whose promise that unit completes (round-5 id 41)
- **hands-off** `DEPL-dShippedRelease-144` — `review-replay selftest` joins §7's list, and the batch reads S3, §6 and the rest of §7 (round-5 ids 10, 30, 52)

## 4. Design

### Evidence

- `tools/workflows/review_replay.py:164-168` is the kept loop, and `:175` is the `zip`.
- The docstring at `:157` records that "one cut row ends the table and drops every row after it".
- `tools/workflows/tier2-review.js:1902` says the appendix copy is not verified, so a wrapped row is a real input.
- A read-only probe over the 244 tracked reports holding an appendix found no row whose cell count differs from its header's, and no `|` line after a table's end. PINNED at `e8ced8ac`.

### Supersedes

- Unit 116 S1's "every table row": each row is returned, or the table reads `malformed`.
- Unit 116 S2's `malformed` gains these two states.
- Unit 115 S4's "A table the door calls `malformed`, a missing column" reads with both.

### Files touched (estimate)

- `tools/workflows/review_replay.py`: S1, S2, S4
- `tools/loop/deploy_fixture.py`: the case of §6

### Alternatives rejected

- **Padding a short row with empty cells.** It files a finding from half a row, and the verdict cell may be the missing one.
- **Skipping a blank line inside the table.** It reads a row the copy may have cut, and a wrapped row still splits.

## 5. Production-readiness checklist

- security — closes a count that agrees with itself on a damaged report; no new surface.
- perf / scale — N/A — one length compare per row.
- error / empty / loading states — S1 and S2 name the two damaged shapes, and AC1 plants each.
- observability — `--facts` prints `malformed`, and the error names the row.
- risks — a harness that wraps one honest row reds its landing, and `dispose-with-reason` is the way out; a silent low count is the alternative.
- testing — the criteria of §6 and the arms of §7.
- migration — N/A — no tracked report holds either shape, as §4's probe shows.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/workflows/review_replay.py --facts <plant>` reads a table with a blank line between
  two rows, and one with a row of too few cells, each prints `table` `malformed`.
  Red when: the `break` or the `zip` stands, and rows after the damage vanish.
- **AC2** — When `python deploy_items.py dispose-landing <sha> <report>` runs on either plant, it exits 2, `review` keeps
  its value and the intake stub's log is empty.
  Red when: writer and term agree on a low count.
- **AC3** — When `python tools/workflows/review_replay.py --known <plant> --candidate <record>` reads such a plant, it
  exits 2 printing `malformed`.
  Red when: the replay benchmark scores a table the door refuses.

## 7. Gates

`verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/workflows/review_replay.py · covers AC1 AC3 · the two inline plants, their failing case the existing `break` and `zip` · `ARMS_DECLARED` rises by two

New arm: tools/loop/deploy_fixture.py · covers AC2 · a report holding either plant, its failing case `malformed` meaning a missing column alone · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 58 (HIGH, item H9) of the round-4 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-5 spec audit's promoted units declare toward this unit (units 143, 144); the bullet to unit 144 carries the sentence this unit's own pass needs, because that batch builds last, and no other section moved.

## 10. Reuse audit

The seam extended is `read_appendix_table` (unit 116 S1), the loop at `tools/workflows/review_replay.py:164`.
`python tools/codebase-map/reuse_lookup.py "malformed table when a row cell count differs from the header"`
ranked the name-stem helpers `rows`, `row` and `counts` and no table reader, and the class is
`memory/gotchas/parser-drops-rows-it-cannot-place.md`, which a read of the report found, so the probe and the
source disagree and the source stands. The recall probe surfaced PLAY-dOrderedCharter-24 and TOOL-dTotalRecall-97,
which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does a table parser refuse a row it cannot place" --terms "parser drops rows cannot place cell count header malformed blank line break zip appendix table"`
