---
slug: dWitnessedBar
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-31
status: OPEN
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
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13
ids TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26
ids TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-31

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dWitnessedBar's 30 clause(s) and 37 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 30 (cl-dClosedLoop-0339, cl-dClosedLoop-0340, cl-dClosedLoop-0341, cl-dClosedLoop-0342, cl-dClosedLoop-0343, cl-dClosedLoop-0344, cl-dClosedLoop-0345, cl-dClosedLoop-0346, cl-dClosedLoop-0347, cl-dClosedLoop-0348, cl-dClosedLoop-0349, cl-dClosedLoop-0350, cl-dClosedLoop-0351,
  cl-dClosedLoop-0352, cl-dClosedLoop-0353, cl-dClosedLoop-0354, cl-dClosedLoop-0355, cl-dClosedLoop-0356, cl-dClosedLoop-0357, cl-dClosedLoop-0358, cl-dClosedLoop-0359, cl-dClosedLoop-0360, cl-dClosedLoop-0361, cl-dClosedLoop-0362, cl-dClosedLoop-0363, cl-dClosedLoop-0364, cl-dClosedLoop-0365,
  cl-dClosedLoop-0366, cl-dClosedLoop-0367, cl-dClosedLoop-0368)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.test.attribute, item.test.exit, item.test.flakes, item.test.merge, item.test.route, item.test.seed, item.test.seen-red, item.test.select, item.test.verdict, policy-key.hooks.bypass, policy-key.retrofit.unseeded, policy-key.retrofit.widen,
  policy-key.tests.landing-levels, policy-key.tests.product, policy-key.tests.without-cadence, policy-key.trace.leg-output, policy-key.verdict, policy-key.verdict.blocks, policy-key.verdict.flakes, policy-key.verdict.flakes.entry, policy-key.verdict.flakes.release, policy-key.verdict.held,
  policy-key.verdict.red-route, policy-key.verdict.remote.pin, policy-key.verdict.remote.pin-scope, policy-key.verdict.remote.trust, policy-key.verdict.tree, record-kind.attribution, record-kind.flake, record-kind.routing, record-kind.seen-red, record-kind.selection, record-kind.verdict,
  system.retrofit, tag-namespace.check, tag-namespace.leg, tag-namespace.pack
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0340, cl-dClosedLoop-0341, cl-dClosedLoop-0342, cl-dClosedLoop-0343, cl-dClosedLoop-0348, cl-dClosedLoop-0349, cl-dClosedLoop-0354, cl-dClosedLoop-0355, cl-dClosedLoop-0356, cl-dClosedLoop-0358, cl-dClosedLoop-0359, cl-dClosedLoop-0367
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md)
- **Child builds:** [dBoundRoles](../dBoundRoles/README.md), [dMindYourWords](../dMindYourWords/README.md), [dScopedBuild](../dScopedBuild/README.md), [dShippedRelease](../dShippedRelease/README.md), [dTendedCadence](../dTendedCadence/README.md), [dTotalRecall](../dTotalRecall/README.md)
<!-- /gen:build-edges -->
