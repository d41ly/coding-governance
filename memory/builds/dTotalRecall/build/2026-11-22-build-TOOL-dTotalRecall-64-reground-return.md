**Serves:** research TOOL-dTotalRecall-64

# TOOL-dTotalRecall-64 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-64-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-64-reground-spec-writer.md), in substance.

- Re-grounded at rev-3, base `c2143acf`; `check-spec-tokens.py --spec`, `--check-specs dTotalRecall TOOL-dTotalRecall-64`, hygiene check 12 and the pinned-facts check exit 0.
- Moved by the landed code: cites by symbol (`tree_lib.py#_id_alternation`, `#build_id_token_re`, `id_grammar.py#grammar_for`, `#build_grammar`); the text quoted for unit 46's S1 matches unit 54 rev-4's body through `load_sibling`; the S2 and S3 amendments checked against unit 46 rev-4, S3 given in full; AC1's unit-46 half greps §9 for `amended by TOOL-dTotalRecall-64`, which could not pass before the pass; AC2's unresolvable `git show` spelling reworded.
- F2 RESOLVED (agent, delegated) option (b): this pass leaves unit 38's spec frozen (CLOSED at order 8, BUILD-METHOD M4), relying on TOOL-dTotalRecall-70 S14's planned deviation record; AC1's unit-38 half checks the spec unchanged. Parked: none.
- Follow-up: TOOL-dTotalRecall-70's S14 cause, its consumes-from text and its §4 claim about `SUFFIX_RE` change at its own re-ground.
