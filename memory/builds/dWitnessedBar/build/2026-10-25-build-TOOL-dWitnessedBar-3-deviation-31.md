# TOOL-dWitnessedBar-3 deviation 31 — a DEAD PROBE red blocks under every value of verdict.blocks

**Serves:** deviation TOOL-dWitnessedBar-3

- **Departs from:** `cl-dClosedLoop-0341@0f53eec5` [the classes `verdict.blocks` lets pass]
- **Hand-off:** design-to-spec
- **Before:** attribution decides what blocks, and the bar's labels `MIXED`, `CONTENDED` and `DEAD PROBE` route by `verdict.blocks`, to an ask when they do not block, so a `DEAD PROBE` red passes under a value that does not name it (layer-flow `[settled]`, flow-steps `test.route`)
- **After:** attribution decides what blocks by TOOL-dWitnessedBar-3's block table, under which a `DEAD PROBE` red, and a red the attribution names no class for, blocks under every value of `verdict.blocks`; `MIXED` and `CONTENDED` pass under `own-only` and block under the other two values
- **Cause:** design defect
- **Reason:** A `DEAD PROBE` means the attribution made no comparison, and every red reads it when `lib-attribute.sh` is missing beside the runner, so a value under which it passes lets a red the run caused land unexamined. Blocking it is the charter's deny-by-default, and the only option that survives the security veto (TOOL-dWitnessedBar-3 §8 F1).
- **Evidence:** TOOL-dWitnessedBar-3 §4 "The block table" and §8 F1; `tools/run-gates/run-gates.sh:4939-4940`, where a missing `lib-attribute.sh` reads every red `DEAD PROBE`
- **Risk:** stricter
- **Approver:** spec writer, TOOL-dWitnessedBar-3 §8 F1, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** amends cl-dClosedLoop-0341@0f53eec5
- **Caused-by:** TOOL-dWitnessedBar-3
