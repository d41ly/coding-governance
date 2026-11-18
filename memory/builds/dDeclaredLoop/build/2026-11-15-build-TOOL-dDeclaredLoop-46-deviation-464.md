# TOOL-dDeclaredLoop-46 deviation 464 — TOOL-dDeclaredLoop-46's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-46

- **Departs from:** `TOOL-dDeclaredLoop-46@rev-4`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-46`'s spec as the revision at `TOOL-dDeclaredLoop-46@rev-4` reads it.
- **After:** the spec at rev-5: the version is one above the higher of the branch's and origin/main's values, the floor is that tuple, AC5 compares the floor with origin/main's runner and canary at the close and on the landing's reconciled tree, and the reconcile raises the floor where origin/main has reached it (F5).
- **Cause:** builder discovery
- **Reason:** origin/main already ships run-gates 1.48 with no stage admission, so rev-4's S1 would have minted a shipped version.
- **Evidence:** `memory/builds/dDeclaredLoop/build/2026-11-15-build-TOOL-dDeclaredLoop-46-1-builder-return.md`, and the rev-5 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-build-TOOL-dDeclaredLoop-46-1-builder-return
