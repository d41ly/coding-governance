**Serves:** research TOOL-dTotalRecall-21

# TOOL-dTotalRecall-21 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-21-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-21-reground-spec-writer.md), in substance.

- Folded to rev-3 at HEAD `ed5a7d52`, a design change and not a path refresh: the landed tag index works differently from what the parent specs planned. `check-spec-tokens.py --spec`, `--check-specs` and hygiene check 12 exit 0.
- The index is `<git-common-dir>/gov/index-s<INDEX_SCHEMA>.db`, written by `build_index(root, tree, ctx, con, stats)` and reached through `load_view`; the budget names live in `id_grammar.py`; AC5 corrupts the header rather than zeroing the file; AC2 and AC7 compare against the kit at the pass's base.
- `ensure_index` is renamed `load_served_set` for the lexicon; Files touched grows to the pinned digest, the skill template and render, `common_dir.py`, the legacy-homes ledger, the dossier and `symbols.json`.
- F5 RESOLVED (agent, delegated): recall writes its own full-text tables in its own locked transaction, so an alias or conf edit to a built tree refreshes them; the build records a deviation from PLAY-dOrderedCharter-19 rev-8 S4. F6: rows keyed by path and blob, since extraction depends on the path. F7: recall hashes untracked corpus files per call.
- Units 9, 23 and 43 consume the changed interfaces; unit 9's writer was told mid-run.
