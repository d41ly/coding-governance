---
name: agent-output-interpolated-into-an-instruction
description: a field an agent returned is spliced unchecked into the text the main loop is told to act on, so a role agent's free text reaches the instruction channel of a session holding grants it lacks
kind: class
universal: false
---

# An agent's output interpolated into an instruction

## Symptom

A harness spawns an agent with a return schema, then composes a sentence the caller is told to act
on, `nextAction` or a prompt for the next stage, and concatenates one of the returned fields into it.
The schema types the field a string and tests nothing else. The value the harness itself was handed
beside it is shape-tested, because it is spelled inside backticks; the agent's half is not. A data
field becomes part of an instruction, written by an agent with fewer grants than its reader.

## Where it bit

aNimbleMend's unit harness, `tools/workflows/unattended-unit.js`, concatenated the builder's `sha`
raw into `nextAction`, the field the build skill tells the main loop to act on, while `passLegs`
beside it was refused on a newline or a backtick. Before that build `sha` travelled only as its own
return field and a log line. The closing review's round 1 found it as M1
(`memory/builds/aNimbleMend/reviews/2026-11-12-review-TOOL-aNimbleMend-1-closing-diff-review-round1.md`).

## The fix

Every agent-returned field that reaches an instruction passes a shape test first, and a value that
fails names nothing there. `TOOL-aNimbleMend-15` holds `sha` and `base` to `/^[0-9a-f]{7,64}$/`
before either reaches `nextAction`; the return's own field and the log line keep the raw value.

Gated by the `passLegs` arms of `tools/workflows/unattended-build.test.sh`, one per field: a `sha`
holding a space and a backtick, and an ill-shaped `base`, each asserted absent from `nextAction`.
For a field a later harness adds, this record is the checklist entry: ask which sentence the field
is spliced into, who acts on that sentence, and which test the value passed first.
