# TOOL-dSafePassage-10 deviation 167 — `resolve_landing_base` is TOOL-dSafePassage-1's already-extracted ladder renamed, not a second extraction from `cmd_epoch`

**Serves:** deviation TOOL-dSafePassage-10

- **Departs from:** TOOL-dSafePassage-10@rev-4 [§2 S6, §4 "The gate" step 1]
- **Hand-off:** spec-to-code
- **Before:** "The base resolution inside `cmd_epoch` (`tools/govkit/govkit.py:13446-13474`) is extracted into `resolve_landing_base`, which `cmd_epoch` and the gate both call."
- **After:** `cmd_epoch` carries no inline ladder at this branch's HEAD: TOOL-dSafePassage-1 already extracted it as `derive_push_base`. That definition is renamed `resolve_landing_base`, unchanged, and `cmd_epoch` and the step gate call it; `derive_push_base` stays bound to the same function object, so `upgrade_steps.py frozen` keeps calling it by unit 1's name.
- **Cause:** builder discovery
- **Reason:** extracting a second copy would leave govkit two functions for one base rule, the defect the round-1 audit's D-10 names; renaming the one that exists gives S6's state — one definition, called by `cmd_epoch` and the gate — and leaves `cmd_frozen` as TOOL-dSafePassage-35 S35 reads it at this unit's landing, for TOOL-dSafePassage-26 S1 to join.
- **Evidence:** this unit's acceptance ledger, AC10: `git grep -n -e "resolve_landing_base(" -- tools/govkit` prints one definition in `tools/govkit/govkit.py` and the calls in `cmd_epoch` and `tools/govkit/step_gate.py`.
- **Risk:** editorial
- **Approver:** author, the gov-builder pass of TOOL-dSafePassage-10, recorded in this unit's pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dSafePassage-14
- **Caused-by:** TOOL-dSafePassage-1
