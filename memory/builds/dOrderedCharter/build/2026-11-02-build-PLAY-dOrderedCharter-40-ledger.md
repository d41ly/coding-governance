# PLAY-dOrderedCharter-40 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-40

Each line is a probe this pass ran at rev-5 of the spec, with the pass applied in the worktree and staged. No leg,
suite or bar ran in the pass: the reader, schema, grammar and pin functions were called directly, the resolver's
`show` and `where` verbs ran over the tree, and the two new plants ran through the resolver's own fixture. The
change records were written by the stand-in door's `write_change`, the function `build_records.py new change`
calls, with its day held to the dispatch's declared names. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-40
- AC1 — `read_units` filtered on origin `playbook-render` returned `unit.drive-table`, `unit.kinds-register`, `unit.policy-schema` and `unit.unit-registry`; `run_schema` and `run_one_fact` each printed four rows and no red and `run_grammar` printed four unit rows and no red, each returning 0 (PINNED, four rows, counted at 79cbe680). Before the manifest was staged, the same probe printed each verb `unarmed`.
- AC2 — `gov_tag.py show unit.kinds-register` exited 0 naming the manifest row, where before the pass it exited 1 with the tag resolving to no row; the change-record glob lists four records, one per row (PINNED, counted at 79cbe680), each read by `build_records.py read` with exit 0, each `After` the pin `derive_row_pin` derives: `unit.policy-schema@85b441ca`, `unit.drive-table@9b7d467d`, `unit.kinds-register@63ad2ffb`, `unit.unit-registry@1155c58a`.
- AC3 — `gov_tag.py show doc.reference.kinds` exited 0 naming the declaration's `[[reference]]` row and printing its `h1` line; `--fixture --plant reference-row` exited 0 with the fixture's `doc.reference.fixture` resolved to its row and the fixture's check green; `--plant reference-no-h1` exited 1 printing that member `lacks h1`; `render_reference_pages` in check mode returned 0, three pages checked and none drifted (PINNED, unit 37 rev-7 S1).
- AC4 — `render_playbook.py --target . --check` exited 0, the charter's region matching a fresh render.

**Owed to the close.** The RED-first observation of the `New arm:` line, the tag resolver's `reference-row` and
`reference-no-h1` plant rows in the playbook adopter, and the section-7 legs, the `tags` leg among them, which the
role hook refuses a builder.
