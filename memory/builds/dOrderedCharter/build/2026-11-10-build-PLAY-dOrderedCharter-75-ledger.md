# PLAY-dOrderedCharter-75 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-75

Each line is a probe this pass ran at rev-2 of the spec, over `a7d937b25` with the pass applied in the worktree.
The pass re-applies the code an earlier run built at rev-1, whose CLOSED commit the fork check refused for F2's
missing mark; rev-2 moved no design text. No leg, suite or bar ran in the pass: the plants ran through the tag
resolver's own fixture, and the prose readers by `git grep`. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-75
- AC1 — `python tools/playbook/gov_tag.py check` — run by the main loop over the tree after the pass, it exited 0 printing `tags: join reader · selects · unarmed` and `tags: join practice · selects · unarmed` and no line holding `is declared and selects no unit` (DERIVED at 8198bad3f).
- AC2 — with the `unscoped-unit` plant added and the join's arm put back to its any-unit-row test in a scratch break, restored after, `gov_tag.py --fixture --plant unscoped-unit` exited 1 printing `` `reader.every` is declared and selects no unit``. After S1 the same command exited 0 printing `tags: join reader · selects · unarmed: no unit's scope names a reader tag, so no member is graded as selecting` and no line holding `is declared and selects no unit`; `--plant dead-selector` still exited 1 printing `` `reader.ghost` is declared and selects no unit``, and its second half `without reader.ghost: rc=0`.
- AC3 — `git grep -l "names a tag of"` over `help/tags.md`, `tools/playbook/README.md` and `tools/playbook/tag_index.py` listed all three files, and `git grep -n "unit rows exist"` over the two prose files printed nothing.

**Owed to the close.** AC1, `gov_tag.py check` over the tree, which the role hook refuses a builder; the
RED-first observation of the `New arm:` line, the `unscoped-unit` row of the playbook adopter's plant rows;
and the section-7 legs, the `tags` leg among them.
