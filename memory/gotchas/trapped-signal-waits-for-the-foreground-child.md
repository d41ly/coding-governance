---
name: trapped-signal-waits-for-the-foreground-child
description: a bash script that TRAPS TERM, HUP or INT runs the handler only after its foreground child returns, so a killed script outlives the kill for as long as that child runs
kind: class
universal: false
---

# Trapping a signal delays it

## Symptom

A script gains `trap '…' TERM` so it can record that it was killed. From then on, killing it does
not end it: it runs until the command it was waiting on finishes, and only then runs the handler.

## Cause

Bash runs a trapped signal's handler BETWEEN commands. While it waits on a foreground child it notes
the signal and defers the handler until that wait returns. An UNTRAPPED fatal signal takes its
default action at once, and bash still runs the EXIT trap on the way out.

Measured on node `d`, 2026-09-13. TERM ended an untrapped script running `sleep 4` in 0.33 s, and the
same script with `trap 'exit 143' TERM` in 4.05 s. An untrapped script waiting on a 20 s child exited
within 0.2 s of TERM, and its EXIT trap ran with `$?` reading 0.

## Where it bit

At spec time, before it could ship. `tools/unattended/unattended.sh` runs the merge bar in the
foreground under `GATE_BOUND`, 3600 s by default, inside `--close`. A TERM trap added to record
killed calls would have held a killed close for up to an hour.

## The fix

Trap EXIT and nothing else. Mark every exit the script CHOOSES, the way the driver sets
`RUNLOG_CLEAN=1` immediately before each one, and let the EXIT trap read the mark: present is a
chosen exit, absent is a signal. KILL runs no trap at all, so a start record with no end record is
that case's signature. The price is that under a signal the EXIT trap's `$?` is whatever the last
command left, often 0, so the record's `exit=` field says how the process ended and `rc` does not.

**NOT FOR A GIT HOOK, OR ANYTHING ELSE GIT RUNS ON WINDOWS** (2026-10-11, `TOOL-aSignalledHook-1`).
There a process that dies by an untrapped signal is read as exit 0, so following this fix in
`.githooks/pre-push` let a TERM land a push with no bar. Trap the signal there, and run the long
child in the background and `wait` on it so the trap is not delayed:
`signal-killed-hook-reads-as-success.md`.

## Gate

Gated by `tools/unattended/runlog-writer.test.sh`, arm AC3: TERM sent while `--close` waits on a 20 s
stub must end the driver while the stub is still alive. The arm was staged RED by adding
`trap 'exit 143' TERM` to the driver.
