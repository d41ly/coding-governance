# TOOL-aSignalledHook-1 — a signal-killed pre-push hook refuses the push, and a success with no hook verdict is caught by the lander

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 1 · advances TOOL-aSurfacedLexicon-25

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aSignalledHook-1-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aSignalledHook-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aSignalledHook-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aSignalledHook-1-brief.md) | research | — |
| [2026-10-11-review-TOOL-aSignalledHook-1-closing-diff-round1.md](../reviews/2026-10-11-review-TOOL-aSignalledHook-1-closing-diff-round1.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

On Git for Windows a pre-push hook that DIES BY A SIGNAL is read by git as success, so the push lands
with no bar: measured on node `a` (git 2.54.0.windows.1, MSYS bash 5.3.9) for TERM, HUP, INT and KILL
sent to the hook, and for a Windows TerminateProcess of the hook's bash. The landing of 69e0ff0f on
2026-10-11 01:33:35 +0300 is that class: the hook's run-log END reads `rc=0 exit=unclean
decision=full` at 01:33:30 while its bar was still queued in the turnstile. Make every catchable
signal end the hook with an ordinary non-zero exit that refuses the push, and make the uncatchable
remainder (KILL, TerminateProcess) visible to the lander instead of reading as a gated landing. The
unexplained no-bar push of `TOOL-aSurfacedLexicon-25` shows the same transcript shape, a queued bar and
then the remote contacted, at a date with no run log to confirm the cause; this unit advances it.

## 2. Scope (IN)

- **S1** — `.githooks/pre-push` traps HUP, INT, QUIT, PIPE and TERM from its first executable line.
  The handler ignores further signals, sends TERM to the bar when one is running, writes the refusal
  token `signalled` (run-log decision `refuse-signal`) and exits `128+n` through an ordinary `exit`.
  AC1, AC5, AC6.
- **S2** — the bar runs as a child the hook WAITS on (`$gate </dev/null &` then `wait`) instead of in
  the foreground, so a trapped signal is handled at once rather than after the bar returns, and the
  hook's exit is still the bar's status. AC1, AC2, AC7.
- **S3** — the hook clears an allow record `pre-push-allow` in its git dir on every run, and writes
  `<pushed sha><TAB><gate run id>` there at its success exit on a default-branch push and at its
  `covered` exit, which allows a push whose tree already carries a green, never on any other exit.
  AC3, AC4, AC9.
- **S4** — `tools/push-main.sh` clears that record before every push on both the attended path and
  `--land`. On a git exit of 0 it requires a record naming the pushed sha, captured before the push;
  without one it prints a `landed UNGATED` line naming the hook, writes no lander marker and exits 4.
  When the remote already held the pushed sha before the push, nothing was pushed and no record is
  owed, and it says so. A `signalled` refusal is reported as such. AC3, AC4, AC8.
- **S5** — the run-log suite's TERM arm and its exit-site table move to the new behaviour: TERM while
  the bar runs ends the hook promptly, clean, as `refuse-signal`, with the bar stopped. AC5.
- **S6** — the hook header's "NO SIGNAL TRAP, ON PURPOSE" paragraph is replaced by what is true now,
  and its WHAT THIS DOES NOT CATCH names KILL and TerminateProcess and where they are caught instead.
  NOT OBSERVED — comment prose, which no arm reads.
- **S7** — the class is recorded under `memory/gotchas/`. NOT OBSERVED — a record, which no arm reads.

## 3. Non-goals (OUT)

- Preventing a landing after a KILL or a TerminateProcess of the hook. No process can trap either,
  and git reads the result; S4 makes it loud after the fact, it cannot unpush.
- Any change to `tools/run-gates/run-gates.sh`. A fork that fails with EAGAIN exits bash 254 once its
  retries are spent (measured), which the hook already refuses; a failed fork inside a command
  substitution in the turnstile loop leaves the bar waiting. Neither is a fail-open.
- Reverting or re-gating 69e0ff0f; that is a landing decision, not this unit's.
- The branch bar (`GOV_BRANCH_GATE_CMD`) keeps running in the foreground; a non-default push lands
  no default branch.

### Edges

- **hands-off** external — reverting or re-gating the ungated landing 69e0ff0f is the owner's call.

## 4. Design

**Why git reads a signal death as success.** MSYS records a signal death as wait status `n` and, for a
process whose parent is native, byte-swaps it into the Windows exit code `n << 8`. Git for Windows
reads `GetExitCodeProcess` and takes `WEXITSTATUS(x) = x & 0xff`, which is 0. The hook's bash is the
exec'd child of an `env.exe` stub that git waits on; a tree kill of git's parent does not reach the
hook's bash, whose Windows parent is gone, which is why an orphaned hook can outlive its push.

**The handler** (`write_signal_refusal <name> <status>`), installed by five `trap` lines at the top
of the hook. It runs `trap '' HUP INT QUIT PIPE TERM` first, so a second signal or a write to a dead
pipe cannot re-enter it. It then sends TERM to `PP_BAR_PID` when that is set: the runner's own TERM
trap reaps its legs and drops its turnstile ticket. Then it writes the `signalled` refusal through
`write_refusal` when that function is defined, sets the clean-exit mark, and runs `exit "$2"`. Below
the EXIT trap the END line then reads `exit=clean decision=refuse-signal rc=<128+n>`. Above it, a
signal writes one `once` line, as the earlier refusals do.

**The waited child.** `$gate </dev/null &` sets `PP_BAR_PID=$!`, and `wait "$PP_BAR_PID"` sets `rc`.
A trapped signal interrupts `wait` immediately, which a foreground child does not allow. stdin was
already `/dev/null`. A non-interactive shell starts an async child with INT and QUIT ignored, so the
runner can no longer trap INT; the hook forwards TERM instead, which the runner does trap.

**The allow record.** `$gd/pre-push-allow`, beside `pre-push-refusal` and `pre-push-bar`, cleared at
the same site those are cleared. It is written only immediately before the final `exit "$rc"` when
`rc` is 0 and a default-branch ref was pushed, so a skip, a refusal or a signal never leaves one.
push-main reads it after `git push` returns 0. A record naming another sha is treated as absent.

**What the incident's evidence does and does not say.** A hook bash under Git for Windows always shows
`ppid 1`, because its parent is the native `env.exe` stub, so "reparented to pid 1" is not evidence of
anything. The run log says the incident hook ran its EXIT trap at 01:33:30, which bash does on an
untrapped fatal signal just before it dies. The fork failure in the same log (0xC0000142, then one
`fork: retry`) is consistent with the session's console being torn down, and it did not cause the
landing: bash spends 15 s on four retries before it exits 254, and the push came before a second retry was printed.

### Rollout

The lander and the hook ship in one kit entry (`push-main`) and land in one commit. A lander running
beside an OLDER hook reads every landing as `landed UNGATED`, which fails closed and names its cause.
Under this repo's relative `core.hooksPath` each tree runs its own copy, so the pair moves together.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/pre-push.runlog.test.sh`
- `tools/push-main.sh`
- `tools/push-main.test.sh`

### Alternatives rejected

- A wrapper hook that runs the real body as a child and maps its signal death to `exit 1`. The
  wrapper is itself a process that can be killed, so it moves the hole rather than closing it.
- Waiting for the bar to exit inside the handler. A wedged bar would then hold the refused push open,
  which is the defect the old header comment was avoiding.

## 5. Production-readiness checklist

- security — this is the security fix: a merge bar that failed open. The allow record is a file in
  the pusher's own git dir, as the refusal and bar files already are, so it carries no new trust.
- perf / scale — N/A — one extra `printf` per gated push; the bar's cost is unchanged.
- error / empty / loading states — a signal before the run log exists still refuses, with no END.
- observability — the `signalled` refusal, the `refuse-signal` decision on END and the lander's
  `landed UNGATED` line are the three new signals.
- risks — backgrounding the bar changes its INT disposition; the TERM forward covers it (S2).
- testing — new arms in `pre-push.test.sh` and `push-main.test.sh`, and the run-log AC3 arm moved.
- migration — N/A — no data; the first push after the change writes the record.
- user docs — N/A — no `help/` tree; the hook header and the gotcha carry it.

## 6. Acceptance criteria

- **AC1** — When a default-branch `git push` is in flight on a fixture whose stub runner sleeps and
  the hook's bash is sent `TERM`, and separately `HUP`, the push is refused: git exits non-zero, the
  remote ref is unchanged, `pre-push-refusal` reads `signalled`, and the stub runner is no longer
  running. Red when: the hook dies by the signal, git exits 0 and the remote ref moves, as measured
  before this unit.
- **AC2** — When the signal of AC1 is sent, the hook has exited before the stub runner's `sleep`
  would have ended. Red when: the trap is deferred behind a foreground bar until it returns.
- **AC3** — When `push-main.sh` pushes through a hook that exits 0 without writing `pre-push-allow`
  (the observable a KILLed hook leaves on Git for Windows), it prints `landed UNGATED`, exits 4 and
  writes no lander marker, on the attended path and on `--land`. Red when: it accepts git's exit 0
  alone and prints `landed`, on either path.
  fixture: a substitute hook, so the arm runs on any platform; a real KILL reads as success only on
  Git for Windows.
- **AC4** — When a green push lands through the real hook, `pre-push-allow` names the pushed HEAD and
  `push-main.sh` prints `landed` and writes the lander marker. Red when: the record is missing or
  names another sha and a gated landing is refused.
- **AC5** — When the run-log suite's TERM arm signals the hook while its bar runs, END reads
  `exit=clean`, `decision=refuse-signal` and `rc=143`, the bar is stopped, and the exit-site table
  carries the handler's `exit`. Red when: END reads `exit=unclean` or the table misses the site.
- **AC6** — When the hook is sent `TERM` before it reaches the bar, the push is still refused with
  `signalled`. Red when: an early signal exits through bash's default disposition.
- **AC7** — When the stub runner exits `254`, the status bash returns once its fork retries are spent,
  the push is refused. Red when: a non-zero bar status other than 1 reads as a pass.
- **AC8** — When `push-main.sh` is re-run with the remote already at HEAD, it says nothing was pushed
  and exits 0. Red when: a push of nothing, which leaves no `pre-push-allow`, is reported
  `landed UNGATED`.
- **AC9** — When a push is `covered` by a recorded green and runs no bar, the hook still writes
  `pre-push-allow` naming the pushed commit. Red when: the covered exit writes none and every covered
  landing reads UNGATED.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `push-main self-test`

New arm: .githooks/pre-push.test.sh · covers AC1 AC2 AC6 AC7 AC9 · a stub runner that sleeps, signalled mid-push; a runner exiting 254; a covered push in the BG block · none
New arm: tools/push-main.test.sh · covers AC3 AC4 AC8 · a substitute hook exiting 0 with no allow record, on both paths; the real hook as control; a re-run with nothing to push · none
New arm: .githooks/pre-push.runlog.test.sh · covers AC5 · the existing TERM arm, its assertions inverted · none

## 8. Open questions

- **F1 — Should push-main also detect a success with no hook verdict?** Recommendation: yes; a
  KILLed hook cannot be stopped in-process, and the lander marker is what an unattended run trusts.
  RESOLVED (owner, 2026-10-11): yes, in this unit.

## 9. Revision log

- rev-1 · 2026-10-11 · first draft.
- rev-2 · 2026-10-11 · S3 S4 AC3 AC8 AC9 §7 · closing review round 1: the covered exit writes the
  allow record, a push of nothing is not UNGATED, the pushed sha is captured before the push, and the
  `--land` path gets its own arm.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` cannot see shell seams; the seams this extends are the hook's
existing refusal channel (`write_refusal`, `pre-push-refusal`) and the lander's verdict-file pair
(`pre-push-bar` read by `write_lander_marker`). The allow record is a third file of that pair's kind,
so no new channel is invented.

Recall terms used: pre-push hook, signal, TERM trap, exit=unclean, run log END, lander marker,
pre-push-refusal, pre-push-bar, fail open, Git for Windows, push-main, turnstile queue
