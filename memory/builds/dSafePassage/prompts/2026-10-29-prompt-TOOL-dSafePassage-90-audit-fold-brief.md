**Serves:** research TOOL-dSafePassage-90 TOOL-dSafePassage-91

# Brief: fold the round-1 spec audit of 90 and 91 into both specs

## The prompt

> The round-1 spec audit of TOOL-dSafePassage-90 and -91 (`memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-90-91-spec-audit-round1.md`) returned CLEAN WITH FIXES: 0 blockers, 0 highs, 5 medium and 5 low items, precision 1.0. Neither unit is built yet, so every item folds into its spec before 90's builder starts.

## The brief

### Goal
Fold every confirmed item of the audit record into the spec it names, at the fix the record's skeptic judged sound (the skeptic's corrected fix for ids 10 and 13). Each spec edited gets a rev bump and one §9 line naming the audit record and this brief. Verify every cited line at `a3ad798cf` before citing it.

### Items
- **90:** M5 (id 13), and 90's half of L1 (ids 3, 5): its ordering note names the block the two units really share.
- **91:** M1 (ids 1, 4, 8, 10), M2 (id 2), M3 (id 11), M4 (id 12), 91's half of L1 (ids 3, 5), L2 (id 6), L3 (id 7), L4 (id 9), L5 (id 14).
- **Write sets.** Where a fold changes a unit's Files touched, update that list.
- **Left-shift gates.** List each item's checklist entry in your return for the main loop; do not author them.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
Each confirmed item is folded into exactly one spec's text, or refused with its reason. Every spec edited stays conforming, with §8 `none` or only RESOLVED forks. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in each §6 is tracked by git.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
