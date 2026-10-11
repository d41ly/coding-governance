# TOOL-aFrugalTurnstile-3 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-3

No merge bar, no runner and no self-test suite ran in this pass. AC1 to AC5 ran one scratch script
that cut the writer out of the driver with the suite's `slice_fn` recipe, defined `GIT` as plain
git, and called it in a scratch repository and a linked worktree under a short temp root. On the
driver at `bef97330` the cut found no writer, so all five were RED; on the working driver all five
were GREEN. AC6 to AC8 ran four slices of the driver suite, each its prologue plus one new block,
from the temp root with the kit-dir variable set to `tools/unattended`. The AC6 slice over the base
driver, extracted with `git archive bef97330`, was RED on its `hit` and both `same` lines, and the
three AC6 and AC7 slices over the working driver were GREEN (n 23, 22 and 23, st 0). AC7 cannot be
RED at base on its absence lines, because the base writes no record; its `hit` line is RED there,
since the base driver holds the sentence zero times. AC8 was GREEN on the working driver and RED on
a staged break, a driver copy with `bar_paths` and its argument dropped, where the key-order `same`
failed and named the missing key. The close still owes both new arm blocks in
`tools/unattended/unattended.test.sh`, run by the suite in full, and every §7 leg.

**Evidences:** TOOL-aFrugalTurnstile-3
- AC1 — `by unattended` — rc 0, kind full, HEAD and a clean tree wrote the ten keys with `by unattended`, `kind full`, the passed bar and run id, and a tree equal to `git rev-parse HEAD^{tree}`.
- AC2 — `write_bar_green` — rc 1 printed nothing and left no `gate-bar-green`.
- AC3 — `write_bar_green` — an untracked file left no record and printed `no gate-bar-green written: the tree is not clean`.
- AC4 — `head before` — the parent of HEAD as `head before` left no record and printed `HEAD moved`.
- AC5 — `gate-bar-green.shared` — called from a `git worktree add` tree, the record was written in the worktree's git dir and the common dir held `gate-bar-green.shared`.
- AC6 — `GATE_CMD` — `--preflight` then `--close` with GATE_FULL=1 left a record whose `bar` was the declared `GATE_CMD` `bash probe-gate.sh` and whose `by` was `unattended`; the base driver left none.
- AC7 — `the bar did not run full` — without GATE_FULL under `primary` the close printed `the bar did not run full` and wrote none; with the probe exiting 1 the item was unmet and none was written.
- AC8 — `cut -f1` — both writers' `cut -f1` columns equalled each other and the ten keys in order; the copy with `by` dropped compared unequal, and the staged break failed the comparison.
- AC9 — `1` — `grep -c 'WHAT THIS RECORD DOES NOT CHECK' tools/unattended/unattended.sh` printed `1`.
