# TOOL-dDeclaredLoop-42 deviation 422 — TOOL-dDeclaredLoop-42's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-42

- **Departs from:** `TOOL-dDeclaredLoop-42@rev-2`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-42`'s spec as the revision at `TOOL-dDeclaredLoop-42@rev-2` reads it.
- **After:** the spec at rev-3: the plants are spelled --fixture --plant as unit 17 built them, resolve_bash is already inline so S1 only calls it, teardown already never raises so S5 keeps only the leak line, the tree kill is one canonical in tools/lib/run_tree_kill.py copied into both kits under a parity row (F2), a leak is one stderr line (F3), and S7 updates the loop docs.
- **Cause:** design defect
- **Reason:** the spec predated unit 17's loop_witness.py and the run-gates kit's tree kill, so its command spelling, its teardown and its kill placement no longer matched the code at HEAD.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-14-prompt-TOOL-dDeclaredLoop-42-reground-brief.md`, and the rev-3 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-14-prompt-TOOL-dDeclaredLoop-42-reground-brief
