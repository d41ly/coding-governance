---
name: reseed-at-a-later-sha-launders-the-base
description: a seed command that rewrites a whole population at every run turns every offence added since the first seed into a seeded row, so the ratchet compares against a base it has just reset
kind: class
universal: false
---

# A re-seed resets the ratchet it seeds

## Symptom

A command seeds a check's tolerated population at a SHA. It runs again later: at a kit update, at a
widened predicate, or at someone's ask. If it rewrites the whole population, every offence added since
the first seed becomes a seeded row. "Never gains" then grades against a base that already holds those
offences, and the ratchet reads green over a population it has laundered.

## Where it bit

dClosedLoop's retrofit design, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`, `[seed]`).
`test.seed` wrote the whole population at every registration.

gov's own adopters already refuse to do that. The codebase map's adopter says a re-seed "would mask" a
real violation (`tools/codebase-map/adopt-codebase-map.sh`). The drift audit's adopter says it "would
silently reset every ratchet".

The design cited their seeding as its motivation and dropped their guard
(`memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md`, H3).

## The fix

- Seed only an absent population.
- A later run adds only the keys that a new or widened predicate measures, each with its widen
  record.
- A later run never rewrites, removes or re-dates a row.

It has no machine gate yet. The design owes a check that reds a seed run which removes or re-dates a
row, seen red on a planted offence re-seeded at a later SHA (the retrofit record's `[ratchet]`).
