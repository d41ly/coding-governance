# TOOL-dDeclaredLoop-4 deviation 43 — TOOL-dDeclaredLoop-4's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-4

- **Departs from:** `TOOL-dDeclaredLoop-4@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-4`'s spec as the revision at `TOOL-dDeclaredLoop-4@rev-3` reads it.
- **After:** the spec at rev-4: claims resolve against read_steps, a stage's witness is read through the definition's own readers (F5), this pass admits stage to the canary's KNOWN copies (F6), the leg is gov's own exempt_leg row (F7), and the counts are re-pinned.
- **Cause:** design defect
- **Reason:** the spec predated units 5, 9, 15 and 25's landed code: check_loop admits only the five gov steps, check_witness_classes already refuses an unwitnessed step, and the canary rejects a manifest key outside its KNOWN lists.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-4-reground-brief.md`, and the rev-4 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-4-reground-brief
