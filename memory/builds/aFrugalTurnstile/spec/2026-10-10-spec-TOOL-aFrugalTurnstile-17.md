# TOOL-aFrugalTurnstile-17 — the post-merge minors: a clean-tree precondition, two guards armed, the protocol row corrected

**Status:** OPEN · rev-1 · 2026-10-10 · node a · Tier-2 · base bef97330 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Three confirmed minors from the closing review, batched because their write set is disjoint from the boundary minors: `post-merge.sh` records a full green without checking that its worktree is clean (M3); two of its guards have no arm (L3); and the protocol's `GATE_POLICY_FILE` row puts `GATE_POST_MERGE` in a file nothing reads it from (M5). Promoted from the closing review's item M3, M5 and L3 (finding ids 5, 17 and 14), 2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md, at the CONVERGED exit (build method M4: every confirmed finding is promoted).

## 2. Scope (IN)

- **S1 — M3.** `tools/run-gates/post-merge.sh`'s writer requires `git -C <worktree> status --porcelain --ignore-submodules=untracked` to print nothing, else prints one line and writes nothing. Observed by AC1.
- **S2 — L3.** Evidence-suite arms reach the guard that turns a runner's exit 0 without verdict GREEN into RED, and the guard that refuses when the worktree's HEAD moved. Observed by AC2, AC3.
- **S3 — M5.** The protocol's `GATE_POLICY_FILE` row says `INHERITED_RED` and its bound are read from that file and `GATE_POST_MERGE` always from the pre-push hook's `.githooks/gate-env.sh` at R; the kit template stays byte-identical, inside the protocol's size row. Observed by AC4.

## 3. Non-goals (OUT)

- Any finding of the review this unit does not name; each has its own promoted unit.
- A kit-version bump: one bump per touched kit happens after the last unit.

### Edges

none

## 4. Design

The fix is the review's, judged SOUND by its skeptic (or the skeptic's corrected fix where it judged the finder's unsound); see the report's item M3, M5 and L3 for the defect, the reachable path and the left-shift gate.

### Files touched (estimate)

- `tools/run-gates/post-merge.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/unattended/PROTOCOL.template.md`

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

- **AC1** — When a wrapper bar edits a tracked file in the post-merge worktree and exits 0, no `gate-bar-green.shared` is written and the output names the dirty tree. Red when: one is written, the behaviour at the previous commit.
- **AC2** — When a runner stub exits 0 and writes `verdict RED`, with `refs/gov/bar-red` staged at an ancestor, `post-merge.sh` exits 1 and the ref stays. Red when: it exits 0.
- **AC3** — When the bar moves the worktree's HEAD, `post-merge.sh` exits 2 with `REFUSED`. Red when: it exits 0 or 1.
- **AC4** — When `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` runs it exits 0, the `GATE_POLICY_FILE` row names `gate-env.sh` for `GATE_POST_MERGE`, and `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` exits 0. Red when: any fails.

## 7. Gates

`run-gates evidence` · `unattended protocol size` · `unattended kit gate` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC3 · a dirty-tree wrapper, a RED-verdict runner, a HEAD-moving bar · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-10 · §1-§7: promoted from the closing review round 1, item M3, M5 and L3.

## 10. Reuse audit

The seams are this build's own, named in §2 by file and function; `reuse_lookup.py` cannot see `.sh` (memory note "reuse_lookup cannot see shell seams"), so they were read from source at 61e5103c8. No existing seam does what §2 adds.

Recall terms used: pre-push full green stamp scoped boundary candidate post-merge red decide lineage ledger scrub
