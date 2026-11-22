**Serves:** journal TOOL-dWitnessedBar-30

# TOOL-dWitnessedBar-30 — builder return 1 (run `wf_01af1077-4ae`), committed 9487ac1f09ef156f784ed988746d6a45debf5cbc

## Why

TOOL-dWitnessedBar-30 is built as rev-4 says and committed in two commits, both with `Pass: TOOL-dWitnessedBar-30`. The pass commit is ceeac2dcfcf4dd40d53938b3f5fc38859481a80c and sets the spec status to CLOSED. The follow-up, 9487ac1f0, fixes two findings from the bug-class checklist. Before writing, I checked every symbol, blob pin, policy default, README heading and path in the spec's write set against the tree. All of them held, so there is no divergence to report.

## Summary

The unit is built and committed, but two parts were never run: the runner change and the live quiet-host re-run. No merge bar, gate leg, suite or runner ran in this pass. The only gate-side tool used was the naming lexicon's `--suggest`, on all 23 new function names, which it accepted.

**What changed**
- `tools/run-gates/verdict_flow.py`:
  - A selection row now has a fifth field, its mode (`hold` or `run`); a four-field row reads as `hold`, and `select --check` ignores the mode.
  - `select` reads the asks and the flake records at R in the one scratch worktree `read_asks_at` adds (it takes a new `then` reader). A quarantined leg gets mode `run` when its newest row since the hold is more than 24 hours old, or it has none.
  - A leg is released after `verdict.flakes.release` greens in a row, or when its manifest row changed since its ask was filed. Each release prints `release  <leg>  <ask id>  <reason>`.
  - `route` stamps `routed <epoch>` on a contended row, carrying a sibling record's stamp while that row still waits.
  - New verb `quiet-rerun` runs a blocking CONTENDED red once, alone, on a quiet host, or prints an `owner` line once the wait passes `flow.wait-ceiling`.
  - Four new fixtures: `held-run`, `daily`, `release`, `contended-pair`.
- `run-gates.sh`: reads the mode and runs a `run` leg past its guard, the docs mode and the reuse cache. Its result goes into `held.<n>` as `ok` or `fail`, never into `failed`, `ran` or the verdict.
- `profile_bar.py`: `check_quiet` gets a POSIX `ps` arm with the same liveness check.
- `unattended.sh`: adds `write_ask_closing` and `write_flake_releases`, called after the bar on every return code. `run_verdict_route` now runs `quiet-rerun` and files each `owner` line as a HIGH ask.
- Also updated:
  - the policy catalogue and its re-rendered pages: `help/reference/policy.md`, `unsummarised-keys.txt`
  - the run-gates README
  - the kickoff manifest's `last-audit` re-stamp
  - the generated views: symbol map, as-built view, build index
  - the acceptance ledger and deviation 301

**What was checked, and what it stands in for**
- All 16 `verdict_flow.py --fixture` cases exit 0. They stand in for the `run-gates evidence` and `unattended kit gate` legs for the Python logic. Mutation probes turned the new fixtures red when a red inside the streak was skipped, when `verdict.held` decided the mode, and when the wait had no ceiling.
- Stub-runner probes stand in for the `profile-bar selftest` leg for AC6's stub half.
- Probes of the runner's selection parse and of the driver functions, run as slices with their collaborators stubbed, stand in for the `run-gates canary` leg and the `unattended kit gate` leg for that logic.
- `backlog.py` parses the closing row byte-for-byte as `render_status_row` writes it.
- `bash -n` is clean on all four shell files.
- AC7 greps print 1 and 0; AC3's grep prints 4.

**Owed to the main loop at the close**
- `New arm:` `tools/run-gates/run-gates.test.sh` arm 3h3r (AC1: bar GREEN, the leg's `.leg` row written, `held.1` reads `quarantine · fail`). Floor 465 -> 468. Its run and RED-first observation are owed; a staged break is to drop the heldrun marker in the guard pass.
- `New arm:` `tools/run-gates/profile_bar.test.sh` arm 9p (AC6). Floor 40 -> 43. Its run and RED-first observation are owed; a staged break is to remove the own-pid liveness check in `check_quiet_posix`.
- AC6's live half needs a Linux node.
- `run_quiet_leg`'s real alone-run through `run-gates.sh` has only been probed with the runner call stubbed.
- Every leg in spec section 7.

**Bug-class checklist**
It ran over both commits. It flagged a real hang risk: the alone-run captured the runner's output through a pipe, so a leg outliving the kill could hold the wait open. The follow-up commit sends that output to the null device instead. It also flagged two refusals with no arm, so `release` and `contended-pair` gained cases for a bad `verdict.flakes.release` and a zero `flow.wait-ceiling`.

No probe hit its time bound. `help/reference/drive.md` and `help/reference/units.md` were already modified before this pass and were left unstaged; this pass added no content to them, since `git diff` shows nothing but line-ending warnings.

Key files:
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/verdict_flow.py
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-30-1-acceptance-ledger.md
- C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-30-deviation-301.md
