# TOOL-aPrimedIndex-7 — acceptance ledger

**Serves:** journal TOOL-aPrimedIndex-7

No merge bar and no self-test suite ran in this pass. Criteria 1, 2, 4 and 5 were observed through
the new canary block 1t, run as a slice: the suite's prologue plus that block, from inside the kit
directory, with the slice deleted before the commit. Against the built verb and runner it printed
`SLICE PASS (7 assertions)` in 154 s. Blocks 1r to 1t together also passed once, apart from 1t-a's
first form; that form timed the whole verb and failed on interpreter start-up alone, about 2 s per
python on node `a`. 1t-a now reads the verdict's own seconds.

Two red runs. Against the verb and runner as committed before this pass, 1t-a, 1t-b, 1t-d and 1t-e
printed `canary:` lines, and 1t-a read `took 8s to time out` through the pipe. Against the built
files with the stop after a failed stage removed and `--regen-list` routed to `--check`, 1t-c and
1t-d printed theirs. Both files were restored byte-identical (`cmp`).

Criterion 3 and the documents were observed directly. The close still owes the run-gates canary
whole.

**Evidences:** TOOL-aPrimedIndex-7
- AC1 — `GATE_REGEN_BOUND=2` — slice arm 1t-a: a fixture check of `bash -c 'sleep 8 & wait'` printed `(timed out, 3s)`. A direct run printed the same with a 6 s wall clock, of which python start-up alone measured 2 s. The pipe version printed 8 s.
- AC2 — `declined` — slice arm 1t-b printed `regen: declined · stage 1 · one` and stage 2 wrote its marker, exit 0. Slice arm 1t-c, with the stage-1 check failing too, printed `regen: FAILED · stage 1 · one` and `stopped after stage 1`, exit 1, with no marker.
- AC3 — `PYTHONUTF8=0` — with it set, `regen.py --list` wrote `·` as the UTF-8 bytes `302 267`. Run from PowerShell, where `shutil.which('bash')` named `C:\Windows\system32\bash.EXE`, `regen.py --check` read every bash item fresh in this linked worktree. Its only two stale items were this pass's own outputs, which were regenerated afterwards.
- AC4 — `gate queue:` — slice arm 1t-d: the runner's `--regen-list` output equalled the verb's `--list`, and `--regen` and `--regen-check` exited 0. Neither printed a `gate queue:` or `gate profile:` line.
- AC5 — `declaration refused` — slice arm 1t-e: a check naming a missing `gone.sh` made `regen.py --list` exit 2 naming `tools/three/gone.sh` and "not in this tree". The runner exited 2 with `declaration refused` and without the `--regen` remedy.
- AC6 — `grep -n "write" tools/unattended/README.md` — it shows the new sentence naming `write`, `check` and `stage`. `regen.py --list` on this tree printed `regen: skipped · memory-tree · [[regenerate]] bash tools/memory-tree/adopt-memory-tree.sh --render` and the `--arm-routing` row.
