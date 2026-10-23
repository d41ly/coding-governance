---
slug: dFairHearing
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-19 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-24 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40
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
**Build status:** DEFERRED · 38 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14
ids TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-19 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-24 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28
ids TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dFairHearing-13 — the lens catalogue as data, rendered into the harness's five-slot literals, and a slot count in the fan-out leg](spec/2026-10-23-spec-TOOL-dFairHearing-13.md) | 1 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-2 — the design-audit preset of the spec-audit kind, chosen by a preset argument](spec/2026-10-23-spec-TOOL-dFairHearing-2.md) | 2 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-3 — opt-in lenses swapped into a five-slot literal, and review.pin as the stand-in that maps them](spec/2026-10-23-spec-TOOL-dFairHearing-3.md) | 3 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dFairHearing-9 — portability, topology and adopter migration as anchored checklist classes, and lens notes derived per preset after a swap](spec/2026-10-23-spec-TOOL-dFairHearing-9.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-4 — skeptic batches sorted by cited address](spec/2026-10-23-spec-TOOL-dFairHearing-4.md) | 5 | 2 | DEFERRED | rev-4 | 2026-10-23 |
| [TOOL-dFairHearing-5 — duplicates counted as merged confirmations, the orphan check on both kinds](spec/2026-10-23-spec-TOOL-dFairHearing-5.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-6 — items carrying a grade per id, ranked by the highest](spec/2026-10-23-spec-TOOL-dFairHearing-6.md) | 7 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-7 — refuted claims and same-address twins handed to the synthesizer to flag](spec/2026-10-23-spec-TOOL-dFairHearing-7.md) | 8 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dFairHearing-11 — every agent the review harness spawns is typed from a declared stage, and an opted-in review step runs twin finder runs the synthesis merges](spec/2026-10-23-spec-TOOL-dFairHearing-11.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-8 — fix verdicts judged by class behind a switch, and every confirmed finding given one disposition from the report's grammar](spec/2026-10-23-spec-TOOL-dFairHearing-8.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-16 — agent-cap's review rules moved to the review kit, each seen red at its new home before the hook stops carrying it](spec/2026-10-23-spec-TOOL-dFairHearing-16.md) | 11 | 2 | DEFERRED | rev-5 | 2026-10-23 |
| [TOOL-dFairHearing-10 — the review records brought back in line with the code at their sources, each live copy re-rendered](spec/2026-10-23-spec-TOOL-dFairHearing-10.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-22 — agent-cap fails closed on a spec-audit call when the opt-in pack is not beside it](spec/2026-10-23-spec-TOOL-dFairHearing-22.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-12 — the scorer factory: one replay scorer, with aScoutedSeam's grader as its second instance](spec/2026-10-23-spec-TOOL-dFairHearing-12.md) | 13 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-14 — the experiment shape's method, enforced or recorded by the scorer factory](spec/2026-10-23-spec-TOOL-dFairHearing-14.md) | 14 | 2 | DEFERRED | rev-5 | 2026-10-23 |
| [TOOL-dFairHearing-1 — the owed replays: the design-audit preset run blind at blob 767187aa, and the verdicts that flip the dark switches](spec/2026-10-23-spec-TOOL-dFairHearing-1.md) | 15 | 2 | DEFERRED | rev-4 | 2026-10-23 |
| [TOOL-dFairHearing-21 — the held-out freeze check hashes the bytes it scores and refuses a shallow history](spec/2026-10-23-spec-TOOL-dFairHearing-21.md) | 15 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-15 — the review's bug-class checklist, selected by the pinned range and handed by the harness itself](spec/2026-10-23-spec-TOOL-dFairHearing-15.md) | 16 | 2 | DEFERRED | rev-5 | 2026-10-23 |
| [TOOL-dFairHearing-17 — each review round's state, computed by the harness and carried in its record](spec/2026-10-23-spec-TOOL-dFairHearing-17.md) | 17 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dFairHearing-18 — the whole-design walk as a preset of the design audit, and its recall grade](spec/2026-10-23-spec-TOOL-dFairHearing-18.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-20 — a gapped whole-design walk reds the harness's returned counts, not only its prose](spec/2026-10-23-spec-TOOL-dFairHearing-20.md) | 19 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-23 — the round-1 spec audit's 49 minors: one contract per shared name, criteria a correct build can pass, and the fixtures and records the moved code needs](spec/2026-10-23-spec-TOOL-dFairHearing-23.md) | 19 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-25 — the owed replays run after the replay contract is corrected, and their verdicts set the dark switches](spec/2026-10-23-spec-TOOL-dFairHearing-25.md) | 20 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-26 — every rule 0 and rule 5 arm of the hook's suite found at its new home and gone from the old one, counted by label whatever helper writes it](spec/2026-10-23-spec-TOOL-dFairHearing-26.md) | 20 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-27 — the spec audit of units 20 to 23, its 31 minors: criteria a correct build can pass, refusals that name their cause, and the readers a move leaves behind](spec/2026-10-23-spec-TOOL-dFairHearing-27.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-28 — the hook suite's census re-pinned to 59 and 14, measured by a script file whose pattern no shell can fold](spec/2026-10-23-spec-TOOL-dFairHearing-28.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-29 — the five escaped-quote arms of the hook's suite checked by name, at their home and gone from the old one](spec/2026-10-23-spec-TOOL-dFairHearing-29.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-30 — unit 15's with-and-without replay run with one fresh clone per record and arm, so no arm reviews a tree holding the other's report](spec/2026-10-23-spec-TOOL-dFairHearing-30.md) | 21 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dFairHearing-31 — the version-line check resolves the bar's own base first, and refuses by name when it cannot, rather than passing on an empty diff](spec/2026-10-23-spec-TOOL-dFairHearing-31.md) | 22 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-35 — unit 15's replay scored by one attempt rule fixed before the runs, so no figure rests on the attempt a runner prefers](spec/2026-10-23-spec-TOOL-dFairHearing-35.md) | 22 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-32 — the round-3 spec audit's 32 minors: criteria that observe what their specs change, one source per procedure, and refusals that name their cause](spec/2026-10-23-spec-TOOL-dFairHearing-32.md) | 23 | 2 | DEFERRED | rev-3 | 2026-10-23 |
| [TOOL-dFairHearing-33 — the version check reads every declared kit version constant through govkit's own reader, so no carrier's form escapes a typed pattern](spec/2026-10-23-spec-TOOL-dFairHearing-33.md) | 23 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-34 — the version check reads every gov:kit marker in every file the build changed, not four typed directories](spec/2026-10-23-spec-TOOL-dFairHearing-34.md) | 23 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-36 — the round-4 spec audit's 13 minors on units 28, 29 and 31: probes that read every node's bytes alike, misses seen red, and the bar's own base](spec/2026-10-23-spec-TOOL-dFairHearing-36.md) | 24 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-37 — the round-4 spec audit's 19 minors on units 30 and 32: one replay procedure that isolates each arm, criteria over the scored attempt, and checks that can go red](spec/2026-10-23-spec-TOOL-dFairHearing-37.md) | 24 | 2 | DEFERRED | rev-2 | 2026-10-23 |
| [TOOL-dFairHearing-38 — a `selected` verdict observed by the parser `gotchas.py` has, so a correct build passes and a shipped flag reds](spec/2026-10-23-spec-TOOL-dFairHearing-38.md) | 25 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dFairHearing-39 — a criterion quoting an error text its tool never emits, carried into the bug-class catalogue a spec commit selects](spec/2026-10-23-spec-TOOL-dFairHearing-39.md) | 25 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [TOOL-dFairHearing-40 — the round-5 spec audit's 35 minors: one build-wide version reading on one base, an attempt checker that refuses what it cannot place, and criteria a correct build can pass](spec/2026-10-23-spec-TOOL-dFairHearing-40.md) | 26 | 2 | DEFERRED | rev-1 | 2026-10-23 |
<!-- /gen:build-units -->

Records: 93 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40.

Ids whose spec moved past its audited revision: TOOL-dFairHearing-1@rev-2 TOOL-dFairHearing-10@rev-1 TOOL-dFairHearing-11@rev-1 TOOL-dFairHearing-12@rev-1 TOOL-dFairHearing-13@rev-1 TOOL-dFairHearing-14@rev-3 TOOL-dFairHearing-15@rev-1 TOOL-dFairHearing-16@rev-1 TOOL-dFairHearing-17@rev-2
TOOL-dFairHearing-18@rev-1 TOOL-dFairHearing-2@rev-1 TOOL-dFairHearing-20@rev-1 TOOL-dFairHearing-21@rev-1 TOOL-dFairHearing-22@rev-1 TOOL-dFairHearing-23@rev-1 TOOL-dFairHearing-25@rev-1 TOOL-dFairHearing-26@rev-1 TOOL-dFairHearing-27@rev-1 TOOL-dFairHearing-28@rev-1 TOOL-dFairHearing-29@rev-1
TOOL-dFairHearing-3@rev-1 TOOL-dFairHearing-30@rev-1 TOOL-dFairHearing-31@rev-1 TOOL-dFairHearing-32@rev-1 TOOL-dFairHearing-33@rev-1 TOOL-dFairHearing-34@rev-1 TOOL-dFairHearing-35@rev-1 TOOL-dFairHearing-36@rev-1 TOOL-dFairHearing-37@rev-1 TOOL-dFairHearing-4@rev-3 TOOL-dFairHearing-5@rev-1
TOOL-dFairHearing-6@rev-1 TOOL-dFairHearing-8@rev-1 TOOL-dFairHearing-9@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dFairHearing's 18 clause(s) and 10 owned node(s), over 38 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 18
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-23-spec-TOOL-dFairHearing-20.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-21.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-22.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dFairHearing-23.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-25.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-26.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-27.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dFairHearing-28.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-29.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-30.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-31.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dFairHearing-32.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-33.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-34.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-35.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dFairHearing-36.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-37.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-23-spec-TOOL-dFairHearing-39.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-23-spec-TOOL-dFairHearing-40.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0071, cl-dClosedLoop-0072, cl-dClosedLoop-0073, cl-dClosedLoop-0074, cl-dClosedLoop-0076, cl-dClosedLoop-0080, cl-dClosedLoop-0081, cl-dClosedLoop-0082, cl-dClosedLoop-0084
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dFairHearing-13` | no |
| 2 | `TOOL-dFairHearing-2` | no |
| 3 | `TOOL-dFairHearing-3` | no |
| 4 | `TOOL-dFairHearing-9` | no |
| 5 | `TOOL-dFairHearing-4` | no |
| 6 | `TOOL-dFairHearing-5` | no |
| 7 | `TOOL-dFairHearing-6` | no |
| 8 | `TOOL-dFairHearing-7` | no |
| 9 | `TOOL-dFairHearing-11` | no |
| 10 | `TOOL-dFairHearing-8` | no |
| 11 | `TOOL-dFairHearing-16` | no |
| 12 | `TOOL-dFairHearing-10`, `TOOL-dFairHearing-22` | yes |
| 13 | `TOOL-dFairHearing-12` | no |
| 14 | `TOOL-dFairHearing-14` | no |
| 15 | `TOOL-dFairHearing-1`, `TOOL-dFairHearing-21` | yes |
| 16 | `TOOL-dFairHearing-15` | no |
| 17 | `TOOL-dFairHearing-17` | no |
| 18 | `TOOL-dFairHearing-18` | no |
| 19 | `TOOL-dFairHearing-20`, `TOOL-dFairHearing-23` | yes |
| 20 | `TOOL-dFairHearing-25`, `TOOL-dFairHearing-26` | yes |
| 21 | `TOOL-dFairHearing-27`, `TOOL-dFairHearing-28`, `TOOL-dFairHearing-29`, `TOOL-dFairHearing-30` | yes |
| 22 | `TOOL-dFairHearing-31`, `TOOL-dFairHearing-35` | yes |
| 23 | `TOOL-dFairHearing-32`, `TOOL-dFairHearing-33`, `TOOL-dFairHearing-34` | yes |
| 24 | `TOOL-dFairHearing-36`, `TOOL-dFairHearing-37` | yes |
| 25 | `TOOL-dFairHearing-38`, `TOOL-dFairHearing-39` | yes |
| 26 | `TOOL-dFairHearing-40` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dSafePassage](../dSafePassage/README.md)
- **Child builds:** [dCalibratedLens](../dCalibratedLens/README.md), [dDeclaredLoop](../dDeclaredLoop/README.md)
<!-- /gen:build-edges -->
