**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-3

# Brief: dRankedPlan's specs re-grounded against the parent revisions the cross-check of 2026-11-05 read

## The prompt

> Write re-ground briefs and `gov-spec-writer` folds with rev bumps, §9 lines and spec-revised
> deviation records. Parent-text errors are reported, never edited.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask for a
cross-read of seven chain builds against the parent revisions `63669d505`, `66f7b8d32` and `58b395b6e`.

## The brief

### Goal

Revise TOOL-dRankedPlan-3 so its triage pass writes only where TOOL-dTotalRecall-2's door lets it mint. The unit keeps its design; S5 gains the rule for a home build another session holds, and an AC observes it.

### Items

Read the cross-check record first, `memory/builds/dRankedPlan/build/2026-11-05-build-TOOL-dRankedPlan-1-parents-crosscheck.md`. Its rows name each MISMATCH; the readers' returns in `memory/builds/dRankedPlan/build/2026-11-05-build-TOOL-dRankedPlan-1-crosscheck-returns.md` quote both sides and state the change. The specs are read at the branch tip, which holds the owner's fork picks of 2026-11-05 merged after the readers ran: re-read both sides of every row before you edit, against today's text. A row the parent's text does not bear out, or that a fork pick already settled, is not edited: return it as refused, with the line that refutes it. Cite a parent by section, not by line, wherever you touch a cite.

One writer per group below. The spec your task block's `input:spec` names leads one group: revise every spec of that group and no other.

#### Group A, led by spec 3: spec 3

- **Row 6, S5, a home build held by another session.** `triage.py` writes through the door one record per pass per home build it decided an ask in; tr2 mints a `<n>` record only under the home build's lease or claim and refuses one another session holds (tr2 §4 "Minting"). Fold, decided: S5 skips a home build another session leases or claims, printing `triage — <home> held by <holder>`, and leaves that home's asks undecided for the next pass; S6's "the build whose folder holds the record" is unchanged. A new AC plants a foreign-held home and reds when the pass writes into it or exits non-zero. Name the holder through the door's own refusal line, not a lease read of the pass's own.

### Acceptance

- `wc -c` of every spec you revise is under 49152.
- Each revised spec's **Status:** line carries its next rev and the date `2026-11-05`, every other
  field kept, and its §9 holds one new line in the existing form: `- rev-<n> · 2026-11-05 · <sections>
  · <what moved>, by the brief prompts/2026-11-05-prompt-TOOL-dRankedPlan-1-parents-reground.md`.
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
