**Serves:** diff-review TOOL-dFinishedRecord-1

# Tier-2 closing diff review: dFinishedRecord, ROUND 1

*This is the closing review of build dFinishedRecord (gov, 2026-11-05). It covers the cumulative diff of the build's single unit, TOOL-dFinishedRecord-1, landing on main. Every finding below survived a skeptic prompted to refute it. The author of this report re-read the load-bearing lines in the tree: check 24's call site at `tools/unattended/check-unattended.sh:4195-4205` and the roster row at `memory/builds/dFinishedRecord/README.md:47`.*

**Reviewed range:** 3acab47a883b40fcedd1a8dffefb3a32179c36e3...9feeafc6b6ca8dfef0c3560829930ccc2d476942. **ROUND:** 1.

## Verdict: CLEAN WITH FIXES

No blocker, HIGH or MEDIUM finding survived. Two LOW findings stand, and each has a fix the skeptic judged sound. The shipped behaviour of check 24 is correct today. One finding is a missing regression arm. The other is a wrong description of the mechanism in the build's own README.

## Review shape

Intensity full: raw 3, confirmed 2, refuted 1, unverified 0 (0 uncertain), precision 0.67.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |

The adjudicated tally, counted two ways:

- **By item:** 0 BLOCKER, 0 HIGH, 0 MEDIUM, 2 LOW, which is 2 items.
- **By raw confirmed finding:** 0 blocker, 0 high, 0 medium, 2 low, which is 2 findings.

No item merges findings. Each confirmed finding takes its binding grade unchanged.

## Run integrity

- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 3/3 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 2 judged sound, 0 judged unsound, 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 0 re-graded by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

No integrity counter is non-zero, so the run is complete.

Four limits on what that completeness means:

- **Intent:** neither `specs` nor `context` was supplied. The lenses had only the range's commit messages as intent.
- **Lens notes:** none were supplied. Every lens ran on the kit's generic brief.
- **Checklist:** none was swept, because the project's bug-class checklist is absent. The zero counts on security, correctness and seams are not evidence that the project's recurring bug classes are absent.
- **By design:** none supplied. There was no caller byDesign and no block.

## Findings

### L1 (LOW, id 2): check 24's HELD exclusion has no arm

- **Where:** `tools/unattended/check-unattended.sh:4201`, with the arms in `tools/unattended/check-unattended.test.sh`.
- **What is wrong:** check 24's loop skips only LANDED and ABORTED records, so a HELD record reaches the new call to `check_derived_landed`. That predicate (line 698) also admits a HELD record whose `hold-code` is in HOLD_CODES_HANDOFF and whose landing commit the tip reaches. The spec states this case is excluded too (spec line 130). All three new arms (A, B, C) set `phase: LANDING`, and none uses a HELD record.
- **Consequence:** check 24's HELD exclusion is changed behaviour that no check can fail. The predicate is shared with checks 7 and 23, and check 7's HELD arm covers it, so the gap is limited to check 24's own call. A later edit that narrows that call would still pass the suite, for example dropping HELD or gating on `$ph = LANDING` before the call. Nothing wrong ships today.
- **Fix (judged SOUND by the skeptic):** add arm D after arm C. In it:
  1. Set tRos's record to `phase: HELD` with a `hold-code` from HOLD_CODES_HANDOFF.
  2. Commit it, push it to origin main, then `add_u7` and commit.
  3. `hit` 'check 24 EXCLUDED memory/builds/tRos/RUN.md' and `miss` 'check 24 FAILED'.
  4. Restore origin to `$ANCHOR0`.
  5. Raise FLOOR_ASSERTIONS (now 1140) and FLOOR_SHARD_8 (now 215) by 2 each.
- **Left-shift:** no existing gate fits this class. Add a bug-class checklist entry: when a check calls a shared admission predicate, it needs one arm for each phase the predicate admits at that call site, not only the phase that motivated the change.

### L2 (LOW, id 3): the build README places the call where the spec rejected it

