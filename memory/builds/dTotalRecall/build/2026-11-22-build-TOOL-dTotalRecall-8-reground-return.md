**Serves:** research TOOL-dTotalRecall-8

# TOOL-dTotalRecall-8 re-ground — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-8-reground-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-8-reground-spec-writer.md), in substance.

- Re-grounded at rev-4, base `8b8b1374`, header `closes TOOL-dTotalRecall-102 TOOL-dTotalRecall-103`; `check-spec-tokens.py --spec` and `unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-8` exit 0.
- F6 RESOLVED (agent, delegated): the record moves to the playbook-render kit, beside its landed tag index `tools/playbook/tag_index.py`; `code_record.py` and its kit copy of `extract_code.py` sit in `tools/playbook/`, its tables in the one index file through `load_index`, no `[[namespace]]` row, the leg in `tools/playbook/kit.toml`.
- F4 rewritten: no new policy adapter; the derivation reads through `tools/playbook/policy_value.py#read_policy_value`.
- F7 RESOLVED: unit 1's landed `add_record_kind` (`360b653fd`) writes every row as `fields`, so `new` gains `--form`, observed by AC12.
- Asks folded: TOOL-dTotalRecall-102 (§3 names TOOL-dFurnishedOrders-17 for the `code` slot and `memory.code-budget`) and TOOL-dTotalRecall-103 (S14, a `neighbourhood` verb of the same record in TOOL-dFurnishedOrders-17's §4 row grammar, AC11).
- Follow-ups: TOOL-dFurnishedOrders-17 S3 resolves the reader under `memory-tree`, which F6 moves to `playbook` (an ask on that build); units 2, 3, 4, 5, 7, 9, 16 and 19 consume a memory-tree `policy_value.py` from this unit, which it no longer mints, each re-pointed onto `tree_lib.py#read_policy_value` at its own re-ground.
