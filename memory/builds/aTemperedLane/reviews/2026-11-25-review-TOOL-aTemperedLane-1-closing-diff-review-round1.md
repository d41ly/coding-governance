**Serves:** diff-review TOOL-aTemperedLane-1 TOOL-aTemperedLane-2

# aTemperedLane — Tier-2 CLOSING DIFF review, round 1

*Node `a`, 2026-11-25. An adversarial pass over the cumulative diff landing on main: units TOOL-aTemperedLane-1 (L3 past the `gen:spec-records` region) and TOOL-aTemperedLane-2 (L2 at the first parent's list). Five finder lenses ran, then skeptic batches prompted to refute each finding, then this synthesis. Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.*

**Range reviewed: `3d6c1702afb6c2e86638785950d80657a187192c...7654f9db2c06253cc038c2a56705b2b0350a20ae`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

No finding is a BLOCKER or a HIGH.
One MEDIUM item (findings 1 and 7) is a false claim: the help page and the build README say a guarded line the fix commit itself removes still guards, and deleting the whole list breaks that.
Two MEDIUM items are coverage gaps over code that is correct today: the unreadable parent list, and the first-parent rule on a merge.
Two LOW items are coverage gaps with no present behaviour defect.
Correct M1's claim before the landing, or make it true in code.
M2 and M3 are each one fixture with its arm.
The LOWs can be folded or filed.

## Review shape

Intensity full, raw 7, confirmed 6, refuted 1, merged 0, unverified 0 (0 uncertain), precision 0.86.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |
| correctness | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| seams | yes | 0 | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 4 | 4 | 0 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 5 items (0 blocker, 0 high, 3 medium, 2 low).
Adjudicated tally by raw confirmed finding: 6 (0 blocker, 0 high, 3 medium, 3 low).
The two tallies differ because findings 1 and 7 describe one defect and form one item.
Every confirmed finding keeps its bracketed binding grade.
The refuted finding 2 (the L3 exemption's population) is a different defect from every confirmed one, so no twin is flagged.

**Run integrity:**

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 4/4 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified.
- 0 orphaned duplicate refutations demoted to unverified.
- 0 duplicate refutations counted as merged confirmations.
- 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 3 judged sound (3, 5, 6), 2 judged UNSOUND (4, 7), 1 judged INSTANCE-ONLY (1), curing the cited instance and leaving its class standing, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 3 RE-GRADED by the skeptic (1 and 5 MEDIUM to LOW, 7 HIGH to MEDIUM).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: NEITHER `specs` nor `context` was supplied, so the lenses had only the range's commit messages.
- Checklist: 35 items, acquired by the harness from `--for-diff 3d6c1702afb6c2e86638785950d80657a187192c..7654f9db2c06253cc038c2a56705b2b0350a20ae`, each assigned to exactly one of 5 lenses: security 7, correctness 7, seams 7, verification 7, intent 7.
- By design: none supplied, no caller byDesign and a block of 0.
- Refuted findings shown: 1. Same-address pairs shown: 0.
- Dispositions: unclassed is `refuse`; 35 class slugs handed; 226 leg names read from tools/gate-legs.json.

Every count that would mark the run incomplete is zero, so this run is complete.
The correctness and seams lenses returned no finding.

## MEDIUM

### M1. A fix commit that deletes the whole guarded list escapes the parent's list, and the documents say it does not (findings 1, 7)

**Where:** `tools/memory-tree/routed_commits.py@f9517a1c:513`, in `read_parent_lists` (the early return at :514, the `.governance/` fallback at :603).
The claims: `help/red-fix-lane.md@1dd6ceb8:87` and `memory/builds/aTemperedLane/README.md@2badd675:23`.
The "not checked" lists that omit the case: `tools/memory-tree/routed_commits.py@f9517a1c:61` and `help/red-fix-lane.md@1dd6ceb8:217`.

**What is wrong:** where the list is looked for in the parent's tree depends on the working tree still holding it.
`resolve_guarded_path` finds the policy kit by its `guarded-paths.txt` anchor on disk.
When that file is gone it answers the empty string, `read_parent_lists` returns `{}`, and `read_guarded_paths` returns None.
L2 then refuses only paths under `.governance/`, although the first parent holds a list.
The fallback itself is not new: the base behaved the same way, and spec -2's S2 and its rule table choose it.
What the diff introduced is the false claim.
The help page says "a line the commit itself removes still guards", and the build README says a self-shortened list is caught.
The diff also dropped the base's disclosure that "a guarded list the fix commit itself shortened" goes unchecked.
Deleting the list is the extreme shortening, and no "not checked" list names it.
The moved-list clause covers a different case, since there the working tree's list grades.
The only arm for a missing list is g10, which edits a `.governance/` path that the fallback refuses anyway.

**Evidence:** with `resolve_kit_dir` raising LookupError, the skeptics' read-only probe gave `''`, None and `{}`, while HEAD holds `tools/policy/guarded-paths.txt`.
Over four agent-file commits of branch/unattended-dboundroles-62c3df, dd72a598, 0b2d6853 and fcc659e0 went from L2 findings to none.
bfccd912 kept only its `.governance/` paths.

**Consequence:** a Red-fix commit can remove the list and edit a non-`.governance/` path on it, and L2 reports nothing.
Any later commit that deletes the list drops every non-`.governance/` line for the whole history.
A single four-line list fits L1, and L4 does not see deletions.
The effect is contained today, since all four lines of main's list are under `.governance/`.
The path opens once the agent-file lines land.

**Grades:** finding 7 binds at MEDIUM (its skeptic lowered the finder's HIGH, because it needs a pushed tip with the whole list gone).
Finding 1 binds at LOW (its skeptic weighed the remainder as a documentation overclaim, the code being as the spec chose).
The item takes the highest grade, MEDIUM.

**Fix, finding 7 (the finder's proposal was REJECTED; this is the skeptic's corrected fix):** where the working tree's list does not resolve, still read each first parent's list at a path found without the file on disk.
Candidates for that path are another policy-kit anchor, the install receipt row's path unchecked for existence, else the conventional sibling `policy/guarded-paths.txt` inside the repository.
Refuse the UNION of that list's paths and every path under `.governance/`, so AC6 stands.
Add an arm: a fix commit deletes the list and edits src/b.txt, the disk copy removed, expecting L2 naming src/b.txt.
Alternatively keep the code and state the gap in the spec, docstring, help page and README row: a pushed tip with no list on disk drops the parent's list and refuses only `.governance/`.
Qualify "still guards" and the build README's "is caught" in either case.

**Fix, finding 1 (judged INSTANCE-ONLY; this is the skeptic's class-level fix):** state in the help page's not-checked list and in the module docstring that a list absent from the working tree, deleted by the fix commit or by any later one, leaves only the `.governance/` prefix.
Narrow the help sentence to "a line the commit itself removes, the list still being present, still guards".
If behaviour is to change instead, also resolve the repo-relative list path from the install receipt row without requiring the file to exist, before the tool-root probe, and read the parent there.
The finder's proposal, deriving the path from the deletion's raw-log entry or from the tool root, cures the cited instance alone.
A later deletion in an install that homes the kit elsewhere by receipt resolves from neither.

**Left-shift gate:** the deleted-list arm above in the `routed-commits selftest` leg, seen red against today's code first, if the code changes.
If the gap is kept, the same fixture as an arm that pins exit 0, so the not-checked sentence has a check that fails when it stops being true.

### M2. No arm reaches the unreadable-parent-list branch (finding 3)

**Where:** `tools/memory-tree/routed_commits.py@f9517a1c:524`, the `except UnicodeDecodeError` in `read_parent_lists`, with the non-blob answer of `read_blob_batch` at :290.

**What is wrong:** spec -2 section 4 says a first parent whose list is not UTF-8, or is not a blob, reads as no list and falls back to the working list.
No self-test arm stages either.
The `parentlist` and `parentroot` fixtures hold only an absent list (g2) or text lists, and `build_fixture` encodes every body as UTF-8, so it cannot write one.
The ledger records the two cases only as a one-off probe remark.
The directory half is weaker than the finding said: an absent list and a directory share the None branch, which g2 exercises.

**Consequence:** the shipped code is correct today.
Replacing `pass` with `got[sha] = []` would turn L2 off for that commit and leave every arm green.
A commit that corrupts the list, followed by a fix commit editing a guarded file, would then pass.

**Fix (judged SOUND by the skeptic):** add two arms beside AC5.
One parent holds a non-UTF-8 list, with `build_fixture` accepting bytes.
The other holds a directory at the list path.
Expect each child fix editing src/a.txt to exit 1 naming L2, and stage red with `got[sha] = []`.

**Left-shift gate:** those two arms, in the `routed-commits selftest` leg.

### M3. No check can fail if the rule reads a parent other than the first (finding 4)

**Where:** `tools/memory-tree/routed_commits.py@f9517a1c:516`, `c['parents'][0]` in `read_parent_lists`.

**What is wrong:** every commit in the `parentlist` and `parentroot` fixtures has at most one parent, and no limits arm hands the verb a merge.
The verb grades merges, as its docstring says ("merge or not", :59).

**Consequence:** the shipped code is correct today.
`parents[-1]` in its place passes every arm.
A fix-trailered merge would then be graded by the side lineage's list, which may omit a guarded path, while its diff is still read against the first parent.
The verb would report `is inside all four`.
Only the manual verb reaches merges, so the effect is contained.

**Fix (the finder's proposal was REJECTED; this is the skeptic's corrected fix):** put the trailered merge in its own scratch fixture, not `parentlist`.
A merge in `parentlist` breaks the AC7 arm, which requires `len(first_up) == 8` and `red == early` over a log that does not drop merges.
Give the new fixture a base commit, a side commit whose list omits src/b.txt, and a first-parent commit whose list names src/b.txt.
The merge carries the Red-fix trailer and edits src/b.txt, with explicit `parent` and `merge` positions.
Use the same disk list (src/a.txt only) and KIT stub, run the verb on the merge, and expect exit 1 naming L2 src/b.txt.
Stage red with `parents[-1]`.

**Left-shift gate:** that arm, in the `routed-commits selftest` leg.

## LOW

### L1. The torn-stream refusals and the non-blob skip of `read_blob_batch` have no arm (finding 5)

**Where:** `tools/memory-tree/routed_commits.py@f9517a1c:282` and :289.

**What is wrong:** both Refusals and the non-blob body skip are new in this diff, and nothing in the self-test exercises them.
The self-test never stubs `run_git`, and spec -1 section 7's New arm covers AC2 to AC7 only.
AC8's torn-stream result was seen once in the ledger and is gated by nothing.

**Consequence:** the function now frames the spec map, the leg manifests, the L3 blobs and the L2 lists.
An edit that returns a short body, or None, instead of refusing would pass the whole self-test.
A truncated guarded list would then read as a shorter list, and L2 would pass in place of exiting 2.
The finding is LOW because `run_git` already refuses a non-zero git exit, so only a future edit combined with a torn zero-exit stream is missed.

**Fix (judged SOUND by the skeptic):** add a self-test arm that stubs `run_git` with a stream cut before a header, one cut inside a body, and one holding a tree answer before a blob.
Assert two Refusals, then None followed by the right body.

**Left-shift gate:** that arm, in the `routed-commits selftest` leg.

### L2. Nothing asserts that the marker consumers read `tree_lib`'s predicate (finding 6)

**Where:** `tools/memory-tree/marker-contract.test.sh@21ac8011:228`.

**What is wrong:** the diff moved the one-CR source grep from gen_build_index.py to tree_lib.py together with the predicate.
Nothing asserts that gen_build_index.py and routed_commits.py read that predicate, and AC9's identity check was a one-off.
The case table's Python reader still lives in gen_build_index.

**Consequence:** a local `check_marker_line` in gen_build_index that uses `rstrip("\r")` would pass.
The grep finds tree_lib's line, and the one-CR behavioural case accepts either spelling.
Before the move, the grep read the file that held the reader.
No present behaviour is wrong.

**Fix (judged SOUND by the skeptic):** extend the arm with a python check that `gen_build_index.check_marker_line`, `routed_commits.check_marker_line` and `tree_lib.check_marker_line` are one object.

**Left-shift gate:** that identity check in the `marker contracts` leg.

review-shape kind=diff-review round=1 intensity=full at=synth raw=7 confirmed=6 refuted=1 merged=0 unverified=0 blocker=0 high=0 medium=3 low=3 agents=10 out-tokens=50043 trigger=- shape=- efforts=- role-sha=-
review-round round=1 limit=- prior=- count=0 state=CONVERGED

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/memory-tree/routed_commits.py:514 | medium | low | confirmed | I re-ran the probe with resolve_kit_dir raising LookupError: resolve_guarded_path gave '', read_guarded_paths None and read_parent_lists {}, although HEAD holds tools/policy/guarded-paths.txt. A commit that deletes the list is therefore graded by the .governance/ prefix alone. That behaviour is pre-existing: at the base a missing list also gave None and the same prefix, and S2 plus the rule table keep it explicitly 'as today'. What the diff introduced is the claim. help/red-fix-lane.md now says 'So a line the commit itself removes still guards', and the diff dropped the old disclaimer 'or a guarded list the fix commit itself shortened'. Neither the help page's nor the docstring's not-checked list names deletion, so the sentence is false for a deleted list. The remaining defect is a documentation overclaim. All four shipped lines are under .governance/, so deletion changes no verdict here today. Fix verdict 'instance': the D entry covers the deleting commit, and the tool-root path covers the default layout. A later deletion in an install that homes the kit elsewhere by receipt resolves from neither. | instance | - | class:amendment-leaves-its-other-half-standing |
| 2 | security | tools/memory-tree/routed_commits.py:587 | low | - | refuted | The code reading is right: build_spec_path_re filters on the folder alone, while the generator checks the region only for .md files whose header parse_spec accepts. The defect is not reachable. My probe over 3139 tracked spec paths found 3134 with a single ordered pair, none of those headerless, and no non-.md file. The generator adds a pair only to files it parsed as units. A fix commit cannot create the state: an added file is status A and an introduced pair has no pair on its old side, so both stay L3. Removing a header changes bytes outside the region, so that is L3 too. The state needs an earlier, non-lane commit to hand-place the pair in a file that is not a unit record. The only consequence is ungraded text between markers in a file the index ignores. Fix verdict 'instance': the generator also skips whole builds whose stale README header is waived (the tolerated/continue branch in gen_build_index.py), and their well-headed specs would still be exempt yet ungraded. | instance | - | - |
| 3 | verification | tools/memory-tree/routed_commits.py:524 | medium | medium | confirmed | Judged from source. The shipped code is correct: the UnicodeDecodeError branch in read_parent_lists leaves the commit out, so check_red_fix_limits uses the working list. No self-test arm reaches that branch. parentlist and parentroot stage only an absent list or text lists, and build_fixture encodes every body as UTF-8. The ledger notes the two cases only as a probe remark (line 22). Spec -2 section 4 and section 5 state the rule, so `got[sha] = []` in the except would leave every arm green. The directory half is weaker than claimed. Absent and directory share the None branch, which g2 exercises, and a tree body holds raw sha bytes that usually fail UTF-8 decoding, so it normally falls back anyway. This is a coverage gap over code that is correct today. The fix reaches both input kinds, and its src/a.txt expectation distinguishes fallback from an empty list. | sound | rule-stated-with-no-check-that-fails | class:rule-stated-with-no-check-that-fails |
| 4 | verification | tools/memory-tree/routed_commits.py:516 | medium | medium | confirmed | Judged from source. read_parent_lists uses c['parents'][0], and no limits fixture holds a merge: the only `merge` fixtures are the range, AC7, newest-unit and store ones, none graded by check_red_fix_limits for L2. All parentlist and parentroot commits have at most one parent. The verb grades merges (main, line 1904), so parents[-1] would leave every arm green while the diff is still read with --diff-merges=first-parent. The spec's central wording is `first parent`. The code is correct today and only the manual verb reaches merges, so the effect is contained. The fix as written breaks a sibling arm. The AC7 arm builds first_up from read_routed_commits(HEAD) with no merge filter, requires len 8 and requires red == early. A trailered merge in parentlist makes 9 and adds an L2 sha to early that the leg, which skips merges, never puts in red. | unsound | rule-stated-with-no-check-that-fails | class:rule-stated-with-no-check-that-fails |
| 5 | verification | tools/memory-tree/routed_commits.py:282 | medium | low | confirmed | Both Refusals and the non-blob body skip are new: base load_spec_paths used raw.index and sliced the body unguarded. A grep for both refusal messages finds only the raise lines at 282 and 289. The self-test stubs other globals but never run_git, and read_blob_batch is named only at its definition and four callers. Spec section 7's New arm covers AC2 to AC7, and AC8's torn-stream result is a one-off ledger observation. The shipped code is correct and run_git already refuses a non-zero git exit, so only a future edit combined with a torn zero-exit stream would be missed; hence low. The fix works because read_blob_batch looks up run_git in module globals, which the self-test already swaps elsewhere, and its three streams cover every unarmed branch. | sound | rule-stated-with-no-check-that-fails | class:rule-stated-with-no-check-that-fails |
| 6 | verification | tools/memory-tree/marker-contract.test.sh:228 | low | low | confirmed | The diff moved the grep target from gen_build_index.py to tree_lib.py along with the predicate, and gen_build_index and routed_commits now import it. The leg's reader still drives gen_build_index.apply_region, and no check I found asserts the re-import; AC9's identity check was a one-off probe. A local redefinition in gen_build_index using rstrip would satisfy the grep through tree_lib and pass the one-CR case, where the base grep read that same file and would have failed if the function were re-spelled. It is a narrow loss of gate coverage with no current behaviour defect. The fix is sound: the leg already imports gen_build_index from KIT_MT with $PY, routed_commits imports the name from tree_lib, and the identity check catches a module-level re-spelling in either consumer. | sound | - | gate:marker contracts |
| 7 | intent | tools/memory-tree/routed_commits.py:513 | high | medium | confirmed | read_parent_lists returns {} whenever resolve_guarded_path is empty, and resolve_kit_dir needs the guarded-paths.txt anchor on disk, so a fix commit that deletes the list is graded by the .governance/ prefix alone. I re-ran the probe read-only: dd72a598, 0b2d6853 and fcc659e0 went from L2 findings to none once resolve_kit_dir raised LookupError, and bfccd912 kept only its .governance/ paths. Scope: the fallback behaviour is the same at the base, and the spec's fourth rule row chooses it. But this diff introduced a false contract: help/red-fix-lane.md says 'a line the commit itself removes still guards', the build README says a self-shortened list is caught, and the diff removed the base's disclosure that a 'guarded list the fix commit itself shortened' is unchecked. Deleting the list is the extreme shortening, and no new 'not checked' list names it. The moved-list clause says the working tree's list then grades, which is not this case. The only arm for a missing list is g10, which edits a .governance/ path. Not high: it needs a pushed tip with the whole list gone, and today's list on main holds only .governance/ lines, which the fallback still refuses. The proposed fix is unsound: using .governance/ only where the parent holds no list reverses AC6. In its fixture, g10's parent holds a list that does not name .governance/policy.toml, so with the disk list removed and the parent's list read by a sibling path, g10 would exit 0 and deny by default would be loosened. | unsound | - | class:amendment-leaves-its-other-half-standing |
