**Serves:** journal TOOL-dBoundRoles-1

# TOOL-dBoundRoles-1 — the second builder's return, a divergence

Run `wf_34a1cec1-85d`, started at `2a8c53282` on rev-7. It wrote no product path and committed nothing;
`diverged: true`.

## The divergence, as returned

§2 S1 (and §4 Files touched, §6 AC1, AC2, AC5, AC6, §8 F4 and F8, which all spell the key `acts-as`) cannot be built
as written. S1 makes `acts-as` a row of `tools/roles/role-schema.toml`, but `tools/roles/roles_lib.py#load_role_schema`
refuses any field key that does not match `[A-Za-z][A-Za-z0-9]*`, raising `R2 — field N's key 'acts-as' is not one
word`, and it does so at import, because `FRONT_MATTER_KEYS` is derived from `load_role_schema()` at module level. A
scratch probe confirmed it: a copy of `roles_lib.py` and `role-schema.toml` with the row `key = "acts-as"` added raised
that error on `import roles_lib`. The row as specced breaks every importer of the roles library (`check_roles.py`,
`render_agents.py`, `handoff.py`, `tools/loop/loop_lib.py#read_role_defaults`, `tools/loop/factories.py#write_role`).
`tools/roles/roles_lib.py` is not in §4 Files touched. Options it named: (a) Files touched gains `roles_lib.py`, S1
states that `load_role_schema`'s key grammar widens to a hyphenated word, and which `SCHEMA_SHAPES` value each new row
takes (the set holds no tag or closed-value shape); (b) the key is renamed to one word throughout.

## What held

Every other claim at HEAD `2a8c53282`: R2, R6, R7, R8, `BODY_CEILINGS`, `WORKFLOW_NAMES`, `WRITE_FOLDERS`,
`resolve_kit_dir`'s home-`playbook` probe for AC1's scratch (F11), `render_roles_index`, `render_agent_file`,
`write_role` and its flags, `write_workflow`, the `kind.role` usage row, the layer check and its plants, and the loop
item check, its plants and fixture mode. The workflows kit's two suites and README still spell the two old reviewer
slots, which the spec hands to TOOL-dBoundRoles-44.
