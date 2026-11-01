# DEPL-dShippedRelease-115 — no appendix is valid only on a clean verdict, so the guard reads what the count does not

**Status:** DEFERRED · rev-3 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-123 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-124 DEPL-dShippedRelease-119 DEPL-dShippedRelease-121 DEPL-dShippedRelease-120 DEPL-dShippedRelease-122 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 4 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, which shares item H3 with
ids 30 and 49 (DEPL-dShippedRelease-116, -117). Unit 85 S1 counts 0 for a report with no table, and
`dispose-landing` takes `<n>` from the same function, so the guard shares its input with what it
guards. A `CLEAN WITH FIXES` report that lost its appendix writes `disposed · 0 finding(s)`, files nothing
and passes `count`, and unit 85 §5's "loud direction" is false. This unit keys the empty case on inputs
the count does not read: the verdict and the shape line.

## 2. Scope (IN)

- **S1** — The rule. `check_report_table(facts, verdict)` in `tools/loop/deploy_items.py` passes a report
  with a table, and passes a report with none only on `## Verdict: CLEAN` with no shape line or with a
  shape line reading `confirmed=0`. Observed by AC1, AC2, AC3.
- **S2** — The writer. `dispose-landing` calls S1 before it files anything, and a failure is refused,
  exit 2, printing `dispose — <sha8> · no appendix under <verdict>`, with `review` keeping its value.
  Observed by AC1.
- **S3** — The term. `check_review_field` calls S1, and a failure prints `forged · count`. Observed by
  AC4.
- **S4** — A malformed table. A table the door calls `malformed`, a missing column, fails S1 under any
  verdict. Observed by AC2.

## 3. Non-goals (OUT)

- The rows and the door: DEPL-dShippedRelease-116.
- The shape line's compare with a table's rows: DEPL-dShippedRelease-117.
- A checklist item that a guard and its value must not read one function: the audit's left-shift item,
  and this rule is its one instance.

### Edges

- **consumes-from** `DEPL-dShippedRelease-116` — `read_report_facts`' `table` and rows
- **consumes-from** `DEPL-dShippedRelease-117` — the key `shape`, which the empty case reads
- **consumes-from** `DEPL-dShippedRelease-85` — S1's empty case and §5's risk line, which this unit supersedes
- **hands-off** `DEPL-dShippedRelease-136` — S1 and §4's table, which that unit restates (round-4 id 57)
- **hands-off** `DEPL-dShippedRelease-137` — S4, which fails a `malformed` table under any verdict (round-4 id 58)
- **hands-off** `DEPL-dShippedRelease-144` — AC4's shape, which the batch repeats (round-5 id 10)

## 4. Design

### Evidence

- `tools/workflows/tier2-review.js:1902` says the appendix copy is not verified, and report id 30 read 14 `CLEAN WITH FIXES` and 42 `BLOCKED` records with no appendix among 72 tracked records. PINNED at the audit.
- The review-shape line carries `confirmed=<n>` at `at=synth`, and a count the run has not produced prints `-` (`tools/workflows/tier2-review.js:75-83`).
- Unit 84 S2 catches only `BLOCKED` at `<n>` 0.

### The empty case

| Verdict | Table | Shape line | S1 |
|---|---|---|---|
| any | present, well-formed | any | passes, and DEPL-dShippedRelease-117 reads the compare |
| `CLEAN` | none | none | passes |
| `CLEAN` | none | `confirmed=0` | passes |
| `CLEAN` | none | `confirmed` above 0, or `-` | fails |
| `CLEAN WITH FIXES`, `BLOCKED` | none | any | fails |
| any | malformed | any | fails |

### Supersedes

- Unit 85 S1's "a report with no such table counts 0".
- Unit 85 §5's risks line: a report with findings and no table is refused at the disposal, by the plant AC1 names, and it never reaches the term by that route.
- Unit 14 AC6's plant reads with `confirmed=0` or no shape line: DEPL-dShippedRelease-113's record holds none.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `check_report_table` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3, S4
- `tools/loop/deploy_fixture.py`: the cases of §6

## 5. Production-readiness checklist

- security — closes a green term on a report whose findings vanished; no new surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — §4's table states each.
- observability — each state prints the line §2 names, on green and red.
- risks — a `CLEAN` report that lost its appendix and its shape line reads clean; the verdict is the review's word, and nothing then says otherwise.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py dispose-landing <sha> <report>` runs on a `CLEAN WITH FIXES` report
  whose appendix heading is renamed, it exits 2 printing `no appendix`, `review` keeps its value and the
  intake stub's log is empty.
  Red when: confirmed findings vanish on `disposed · 0 finding(s)`.
- **AC2** — When it runs on a `CLEAN` report stating `confirmed=2` with no appendix, on one stating
  `confirmed=-`, and on one whose table has no `verdict` column, each exits 2.
  Red when: a report whose own shape line says findings exist disposes at 0.
- **AC3** — When it runs on a `CLEAN` report with no table and no shape line, and on one stating
  `confirmed=0`, each writes `disposed · 0 finding(s)`.
  Red when: the honest clean record, DEPL-dShippedRelease-113's, is refused.
- **AC4** — When `python deploy_fixture.py --case review-no-appendix` sets the field by hand to the report
  of AC1, `--deploy close` exits 3 printing `forged · count`.
  Red when: writer and term agree on 0 over a report that lost its findings.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 AC4 · `review-no-appendix`, its failing case a report with no table counted 0 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 4 (HIGH, item H3) of the round-3 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-4 spec audit's promoted units declare toward this unit (units 136, 137); no scope, design or criterion moved.
- rev-3 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-5 spec audit's promoted units declare toward this unit (units 144); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `check_review_field` and `dispose-landing` (units 73, 14), reading DEPL-dShippedRelease-116's facts.
`python tools/codebase-map/reuse_lookup.py "refuse an empty appendix unless the verdict is clean"`
ranked `CensusRefused`, a name-stem hit in another kit, and no reader of a report's empty case, so no
existing seam fits and §4's table is new. The recall probe surfaced TOOL-dMergedTally-1 and unit 79,
which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "when is a report with no appendix valid" --terms "no-appendix CLEAN WITH FIXES shape line confirmed count guard empty case dispose forged"`
