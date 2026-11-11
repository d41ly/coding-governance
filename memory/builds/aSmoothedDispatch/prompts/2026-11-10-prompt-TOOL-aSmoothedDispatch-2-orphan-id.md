# Revision brief — aSmoothedDispatch: spec 2 cites an id no spec defines

**Serves:** research TOOL-aSmoothedDispatch-2

## The brief

### Goal
Spec 2 at rev-2 cites dUnstalledConvoy's unit twenty-one twice, in §2 and in §10. No spec under `memory/builds/dUnstalledConvoy/spec/` defines that id, so `gen_build_index.py --write` writes it into that build's `ids:` front matter and its index region as an orphan. Revise spec 2 as a rev bump with its revision-log line naming this record, so it no longer spells the id.

### Items
1. §2's sentence "The containment direction is the fix dUnstalledConvoy's unit twenty-one made" names the record that holds the fix instead, by path: `memory/builds/dUnstalledConvoy/reviews/2026-08-21-review-TOOL-dUnstalledConvoy-1-12-lib-fix.md`.
2. §10's "the dUnstalledConvoy's unit twenty-one containment arms" becomes "the containment arms that review's fix added", or the same path.

### Acceptance
A grep of spec 2 for that id finds nothing, and `python -B tools/memory-tree/gen_build_index.py --write` leaves `memory/builds/dUnstalledConvoy/README.md` unchanged. The main loop runs the render.

### Gates
Spec tokens and the build index render, run by the main loop after you return.

### Non-goals
Any other change to spec 2, or to any other spec.

### Limitations
Edit only spec 2. Do not stage, commit or run a gate.
