---
name: overlap-judged-from-the-invocation-interval
description: a guard that two jobs ran at once, timed around the commands that started them, includes their queue wait, so a pair the scheduler serialized still overlaps
kind: class
universal: false
---

# They were started together, not run together

## Symptom

A check proves two jobs overlapped by comparing timestamps taken before and after each command. The
commands start at once, so the windows overlap even when the system under test made the second wait
for the first, and the check certifies a concurrency nobody observed.

## The instance

`memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh` stamped the
clock around `tools/run-gates/run-gates.sh`, whose turnstile queue wait sits inside each window. The
closing review of aPairedSlots found it (its H4).

## The remedy

Read the admitted interval from the system under test: what it granted, and when. For the turnstile
that is each run record's `slot` and `acquired` against the other record's `ended`; distinct slots 1
and 2 arise only from two holders at once.

## Gating

No machine gate for the class. The two-bar check reads the run records since TOOL-aPairedSlots-14.
