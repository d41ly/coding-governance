**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32

# Brief: dDeclaredLoop's specs re-grounded against the parent revisions the cross-check of 2026-11-05 read

## The prompt

> Write re-ground briefs and `gov-spec-writer` folds with rev bumps, §9 lines and spec-revised
> deviation records. Parent-text errors are reported, never edited.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask for a
cross-read of seven chain builds against the parent revisions `63669d505`, `66f7b8d32` and `58b395b6e`.

## The brief

### Goal

Revise TOOL-dDeclaredLoop-20, -21, -30, -31 and -32 so every statement of when a review loop ends and where its findings go agrees with TOOL-dDeclaredLoop-32 rev-3 and TOOL-dFairHearing-17 rev-4: a spec subject takes `no-fall`, ends at its target or bound and is promoted to units, and BUILD-METHOD M4's spec-audit rule disposes its findings and stops its chain; closing-review follow-ups and fix passes keep strict fall and budget routing. dl20 and dl32 are this build's own specs; their fixes here correct the text the rev-3 fold left behind.

### Items

Read the cross-check record first, `memory/builds/dDeclaredLoop/build/2026-11-05-build-TOOL-dDeclaredLoop-1-parents-crosscheck.md`. Its rows name each MISMATCH; the readers' returns in `memory/builds/dDeclaredLoop/build/2026-11-05-build-TOOL-dDeclaredLoop-1-crosscheck-returns.md` quote both sides and state the change. The specs are read at the branch tip, which holds the owner's fork picks of 2026-11-05 merged after the readers ran: re-read both sides of every row before you edit, against today's text. A row the parent's text does not bear out, or that a fork pick already settled, is not edited: return it as refused, with the line that refutes it. Cite a parent by section, not by line, wherever you touch a cite.

One writer per group below. The spec your task block's `input:spec` names leads one group: revise every spec of that group and no other.

#### Group A, led by spec 32: specs 32 and 20

- **dl32, row 28, §4 "byte-for-byte".** The paragraph keeping dl21's four tests says "with neither new argument the function is byte-for-byte its predecessor", though the grammar now gates the second test on `no-fall` and has three new arguments. State that the second test is gated by `no-fall` and that with arguments 4 to 6 unset the behaviour equals dl21's.
- **dl32, row 29, the asks sentence and the Rollout sentence.** "A review loop's open findings go to asks once the budget is spent" becomes a closing-review loop's; "The landing turns the rule on for every subject at once" becomes every closing-review and fix-pass subject.
- **dl32, row 30, S6, check 2.** S6 widens check 2's non-decrease reading to every subject, though check 2's non-convergent red would then fire on a legally flat `no-fall` spec subject. Limit the flat reading to the build slug and fix-pass rows, re-cite the reading by name rather than `:842`, and add to AC7 a plant of a flat, non-terminal spec subject that stays green.
- **dl32, row 31, the edge to dl20.** dl32 says `review.dispose` promotes by the target it writes, while dl20's dispose row routes a new mechanism by the budget. Fold with dl20 below: the edge states that a spec subject's target is always ` · to units`.
- **dl32, row 27 (pre-existing), the `roundLimit` claim.** dl32 says it passes `review.max-rounds` to TOOL-dFairHearing-17's harness as `roundLimit`; no scope item does. Decided: drop the claim, and say no dDeclaredLoop unit takes up fh17's `roundLimit` edge. The edge itself is reported to dFairHearing, whose run is live.
- **dl20, the dispose row and S8, the rev-3 fold's leftovers.** (a) The `item.review.dispose` row sends a spec audit's new-mechanism finding to asks once the budget is spent; state that a spec subject's promotion takes dl32's target, always units. (b) S8, the `item.review.fold` row and AC1 give the fold a NON-CONVERGENT route a `no-fall` spec subject never reaches; replace it with the spec subject's terminal states, BOUNDED or CEILING. (c) The trigger row and the dl32 edge refuse a round past `flow.route-backs` for every subject; limit it to the build slug, as dl32 S2 does. (d) Pre-existing: the dispose row's routes lack the plan-revision and landing-record routes that §3 and the note under the table call its declared routes; add them to the row as declared and unarmed, or make §3 and the note say they are not yet declared, whichever the row's own §3 supports.

#### Group B, led by spec 30: specs 30, 31 and 21

- **dl30, row 17, §3 non-goal.** It gives dl32 "the strict-decrease routing of every `until-*` and `while-*` value". Limit it to `while-*` follow-ups and fix passes, and name BUILD-METHOD M4's spec-audit rule as the owner of a spec audit's stop and disposal.
- **dl30, row 18, S6, the per-item early limit.** Past `flow.route-backs` any item's loop ends `non-converging`, a spec subject included. State that the limit ends follow-up, fix-pass and route-back items only, and that a spec subject's draws are counted but never end its loop (dl32 S2, S3).
- **dl30, row 19, S4, `exhausted`.** Every draw site stops its repetition on `exhausted`. Decided: a spec subject's `review-round` draw is still made and counted, but an `exhausted` answer does not refuse its round; it ends at its target or bound (dl32 S3, S4). Say so in S4 and in the driver paragraph, and add a plant to AC7 or the nearest criterion that reds when a spec subject's round is refused on a spent budget.
- **dl31, row 22, §3 non-goal.** "When a loop ends and where its findings go" is dl32's for follow-up and fix-pass loops; a spec audit's end and disposal are BUILD-METHOD M4's spec-audit rule's. The ` · to on-exhausted` sentence is unchanged.
- **dl21, row 10, §4.** The non-decrease reading applies to the closing-review subject; a spec audit passes `no-fall` (dl32 S3) and ends at its target, BOUNDED or CEILING.
- **dl21, row 11, §3 non-goal.** Name dl32 for follow-ups and fix passes, and M4's spec-audit rule, through dl20's dispose row, for spec audits.
- **dl21, row 14, S4 and F4, the `REVIEW_ROUNDS` readers.** The M4 rewrite left a second mention in `tools/memory-tree/BUILD-METHOD.template.md`, the chain paragraph ("Each generation is a FRESH subject, so `REVIEW_ROUNDS` bounds no chain"). S4 lists both readers and rewords the second so no policy key reads as a chain stop.
- **dl21, row 5 (pre-existing), S3, the parity arm's ceiling.** S3 re-points fh17's parity arm to take the ceiling "as its own variable" but names no value; at the default, fh17's limit-4 row reads CEILING in the driver and BOUNDED in the harness. State that the arm sets the ceiling variable from each row's limit so the driver's ceiling is one round past it, as fh17's harness rule is.
- **dl21, row 7 (pre-existing), the `roundLimit` claim.** Drop the claim that dl32 passes `review.max-rounds` to fh17's harness as `roundLimit` (the non-goal and its edge line), as Group A drops it from dl32.

### Acceptance

- `wc -c` of every spec you revise is under 49152.
- Each revised spec's **Status:** line carries its next rev and the date `2026-11-05`, every other
  field kept, and its §9 holds one new line in the existing form: `- rev-<n> · 2026-11-05 · <sections>
  · <what moved>, by the brief prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-reground.md`.
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
