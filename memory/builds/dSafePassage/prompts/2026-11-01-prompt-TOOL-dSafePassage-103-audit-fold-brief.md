**Serves:** research TOOL-dSafePassage-103

# Brief: fold the round-1 spec audit of 103 into its spec

## The prompt

> The round-1 spec audit of TOOL-dSafePassage-103 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-103-spec-audit-round1.md`) returned CLEAN WITH FIXES: 0 blockers, 0 highs, 2 medium and 7 low items over 10 confirmed findings, precision 1.0. 103 is not built yet, so every item folds into its spec before the builder starts.

## The brief

### Goal
Fold every item of the audit record into 103's spec, at the fix the record's skeptic judged sound (the skeptic's corrected fix for id 9, whose finder fix was judged unsound). The spec gets a rev bump and one §9 line naming the audit record and this brief. Verify every cited line at the current HEAD before citing it.

### Items
- **Medium:** M1 (ids 1, 8): S4 and AC6 also cover `tools/policy/README.md` line 650 (the `arm_legacy_homes` row) and the Refusal-cause docstrings at `check_policy.py` 401 and 672. M2 (id 2): AC6 observes the `derive_census_tree` docstring in `tools/policy/policy.py` and the WHERE IT INSTALLS paragraph of `check_policy.py`.
- **Low:** ids 3 (§7 says the branch's `policy check` leg cannot see S1, and names what does), 4, 5 (the `symbols.json` regen and its map-freshness leg), 6 (the recall-floor legs the ledger trips), 7 (the README module table), 9, 10.
- **Write sets.** Where a fold changes Files touched, update that list.
- **Left-shift gates.** List each item's checklist entry in your return for the main loop; do not author them.

### Non-goals
No product code; no edit to any other spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
Each item is folded into 103's text, or refused with its reason. The spec stays conforming, with §8 `none`. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git; no backticked §6 token is a bare suite path, a code fragment that embeds a repository path, or a regex-escaped path.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
