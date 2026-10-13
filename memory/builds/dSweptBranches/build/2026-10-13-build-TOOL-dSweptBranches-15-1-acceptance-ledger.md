# Acceptance ledger — TOOL-dSweptBranches-15

**Serves:** journal TOOL-dSweptBranches-15

Built on `7661570b`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-15
- AC1 — `branch_reconcile.py` — an idle worktree whose initialised submodule holds an edited file reads `UNKNOWN` naming `submodule content sub`. Before the fix it read `MERGED`, the submodule graded covered by `None == None`. Red again with the submodule path compared as a blob

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.
