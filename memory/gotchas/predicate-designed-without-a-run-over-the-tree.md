---
name: predicate-designed-without-a-run-over-the-tree
description: a design states a new check's predicate without running it over today's population, so the check reds on hundreds of existing sites the day it arms, or ships with an exemption written by hand
kind: class
universal: false
---

# A check never run over the tree it will guard

## Symptom

A design record names a new check: a name shape, a grammar, a uniqueness rule, or a "keys, not a
scalar" rule. The design never runs the predicate over the tree as it stands. The day the check arms,
one of two things happens:
- it reds on every existing site that breaks the rule;
- its author writes an exemption by hand to get it green, so the check has never been seen red on
  its real population.

## Where it bit

The systems and retrofit audit of dClosedLoop, 2026-10-17
(`memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md`), found
four instances:
- M26: 139 of the 140 leg names fail the tag shape that the new `leg` namespace adds.
- M33: 374 `gov:` marker sites, over 20 words, fall outside a grammar that defines two words.
- M35: 13 tracked memory records repeat a heading that a uniqueness check reds.
- M16: 9 scalar pins, the lexicon's among them, fall under a "keys, not a scalar" rule.

The designs are in `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md` and
`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`.

It bit again in the shape audit, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`). Three populations
were typed rather than run: the causes, pins and work-order gates armed over today's corpus with no legacy population,
where a run over the tree would have shown almost no record carrying a cause; the region-parser factory's typed five,
beside which a query finds two more; and the floor inventory's grep for one version, which missed a `py>=3.10`.

## The fix

- Before a design states a predicate, run it over the real tree, as the charter's class rule says, and
  record the count it reports.
- Give each existing class of sites a disposition: renamed, registered, exempted with a reason, or
  seeded as a tolerated population.

It has no machine gate yet. The design owes a check that reports, when a predicate registers, how many
sites fail it.
