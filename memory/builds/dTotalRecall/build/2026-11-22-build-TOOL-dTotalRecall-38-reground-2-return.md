**Serves:** research TOOL-dTotalRecall-38

# TOOL-dTotalRecall-38 second re-ground over unit 5 as built — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-38-reground-2-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-38-reground-2-spec-writer.md), in substance.

- Folded to rev-6 at HEAD `e514feb71`; `--check-specs`, `check-spec-tokens.py --spec`, hygiene check 12 and `writing_practice.py check pinned-facts` read green; the census counts hold.
- The caller-bound readers parse under the families their own validators used: the `backlog.py` and `migrate_backlog.py` fixtures carry families this repo does not declare, so a tree-family parse would red two self-tests. F4 RESOLVED (agent, delegated): `parse_id_parts` takes a keyword-only `alt`, the five caller-bound readers pass `backlog.ANY_FAMILY` and `cmd_new_build` passes `_id_alternation(conf)`.
- F5 RESOLVED (agent, delegated): drift-audit's `_parse_slug` takes `root` and falls back to stripping the first and last segment where the memory-tree kit is absent, as its selftest fixture is.
- The slug-class binding is cited as landed by unit 5; unit 45's fourth reader `check_policy.py#derive_run_kind` is named; the regex cache is unit 66's, not unit 54's. AC1 gains the `alt` case, AC2 runs over a scratch clone, new AC5 checks the readers' answers.
- Edges the writer could not write: unit 54 must land the keyword-only `alt`, and unit 38 consumes `parse_id_parts` from unit 54, so the order inside step 8 is 54, then 38, then 4.

## The main loop's decision on the step-8 order

Decided, not parked: units 38, 4 and 54 share build order 8 and the table states no order inside a step, so they build 54, 38, 4, the order their edges give. Unit 54's writer folds the `alt` keyword into its spec before any of the three is dispatched.
