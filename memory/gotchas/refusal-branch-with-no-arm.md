---
name: refusal-branch-with-no-arm
description: a coded refusal or decline branch has no suite arm that reaches it, so the branch can be collapsed with every arm green
kind: class
universal: false
---

# A refusal branch with no arm

## Symptom

A function chooses among several decline lines, first match wins: "the tree moved", "no record", "the
record cannot be replayed", then the success path. The suite arms the first two and the success path.
The third runs in production and prints its own line, but no arm reaches it, so it can be collapsed into
its neighbour, or its line lost, with every arm green. The same holds for a verdict with several reasons:
the first reasons a fixture is easy to stage get arms, and the ones that need a dead probe do not.

This differs from a rule stated in prose with no check: the branch here is CODE, it runs, and only its
arm is missing. The tell to hand a reviewer: **list each distinct refusal or decline line the function
can print, and grep the suite for each one.** A line no arm asserts is a branch no arm reaches.

## Where it bit

The closing diff review of build `aLightenedLoop`, round 1, items L1 and M6
(`memory/builds/aLightenedLoop/reviews/2026-11-14-review-TOOL-aLightenedLoop-1-5-implementation-diff-round1.md`).
`run_spec_token_check` in `tools/unattended/unattended.sh` had three not-recorded lines and the driver
suite `tools/unattended/unattended.test.sh` asserted two. `print_wake` had FULL reasons for an absent,
LANDING or terminal phase, a dead clock probe and a dead task probe, none of them armed.

## The fix

One arm per distinct refusal or decline line, seen red with only that branch deleted.
`TOOL-aLightenedLoop-6` adds a stub whose input record holds a line no replay can repeat, three phase
arms, and two `--wake` arms with a stub `date` first on `PATH` for one call each, so no later arm
inherits it.

Gated: no machine gate yet. The review's M6 and L1 left-shift would extend the
`harness arms (fail branches armed or pinned)` leg to these lines; until it does, the class is a
reviewer's question.

## What this does NOT say

It does not say a branch that cannot be staged needs an arm. A branch no fixture can reach is PINNED
with its reason, as the driver pins its resolver's failure, and an arm that could never be seen red is
no arm.
