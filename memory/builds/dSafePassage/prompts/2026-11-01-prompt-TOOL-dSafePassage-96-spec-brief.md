**Serves:** research TOOL-dSafePassage-96

# Brief: the round-7 closing review's three minors

## The prompt

> The round-7 closing diff review of dSafePassage over the round-6 promotion (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-95-closing-diff-round7.md`, recorded as subject dSafePassage-r6-promotions, CONVERGED, precision 0.75) confirmed 3 items: 0 blocker, 0 high, 1 medium, 2 low. BUILD-METHOD M4 batches them into one unit.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-96, closing all three items at the fix the review's skeptic judged sound. Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, one mechanism, §6 criteria each with a Red-when (run at the spec's base, and labelled a preservation check where already green there), §7 gates with a `New arm:` line, §10 reuse, and §8 `none`. Add its row to the README `roster:units` table. Verify every cited line at `744d25517` before citing it; 95 is CLOSED. Keep the spec small: three edits inside `check_floor_bash`.

### Items
- **Item 1 (medium, id 1) and item 2 (low, id 4), one defect:** the two `[dSP-95]` restore checks never read `argv94` or `cut94`, so each reads `ok` on a path it did not run. Add the path condition to each check.
- **Item 3 (low, id 2):** `build_staged_copy` at `selftest.py:4495` fails with FileExistsError on a reused tmp. Remove the directory before staging, or stage under a fresh directory, as the review states.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
All three items are closed by 96's §2 scope. The spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git, no backticked §6 token is a bare suite path such as `tools/govkit/selftest.py`, and no AC's diff or grep is already non-empty at the spec's own commit because a generated records block moved.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
