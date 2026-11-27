**Serves:** research TOOL-dTotalRecall-5

# TOOL-dTotalRecall-5 divergence fold — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-5-divergence-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-5-divergence-spec-writer.md), in substance.

- Folded to rev-9, INPROGRESS kept; `check-spec-tokens.py --spec`, hygiene check 12 and `--check-specs dTotalRecall TOOL-dTotalRecall-5` exit 0; the spec is over the live-spec ceiling in warn mode.
- F11 RESOLVED (agent, delegated), option (c): a slug word is `[A-Z][a-z]+`, the return's (a) without digits, since `[A-Z][a-z0-9]+` lets `ID_RE` admit `TOOL-dFoo1-3`, which TOOL-dTotalRecall-66's S9 and AC6 rely on refusing; (b) fails AC12 (veto 1). It matches `memory/HYGIENE.md`'s letters-only rule, and every build folder, flip slug and id `read_bindings` reads fits it (DERIVED, the writer's run at HEAD); S4 states the one widening, in-slug dates.
- S8 adds the canonical `resolve_kit_dir` block to `tools/runlog/runlog_lib.py` and `tools/branch-reconcile/branch_reconcile.py`, joining the existing `resolve_kit_dir` row of `tools/lib/resolve-python.test.sh#PARITY_ROWS` by its marker; S8 counts the two new rows `slug_legacy_py` and `slug_legacy_sh` beside those copies.
- §4's census command spells its backslash-d arm bracketed, and §1, §4 and AC7's figures are re-pinned on it.
