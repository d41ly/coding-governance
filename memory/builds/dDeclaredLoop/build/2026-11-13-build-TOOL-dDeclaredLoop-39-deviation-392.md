# TOOL-dDeclaredLoop-39 deviation 392 — TOOL-dDeclaredLoop-39's spec re-grounded on the code as built

**Serves:** deviation TOOL-dDeclaredLoop-39

- **Departs from:** `TOOL-dDeclaredLoop-39@rev-1`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-39`'s spec as the revision at `TOOL-dDeclaredLoop-39@rev-1` reads it.
- **After:** the spec at rev-2: the reader's default runner is pinned in place, the gated leak list is reused, the shell stopgap unit 23 left is removed, and §8 F2 to F5 are resolved to A.
- **Cause:** design defect
- **Reason:** the spec predates unit 23's build: Python consumers already pass a pinned runner, so the open gap is the reader's default runner, and the runlog copy does not exist.
- **Evidence:** the re-ground brief `memory/builds/dDeclaredLoop/prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-39-reground-brief.md`, and the rev-2 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-13-prompt-TOOL-dDeclaredLoop-39-reground-brief
