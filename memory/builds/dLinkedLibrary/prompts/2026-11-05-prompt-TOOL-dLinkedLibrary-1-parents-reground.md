**Serves:** research TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-22

# Brief: dLinkedLibrary's specs re-grounded against the parent revisions the cross-check of 2026-11-05 read

## The prompt

> Write re-ground briefs and `gov-spec-writer` folds with rev bumps, §9 lines and spec-revised
> deviation records. Parent-text errors are reported, never edited.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask for a
cross-read of seven chain builds against the parent revisions `63669d505`, `66f7b8d32` and `58b395b6e`.

## The brief

### Goal

Revise TOOL-dLinkedLibrary-1, -8, -13 and -22 so their one citation of TOOL-dTotalRecall-1 S9's verb names the section, not a line that the parent's generated region moved. No design changes.

### Items

Read the cross-check record first, `memory/builds/dLinkedLibrary/build/2026-11-05-build-TOOL-dLinkedLibrary-1-parents-crosscheck.md`. Its rows name each MISMATCH; the readers' returns in `memory/builds/dLinkedLibrary/build/2026-11-05-build-TOOL-dLinkedLibrary-1-crosscheck-returns.md` quote both sides and state the change. The specs are read at the branch tip, which holds the owner's fork picks of 2026-11-05 merged after the readers ran: re-read both sides of every row before you edit, against today's text. A row the parent's text does not bear out, or that a fork pick already settled, is not edited: return it as refused, with the line that refutes it. Cite a parent by section, not by line, wherever you touch a cite.

One writer per group below. The spec your task block's `input:spec` names leads one group: revise every spec of that group and no other.

#### Group A, led by spec 1: specs 1, 8, 13 and 22

- **Rows 3, 9, 17 and 24.** ll1 (its `decision` row registration), ll8 (its column note), ll13 S1 and ll22 S1 cite `TOOL-dTotalRecall-1:101-102` for S9's verb taking no flag for the other columns. Since `58b395b6e`, tr1:101-102 is S8's text and S9's flags sit four lines lower. Re-cite each as `TOOL-dTotalRecall-1 S9`. If any other `TOOL-dTotalRecall-1:<line>` or `TOOL-dTotalRecall-2:<line>` cite in these four specs now points at a moved line, correct it the same way and name it in your return as writer-found.

### Acceptance

- `wc -c` of every spec you revise is under 49152.
- Each revised spec's **Status:** line carries its next rev and the date `2026-11-05`, every other
  field kept, and its §9 holds one new line in the existing form: `- rev-<n> · 2026-11-05 · <sections>
  · <what moved>, by the brief prompts/2026-11-05-prompt-TOOL-dLinkedLibrary-1-parents-reground.md`.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your
  specs staged into it through `GIT_INDEX_FILE`, names nothing of your specs. Delete the copy after.
  Findings that only a `gen_build_index.py --write` render cures belong to the main loop: name them and
  leave them.

### Gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### Non-goals

- No file outside the specs your group names. No commit, no stage into the real index, no deviation
  record: the main loop writes those.
- No file of another build. A parent spec that looks wrong is a line in your return, not an edit.
- No fork opened or re-opened; a fork the owner's picks resolved stays resolved as written.
- No change to what a unit builds beyond what an item states.

### Reuse

The parents' specs as the interface; the cross-check record as the map of what moved. `memory/builds/dShippedRelease/prompts/2026-11-03-prompt-DEPL-dShippedRelease-1-parents-reground.md` is the most recent precedent.
