---
name: line-keyed-registry-reds-on-a-file-that-grew
description: a waiver keyed <path>:<line> stops matching when anything is inserted above it, so a gate reds on a file whose waived line nobody touched
kind: class
---

# A registry keyed by line number reds on a file that GREW

## Symptom

A gate reds naming a literal you did not edit, in a file you did edit. The literal is waived. The
waiver row reads `<path>:<line>` and the line number no longer matches, because your change added
lines ABOVE it.

Measured on `tools/install-prefix-waivers.txt` during `dTracedLattice`: one row,
`tools/codebase-map/map_lib.py`'s `REGEN_CMD`, re-keyed FOUR times in one build — 1387, 1426, 1454,
1475, 1493 — once per pass that grew the file. Every red named a line the pass had not been near.

## Why it bites

The registry is line-keyed for a good reason: a waiver that named only a path would waive every
future instance in that file, which is the exemption-widening the shrink-only rule exists to stop.
The cost of that precision is that the key is not stable under insertion, and nothing about the
error message says so — it reads as a new violation.

## What to do

**Re-key the line, never add a row.** The waiver COUNT is shrink-only; changing a line number leaves
it unchanged, while adding a row raises it and needs a justification the situation does not have.
Derive the new number from the checker's own output rather than counting by hand.

## The sibling arm is a BAN, not a ratchet, and it behaves differently

`tools/check-install-prefix.sh` has a second arm over `tools/install-prefix-carried.txt`, and
`--write-ratchet` REFUSES to absorb a new carrier — deliberately, so the remedy the gate prints is
not a self-service exemption form. A shipped file that starts carrying a `tools/<kit>/<file>`
literal has two legal answers: DERIVE the path (`map_lib.kit_rel()`), or hand-write a row with a
reason in the fourth column. **A test arm is a shipped file for this purpose** — a fixture spelling
a kit path tripped it in this same build.

## The general shape

Any registry whose key is a POSITION rather than an identity has this property: `<path>:<line>`,
`<file>:<offset>`, an index into a generated list. If the key can move without the fact changing,
the check reports motion as violation. Prefer a content key where one exists; where the position IS
the point, expect to re-key and say so in the registry's own header.

## The gate

GATED BY `bash tools/check-install-prefix.sh`, which is the thing that reds — that is
the point of the class rather than a gap in it. What no gate covers is the RE-KEY: nothing
distinguishes a waiver whose line moved from a waiver that should not exist, so the discipline is
prose. A checker could compare each waived line's CONTENT against the row it was written for, and
there is NO MACHINE GATE for it and that is a real unit nobody has specced.
