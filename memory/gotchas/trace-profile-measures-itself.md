---
name: trace-profile-measures-itself
description: a per-line set -x profile charges its own write overhead to the next line, so its seconds rank by call count and an optimisation aimed at them moves nothing
kind: class
---

# A `set -x` profile that ranks call count and calls it time

## Symptom

You profile a shell program by timestamping every traced line:

```bash
PS4='+ ${EPOCHREALTIME} ${LINENO} ' bash -x ./thing 2>trace.txt
```

then aggregate the delta between consecutive lines onto the earlier one. The result names two or
three hot lines with convincing precision. You optimise them. The wall clock does not move.

The tell is in the totals and it is easy to walk past: the traced run took **28.5 s** against an
untraced **11 s**. More than half of what the profile measured was the profiler.

## Where it bit

`tools/unattended/check-unattended.sh`, 2026-08-23. The trace attributed 4.33 s to two `grep` lines
inside a loop that ran 292 times, and 8.35 s to 34 `bash -c` calls. Acting on the first cut 231 grep
spawns out of 469, and five interleaved before/after readings showed no difference outside the noise.

The mechanism: `bash -x` writes one line to stderr **per command executed**, and that write completes
before the next timestamp is taken, so its cost lands on whichever line comes next. Overhead is
therefore proportional to how many times a line runs. A line executed 292 times collects 292 writes
worth of it. The profile was a call-count histogram in a time profile's clothes — and the two rank
differently whenever a cheap statement runs often and an expensive one runs rarely, which is the
normal shape of a loop.

Here the real answer was the opposite: 34 executions of one line were 5.02 s of a 10.74 s invocation
because each spawned a shell, while 292 executions of another were under a second.

## The fix

Timestamp REGIONS, not lines. Insert a handful of writes at boundaries you choose and let everything
between them be untouched:

```bash
printf 'MARK %s %s\n' "<tag>" "$EPOCHREALTIME" >&2
```

Eighteen of those cost nothing measurable and put the time where it actually was. Pick boundaries by
structure — one per check, one per phase, one per loop you suspect — and bisect from there.

`set -x` remains the right tool for COUNTING. The spawn tally taken from the same trace was exact and
load-independent, and it is what the eventual change was justified with. Use its counts, never its
seconds.

There is **no machine gate** for this class. Nothing in a tree can tell a correct profile from a
self-measuring one; the documented check is the one-line sanity test above — compare the traced run's
total against an untraced one, and distrust the seconds whenever tracing more than doubles it.
