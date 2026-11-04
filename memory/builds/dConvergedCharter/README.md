---
slug: dConvergedCharter
node: d
opened: 2026-10-21
streams: playbook
roster: PLAY
ids: PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-24 PLAY-dConvergedCharter-25 PLAY-dConvergedCharter-26 PLAY-dConvergedCharter-27 PLAY-dConvergedCharter-28 PLAY-dConvergedCharter-29 PLAY-dConvergedCharter-30 PLAY-dConvergedCharter-31 PLAY-dConvergedCharter-32 PLAY-dConvergedCharter-33 PLAY-dConvergedCharter-34 PLAY-dConvergedCharter-35 PLAY-dConvergedCharter-36 PLAY-dConvergedCharter-37
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
**Build status:** OPEN · 23 unit(s) · node d · opened 2026-10-21 · streams playbook
ids PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11
ids PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22
ids PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-24 PLAY-dConvergedCharter-25 PLAY-dConvergedCharter-26 PLAY-dConvergedCharter-27 PLAY-dConvergedCharter-28 PLAY-dConvergedCharter-29 PLAY-dConvergedCharter-30 PLAY-dConvergedCharter-31 PLAY-dConvergedCharter-32 PLAY-dConvergedCharter-33
ids PLAY-dConvergedCharter-34 PLAY-dConvergedCharter-35 PLAY-dConvergedCharter-36 PLAY-dConvergedCharter-37

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [PLAY-dConvergedCharter-22 — the census of gov's own flow and role settings, each row ruled by the owner and the gov-only ones moved](spec/2026-11-03-spec-PLAY-dConvergedCharter-22.md) | 1 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-11 — every kit conf key the retrofit does not convert folded into the policy file, its readers inventoried by value and re-pointed](spec/2026-11-03-spec-PLAY-dConvergedCharter-11.md) | 2 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-17 — the `/build` Skill retired once the supervisor drives attended builds, its client held by a `skill` shim for the deprecation window](spec/2026-11-03-spec-PLAY-dConvergedCharter-17.md) | 3 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-12 — the unattended kit, its four guides and `/unattended` retired once the driver carries every run, every reader by path and by value re-pointed or retired with it](spec/2026-11-03-spec-PLAY-dConvergedCharter-12.md) | 4 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-16 — the `/session-kickoff` Skill retired: its kit homed under the tool root, a `[[retired]]` row, a forwarding stub and the dangling-link report](spec/2026-11-03-spec-PLAY-dConvergedCharter-16.md) | 5 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-5 — adopters migrated onto the ranked charter and the loop by the walk that exists, each read migrated or put to the owner](spec/2026-11-03-spec-PLAY-dConvergedCharter-5.md) | 6 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-20 — the conf fold and the unattended kit's retirement shipped as upgrade steps, every shim closed when its window does, and the adopter exit check widened](spec/2026-11-03-spec-PLAY-dConvergedCharter-20.md) | 7 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-21 — `tools/roles/house/policy.toml` retired as a seed: a repository's unruled efforts folded into `roles.effort.*` by an upgrade step, and the house-file fallback gone](spec/2026-11-03-spec-PLAY-dConvergedCharter-21.md) | 8 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-23 — the release asks' join: one key hash and one ask text for Maintain's and `release.route`'s `release-verify-failed` filings](spec/2026-11-03-spec-PLAY-dConvergedCharter-23.md) | 9 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-6 — every record kind on dTotalRecall's registry: the residue sweep of the memory tree's homes, and the kinds no spec registers](spec/2026-11-03-spec-PLAY-dConvergedCharter-6.md) | 10 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-3 — records merged by evidence: two kinds the registry and the commit history call one become one, the other name an alias shipped as an upgrade step](spec/2026-11-03-spec-PLAY-dConvergedCharter-3.md) | 11 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-19 — the guides' positional citations migrated to tags, legacy anchors kept as aliases, and the per-directory line-ending pins retired into class pins](spec/2026-11-03-spec-PLAY-dConvergedCharter-19.md) | 12 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-2 — every remaining positional reference in live text migrated to tags, frozen records resolved through redirect rows](spec/2026-11-03-spec-PLAY-dConvergedCharter-2.md) | 13 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-13 — feature-specific guide prose migrated into feature-scoped units through one prose mover](spec/2026-11-03-spec-PLAY-dConvergedCharter-13.md) | 14 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-1 — protocol text derived to facts only: each protocol document's load-bearing statements written as typed units, its rationale left for the explanation tree](spec/2026-11-03-spec-PLAY-dConvergedCharter-1.md) | 15 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-10 — the protocols and skills scopes of the one renderer: protocol slices and Skill entries rendered from units](spec/2026-11-03-spec-PLAY-dConvergedCharter-10.md) | 16 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-7 — protocols and templates as tag-sliced views, the guides retired, their rationale in units' `help` and the `help/why/` tree under `help.explanation`](spec/2026-11-03-spec-PLAY-dConvergedCharter-7.md) | 17 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-9 — Skills as level-4 thin entries from their commands' drive rows, renamed `gov-<name>` by upgrade step, the old names forwarded, the prefix and stale-path arms](spec/2026-11-03-spec-PLAY-dConvergedCharter-9.md) | 18 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-8 — the remaining renderers absorbed, each retired with its last document, and the arm that refuses one retired early](spec/2026-11-03-spec-PLAY-dConvergedCharter-8.md) | 19 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-15 — the hand-written `help/` pages, the kit READMEs, root `README.md` and the runbook migrated: a generated reference half, a how-to half under the docs leg, render parity on both](spec/2026-11-03-spec-PLAY-dConvergedCharter-15.md) | 20 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-4 — superseded parts retired through ratified proposals: one supersession proposer, its route and the ratification check](spec/2026-11-03-spec-PLAY-dConvergedCharter-4.md) | 21 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-14 — every part at its fate: the fates table as rows with path globs, and its join run as convergence's exit check](spec/2026-11-03-spec-PLAY-dConvergedCharter-14.md) | 22 | 2 | OPEN | rev-1 | 2026-11-03 |
| [PLAY-dConvergedCharter-18 — the owner's cycle walked by key from a planted build's intake, red on a hop resolved by search or prose](spec/2026-11-03-spec-PLAY-dConvergedCharter-18.md) | 23 | 2 | OPEN | rev-1 | 2026-11-03 |
<!-- /gen:build-units -->

