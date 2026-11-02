**Serves:** research TOOL-dSafePassage-95

# Brief: fold the round-1 spec audit of 95 into its spec

## The prompt

> The round-1 spec audit of TOOL-dSafePassage-95 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-95-spec-audit-round1.md`) returned CLEAN WITH FIXES: 0 blockers, 1 high, 1 medium and 4 low items, precision 0.89. 95 is not built yet, so every item folds into its spec before its builder starts.

## The brief

### Goal
Fold every confirmed item of the audit record into 95's spec, at the fix the record's skeptic judged sound (the skeptic's corrected fix for id 9). Bump the spec's rev and add one §9 line naming the audit record and this brief. Verify every cited line at `293394394` before citing it.

### Items
- **H1 (id 1) and M1 (ids 3, 5, 8), one defect:** AC3's third command reads red on a correct build because 95's own spec commit re-rendered 94's generated records block. Scope that diff to what the build can change, and say why.
- **L1 (id 2), L2 (id 6), L3 (id 7), L4 (id 9).**
- **Left-shift gates.** List each item's checklist entry in your return for the main loop; do not author them.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
Each confirmed item is folded into 95's text, or refused with its reason. The spec stays conforming, with §8 `none`. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git, and no backticked §6 token is a bare suite path such as `tools/govkit/selftest.py`.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
