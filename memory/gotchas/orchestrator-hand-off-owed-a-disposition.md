---
name: orchestrator-hand-off-owed-a-disposition
description: a spec that hands a discovery to "this run's orchestrator" names a recipient the run tracks nowhere, so the discovery is dropped silently unless the close checks every such line resolves to a unit or a parked row
kind: class
---

# A hand-off to the orchestrator is owed a disposition the close can see

## Symptom

A unit's builder finds something outside its unit: a class gate the instance it fixed belongs to, a
second defect of the same shape. It cannot mint a unit, so its spec hands the discovery off, in a
line addressed to "this run's orchestrator", which "adopts it as a unit or parks it". The unit
closes. Nothing the run keeps lists that line: the roster holds units, the run-state file `RUN.md`
holds parked rows, and a spec sentence is neither. The orchestrator never reads it, the close never
asks, and a class record written by the same unit tells the next reader the gate was handed to
someone, which reads as owned.

## Where it bit

`TOOL-aGraftedHelix-27` handed the location-probe class gate to the run's orchestrator. The build's
closing diff review found no unit and no parked row for it (`TOOL-aGraftedHelix-32`, from that
review's M7), and the class record pointed at a recipient that never took it. The mandate allowed
two dispositions, adopt or park, and the discovery got neither.

## Why it survives

A hand-off line reads as a disposition to its author, because it names who decides. It is one only
when the named party's own process reads it, and an orchestrator driving
`tools/workflows/unattended-build.template.js` reads verdicts, rosters and parked rows, never spec
prose. Most hand-offs are fine: they address an external owner through `hands-off** external`
lines, which the dependency graph already carries.

## Its gate

No machine gate. Measured at `9024901c`: 151 `hands-off** external` lines across every spec, of which
one addressed an orchestrator. A grep arm over the first population would red 150 legitimate
deferrals, and the wording of an orchestrator hand-off is free prose, so no predicate separates them.
The documented check, at a build's close: grep the build's specs for any line handing work to the
orchestrator or to "this run", and resolve each to a unit in the roster or a parked row in the
run-state file carrying its question, its options and its reason. A line resolving to neither is
this class.

## Related

[[retirement-inventory-misses-readers-by-value]] is the same blindness from the other side: there an
inventory misses a reader nobody listed, here a reader is named and the inventory it would need to
appear in does not exist.
