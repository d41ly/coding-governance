**Serves:** research TOOL-dSafePassage-98

# Brief: the round-9 closing review's one low, and the end of the review chain

## The prompt

> The round-9 closing diff review of dSafePassage over the round-8 promotion (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-97-closing-diff-round9.md`, recorded as subject dSafePassage-r8-promotions) confirmed 1 low and refuted 4, precision 0.2. BUILD-METHOD M4: a promoting round whose precision falls below the review protocol's floor ENDS the chain, and its promotions are built from their specs as written. This is the last unit of the chain.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-98, carrying the correction to TOOL-dSafePassage-97's S3 at the fix the review's skeptic judged sound (its corrected fix, where it rejected the finder's): 97's S3 says the build pass writes its acceptance ledger "and nothing else", while its build commit `e3038fea6` also writes 97's spec status, README.md and RUN.md, and its AC3 reads only 96's authored text and `tools/`. 97 is CLOSED, so 98 carries the narrowed reading in its own text, with the optional write-set probe the skeptic names. 98 writes no product code; its build output is its acceptance ledger. Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16`, node `a`, `**Derived:** TOOL-dSafePassage-1` with the review record named in its §9, §6 criteria each with a Red-when, §7 gates with no `New arm:` line (say why), §10 reuse, §8 `none`. Add its row to the README `roster:units` table. Verify every cited line at the current HEAD before citing it. Keep it to one correction.

### Items
- **Id 4 (low):** 97's S3 claims its build pass writes "nothing else", which its build commit already contradicts and its AC3 cannot observe. Narrow the claim to what the build pass writes, and carry the skeptic's optional write-set probe (`git diff --name-only e3038fea6^ e3038fea6`) as the observation that would show an unintended write.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
The one item is carried in 98's text. The spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git; no backticked §6 token is a bare suite path or a code fragment that embeds a repository path (the spec-token check reads either as a path); and no AC's diff or grep is already non-empty at the spec's own commit because a generated records block moved.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
