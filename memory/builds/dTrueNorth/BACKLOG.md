# dTrueNorth — asks

## Asks

- TOOL-dTrueNorth-21 · filed 2026-10-21 · TWO LIVE SPECS OF dPinnedHandoff OMIT TWO LEGS THEIR FILES TRIP. Since TOOL-dTrueNorth-11 the guards of `build-index selftest` and `memory-hygiene self-test` name `tools/check-spec-tokens.py`, which `TOOL-dPinnedHandoff-2` and `TOOL-dPinnedHandoff-3` list in their files touched; `-2`'s §7 names neither leg and `-3`'s lacks `build-index selftest`. Two rows in `memory/project/spec-token-waivers.txt` hold the three hits meanwhile. · accept both specs' §7 leg lines name the legs, and the two waiver rows are deleted in the same commit
- TOOL-dTrueNorth-22 · filed 2026-10-22 · A LIVE SPEC OF aOrientedCast OMITS A LEG ITS FILES TRIP. Since TOOL-dTrueNorth-12 the guard of `routed-commits selftest` names `{prefix}/unattended/lib-unattended.sh`, and `TOOL-aOrientedCast-28` lists `tools/unattended/` in its files touched without naming that leg in its §7. One row in `memory/project/spec-token-waivers.txt` holds the hit meanwhile. · accept that spec's §7 leg line names `routed-commits selftest`, and the waiver row is deleted in the same commit
- TOOL-dTrueNorth-100 · filed 2026-10-22 · held red: suite build-index selftest red at 271aa59d on the daily held job, run 39755797862 · seen `{prefix}/memory-tree/gen_build_index.py`@271aa59d run `python3 {prefix}/memory-tree/gen_build_index.py --selftest` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dTrueNorth-101 · filed 2026-10-22 · held red: suite measure-legs selftest red at 271aa59d on the daily held job, run 39755797862 · seen `{prefix}/run-gates/measure_legs.py`@271aa59d run `python3 {prefix}/run-gates/measure_legs.py --selftest` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dTrueNorth-102 · filed 2026-10-22 · held red: suite branch-reconcile selftest red at 271aa59d on the daily held job, run 39755797862 · seen `{prefix}/branch-reconcile/selftest.py`@271aa59d run `python {prefix}/branch-reconcile/selftest.py` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dTrueNorth-103 · filed 2026-10-22 · held red: suite spec-tokens self-test red at 271aa59d on the daily held job, run 39755797862 · seen `{prefix}/check-spec-tokens.test.sh`@271aa59d run `bash {prefix}/check-spec-tokens.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dTrueNorth-104 · filed 2026-10-22 · held red: suite unattended driver selftest shard 3/8 red at 271aa59d on the daily held job, run 39755797862 · seen `.github/workflows/remote-ci.yml`@271aa59d · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dTrueNorth-105 · filed 2026-10-22 · held red: suite unattended gate-guard selftest red at 271aa59d on the daily held job, run 39755797862 · seen `.github/workflows/remote-ci.yml`@271aa59d · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dTrueNorth-106 · filed 2026-10-22 · held red: suite unattended driver selftest shard 1/8 red at 271aa59d on the daily held job, run 39755797862 · seen `.github/workflows/remote-ci.yml`@271aa59d · accept the suite is green on the daily held job at the default branch's tip

## Dispositions

- SEV · TOOL-dTrueNorth-21 · LOW · two waiver rows hold three guards-join hits on another build's live specs; no verdict moves
- DEFERRED · TOOL-dTrueNorth-21 · until TOOL-dPinnedHandoff-2 · filed 2026-10-21; the cure is a revision of that build's own specs, outside this build's writes (README rule 7)
- SEV · TOOL-dTrueNorth-22 · LOW · one waiver row holds one guards-join hit on another build's live spec; no verdict moves
- DEFERRED · TOOL-dTrueNorth-22 · until TOOL-aOrientedCast-28 · filed 2026-10-22; the cure is a revision of that build's own spec, outside this build's writes (README rule 7)
- SEV · TOOL-dTrueNorth-100 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dTrueNorth-100 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dTrueNorth-101 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dTrueNorth-101 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dTrueNorth-102 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dTrueNorth-102 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dTrueNorth-103 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dTrueNorth-103 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dTrueNorth-104 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dTrueNorth-104 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dTrueNorth-105 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dTrueNorth-105 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dTrueNorth-106 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dTrueNorth-106 · filed by an unattended run for the owning build; outside this build's goal
