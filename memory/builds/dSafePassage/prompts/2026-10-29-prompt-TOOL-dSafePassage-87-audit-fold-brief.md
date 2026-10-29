**Serves:** research TOOL-dSafePassage-87 TOOL-dSafePassage-89 TOOL-dSafePassage-88

# Brief: fold the round-1 spec audit of 86 to 89 into 87, 89 and 88

## The prompt

> The round-1 spec audit of TOOL-dSafePassage-86, -87, -89 and -88 (`memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-spec-audit-round1.md`) returned CLEAN WITH FIXES: 0 blockers, 0 highs, 5 medium items and 10 low items, precision 0.90. 86 was built beside the audit, from rev-3, so its one item (L7) moves into 87, which edits the same file after it.

## The brief

### Goal
Fold every confirmed item of the audit record into the spec it names, at the fix the record's skeptic judged sound (the skeptic's corrected fix for id 7, M2). Each spec edited gets a rev bump and one §9 line naming the audit record and this brief. Verify every cited line at this branch's HEAD (86 is built there) before citing it.

### Items
- **87:** M1 (id 1), M2 (id 7), M3 (id 8), M4's 87 half (id 19, S7), L2 (id 2), L4 (id 6), L5 (id 9), L8 (id 13). Also take 86's L7 (id 12): 87 re-points `derive_release_engine` in `tools/govkit/upgrade_walk.py` at `gk.resolve_tool_path`, as the record's fix states, keeping 86's grader green, and 87's §10 names `resolve_tool_path` as the seam extended.
- **89:** M4's 89 half (id 15), L1 (ids 5, 10, 16, 21), L6 (id 11). Where 89's AC2 names a walk stop that 88 later removes, state that AC2 is observed at 89's own pass, before 88 builds.
- **88:** M5 (id 18), L3 (id 4), L9 (id 14), L10 (id 20).
- **Write sets.** Where a fold changes a unit's Files touched, update that list.
- **Left-shift gates.** Each item names a checklist entry. Do not author checklist entries; list them in your return for the main loop.

### Non-goals
No product code; no edit to a CLOSED spec, 86 included; no commit, no stage into the real index, no RUN.md row; no finding outside the record.

### Acceptance
Each confirmed item is folded into exactly one spec's text, or refused with its reason. Every spec edited stays conforming, with §8 `none` or only RESOLVED forks. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index. Every backticked path in each §6 is tracked by git.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
