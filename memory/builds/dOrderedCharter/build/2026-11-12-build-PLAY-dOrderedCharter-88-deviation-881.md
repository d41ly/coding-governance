# PLAY-dOrderedCharter-88 deviation 881 — the join's second caller passes the wildcard too

**Serves:** deviation PLAY-dOrderedCharter-88

- **Departs from:** `PLAY-dOrderedCharter-88@rev-1` [Scope]
- **Hand-off:** spec-to-code
- **Before:** S3 names `run_check` in `tools/playbook/gov_tag.py` as the one caller of `check_namespace_joins`, and S2 gives the new keyword-only `every` no default.
- **After:** the self-test arm `arm_arms` in `tools/playbook/instruction_units.py` calls `check_namespace_joins` too, so it passes `every=EVERY`, the module's own spelling of the wildcard. The parameter keeps no default.
- **Cause:** builder discovery
- **Reason:** with no default, the second call site raises `TypeError` for the missing keyword, so the `arms` plant of the instruction-unit fixture would fail. Passing the wildcard keeps S2's design whole, and that arm grades only the `unit` namespace, where the rule never fires.
- **Evidence:** `git grep -n check_namespace_joins -- tools` lists `tools/playbook/instruction_units.py#arm_arms` beside `tools/playbook/gov_tag.py#run_check`; after the edit, `instruction_units.py fixture --plant arms` exited 0 with `fixture · green · 0 expectation(s) failed` (PINNED, that plant run in this pass).
- **Risk:** editorial
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-88
