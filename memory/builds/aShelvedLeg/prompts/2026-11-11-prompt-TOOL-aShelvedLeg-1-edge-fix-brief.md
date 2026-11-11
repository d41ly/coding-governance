# Brief — aShelvedLeg: the reciprocal hands-off edges

**Serves:** research TOOL-aShelvedLeg-1 TOOL-aShelvedLeg-2

## The brief

### Goal
The bar reds on memory hygiene check 12: spec 2's §3 declares **consumes-from** `TOOL-aShelvedLeg-1`, and spec 1 declares no matching **hands-off** `TOOL-aShelvedLeg-2` back. Unit 3's spec, written beside this, declares **consumes-from** `TOOL-aShelvedLeg-2`, so spec 2 owes a **hands-off** `TOOL-aShelvedLeg-3` back. Add each missing edge as a rev bump with its revision-log line, and change nothing else. Both specs are CLOSED; this is the same reciprocal-edge exception aSwiftRefusal's specs 2 and 3 took at 478bf8254.

### Items
1. Spec 1's `### Edges` gains a **hands-off** `TOOL-aShelvedLeg-2` line: unit 2 corrects the closing review's minors on what unit 1 wrote. Rev-2 to rev-3, one revision-log line.
2. Spec 2's `### Edges` gains a **hands-off** `TOOL-aShelvedLeg-3` line: unit 3 corrects unit 2's closing-review minors. Rev-1 to rev-2, one revision-log line.

### Acceptance
`bash tools/memory-tree/check-memory-hygiene.sh --only 12` prints no `check 12 FAILED` line naming a spec under `memory/builds/aShelvedLeg/spec/` once unit 3's spec is also in the tree, and `python tools/check-spec-tokens.py` prints no hit there.

### Gates
spec tokens · memory hygiene.

### Non-goals
Any change to a spec's scope, design, criteria, status or forks. Unit 3's spec.

### Limitations
One spec per agent: the spec this handoff names is the only file it edits.

### Reuse
The edge lines aSwiftRefusal's specs 2 and 3 gained at 478bf8254.
