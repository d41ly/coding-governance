**Serves:** research TOOL-dTotalRecall-1 TOOL-dTotalRecall-11 TOOL-dTotalRecall-25

# Brief: dTotalRecall's specs re-grounded against the parent revisions the cross-check of 2026-11-05 read

## The prompt

> Write re-ground briefs and `gov-spec-writer` folds with rev bumps, §9 lines and spec-revised
> deviation records. Parent-text errors are reported, never edited.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask for a
cross-read of seven chain builds against the parent revisions `63669d505`, `66f7b8d32` and `58b395b6e`.

## The brief

### Goal

Revise TOOL-dTotalRecall-11 and -25 so what they say of dDeclaredLoop's `review.cost` row and of TOOL-dTotalRecall-2 S9's door agrees with those specs as they stand. Neither unit's build changes.

### Items

Read the cross-check record first, `memory/builds/dTotalRecall/build/2026-11-05-build-TOOL-dTotalRecall-1-parents-crosscheck.md`. Its rows name each MISMATCH; the readers' returns in `memory/builds/dTotalRecall/build/2026-11-05-build-TOOL-dTotalRecall-1-crosscheck-returns.md` quote both sides and state the change. The specs are read at the branch tip, which holds the owner's fork picks of 2026-11-05 merged after the readers ran: re-read both sides of every row before you edit, against today's text. A row the parent's text does not bear out, or that a fork pick already settled, is not edited: return it as refused, with the line that refutes it. Cite a parent by section, not by line, wherever you touch a cite.

One writer per group below. The spec your task block's `input:spec` names leads one group: revise every spec of that group and no other.

#### Group A, led by spec 11: specs 11 and 25

- **Row 7, tr11 §3, the writers of `new shape-run`.** tr11 §3 names TOOL-dDeclaredLoop-20's `review.cost` act row as a caller of `gov_record.py new shape-run`; dl20 S3 limits `review.cost` to the shape line's four fields and no dDeclaredLoop spec calls the verb. §3 stops naming dl20 as a caller; it states that no parent spec owns the review-act writer yet, a later unit or an ask does, and that TOOL-dWellOiledMachine-19 calls the `--act` form.
- **Rows 10 and 11, tr25 §8 F2 and the §3 non-goal, the `fence` row's writer.** Both say tr2's door replaces the `stream-plan` row's `hand` writer when the planner lands. Since TOOL-dTotalRecall-1 rev-5, tr2 S9 moves only `fields`-form `hand` rows and names the owner of every other row's door in its pass's `Decided:` trailer. F2 (resolved as it stands, its pick untouched) and the non-goal say the `fence` row keeps `hand` through tr2 S9, that trailer names dIndexedDesign's planner as the door's owner, and the writer cell moves when that planner lands its own verb, not through tr2's door.

### Acceptance

- `wc -c` of every spec you revise is under 49152.
- Each revised spec's **Status:** line carries its next rev and the date `2026-11-05`, every other
  field kept, and its §9 holds one new line in the existing form: `- rev-<n> · 2026-11-05 · <sections>
  · <what moved>, by the brief prompts/2026-11-05-prompt-TOOL-dTotalRecall-1-parents-reground.md`.
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
