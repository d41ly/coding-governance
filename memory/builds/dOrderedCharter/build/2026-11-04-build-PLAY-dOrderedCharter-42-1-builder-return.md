# dOrderedCharter — unit 42's builder return

**Serves:** journal PLAY-dOrderedCharter-42

Run wf_3fb61edf-fc4, summarized from its return.

- Built at rev-5 as pass commit `d582674ce`.
- `tools/memory-tree/tree_lib.py` gains `TYPED_RECORD_KINDS`: deviation, exception, override and change.
  - `RECORD_KIND_TOKENS` is the four untyped kinds plus those.
  - The bindings reader's file-name rule covers every typed kind both ways, only on the stem.
  - The old any-name deviation pattern is gone.
- `tools/memory-tree/build_records.py`:
  - It refuses at import when its `KINDS` differs from the tuple.
  - It enters override and change as pending on units 2 and 15.
  - It shares one `write_record` with the exception writer.
  - It gains a `typed-kinds` round-trip plant.
- The hygiene suite gains one assertion, taking its floor from 673 to 674.
- The hygiene template names the new kinds, and `memory/HYGIENE.md` is re-rendered.
- Generated files rewritten: the build README row, `memory/backlog/PLAY.md` (ask 59 closes with this unit) and
  `symbols.json`.
- Observed by probe:
  - AC1 to AC3 and AC6: scratch repositories and a scratch kit.
  - AC4: the round-trip plant.
  - AC5: the template.
  - The real tree's bindings print 0 malformed rows.
- No divergence.
- Owed at the close:
  - RED then GREEN for the `New arm:` line on the round-trip plant.
  - The suite floor raise, counted by reading.
  - The section-7 legs.
