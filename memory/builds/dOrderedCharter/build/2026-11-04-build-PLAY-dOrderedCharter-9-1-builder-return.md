# dOrderedCharter — unit 9's builder return

**Serves:** journal PLAY-dOrderedCharter-9

Run wf_f3df09fc-2cf, summarized from its return.

- Built at rev-5 as pass commit `bad313dc5`, over 16 files.
- `tools/playbook/instruction_units.py` gains:
  - `Unit` and `UnitRowError`;
  - `parse_unit_rows`, the one parser of a manifest's text at any revision;
  - `derive_manifest_kind`, the one test for which paths are manifests;
  - `read_units`, whose origin comes from the kit's `kit.toml` id;
  - unit selection and rendering.
- `extract_unit` and `extract_repo` move beside the parser, so the extractor version covers it. The two namespace
  rows, the extractor table and the fixture registry row follow, and `derive_unit_rows` is deleted.
- `tag_index`'s extractor lookup finds a module in its own kit when a fixture registry lacks it.
- `edge_grammar.py` reads unit rows through the one parser and reads `scope`, never `select`. A string enforced-by
  value yields no edge.
- The grammar leg's unit half grades every row the reader returns, and prints unarmed on a tree with none.
- Owed by unit 12, done:
  - `read_lock` refuses a non-table target entry by name, and the lock plant covers it;
  - the session-kickoff dossier names the lock.
- Deviation 94, `author-recorded`, holds four departures. The notable one: `tools/playbook/tag_bundle.py`'s fixture
  spelled the selector `select`, a third reader the spec's Readers clause missed, and it now spells `scope`.
- Observed by probe:
  - All 12 module plants are green.
  - Three injected breaks red `two-kits`, `render` and `unreadable`.
  - AC4 and AC6 greps.
  - The affected `gov_tag` and `edge_grammar` plants.
  - The lexicon is back at its pin after one rename.
- No divergence.
- Owed at the close:
  - The tags, edges and grammar legs over the tree.
  - The section-7 legs.
  - RED then GREEN for the `New arm:` line on `instruction_units.py`.
