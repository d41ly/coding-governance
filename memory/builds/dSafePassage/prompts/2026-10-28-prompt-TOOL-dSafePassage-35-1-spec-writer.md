**Serves:** research TOOL-dSafePassage-35

# Brief: TOOL-dSafePassage-35 rebased onto what TOOL-dSafePassage-26 already built

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-35 back as a DIVERGENCE before writing code (`wf_5a22584f-d1b`, HEAD `56aef62aa`), and the run revises the spec under M2.

## The brief

### Goal

Every scope item of TOOL-dSafePassage-35 builds against the code at HEAD. Where TOOL-dSafePassage-26 (CLOSED, dfcef45a7) has already built an item or a different rule for it, the spec says so and keeps only the residual. AC21's closure is satisfiable within the unit's Files touched.

**What the builder measured at HEAD:**

1. **S24 / AC21 / §5 risk.** `tools/govkit/upgrade_steps.py` borrows 14 names from govkit through `load_govkit()` (`:1928`), not the 5 that S24 names. The other nine are `derive_tool_root`, `STAGING_JOURNAL_REL`, `RECLAIM_GUARD_SUFFIX`, `WRITE_LOCK_REL`, `ATTENDED_ORDER_PREFIX`, `write_row_order`, `take_write_lock`, `resolve_prefix_token`, `load_deploy` and `git_pathspec`. TOOL-dSafePassage-26 kept that borrowing deliberately; `load_govkit`'s docstring names them. TOOL-dSafePassage-42 S14 and AC10 read S24's moved set as the ast closure of the four moved functions only. As written, AC21 ("no name govkit defines that the module does not define or copy") cannot go green without moving the write lock and its callees, which nothing scopes.
2. **S28 / §8 F3 / §4 Inventory.** TOOL-dSafePassage-26 S31 already built a corrupt-image rule. `write_before_image` (`:656-666`) uses `read_image_changes`, which refuses, naming the image, when a path the image lists changed after it was written. S28 asks instead for a tree-wide `git status --porcelain` test and a new `raise Refusal` site, with BRANCH_PIN +1. F3 never weighed the image-scoped rule that now exists.
3. **Smaller mismatches:**
   - S27's target-side read already exists (`read_line_ending_config(target)`); only the `autocrlf-local` plant is missing.
   - S5's `lock-reused` plant already sets `started` 600 s back.
   - S25 does nothing, because TOOL-dSafePassage-26 is CLOSED.
   - The §4 verdict table says a differing `boot_id` reads `dead`; HEAD reads `unknown`, so S26 is a real change.
   - AC20's count of seven at `3708a705` may have moved since TOOL-dSafePassage-69 raised the floor row to 3.12. Re-measure it.

**The main loop's recommendations.** Take each unless the code shows it breaks a written criterion; a recommendation you reject goes to §8 with its reason.
- **(1)** Scope AC21 to S24's set. Name the other nine borrowed names as kept, citing TOOL-dSafePassage-26's docstring and the reason. Moving the write lock is not this unit's job (YAGNI). TOOL-dSafePassage-42 S14/AC10 already read it that way, so check that they still agree.
- **(2)** Keep TOOL-dSafePassage-26 S31's image-scoped rule. It is narrower than a tree-wide `git status`, which would refuse on any unrelated dirty file. S28 then shrinks to whatever residual the existing rule does not cover, or is withdrawn, and BRANCH_PIN does not move. Correct the Inventory line.
- **(3)** Each smaller mismatch becomes a residual: S27 becomes the plant only, S5 is struck as built, S25 is struck, and the verdict table is corrected.

### Items

1. **Revise TOOL-dSafePassage-35** as a rev bump dated 2026-10-28, still `DEFERRED`, with the dispositions above. Add one §9 line naming this brief. Every AC must be observable on HEAD's code plus this unit's residual.
2. **Cross-read TOOL-dSafePassage-42**, which reads S24's closure, and every DEFERRED sibling that cites S24, S28 or BRANCH_PIN's move. Fix a disagreement in place, with a rev bump and a §9 line. CLOSED specs are read-only.
3. **Commit nothing.** Return the files you wrote and each item's disposition.

### Acceptance

- Each of (1) to (3) has a named disposition, backed by code lines.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, and no edit to a CLOSED spec.
- No commit and no stage into the real index.
