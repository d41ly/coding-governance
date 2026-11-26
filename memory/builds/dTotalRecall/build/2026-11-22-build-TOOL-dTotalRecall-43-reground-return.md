**Serves:** research TOOL-dTotalRecall-43
**Caused-by:** TOOL-dTotalRecall-43

# TOOL-dTotalRecall-43 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-43-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-43-reground-spec-writer.md), in substance.

- Folded to rev-6 at HEAD `e1321ce78`; `--check-specs`, `check-spec-tokens.py --spec` and hygiene check 12 exit 0; the spec is under its size ceiling with no criterion dropped.
- Clauses a landed unit already met are re-observations; S4, S35 and S49 are overtaken; S10, S26, S27, S29, S37, S39, S43 and S57 are narrowed to what is left.
- S11, S12 and S50 point at `tree_lib.py#read_policy_value`, their criteria grepping for the import; S13 and S52 at `tools/playbook/record_extract.py`; S53's second caller is `tools/workflows/replay_scorer.py`.
- S55 and S56 are NOT OBSERVED, parked with unit 8 on ask TOOL-dTotalRecall-109; S6 states the order 21 to 27 window.
- F4 RESOLVED (agent, delegated): S19's ledger merge keeps one registration, leg `record-kinds`, with one seed emitting both slices; two registrations fail AC19 and a widened ledger schema changes every adopter's contract.
- For unit 52: its `record-kinds-legacy` table lives in `tools/govkit/registry.toml`, and its re-ground absorbs F4's one-leg, one-seed shape.
