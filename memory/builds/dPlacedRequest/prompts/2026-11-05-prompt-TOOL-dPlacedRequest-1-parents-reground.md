**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-5

# Brief: dPlacedRequest's specs re-grounded against the parent revisions the cross-check of 2026-11-05 read

## The prompt

> Write re-ground briefs and `gov-spec-writer` folds with rev bumps, §9 lines and spec-revised
> deviation records. Parent-text errors are reported, never edited.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask for a
cross-read of seven chain builds against the parent revisions `63669d505`, `66f7b8d32` and `58b395b6e`.

## The brief

### Goal

Revise TOOL-dPlacedRequest-5 so its hand-out hold agrees with TOOL-dDeclaredLoop-20 S7 as it stands. The unit keeps its design; only the cause its Design-exit audit fires with, and the criterion that observes the hold, change.

### Items

Read the cross-check record first, `memory/builds/dPlacedRequest/build/2026-11-05-build-TOOL-dPlacedRequest-1-parents-crosscheck.md`. Its rows name each MISMATCH; the readers' returns in `memory/builds/dPlacedRequest/build/2026-11-05-build-TOOL-dPlacedRequest-1-crosscheck-returns.md` quote both sides and state the change. The specs are read at the branch tip, which holds the owner's fork picks of 2026-11-05 merged after the readers ran: re-read both sides of every row before you edit, against today's text. A row the parent's text does not bear out, or that a fork pick already settled, is not edited: return it as refused, with the line that refutes it. Cite a parent by section, not by line, wherever you touch a cite.

One writer per group below. The spec your task block's `input:spec` names leads one group: revise every spec of that group and no other.

#### Group A, led by spec 5: spec 5

- **Row 6, S6 and S7, the hold under `owed-only`.** pr5 S7 holds the roster's hand-out until a placed audit's verdict is terminal, while S6 fires that audit with `--cause placement`, and dl20 S7 holds the hand-out under `review.blocks = owed-only` only for the cause `owed` (dl20 S7; its §4 "Rollout" paragraph). Fold, decided: S6 fires the Design-exit audit with `--cause owed` once `AUTH_SPEC_AUDIT_FROM` holds `placement`, since the preflight's owed line AC1 reads already says the audit is owed there, and keeps `--cause placement` for the at-once firing past the position. S7 states the hold as dl20 S7 gives it for each `review.blocks` value. AC1 or AC6 gains a plant under `review.blocks = owed-only` that reds when the hand-out is not held at the position.

### Acceptance

- `wc -c` of every spec you revise is under 49152.
- Each revised spec's **Status:** line carries its next rev and the date `2026-11-05`, every other
  field kept, and its §9 holds one new line in the existing form: `- rev-<n> · 2026-11-05 · <sections>
  · <what moved>, by the brief prompts/2026-11-05-prompt-TOOL-dPlacedRequest-1-parents-reground.md`.
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
