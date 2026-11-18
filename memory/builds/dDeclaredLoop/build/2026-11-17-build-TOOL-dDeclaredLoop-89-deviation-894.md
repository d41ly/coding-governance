# TOOL-dDeclaredLoop-89 deviation 894 — the conf-name predicate extracted as a third function

**Serves:** deviation TOOL-dDeclaredLoop-89

- **Departs from:** `TOOL-dDeclaredLoop-89@rev-5` [§4]
- **Hand-off:** spec-to-code
- **Before:** §4's inventory mints two functions, `derive_conf_rebinds` and `load_tree_lib`, while S1 has both passes call the one conf-name predicate the binding walk of `TOOL-dDeclaredLoop-87` applies, never a second spelling of the two conf names.
- **After:** the pass also mints `check_conf_name(node, docs=())` in `tools/loop/loop_lib.py`, True where a node's syntax subtree holds a str constant naming a conf outside the docstring ids; the binding walk of `derive_conf_constants` and both passes of `derive_conf_rebinds` call it. Its verb `check` is declared, checked with the lexicon's suggest verb, and the codebase map gains its row. `derive_conf_reads` keeps its own per-node test, which this unit's scope does not name.
- **Cause:** builder discovery
- **Reason:** at the base the walk of `TOOL-dDeclaredLoop-87` tests the conf names inline in a generator, so no callable predicate existed to call; holding it once in a function is what S1's "called" and the charter's reuse rule ask at its second instance.
- **Evidence:** `tools/loop/loop_lib.py#derive_conf_constants` at the base `7d4a42868`; `tools/loop/loop_lib.py#check_conf_name` in this pass's commit; the AC2 probe recorded in the acceptance ledger.
- **Risk:** additive
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** PLAY-dClosedLoop-2
