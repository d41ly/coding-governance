**Serves:** research TOOL-dSafePassage-84

# Brief: the read-only preview and the write run answer one question two ways for a receipt below schema 3

## The prompt

> TOOL-dSafePassage-78 (`460ffb587`) made `govkit update --write` walk no step when the receipt is below schema 3, printing `steps: not walked` with the reason. Its builder found, through the bug-class checklist's two-answers-to-one-question class, that the read-only preview at `tools/govkit/govkit.py` (the `else` branch printing `would walk <id>`, near line 10604) still lists the pending steps as walkable for such a receipt. BUILD-METHOD M10 adopts that discovery as a unit at once.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-84, which makes the read-only preview answer exactly as the write run does for a receipt below schema 3, by sharing the one condition 78 added rather than restating it, so preview and write cannot drift again. The spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16` (TOOL-dSafePassage-61 holds order 16 and stays non-terminal), node `a`, carries `**Derived:** TOOL-dSafePassage-78`, declares no `consumes-from` edge onto a CLOSED unit, and has one mechanism, §6 criteria each with a Red-when, §7 gates with a `New arm:` line, and §10 reuse. Add its row to the README `roster:units` table. It builds before TOOL-dSafePassage-81, which renames last; say so in §4.

### Items
- The preview's `else` branch and the write run's walk condition (78's `or schema < 3`) read one predicate.
- The preview prints the not-walked line and the pending count for such a receipt, as the write run does.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row.

### Acceptance
The spec is conforming and cites the two sites at `460ffb587`. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in it other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
