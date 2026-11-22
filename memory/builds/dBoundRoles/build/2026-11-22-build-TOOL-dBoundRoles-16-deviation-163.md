# TOOL-dBoundRoles-16 deviation 163 — R9 names a role's missing kind once, with every stage, and the builder's additions the spec did not state

**Serves:** deviation TOOL-dBoundRoles-16

- **Departs from:** `TOOL-dBoundRoles-16@rev-7` [S5, §4 Inventory]
- **Hand-off:** spec-to-code
- **Before:** S5 says R9 reds a stage whose role does not declare the stage's kind, and AC4 asks one R9 line naming the stage and the kind; §4 Inventory mints `load_workflow_kinds` and `derive_stage_rows` and no other function.
- **After:** `tools/roles/check_roles.py#check_roles` prints one R9 line per role and kind its `shapes` lacks, on the role file, naming every stage run in that kind (gov-builder at `single` names `spec-write.builder` and `build.builder` on one line); the kinds are `tools/roles/roles_lib.py#WORKFLOW_KINDS`, graded both ways against the `[[kind]]` rows; `tools/roles/roles_lib.py#load_workflow_table` is the one parse `load_workflows` and `load_workflow_kinds` share, and `load_workflow_kinds` raises on a repeated or non-string kind; `tools/roles/roles_lib.py#parse_role_shapes` is the one split R2, R9 and the role index read; `tools/roles/check_roles.py#read_unit_tags`, `#read_scorer_instances`, `#check_tracked_path` and `#check_experiment_table` carry the unit join, the scorer join and the experiment rules; R9 also refuses `of` on a non-twin entry and a `fan` or `cap` on the `experiment` kind row; `experiment` joins `WORKFLOW_KEYS`, so the README's Workflows table gains a column per new key.
- **Cause:** builder discovery
- **Reason:** a role missing a kind it runs in under two workflows is one declaration to fix, so one line per stage would print the same fix twice and break AC4's one line wherever the role runs the kind in a second entry (the main loop's M3 resolution, choice 2 of the build brief); the five names are closed in code because `twin` and `experiment` carry fields of their own R9 grades by the kind's name, and grading them both ways keeps the rows and the names one fact; each helper is a read or a rule the spec states, given a name the lexicon admits (`python tools/lexicon/lexicon.py --suggest <name> --as py.function` printed OK for each); and the catalogue region renders every `WORKFLOW_KEYS` key, so a new key is a new column by derivation.
- **Evidence:** the build brief `2026-11-22-prompt-TOOL-dBoundRoles-16-build-brief`, its four decided choices; at the pass's base `d173e8ced` gov-builder runs per-unit in the `spec-write` and `build` entries' `builder` rows (DERIVED from the builder's read of `tools/roles/workflows.toml`).
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** ask TOOL-dBoundRoles-27
- **Caused-by:** TOOL-dBoundRoles-16
