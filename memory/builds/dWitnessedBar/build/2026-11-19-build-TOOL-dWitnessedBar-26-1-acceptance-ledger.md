# TOOL-dWitnessedBar-26 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-26

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed through
probes of the unit's own code on node d, 2026-11-19: the two canonicals' CLIs under staged `PATH`
values, a `python -c` call of `scan_bare_bash` over the tree and over a fixture repository under
`%TEMP%`, a `python -c` call of govkit's `resolve_shell_argv`, the floor stub and `regen.py --check`
run directly, and an `awk` cut of every inline block compared with its canonical. The staging used a
copy of `C:/Windows/System32/bash.exe` placed outside System32, Git's `cmd` directory, and System32 itself.
Each `New arm:` of spec section 7 still owes its RED-first observation, which the main loop makes at
the close, and so does every suite the section names.

**Evidences:** TOOL-dWitnessedBar-26
- AC1 — `answered Linux` — `python resolve_bash.py --host windows` ran with `PATH` set to the copy's
  directory, then System32, then Git's `cmd`. It printed three `tried:` lines in candidate order:
  Git's `bin/bash.exe` with `runs`, the copy with `answered Linux`, and System32's with
  `a launcher`. It then printed `bash: C:/Program Files/Git/bin/bash.exe` and exited 0.
- AC2 — `GOV_BASH` — the same command with Git's `cmd` left off `PATH` printed
  `git --exec-path: did not run`, the copy as `answered Linux` and System32's as `a launcher`. It
  then printed a `refused:` line that names all three and ends `set GOV_BASH to Git's bash`, printed
  no `bash:` line, and exited 2.
- AC3 — `--host posix` — with `PATH` set to the copy alone, the command printed the copy with `runs`,
  then `bash:` naming the copy, and exited 0.
- AC4 — `tried:` — with `GOV_BASH` set to a Python file, the command printed one `tried:` line,
  `<value>: did not run`, then a refusal naming `GOV_BASH` and the value, and exited 2. With
  `GOV_BASH` set to Git's own `bash.exe`, it printed that path and exited 0.
- AC5 — `node resolve_bash.js` — under each of the four stagings above, the twin's stdout was
  byte-identical to the Python CLI's (`cmp`) and its exit code was the same.
- AC6 — `resolve_bash_js` — the parity arm's `blk` range, widened to read a `// >>> ` marker, cut
  `resolve_bash_py` from the canonical and its 13 inline copies, `tools/govkit/upgrade_steps.py`
  among them. It cut `resolve_bash_js` from the canonical, `tools/unattended/stop-guard.js` and
  `tools/policy/policy-mirror.js`. Every copy equalled its canonical. The one-byte red half, and the
  suite's own run of the rows and of section `2j`, are owed to the close.
- AC7 — `scan_bare_bash` — called with the worktree root at the pass tip, it returned `[]`. Before the
  sites were rewritten, the same call listed 15 lines (DERIVED, that scan's output): the seven PATH loops, `tools/govkit/selftest.py`'s
  two name loops and its `["bash", …]` launch, govkit's membership test, `tools/loop/factories.py`'s
  and `tools/policy/check_policy.py`'s `or "bash"` fall-backs, `stop-guard.js`'s spawn, and the scan's
  own name tuple. It was then called over a fixture repository holding
  `subprocess.run(["bash", "x.sh"])`, `("bash.exe", "bash")`, `[f() or "bash", "x.sh"]`,
  `spawnSync('bash', [])` and `f() || 'bash'`. It named all five, each with its shape.
- AC8 — `Refusal` — with `PATH` staged as in AC2 and `GOV_BASH` unset,
  `govkit.resolve_shell_argv(["bash", "x.sh"])` raised `Refusal`, and its text named every `tried`
  line and `GOV_BASH`. With Git's `cmd` on `PATH`, it returned
  `['C:/Program Files/Git/bin/bash.exe', 'x.sh']`. Under the first staging,
  `python tools/govkit/steps/python_floor.py preflight` exited 2. Its stderr was one
  `python_floor.py: govkit: no bash runs: …; set GOV_BASH to Git's bash` line with no `Traceback`.
- AC9 — `regen: REFUSED` — `python tools/run-gates/regen.py --check` with `GOV_BASH` set to a file
  that is not a bash printed one `regen: REFUSED` line naming `GOV_BASH` and exited 2, before
  `run_checks` ran any row.
