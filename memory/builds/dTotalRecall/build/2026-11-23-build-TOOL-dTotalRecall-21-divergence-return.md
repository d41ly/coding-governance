**Serves:** journal TOOL-dTotalRecall-21
**Caused-by:** TOOL-dTotalRecall-21

# TOOL-dTotalRecall-21 divergence fold — the spec writer's return

The gov-spec-writer return for [2026-11-23-prompt-TOOL-dTotalRecall-21-divergence-spec-writer](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-21-divergence-spec-writer.md), in substance.

- Folded to rev-4, status `INPROGRESS`; `--check-specs`, `check-spec-tokens.py --spec`, pinned-facts and hygiene check 12 read green.
- New S10: `tag_index.py#load_index`'s reset drops every virtual table first, re-reads the table list and drops the rest in its one transaction; the module docstring follows, and S10 carries its Readers line.
- F8 RESOLVED (agent, delegated): option (a), since re-reading at each step or dropping by name can name an FTS5 shadow table, which SQLite's defensive setting refuses; the departure from PLAY-dOrderedCharter-55@rev-7 S16 is recorded as a deviation, as F5's is.
- New AC8 runs `gov_tag.py --rebuild`, a query, then `--rebuild` again, red on the second reset refusing; the `selftest.py` New arm covers it.
- Files touched gains `tools/playbook/tag_index.py`, `memory/guides/SESSION-KICKOFF.md` and the F5 and F8 deviation records, each written through the door with `--caused-by TOOL-dTotalRecall-21`; three always-run legs join the leg line.
