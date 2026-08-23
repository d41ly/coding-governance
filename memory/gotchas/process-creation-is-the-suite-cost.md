---
name: process-creation-is-the-suite-cost
description: a shell suite that is 93% not-CPU is paying an on-access antivirus scanner per exec, so its cost is spawn count and nothing in the code reads that way
kind: class
---

# A shell suite whose cost is process creation, not work

## Symptom

A test suite over a microscopic repo takes tens of minutes and every explanation for it is wrong.
The code looks cheap — greps over files of a few thousand lines — and reading it suggests seconds.
Sharding it helps exactly in proportion to how the arms split, which is the signature of a cost that
is per-arm and constant rather than per-byte.

The one measurement that settles it takes five seconds:

```bash
time bash the-suite-or-one-invocation-of-it
```

`real 14.4s  user 0.33s  sys 0.62s` — under a second of CPU in a fourteen-second run. Nothing in the
program is computing. It is waiting, and what it waits on is `exec`.

## Where it bit

`tools/unattended/check-unattended.sh`, measured on node `d` 2026-08-23 inside its own fixture. 469
external process spawns per invocation, 243 invocations in the suite, so about 114,000 process
creations for one run of one suite. Per-spawn cost on that node, measured directly with a
100-iteration loop: **0.019-0.039 s for a binary, 0.032 s for `bash -c`, 0.010 s for a fork with no
exec**. On a machine with no on-access scanner the same numbers are around a millisecond.

469 × 0.022 s = 10.3 s against a 10.7 s measured invocation. The model reproduces the reading exactly,
which is how you know it is the cost and not a coincidence.

The scanner was visible the whole time and nobody looked:

```powershell
Get-Process | Sort-Object CPU -Descending | Select-Object -First 8 Name, CPU, WS
```

`ekrn` — ESET's scanning service — top of the list at 4529 s of CPU, machine at 80% load.

## The fix

Count spawns, then remove them. An execution trace counts them reliably even when its SECONDS are
worthless:

```bash
PS4='+ ${EPOCHREALTIME} ${LINENO} ' bash -x ./thing 2>trace.txt
```

The shapes that produce them in bulk are loops that run a command per (item, file) pair when the file
half does not depend on the item: hoist the per-file read out, match the item half in the shell. Same
for a `bash -c` per specimen — feed one shell the whole specimen set. Here that took 469 to 220 with
no predicate changed.

Two things this class demands of anyone acting on it:

- **Wall clock on an AV-fronted machine is not measurable to better than a factor of two.** Readings
  of the same workload varied 10.7 s to 26 s across one session. Interleave old and new, take the
  minimum, and prefer a DETERMINISTIC proxy — the spawn count — for the claim you actually write down.
- **A declared time ceiling on such a suite must have headroom for someone else's scan**, or it reds
  on ambient load and gets ignored, which is worse than not having one. Write the derivation beside
  the number so a later reader can see which part is the code's and which is the machine's.

There is **no machine gate** for this class and there cannot be a portable one: the cost is a property
of the machine the suite runs on, not of the tree. What replaces it is a documented check — a declared
wall-clock ceiling per suite, enforced by `tools/unattended/run-unattended-gates.sh`, which reds when a
suite goes over and reds when a suite arrives without a ceiling at all.
