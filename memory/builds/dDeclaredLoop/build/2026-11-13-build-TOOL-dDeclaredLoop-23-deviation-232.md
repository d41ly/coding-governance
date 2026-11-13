# TOOL-dDeclaredLoop-23 deviation 232 — TOOL-dDeclaredLoop-23's spec re-grounded on the code as built

**Serves:** deviation TOOL-dDeclaredLoop-23

- **Departs from:** `TOOL-dDeclaredLoop-23@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-23`'s spec as the revision at `TOOL-dDeclaredLoop-23@rev-2` reads it.
- **After:** the spec at rev-3: the trailer rows, the commit class's resolver and the routed-commits reader are re-grounded on the landed edge grammar, and §8 F5 to F9 are resolved.
- **Cause:** design defect
- **Reason:** the spec predates the parents' build: the landed adapter refuses a typeless trailer row, the native-class reader takes a different resolver form, and two legs carry no interpreter.
- **Evidence:** the re-ground brief `memory/builds/dDeclaredLoop/prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-23-reground-brief.md`, and the rev-3 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-13-prompt-TOOL-dDeclaredLoop-23-reground-brief
