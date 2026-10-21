---
slug: dConvergedCharter
node: d
opened: 2026-10-21
streams: playbook
roster: PLAY
ids: PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-24
status: OPEN
spec-audit: 2026-10-21
parents: dScopedBuild dShippedRelease dCalibratedLens dMindYourWords
may: PLAY-dClosedLoop-3
---

# dConvergedCharter — the Convergence build of the dClosedLoop chain

## The problem this build exists to solve

dConvergedCharter owns 15 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-spine-04,
gap-spine-05, gap-maint-04, gap-found-12, gap-found-13, gap-tool-05, gap-tool-06, gap-tool-08, gap-tool-09,
gap-found-27, gap-orient-21, gap-found-28, gap-roles-26, gap-found-32, gap-found-36. Closing every one is this build's
goal bound.

## Expected improvements

- Each of the 23 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 15 owned gaps above close.

## Detriments if this is not built

- Its 15 owned gaps stay open.
- No chain build names it as a parent, and the chain is done only when it lands.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dConvergedCharter` green before the first pass; a moved instrument
  blob is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dConvergedCharter`, a record per member "recorded by nobody", the same with `--write`
  (commit it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again
  after a re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-17.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `PLAY-dConvergedCharter-1` | `cl-dClosedLoop-0475@2b542935` | protocol text derived to facts only |
| 2 | `PLAY-dConvergedCharter-2` | `cl-dClosedLoop-0476@46c25c62` | every remaining positional reference migrated to tags |
| 3 | `PLAY-dConvergedCharter-3` | `cl-dClosedLoop-0477@47475290` | records merged by evidence |
| 4 | `PLAY-dConvergedCharter-4` | `cl-dClosedLoop-0478@5ccb9b38` | superseded parts retired through ratified proposals |
| 5 | `PLAY-dConvergedCharter-5` | `cl-dClosedLoop-0479@8dc7a199` | adopters migrated onto the ranked charter and the loop |
| 6 | `PLAY-dConvergedCharter-6` | `cl-dClosedLoop-0480@7f73d023` | every record kind on dTotalRecall's registry |
| 7 | `PLAY-dConvergedCharter-7` | `cl-dClosedLoop-0481@a6574329` | protocols and templates rendered as tag-sliced views from the loop's checklists |
| 8 | `PLAY-dConvergedCharter-8` | `cl-dClosedLoop-0482@c8b56d3a` | the remaining renderers absorbed |
| 9 | `PLAY-dConvergedCharter-9` | `cl-dClosedLoop-0483@5b53c82b` | Skills converged to level-4 thin entries |
| 10 | `PLAY-dConvergedCharter-10` | `cl-dClosedLoop-0484@7e1eaeeb` | the protocol slices and Skill entries rendered from units |
| 11 | `PLAY-dConvergedCharter-11` | `cl-dClosedLoop-0485@dde21704` | every kit conf key the retrofit does not convert folded into the policy file |
| 12 | `PLAY-dConvergedCharter-12` | `cl-dClosedLoop-0486@36def3b5` | the unattended kit |
| 13 | `PLAY-dConvergedCharter-13` | `cl-dClosedLoop-0487@ff29708d` | feature-specific guide prose migrated into feature-scoped units (night pass |
| 14 | `PLAY-dConvergedCharter-14` | `cl-dClosedLoop-0488@7cf98c51` | every part in the fates table at its fate |
| 15 | `PLAY-dConvergedCharter-15` | `cl-dClosedLoop-0489@74c9a546` | the hand-written `help/` pages |
| 16 | `PLAY-dConvergedCharter-16` | `cl-dClosedLoop-0490@166e1002` | the `/session-kickoff` Skill retired once the orientation scout and `kickoff.runs` have landed: a `[[retired]]` row with an inventory of its readers by path and by value over the tree |
| 17 | `PLAY-dConvergedCharter-17` | `cl-dClosedLoop-0491@3aafd2a1` | the `/build` Skill retired once dWellOiledMachine's supervisor drives attended builds: a `[[retired]]` row with its readers inventoried by value |
| 18 | `PLAY-dConvergedCharter-18` | `cl-dClosedLoop-0492@a532274c` | the owner's cycle walked by key: from a planted build's intake |
| 19 | `PLAY-dConvergedCharter-19` | `cl-dClosedLoop-0493@0d92d2e3` | the guides' positional citations migrated to tags |
| 20 | `PLAY-dConvergedCharter-20` | `cl-dClosedLoop-0494@eb095d63` | the conf fold and the unattended kit's retirement shipped as upgrade steps |
| 21 | `PLAY-dConvergedCharter-21` | `cl-dClosedLoop-0495@53f4c9b2` | `tools/roles/house/policy.toml` retired as a seed: a repository's efforts folded into the `roles.effort.*` policy keys |
| 22 | `PLAY-dConvergedCharter-22` | `cl-dClosedLoop-0496@a94b54b6` | the census of gov's own flow and role settings: the legs no descriptor declares |
| 23 | `PLAY-dConvergedCharter-23` | `cl-dClosedLoop-0502@fbfa8f4f` | the release asks' join: Maintain's `release-verify-failed` ask and `release.route`'s keyed alike by (reading |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams playbook
ids PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11
ids PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22
ids PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-24

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dCalibratedLens](../dCalibratedLens/README.md), [dMindYourWords](../dMindYourWords/README.md), [dScopedBuild](../dScopedBuild/README.md), [dShippedRelease](../dShippedRelease/README.md)
<!-- /gen:build-edges -->
