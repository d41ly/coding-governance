# dOrderedCharter — unit 68's builder return

**Serves:** journal PLAY-dOrderedCharter-68

Run wf_98666c84-1aa, summarized from its return.

- Built at rev-1 as pass commit `dd7213e94`.
- What the unit landed:
  - `tools/playbook/tag_index.py#scan_unfenced` reads through `tree_lib.unfenced_lines` and reports the line an unclosed fence opens on.
  - `extract_citations` writes an `unclosed` row, and the new `check_unclosed` reds it outside `memory/builds/` and prints it for a frozen record.
  - Two plants, `unclosed-fence` and `unclosed-record`, with their rows in `adopt-playbook.sh`'s tag plant table.
  - `help/tags.md`, `tools/playbook/README.md` and the bug-class record name the new red.
- Owed by unit 67, done: `py_reads.py`'s nested `gaps` is `derive_gaps`, and the lexicon prints `lexicon OK`.
- Observed by probe:
  - AC1 and AC2, each red before the change.
  - AC3 exits 1 and AC4 exits 0 on their plants.
  - The `none` and `scope-guide` plants unchanged.
  - AC6's counts, syntax checks, and the lexicon.
- No divergence.
- Owed at the close:
  - AC5: the tags leg over the tip, printing the frozen line for dFramedEntrypoint's enforcement record.
  - RED then GREEN for the two new plant rows.
  - The section-7 legs, and `py_reads.py --selftest` for the rename.
