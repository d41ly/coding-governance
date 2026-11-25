**Serves:** diff-review TOOL-dTotalRecall-115 TOOL-dTotalRecall-116 TOOL-dTotalRecall-117 TOOL-dTotalRecall-118 TOOL-dTotalRecall-119 TOOL-dTotalRecall-120 TOOL-dTotalRecall-121 TOOL-dTotalRecall-21
**Caused-by:** TOOL-dTotalRecall-115

# dTotalRecall — Tier-2 CLOSING DIFF review, round 2

*Node `d`, 2026-11-25. This round reviews the fold of round 1: units TOOL-dTotalRecall-115 to TOOL-dTotalRecall-121, one per HIGH of round 1 and one batch for its minors, and the `query.py` block restored under TOOL-dTotalRecall-21. Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent came from 9 spec documents supplied as `specs`, beside the range's commit messages. The checklist had 83 items, acquired by the harness from `--for-diff acbb74bb38af4c6b6408cf356ca91fe02d9d3277..146df78025b4f87a6a9449fe3225b5472f69a168`, each assigned to exactly one lens: security 17, correctness 17, seams 17, verification 16, intent 16. By design: the caller's byDesign, plus 1 invariant from the checklist's by-design block.* (DERIVED 2026-11-25, the review)

**Range reviewed: `acbb74bb38af4c6b6408cf356ca91fe02d9d3277...146df78025b4f87a6a9449fe3225b5472f69a168`**

**Round: 2.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER and none is HIGH.
Nine items are MEDIUM and two are LOW.
Two of the MEDIUMs are behaviour the fold introduced.
M1: the new stage-failure rollback can overwrite another writer's bytes.
M2: a blob-pinned section read refuses a valid address that the unpinned read resolves.
Five MEDIUMs (M3 to M7) are fold code whose branch no standing arm can red.
Two MEDIUMs are records that say what is not so: M8, an assertion floor that does not count the arms it says it counts, and M9, three `Decided:` lines git does not read as trailers.
I recommend folding M1 and M2 before the landing, each with a plant seen red first.
The rest can be folded or filed.

## Review shape

Intensity full, raw 12, confirmed 12, refuted 0, merged 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| correctness | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| seams | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 6 | 6 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 3 | 3 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 11 items (0 blocker, 0 high, 9 medium, 2 low).
Adjudicated tally by raw confirmed finding: 12 (0 blocker, 0 high, 9 medium, 3 low).
The two tallies differ because findings 3 and 9 are one defect.
Every confirmed finding takes its binding grade.
No finding was refuted, so no twin is flagged.

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 7 judged sound (findings 2, 4, 5, 6, 10, 11, 12), 2 judged UNSOUND (findings 8, 9), 3 judged INSTANCE-ONLY (findings 1, 3, 7), 0 none proposed, 0 NOT JUDGED.
- An INSTANCE-ONLY fix cures the cited instance and leaves its class standing, so those items carry the skeptic's class-level fix.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Refuted findings shown: 0. Same-address pairs shown: 0.
- Dispositions: unclassed is `refuse`; 83 class slugs handed; 230 leg names read from tools/gate-legs.json.

Every count that would mark the run incomplete is zero, so this run is complete.

## MEDIUM

### M1. The stage-failure rollback writes back or deletes without checking that the file is still this call's (finding 1)

**Where:** `tools/memory-tree/gov_record.py@1d4258c0:268` (`write_new_ask`), with the same unconditional unlink at `tools/memory-tree/build_records.py@3b49c05d:1435-1438` (`write_new_record`).

**What is wrong:** after a refused `git add`, `write_new_ask` runs `path.unlink()` or `_write_atomic(path, held)` without re-reading the file.
The forward write just above it does compare and swap (S40, `now != held`).
At the base the `git add` result was ignored, so the branch is this fold's.

**Consequence:** the rollback runs when something else holds the index lock in the same worktree.
If that other writer changes BACKLOG.md between this call's write and the return of its `git add`, the rollback replaces those bytes with the older ones, or deletes the file.
The refusal then says the file was 'put back as it was'.
The window is one git spawn wide, and a second filing cannot realistically land inside it, so only a direct editor write is at risk.
Established by reading; the race was not run.

