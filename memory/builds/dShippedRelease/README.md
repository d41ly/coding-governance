---
slug: dShippedRelease
node: d
opened: 2026-10-21
streams: deployer
roster: DEPL
ids: DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-32
status: OPEN
spec-audit: 2026-10-21
parents: dWitnessedBar dTotalRecall dBoundRoles dWellOiledMachine dLinkedLibrary dFurnishedOrders
may: PLAY-dClosedLoop-3
---

# dShippedRelease — the Deploy build of the dClosedLoop chain

## The problem this build exists to solve

dShippedRelease owns 24 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-deploy-01,
gap-deploy-02, gap-deploy-03, gap-deploy-04, gap-deploy-05, gap-deploy-06, gap-deploy-08, gap-deploy-09,
gap-deploy-10, gap-deploy-11, gap-deploy-12, gap-deploy-13, gap-deploy-14, gap-flow-08, gap-tool-02, gap-tool-04,
gap-tool-07, gap-deploy-21, gap-deploy-22, gap-deploy-23, gap-tool-11, gap-deploy-27, gap-deploy-28, gap-deploy-29.
Closing every one is this build's goal bound.

## Expected improvements

- Each of the 31 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 24 owned gaps above close.

## Detriments if this is not built

- Its 24 owned gaps stay open.
- Its 1 child build waits on it: dConvergedCharter.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dShippedRelease` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dShippedRelease`, a record per member "recorded by nobody", the same with `--write` (commit
  it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
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
| 1 | `DEPL-dShippedRelease-1` | `cl-dClosedLoop-0413@7914d7c9` | the landing record |
| 2 | `DEPL-dShippedRelease-2` | `cl-dClosedLoop-0507@e74286a1` | `deploy.distill` unarmed until dScopedBuild lands `build.distill`: it records on the landing record that it measured nothing |
| 3 | `DEPL-dShippedRelease-3` | `cl-dClosedLoop-0414@d9d47e83` | kit release notes |
| 4 | `DEPL-dShippedRelease-4` | `cl-dClosedLoop-0415@82cfbcec` | the deploy engine |
| 5 | `DEPL-dShippedRelease-5` | `cl-dClosedLoop-0508@68f388b5` | the release arms dWellOiledMachine's sweep and lander leave to this build: a `deploy.released` wait given `build.release-ceiling` as its declared deadline |
| 6 | `DEPL-dShippedRelease-6` | `cl-dClosedLoop-0416@7154a42c` | the first engine adapter |
| 7 | `DEPL-dShippedRelease-7` | `cl-dClosedLoop-0417@3e86117a` | the adopter register and currency watch |
| 8 | `DEPL-dShippedRelease-8` | `cl-dClosedLoop-0418@0096c2c8` | optional emitted CI |
| 9 | `DEPL-dShippedRelease-9` | `cl-dClosedLoop-0419@c78ef1a4` | a derived runbook: the operator order for install and update |
| 10 | `DEPL-dShippedRelease-10` | `cl-dClosedLoop-0420@7a9716bf` | the kit factory and its conformance gate |
| 11 | `DEPL-dShippedRelease-11` | `cl-dClosedLoop-0421@62dc6590` | a dependent's landing held until its parent lands (`deps.landing`) |
| 12 | `DEPL-dShippedRelease-12` | `cl-dClosedLoop-0422@027c3b9f` | landings ordered through the landing queue it builds |
| 13 | `DEPL-dShippedRelease-13` | `cl-dClosedLoop-0423@a58b92bf` | the lander running the core checks on the landed tree before it releases the build |
| 14 | `DEPL-dShippedRelease-14` | `cl-dClosedLoop-0424@efed0e2f` | the landing review blocking the build's close rather than the push |
| 15 | `DEPL-dShippedRelease-15` | `cl-dClosedLoop-0425@3b7313d6` | promotion after landing through environments as an integrations extension point |
| 16 | `DEPL-dShippedRelease-16` | `cl-dClosedLoop-0426@a52a5e6d` | an unattended `kits.offer` in a govkit mode that runs nothing from the adopter's tree |
| 17 | `DEPL-dShippedRelease-17` | `cl-dClosedLoop-0427@131c1447` | the install and update hooks that call `adopt` and `test.seed` |
| 18 | `DEPL-dShippedRelease-18` | `cl-dClosedLoop-0428@e9fcd4a6` | every release updating gov's own install first |
| 19 | `DEPL-dShippedRelease-19` | `cl-dClosedLoop-0429@78bd7623` | the integrations import of an adopter's CI jobs as legs |
| 20 | `DEPL-dShippedRelease-20` | `cl-dClosedLoop-0430@25fe9858` | an update `kits.offer` offers runs neither `adopt` nor `test.seed` in the adopter's tree |
| 21 | `DEPL-dShippedRelease-21` | `cl-dClosedLoop-0431@3ef16038` | the kit factory's purpose field and a `kit.toml` for govkit and lib |
| 22 | `DEPL-dShippedRelease-22` | `cl-dClosedLoop-0432@e42728b4` | the ask tracker's one-way mirror |
| 23 | `DEPL-dShippedRelease-23` | `cl-dClosedLoop-0433@ff09e77e` | the deployer's definition |
| 24 | `DEPL-dShippedRelease-24` | `cl-dClosedLoop-0434@df3486aa` | `install.guards`: the core guards installed into the project's settings |
| 25 | `DEPL-dShippedRelease-25` | `cl-dClosedLoop-0435@df636953` | the receipt's schema 5 gaining `superseded` |
| 26 | `DEPL-dShippedRelease-26` | `cl-dClosedLoop-0436@57841d5d` | the platform matrix verified per release: platform runner adapters for `platforms.supported` under `platforms.verify` |
| 27 | `DEPL-dShippedRelease-27` | `cl-dClosedLoop-0437@b595f1f2` | `carries` on the landing record |
| 28 | `DEPL-dShippedRelease-28` | `cl-dClosedLoop-0438@088c545a` | `adopt.declarations`: at install and update |
| 29 | `DEPL-dShippedRelease-29` | `cl-dClosedLoop-0439@1aecad6a` | the update's report extended to every kind: each gov row's state in the repository |
| 30 | `DEPL-dShippedRelease-30` | `cl-dClosedLoop-0440@13cc3301` | a patch build raised by a landing |
| 31 | `DEPL-dShippedRelease-31` | `cl-dClosedLoop-0441@1aab6ce8` | the word fleet left to node units: the register of adopters built as the adopter register |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams deployer
ids DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12
ids DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24
ids DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-32

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 12 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dShippedRelease's 31 clause(s) and 60 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 31 (cl-dClosedLoop-0413, cl-dClosedLoop-0507, cl-dClosedLoop-0414, cl-dClosedLoop-0415, cl-dClosedLoop-0508, cl-dClosedLoop-0416, cl-dClosedLoop-0417, cl-dClosedLoop-0418, cl-dClosedLoop-0419, cl-dClosedLoop-0420, cl-dClosedLoop-0421, cl-dClosedLoop-0422, cl-dClosedLoop-0423,
  cl-dClosedLoop-0424, cl-dClosedLoop-0425, cl-dClosedLoop-0426, cl-dClosedLoop-0427, cl-dClosedLoop-0428, cl-dClosedLoop-0429, cl-dClosedLoop-0430, cl-dClosedLoop-0431, cl-dClosedLoop-0432, cl-dClosedLoop-0433, cl-dClosedLoop-0434, cl-dClosedLoop-0435, cl-dClosedLoop-0436, cl-dClosedLoop-0437,
  cl-dClosedLoop-0438, cl-dClosedLoop-0439, cl-dClosedLoop-0440, cl-dClosedLoop-0441)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.adopt.declarations, item.deploy.close, item.deploy.core, item.deploy.current, item.deploy.distill, item.deploy.land, item.deploy.mandate, item.deploy.notify, item.deploy.parents, item.deploy.record, item.deploy.released, item.deploy.snapshot, item.deploy.unlease,
  item.kits.adopters, item.kits.currency, item.kits.cut, item.kits.install, item.kits.install-attended, item.kits.offer, item.kits.update, item.kits.update-attended, item.kits.version, item.release.approve-auto, item.release.approve-owner, item.release.pick, item.release.promote,
  item.release.record, item.release.route, item.release.verify, policy-key.build.closes, policy-key.build.release-ceiling, policy-key.build.release-hold, policy-key.commits.squash, policy-key.currency.max-behind, policy-key.currency.on-behind, policy-key.deploy.currency,
  policy-key.deploy.on-verify-fail, policy-key.deploy.promotion, policy-key.deploy.runs, policy-key.deps.landing, policy-key.install.from, policy-key.install.guards, policy-key.install.steps, policy-key.integrations.tracker, policy-key.kits.cadence, policy-key.kits.host,
  policy-key.kits.watch-cadence, policy-key.landing.order, policy-key.platforms.supported, policy-key.platforms.verify, policy-key.release.environments, record-kind.adopter-register, record-kind.adopters, record-kind.comparison, record-kind.currency, record-kind.kit-release, record-kind.landing,
  record-kind.receipt, record-kind.release, record-kind.release-exit
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0413, cl-dClosedLoop-0416, cl-dClosedLoop-0419, cl-dClosedLoop-0420, cl-dClosedLoop-0433
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md), [dFurnishedOrders](../dFurnishedOrders/README.md), [dLinkedLibrary](../dLinkedLibrary/README.md), [dTotalRecall](../dTotalRecall/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
- **Child builds:** [dConvergedCharter](../dConvergedCharter/README.md)
<!-- /gen:build-edges -->
