---
name: check-format-grades-two-populations
description: the build README slot gate binds every tracked README on one axis and only the declared ones on the other, so a new folder can red on a rule its author never opted into
kind: class
---

# `--check-format` grades TWO populations, and a new build README is in the wider one

## Symptom

A build folder is opened and the `build README slot contract` leg reds on its README over the
`<!-- roster:units -->` pair or a slot's POSITION. The author looks in
`memory/project/readme-contract.txt`, finds the new README is not listed, and concludes the file
is outside the contract. It is outside the NARROW population and inside the wide one.

## Where it bit

`tools/memory-tree/gen_build_index.py` under `--check-format` grades two populations. The
`roster:units` pair and slot position bind EVERY tracked build README (`TOOL-dHonouredPark-1`). The
closed heading CANON and its per-slot byte budgets bind only what
`memory/project/readme-contract.txt` declares. A reader who knows the second rule and not the first
reads the contract file as the whole gate. All of it — both populations, why the roster pair stays
authored, and which readers still consume it — is `memory/map/features/build-readme-surface.md`.

## The fix

Seed a new README's roster pair from its OWN spec ids, and put the slots in the canon's order,
whether or not the file is in the contract. Read the dossier before the contract file: the contract
is the narrower population and cannot explain a failure on the wider one.

Gated by that leg — the class is that its two populations read as one, not that either is
unchecked.
