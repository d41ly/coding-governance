---
name: rate-quoted-without-its-denominator
description: a rate put to the owner in a fork divides by the wrong population, so the option's own cost reads several times off
kind: class
universal: false
---

# Per what?

## Symptom

A fork's option carries a rate, so the owner can weigh its cost: proposals per build, findings per
review. The rate divides by a wider population than the one the option names, such as all builds
instead of the builds the option touches. The owner answers on a volume that is wrong by the ratio of
the two populations, and nothing in the record shows the division.

## Where it bit

The library round's LB-2, 2026-10-16, in
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-layer-library.md`. The option said
about 1.6 reuse proposals per build that builds a new seam. That figure is 256 specs over all 163
builds. Over the 67 builds that build a new seam, the rate is about 3.8. The research return
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-research-library-paths.md`) made
the same slip. The round's review
(`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md`, M11) caught it
after the owner had answered.

## The fix

- State a rate as its numerator over its denominator, naming each population, before the quotient.
- Keep the command that printed both counts beside the record that quotes the rate.
- Where a quoted rate turns out wrong after the owner answered, add a dated correction and tell the
  owner, without re-arguing the answer.

The fork records under `/build/` are its population. It has no machine gate yet, because a fork's
option text is prose.
