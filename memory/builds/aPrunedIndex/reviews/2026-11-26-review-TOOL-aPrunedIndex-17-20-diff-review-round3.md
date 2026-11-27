**Serves:** diff-review TOOL-aPrunedIndex-1 TOOL-aPrunedIndex-2 TOOL-aPrunedIndex-3 TOOL-aPrunedIndex-4 TOOL-aPrunedIndex-10 TOOL-aPrunedIndex-17 TOOL-aPrunedIndex-20

# aPrunedIndex — closing diff review of the round 2 fold (units 17 and 20), round 3

*2026-11-26. A Tier-2 adversarial pass over the fold since round 2's tip. Roles: finders gov-diff-reviewer,
skeptic batches gov-skeptic, synthesis gov-synthesizer.*

Reviewed: 22c3e175d4dab01b6005a757a6aaf98332037316...3d93e3e18cf57b9ee43f300c93c3171a37d294be

Round: 3

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs. One medium and four lows need fixing: five items holding eight confirmed findings.
Nothing in the code changes behaviour on any current path.
The medium is a rule in unit 17's hold that no bar arm can turn red.

Subjects: unit 17 (commit c39996768) adds `set_git_held()`, `derive_held_key` and `read_held_git` to
`tools/playbook/gov_tag.py`, holding allow-listed git reads for the five `HELD_PLANTS`.
Unit 20 (commit 8b6d80c17) runs `tag_bundle.py#run_selftest`'s plants on a 4-worker pool, graded in `SELFTEST_ROWS` order.
The rest of the range is records: spec revisions, audits, ledgers, the owner's scope approval, and asks 21 to 23.

Review shape: intensity full, raw 10, confirmed 8, refuted 2, merged 0, unverified 0 (0 uncertain), precision 0.80.
Adjudicated tally by item: 5 items, 0 blocker, 0 high, 1 medium, 4 low.
Adjudicated tally by raw confirmed finding: 8 findings, 0 blocker, 0 high, 1 medium, 7 low.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 3 | 2 | 1 | 0 | 0 | 0 | 0.67 |

## Run integrity

- Lenses: 5/5 returned, 0 DIED. Skeptic batches: 5/5 returned, 0 DIED.
- 0 contradictory verdicts were demoted to unverified.
- 0 orphaned duplicate refutations were demoted to unverified.
- 0 duplicate refutations were counted as merged confirmations.
- 0 spurious verdicts were discarded, and there were 0 duplicates.
- Fixes on confirmed findings: 6 judged sound, 0 UNSOUND, 2 INSTANCE-ONLY (each cures the cited instance and leaves its class standing), 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 2 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 13 items, each assigned to one lens: security 3, correctness 3, seams 3, verification 2, intent 2.
- By design: the caller's byDesign.
- Shown: 2 refuted findings and 1 same-address pair.
- Dispositions: unclassed refuse; 13 class slugs handed; 226 leg names read from `tools/gate-legs.json`.

Every counter above is zero where it would mark a loss, so this run is complete.
The security lens's zero is evidence from a lens that returned, not a gap.

## Items

### 1. MEDIUM — the hold rule's `.git`-exists guard has no arm that can fail (id 5)

- **Where:** `tools/playbook/gov_tag.py@6c0431dd:719`, the `lexists` guard in `derive_held_key`.
- **What is wrong:** No gate can fail when the guard is removed.
  With it deleted, all five held plants still exit 0.
  The guard's false branch runs zero times across them, because no plant reads `--git-common-dir` or `--show-toplevel` where no `.git` entry stands.
  Only AC2's one-time `python -c` probe has ever checked it, and that probe is not on the bar.
  A widened allow-list is caught only in part: holding every `rev-parse` and `ls-tree` turned released-cost red and left dead-versions and named-probe green.
- **Consequence:** A later edit could drop the guard with `tags bundle selftest` green.
  The effect stays inside the selftest plants, because holding applies only there; this is why it is medium.
