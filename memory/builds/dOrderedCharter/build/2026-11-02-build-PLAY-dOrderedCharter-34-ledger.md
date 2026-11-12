# PLAY-dOrderedCharter-34 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-34

Each line is a probe this pass ran at rev-10 of the spec, with the pass applied. No leg, suite or bar ran in the
pass: every plant ran through `tools/playbook/fixtures/composition.py --plant` over a throwaway repository on
`main`, the census through `tools/playbook/practice_census.py`, and the relay through
`tools/govkit/govkit.py#derive_composition_lines` called alone (DERIVED at fc6a05462 with this pass applied). Five
plants were also run with the code they guard stubbed to its broken form, and each changed its answer. This
record cites no code line.

**Evidences:** PLAY-dOrderedCharter-34
- AC1 — the render of gov's charter, `render_playbook.py --target .`, exited 0 and left `AGENTS.md` and `.governance/instructions.lock` byte-identical, `git status` naming neither: gov's overlay holds no level-0 unit, so the project block is the key's lines alone. `project-block` exited 0: the key's two lines then the two level-0 units in overlay order, and with the key unanswered the units alone and no default bullet. With `build_project_block` stubbed to the old placeholder read it exited 1.
- AC2 — `marked-part` exited 0: gov's two level-4 lines, then the repository unit once between `<!-- gov:repo -->` and `<!-- /gov:repo -->`, and a second render byte-identical with one pair. `unplaced` exited 0 with one note, `unplaced   repo.four · level 4 · no unit slot of this render selects it`. With the levels the note reads stubbed empty, `unplaced` exited 1.
- AC3 — `level-6` exited 0 on the render's exit 1 naming `repo.task` and `level 6`.
- AC4 — `over-budget --enforce warn` exited 0 on one line, `BUDGET WARN · AGENTS.md · 21311 bytes over AGENTS.md 20480 · budgets.enforce is warn · key budgets."AGENTS.md" · largest: gov:playbook 18019 · repository 2292 · gov:alpha 1000` (DERIVED at fc6a05462 with this pass applied); `--enforce refuse` exited 0 on the render's exit 1 with no `AGENTS.md` written.
- AC5 — `over-codex --enforce warn` exited 0 on the render's exit 1, one `REFUSED` line, `BUDGET REFUSE · AGENTS.md · 33210 bytes over CODEX_MAX 32768 · Codex's limit for a file it reads whole · largest: gov:playbook 18076 · repository 14134 · gov:alpha 1000`, and no file written (DERIVED at fc6a05462 with this pass applied). With `measure_contributors` stubbed empty it exited 1.
- AC6 — `alias-copy` exited 0: `--check` exited 1 naming `GEMINI.md` once a unit changed, the render re-wrote it as the composition in the same run, and `--check` then exited 0. With the alias check and write both stubbed it exited 1.
- AC7 — `seeded-template` exited 0: the composition byte-identical with and without `playbook_path` answered, no byte of the seed in it, one `retired` note naming `playbook_path`. `installed-template` exited 0: the render read the kit's copy with `gov_root` an empty directory, and with the copy removed refused naming both paths. The grep over `tools/playbook/kit.toml` found the `[[files]]` rule's include and its `to` beside the engine.
- AC8 — `delta` exited 0 printing six state lines, one per state, and one widening line, `fixture.adopter.alpha-tuned on fixture.alpha · needs remove fixture.beta`, each in update's widths; with the row composition stubbed it exited 1. `derive_composition_lines` over the six state lines, a widening and a foreign line kept the seven and dropped the foreign one. The `update` half is the govkit selftest arm, owed (deviation 348).
- AC9 — the census over gov's tree printed one ruling per row of the catalogue, `practice.writing` the one `gov-only` row with `stays`, `practice.portable` `ship` with two of its legs shipping (DERIVED at fc6a05462 with this pass applied). Its four plants exited 0: `gov-only` and `outside-foundation` printed `gov-only` with `moves` and `stays`, `no-evidence` printed `ship`, `row-kept` printed `gov-only` with `moves, row kept`.
- AC10 — the census record lists every row's ruling and the one disposition, `stays`; the moved set is empty, so no catalogue, pending or overlay edit was made, and that is read as no move, never as coverage of one. The core meta-check and the roles render check are owed to the close.
- AC11 — the grep over `help/composition.md` and `help/README.md` found the page's budget section and the index line; its pathspec is unit 49's to correct and is observed at that pass.

**Owed to the close.** The bar, and the RED-first observation of the two `New arm:` lines: the render selftest's
block running `composition.py` over every plant, and the govkit selftest's relay arm. The policy fixtures' one-line
rule plant, whose exits a scratch replica of it observed green under `warn` and refusing under `refuse`.
