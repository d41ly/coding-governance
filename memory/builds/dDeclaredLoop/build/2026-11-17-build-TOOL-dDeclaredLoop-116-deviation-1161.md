# TOOL-dDeclaredLoop-116 deviation 1161 — the closing diff review promoted a unit for its second high

**Serves:** deviation TOOL-dDeclaredLoop-116

- **Departs from:** dDeclaredLoop [roster]
- **Hand-off:** design-to-spec
- **Before:** dDeclaredLoop's roster carries the units its README listed when the build reached its close, every one CLOSED but `TOOL-dDeclaredLoop-34`, which is deferred against ask `TOOL-dDeclaredLoop-113`.
- **After:** the roster also carries `TOOL-dDeclaredLoop-116`: every loop reader of the builds root takes it from resolve_memory_root, the five readers round 1 named included.
- **Cause:** review finding
- **Reason:** the build method's diff-exit rule, owner ruling of 2026-10-04, promotes every finding the closing diff review confirms at its exit, a HIGH to a unit whose mechanism closes it; this unit closes round 1's item 2. This is a build run, so the unit is specced and built in this run before the close.
- **Evidence:** the closing diff review, `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md` and `memory/builds/dDeclaredLoop/reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md`; the rescope add row for `TOOL-dDeclaredLoop-116` in `memory/builds/dDeclaredLoop/RUN.md`; the unit's spec, `memory/builds/dDeclaredLoop/spec/2026-11-17-spec-TOOL-dDeclaredLoop-116.md`.
- **Risk:** additive
- **Approver:** author, the main loop of the unattended run under the build README's mandate
- **Follow-through:** new unit TOOL-dDeclaredLoop-116
- **Caused-by:** PLAY-dClosedLoop-2
