**Serves:** research TOOL-dWitnessedBar-88

# Round-10 fix pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-88-1-spec-writer.md`, run direct/aee2e852998b35af2, one per stop, extracted from its transcript by script.

## Return 1

I cleared both `[bar]` hits in TOOL-dWitnessedBar-88. Nothing else in the spec changed. I could not run `tools/check-spec-tokens.py` itself, because my role allows only the hygiene gate and the lexicon. So the main loop's run of that checker is still the real test.

**TOOL-dWitnessedBar-88: authored (edited in place at rev-1, no rev bump)**
File: `C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-88.md`

**What caused the hits.** The checker's `BAR` regex (`tools/check-spec-tokens.py:357-361`) flags any backticked token in an acceptance criterion that starts with a suite path. Two criteria had the suite path alone in backticks, which reads as a call to run the suite:
- **AC3** described cutting the functions out of `` `tools/run-gates/run-gates.gov.test.sh` `` with `awk`.
- **AC5** described a fixture commit that touches `` `tools/run-gates/run-gates.gov.test.sh` ``.

**The fixes.**
- **AC3** now gives the cut as a real command, `awk '/^check_canary_keys\(\)/,/^}/' tools/run-gates/run-gates.gov.test.sh`, "and its like for the other two". Because the token starts with `awk`, it is a probe of the code the unit changes, not a run of the suite. Units 74 and 76 put `check_cr_reached()` and `check_canary_keys()` at column 0 on the built tree, so the range matches there. Neither function is in the current tree yet.
- **AC5**'s fixture commit now "touches the path the `git log` below names". The fixture and its meaning are unchanged; only the bare path token is gone.
- **§7** already has the `New arm: tools/run-gates/run-gates.gov.test.sh` line (covering AC2, AC10 and AC17), so it needed no edit.

**Checks.**
- A scratch copy of the `BAR` regex, run over all 124 backticked tokens in §6, now matches none.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exits 0 and prints no line naming TOOL-dWitnessedBar-88. Its other output is notes about specs in dSafePassage and units 20 and 24 of this build.

No other spec, `order` verb or deviation record was touched. I did not stage, commit or run the index generator.
