# TOOL-dDeclaredLoop-40 deviation 403 — TOOL-dDeclaredLoop-40's spec re-grounded on the code as built

**Serves:** deviation TOOL-dDeclaredLoop-40

- **Departs from:** `TOOL-dDeclaredLoop-40@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-40`'s spec as the revision at `TOOL-dDeclaredLoop-40@rev-2` reads it.
- **After:** the spec at rev-3: the lookup unit 23 already built leaves the scope, the floor sits in the key-table reader and carries Red-fix, and §8 F3 and F4 are resolved to (b).
- **Cause:** design defect
- **Reason:** the spec predates unit 23's build, which resolves the key table through the kit resolver and holds two copies of the reader, not four.
- **Evidence:** the re-ground brief `memory/builds/dDeclaredLoop/prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-40-reground-brief.md`, and the rev-3 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-13-prompt-TOOL-dDeclaredLoop-40-reground-brief
