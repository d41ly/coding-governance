**Serves:** research TOOL-dTotalRecall-43
**Caused-by:** TOOL-dTotalRecall-43

# TOOL-dTotalRecall-43 divergence fold — the spec writer's return

The gov-spec-writer return for [2026-11-23-prompt-TOOL-dTotalRecall-43-divergence-fold-spec-writer](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-43-divergence-fold-spec-writer.md), in substance. Every one of the builder's five points re-derived true at HEAD.

- Unit 43 folded to rev-8 (INPROGRESS), unit 52 to rev-5 (DEFERRED); `--check-specs` over both, `check-spec-tokens.py --spec` and hygiene check 12 read green.
- S19: §8 F6 RESOLVED (agent, delegated), option (b): the `record-kinds-legacy` merge moves to unit 52, whose S4 now holds it and whose AC5 is the old AC19's count. The two homes share one key, the dClosedLoop execution record's `research` row (DERIVED 2026-11-23).
- S22: §8 F7 RESOLVED (agent, delegated): `fts_blob` stays, since `blob_parsed` carries no path and recall serves untracked pairs; `query.py#derive_recall_digest` takes S21's shared version rule and `CACHE_VERSION` goes.
- S21: one version rule, `import_walk.py#derive_closure_version`, which `tag_index.py#derive_extractor_versions` and `tree_lib.py#load_leg_reader` both call; `leg_row` stays, and the Readers line names the three leg readers at HEAD, `spec-head` among them.
- Files touched gains `tools/memory-tree/import_walk.py` and drops the S19 paths; the spec is 49136 B (DERIVED), under its 49152 B ceiling (PINNED 2026-11-20).
- Outside its grant: unit 53's edge still says it gets "the merged ledger" from unit 43; S44 says `derive_anchor` has three callers where HEAD has four (`gov_tag.py` the fourth); F4 still cites AC19, now unit 52's AC5.
