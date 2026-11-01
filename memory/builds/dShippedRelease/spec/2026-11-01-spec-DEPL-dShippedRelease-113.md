# DEPL-dShippedRelease-113 — `record-clean` writes the landing review's record when the harness returned none

**Status:** OPEN · rev-3 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 14 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-123 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-124 DEPL-dShippedRelease-119 DEPL-dShippedRelease-121 DEPL-dShippedRelease-120 DEPL-dShippedRelease-122 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 3 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, which shares item H2 with
id 22 (DEPL-dShippedRelease-114). `tools/workflows/tier2-review.js` returns `report: null` on both clean
paths, a run with no finding and a run with every finding refuted, while unit 14 S4 needs a `<report>`.
Under `review.deploy = owed` the cleanest review leaves `pending` with nothing to dispose. This unit names
the one writer of that record, so all four terms still read a landed blob.

## 2. Scope (IN)

- **S1** — The writer. `write_clean_record(sha, harness_return, root)` in `tools/loop/deploy_items.py`,
  reached as `python deploy_items.py record-clean <sha> <return.json>`, takes a return reading `report`
  null, `exit` `complete` and `pending` empty. It writes
  `memory/builds/<slug>/reviews/<date>-review-<first id of units>-landing-<sha8>.md`. Observed by AC1.
- **S2** — The bytes, in the order `tools/workflows/tier2-review.js:1853` states: line 1
  `**Serves:** diff-review <the record's units>`, a title, the range line stating `read_pin_range`'s base
  and `<sha>` and the return's `round`, then `## Verdict: CLEAN`, a paragraph quoting the return's `note`,
  and the return's `appendix` when it is non-empty. Observed by AC1, AC2.
- **S3** — One route. The verb then runs `dispose-landing <sha> <that path>`, so the value is written by
  one writer and S5 of unit 14 lands the record. Observed by AC1.
- **S4** — Everything else refuses, exit 2, writing nothing: a return with a `report`, one with `pending`
  non-empty, a `<return.json>` that does not parse, and a record whose `units` holds no id. A return
  with `exit` `deferred-platform` is DEPL-dShippedRelease-114's. Observed by AC3.

## 3. Non-goals (OUT)

- `deferred-platform` and the end-to-end case: DEPL-dShippedRelease-114, the other half of item H2.
- A change to `tools/workflows/tier2-review.js`: §8 F1.

### Edges

- **consumes-from** `DEPL-dShippedRelease-85` — S1's reader, whose unstated clean path this unit states
- **consumes-from** `DEPL-dShippedRelease-14` — `dispose-landing` and S5's records landing
- **consumes-from** `DEPL-dShippedRelease-110` — S2's refusal, which the range line must pass
- **hands-off** `DEPL-dShippedRelease-114` — `record-clean`, which that unit drives from a harness return
- **hands-off** `DEPL-dShippedRelease-130` — S1's record path (round-4 id 4)
- **hands-off** `DEPL-dShippedRelease-135` — S1 and S4, whose admission that unit restates (round-4 id 56)
- **hands-off** `DEPL-dShippedRelease-138` — the text and code the batch repairs (round-4 ids 3, 13, 16, 17, 25, 33, 34, 70)
- **hands-off** `DEPL-dShippedRelease-142` — S1's verb and S4's refusals, which that unit's key row joins (round-5 id 40)
- **hands-off** `DEPL-dShippedRelease-144` — the record's path and `write_clean_record`, which the batch reads (round-5 ids 7, 9, 12, 28, 42, 43)

## 4. Design

### Evidence

- `tools/workflows/tier2-review.js:1337` and `:1667` return `report: null` on the two paths, and `:1677` says no report is written on that path, so "a caller may write them".
- `tools/workflows/README.md:334-335` says a run whose every finding is refuted writes no report and the caller writes it down if it wants one.
- `tools/workflows/unattended-build.js:2566-2578` is the same gap for a spec audit: it names the owed record, line by line, for its caller.
- Unit 106 S49's `dispose-with-reason` writes `## Verdict: BLOCKED`, so with no writer here a clean review is recorded as a blocked one (report id 22).

### The record

