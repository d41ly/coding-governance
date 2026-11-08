# dOrderedCharter — unit 72's builder return

**Serves:** journal PLAY-dOrderedCharter-72

Run wf_bb6c9e92-101, summarized from its return. Run wf_e62ccbb1-b49 handed back before any write, and rev-2 kept `FIXTURE_KIT` and its eighteen readers.

- Built at rev-2 as pass commit `60bbf65b2`.
- What the unit landed:
  - `positional-refs.txt` and `positional-producers.txt` moved byte for byte to `memory/project/`, and `tools/playbook/positional.py` finds them through the memory root.
  - `tools/playbook/tag_index.py` resolves the `{prefix}` token, and `namespaces.toml` spells all 12 kit paths with it.
  - Every fixture and tool that spelled the kit's path derives it from its own location.
  - The hygiene engine admits the positional list by name, and `.memory-tree.conf` registers the producer list.
- Observed by probe:
  - AC2: the positional check exits 0 with the same counts as before the move.
  - AC3, by the ban's counter run over the 19 files: from 70 spellings to none.
  - AC7: memory hygiene's index and pin checks exit 0.
  - AC1, AC4, AC5, AC10 and AC11 greps, and AC6 and AC9 by in-process runs.
  - The lexicon at its pin of 1209.
- No divergence, and no deviation record.
- Owed at the close:
  - The install-prefix, drift-audit, dead-path, method-carrier and tags legs.
  - AC9's six suite runs, and the scratch install for AC6.
  - RED then GREEN for both `New arm:` lines.
