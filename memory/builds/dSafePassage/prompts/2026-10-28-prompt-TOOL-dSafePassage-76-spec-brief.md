**Serves:** research TOOL-dSafePassage-76 TOOL-dSafePassage-77

# Brief: the closing review's mediums and lows, in two disjoint write sets

## The prompt

> The closing diff review of dSafePassage, round 1 (`memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md`), confirmed 20 findings: 0 blocker, 5 high, 10 medium, 5 low. BUILD-METHOD M4 disposes each by severity: a HIGH is promoted to a unit whose mechanism closes it, and the mediums and lows are batched into one unit, two only when they split into disjoint write sets.

## The brief

### Goal
Author the specs of TOOL-dSafePassage-76 TOOL-dSafePassage-77, each closing the review items this brief assigns it, at the fix the review's skeptic judged sound (the corrected fix where the finder's was judged UNSOUND).. Each spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16` (TOOL-dSafePassage-61 holds order 16 and stays non-terminal, so no new unit may sit above it), carries `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, declares no `consumes-from` edge onto a CLOSED unit (name CLOSED units it reads as read-and-closed), and has one mechanism, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, and §10 reuse. Add each unit's row to the README `roster:units` table. Verify every cited line against the code at HEAD before citing it; the review's line numbers are at `83817478f`. A choice the review and the code do not settle is a §8 fork with a recommendation.

### Items
- TOOL-dSafePassage-76 batches the engine-side items, M1 (id 3), M3 (id 6), M4 (id 7), M5 (id 10), M9 (id 19), L1 (id 11), L2 (id 12), L3 (id 13) and L5 (id 21), over `tools/govkit/upgrade_steps.py`, `tools/govkit/govkit.py`, `tools/lib/python_floor.py`, their help pages and govkit selftest; M1 builds on TOOL-dSafePassage-72's `check_contained`, so 76 builds after 72 by order of dispatch, not by a `consumes-from` edge.
- TOOL-dSafePassage-77 batches the walk-leg items, M6 (id 14), M7 (id 16), M8 (id 17), M10 (id 20) and L4 (id 18), over `tools/govkit/upgrade_walk.py` and its arms and fixtures only, a write set disjoint from 76's; M10's measured-defect hand-off is an ask row in this build's `BACKLOG.md`, named in 77's scope.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row (the main loop runs `--rescope`); no finding outside this brief's items.

### Acceptance
Each assigned review item is closed by exactly one unit's §2 scope, and every spec authored is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
