---
name: move-inventory-misses-readers-by-path
description: a move's consumer inventory lists the modules that import the moved names and misses everything that reaches them by path, a scan set, a fixture copy, a template copied into adopters or a glob over descriptors, so the move passes its own checks and strands those readers
kind: class
universal: false
---

# A move's inventory misses the readers that reach it by path

## Symptom

A design moves a module, a set of names or a descriptor, and lists its consumers by searching for imports. Readers
that reach the moved thing by path never appear:
- a gate's hand-listed scan set;
- a fixture that copies the file;
- a template copied into every adopter;
- a glob such as `*/kit.toml`.

After the move, the gate scans the old file and prints clean, and the fixture stops supplying what its subject
imports. An adopter's gate breaks on update. A new descriptor joins a population it was never meant for.

## Where it bit

dClosedLoop's whole-design audit, 2026-10-18
(`memory/builds/dClosedLoop/reviews/2026-10-18-review-PLAY-dClosedLoop-1-design-audit.md`, H4, M9 and M16):
- the id grammar's move left `check-verdict-epoch.sh` scanning `extract.py`;
- the `map_lib` move named no consumer;
- a `kit.toml` for gov's internal lib would join every kit glob.

## The fix

- Build the inventory by path as well as by import: a search for the file's name, scan sets, fixture copies, adopter
  templates, and every glob the new or moved file matches.
- Re-point or re-export in the move's own unit, and prove a scan set's change with a staged break in the moved file.
- Related: `retirement-inventory-misses-readers-by-value`.
