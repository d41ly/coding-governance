---
slug: dShippedRelease
node: d
opened: 2026-10-21
streams: deployer
roster: DEPL
ids: DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-32 DEPL-dShippedRelease-33 DEPL-dShippedRelease-34 DEPL-dShippedRelease-35 DEPL-dShippedRelease-36 DEPL-dShippedRelease-37 DEPL-dShippedRelease-38 DEPL-dShippedRelease-39 DEPL-dShippedRelease-40 DEPL-dShippedRelease-41 DEPL-dShippedRelease-42 DEPL-dShippedRelease-43 DEPL-dShippedRelease-44 DEPL-dShippedRelease-45 DEPL-dShippedRelease-46 DEPL-dShippedRelease-47 DEPL-dShippedRelease-48 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78
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
**Build status:** OPEN · 61 unit(s) · node d · opened 2026-10-21 · streams deployer
ids DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12
ids DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24
ids DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-32 DEPL-dShippedRelease-33 DEPL-dShippedRelease-34 DEPL-dShippedRelease-35 DEPL-dShippedRelease-36
ids DEPL-dShippedRelease-37 DEPL-dShippedRelease-38 DEPL-dShippedRelease-39 DEPL-dShippedRelease-40 DEPL-dShippedRelease-41 DEPL-dShippedRelease-42 DEPL-dShippedRelease-43 DEPL-dShippedRelease-44 DEPL-dShippedRelease-45 DEPL-dShippedRelease-46 DEPL-dShippedRelease-47 DEPL-dShippedRelease-48
ids DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60
ids DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72
ids DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-dShippedRelease-10 — the kit factory, its conformance gate, and one version and one wiring verdict](spec/2026-10-30-spec-DEPL-dShippedRelease-10.md) | 1 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-21 — a purpose on every kit, descriptors for govkit and lib, and inline copies generated](spec/2026-10-30-spec-DEPL-dShippedRelease-21.md) | 2 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-65 — every failure line of `check-kit-versions.sh` gets a home in `derive_version_findings` or a named retirement](spec/2026-10-30-spec-DEPL-dShippedRelease-65.md) | 2 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-66 — a retired leg stays resolvable for a live spec older than its retirement, by a row naming its successor](spec/2026-10-30-spec-DEPL-dShippedRelease-66.md) | 2 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-23 — the deployer's definition, registered as an expansion's item role](spec/2026-10-30-spec-DEPL-dShippedRelease-23.md) | 3 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-31 — the adopter register, and the word fleet left to node units](spec/2026-10-30-spec-DEPL-dShippedRelease-31.md) | 4 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-11 — a dependent's landing held until its parent lands](spec/2026-10-30-spec-DEPL-dShippedRelease-11.md) | 5 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-12 — the landing queue, the landing turn, and the lander's outcome record](spec/2026-10-30-spec-DEPL-dShippedRelease-12.md) | 6 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-49 — `read_parent_state` reads `landed` only for a parent whose units shipped](spec/2026-10-30-spec-DEPL-dShippedRelease-49.md) | 6 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-50 — a carried parent reads `held`, only a terminal disposition reads `withdrawn`, and a spec-run landing is exempt from the hold](spec/2026-10-30-spec-DEPL-dShippedRelease-50.md) | 6 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-1 — the landing record, one ref per landed SHA and its one reader](spec/2026-10-30-spec-DEPL-dShippedRelease-1.md) | 7 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-70 — a second node reads a landed SHA by containment, and an unlanded SHA by its own class](spec/2026-10-30-spec-DEPL-dShippedRelease-70.md) | 7 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-71 — a queue entry leaves by a written exit, so a refused or held head blocks no other landing](spec/2026-10-30-spec-DEPL-dShippedRelease-71.md) | 7 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-72 — only an admission exit 0 lands, and every other exit stops with nothing pushed](spec/2026-10-30-spec-DEPL-dShippedRelease-72.md) | 7 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-2 — `deploy.distill` unarmed, recording that it measured nothing](spec/2026-10-30-spec-DEPL-dShippedRelease-2.md) | 8 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-13 — `deploy.core`: the core checks read on the landed tree, the per-SHA verdict and the patch a red files](spec/2026-10-30-spec-DEPL-dShippedRelease-13.md) | 9 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-4 — the deploy engine: `deploy.current` to `deploy.close`, `deploy.unlease` and the mailbox it closes](spec/2026-10-30-spec-DEPL-dShippedRelease-4.md) | 10 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-53 — `deploy.record` copies the core verdict at its write, and `deploy.core` never writes to an absent ref](spec/2026-10-30-spec-DEPL-dShippedRelease-53.md) | 10 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-14 — the landing review, blocking the build's close and never the push](spec/2026-10-30-spec-DEPL-dShippedRelease-14.md) | 11 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-56 — a `running` core passes to `deploy.record`, so a landing record exists for the length of the bar](spec/2026-10-30-spec-DEPL-dShippedRelease-56.md) | 11 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-58 — every `step.deploy` item has a verb and an adapter row, and the documented order reaches `run_deploy_land`](spec/2026-10-30-spec-DEPL-dShippedRelease-58.md) | 11 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-59 — the records landing takes the turn and skips the queue's order, and a slug with no entry is enqueued at the call](spec/2026-10-30-spec-DEPL-dShippedRelease-59.md) | 11 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-68 — the late records landing passes the lander after the tombstone, from a tree of its own](spec/2026-10-30-spec-DEPL-dShippedRelease-68.md) | 11 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-69 — a landing that closes by carry-forward hands its lease back, so a second run of one slug can acquire it](spec/2026-10-30-spec-DEPL-dShippedRelease-69.md) | 11 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-15 — promotion through environments: the `integrations` kit, the seven `release.*` items and a compare-and-swap on every promote](spec/2026-10-30-spec-DEPL-dShippedRelease-15.md) | 12 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-51 — the landing review's base is the recorded tip before the push](spec/2026-10-30-spec-DEPL-dShippedRelease-51.md) | 12 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-52 — a landing with no outcome record derives its prior tip from the nearest first-parent merge](spec/2026-10-30-spec-DEPL-dShippedRelease-52.md) | 12 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-60 — `--deploy review` reads its own field first, so a re-walk neither re-fires nor overwrites a disposal](spec/2026-10-30-spec-DEPL-dShippedRelease-60.md) | 12 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-73 — `check_landing_review` re-derives its pass from sources the field does not control](spec/2026-10-30-spec-DEPL-dShippedRelease-73.md) | 12 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-55 — `release.pick` stops at what an environment already runs, so a re-tick promotes nothing older](spec/2026-10-30-spec-DEPL-dShippedRelease-55.md) | 13 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-6 — the first engine adapter, `compose-systemd`, for signed container images](spec/2026-10-30-spec-DEPL-dShippedRelease-6.md) | 13 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-27 — `carries` on the landing record, the `landing` class, publications, `commits.squash` and Codex targets](spec/2026-10-30-spec-DEPL-dShippedRelease-27.md) | 14 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-77 — the engine answers an empty environment, a named service and a failed restart](spec/2026-10-30-spec-DEPL-dShippedRelease-77.md) | 14 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-5 — the `deploy.released` wait: `build.release-ceiling` as its deadline and the release hold's one owner item](spec/2026-10-30-spec-DEPL-dShippedRelease-5.md) | 15 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-30 — the patch build's shared budget: one red, one patch, a draw on the root's lease and the third keep-waiting](spec/2026-10-30-spec-DEPL-dShippedRelease-30.md) | 16 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-3 — `kits.cut`: the annotated release tag and its generated notes](spec/2026-10-30-spec-DEPL-dShippedRelease-3.md) | 17 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-25 — the receipt's schema 5: `release`, `source_remote` and the step that raises it](spec/2026-10-30-spec-DEPL-dShippedRelease-25.md) | 18 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-61 — gov's own harnesses declare `install.from`, so the default refuses no suite once a tag exists](spec/2026-10-30-spec-DEPL-dShippedRelease-61.md) | 19 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-62 — the `release-tag` refusal runs before the first write, on `apply` and on `update`](spec/2026-10-30-spec-DEPL-dShippedRelease-62.md) | 19 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-63 — `derive_public_remote` strips the whole userinfo of a non-ssh remote](spec/2026-10-30-spec-DEPL-dShippedRelease-63.md) | 19 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-64 — `check_release_field` reds any userinfo a shipped receipt holds, through a block the run-gates kit carries](spec/2026-10-30-spec-DEPL-dShippedRelease-64.md) | 19 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-7 — the adopter register read and the currency watch: `kits.currency` in each adopter, `kits.adopters` in gov](spec/2026-10-30-spec-DEPL-dShippedRelease-7.md) | 19 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-16 — the unattended `kits.offer`: an update run in a mode that runs nothing from the adopter's tree, pushed through the adopter's own scoped grant](spec/2026-10-30-spec-DEPL-dShippedRelease-16.md) | 20 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-20 — an offered update runs neither `adopt` nor `test.seed`, its order names the adopter's own run of each, and outbox orders are graded](spec/2026-10-30-spec-DEPL-dShippedRelease-20.md) | 21 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-76 — the offer spells two environments: the grant for clone and push, and none for `update`](spec/2026-10-30-spec-DEPL-dShippedRelease-76.md) | 21 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-17 — `kits.install` and `kits.update`: the walk that closes on dSafePassage's outcomes, the attended hooks, the backlog step, and a fresh install in one pass](spec/2026-10-30-spec-DEPL-dShippedRelease-17.md) | 22 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-75 — the `codex-retrust` orders row carries the shape its readers consume](spec/2026-10-30-spec-DEPL-dShippedRelease-75.md) | 22 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-28 — `adopt.declarations`: today's flow and role customizations proposed as overlay rows, each ruled once](spec/2026-10-30-spec-DEPL-dShippedRelease-28.md) | 23 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-67 — `install --all` selects through `resolve_selection`, the one selection `cmd_apply` already calls](spec/2026-10-30-spec-DEPL-dShippedRelease-67.md) | 23 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-29 — the update's report over every kind: each row's state, every repository row, every widening, and a lost change told from an unrelated hole](spec/2026-10-30-spec-DEPL-dShippedRelease-29.md) | 24 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-18 — every release updates gov's own install first: `kits.cut` refuses a tag at a SHA with no green gov-first record](spec/2026-10-30-spec-DEPL-dShippedRelease-18.md) | 25 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-24 — `install.guards`: the core guards in the project's settings, or in managed settings where the operator opts in](spec/2026-10-30-spec-DEPL-dShippedRelease-24.md) | 26 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-8 — optional emitted CI: every `uses:` pinned by sha from one declaration gov's own workflow also uses, under least-privilege `permissions:`](spec/2026-10-30-spec-DEPL-dShippedRelease-8.md) | 27 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-26 — the platform matrix verified per release: runner rows for `platforms.supported` under `platforms.verify`, generalizing `run-held-wsl.sh`, and a Linux job in emitted CI at the floor](spec/2026-10-30-spec-DEPL-dShippedRelease-26.md) | 28 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-54 — `emitted ci pins` grades row use only over a `--workflow`, so an adopter's base argv is green](spec/2026-10-30-spec-DEPL-dShippedRelease-54.md) | 28 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-57 — `ci_emit.py check`'s fixture states its green baseline, so unit 8's row criteria can fail](spec/2026-10-30-spec-DEPL-dShippedRelease-57.md) | 28 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-74 — a non-opting install of the integrations kit reads an accepted stop, not a missing render](spec/2026-10-30-spec-DEPL-dShippedRelease-74.md) | 28 | 2 | OPEN | rev-1 | 2026-10-30 |
| [DEPL-dShippedRelease-19 — the integrations `import` of an adopter's CI jobs as legs: only a job ruled `import`, test jobs only, each through an adapter row](spec/2026-10-30-spec-DEPL-dShippedRelease-19.md) | 29 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-22 — the ask tracker's one-way mirror, the adapter `integrations.tracker: mirror-out` selects](spec/2026-10-30-spec-DEPL-dShippedRelease-22.md) | 30 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-9 — a derived runbook: the operator order for install and update, rendered from the kit descriptors, a hand edit red at render parity](spec/2026-10-30-spec-DEPL-dShippedRelease-9.md) | 31 | 2 | OPEN | rev-2 | 2026-10-30 |
| [DEPL-dShippedRelease-78 — the round-1 spec audit's 77 minors, batched: the Readers of what unit 10 retires, the legs and rows each unit owes, honest failure states, and the observations that read the wrong thing](spec/2026-10-30-spec-DEPL-dShippedRelease-78.md) | 32 | 2 | OPEN | rev-1 | 2026-10-30 |
<!-- /gen:build-units -->

Records: 30 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58
DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70
DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78.

Ids whose spec moved past its audited revision: DEPL-dShippedRelease-1@rev-1 DEPL-dShippedRelease-10@rev-1 DEPL-dShippedRelease-11@rev-1 DEPL-dShippedRelease-12@rev-1 DEPL-dShippedRelease-13@rev-1 DEPL-dShippedRelease-14@rev-1 DEPL-dShippedRelease-15@rev-1 DEPL-dShippedRelease-16@rev-1
DEPL-dShippedRelease-17@rev-1 DEPL-dShippedRelease-19@rev-1 DEPL-dShippedRelease-2@rev-1 DEPL-dShippedRelease-20@rev-1 DEPL-dShippedRelease-21@rev-1 DEPL-dShippedRelease-22@rev-1 DEPL-dShippedRelease-24@rev-1 DEPL-dShippedRelease-25@rev-1 DEPL-dShippedRelease-26@rev-1 DEPL-dShippedRelease-27@rev-1
DEPL-dShippedRelease-28@rev-1 DEPL-dShippedRelease-29@rev-1 DEPL-dShippedRelease-3@rev-1 DEPL-dShippedRelease-31@rev-1 DEPL-dShippedRelease-4@rev-1 DEPL-dShippedRelease-5@rev-1 DEPL-dShippedRelease-6@rev-1 DEPL-dShippedRelease-7@rev-1 DEPL-dShippedRelease-8@rev-1 DEPL-dShippedRelease-9@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dShippedRelease's 31 clause(s) and 60 owned node(s), over 61 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 31
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-30-spec-DEPL-dShippedRelease-49.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-51.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-30-spec-DEPL-dShippedRelease-52.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-53.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-55.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-30-spec-DEPL-dShippedRelease-56.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-57.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-58.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-59.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-30-spec-DEPL-dShippedRelease-60.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-61.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-62.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-63.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-30-spec-DEPL-dShippedRelease-64.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-65.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-66.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-67.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-30-spec-DEPL-dShippedRelease-68.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-69.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-70.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-71.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-30-spec-DEPL-dShippedRelease-72.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-73.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-74.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-75.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-30-spec-DEPL-dShippedRelease-76.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-77.md` (PLAY-dClosedLoop-2), `spec/2026-10-30-spec-DEPL-dShippedRelease-78.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0413, cl-dClosedLoop-0416, cl-dClosedLoop-0419, cl-dClosedLoop-0420, cl-dClosedLoop-0433
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `DEPL-dShippedRelease-10` | no |
| 2 | `DEPL-dShippedRelease-21`, `DEPL-dShippedRelease-65`, `DEPL-dShippedRelease-66` | no |
| 3 | `DEPL-dShippedRelease-23` | no |
| 4 | `DEPL-dShippedRelease-31` | no |
| 5 | `DEPL-dShippedRelease-11` | no |
| 6 | `DEPL-dShippedRelease-12`, `DEPL-dShippedRelease-49`, `DEPL-dShippedRelease-50` | no |
| 7 | `DEPL-dShippedRelease-1`, `DEPL-dShippedRelease-70`, `DEPL-dShippedRelease-71`, `DEPL-dShippedRelease-72` | no |
| 8 | `DEPL-dShippedRelease-2` | no |
| 9 | `DEPL-dShippedRelease-13` | no |
| 10 | `DEPL-dShippedRelease-4`, `DEPL-dShippedRelease-53` | no |
| 11 | `DEPL-dShippedRelease-14`, `DEPL-dShippedRelease-56`, `DEPL-dShippedRelease-58`, `DEPL-dShippedRelease-59`, `DEPL-dShippedRelease-68`, `DEPL-dShippedRelease-69` | no |
| 12 | `DEPL-dShippedRelease-15`, `DEPL-dShippedRelease-51`, `DEPL-dShippedRelease-52`, `DEPL-dShippedRelease-60`, `DEPL-dShippedRelease-73` | no |
| 13 | `DEPL-dShippedRelease-55`, `DEPL-dShippedRelease-6` | yes |
| 14 | `DEPL-dShippedRelease-27`, `DEPL-dShippedRelease-77` | no |
| 15 | `DEPL-dShippedRelease-5` | no |
| 16 | `DEPL-dShippedRelease-30` | no |
| 17 | `DEPL-dShippedRelease-3` | no |
| 18 | `DEPL-dShippedRelease-25` | no |
| 19 | `DEPL-dShippedRelease-61`, `DEPL-dShippedRelease-62`, `DEPL-dShippedRelease-63`, `DEPL-dShippedRelease-64`, `DEPL-dShippedRelease-7` | no |
| 20 | `DEPL-dShippedRelease-16` | no |
| 21 | `DEPL-dShippedRelease-20`, `DEPL-dShippedRelease-76` | no |
| 22 | `DEPL-dShippedRelease-17`, `DEPL-dShippedRelease-75` | no |
| 23 | `DEPL-dShippedRelease-28`, `DEPL-dShippedRelease-67` | no |
| 24 | `DEPL-dShippedRelease-29` | no |
| 25 | `DEPL-dShippedRelease-18` | no |
| 26 | `DEPL-dShippedRelease-24` | no |
| 27 | `DEPL-dShippedRelease-8` | no |
| 28 | `DEPL-dShippedRelease-26`, `DEPL-dShippedRelease-54`, `DEPL-dShippedRelease-57`, `DEPL-dShippedRelease-74` | no |
| 29 | `DEPL-dShippedRelease-19` | no |
| 30 | `DEPL-dShippedRelease-22` | no |
| 31 | `DEPL-dShippedRelease-9` | no |
| 32 | `DEPL-dShippedRelease-78` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md), [dFurnishedOrders](../dFurnishedOrders/README.md), [dLinkedLibrary](../dLinkedLibrary/README.md), [dTotalRecall](../dTotalRecall/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
- **Child builds:** [dConvergedCharter](../dConvergedCharter/README.md)
<!-- /gen:build-edges -->
