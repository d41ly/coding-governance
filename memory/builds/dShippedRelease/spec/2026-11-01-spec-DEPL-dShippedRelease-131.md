# DEPL-dShippedRelease-131 — a refused pin has one way out, and `dispose-landing` admits it

**Status:** OPEN · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 35 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-126-round4-disposal-return.md) | research | DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 5 of `reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md`, HIGH, item H3, which stands beside
id 62 in the minors batch. Unit 125 S31's only disposal for a refused pin is `dispose-with-reason`, whose report
states no range. That verb runs `dispose-landing`, unit 110 S2 refuses `none` with exit 2, and S2 also needs
the pin that refused, while S31 lands on units 80, 90 and 106 S49 and never on unit 110. On a linear-history
landing under `owed` the owner's one option exits 2, `review` stays `unfired`, and the close holds for ever.
This unit states the one exception, keyed so it cannot admit anything else.

## 2. Scope (IN)

- **S1** — The landing. Unit 125 S31 lands on unit 110 S2 too, and this unit's edges carry that. Observed by AC1.
- **S2** — The report. On a refused pin `dispose-with-reason` passes `render_landing_record` a `base` of None and
  `write_reason_record` a `ref` of `pin:<class>`, so the report states no range and names the class that
  refused. Observed by AC1.
- **S3** — The admission. `test_report_names_landing` is true on a `range` of `none` only when `read_pin_range`
  refuses naming a class, the report's verdict is `BLOCKED`, and its one confirmed row's `ref` reads
  `pin:<that class>`. Unit 110 S2 calls that function for its `none` refusal, so the skip and the term read one
  test. Observed by AC1, AC2, AC3.
- **S4** — Everything else stands. A `none` report while the pin answers is refused by unit 110 S2, printing
  `none`, and a `none` report under any other verdict, or naming another class, is no admission. Observed by
  AC2, AC3.
- **S5** — The term. Unit 125 S30's `pin refused` hold fires on a report S3 does not admit. A field naming an
  admitted report passes `landing`, so S30 and S31 no longer contradict each other. Observed by AC1.

## 3. Non-goals (OUT)

- The line `dispose-landing` prints on a refused pin for any other report: review id 62, in the minors batch.
- The pin's refusal classes: unit 14 S3's pin and the `linear-history` class of unit 125 AC20 stand.
- A batch unit's `landing on` list being checked against what it contradicts: the audit's left-shift item.

### Edges

- **consumes-from** `DEPL-dShippedRelease-125` — S30 and S31, which this unit reconciles
- **consumes-from** `DEPL-dShippedRelease-110` — S2's refusal of `none`, which gains its one exception
- **consumes-from** `DEPL-dShippedRelease-109` — `test_report_names_landing` and `read_pin_range`, which S3 reads
- **consumes-from** `DEPL-dShippedRelease-130` — `render_landing_record` and `write_reason_record`, which S2 calls
- **hands-off** `DEPL-dShippedRelease-138` — S3's exception, beside which id 62 states every other refused pin

## 4. Design

### Evidence

- Unit 125 S31: "Its disposal is `dispose-with-reason` alone, whose report states no range, and `test_report_names_landing` admits that only while the pin refuses with that class."
- Unit 110 S2 refuses a `range` of `none` with exit 2 and calls no such test, so the two texts disagree (report ids 5 and 62).
- Unit 125 S30 prints `held · check_landing_review · pin refused · <class>` with no condition, and §4 of unit 109 runs `landing` last, so the hold fires after the report passed every other term.
- A row's `ref` is a cell the door already returns (DEPL-dShippedRelease-116 S2), so the class needs no new `--facts` key.

### The refused pin, by report

| `range` | Verdict | Row `ref` | `read_pin_range` | `test_report_names_landing` |
|---|---|---|---|---|
| `none` | `BLOCKED` | `pin:<class>` | refuses with that class | true |
| `none` | `BLOCKED` | `pin:<class>` | refuses with another, or answers | false |
| `none` | any other | any | refuses | false |
| a pair | any | any | refuses | false |

### Supersedes

- Unit 125 S31's landing list, which gains unit 110 S2.
- Unit 125 S30's unconditional hold, which reads as S5 states.
- Unit 110 S2's refusal of `none`, which reads as S3 and S4 state.
- Unit 125 AC21 stands, reached by S3.

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S2, S3, S5
- `tools/loop/deploy_fixture.py`: the cases of §6

### Alternatives rejected

- **Skipping the compare on any `BLOCKED` report.** A foreign `BLOCKED` report stating no range would then certify a landing whose pin answers.
- **Admitting by a new `--facts` key.** The class already sits in a cell the door returns.

## 5. Production-readiness checklist

- security — the exception is keyed on the live pin's refusal, the verdict and the class, so a report cannot admit itself where the pin answers. A session able to land a report through this route is the exposure units 83 to 90 §5 state, and the report names itself `BLOCKED`.
- perf / scale — N/A — one read on a path that runs once per landing.
- error / empty / loading states — §4's table states each report, and §6 plants the admitted one and two refused ones.
- observability — the term prints its line on each state, and an admitted report's row names the class.
- risks — a dead pin read is no refusal, so it admits nothing, and id 62's line holds it.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — unit 106 S49's item is what an operator meets.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-owed-linear-history` runs under `review.deploy = "owed"`
  and answers `dispose-with-reason`, it exits 0, `read-landing` prints `review<TAB>disposed · 1 finding(s)`, the
  record's row `ref` reads `pin:linear-history`, and `--deploy close` records its transition.
  Red when: unit 110 S2 refuses the owner's one option, so the close holds for ever.
- **AC2** — When `--case review-none-pin-answers` runs that report on a landing whose pin answers,
  `dispose-landing` exits 2 printing `none`, the case unit 110 AC2 names.
  Red when: the exception reaches a landing with a usable pin.
- **AC3** — When the case runs a `CLEAN WITH FIXES` report stating no range, and a `BLOCKED` report naming
  another class, on a refused pin, each exits 2, and `review` keeps its value.
  Red when: a report other than the owner's disposal passes on a refused pin.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · `review-none-pin-answers`, its failing case the admission keyed on the `BLOCKED` verdict alone · none

## 8. Open questions

- **F1 — How is the class bound to the report?** Options: (a) the row's `ref` cell, `pin:<class>`; (b) no binding,
  admitting on the live pin alone; (c) a `--facts` key. (b) admits any `BLOCKED` no-range report on a refused pin,
  and (c) adds a key for what a cell already carries. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3,
  deny by default on a key the door already returns. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 5 (HIGH, item H3) of the round-4 spec audit.

## 10. Reuse audit

The seam extended is `test_report_names_landing` (unit 109 S4), the function unit 125 S31 names.
`python tools/codebase-map/reuse_lookup.py "admit a report with no range while the pin refuses"`
ranked the name-stem helpers `report`, `CensusRefused` and `Report` and no reader of a binding, because
`tools/loop/` is specced and unbuilt, so no existing seam fits outside that function. The recall probe
surfaced unit 90, unit 14's scout and the round-3 report, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "what does a refused landing pin do at the disposal" --terms "review_pin refusal linear-history dispose-landing test_report_names_landing pin refused class none owner way out"`
