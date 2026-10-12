---
name: a-runner-knob-owes-a-push-class
description: a new GATE_ or GOV_ knob the gate runner reads has no push-boundary class until it joins one, and the arm that says so is guarded away from the unit that adds it
kind: class
universal: false
---

# A runner knob owes the push boundary a class

## Symptom

A unit adds an environment knob to `tools/run-gates/run-gates.sh`, every leg its bar runs is green,
and the next unit that touches `.githooks/` inherits a red from the pre-push suite's H49 arm:
`unclassified-or-twice <KNOB> (0)`. Meanwhile nothing has decided whether a caller's
`<KNOB>=… git push` may change what the push bar checks.

## Cause

`.githooks/pre-push` sorts every `GATE_` and `GOV_` name the runner reads into three classes: the
knobs it drops before the bar, the knobs it scrubs from every non-STUB bar, and the knobs the suite
declares inert. The H49 arm in `.githooks/pre-push.test.sh` greps the runner for every such name and
reds on one in no class. That arm lives in the pre-push self-test, whose leg is guarded on
`.githooks/` and the lib directory, so a unit touching only the runner never runs it.

## Where it bit

TOOL-aPrimedIndex-3 added `GATE_REGEN_CHECK`, the switch that skips the bar's generated-output
preflight. The closing review of build `aPrimedIndex` found it in no class, replayed the arm's
check read-only, and promoted the fix (TOOL-aPrimedIndex-6). The knob is scrubbed rather than inert,
because a skipped preflight can let a guard-scoped stale output through a bar that would otherwise
refuse it.

## The fix

Classify the knob in the same unit that adds it. Ask the question the classes encode: may a caller
of the push change what the bar checks with this knob? If yes, it is inert and goes in the suite's
list with its reason; if no, the hook scrubs it.

## Gating

Gated by the H49 arm of the pre-push self-test, and its guard is why the verdict arrives late. No
machine gate reaches the unit that adds the knob; this record is that left-shift, selected for any
diff touching the runner.
