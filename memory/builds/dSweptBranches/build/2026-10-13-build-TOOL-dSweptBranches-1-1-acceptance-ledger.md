# Acceptance ledger — TOOL-dSweptBranches-1

**Serves:** journal TOOL-dSweptBranches-1

Built on `5b01cd34`, inline. The census arms ran through a scratch driver that imports the kit's
self-test and runs only `arm_census`, because the gate guard refuses the whole suite before
VERIFYING and the owner's rule lets a unit run the test file it is writing. Each break below was
staged on a copy of `branch_reconcile.py`, observed red, and the copy restored byte-for-byte.

On gov itself the report took 1.3 s over 10 worktrees, 15 local and 26 remote branches, with every
row `UNKNOWN` from the stub.

**Evidences:** TOOL-dSweptBranches-1
- AC1 — `branch_reconcile.py` — over the census fixture it lists the primary, nested, three sibling (one detached, one prunable) and temp worktrees, 7 local, 2 `upstream` and 1 stash ref, and the staged, unstaged, untracked, merging and submodule-drift fields; 14 of 14 arms green. Red observed with the nested test returning `worktree/elsewhere`
- AC2 — `branch_reconcile.py` — two runs printed identical bytes; red observed with the age reading the clock in microseconds
- AC3 — `GOV_REMOTE` — `nope` and a second remote each exit 2 naming `GOV_REMOTE`; red observed with the ladder replaced by a literal `origin`, which failed four arms
- AC4 — `branch_reconcile.py` — the primary's evidence carries no untracked count with the nested worktree beside it; red observed with the exclusion replaced by `if False:`
- AC5 — `PREDICATES` — emptied, every row reads `UNKNOWN` with `no predicate decided`; red observed with the ladder's default set to `MERGED`
- AC6 — `govkit.py selfcheck` — exits 0 with 28 entries and 0 unclaimed; `check-kit-versions.sh` clean over 16 carriers; `gen_map.py --check` exits 0; runbook parity back to its pin of 18 with the new anchored section

## Owed at the close

The `branch-reconcile selftest` leg and every leg on the spec's §7 line run in the close's bar.
The selftest budget of 60 s is a floor, re-measured once every unit is built.
