**Serves:** spec-audit TOOL-aPrunedIndex-24@rev-1
**Caused-by:** TOOL-aPrunedIndex-24

# Tier-2 spec audit: TOOL-aPrunedIndex-24, round 1

Provenance: synthesis by gov-synthesizer from the gov-spec-reviewer finders and the gov-skeptic batches. Preset unit-spec.

Reviewed: memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md@474296c541475ee61cf8bddf4f2b2d25240cc1b9
ROUND 1

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs. Six items need spec edits before the build: two medium and four low.

Review shape: intensity full, raw 8, confirmed 8, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| coherence | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |

The adjudicated tally is 6 items: 0 blocker, 0 high, 2 medium and 4 low. By raw confirmed finding it is 8: 0 blocker, 0 high, 2 medium (ids 6 and 7) and 6 low (ids 1, 2, 3, 4, 5 and 8).

Run integrity:
- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 4/4 returned, 0 died.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 7 judged sound, 1 judged UNSOUND (id 4), 0 instance-only, 0 none proposed, 0 not judged.
- Severity: 0 ungraded by the skeptic, 2 re-graded by the skeptic (ids 1 and 3, medium to low).
- Unverified: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-spec-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 8 spec documents were supplied as `specs`, as sibling context.
- Checklist: 24 items across 5 lenses (coherence 5, grounding 5, reuse 5, blast-radius 5, failure-envelope 4).
- By design: none supplied. Move check: no checked subject moved.
- Refuted findings shown: 0. Same-address pairs shown: 0. Twin flags: none.
- Dispositions: unclassed refuse. 23 class slugs were handed, and 226 leg names were read from tools/gate-legs.json.

Every count above is zero where it should be, so this run is complete.

## Items

### 1. MEDIUM: S3 names no git verb for its two reads, so the stored-failure spawn check can pass on an unkeyed read (ids 6, 1)

- **Where:** spec section 2 S3, and the section 4 paragraph "The all-zero `^{tree}` read matches HELD_ID_RE, so it is a keyed read".
- **What is wrong:** S3 gives the reads as `ti.read_git` of `"0" * 40 + "^{tree}"` and of `<id>^{tree}`, with no verb. `derive_held_key` (tools/playbook/gov_tag.py@6c0431dd:720) returns None unless args[0] is `rev-parse` or `ls-tree`. Read word for word, the failing read is unkeyed and spawns twice whether or not `read_held_git` stores failures. The "failures asked again" check would then print `held` under the very break it guards. Section 4 says the read is keyed, but S3 does not supply the verb that makes it so.
- **Consequence:** contained. Built literally, the held half (`git <id>^{tree}`) raises TagError, which pushes the builder to add a verb. AC2's stored-failure break, a staged-red arm in section 6, would also catch an unkeyed failing read at the close. The cost is a lost build iteration and a misleading spec line.
- **Grades:** id 6 medium (binding). Id 1 low (binding; re-graded by the skeptic from medium because the build would surface the gap). The item takes medium.
- **Fix (judged SOUND by the skeptic for both ids):** In S3, spell both reads with their verb: `ti.read_git(root, "rev-parse", "0" * 40 + "^{tree}")` and `ti.read_git(root, "rev-parse", <id> + "^{tree}")`. Add to S3 that the plant asserts `derive_held_key(root, ("rev-parse", "0"*40 + "^{tree}")) is not None` before it counts spawns. Keep AC2's stored-failure break as the probe that sees the spawns line go red.
- **Left-shift gate:** a spec-tokens-style check that every `read_git` call quoted in a spec names a verb as its first argument. Until then, add a checklist line: "a spec that says a read is keyed shows the args the key derivation reads".

### 2. MEDIUM: AC5 grades one selftest wall against 159 s with no load condition (id 7) (PINNED, 2026-11-26)

- **Where:** spec section 5 AC5.
- **What is wrong:** AC5 is one `tag_bundle.py --selftest` reading, red when the wall reaches 159 s. It names no load condition, no gauge, and no retake or deviation route. Unit 24 drops the `git --version` gauge band and retakes that spec 20's AC5 carried. (PINNED, 2026-11-26)
- **Consequence:** contained to one close criterion. The ledgers show load alone has pushed this leg past 159 s: unit 10 recorded 521 s, unit 20 recorded before-walls of 121.5, 104.0 and 111.8 s, and its gauge swung 3 to 10 times. A correct build can go red on load. A quiet node can also turn it green without measuring the 15th plant's real cost. (PINNED, 2026-11-26)
- **Grades:** id 7 medium (binding).
- **Fix (judged SOUND by the skeptic):** Name a load condition in AC5. Either take the reading alone with a load gauge recorded beside it (for example the mean of 20 `git --version` spawns, as unit 20 used), or state that a wall at or over 159 s with the gauge outside a stated band is a re-read, not a red. Record the gauge in the ledger with the wall. (PINNED, 2026-11-26)
- **Left-shift gate:** add a checklist line: "a wall-clock criterion names its load gauge, its band and its retake route". This class has now cost units 17 and 20 an owner waiver each.

