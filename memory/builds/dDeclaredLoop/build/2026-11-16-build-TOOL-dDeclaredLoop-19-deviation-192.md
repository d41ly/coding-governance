# TOOL-dDeclaredLoop-19 deviation 192 — the driver suite reaches the module, and the policy read is one revision read

**Serves:** deviation TOOL-dDeclaredLoop-19

- **Departs from:** `TOOL-dDeclaredLoop-19@rev-3` [§5]
- **Hand-off:** spec-to-code
- **Before:** §5's sweep keeps `check_authorization`'s population green because "the driver suite runs a copied driver with no loop kit beside it, which reads `opt-in` and prints nothing new"; §5's perf line says the list "composes the items once at the pin"; S1 reads the policy keys "through the policy kit's `resolve`".
- **After:** the driver suite sources and runs this tree's own driver, whose loop kit resolves beside it, as its `budget.py` arms already show, so the suite's preflights read `breakpoints.py stage`, its closes `breakpoints.py list` and its single-slug plans print the list; each stays green by the first clause of the same rows, the defaults: the suite's policy file sets no `review.design`, so the opt-in reads `opt-in`, and no `autonomy` or `decisions.major`, so the one owner line is the plan gate, released by `authorization`. The seven keys are read over one `read_revision` through the kit's `resolve_read`, each a string literal at its `read_value` call, in place of seven `resolve` calls; the list composes the items twice, once inside `read_tag_policy` and once for the tag order, since `read_tag_policy` returns no tags.
- **Cause:** builder discovery
- **Reason:** the sweep re-run at the base of this pass found the suite's `SCRIPT` is `tools/unattended/unattended.sh` itself, never a copy, and the extracted `read_tag_policy` keeps its own composition read; one revision read keeps the preflight's added cost to one policy read.
- **Evidence:** `tools/unattended/unattended.test.sh#run_driver`, the TOOL-dDeclaredLoop-31 `--exhausted` arm asserting `unfrozen` through this tree's `budget.py`, `tools/loop/composition.py#read_tag_policy`, and `tools/loop/breakpoints.py#read_policy_values`.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the suite's arms read the defaults the rows name, observed at the close's suite run
- **Caused-by:** TOOL-dDeclaredLoop-31
