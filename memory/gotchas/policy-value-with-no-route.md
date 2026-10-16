---
name: policy-value-with-no-route
description: a policy key catalogues a value that no item reading the key routes or witnesses, so a preset that selects the value cannot run
kind: class
universal: false
---

# A catalogued value with nowhere to go

## Symptom

Every behaviour is a switchable policy, so a key lists its allowed values and a preset picks one. The
items that read the key are written for the default. A non-default value then has no witness arm, no
route or no owner item. A preset that selects it either behaves like the default or stops with no next
item. The catalogue row and the preset table both read complete, because each lists the value.

## Where it bit

The library round, 2026-10-16, in the step definitions
(`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`) and v2's catalogue
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`). The round's
review (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-library.md`, M1, M2 and
M7) found three keys whose non-default values had no arm:
- `review.unclassed: reason` and `owner-rules` had no `none` disposition in `review.report`, and no
  owner route;
- `decisions.major: author-owner-ratifies`, the strict preset's value, had no owner item;
- `reuse.propose`'s witness typed the default's population in front of the key.

## The fix

- For each key an item reads, write each catalogued value's arm into the item: its witness, its route,
  and any owner item, with every outcome routed.
- Never type the default's guard in front of the key: the key selects the population.
- Walk each preset through the transition table before calling a catalogue row done.

The design records under `/build/` are its population. It has no machine gate yet: the join that
dDeclaredLoop owes beside the transition table (`gap-flow-15`) now names this walk.