**Grades:** 1 MEDIUM.

**Fix (the skeptic's class-level fix; the finder's is INSTANCE-ONLY):** one helper in `build_records.py` beside `add_to_index`, taking the written bytes and the prior bytes (or None).
It re-reads the file and restores or unlinks only where the file still equals the written bytes; otherwise it leaves the file and says it moved and is unstaged.
Call it from both `gov_record.write_new_ask` rollbacks and from `write_new_record`'s refused-stage branch, and keep the read-back branch's index removal under the same comparison.
The finder's proposal, one helper for the two `gov_record` branches, cures the cited instance alone and leaves the record doors' unlink standing.

**Left-shift gate:** an arm that monkeypatches `build_records.add_to_index` to append a foreign row and return a refusal, asserting the foreign row survives with and without an existing BACKLOG.md, and the same through the record door. Class `destructive-step-before-its-precondition`.

### M2. A section address is answered one way unpinned and another way blob-pinned (finding 2)

**Where:** `tools/memory-tree/record_find.py@f8ed47fd:498` (`read_section`), with `tools/memory-tree/record_find.py@f8ed47fd:521` and the pick at `tools/memory-tree/record_find.py@f8ed47fd:531`.

**What is wrong:** with no blob, every record row of the key is tried until one's extent holds the section.
With a blob, one row alone is taken: an unordered `fetchone()` where the blob is indexed, or `found[0]` where it is not.
This fold made containment strict at the pick and removed the any-section fallback, so a section under a later row of the same key in the same blob is now refused.

**Consequence:** the file `memory/builds/dPromptedSeam/reviews/2026-08-25-review-TOOL-dPromptedSeam-1-2-spec-audit-round-1.md@972f10ed:84` opens the second of three rows of `TOOL-dPromptedSeam-1`, and its 'majors' section is inside that row only.
By the code, `show TOOL-dPromptedSeam-1#section.tool-dpromptedseam-1-majors` resolves unpinned and exits 2 with 'names no section' when pinned to that blob.
Before this fold the pinned address returned the section.
A valid pinned read is refused in `show`, `budget` and edge resolution, and with no ORDER BY the row taken depends on storage order.
The refusal is loud, so the effect is contained.
The extraction was observed; the end-to-end CLI run was not completed, so the refusal is read from the code.

**Grades:** 2 MEDIUM.

**Fix (judged SOUND):** in the blob branch fetch all record rows of the key (`fetchall`, `ORDER BY b.line`) and keep every entry of `found`.
When a tag is given, pick the first row whose extent contains a section of that tag, as the unpinned branch does; otherwise use the first row.

**Left-shift gate:** a plant of one file with two `## <id>` headings and the tag under the second, addressed unpinned, pinned and by an unheld blob, each expecting exit 0. Class `two-guards-one-question-two-answers`.

### M3. The slug pre-check's arm cannot red on the pre-check (finding 4)

**Where:** `tools/memory-tree/gen_build_index.py@1592a300:6188`, over `tools/memory-tree/gov-claim.sh@3467b47c:959`.

**What is wrong:** the AC4 arm 'a slug opening with a dash or a digit refuses before the remote' uses `-x` and `9x`.
`-x` is refused by the option parser, never by the regex.
`9x` compares only the first three words, 'refused the slug', which the later grammar refusal prints too.

**Consequence:** the arm passes on the old `^[A-Za-z0-9]+$` and with the pre-check line deleted.
The letter-first rule of spec 121 S4 has no check that can fail, and 'before the remote' is not asserted.
The derived slug grammar still bounds the ref name, so the effect is contained.

**Grades:** 4 MEDIUM.

**Fix (judged SOUND):** compare the whole reason.
Assert the text holds 'the slug is not a letter, then letters, digits or dashes' for `9x` and for a slug such as `x/y` or `x_y`, and assert no `refs/gov/claims` ref for them on the remote.
Drop `-x`, or label it the option parser's.

**Left-shift gate:** the corrected arm itself, seen red with the pre-check line cut. Class `refusal-branch-with-no-arm`.

