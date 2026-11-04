# PLAY-dOrderedCharter-9 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-9

Each line is a probe this pass ran, at rev-5 of the spec, from the worktree root with the pass applied:
`git grep` reads, and `instruction_units.py fixture --plant <case>` once per plant, each plant in a throwaway
repository under the host temp directory. Each plant was also seen red on a break staged in-process: a loose
manifest predicate failed `two-kits`, a derived unit rendering its typed text failed `render`, and a reader
dropping its faults failed `unreadable` six times. The legs the spec's Gates section names, the merge bar,
and the RED-first observation of the New arm are the main loop's at the close: the role hook refuses a
builder those.

**Evidences:** PLAY-dOrderedCharter-9
- AC1 — `fixture --plant row` exited 0: every field of a row carrying all fifteen read back equal, `origin` read `alpha-kit` from the kit's descriptor on both rows, the second row's forged `origin` ignored, and its undeclared `class` read `fixed`
- AC2 — `fixture --plant two-kits` exited 0: `read_units` returned `unit.a1`, `unit.a2`, `unit.b1` in path then row order, `extract_unit` claimed the two kit manifests alone, `extract_repo` the overlay alone, `read_tree_edges` read the two and the overlay, and none read `tools/alpha/sub/instructions.toml` or `docs/instructions.toml`
- AC3 — `fixture --plant unreadable` exited 0: the TOML error, `level = "nine"` and `scope = "reader.every"` each gave a fault naming the file and the row, `read_units` raised one `UnitRowError` naming all three, `edges = ["part-of"]` read back as its string while `read_unit_edges` raised `EdgeRefusal` naming the file, the row's line and the entry, and the string `enforced-by` yielded no `enforces` edge where a list yielded one
- AC4 — `git grep -n -E '\.get\("unit"\)|, "unit"\)' -- tools/playbook/` printed one line, in `instruction_units.py#parse_unit_rows`; `git grep -n -F '"select"' -- tools/playbook/edge_grammar.py` printed nothing; `fixture --plant arms` exited 0, the grammar half, the `unit` namespace's join and the unit edge site each printing `unarmed` or nothing with no row and grading the fixture's two rows once committed
- AC5 — `fixture --plant render` exited 0: the selector `reader.driver` rendered three of four rows in level order, the `cmd:git rev-parse --abbrev-ref HEAD` fact as the command's output, the `policy:tags.slice` row as `leaf`, the value `policy.py get tags.slice` printed over the committed fixture tree and never its typed text, and the directive's text; a fifth row sourced `policy:zz.unknown` refused the render naming `zz.unknown`
- AC6 — `fixture --plant extractor` exited 0: `extract_unit` over the base revision's blob, deleted from the working tree, returned its tag and `selector` rows, `derive_extractor_versions` over a copy of the kit named `instruction_units:extract_unit` and `instruction_units:extract_repo`, a byte added inside the copy's `parse_unit_rows` changed both versions, and `git grep -n -F 'extractor = "instruction_units:extract_' -- tools/playbook/namespaces.toml` printed two lines
