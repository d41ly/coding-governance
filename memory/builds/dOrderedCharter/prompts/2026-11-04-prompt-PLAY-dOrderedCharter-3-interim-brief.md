**Serves:** research PLAY-dOrderedCharter-3

# Brief: spec 3's interim ruling on BUILD-METHOD's envelope

## The prompt

> execute keeping the build unattended

— owner, 2026-11-03. Spec 3's fork F5 is the owner's and it blocks the unit. An unattended run never stops to ask: it rules an
interim option that changes nothing the owner reserves, and it parks the question. The raise is parked already.

## The brief

### Goal

Revise spec 3 so the unit builds with fork F5 still open: BUILD-METHOD's envelope is held, its row and its prose stay untouched,
and the hold is visible, never read as coverage.

### Items

1. **Where you write.** A unit is building in the tree, so edit only this scratch copy:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold5/2026-10-23-spec-PLAY-dOrderedCharter-3.md`. Its base is the tracked spec at rev-7. Write nothing under the repository.
2. **F5 stays OPEN.** Its options, vetoes and recommendation stay. Add the run's interim ruling under it, recorded as an interim,
   never as the fork's resolution. The owner's choice among (a) to (e) stays theirs.
3. **The hold.** `memory/guides/BUILD-METHOD.md` keeps its registry row and carries no envelope.
   - Its source `tools/memory-tree/BUILD-METHOD.template.md` and its row in `tools/template-size-limits.txt` are unchanged by this unit.
   - The row declares the hold, in a field the reader validates. Pick the shape by the fork rule, and record the loser in section 8.
4. **The gate states it.** Every `envelopes --check` run prints the held path and that it is NOT checked, and its count of
   covered documents leaves the held one out. Say in the spec what the gate does not check, because a skip is never coverage.
5. **The hold retires itself.** The gate reds, naming the path, when any of these holds:
   - the held document carries an envelope;
   - the document plus its envelope now fits its row, so the owner has moved it;
   - a second row declares a hold.

   One commit then lands the owner's ruling: the row's move, the envelope, and the hold's deletion. Say so.
6. **Every clause that reads the old state moves with it.** At least S2, S5, S6, S7, section 3's Edges where needed, section 4's
   Inventory, section 5's risks, AC1, AC4, AC5 and AC7, and the sentence ending F5 that says the unit does not build. Add the
   planted cases to `tools/playbook/instruction_units.py#PLANTS`, and an acceptance bullet with its Red when line for each red
   in item 5.
7. **Downstream readers.** Read specs 2, 4, 5, 8, 29 and 49 for anything assuming every registered row carries an envelope. Do not
   edit them. Name each one affected in your return, with what it assumes.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`.
- Add one history line naming this brief, with the S and AC ids it touched.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance
  bullets. An acceptance bullet spells a plain tracked path, with no `#` and no `HEAD:` prefix.
- New text names a section in words, and names a check by what it checks.
- Avoid retirement words in section 2, or add the Readers clause they owe.

### Acceptance

- The scratch copy's rev is 8, F5 still reads OPEN, and the interim is recorded under it.
- Nothing in the scratch copy has the unit moving BUILD-METHOD's row, source or prose.
- Each red in item 5 has an acceptance bullet and a named plant.
- `python tools/memory-tree/check-spec-tokens.py` semantics hold for new tokens: plain tracked paths in acceptance bullets.

### Gates

None run: this is a scratch edit. The main loop live-sweeps the spec before its dispatch.

### Non-goals

- No raise, no trim, and no decision among F5's options.
- No edit outside the scratch copy.
- No code.
