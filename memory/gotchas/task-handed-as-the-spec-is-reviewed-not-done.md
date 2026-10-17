---
name: task-handed-as-the-spec-is-reviewed-not-done
description: a task handed to a reviewer role through its spec input is read as the subject, so the reviewer audits the task's own text instead of doing it, and returns findings about the brief
kind: class
universal: false
---

# A task handed as the spec is reviewed, not done

## Symptom

A reviewer role takes one input, the spec it audits, and its standing instructions say to hunt that spec's
defects. A dispatcher writes a task, files it where the renderer accepts a spec, and hands it over. The
reviewer does exactly what its role says: it audits the task. It returns findings about the brief, such as
an ambiguous rule, a leaky method or a missing disposition, and never performs the work the brief asked
for. Each return looks thorough, so the miss shows only when someone checks what was asked against what came
back.

## Where it bit

dClosedLoop's ownership re-verification, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-ownership-verify.md`, `[misfire]`).

The owner asked three agents to re-verify the ownership table. The handoff gave three gov-spec-reviewers the
task through `input:spec`, since the renderer refused inline text for that input. All three audited the
task: they returned four, five and seven findings about the brief, and derived no owner.

## The fix

- Hand a reviewer the artifact under review as its spec, and the task through the harness's context.
- Hand a task that must be performed to a role whose input is a question, as the researcher's is.
- Before dispatching, read the rendered task as the role will. If the role's instructions say "audit what
  you are handed", the handed text is the subject.
