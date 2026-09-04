# TOOL-aWeldedTribunal-8 — acceptance ledger

**Serves:** build TOOL-aWeldedTribunal-8

## What changed

Four rows in `memory/backlog/TOOL.md` flipped to `CLOSED`, each with the evidence that closed it in
its own tail. One row annotated as PARTIALLY ADDRESSED and deliberately left OPEN.

## Each criterion, answered

- **AC1 / AC2** — `TOOL-dScaffoldedMirror-22`, `TOOL-aGroundedOrientation-4`,
  `TOOL-aFlaggedScaffold-4` and `TOOL-aScouredKit-25` all read `CLOSED`. `TOOL-dScrubbedConduit-2`
  already did and was not touched.
- **AC3** — `row_grammar.py --check` rc 0, `corpus_ids.py --check` rc 0,
  `check-memory-hygiene.sh --staged` rc 0.
- **AC4** — every closure tail names a file and a line, or the unit it is a duplicate of. No closure
  is a bare status flip.

## What the closures say

| Row | Closed against |
|---|---|
| `TOOL-dScaffoldedMirror-22` | `dSealedTally`'s ordering fix, `tools/unattended/unattended.sh` lines 2444-2446 |
| `TOOL-aGroundedOrientation-4` | the same fix — one defect, two rows |
| `TOOL-aFlaggedScaffold-4` | `DEPL-dRetiredFork-4`'s `git_pathspec`, `tools/govkit/govkit.py` line 3724 |
| `TOOL-aScouredKit-25` | a DUPLICATE of `TOOL-aFlaggedScaffold-3`, per its own text |

## The row that STAYS OPEN, and why that is the honest answer

`TOOL-aFlaggedScaffold-3` is one of the owner's eleven and it is NOT closed. `TOOL-aWeldedTribunal-6`
built the REPORT half — `update` now names every source gov ships that the target does not hold and
says the install is INCOMPLETE — and by its own first non-goal it does not LAND the bytes, which is
what the row asks for. Landing means synthesising a receipt row whose role, commit and origin the
verb has no evidence for; that is an owner decision.

The row now carries a `PARTIALLY ADDRESSED` note saying exactly that, so a later reader is not left
to infer it from two rows at different statuses. Round 2 of the spec audit caught rev-1 trying to
close `TOOL-aScouredKit-25` against unit 6 instead, which would have put two rows with identical
headlines at opposite statuses — the stale-row harm this unit exists to remove, inverted.

## Two more stale rows found and NOT closed

`TOOL-dRatifiedSeam-2` and `TOOL-dTieredTribunal-28` both name the same `--landed` ordering defect
`dSealedTally` fixed, so both are stale too. Neither is in the owner's list. Closing rows nobody
asked about widens a records diff past what anyone reviewed, so they are NAMED in
`TOOL-dScaffoldedMirror-22`'s tail instead — the next run finds them already identified.

## One thing the tooling taught me here

`--dispatch` REFUSED to declare `memory/backlog/TOOL.md` as this pass's write set, because it is a
shared mutable record and M6 clause 3 forbids pairing one with anything. That is the verb enforcing
the build method rather than trusting it, and it is the right refusal: a solo pass needs no
declaration, and a co-declaration would have been the bug.
