# aPrimedIndex — asks

## Asks
- TOOL-aPrimedIndex-5 · filed 2026-10-11 · the held lander self-test's arm 26 expects the attended mint subject to end in the fixture's unit id, but since TOOL-aRoutedQuill-12 the newest-unit reader names only an id that a spec at HEAD defines, and the arm's clone defines no `tFix` spec; the arm reds the same way at this build's base and after it, so the red is inherited and the arm cannot fail on the subject it was written to pin · seen `tools/push-main.test.sh`@77c7a903:705 · accept arm 26 passes in a run of `push-main.test.sh` whose fixture defines, as a spec at HEAD, the unit the mint commit names
- TOOL-aPrimedIndex-11 · filed 2026-10-12 · held red: suite push-main self-test red at 9b743831 on the daily held job, run 38133597959 · seen `{prefix}/push-main.test.sh`@9b743831 run `bash {prefix}/push-main.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aPrimedIndex-12 · filed 2026-10-12 · held red: suite pre-push self-test red at 9b743831 on the daily held job, run 38133597959 · seen `.githooks/pre-push.test.sh`@9b743831 run `bash .githooks/pre-push.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aPrimedIndex-13 · filed 2026-10-12 · held red: suite memory-hygiene self-test red at 9b743831 on the daily held job, run 38133597959 · seen `{prefix}/memory-tree/check-memory-hygiene.test.sh`@9b743831 run `bash {prefix}/memory-tree/check-memory-hygiene.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aPrimedIndex-14 · filed 2026-10-12 · held red: suite unattended driver selftest shard 5/8 red at 9b743831 on the daily held job, run 38133597959 · seen `.github/workflows/remote-ci.yml`@9b743831 · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aPrimedIndex-15 · filed 2026-10-12 · held red: suite unattended driver selftest shard 7/8 red at 9b743831 on the daily held job, run 38133597959 · seen `.github/workflows/remote-ci.yml`@9b743831 · accept the suite is green on the daily held job at the default branch's tip

## Dispositions
- SEV · TOOL-aPrimedIndex-5 · LOW · a held self-test's stale fixture; no shipped path is wrong and no bar leg runs the arm
- CLOSED · TOOL-aPrimedIndex-5 · by 4827b2073 · arms 26 and 29 commit a spec defining the unit their commits name, so the newest-unit reader answers and arm 26 passes; adopted by TOOL-aPrimedIndex-8
- SEV · TOOL-aPrimedIndex-11 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPrimedIndex-11 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-aPrimedIndex-12 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPrimedIndex-12 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-aPrimedIndex-13 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPrimedIndex-13 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-aPrimedIndex-14 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPrimedIndex-14 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-aPrimedIndex-15 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-aPrimedIndex-15 · filed by an unattended run for the owning build; outside this build's goal
