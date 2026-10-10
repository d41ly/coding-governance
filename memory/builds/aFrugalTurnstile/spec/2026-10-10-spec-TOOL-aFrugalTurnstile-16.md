# TOOL-aFrugalTurnstile-16 — the boundary's minors: one scoped base for both writers, the runner-stamp refusals armed, inherited bases and SHA-256 handled

**Status:** OPEN · rev-1 · 2026-10-10 · node a · Tier-2 · base bef97330 · streams tooling · order 8

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Four confirmed minors from the closing review, batched as one unit because they share the hook and the driver: the driver's scoped record names the adopted scoped sha as its base where the hook's names the full base (M2); no arm reaches the cover pass's runner-stamp refusals (M4); a scoped record over an inherited green can never be adopted (L1); and the driver rejects a 64-hex base (L2). Promoted from the closing review's item M2, M4, L1 and L2 (finding ids 4, 7, 9, 12, 16, 13, 10 and 11), 2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md, at the CONVERGED exit (build method M4: every confirmed finding is promoted).

## 2. Scope (IN)

- **S1 — M2.** `--decide`'s scoped line carries both shas, `scoped <scoped_base> <scoped_full>` (before the bar field TOOL-aFrugalTurnstile-13 adds); the close exports `GATE_BASE` from the first and writes the record's `base` from the second. The TOOL-3 parity arm compares whole records for kind scoped with a non-empty base, not `cut -f1`. Observed by AC1, AC2.
- **S2 — M4.** Arms in `.githooks/pre-push.test.sh` push the AC9 fixture with each altered runner stamp (a foreign `manifest`, a different `manifest_blob`, a different `fingerprint`) and assert no cover; with a non-covering bar record planted, the `not covered` line names the reason. Observed by AC3.
- **S3 — L1.** The hook's writer and the close decline a scoped record when the decision rests on an inherited green: `--decide` prints `-` as the full base there. Observed by AC4.
- **S4 — L2.** The driver accepts a 40- or 64-hex base, the hook's `case "${#x}:$x"` shape. Observed by AC5.

## 3. Non-goals (OUT)

- Any finding of the review this unit does not name; each has its own promoted unit.
- A kit-version bump: one bump per touched kit happens after the last unit.

### Edges

none

## 4. Design

The fix is the review's, judged SOUND by its skeptic (or the skeptic's corrected fix where it judged the finder's unsound); see the report's item M2, M4, L1 and L2 for the defect, the reachable path and the left-shift gate.

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

- **AC1** — When the decision adopts a `kind scoped` record M whose `base` is B, `--decide` prints `scoped M B` and the close's `gate-bar-green.scoped` carries `base` B. Red when: it carries M, the behaviour at the previous commit.
- **AC2** — When the parity arm calls both writers with kind `scoped` and base B, the two records are byte-identical but for `by` and `stamped`. Red when: they differ elsewhere.
- **AC3** — When each of the three altered runner stamps is the only candidate, the marker grows by one and no `covered on main push` line appears. Red when: any is covered.
- **AC4** — When a push scopes from an inherited green, no `gate-bar-green.scoped` is written and the decline line names `inherited`. Red when: one is written.
- **AC5** — When the close parses `scoped` with a 64-hex sha that exists, it honours it. Red when: it falls back to the full bar.

## 7. Gates

`pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `unattended kit gate` · `codebase-map coverage + freshness`

New arm: .githooks/pre-push.test.sh · covers AC1 AC3 AC4 · the AC9 fixture with altered stamps and an inherited green · none
New arm: tools/unattended/unattended.test.sh · covers AC2 AC5 · the writer parity slice and a 64-hex stub answer · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-10 · §1-§7: promoted from the closing review round 1, item M2, M4, L1 and L2.

## 10. Reuse audit

The seams are this build's own, named in §2 by file and function; `reuse_lookup.py` cannot see `.sh` (memory note "reuse_lookup cannot see shell seams"), so they were read from source at 61e5103c8. No existing seam does what §2 adds.

Recall terms used: pre-push full green stamp scoped boundary candidate post-merge red decide lineage ledger scrub
