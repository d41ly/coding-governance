# TOOL-aFrugalTurnstile-14 — a run whose tree moved writes no lineage-qualified ledger row

**Status:** OPEN · rev-1 · 2026-10-10 · node a · Tier-2 · base bef97330 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The runner's ledger block sets a row's `full` from `GATE_FULL` and `TREE_CLEAN` alone, before `tree_moved` is known, so a FULL run whose tree moved mid-bar writes `ok` rows marked `full 1` whose keys may describe other content. A later `GATE_REUSE=lineage` run reuses them and can stamp `gate-full-green`. Promoted from the closing review's item H3 (finding ids 8), 2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md, at the CONVERGED exit (build method M4: every confirmed finding is promoted).

## 2. Scope (IN)

- **S1 — the order.** In `tools/run-gates/run-gates.sh`, `FPRINT_END` and `tree_moved` are computed before the ledger block, and a row's `full` is `1` only when `GATE_FULL` was set, the start tree was clean AND `tree_moved` is `no`. The existing later reads of `tree_moved` use the value already computed. Observed by AC1, AC2.

## 3. Non-goals (OUT)

- Any finding of the review this unit does not name; each has its own promoted unit.
- A kit-version bump: one bump per touched kit happens after the last unit.

### Edges

none

## 4. Design

The fix is the review's, judged SOUND by its skeptic (or the skeptic's corrected fix where it judged the finder's unsound); see the report's item H3 for the defect, the reachable path and the left-shift gate.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.evidence.test.sh`

## 5. Production-readiness checklist

- security — the change narrows what a green record may certify; nothing new is trusted.
- perf / scale — no new spawn on the common path beyond what each criterion names.
- error / empty / loading states — every refused input prints one line and takes the safe (larger) path.
- observability — the new refusal or decline line is named in §2.
- testing — the arm in §7, run at VERIFYING; the pass observes each criterion in a scratch fixture.
- migration — none; records written before this unit read as they did.
- risks — the fix can only force more work where it is wrong, never less; a mis-scoped predicate costs a saving, not a verdict.
- user docs — the touched script's header sentence.

## 6. Acceptance criteria

Each criterion is observed in a scratch fixture first against the file at the previous commit, then against the edit.

- **AC1** — When a FULL run's leg edits a tracked file mid-bar, every row the run writes to `gate-ledger.tsv` carries an empty `full` field. Red when: a row carries `full` `1`, the behaviour at the previous commit.
- **AC2** — When a `GATE_REUSE=lineage` run follows on the restored tree, it reuses none of that run's rows and writes no `gate-full-green` from reuse. Red when: it prints a reuse of one of those legs.

## 7. Gates

`run-gates evidence` · `run-gates canary` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 · a leg that edits a tracked file under GATE_FULL=1, then a lineage run · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-10 · §1-§7: promoted from the closing review round 1, item H3.

## 10. Reuse audit

The seams are this build's own, named in §2 by file and function; `reuse_lookup.py` cannot see `.sh` (memory note "reuse_lookup cannot see shell seams"), so they were read from source at 61e5103c8. No existing seam does what §2 adds.

Recall terms used: pre-push full green stamp scoped boundary candidate post-merge red decide lineage ledger scrub
