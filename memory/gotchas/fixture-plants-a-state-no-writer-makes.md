---
name: fixture-plants-a-state-no-writer-makes
description: a fixture writes by hand the ref, file or row its reader reads, in a place no production writer fills, so the arm is green over a state no real tree reaches and the reader selects nothing there
kind: class
universal: false
---

# A fixture plants a state production cannot reach

## Symptom

An arm is green and its rule really fires: the fixture holds the input and the reader reads it. In a real
tree the reader selects nothing, because the fixture wrote that input itself, where the reader looks and
where no writer puts it. Reader and fixture share one mistake, so each confirms the other.

## Where it bit

The dTotalRecall closing review of 2026-11-25
(`memory/builds/dTotalRecall/reviews/2026-11-25-review-TOOL-dTotalRecall-1-closing-diff-review-round1.md`, H5).
The orphan walk's claim root listed the local `refs/gov/claims/`, the namespace of the remote. The claim CLI
fills a clone's cache, `refs/gov/remote/claims/`, and nothing writes the local one. The `claim-root` plant made
the ref with a git plumbing write of its own and passed. In every clone the claim root held no slug, so a record
caused by a unit of a claimed build with no README yet read as an orphan.

## The fix

- A fixture reaches a state only through the writer production uses: here `run_claim_cli` of
  `tools/memory-tree/gen_build_index.py`, over a bare remote of the fixture's own.
- Where no production writer can make the state, the fixture says why on the line that plants it. A state
  nothing can make is the finding, not a fixture.
- The reader takes the location from its writer's module, so the two cannot spell it apart.

## Gated by

`tools/memory-tree/check-memory-hygiene.test.sh`, which runs the `claim-root` plant of
`tools/memory-tree/record_causes.py` and asserts the cache ref the CLI left and no orphan. It guards this one
reader; whether another fixture plants what nothing writes is a review question.

## What this does NOT say

- It coexists-with `fixture-passes-by-finding-nothing`: there the arm never meets the rule; here it meets the
  rule, in a state production cannot reach.
