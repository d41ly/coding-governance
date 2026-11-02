**Serves:** research TOOL-dSafePassage-97

# Brief: the round-8 closing review's five wording lows

## The prompt

> The round-8 closing diff review of dSafePassage over the round-7 promotion (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-96-closing-diff-round8.md`, recorded as subject dSafePassage-r7-promotions, CONVERGED, precision 0.89) confirmed 5 low items and found 96's code edits correct. All five are wording defects in TOOL-dSafePassage-96's spec, which is CLOSED and read-only. BUILD-METHOD M4 batches them into one unit.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-97, carrying the corrections to 96's text the way TOOL-dSafePassage-95's section 4 carried 94's: a corrections table, one row per item, each naming 96's line at `ab71837da`, what it says, and the corrected reading (the skeptic's corrected fix for id 8). 97 writes no product code; its only build output is its acceptance ledger. Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, §6 criteria each with a Red-when, §7 gates (no `New arm:` line, and say why: no product code changes), §10 reuse, and §8 `none`. Add its row to the README `roster:units` table. Verify every cited line at `ab71837da` before citing it.

### Items
- **Item 1 (ids 2, 14):** AC2 to AC4's scratch tree, taken from `git archive HEAD tools`, holds the build only after the build commit.
- **Item 2 (ids 3, 7, 12, 15):** §7's leg count, five where `--legs-for` names 17 (5 guarded, 12 broad); paste the `--legs-for` output.
- **Item 3 (ids 6, 10, 16):** S3's rerun safety covers only a direct `check_floor_bash` call.
- **Item 4 (ids 4, 8, 13, 17):** the Measured row's "S4" is TOOL-dSafePassage-95's S4; one spelling for the break; each line cite names its tree.
- **Item 5 (ids 5, 9, 18):** the `New arm:` lines' staging column names AC4's `finally` cut.
- **The review's left-shift gate** (gate the CLOSED flip on a folded audit): list it in your return for the main loop; do not author it.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
All five items are carried in 97's corrections table. The spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git, no backticked §6 token is a bare suite path, and no AC's diff or grep is already non-empty at the spec's own commit because a generated records block moved.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
