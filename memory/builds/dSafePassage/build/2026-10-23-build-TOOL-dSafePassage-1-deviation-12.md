# TOOL-dSafePassage-1 deviation 12 — the minimal guard admits one value-preserving step write

**Serves:** deviation TOOL-dSafePassage-1

- **Departs from:** `cl-dClosedLoop-0012@937c308e` [the admitted write shape]
- **Hand-off:** design-to-spec
- **Before:** the minimal guard refusing agent writes to the policy file, the minimal guard admitting one agent write shape meanwhile, a single measured-file cap under `budgets.*` raised, nothing else changed, with its change record attached
- **After:** the minimal guard refusing agent writes to the policy file, the minimal guard admitting one agent write shape meanwhile, a single measured-file cap under `budgets.*` raised, nothing else changed, with its change record attached, and, only where the landed guard refuses it, a second shape: the write a declared upgrade step makes when run on gov's own tree, admitted only when every `budgets.*` value reads the same through the policy reader after the write as before it
- **Cause:** design defect
- **Reason:** `cl-dClosedLoop-0018` moves every row of `template-size-limits.txt` into `budgets.*` by a step, and gov is the first tree every step migrates, so the step writes gov's policy file in one commit that raises no cap and moves no value. The guard's one admitted shape is a single raise, so it can refuse that write while admitting a riskier one. The second shape admits nothing a cap reader can see. The build run re-grounds against the landed guard first and makes this change only where the guard refuses the step's write.
- **Evidence:** TOOL-dSafePassage-1 §8 F8, S7 and S8; v2's `[policies]` row for `budgets.*` (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1346`), "`template-size-limits.txt` moved by dSafePassage's step"
- **Risk:** loosening
- **Approver:** author, TOOL-dSafePassage-1 §8 F8, under the chain's `author-recorded` value
- **Follow-through:** amends cl-dClosedLoop-0012@937c308e
- **Caused-by:** TOOL-dSafePassage-1
- **Surface:** the minimal guard's admitted agent-write shapes for `.governance/policy.toml`, widened by one value-preserving step write, only where the landed guard refuses it, rung 5 (ER:388)
