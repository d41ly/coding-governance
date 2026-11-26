**Serves:** diff-review TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-5 TOOL-aPrunedIndex-6 TOOL-aPrunedIndex-7 TOOL-aPrunedIndex-8 TOOL-aPrunedIndex-9 TOOL-aPrunedIndex-10 TOOL-aPrunedIndex-11 TOOL-aPrunedIndex-12 TOOL-aPrunedIndex-13 TOOL-aPrunedIndex-14 TOOL-aPrunedIndex-15 TOOL-aPrunedIndex-16 TOOL-aPrunedIndex-17 TOOL-aPrunedIndex-18 TOOL-aPrunedIndex-19 TOOL-aPrunedIndex-20 TOOL-aPrunedIndex-21 TOOL-aPrunedIndex-22 TOOL-aPrunedIndex-23 TOOL-aPrunedIndex-24 TOOL-aPrunedIndex-25 TOOL-aPrunedIndex-26 PLAY-dClosedLoop-1 TOOL-aTwinnedPass-1 TOOL-dPlacedRequest-95 TOOL-dPlacedRequest-105 TOOL-dSettledStage-1

# aPrunedIndex: closing diff review of the round 3 fold (unit 24 and the waiver records), round 4

*2026-11-26. A Tier-2 adversarial pass over the fold since round 3's tip. Roles: finders gov-diff-reviewer,
skeptic batches gov-skeptic, synthesis gov-synthesizer.*

Reviewed: 3d93e3e18cf57b9ee43f300c93c3171a37d294be...8733e3654a5d98add31b5331f0d3d331780fdcd3

Round: 4

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs.
Two mediums and one low need fixing: three items holding six confirmed findings.
Every finding sits in a record, and no code or budget row moves.
The two mediums are the owner's waiver deviations for units 17 and 20, which waive only the gauge band while the readings also break other red conditions of the same criterion.

Subjects: unit 24 (TOOL-aPrunedIndex-24, commit 2f8d3b837) adds a `held-key` plant to `tools/playbook/gov_tag.py` and its row to `tools/playbook/tag_bundle.py#SELFTEST_ROWS` (15 rows now).
The plant pins spec 17's eleven-read key vector, including the `.git`-exists guard, at the fixture root and at a directory with no `.git`.
It checks that a failing read spawns git on each call and a held read spawns once, and reads every `HELD_FLAGS` member against a pinned list.
`"--"` is removed from `HELD_FLAGS`.
The rest of the range is records: round 3's ledger amendments, the owner's waiver deviations for units 17 and 20, unit 24's spec rev-2 and audit, and asks TOOL-aPrunedIndex-25 and -26.

Review shape: intensity full, raw 6, confirmed 6, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.
Adjudicated tally by item: 3 items, 0 blocker, 0 high, 2 medium, 1 low.
Adjudicated tally by raw confirmed finding: 6 findings, 0 blocker, 0 high, 4 medium, 2 low.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 3/3 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified.
- 0 orphaned duplicate refutations were demoted to unverified.
- 0 duplicate refutations were counted as merged confirmations.
- 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 0 judged sound, 0 judged UNSOUND, 6 judged INSTANCE-ONLY (each cures the cited instance and leaves its class standing), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 2 RE-GRADED by the skeptic (ids 1 and 3, high to medium).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: 1 spec document supplied as `specs`, beside the range's commit messages.
- Checklist: 10 items, each assigned to one of 5 lenses (security 2, correctness 2, seams 2, verification 2, intent 2).
- By design: the caller's byDesign.
- Refuted findings shown: 0. Same-address pairs shown: 0. No twin flags.
- Dispositions: unclassed refuse; 10 class slugs handed; 226 leg names read from `tools/gate-legs.json`.

Every lens and skeptic batch returned, so the run is complete.
The zero security yield is a returned lens's result, not a gap.

## Items

### 1. MEDIUM: deviation 17-1 waives only AC8's gauge band, but AC8's ratio bound and 106 s cap also failed, and it gives the wrong worst reading (ids 1, 3)

Where: `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-deviation-1.md@e769e42c:8` (title at line 1), and the owner prompt it cites, `memory/builds/aPrunedIndex/prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md@796af11f:11-13`.

