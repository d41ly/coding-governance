# TOOL-aLevelledCopy-2 — acceptance ledger

**Serves:** journal TOOL-aLevelledCopy-2

No merge bar and no self-test suite ran in this pass. The criteria were observed directly on node a.
Each new arm of `tools/check-wiring.test.sh` ran as a slice inside the kit directory. A slice is the
suite's prologue, the arm block's shared header and that one arm. The slices used fixture repos under
a short `%TEMP%\lc2` directory, each with its own `GIT_CONFIG_GLOBAL` and `GIT_CONFIG_NOSYSTEM=1`.
Against the built checker, all nine slices printed only `ok` lines and exited 0. Each slice then ran
against a scratch copy of the checker carrying that arm's staged break, or a copy of `push-main.sh`
for AC8. All nine printed `FAIL` and exited 1. After cleanup the built checker is the only copy. The
close still owes `check-wiring self-test` and `push-main self-test` run whole. It also owes the
`transition-audit arms`, `straggler-guard arms`, `lexicon naming predicates`, `install-prefix
(shipped surface)` and `memory hygiene` legs.

**Evidences:** TOOL-aLevelledCopy-2
- AC1 — `FIXED    ssh` — `--session` on an unset fixture set `core.sshCommand` byte-equal to the value from running the definition line alone. `health.log` held one `sshcommand-set` line. A second run printed `ok       ssh` and the count stayed 1. Break, the `add_health_event` call neutralised: both AC1 lines printed `FAIL`.
- AC2 — `ServerAliveInterval=31` — with the fixture copy's definition line edited from 30 to 31, the value set carried 31. Break, a literal 30 string assigned after the derivation: `FAIL`.
- AC3 — `note     ssh` — `ssh -i ~/.ssh/id_test` was pre-set at local scope, then separately at the fixture's global scope. After `--fix` then `--session`, `--show-scope --get-all` printed only that value at that scope, and the run printed a `note     ssh` line naming `(local)` and then `(global)`. Break, the read narrowed to `--local`: the global case printed `FAIL`.
- AC4 — `ok       ssh` — an operator value `ssh -o ServerAliveInterval=15` printed `ok       ssh       — core.sshCommand is the operator's (local) and carries its own keepalive` under `--check`. Break, the operator-keepalive branch removed: `FAIL`.
- AC5 — `skip     ssh` — the https remote and the no-remote fixture each printed `skip     ssh       — no remote pushes over ssh`, and `git config core.sshCommand` printed nothing. Break, every `://` URL read as ssh: the https case printed `FAIL`.
- AC6 — `UNWIRED  ssh` — a deleted and a duplicated definition line each printed `UNWIRED  ssh       — cannot derive the keepalive from tools/push-main.sh` with exit 1. Break, the exactly-one count guard dropped: the duplicated case printed `FAIL`.
- AC7 — `Fix:` — `--check` on an unset ssh fixture printed `UNWIRED  ssh` with `Fix: git config core.sshCommand '<value>'` and exited 1, and nothing was written. Break, the arm's fix branch forced on: `FAIL`.
- AC8 — `grep -c ServerAliveInterval tools/push-main.sh` — it printed 1, on the `GOV_SSH_KEEPALIVE=` line. The `GIT_SSH_COMMAND:=\$GOV_SSH_KEEPALIVE` count printed 1, and `grep -c ServerAliveInterval tools/check-wiring.sh` printed 0. Break, a push-main copy with a second literal in a comment: `FAIL`.
- AC9 — `sed` — the two lines extracted with `sed` and evaluated with `GIT_SSH_COMMAND` unset held the original three-option string. With `ssh -i k` preset they held `ssh -i k`. `bash -n tools/push-main.sh` exited 0.
- AC10 — `skip     ssh` — with no `push-main.sh` in the fixture, `--session` printed `skip     ssh       — push-main is not adopted here…` and set nothing. Break, the path taken without a file test: `FAIL`.
- AC11 — `grep -n sshcommand-set tools/check-wiring.sh` — it hit the header's health-event sentence on line 31 and the arm's `add_health_event` call. The usage line's auto-fix list names `core.sshCommand`.
- AC12 — `skip` — `bash tools/check-wiring.sh --check` in gov's own worktree printed `skip     ssh       — no remote pushes over ssh` and exited 0.
- AC13 — `FAIL` — every slice printed only `ok` against the built checker and at least one `FAIL` against its staged break, as AC1 to AC8 and AC10 record. Each slice took 1 to 4 minutes, not the spec's estimated 20 s, because one checker run in a fixture costs about 45 s on node a.