- **Fix (judged SOUND by the skeptic):** Make AC2's eleven-read table an arm the bar runs.
  One way is a `held-key` plant or a row in tag_bundle's selftest that calls `derive_held_key` and compares the vector.
  Observe it red twice: once with the `lexists` condition deleted in memory, and once with `HEAD` added to the accepted revisions.
- **Left-shift gate:** Put the new arm under `tags bundle selftest`, and have `harness arms (fail branches armed or pinned)` count the guard's false branch.
- **Grade:** medium, the binding grade.

### 2. LOW — unit 17's ledger preamble still calls AC6 and AC8 owed (ids 2, 7, 9)

- **Where:** `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-1-acceptance-ledger.md@c669ed36:8`, lines 8-9.
- **What is wrong:** The preamble says "The five arms' staged reds (AC6), AC8 and the legs of section 7 are owed at the close."
  Commit 3d93e3e18 recorded AC6 (29 breaks re-staged at 8b6d80c17, each exiting 1) at line 17, AC8 RED at line 19, and the seen-red line at line 21, and left the preamble as it was.
  This is the stale-owed-sentence defect that round 2 fixed in the unit 1-4 and unit 10 ledgers, written again into a ledger that first appears in this range.
- **Consequence:** The ledger gives two answers to whether AC6 and AC8 were observed.
  The next close pass may re-run the staged breaks, or may distrust the recorded lines.
  Only the records are affected.
- **Fix:** For id 2 the skeptic judged the finder's fix INSTANCE-ONLY.
  For ids 7 and 9 the skeptic judged the fix SOUND.
  The fix is the skeptic's class-level fix for id 2, which includes the sound fixes:
  - Amend lines 8-9 the way round 2 amended the older ledgers. Say only the section 7 legs are owed at the close, and only if they still are. Say the main loop recorded AC6's staged reds and AC8 at 8b6d80c17, on the AC6, AC8 and seen-red lines below. (PINNED, 2026-11-26)
  - Amend unit 20's AC4 'owed' sentence too (item 3).
  - Add round 2's class check. This is a memory-hygiene leg that reds an acceptance ledger in either of two cases: its 'owed' sentence names an AC that the same ledger records as observed, or its unit is CLOSED. A recorded override that names the AC exempts it.

  The finder's own proposal for id 2 (amend lines 8-9 only) cures the cited instance alone.
- **Left-shift gate:** The `memory hygiene` leg check above.
- **Grade:** low for all three ids, their binding grade.

### 3. LOW — unit 20's AC4 diff read is still owed on a CLOSED unit (ids 1, 10)

- **Where:** `memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-20-1-acceptance-ledger.md@e1b3f038:15`.
- **What is wrong:** AC4 still says "The build commit's `git diff --name-only` is owed a read at the close against the cut-line list."
  No record in the range carries that read out.
  Even so, the README marks TOOL-aPrunedIndex-20 CLOSED, and spec 20 says this rule is 'Observed by AC4'.
  Both skeptics re-ran the diff (`8b6d80c17^ 8b6d80c17`, and `5b44ad17b 8b6d80c17`). It names memory records, `symbols.json` and `tools/playbook/tag_bundle.py`, and no cut-line file. The claim holds today.
- **Consequence:** A closed unit's record certifies a check nobody recorded.
  This is the same 'criterion claimed but owed' shape that round 2 fixed for unit 10's AC9.
  Only the records are affected.
- **Fix:** For id 1 the skeptic judged the finder's fix INSTANCE-ONLY.
  For id 10 the skeptic judged the fix SOUND.
  The fix is the skeptic's class-level fix for id 1:
  - Record the observed diff on every ledger 'owed at the close' line whose unit is CLOSED. That covers unit 20's AC4 and the section 7 legs in unit 17's preamble, lines 8-9. (PINNED, 2026-11-26)
  - On the AC4 line, record the `git diff --name-only 5b44ad17b 8b6d80c17` output. State that none of tag_index.py, gov_tag.py, gate-legs.json, positional.py, position.py or routed_commits.py appears in it. Then remove the 'owed' sentence.
  - Add the memory-hygiene leg that round 2 proposed. It reds a CLOSED spec whose ledger still holds an unresolved 'owed' sentence, unless a recorded override names that AC.

  The finder's own proposal for id 1 (record the output on the AC4 line and drop the sentence) cures the cited instance alone.
