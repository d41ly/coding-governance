---
name: an-allow-that-bypasses-a-judge-names-none
description: a permission hook answers allow on calls that a judge, a classifier or a person, would otherwise have seen, and names no judge in its place, so a destructive call runs with nothing judging it
kind: class
universal: false
---

# An allow that bypasses a judge, and names none

## Symptom

A design adds a hook that answers a permission request with allow. Before it, a judge saw those calls:
auto mode's classifier, or the person at the prompt. The hook's own checks are governance checks, such
as a write gate or a spawn cap. None of them asks whether a command is dangerous. So once the hook
allows, a destructive command runs, and nothing judges it. No benign-call fixture notices.

## Where it bit

dClosedLoop's runtime design, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`, `[act]`). An
attended or unbound session's gated call was approved once the guard packs passed. The ask rule on
every gated tool had already taken those calls away from auto mode's classifier, so neither the
classifier nor the person saw them.

The folds' closing review found it
(`memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-debt-folds.md`, H1). The
owner's RT-4 answer keeps the classifier or the person as the judge of attended sessions.

## The fix

- Every allow a hook answers names the judge that replaced the one it bypasses.
- A fixture plants a destructive call, such as an `rm -rf` of a scratch path, and expects it never
  approved without that judge.

It has no machine gate yet. The runtime design's `binding` fixture holds the planted arm
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`, `[tests]`).
