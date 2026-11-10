**Serves:** diff-review TOOL-aShelvedLeg-1

# Closing diff review, round 2: aShelvedLeg unit 1, the unattended kit gate row declared no-trailer

2026-11-10 · Tier-2 · on `branch/clever-babbage-44839c` · adversarial fan through `tier2-review.js`: 5 finder lenses (gov-diff-reviewer), 1 skeptic batch (gov-skeptic), then this synthesis (gov-synthesizer). The subject is the cumulative diff landing on main.

**Reviewed range:** `3203e2ac4e6c6e6ea64197bd24bc05e094bcf8cc...13b83e12a86e1e7802e12f261233b9a421daf5d1`. **ROUND 2.**

## Verdict: CLEAN WITH FIXES

Nothing blocks the landing. The round-1 blocker is cured: the row is now declared `no-trailer:`. That declaration brings one MEDIUM defect with it. The row's FAIL column is always 0, so its reading is rc only, while the header says it gets the same reading as its two siblings. Fold the fix before the close.

## Review shape

Intensity full, raw 1, confirmed 1, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |

Adjudicated tally by item: 1 item, MEDIUM. By raw confirmed finding: 1 finding (id 1), graded MEDIUM. Blockers 0, highs 0.

### Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 1/1 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified. 0 orphaned duplicate refutations demoted to unverified. 0 duplicate refutations counted as merged confirmations. 0 spurious verdicts discarded. 0 duplicates.
- Fixes on confirmed findings: 0 judged SOUND, 1 judged UNSOUND, 0 judged INSTANCE-ONLY, 0 with no fix proposed, 0 NOT JUDGED. An unjudged fix would be the finder's proposal and nothing more.
- Severity on confirmed findings: 0 UNGRADED by the skeptic. 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: neither `specs` nor `context` was supplied. The lenses had only the range's commit messages.
- Checklist: 7 items, acquired by the harness from `--for-diff 3203e2ac4e6c6e6ea64197bd24bc05e094bcf8cc..HEAD`. Each went to exactly one lens: security 2, correctness 2, seams 1, verification 1, intent 1.
- By design: none supplied. There was no caller byDesign, and the block held 0 entries.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twins to flag.
- Dispositions: unclassed refuse. 7 class slugs were handed in, and 149 leg names were read from `tools/gate-legs.json`.
- Every count above is zero where it should be, so this run is complete.

## Items

### 1. MEDIUM: the `unattended kit gate` row is graded on rc alone, but the header says it gets rc plus a FAIL count (id 1)

- **What:** commit 13b83e12a adds `# no-trailer: unattended kit gate` to `tools/run-gates/selftest-pooled-evidence.txt:25`. Its header clause at `:22` says `check-unattended.sh` "likewise" has no `PASS (` line. That puts the row in the "rc plus ^FAIL count" reading the two suites above it get. But `tools/run-gates/run-selftests.sh:1597` counts failures with `grep -c '^FAIL'`. `tools/unattended/check-unattended.sh:316` reports each failed check as `UNATTENDED check N FAILED — ...`, and the checker prints no line that starts with `FAIL`.
- **Consequence:** this row's FAIL column is always 0. The declared-trailer-less READ branch (`run-selftests.sh:1636-1640`) still prints "rc-plus-FAIL only" for it. A red calibrate reading (rc 1, 0 FAIL) therefore matches any later red `--pooled` run, however different its failing checks are. The comparison cannot tell two different reds apart for this row. The header hides that by calling the row the same as `check-brief-recorded.test.sh` and `check-pass-order.test.sh`, which do print `^FAIL` lines. The effect is contained because the row is held off every automatic bar. It only matters when a red calibrate reading is compared with a different red `--pooled` run.
- **Fix (judged UNSOUND by the skeptic; the skeptic's corrected fix follows):** make the fails column count this checker's own failure lines. In `run-selftests.sh`, count `^UNATTENDED check [^ ]+ FAILED` together with `^FAIL`, or let each row declare its own fail pattern. If that is not done, keep the declaration and rewrite the header to say that this row's reading is rc only, because its failure lines are `UNATTENDED check N FAILED`, not `^FAIL`.
- **Left-shift gate:** extend `run-selftests self-test` with a fixture row declared `no-trailer:` whose script prints only non-`^FAIL` failure lines and exits 1. The fixture must show whether the calibrate's recorded FAIL count separates that run from one with a different failure set. A static arm under `--check` should also refuse any `no-trailer:` row whose script cannot print a line the fails pattern counts.

review-shape kind=diff-review round=2 intensity=full at=synth raw=1 confirmed=1 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=1 low=0 agents=7 out-tokens=20677
review-round round=2 limit=- prior=- count=0 state=-

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | verification | tools/run-gates/selftest-pooled-evidence.txt:22 | medium | medium | confirmed | The diff (13b83e12a) adds `# no-trailer: unattended kit gate` at selftest-pooled-evidence.txt:25 and a header clause saying check-unattended.sh 'likewise' has no `PASS (` line. run-selftests.sh:1597 computes the fails column with `grep -c '^FAIL'`. check-unattended.sh reports failures only through fail() at :316 (`UNATTENDED check $1 FAILED — $2`), and a grep found no echo or printf that starts a line with FAIL. So the row's fails reading is always 0, and the declared-trailer-less READ branch (:1636-1640) records it as 'rc-plus-FAIL' when it is really rc only. The two siblings it is compared with (check-brief-recorded.test.sh:263-265, and pass-order in the same way) do print ^FAIL lines, so 'likewise' overstates the parity this row gets. The defect is real and the diff introduced it. Its effect is contained: the row is held off every automatic bar, and the problem only matters when a red calibrate reading is compared with a different red --pooled run. | unsound | - | new:fail-count-reads-a-pattern-the-row-never-prints |
