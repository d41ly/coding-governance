# TOOL-dTotalRecall-22 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-22

No merge bar, no self-test suite and no gate leg ran in this pass. Every probe ran on node d, 2026-11-22,
from base `1ca91e849` with the pass applied in the working tree. The cardinality plants build their
scratch files under the system temp directory, as `edge_grammar.py#run_fixture` makes them. The gates of
§7 and the three `New arm:` RED-first observations are OWED to the close, after the last unit is terminal;
once the leg was declared, the role's hook refused a direct run of `edge_grammar.py --cardinality
--registry` as that leg, so the readings below of AC2 and AC6 were taken before the declaration.

**Evidences:** TOOL-dTotalRecall-22
- AC1 — `cardinality-missing` — a `python -c` probe of `tools/playbook/edges.toml` through `tomllib` found `cardinality` with both ends on every `declared` row, `supersedes` reading `per-target = "1"`, `caused-by` reading `per-source = "1"` and `cites` carrying none (the row count DERIVED by `edge_grammar.py --list`, unchanged); `edge_grammar.py --fixture --plant cardinality-missing` printed `edge 'part-of' (row 1) lacks cardinality` and exited 2.
- AC2 — `cardinality-mirror` — `edge_grammar.py --cardinality --registry` exited 0 and printed `cardinality: registry · 10 kind(s) mirror a bounded type; 0 differ` (DERIVED, the count §4 "The mirror" PINNED at `803a3b802`); `--fixture --plant cardinality-mirror` printed `cardinality: registry · deviation · caused-by per-source is "many" here, "1" in edges.toml` and exited 1.
- AC3 — `check_edge_bounds` — a `python -c` probe called `design_lib.check_edge_bounds` with `("supersedes", "A", "D", …)` and `("supersedes", "B", "D", …)`: bound `("many", 1)` (the bound AC3 PINNED) returned one `Violation` at end `target`, node `D`, both edges its members; bound `("many", "many")` returned none.
- AC4 — `unordered amends of` — `asbuilt_view.py --fixture --plant unordered-amends` printed the same finding before and after the change, the view sha masked, diffed byte for byte; a `python -c` probe that set `asbuilt_view.check_edge_bounds` to return nothing printed `findings 0` (DERIVED, that run's count) for the plant.
- AC5 — `cardinality-merge` — the plant printed `git merge was clean, HEAD a merge of 2 parents` (DERIVED, `git rev-list --parents`) and `cardinality: supersedes per-target 1 exceeded at PLAY-xDec-1 by` both records' paths, under `memory/builds/xAlpha/build/` and `memory/builds/xBeta/build/`, each at its edge line, and exited 1; `--plant cardinality-branch` printed no violation and exited 0. The red-to-green staging by dropping the per-target group is OWED to the close as the first `New arm:` line.
- AC6 — `--cardinality --registry` — at the pass's working tree it exited 0, its last line naming the edges and types read with the edge count above zero (DERIVED at each run) and no refused line. The leg's own run, red in a scratch worktree with two records superseding one target and green at the tip, is OWED to the close as the third `New arm:` line.
- AC7 — `practice.one-fact` — a `python -c` probe of `tools/gate-legs.json` found one row named `edge cardinality (per source and per target, over the merged tree)`, its argv ending `edge_grammar.py --cardinality --registry`, `"pack": "tags"` and `enforces` holding `practice.one-fact`; `leg_factory.py --list` named its declaring file `tools/govkit/registry.toml`.
- AC8 — `--cardinality --registry` — `docs_leg.py --fingerprints` printed the usage row of `tools/playbook/edge_grammar.py` at the fp8 the `help/tags.md` stamp carries, and a `grep -c` of that page found the phrase. The `docs` leg is OWED to the close.
