# TOOL-dDeclaredLoop-67 deviation 673 — the budget module's notice and origin lines open with its own `loop:`, not `budget:`

**Serves:** deviation TOOL-dDeclaredLoop-67

- **Departs from:** `TOOL-dDeclaredLoop-67@rev-4` [§4]
- **Hand-off:** spec-to-code
- **Before:** the spec spells the `draw` verb's merge notice `budget: budget · notice · <record> merges as <answer>, not union: ...` and the `origin` verb's line `budget: budget · origin · <slug|none>`.
- **After:** `tools/loop/budget.py#main` prints both through the module's `SAY`, as every other line it prints: `loop: budget · notice · <record> merges as <answer>, not union: add <root>/builds/*/build/*-transition-*.md merge=union to .gitattributes` and `loop: budget · origin · <slug|none>`. The driver's refusal keeps the spec's `budget: patch draw refused — <slug> on <node> is a live patch run of <origin>`, a line the driver writes and not the module.
- **Cause:** builder discovery
- **Reason:** every line `budget.py` prints opens `loop: budget · `, the prefix the driver's readers of that module match, `read_exhausted_ending` among them; a second prefix on two lines of one verb set would split one module's output across two spellings with no reader asking for it.
- **Evidence:** `python budget.py --fixture --plant attr-missing` printed one `loop: budget · notice · ` line under no `.gitattributes` and none under the union line; `python budget.py origin --build tFixPatch` printed `loop: budget · origin · tFix` in the plant's scratch repository.
- **Risk:** editorial
- **Approver:** author, the builder pass, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** usage — the two lines read with the module's prefix; no spec edit is owed
- **Caused-by:** PLAY-dClosedLoop-2
