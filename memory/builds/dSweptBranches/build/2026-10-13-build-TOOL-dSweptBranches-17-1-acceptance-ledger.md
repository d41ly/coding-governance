# Acceptance ledger — TOOL-dSweptBranches-17

**Serves:** journal TOOL-dSweptBranches-17

Built on `8bfafdca`, inline, promoted at the closing review's exit. The arm was written first
and observed red against the code before the fix; then the fix's break was staged on a copy of
the CLI, observed red, and the bytes restored.

**Evidences:** TOOL-dSweptBranches-17
- AC1 — `VERDICT_RANK` — the extended write fixture holds every verdict, a superseded branch whose worktree carries covered dirt is removed with it, and the stash list is unchanged by `--write --remote`; red with `SUPERSEDED` out of the deletable set, and with the stash keep removed
- AC2 — `--ignored=matching` — an idle worktree's ignored `debug.log` is named `ignored 1` in its evidence; before the fix it was not; red with ignored paths unread
- AC3 — `GOV_REMOTE` — exported as `nope` in the outer environment, an in-process inventory under `seed_environ()` still resolves `upstream`; the census arm's seam check now runs inside it
- AC4 — `remove_worktree` — a skeleton holding a link to a scratch directory outside it is removed and the directory's `index.js` survives; red with the walk following links. A node that cannot create a link records the check as skipped, never as passed
- AC5 — `branch_reconcile.py` — a repository with no memory tree prints the `skipped — records, rotated and run-record predicates · no memory tree` line; before the fix it did not; red with the announcement removed
- AC6 — `branch_reconcile.py --write` — with a file at the manifest directory's path the run exits 2 and deletes nothing; before the fix it raised; red with the directory created outside the refusal
- AC7 — `build_rows` — over a fixture holding every keep and a stash entry no action carries ` · `, every keep outside the deletable set reads `keep (<verdict>)`, and a container nested under the primary names its kept worktree by its row name; before the fix the first two read a bare `keep` and the reason named the raw path; red with each reverted
- S6 — spec 3 rev-4 names `WRITE_TRACE` in §4 and AC1, recorded before each act

## Owed at the close

The `branch-reconcile selftest` leg runs in the close's bar.
