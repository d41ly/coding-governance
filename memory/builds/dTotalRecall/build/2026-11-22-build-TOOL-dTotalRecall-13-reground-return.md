**Serves:** research TOOL-dTotalRecall-13

# TOOL-dTotalRecall-13 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-13-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-13-reground-spec-writer.md), in substance.

- Re-grounded at rev-3, base `8b8b1374`; `check-spec-tokens.py --spec`, `unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-13` and hygiene check 12 (with 25) exit 0; 30137 B (DERIVED, `wc -c`). Status stays DEFERRED; the Carries line and records region unchanged.
- Moved by the landed code: every bare `path:line` became `path#symbol`; S1's moved range is `ext_of` through `extract_text` with `PATTERN_SETS`, the `check_ts_`/`read_ts_` helpers and the `_SH_`/`_TS_` constants, excluding `resolve_pattern_sets` and `KNOWN_EXTS`; S6's lexer range starts at `_IDENT_TOKEN_RE` with the `_LEX_PROFILES` loop; S7's drift-audit copy sits inside `build_lexicon_marginal_offense_rate` with signature `(ctx, sha, armed, lex, sets)`.
- The kit version bumps are dropped as a non-goal: the lander mints versions (`govkit.py#cmd_mint`).
- New S8: the five lexicon offenders that move (`ext_of`, `_python_defs`, `_probe_defs` with its nested `hits`, `_identifier_tokens`) owe a re-measured `VERB_OFFENDER_PIN` in `.lexicon.conf` by `lexicon.py --measure`.
- New S9 and AC8: the `drift-audit selftest` leg's guard in `tools/govkit/registry.toml` gains `{prefix}/lexicon/extract_code.py`, re-rendered into `tools/gate-legs.json`.
- AC4 corrected: the scratch run expects the tip's rows minus `adopt-lexicon.sh`'s, and its tree needs `.githooks/`, `skills/`, `.codebase-map.conf` and a `git init`.
- Fork F4 RESOLVED (agent, delegated): a file with unresolved merge conflicts reads only its stage-0 entry, so it gets no `index` entry.
- Parked: none. Outside the grant: `memory/project/positional-refs.txt` holds seeded rows keyed on this spec's old bare cites, drained in the main loop's commit.