- **Left-shift gate:** The `memory hygiene` leg check above. It is the same check as item 2's, so build it once.
- **Grade:** low for both ids, their binding grade.

### 4. LOW — the hold's never-store-a-failure rule has no arm that can fail (id 6)

- **Where:** `tools/playbook/gov_tag.py@6c0431dd:742`, the store in `read_held_git`.
- **What is wrong:** `read_held_git` stores only a successful answer, and no plant tests that.
  A variant that stores and replays exceptions passes gc-predates, the one plant whose reads fail, with zero stored-failure replays.
  So S2's 'a failed read asks git again' rests on AC3's one-time probe alone.
- **Consequence:** An edit that caches failures, for example `functools.lru_cache` over the reader, would pass the bar.
  The defect is latent and confined to the selftest plants.
- **Fix (judged SOUND by the skeptic):** Add an arm that the bar runs. It reads the all-zero `^{tree}` twice inside `set_git_held()` and asserts two spawns, which makes AC3's probe permanent.
  Stage it red with a variant that stores the exception.
- **Left-shift gate:** Put the arm under `tags bundle selftest`, beside item 1's.
- **Twin:** Refuted id 3 (seams, the same address) describes this defect. Its skeptic refuted it as an untested-by-design rule with no current wrong result. It is noted here only as a twin. It is not reinstated or counted.
- **Grade:** low, the binding grade.

### 5. LOW — `"--"` in `HELD_FLAGS` is dead (id 4)

- **Where:** `tools/playbook/gov_tag.py@6c0431dd:446`.
- **What is wrong:** `derive_held_key` handles `arg == "--"` in its own branch (line 726) before the `arg not in HELD_FLAGS` test (line 730).
  Every later argument is skipped once `paths` is set.
  So the set's `"--"` member is never consulted, even though the comment at line 444 ("every flag it may carry") says the set governs it.
- **Consequence:** Behaviour is unchanged.
  The next edit is misled: removing `"--"` from the set, to forbid path-limited holds, would change nothing.
- **Fix (judged SOUND by the skeptic):** Remove `"--"` from `HELD_FLAGS`, leaving `{"--full-tree", "--name-only", "-r", "-z"}`.
  Alternatively, drop the dedicated branch and let membership gate it.
  Either way, keep one owner of the separator rule.
- **Left-shift gate:** A unit-level check in item 1's `held-key` arm. It would assert that every `HELD_FLAGS` member changes `derive_held_key`'s answer when removed.
- **Grade:** low, the binding grade.

## Refuted

- id 3 (seams, `tools/playbook/gov_tag.py@6c0431dd:742`): refuted. It is a twin of confirmed id 6 (item 4).
- id 8 (intent, unit 17 ledger line 17, the AC6 break count): refuted. The ledger's 29 matches the seen-red lines once unit 3's "before and after" is counted as two breaks. It is not a twin of any confirmed finding.

