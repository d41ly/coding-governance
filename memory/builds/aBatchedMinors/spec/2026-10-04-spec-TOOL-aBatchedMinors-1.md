# TOOL-aBatchedMinors-1 — RETIRED: a `minors` count the review harness already returns

**Status:** WONTDO · rev-1 · 2026-10-04 · node a · Tier-1 · base 5ba0fc4f · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-prompt-TOOL-aBatchedMinors-1-0-run-mandate.md](../prompts/2026-10-04-prompt-TOOL-aBatchedMinors-1-0-run-mandate.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The roster opened this unit so that `tools/workflows/tier2-review.js` would return the confirmed
MEDIUM and LOW count beside `blockers` and `highs`, giving the closing review's record a number nobody
has to count by hand.

It is retired before any code, because the harness already returns that number.

## 2. Scope (IN)

Nothing. The unit is retired before any code.

## 3. Non-goals (OUT)

Everything previously in scope: the `minors` return key, its early-return `null`s and its suite arm.

## 4. Design

### Evidence

Read at base `5ba0fc4f`. The harness derives `blockers` and `highs` from `perRaw`, a tally over RAW
confirmed ids in which every confirmed id sits in exactly one severity; when it does not, both counts
are `null`. So whenever `blockers` and `highs` are integers, `perRaw` sums to `confirmed`, and the
MEDIUM-plus-LOW count is `confirmed - blockers - highs` exactly. `unattended-build.js` already reads
it that way: its disposal stage owes a fold for `confirmed - blockers - highs` findings.

A `minors` key would be a second answer to a question the return already answers — the
two-answers-to-one-question class — and a reader could find the two disagreeing only by a defect.

### Files touched (estimate)

None.

## 5. Production-readiness checklist

- risks — none; nothing is built.

## 6. Acceptance criteria

- **AC1** — When `TOOL-aBatchedMinors-4` states how the closing review's `--minors` is derived, it
  names `confirmed - blockers - highs` from the harness return, summed over the rounds.
  Red when: the Skill tells the operator to count mediums and lows from the report by hand.

## 7. Gates

`spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · authored retired: the harness return already determines the count.

## 10. Reuse audit

The seam is the harness's existing return. `python tools/codebase-map/reuse_lookup.py "closing review
disposition promote findings to units by severity"` ranked name-stem neighbours only; the evidence is
the read of `tier2-review.js`'s tally and `unattended-build.js`'s disposal arithmetic above.

Recall terms used: closing review disposition promote fold severity BLOCKER HIGH MEDIUM LOW unit rescope CONVERGED
