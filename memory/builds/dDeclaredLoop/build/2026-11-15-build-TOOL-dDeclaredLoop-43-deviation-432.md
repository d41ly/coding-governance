# TOOL-dDeclaredLoop-43 deviation 432 — TOOL-dDeclaredLoop-43's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-43

- **Departs from:** `TOOL-dDeclaredLoop-43@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-43`'s spec as the revision at `TOOL-dDeclaredLoop-43@rev-2` reads it.
- **After:** the spec at rev-3: the restore and the caller's record leave scope as built by unit 2's write_guarded, and the unit writes through an mkstemp temp file beside the target replaced with os.replace (F2), restores the same way, hands a callable the pre-filled temp path, keeps the code inside the guarded_write_py block (F3), and adds a write-guarded-rollback plant.
- **Cause:** design defect
- **Reason:** the spec predated unit 2's tools/lib/guarded_write.py, which already restores the prior bytes, so its two-path design and its read-only-directory fixture no longer matched the code at HEAD.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-43-reground-brief.md`, and the rev-3 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-43-reground-brief
