# TOOL-aLevelledCopy-7 — acceptance ledger

**Serves:** journal TOOL-aLevelledCopy-7

No merge bar and no self-test suite ran in this pass. The criteria were observed directly on node a.
The suite's ssh block ran as one slice inside the kit directory: the prologue, then the LC2 and LC7
arms. Against the built checker every line printed `ok`, 20 of 20, in about 6.5 minutes. The same
slice then ran against a copy of the checker taken with `git show` from the commit before this
unit's build commit. Every LC7 line printed `FAIL` there, and every LC2 line still printed `ok`. A
second slice held LC2 AC1 and AC7 with the seed's `unset GIT_SSH GIT_SSH_VARIANT` line removed. It
printed `FAIL` against the built checker, which is S5's red. Both slices and the copy were deleted
afterwards. The close still owes `check-wiring self-test` run whole, and the `transition-audit arms`,
`straggler-guard arms`, `lexicon naming predicates`, `install-prefix (shipped surface)` and
`memory hygiene` legs.

**Evidences:** TOOL-aLevelledCopy-7
- AC1 — `GIT_SSH` — with `GIT_SSH=/bin/false` exported, `--session` printed `note     ssh       — GIT_SSH is the operator's choice of SSH program`, no `FIXED    ssh` line, `git config core.sshCommand` printed nothing, and `health.log` held no `sshcommand-set` line. Against the pre-unit checker: `FAIL`.
- AC2 — `GIT_SSH_VARIANT` — with only `GIT_SSH_VARIANT=ssh` exported, the `note     ssh` line named `GIT_SSH_VARIANT` and nothing was set. Against the pre-unit checker: `FAIL`.
- AC3 — `ssh.variant` — with `ssh.variant=plink` in the fixture's global config file, the `note     ssh` line named `ssh.variant` and nothing was set. Against the pre-unit checker: `FAIL`.
- AC4 — `UNWIRED  ssh` — `--check` under each of the three triggers exited 0, printed the matching `note     ssh` line, and printed no `UNWIRED  ssh` line and no `Fix: git config core.sshCommand`. Against the pre-unit checker all three printed `FAIL`.
- AC5 — amended rev-2 — the failing `git` is a shim first on the run's `PATH`, not an `export -f` function, because the lexicon leg grades a function named `git` as a definition. With it, `--session` printed `note     ssh       — cannot read ssh.variant (git config exit 3)` and nothing was set. Against the pre-unit checker: `FAIL`.
- AC6 — `GIT_SSH=/bin/false` — the suite now exports `GIT_SSH=/bin/false` and `GIT_SSH_VARIANT=plink` before the LC2 block, and every LC2 line printed `ok`. With the seed's unset line removed, LC2 AC1 and AC7 printed `FAIL`.
- AC7 — `grep -nw GIT_SSH tools/check-wiring.sh` — it hit the header's ssh paragraph on lines 44, 45 and 48 and the arm on lines 1344 and 1348. `grep -c ssh.variant tools/check-wiring.sh` printed 5. The same grep on the pre-unit checker printed 0 hits.
- AC8 — `FAIL` — each new arm printed `ok` against the built checker and `FAIL` against the pre-unit copy, as AC1 to AC5 record. A slice took about 6.5 minutes, not the spec's estimated 20 s, because one checker run in a fixture costs about 20 s on node a.
