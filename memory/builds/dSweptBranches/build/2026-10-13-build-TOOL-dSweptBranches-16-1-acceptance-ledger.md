# Acceptance ledger — TOOL-dSweptBranches-16

**Serves:** journal TOOL-dSweptBranches-16

Built on `e238a4fb`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-16
- AC1 — `branch_reconcile.py` — an idle worktree with an unstaged edit of `a.txt` and a staged edit of `b.txt` to new bytes reads `UNMERGED-LIVE` naming `changed`; a worktree at an older commit whose staged file restores the default's bytes reads `MERGED`. The code was already correct, so this unit adds only the arm; it is red with the uncovered changed-path branch flipped to covered, the mutation the closing review measured green before

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.
