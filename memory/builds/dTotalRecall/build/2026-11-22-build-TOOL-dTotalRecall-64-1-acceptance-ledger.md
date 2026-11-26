# TOOL-dTotalRecall-64 — acceptance ledger, build pass 1

**Serves:** log TOOL-dTotalRecall-64

No merge bar, no self-test suite and no gate leg ran in this pass. The pass is a spec amendment: the spec writer
wrote unit 46's spec from [2026-11-22-prompt-TOOL-dTotalRecall-64-build-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-64-build-spec-writer.md),
and the main loop ran the probes below on node d, 2026-11-22, over the worktree with the amendment applied, base `a83e9643a`.

**Evidences:** TOOL-dTotalRecall-64
- AC1 — `read_root_conf` — the three-phrase `grep -cE` over unit 46's spec printed 0, the §9 count of `amended by TOOL-dTotalRecall-64` printed 1, and `git diff --quiet` over unit 38's spec from the pass base exited 0 (each DERIVED 2026-11-22).
- AC2 — `ast.get_source_segment` — OWED to unit 46's pass tip; the writer's preview at this tip printed the two `parse_id_parts` segments equal.
