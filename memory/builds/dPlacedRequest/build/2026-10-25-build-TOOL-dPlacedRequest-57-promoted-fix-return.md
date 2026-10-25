**Serves:** research TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59

# The promoted-fix pass — dPlacedRequest round 6, its return

The return of the gov-spec-writer dispatched from `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-11-spec-writer.md`, run direct/a830fb708d0525972, extracted from its transcript by script.

I fixed the one check-25 hit by rewording TOOL-dPlacedRequest-58's S1. The hygiene gate (`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`) now exits 0 with no check-25 hit, and TOOL-dPlacedRequest-58 does not appear in its output.

**The hit and its disposition:** S1 was flagged because it said "removes" next to the backticked handshake paths `$h/once`, `$h/held` and `$h/release`. S1 doesn't retire anything named. It clears the test arm's temporary handshake files at the end of each attempt. Following the brief's second branch, I reworded the item rather than adding a `**Readers:**` clause. "removes" became "clears", and none of check 25's retirement words remain in S1 or S2. Nothing about what S1 does, or how it is observed (AC1, AC2), changed.

**Edits to TOOL-dPlacedRequest-58:**
- S1: "removes" became "clears".
- Status header: rev-1 became rev-2.
- §9: added a rev-2 line recording the reword and why S1 owes no `**Readers:**` clause.

The gate also printed "did not grade" notices for check 25 on other builds' specs and on units -3, -33, -34 and -43. These are existing "READER NOT IN TREE" cases, not failures, and are outside this brief. I made no other edits, no product code, no commit, no index render and no binding line. My edit is in the working tree and not re-staged.

File: C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-58.md
