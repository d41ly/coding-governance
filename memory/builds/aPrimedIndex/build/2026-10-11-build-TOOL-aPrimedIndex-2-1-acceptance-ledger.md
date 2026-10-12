# TOOL-aPrimedIndex-2 — acceptance ledger

**Serves:** journal TOOL-aPrimedIndex-2

No merge bar and no self-test suite ran in this pass. Criteria 1 and 5 were observed on this
worktree. Criteria 3 and 4 were observed in `pi2`, a `git clone --local` of this branch at its unit-1
commit under a short root in `TEMP`, carrying this pass's reader and runner. Criterion 2 was
observed through the new canary block 1r, run as a slice: the suite's prologue plus that block, from
inside the kit directory, with the slice deleted before the commit. The block printed `SLICE PASS (4
assertions)`. With `build_items` changed to skip a partial row instead of refusing it, 1r-c printed
its `canary:` line and the slice printed `SLICE FAIL`. Restored, it passed again. The clone also
found a second defect, folded here as part of S1: under an inherited `PWD` naming node `a`'s TEMP by
its 8.3 short name, the drift-audit render wrote `../../../../../DAILY-~1/...` paths into its Skill.
The reader now drops `PWD` for every child it runs, and the re-run moved no render. The close still
owes the run-gates canary whole.

**Evidences:** TOOL-aPrimedIndex-2
- AC1 — `regen.py --list` — on this tree it printed the eleven items of TOOL-aPrimedIndex-1's inventory, the eight stage-1 renders, then the two stage-2 indexes, then the stage-3 map, each once, and `regen: 11 declared across 9 kit(s), in 3 stage(s)`.
- AC2 — `regen.py --list` — slice arm 1r-c: a fixture descriptor whose `[[generated]]` row carries `write` alone exited 2 with `REFUSED`, naming `tools/fake/kit.toml` and "all three or none". Break above.
- AC3 — `regen.py --check` — in `pi2` with one row removed from `memory/gotchas/INDEX.md` and committed, it exited 1 with `regen: STALE · stage 2 · memory-tree · memory/gotchas/INDEX.md` and `10 fresh · 1 stale`. `git status --porcelain` was byte-identical before and after. On the clone before the edit it exited 0 with `11 fresh · 0 stale` in 106 s.
- AC4 — `regen.py --write` — in the same clone it printed `stage 2 · 2 item(s) · written · moved: memory/gotchas/INDEX.md` and moved nothing in stages 1 and 3. A following `--check` exited 0, `11 fresh`. In a two-kit fixture whose stage-1 write exits 1, `--write` printed `stopped after stage 1` and exited 1, and the stage-2 write's marker file was never created.
- AC5 — `--regen-list` — handed to the runner as its first argument through `bash`, its output was byte-identical to `regen.py --list` (`cmp` exited 0), and `grep -n "regen" tools/run-gates/README.md` shows the three verbs, the exit table and both knobs.
