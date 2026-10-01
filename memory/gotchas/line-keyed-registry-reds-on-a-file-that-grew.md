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

Measured on the install-prefix gate's waiver registry during `dTracedLattice`, before
`TOOL-aRepatriatedFork-30` deleted that registry: one row,
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

## Where this bit is gone, and what replaced it

The install-prefix gate kept that registry and a second, carried-literal ledger beside it. Both were
deleted by `TOOL-aRepatriatedFork-30`, which left `tools/check-install-prefix.sh` a pure ban with no
waiver file and no carried list. There is nothing there to re-key or hand-write any more: a shipped
file that spells a kit path has one legal answer, DERIVE the path. A test arm is still a shipped file
for that ban.

## The general shape

Any registry whose key is a POSITION rather than an identity has this property: `<path>:<line>`,
`<file>:<offset>`, an index into a generated list. If the key can move without the fact changing,
the check reports motion as violation. Prefer a content key where one exists; where the position IS
the point, expect to re-key and say so in the registry's own header.

## The gate

No registry in this repo is keyed by line today. `tools/dead-path-waivers.txt` is keyed by the
waived line's TEXT and an occurrence ordinal instead (`TOOL-dHonouredPark-3`), which is this page's
advice taken. The class stays for the next registry someone keys by position. Whatever gate owns
such a registry is the thing that reds; what no gate covers is the RE-KEY, because nothing
distinguishes a waiver whose line moved from a waiver that should not exist. There is
NO MACHINE GATE for that, and the discipline is prose.
