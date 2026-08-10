# decisions — index

> **Rotated 2026-08-10** — 79 rows moved byte-identical to [`archive/DECISIONS.2026-08-10.md`](archive/DECISIONS.2026-08-10.md), covering `PLAY-cDerivedGlossary-1` and `TOOL-aRuledParchment-1`..`TOOL-aMendedLedger-7`. Nothing deleted; the all-time id-collision grep still reaches them there.
>
> One line per decision, APPEND-ONLY, every family in one file. Detail in `decisions/`.
> Grouped by family for reading; the file is never re-sorted and a landed row is never edited.

## PLAY — playbook

*(none yet)*

## KICK — kickoff

*(none yet)*

## TOOL — tooling

- TOOL-aMendedLedger-8 · U9 REPLACES the merge driver's algorithm rather than patching it a fourth time: two planes split by row SHAPE, structure delegated to `git merge-file`, only the row set key-merged, recombined via a token skeleton. The bar is a live control per case
- TOOL-aMendedLedger-9 · a row one side MOVED and the other DELETED was dropped at rc 0 where git keeps it. The row plane is position-blind, so the SKELETON arbitrates: a surviving token for a deleted key means a move, and the disagreement becomes a scoped conflict

## DEPL — deployer

*(none yet)*
