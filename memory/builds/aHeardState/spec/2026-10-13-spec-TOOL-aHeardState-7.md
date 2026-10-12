# TOOL-aHeardState-7 — the format-guard header states what happens to a continuation's commits, and an arm pins it

**Status:** CLOSED · rev-2 · 2026-10-13 · node a · Tier-1 · base 2f9dfaf0 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-aHeardState-1-2-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aHeardState-1-2-acceptance-ledger.md) | journal | TOOL-aHeardState-1 TOOL-aHeardState-2 TOOL-aHeardState-3 TOOL-aHeardState-4 TOOL-aHeardState-5 TOOL-aHeardState-6 TOOL-aHeardState-8 |

<!-- /gen:spec-records -->

## 1. Goal

Closing review round 1 id 3 (HIGH), with id 12 (LOW): the hook's header says commits made in a
`stop_hook_active` continuation are absorbed into the baseline ungraded. The code returns before the
sidecar write on such a stop, so those commits are demanded at the next unchained armed stop. The code
follows spec 1 §4; the header is wrong, and no arm pins either reading.

## 2. Scope (IN)

- **S1** — the WHAT THIS DOES NOT CHECK paragraph of `tools/hooks/format-guard.js` says a chained stop
  is not graded and a commit made in the continuation is demanded at the next unchained armed stop.
  NOT OBSERVED — comment prose, which no arm reads.
- **S2** — an arm in `tools/hooks/format-guard.test.sh`: after a baseline, a commit, a
  `stop_hook_active: true` stop that allows, then an unchained stop with no committed line, which
  blocks naming that commit. Observed by AC1.

## 3. Non-goals (OUT)

- Changing the behaviour: absorbing continuation commits would need the hook to arm on chained stops.

### Edges

none

## 4. Design

A header correction and one arm of three stops over the existing fixture helpers.

### Files touched (estimate)

- `tools/hooks/format-guard.js`
- `tools/hooks/format-guard.test.sh`

## 5. Acceptance criteria

- **AC1** — When the arm's chained stop is followed by an unchained stop over the fixture repository,
  `format-guard.js` blocks naming the commit made before the chained stop. Red when: the chained stop
  moves the baseline and the unchained stop allows.

## 6. Gates

`format-guard self-test` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted from closing review round 1 id 3; closes id 12.
- rev-2 · 2026-10-13 · §7 · the closing review's guard narrowing (TOOL-aHeardState-4 and -5) put `tools/hooks/` back in the spec-tokens join and made the `format-guard self-test` guard joinable, so the leg line names them.
