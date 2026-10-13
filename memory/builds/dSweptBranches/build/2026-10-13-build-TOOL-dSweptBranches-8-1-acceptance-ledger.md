# Acceptance ledger — TOOL-dSweptBranches-8

**Serves:** journal TOOL-dSweptBranches-8

Built on `91d1e62a`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-8
- AC1 — `branch_reconcile.py` — a registered path replaced by another repository with a commit reads `UNKNOWN` with `not provably this repository's worktree`, and `--write` leaves its `.git` directory and file; a worktree whose path is gone is dropped by git's own removal and the run exits 0; with git's removal failing on the foreign path, `remove_worktree` returns `failed` and runs no `rm -rf`. Before the fix the foreign repository read `MERGED` and `--write` destroyed it. Red again with the inventory's identity check off, and with the fallback unguarded. A staged break of a prune-first branch for a gone path stayed green, so that branch was deleted and spec rev-2 records it

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.
