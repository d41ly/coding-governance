# dCalibratedLens — asks

## Asks

- TOOL-dCalibratedLens-18 · filed 2026-10-21 · build every roster unit of this build from its spec, filed by the opening so the spec run closes by carry-forward with each unit's spec header advancing this ask (README rule 1) · accept every unit of the README's `roster:units` pair is built from its spec and CLOSED, the last one's header carrying `closes` for this ask
- TOOL-dCalibratedLens-49 · filed 2026-11-03 · held red: suite line-length gate selftest red at 84acebdc on the daily held job, run 41446344406 · seen `{prefix}/check-line-length.test.sh`@84acebdc run `bash {prefix}/check-line-length.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dCalibratedLens-50 · filed 2026-11-03 · held red: suite memory-recall kit selftest red at 84acebdc on the daily held job, run 41446344406 · seen `{prefix}/memory-recall/selftest.py`@84acebdc run `python3 {prefix}/memory-recall/selftest.py` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dCalibratedLens-51 · filed 2026-11-03 · held red: suite manifest-check self-test red at 84acebdc on the daily held job, run 41446344406 · seen `skills/session-kickoff/manifest-check.test.sh`@84acebdc run `bash skills/session-kickoff/manifest-check.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dCalibratedLens-52 · filed 2026-11-03 · held red: suite upgrade-walk red at 84acebdc on the daily held job, run 41446344406 · seen `{prefix}/govkit/upgrade_walk.py`@84acebdc run `python {prefix}/govkit/upgrade_walk.py` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dCalibratedLens-53 · filed 2026-11-03 · CHECK 24 READS A SPEC TITLE'S FOREIGN ID AS A ROSTER UNIT. The unattended kit gate's check 24 ADD arm (`tools/unattended/check-unattended.sh`) collects every `[A-Z]+-[A-Za-z0-9]+-[0-9]+` token in the build README's generated units table, so a spec whose H1 quotes another build's unit id (dCalibratedLens units 32 and 42 named two dTotalRecall units) reads that unit as one added to the run's roster with no rescope row; the dCalibratedLens close's bar went red on it, OWN, and the titles were reworded to land · accept check 24 reads the units table's unit-id column alone, seen green on a planted spec title quoting another build's unit id and red on a planted roster unit added with no rescope row
- TOOL-dCalibratedLens-54 · filed 2026-11-03 · held red: suite unattended driver selftest shard 4/8 red at 2c50ab31 on the daily held job, run 41632620578 · seen `.github/workflows/remote-ci.yml`@2c50ab31 · accept the suite is green on the daily held job at the default branch's tip
- TOOL-dCalibratedLens-55 · filed 2026-11-03 · held red: suite unattended runlog-writer selftest red at 2c50ab31 on the daily held job, run 41632620578 · seen `.github/workflows/remote-ci.yml`@2c50ab31 · accept the suite is green on the daily held job at the default branch's tip

## Dispositions

- SEV · TOOL-dCalibratedLens-18 · MED · the build's units stay unbuilt and its owned gaps open
- SEV · TOOL-dCalibratedLens-49 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dCalibratedLens-49 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dCalibratedLens-50 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dCalibratedLens-50 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dCalibratedLens-51 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dCalibratedLens-51 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dCalibratedLens-52 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dCalibratedLens-52 · filed by an unattended run for the owning build; outside this build's goal
- DEFERRED · TOOL-dCalibratedLens-18 · until TOOL-dCalibratedLens-48 · the spec run carries every unit forward DEFERRED against this ask, each spec header advancing it; the build run builds them, and its last unit in build order, TOOL-dCalibratedLens-48 at order 21 today, closes it (README rule 1)
- SEV · TOOL-dCalibratedLens-53 · MED · a spec title naming another build's unit reds the close of a build that adds no unit
- KEEP · TOOL-dCalibratedLens-53 · a gate defect in the unattended kit, outside this build's goal; filed for the kit's next build
- SEV · TOOL-dCalibratedLens-54 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dCalibratedLens-54 · filed by an unattended run for the owning build; outside this build's goal
- SEV · TOOL-dCalibratedLens-55 · HIGH · a held self-test is red on the default branch's daily job
- KEEP · TOOL-dCalibratedLens-55 · filed by an unattended run for the owning build; outside this build's goal
