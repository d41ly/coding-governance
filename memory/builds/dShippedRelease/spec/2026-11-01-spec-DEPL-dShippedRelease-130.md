# DEPL-dShippedRelease-130 — `dispose-with-reason`'s report has one home and one set of bytes, and a parser test replaces AC4's grep

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 15 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 4 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, HIGH, item H2. Unit 116 AC4 forbids
the literal `Appendix — every finding` in `tools/loop/deploy_items.py`, while `review_replay.py` requires that
exact heading and those columns, and unit 106 S49 names no home for the report `dispose-with-reason` writes.
So that writer either reds AC4 or writes a report `dispose-landing` refuses, and the way out of a refused
disposal, which units 114 S3, 118 S5 and 125 S31 all rely on, is dead. This unit gives the report one home,
states its bytes once, and turns AC4 into a test of what it was for: a second parser.

## 2. Scope (IN)

- **S1** — The home. `render_landing_record(units, base, sha, round, verdict, body)` in
  `tools/loop/deploy_items.py` returns the record in the order `tools/workflows/tier2-review.js:1853` states:
  `**Serves:** diff-review <units>`, a title, the range line
  ``**Reviewed range:** `<base8>...<sha8>`. **ROUND <round>.**``, `## Verdict: <verdict>`, then `body`. With `base`
  None it writes no range line. Observed by AC1, AC2.
- **S2** — The report's bytes. `write_reason_record(sha, reason, ref, root)` writes
  `render_landing_record(<the record's units>, <the pin's base>, sha, 1, "BLOCKED", body)` at unit 113 S1's path.
  `body` is one sentence and `## Appendix — every finding` with the columns `id`, `lens`, `ref`, `verdict` and
  `reason`, and one row: `1`, `owner`, `ref`, `confirmed`, and the reason. `ref` reads `landing:<sha8>`, and the
  reason is folded as `renderCell` folds a cell, line breaks to a space and `|` to `\|`. Observed by AC1, AC2.
- **S3** — The verb. `python deploy_items.py dispose-with-reason <sha> --reason <text>` runs S2 and then
  `dispose-landing <sha> <that path>`. An empty reason refuses, exit 2, writing nothing. On a `review` already
  reading `disposed · …` it prints that value and exits 0, writing nothing. Observed by AC1, AC3.
- **S4** — The parser test. Unit 116 AC4 reads: an `ast` walk of `deploy_items.py`, run by its `--selftest`, finds
  the heading literal in `write_reason_record` alone and in no comparison, so a writer stands and a second
  parser reds. Observed by AC4.
- **S5** — One route. Unit 106 S49's option `dispose-with-reason` is S3's verb, and its bytes are S2's.
  Observed by AC3.

## 3. Non-goals (OUT)

- `write_clean_record` calling this function: review id 34, in the minors batch.
- The report's reach when the pin refuses: DEPL-dShippedRelease-131.
- The binding's edge to unit 106: review id 52, in the minors batch.
- The `landing-review-stalled` item and `re-fire`: unit 106 S49 stands.

### Edges

- **consumes-from** `DEPL-dShippedRelease-116` — AC4, which this unit restates, and the `--facts` door the report must pass
- **consumes-from** `DEPL-dShippedRelease-110` — S2's refusal, which the range line must pass
- **consumes-from** `DEPL-dShippedRelease-112` — S1's `diff-review` binding, which the first line must pass
- **consumes-from** `DEPL-dShippedRelease-109` — `read_pin_range`, S2's base
- **consumes-from** `DEPL-dShippedRelease-113` — S1's record path
- **hands-off** `DEPL-dShippedRelease-106` — S49's report and option, which read as S2 and S3 state
- **hands-off** `DEPL-dShippedRelease-131` — `write_reason_record` with no base, the report of a refused pin
- **hands-off** `DEPL-dShippedRelease-138` — `render_landing_record`, which ids 3, 34 and 52 read

## 4. Design

### Evidence

- `tools/workflows/review_replay.py:64` is `APPENDIX_HEADING`, and `parse_appendix_rows` compares a stripped line with it (`:160`) and requires `id`, `lens`, `ref` and `verdict` (`:172`).
- `tools/workflows/tier2-review.js:1631` renders nine columns, `reason` among them, so a fifth column here is the harness's own name.
- Unit 106 S49 says only that the report holds `## Verdict: BLOCKED` and the reason as its one confirmed row, and unit 106 §8 F5 fixes that verdict.
- Units 112 S1, 115 §4 and 110 S2 each refuse a report missing the binding, the table or the range.

