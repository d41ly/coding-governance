# TOOL-dDeclaredLoop-25 deviation 254 — TOOL-dDeclaredLoop-25's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-25

- **Departs from:** `TOOL-dDeclaredLoop-25@rev-5`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-25`'s spec as the revision at `TOOL-dDeclaredLoop-25@rev-5` reads it.
- **After:** the spec at rev-6: the gov-rename plant keeps the shipped definition and plants a change record renaming an old tag onto step.test, a stage naming a succeeded tag is resolved before the frame rules read it, and every plant passes the shipped definition (F9 (a)).
- **Cause:** builder discovery
- **Reason:** check_program calls check_loop first and refuses any step tag outside STEP_TAGS, so a plant renaming a gov step could never reach the re-point.
- **Evidence:** `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-25-1-builder-return.md`, and the rev-6 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-build-TOOL-dDeclaredLoop-25-1-builder-return
