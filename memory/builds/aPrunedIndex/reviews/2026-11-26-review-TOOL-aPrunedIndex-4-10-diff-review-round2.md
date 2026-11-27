**Serves:** diff-review TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-10
**Caused-by:** TOOL-aPrunedIndex-1

# aPrunedIndex — closing diff review of the round 1 fold (units 4 and 10), round 2

*2026-11-26. A Tier-2 adversarial pass over the fold since round 1's tip. Roles: finders gov-diff-reviewer,
skeptic batches gov-skeptic, synthesis gov-synthesizer.*

Reviewed: d5288a92d559cedf8b867c683190b3d74b8467ba...22c3e175d4dab01b6005a757a6aaf98332037316

Round: 2

## Verdict: CLEAN WITH FIXES

No blocker and no high stands.
By item: 0 blocker, 0 high, 2 medium, 1 low, 3 in all.
By raw confirmed finding: 0 blocker, 0 high, 3 medium, 1 low, 4 in all.
The medium item B merges ids 3 and 4.
No finding contests the fold's code: the README's cost ceiling, the `write_commit_texts` rename and the two new `gc-predates` steps all stand.
Every item sits in the records: one stale cost figure behind a budget row, one criterion owed under a CLOSED status and a commit subject claiming it timed, and two stale "owed" sentences.

The review shape is intensity full, raw 5, confirmed 4, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.80.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

## Run integrity

- Lenses 5/5 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED. The run is complete.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 3 judged sound, 0 judged UNSOUND, 1 judged INSTANCE-ONLY (it cures the cited instance and leaves its class standing), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: 2 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 15 items, each assigned to exactly one of 5 lenses (security 3, correctness 3, seams 3, verification 3, intent 3).
- By design: the caller's byDesign.
- Refuted findings shown: 1. Same-address pairs shown: 0. Twins flagged: 0.
- Dispositions: unclassed refuse; 15 class slugs handed; 226 leg names read from `tools/gate-legs.json`.

## Items

### A. MEDIUM — the `tags bundle selftest` budget and evidence rows rest on one 106 s reading the ledger's own plant timings contradict (id 1) (PINNED, 2026-11-26)

**Where:** `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-10-1-acceptance-ledger.md@0fbe85b1:18`, with `tools/run-gates/selftest-budgets.txt@d09d433d:146` (159 s) and `tools/run-gates/ceiling-evidence.txt@a8ce27b0:149` (106.0 s). (PINNED, 2026-11-26)

**What is wrong:** b06c5e1d9 wrote the 159 s budget row and the 106.0 s evidence row from one whole-leg reading of 106 s. Unit 10's ledger re-certifies both, calling 106 s "the build's final figure". (PINNED, 2026-11-26)
`tag_bundle.run_selftest` (`tools/playbook/tag_bundle.py@8a284c47:391-410`) runs every `SELFTEST_ROWS` plant serially, one `subprocess.run` each.
So the leg's wall is at least the sum of its plants.
The same ledger, on node a the same day, under the same "other sessions loading" condition, pins `released-rows` alone at 192.5 s (`@0fbe85b1:13`) and `gc-predates` at 75.9 to 112.8 s (`@0fbe85b1:18`).
Under that load the leg costs at least about 268 s. (PINNED, 2026-11-26)
That is above the 159 s budget, so `run-selftests.sh --serial` would go red OVER BUDGET. (PINNED, 2026-11-26)
The records give two answers to the leg's cost.
AC8's spread rule compares `gc-predates` only against itself, so it cannot see this.

**Consequence:** a cost verdict that is wrong under load, and a 300 s ceiling that `derive-ceilings --check` grades against 106 with more headroom than exists. No wrong result ships. (PINNED, 2026-11-26)
One sub-claim is overstated, as the skeptic noted. Plant-alone runs are not whole-leg readings, so the evidence row is not literally stale against its recorded maximum. Its weakness is that it rests on one leg reading under unstated load.

**Fix (judged SOUND by the skeptic):** Re-time `python tools/playbook/tag_bundle.py --selftest` alone at 22c3e175d, three readings on one box, with the load recorded beside each.
Rewrite the budget row by hand as the worst reading x1.5.
Rewrite the evidence row through `derive-ceilings.py --write --observed`.
Reword the AC8 ledger line so it says the plant-spread rule judges `gc-predates` only, not the leg.

**Left-shift gate:** a probe in the `tags bundle selftest` budget path: when the sum of per-plant walls pinned in a build's ledgers exceeds the leg's evidence row, the row is stale and the check reds. The class is already asked as `TOOL-aPrunedIndex-12`.

### B. MEDIUM — unit 10 is CLOSED with AC9 unmeasured, while commit 22c3e175d's subject says "AC9 timed" (ids 3, 4)

**Where:** `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-10-1-acceptance-ledger.md@0fbe85b1:19`, and `memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-10.md@95255322:3` (`Status: CLOSED · rev-2`). Finding 3 cites line 18; the AC9 line is 19.

