---
name: inherited-env-retargets-a-check
description: a check started under a runner that exports a file override grades the override and not the declaration it certifies, and its green line names neither
kind: class
universal: false
---

# An inherited environment variable retargets a check

## Symptom

A check reads its subject through an environment override, a manifest path say, and falls back to
the file beside its kit. A runner exports that override to every child for its own reason, a
filtered or derived copy of the file. A check declared in a descriptor and started by that runner
inherits the variable and grades the derived copy. Its line reads fresh, the declaration was never
opened, and nothing in the output says which file was graded.

## Where it bit

aNimbleMend's `tools/run-gates/kit.toml` staged `pass_legs.py --check` as a `[[regenerate]]` row,
and `tools/run-gates/regen.py` passes the environment through. The pass-leg adapter starts the bar
runner with `GATE_LEGS` naming its filtered list, so a pass run's freshness preflight graded that
list: a row lacking its field was invisible there, and a field typed on a row the filter drops read
as clean. An earlier unit had put every pass leg behind the shim that unsets the variable and left
the preflight out. The closing review's round 1 found it as M6
(`memory/builds/aNimbleMend/reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md`).

## The fix

A check that a runner with a manifest override can start states which file it grades, and starts
with the override unset. `TOOL-aNimbleMend-15` runs both halves of the row behind the leg shim,
`run-held-wsl.sh --leg`, so the check grades the manifest beside the kit under any runner.

Gated by arm 14i of `tools/run-gates/run-gates.test.sh`: a pass-leg run through the preflight, where
a `pass_leg` typed on a row the filtered list drops must refuse the run, and does not once the shim
is taken out of the fixture's descriptor. For another descriptor row or another override, this
record is the checklist entry: list the variables the runner exports, and ask of each check it
starts whether one of them moves its subject.
