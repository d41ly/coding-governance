# TOOL-aIndexedAnchor-2 — acceptance ledger

**Serves:** log TOOL-aIndexedAnchor-2
**Caused-by:** TOOL-aIndexedAnchor-2

One builder pass over base `ccef58129`, committed as `9968d68ca`. The suite runs below were made by the main
loop at the close, one in this worktree and one in a detached scratch worktree of `9968d68ca` whose
`lib-unattended.sh` had the two sibling patterns removed from `build_commit`'s grep; that worktree was removed.

**Evidences:** TOOL-aIndexedAnchor-2
- AC1 — the `build_commit 229f1ddef..7a7566928 TOOL-aIndexedAnchor-1 memory/builds/aIndexedAnchor` probe answered `398ba9252`, the unit's product commit, where the shipped library answered the spec commit `1b161ee30`; re-run at `9968d68ca` by the loop witness, exit 0.
- AC2 — `bash tools/unattended/check-pass-order.sh` in the `sibling records` arm's spec-half fixture exited 0, printed `graded 1 closed unit` and no `FAILED`.
- AC3 — `bash tools/unattended/check-pass-order.sh` in the arm's product-half fixture exited 1 naming `ARCH-tS-1 — BUILT at` the `ARCH-tS-1: build the thing` commit, with the patterns present and with them absent.
- AC4 — the same arm's exclusion-line check read `<build folder> <every build's BACKLOG.md and README.md>`.
- seen-red — `unattended pass-order selftest` — red `9968d68ca` — green `9968d68ca` — `sibling records`: the two sibling patterns removed from `build_commit`'s grep red the spec half's exit code and its no-violation check; the product half stayed green; the suite's other 87 failures read identically in both trees, environmental and not this unit's
