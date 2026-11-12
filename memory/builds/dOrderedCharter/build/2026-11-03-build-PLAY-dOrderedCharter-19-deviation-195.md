# PLAY-dOrderedCharter-19 deviation 195 — the resolver's helpers, its fixture's plants and its output lines, as built

**Serves:** deviation PLAY-dOrderedCharter-19

- **Departs from:** `PLAY-dOrderedCharter-19@rev-8 [§2 S11, S13, §4 The CLI, §4 Inventory]`
- **Hand-off:** spec-to-code
- **Before:** §4 "### Inventory" mints the ten functions it names; S13's fixture has "a three-row registry"; §4 "### The CLI" says every line opens `tags:`; S11 targets each alias at a `doc.<name>#<seg>` section.
- **After:** `tag_index.py` also defines the readers, writers and view builders the index needs (`load_extractors`, `derive_heading_seg`, `scan_unfenced`, `read_git_stdout`, `read_git`, `load_memory_tree`, `load_index`, `derive_context`, `_write_parsed`, `_write_path_rows`, `_derive_applicable`, `read_worktree_trees`, `remove_unheld_rows`, `build_overlay`, `load_view`, `read_rows`, `read_text_of`, `read_aliases`, `read_population`, `derive_namespace_state`, `_derive_span_ns`, `check_owned`, `read_layer_kinds`, `read_index_rows`), and `gov_tag.py` its CLI and fixture helpers; `map_lib.py` carries an inline `resolve_kit_dir` copy to find memory-tree; the fixture registry holds three rows, `doc`, `practice` and `layer`, and the two `scope` plants add a fourth, `unit`, so a `unit.x` citation has an unarmed namespace to count into; each plant is one case run under one `--set` value per call, the cases being `none`, `rebuild`, `two-paths`, `dirty`, `one-commit`, `slice`, `retired`, `retired-old`, `retired-reminted`, `bare`, `bare-charter`, `owned`, `owned-core`, `scope` and `scope-guide`; `--list-positional` prints the bare `<path>\t<ref>` rows `positional-refs.txt` keeps, and every other line, `where`'s included, opens `tags:`; the summary also counts the paths outside Markdown not read; each `HYGIENE check <n>` alias targets the check catalog's `##` section.
- **Cause:** builder discovery
- **Reason:** a blob-keyed index whose rows a path names needs a path-independent row form and a way to name it per path; the hygiene checks are numbered items of one section and no `##` heading of their own; a row file `--list-positional` seeds cannot carry a prefix its rows lack; codebase-map spells no sibling kit's path, so it finds memory-tree's module the way the playbook kit finds the roles kit.
- **Evidence:** the hygiene catalog's 29 checks are `<n>. **…**` lines under `## The check catalog`; every new name but the five moved ones passed `lexicon.py --suggest`; the index over gov's tree held 313,840 span rows and measured about 180 MB on disk after a 35.5 s cold build.
- **Risk:** additive
- **Approver:** author, the unit's builder, recorded in this pass commit under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-38
- **Caused-by:** PLAY-dOrderedCharter-19
