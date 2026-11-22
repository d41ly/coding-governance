# TOOL-dTotalRecall-46 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-46

No merge bar, no self-test suite and no gate leg ran in this pass. The pass builds no body: it observes
`tools/memory-tree/id_grammar.py#parse_id_parts` as `TOOL-dTotalRecall-54` landed it at `74af3faa4`, and
writes no product path. Every probe below ran on node d, 2026-11-22, from base `254057fa6`, over the worktree
before the pass commit, the cited-family cases over a scratch tree under the run's scratch directory whose
`.memory-tree.conf` declares `MEMORY_ROOT=memory`, `FAMILIES="tooling:TOOL"` and `RECALL_CITED_FAMILIES="ZED"`.
The gates of §7 are OWED to the close, after the last unit is terminal; §7 declares no `New arm:` line.

**Evidences:** TOOL-dTotalRecall-46
- AC1 — `inspect.getsource` — a `python -c` probe from the repository root with `tools/memory-tree` on `sys.path` printed `('TOOL', 'dTotalRecall', 38)` for `id_grammar.parse_id_parts("TOOL-dTotalRecall-38", ".")`; `grep -c 'ID_RE'` over the function's `inspect.getsource` printed 0 and exited 1 (DERIVED 2026-11-22); over the scratch tree the call on `ZED-aFoo-2` printed `('ZED', 'aFoo', 2)`.
- AC2 — `TOOL-aDrainedSluice-9b` — the same probe printed `('TOOL', 'aDrainedSluice', 9)`.
- AC3 — `ARCH-001` — the same probe raised `ValueError` for each of `ARCH-001`, `ABL-d119`, `TOOL-x` and `TOOL-dTotalRecall-38@rev-2`, each message `not an id under this tree's grammar: <id>` naming the id it was given; none returned a tuple.

**Evidences:** TOOL-dTotalRecall-63
- AC2 — `_id_alternation` — run from `tools/memory-tree/` over the scratch tree, `parse_id_parts("ZED-aFoo-2", tree)` printed `('ZED', 'aFoo', 2)`; the liveness control, the same call with `alt=tree_lib._id_alternation(id_grammar.load_conf(tree))`, raised `ValueError`, so the case separates the two bodies; `inspect.getsource(id_grammar.parse_id_parts).count('_id_alternation')` printed 0 (DERIVED 2026-11-22); `git merge-base --is-ancestor 74af3faa4 HEAD` exited 0 at base `254057fa6`, so `git log --reverse --format=%s` lists unit 54's pass commit before this pass's commit, which sits on that base.

**Evidences:** TOOL-dTotalRecall-64
- AC2 — `ast.get_source_segment` — run from `tools/memory-tree/`, the `parse_id_parts` segment of `id_grammar.py` as `git show 74af3faa4` prints it and the segment of the working file printed equal, `True` (DERIVED 2026-11-22).
