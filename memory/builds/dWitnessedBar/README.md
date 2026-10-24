---
slug: dWitnessedBar
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-31 TOOL-dWitnessedBar-32 TOOL-dWitnessedBar-33 TOOL-dWitnessedBar-34 TOOL-dWitnessedBar-35 TOOL-dWitnessedBar-36 TOOL-dWitnessedBar-37 TOOL-dWitnessedBar-38 TOOL-dWitnessedBar-39
spec-audit: 2026-10-21
parents: dDeclaredLoop
may: PLAY-dClosedLoop-3
---

# dWitnessedBar — the Test build of the dClosedLoop chain

## The problem this build exists to solve

dWitnessedBar owns 27 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-test-01,
gap-test-02, gap-test-03, gap-test-04, gap-test-05, gap-test-06, gap-test-07, gap-test-08, gap-test-09, gap-test-10,
gap-test-11, gap-test-12, gap-test-13, gap-flow-09, gap-tool-01, gap-test-14, gap-test-15, gap-test-16, gap-test-17,
gap-test-19, gap-tool-13, gap-tool-15, gap-test-20, gap-tool-20, gap-tool-21, gap-test-21, gap-test-22. Closing every
one is this build's goal bound.

## Expected improvements

- Each of the 30 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 27 owned gaps above close.

## Detriments if this is not built

