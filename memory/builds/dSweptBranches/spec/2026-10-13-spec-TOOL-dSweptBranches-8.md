# TOOL-dSweptBranches-8 — a registered worktree path holding another repository is never graded as the worktree, and rm -rf reaches only a proven worktree

**Status:** CLOSED · rev-2 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-1-runlog-5b01cd34.md](../build/2026-10-13-build-TOOL-dSweptBranches-1-runlog-5b01cd34.md) | journal | TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 TOOL-dSweptBranches-5 TOOL-dSweptBranches-7 TOOL-dSweptBranches-9 TOOL-dSweptBranches-10 TOOL-dSweptBranches-11 TOOL-dSweptBranches-12 TOOL-dSweptBranches-13 TOOL-dSweptBranches-14 TOOL-dSweptBranches-15 TOOL-dSweptBranches-16 TOOL-dSweptBranches-17 |
| [2026-10-13-build-TOOL-dSweptBranches-8-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-8-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-8-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-8-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's round 1, H2 (ids 1). A worktree path is graded and removed only after it is proven to be this repository's worktree: `<path>/.git` a file whose common dir is the inventory's own.

## 2. Scope (IN)

- **S1** — read_worktrees proves each existing linked worktree's identity: `<path>/.git` is a FILE and `git -C <path> rev-parse --path-format=absolute --git-common-dir` equals the inventory's common dir by `derive_key`. A worktree that fails it is flagged `foreign`, its status is not read, and it reads `UNKNOWN`. Observed by AC1.
- **S2** — remove_worktree runs S1's identity check before git's removal, because a removal that fails part-way may take the `.git` file the check reads, and its `rm -rf` fallback runs only when that check passed; otherwise the row fails. A registered worktree whose path is gone needs no special case: git's own removal drops it, measured. Observed by AC1.

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

- **AC1** — When a registered worktree path is replaced by a separate repository with a commit of its own, `branch_reconcile.py --write --fresh-hours 0` reports it `UNKNOWN` and that repository survives; a prunable worktree whose path is gone is pruned and the run exits 0.
  Red when: the identity check or the guard on the `rm -rf` fallback is removed.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 · a fixture per criterion, observed red before its fix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted at the closing diff review's exit.
- rev-2 · 2026-10-13 · S2 · the prune-only branch for a gone path is dropped: git's removal already drops such a worktree, so a staged break of the branch stayed green, and the check is run before git's removal rather than after it.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours for this behaviour, so no existing seam fits
beyond this kit's own functions. The seam is read_worktrees and remove_worktree in `tools/branch-reconcile/branch_reconcile.py`, which this build wrote. The fix is the round-1 skeptic's, in `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md`.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
