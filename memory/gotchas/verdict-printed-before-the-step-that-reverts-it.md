---
name: verdict-printed-before-the-step-that-reverts-it
description: a verb prints a verdict about bytes it just wrote, and a later step of the same run can revert those bytes, so the operator reads a verdict about a tree the run did not leave
kind: class
---

# A verdict printed before the step that can revert its bytes

## Symptom

A run prints a clean verdict about a file — a hole discharged, a check passed, a row re-measured —
and then, further down the same output, rolls that file back. Nothing after the rollback restates
the verdict, so the operator acts on the earlier line, which describes bytes the tree no longer holds.

## Where it bit

`tools/govkit/govkit.py`, `govkit update`, build dRemeasuredRender, 2026-10-11. The
`DEPL-dRemeasuredRender-2` hole re-probe printed `is discharged after the render; the early verdict
does not stand` inside the per-kit regenerate loop. The verify pass runs after that loop, and a kit
whose `[check]` goes green to red is rolled back there, its rendered files restored from the
pre-render snapshot. The closing diff review (round 1, ids 1, 5 and 11) found it; the same build's
`DEPL-dRemeasuredRender-1` had already placed its receipt re-measure after the verify pass for exactly
this reason, so the two units answered one question two ways.

## Why

A long verb has a natural place to print each fact — next to the code that computes it — and a later
step that can undo the work is easy to forget at that place. The verdict is true when printed and
false when the run ends.

## The fix

Print a verdict about written bytes only once every step that can revert them has run, beside the
other facts that wait for the same point. `DEPL-dRemeasuredRender-4` moved the re-probe to sit beside
the re-measure step, after the verify pass, and its line names a rollback when there was one.

## Gate

Gated by `tools/govkit/selftest.py`, arm `[dRR-4 AC1]`: a fixture kit whose render discharges its
hole and whose `[check]` then goes green to red must report the hole undischarged over the restored
bytes. Staged RED against the code as it stood at `bac1a4fb`, which printed the discharged line before
the rollback. No gate finds the class in general: a structural arm over every line `update` prints
about a rendered file was proposed by the review and left to its own unit.
