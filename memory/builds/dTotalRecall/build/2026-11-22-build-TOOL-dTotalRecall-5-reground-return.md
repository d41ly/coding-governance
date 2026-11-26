**Serves:** research TOOL-dTotalRecall-5

# TOOL-dTotalRecall-5 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-5-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-5-reground-spec-writer.md), in substance.

- Re-grounded at rev-6, base `8b8b1374`; `check-spec-tokens.py --spec`, `--check-specs dTotalRecall TOOL-dTotalRecall-5`, hygiene check 12 (with 25) and the pinned-facts check are clean for the spec.
- Moved by the landed code: the policy read is `tree_lib.py#read_policy_value`, which raises `LookupError` or `ValueError` and reads the policy file at the landed revision, so AC2's and AC10's probes commit in a scratch clone; gawk and bash `=~` refuse the `(?:` group, so a new §4 section builds one shape with two group openers and the shell side prints the ERE form; `cmd_placed_build` and `render_placed_build_readme` (TOOL-dPlacedRequest-21) also write the `slug-grammar:` line and check `mint_re` (S3); `Conf.digest` folds the slug class (S4, AC4); S9 points at `render_live` and `render_shards`; the census is restated as a `git grep` command with its counts re-pinned; Files touched gains five loop-kit files, `build_records.py`, `ratchet.py`, `seen_red.py`, `instruction_units.py` and S12's files.
- New S12 and AC11 (the `[docs]` rule): the three `builds.slug-*` keys' catalogue `summary` and `usage` filled, `unsummarised-keys.txt` drained, the policy page re-rendered and their rows removed from `docs-undocumented.txt`.
- Names: `slug_grammar` is `derive_slug_grammar` and `SlugGrammar.label` is `render_label`; `--mint-check` dropped (no reader).
- Forks RESOLVED (agent, delegated): F7 two spellings from one construction, the ERE form exported; F8 the clause's word flips spelled `1-1` and `3-3`, the catalogue admitting only `[0-9]+-[0-9]+`. Parked: none.
- Follow-up: units 2, 3, 4, 6 and 66 take the new names at their re-grounds.
