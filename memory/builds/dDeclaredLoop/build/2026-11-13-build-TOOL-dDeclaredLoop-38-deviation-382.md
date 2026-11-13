# TOOL-dDeclaredLoop-38 deviation 382 — TOOL-dDeclaredLoop-38's spec re-grounded on the code as built

**Serves:** deviation TOOL-dDeclaredLoop-38

- **Departs from:** `TOOL-dDeclaredLoop-38@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-38`'s spec as the revision at `TOOL-dDeclaredLoop-38@rev-2` reads it.
- **After:** the spec at rev-3: the unit's scope is the trailer CLI's LF-only output alone; the wrapper's CR drop, already built with unit 23, leaves it, and §8 F2 is resolved to (b).
- **Cause:** re-ground before dispatch
- **Reason:** the spec predates unit 23's build, which already drops the CR in the shell wrapper and moved the runlog re-point to unit 56.
- **Evidence:** the re-ground brief `memory/builds/dDeclaredLoop/prompts/2026-11-13-prompt-TOOL-dDeclaredLoop-38-reground-brief.md`, and the rev-3 line in this spec's §9.
- **Risk:** editorial
- **Approver:** the run, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** none
- **Caused-by:** 2026-11-13-prompt-TOOL-dDeclaredLoop-38-reground-brief
