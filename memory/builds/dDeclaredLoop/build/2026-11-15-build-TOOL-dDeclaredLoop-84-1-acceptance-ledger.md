# TOOL-dDeclaredLoop-84 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-84

No merge bar, no self-test suite and no gate leg ran in this pass. The pass wrote spec text only: 82
S4's sentence keeping the rest of 75 S27's exit table, and 82 AC4's class-level checks, as a rev-6
bump of the 82 spec with its revision-log line citing the round-6 spec audit by file stem. Each
criterion was observed by its own grep over the 82 spec in the working tree, and every grep was also
run at the pass's base `d26b25130` before the edit, where each printed 0, so each can read red. The
checks the new AC4 names were read against the tree as it stands: over the 75 spec,
`grep -c "any other exit code grades against the parents alone"` printed 0 and the S27-to-S28 range
grep for `never a fall to the parents` printed 1, and
`python tools/loop/guard.py --fixture --plant push-merge-tree-fatal` exited 1 with its graded line
naming `the clean re-merge failed: 128 fatal: fx stand-in`. The `its blob parses` grep over 75 still
prints 1: retiring it is 82's own pass.

Owed to the close: every leg the spec's section 7 names. The spec declares no `New arm:` line.

**Evidences:** TOOL-dDeclaredLoop-84
- AC1 — `never a fall to the parents` — over the S4-to-S5 range of the 82 spec, `grep -c` printed 1 for it and 1 for `TOOL-dDeclaredLoop-83`; at the base each printed 0.
- AC2 — `any other exit code grades against the parents alone` — over the AC4-to-AC5 range of the 82 spec, `grep -c` printed 1 for it, 1 for `never a fall to the parents` and 1 for `push-merge-tree-fatal`; at the base each printed 0.
- AC3 — `2026-10-24-review-TOOL-dDeclaredLoop-80-spec-audit` — over the section 9 to section 10 range of the 82 spec, `grep -c` printed 1; at the base it printed 0.