What is wrong: spec 17 AC8 (line 335ff, red-when at line 365) is green only if all four conditions hold.
They are exit 0 under 300 s, gauges within 1.5x, worst after over worst before <= 0.90, and worst after <= 106 s.
The unit 17 ledger's AC8 line records set 3 as before 94.4/99.7/139.5 s and after 82.1/132.0/99.9 s.
That gives a ratio of 132.0/139.5 = 0.95, over the 0.90 bound, and a worst after of 132.0 s, over the 106 s cap.
The deviation prints "ratios 0.80 to 0.95 against its 0.90 bound" but names only "The gauge band was not met" as the departure.
It also says the 159 s budget row "already covers the worst reading of 104.7 s".
That 104.7 s is unit 20's worst after reading, not unit 17's, which is 132.0 s (worst before 139.5 s).
The owner prompt 17-5 put the same 104.7 s to the owner and asked only about the band.

Consequence: unit 17 reads as CLOSED and accepted with two AC8 red conditions broken and not recorded as waived.
The owner's ruling rests on a misstated maximum and covers one of the three failed conditions.
The effect stays in the records.
No budget or evidence row was written, and 132.0 s and 139.5 s still sit under the 159 s row.

Grades: id 1 medium (finder high, skeptic re-graded medium, binding). id 3 medium (finder high, skeptic re-graded medium, binding).
The id 3 skeptic also corrected the finding's claim that ask TOOL-aPrunedIndex-18 sizes budgets from 104.7 s.
Ask 18 is a review-class gate ask (BACKLOG line 16) and sizes no budget.

Fix (both ids judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):
- Fix this together with item 2 as one class.
- Restate the title, Before and After lines of deviations 17-1 and 20-1 to name every failed AC condition and the true worst readings.
- For 17 that is the gauge band, ratio 0.95 > 0.90, worst after 132.0 s > 106 s, and worst before 139.5 s.
- Amend both ledgers' RED lines, which each say only "all three sets out of the gauge band", the same way.
- Correct the shared owner prompt 17-5's "104.7 s" line to those figures.
- Put the full set of breaches to the owner, record the answer in a new prompt record, and cite it from both deviations.

The finders' proposal cures this instance alone: restate deviation 17-1's lines and the prompt's figure, then re-ask the owner about the ratio and the cap.

Left-shift: dispositions `class:amendment-leaves-its-other-half-standing` (id 1) and `class:fold-text-is-unreviewed-surface` (id 3).
Suggested gate: a deviation-record check that reads the AC it cites from its spec and refuses a deviation whose "Departs from" list omits any red condition the cited ledger line's readings break.

### 2. MEDIUM: deviation 20-1 waives only AC5's gauge band, though its own ratio of 0.76 breaks the 0.75 bound, and its "covers the worst reading" claim is false (ids 2, 4)

Where: `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-20-deviation-1.md@2635bb28:8` (title and Before line at line 1), and the same owner prompt `memory/builds/aPrunedIndex/prompts/2026-11-26-prompt-TOOL-aPrunedIndex-17-5-owner-waiver.md@796af11f:9-13`.

What is wrong: spec 20 AC5 (line 177ff, red-when at line 198) is red when the ratio exceeds 0.75, separately from the gauge band.
The unit 20 ledger's AC5 line gives set 2 as max after 82.6 s over max before 108.6 s, a ratio of 0.76.
The deviation's After line prints "0.57 to 0.76 against its 0.75 bound", yet its title and Before line name only the gauge band.
The owner prompt asked only about the band.
The After line also says the 159 s row (`selftest-budgets.txt:146`, `tags bundle selftest 159`) "already covers the worst reading of 104.7 s".
Set 3's before reading of 181.4 s is the worst on the full tree, and it is over that row.

Consequence: AC5's ratio breach is accepted without being recorded as a departure or put to the owner.
A reader of the deviation index takes the 0.75 bound as met, and reads a false coverage claim about the budget row.
The effect is contained: no row was written, and every after reading is at or under 104.7 s.

Grades: id 2 medium (binding). id 4 medium (binding).

