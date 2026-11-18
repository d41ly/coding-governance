# TOOL-dDeclaredLoop-85 deviation 853 — TOOL-dDeclaredLoop-85's spec revised before its build

**Serves:** deviation TOOL-dDeclaredLoop-85

- **Departs from:** `TOOL-dDeclaredLoop-85@rev-4`
- **Hand-off:** spec-revised
- **Before:** `TOOL-dDeclaredLoop-85`'s spec as the revision at `TOOL-dDeclaredLoop-85@rev-4` reads it.
- **After:** the spec at rev-5: a probe that cannot start reads probe failed, a failed probe prints 81's every-parent line, the probe memo is a cleared functools.cache, the plants grade in-process, one build_failure_detail spells the detail (F3), and rev-4's rewrite of 81's spec leaves scope.
- **Cause:** design defect
- **Reason:** the spec predated 81 rev-5, which builds the probe and run_merge_tree before this unit, and the self-test that runs every plant in one process.
- **Evidence:** `memory/builds/dDeclaredLoop/prompts/2026-11-15-prompt-TOOL-dDeclaredLoop-85-reground-brief.md`, and the rev-5 line in this spec's §9.
- **Risk:** editorial
- **Approver:** spec writer, the gov-spec-writer handoff of this revision, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`); the fork picks are the run's under its mandate
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** 2026-11-15-prompt-TOOL-dDeclaredLoop-85-reground-brief
