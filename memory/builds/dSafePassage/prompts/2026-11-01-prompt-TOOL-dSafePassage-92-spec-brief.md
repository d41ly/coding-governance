**Serves:** research TOOL-dSafePassage-92 TOOL-dSafePassage-93

# Brief: the round-4 closing review's high and its batched minors

## The prompt

> The round-4 closing diff review of dSafePassage over the round-3 promotions (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-90-91-closing-diff-round4.md`, recorded as subject dSafePassage-r3-promotions, CONVERGED, precision 1.0) confirmed 4 findings: 0 blocker, 1 high, 2 medium, 1 low. BUILD-METHOD M4 promotes the high to a unit and batches the mediums and the low into one unit.

## The brief

### Goal
Author the specs of TOOL-dSafePassage-92 and TOOL-dSafePassage-93, each closing the review items this brief assigns it at the fix the review's skeptic judged sound (its corrected fix where it rejected the finder's: ids 3 and 4). Each spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, carries `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, has one mechanism, §6 criteria each with a Red-when (each run at the spec's base, and labelled a preservation check where it is already green there), §7 gates with a `New arm:` line, and §10 reuse, and its §8 reads `none` or only RESOLVED forks. Add each row to the README `roster:units` table. Verify every cited line at `2e6d48453` before citing it; 90 and 91 are CLOSED, so a change to their code is this unit's own. Keep each spec small: these are test-arm corrections.

### Items
- **TOOL-dSafePassage-92 closes the high (id 1):** `[dSP-91 L2]` in `tools/govkit/selftest.py` goes red falsely on a Windows host with the WSL launcher and no distribution. Because id 3 grades the same check's positive needle, 92 may also take id 3 if one mechanism (the tail predicate) closes both; say so, and keep id 3 out of 93 then.
- **TOOL-dSafePassage-93 batches** id 2 (a hard-link `[dSP-90]` sibling triggering the link-or-alias refusal text), id 4 (the record's `set_environ` claim narrowed, or the two remaining hand-typed copies folded, whichever the skeptic's correction states), and id 3 if 92 does not take it. It builds after 92.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside this brief's items.

### Acceptance
Each assigned item is closed by exactly one unit's §2 scope. Every spec authored is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in each §6 is tracked by git.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
