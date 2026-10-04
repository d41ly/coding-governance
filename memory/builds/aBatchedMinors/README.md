---
slug: aBatchedMinors
node: a
opened: 2026-10-04
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aBatchedMinors-1 TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4 TOOL-aBatchedMinors-5 TOOL-aBatchedMinors-6
---

# aBatchedMinors — every closing-review finding becomes a unit, minors batched

## The problem this build exists to solve

At the closing diff review's exit, BLOCKER and HIGH findings are promoted to units, while MEDIUM and
LOW are "folded into their spec" with nothing that checks they were. One build's round-3 mediums and
lows stood unfolded for weeks. The owner rules that every closing-review finding is promoted, with
mediums and lows grouped into one or two units. The prompt is in `prompts/`.

## Expected improvements

- A closing review's MEDIUM and LOW findings are built as units, not left as spec prose.
- The driver refuses a closing-review exit that records standing findings with no promotion.
- The merge bar demands one unit per blocker and high, plus one for the minors batch.
- The exit's counts derive from the review harness's own tally, so nobody parses a report.

## Detriments if this is not built

- Mediums and lows keep landing as spec edits that no gate reads, and some are never fixed.
- The owner's ruling lives in a transcript, and the method keeps teaching the fold.

## Build-level rules

- Closing diff review only; spec-audit disposition is unchanged and stated as a non-goal.
- Counts come from `tier2-review.js`'s own tally; no parser over review prose.
- Reuse first: `verb_review`'s state gate, check 2's needs clause, the harness's per-raw tally.
- Every new refusal or gate clause is observed RED on a staged break before it lands.
- No spec audit: none is owed, and the closing diff review is the specs' first review.
- Classified at kickoff (M2): all four MISSING; unit 1 retired at speccing (WONTDO, the harness already
  returns its count). Units 2 to 4 authored and built inline, in order: units 2
  and 3 share a row grammar, and unit 4 documents what 2 and 3 built.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBatchedMinors-1` | 1 | `tier2-review.js` returns `minors`, the confirmed MEDIUM and LOW count, beside `blockers` and `highs` |
| 2 | `TOOL-aBatchedMinors-2` | 2 | `--review` takes `--highs` and `--minors` on the closing review's exit and requires `promote` when any stood |
| 3 | `TOOL-aBatchedMinors-3` | 2 | check 2 demands blockers + highs + one unit for the minors from a closing-review exit row |
| 4 | `TOOL-aBatchedMinors-4` | 1 | the method, the Skill, the verbs entry and a decision record state the batched-promotion rule |
| 6 | `TOOL-aBatchedMinors-6` | 2 | promoted from the closing review: round 1's three mediums and eleven lows, batched |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 5 unit(s) · node a · opened 2026-10-04 · streams tooling
ids TOOL-aBatchedMinors-1 TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4 TOOL-aBatchedMinors-5 TOOL-aBatchedMinors-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aBatchedMinors-1 — RETIRED: a `minors` count the review harness already returns](spec/2026-10-04-spec-TOOL-aBatchedMinors-1.md) | 1 | 1 | WONTDO | rev-1 | 2026-10-04 |
| [TOOL-aBatchedMinors-2 — the closing review's exit records its standing findings and promotes them all](spec/2026-10-04-spec-TOOL-aBatchedMinors-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-10-04 |
| [TOOL-aBatchedMinors-3 — check 2 demands one unit per blocker and high, plus one for the minors](spec/2026-10-04-spec-TOOL-aBatchedMinors-3.md) | 3 | 2 | CLOSED | rev-1 | 2026-10-04 |
| [TOOL-aBatchedMinors-4 — the method, the Skill and the verbs entry state the batched-promotion rule](spec/2026-10-04-spec-TOOL-aBatchedMinors-4.md) | 4 | 1 | CLOSED | rev-2 | 2026-10-04 |
| [TOOL-aBatchedMinors-6 — the closing review's batched minors, round 1](spec/2026-10-04-spec-TOOL-aBatchedMinors-6.md) | 6 | 2 | CLOSED | rev-1 | 2026-10-04 |
<!-- /gen:build-units -->

Records: 6 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aBatchedMinors-1 TOOL-aBatchedMinors-2 TOOL-aBatchedMinors-3 TOOL-aBatchedMinors-4 TOOL-aBatchedMinors-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aBatchedMinors-1` | no |
| 2 | `TOOL-aBatchedMinors-2` | no |
| 3 | `TOOL-aBatchedMinors-3` | no |
| 4 | `TOOL-aBatchedMinors-4` | no |
| 6 | `TOOL-aBatchedMinors-6` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
