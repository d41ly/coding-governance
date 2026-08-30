# TOOL-aGatheredDeclaration-8 — lanes, the tool probe, and the dispatcher they need

**Status:** OPEN · rev-2 · 2026-08-31 · node a · Tier-2 · base 44734f15 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round2.md) | spec-audit | TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7 |

<!-- /gen:spec-records -->

## 1. Goal

Implement the `[[lane]]` rows `TOOL-aGatheredDeclaration-2` declares: ordered lanes, a per-lane
concurrency, a short-circuit that skips later lanes without launching them, and the per-leg `tool`
probe that turns a missing binary into a named FAIL rather than a silent pass. This is the
dispatcher change unit 2 was carrying unpriced.

## 2. Scope (IN)

- **S1** — LANE ORDER: lanes run in declaration order. Every leg of lane N completes before any leg
  of lane N+1 dispatches.
- **S2** — PER-LANE CONCURRENCY: `concurrency = <n>` is a literal width and `concurrency = "profile"`
  takes the selected profile's. `GATE_JOBS` continues to override the width alone, per lane.
- **S3** — SHORT CIRCUIT. The key is DECLARED by `TOOL-aGatheredDeclaration-2` S11 and READ here;
  at rev-1 it was declared by neither, because unit 2's example lane set shrank to one row in the
  same fold that created this unit. A lane declaring `short_circuit = true` whose legs did not all pass causes
  every leg in every later lane to be SKIP-marked without launching, each reported with a verb and a
  reason DISTINCT from the guard skip's.
- **S4** — the DISPATCH HINT is partitioned per lane. Today one global longest-first order is built
  over every leg at `run-gates.sh:846-870`; unpartitioned it would interleave lanes and defeat S1
  outright.
- **S5** — the `tool` PROBE: a leg declaring `tool` has that binary checked for usability before the
  run, and an unusable one produces `GATE FAIL <leg>` naming the missing tool. Never a skip.
- **S6** — gov's own leg assignment stays exactly as `TOOL-aGatheredDeclaration-2` left it — one lane
  — so this unit's landing is a MECHANISM landing and lane assignment is measured separately.

## 3. Non-goals (OUT)

- Assigning gov's 86 legs to lanes. That is a behaviour change and it needs
  `<git-dir>/gate-ledger.tsv` read as a measurement, which is its own unit. Shipping the mechanism
  and the assignment together would leave no control, exactly as `gate-profiles.txt`'s `modest` row
  records for the profile table.
- The declaration format. `TOOL-aGatheredDeclaration-2` owns the schema and ships the `[[lane]]`
  rows; this unit reads them.
- Porting inCMS's runner. Its lane model is the prior art and its `fast`/`heavy`/`serial` names are
  the vocabulary; its 863 lines are not.

## 4. Design

### Data model

```toml
[[lane]]
name = "fast"                # sequential and streamed; a failure here stops the rest
concurrency = 1
short_circuit = true

[[lane]]
name = "heavy"
concurrency = "profile"      # the selected profile row's width
```

Ordering is DECLARATION order, not a `priority` key: two ways to say the same thing is the class this
whole build exists to remove.

### The dispatcher

Today: one pool at `JOBS=${GATE_JOBS:-$PROF_WIDTH}` (`run-gates.sh:372`), one admission test
(`:1272`), one global longest-first hint (`:846-870`). After this unit the loop runs once per lane,
taking that lane's width and that lane's slice of the hint. A lane whose predecessor short-circuited
does not enter the loop at all; its legs are marked before the pool is touched.

### The skip verb must be distinguishable