Records: 20 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-10 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-13 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-15 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17
PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-20 PLAY-dConvergedCharter-21 PLAY-dConvergedCharter-22 PLAY-dConvergedCharter-23 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-5 PLAY-dConvergedCharter-6
PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-9.

Ids whose spec moved past its audited revision: none — 0 of 23 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dConvergedCharter's 23 clause(s) and 1 owned node(s), over 23 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 23
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0475, cl-dClosedLoop-0476, cl-dClosedLoop-0477, cl-dClosedLoop-0478, cl-dClosedLoop-0479, cl-dClosedLoop-0480, cl-dClosedLoop-0484, cl-dClosedLoop-0487, cl-dClosedLoop-0494, cl-dClosedLoop-0496
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `PLAY-dConvergedCharter-22` | no |
| 2 | `PLAY-dConvergedCharter-11` | no |
| 3 | `PLAY-dConvergedCharter-17` | no |
| 4 | `PLAY-dConvergedCharter-12` | no |
| 5 | `PLAY-dConvergedCharter-16` | no |
| 6 | `PLAY-dConvergedCharter-5` | no |
| 7 | `PLAY-dConvergedCharter-20` | no |
| 8 | `PLAY-dConvergedCharter-21` | no |
| 9 | `PLAY-dConvergedCharter-23` | no |
| 10 | `PLAY-dConvergedCharter-6` | no |
| 11 | `PLAY-dConvergedCharter-3` | no |
| 12 | `PLAY-dConvergedCharter-19` | no |
| 13 | `PLAY-dConvergedCharter-2` | no |
| 14 | `PLAY-dConvergedCharter-13` | no |
| 15 | `PLAY-dConvergedCharter-1` | no |
| 16 | `PLAY-dConvergedCharter-10` | no |
| 17 | `PLAY-dConvergedCharter-7` | no |
| 18 | `PLAY-dConvergedCharter-9` | no |
| 19 | `PLAY-dConvergedCharter-8` | no |
| 20 | `PLAY-dConvergedCharter-15` | no |
| 21 | `PLAY-dConvergedCharter-4` | no |
| 22 | `PLAY-dConvergedCharter-14` | no |
| 23 | `PLAY-dConvergedCharter-18` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dCalibratedLens](../dCalibratedLens/README.md), [dMindYourWords](../dMindYourWords/README.md), [dScopedBuild](../dScopedBuild/README.md), [dShippedRelease](../dShippedRelease/README.md)
<!-- /gen:build-edges -->
