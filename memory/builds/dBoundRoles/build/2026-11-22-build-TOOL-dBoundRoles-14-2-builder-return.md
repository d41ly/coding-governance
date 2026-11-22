**Serves:** journal TOOL-dBoundRoles-14

# TOOL-dBoundRoles-14 — the second builder's return, a divergence

Run `wf_37ac53bc-1d1`, builder agent `ac44345db1ae10662`, started at `f07875f22` on rev-6. It wrote no product path and
committed nothing; `diverged: true`.

## The divergence, as returned

§4 "### The binding join" (which S5 and AC2 build on) says the join reads from the index "the units' selector rows as
PLAY-dOrderedCharter-10 S4 reads them, a unit's selectors sharing its `tag` row's path and line
(`tools/playbook/instruction_units.py#extract_unit`)". At HEAD, in extract_unit (tools/playbook/instruction_units.py@73883269:470-474), each
row's line is `n = u.line + <offset of the first span line holding "<val>">`. A unit's `tag` row sits on its `tag =`
line, and each selector row on the `scope =` line, or its own line when the scope array spans several lines. Probe:
`extract_unit({'memory_root':'memory'}, 'tools/corekit/instructions.toml', '[[unit]]\ntag = "unit.alpha"\nscope =
["role.gov-builder", "practice.yagni"]\n')` returns `('unit.alpha','tag',2,…)` but `('role.gov-builder','selector',3,…)`
and `('practice.yagni','selector',3,…)`, each row's end_line equal to its line. No row carries the unit's span, and no
reader in tools/playbook groups selectors per unit; "nearest tag row above" is wrong, since `scope` may precede `tag`.

Options it named: (a) check_role_bindings re-parses each indexed unit manifest's blob through
`instruction_units.parse_unit_rows`, which gov_tag.py already imports; (b) extract_unit emits each unit's selector rows at
its tag row's line, or carries the unit span as the tag row's end_line, adding `tools/playbook/instruction_units.py` to
Files touched and moving the red locations check_namespace_joins prints for selectors; (c) another grouping key.

## What held

Every other claim probed held at HEAD f07875f2: the 25 READ_KEYS, eleven role files with gov-tester, 7 distinct stage
keys, the extractor contract and DEFINE_KINDS, the path-only purpose-source, layer.roles core, dBoundRoles in
chain.toml, resolve_kit_dir via policy_value, SHAPE_PLANTS/PLANTS/run_plant_rows, handoff.py `render --stdout` and its
input/upstream check, arm 22's `brief:` filter, help/tags.md's "Eighteen" and its `role` sentence, the playbook README's
armed-by table, and no backticked or bracketed role./field. citation outside memory/builds.
