**Serves:** research TOOL-dSafePassage-92 TOOL-dSafePassage-93

# Brief: fold the round-1 spec audit of 92 and 93 into both specs

## The prompt

> The round-1 spec audit of TOOL-dSafePassage-92 and -93 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-92-93-spec-audit-round1.md`) returned CLEAN WITH FIXES: 0 blockers, 1 high, 4 medium and 8 low items, precision 1.0. Neither unit is built yet, so every item folds into its spec before 92's builder starts.

## The brief

### Goal
Fold every confirmed item of the audit record into the spec it names, at the fix the record's skeptic judged sound (the skeptic's corrected fix for ids 3 and 14). Each spec edited gets a rev bump and one §9 line naming the audit record and this brief. Verify every cited line at `f9b39338f` before citing it.

### Items
- **92:** H1 (id 6) and M1 (ids 1, 12), one defect: forgive a FileNotFoundError or OSError only when the tail shows a `subprocess.py` frame, with a sixth `[dSP-92]` shape for the missing-module case. Also M2 (id 7), M3 (id 13), L1 (id 2), L2 (id 3).
- **93:** M4 (id 14), L3 (ids 4, 10), L4 (id 5), L5 (id 8), L6 (id 9), L7 (id 11), L8 (id 15).
- **Write sets.** Where a fold changes a unit's Files touched, update that list.
- **Left-shift gates.** List each item's checklist entry in your return for the main loop; do not author them.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
Each confirmed item is folded into exactly one spec's text, or refused with its reason. Every spec edited stays conforming, with §8 `none` or only RESOLVED forks. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in each §6 is tracked by git, and no backticked §6 token is a bare suite path such as `tools/govkit/selftest.py` (the spec-token check reads one as a suite run).

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
