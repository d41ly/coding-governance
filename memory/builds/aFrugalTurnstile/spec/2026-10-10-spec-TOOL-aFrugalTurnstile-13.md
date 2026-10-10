# TOOL-aFrugalTurnstile-13 — the close honours a `--decide` answer only for the bar it will run

**Status:** OPEN · rev-1 · 2026-10-10 · node a · Tier-2 · base bef97330 · streams tooling · order 7

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`pre-push --decide` decides for the hook's bar, `${GOV_GATE_CMD:-bash $GATE_RUNNER}`, and the close then skips or scopes its own `$GATE_CMD` without checking the two are one bar. An adopter whose wrapper `GATE_CMD` differs from the hook's bar would have gates-green met on a tree the declared bar never graded. Promoted from the closing review's item H2 (finding ids 2), 2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md, at the CONVERGED exit (build method M4: every confirmed finding is promoted).

## 2. Scope (IN)

- **S1 — `--decide` names its bar.** The decision line gains the bar it decided for as a trailing field after a TAB: `full <why>\t<bar>`, `scoped <base>\t<bar>`, `covered <record>\t<bar>`, where `<bar>` is the vetted `$gate`. The hook's other output is unchanged. Observed by AC1.
- **S2 — the close compares.** The driver honours the answer only when that field equals `$GATE_CMD` byte for byte; otherwise it runs `GATE_FULL=1` and prints `unattended: gates-green — pre-push --decide decided for '<bar>', not this close's bar '<GATE_CMD>'; running the full bar`. A line with no field is refused the same way. Observed by AC2, AC3.

## 3. Non-goals (OUT)

- Any finding of the review this unit does not name; each has its own promoted unit.
- A kit-version bump: one bump per touched kit happens after the last unit.

### Edges

none

## 4. Design

The fix is the review's, judged SOUND by its skeptic (or the skeptic's corrected fix where it judged the finder's unsound); see the report's item H2 for the defect, the reachable path and the left-shift gate.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`

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

- **AC1** — When `pre-push --decide <tip> <R>` runs in the TOOL-aFrugalTurnstile-7 fixture, its one stdout line ends in a TAB and the vetted bar. Red when: the line carries no bar field.
- **AC2** — When a declared `GATE_POST_MERGE=local` close runs with `GATE_CMD` naming a wrapper and the stub hook answering `covered <record>` followed by a TAB and the runner's own bar string, the wrapper runs with GATE_FULL set to 1 and the output carries `not this close's bar`. Red when: the close is met without a bar, the behaviour at the previous commit.
- **AC3** — When the stub's bar field equals `GATE_CMD`, the answer is honoured as before (`met without a bar` for covered). Red when: an equal bar is refused.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `unattended kit gate` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 · the FT9 stub hook with a bar field, a wrapper GATE_CMD · none
New arm: .githooks/pre-push.test.sh · covers AC1 · the --decide fixture · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-10 · §1-§7: promoted from the closing review round 1, item H2.

## 10. Reuse audit

The seams are this build's own, named in §2 by file and function; `reuse_lookup.py` cannot see `.sh` (memory note "reuse_lookup cannot see shell seams"), so they were read from source at 61e5103c8. No existing seam does what §2 adds.

Recall terms used: pre-push full green stamp scoped boundary candidate post-merge red decide lineage ledger scrub