### M4. No arm drives the map experiment to its byte-term figures (finding 5)

**Where:** `tools/workflows/replay_scorer.py@11b238ed:1459` (`measure_map_experiment`).

**What is wrong:** the `armed` derivation and the `term bytes: unarmed` line run in no selftest.
`check_map_known_arm` stops at refusals over an empty candidates list, and `check_map_verdict_arm` hand-feeds `armed` to `derive_map_verdict`.

**Consequence:** a wiring such as `armed: True`, or one that reads the wrong collection, keeps every arm green, and a map replay whose byte term read zero everywhere prints `verdict win`.
That is round 1 M10's consequence, checked now only in the pure function.
The code is correct today and the gap is confined to a replay tool.

**Grades:** 5 MEDIUM.

**Fix (judged SOUND):** an arm driving the experiment over a manifest with two arms and two runs each, whose transcripts all read 0 bytes before the act, asserting `term bytes: unarmed` and no `verdict win`; plus one with a nonzero transcript asserting the figures line.

**Left-shift gate:** that arm, seen red with `armed` pinned True. Class `refusal-branch-with-no-arm`.

### M5. The candidate loop's extent test has no plant that can red it (finding 6)

**Where:** `tools/memory-tree/record_find.py@f8ed47fd:491`.

**What is wrong:** the only plant, `section-outside`, uses a key with one row.
With the predicate reverted to a bare tag match, that same row is taken and the final pick refuses anyway, so every assertion of the arm holds.

**Consequence:** round 1 M5 asked for the containment in both places, and spec 121 S5 names the candidate loop.
With it reverted, a key anchored in two files, the first holding the tag outside the record's extent, makes `show` exit 2 instead of reaching the second file's section.
The suite would not see that regression.

**Grades:** 6 MEDIUM.

**Fix (judged SOUND):** extend the `section-outside` plant, or add one: a key with two rows, the first path's file holding the tag only outside the key's extent and the second holding it inside; assert the second's text and exit 0.

**Left-shift gate:** that plant, seen red with the loop's containment cut. Class `observed-by-claim-no-arm-discharges`.

### M6. The branch for a blob another tree of the node holds is reached by no plant (finding 7)

**Where:** `tools/memory-tree/record_find.py@f8ed47fd:503` (`held is not None and not path`).

**What is wrong:** the three `blob-*` plants and `unheld-blob` run in a fixture with one worktree.
The `path_row` lookup, its `min()` choice among several paths and the 'stands at no path the index holds' refusal are never entered by a standing arm.

**Consequence:** the branch picks which path a blob-pinned `show` reports when another worktree holds the blob, the normal case in this repository.
A wrong pick or a deleted refusal leaves every suite arm green.
Spec 116 backs it with a one-time probe only.

**Grades:** 7 MEDIUM.

**Fix (the skeptic's class-level fix; the finder's is INSTANCE-ONLY):** plant a second worktree whose branch holds the edited record at two paths, the stem path and another sorting before it.
Index both trees, run show `<key>@<blob>` from the first, and assert the stem path and the text; see it red on the lookup cut and on a plain `min`.
Add a case that deletes the blob's `path_row` rows from the fixture index and expects 'stands at no path the index holds', or delete that refusal if it cannot be reached.
The finder's proposal, one second-worktree plant red on the lookup cut to an empty path, cures the lookup alone.

**Left-shift gate:** those plants. Class `refusal-branch-with-no-arm`.

### M7. The record door's unread-header branch has no standing check (finding 8)

**Where:** `tools/memory-tree/build_records.py@3b49c05d:1402` (`write_new_record`, `read_key_fields` returning None).

**What is wrong:** every record in the `door-header` cases is written by the door, and none has its header edited to a form `read_header_edges` refuses.
The text 'unread, its header refusing to read' stands only at its definition.

**Consequence:** spec 117 AC3's red condition, 'an unreadable header reads as the same record', was met by a pass-time probe only.
A partial key instead of None, or a None that raises TypeError in `derive_content_key`, stays green.

**Grades:** 8 MEDIUM.