- **Where:** `memory/builds/dFinishedRecord/README.md:47`, the roster's Mechanism cell.
- **What is wrong:** the cell says check 24 asks `check_derived_landed` "after its recorded-phase skip". The code asks it after the build-README skip (`[ -f "$bre" ] || continue` at `check-unattended.sh:4195`), which itself comes after the phase skip. The code comment says the call comes "AFTER every skip, as check 23 asks it". The spec's 'Alternatives rejected' section (line 189) rejects the placement directly after the recorded-phase skip.
- **Consequence:** there is no runtime effect, because the leg and its arms follow the spec. The risk is to the next change. If it follows the roster and moves the call ahead of the README skip, a record with no build README would print a `check 24 EXCLUDED` line even though it was never graded. That is the case the spec rejected.
- **Fix (judged SOUND by the skeptic):** reword the Mechanism cell to: check 24's roster loop asks `check_derived_landed` after all of its skips (phase and build README), as check 23 does, and excludes a derived-LANDED record.
- **Left-shift:** no gate can check a prose mechanism against code. Add a bug-class checklist entry: a roster Mechanism cell must not describe a placement or design that the unit's spec lists under 'Alternatives rejected'. Check this at the close.

## Refuted

Id 1 (verification, medium) was refuted. It said the spec's CLOSED header comes before any red-then-green observation record. That order is what `memory/guides/BUILD-METHOD.md` prescribes: the main loop records the observations at the close, before the bar. The detail is in the appendix.

review-shape kind=diff-review round=1 intensity=full at=synth raw=3 confirmed=2 refuted=1 unverified=0 blocker=0 high=0 medium=0 low=2 agents=9 out-tokens=33805

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | verification | memory/builds/dFinishedRecord/spec/2026-11-05-spec-TOOL-dFinishedRecord-1.md:3 | medium | - | refuted | The order the finding objects to is the order the method prescribes. The spec's rollout step 3 says the pass runs no gate leg and no suite. Step 5 and the AC1-AC3 'permission:' lines (spec lines 224, 229, 234, 240) give the red-then-green observation to the main loop at the close. AC5 is also assigned to the close (line 246). memory/guides/BUILD-METHOD.md:198-203 says a pass runs no suite and that a new arm's RED-first observation is the main loop's at the close, after the last unit is terminal. Lines 284-286 say the main loop observes each `New arm:` line red and green before the bar and records both in the unit's acceptance ledger under a separate `Pass: none` commit. The repo shows the same pattern elsewhere: unit passes set their own spec header to CLOSED in the pass commit (dc4813c40 and 871f3c975 for dCountedConsumers), and the RED-first observations land in a later records commit (e2fa66f0e for dFoldedAudit). So a CLOSED header with no observation record yet is the expected state while the close is still running, and this review is part of that close. It is not a defect the diff introduced. The work the finding names is still owed, and the method already makes it a required step before the bar, so nothing lets it be skipped. I read the arms at check-unattended.test.sh:4229-4272 and the floor raise of +7 (3 hit, 3 miss, 1 same) and found them consistent with the spec. I did not run the suite, because a reviewer runs no gate. | unsound | - |
| 2 | verification | tools/unattended/check-unattended.sh:4201 | low | low | confirmed | The finding holds. In tools/unattended/check-unattended.sh, check 24's loop skips only LANDED and ABORTED records, so a HELD record reaches the new call to check_derived_landed. That function (line 698) admits HELD when its hold-code is in HOLD_CODES_HANDOFF, and the spec says so explicitly ('A HELD record under a hand-off code ... is excluded too'). In the diff to check-unattended.test.sh, all three new arms (A, B, C) run `sed 's/^phase: .*/phase: LANDING/'`, and none uses a HELD record. So check 24's HELD exclusion is new behaviour that nothing tests: a later edit that narrows check 24's call to LANDING only would pass the suite. The predicate itself is shared, and check 7's HELD arm (test line ~6614) covers it, so the gap is contained to check 24's own call. That makes the impact low: a missing regression arm, with no wrong result shipped today. | sound | - |
| 3 | intent | memory/builds/dFinishedRecord/README.md:47 | low | low | confirmed | memory/builds/dFinishedRecord/README.md:47 is added by this diff. Its roster row says check 24 asks `check_derived_landed` 'after its recorded-phase skip'. In tools/unattended/check-unattended.sh, the call at line 4201 comes after `[ -f "$bre" ] \|\| continue` at line 4195, and that line comes after the phase skip. The code comment there says the call is asked 'AFTER every skip, as check 23 asks it'. The spec's 'Alternatives rejected' section (line 189) rejects the placement directly after the recorded-phase skip. So the README describes a placement that was not built. It has no runtime effect: it is a wrong record of the mechanism that could mislead the next change, and its consequence is limited to that. That makes it low. | sound | - |
