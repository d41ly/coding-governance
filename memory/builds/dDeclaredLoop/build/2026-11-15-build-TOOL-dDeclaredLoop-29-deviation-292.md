# TOOL-dDeclaredLoop-29 deviation 292 — TOOL-dDeclaredLoop-29's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-29

- **Departs from:** `TOOL-dDeclaredLoop-29@rev-3`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-29`'s spec as the revision at `TOOL-dDeclaredLoop-29@rev-3` reads it.
- **After:** the spec at rev-4: the checks live in check_upstream_rows called from loop_items.py's run_check (F5), the verbs read the composed items through an extracted read_composed_items (F6), each finding grades on its edge's gate (F7), and the join is check_upstream_answers (F8).
- **Cause:** design defect
- **Reason:** load_loop reads no item rows, position.py copied the composed-item read twice, and the lexicon refuses join_upstream.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-29-reground-brief.md`, and the rev-4 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-29-reground-brief
