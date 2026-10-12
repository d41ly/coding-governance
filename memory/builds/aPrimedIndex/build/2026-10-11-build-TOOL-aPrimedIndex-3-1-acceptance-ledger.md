# TOOL-aPrimedIndex-3 — acceptance ledger

**Serves:** journal TOOL-aPrimedIndex-3

No merge bar and no self-test suite ran in this pass. Criteria 1 to 4 were observed through the new
canary block 1s, run as a slice: the suite's prologue plus that block, from inside the kit
directory, with the slice deleted before the commit. Against the built runner it printed `SLICE
PASS (6 assertions)` in 3 m 9 s. With the preflight block cut from the runner it printed five
`canary:` lines and `SLICE FAIL`; restored byte-identical, it passed. Criterion 5 was observed in
`pi3`, a `git clone --local` of this branch at the unit-2 commit under a short root in `TEMP`,
carrying this pass's runner, over a one-leg `GATE_LEGS` manifest. The gate guard refused a
`GATE_FULL=1` prefix during BUILDING, so these runs carried none; a one-leg manifest has no guard to
lift. The close still owes the run-gates canary whole.

**Evidences:** TOOL-aPrimedIndex-3
- AC1 — `run-gates: REFUSED` — slice arm 1s-a: a fixture descriptor whose staged `check` exits 1 made the runner exit 2 with `regen: STALE`, `run-gates: REFUSED` and the `--regen` remedy, and its output carried no `gate queue:` and no `GATE ` line. With the preflight cut, 1s-a reported exit 0 and a reached leg.
- AC2 — amended rev-2 — the empty case is a tree with no kit descriptor at the tool root, which the runner announces itself, `no kit descriptor under tools/`, spawning no python; slice arm 1s-e observed it and the leg ran, and slice arm 1s-b observed the fresh case print `regen: 1 declared · 1 fresh · 0 stale` and `GATE ok    quick`. The section 9 line for rev-2 logs it.
- AC3 — `GATE_REGEN_CHECK` — slice arm 1s-c: over the stale fixture with `GATE_REGEN_CHECK=0`, the runner printed `generated outputs NOT checked — GATE_REGEN_CHECK=0; a stale one reds its own leg at the end of the bar` and ran its leg to exit 0.
- AC4 — `grep -n "regen" tools/run-gates/README.md memory/guides/MERGE-BAR.md` — it printed 15 lines in the README, among them the exit-2 row and the section "Every bar proves them fresh before it queues", and 3 in `MERGE-BAR.md`, the new paragraph. Slice arm 1s-d: the `--print-profile` run printed no `regen:` line.
- AC5 — `--regen` — in `pi3`, with one row removed from `memory/gotchas/INDEX.md` and committed, the runner exited 2 after 82 s. It printed `regen: STALE · stage 2 · memory-tree · memory/gotchas/INDEX.md` and `run-gates: REFUSED`, and no queue or leg line. After `run-gates.sh --regen` (`moved: memory/gotchas/INDEX.md`) and a commit, the same bar printed `regen: 11 declared · 11 fresh · 0 stale · 61s`, acquired the queue, ran its leg and printed `gates GREEN — 1/1 legs passed`.
