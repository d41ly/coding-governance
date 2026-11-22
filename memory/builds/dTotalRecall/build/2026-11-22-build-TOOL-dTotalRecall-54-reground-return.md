**Serves:** research TOOL-dTotalRecall-54

# TOOL-dTotalRecall-54 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-54-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-54-reground-spec-writer.md), in substance.

- Re-grounded at rev-3, base `8b8b1374`; `check-spec-tokens.py --spec`, `--check-specs dTotalRecall TOOL-dTotalRecall-54` and hygiene check 12 exit 0.
- Moved by the landed code: `grammar_for`, `build_grammar`, `_eras` and `resolve` live in `tools/memory-tree/id_grammar.py` (PLAY-dOrderedCharter-18), every bare cite now by symbol; the §4 parser body, run against HEAD, parses the plain, suffixed and cited-family cases and refuses the malformed ones over `build_id_token_re`'s slug class today; S1 admits a `None` root (unit 38 rev-4), AC1 probing it; new S5 and AC5 reach `tree_lib` lazily through `load_sibling`, extracted from `_parse_spec_h1`'s inline guard, since `id_grammar.py` imports only the standard library at module level; the per-root cache claim now points at TOOL-dTotalRecall-66 S35; §3 records that unit 5 rev-6 does not yet scope the slug-class binding; four legs added to the leg line and `tools/memory-recall/selftest.py` to Files touched.
- F2 RESOLVED (agent, delegated): the parser's arm lives in `tools/memory-recall/selftest.py` (its `make_repo` and `read_grammar`), since `id_grammar.py` has no self-test and no leg. Parked: none.
- Follow-up: units 38, 46, 60 and 66 declare `New arm:` lines at `id_grammar.py`, which no leg runs; each takes F2's home at its re-ground.
