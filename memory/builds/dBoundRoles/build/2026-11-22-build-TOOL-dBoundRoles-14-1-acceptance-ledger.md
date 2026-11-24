**Serves:** journal TOOL-dBoundRoles-14

# TOOL-dBoundRoles-14 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a fixture or a probe of the code it
changed, on the worktree before the pass commit. No gate, suite or bar ran in the pass: the two `New arm:`
arms of section 7 and their RED-first observations are owed to the main loop at the close.

**Evidences:** TOOL-dBoundRoles-14
- AC1 — `role.gov-buildr` — `python gov_tag.py --fixture --plant role-rows` exited 1, printing `members role.gov-builder role.gov-skeptic, check: rc=1` and that `role.gov-buildr` is cited and undeclared in role, with no such line for `role.gov-builder`; the AC1 grep of `tag_index.py` in `tools/playbook/` printed nothing. OWED: the `role-rows` row's RED-first observation at the close.
- AC2 — `unit.alpha` — the `role-binding` plant exited 1 with two role-binding reds, `tools/playbook/instructions.toml:5 · role binding · unit unit.alpha binds yagni to role.gov-builder, whose rules does not cite it` at its `[[unit]]` line, and `tools/roles/agents/gov-builder.agent.md:2 · role binding · role.gov-builder cites verify, and no role-bound unit of it selects role.gov-builder`; no red named `unit.beta`; with gov-builder citing `yagni` alone it printed `rc=0`. OWED: the `role-binding` rows' RED-first observation at the close.
- AC3 — `field.task.titel` — the `field-rows` plant exited 1 naming `field.task.titel` as cited and undeclared in field, and printed `field.task.title 1 · field.input.spec 1 · field.stage.spec-writer 1 · field.stage.skeptic 1` over 32 members, the 25 read keys and the 7 distinct stage keys.
- AC4 — `grep -n 'dBoundRoles' README.md` — in `tools/playbook/` it prints the one line naming `role` and `field` as registered; the `ns =` count grep of `namespaces.toml` printed 2, its `.md#` purpose-source grep nothing, and the `help/tags.md` row count grep at the root 2.
- AC5 — `('task:title', True) ('task:title', False) field.stage.diff-finder` — printed by the AC5 `python -c` run in `tools/roles/`.
- AC6 — `field.task.titel` — `python check_roles.py` in `tools/roles/` exited 0 over the eleven migrated `reads:` lines; `field.task.titel` planted in gov-builder gave one R3 line naming it, exit 1; gov-reuse-scout's `field.card.reuse` without `?` gave one R3 line saying `card:reuse` must be optional; the gov-skeptic `handoff.py render ... --stdout` printed `task-sha=6a7a723aed39` before the migration and after it, the output otherwise byte-equal. OWED: arm 26's RED-first observation at the close.
- AC7 — `field` — `printf 'role.field.x\n' | python tools/lexicon/lexicon.py --tags` exited 1 printing `first segment 'field' is a namespace word`, the words read from the registry.
- seen-red — `playbook render selftest` — red `f3ec096a8` — green `f3ec096a8` — the role extractor answering nothing, then the binding red dropped: role-rows exits 0 and role-binding loses its line