- Its 27 owned gaps stay open.
- Its 6 child builds wait on it: dBoundRoles, dTotalRecall, dMindYourWords, dScopedBuild, dShippedRelease,
  dTendedCadence.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dWitnessedBar` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dWitnessedBar`, a record per member "recorded by nobody", the same with `--write` (commit it
  as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-16.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dWitnessedBar-1` | `cl-dClosedLoop-0339@8e7bc7ae` | gate health measured and the reliability bar |
| 2 | `TOOL-dWitnessedBar-2` | `cl-dClosedLoop-0340@1984aa46` | bypasses recorded |
| 3 | `TOOL-dWitnessedBar-3` | `cl-dClosedLoop-0341@0f53eec5` | attribution deciding what blocks |
| 4 | `TOOL-dWitnessedBar-4` | `cl-dClosedLoop-0342@a3fc832c` | the runner-written verdict the pre-push hook reads |
| 5 | `TOOL-dWitnessedBar-5` | `cl-dClosedLoop-0343@3d7be760` | held legs by policy |
| 6 | `TOOL-dWitnessedBar-6` | `cl-dClosedLoop-0344@5cea08b4` | the verdict backends registered under `verdict` |
| 7 | `TOOL-dWitnessedBar-7` | `cl-dClosedLoop-0345@3265ae12` | `test.seen-red` reading the seen-red records `build.acceptance` writes |
| 8 | `TOOL-dWitnessedBar-8` | `cl-dClosedLoop-0346@c53fd58e` | flake quarantine |
| 9 | `TOOL-dWitnessedBar-9` | `cl-dClosedLoop-0347@934d7dcb` | the product-test contract with runner adapters |
| 10 | `TOOL-dWitnessedBar-10` | `cl-dClosedLoop-0348@ca24547a` | derived pre-commit list and multi-node cost evidence |
| 11 | `TOOL-dWitnessedBar-11` | `cl-dClosedLoop-0349@79373aa7` | the gate-leg factory and its conformance gate |
| 12 | `TOOL-dWitnessedBar-12` | `cl-dClosedLoop-0350@37beff65` | the `leg` |
| 13 | `TOOL-dWitnessedBar-13` | `cl-dClosedLoop-0351@d6eaa553` | retrofit's baseline ledger factory in `tools/lib` |
| 14 | `TOOL-dWitnessedBar-14` | `cl-dClosedLoop-0352@2cbf95b4` | the `ratchet` leg pack |
| 15 | `TOOL-dWitnessedBar-15` | `cl-dClosedLoop-0353@24ae0391` | `test.seed` at every check's registration |
| 16 | `TOOL-dWitnessedBar-16` | `cl-dClosedLoop-0354@1a484582` | gov's own 27 registries converted in place onto the ledger (RF-5) |
| 17 | `TOOL-dWitnessedBar-17` | `cl-dClosedLoop-0355@0f895fff` | the seven record and row pins as keyed populations |
| 18 | `TOOL-dWitnessedBar-18` | `cl-dClosedLoop-0356@4d098894` | the positional references |
| 19 | `TOOL-dWitnessedBar-19` | `cl-dClosedLoop-0357@4d3bcfbb` | the leg's purpose field in `gate-legs.json` |
| 20 | `TOOL-dWitnessedBar-20` | `cl-dClosedLoop-0358@a04b8b39` | the legacy-homes list dGroundRules declares |
| 21 | `TOOL-dWitnessedBar-21` | `cl-dClosedLoop-0359@390176b3` | a fix pass that keeps its check: its allowance excluding the red leg's own test files and gate script |
| 22 | `TOOL-dWitnessedBar-22` | `cl-dClosedLoop-0360@f873b4dc` | the `tests=` and `enforces=` edge fields on legs (night pass |
| 23 | `TOOL-dWitnessedBar-23` | `cl-dClosedLoop-0361@59790344` | a minimal tester agent in today's roles kit |
| 24 | `TOOL-dWitnessedBar-24` | `cl-dClosedLoop-0362@46f28632` | the portability leg pack: a line-ending class leg |
| 25 | `TOOL-dWitnessedBar-25` | `cl-dClosedLoop-0363@4ad46937` | the verdict record naming its bar run and its cause |
| 26 | `TOOL-dWitnessedBar-26` | `cl-dClosedLoop-0364@2fbc8cf5` | one bash resolver in `tools/lib` with its JavaScript twin |
| 27 | `TOOL-dWitnessedBar-27` | `cl-dClosedLoop-0365@47113ea2` | a wrong-shell refusal at every entry point: a gov script started by WSL's bash on a Windows checkout |
| 28 | `TOOL-dWitnessedBar-28` | `cl-dClosedLoop-0366@a7d91105` | a repository's legs from its overlay's leg rows through the leg factory |
| 29 | `TOOL-dWitnessedBar-29` | `cl-dClosedLoop-0367@c53d0fb3` | every size warning shown on a passing run |
| 30 | `TOOL-dWitnessedBar-30` | `cl-dClosedLoop-0368@53672db0` | a quarantined leg released after `verdict.flakes.release`' streak of consecutive greens |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 30 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13
ids TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26
ids TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-31 TOOL-dWitnessedBar-32 TOOL-dWitnessedBar-33 TOOL-dWitnessedBar-34 TOOL-dWitnessedBar-35 TOOL-dWitnessedBar-36 TOOL-dWitnessedBar-37 TOOL-dWitnessedBar-38 TOOL-dWitnessedBar-39

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dWitnessedBar-26 — one bash resolver in `tools/lib` with its JavaScript twin](spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md) | 1 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-27 — a wrong-shell refusal at every entry point](spec/2026-10-25-spec-TOOL-dWitnessedBar-27.md) | 2 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-13 — retrofit's baseline ledger factory in `tools/lib`](spec/2026-10-25-spec-TOOL-dWitnessedBar-13.md) | 3 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-15 — `test.seed` at every check's registration](spec/2026-10-25-spec-TOOL-dWitnessedBar-15.md) | 4 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-12 — the `leg`, `check` and `pack` tag namespaces, and a `tag` on every leg](spec/2026-10-25-spec-TOOL-dWitnessedBar-12.md) | 5 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-22 — the `tests=` and `enforces=` edge fields on legs](spec/2026-10-25-spec-TOOL-dWitnessedBar-22.md) | 6 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-19 — the leg's `purpose` field in `gate-legs.json`, every leg reviewed](spec/2026-10-25-spec-TOOL-dWitnessedBar-19.md) | 7 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-11 — the gate-leg factory and its conformance gate, every leg declaring the principles it enforces](spec/2026-10-25-spec-TOOL-dWitnessedBar-11.md) | 8 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-14 — the `ratchet` leg pack, and a population's growth admitted only as `retrofit.widen` says](spec/2026-10-25-spec-TOOL-dWitnessedBar-14.md) | 9 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-16 — gov's own registries converted in place onto the ledger (RF-5), with the readers the conversion owes](spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md) | 10 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-17 — the seven record and row pins as keyed populations, and the date cutoffs registered as cutoffs](spec/2026-10-25-spec-TOOL-dWitnessedBar-17.md) | 11 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-18 — the positional references, IW-1's legacy list and the unpinned facts registered from dOrderedCharter's keyed lists, and dSafePassage's landed step rows as an append-only population](spec/2026-10-25-spec-TOOL-dWitnessedBar-18.md) | 12 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-20 — the legacy-homes list converted into a ledger population keyed by conf and key](spec/2026-10-25-spec-TOOL-dWitnessedBar-20.md) | 13 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-24 — the portability leg pack: every P37 rule on a leg, each arm seen red on a planted case](spec/2026-10-25-spec-TOOL-dWitnessedBar-24.md) | 14 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-10 — the pre-commit list derived from the leg rows, and cost evidence from every node](spec/2026-10-25-spec-TOOL-dWitnessedBar-10.md) | 15 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-9 — the product-test contract: `level` on legs, the three `tests.*` keys, and runner adapters](spec/2026-10-25-spec-TOOL-dWitnessedBar-9.md) | 16 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-4 — the runner-written verdict per tree, the pre-push hook reading it, and the tree Test verifies](spec/2026-10-25-spec-TOOL-dWitnessedBar-4.md) | 17 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-25 — the verdict names its bar run and its cause, and a failing leg's output tail is kept by hash](spec/2026-10-25-spec-TOOL-dWitnessedBar-25.md) | 18 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-23 — a minimal tester agent in today's roles kit](spec/2026-10-25-spec-TOOL-dWitnessedBar-23.md) | 19 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-3 — attribution deciding what blocks](spec/2026-10-25-spec-TOOL-dWitnessedBar-3.md) | 20 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-5 — held legs by policy](spec/2026-10-25-spec-TOOL-dWitnessedBar-5.md) | 21 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-8 — flake quarantine](spec/2026-10-25-spec-TOOL-dWitnessedBar-8.md) | 22 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-1 — gate health measured and the reliability bar](spec/2026-10-25-spec-TOOL-dWitnessedBar-1.md) | 23 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-30 — a quarantined leg released after its streak, and a contended red re-run on a quiet host](spec/2026-10-25-spec-TOOL-dWitnessedBar-30.md) | 24 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-29 — every size warning a passing leg prints, shown in the runner's summary and verdict record and attributed to its unit](spec/2026-10-25-spec-TOOL-dWitnessedBar-29.md) | 25 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-7 — `test.seen-red` reading one seen-red record per gate a build adds or changes, the acceptance-ledger line standing in for `build.acceptance`](spec/2026-10-25-spec-TOOL-dWitnessedBar-7.md) | 26 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-21 — a fix pass that keeps its check: its allowance less the red leg's own files and the acceptance commands' own files](spec/2026-10-25-spec-TOOL-dWitnessedBar-21.md) | 27 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-6 — the verdict backends registered under `verdict`: the local hook, the peer-node verifier and the `remote-ci` slot with its witness rule and pin](spec/2026-10-25-spec-TOOL-dWitnessedBar-6.md) | 28 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-2 — each hook bypass recorded under `hooks.bypass`, and `refused` held by an off-node witness](spec/2026-10-25-spec-TOOL-dWitnessedBar-2.md) | 29 | 2 | OPEN | rev-1 | 2026-10-25 |
| [TOOL-dWitnessedBar-28 — a repository's legs from its overlay's leg rows through the leg factory, gov's legs changed only by pinned patches, every other leg landing](spec/2026-10-25-spec-TOOL-dWitnessedBar-28.md) | 30 | 2 | OPEN | rev-1 | 2026-10-25 |
<!-- /gen:build-units -->

Records: 18 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19
TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-30
TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9.

Ids whose spec moved past its audited revision: none — 0 of 30 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dWitnessedBar's 30 clause(s) and 37 owned node(s), over 30 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 30
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 5 (cl-dClosedLoop-0341, cl-dClosedLoop-0345, cl-dClosedLoop-0354, cl-dClosedLoop-0359, cl-dClosedLoop-0366)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0340, cl-dClosedLoop-0342, cl-dClosedLoop-0343, cl-dClosedLoop-0348, cl-dClosedLoop-0349, cl-dClosedLoop-0355, cl-dClosedLoop-0356, cl-dClosedLoop-0358, cl-dClosedLoop-0367
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dWitnessedBar-26` | no |
| 2 | `TOOL-dWitnessedBar-27` | no |
| 3 | `TOOL-dWitnessedBar-13` | no |
| 4 | `TOOL-dWitnessedBar-15` | no |
| 5 | `TOOL-dWitnessedBar-12` | no |
| 6 | `TOOL-dWitnessedBar-22` | no |
| 7 | `TOOL-dWitnessedBar-19` | no |
| 8 | `TOOL-dWitnessedBar-11` | no |
| 9 | `TOOL-dWitnessedBar-14` | no |
| 10 | `TOOL-dWitnessedBar-16` | no |
| 11 | `TOOL-dWitnessedBar-17` | no |
| 12 | `TOOL-dWitnessedBar-18` | no |
| 13 | `TOOL-dWitnessedBar-20` | no |
| 14 | `TOOL-dWitnessedBar-24` | no |
| 15 | `TOOL-dWitnessedBar-10` | no |
| 16 | `TOOL-dWitnessedBar-9` | no |
| 17 | `TOOL-dWitnessedBar-4` | no |
| 18 | `TOOL-dWitnessedBar-25` | no |
| 19 | `TOOL-dWitnessedBar-23` | no |
| 20 | `TOOL-dWitnessedBar-3` | no |
| 21 | `TOOL-dWitnessedBar-5` | no |
| 22 | `TOOL-dWitnessedBar-8` | no |
| 23 | `TOOL-dWitnessedBar-1` | no |
| 24 | `TOOL-dWitnessedBar-30` | no |
| 25 | `TOOL-dWitnessedBar-29` | no |
| 26 | `TOOL-dWitnessedBar-7` | no |
| 27 | `TOOL-dWitnessedBar-21` | no |
| 28 | `TOOL-dWitnessedBar-6` | no |
| 29 | `TOOL-dWitnessedBar-2` | no |
| 30 | `TOOL-dWitnessedBar-28` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md)
- **Child builds:** [dBoundRoles](../dBoundRoles/README.md), [dMindYourWords](../dMindYourWords/README.md), [dScopedBuild](../dScopedBuild/README.md), [dShippedRelease](../dShippedRelease/README.md), [dTendedCadence](../dTendedCadence/README.md), [dTotalRecall](../dTotalRecall/README.md)
<!-- /gen:build-edges -->
