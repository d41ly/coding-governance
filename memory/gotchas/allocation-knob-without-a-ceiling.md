---
name: allocation-knob-without-a-ceiling
description: a knob that sizes an allocation or a loop, validated only as a positive integer, hangs the process on a mistyped value before anything it guards runs
kind: class
universal: false
---

# One more digit was a hang

## Symptom

A configuration value counts how many of something to build, and is checked only for being a positive
integer of bounded length. A mistyped value of many digits builds that many before any timeout, wall
or fail-open bound starts, so the process hangs where nothing reports it.

## The instance

The `slots` knob of `tools/run-gates/gate-profiles.txt`, and `GATE_TURNSTILE_SLOTS` over it, sized the
slot path array in `tools/run-gates/run-gates.sh` with no upper bound, beside a `GATE_JOBS` clamped at
64 (aPairedSlots closing review, M9).

## The remedy

A knob that sizes an allocation declares a maximum beside its minimum: refused in the table, ignored
with a NOTE in an override, and armed one above it.

## Gating

Gated by `tools/run-gates/run-gates.test.sh` section 11s, for `slots` only.
