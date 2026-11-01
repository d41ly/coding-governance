**Serves:** research TOOL-dSafePassage-101

# Brief: fold the round-1 spec audit of 101 into its spec

## The prompt

> The round-1 spec audit of TOOL-dSafePassage-101 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-101-spec-audit-round1.md`) returned CLEAN WITH FIXES: 0 blockers, 0 highs, 6 medium and 7 low items over 19 confirmed findings, precision 1.0. 101 is not built yet, so every item folds into its spec before the builder starts. 99's rev-3 edit (S1) is already committed at `a78d6affc`.

## The brief

### Goal
Fold every item of the audit record into 101's spec, at the fix the record's skeptic judged sound (the skeptic's corrected fix where it rejected the finder's, as for M6). The spec gets a rev bump and one §9 line naming the audit record and this brief. Verify every cited line at `a78d6affc` before citing it.

### Items
- **Medium:** M1 (id 1), M2 (id 2), M3 (id 3), M4 (ids 8, 16), M5 (id 11): answer TOOL-dSafePassage-83's three reasons in 101's "The edge ruling", or take 83's side if the reasons stand; M6 (id 13): AC1 observes 99's rev-3 header at `a78d6affc`.
- **Low:** L1 (ids 10, 14), L2 (ids 4, 9, 18), L3 (id 5), L4 (ids 6, 17), L5 (ids 7, 19), L6 (id 12), L7 (id 15).
- **Write sets.** Where a fold changes Files touched, update that list.
- **Left-shift gates.** List each item's checklist entry in your return for the main loop; do not author them.

### Non-goals
No product code; no edit to any other spec (99 is already at rev-3); no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
Each item is folded into 101's text, or refused with its reason. The spec stays conforming, with §8 `none` or only RESOLVED forks. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git, and no backticked §6 token is a bare suite path or a code fragment that embeds a repository path.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
