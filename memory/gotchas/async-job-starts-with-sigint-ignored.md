---
name: async-job-starts-with-sigint-ignored
description: a job a non-interactive shell starts with `&` has SIGINT ignored, bash cannot trap a signal it started with ignored, so an INT sent to it, or to anything it starts, is silently dropped
kind: class
universal: false
---

# An async job cannot trap INT

## Symptom

A test script starts a process with `&` and sends it INT to check its INT trap, and the process
ignores it and runs to its normal end, so the trap reads as missing when it is fine. Turning job
control on with `set -m` before the launch makes the arm pass when the script is run directly, and
the same arm fails again once the script runs as a leg of the merge bar.

## Cause

With job control off, bash starts every `&` job with SIGINT and SIGQUIT ignored. An ignored disposition
survives `fork` and `exec`, and bash refuses to trap or reset a signal that was ignored when it
started. The merge bar dispatches each leg as an `&` job, so a suite running as a leg starts with
SIGINT ignored, and so does everything that suite starts in turn, with or without `&`.

Measured on node `d`, 2026-09-13, in the shape of the runner's own traps. A child started with `&` from
a script ignored INT and ran on; the same child under `set -m` trapped it and exited 130; and with the
outer script itself launched as an `&` job, `set -m` no longer helped and INT was dropped again.

## Where it bit

While building `tools/run-gates/run-gates.runlog.test.sh`, whose arm AC3 sends INT to a running bar.
The first launch design used `set -m`, which a direct probe passed, and the probe then dropped INT once
it was itself started as an `&` job, which is how the bar starts every leg.

## The fix

Launch the process under test through `timeout --foreground <bound>`. `timeout` installs its own INT
handler whatever it inherited, and a handled signal resets to the default across `exec`, so its child
can trap INT; the bound also stops a trap that never fires from hanging the suite. Send the signal to
the child's own pid, not to `timeout`'s, or the arm grades timeout's forwarding instead of the trap.

## Gate

Gated by `tools/run-gates/run-gates.runlog.test.sh`, arm AC3. Its launch is itself an `&` job, so the
runner it starts would inherit SIGINT ignored in a direct run as well as under the bar, and the arm
was staged RED on a mirror by removing `timeout --foreground` from that launch.
