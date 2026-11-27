**Serves:** research TOOL-dTotalRecall-36

# TOOL-dTotalRecall-36 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-36-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-36-reground-spec-writer.md), in substance.

- Folded to rev-4 at HEAD `ed5a7d523`; `check-spec-tokens.py --spec`, hygiene check 12 and `--check-specs` exit 0; the records block, the Edges block and F1 and F2 are byte-identical.
- Citations moved to symbols; the writer census re-derived with its command, three writers new since base (`loop/upstream.py#write_upstream_record`, `unattended.sh#write_chain_round`, `migrate_backlog.py#render_census`) becoming new S8 and AC7; F3 RESOLVED (agent, delegated) to (a), the keep reasons gaining reader-prefix text.
- S8 widens `derive_chain_verdict`'s head skip, else a cause line reads as a bad round row; S7 extracts unit 40's landed file walk as `read_code_paths` rather than copying it.
- S6's backfill is Markdown only and skips run records and chain-round records, whose readers hold the head's exact bytes; a run record's cause is its first sorted id; AC4 supplies every view placeholder; the check-22 claim corrected.
- Found at HEAD: `upstream.py#write_upstream_record` calls `re.fullmatch(ID, unit)` with unit 5's `SlugPattern`, which raises `TypeError`; S8 spells it `ID.fullmatch(unit)`. A sweep of every `SlugPattern`-bound name finds that call the only one handed to a `re` function.
- Build-order note: units 48 and 49 finish two of this unit's parts, so they follow it closely.
