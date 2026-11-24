**Serves:** journal TOOL-dBoundRoles-81

# TOOL-dBoundRoles-81 — acceptance ledger

Each criterion of section 6, read by the pass that built the unit with a probe of the code it changed, on the
worktree before the pass commit at base `145934181`: each `front-matter-` plant of
`tools/playbook/fixtures/row_kind.py#PLANTS` run by the fixture's own `--plant` CLI, each in the throwaway
repository `tools/playbook/fixtures/row_kind.py#main` makes under the host temp folder; the roles kit's verb
`tools/roles/check_roles.py#print_rows` over gov's own role file and workflow table; the compose verb's output per
kind compared before and after the edit; a `python -c` probe running the `front-matter-rows` plant with
`tools/playbook/overlay_rows.py#read_source_paths` replaced by one answering the glob itself, the staged break the
`New arm:` line names, which exited 2 unarmed where the plant expects 0, and another with
`tools/playbook/tag_index.py#resolve_roles_verb` answering None, which exited 2 naming the reader; and a grep of the
registry. The new selftest rows were evaluated against the plants by a probe reading them out of
`tools/playbook/render_playbook.py`, all passing. No gate, suite or bar ran in the pass: the `New arm:` arm section 7
declares, its RED-first observation with the glob read as one blob, and the legs section 7 lists are owed to the main
loop at the close.

**Evidences:** TOOL-dBoundRoles-81
- AC1 — `front-matter-rows` — `python tools/playbook/fixtures/row_kind.py --plant front-matter-rows` exited 0 printing a `row role.<name>` line for each fixture role file, each with `origin` `role` and `source` its own file under the glob, the overlay row with `origin` `repository`, and a `row workflow.<name>` line for each entry of the fixture workflows file, each with `origin` `workflow` and `source` that file. OWED: the `front-matter-rows` selftest row of the `playbook render selftest` leg, RED first with the glob read as one blob, at the close.
- AC2 — `--print-rows role` — `python tools/roles/check_roles.py --print-rows role < tools/roles/agents/gov-builder.agent.md` printed one object tagged `role.gov-builder` whose `tools`, `reads`, `shapes`, `gates` and `never` are lists, `gates` keeping `lexicon naming predicates?` as spelled, `writes` the list holding `product` and `budget` the string the file holds; `--print-rows workflow < tools/roles/workflows.toml` printed one object per `[[workflow]]` entry, each tagged `workflow.<name>`, as many as the file's entry headers (DERIVED, counted by `grep -c` at the probe). An indented key, a typed `tag` and a file that is not TOML each exited 2 with the defect on stderr. OWED: nothing beyond the legs section 7 lists at the close.
- AC3 — `compose --kind item` — `python tools/playbook/overlay_rows.py compose --kind item` printed output byte-identical to what the same command printed on the worktree at base `145934181` before the first edit, so its `pins` are equal (DERIVED, compared by `cmp`); `scenario`, `stage` and `role` compared byte-identical too, `role` still unarmed for want of a schema; the `item` row of `tools/playbook/namespaces.toml` names no `rows` key. OWED: nothing beyond the legs section 7 lists at the close.
- AC4 — `front-matter-refused` — `--plant front-matter-refused` exited 1 with an `overlay-rows: red` line naming the reader, the fixture role file whose `tools` key is indented, and the verb's line `R2 — front-matter key is indented`; `--plant front-matter-unarmed` exited 2 with a line naming `unarmed` and the glob its namespace source spells. OWED: the `front-matter-refused` and `front-matter-unarmed` selftest rows, RED first, at the close.
- AC5 — `rows = "tag_index:read_roles_rows"` — `grep -n 'rows = "tag_index:read_roles_rows"' tools/playbook/namespaces.toml` printed the `role` row's line. OWED: nothing beyond the legs section 7 lists at the close.
- seen-red — `playbook render selftest` — red `f3ec096a8` — green `f3ec096a8` — the source glob matching no file: front-matter-rows exits 2
