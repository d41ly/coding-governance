# Fix brief — TOOL-dFoldedAudit-17 at rev-3

**Serves:** research TOOL-dFoldedAudit-17

## The brief

### Goal
Revise TOOL-dFoldedAudit-17's spec to rev-3, folding the second builder divergence recorded in `build/2026-11-02-build-TOOL-dFoldedAudit-17-4-builder-return.md`. Keep the status at INPROGRESS. Commit nothing.

### Items
1. The merge runs in the run worktree itself, not in a clone. That worktree is `C:/projects/coding-governance/.claude/worktrees/gov-build-m4-spec-audit-694e7b`, on `branch/gov-build-m4-spec-audit-694e7b`. Pre-commit's branch guard (`.githooks/pre-commit:71-93`) refuses a commit in a clone's primary tree on a non-default branch, and a sibling worktree is the place it admits. The worktree already has the hooks path and both merge drivers, and units 1 to 16 committed there. The write gate admits product writes there because this unit is routed and INPROGRESS. Remove the clone, the driver copy and the fast-forward from S1 and S10. M and F are made in the worktree, and `git fetch origin` reads the GitHub remote directly. A failed step leaves the worktree to be restored with `git merge --abort`. State that, and name it as the unit's stop.
2. S7: manifest line 223 names the resolver floor. It was added on main in `201eb127` and is current, so the expected delta stays none. Correct the sentence. Spell the record line as the kit does: `manifest-audit: delta none · watch-commits-since-stamp: <n>`.
3. §B notes main's `docs-undocumented.txt` addition to `PROJECT_REGISTRY_EXTRA`. It merges clean.
4. S8 names every file `gen_build_index.py --write` rewrites: dSafePassage's README generated block, the 2026-11 ledger and the dClosedLoop as-built view. Each is a render, not an authored write.
5. Correct the `:1405` citation to what it points at.
6. Commit trailers follow the charter: `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.

### Acceptance
Rev-3 with a §8 revision-log line for each item. No clone remains in S1 or S10, and every criterion that read the clone reads the run worktree.

### Gates
`tools/check-spec-tokens.py`, run by the main loop after this pass.

### Non-goals
No change to the resolutions themselves, and no write outside this build's `spec/`.
