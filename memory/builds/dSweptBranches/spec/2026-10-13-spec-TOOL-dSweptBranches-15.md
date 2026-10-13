# TOOL-dSweptBranches-15 — a submodule with uncommitted content makes its worktree UNKNOWN

**Status:** OPEN · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 14

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's round 1, H9 (ids 27). A changed submodule path is never compared as two missing blobs; it makes the worktree `UNKNOWN`.

## 2. Scope (IN)

- **S1** — A changed path whose status record is a submodule (`S…`), or that is a directory, is `submodule content`, which makes the worktree `UNKNOWN`. A path counts as absent only when it does not exist on disk and the default tree has no entry for it. Observed by AC1.

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

- **AC1** — When an idle worktree's submodule holds a modified file, `branch_reconcile.py` reports the worktree `UNKNOWN` naming `submodule content`.
  Red when: a submodule path is compared as a missing blob on both sides.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 · a fixture per criterion, observed red before its fix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted at the closing diff review's exit.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours for this behaviour, so no existing seam fits
beyond this kit's own functions. The seam is parse_status and check_worktree in `tools/branch-reconcile/branch_reconcile.py`, which this build wrote. The fix is the round-1 skeptic's, in `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md`.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
