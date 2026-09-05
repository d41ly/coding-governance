# Brief — TOOL-aHoistedPass-5, folding round-1 spec-audit findings 33 and 7

**Serves:** history TOOL-aHoistedPass-5

*What the round-1 fold pass was handed for this unit, recorded because "which instructions produced
this diff" must have an answer on disk rather than in a transcript nobody kept. The pass ran as a
subagent with write access to ONE file, concurrently with the sibling brief for
`TOOL-aHoistedPass-6`; the two write sets are disjoint by file.*

## The write set declared before dispatch

`memory/builds/aHoistedPass/spec/2026-09-04-spec-TOOL-aHoistedPass-5.md`, and nothing else. In
particular NOT `tools/hooks/agent-cap.js`, which this spec cites but does not own, and NOT the
generated index or its generator — the parent re-renders those once, after both folds return.

`--dispatch` was NOT used to record this pair. It refuses on `check 49` because it grades a BUILD
pass against the build's declared order, and `TOOL-aHoistedPass-5` sits at `order 4` behind six units
that are neither terminal nor dispatched. A fold is not a build pass; the refusal is correct and the
declaration lives here instead.

## The instructions

Fold two confirmed findings from
[the round-1 spec audit](../reviews/2026-09-05-review-TOOL-aHoistedPass-1-spec-audit-round1.md).

**Finding 33 (high).** Section 3 asserts the fan-out hook is unchanged since `c4fcf5ad`. It is not:
`TOOL-aWeldedTribunal-1/2/3` plus four folds moved `tools/hooks/agent-cap.js` from 1610 to 1814 lines
between that base and BASE `e828f778`, widening the loop predicate, so every `agent-cap.js:<line>` in
section 4's nine-row inventory points at unrelated code. Three parts to the fix, and the third is the
one that costs something:

1. Restate section 3 against BASE, and NAME the command that proves whatever claim it makes about the
   file. A spec asserting a file is unchanged since a base must name the command that proved it; an
   unverified negative claim is exactly the shape a liveness assertion exists to catch.
2. Re-derive the nine anchors by opening the real file, preferring a NAME over a line number, because
   a named target survives the next shift.
3. RE-RUN the nine fixtures against the shipped hook, capturing each exit code WITHOUT a pipe — a
   pipe returns the pipe's status, which has already misled this repository once. Where an observed
   code differs from what section 4 claims, say so in the revision entry rather than overwriting it
   quietly.

**Finding 7 (medium).** The eight-key args contract and its `JSON.parse` guard have no acceptance
criterion; AC11 observes only the absence of `roster` and `reportPath`. A child shipped with `repo`
defaulted, or with the guard missing, passes every criterion in section 6 and then builds in the
wrong tree. Add a per-key refusal criterion and a string-payload criterion: an input contract is a
trust boundary, and a trust boundary gets a per-key refusal test rather than a schema assertion.

## The bounds it was given

- No commit, no `git add`, no `gen_build_index.py`.
- Bump `rev-3` to `rev-4`, date `2026-09-05`, leave `base c4fcf5ad` alone, append one revision entry.
- LF only; binary mode if edited through Python.
- **Take no kit-version bump.** The `review-harness` 1.6-to-1.7 move belongs to
  `TOOL-aHoistedPass-6`, on the explicit ground that this spec names none. Wanting one is a note, not
  an edit.
- Invent no measurement. Every address written must be one the pass opened, and every exit code one
  it observed.
