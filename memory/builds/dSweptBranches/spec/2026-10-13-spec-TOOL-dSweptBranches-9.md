# TOOL-dSweptBranches-9 — the patch predicate matches only a copy that shares more lines than it drifts, on the same files

**Status:** CLOSED · rev-2 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-9-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-9-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-9-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-9-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's round 1, H3 (ids 4, 11, 25). A same-subject commit counts as a rebased copy only when both touch the same files, neither patch is empty, and the lines they share outnumber their drift.

## 2. Scope (IN)

- **S1** — The `patch` predicate matches a same-subject candidate only when the two commits touch the same file set, neither `+`/`-` multiset is empty, the drift is at most `DRIFT_LINES`, and the shared line count `sum((a & b).values())` exceeds the drift. Observed by AC1.

## 3. Non-goals (OUT)

- No change outside the mechanism named above; the other promoted items are their own units.

### Edges

- **consumes-from** `TOOL-dSweptBranches-2` — the code this unit amends.

## 4. Design

The fix is the round's skeptic-judged fix, recorded in the review cited in §10, built as stated
there and observed red before it lands.

### Files touched (estimate)

- `tools/branch-reconcile/branch_reconcile.py`
- `tools/branch-reconcile/selftest.py`
- `tools/branch-reconcile/README.md`

### Alternatives rejected

- Folding this into another promoted unit: the closing review's exit rule promotes one unit per
  HIGH item, and the MEDIUM and LOW items as one batch.

## 5. Production-readiness checklist

- security — closes the review's finding; the costly error is a false deletable verdict.
- perf / scale — at most a few git calls per row or per commit.
- error / empty / loading states — an undecidable case keeps the row.
- observability — the evidence names what decided the row.
- risks — more rows kept, never more removed.
- testing — each criterion observed red before its fix.
- migration — N/A.
- user docs — the kit README.

## 6. Acceptance criteria

- **AC1** — When two same-subject one-line commits touch disjoint lines, or different files, `branch_reconcile.py` reads the branch `UNMERGED-LIVE`, while the rebased-copy fixture still reads `SUPERSEDED` by `patch`.
  Red when: the file-set or shared-lines rule is removed.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 · a fixture per criterion, observed red before its fix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted at the closing diff review's exit.
- rev-2 · 2026-10-13 · S1 · AC1 · the non-empty test is the shared-lines rule's own consequence (no shared line is never more than the drift), so it is not a separate clause; AC1 gains the same lines added to a different file, the case only the file-set rule refuses.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours for this behaviour, so no existing seam fits
beyond this kit's own functions. The seam is derive_coverage in `tools/branch-reconcile/branch_reconcile.py`, which this build wrote. The fix is the round-1 skeptic's, in `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md`.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
