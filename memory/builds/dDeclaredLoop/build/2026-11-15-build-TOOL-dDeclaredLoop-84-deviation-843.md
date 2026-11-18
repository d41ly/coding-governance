# TOOL-dDeclaredLoop-84 deviation 843 — TOOL-dDeclaredLoop-84's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-84

- **Departs from:** `TOOL-dDeclaredLoop-84@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-84`'s spec as the revision at `TOOL-dDeclaredLoop-84@rev-3` reads it.
- **After:** the spec at rev-4: the half that rewrote 78 leaves scope since 78 lands first (F3), S1 is 82's restatement written on 81 rev-5 and 83 rev-4, and S2 gives 82's AC4 the class-level checks (F4).
- **Cause:** design defect
- **Reason:** unit 78 lands at order 19, before this unit, and a landed spec is frozen; 81 rev-5 already states the narrowed exit table.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-84-reground-brief.md`, and the rev-4 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-84-reground-brief
