# Acceptance ledger — TOOL-dSweptBranches-12

**Serves:** journal TOOL-dSweptBranches-12

Built on `43791602`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-12
- AC1 — `GOV_DEFAULT_BRANCH` — set to `develop` while `upstream/HEAD` names `main`, an ancestor of `develop`: local and `upstream` `main` read `keep (the default branch)`, and `--write --remote` leaves both. Before the fix local `main` read `delete branch` and was deleted, and `upstream/main` was handed to the push, which the bare remote refused only because it was its HEAD. Red again with the default names cut to the chosen branch

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.
