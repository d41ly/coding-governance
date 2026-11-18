# TOOL-dDeclaredLoop-21 deviation 217 — TOOL-dDeclaredLoop-21's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-21

- **Departs from:** `TOOL-dDeclaredLoop-21@rev-7`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-21`'s spec as the revision at `TOOL-dDeclaredLoop-21@rev-7` reads it.
- **After:** the spec at rev-8: §8 F8 (a): the landed step's program stays byte-identical and the shared module has one caller; §8 F9 (a): the driver and check-unattended read four default constants with a NOTE where the module or policy kit does not resolve; §8 F10: only verb_review reads the bounds; §5 carries a sweep of every caller, fixture and contract the change reaches.
- **Cause:** builder discovery
- **Reason:** rev-7 edited a landed step's frozen program and named no reading where the module or policy kit is absent, which about 46 suite calls run.
- **Evidence:** `memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-21-4-builder-return.md`, and the rev-8 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-16-build-TOOL-dDeclaredLoop-21-4-builder-return