**What is wrong:** at the tip the AC9 line still reads "owed at the close". It holds no wall time and no `blobs parsed` or `extractor runs` counts.
Commit 22c3e175d adds only the two seen-red rows to this ledger (2 insertions), yet its subject claims "AC9 timed".
Spec 10's AC9 makes this line its red condition ("the ledger holds no such line"), and that red-when holds at the tip.
The spec status was set to CLOSED in b84274b2b, inside this range.
`git grep` for `blobs parsed` or `extractor runs` under the build finds only unit 1's timings, a spec-audit review and spec 10's own AC9 text.
Round 1 confirmed the same class for unit 4's AC8.

**Consequence:** AC9 is the only criterion that measures the `instruction_units` re-parse cost the Migration section accepts on every node. Nothing records it. A close or later review that trusts the commit subject will treat that cost as measured. No code behaviour changes.

**Fix (id 3, judged SOUND by the skeptic):** Either record AC9's run on ledger line 19, or correct the record so it no longer claims AC9 was timed. The run is `gov_tag.main(["check"])` over a private index copy at b84274b2b, with its wall time and its `blobs parsed` and `extractor runs` counts.
Finding 3's fix also rewords ledger line 8 and AC6; that half is item C's defect and fix.

**Fix (id 4, judged INSTANCE-ONLY by the skeptic), the class-level fix:** add a check that refuses a spec Status of CLOSED while its unit's acceptance ledger still has any `ACn — owed` line, unless a recorded override names that AC.
Apply it to every ledger under `memory/builds/aPrunedIndex/build/`. Unit 3's ledger still carries `AC4 — owed at the close` and `AC9 — owed at the close`.
The finder's proposal cures the cited instance alone. It runs AC9 as specified, pins the reading on line 19, and holds unit 10 open until that line exists or a recorded override names AC9.

**Left-shift gate:** the class-level check above, a memory-hygiene leg that reds a CLOSED spec beside an owed ledger line. Pair it with a check that a `records(...)` commit subject claiming an AC measured touches that AC's ledger line.

### C. LOW — two ledger sentences still call the staged reds owed after lines 20-21 record them seen red (id 5)

**Where:** `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-10-1-acceptance-ledger.md@0fbe85b1:8`, and AC6 at `@0fbe85b1:16`, against the seen-red rows at `@0fbe85b1:20-21`.

**What is wrong:** 22c3e175d added the two seen-red rows (step 7 FAILED, step 8 FAILED, each exit 1 under a staged swallow). It left two earlier sentences standing.
Line 8 says "Both new arms' staged reds ... are owed at the close", and AC6 ends "The staged breaks' FAILED and exit 1 are owed at the close."
Finding 3 also reported this contradiction. It counts once, under item B.

**Consequence:** the ledger answers "were AC6's red arms observed?" both ways. A reader or derivation that reads the AC6 line alone takes the reds as never observed. The records only are affected.

**Fix (judged SOUND by the skeptic):** In the same record, reword line 8 so only the section 6 legs and AC9 stay owed. Reword AC6's last sentence to cite the two seen-red lines, each with its FAILED step and exit 1. (PINNED, 2026-11-26)

**Left-shift gate:** a ledger check that reds an `owed` sentence naming an arm for which the same ledger holds a `seen-red` row. The class is already asked as `TOOL-aPrunedIndex-13`.

## Refuted

Id 2 (verification, `tools/playbook/gov_tag.py@27cfdb44:1134`) claimed the "row counts unmoved" half of steps 7 and 8 can never fail.
The skeptic refuted it. Spec 10 lines 145-148 already disclose that the counts guard against a move and discriminate nothing, and that the refusal is the discriminating assertion. (PINNED, 2026-11-26)
It is no twin of any confirmed finding and is not counted.

