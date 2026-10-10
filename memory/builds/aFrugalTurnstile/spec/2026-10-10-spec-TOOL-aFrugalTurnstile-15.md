# TOOL-aFrugalTurnstile-15 — a post-merge red clears only on a FULL green that descends from it

**Status:** OPEN · rev-1 · 2026-10-10 · node a · Tier-2 · base bef97330 · streams tooling · order 7

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`check_post_merge_red` clears the red whenever the adopted or covering sha strictly descends from it, and that sha can be a `kind scoped` record's own. Design D8, the charter's §1 Landing line and the runbook promise the red binds until a FULL green descends from it. Promoted from the closing review's item H4 and M1 (finding ids 15 and 3), 2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md, at the CONVERGED exit (build method M4: every confirmed finding is promoted).

## 2. Scope (IN)

- **S1 — the full sha.** In `.githooks/pre-push`, the sha handed to `check_post_merge_red` is the full green the decision rests on: `scoped_full` on the adopted path; for a cover, the covering record's `base` when its kind is `scoped` and its own sha when its kind is `full` or it is a runner stamp. A scoped record whose base does not strictly descend from the red therefore forces FULL. Observed by AC1, AC2, AC3.
- **S2 — the design record.** The design record gains a §6 rev line saying D8's rule is the full green, and that TOOL-aFrugalTurnstile-7 S3's 'adopted green' is read as the full green under it. Observed by AC4.

## 3. Non-goals (OUT)

- Any finding of the review this unit does not name; each has its own promoted unit.
- A kit-version bump: one bump per touched kit happens after the last unit.

### Edges

none

## 4. Design

The fix is the review's, judged SOUND by its skeptic (or the skeptic's corrected fix where it judged the finder's unsound); see the report's item H4 and M1 for the defect, the reachable path and the left-shift gate.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `memory/builds/aFrugalTurnstile/build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md`

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

- **AC1** — When `GATE_POST_MERGE=local` is declared at R, `refs/gov/bar-red` names X, and the only candidate is a `kind scoped` record at a descendant of X whose `base` is older than X, the push decides `FULL gate` and prints no `cleared` line. Red when: it scopes, the behaviour at the previous commit.
- **AC2** — When the same scoped record covers the pushed tree, the push is not covered and decides `FULL gate`. Red when: it is covered.
- **AC3** — When the record's `base` is a full green that strictly descends from X, the red reads `cleared` and the push scopes. Red when: a full descendant is refused.
- **AC4** — When `grep -c 'rev D8' memory/builds/aFrugalTurnstile/build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md` runs, it prints `1`. Red when: `0`.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

New arm: .githooks/pre-push.test.sh · covers AC1 AC2 AC3 · a staged refs/gov/bar-red and a scoped record on an old base · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-10 · §1-§7: promoted from the closing review round 1, item H4 and M1.

## 10. Reuse audit

The seams are this build's own, named in §2 by file and function; `reuse_lookup.py` cannot see `.sh` (memory note "reuse_lookup cannot see shell seams"), so they were read from source at 61e5103c8. No existing seam does what §2 adds.

Recall terms used: pre-push full green stamp scoped boundary candidate post-merge red decide lineage ledger scrub
