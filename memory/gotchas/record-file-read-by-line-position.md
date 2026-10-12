---
name: record-file-read-by-line-position
description: a key-TAB-value record file read by its first line takes whatever key the writer put first, and a TAB inside that value shifts every column after it in the row that copies it
kind: class
universal: false
---

# The first line was not the verdict

## Symptom

An instrument copies one value out of a run record into a TSV row by reading the record file's first
line. The writer's first line is a different key, `ended<TAB><time>`, so the row gains a field and
every later column, the proof among them, sits one place right. Nothing reds: a reader that counts on
position reads the expected-leg count as a proof and the end time as a leg count.

## The instance

`memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh` and
`memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh` read the
`verdict` file with `head -1`, and `tools/run-gates/run-gates.sh` writes `ended` first on every
path. The closing review of aPairedSlots found both (its H2 and H3).

## The remedy

Read a key-value file by key, with an awk that prints the second field of the line whose first is
the key, and have a reader of a TSV row assert the row's field count against its header before it
reads a column.

## Gating

No machine gate for the class. The two instruments read by key since TOOL-aPairedSlots-12 and
-13, and the two-bar check refuses a row of the wrong width by name.
