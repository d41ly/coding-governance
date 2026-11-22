**Serves:** journal TOOL-dBoundRoles-16

# TOOL-dBoundRoles-16 — the builders' returns, write-set stops and a divergence

Three runs on rev-6 committed nothing. The first two (`wf_2669408c-2f0` at `46e317547`, `wf_f845c411-bc5` at
`6f93ab7fd`) found no spec divergence and stopped on the declared write set: the four F7 change records, then the
generated outputs. Both are answered in the brief. The third (`wf_e3c2d4a9-882`, started at `8a5cf9347`) returned
`diverged: true`.

## The divergence, as returned

§4 Files touched, §4 Migration and §7 leave out the loop kit's factories. S2 and S5 make `shapes` a required field
of every agent role, a `role-schema.toml` row R2 reads into `tools/roles/check_roles.py#AGENT_ROLE_KEYS`, and make
`kind`, `checklist` and `orientation` required on every workflow entry that lists a role. The factories write neither:

1. `tools/loop/factories.py#write_role` builds a new role's front matter from a fixed set of values with no `shapes`
   and no flag for it, then grades it with `check_roles.py --write`. Once this unit lands, every `core.py new role`
   refuses its role on an R2 line, the factory's `role-new` selftest case reds, and so does the `loop factories
   fixtures` leg, which §7 does not list.
2. `tools/loop/factories.py#write_workflow` writes a `[[workflow]]` row with name, driver, harness, roles,
   enforced-by and trigger only, so `core.py new workflow --roles <slot>` mints an entry R6 and R9 refuse. The
   `workflow-new` case passes only because it passes an empty `--roles`.

The builder named what the spec would have to say: `tools/loop/factories.py` (and `tools/loop/README.md` if the
factory's flags are documented there) in Files touched and the write set; how the role factory writes `shapes` and
how the workflow factory writes the three fields, or refuses `--roles` without them; `loop factories fixtures` in §7;
and the roles README's sentence on what `core.py new role` writes.

It also noted, for the next dispatch: arm 30 of `tools/roles/adopt-roles.test.sh` adds a `scratch` entry with no
`kind`, which needs `kind = "single"` and its `judge` row `kind = "panel"` once `kind` is required; and scoping the four
unit rows to `role.*` tags arms the tag gate's role-bindings join, which the close should observe.

Every other claim it probed held at `8a5cf9347`.
