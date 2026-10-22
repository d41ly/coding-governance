# TOOL-dTrueNorth-27 deviation 29 — the driver's refusal ceiling rises 319 -> 323, the census dTrueNorth's dispatch refusals made

**Serves:** deviation TOOL-dTrueNorth-27

- **Departs from:** dTrueNorth [REFUSAL_CEILINGS]
- **Hand-off:** design-to-spec
- **Before:** `.memory-tree.conf` budgets `tools/unattended/unattended.sh` at 319 fail branches and refusal sites under decision TOOL-aSweptBar-6, and dTrueNorth's units 16, 20 and 26 added four code-49 refusals to `--dispatch`, a census of 323.
- **After:** the driver's `REFUSAL_CEILINGS` token reads 323, dated 2026-10-22 under decision TOOL-dTrueNorth-28, after a retirement review of the four sites found no candidate, each failing R3.
- **Cause:** builder discovery
- **Reason:** The plain merge bar at f4b9849c9 reds `harness arms` on the census. Each of the four refusals guards a dispatch condition that no other refusal reads at the dispatch, so none retires, and the ceiling token is a governance-carrier change no dTrueNorth clause names, so the fork was settled at rung 5 by the standing ruling.
- **Evidence:** `memory/builds/dTrueNorth/build/2026-10-22-build-TOOL-dTrueNorth-27-bar1.log`; TOOL-dTrueNorth-27 §4, its retirement review, and §8 F4; the decision row `TOOL-dTrueNorth-28`; the standing ruling ER:388 (`memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:914-922`), decision row `PLAY-dClosedLoop-6`
- **Risk:** loosening
- **Approver:** author, the run's main loop, under the chain's `author-recorded` value, citing ER:388 (`PLAY-dClosedLoop-6`)
- **Follow-through:** new unit TOOL-dTrueNorth-27
- **Caused-by:** PLAY-dClosedLoop-6
- **Surface:** REFUSAL_CEILINGS in .memory-tree.conf, its token for tools/unattended/unattended.sh
