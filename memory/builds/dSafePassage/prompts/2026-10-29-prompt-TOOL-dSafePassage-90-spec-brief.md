**Serves:** research TOOL-dSafePassage-90 TOOL-dSafePassage-91

# Brief: the round-3 closing review's high and its batched minors

## The prompt

> The round-3 closing diff review of dSafePassage over the round-2 promotions (`memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-closing-diff-round3.md`, recorded as subject dSafePassage-r2-promotions, CONVERGED, precision 1.0) confirmed 7 findings: 0 blocker, 1 high, 4 medium, 2 low. BUILD-METHOD M4 promotes the high to a unit whose mechanism closes it and batches the mediums and lows into one unit.

## The brief

### Goal
Author the specs of TOOL-dSafePassage-90 and TOOL-dSafePassage-91, each closing the review items this brief assigns it at the fix the review's skeptic judged sound (its corrected fix where it rejected the finder's: ids 3, 5, 6 and 7). Each spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, carries `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, has one mechanism, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, and §10 reuse, and its §8 reads `none` or only RESOLVED forks. Add each row to the README `roster:units` table. Verify every cited line at `cbaaeebeb` before citing it; 86, 87, 89 and 88 are CLOSED and read-only, so a change to their code is this unit's own.

### Items
- **TOOL-dSafePassage-90 closes H1 (id 3):** rolling back a case-only rename on a case-insensitive filesystem deletes the file it just restored and reports it restored. Four of the seven findings (ids 1, 2, 3, 5) share one cause: 88's `samefile` arm in `own_file` now lets a case-only rename through to `git mv`. Weigh two mechanisms and pick one from the code and the records, saying why: (a) the review's fix, which keeps the case-only move and teaches the snapshot and restore to treat the two spellings as one path; (b) taking the `samefile` arm back out of `own_file`, so a case-only rename is refused as an occupied destination again, as it was at `b634d60e5`, with a refusal that names the case-only cause and a remedy. Option (b) loses no data and reverts the spec audit's M5 (id 18); option (a) keeps M5 and needs a rollback change. If (b) closes M1 (id 1), M2 (id 2) and M3 (id 5) as unreachable, say so per id and move them from 91 into 90.
- **TOOL-dSafePassage-91 batches** whichever of M1 (id 1), M2 (id 2), M3 (id 5) 90 does not close, plus M4 (id 6), L1 (id 4) and L2 (id 7). It builds after 90.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside this brief's items.

### Acceptance
Each assigned item is closed by exactly one unit's §2 scope, or shown unreachable with code lines. Every spec authored is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in each §6 is tracked by git (`python tools/check-spec-tokens.py` reads untracked ones as findings).

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
