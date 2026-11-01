# DEPL-dShippedRelease-83 — `disposed` reads its report from this build's reviews folder alone

**Status:** OPEN · rev-4 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 13 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 29 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, BLOCKER, which shares item B3 with ids 47 and 88
(DEPL-dShippedRelease-84, -85) and stands beside id 4 (DEPL-dShippedRelease-90). Unit 73 S2 tests only
`git cat-file -e <advertised tip>:<report path>` and a `## Verdict` line, and the path comes from a
field any session can write. 676 of 714 tracked review records pass, so a session writes
`disposed · 0 finding(s) · <any existing report>` and closes with no review. This unit confines the
path and owns the one read the other three terms join.

## 2. Scope (IN)

- **S1** — The reader. `read_landing_report(slug, value, root)` in `tools/loop/deploy_items.py` parses
  `disposed · <n> finding(s) · <report path>`, requires the path to sit directly under
  `memory/builds/<slug>/reviews/`, with no `..` segment, and returns `n`, the path and the blob at the
  advertised tip. Any failure is `forged · path`. Observed by AC1, AC2.
- **S2** — The term. `check_review_field` calls S1 in place of unit 73 S2's `git cat-file -e`, then
  the terms of units 84, 85 and 90, in the order of §4. Observed by AC1.
- **S3** — The plants. `review-forged-other-build` names a real report of another build, and
  `review-forged-traversal` a path climbing out of the folder. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- The verdict, the count and the landing binding: DEPL-dShippedRelease-84, -85 and -90.
- A signature: unit 73 §8 F1 stands.
- A close-term checklist item: the audit's left-shift item, which no clause of this build names.

### Edges

- **consumes-from** `DEPL-dShippedRelease-73` — `check_review_field` and its S2, which this unit supersedes
- **consumes-from** `DEPL-dShippedRelease-14` — `dispose-landing`'s value and S5's records landing
- **hands-off** `DEPL-dShippedRelease-84` — `read_landing_report`, whose blob that unit's verdict term reads
- **hands-off** `DEPL-dShippedRelease-85` — `read_landing_report`, whose `n` and blob that unit's count term reads
- **hands-off** `DEPL-dShippedRelease-90` — `read_landing_report`, whose blob that unit's landing term reads
- **hands-off** `DEPL-dShippedRelease-109` — `read_landing_report`, whose blob the facts are read from (round-3 id 2)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 52)
- **hands-off** `DEPL-dShippedRelease-133` — S1's path rule, which the written value must pass (round-4 id 23)
- **hands-off** `DEPL-dShippedRelease-144` — S1's shape test, which the batch runs ahead of the read (round-5 id 44)

## 4. Design

### Evidence

- Unit 73 S2 reads the path from the field, and unit 1 S6 lets any session set `review`.
- `git grep -l '^## Verdict' -- 'memory/builds/*/reviews/*.md'` printed 676 at the audit (report id 29), of 714 tracked records.
- Unit 14 S4 writes the value and S5 puts the report under `memory/builds/<slug>/reviews/`, so an honest value always passes the path test.

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

- Unit 73 S2 whole, and its AC2's "with the report on the tip and a `## Verdict` line it passes": DEPL-dShippedRelease-90's AC3 observes the honest pass over all four terms.
- Unit 73 §5's security and risks lines: §5 here.
- Unit 73 S3's line gains its term, so `forged` stays the word unit 73's AC1 and AC2 read.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_landing_report` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2
- `tools/loop/deploy_fixture.py`: S3's cases

## 5. Production-readiness checklist

- security — the term reads the tip's tree and the landing's own pin, and a session still writes the field. Unit 73 §5's "outside the reviewed session's reach" is corrected to that: a session able to land a new report naming this landing passes, in the open on the default branch, and unit 73 §8 F1 keeps a signature out.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a report moved out of its build's folder reads `forged`; moving one is no operation of this kit.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python deploy_fixture.py --case review-forged-other-build` sets
  `disposed · 0 finding(s) · memory/builds/other/reviews/<a real report>.md`, `--deploy close` exits 3
  printing `forged · path`.
  Red when: any report on the default branch passes, the forgery unit 73 exists to stop.
- **AC2** — When `--case review-forged-traversal` sets a path under this build's folder holding a
  `..` segment, `--deploy close` exits 3 printing `forged · path`.
  Red when: the prefix test reads the spelling and not the path.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 · the two plants, their failing case the prefix test cut out · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 29 (BLOCKER, item B3) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 109, 125); no scope, design or criterion moved.
- rev-3 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-4 spec audit's promoted units declare toward this unit (units 133); no scope, design or criterion moved.
- rev-4 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-5 spec audit's promoted units declare toward this unit (units 144); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `check_review_field` (unit 73 S1, S2), the one term a close reads.
`python tools/codebase-map/reuse_lookup.py "bind a review report to the landing commit it reviewed"`
ranked name-stem helpers (`report`, `build_commit`, `Report`, `render_report`) and no report-to-landing
reader; `VERDICT_RE` at `tools/runlog/model.py:167` is the nearest reader and sits in another kit, so
this unit reads the blob itself. The recall probe surfaced TOOL-aBlindedTrial-6 and report item B3,
which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how is a review report tied to the landing it reviewed" --terms "review report Verdict Reviewed range disposed forged landing subject dispose-landing binding closed set"`
