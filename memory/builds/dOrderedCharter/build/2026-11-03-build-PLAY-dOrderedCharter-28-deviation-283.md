# PLAY-dOrderedCharter-28 deviation 283 — the edge check's helpers, the writer key, the note refs' type and the files touched, as built

**Serves:** deviation PLAY-dOrderedCharter-28

- **Departs from:** `PLAY-dOrderedCharter-28@rev-5 [§4 Data model, §4 Inventory, §4 Files touched]`
- **Hand-off:** spec-to-code
- **Before:** §4 "### Data model" gives an `[[edge]]` row the keys of PLAY-dOrderedCharter-24's rows and S1 names `instructions.edit` as `promoted-from`'s one writer; §4 "### Inventory" mints seven adapters, `resolve_edge`, `read_text_history`, `--check` and the leg; S5 reads a `gov:note` line's `refs=` segment "in the edge-target form" with no type; §4 "### Files touched" names nine files.
- **After:** an `[[edge]]` row carries an optional `writer` key, `promoted-from`'s `instructions.edit`, which `check_edges` reads; `edge_grammar.py` also defines the readers and helpers the check needs (`read_toml_rows`, `read_trailer_keys`, `read_native_classes`, `derive_native_class`, `read_native_members`, `derive_target_fault`, `check_site_targets`, `check_native_classes`, `derive_unit_texts`, `derive_view_texts`, `build_resolve_context`, `read_tag_rows`, `run_resolve`, `read_tree_edges`, `run_check`, `read_site_edges`, `resolve_repo_root`, `build_resolve_fixture`, `run_fixture`) and the flag `--base`; a note's refs are typed as the derived `cites` edges, and a `Decided:` trailer as a `decides` edge to its commit with the decision text as its source; the files touched also hold `tools/playbook/gov_tag.py` (its summary prints the native classes), `tools/playbook/adopt-playbook.sh` (the plants' selftest rows), `tools/govkit/usage.toml` and `help/tags.md` (the CLI's flags and the page), `memory/guides/SESSION-KICKOFF.md` (the re-stamp a `tools/gate-legs.json` edit owes) and the generated map; the playbook render selftest's guard gains `tools/memory-tree/corpus_ids.py`, the `family-id` resolver its `resolve-family` plant runs.
- **Cause:** builder discovery
- **Reason:** a writer named in S1 needs a field a row can hold for `check_edges` to read; the native rows' `pattern` and `resolver` are names to import and run, and the pins' revisions, the resolve plants' scratch repository and the tree's sites each need a reader of their own; a code note's references are what the derived `cites` type records; a `Decided:` value is prose, never an address, so the commit is its target; a leg a guard does not name would go unrun when the resolver it calls changes.
- **Evidence:** `--check --base ce13efbe` over the tree read 9241 edges, 0 red; every new name passed `lexicon.py --suggest --as py.function`; the fifteen new selftest rows and the twenty-three existing edge rows ran 38 ok by a loop over their own fields.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-28
