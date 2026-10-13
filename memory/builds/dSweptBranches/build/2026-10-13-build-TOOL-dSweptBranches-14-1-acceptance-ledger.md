# Acceptance ledger — TOOL-dSweptBranches-14

**Serves:** journal TOOL-dSweptBranches-14

Built on `cfa6573e`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-14
- AC1 — `branch_reconcile.py` — a branch whose merge of `main` added `evil.txt`, and whose one other commit `main` cherry-picked, reads `UNMERGED-LIVE`. Before the fix it read `EQUIVALENT` with `git cherry: all 1 commit(s) already applied`. Red again with a merge covered without reading its diff, and with `git cherry` trusted over an unclean merge

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.
