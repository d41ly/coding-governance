**Serves:** research TOOL-dSafePassage-104

# Brief: fold the round-1 spec audit of 104 into its spec

## The prompt

> The round-1 spec audit of TOOL-dSafePassage-104 (`memory/builds/dSafePassage/reviews/2026-11-02-review-TOOL-dSafePassage-104-spec-audit-round1.md`) returned CLEAN WITH FIXES: 0 blockers, 0 highs, 2 medium and 4 low items over 6 confirmed findings, precision 1.0. 104 is not built yet, so every item folds into its spec before the builder starts.

## The brief

### Goal
Fold every item of the audit record into 104's spec, at the fix the record's skeptic judged sound. The spec gets a rev bump and one §9 line naming the audit record and this brief. Verify every cited line at the current HEAD before citing it.

### Items
- **Medium:** finding 5 (AC7's second probe reads the commit that must carry its own ledger line; observe it before the commit, or let the main loop observe it after); finding 6 (AC9 names the main sha it grades and checks that `ask#2` is absent, not only that the count meets the pin).
- **Low:** findings 1 (a criterion that observes `derive_answer` stays nested), 2 (§7's guard sentence corrected and the unguarded `policy check` leg named), 3 (§10 quotes reuse_lookup's ranking as it ran, or says it is a selection), 4 (Files touched names 104's own spec, the ledger's path and `memory/backlog/TOOL.md`).
- **Left-shift gates.** List each item's checklist entry in your return for the main loop; do not author them.

### Non-goals
No product code; no edit to any other spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
Each item is folded into 104's text, or refused with its reason. The spec stays conforming, with §8 `none`. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git; no backticked §6 token is a bare suite path, a code fragment that embeds a repository path, or a regex-escaped path.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
