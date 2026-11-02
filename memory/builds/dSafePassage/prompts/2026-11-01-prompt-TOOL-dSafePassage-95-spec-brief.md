**Serves:** research TOOL-dSafePassage-95

# Brief: the round-6 closing review's nine minors

## The prompt

> The round-6 closing diff review of dSafePassage over the round-5 promotion (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-94-closing-diff-round6.md`, recorded as subject dSafePassage-r5-promotions, CONVERGED, precision 0.83) confirmed 9 items: 0 blocker, 0 high, 2 medium, 7 low. BUILD-METHOD M4 batches them into one unit. Item 1 is a red bar leg at the tip and must be closed for the close to go green.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-95, closing all nine items at the fix the review's skeptic judged sound (its corrected fix where it rejected the finder's). Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, one mechanism (the `check_floor_bash` arms of 94 made self-consistent), §6 criteria each with a Red-when (run at the spec's base, and labelled a preservation check where already green there), §7 gates with a `New arm:` line, §10 reuse, and §8 `none` or only RESOLVED forks. Add its row to the README `roster:units` table. Verify every cited line at `0e5967090` before citing it; 94 is CLOSED. Keep the spec small.

### Items
- **Item 1 (medium, id 23):** the `os.utime` line at `selftest.py:4527` trips the suite's `[dSP-71] AC4` `read_handpicked_copies` guard. Close it the way the review states; say which, and show the guard's read at the base and after.
- **Item 2 (medium, ids 24, 30):** a check observes the mtime pin, so dropping it reds.
- **Items 3 to 9 (low):** the spec-text and test-arm gaps the record names (the pin's AC and fixed N, the unobserved `finally`, the unguarded staging and memo read, the uncounted anchor replace, staging `steps94` through `build_staged_copy`, the unasserted `.pyc` precondition, the one-line-short citation). Where an item is spec text in the CLOSED 94, say how 95's own text or ledger carries the correction instead.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
All nine items are closed by 95's §2 scope or carried in its ledger. The spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git, and no backticked §6 token is a bare suite path such as `tools/govkit/selftest.py` (the spec-token check reads one as a suite run).

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
