---
name: absence-read-from-one-of-several-homes
description: a fact stated in several homes is read from one, so a derived view or a probe reports it absent wherever that home is silent, and the blank reads exactly like a real gap
kind: class
universal: false
---

# A fact read from one of its homes reads as absent

## Symptom

A derived view renders a relation from one source per kind of node. The design states the relation in
several: a table column for some nodes, a section's prose for others, a citation in a third record for
the rest. Wherever the source the view reads is silent, the view renders a blank.

The blank looks the same as a real gap, and the same as a relation that is absent by design, so a
reader cannot tell the three apart. A check over the view passes, because it never asks for the
relation where the view left it blank.

## Where it bit

dClosedLoop's project map, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`,
`[reload-pointer]` and `[fixes]`).

- The generator took a step's owner only from its stage's build, so the adopt and lifecycle steps read
  as unowned. v2's chain rows cite all five adopt items, and flow-steps' `[lifecycle]` names
  dWellOiledMachine.
- The probe written to check that blank read only v2's chain rows, so it repeated the lifecycle miss.
- Ownership has four homes in that design: the chain table's stage column, chain-row prose,
  step-section prose and the systems' owner tables. None of them is a declared field.

It bit again in the shape audit, 2026-10-19
(`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-shape-reviews-compared.md`). The commit-key and
cause checks read act bindings from the node they run on, while bindings live on the node that made the act, so a lander
or a peer would read another node's work as unbound. Each act now pushes a minimal binding record the checks read on any
node, a missing one counted `not-local` and never passed.

## The fix

- Give the relation one home, a declared field, and derive every other statement of it from that field.
- Until then, a view or a probe that reports a relation absent names every home it read, and reads
  them all before it calls the relation missing.
- A blank in a derived view says which kind it is: nothing by declaration, or not declared.

It has no machine gate yet. The project map's owner check, widened to every node a build must build
and reading one declared field, is the gate the design owes (`[fixes-concept]`).
