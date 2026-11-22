**Serves:** journal TOOL-dBoundRoles-3

# TOOL-dBoundRoles-3 — the main loop's decision on the missing declaration verb

S2 reads one item's declaration by running the loop kit's `loop_lib.py declaration --item <tag> --json`, the verb
the owner's ruling on §8 F5 chose and asked of dDeclaredLoop. That build has landed and the verb is absent: the loop
kit carries `tools/loop/loop_lib.py#resolve_item_declaration` and `#check_item_declarations` but no subcommand that
prints one item's declaration.

The owner approved the surface in that ruling; only its builder is open. So this unit's pass builds the verb, by M3 as
a delegated resolution, rather than carrying this unit and the four that consume it (TOOL-dBoundRoles-4, -7, -23 and
-43) forward against an ask. The verb prints `resolve_item_declaration` for one item as JSON, exits nonzero naming the
item where the loop declares none, and is documented where the loop kit documents its verbs. widens: none · relaxes:
none.

The write set therefore adds `tools/loop/loop_lib.py`, `tools/loop/README.md` and `help/loop.md`, beside
`tools/playbook/instruction_units.py` for any marker bytes the unit moves, `tools/govkit/usage.toml` for any verb row,
and `help/roles.md`. The builder records the verb and every other change the spec does not state in one deviation
record.
