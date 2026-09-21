---
name: guard-fed-the-value-it-supersedes
description: a guard on a relaunch reads only the pid the launch it guards was meant to replace, so the process the launch itself created is invisible to the next launch and the guard never sees the duplicate it exists to stop
kind: class
universal: false
---

# The guard reads the old pid; the launch made a new one

## Symptom

A procedure replaces a process: it reads a recorded pid, kills its tree if alive, and launches a
successor. The kill and the "is it alive" probe are correct, and every arm that seeds a recorded pid
passes. But the successor's pid is written nowhere the next run of the procedure reads — the record
still names the OLD pid, which the successor was supposed to overwrite and did not — so the next run
reads `pid-alive: no`, kills nothing, and launches a second successor beside the first. The guard
was fed only the value the act it guards was meant to supersede.

## The instance

`tools/unattended/resume-tick.sh` at spec rev-4 of `TOOL-aWokenSentinel-5`: the tick killed the
RECORDED pid's tree and launched `claude -p --resume`, and the record's `pid:` changes only when the
resumed session itself runs `--resume --keepalive-id`. A resumed session that hung before doing so,
or ignored the payload's first instruction — recorded fleet behaviour — left the lease naming the
dead pid; the next `STALE` tick read `pid-alive: no`, killed nothing, and launched a second
skip-permissions agent into the same tree, a third the tick after. The `NO IN-FLIGHT GUARD` header
reasoned only about a launch that produced no turn (closing review id 3).

## The remedy

Record what the act produced where the next run of the procedure reads: the tick writes
`launched <pid>` onto the attempt line it already parses, and the next tick reads it back — alive
with the tree unmoved since the launch is IN-FLIGHT and skips; alive with the tree moved since is a
hung successor and joins the kill. The arm observes the second run, not the first: a launch, then a
second `STALE` run with the launched pid alive, asserting the skip line and ONE attempt line; and a
seeded line older than the last move whose launched pid is a live `sleep`, asserting the sleep gone
and attempt 2 launched.

## Gating

Gated by `tools/unattended/resume-tick.test.sh`, the `AC13` arms: the in-flight half inside the AC1
block (a second STALE tick after a launch prints `skip · IN-FLIGHT · launched <pid>` and writes no
line), and the hung half (a seeded old line with the suite's own `sleep` as the launched pid; the
sleep is gone from `tasklist` afterwards and attempt 2 launches). Observed RED against a tick copy
with the in-flight branch removed (attempt 2 launched, two lines) and one with the launched-pid kill
removed (the sleep survived). The class is gated for the tick alone; the anchors above put this
record in front of a diff that adds a second relauncher.