### 3. LOW: S4's flags check passes vacuously when a HELD_FLAGS member is removed, and section 1 overclaims (id 8)

- **Where:** spec section 2 S4, section 1 Goal, and section 2 S6.
- **What is wrong:** S4 loops over whatever HELD_FLAGS holds, so a removed member is never iterated and an empty set still passes. The S6 selftest row matches only the plant's last line (tools/playbook/tag_bundle.py@212497e0:411 checks `want in out`), so the pinned `flags read:` line is never graded on the bar. AC3 pins the set only as a one-time close probe. Section 1's claim that the plant reds when the members of HELD_FLAGS break does not cover a removal.
- **Consequence:** removing `-r` or `-z` leaves the plant at exit 0 and the selftest green. Held reads with those flags go unkeyed and run slower. They never return wrong answers.
- **Grades:** id 8 low (binding).
- **Fix (judged SOUND by the skeptic):** Either make the S4 check also fail when `sorted(HELD_FLAGS) != ['--full-tree', '--name-only', '-r', '-z']`, or make the S6 row match the full flags line. Otherwise, narrow section 1 and add "a member removed from HELD_FLAGS" to "What it cannot see".
- **Left-shift gate:** class fixture-passes-by-finding-nothing. Add a checklist line: "a loop-over-members check also pins the member list".

### 4. LOW: The S5 comment edit and S1's "no top-level function" clause have no criterion, though S5 claims AC1 and AC3 observe it (ids 2, 4)

- **Where:** spec section 2 S5 and S1, against section 5 AC1 to AC5.
- **What is wrong:** S5 says the rewritten comment is "Observed by AC1 and AC3". AC1 reads only the plant's output lines and exit code. AC3 reads only `sorted(gov_tag.HELD_FLAGS)` and the keys vector. Nothing reads the comment. S1's "defining no top-level function" is likewise checked by no AC.
- **Consequence:** a build can leave `#: S1: ... and every flag it may carry` (tools/playbook/gov_tag.py@6c0431dd:444) unchanged, or add a top-level helper, and stay green. That comment is the only prose that explains why the separator rule belongs to the `--` branch. If it stays stale, the next change could add `--` back. Behaviour does not change.
- **Grades:** id 2 low (binding). Id 4 low (binding).
- **Fix:** For id 2, the fix was judged SOUND by the skeptic: add a line to AC3 that prints the comment line(s) directly above `HELD_FLAGS`, requires the words "before its paths", and is red while the only comment is the shared `#: S1:` line. For S1, either add an AC4 check that `memory/map/generated/symbols.json` is absent from the build diff, or drop the clause. For id 4, the finder's fix was REJECTED by the skeptic, and the skeptic's corrected fix applies: in S5, name the comment edit as observed by the diff review alone, or add to AC3 a check that the `#:` comment line above `HELD_ID_RE` contains "before its paths", for example `grep -n -B2 '^HELD_FLAGS' tools/playbook/gov_tag.py`, red when no printed line contains that phrase. Any such check must read the comment where item 5's rewording places it.
- **Left-shift gate:** class observed-by-claim-no-arm-discharges. A spec check could verify that each "Observed by ACn" claim names something that AC's command prints.

### 5. LOW: S5 rewrites "the comment above HELD_FLAGS", but that comment is shared with HELD_ID_RE (id 5)

- **Where:** spec section 2 S5, the comment clause.
- **What is wrong:** HELD_FLAGS has no comment of its own. The only `#:` line (tools/playbook/gov_tag.py@6c0431dd:444) sits above HELD_ID_RE and describes both constants. A rewrite worded as S5 asks drops or narrows the HELD_ID_RE description.
- **Consequence:** cosmetic. The next reader of the regex loses the note that it names one full object id, alone or naming its tree.
- **Grades:** id 5 low (binding).
- **Fix (judged SOUND by the skeptic):** Reword S5 to either (a) give HELD_FLAGS its own `#:` line and keep the id sentence above HELD_ID_RE, or (b) edit only the flag clause of the shared line, changing "and every flag it may carry" to "and every flag it may carry before its paths". AC3 or the ledger can then quote the resulting lines.
- **Left-shift gate:** add a checklist line: "a spec that rewrites a comment quotes its current text and the constants it covers".

