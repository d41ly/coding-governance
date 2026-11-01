# DEPL-dShippedRelease-118 — a row left unadjudicated stops the disposal, so a degraded review certifies nothing

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 50 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, item H4. Unit 85 S1
counts only `confirmed` cells, while `tools/workflows/tier2-review.js:1598` also emits `uncertain` and
`unverified`, and `:2068` reports such a run as PARTIAL. No unit names them, so a review whose findings
were never adjudicated writes `disposed · 0 finding(s)`, files nothing for them and passes `count`. This
unit gives the outstanding rows their third state.

## 2. Scope (IN)

- **S1** — The closed set. `REPORT_ROW_VERDICTS` in `tools/loop/deploy_items.py` holds `confirmed`,
  `refuted`, `uncertain` and `unverified`, and `check_row_verdicts(rows)` returns the rows reading
  `uncertain`, `unverified` or a value outside the set. Observed by AC1, AC2.
- **S2** — The writer. `dispose-landing` refuses a report S1 flags, exit 2, printing
  `dispose — <sha8> · <k> finding(s) not adjudicated`, before it files anything, and `review` stays
  `pending`. Observed by AC1.
- **S3** — The term. `check_review_field` prints `forged · count` on a field naming such a report.
  Observed by AC3.
- **S4** — One fact. `--selftest` compares `REPORT_ROW_VERDICTS` with the literals of
  `tools/workflows/tier2-review.js`, reached by `resolve_kit_dir("workflows", ...)`, and prints
  `not graded · no workflows kit` where the kit is absent, the shape unit 84 S3 states. Observed by AC4.
- **S5** — The route. A held `pending` reaches unit 106 S49's owner item, whose `re-fire` and
  `dispose-with-reason` are the two ways out. Observed by AC2.

## 3. Non-goals (OUT)

- The rows: DEPL-dShippedRelease-116.
- The `review-stalled` item itself: unit 106 S49 stands.

### Edges

- **consumes-from** `DEPL-dShippedRelease-116` — every row's verdict cell
- **consumes-from** `DEPL-dShippedRelease-85` — S1's `confirmed`-only count
- **consumes-from** `DEPL-dShippedRelease-84` — S3's shape for a compare across the kit boundary
- **hands-off** `DEPL-dShippedRelease-106` — S49's owner item, the way out of this refusal

## 4. Design

### Evidence

- `tools/workflows/tier2-review.js:1598` writes `confirmed`, `refuted` or `uncertain` from a skeptic's verdict, and `unverified` otherwise.
- `tools/workflows/tier2-review.js:2068` reports `PARTIAL: <n> finding(s) are unverified`.
- A grep of units 14, 73, 83, 84, 85, 90 and 106 for `uncertain` printed nothing at the audit, and report id 50 tallied 7288 `confirmed` and 844 `refuted` rows only, so no tracked record plants this. PINNED at the audit.

### Supersedes

- Unit 85 S1's silence on every value but `confirmed`.
- The term table of DEPL-dShippedRelease-109 reads this rule in its `count` row.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `check_row_verdicts` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `REPORT_ROW_VERDICTS` | module constant, `tools/loop/deploy_items.py` | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3, S4
- `tools/loop/deploy_fixture.py`: the cases of §6

### Alternatives rejected

- **Filing and counting each outstanding row.** It turns a finding nobody adjudicated into a patch ask, and it certifies the landing with the review still degraded.

## 5. Production-readiness checklist

- security — closes a certification by a degraded review; no new surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — S1 and S2 name the outstanding and the unknown value, and §6 plants each.
- observability — the refusal counts the outstanding rows, and the term prints its line.
- risks — a review with one unverified row holds the close until an owner answers; a degraded review certifying a landing is the alternative.
- testing — the criteria of §6 and the arms of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — unit 106 S49's item is what an operator meets.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py dispose-landing <sha> <report>` runs on a `CLEAN WITH FIXES` report
  holding one `unverified` row, and again one `uncertain` row, each exits 2 printing `not adjudicated`,
  `read-landing` prints `review<TAB>pending`, and the intake stub's log is empty.
  Red when: a review the harness calls PARTIAL certifies the landing.
- **AC2** — When it runs on a row reading `lgtm`, it exits 2 naming the count; answering
  `dispose-with-reason` afterwards writes `disposed`.
  Red when: an unknown verdict counts as refuted, or the refusal has no way out.
- **AC3** — When `python deploy_fixture.py --case review-unadjudicated` sets the field by hand to the report
  of AC1, `--deploy close` exits 3 printing `forged · count`.
  Red when: the count passes on rows nobody adjudicated.
- **AC4** — When `python deploy_items.py --selftest` runs with a fifth literal added to a scratch copy of
  `tools/workflows/tier2-review.js`, it exits 1 naming `REPORT_ROW_VERDICTS`; on the tree it exits 0.
  Red when: the harness emits a verdict no reader enumerates.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `review-unadjudicated`, its failing case `unverified` read as no row · none

New arm: tools/loop/deploy_items.py · covers AC4 · the scratch copy of the harness, its failing case the compare cut out · none

## 8. Open questions

- **F1 — What does an outstanding row do?** Options: (a) refuse the disposal and leave `pending`; (b) file
  and count each one. (b) certifies a review the harness calls degraded, and (a) has a route through unit
  106 S49. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the report's first option. widens:
  none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 50 (HIGH, item H4) of the round-3 spec audit.

## 10. Reuse audit

The seam extended is `dispose-landing` and `check_review_field` (units 14, 73), reading DEPL-dShippedRelease-116's rows, with the compare unit 84 S3 states.
`python tools/codebase-map/reuse_lookup.py "enumerate verdict column values a report may hold"`
ranked the name-stem helper `report` and no reader of the column, because every Python reader takes
`confirmed` alone, so no existing seam fits. The recall probe surfaced TOOL-aFoldedQuarry-2 and unit 85,
which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what verdict values can an appendix row hold" --terms "verdict uncertain unverified confirmed refuted PARTIAL UNVERIFIED skeptic appendix degraded review"`
