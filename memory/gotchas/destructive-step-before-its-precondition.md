---
name: destructive-step-before-its-precondition
description: a destructive step ordered before the probe for the precondition that makes it useful runs on exactly the case where nothing can follow it, so the harm lands and the benefit never does
kind: class
universal: false
---

# Kill first, then ask whether you could have resumed

## Symptom

A procedure has a destructive step — a tree kill, a file removal, a lease takeover — and a step after
it that is the whole reason for the destruction: a relaunch, a rewrite, a re-lease. The second step
has a precondition the first does not: a logged-in CLI, a reachable remote, a writable dir. The
precondition is probed, correctly, and its failure is announced, correctly — AFTER the destructive
step has run. On the failing case the procedure destroys and then prints that it cannot rebuild.

Every arm passes. The kill arm sees the kill. The logged-out arm sees the SKIP line. Nothing asserts
that the target of the kill is still alive when the SKIP prints, because the two arms were written
one per row of the decision table and the defect is in the ORDER of the rows.

## The instance

`tools/unattended/resume-tick.sh` at spec rev-1 of `TOOL-aWokenSentinel-5`: the table put `STALE ·
pid-alive yes → kill the tree` above `STALE · not logged in → SKIP`. On a node whose CLI is logged out
the tick's first act was `taskkill //PID <pid> //T //F` on the recorded session's tree and its second
was to print that nothing can resume the run. A killed session with no resumer, and on the
false-`STALE` case a healthy one — the spec-audit's H4, promoted to `TOOL-aWokenSentinel-12`.

## The remedy

Order the precondition's probe FIRST, before anything irreversible, so a probe that decides whether
the rest can happen is the first thing the row costs. Then make the arm observe the precondition
FAILING with the destructive target STILL ALIVE: start a live process, record its pid as the target,
run the procedure with the precondition stubbed to fail, and assert the process is listed afterwards.
An arm that only asserts the announced skip is satisfied by the swapped order.

## Where this repo's killers live

The catalogue anchors by PATH and cannot read a verb, so this record names the files where an
out-of-process kill is written and `--for-diff` selects it for a diff touching one:

- `tools/unattended/resume-tick.sh` — `run_kill_tree`, the tick's `taskkill //T` on the recorded pid,
  ordered after `check_login`.
- `tools/process-monitor/reap.py` — `run_kill`, the per-row reaper over a derived scope.
- `tools/unattended/unattended.sh` — `run_bounded`, whose `timeout -k` kills the bounded child.

A kill written in a file this list does not name is not selected; add the path here when one lands.

## Gating

Gated by `tools/unattended/resume-tick.test.sh`, the `U12` arm: a background `sleep` recorded as the
run's pid, the stub CLI answering logged-out, the tick asserted to print the SKIP line with the sleep
still listed by `tasklist` (`kill -0` elsewhere), `auth status` logged and no `-p`, no sidecar log.
Observed RED against a tick copy with the login call and the kill call swapped. The class itself is
gated for the tick alone; the reaper and the driver's bound carry no precondition-ordering arm, and
the anchors above are what puts this record in front of the diff that would add one.
