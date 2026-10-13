# TOOL-dSweptBranches-12 — every name the default branch goes by is kept, the remote's own HEAD branch included

**Status:** CLOSED · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-12-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-12-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-12-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-12-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the closing review's round 1, H6 (ids 6). Write mode keeps the ladder's chosen default branch and the remote's observed HEAD branch, locally and on the remote.

## 2. Scope (IN)

- **S1** — resolve_default keeps the ladder's observed remote `HEAD` branch. derive_action keeps every default name, locally and as `<remote>/<name>`, and write_deletions filters all of them out of the push. Observed by AC1.

## 3. Non-goals (OUT)

- No change outside the mechanism named above; the other promoted items are their own units.

### Edges

- **consumes-from** `TOOL-dSweptBranches-3` — the code this unit amends.

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

- **AC1** — When `GOV_DEFAULT_BRANCH` names `develop` while `upstream/HEAD` names `main`, an ancestor of `develop`, `branch_reconcile.py --write --remote` keeps local and remote `main`, and both rows read `keep (the default branch)`.
  Red when: only the chosen branch is excluded.

## 7. Gates

`branch-reconcile selftest` · `codebase-map coverage + freshness` · `memory hygiene`

New arm: `tools/branch-reconcile/selftest.py` · covers AC1 · a fixture per criterion, observed red before its fix · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, promoted at the closing diff review's exit.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours for this behaviour, so no existing seam fits
beyond this kit's own functions. The seam is resolve_default and derive_action in `tools/branch-reconcile/branch_reconcile.py`, which this build wrote. The fix is the round-1 skeptic's, in `memory/builds/dSweptBranches/reviews/2026-10-13-review-TOOL-dSweptBranches-1-2-3-4-5-closing-diff-round1.md`.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
