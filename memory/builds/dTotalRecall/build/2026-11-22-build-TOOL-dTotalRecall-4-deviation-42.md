# TOOL-dTotalRecall-4 deviation 42 — the id grader's tree, the helpers the schema is read through, and the verdict token

**Serves:** deviation TOOL-dTotalRecall-4

- **Departs from:** `TOOL-dTotalRecall-4@rev-6` [S2, §4 "The routing region", §4 "The agent's root" and §4 "Inventory"]
- **Hand-off:** spec-to-code
- **Before:** S2 names the grader `check_front_matter_value(key, value, conf, grammar)`, and §4 "The schema" has its `ids` and `id-ranges` types match `tree_lib.py#build_id_token_re` and `#_expand_ids` "for root", which that signature does not carry; §4 "Inventory" mints eight functions; §4 "The routing region" renders a review's `## Verdict:` token "where it carries one"; §4 "The agent's root" applies the default on a `LookupError` or a `ValueError`.
- **After:** `tools/memory-tree/gen_build_index.py#check_front_matter_value` takes a fifth, optional `root=None`, the tree `build_id_token_re` and `_expand_ids` match for, passed by `#collect` and absent from the parser's tree-free call; the four-argument call the spec names behaves as stated. Beside the minted names the pass adds `DERIVED_KEYS` and `TREE_BOUND_TYPES` (both derived from `FRONT_MATTER_KEYS`), `TYPED_DERIVED` (the population's name), `ROUTE_NAMED` (the two records a routing row names), `#cmd_print_typed_derived` (the `--print-typed-derived` seed's body), `#test_front_matter_schema` (the `--selftest` arm of section 7), and in the roles kit `tools/roles/handoff.py#AGENT_ROOT_DEFAULT`, `#AGENT_ROOT_LINES`, `tools/roles/render_agents.py#check_agent_root_arms` and `#FIXTURE_TREE_LIB`. The verdict token is the leading upper-case words of the `## Verdict:` value, because 2 older records in `memory/builds/cSettledDocket/reviews/` run prose after the token (DERIVED 2026-11-22, the render over this tree) and their whole value put that row at 366 characters, over `BUILD_README_ENTRY_CAP_CHARS`. `read_agent_root` also takes an `ImportError` and a value outside the catalogue's two as a refusal. The `families` and `streams` refusals keep the words the two enum checks they replace printed (`<key> value '<v>' is outside the FAMILIES set`), which the example-family arms read. `tools/loop/claim.py#read_anchor_unit` answers `<FAMILY>` where `read_derived_front_matter` raises `Problem`, as it did where no roster line read.
- **Cause:** builder discovery
- **Reason:** a grader over ids that matches them for no tree would grade a fixture's ids against this repository's slug grammar; a seed, an arm and a constant each need a name; the cap the region was bounded by holds only for a verdict that is a token.
- **Evidence:** the pass commit of TOOL-dTotalRecall-4 and its acceptance ledger, `2026-11-22-build-TOOL-dTotalRecall-4-1-acceptance-ledger.md`.
- **Risk:** additive
- **Approver:** author, under the build's `author-recorded` value
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-4
