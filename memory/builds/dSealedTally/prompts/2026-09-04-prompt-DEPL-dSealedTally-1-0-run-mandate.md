# Run mandate — dSealedTally

**Serves:** journal DEPL-dSealedTally-1 DEPL-dSealedTally-2 DEPL-dSealedTally-3 DEPL-dSealedTally-4 DEPL-dSealedTally-5 TOOL-dSealedTally-1

node d · 2026-09-04 · order 0 · streams tooling+deployer · authorized-by prompt

## The prompt, verbatim

The owner invoked `/unattended` with `--prompt` and this value, taken as the prompt itself because
it carries whitespace and names no readable file:

```
build DEPL-dRatifiedSeam-2...-6 TOOL-dRatifiedSeam-2
```

The bytes travel here rather than a reference, because the build folder is the authorization and may
not point at a file that can be edited after the run starts.

## What it resolves to

Six backlog rows, all OPEN, all filed by `dRatifiedSeam` on 2026-09-03 and 2026-09-04 rather than
folded into it. `-2...-6` is the inclusive DEPL range 2, 3, 4, 5, 6.

| Row | What it says |
|---|---|
| `DEPL-dRatifiedSeam-2` | landed sources sit outside the verify-and-rollback pass |
| `DEPL-dRatifiedSeam-3` | `rename_dests` is populated lazily, so a rename destination lands as new |
| `DEPL-dRatifiedSeam-4` | the tracked-count predicate needs a set, and the obvious fix is wrong |
| `DEPL-dRatifiedSeam-5` | `index_read` has no liveness on git's exit code |
| `DEPL-dRatifiedSeam-6` | the govkit self-test grades commit topology rather than the tree |
| `TOOL-dRatifiedSeam-2` | `--landed` writes its terminal phase before the check that refuses it |

Each becomes one unit under this build's own slug, per the pattern `dRatifiedSeam` itself followed
when it built two `dRetiredFork` rows: the backlog row is the finding and stays where it is until
its unit closes; the unit is the work and carries a new id.

## What was decided without an owner turn, and why no question was asked

The only candidate for the single permitted owner turn was how to verify a change to
`tools/unattended/unattended.sh` when that kit's self-test suites carry a standing do-not-run
instruction. That instruction answers it itself: a hermetic probe built from the suite's own setup,
or a staged-break equivalence corpus, and the owner gets the one command if only a full run would
settle it. So the question was already answered and asking it would have been a stall.

Acceptance and gates are derivable for all six rows — each names a measured defect with an
observable — so neither disqualifying field was missing.
