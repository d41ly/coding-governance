**Serves:** research TOOL-dSafePassage-99 TOOL-dSafePassage-101

# Brief: TOOL-dSafePassage-99 at rev-3, its §3 edges read as prose (TOOL-dSafePassage-101 S1)

## The prompt

> The close's merge bar at `70273a468` reds memory hygiene check 12 on TOOL-dSafePassage-99's §3: it declares **consumes-from** `TOOL-dSafePassage-87` and `TOOL-dSafePassage-71`, and neither CLOSED unit declares a matching **hands-off** back. TOOL-dSafePassage-101 S1 (`memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-101.md`, §2 S1 and §4 "The edge ruling") assigns the edit of 99's spec to a gov-spec-writer pass committed before 101's build, because scratch-guard lets only that role write the spec class.

## The brief

### Goal
Make exactly the edit TOOL-dSafePassage-101 S1 and its §4 "The edge ruling" state, to `memory/builds/dSafePassage/spec/2026-11-01-spec-TOOL-dSafePassage-99.md`: its §3 `### Edges` block drops the two `**consumes-from**` bullets and reads `none`, followed by the replacement paragraph 101's §4 quotes, verbatim; its header moves to rev-3, the status staying CLOSED; and its §9 gains one rev-3 line naming §3, check 12 and TOOL-dSafePassage-101. Verify the paragraph's cited lines are 99's own before writing it.

### Items
- **S1:** the edit above, and nothing else in 99's text.
- **Check:** `bash tools/memory-tree/check-memory-hygiene.sh --staged`, over a copy of the index with only 99's spec staged through `GIT_INDEX_FILE`, names no check 12 line for 99.

### Non-goals
No edit to any other spec, 87 and 71 included; no product code; no commit, no stage into the real index, no RUN.md row; no index regeneration.

### Acceptance
99's §3 reads `none` and the paragraph, its header rev-3 and CLOSED, its §9 one rev-3 line. The hygiene gate as above names no finding in 99 other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
