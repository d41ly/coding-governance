**Serves:** research TOOL-dWitnessedBar-97

# Round-14 H1 pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-97-1-spec-writer.md`, run direct/a7c795f16da3cd2f7, one per stop, extracted from its transcript by script.

## Return 1

I shortened unit 97's H1 to 255 bytes, newline included, which meets the "at most 255" limit with no bytes to spare. The new H1:

### TOOL-dWitnessedBar-97 — the round-1 audit of units 91 and 92, 10 minors batched: derivation notes naming launcher, exit and script, an isolated third clone, pass commits read through the shipped seams, unit 91's note graded and every unit ledger read

It is 254 bytes without the newline, down from 293. The prefix and em dash are kept, and all five themes are still there. The cuts were "that name their" to "naming", "every pass commit" to "pass commits", "by the note check," dropped, and "every ledger of a unit" to "every unit ledger".

- **The change:** only line 1 of `C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-97.md` changed (1 insertion, 1 deletion). It stays at rev-1, and I touched no other spec or deviation record. Nothing is staged or committed: the file shows `AM`, and my edit is only in the working tree.
- **Hygiene gate:** it still exits 1, because I did not run `gen_build_index.py`. Check 7 still sees the old 380-character row in `memory/builds/dWitnessedBar/README.md`. Check 9 marks that README and the unit-97 spec as stale against a fresh render, so it will stay red until the index is regenerated.
- **Predicted row length:** I swapped the new title into the current row and it comes to 340 characters by my count, about 342 by the checker's. The checker's count runs 2 above mine (it reports 380 for a row I measure at 378). Either way it is under the 350 cap.
- **Lexicon:** `lexicon.py --check` exits 0, but it treats `.md` files as `dark`, so it did not check this H1 at all.

Before committing, whoever dispatched me needs to run `python tools/memory-tree/gen_build_index.py --write` and then re-run `bash tools/memory-tree/check-memory-hygiene.sh` to confirm checks 7 and 9 clear.
