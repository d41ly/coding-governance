**Serves:** research TOOL-dTotalRecall-4

# TOOL-dTotalRecall-4 second re-ground over unit 5 as built — the spec writer's return

The gov-spec-writer return for [2026-11-22-prompt-TOOL-dTotalRecall-4-reground-2-spec-writer](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-4-reground-2-spec-writer.md), in substance.

- Folded to rev-6 at HEAD `e514feb71`; hygiene check 12, `check-spec-tokens.py --spec`, `--check-specs` and `writing_practice.py check pinned-facts` read green; the spec sits under its size ceiling.
- The tree-bound types read the grammar through `gen_build_index.py#read_slug_grammar`, unit 5's wrapper that turns a refusal into a `Problem`; the `grammar` type names `id_grammar.py#parse_slug_grammar` and its `ConfError`; the `ids` and `id-ranges` types match through `tree_lib.py#build_id_token_re` and `#_expand_ids`.
- The `date` type is a real calendar date, so AC2's refused value is refused; every README's date already passes.
- `render_new_build_readme` drops its now-unused `conf` parameter, and the `python reads` leg joins the gates line.
- The registry row gains unit 16's `purpose` column, written by hand since `record_kinds.py new` takes only the `fields` and `fence` forms; `TYPED_RECORD_KINDS` counts unit 25's `stream-plan`.
- Every census count re-pinned unchanged except `collect`'s run time. No fork, nothing parked, no edge with units 38 or 54.
