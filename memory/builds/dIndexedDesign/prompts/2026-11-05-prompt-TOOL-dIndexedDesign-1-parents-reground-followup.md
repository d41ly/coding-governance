**Serves:** research TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-13

# Brief: the re-ground's writer-found follow-ups on dIndexedDesign specs 8, 10, 11 and 13

## The prompt

> Write re-ground briefs and `gov-spec-writer` folds with rev bumps, §9 lines and spec-revised
> deviation records. Parent-text errors are reported, never edited.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask for a
cross-read of seven chain builds against the parent revisions `63669d505`, `66f7b8d32` and `58b395b6e`.

## The brief

### Goal

Fold the two defects the re-ground's own writers found in dIndexedDesign specs they did not own:
three `--purpose` texts over TOOL-dTotalRecall-16 S1's 120-byte cap, and spec 8's unversioned
`returns`. Each spec keeps its design.

### Items

The re-ground's group writers returned these; their returns are in
`memory/builds/dIndexedDesign/build/2026-11-05-build-TOOL-dIndexedDesign-1-reground-returns.md`.
Re-read both sides before you edit. An item the parent's text does not bear out is not edited:
return it as refused, with the line that refutes it.

One writer, one group, led by spec 8: specs 8, 10, 11 and 13.

- **Specs 10, 11 and 13, the purpose cap.** TOOL-dTotalRecall-16 S1 holds a purpose `text` to at most
  120 bytes on one line. Spec 10's playbook purpose is 198 bytes, spec 11's playbook-set purpose 132
  and spec 13's `seams` purpose 137. Shorten each to 120 bytes or fewer, keeping what the kind is, and
  where an AC quotes the text, the AC with it.
- **Spec 8, row 99's class.** S11 sets `item.design.decompose`'s `returns` to
  `record-kind.feature-design` with no version, which TOOL-dDeclaredLoop-24 writes as
  `record-kind.<name>@<n>`. Write `@1`, and place its `[[record-version]]` row as spec 20's revised
  S10 places its own: where the per-kind table row it hashes is added, in that unit's pass or later,
  named in the spec that adds it only if that spec is this group's; otherwise state in spec 8 which
  unit's pass adds it and return it as an item for the main loop.

### Acceptance

- `wc -c` of every spec you revise is under 49152.
- Each of these four specs already took its next rev on 2026-11-05 in the same re-ground. Keep that
  rev and date on its **Status:** line, and extend that day's §9 line with this fold's sections and
  what moved, ending `, and by the brief prompts/2026-11-05-prompt-TOOL-dIndexedDesign-1-parents-reground-followup.md`.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your
  specs staged into it through `GIT_INDEX_FILE`, names nothing of your specs. Name the copy uniquely
  inside your scratch directory and delete it after. Findings that only a `gen_build_index.py --write`
  render cures belong to the main loop: name them and leave them.

### Gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### Non-goals

- No file outside these four specs. No commit, no stage into the real index, no deviation record.
- No file of another build. A parent spec that looks wrong is a line in your return, not an edit.
- No fork opened or re-opened.
- No change to what a unit builds beyond what an item states.

### Reuse

Spec 20's revised S4, S7 and S10 and spec 34's revised S3 as the model for the purpose and the
version row.