```
**Serves:** diff-review DEPL-dExample-1 DEPL-dExample-2
# Landing review of 1a2b3c4d — no report returned
**Reviewed range:** `0f0f0f0f...1a2b3c4d`. **ROUND 1.**
## Verdict: CLEAN
The harness returned no report: <note>.
```

### Supersedes

- Unit 14 S4's `<report>` argument gains this one producer.
- Unit 85 §4's third Evidence bullet: unit 14 AC6's `## Verdict: CLEAN` report exists only by this writer.
- Unit 90 AC3's `review-clean` plant, on this path: DEPL-dShippedRelease-114 drives it from a return.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `write_clean_record` | function, `tools/loop/deploy_items.py` | `py.function`, OK by `--suggest` at writing |
| `record-clean` | verb of `deploy_items.py` | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`: S1, S2, S3, S4
- `tools/loop/deploy_fixture.py`: the cases of §6
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`: `record-clean`
- `help/deploy.md`: what a clean landing review writes

### Alternatives rejected

- **`dispose-landing --clean`, with no record.** The field would name no report, so `path`, `verdict` and `landing` would have no blob to read.
- **The harness writing the record on its clean paths.** It has no filesystem, as `tools/workflows/unattended-build.js:2524` records.

## 5. Production-readiness checklist

- security — the verb reads a local JSON file a session supplies, and writes one record under the build's own folder. It is self-asserted, as units 85 and 90 §5 concede of any report a session can land, and it opens no new hole.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — S4 names each refused state, and AC3 plants them.
- observability — the verb prints the record's path, and `dispose-landing` its own line.
- risks — a `note` holding a `## Verdict:` line would forge a second verdict; S2 writes the `note` on one line, prefixed, so unit 84's one-line test reads only the heading.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — `help/deploy.md` states the verb, and `tools/unattended/VERBS.template.md` its line.

## 6. Acceptance criteria

- **AC1** — When `python deploy_items.py record-clean <sha> <return.json>` runs on a return reading
  `report` null, `exit` `complete`, `pending` `[]` and `appendix` empty, the record exists with
  `## Verdict: CLEAN`, `read-landing` prints `review<TAB>disposed · 0 finding(s)`, and the value's path is
  that record.
  Red when: a clean review has no record to dispose, so `pending` holds the close.
- **AC2** — When the return carries an appendix of one refuted row, the record holds that table, and the
  field still reads `disposed · 0 finding(s)`.
  Red when: a review whose every finding was refuted loses its appendix, or counts a refuted row.
- **AC3** — When it runs on a return with a `report`, with `pending` `["lens-a"]`, and on a file that does
  not parse, each exits 2 and `git status --porcelain` lists no new record.
  Red when: a report or a dead lens reads as clean.

## 7. Gates

`recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC1 AC2 AC3 · a `report` null return, its failing case the record written with no `dispose-landing` · none

## 8. Open questions

- **F1 — Who writes the record?** Options: (a) a named verb of `deploy_items.py`, from the return; (b) the
  session, by hand, from a recipe, as `tools/workflows/unattended-build.js` hands a spec audit's caller;
  (c) the harness. (c) has no filesystem, and (b) leaves the bytes unwitnessed where a fixture can run
  (a). RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, one named writer, the report's corrected
  fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 3 (HIGH, item H2) of the round-3 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-4 spec audit's promoted units declare toward this unit (units 130, 135, 138); no scope, design or criterion moved.
- rev-3 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-5 spec audit's promoted units declare toward this unit (units 142, 144); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `dispose-landing` (unit 14 S4), and the record's shape is the recipe at `tools/workflows/unattended-build.js:2566-2578`.
`python tools/codebase-map/reuse_lookup.py "write a minimal review record when the harness returned no report"`
ranked the name-stem helper `write` and missed that recipe, which a read of the cited lines found, so the
probe and the source disagree and the source stands. The recall probe surfaced TOOL-aProbedUnit-12, the
same gap on a spec audit, and TOOL-dTieredTribunal-16, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "who writes the record when a clean review returns no report" --terms "report null clean path synthesis skipped appendix caller writes record spec audit binding"`