### The record

```
**Serves:** diff-review DEPL-dExample-1
# Landing review of 1a2b3c4d — disposed with a reason
**Reviewed range:** `0f0f0f0f...1a2b3c4d`. **ROUND 1.**
## Verdict: BLOCKED
The owner disposed this landing's review with the reason below.

## Appendix — every finding

| id | lens | ref | verdict | reason |
|---|---|---|---|---|
| 1 | owner | landing:1a2b3c4d | confirmed | the review died and is not being re-fired |
```

### Supersedes

- Unit 116 AC4 whole, and S4 here is its observation.
- Unit 106 S49's "writes a report with `## Verdict: BLOCKED` and the reason as its one confirmed row": the bytes are S2's.
- Unit 106 AC26's `dispose-with-reason` is S3's verb, and the criterion stands.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `render_landing_record` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `write_reason_record` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `dispose-with-reason` | verb of `deploy_items.py` | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1 to S5
- `tools/loop/deploy_fixture.py`: the case of §6

### Alternatives rejected

- **A `--render-record` door on `review_replay.py`.** It puts a writer in the kit that reads, and a spawn on a path with no read in it, for bytes `write_clean_record` needs in the same file.

## 5. Production-readiness checklist

- security — the verb writes one record under the build's own folder from text an owner supplies. The reason is folded into one cell, so it cannot forge a row or a heading, and the record is self-asserted, as units 85 and 90 §5 concede.
- perf / scale — N/A — a path an owner takes once per stalled landing.
- error / empty / loading states — S3 names the empty reason and the disposed value.
- observability — the verb prints the record's path, and `dispose-landing` its own line.
- risks — the `ast` test reads this module alone; a parser reached through another module is unit 116 §4's door by construction.
- testing — the criteria of §6 and the arms of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — unit 106 S49's item is what an operator meets, and DEPL-dShippedRelease-113 writes `help/deploy.md`.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py dispose-with-reason <sha> --reason 'a | b'` runs on a landing reading
  `pending`, the record's first line opens `**Serves:** diff-review`, `read-landing` prints
  `review<TAB>disposed · 1 finding(s) · <path>`, and the intake stub's log holds one line.
  Red when: the report reads `no-appendix` or `no diff-review binding`, so the way out is refused.
- **AC2** — When `python tools/workflows/review_replay.py --facts <that record>` runs, it prints `table` `ok`,
  `kind` `diff-review`, the landing's `range`, and one row whose `verdict` reads `confirmed` and whose `reason`
  reads `a | b`.
  Red when: a raw `|` in a reason shifts the verdict cell.
- **AC3** — When `python deploy_fixture.py --case review-reason-record` walks that record through the records
  landing, `--deploy close` records its transition and prints no `forged`; a second run of the verb prints the
  value and writes nothing.
  Red when: the route the owner item offers reads as a forgery.
- **AC4** — When `python deploy_items.py --selftest` runs, its `ast` arm prints `write_reason_record` as the one
  site of the heading, and on a scratch copy adding a function comparing a line with it the arm exits 1 naming
  that function.
  Red when: a second parser of the table lands.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC3 · `review-reason-record`, its failing case the appendix cut from `body` · none

New arm: tools/loop/deploy_items.py · covers AC4 · a scratch copy holding a second reader, its failing case a grep for the literal in place of the walk · none

## 8. Open questions

- **F1 — Where does the report's writer live?** The report says to choose this first. Options: (a) inside
  `deploy_items.py`, with AC4 scoped to a parser test; (b) outside it, as a `--render-record` door on
  `review_replay.py`. (b) has the reading kit write records, and id 34 needs the same opening in
  `deploy_items.py`. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, one function for both writers.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 4 (HIGH, item H2) of the round-4 spec audit.

## 10. Reuse audit

The seam extended is the record `write_clean_record` writes (unit 113 S2) and `render_review_report`'s opening order (unit 111 S1), the one the harness states.
`python tools/codebase-map/reuse_lookup.py "render a review record opening from one function"`
ranked the name-stem helpers `records` and `render` and no record writer, because `tools/loop/` is specced
and unbuilt, so no existing seam fits outside unit 113. The recall probe surfaced
TOOL-dUnstalledConvoy-13, TOOL-aLoosenedCeiling-6 and TOOL-dTieredTribunal-16, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "who writes a landing review record when the review died" --terms "dispose-with-reason record opening render BLOCKED confirmed row appendix binding Serves range writer"`