**Fix (the skeptic's corrected fix; the finder's was REJECTED):** use a record of its own.
After the key loop, write a fresh name (`n-unread`) through the door, commit, append a second `**Caused-by:**` line inside its header lines, commit, and repeat the same call.
Expect exit 2 with 'unread, its header refusing to read' and the ban on 'exists '.
Raise the case literal and docstring, and leave the shared record untouched.

**Left-shift gate:** that case. Class `refusal-branch-with-no-arm`.

### M8. The runlog floor does not count two of the arms its comment says it counts (finding 10)

**Where:** `tools/runlog/selftest.py@b1ff7157:556`, with the comment at `tools/runlog/selftest.py@b1ff7157:552-554` and the spec claim at `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-118.md@8267b258:94`.

**What is wrong:** the spec says the restored arms are 'what the 1711 already counts', and the comment says all nine 'move nothing here'.
The raise to 1711 counts seven arms.
`test_memory_dtr43_paths` (13 assertions with its decoy checks) and `test_memory_dtr53_paths` (9) are outside it, and the floor was not raised for them. (DERIVED 2026-11-25, the review)

**Consequence:** those two arms can be dropped again, or stranded past an early exit, without the floor seeing it, and a merge dropping arms unnoticed is why the unit exists.
The comment tells the next editor they are counted.
This is round 1 M9's class, for a sibling suite.
The unit's ledger and its `Decided:` line disclose the gap and leave it, and spec 121 S9 re-pins the hygiene suite's floor only.

**Grades:** 10 MEDIUM.

**Fix (judged SOUND):** raise `ASSERTION_FLOOR` by 22 more, to 1746, with the RAISED line rewritten to name the dtr43 (10+3) and dtr53 (6+3) arms beside dtr118 (10+3).
Or pin it to the whole-run count at the close, as S9 does for the hygiene suite.

**Left-shift gate:** the build's probe, deleting the two arms in a scratch copy and seeing the floor red; the `runlog selftest` leg then holds the figure. Class `floor-left-below-the-arms-it-guards`, which stands in `memory/gotchas/` and was not among the slugs this run was handed.

### M9. Three unit commits carry a `Decided:` line git does not read as a trailer (finding 11)

**Where:** `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-121.md@6797bd9b:59` (S12), over commits `19a209739`, `8451b1de2` and `07486a8f8`.

**What is wrong:** those three messages hold `Decided:` in a paragraph above the final trailer block, so git's parse returns none.
S12 cites the commit of TOOL-dTotalRecall-116 as the model of a `Decided:` trailer, which it is not.
The commits of 118, 119 and 121 carry theirs in the block.

**Consequence:** `tools/runlog/model.py@29912fc2:607` reads decisions by git's parse, and `edge_grammar` derives a `decides` edge from the same trailer.
The hand-set shell-role counts of 115 and 116 and 117's out-of-scope README and map edits are therefore no ledger entries.
The near-miss tally surfaces that something is missing and loses the text; the prose is still in the bodies.

**Grades:** 11 MEDIUM.

**Fix (judged SOUND):** restate the three decisions as `Decided:` lines in the final trailer block of a later commit of this build, each naming the sha it covers, and correct S12's claim through the spec's revision path.

**Left-shift gate:** the commit-msg hook refuses a message with a column-0 `Decided:` line that `git interpret-trailers --parse` does not return. Class `trailer-parse-reads-only-the-final-block`.

## LOW

### L1. `check_read_call` reads a writing option as a read, and its exclusions have no arm (findings 3, 9)

**Where:** `tools/workflows/replay_scorer.py@11b238ed:1341`, with the quoted-span exclusion at `tools/workflows/replay_scorer.py@11b238ed:1332`.

**What is wrong:** READ_PROGRAMS and GIT_READS admit a program or subcommand with no option check beyond `sed`'s in-place one.
`git diff a..b --output=x.txt`, `find . -delete` and `find . -fprint x` all answered True when called.
The docstring says a shell call that writes a file is the act, and lists only `find -exec` among its gaps.
The `map-transcript` arm also holds no quoted `>` and no heredoc: with QUOTED_SPAN made a no-op, `grep -n "a > b" f` turns into the act and no arm sees it.

