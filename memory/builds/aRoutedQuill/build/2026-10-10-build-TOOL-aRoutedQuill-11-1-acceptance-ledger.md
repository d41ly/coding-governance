# TOOL-aRoutedQuill-11 — acceptance ledger

**Serves:** journal TOOL-aRoutedQuill-11

No merge bar and no held suite ran in this pass. The criteria were observed directly on node a,
each checker case in its own `git clone --local` of parent 7bd1cb3b with the three changed files
copied in and the conf edited there, never in the worktree; the clones were removed afterwards.
The six checker runs went concurrently. Two staged breaks were observed red: the parent's
`scratch-guard.js` failed the AC3 probe with exit 1, and the parent's `check-wiring.sh`, in a
clone with no `MEMORY_ROOT`, printed `ok       routed` while the gate's own reader said
`MEMORY_ROOT is blank or absent`. The new arms in `check-wiring.test.sh` were not run here; the
close owes the `check-wiring self-test` leg and the rest of §7 inside the bar.

**Evidences:** TOOL-aRoutedQuill-11
- AC1 — `check-wiring.sh` — with the `MEMORY_ROOT=` line deleted, `--check` printed the `UNWIRED  routed    — MEMORY_ROOT is blank or absent in .memory-tree.conf, so the write gate is UNARMED` line and exited 1; the parent's checker printed `ok       routed` on the same conf.
- AC2 — `check-wiring.sh` — `MEMORY_ROOT=""` and `export MEMORY_ROOT=memory` with `ROUTED_PATHS="memory/"` each printed the node probe's line verbatim inside the `UNWIRED  routed` line; the repo's own conf printed an empty node line and `ok       routed`, the liveness half.
- AC3 — `scratch-guard.js` — the `typeof checkUnarmed` probe exited 0 at the worktree root and 1 against the parent's copy.
- AC4 — `check-wiring.sh` — with the one directory holding `node` dropped from `PATH`, the routed line read `skip     routed    — no node on PATH` and no `UNWIRED  routed` line printed.
- AC5 — `check-wiring.test.sh` — `grep -c 'RQ11'` printed 2 and `grep -c 'MEMORY_ROOT=memory'` printed 11.
- AC6 — `check-wiring.sh` — the `sed` and `grep -cE` probe over `check_routed` printed 0, and 1 over the parent's copy.
