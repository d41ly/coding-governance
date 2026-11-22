# TOOL-dBoundRoles-21 deviation 213 — the builder's additions the spec did not state

**Serves:** deviation TOOL-dBoundRoles-21

- **Departs from:** `TOOL-dBoundRoles-21@rev-7 [§4 Inventory, §4 Files touched]`
- **Hand-off:** spec-to-code
- **Before:** §4 Inventory mints `read_policy_setting`, `resolve_role_model`, `HARNESS_MODEL_EQUIVALENT`, `check_gate_names`, `POLICY_DERIVED_LINE` and `ROLE_EFFORT`, and §4 "### The model" writes the resolver as `resolve_role_model(slot, harness, root)`; §4 Files touched names no page under `help/` but the reference page, and neither `tools/hooks/README.md` nor the codebase map.
- **After:** `tools/roles/roles_lib.py#resolve_role_model` takes a fourth, optional `kit_dir`, the role kit whose role file declares the model, this file's own directory unless given, so `tools/roles/render_agents.py#run_mode` passes the kit it renders and the render selftest's fixture kits read their own role files; `tools/roles/roles_lib.py#resolve_house_table` holds the level-table pick `resolve_effort` and `resolve_stage_efforts` both make, None where the house file is absent; `tools/roles/roles_lib.py#resolve_effort` raises `RolesError` where no step yields a level; `load_policy` returns `declared`, each role's front-matter `effort`, beside the merged `gates`; the key answers are kept in the private `_POLICY_ANSWERS`. `help/roles.md` states the keys and the `gates` field, `tools/hooks/README.md` names the field as the index's source, and `memory/map/generated/symbols.json` gains the four new functions by `tools/codebase-map/gen_map.py --write`.
- **Cause:** builder discovery
- **Reason:** the three-argument resolver reads only the roles kit beside `roles_lib.py`, so a render of any other kit directory, the selftest's twelve fixtures among them (PINNED by `grep -c 'tempfile.TemporaryDirectory()'` at `7a0e819cc`), would read the wrong role file; the level-table pick is the same three lines in both resolvers, extracted at its second instance by the charter's `[reuse]`; a level no step yields would otherwise be `None` written as `effort: None`; and the charter's `[docs]` rule holds `help/roles.md` current, whose "Change a role's effort" bullet named the house file alone. The lexicon admits each new name (`python tools/lexicon/lexicon.py --suggest <name> --as py.function` printed OK for each).
- **Evidence:** at `7a0e819cc` `help/roles.md` told an adopter to edit `house/policy.toml` for a role's effort and gates, and `tools/hooks/README.md` named the `[gates]` table as the index's one source (DERIVED from the builder's read).
- **Risk:** additive
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** TOOL-dBoundRoles-21
