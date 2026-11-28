# Brief — aIndexedAnchor: the attended lander's marker is a registered record

**Serves:** research TOOL-aIndexedAnchor-4
**Caused-by:** TOOL-aIndexedAnchor-1

The push bar over aIndexedAnchor's attended landing, run from the primary tree, redded `record-kinds` MIXED:
`RED pocket push-main-active: no row's <git-common-dir>/ home matches this entry of
C:/projects/coding-governance/.git; register its family as a witness row, or move it out of the common dir`.
It was the leg's one unmatched common-dir entry of 82. The owner was offered registering the row in this build or
waiting for another build to land first, and chose the row.

## The prompt

> Register its row here

## The brief

### Goal
`tools/memory-tree/record-kinds.toml` registers the attended lander's `push-main-active` marker as a witness
row, so an attended landing from the primary tree no longer reds `record-kinds` on its own marker.

### Items
1. One `[[record-kind]]` row whose `home` is `<git-common-dir>/push-main-active`, written by `push-main.sh`
   (`tools/push-main.sh` sets `marker="$gd/push-main-active"`), in the shape of the existing common-dir rows
   such as `gate-ledger`, with every field the table and its gates require.

### Acceptance
`record-kinds` over a common dir holding `push-main-active` reports no unmatched pocket for it, seen red
without the row.

### Gates
`record-kinds`, and every leg the spec's files trip.

### Non-goals
`tools/push-main.sh` and where it writes its marker; the `record causes` red; any other row of the table.

### Limitations
The marker exists only while an attended landing runs, so the bar that grades the landing is the one that sees it.

### Reuse
The common-dir rows of `record-kinds.toml` (`gate-ledger`, `health-logs`, `history-verdicts`) are the
shape; the leg's own refusal names the remedy. Recall terms used: record-kinds pocket common dir witness row
push-main-active marker attended lander.

## Drawn from the session

> Should I register the `push-main-active` row in this build and land both builds from the primary tree, or wait for the peer to land aAnsweredPark first?
— agent, 2026-11-28, the question the owner answered

## Owner confirmation

Asked: Should I register the `push-main-active` row in this build and land both builds from the primary tree, or wait for the peer to land aAnsweredPark first?
Answer: Register its row here

## route
- build: aIndexedAnchor
- unit: TOOL-aIndexedAnchor-4 · spec memory/builds/aIndexedAnchor/spec/2026-11-28-spec-TOOL-aIndexedAnchor-4.md
- brief: memory/builds/aIndexedAnchor/prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-4-brief.md
