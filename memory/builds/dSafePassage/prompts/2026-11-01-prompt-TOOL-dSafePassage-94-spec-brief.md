**Serves:** research TOOL-dSafePassage-94

# Brief: the round-5 closing review's two minors

## The prompt

> The round-5 closing diff review of dSafePassage over the round-4 promotions (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-92-93-closing-diff-round5.md`, recorded as subject dSafePassage-r4-promotions, CONVERGED, precision 1.0) confirmed 2 findings: 0 blocker, 0 high, 1 medium, 1 low. BUILD-METHOD M4 batches them into one unit.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-94, closing both items at the fix the review's skeptic judged sound (its corrected fix for id 1, where it rejected the finder's). Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, one mechanism, §6 criteria each with a Red-when (run at the spec's base, and labelled a preservation check where already green there), §7 gates with a `New arm:` line, §10 reuse, and §8 `none` or only RESOLVED forks. Add its row to the README `roster:units` table. Verify every cited line at `c86d51fa5` before citing it; 92 and 93 are CLOSED. Keep the spec small: these are test-arm corrections inside `check_floor_bash`.

### Items
- **Id 1 (medium):** `[dSP-91 L2]` cannot tell the stub's fallback spawn at `python_floor.py:36` from a spawn crashing inside `resolve_bash`. The skeptic's fix: an in-process assertion in the `GOV_BASH`-unset block that `resolve_shell_argv(["bash", "x"])` returns `["bash", "x"]` with `_BASH` set to None, restored in a `finally`, with the `check_runs` except-`ValueError` regression as its red probe; `test_floor_fallback` keeps grading the tail only.
- **Id 2 (low):** `read_stub_tail` leaves the stand-in's `__pycache__` between shapes. The skeptic's fix: remove it before each write, with the same-length two-body probe as its red.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside this brief's items.

### Acceptance
Both items are closed by 94's §2 scope. The spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git, and no backticked §6 token is a bare suite path such as `tools/govkit/selftest.py` (the spec-token check reads one as a suite run).

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
