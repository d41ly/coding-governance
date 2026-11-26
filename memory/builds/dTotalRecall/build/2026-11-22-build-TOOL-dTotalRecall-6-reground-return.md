**Serves:** research TOOL-dTotalRecall-6

# TOOL-dTotalRecall-6 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-6-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-6-reground-spec-writer.md), in substance.

- Re-grounded at rev-3, base `8fbc5a33`; `--check-specs dTotalRecall TOOL-dTotalRecall-6`, `check-spec-tokens.py --spec`, hygiene check 12 and the pinned-facts check are clean.
- Moved by the landed code: every bare cite into `gen_build_index.py` now by symbol and the `parents:` READMEs re-counted with their command; `amends.to` landed as `["any"]`, so three namespace lists widen, AC9 also checking `family-id` in `patches.to`; a unit-id target types through unit 54's `parse_id_parts` (a new consumes-from edge) and resolves through unit 4's `derive_defined_ids`, slugs through unit 5's `BUILD_SLUG_RE`; `read_relation_rows()` reads `edges.toml` as `commit_trailers.py#read_key_table` does; `check_relation_cycles` is a thin caller of `backlog.py#scan_cycles`; `invert_relations` is `derive_relation_inverses` (the lexicon refuses `invert`); the pending check reads each ref's `refs/gov/remote/` cache copy; a new §4 "The render" pins the line format; §7 gains six legs and a second arm line for `tools/loop/loop_parents.py`.
- Forks RESOLVED (agent, delegated): F7 the loop kit's three own `parents:` splitters (`budget.py#derive_patch_origin`, `loop_parents.py#read_withdrawn_parents`, `position.py#derive_position_into`) read the `after` edges through `parse_relations`, new S9, S10, AC10, AC11 and `help/loop.md`; F8 a tag's state comes from `edge_grammar.py#resolve_edge`, read only by `--print-relations`. Parked: none.
- Sibling edit: TOOL-dTotalRecall-54 rev-4 gains `hands-off TOOL-dTotalRecall-6`.
- Follow-ups: TOOL-dTotalRecall-43 S18's cycle-walker lift already exists as `scan_cycles`; F7's change to `read_withdrawn_parents` reaches DEPL-dShippedRelease-11, its consumer.
