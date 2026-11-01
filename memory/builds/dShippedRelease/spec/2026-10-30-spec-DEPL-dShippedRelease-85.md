# DEPL-dShippedRelease-85 — `disposed` re-derives its finding count from the report it names

**Status:** DEFERRED · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 13 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 88 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, BLOCKER, which shares item B3 with ids 29 and 47
(DEPL-dShippedRelease-83, -84). `disposed · 0 finding(s) · <old report>` closes under `owed` because
nothing compares `<n>` with the report, so a session can state that nothing was found and no finding
is filed. This unit derives the count once, for both the writer and the term.

## 2. Scope (IN)

- **S1** — The count. `derive_report_count(text)` in `tools/loop/deploy_items.py` counts the rows of
  the report's `## Appendix — every finding` table whose verdict cell reads `confirmed`; a report with
  no such table counts 0. `dispose-landing` takes `<n>` from it, so the writer and the term read one
  rule. Observed by AC2.
- **S2** — The term. `check_review_field` fails a `<n>` differing from S1 over the blob, printing
  `forged · count`. Observed by AC1.

## 3. Non-goals (OUT)

- What each finding files: unit 14 S4 and `write_review_patches` stand.
- Reading the `review-shape` line's `confirmed=`: §4's alternative.

### Edges

- **consumes-from** `DEPL-dShippedRelease-83` — `read_landing_report`, whose `n` and blob this unit's term reads
- **consumes-from** `DEPL-dShippedRelease-73` — `check_review_field`, which gains this term
- **consumes-from** `DEPL-dShippedRelease-14` — `dispose-landing`, which takes `<n>` from this unit's function
- **hands-off** `DEPL-dShippedRelease-106` — `derive_report_count`, which the minors batch's report satisfies (review id 97)
- **hands-off** `DEPL-dShippedRelease-113` — S1's reader, whose unstated clean path this unit states (round-3 id 3)
- **hands-off** `DEPL-dShippedRelease-114` — the clean path this unit's walk reaches (round-3 id 22)
- **hands-off** `DEPL-dShippedRelease-115` — S1's empty case and §5's risk line, which this unit supersedes (round-3 id 4)
- **hands-off** `DEPL-dShippedRelease-116` — S1, whose body this unit replaces, and §10's claim (round-3 id 30)
- **hands-off** `DEPL-dShippedRelease-117` — §3's non-goal and §4's alternative, which this unit amends (round-3 id 49)
- **hands-off** `DEPL-dShippedRelease-118` — S1's `confirmed`-only count (round-3 id 50)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 51)

## 4. Design

### Evidence

- `tools/workflows/tier2-review.js:1634` writes `## Appendix — every finding`, and the report this unit answers holds one row per finding with a `verdict` cell.
- Unit 14 S4 reads "the review record's confirmed findings" and names no reader of them.
- Unit 14 AC6 plants a report reading `## Verdict: CLEAN` with `disposed · 0 finding(s)`, which S1's empty case keeps.

### The read, as units 83, 84, 85 and 90 leave it

`check_review_field` on a `disposed · <n> finding(s) · <report path>` value, in order, each failure
printing `held · check_landing_review · forged · <term>`:

| Term | Test | Unit |
|---|---|---|
| `path` | the path sits directly under `memory/builds/<slug>/reviews/` and its blob is on the advertised tip | 83 |
| `verdict` | the blob holds exactly one `## Verdict:` line, a member of the closed set | 84 |
| `count` | `<n>` equals `derive_report_count` over the blob | 85 |
| `landing` | the blob's `**Reviewed range:**` line equals this landing's pin | 90 |

### Supersedes

- Unit 14 S4's unspecified reader of the confirmed findings: S1 names it.
- Unit 73 S2's silence on `<n>`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_report_count` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2
- `tools/loop/deploy_fixture.py`: the cases of §6

### Alternatives rejected

- **The `review-shape` line's `confirmed=`** (`tools/workflows/tier2-review.js:79`). It is a tally beside the rows `dispose-landing` files, so the count and the filing could disagree; counting the rows reads what gets filed.

## 5. Production-readiness checklist

- security — the term reads the tip's tree and the landing's own pin, and a session still writes the field. Unit 73 §5's "outside the reviewed session's reach" is corrected to that: a session able to land a new report naming this landing passes, in the open on the default branch, and unit 73 §8 F1 keeps a signature out.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a harness that renames the appendix makes every report count 0, and a report with findings then reads `forged · count` at the close, the loud direction.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-forged-count` plants a report with two
  `confirmed` rows beside `disposed · 0 finding(s) · <that report>`, `--deploy close` exits 3 printing
  `forged · count`.
  Red when: a session states no finding over a report that holds two.
- **AC2** — When `python deploy_items.py dispose-landing <sha> <that report>` runs in the same case,
  the field reads `disposed · 2 finding(s)` and two intakes are filed, the writer and the term
  agreeing.
  Red when: the writer's count and the term's differ on one report.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · `review-forged-count`, its failing case the compare cut out · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 88 (BLOCKER, item B3) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 113, 114, 115, 116, 117, 118, 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `dispose-landing` (unit 14 S4) and `check_review_field` (unit 73).
`python tools/codebase-map/reuse_lookup.py "bind a review report to the landing commit it reviewed"`
ranked name-stem helpers (`report`, `build_commit`, `Report`, `render_report`) and no reader of a
report's appendix, so this unit reads the table `tools/workflows/tier2-review.js:1634` writes. The
recall probe surfaced TOOL-aBlindedTrial-6 and report item B3, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how is a review report tied to the landing it reviewed" --terms "review report appendix confirmed count disposed forged dispose-landing write_review_patches findings intake"`