**Consequence:** a lens whose first act is such a write has the bytes after it counted as before the act.
The options are rare and only the replay's byte term is affected.

**Grades:** 3 LOW, 9 LOW.

**Fix:** finding 3's proposal is INSTANCE-ONLY and finding 9's was REJECTED, so this joins the skeptic's class-level fix and corrected fix.
Return False for any segment whose read program or git read carries a writing option: the exact word `--output` or the prefix `--output=` for a git read, and `-delete`, `-fprint`, `-fprint0`, `-fprintf`, `-fls`, `-exec`, `-execdir`, `-ok` and `-okdir` for `find`, beside `sed`'s in-place check.
Never refuse `-o` on a git read: `git grep -o` and `git ls-files -o` are plain reads.
Drop the `find -exec` exception from the docstring.
Add each option as an act to `check_map_transcript_arm`, add a quoted-`>` grep and a heredoc read to the `map-transcript` calls, and have the README point to the listed gaps.
Finding 3's own proposal, refusing `--output` on git reads alone, cures the cited instance and leaves the `find` forms standing.

**Left-shift gate:** those `map-transcript` cases, each seen red on the current code. Findings 3 and 9 take the classes `read-allowlist-admits-a-writing-option` (new) and `observed-by-claim-no-arm-discharges`: AC10 observes the quoted `>` by a one-time probe.

### L2. A delivered feed sentence is one unwrapped line (finding 12)

**Where:** `tools/unattended/VERBS.template.md@455e49ad:862`, and its installed copy `memory/guides/UNATTENDED-VERBS.md@455e49ad:862`.

**What is wrong:** spec 121 section 4 asks for the feed sentences 'wrapped as their neighbours are'.
The fold joined two lines into one of 160 characters, where its neighbours run at about 100 columns. (DERIVED 2026-11-25, the review)
The unit's second builder return notes it and leaves it.

**Consequence:** cosmetic; no reader or gate depends on it.

**Grades:** 12 LOW.

**Fix (judged SOUND):** re-wrap the line to the neighbours' width in `VERBS.template.md` and reinstall the guide with `adopt-unattended.sh`.

**Left-shift gate:** none fits: the `line length` leg grades the subjects it declares, and other lines of this file are longer. It stays in the checklist under class `fold-text-is-unreviewed-surface`.

## Unverified and refuted

None.