Fix (both ids judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):
- Apply item 1's correction to deviation 20-1 as part of the same class fix.
- Name the gauge band and the ratio of 0.76 > 0.75 (set 2) as failed conditions.
- Replace "the worst reading of 104.7 s" with the real readings: worst after 104.7 s, worst before 181.4 s, which is over the 159 s row.
- Amend the unit 20 ledger's RED line to match.
- Cite the one owner answer covering every breach in both units.

The finders' proposal cures this instance alone: name the ratio breach in deviation 20-1 and get it accepted by the owner or retake AC5.

Left-shift: dispositions `class:amendment-leaves-its-other-half-standing` (id 2) and `class:fold-text-is-unreviewed-surface` (id 4).
Suggested gate: the deviation-record check from item 1, plus a test that any "covers the worst reading of N s" figure equals the max of the cited ledger line's readings.

### 3. LOW: unit 24's seen-red line records the `tags bundle selftest` leg red, but only the in-process plant was observed red (ids 5, 6)

Where: `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-24-1-acceptance-ledger.md@d2855fd6:18`, and spec 24's section 6 arms at `memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md@b8d00905:214-216`.

What is wrong: line 18 records the leg `tags bundle selftest` as red at 2f8d3b837 under five breaks "patched in memory".
Ledger line 5 says no merge bar, suite or gate leg ran, and the readings came from a scratch probe calling `gov_tag.main([...])` in-process.
The leg launches each plant through `run_plant_process` (`tools/playbook/tag_bundle.py:393-397`), which starts a fresh `sys.executable gov_tag.py` subprocess.
An in-memory patch cannot reach that subprocess, so the leg was only ever seen green.
Spec 24's section 6 arms say the row was "staged red" by source edits such as deleting the `os.path.lexists` guard.
The break actually run wrapped `derive_held_key` in memory.

Consequence: the record certifies a gate red that was never run red, and it describes a staged break that was not the one run.
The plant's own red is real: each break gave exit 1 with FAILED on its own line.
The row compares rc against 0, so a plant exiting 1 would turn the leg red, and nothing ships wrong.
A later reader would still take line 18 as proof that the leg's row matching was exercised on a failing case.

Grades: id 5 low (binding). id 6 low (binding). id 6 was confirmed as a duplicate of id 5.

Fix (both ids judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level fix):
- Reword ledger line 18 and all three section 6 arms (spec 24 lines 214-216) to say the `held-key` plant, not the leg, was observed red in-process under in-memory breaks.
- Otherwise, stage all five breaks as source edits in a scratch copy, run the leg, and record its FAIL on the `held-key` row for each.

The finders' proposals cure this instance alone: reword line 18, or stage one break in source and record the leg's FAIL beside the restored PASS.

Left-shift: dispositions `class:criterion-asserts-what-its-own-command-cannot-show` (id 5) and `class:observed-by-claim-no-arm-discharges` (id 6).
Suggested gate: a seen-red record check that refuses a line naming a gate leg red when the same ledger states no gate leg ran.

