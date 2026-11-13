# Brief — aLiftedCeiling: the instruction-edits leg's ceiling covers its wait on the tag index

**Serves:** research TOOL-aLiftedCeiling-1

## The prompt

> Yes, raise it

## The brief

### Goal
Raise the `instruction edits (manifest checks)` leg's declared ceiling so a bar whose tag-index writers meet one unbuilt tree
runs the leg once, waiting, instead of timing it out and retrying it.

### Items
1. The leg's ceiling in `tools/gate-legs.json` rises from 180 to the value its wait needs, argued from the leg's readings and its partner's, with the evidence recorded the way the run-gates kit records ceiling evidence. [planned TOOL-aLiftedCeiling-1]

### Acceptance
The manifest declares the new ceiling for the leg, the evidence file carries the reading that argues it, and a race of the two
tag-index checks on a fresh index in a scratch clone keeps the leg inside its new ceiling.

### Gates
`instruction edits (manifest checks)`, the run-gates kit's ceiling legs, `spec tokens (a spec's own names resolve)`, and the full
bar at the close.

### Non-goals
No change to the tag index, its busy timeout or any other leg's ceiling.

### Limitations
A ceiling is a kill bound, never a target: the raise is sized to the wait, not to make a slow leg pass. The kickoff manifest
watches `tools/gate-legs.json`, so the unit re-stamps it.

### Reuse
The seam is the leg's `ceiling` key in `tools/gate-legs.json` and the run-gates kit's `derive-ceilings.py`, which records a
reading with `--write --observed`.

## Drawn from the session

> Raise instruction edits' 180 s ceiling so the wait stops costing a retry?
— agent, 2026-11-12, the closing question after aQueuedIndex landed at aa8f08000

> The retried leg is instruction edits: its wall-clock ceiling is 180 s, and it now waits behind the tags leg's tree build, which takes about 95 s under load. The tags leg's ceiling is 420 s.
— agent, 2026-11-12, after aQueuedIndex's landing bar

## Owner confirmation

Asked: Raise instruction edits' 180 s ceiling so the wait stops costing a retry?
Answer: Yes, raise it
