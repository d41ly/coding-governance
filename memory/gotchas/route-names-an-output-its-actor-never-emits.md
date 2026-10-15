---
name: route-names-an-output-its-actor-never-emits
description: a designed route or witness names an output, exit class or record that its actor never produces on that path, so the route is dead or waits forever
kind: class
universal: false
---

# A route reads what its actor never writes

## Symptom

A design record routes an item on an outcome, or proves it by a witness, that the named actor does not
produce where the route sits: a line the tool prints only on another branch, an exit class it never
returns there, a record it writes only on another path, or a result it starts and never collects. The
table reads well, because each word is something the tool does somewhere.

## Where it bit

The fold of the layer reviews, 2026-10-16, in
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`; the fold's
closing review (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-fold.md`, H1,
H2, M1, M9) caught four:
- `test.flakes` hung off the green verdict, but `tools/run-gates/run-gates.sh` prints
  `nondeterministic · <leg>` only on a run it has already turned red;
- exit 4 of `tools/push-main.sh` was routed to the post-merge bar's verdict, though that exit starts
  no bar and writes no marker;
- every exit 1 went back to Test, though one exit 1 comes after a landed push;
- `--land` was said to push the prepared merge and nothing else, though its race path re-prepares
  and pushes again.

## The fix

Before a route names an outcome, read the actor's code on that path:
- name the run outcome on which a printed line appears, and cite the evidence test that asserts it;
- check every exit class against the actor's exit lines, and its retry and loop paths;
- give every witness its carrier and the code that writes it, such as `<common-dir>/gate-post-merge`
  written by `tools/run-gates/post-merge.sh`.

It has no machine gate yet, because a design record's routes are prose. The join that dDeclaredLoop
owes over the step definitions (`gap-flow-15`) grades routes against the transition table, not
against an actor's code, so this entry is the guard until a route is declared as data.
