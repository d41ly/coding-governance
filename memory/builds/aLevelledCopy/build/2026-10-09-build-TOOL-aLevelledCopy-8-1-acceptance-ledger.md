# TOOL-aLevelledCopy-8 — acceptance ledger

**Serves:** journal TOOL-aLevelledCopy-8

No merge bar and no self-test suite ran in this pass. The criteria were observed directly on node a.
Each new arm ran alone as a slice inside the kit directory: the suite's prologue, the LC2 setup where
the arm sits in that block, the one arm, and a pass/fail footer. Against the built checker every new
line printed `ok`, 10 of 10. Each slice then ran with `SCRIPT` pointed at a scratch copy of the
checker carrying that arm's staged break, written beside it by a script that asserted each break's
replacement count, and every arm under its break printed `FAIL`. The existing LC2 and LC7 arms ran
as one slice against the built checker and printed 20 of 20 `ok` in about 4.7 minutes, so the
`n=0` text and the new read left TOOL-aLevelledCopy-2's and TOOL-aLevelledCopy-7's arms green. All
slices and broken copies were deleted afterwards. AC8 ran `govkit selfcheck` twice, about 26 s a run.
The close still owes `check-wiring self-test` run whole, plus the `transition-audit arms`,
`straggler-guard arms`, the govkit-directory legs, `recall floor arms`, `lexicon naming predicates`,
`install-prefix (shipped surface)`, `kit version markers`, `kit epoch` and `memory hygiene` legs.

**Evidences:** TOOL-aLevelledCopy-8
- AC1 — `sshcommand-set` — with config.lock held in the ssh fixture, `--fix` printed `UNWIRED  ssh       — could not set core.sshCommand` and exited 1, `--session` printed the same line and exited 0, `health.log` held no `sshcommand-set` line, and after the lock was released `git config core.sshCommand` printed nothing. With the else branches removed: `FAIL`.
- AC2 — `hookspath-set` — with the lock held and `core.hooksPath` unset, `--fix` printed `UNWIRED  hooks     — could not set core.hooksPath`, exited 1, printed no `FIXED` line and logged no `hookspath-set` line. With the else branches removed: `FAIL`.
- AC3 — `merge-driver-set` — with the lock held, the merge=ours fixture printed `UNWIRED  merge     — could not set merge.ours.driver` and the `install_driver` fixture at state 4 printed `UNWIRED  merge     — could not set merge.rows.driver`, each exiting 1, with no `merge-driver-set` line. With the else branches removed: both `FAIL`.
- AC4 — `--show-scope` — with a global `ssh -i ~/.ssh/id_test` and a shim exiting 129 on any argv carrying `--show-scope`, `--session` printed `note     ssh       — core.sshCommand is the operator's (scope unread)` and `git config --local core.sshCommand` printed nothing. With the read restored to the swallowed `--show-scope ... || true` form deciding the branch: `FAIL`.
- AC5 — `config --get core.sshCommand` — with the shim exiting 3 on `config --get core.sshCommand`, `--check` printed `note     ssh       — cannot read core.sshCommand (git config exited 3); NOT setting it` and no `UNWIRED  ssh` line, and `--session` wrote nothing. Under the same restored read: `FAIL`.
- AC6 — `update the push-main kit` — with the definition line deleted, `--check` exited 1 and its line began `UNWIRED  ssh       — cannot derive the keepalive from tools/push-main.sh` and carried `predates` and `update the push-main kit`. With the `n=0` branch removed, so today's text printed: `FAIL`.
- AC7 — `skip LC2 arms` — in a `git clone --local` under `%TEMP%\lc8`, with the built checker and suite copied in and the clone's `tools/push-main.sh` holding no definition line, the prologue, LC2 guard and LC2 AC1 slice printed `FAIL LC2 AC1` twice while the clone had no receipt. After `{"schema": 3, "files": []}` was written to `.governance/install.json` it printed `skip LC2 arms — the installed push-main.sh predates GOV_SSH_KEEPALIVE (kit skew); …` and no `FAIL`.
- AC8 — `requires_if` — with the row's kit changed to `push-mian`, `python tools/govkit/govkit.py selfcheck` exited 1 printing `govkit: entry 'check-wiring' requires_if names 'push-mian', which is not a registry entry`. Restored, it exited 0 and printed no `requires_if` line.
- AC9 — `ran` — with the fixture's definition line `GOV_SSH_KEEPALIVE='ssh'$(touch "<fixture>/ran")`, `--session` left no file named `ran`, printed `UNWIRED  ssh       — cannot derive`, and set nothing. With the `sed` derivation swapped for `eval "$(grep '^GOV_SSH_KEEPALIVE=' "$pm")"`: `FAIL`.
- AC10 — `ssh://` — the remote C:/x/origin.git printed `skip     ssh       — no remote pushes over ssh` and set nothing, and ssh://git@example.invalid/o/r.git printed `FIXED    ssh` with the local value equal to the derived one. With `${#host} -gt 1` changed to `-gt 0` the drive-path arm printed `FAIL` and the `ssh://` arm `ok`; with the `ssh://` case line removed the reverse.
- AC11 — `FAIL` — each new arm printed `ok` against the built checker and `FAIL` against its staged break, as AC1 to AC6, AC9 and AC10 record. AC7's red is the receipt-less clone's `FAIL LC2 AC1`. The new-arm slices were not timed one by one.
