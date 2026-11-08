---
name: forwarded-arg-opens-an-unhandled-return-shape
description: a harness starts forwarding an argument to its callee, which opens a return shape the adapter never handled, so a real verdict reaches a refusal written for another case and is misnamed
kind: class
universal: false
---

# A forwarded argument opens a return shape nobody handled

## Symptom

A harness adds one argument to a call it already makes. The argument looks like plumbing, but the
callee has a path only that argument reaches, and the path returns a shape the adapter has never
seen. The adapter's existing tests read it as the nearest case they know, so a real verdict dies in a
refusal written for something else, under that refusal's diagnosis.

The forwarding arm passes, because it checks that the argument arrived, and nothing checks what
comes back once it does.

## Where it bit

The owner-ordered diff review of the dFairHearing build,
2026-11-05-review-TOOL-dFairHearing-43-47-diff-review, id 9. TOOL-dFairHearing-43 forwarded `walk` to
the audit in `tools/workflows/unattended-build.template.js`. Before that a whole-design call threw in
the callee, so the walk-red return was unreachable. Once reached, it held `blockers: null` beside an
integer `confirmed` and no dead agent, and the adapter's integer test threw `That is a DEGRADED run`
over a real BLOCKED verdict. The forwarding arms stubbed only a converged return.

## The fix

When a call starts passing an argument, read every return the callee reaches through it, and give
each shape its own branch ahead of the refusals. Stub the new shape in an arm, not only the old
return. A verdict the driver cannot count as a round stops by name, with its reason and an empty
roster, and records nothing.

## Its gate

Gated by `tools/workflows/unattended-build.test.sh`, its `FH48 AC4` arm.
