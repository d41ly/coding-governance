**Serves:** journal TOOL-dSafePassage-31

# TOOL-dSafePassage-31 — acceptance ledger

The unit as built, at spec rev-3. In `tools/govkit/upgrade_steps.py`: `read_pid_namespace` reads
`PID_NS_LINK` (`/proc/self/ns/pid`) where the link exists and returns `""` where it does not;
`add_boot_start`, the one record writer `take_write_lock` and the reclaim guard both call, writes
`pid_ns` beside `platform`, `boot_id` and `started_boot`; `check_holder_dead` reads an absent
`pid_ns` as `""` and answers `unknown` where it differs from this process's, after the `platform`
and `boot_id` rows and before the census, and `unknown` naming the error where the link exists and
cannot be read. The `lock` fixture family gains `lock-foreign-pidns` and `lock-no-pidns`, its child
a `pidns <value>` stand-in for `read_pid_namespace`; `plant_lock` and the `guard-dead` guard record
this process's `pid_ns`, so the existing plants keep their verdicts on a Linux judge. The selftest
gains two `[dSP-31]` rows; `help/upgrade-steps.md`'s "After a kill" paragraph names the `pid_ns`
refusal and TOOL-dSafePassage-32's missing-boot-reading refusal. `govkit.py` is unchanged: the
record is written through `add_boot_start`, which `take_write_lock` already calls.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows) by the fixture CLI or a `python` probe of the changed code.

- AC1 — `fixture lock --plant lock-dead` exit 0: `lock: held by pid 17040 · host compeeto-agent · pid_ns ''`. The WSL half: node d no longer has a distro named `Ubuntu` (`wsl.exe -d Ubuntu` answered `WSL_E_DISTRO_NOT_FOUND`; `wsl.exe -l` lists `claude-u26` and `docker-desktop`), so the probe ran under `wsl.exe -d claude-u26`: `read_pid_namespace()` printed `pid:[4026532398]`, and `add_boot_start` returned a record carrying `'pid_ns': 'pid:[4026532398]'`. Under that distro, `fixture lock --plant lock-dead` exit 0 with `pid_ns 'pid:[4026532398]'`, so the existing plants still reclaim on a Linux judge.
- AC2 — `fixture lock --plant lock-foreign-pidns` exit 1: `refusing rather than joining in: unknown, it was taken under pid_ns 'pid:[4026532244]', not this process's 'pid:[4026532221]'`, `lock: the planted lock unchanged`. Red when, observed: the row patched to `if False:` reclaimed, printed `lock: the planted lock CHANGED` and three `lock: FAILED` lines, exit 1; restored byte-identical (`cmp`).
- AC3 — `fixture lock --plant lock-no-pidns` exit 1: `unknown, it was taken with no pid_ns recorded`, `lock: the planted lock unchanged`, then the take with this process's `pid_ns` `""` reclaimed the dead holder: `lock: with no pid_ns here, the take exits 0`. Under `wsl.exe -d claude-u26` the same plant printed the same reclaim. Red when, observed: the same `if False:` patch reclaimed on the first take, `lock: FAILED` lines, exit 1.

Regression probes of the touched plants on node d: `guard-dead` exit 0, `lock-foreign-namespace` exit 1 with its `platform 'gk-elsewhere'` refusal.

OWED AT THE CLOSE: the bar's legs §7 names, and the New arm's RED-first observation (the two
`[dSP-31]` rows of `tools/govkit/selftest.py`, red on a judge copy that skips the `pid_ns` row,
green restored).
