**Serves:** diff-review TOOL-dBoundRoles-95

# dBoundRoles — Tier-2 SECURITY diff review of TOOL-dBoundRoles-95, round 1

*2026-11-25. The subject is TOOL-dBoundRoles-95 alone, the unit the owner ordered to close TOOL-dBoundRoles-23 F6.*
*The property under review: where the landed policy file leaves `policy-file.guard` at `owner-only`, a run's own write of `.governance/policy.toml` never passes as the owner's.*
*Roles: finders gov-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.*
*Intent: 1 spec document supplied as `specs`, beside the range's commit messages.*
*Checklist: 44 items, acquired by the harness from `--for-diff 521f638d885160b500d18fe9cb84006c0d37e093..a911378eb2944bfe3d56f495aca7f530674fa6b0`, each assigned to exactly one of 5 lenses: security 9, correctness 9, seams 9, verification 9, intent 8.*
*By design: the caller's byDesign.*
*Security model: the guards are advisory against an agent. They stop forgetting and not evasion, and the header's listed limits stand.*
*Every citation in the body is blob-pinned as `<path>@<sha8>:<line>`, the sha8 being the file's blob at the reviewed head.*

**Range reviewed: 521f638d885160b500d18fe9cb84006c0d37e093...a911378eb2944bfe3d56f495aca7f530674fa6b0**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No item is a BLOCKER.
One item is a HIGH, H1, and three raw findings state it.
H1 answers the question the caller asked: the builder's named limit must be closed for the property to hold, and it is wider than the builder named.
The code cure is one line, and it fails closed.
I recommend building H1's fix before this unit lands, since the owner's answer was "Close it before landing".
Exposure in gov's own repository is latent, because its main history never set either open value.
M1 and the LOW item L1 are missing arms over code that reads correctly today.
L2 is refusal and header text.

## Review shape

Intensity full, raw 7, confirmed 6, refuted 0, merged 1, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 0 | 0 | 1 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 4 items (0 blocker, 1 high, 1 medium, 2 low).
Adjudicated tally by raw confirmed finding: 6 (0 blocker, 3 high, 1 medium, 2 low).
The two tallies differ because H1 holds three findings, 2, 3 and 6.
Every confirmed finding takes its binding grade; none was regraded here.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 1 duplicate refutation counted as a merged confirmation: the security lens's finding 1, a duplicate of finding 2.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 4 judged sound (findings 2, 3, 4, 6), 0 judged UNSOUND, 2 judged INSTANCE-ONLY (findings 5, 7), 0 none proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing, so L1 and L2 carry the skeptic's class-level fix.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 0. Same-address pairs shown: 0.
- Dispositions: unclassed is `refuse`; 44 class slugs handed; 224 leg names read from tools/gate-legs.json.

No lens and no skeptic batch died.
The one non-zero count, the merged duplicate, is counted inside H1's defect and in no tally above.
The seams lens returned nothing, and it returned, so its zero is a reading and not a gap.
H1 was established by reading the source and was not executed: the scratch-guard hook blocked the skeptic's scratch reproduction.
No refuted finding was shown, so no twin is flagged.

## HIGH

### H1. A run's catalogue or cap-census edit moves the guard read to an older open value (findings 2, 3, 6)

**Where:** the acceptance of a `last-valid` answer in `read_guard_value`, at `tools/policy/guard.py@23e97f39:352`.
The finders of findings 2 and 3 cite lines 350 and 352 of the same function.
Validity is judged at `tools/policy/policy.py@b1894836:780`, which loads the working tree's catalogue, and at `tools/policy/budgets.py@7fadb5dd:372`, which reads the working tree's cap census.
The limit as the builder named it stands at `tools/policy/guard.py@23e97f39:39` and `help/policy.md@71e153a4:353`.

**What is wrong:** `read_guard_value` takes any answer whose source is `file` or `last-valid` and whose reason lacks the words `the catalogue default`.
A `last-valid` answer comes from an older landed revision, reached because the landed file reads as invalid.
`read_revision` judges the landed text against `load_catalogue(KIT)`, the working tree's catalogue.
`validate` also calls `check_budgets` with no census, which opens the working tree's `tools/policy/caps.toml`, and a `budgets.<cap>` or a `budgets.pinned` name with no census row is a problem.
So a run that drops or renames one catalogue row or one cap row that the landed file uses makes the valid landed file read as invalid.
Neither file is on the guarded list, and the edit works staged or not.
`read_last_valid` then walks first-parent history to the newest revision that still validates.
Where that revision set the key open, the reason ends `set in .governance/policy.toml at <sha>`, so the text match lets it through.

