# Acceptance ledger — TOOL-dSweptBranches-9

**Serves:** journal TOOL-dSweptBranches-9

Built on `8b1a1e9b`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-9
- AC1 — `branch_reconcile.py` — a same-subject commit on another file, a same-subject edit of disjoint lines, and the same five lines added to a different file each read `UNMERGED-LIVE`, while the rebased-copy fixture still reads `SUPERSEDED` by `patch 2`. Before the fix the first two read `SUPERSEDED`. Red again with the file-set rule off (the different-file copy) and with the shared-lines rule off (the disjoint edit)

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.
