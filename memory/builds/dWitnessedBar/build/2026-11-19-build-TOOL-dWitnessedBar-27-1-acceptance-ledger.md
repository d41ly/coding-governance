# TOOL-dWitnessedBar-27 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-27

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: the canonical
`refuse-wrong-shell.sh` run under Git's bash and under `wsl.exe`, a member and a sourcer run under
`wsl.exe`, the two resolver canonicals called from `python -c` and `node -e`, the coverage arm's
function and section `2n`'s rows cut out of `resolve-python.test.sh` with `sed` and run alone, over
the worktree and over a scratch clone under `%TEMP%`, and an `awk` cut of every inline block compared
with its canonical. The `New arm:` of spec section 7 still owes its RED-first observation, which the
main loop makes at the close, and so does every suite the section names.

**Evidences:** TOOL-dWitnessedBar-27
- AC1 — `Git's bash` — `wsl.exe -e bash refuse-wrong-shell.sh`, run in the worktree's `tools/lib/`,
  printed the two `refuse_wrong_shell:` lines naming the file's `/mnt/c/` path and
  `run it with Git's bash (C:/Program Files/Git/bin/bash.exe).`, and exited 2.
- AC2 — `/home/u/mirror.held/s/tools/x.sh` — `wsl.exe -e bash refuse-wrong-shell.sh --probe` with
  that path exited 0 and printed nothing.
- AC3 — `/mnt/c/r/tools/x.sh` — `bash refuse-wrong-shell.sh --probe` with that path under Git's bash,
  `WSL_DISTRO_NAME` unset, exited 0. The same probe with `WSL_DISTRO_NAME` set exited 2.
- AC4 — `refuse_wrong_shell:` — `wsl.exe -e bash merge-rows.sh` in `tools/memory-tree/` printed the
  two refusal lines and nothing else, and exited 2.
- AC5 — `refuse_wrong_shell || exit 2` — the 82 inline members and the six sourcers, 88 files (DERIVED, the spec's PINNED population)
  (DERIVED, that comparison's output), all sit in the files `git grep -l` lists for the call, and
  `grep -c` over `resolve-python.sh` printed 0. The coverage arm's function, run over the worktree,
  printed no break and the counts 82 inline, 82 blocks, 6 sources and 88 calls (DERIVED). In a scratch
  clone with `merge-rows.sh`'s call cut and a new `tools/planted.sh` carrying only a `resolve_python`
  block, it named both files. A further plant of a stray block, a source with no call, a call with no
  source and a call in the library named each file under its own assertion. The suite's own run of
  the arm is owed to the close.
- AC6 — `tried:` — `wsl.exe -e python3 resolve_bash.py` in `tools/lib/` printed one `refused:` line
  naming the file's `/mnt/c/` path and Git's bash, printed no `tried:` line, and exited 2. Node d's WSL
  has no `node`, so the JavaScript half is observed by AC7's truth table, as the criterion allows.
- AC7 — `/mnt/data/` — section `2n`'s rows, cut out and run alone, gave `1 0 0 0 0 0` from the shell
  probe, `wrong_shell_at` and `wrongShellAt`, one verdict per row. With the Python twin's drive test
  cut to `p.startswith("/mnt/")`, the row `/mnt/data/x.sh` refused in Python and the section's
  Python assertion failed. Where WSL's interop entry exists, a marker-0 row asks the sourced shell
  predicate, because that entry cannot be unstaged; node d's Git bash has none, so every row ran
  through `--probe`.
- AC8 — `run it with Git` — `grep -n` printed lines 43 and 56 of `refuse-wrong-shell.sh` and line 67 of
  `help/python-floor.md`, each carrying `run it with Git's bash (C:/Program Files/Git/bin/bash.exe).`
- AC9 — `refuse-wrong-shell.sh` — the `git grep -n -E` of the criterion printed five lines, and each
  names `refuse-wrong-shell.sh`.
