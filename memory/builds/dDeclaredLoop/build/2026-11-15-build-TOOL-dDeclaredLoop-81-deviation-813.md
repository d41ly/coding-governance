# TOOL-dDeclaredLoop-81 deviation 813 — TOOL-dDeclaredLoop-81's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-81

- **Departs from:** `TOOL-dDeclaredLoop-81@rev-4`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-81`'s spec as the revision at `TOOL-dDeclaredLoop-81@rev-4` reads it.
- **After:** the spec at rev-5: run_merge_tree reads merge-tree's stderr through subprocess.run, S2 names conflicted and failed, the plants grade in-process with review.max-rounds, a failed merge reads one informational line plus the per-key findings (F3), and one plant carries both unrelated-history scenarios (F4).
- **Cause:** design defect
- **Reason:** the spec predated unit 59's read_remerge_policy and the push arm's diff-tree pre-filter, and its plants graded in a subprocess a stand-in cannot reach.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-81-reground-brief.md`, and the rev-5 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-81-reground-brief
