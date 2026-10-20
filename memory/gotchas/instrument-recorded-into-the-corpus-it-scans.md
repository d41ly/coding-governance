---
name: instrument-recorded-into-the-corpus-it-scans
description: a probe's source is recorded beside its results, the page it scans later embeds that record, and its literal pattern matches its own quotation, so a clean page reads as broken, or a broken one as clean
kind: class
universal: false
---

# An instrument recorded into the corpus it scans matches itself

## Symptom

A probe scans a generated page for a literal pattern. The project records each instrument's source
beside its results, and the page embeds every record. Once the probe's record lands, the page holds the
probe's own pattern as data, and the probe counts that quotation as a hit. A probe that looks for a
defect finds a false one. A probe that looks for a required part finds it present when it is not.

## Where it bit

dClosedLoop's atlas, 2026-10-17
(`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`,
`[reload-summary]`).

The atlas step probe counted the page's theme blocks by the literal `--l-entry:`. The project-map
record's `[test-run-found]` embeds the probe, and the atlas embeds that record. So the probe found a
fourth "theme block" with no step tokens in it, and reported eight findings against a page that drew
every step.

## The fix

- Scope the scan to the structure that holds the real data, here the page's style elements, never the
  whole page.
- Re-run a probe over a page built from records after the probe's own record lands.