review-shape kind=diff-review round=2 intensity=full at=synth raw=5 confirmed=4 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=3 low=1 agents=11 out-tokens=47122 trigger=- shape=- efforts=- role-sha=-
review-round round=2 limit=- prior=- count=0 state=-

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | seams | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-10-1-acceptance-ledger.md:18 | medium | medium | confirmed | The cited lines say what the finding claims, and this range introduced them. b06c5e1d9 wrote the 159 budget row (selftest-budgets.txt:146) and the 106.0 evidence row (ceiling-evidence.txt:149). Unit 10's ledger line 18 then re-certifies both from 106 s as 'the build's final figure'. tag_bundle.run_selftest (tools/playbook/tag_bundle.py@8a284c47:391-410) runs each SELFTEST_ROWS plant in its own subprocess.run, one after another, so the leg's wall is at least the sum of its plants. The same ledger, same node, same day, also records released-rows alone at 192.5 s (line 13) and gc-predates at 75.9-112.8 s (line 18), both taken while other sessions were loading the node. Under that load the leg costs at least 268 s, which is above the 159 budget, and run-selftests.sh --serial goes red on an OVER BUDGET. So the records give two answers to one question. The AC8 spread rule compares gc-predates against itself and cannot see this. One sub-claim is overstated: by derive-ceilings' definition the evidence row holds whole-leg readings, and plant-alone runs are not leg readings, so the row is not literally stale against the recorded maximum. The weakness is that it rests on one leg reading under unstated load. The effect is contained: a cost verdict and the ceiling's grading headroom. No wrong result ships. | sound | two-answers-to-one-question | class:two-answers-to-one-question (PINNED, 2026-11-26) |
| 2 | verification | tools/playbook/gov_tag.py@27cfdb44:1134 | medium | - | refuted | The spec already says what the finding reports as hidden. Spec 10, lines 145-148, states: "What the steps do not check: the counts guard against a move and discriminate nothing. `wt5` holds no row, so a `--gc` that wrongly read it would collect nothing in this fixture ... The refusal is the discriminating assertion." So AC4 and AC5 do not present the counts as a sweep-before-refuse guard, and the ledger rows are records under that disclosed reading. The code at tools/playbook/gov_tag.py@27cfdb44:1130-1141 agrees. No dead rows exist by step 7, because step 3 swept `dead` to 0 and step 4 swept three's version to 0. That means "sweeps before refusing" has nothing to sweep in this fixture, and the spec says as much. "Can never fail" also overstates it. `moved == counted` reads the rows of root's live version and four's conf key, so it would go red under a --gc that deleted live rows, for example one that treated a failed probe as an empty live set. It is a weak but real guard against a move, which is exactly what the spec claims for it. The missing case is a scoped limitation the spec states, not a certification of something unchecked. | instance | - | - |
| 3 | verification | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-10-1-acceptance-ledger.md:18 | medium | medium | confirmed | I read the ledger as it stands at 22c3e175d (`git show 22c3e175d:<ledger>`). Line 19 (the finding says 18, but AC8 is on 18) reads 'AC9 — owed at the close: the main loop's gov_tag.main(["check"]) over a private copy...'. It has no wall time and no `blobs parsed` or `extractor runs` counts. Commit 22c3e175d touches the ledger with only 2 insertions, the two seen-red rows on lines 20-21, yet its subject says 'AC9 timed'. Spec 10 line 258-261 has AC9 record the wall and both counts, and its red-when ('the ledger holds no such line') holds at the tip. The self-contradiction is real too: line 8 says 'Both new arms' staged reds ... are owed at the close', and AC6 (line 16) says 'The staged breaks' FAILED and exit 1 are owed at the close', while lines 20-21 record both reds as seen. Both defects were introduced in this range; the ledger is new in it. The effect stays in the records: no code is wrong, but the close could read AC9 as measured when it was not. | sound | fold-text-is-unreviewed-surface | class:fold-text-is-unreviewed-surface |
| 4 | intent | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-10-1-acceptance-ledger.md:19 | medium | medium | confirmed | Checked at 22c3e175d. Line 19 of the unit 10 acceptance ledger still reads 'AC9 — owed at the close: the main loop's gov_tag.main(["check"]) over a private copy...'. Line 8 also lists AC9 as owed. Line 3 of spec 10 reads 'Status: CLOSED · rev-2', and that status was set in b84274b2b, inside this range. Commit 22c3e175d's subject says 'AC9 timed', but its ledger diff adds only the two seen-red lines (2 insertions), and no AC9 reading appears anywhere. Grepping memory/builds/aPrunedIndex for 'blobs parsed' or 'extractor runs' finds only unit 1's timings file, a spec-audit review and spec 10's own AC9 text. AC9 at spec 10 line 258 makes this ledger line the red condition: 'Red when: the ledger holds no such line, so the re-parse that section 4's Migration accepts stands unmeasured.' The Migration section, around lines 185-190, accepts that re-parse because gov_tag.py is in instruction_units' import closure. So the defect is real and this fold introduced it. It is not a duplicate: round 1's confirmed item was unit 4's AC8, and this is unit 10's AC9. The effect is contained: it is a missing measurement plus a commit subject that claims the measurement exists. No code behaviour changes, so medium. | instance | - | new:unit-closed-with-criterion-owed |
| 5 | intent | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-10-1-acceptance-ledger.md:8 | low | low | confirmed | I read the ledger at 22c3e175d. Line 8 still says 'Both new arms' staged reds, the legs of section 6, and AC9 are owed at the close', and line 16 (AC6) still ends 'The staged breaks' FAILED and exit 1 are owed at the close.' The diff of 22c3e175d to this file adds only lines 20-21, two seen-red rows that record step 7 FAILED and step 8 FAILED, each exiting 1 under a staged swallow. Neither earlier sentence was touched, so the record now says the reds are owed in one place and observed in another. The defect came in with this fold, because both the stale lines and the new rows were written within it. It is records only and changes no behaviour, so it is low. | sound | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
