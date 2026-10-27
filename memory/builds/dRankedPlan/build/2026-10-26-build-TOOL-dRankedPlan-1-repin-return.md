**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-9

# The re-pin pass's return — dRankedPlan

The gov-spec-writer return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-4-spec-writer.md`, over `memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-repin-brief.md`, extracted from its transcript by script, never retyped.

I made all three fixes in place and committed nothing. The hygiene check (`check-memory-hygiene.sh --only 2,12,25`) exits 0 with no findings.

**TOOL-dRankedPlan-5** (`C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-5.md`)
- Line 5 now reads `**Carries:** cl-dClosedLoop-0373@70fb5631 whole` → `**Carries:** cl-dClosedLoop-0373@f1eb8c00 whole`.
- `f1eb8c00` is the "now" hash the brief's Items list gives this clause, by deviation 51. The as-built view's row for 0373 (line 386) holds the amended text and names deviation 51.

**TOOL-dRankedPlan-9** (`C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-9.md`)
- Line 5 now reads `**Carries:** cl-dClosedLoop-0377@fd363a7f whole` → `**Carries:** cl-dClosedLoop-0377@a78b3ac9 whole`.
- `a78b3ac9` is the "now" hash the Items list gives this clause, by deviation 91 (view line 390).
- I left deviation 91 untouched. Its line 14 still reads `amends cl-dClosedLoop-0377@fd363a7f`.

**TOOL-dRankedPlan-6** (`C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-6.md`)
- The fixture is now named `2026-10-27-build-TOOL-dX-1-plan-1.md` instead of `2026-10-27-build-TOOL-dX-1-plan.md`, in both places it appears: the §4 example at line 114 and AC3 at line 186. This matches unit 16's `<date>-build-<FAMILY>-<slug>-1-plan-1.md` (unit 16 lines 38 and 320).
- No other place in unit 6 spells the name. Its §4 note and its §5 "Alternatives rejected" both say it reads the plan kind from `**Serves:**` and never from a filename.
- The fixtures and probes still hold with the new name. I checked them against `tools/workflows/tier2-review.template.js`:
  - `SPEC_SUBJECT_PATH = /(?:^|\/)builds\/[^/]+\/spec\//` (:317) still does not match a path under `build/`, so the record is still served as a bare design-document subject (:428-434).
  - `PIN_ID` (:416) tests the subject's `id` field, not its filename, so the anchor `TOOL-dX-1` still matches.
  - AC1 and AC2 key on the `**Serves:**` line, so the name change does not touch them.

**Hygiene check**
- Checks 2, 12 and 25 ran and the script exited 0. The full output is in `C:\Users\DAILY-~1\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-unattended-drankedplan-1fc3d7\43fa2011-5bb6-422a-bd52-776c30d97bd4\scratchpad\hyg.txt`.
- Five lines do name dRankedPlan files: units 2, 3, 10 and 16. They are check 25's informational "did not grade … READER NOT IN TREE covers it" notes about `loop_table.py` and `derive_position`, not findings, and the same kind of note appears for other builds.
- No line names units 5, 6 or 9.

I did not re-run `tools/check-spec-tokens.py`. My brief limits me to the hygiene and lexicon gates, so confirming that its two stale-pin hits are gone is for the main loop.
