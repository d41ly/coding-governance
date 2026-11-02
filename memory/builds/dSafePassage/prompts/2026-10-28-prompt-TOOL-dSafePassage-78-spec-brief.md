**Serves:** research TOOL-dSafePassage-78

# Brief: the govkit selftest arms this build left red at its head

## The prompt

> The close's New-arm observation (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`) found 17 govkit selftest arms of this build's own units failing at `83817478f` whatever break was staged, so the selftest leg is red at the build's head. BUILD-METHOD M10 adopts that discovery as a unit at once.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-78, which makes each of the arms below pass at the head for the right reason, or retires an arm whose assertion cannot hold, after reading which side is wrong: the arm's fixture, or the product it observes. The spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16` (TOOL-dSafePassage-61 holds order 16 and stays non-terminal), carries `**Derived:** TOOL-dSafePassage-1` with the batch-b researcher handoff named in its §9, declares no `consumes-from` edge onto a CLOSED unit, and has one mechanism (the arms' red at the head), §6 criteria each with a Red-when, §7 gates with a `New arm:` line, and §10 reuse. Add its row to the README `roster:units` table. Reproduce each red before specifying its fix: run one check function or one inline `main()` block of `tools/govkit/selftest.py` in a `git clone --shared` under the temp root, never the whole suite and never in this worktree.

### Items
- `[dSP-2] S2` ×3, "the walk refuses a spoiled|unstaged|escaping step, naming it": the scratch target is not a git repository, so `git rev-parse --absolute-git-dir` (from `015fa02e3`, TOOL-dSafePassage-30) refuses before the refusal the arm asserts.
- `[dSP-3 AC2]` ×2 and `[dSP-3 AC9]`: `walk stopped at govkit/receipt-schema-4: exit 1: receipt-schema-4: up refused · … schema 2 is below 3`.
- `[dSP-8] AC3`, "its files are the destinations plan lists": `231 rows, 337 destinations`.
- `[dSafePassage-6] AC6 … --expect <other> … missing` ×10: the arm requires `"MISS" not in stdout` on a case that exits 1 by design, which is a MISS.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no arm outside these items.

### Acceptance
Each item is disposed in §2 with the side found wrong and the line that shows it, and the spec is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in it other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
