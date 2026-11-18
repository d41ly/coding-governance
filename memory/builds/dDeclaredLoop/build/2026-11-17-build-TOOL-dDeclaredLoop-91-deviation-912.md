# TOOL-dDeclaredLoop-91 deviation 912 — the plant's description names the module-scope group, the README row names the table, and the sweep's citation count reads its own line

**Serves:** deviation TOOL-dDeclaredLoop-91

- **Departs from:** `TOOL-dDeclaredLoop-91@rev-4` [§2, §5]
- **Hand-off:** spec-to-code
- **Before:** S3 adds the module-scope group of rows to the `conf-read-forms` branch of `tools/loop/budget.py#run_budget_plant` and states no edit of that plant's `PLANTS` description; S5 has the `derive_conf_rebinds(tree, docs)` row of `tools/loop/README.md` say a class is a loader and name the decorator, default and class-base positions; the sweep's citation grep is annotated as matching 2 PINNED `91 AC3`, 1 PINNED `91 S1` and 2 PINNED `91 S5` citations, all in the spec of `TOOL-dDeclaredLoop-94`.
- **After:** the `PLANTS` description of `conf-read-forms` names the new rows in words, a global in a class body and a walrus in a default, a keyword-only default, a lambda default, a class base and a decorator, the two body walruses binding none, and the execution comparison, naming each conf in words and never by its file name, as unit 90 extended the same description for its rows; the README row also names `_MODULE_SCOPE_PARTS` as the table the walk reads; the citation grep run at the base matched one more of each citation, every extra one in the annotation line of this spec's own sweep, while the spec of `TOOL-dDeclaredLoop-94` holds exactly the counts the annotation states.
- **Cause:** builder discovery
- **Reason:** a description that lists every row of its plant but the new group would state the plant short of its code, and the table is where a reader of the row finds the positions; the grep's extra matches are the annotation reading itself, no citation moved. No design claim moved.
- **Evidence:** `tools/loop/budget.py#PLANTS`, the `derive_conf_rebinds(tree, docs)` row of `tools/loop/README.md`, and the sweep's citation grep run at the base `2a95c3eb9`.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dDeclaredLoop-35
- **Caused-by:** PLAY-dClosedLoop-2
