**Serves:** research TOOL-dSafePassage-102

# Brief: fold the round-1 spec audit of 102 into its spec

## The prompt

> The round-1 spec audit of TOOL-dSafePassage-102 (`memory/builds/dSafePassage/reviews/2026-11-01-review-TOOL-dSafePassage-102-spec-audit-round1.md`) returned CLEAN WITH FIXES: 0 blockers, 0 highs, 2 medium and 1 low item over 5 confirmed findings, precision 0.71. 102 is not built yet, so every item folds into its spec before the builder starts.

## The brief

### Goal
Fold every item of the audit record into 102's spec, at the fix the record's skeptic judged sound (the skeptics' corrected fix for item 1). The spec gets a rev bump and one §9 line naming the audit record and this brief. Verify every cited line at the current HEAD before citing it.

### Items
- **Item 1 (ids 1, 3, 6):** AC3 grades the reason field and the comment lines of `memory/project/fork-ceilings.txt`: field-level joins, a zero count of changed comment lines, row counts of 5, and the staged breaks the record names.
- **Item 2 (id 2):** correct the `run-gates-2leg` row's history to what its own reason says (the polled reading still needs a +2 margin), and take the record's measured option: the build measures each of the five rows three times with `--only` and sets each ceiling to the largest of the three readings, still inside the file's max(3, 5 %) band, halting on a reading the bar's own did not bound. The owner ruled "raise the five fork ceilings with evidence"; three readings are that evidence.
- **Item 3 (id 5):** Files touched names the spec's Status flip and the `gen_build_index.py --write` renders of the build README and `memory/backlog/TOOL.md`.

### Non-goals
No product code; no edit to any other spec; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
Each item is folded into 102's text, or refused with its reason. The spec stays conforming, with §8 `none`. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in §6 is tracked by git; no backticked §6 token is a bare suite path or a code fragment that embeds a repository path, and none carries a regex-escaped path.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