review-shape kind=diff-review round=4 intensity=full at=synth raw=6 confirmed=6 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=4 low=2 agents=9 out-tokens=42899 trigger=- shape=- efforts=- role-sha=-
review-round round=4 limit=- prior=- count=0 state=-

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-deviation-1.md:8 | high | medium | confirmed | The deviation record is new in this range (git diff --stat shows +15 lines). Spec 17 AC8 at line 335ff requires all four conditions: exit 0 under 300 s, gauges within 1.5x, worst after over worst before <= 0.90, and worst after <= 106 s. The unchanged ledger AC8 line gives set 3 as before 94.4/99.7/139.5 and after 82.1/132.0/99.9, so the ratio is 132.0/139.5 = 0.95 and the worst after is 132.0 s, which breaks both the ratio bound and the 106 s cap. The deviation's After line states the 0.80 to 0.95 ratios, then names only 'The gauge band was not met', and gives 'the worst reading of 104.7 s'. That 104.7 s is unit 20's worst after, not unit 17's. The owner prompt 17-5 put the same 104.7 s in front of the owner and named only the gauge band. So the record misstates the basis of the ruling and leaves two failed conditions unnamed. Graded medium rather than high: the deviation does print the 0.95-vs-0.90 figure, no budget or evidence row was written, and 132.0 and 139.5 s still sit under the 159 s row. The effect stays inside the records and the follow-through ask 18. | instance | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 2 | correctness | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-20-deviation-1.md:8 | medium | medium | confirmed | Deviation 20-1 is new in this range. Spec 20 AC5 (line 177ff) needs four conditions, one of them a ratio <= 0.75. The ledger AC5 line gives set 2 as max after 82.6 over max before 108.6, which is 0.76 and over the bound. The deviation names that 0.75 bound but waives only the gauge band. Set 3's before reading of 181.4 s is the worst reading on the full tree, and it is above the 159 s budget row (selftest-budgets.txt:146 'tags bundle selftest 159'). So the claim that the row 'already covers the worst reading of 104.7 s' is false. Graded medium: no row was written, the after readings all sit at or under 104.7 s, and the defect stays inside the record and ask 18. | instance | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 3 | seams | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-deviation-1.md:8 | high | medium | confirmed | In scope: the deviation file is new in this range and absent at 3d93e3e18. Deviation 17-1 line 1 says only 'gauge band unmet', and line 8 gives the worst reading as 104.7 s. The unit 17 ledger's AC8 line records set 3 with after readings of 82.1, 132.0 and 99.9 s against before readings up to 139.5 s, so the ratio is 132.0/139.5 = 0.95. Spec 17 makes AC8 red when the ratio exceeds 0.90 or the worst after exceeds 106 s. Both of those failed in set 3 and are not named as departures. The owner-waiver prompt (lines 11-13) asked only about the band and told the owner 'the worst reading on the full tree was 104.7 s'. That is false for unit 17, so the waiver rests on a misstated premise. Two parts of the finding are wrong. Ask 18 is a review-class gate ask (BACKLOG line 16) and sizes no budget. And 132.0 s is still under the 159 s budget, so the 'covers' clause holds in substance. The record is wrong and was never put to the owner, but no code or row moves, so this is medium, not high. | instance | fold-text-is-unreviewed-surface | class:fold-text-is-unreviewed-surface |
| 4 | seams | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-20-deviation-1.md:8 | medium | medium | confirmed | In scope: deviation 20-1 is new in this range. Its title and Before line name only the gauge band. Its own After line gives ratios of '0.57 to 0.76 against its 0.75 bound'. The unit 20 ledger's AC5 line gives set 2 as 0.76, and spec 20's red-when lists 'the ratio exceeds 0.75' as a separate red condition. The waiver prompt (lines 9-13) asked the owner only about the gauge band. So a ratio breach is accepted but never recorded as a departure or approved. No code is affected, so medium. | instance | fold-text-is-unreviewed-surface | class:fold-text-is-unreviewed-surface |
| 5 | verification | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-24-1-acceptance-ledger.md:18 | low | low | confirmed | Ledger line 5 says that no merge bar, suite or gate leg ran in this pass, and that the readings came from a scratch probe calling gov_tag.main in-process. Line 18 still records `tags bundle selftest` as red at 2f8d3b837, with the five breaks 'patched in memory'. The leg's run_plant_process (tag_bundle.py:393-397) starts a fresh `sys.executable gov_tag.py` subprocess, so an in-memory patch can never reach it. What was seen red was the plant, not the leg. Spec 24 lines 214-216 describe the leg row as 'staged red' by source-level breaks. The ledger is new in this range, so the defect is in scope. The impact is limited to the record: the row compares rc against 0, so a plant exiting 1 would still turn the leg red. | instance | criterion-asserts-what-its-own-command-cannot-show | class:criterion-asserts-what-its-own-command-cannot-show |
| 6 | intent | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-24-1-acceptance-ledger.md:18 | low | low | confirmed | duplicate of id=5. Same observation: ledger line 18 names the `tags bundle selftest` leg red at 2f8d3b837, but line 5 states no gate leg ran and the breaks were in-memory patches under an in-process gov_tag.main probe. The leg runs each plant as a subprocess (tag_bundle.py:393-397), so it could not have seen them. | instance | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
