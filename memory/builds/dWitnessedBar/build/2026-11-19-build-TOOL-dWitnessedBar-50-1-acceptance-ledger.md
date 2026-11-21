# TOOL-dWitnessedBar-50 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-50

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: the new
`--coverage` mode of `tools/lib/refuse-wrong-shell.sh` run on the worktree and in a scratch clone
under `%TEMP%`, `scan_rws_coverage` cut from `tools/lib/resolve-python.test.sh` and run alone over the
tree, the hook's block cut with the parity arm's `blk` range, and the hook run under WSL's bash. The
`New arm:` line of spec section 7 still owes its RED-first observation, which the main loop makes at
the close, and so does every leg that section names.

**Evidences:** TOOL-dWitnessedBar-50
- AC1 — `bash refuse-wrong-shell.sh --coverage` — run in `tools/lib/` on the built tree it printed
  `89 members, derived from 92 files the predicate selects less 3 named exclusions`, named
  `tools/unattended/lib-unattended.sh`, `tools/unattended/pass-tree.sh` and
  `tools/unattended/pass-tree.test.sh` each with its reason, and exited 0; `grep -c` of the call in
  `.githooks/pre-commit` printed 1. Before the hook's edit the same run exited 1 naming
  `.githooks/pre-commit` twice, the red the criterion names. `scan_rws_coverage` alone printed no break
  and `counts 82 83 6 89 92`; with its assertion 2 put back to unit 27's inline-member set it named the
  hook. The hook's block cut by `blk` equalled the canonical's.
- AC2 — `wsl.exe -e bash .githooks/pre-commit` — at this worktree's root on node d with nothing staged
  it exited 2, and its first two lines were the `refuse_wrong_shell:` lines naming
  `/mnt/c/.../.githooks/pre-commit`; the one line ahead of them was `wsl.exe`'s own systemd notice,
  printed before bash started.
- AC3 — `exits 1 naming that file` — in a scratch clone at `%TEMP%/u50c`: with the hook's call cut
  `--coverage` exited 1 naming `.githooks/pre-commit`; with a tracked `tools/planted-u50.sh` calling
  `$(resolve_python)` and carrying no block it exited 1 naming that file; with the reason of
  `tools/unattended/pass-tree.sh` emptied it exited 1 naming that exclusion as refused. A tracked
  non-`.sh` file under `.githooks/` with a `sh` shebang beginning a line with `resolve_python` was
  named too; restored, the clone exited 0.
