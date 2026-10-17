---
name: ratchet-migration-ignores-how-each-source-grows
description: a migration puts many registries under one shrink-only ratchet without asking how each one grows, so an append-only history or a declared set reds on correct work, or widen records turn routine and the ratchet stops meaning anything
kind: class
universal: false
---

# One ratchet over registries that grow differently

## Symptom

A design moves many files of tolerated populations onto one primitive whose rule is "never gains". Some
of those files are debt that should only shrink. Others are append-only histories, declared sets that
gain a row with every new subject, or ceilings. Under one rule, every correct addition to the second
kind reds. The remedy, a widen record, then becomes routine, and the ratchet stops telling debt from
growth.

## Where it bit

dClosedLoop's retrofit design, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`, `[ledger]`).
RF-5 moved gov's 27 registries onto a shrink-only ledger.

The systems and retrofit audit found the defect
(`memory/builds/dClosedLoop/reviews/2026-10-17-review-PLAY-dClosedLoop-1-systems-retrofit.md`, H1).
Two of the 27 declare themselves append-only, refusal-retirements and transition-audit. readme-contract
gains a row for every new build README.

Read from each file's own header, the 27 are:
- 17 shrink-only debt;
- 2 append-only histories;
- 7 declared sets;
- 1 ceiling.

## The fix

- Give each registration a direction, and apply "never gains" to shrink-only debt alone.
- Before migrating a source, classify it by how it grows, and refuse a registration that has no
  direction.

It has no machine gate yet. The registry classification probe is filed with its planted run in
`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md`
`[probes-86]`. It holds the classification as a table, and exits 1 on a registry that has none.
