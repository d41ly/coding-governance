---
name: signal-trap-runs-the-exit-handler-twice
description: a signal trap that calls the exit handler and then exits runs that handler twice, because the exit fires the EXIT trap too, so anything the handler appends is appended twice
kind: class
universal: false
---

# A signal trap that exits runs the exit handler twice

## Symptom

A script traps EXIT with a handler, and traps TERM, INT and HUP with `handler; exit 143` so that a
signal still ends it with the conventional status. Everything idempotent in the handler looks fine.
The first step in it that is NOT idempotent, such as appending a line to a log, happens twice on every
caught signal and once on every other exit.

## Cause

The signal trap runs the handler and then calls `exit`, and that `exit` fires the EXIT trap, which
runs the handler again. In the first entry `$?` is whatever the trap found: 128+n when the signal
interrupted `wait`, but the command's own status, often 0, when the signal was held behind a
foreground command until it ended. In the second entry it is the status the `exit` was given.

Measured on node `d`, 2026-09-13, with a probe in the runner's own trap shape. Each of TERM, INT and
HUP entered the handler twice, and an append guarded by a flag wrote exactly one record for each. A
TERM sent during `x=$(sleep 3)` ran the trap three seconds later with `$?` at 0.

## Where it bit

At spec time, before it shipped. `tools/run-gates/run-gates.sh` installs `trap cleanup EXIT` beside
`trap 'cleanup; exit 143' TERM` and its INT and HUP siblings, and `cleanup` had been kept idempotent
for this reason, since the EXIT trap fires after the signal traps and must not undo a release. The
round-1 audit of `TOOL-dLoggedFlight-3` found that a run-log append added to `cleanup` would write two
lines for every killed bar.

## The fix

Guard the non-idempotent step with a flag set on its first entry, and carry the signal's status into
that entry explicitly: `trap 'RUNLOG_RC=143; cleanup; exit 143' TERM`, with the step reading
`RUNLOG_RC` before `$?`. Reducing the signal trap to a bare `exit 143` would also run the handler once,
and the unit's spec rejected it because it changes when the handler's existing work runs relative to
the signal.

## Gate

Gated by `tools/run-gates/run-gates.runlog.test.sh`, arm AC3: TERM, INT and HUP each sent to a running
bar must leave exactly one line, reading `verdict=NONE` with 143, 130 and 129, and a TERM held behind
a stubbed `$(fingerprint)` must still read 143. The arm was staged RED on a mirror by removing the
guard, which wrote two lines, and by dropping `RUNLOG_RC`, which the three `wait -n` bars did not
notice and the held one wrote as a status of 0.
