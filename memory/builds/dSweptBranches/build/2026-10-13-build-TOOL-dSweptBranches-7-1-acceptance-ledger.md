# Acceptance ledger — TOOL-dSweptBranches-7

**Serves:** journal TOOL-dSweptBranches-7

Built on `d1daaf13`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-7
- AC1 — `branch_reconcile.py` — a worktree whose `.git` file was removed, holding an untracked file, reads `UNKNOWN` with `worktree status could not be read`, and `--write` leaves the file; before the fix it read `MERGED` and `--write` deleted the file; red again with the fix's guard set to `if False:`

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.