**Consequence:** the owner sets `policy-file.guard` to `agents-within-mandate` or `agents-with-reason`, and later sets it to `owner-only` or removes it.
A run's branch then drops a row the landed file uses, which can be ordinary work such as retiring a capped file.
`check_run_mandate` admits the run's own write of the policy file, and step 4 of the loop guard and `policy_edit.py set` follow, since all three use the one read.
The landed `owner-only` or unset value is never consulted, so the property and S2 are false on this path.
The header, `help/policy.md` and deviation 951 name the catalogue alone and do not name the cap census.
No arm sees it: the only `last-valid` scenario lands `nobody` over a revision that sets no key, at `tools/policy/check_policy.py@28691f26:3082`, so it exercises the text match alone.
The path is narrow, because an open value must stand in landed first-parent history.

**Judgment the caller asked for:** it must be closed, and naming it in the header does not close it.
The spec's F2 closed the same vector, an unguarded catalogue edit, for the moved default.
S2 says a value is answered only where the landed file sets one.

**Grade:** findings 2, 3 and 6 are HIGH, as bound.

**Fix (judged SOUND for each finding):** take `source == "file"` alone as landed, so line 352 becomes `landed = source == "file"`.
Every other source then answers `owner-only`, which drops the fragile text match too.
The existing invalid-file scenario stays green, since the reason is still returned and still holds `is invalid`.
Correct the docstring of `read_guard_value`, the header, `tools/policy/README.md@0eb06463:476` and `help/policy.md@71e153a4:353`, so that none calls the catalogue edit a limit.
The spec's value table lists `last-valid`, and that spec is CLOSED, so record the departure as a deviation.
The cost is that a run's policy write is refused while the landed file is invalid, until the owner fixes it.
Add these `guard-run-policy` scenarios, each observed red on the current line first:

1. Land the valid file with `agents-within-mandate`, then land it with `owner-only` and a `[budgets]` cap that has a census row. On `run/t`, remove that row from `caps.toml`, read back that `policy.py get` answers `agents-within-mandate` with source `last-valid`, and owe exit 1.
2. The same with a catalogue edit that invalidates a leaf only the newest landed file sets.

Reverting the fix must turn each back to exit 0.

**Left-shift:** `gate:policy fixtures` for the two scenarios, and `class:carried-forward-row-read-as-current` for the read: a reader of a stored value must test when it was written and by what it is judged, not only its state.

## MEDIUM

### M1. No arm fails when step 4 goes back to the resolver (finding 4)

**Where:** step 4 of `check_staged`, at `tools/loop/guard.py@dc73ce48:316`.

**What is wrong:** the diff switched step 4 from `policy.resolve("policy-file.guard").value` to `mguard.read_guard_value`.
The loop guard's plants set the key explicitly on main or leave it at the unmoved catalogue default.
No plant moves the catalogue's default and none makes the landed file invalid, so both reads answer the same in every plant.
A revert of the switch stays green.
AC5 to AC7 cover other surfaces, and AC8 is a one-time `git grep` and not a gate.

**Consequence:** section 4 of the spec says the `agents-with-reason` branch reads the landed file's own value and never a moved default, off a run too.
If step 4 regresses, an agent's commit can move the catalogue default to `agents-with-reason`.
Its next commit, touching the policy file alone with a decision row and a change record, is then admitted through the branch at `tools/loop/guard.py@dc73ce48:327`, which overrides the minimal guard's exit 1.
The shipped code is correct today.

**Grade:** MEDIUM, as bound.

**Fix (judged SOUND):** add a loop guard plant over a scratch copy of the policy kit whose catalogue row default is `agents-with-reason`, with a landed file that sets no key.
Read back that the reader prints that default.
Stage `review.max-rounds` with its record and its decision row, both off a run and on `run/t`, and owe exit 1.
Observe it red with step 4 put back to `policy.resolve`.
The scratch tree must hold the loop kit beside the policy kit copy, since the sibling is resolved from the loop kit's own directory.