review-shape kind=diff-review round=2 intensity=full at=synth raw=12 confirmed=12 refuted=0 merged=0 unverified=0 blocker=0 high=0 medium=9 low=3 agents=10 out-tokens=98158 trigger=- shape=- efforts=- role-sha=-
review-round round=2 limit=3 prior=8 count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/memory-tree/gov_record.py@1d4258c0:268 | medium | medium | confirmed | Read gov_record.py 258-271: the forward write compares now != held, but the new refused branch unlinks or rewrites held with no re-read. At the base the git add result was ignored and no rollback existed here (only the read-back one), so this branch is new. Exposure is contained: a second filing cannot realistically land inside the window, since it must parse, mint and compare-and-swap, so only a direct editor write during one failing git add is lost. Not run. The fix covers both gov_record branches, but build_records.py 1435-1438 carries the same unconditional unlink after a refused add_to_index for the record doors, so the class is left standing there. | instance | - | class:destructive-step-before-its-precondition |
| 2 | correctness | tools/memory-tree/record_find.py@f8ed47fd:498 | medium | medium | confirmed | Read record_find.py 484-533: the unpinned branch walks every row of the key and takes one whose extent holds the section; the pinned branch takes one unordered fetchone (or found[0]), and the pick no longer falls back. The base fell back to any section of the tag, so the pinned refusal is introduced here. The cited file has '## TOOL-dPromptedSeam-1' headings at lines 17, 84 and 111; record_extract.extract_record emits one row per anchored heading with no dedupe, and the anchor mode defaults to derived, so headings get section tags. S5's 'a key with a short extent names its own lines alone' does not cover it: line 84 is inside one of the key's own rows. The effect is a loud refusal of a valid address, contained. The CLI was not run end to end. The fix makes both blob paths pick as the unpinned one does, with a stable order. | sound | two-guards-one-question-two-answers | class:two-guards-one-question-two-answers |
| 3 | seams | tools/workflows/replay_scorer.py@11b238ed:1341 | low | low | confirmed | Called check_read_call directly: 'git diff a..b --output=x.txt' returns True, while the docstring says a shell call that writes a file is the act and does not list this exception. At the base derive_tool_class answers 'other' for that command and it is no search, so it was the act there; the change is this diff's. Same call also returns True for 'find . -delete' and 'find . -fprint x', undisclosed write options of a read program (find -exec alone is named), so the proposed git-only check leaves the class standing. | instance | - | new:read-allowlist-admits-a-writing-option |
| 4 | verification | tools/memory-tree/gen_build_index.py@1592a300:6188 | medium | medium | confirmed | tools/memory-tree/gov-claim.sh@3467b47c:947 refuses -x in the option parser ('-x is no option'), before the pre-check at 959. The base pre-check ^[A-Za-z0-9]+$ admits 9x, and the grammar match at 980 then refuses it with 'the slug 9x is not admitted'. The arm at tools/memory-tree/gen_build_index.py@1592a300:6188 compares only exit 2 and the first three words, 'refused the slug', so it passes on the base pre-check and with line 959 deleted. I printed slug-re for this tree and it opens with a lower-case letter, so 9x is refused there anyway. The effect is contained because that grammar still bounds the ref name. No other arm covers the letter-first rule, and nothing asserts 'before the remote'. The fix is sound: the full text is unique to line 959, so deleting or reverting that line reds it for 9x, x_y and x/y. | sound | vacuous-selector-empty-population | class:refusal-branch-with-no-arm |
| 5 | verification | tools/workflows/replay_scorer.py@11b238ed:1459 | medium | medium | confirmed | In replay_scorer.py, `measure_map_experiment` is named only in the INSTANCES table (line 1534), and no other file under tools/ names it. check_map_known_arm reaches it only with `candidates: []` and an unknown item or an unnamed heading finding, so it refuses in read_map_known, the first line. Its last case calls read_map_known directly. check_map_verdict_arm hand-feeds `armed`. Neither the `armed` derivation at 1459 nor the `term bytes: unarmed` line at 1467 runs in any selftest, so `armed: True` would stay green and print `verdict win`. The code is correct today and the gap is confined to a replay tool. The proposed end-to-end arm, red with `armed` pinned True, cures it. | sound | - | class:refusal-branch-with-no-arm |
| 6 | verification | tools/memory-tree/record_find.py@f8ed47fd:491 | medium | medium | confirmed | tools/memory-tree/record_find.py@f8ed47fd:491 gained the extent test. The only plant is section-outside: TOOL-bFix-11 stands in one file (notes.md), with the section under TOOL-bFix-12. With line 491 reverted to a bare tag match, rec is that same row and the pick at the end of read_section still raises 'names no section of', so every assertion at tools/memory-tree/check-memory-hygiene.test.sh@53497e57:3762-3763 holds. The loop's purpose, per its comment, is a key anchored in several files, and no plant has a tag outside the extent in the first and inside it in a later one. A regression would refuse a section that exists, silently for the suite. Spec S5 names the candidate loop explicitly. The fix is sound: with the cut, the first row is picked and refused, so asserting the second file's text and exit 0 reds. | sound | - | class:observed-by-claim-no-arm-discharges |
| 7 | verification | tools/memory-tree/record_find.py@f8ed47fd:503 | medium | medium | confirmed | build_fixture and run_fixture (record_find.py) make one repository and no second worktree. unheld-blob amends the old blob away, so the branch's own comment has its rows lost. The blob-* plants give held None, and no other plant passes @blob. So `held is not None and not path` is never entered by a standing arm. The path_row lookup is new: the base file has no such query, only RECORD_ROWS. Spec 116 backs indexed-path selection only with AC6's probe, which covers a decisions file. The proposed plant covers the lookup only. The refusal and the min() choice among several paths, which the finding's impact names, stay unplanted. | instance | - | class:refusal-branch-with-no-arm |
| 8 | verification | tools/memory-tree/build_records.py@3b49c05d:1402 | medium | medium | confirmed | read_key_fields returns None on ValueError, and lines 1403 and 1407-1408 handle it. grep finds the message only at its definition. I read door-header's cases: every record is written by the door and none has its header edited to a refused form. AC3 is a probe only, so a partial key or a TypeError there stays green. The fix as worded is unsound. Mutating the shared `name` record after `replay` leaves it unread for the unit, title, cause, edge and no-edge cases. Each would then be refused 'already holds the record' whatever the content key held, so those five arms go vacuous. The build case and the later lease case also use that record. | unsound | - | class:refusal-branch-with-no-arm |
| 9 | verification | tools/workflows/replay_scorer.py@11b238ed:1332 | low | low | confirmed | map-transcript holds no quoted `>` and no heredoc. I ran check_read_call: with QUOTED_SPAN made a no-op, `grep -n "a > b" f` went True to False, and no arm would see it. `git diff --output=x.patch a b` answers True, as does `find . -delete`. Neither is in the 'Not read' list, and the README says 'writing no file'. This is S10's new code. The effect is limited to an experiment's byte term. The fix's `-o` refusal is wrong: `git grep -o` (only-matching) and `git ls-files -o` (others) are plain reads that it would turn into acts. It also leaves find's -delete and -fprint forms standing. | unsound | - | class:observed-by-claim-no-arm-discharges |
| 10 | intent | tools/runlog/selftest.py@b1ff7157:556 | medium | medium | confirmed | Read the diff of tools/runlog/selftest.py. The 1658->1711 raise lists only AC1, AC2, AC3, AC4, AC6, AC7 and AC9, and 8+7+3+4+4+4+2+21=53. test_memory_dtr43_paths (5 rows x 2 checks + 3 decoy checks = 13) and test_memory_dtr53_paths (3 rows x 2 + 3 = 9) are outside it. main() runs every test_* and fails only when total < ASSERTION_FLOOR, so there are 22 assertions of slack from these arms. The 552-554 comment says all nine 'move nothing here', and spec 118 section 4 says the 1711 counts them; both are false. The base file had no test_memory arm, so the range introduced both the gap and the comment. The unit's return and Decided trailer disclose the gap, but disclosure is not on the by-design list, and spec 121 schedules only the hygiene floor. The effect is contained: the suite stays correct and only the guard is slack. The fix is sound: parse_floor_raise only needs the upper figure to equal the floor and the arithmetic to sum to the raise, so 13+13+9=35 and 1711 -> 1746 satisfies it. | sound | - | new:floor-left-below-the-arms-it-guards |
| 11 | intent | memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-121.md:59 | medium | medium | confirmed | Re-ran git log with %(trailers:key=Decided) over the range. It is empty for 19a209739, 8451b1de2 and 07486a8f8, whose messages hold `Decided:` followed by a blank line and then the trailer block. It is populated for 8e9ad3d6d, cc26d2192 and 18c9ccf24. tools/runlog/model.py@29912fc2:607 reads git's parse only, so these three decisions are no ledger entries; they are only tallied in near_miss (tools/runlog/model.py@29912fc2:1181-1182), which loses their text. Spec 121 S12 cites 116's commit as carrying a `Decided:` trailer, which is false. All of this was introduced in the range. Containment: the near-miss count surfaces that something is missing, and the prose is still in the body. The fix is sound: later trailers restore the records on append-only history, and the hook check covers the class. | sound | trailer-parse-reads-only-the-final-block | class:trailer-parse-reads-only-the-final-block |
| 12 | intent | tools/unattended/VERBS.template.md:862 | low | low | confirmed | tools/unattended/VERBS.template.md:862 is 160 characters. The base wrapped the same sentence over two lines, and the diff joined them. The neighbours run at about 100 columns, and spec 121 line 243 asks for the sentences 'wrapped as their neighbours are'. Other lines over 120 exist in the file, but this one was created here against the stated form. Cosmetic. Re-wrapping the template and reinstalling the guide cures it. | sound | - | class:fold-text-is-unreviewed-surface |
