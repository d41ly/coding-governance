# Brief — aSwiftRefusal: the reciprocal hands-off edges to TOOL-aSwiftRefusal-4

**Serves:** research TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3

## The brief

### Goal
The close bar reds on memory hygiene check 12: spec 4's §3 declares **consumes-from** `TOOL-aSwiftRefusal-2` and **consumes-from** `TOOL-aSwiftRefusal-3`, and neither unit declares the matching **hands-off** `TOOL-aSwiftRefusal-4` back. Add each missing edge as a rev bump with its revision-log line, and change nothing else.

### Items
1. Spec 2's `### Edges` gains a **hands-off** `TOOL-aSwiftRefusal-4` line, mirroring spec 4's consumes-from line: unit 4 moves `check_unit_deferred` into the kit library and calls it from `--rescope` and check 23, with its body unchanged. Rev-2 to rev-3, one revision-log line.
2. Spec 3's `### Edges` gains a **hands-off** `TOOL-aSwiftRefusal-4` line, mirroring spec 4's: check 23 asks the release question of the deferred skip in `read_open_passes`, and unit 4's M3 block arms its `--audit` half. Rev-2 to rev-3, one revision-log line.

### Acceptance
`bash tools/memory-tree/check-memory-hygiene.sh --only 12` prints no `check 12 FAILED` line naming a spec under `memory/builds/aSwiftRefusal/spec/`, and `python tools/check-spec-tokens.py` prints no hit there.

### Gates
spec tokens · memory hygiene.

### Non-goals
Any change to a spec's scope, design, criteria or forks. Specs 1 and 4.

### Limitations
Spec text only; no code, no commit. The main loop commits after both checks read clean.

### Reuse
Spec 2's existing **hands-off** `TOOL-aSwiftRefusal-3` line is the shape; spec 4's §3 lines 78 and 79 carry the content.
