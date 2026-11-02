**Serves:** research TOOL-dSafePassage-99 TOOL-dSafePassage-100

# Brief: fold the round-1 spec audit of 99 and 100 into both specs

## The prompt

> The round-1 spec audit of TOOL-dSafePassage-99 and -100 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-99-100-spec-audit-round1.md`) returned CLEAN WITH FIXES: 0 blockers, 0 highs, 0 mediums and 3 low items, precision 0.8. Neither unit is built yet, so every item folds into its spec before either builder starts.

## The brief

### Goal
Fold every confirmed item of the audit record into the spec it names, at the fix the record's skeptic judged sound (for LOW 1, the narrowing option the record names as the default; for LOW 2, the fourth `[dSP-99]` check the record prefers). Each spec edited gets a rev bump and one §9 line naming the audit record and this brief. Verify every cited line at `6414e1dc6` before citing it.

### Items
- **99:** LOW 1 (ids 3, 5): narrow section 1, S2, section 4 "The held engine" and S3 to import statements, and name selftest.py:9764-9766 as a by-path load left in place; check 3 and AC3 stay as written. LOW 2 (id 4): a fourth `[dSP-99]` check that calls the held engine's `upgrade_steps.load_govkit()` after `govkit_module()` rebinds the table and asserts the result is the held engine, with its AC, Red-when and the `New arm:` line's covers updated; and name the window in "What it does not cover".
- **100:** LOW 3 (id 2): add its acceptance ledger `memory/builds/dSafePassage/build/2026-11-01-build-TOOL-dSafePassage-100-ledger.md` to Files touched and `recall floor` and `recall floor arms` to its §7 leg line, re-checked with `python tools/check-spec-tokens.py --legs-for` over the full write set.
- **Left-shift gates.** List each item's checklist entry in your return for the main loop; do not author them.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
Each confirmed item is folded into exactly one spec's text, or refused with its reason. Every spec edited stays conforming, with §8 `none`. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in each §6 is tracked by git, and no backticked §6 token is a bare suite path such as `tools/govkit/selftest.py` (the spec-token check reads one as a suite run) or a code fragment that embeds a repository path.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