review-shape kind=diff-review round=3 intensity=full at=synth raw=10 confirmed=8 refuted=2 merged=0 unverified=0 blocker=0 high=0 medium=1 low=7 agents=11 out-tokens=61878 trigger=- shape=- efforts=- role-sha=-
review-round round=3 limit=- prior=- count=0 state=-

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-20-1-acceptance-ledger.md:15 | low | low | confirmed | At 3d93e3e18 the unit 20 acceptance ledger, line 15, still says the build commit's `git diff --name-only` 'is owed a read at the close against the cut-line list'. I found no other record in aPrunedIndex at the tip that carries that read. The README at line 72 marks TOOL-aPrunedIndex-20 CLOSED, and spec 20 line 41 says 'Observed by AC4', with line 173 saying it is red when the diff touches a cut-line file. So the unit is recorded closed while half of AC4 is still unobserved. I re-ran `git diff --name-only 8b6d80c17^ 8b6d80c17`. It lists memory/LIVE.md, the aPrunedIndex README, the ledger, spec 20, symbols.json and tools/playbook/tag_bundle.py, and none of the cut-line files, so the claim itself is true. This is a records defect only, so it is low. | instance | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 2 | correctness | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-1-acceptance-ledger.md:8 | low | low | confirmed | The unit 17 ledger is new in this range; it did not exist at 22c3e175d. At 3d93e3e18 its lines 8-9 say 'The five arms' staged reds (AC6), AC8 and the legs of section 7 are owed at the close'. The same file then records AC6 re-staged at 8b6d80c17 with 29 breaks each exiting 1, AC8 as RED with three timed sets, and a seen-red line. That gives two answers about AC6 and AC8. It is a new instance in a new ledger, not a re-raise of round 2's fixed lines in units 1-4. Its effect is limited to the records, so it is low. | instance | - | class:two-answers-to-one-question |
| 3 | seams | tools/playbook/gov_tag.py@6c0431dd:742 | medium | - | refuted | What the finder says is accurate: tools/playbook/gov_tag.py@6c0431dd:735-743 stores nothing when a read raises, because the assignment at line 742 never runs. No file outside memory/ refers to derive_held_key, read_held_git, set_git_held or HELD_PLANTS (I grepped for them), so only the probes AC2 to AC4 check these rules. But that is how spec 17 chose to test them. Its testing line (spec line 253, 'AC2 and AC3 probe the rule and the store') names those probes as the observation for S1 to S3. The diff has no defect that is reachable today. The impact the finder describes only follows if a future change starts caching failures or edits HELD_PLANTS. A regression arm that does not exist yet is not a defect this diff introduced or made reachable. The finding is graded medium and shows no wrong result on any current path, so I refute it. | sound | rule-stated-with-no-check-that-fails | - |
| 4 | seams | tools/playbook/gov_tag.py@6c0431dd:446 | low | low | confirmed | In derive_held_key (tools/playbook/gov_tag.py@6c0431dd:723-731), the branch `arg == "--"` at line 726 runs before the `arg not in HELD_FLAGS` test at line 730. After the separator, `paths` is True and every later argument is skipped by the `continue` at line 725. So the HELD_FLAGS lookup never sees the "--" member defined at line 446, and the comment at line 444 ('every flag it may carry') suggests the set governs it. Unit 17 introduced both lines in this diff. Behaviour does not change; the only harm is that it misleads the next edit. | sound | - | class:guard-above-a-fold-makes-its-fallback-dead |
| 5 | verification | tools/playbook/gov_tag.py@6c0431dd:719 | medium | medium | confirmed | derive_held_key is new in this diff. It is absent at 22c3e175d, and its lexists guard is at tools/playbook/gov_tag.py@6c0431dd:719. A grep of tools/ finds no caller of derive_held_key, read_held_git or set_git_held outside gov_tag.py, so no tag_bundle arm or gate leg probes the rule. I instrumented derive_held_key and ran gov_tag.main(['--fixture','--plant',p]) for each of the five HELD_PLANTS. Every one exited 0, and the guard's false branch ran 0 times: no plant ever reads --git-common-dir or --show-toplevel where no .git entry stands. Removing the guard therefore cannot turn any bar row red. Spec 17 section 5 rests 'testing' on AC2's one-time python -c probe, and section 7 adds arms for AC6 only. The finder's 'stale answer ships with the bar green' overstates it, because holding applies only inside selftest plants. That keeps the effect contained, so medium rather than high. | sound | - | class:rule-stated-with-no-check-that-fails |
| 6 | verification | tools/playbook/gov_tag.py@6c0431dd:742 | low | low | confirmed | read_held_git (tools/playbook/gov_tag.py@6c0431dd:735-744) stores only a successful answer, but nothing on the bar exercises that. I wrapped it to count a keyed read that raised and was asked again within the same plant. Across all five held plants that count was 0, and all exited 0. A variant that caches exceptions would therefore pass tags bundle selftest. S2's rule is observed only by AC3's one-time probe, and no arm outside gov_tag.py references set_git_held. The effect is latent and confined to the selftest plants, so low. | sound | - | class:rule-stated-with-no-check-that-fails |
| 7 | verification | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-1-acceptance-ledger.md:8 | low | low | confirmed | At 3d93e3e18, lines 8-9 of the unit-17 ledger still say 'The five arms' staged reds (AC6), AC8 and the legs of section 7 are owed at the close.' The same commit recorded AC6 (line 17), AC8 RED (line 19) and the seen-red line (line 21) lower in that file and left the preamble as it was. The ledger is new in this range (it does not exist at 22c3e175d), so the defect is in scope. It is not a duplicate of round 2's fix, which was to unit 10's ledger. The effect is contradictory record prose and nothing more, so the grade is low. | sound | amendment-leaves-its-other-half-standing | class:amendment-leaves-its-other-half-standing |
| 8 | intent | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-1-acceptance-ledger.md:17 | medium | - | refuted | The finder miscounted unit 3's seen-red line. That line (unit-3 ledger line 23) says 'the path hashed before and after the bytes are read', which covers two breaks. Unit 3's spec, at its released-rows arm, lists them separately: 'with the path hashed before the bytes are read, with the path hashed after'. That makes 9 released-rows breaks, so units 1 to 4 total 6+5+9+2+5 = 27. Spec 17 AC6 itself notes 'The brief counts 27 for the first group', and with unit 10's 2 the total is 29. The ledger's 9 and 29 match what the seen-red lines name, and spec 17 AC6 tells the main loop to record the count it staged. The spec fixture's 26 is the miscount, not the ledger's 29. | unsound | fold-text-is-unreviewed-surface | - |
| 9 | intent | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-17-1-acceptance-ledger.md:8 | low | low | confirmed | At 3d93e3e18, lines 8-9 of the unit 17 ledger (blob c669ed369) still say "The five arms' staged reds (AC6), AC8 and the legs of section 7 are owed at the close." The same file then records AC6 as re-staged at 8b6d80c17, AC8 as RED with three timed sets, and a seen-red line for the 29 breaks. Spec 17 is marked Status CLOSED. This ledger first appears in this fold (+21 lines in the diff stat), so the defect is in scope. The unit 1, 2, 3 and 4 ledgers each carry round 2's amendment, "The staged reds were observed afterwards at <sha>, as the seen-red lines below record." This ledger does not. The only effect is on the records, which mislead the reader, so the grade is low. | sound | fold-text-is-unreviewed-surface | class:fold-text-is-unreviewed-surface |
| 10 | intent | memory/builds/aPrunedIndex/build/2026-11-26-build-TOOL-aPrunedIndex-20-1-acceptance-ledger.md:15 | low | low | confirmed | At 3d93e3e18, line 15 of the unit 20 ledger (blob e1b3f038) still says "The build commit's `git diff --name-only` is owed a read at the close against the cut-line list." Spec 20 is marked Status CLOSED · rev-2, and its AC4 includes that diff check. I re-ran `git diff --name-only 5b44ad17b 8b6d80c17`. It printed memory/LIVE.md, the build README, the unit 20 ledger, the unit 20 spec, symbols.json and tools/playbook/tag_bundle.py, and no cut-line file. The criterion therefore holds, but the ledger leaves it owed on a unit that is closed. The ledger is new in this fold, so the defect is in scope. Only the records are affected, so the grade is low. | sound | fold-text-is-unreviewed-surface | class:fold-text-is-unreviewed-surface |
