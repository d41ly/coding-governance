**Serves:** research TOOL-dRankedPlan-65

# The promoted-fix pass's return — dRankedPlan round 6

The gov-spec-writer return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-65-1-spec-writer.md`, over `memory/builds/dRankedPlan/prompts/2026-10-27-prompt-TOOL-dRankedPlan-65-promoted-fix-brief.md`, extracted from its transcript by script, never retyped.

TOOL-dRankedPlan-65 is fixed with a one-word change, and the hygiene re-run (`--only 2,12,25`) exits 0 and reports no check 25 finding against unit 65 or any of units 63 to 67.

**What tripped check 25.** In §2, item S1 said `shlex.split(word, posix=True)`, "which removes double quotes". The phrase "removes" is on check 25's retirement list (`tools/memory-tree/check-memory-hygiene.sh:2204`). The same item also holds backticked names like `read_shell_callers`, which the check reads as named things (`:1992`). Put together, the check took S1 for a retirement with no `**Readers:**` clause.

**Why I reworded instead of adding a Readers clause.** S1 doesn't retire anything. It describes how `shlex` handles quoting, so the brief's reword branch applies.

**The change.** In `C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\2026-10-27-spec-TOOL-dRankedPlan-65.md`, §2 S1:
- before: `` `shlex.split(word, posix=True)`, which removes double quotes and turns ``
- after: `` `shlex.split(word, posix=True)`, which strips the double quotes and turns ``

"strips" isn't on either retirement list. Nothing else in the file changed: not the status header, the derived/carries lines, the §3 edges or any §8 mark. S2 and S3 contain no retirement words.

**Re-run result.** The run ends with `HYGIENE --only 2,12,25 ran checks 2 12 25`. It still prints some "check 25 did not grade `<name>` — READER NOT IN TREE covers it" lines. These are notices that a spec used the check's accepted escape, not findings, and the run still exits 0. Six of them point at older dRankedPlan specs (units 2, 3, 10, 16, 29 and 51), and none at units 63 to 67. I didn't change those six because they were outside the brief.

Nothing is committed.
