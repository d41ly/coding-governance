**Serves:** research TOOL-dRankedPlan-68 TOOL-dRankedPlan-70 TOOL-dRankedPlan-74 TOOL-dRankedPlan-77

# The promoted-fix pass's return — dRankedPlan round 7

The gov-spec-writer return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-68-1-spec-writer.md`, over `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-68-promoted-fix-brief.md`, extracted from its transcript by script, never retyped.

All the hits in the fix brief are fixed in place, and the hygiene checks named in the brief no longer flag any dRankedPlan file. I changed no status header, `**Carries:**` line, §3 edge or §8 mark, and committed nothing. TOOL-dRankedPlan-68 is the handoff unit but none of the hits were in its spec, so it is unchanged.

**Hit 1: hygiene check 25** (a §2 item with a retirement word beside a backticked token but no `**Readers:**` clause)
- **`2026-10-27-spec-TOOL-dRankedPlan-70.md` S2:** this item retires nothing. "drops" described the bug this unit prevents, so I reworded it. "so no reading of a JavaScript extent drops the facts" became "so every reading of a JavaScript extent carries the facts".
- **`2026-10-27-spec-TOOL-dRankedPlan-77.md` S11:** this item doesn't retire a named thing either. It swaps a prose sentence in unit 66's §4 Inventory for a row. I changed "and drops "No item mints a function"" to "in place of "No item mints a function"", so no `**Readers:**` clause is needed. None of the replacement words are in check 25's trigger list (`check-memory-hygiene.sh:2204-2205`).

**Hit 2: check-spec-tokens `[path]`** (`tools/loop/ratify.py` is not tracked, and `git ls-files` finds no `ratify.py` anywhere)
- **`2026-10-27-spec-TOOL-dRankedPlan-70.md` AC2:** "runs over `tools/loop/ratify.py` at" became "runs over the loop kit's `ratify.py` at".
- **`2026-10-27-spec-TOOL-dRankedPlan-74.md` AC4:** "imports `tools/loop/ratify.py`" became "imports the loop kit's `ratify.py`".
- The full path is unchanged in §2, §4, §7 and Files touched. No other line in §6 of either spec spells `tools/loop/`.

**Checks run after the edits**
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exited 0, with no FAILED line and no finding naming a dRankedPlan file.
- `python tools/check-spec-tokens.py --list` exited 0. For units 68 to 77 it reports only NEAR lines from the guards join, none from the paths join.
- One gap: I didn't capture a clean run from before the edits. My background run of the checker overlapped the edits, so I can't show it red on the paths hit. That hit rests on the main loop's report plus `ratify.py` being untracked.

Files changed:
- C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-70.md
- C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-74.md
- C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-77.md
