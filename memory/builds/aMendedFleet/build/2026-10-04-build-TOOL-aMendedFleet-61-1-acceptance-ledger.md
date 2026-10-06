# TOOL-aMendedFleet-61 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-61

**Evidences:** TOOL-aMendedFleet-61
- AC1 — `cli-version: 2.1.286` — the unattended suite's prologue, lines 1 to 626, plus the new arm, cut into a slice in the session scratchpad with `HERE` pinned to the kit dir and the fixture root under `%TEMP%`/amf61: 39 of 39 assertions passed, `--preflight` under `AI_AGENT=claude-code_2-1-286_harness` printed `the launching CLI pinned as cli-version: 2.1.286` and the fixture's `RUN.md` carried `cli-version: 2.1.286`. Staged break: with the dash-to-dot turn in `read_cli_version` removed, nine assertions failed and the pin read `absent`
- AC2 — `WARNING` — the same slice: a holder `--resume` under `AI_AGENT=claude-code_2-1-178_harness` printed one `WARNING` naming `2.1.178` and `2.1.286`, exited 0, and the pin still read `2.1.286`. Staged break: with the `print_cli_version_drift` call deleted from `print_resume_orientation`, six assertions failed, the first being this warning
- AC3 — `UNKNOWN` — the same slice: with `AI_AGENT` unset through `env -u`, and with `AI_AGENT=other-agent_2-1-286_harness`, each resume printed `CLI version UNKNOWN — this session's side is missing`, and the unset run's exit equalled the older-CLI run's. Staged break: a `read_cli_version` that skipped the `claude-code_` prefix test read the foreign value as a version, one FAIL
- AC4 — `2.1.99` — the same slice: `2-1-286` printed the same-version line and no `OLDER than`/`newer than` line, `2-1-290` printed one `NOTE` naming both, and `2-1-99` printed one `WARNING` naming both. Staged break: the integer loop replaced by a `[[ $now < $pin ]]` string comparison, and the `2.1.99` arm failed
- AC5 — `read_tick_registration` — the same slice sourced `tools/unattended/lib-unattended.sh`: a stub `schtasks` and `crontab` exiting 0 first on PATH returned 0, a pair exiting 1 returned 1, and a PATH holding only a `uname` wrapper returned 2 with `TR_WHY` reading `... is not on PATH`; preflight with the exit-1 stub printed `WARNING — no scheduled task named gov-resume-tick exists on this node` and exited 0. Staged break: the function returning 1 before its probe, three FAILs
- AC6 — `bash tools/unattended/adopt-unattended.sh --check` — on node a, where the task is not registered, it printed `unattended: WARNING — no scheduled task named gov-resume-tick on this node; …`, no `INFO` line naming it, and exited 0. The base copy of the adopter, from `git show HEAD:`, printed the `INFO` line in the same place and also exited 0
- AC7 — `grep -n "cli-version" tools/unattended/README.md` — one hit, line 199, in the resume-tick section's paragraph on what `--preflight` pins

## The suite arm

The S8 arm in `tools/unattended/unattended.test.sh` was run only as the slice above, never as the
whole suite. The unattended suite, the kit gate and the kit-epoch leg are owed at the close.