**Left-shift:** `class:observed-by-claim-no-arm-discharges`, with the plant standing in the `loop guard fixtures` leg.

## LOW

### L1. The reader's `cannot judge` branch and its shape checks have no plant (finding 5)

**Where:** the `value is None` branch, at `tools/loop/guard.py@dc73ce48:317`, and the shape checks of `read_guard_value`, at `tools/policy/guard.py@23e97f39:343` to 355.

**What is wrong:** no plant owes the text `loop-guard: cannot judge`.
An unresolvable landed revision does reach step 4, since `floor.read_floor` catches the refusal and reads the floor as on.
The minimal guard's one such scenario, `no landed revision`, covers a non-zero reader exit.
Output that does not parse, a wrong shape, a wrong type and a reader that does not start are covered by nothing.

**Consequence:** deleting the branch leaves every loop plant green.
The minimal guard still refuses the policy file, so the effect is exit 1 and a line reading `policy-file.guard = None` where the spec promises exit 2 naming the reader's line.
The deny-by-default shape checks are unproven.

**Grade:** LOW, as bound.

**Fix (the skeptic's class-level fix):** add the loop scenario: the landed revision unresolvable and a guarded change staged, owing exit 2 with `loop-guard: cannot judge`.
In the minimal guard, run a stub `policy.py` that exits 0 over a table of outputs: non-JSON text, `[]`, `{}`, and an object whose value, source or reason is not a string.
Each owes exit 1 with `does not read`.
Exercise the OSError path with an in-process call whose `sys.executable` names no file, asserting `(None, 'policy.py did not start: ...')`.
The finder's proposal, one loop scenario and one stub printing `{}`, cures the cited instance alone: it leaves the unparsed, wrong-type and not-started paths unproven.

**Left-shift:** `class:rule-stated-with-no-check-that-fails`, with the arms standing in the `policy fixtures` and `loop guard fixtures` legs.

### L2. The policy-leaf refusal text and the floor header say a run's branch is admitted (finding 7)

**Where:** the two policy-leaf refusal lines, at `tools/loop/guard.py@dc73ce48:281` and `tools/loop/guard.py@dc73ce48:291`.
The same stale claim stands at `tools/loop/floor.py@e33921ad:8` and `tools/policy/README.md@0eb06463:402`.

**What is wrong:** S4 says the refusal text names a live run's branch only where that branch would be admitted.
Under `owner-only` on a live run's branch, both lines print that commits off a live run's branch are refused whatever `policy-file.guard` reads, and then give the reason that names that key.
Off a run, they still imply that moving to a run's branch admits the commit.
Step 4's sentence, at `tools/loop/guard.py@dc73ce48:333`, was conditioned, and these two were not.
`help/policy.md@71e153a4:405`, the table row for the same floor member, was corrected, and the `floor.py` header was not.

**Consequence:** one line contradicts itself.
The verdict is right and the true reason is appended, so the effect is text only.

**Counter-evidence the skeptic weighed:** section 4 and deviation 951 (3) say the reason stands beside the base's line.
That explains the `guard.py` half, and it neither amends S4 nor covers `floor.py`.

**Grade:** LOW, as bound.

**Fix (the skeptic's class-level fix):** reword the two policy-leaf lines in `tools/loop/guard.py` so they offer a live run's branch only where the landed `policy-file.guard` is in `RUN_WRITABLE`.
Keep the list path's wording, since the list is still admitted on a run under every value.
Correct every remaining statement of guard-self's scope the same way: `tools/loop/floor.py@e33921ad:8` and `tools/policy/README.md:402-403`, as the floor row in `help/policy.md` reads.
The finder's proposal cures the cited instance alone: it leaves the README statement standing.

**Left-shift:** `class:amendment-leaves-its-other-half-standing`, with the sweep of guard-self's scope statements made at the fix.
No fixture needle matches the replaced words, so rewording breaks no arm the skeptic found.

review-shape kind=diff-review round=1 intensity=full at=synth raw=7 confirmed=6 refuted=0 merged=1 unverified=0 blocker=0 high=3 medium=1 low=2 agents=10 out-tokens=59741 trigger=opt-in shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=3 state=CONVERGING

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/policy/guard.py@23e97f39:290 | high | high | refuted | duplicate of id=2. The claim itself is true. It names the same line, tools/policy/guard.py@23e97f39:352 (`landed = source in ("file", "last-valid") and ...`), the same consequence and the same fix. id=2 also covers the wider set of inputs that decide validity (caps.toml). I read read_revision, read_last_valid and read_last_valid_value: an older revision that sets the key gives source last-valid with a reason ending `set in .governance/policy.toml at <sha>`, so landed is True and the older value is returned. Fix: answering only on source `file` cures the class, since a file answer's value comes from the landed table and no working-tree input changes it. | sound | carried-forward-row-read-as-current | - |
| 2 | correctness | tools/policy/guard.py@23e97f39:350 | high | high | confirmed | Read at source, not executed: scratch-guard blocked my scratch repro. tools/policy/guard.py@23e97f39:352 takes any `last-valid` answer whose reason lacks `the catalogue default`. policy.py read_revision and read_last_valid validate landed text with load_catalogue(KIT), the working tree's. validate then calls budgets.check_budgets(doc, text, None), which calls read_cap_census(".") on the working tree's caps.toml and returns a Problem for any budgets.<cap> with no census row. The table then becomes None. The walk reaches the newest older revision that validates, and read_file_value's reason is `set in ... at <sha>`, so an older agents-within-mandate is returned although the landed text says owner-only. check_run_mandate admits it, and loop step 4 and policy_edit use the same read. Neither caps.toml nor catalogue.toml is in guarded-paths.txt, both are ordinary run work, and the header names only the catalogue. That limit is new in this diff, so it is not among the standing limits. The only last-valid scenario in guard-run-policy lands `nobody` over a revision that sets no key, so no arm sees this. The path is narrow: it needs a previously opened key that was later closed. gov's own main history has never set either open value (git log -S is empty), hence high rather than blocker. Fix: `landed = source == "file"` is fail-closed. It keeps the existing invalid-file scenario green, since that still answers owner-only with `is invalid` in the reason. It also covers the catalogue, the census and an owner's typo alike. I found no caller that relies on a last-valid opening. The CLOSED spec's value table is departed from, which needs a deviation record but breaks no code. | sound | - | class:carried-forward-row-read-as-current |
| 3 | verification | tools/policy/guard.py@23e97f39:352 | high | high | confirmed | Read from source, not executed. guard.py read_guard_value accepts source 'last-valid' and excludes only reasons holding 'the catalogue default'. policy.py read_revision validates the landed text against load_catalogue(KIT), which is the working tree's catalogue. read_last_valid then walks first-parent history to an older valid revision, and read_last_valid_value returns that revision's set value with the file step's reason, so an older agents-within-mandate is taken while the landed file says owner-only. The catalogue is not on the guarded list, so a run can commit such an edit, or make a legitimate narrowing with the same effect. check_policy's only last-valid row lands 'valid + guard = nobody' over a 'valid' that sets no guard key, so the set-value branch is unstaged. The spec's table admits last-valid, but its S2 and F2 intend that no unguarded catalogue edit opens the file. The header lists the catalogue as a limit, but this review's by-design list does not, and the caller asked for a judgment: it must close for the property to hold. The path is narrow because it needs an older open value in landed first-parent history. Fix: with source 'file' alone, a catalogue edit can only close the read. The existing invalid-landed row keeps its 'is invalid' needle because the reason is still returned, guard-run-policy-open lands valid files, and a read on a value the file does set never carries the default reason. The proposed row reds on the current code. The header clause naming the catalogue goes with it. | sound | - | gate:policy fixtures |
| 4 | verification | tools/loop/guard.py@dc73ce48:316 | medium | medium | confirmed | Read run_guard_plant in tools/loop/guard.py: the plants set the guard value explicitly on main or leave it unset under the unmoved catalogue default. No plant moves the catalogue or makes the landed file invalid, and run-switched-guard reads the same landed value either way. At the base, step 4 was policy.resolve('policy-file.guard').value. Put back, it answers the same in every plant, so no arm reds. The three loop guard 'New arm' lines in the spec cover AC5 to AC7 and none covers the step 4 read; AC8 is a one-time git grep. The consequence if regressed is real: step 4's agents-with-reason branch overrides the minimal guard's exit 1 given a decision row. Current behaviour is correct, so the effect is contained to a missing arm. Fix: a moved agents-with-reason default with the key unset separates the two reads, both off a run and on run/t, and would red on a revert. The scratch tree must hold the loop kit beside the policy kit copy, since the sibling is resolved from the loop kit's own directory. | sound | - | class:observed-by-claim-no-arm-discharges |
| 5 | verification | tools/loop/guard.py@dc73ce48:317 | low | low | confirmed | Grepping 'cannot judge' in tools/loop/guard.py finds only the print sites (252, 303, 318, 324, 581), so no plant owes that text. update-ref -d occurs only in push-new-branch, which is the push arm. The None branch is reachable: floor.read_floor catches policy.Refusal and returns all-on, so an unresolvable landed revision gets to step 4. The minimal guard's only None scenario is 'no landed revision', a non-zero reader exit; nothing plants exit 0 with bad JSON, a wrong shape or an OSError. The base's refused-resolve branch also had no plant, but the diff rewrote that branch and added the shape checks. The effect is contained: with the branch deleted, the minimal guard still refuses. Fix: the two scenarios cover the loop None branch and the KeyError path. The unparsed, wrong-type and not-started paths the finding names stay unproven. | instance | - | class:rule-stated-with-no-check-that-fails |
| 6 | intent | tools/policy/guard.py@23e97f39:352 | high | high | confirmed | tools/policy/guard.py@23e97f39:352 accepts source 'last-valid' unless the reason holds 'the catalogue default'. read_revision validates the landed text against load_catalogue(KIT), read from the working tree. validate then calls check_budgets with census None, and read_cap_census() reads the working directory's census file. Dropping a catalogue or census row that the landed file uses therefore makes a valid landed file read as invalid. read_last_valid then walks first-parent history and answers from the newest revision that still validates. If that revision set the key open, the reason says 'set in the file', so check_run_mandate, the loop guard and policy_edit set all admit the run. The landed owner-only or unset value is never consulted, which contradicts section 2's property. Section 4's table does list last-valid, but S2 says a value is answered only where the landed file sets one, and the run can trigger the invalidity by an ordinary committed edit. The guard header, help and deviation 951 name the catalogue but not the cap census. The fixture's only invalid-file scenario falls back to a revision with no key set. The path is narrow: the owner must once have opened the key, and gov's own file never set it. Fix: with source 'file' alone, the value comes from the valid landed table and no catalogue or census edit can change it. Every invalid read then answers owner-only. The existing invalid-file scenario still passes, since its reason text is still returned. It covers all callers through the one function, drops the text match, and is only stricter. | sound | - | class:carried-forward-row-read-as-current |
| 7 | intent | tools/loop/guard.py@dc73ce48:281 | low | low | confirmed | Observed at a911378eb. tools/loop/guard.py@dc73ce48:281-282 and :291-292 print 'refused ... for every agent commit off a live run's branch, whatever policy-file.guard [and floor.guard-self] reads' whenever check_run_mandate([POLICY]) returns None. That call now returns None on a live run's branch under owner-only, so the diff made the sentence printable there, followed by a reason that names the key. At base that branch was admitted and the line never printed on a run. S4 (spec :61-63) says the refusal text names a live run's branch only where that branch would be admitted. Only step 4's sentence (:333) was conditioned. tools/loop/floor.py@e33921ad:8 still says guard-self protects its switch 'off a live run's branch'; the diff corrected only lines 22-24, although spec section Texts lists the floor.py header and the help/policy.md row for the same member was corrected. Counter-evidence weighed: section 4 'The wrappers' says the guard-self refusal prints the reason 'beside the line it prints at base', and deviation 951 (3) records that the owner-only line also ends with the reason, as a line 'worded for other branches'. That explains the guard.py half but does not amend S4, and it does not cover tools/loop/floor.py@e33921ad:8. The effect is text only: the verdict is right and the true reason is appended. Fix: no fixture needle in the tools grep matches the replaced words, so rewording breaks no arm found. It leaves another instance of the same stale claim standing in a section the diff edited, tools/policy/README.md:402-403, 'refuses a change to the guard's own switch off a live run's branch', which is also listed under Texts. Its instruction to keep the list path's wording is correct, since the list is still admitted on a run under every value. | instance | - | class:amendment-leaves-its-other-half-standing |
