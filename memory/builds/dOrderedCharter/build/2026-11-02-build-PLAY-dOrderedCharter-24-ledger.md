# PLAY-dOrderedCharter-24 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-24

Each line is a probe this pass ran with the pass applied: `edge_grammar.py`'s own CLI from
`tools/playbook/`, its `--fixture --plant` writing the plant's site and namespace registry into a temp
directory, or a `python -c` over `design_lib`. The playbook render selftest, the merge bar and the
`New arm:` line's RED-first observation are the main loop's at the close: a role agent runs none of them.

**Evidences:** PLAY-dOrderedCharter-24
- AC1 — `python edge_grammar.py --list` — exit 0; thirteen rows, each with its inverse, `cites · inverse cited-by · ... · derived`, then `edges: 13 types, 12 declared, 1 derived`. A scratch copy of `edges.toml` with `has-part` deleted is refused by `read_edge_types`: `edge row 1 lacks inverse`. OWED to the main loop: the arm's RED-first observation
- AC2 — `--plant good-block` — exit 0; `site.md:5 · implements · feature.x` and `site.md:6 · tests · kit.y, kit.z`, two edges, then `edges: green · 2 edge(s)`. `--plant fenced-edge` — exit 0, `edges: green · 0 edge(s)`. OWED to the main loop: the arm's RED-first observation
- AC3 — `--plant space-target`, `bracket-target`, `comma-in-pair`, `two-types-one-line`, `no-equals` — each exit 1 with one refusal `site.md: 2 edge line(s) refused`, naming `site.md:1` and `site.md:3`, each bad line and `the grammar is **Edges:** type=target[,target], one line per type`; the good line 2 is not named. OWED to the main loop: the arm's RED-first observation
- AC4 — `--plant unregistered-type` exit 1 `frobs · is no type of edges.toml's closed set`; `declared-inverse` exit 1 `implemented-by · is the inverse of implements, derived from its row and never declared`; `declared-cites` exit 1 `cites · is derived (derived from the text), never declared`. `derive_inverse_edges` over the good block returned `[('feature.x', 'implemented-by', 's.md:1'), ('kit.y', 'tested-by', 's.md:2'), ('kit.z', 'tested-by', 's.md:2')]`. OWED to the main loop: the arm's RED-first observation
- AC5 — `--plant outside-to` exit 1 `layer=kit.x · is outside layer's to [layer]`; `--plant pin-on-none` exit 1 `part-of=kit.x@1a2b3c4d · pins a target, and part-of's row says pin = "none"`. OWED to the main loop: the arm's RED-first observation
- AC6 — `--plant selector-registered` exit 0, `edges: green · 1 edge(s)` and `edges: edges.toml unchanged` (the shipped file's bytes compared before and after); `--plant selector-describes` exit 1 `instructs=feature.x · is outside instructs's to [selects]`. OWED to the main loop: the arm's RED-first observation
- AC7 — the spec's `python -c` printed `True` over 509 view rows; every row's `(clause id, hash)` dumped before the factoring and after it compared byte-equal (`cmp`); `git grep -n "hashlib.sha256" -- tools/memory-tree/design_lib.py` printed one line, `design_lib.py:177`, inside `derive_pin_hash`.
