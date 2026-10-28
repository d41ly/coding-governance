**Serves:** research TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75

# Brief: the closing review's four HIGH units

## The prompt

> The closing diff review of dSafePassage, round 1 (`memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md`), confirmed 20 findings: 0 blocker, 5 high, 10 medium, 5 low. BUILD-METHOD M4 disposes each by severity: a HIGH is promoted to a unit whose mechanism closes it, and the mediums and lows are batched into one unit, two only when they split into disjoint write sets.

## The brief

### Goal
Author the specs of TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-74 TOOL-dSafePassage-75, each closing the review items this brief assigns it, at the fix the review's skeptic judged sound (the corrected fix where the finder's was judged UNSOUND).. Each spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16` (TOOL-dSafePassage-61 holds order 16 and stays non-terminal, so no new unit may sit above it), carries `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, declares no `consumes-from` edge onto a CLOSED unit (name CLOSED units it reads as read-and-closed), and has one mechanism, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, and §10 reuse. Add each unit's row to the README `roster:units` table. Verify every cited line against the code at HEAD before citing it; the review's line numbers are at `83817478f`. A choice the review and the code do not settle is a §8 fork with a recommendation.

### Items
- TOOL-dSafePassage-72 closes H1 (id 1) and H2 (id 2): `check_contained` in `tools/govkit/upgrade_steps.py` refuses a Windows-shaped path (backslash, rooted, UNC, drive colon) and refuses any link or reparse point on the path through `test_path_linked`, before any read, mkdir, write or unlink.
- TOOL-dSafePassage-73 closes H3 (id 4): the forward walk keys the `via: witness` mark on the reading the reverse walk uses for `rolled-back`.
- TOOL-dSafePassage-74 closes H4 (id 8): `derive_introduced` finds a step id in either quote style, the tomllib parse deciding.
- TOOL-dSafePassage-75 closes H5 (id 9) and M2 (id 5), one defect: `GOV_PYTHON` reaches the step's environment and `help/upgrade-steps.md`'s clean-environment list names it.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row (the main loop runs `--rescope`); no finding outside this brief's items.

### Acceptance
Each assigned review item is closed by exactly one unit's §2 scope, and every spec authored is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