The existing skip tail reads `unchanged vs <branch>`, which is false for a short-circuit skip and
would misreport it as a guard skip. A skip that looks like another kind of skip is the
green-by-absence class one level down, so the short-circuit skip carries its own reason naming the
lane that failed.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` (the dispatch loop, the hint partition, the probe) ·
`tools/run-gates/run-gates.test.sh` · `tools/run-gates/README.md`.

### Alternatives rejected

**Keep one pool and sort legs by lane.** It gets lane ORDER without lane CONCURRENCY, and it cannot
express short-circuit at all, because a sorted single pool has already launched the later legs.

## 5. Production-readiness checklist

- security — N/A. The `tool` probe checks executability; it does not run the binary.
- perf / scale — a `fast` lane that short-circuits is a strict reduction. A poorly declared lane set
  is a regression, which is why S6 keeps gov on one lane until a measurement says otherwise.
- a11y, i18n — N/A.
- error / empty / loading states — a lane declaring neither a literal width nor `"profile"`, and a
  lane list that is empty while legs name lanes, each refuse with exit 2 naming the row.
- observability — the profile line names the lane set and each lane's resolved width. A
  short-circuited run says which lane stopped it.
- risks — the hint partition is the subtle one: a global hint silently defeats S1 while every leg
  still runs, so the run looks correct and the lanes do nothing.
- testing + left-shift gates — the arms below, each observed RED first.
- migration / rollback — a single-lane declaration reproduces today's behaviour exactly, which is
  both the rollback and gov's shipped state.
- user docs — `tools/run-gates/README.md`.

## 6. Acceptance criteria

- **AC1** — When two lanes are declared and both hold legs, no leg of the second lane starts before
  every leg of the first has finished, asserted in `tools/run-gates/run-gates.test.sh` by each leg
  writing a start and end marker and comparing the extremes, not by mtime ordering within a lane.
- **AC2** — When a lane declares `concurrency = 1`, its legs do not overlap; when it declares
  `concurrency = "profile"`, its observed peak occupancy reaches the profile width, asserted with the
  same occupancy technique `tools/run-gates/run-gates.turnstile.test.sh` already uses.
- **AC3** — When a `short_circuit = true` lane has a failing leg, no later-lane leg's argv ever runs,
  asserted by the ABSENCE of files those legs would write. Timing-independent by construction.
- **AC4** — When a leg is skipped by a short circuit, its reported verb and reason are distinct from
  a guard skip's and name the lane that failed, asserted by comparing the two rendered strings in
  `tools/run-gates/run-gates.test.sh`. Observed RED first.
- **AC5** — When a leg declares a `tool` that is not executable, its row is `GATE FAIL <leg>` naming
  the tool, never `GATE skip` and never a pass, asserted in `tools/run-gates/run-gates.test.sh`.
- **AC6** — When two lanes are declared, the dispatch hint each lane consumes contains only that
  lane's legs, asserted in `tools/run-gates/run-gates.test.sh` by planting a `gate-ledger.tsv` that
  would interleave the lanes under a global hint and observing that it does not. Observed RED first
  against the unpartitioned hint.
- **AC7** — When a lane declares a concurrency that is neither a positive integer nor `"profile"`,
  `bash tools/run-gates/run-gates.sh` exits 2 naming the lane. Observed RED first.
- **AC8** — When `tools/gate-legs.toml` declares gov's shipped single lane, the bar's leg set, order
  and verdict are unchanged from before this unit, asserted by comparing full report output at the
  two commits.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `run-gates evidence` · `run-gates turnstile` ·
`profile-bar selftest`. No new leg.

## 8. Open questions

- **F1 — does a short-circuited leg count toward the run's verdict?** It did not run, so calling it
  a pass is the green-by-absence class and calling it a failure attributes another lane's failure to
  it. Recommendation: neither — it is a SKIP with its own reason, the run is already RED from the
  lane that failed, and the summary states how many legs never ran because of it.
  RESOLVED (agent, 2026-08-31, delegated): its own skip verb, counted and named in the summary. It
  reuses the verb vocabulary the runner already has and adds no state to the verdict.

## 9. Revision log

- rev-2 · 2026-08-31 · folded round-2 spec audit finding R16: `short_circuit` was read here and
  declared nowhere. The schema half now sits in `TOOL-aGatheredDeclaration-2` S11, which is where
  the rest of the `[[lane]]` shape lives.
- rev-1 · 2026-08-31 · authored as an amendment during the round-1 spec-audit fold. Split out of
  `TOOL-aGatheredDeclaration-2`, whose S2 asserted "the dispatch loop below it does not change" while
  S6 and S7 required rewriting it — finding F9 of
  `reviews/2026-08-31-review-TOOL-aGatheredDeclaration-1-spec-audit-round1.md`, reached independently
  by R3 of `build/2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md`.

## 10. Reuse audit

The seam is `tools/run-gates/run-gates.sh`'s existing pool — the admission test at `:1272`, the width
resolution at `:372` and the hint build at `:846-870` — verified against source at this revision.
This unit parameterises all three by lane rather than adding a second dispatcher; a second dispatcher
is what `TOOL-aGatheredDeclaration-6` S5 is busy removing one file over.

The design prior art is an adopter's and is not gov's: `C:/projects/incms/main/scripts/gate.sh:566-679`
runs `fast` sequentially with a short circuit into `heavy`, which is a bounded slot pool at
`INCMS_GATE_HEAVY_JOBS`, then `serial`. Its knob is glob-validated as a STRING before reaching any
arithmetic context (`:45-52`) because that variable would otherwise be a command-execution sink
inside the script producing the merge verdict — a hardening this unit takes with the mechanism.
Measurements and the harvest mapping are in
`build/2026-08-31-build-TOOL-aGatheredDeclaration-1-adopter-review.md`.

No `reuse_lookup.py` pass was run for this unit specifically. Its seam was identified by reading the
dispatcher during the audit fold, and the three line references above are the evidence. **That is a
weaker Section 10 than its siblings carry and is stated rather than dressed up.**
