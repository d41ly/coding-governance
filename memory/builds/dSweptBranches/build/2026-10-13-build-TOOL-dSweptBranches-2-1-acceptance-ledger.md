# Acceptance ledger — TOOL-dSweptBranches-2

**Serves:** journal TOOL-dSweptBranches-2

Built on `0baf2e47`, inline. The eight fixture arms were written first and run against unit 1's
stub: 17 of their 19 checks went red, and the two that did not are a fixture assertion that `git
cherry` misses the rebased copy and the stash arm's `UNKNOWN` case, which the stub's default
satisfies. The predicates were then written and all 34 checks went green.

Run over gov's own tree, that first version called `branch/dlandedverdict-rev3` `SUPERSEDED` by the
rotated predicate. Its one unique commit is a 250-line spec rewrite whose prose cites thirteen ids
that each exist somewhere under `memory/`. The predicate now takes rows only, a negative arm holds
that exact shape, and the branch reads `IN-PROGRESS` because its build is `INPROGRESS` on its tip
and not terminal on `main`. The spec's rev-2 records it.

Each break below was staged on a copy of `branch_reconcile.py` by a scratch script, observed red,
and the bytes restored.

**Evidences:** TOOL-dSweptBranches-2
- AC1 — `branch_reconcile.py` — the rebased copy reads `SUPERSEDED` with `patch 2` while `git cherry` lists both commits `+`; red with `DRIFT_LINES = 0`
- AC2 — `branch_reconcile.py` — the pre-fold variant reads `SUPERSEDED` with `landing 1` and no `no-op`; red with the landing predicate off
- AC3 — `branch_reconcile.py` — the records-only commit reads `SUPERSEDED` with `records 1`; red with the default's `RUN.md` phase test never matching
- AC4 — `branch_reconcile.py` — the archived row reads `SUPERSEDED` with `rotated 1` and the citing spec reads `UNMERGED-LIVE`; red with the search reading only `DECISIONS.md`, and red with the id-anywhere rule the gov run refuted
- AC5 — `merge-tree` — the net-zero branch reads `SUPERSEDED` by the no-op proof and the conflicting one `UNMERGED-LIVE`; red with the proof reading exit 1 as a no-op
- AC6 — `lease-utc` — the live lease reads `IN-PROGRESS`, the stale lease on an old tip and the unlanded fix read `UNMERGED-LIVE`; red with the lease rule off
- AC7 — `branch_reconcile.py` — with `--fresh-hours 0` the detached merge and the probe read `MERGED` with their covered content named, the uncovered file `UNMERGED-LIVE`, the nested and temp worktrees `MERGED`; under the default bound the nested one reads `IN-PROGRESS`; red with the content predicates off, and red with the freshness test off
- AC8 — `branch_reconcile.py` — the stash whose bytes landed reads `SUPERSEDED` and the one with new bytes `UNKNOWN`; red with the stash predicate off

On gov the report took 9 s over 10 worktrees and 41 refs.

## Owed at the close

The `branch-reconcile selftest` leg and the spec's §7 legs run in the close's bar. S7's raise rule
carries no arm, as the spec records.
