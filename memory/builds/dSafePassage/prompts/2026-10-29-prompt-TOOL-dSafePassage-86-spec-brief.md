**Serves:** research TOOL-dSafePassage-86 TOOL-dSafePassage-87

# Brief: the round-2 closing review's high and its batched minors

## The prompt

> The round-2 closing diff review of dSafePassage over the round-1 promotions (`memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-84-closing-diff-round2.md`, recorded as subject dSafePassage-r1-promotions, CONVERGED, precision 0.71) confirmed 10 findings: 0 blocker, 1 high, 7 medium, 2 low. BUILD-METHOD M4 promotes the high to a unit whose mechanism closes it and batches the mediums and lows into one unit; their write sets overlap, so one batch.

## The brief

### Goal
Author the specs of TOOL-dSafePassage-86 and TOOL-dSafePassage-87, each closing the review items this brief assigns it at the fix the review's skeptic judged sound (its corrected fix where it rejected the finder's, for ids 1 and 13). Each spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16` (TOOL-dSafePassage-61 holds order 16 and stays non-terminal), node `a`, carries `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, declares no `consumes-from` edge onto a CLOSED unit, has one mechanism, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, and §10 reuse, and its §8 reads `none` or only RESOLVED forks, because a terminal status refuses an open fork. Add each row to the README `roster:units` table. Verify every cited line at `b634d60e5` before citing it. No spec may edit another unit's spec: a change a builder cannot make is a spec-writer edit you make now and name.

### Items
- TOOL-dSafePassage-86 closes H1 (id 13): the upgrade-walk row in the foreign-prefix parity leg reds at every moved prefix because release-0's apply runs a HERE-relative engine path the pinned clone lacks.
- TOOL-dSafePassage-87 batches M1 (id 1), M2 (id 3), M3 (id 4), M4 (id 8), M5 (id 9), M6 (id 10), M7 (id 14), L1 (id 11) and L2 (id 12), and builds after 86.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside this brief's items.

### Acceptance
Each assigned item is closed by exactly one unit's §2 scope, and every spec authored is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
