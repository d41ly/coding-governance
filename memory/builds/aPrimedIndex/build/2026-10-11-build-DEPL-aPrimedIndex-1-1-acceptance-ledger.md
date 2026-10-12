# DEPL-aPrimedIndex-1 — acceptance ledger

**Serves:** journal DEPL-aPrimedIndex-1

No merge bar and no self-test suite ran in this pass. Both criteria were observed by executing the
new self-test block alone. A scratch harness extracted the block from `tools/govkit/selftest.py`
and supplied the suite's `check` and `govkit_module` helpers. It ran twice: once against the built
`tools/govkit/govkit.py`, and once against the reader as committed before this pass, loaded from
`git show HEAD:`. `govkit.py selfcheck` exited 0 over the edit, and the map stayed fresh. The close
still owes the govkit self-test whole.

**Evidences:** DEPL-aPrimedIndex-1
- AC1 — `GATE_REGEN_CHECK=0` — called over a fixture target whose runner prints `GATE ok    fixture leg` only when that value reaches it, and otherwise exits 2, the built reader returned `{'fixture leg': 'green'}`. The committed reader, which has no `env` argument, returned `{}`.
- AC2 — `check` — the block alone printed `ok   [aPrimedIndex-1] the verdict reader skips the runner's preflight, so a leg still reads` and exited 0 against the built reader. Against the committed reader it printed `FAIL` with `{}` and exited 1.
