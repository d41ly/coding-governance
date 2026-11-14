# TOOL-dDeclaredLoop-17 deviation 172 — TOOL-dDeclaredLoop-17's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-17

- **Departs from:** `TOOL-dDeclaredLoop-17@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-17`'s spec as the revision at `TOOL-dDeclaredLoop-17@rev-3` reads it.
- **After:** the spec at rev-4: the attest door leaves scope as already built (F7), the hold state writes the staged gate set (new S6), acceptance run lines go through a lines argument on write_record (F5) with the kind's rules in build_records.py (F6), computed-witness rows live in loop_lib.py with their class derived from the item they serve (F8), and the hold join is observed by a loop_witness.py plant (F9).
- **Cause:** design defect
- **Reason:** the spec predated units 5, 12, 41 and 9, so its attest door, record fields, witness rows and the park policy's hold path no longer matched the code at HEAD.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-17-reground-brief.md`, and the rev-4 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-14-prompt-TOOL-dDeclaredLoop-17-reground-brief