### 6. LOW: The pinned flags line depends on frozenset iteration order (id 3)

- **Where:** spec section 4 (the third printed line), with S4 and AC1.
- **What is wrong:** AC1 requires the plant to print exactly `flags read: --full-tree --name-only -r -z; held`. HELD_FLAGS is a frozenset of str, and str hashing is randomized per process. S4 never says the members are printed sorted. Under PYTHONHASHSEED 1 to 3 the skeptic saw three different orders.
- **Consequence:** display order only. AC1's reading and any ledger quote of the line depend on the hash seed. The selftest row grades only the last line, so the bar is unaffected.
- **Grades:** id 3 low (binding; re-graded by the skeptic from medium).
- **Fix (judged SOUND by the skeptic):** S4 and section 4 say the check prints `sorted(HELD_FLAGS)`, matching AC3's probe. Alternatively, AC1 compares the flags line as a set of members.
- **Left-shift gate:** add a checklist line: "printed output pinned by a criterion never iterates an unordered collection unsorted".

review-shape kind=spec-audit round=1 intensity=full at=synth raw=8 confirmed=8 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=2 low=6 agents=10 out-tokens=81814 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md:section 2 S3 (and section 4 Design, the all-zero ^{tree} paragraph) | medium | low | confirmed | True as stated. The pinned blob 474296c5, S3 at line 35, says `ti.read_git` of `"0" * 40 + "^{tree}"` and of `<id>^{tree}` and names no git verb. tools/playbook/gov_tag.py@6c0431dd:720 returns None unless args[0] is rev-parse or ls-tree. tag_index.read_git (line 614) passes *args straight to read_git_stdout, which runs `git -C repo *args` and adds no verb. I re-ran the probe and it printed `bare None` and `rev-parse True`. The consequence is narrower than the finding claims. Read literally, S3's held half (`read_git(root, "<id>^{tree}")`) would run `git <id>^{tree}` as a git subcommand. That raises TagError instead of 'returning one answer', so a literal build goes red on its own held half and the builder is pushed to add a verb. AC2's stored-failure break, which is also named as a staged-red arm in section 6 line 179, would catch an unkeyed failing read when the unit closes. Section 4 line 86 already states the intent that the read is keyed. So this is an underspecification the build would surface, not a design that ships a check certifying nothing. Graded low. | sound | fixture-passes-by-finding-nothing | class:fixture-passes-by-finding-nothing |
| 2 | coherence | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md:section 2 S5 and S1 against section 5 AC1-AC5 | low | low | confirmed | True. gov_tag.py lines 444-446 show the shared `#: S1: ... and every flag it may carry` comment above HELD_ID_RE, and no comment directly above HELD_FLAGS. S5 (spec line 44) commits to a comment above HELD_FLAGS that names 'the flags a held read may carry before its paths'. S1 (line 27) says the plant defines 'no top-level function'. None of AC1-AC5 (lines 131-166) checks either commitment: AC3 prints only sorted(HELD_FLAGS) and the vector, and AC4 lists symbols.json among neither the named nor the excluded files. A build could leave the stale comment and stay green. The effect is a comment plus an unpinned structural clause with no behavioural consequence, so low. | sound | - | class:observed-by-claim-no-arm-discharges |
| 3 | grounding | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md:section 4 (the third printed line) with S4 and AC1 | medium | low | confirmed | I read spec blob 474296c5. Line 79 shows the flags line as `--full-tree --name-only -r -z`, which is sorted order, and AC1 (lines 131-133) requires the plant to print 'the four lines section 4 shows'. S4 (lines 38-41) says the check 'reads every member of HELD_FLAGS' but never says the members are printed sorted. tools/playbook/gov_tag.py@6c0431dd:446 defines HELD_FLAGS as a frozenset. Running PYTHONHASHSEED=1..3 with a join over the four-member frozenset printed '-r --full-tree -z --name-only', '--name-only -z -r --full-tree' and '--name-only -r -z --full-tree', so a plant that prints by iterating the set is order-unstable. tools/playbook/tag_bundle.py@212497e0:402-416 grades each row by exit and line, so the selftest is unaffected. The effect is limited to how AC1 is read and how the ledger quotes the line, which is display order with no behavioural effect, so I grade it low. | sound | - | new:pinned-output-iterates-an-unordered-set |
| 4 | reuse | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md:section 2 S5 (with section 5 AC1 and AC3) | low | low | confirmed | S5 (lines 42-45) claims the comment edit is 'Observed by AC1 and AC3'. AC1 reads only the plant's output lines and exit code. AC3 (lines 146-148) reads only `sorted(gov_tag.HELD_FLAGS)` and the keys vector. Neither criterion reads the comment. tools/playbook/gov_tag.py@6c0431dd:444 still reads `#: S1: ... and every flag it may carry`, so a build that leaves it unchanged passes both criteria. The defect is limited to a comment, so I grade it low. On the fix: the grep example is wrong for the current layout. Line 444's comment sits above HELD_ID_RE (445), not directly above HELD_FLAGS (446), so `grep -B1 '^HELD_FLAGS'` prints the HELD_ID_RE line and would show Red on a correct build that keeps the comment where it is. The fix's first option, naming the comment edit as observed by the diff review alone, is sound. | unsound | observed-by-claim-no-arm-discharges | class:observed-by-claim-no-arm-discharges |
| 5 | blast-radius | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md:section 2 S5 (the comment clause) | low | low | confirmed | Re-read tools/playbook/gov_tag.py lines 443-446. The only `#:` line, `#: S1: the one full object id a held read names, alone or naming its tree, and every flag it may carry`, sits above HELD_ID_RE, and HELD_FLAGS on the next line has no comment of its own. Spec blob 474296c line 44 (S5) says to rewrite 'the comment above `HELD_FLAGS`' so that it says the set holds the flags a held read may carry before its paths. Followed literally, that rewrite drops or narrows the description of HELD_ID_RE. The effect is only on a comment, so the grade is low. | sound | - | new:shared-comment-rewritten-for-one-constant |
| 6 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md:section 2 S3 (and section 4, "The all-zero `^{tree}` read matches HELD_ID_RE, so it is a keyed read") | medium | medium | confirmed | Spec blob 474296c line 35 (S3) gives both reads as `ti.read_git` of `"0" * 40 + "^{tree}"` and of `<id>^{tree}`, with no git verb. Section 4 (line 86) calls the first one 'a keyed read'. I re-ran the probe and it printed `None True`: with no verb the read gets no key, and with `rev-parse` it gets one. gov_tag.py line 720 returns None unless args[0] is rev-parse or ls-tree. So a read built word for word spawns twice whether or not failures are stored, and the spawns check passes vacuously. AC2's stored-failure break, which must take the plant to 1, would catch this during the build, so the effect is contained: medium. | sound | - | class:fixture-passes-by-finding-nothing |
| 7 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md:section 5 AC5 | medium | medium | confirmed | Spec blob 474296c lines 159-166: AC5 is one `tag_bundle.py --selftest` reading graded against the pinned 159 s, and it is red when the wall reaches 159 s. It names no load condition and no gauge, and gives no retake or deviation route. The cited evidence reproduces. The unit-10 ledger line 23 records a 521 s wall with other sessions' bars running. The unit-20 ledger line 16 records AC5 RED with before-walls of 121.5, 104.0 and 111.8 s. Unit-20 deviation-1 line 10 says the gauge swung 3 to 10 times. Spec 20's own AC5 (lines 180-197) did carry a `git --version` gauge band with retakes, and unit 24 drops that. The ledgers show load alone has pushed this leg past 159 s, so built as written AC5 can go red with no defect in the code. The effect is contained to one close criterion, so the grade is medium. | sound | - | new:wall-criterion-names-no-load-condition (PINNED, 2026-11-26) |
| 8 | failure-envelope | memory/builds/aPrunedIndex/spec/2026-11-26-spec-TOOL-aPrunedIndex-24.md:section 2 S4 / section 1 Goal / section 2 S6 | low | low | confirmed | S4 (line 38) loops over whatever HELD_FLAGS holds, and a member that is gone is never iterated, so the check holds vacuously. In tag_bundle.py run_selftest (line 411) a row passes on `p.returncode == int(rc) and want in out`, where `want` is only the row text S6 gives, which is the plant's last line. The `flags read:` line is therefore not matched against its pinned members, and only the plant's exit code reflects it. AC3 pins the set, but only as a one-time close probe, and no arm on the bar does. The Alternatives section says the liveness read 'catches both kinds that matter here' (an added dead member and a shadowed one). Nothing excludes removal as a non-goal, though, and section 1 claims the plant reds when 'the members of HELD_FLAGS' break. The overclaim is real. The consequence is only uncached reads, meaning slower runs and never wrong answers, so the grade is low. | sound | - | class:fixture-passes-by-finding-nothing |
