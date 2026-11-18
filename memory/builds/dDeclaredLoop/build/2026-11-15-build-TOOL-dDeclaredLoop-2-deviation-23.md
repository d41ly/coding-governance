# TOOL-dDeclaredLoop-2 deviation 23 — TOOL-dDeclaredLoop-2's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-2

- **Departs from:** `TOOL-dDeclaredLoop-2@rev-4`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-2`'s spec as the revision at `TOOL-dDeclaredLoop-2@rev-4` reads it.
- **After:** the spec at rev-5: the live-run admission holds under every guard value (F8) and precedes guard-self on a live run's branch, so a run may change the guard, proof and floor keys and the guarded paths list with a change record (F9 (b)), the harness arm denies the policy file only (F10), the push arm skips an adding commit (F11), the policy kit is reached through read_policy_kit, and the point names read point.instruction.
- **Cause:** owner ruling
- **Reason:** the owner's 2026-11-12 ruling that no file is owner-only to a run, landed by PLAY-dOrderedCharter-84 after this spec was written, made rev-4's owner-only default and its guard-self order contradict the code and the ruling at HEAD.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-2-f9-brief.md`, and the rev-5 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-2-f9-brief
