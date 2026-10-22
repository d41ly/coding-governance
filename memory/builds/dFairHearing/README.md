---
slug: dFairHearing
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-19
status: OPEN
spec-audit: 2026-10-21
parents: dSafePassage
may: PLAY-dClosedLoop-3
---

# dFairHearing — the Review harness build of the dClosedLoop chain

## The problem this build exists to solve

dFairHearing owns 13 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-review-04 to
gap-review-10, gap-review-12, gap-review-13, gap-test-18, gap-review-20, gap-review-21, gap-review-22. Closing every
one is this build's goal bound.

## Expected improvements

- Each of the 18 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 13 owned gaps above close.

## Detriments if this is not built

- Its 13 owned gaps stay open.
- Its 2 child builds wait on it: dDeclaredLoop, dCalibratedLens.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dFairHearing` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dFairHearing`, a record per member "recorded by nobody", the same with `--write` (commit it
  as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dFairHearing-1` | `cl-dClosedLoop-0068@b4e6c04e` | the owed replays first: the design-audit preset run blind at blob 767187aa |
| 2 | `TOOL-dFairHearing-2` | `cl-dClosedLoop-0069@a762d009` | the design-audit preset of the spec-audit kind for design and architecture records |
| 3 | `TOOL-dFairHearing-3` | `cl-dClosedLoop-0070@00ce4e3c` | opt-in lenses (security |
| 4 | `TOOL-dFairHearing-4` | `cl-dClosedLoop-0071@8d3a19dc` | skeptic batches sorted by cited address |
| 5 | `TOOL-dFairHearing-5` | `cl-dClosedLoop-0072@4afd6a04` | duplicates counted as merged confirmations |
| 6 | `TOOL-dFairHearing-6` | `cl-dClosedLoop-0073@242e109b` | items carrying a grade per id |
| 7 | `TOOL-dFairHearing-7` | `cl-dClosedLoop-0074@51869353` | refuted claims and same-address twins handed to the synthesizer to flag |
| 8 | `TOOL-dFairHearing-8` | `cl-dClosedLoop-0075@8c43970c` | fix verdicts judged by class |
| 9 | `TOOL-dFairHearing-9` | `cl-dClosedLoop-0076@8bf57ee9` | portability |
| 10 | `TOOL-dFairHearing-10` | `cl-dClosedLoop-0077@58d0099e` | the review records brought back in line with the code at their sources (`tools/workflows/REVIEW-PROTOCOL.template.md`'s lens list |
| 11 | `TOOL-dFairHearing-11` | `cl-dClosedLoop-0078@ed5e83ae` | the panel's internals |
| 12 | `TOOL-dFairHearing-12` | `cl-dClosedLoop-0079@d8e61ab6` | the scorer factory: one deterministic scorer that re-derives every figure from committed raw outputs |
| 13 | `TOOL-dFairHearing-13` | `cl-dClosedLoop-0080@8c9e5de7` | the lens catalogue as data in the review kit |
| 14 | `TOOL-dFairHearing-14` | `cl-dClosedLoop-0081@3ad56b8f` | the experiment shape's method |
| 15 | `TOOL-dFairHearing-15` | `cl-dClosedLoop-0082@8ac81dad` | the review's bug-class checklist selected by the pinned range and ordered by anchors |
| 16 | `TOOL-dFairHearing-16` | `cl-dClosedLoop-0083@bd47ee4e` | agent-cap's review rules moved to the review kit: the verifier total and the loop markers to the merge bar's harness checks |
| 17 | `TOOL-dFairHearing-17` | `cl-dClosedLoop-0084@5c5896a3` | each round's state in the review report |
| 18 | `TOOL-dFairHearing-18` | `cl-dClosedLoop-0085@796d40aa` | the whole-design walk as a preset of the design audit: walkers sliced by scenario and by step under `review.design-audit.runs` |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14
ids TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-19

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dFairHearing's 18 clause(s) and 10 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 18 (cl-dClosedLoop-0068, cl-dClosedLoop-0069, cl-dClosedLoop-0070, cl-dClosedLoop-0071, cl-dClosedLoop-0072, cl-dClosedLoop-0073, cl-dClosedLoop-0074, cl-dClosedLoop-0075, cl-dClosedLoop-0076, cl-dClosedLoop-0077, cl-dClosedLoop-0078, cl-dClosedLoop-0079, cl-dClosedLoop-0080,
  cl-dClosedLoop-0081, cl-dClosedLoop-0082, cl-dClosedLoop-0083, cl-dClosedLoop-0084, cl-dClosedLoop-0085)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.review.lens, item.review.pin, item.review.refute, item.review.report, policy-key.review.design-audit.runs, policy-key.review.design-audit.seed, policy-key.review.opt-in, policy-key.review.twin, policy-key.review.unclassed, record-kind.review
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0071, cl-dClosedLoop-0072, cl-dClosedLoop-0073, cl-dClosedLoop-0074, cl-dClosedLoop-0076, cl-dClosedLoop-0080, cl-dClosedLoop-0081, cl-dClosedLoop-0082, cl-dClosedLoop-0084
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dSafePassage](../dSafePassage/README.md)
- **Child builds:** [dCalibratedLens](../dCalibratedLens/README.md), [dDeclaredLoop](../dDeclaredLoop/README.md)
<!-- /gen:build-edges -->
