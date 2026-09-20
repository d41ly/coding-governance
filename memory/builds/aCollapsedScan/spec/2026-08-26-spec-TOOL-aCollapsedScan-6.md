# TOOL-aCollapsedScan-6 — RETIRED: hygiene check 20 already gates per-file id uniqueness

**Status:** WONTDO · rev-2 · 2026-08-26 · node a · Tier-1 · base 3c37a1fb · streams tooling · order 4 · superseded by hygiene check 20, which already existed

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-build-TOOL-aCollapsedScan-7-acceptance-ledger.md](../build/2026-08-26-build-TOOL-aCollapsedScan-7-acceptance-ledger.md) | journal | TOOL-aCollapsedScan-4 TOOL-aCollapsedScan-7 |
| [2026-08-26-review-TOOL-aCollapsedScan-4-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-aCollapsedScan-4-spec-audit-round1.md) | spec-audit | TOOL-aCollapsedScan-4 TOOL-aCollapsedScan-7 |
| [2026-08-26-review-TOOL-aCollapsedScan-7-closing-diff.md](../reviews/2026-08-26-review-TOOL-aCollapsedScan-7-closing-diff.md) | diff-review | TOOL-aCollapsedScan-4 TOOL-aCollapsedScan-7 |

<!-- /gen:spec-records -->

## 1. Goal

Retire the finding that nothing gates a duplicate record id, and correct the three records that
carry it. The gate it proposed to build has existed since the row-grammar unit landed, it is on the
merge bar, and it was observed catching exactly the duplicate that provoked the finding.

## 2. Scope (IN)

- **S1** — This spec, carrying the evidence that retires the finding. It flips to `WONTDO` at
  close, AFTER AC2 and AC3 are observed — not before. rev-1 opened at `WONTDO`, and a terminal
  status over unmet acceptance criteria is what would have let the stale backlog row outlive the
  record that retires it, since no M6 pass builds a terminal unit.
- **S2** — The backlog row `TOOL-aCollapsedScan-6` flipped to `WONTDO` with the correction, in
  place, since a backlog row is mutable and its status is updated where it stands.
- **S3** — A `memory/DECISIONS.md` row recording the correction, because the false claim reached
  the decision log's neighbourhood through a commit message and a landing report and the correction
  has to be as findable as the claim.

## 3. Non-goals (OUT)

- Building any duplicate-id check. That is the whole point of the retirement.
- Draining `ROW_DUPLICATE_PIN` from 3 to 0. The three pinned duplicates in `memory/DECISIONS.md`
  are a declared shrink-only pin, and adjudicating whether each is a legitimate supersession is a
  reading of three decision records that this unit has no mandate to make.
- Rewriting the commit message of `3dd03ea1`, which carries the false sentence. History is not
  rewritten; the correction is a new record that supersedes it, which is this repo's stated rule for
  a ratified record.
- Closing the archive gap `memory/map/features/row-grammar.md` names — that a row which rotates out
  and is re-minted is not caught, because the live index and its archive are two files. It is a
  NAMED gap in a dossier, already recorded, and not a discovery of this unit.

## 4. Design

### What actually exists

`tools/memory-tree/row_grammar.py` implements hygiene **check 20**: per-file id uniqueness across
`memory/DECISIONS.md`, the backlog shards and the rotated archives, pinned shrink-only by
`ROW_DUPLICATE_PIN` in `.memory-tree.conf`, currently `3`. It is invoked by
`check-memory-hygiene.sh`, which is the merge-bar leg `memory hygiene`.

### The staged break, observed RED

A duplicate of `TOOL-aCollapsedScan-7` was appended to `memory/backlog/TOOL.md` and the check run:

```
check 20: 4 id(s) appear more than once within one row document (pin 3, shrink-only)
    memory/backlog/TOOL.md: TOOL-aCollapsedScan-7 at lines 225, 226
```

Reverted, control run: `row-grammar: clean (412 row(s) across the row documents, 3 pinned
duplicate(s))`. So the check is armed, scoped correctly, and reports the file, the id and both line
numbers.

### The three claims being retired

| Claim as filed | What is true |
|---|---|
| nothing gates a duplicate id | hygiene check 20 does, per file, on the bar |
| the full bar ran GREEN 39/39 with both duplicates present | no bar run ever saw them — the green predates the reconcile that created them and the post-merge green postdates the repair |
| the decision log's three duplicates show this is not a one-off | they are a DECLARED shrink-only pin, `ROW_DUPLICATE_PIN="3"`, not an ungated hole |

The second is the one worth keeping in view. It was not a reasoning error; it was an unchecked
assertion about which tree a green verdict had covered, made while reporting a defect found by
checking something else.

### Files touched (estimate)

This spec, `memory/backlog/TOOL.md`, `memory/DECISIONS.md`.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — the correction is the deliverable.
- risks — none. Nothing executable changes.
- testing + left-shift gates — the left-shift already exists and is check 20. The class this unit
  actually exposes is an unchecked claim about gate coverage, and `memory/gotchas/` already carries
  `vacuous-selector-empty-population` for its sibling shape.
- migration / rollback — N/A.
- user docs — none owed.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/row_grammar.py --check` runs over the tree, it reports
  clean at the declared pin, and when a duplicate is staged it names the file, the id and both line
  numbers — both observed, before and after.
- **AC2** — When `memory/backlog/TOOL.md` is read, row `TOOL-aCollapsedScan-6` carries `WONTDO` and
  names check 20 as what already covers it.
- **AC3** — When `memory/DECISIONS.md` is read, a row records the correction and names the three
  retired claims.
- **AC4** — When `bash tools/run-gates/run-gates.sh` runs, the bar is green.

## 7. Gates

`memory hygiene` (which owns check 20) · the full bar. No new gate, by construction.

## 8. Open questions

- **F1 — retire, or narrow the finding to the archive gap the dossier names?** RESOLVED (agent,
  2026-08-26, delegated): retire. The archive gap is already recorded in
  `memory/map/features/row-grammar.md` as a NAMED gap, so re-filing it under this id would be a
  second record of a known limit rather than a discovery, and the finding as written was about
  something else entirely.
- **F2 — should the three pinned duplicates be adjudicated here?** RESOLVED (agent, 2026-08-26,
  delegated): no. It needs a reading of three decision records to say whether each is a legitimate
  supersession, and a run under a mandate does not get to decide that the corpus is or is not in
  debt. §3 states it as a non-goal and the backlog keeps the question.

## 9. Revision log

- rev-1 · 2026-08-26 · authored straight to `WONTDO` after the reuse probe and the staged break.
- rev-2 · 2026-08-26 · folded the round-1 spec audit: held at `INPROGRESS` until its own S2 and S3
  are observed, because a terminal status carries live deliverables no pass would ever build.

## 10. Reuse audit

The probe that retired this unit IS the reuse audit: `memory/map/features/row-grammar.md`, reached
from `python tools/memory-recall/query.py`, states that uniqueness is asserted per file and why
corpus-wide was refused. The dossier's keyed claims are CI-verified, which is why they outranked the
prose finding — and the staged break was still run, because a dossier is evidence and not a
substitute for observing the gate fail. Recall terms used: `duplicate id backlog shard decision log
hygiene check merge driver row-keyed conflict ceiling budget gate leg check-30 population liveness`.
