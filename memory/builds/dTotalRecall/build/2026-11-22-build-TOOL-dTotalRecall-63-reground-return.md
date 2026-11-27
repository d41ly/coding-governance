**Serves:** research TOOL-dTotalRecall-63

# TOOL-dTotalRecall-63 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-63-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-63-reground-spec-writer.md), in substance.

- Re-grounded at rev-3, base `c2143acf`; `check-spec-tokens.py --spec`, `--check-specs dTotalRecall TOOL-dTotalRecall-63`, hygiene check 12 and the pinned-facts check are clean; no new function.
- Moved by the landed code: §1 cites `tree_lib.py#_id_alternation` and says "not at the close" (the build's highest order moved); §4 and §10 cite `id_grammar.py#build_grammar`; §4's amendment to unit 46 places its clause after AC1's first sentence and replaces unit 46 rev-4's own Red-when line; AC1's grep now looks for `added by TOOL-dTotalRecall-63`, since its old id grep already passed before any pass; AC2 says the call returns the tuple; §7 places unit 54's arm in `tools/memory-recall/selftest.py`.
- Forks: none decided or parked. Left for TOOL-dTotalRecall-70 (order 33): AC2's build-order read by `git log` order and the scratch tree's conf spelled out in full.
