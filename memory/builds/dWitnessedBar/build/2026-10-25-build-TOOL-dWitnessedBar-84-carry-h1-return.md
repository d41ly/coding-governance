**Serves:** research TOOL-dWitnessedBar-84

# Carry-forward H1 pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-84-1-spec-writer.md`, run direct/acd75a39333c42ca9, one per stop, extracted from its transcript by script.

## Return 1

I've shortened unit 84's H1 by 11 bytes, so its index row should drop from 353 to 342 characters, under the cap of 350. I couldn't confirm that number, because I wasn't allowed to re-render the index. The hygiene gate still fails (rc=1), with the two expected reds described below.

**New H1** (250 bytes, was 261):

### TOOL-dWitnessedBar-84 — the round-1 audit of units 74 to 78, 16 minors batched: single-copy checks reading what exists, a sed admitting the quoted arm, honest return codes, counted loops, one key derivation, the guide guarded, records on one line

All 11 bytes removed are ASCII, so the row loses 11 characters too. The `# TOOL-dWitnessedBar-84 — ` prefix and its em dash are unchanged, and all seven fixes are still named. The cuts were:
- "its 16" became "16"
- "that read" became "reading"
- "that admits" became "admitting"
- "guarded and records" became "guarded, records"

**Revision log:** I added one line to the existing rev-3 entry in §9 and did not bump the rev: `The H1 is shortened to fit the build index's row cap; nothing else moved.`

The Status line (DEFERRED · rev-3) is left as it was. No other spec or deviation record was touched, nothing is staged or committed, and I didn't run the build-index generator.

**Gate results:**
- **Lexicon** (`python tools/lexicon/lexicon.py`): passes, rc=0.
- **Memory hygiene** (`bash tools/memory-tree/check-memory-hygiene.sh`): fails, rc=1, on two checks. Both should clear once you re-render the index:
  - **Check 7:** `memory/builds/dWitnessedBar/README.md:175 (353 chars > 350)`. The README still shows the old title because it hasn't been re-rendered.
  - **Check 9:** the README and the unit-84 spec both differ from a fresh render. The README lags the new H1. The spec's other change is in its auto-generated list of records (the `gen:spec-records` table), which comes from records that name unit 84, not from the title. Most likely the staged brief prompt, which declares `**Serves:** research TOOL-dWitnessedBar-84`, is now one of those records, so this part predates my edit.

Running `python tools/memory-tree/gen_build_index.py --write` when you commit should fix both.

File changed: `C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-84.md`
