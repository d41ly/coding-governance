# dOrderedCharter — unit 40's builder return

**Serves:** journal PLAY-dOrderedCharter-40

Runs wf_0bcbd946-e33, wf_57f95f65-147 and wf_93adf4d7-c27, summarized from their returns.

- The first two runs were refused at `--dispatch` by the order gate before any product write: unit 39, earlier in the order and
  deferred behind parked unit 31, counted as blocking. Spec 40 rev-5 moved the unit into unit 39's order group at `79cbe6800`.
- Built at rev-5 as pass commit `c91c26904`, with no hand-back; spec 40 rev-4 had folded a read-only pre-check against HEAD.
- What the unit landed:
  - `tools/playbook/instructions.toml` with gov's first four unit rows, one per reference page, each written as the edit door's
    `propose add` prints it, with a change record per row.
  - An `h1` on each of the three reference rows, and the tag index keying a `[[reference]]` row on its `registry` through one map,
    `ROW_TAG_KEYS`, so the `doc` namespace grades each reference row's purpose.
  - Two fixture plants in `tools/playbook/gov_tag.py`, `reference-row` and `reference-no-h1`, with their adopter rows.
  - `help/tags.md` and `help/concepts/instruction-layer.md` brought current, recorded as deviation 402.
- Observed by probe: the four unit tags resolve, each change record reads back, the two plants answer as specced, the reference pages
  render without drift, and gov's charter re-renders byte for byte.
- The pass also committed the dClosedLoop as-built view, which the index generator rewrote and the pre-commit hook required.
- Owed at the close: RED then GREEN for the two plants; the tags leg, the reference check, the layers check and the core meta-check,
  which the builder role may not run.
