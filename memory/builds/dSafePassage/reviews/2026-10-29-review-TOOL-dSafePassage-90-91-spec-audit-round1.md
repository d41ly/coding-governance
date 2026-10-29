**Serves:** spec-audit TOOL-dSafePassage-90@rev-1 TOOL-dSafePassage-91@rev-1

# Tier-2 review: TOOL-dSafePassage-90 and -91 spec audit, round 1

Provenance: this is a round-1 adversarial spec audit of two units promoted from the round-3 closing diff review (memory/builds/dSafePassage/reviews/2026-10-29-review-TOOL-dSafePassage-86-87-89-88-closing-diff-round3.md). Unit 90 takes 88's samefile arm back out of `own_file` in `_cmd_update` (tools/govkit/govkit.py). A case-only rename on a case-folding filesystem is then refused before any write, with a message that names the case-only cause. That closes the round-3 review's H1 and M2 and makes its M1 unreachable. Unit 91 batches three things: L1, an in-place row recorded once in the rollback snapshot; M4, a plant-root grader over 87 S7's split in tools/govkit/upgrade_walk.py; and L2, a check on the python-floor stub's bare-bash fallback. The build order is 90, then 91. The finders were gov-spec-reviewer, the skeptic batches were gov-skeptic, and the synthesis was gov-synthesizer. No spec was supplied as intent; `context` was the caller's statement. The by-design list was the caller's byDesign.

Reviewed: memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-90.md@c55f986f881dfeea48eba90f60bc901ff4774b21, memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md@7bb7372ec54160f9aa28746e0b018c62635c80d3

ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs. Each remaining item is a spec edit to make before the build. By item, the tally is 10: medium 5, low 5. By raw confirmed finding, the tally is 14: medium 8, low 6. Two merges account for the difference. Ids 1, 4, 8 and 10 are one defect: AC4's grep count misses the `def` line. Ids 3 and 5 are one defect: the cross-unit edges name a shared govkit.py block that does not exist.

Review shape: intensity full, raw 14, confirmed 14, refuted 0, unverified 0 (0 uncertain), precision 1.00.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| failure-envelope | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |

Run integrity:
- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 12 judged sound, 2 judged unsound (ids 10 and 13), 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded, 0 re-graded by the skeptic.
- Unverified findings: none.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Move check: no checked subject moved.

This run is complete on these counts.

No checklist was swept. The project's bug-class checklist is absent, so a zero count here is no evidence that its recurring bug classes are absent.

## Medium

### M1. AC4's grep count leaves out the `def` line, so a correct build reads red (ids 1, 4, 8, 10)

- **Where:** TOOL-dSafePassage-91 spec, section 6 AC4, checked against section 4 "S2: the plant-root grader".
- **What is wrong:** AC4 says `git grep -n -F "derive_policy_adopter(t)" -- tools/govkit/upgrade_walk.py` prints two lines. S2 itself designs three lines that contain that string:
  - the definition `def derive_policy_adopter(t) -> pathlib.Path:` (spec :187);
  - the call `derive_policy_adopter(t).as_posix()` in `build_release_tree` (spec :195);
  - the call `pol = derive_policy_adopter(t)` in `check_grade_plant_root` (spec :210).
- **Consequence:** A build that follows S2 exactly fails AC4. The builder then has to do one of two wrong things: bend the code to fit the grep (for example, rename the parameter) or record a failed criterion as passed. Either way AC4 stops checking what it exists for: that the inline adopter expression is gone and that both callers share the function. The count also lets through a build that drops one call site but keeps the `def` line. AC4's second grep still catches the inline regression, so the damage stays inside this criterion.
- **Fix:** The skeptic judged the fixes from ids 1, 4 and 8 sound. It rejected id 10's fix and gave this corrected fix: state that AC4's first grep prints three lines, namely the def beside `derive_release_engine`, the call in `build_release_tree` and the call in `check_grade_plant_root`. Either of two sound alternatives also works:
  - keep the count at two and exclude the def line, for example `git grep -n -e "derive_policy_adopter(t)" --and --not -e "^def "`;
  - grep call-site patterns the def cannot match: `derive_policy_adopter(t).as_posix()` and `pol = derive_policy_adopter(t)`.
  In every form, AC4 stays red while the inline `resolve_kit_dir("policy", adopter` line remains.
- **Left-shift gate:** Add a spec-lint step that extracts each AC's `git grep` command and runs it against the code blocks of section 4. Where the stated line count differs from what the designed code produces, the step fails.

### M2. AC5 already passes on today's tree, so it cannot observe S3 (id 2)

- **Where:** TOOL-dSafePassage-91 spec, section 6 AC5, with section 2 S3 and the third New arm in section 7.
- **What is wrong:** S3 does not edit `python_floor.py` (spec :48). Line :36 of `python_floor.py` already routes bare `bash` through `resolve_shell_argv`. The spec's own `l2_probe.py` run at `cbaaeebeb`, before the build, printed `verdict failed rc 127 | Refusal in tail: False | Set GOV_BASH in tail: False`. That is exactly AC5's pass string (spec :292-293, :373-375). The probe runs only upgrade_steps' witness and never touches the new selftest arm.
- **Consequence:** AC5 is green both before and after the build. Section 7 says S3's arm "covers AC5", but AC5 does not observe that arm at all. S3's only other acceptance is AC6, a grep for the label. A `[dSP-91 L2]` check that never runs the witness, or never restores the environment, would still be accepted.
- **Fix (skeptic judged it sound):**
  - Replace AC5 with a criterion that observes the arm and fails before the build: the `[dSP-91 L2]` check's PASS line appears in the `govkit selftest` output.
  - Add a staged-red criterion: with `python_floor.py:36` changed to call `steps.resolve_bash()` directly, the selftest prints that check as FAIL with `upgrade_steps.Refusal` in its detail. This is a write probe, so the build runs it and records the result.
  - Keep the `l2_probe.py` line as a section 4 measurement, not as an acceptance criterion.
- **Left-shift gate:** Make every behavioural AC carry a recorded pre-build red. An AC whose pass string already appears in a pre-build measurement in the same spec is flagged.

### M3. The `[dSP-91 L2]` check asserts only absences, so it goes green on failures that never reach bare bash (id 11)

- **Where:** TOOL-dSafePassage-91 spec, section 2 S3 and section 4 "S3: the floor stub's fallback".
- **What is wrong:** The check is only `"upgrade_steps.Refusal" not in tail and "Set GOV_BASH" not in tail`. Several failures stop before the bare-bash line at `python_floor.py:36`, and each leaves a tail with neither string:
  - the stub's own `resolve_kit_dir` LookupError exit (`python_floor.py:31-35` prints `python_floor.py: ...` and returns 2);
  - a failure to import or spawn the stub;
  - a witness argv that no longer resolves.
- **Consequence:** The check is labelled "falls back to bare bash", yet it reads green while the fallback is dead. It certifies the fallback against the one staged mutation and nothing else.
- **Fix (skeptic judged it sound):** Add a positive marker that every node shares, so the check proves the stub got as far as spawning bare `bash`. For example, require `'bash' in tail or FLOOR_SCRIPT in tail`, and require that the tail does not contain `python_floor.py:`. Add a second staged break that the build must observe red: the stub's `resolve_kit_dir` made to raise LookupError.
- **Left-shift gate:** Add a checklist entry: a selftest check made only of `not in` assertions must pair them with at least one positive marker, and must stage one red for each early-exit path.

### M4. The plant-root grader samples one of the target-side kinds, so a per-kind mis-split passes (id 12)

- **Where:** TOOL-dSafePassage-91 spec, section 2 S2 and section 4 "S2: the plant-root grader".
- **What is wrong:** `upgrade_walk.py:140` picks the root (`troot`) per kind. `read_fixture_rows` serves the plant kind (:149), the condition kind (:157), the arm kind (:162) and gov_plant. The arm rows carry a nested shim `from`/`to` with `{prefix}` (arms.toml:50) and a nested plant `path` (arms.toml:70). The designed grader samples only three things: the `engine-edit` plant, the `withdraw-one` gov_plant and the policy adopter. Its red table stages only whole-expression forms of :140.
- **Consequence:** Consider the regression `troot = derive_tool_root(...) if kind in ("gov_plant", "arm") else read_target_prefix()`. It sends the held-shim arm's `{prefix}/check-kit-versions.sh` to gov's tool root and passes every grader. The existing shim-root grader (:1086-1097) uses its own row, not the arm fixture rows, so it does not catch this either. The path is narrow, and the effect is contained.
- **Fix (skeptic judged it sound):** Have the grader read one `{prefix}` row of every kind that `read_fixture_rows` maps. At minimum, add the arm rows' nested `shim.from` and `plant.path` alongside `engine-edit`. Alternatively, iterate over every kind's rows and require each resolved path to fall under its kind's expected root. Add the per-kind mutation to the staged breaks.
- **Left-shift gate:** A grader over a per-kind dispatch enumerates the dispatch's kinds and asserts one sample per kind. A kind added to `read_fixture_rows` without a sample then reads red.

### M5. The `_alias` refusal blames case folding for any filesystem alias, including links (id 13)

- **Where:** TOOL-dSafePassage-90 spec, section 2 S1 and section 4 "S1" (the `_alias` message).
- **What is wrong:** The spec computes `_alias = ndp.exists() and _own.exists() and ndp.samefile(_own)`, where `ndp = (target / new_dest).resolve()` (govkit.py:11072). `samefile` compares file identity with `os.stat` on any filesystem. So `_alias` is also set in two other cases:
  - a symlink or hard link at `new_dest` that points to the row's file, on any filesystem, case-sensitive ones included;
  - a macOS NFC/NFD alias.
  In every case the refusal prints the unconditional case-only text.
- **Consequence:** Take an adopter whose own link sits at gov's new spelling. They are told the cause is case folding, told not to move the file, and told to run `update` from a checkout on a case-sensitive filesystem. On Linux, that is the checkout they already ran. The real remedy, moving their link, is never offered, so every run holds the kit back with the wrong guidance. The refusal still fires, and no bytes are lost.
- **Fix:** The skeptic judged the finder's fix unsound and gave this corrected fix:
  - Keep `_alias = ndp.exists() and _own.exists() and ndp.samefile(_own)` as the identity test.
  - Choose the wording by whether the two spellings fold together. Where `new_dest.casefold() == row['path'].casefold()`, print the case-only text.
  - Otherwise, print a neutral alias text: "the row's own file under another name (a link or a filesystem alias); the file is untouched. If the name is a link you made, remove the link and re-run".
- **Left-shift gate:** Add a selftest arm that plants a symlink at `new_dest` on a case-sensitive filesystem and asserts that the refusal does not print the case-only text.

## Low

### L1. The two specs' ordering notes name a shared govkit.py block that does not exist (ids 3, 5)

- **Where:** TOOL-dSafePassage-90 spec, section 3 Edges (:71-72) and section 4 Rollout (:302-303); TOOL-dSafePassage-91 spec, section 3 Edges (:66-67).
- **What is wrong:** Unit 90 says 91 edits "the same `govkit.py` snapshot block", but 90 never edits the snapshot. Unit 91 says 90's S1 "edits the same `renamed` write arm", but 91 never edits that arm. In govkit.py, 90 edits only the `renamed` write arm (:11073-11114), and 91 edits only the pre-write snapshot (:10746). The two units actually overlap in two places: the `DEPL-dCarriedReceipt-11` block in selftest.py, where 91's arm sits after `[dSP-90]`, and the `_kit88` rebinding.
- **Consequence:** A builder or reviewer who scopes a merge conflict or a re-read from these edges looks in the wrong block. Behaviour is unaffected.
- **Fix (skeptic judged it sound):** In 90's section 3 Edges and section 4 Rollout, say that 91 edits govkit.py's pre-write snapshot (:10746), which 90 does not touch, and the selftest.py block after `[dSP-90]`. In 91's section 3 Edges, say that 90's S1 edits `_cmd_update`'s `renamed` write arm, which 91 does not touch, and that 91's check anchors after 90's `[dSP-90]` check. Drop "the same".
- **Left-shift gate:** Make each cross-unit edge cite a file:line range. A lint then checks that both specs' edit inventories contain that range.

### L2. S3's comment and rejected-alternative rationale misdescribe how Windows resolves bare `bash` (id 6)

- **Where:** TOOL-dSafePassage-91 spec, section 4 S3 (the check's comment, :249) and section 4 Alternatives rejected for L2 (:327-329).
- **What is wrong:** The comment says "what bare `bash` finds on this PATH". The rationale says bare `bash` with none on PATH raises a `FileNotFoundError` traceback. On Windows, the loader finds C:/Windows/System32/bash.exe, the WSL launcher, before it searches PATH, whatever PATH holds (upgrade_steps.py:372-376). That is why the measured rc was WSL's 127, not a FileNotFoundError.
- **Consequence:** A reader will believe the result depends on PATH. The assertion only looks at the tail, so the check holds either way. The defect is limited to the comment and the rationale.
- **Fix (skeptic judged it sound):** Reword the comment to "what bare `bash` resolves to (on Windows the loader's System32 WSL launcher, elsewhere PATH or nothing), and so the rc, is the node's". In Alternatives, qualify the FileNotFoundError traceback as the case on a node where no bare `bash` resolves at all.
- **Left-shift gate:** Add a checklist entry: a claim about process resolution of a bare argv cites `resolve_bash`'s docstring for the Windows loader order.

### L3. S3 adds a fourth hand-typed copy of the environment save-and-restore loop to selftest.py (id 7)

- **Where:** TOOL-dSafePassage-91 spec, section 4 "S3: the floor stub's fallback" (:250-258), and section 10's claim that S3 extends `check_step_isolation` by reuse.
- **What is wrong:** selftest.py already holds the `held = {k: os.environ.get(k) ...}` save, update and finally-restore loop three times (:3766, :4409, :4437). S3 types it a fourth time, with the same three keys as :4437. Section 10 says S3 reuses that check's fake PATH but does not mention that it re-types the restore block.
- **Consequence:** Behaviour does not change. The next change to how the floor-row checks hold the environment, such as adding a key, has to touch four copies.
- **Fix (skeptic judged it sound):** In S3, have the build add one local `@contextlib.contextmanager` to selftest.py, shaped like `measure_legs.set_environ`. Use it for `[dSP-91 L2]`, or at least for `[dSP-87 AC5]` and `[dSP-91 L2]`. Alternatively, state in section 10 why the inline copy is kept. A copy-installed kit cannot import across kits, so the helper must live in selftest.py.
- **Left-shift gate:** Add a duplicate-block counter over selftest.py's `held = {k: os.environ.get(k)` pattern that flags any new copy.

### L4. S2 does not update `check_graders`' docstring, which lists the graders it runs (id 9)

- **Where:** TOOL-dSafePassage-91 spec, section 2 S2 and section 4 "S2: the plant-root grader" (and its Inventory).
- **What is wrong:** The `check_graders` docstring (upgrade_walk.py:976-980) lists the graders the loop runs: 77 S7's four, 86's `derive_release_engine` and 87's `check_shim_paths`. S2 adds a plant-root grader but does not tell the build to update that docstring, and the spec does not mention the docstring anywhere.
- **Consequence:** After the build, the docstring under-describes what the grader loop covers. The next change that reads it to learn the set of graders misses the plant-root split. This is comment drift only.
- **Fix (skeptic judged it sound):** In S2, add one line: the `check_graders` docstring gains "and TOOL-dSafePassage-91's plant-root split: the target's plants and the policy adopter at the install prefix, gov plants at a moved tool root".
- **Left-shift gate:** Add a selftest that checks every grader name registered in `check_graders` is mentioned in its docstring.

### L5. The grader's bare `next(...)` raises StopIteration past the loop (id 14)

- **Where:** TOOL-dSafePassage-91 spec, section 4 "S2: the plant-root grader" (:207-208), against section 5's error states.
- **What is wrong:** The grader reads its two fixture rows with `next(...)` and no default. If `engine-edit` or `withdraw-one` is missing from the fixture, StopIteration escapes. The grader catches only LookupError, the grader loop (upgrade_walk.py:1107) catches `(Stop, OSError, KeyError, ValueError)`, and the outer handler (:1207) catches `Stop`. None of these catch StopIteration. Section 5 claims the grader returns a red string "rather than raising past the loop".
- **Consequence:** upgrade_walk ends with a traceback instead of the named `grader · plant-root · RED` line. The leg still fails, so only diagnosis suffers.
- **Fix (skeptic judged it sound):** Use `next((...), None)` and return a red string that names the missing fixture row, or catch StopIteration beside LookupError in the grader.
- **Left-shift gate:** Add a checklist entry: a grader's fixture lookups use a default and return a named red. A selftest feeds a fixture with one row removed and asserts that the red line appears.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=14 confirmed=14 refuted=0 unverified=0 blocker=0 high=0 medium=8 low=6 agents=11 out-tokens=106673

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 6 AC4 | medium | medium | confirmed | Both spec blobs match their pins. `grep -n -F "derive_policy_adopter(t)"` on the 91 spec printed line 187 `def derive_policy_adopter(t) -> pathlib.Path:`, line 195 (the call in build_release_tree), line 210 (`pol = derive_policy_adopter(t)` in check_grade_plant_root) and line 368 (AC4 itself). The `def` line contains the fixed string, so if S2 is built as §4 shows it, AC4's `git grep -n -F` over upgrade_walk.py prints three lines. AC4 says 'prints two lines' (spec:368-369), so a correct build reads red. | sound | - |
| 2 | coherence | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 6 AC5 (and section 2 S3, section 7 third New arm) | medium | medium | confirmed | The 91 spec at lines 292-293 records l2_probe.py run over `git archive cbaaeebeb tools`, which is before the build. It printed `verdict failed rc 127 \| Refusal in tail: False \| Set GOV_BASH in tail: False`, and that is exactly AC5's pass string (spec:373-375). Line 48 says python_floor.py is not edited. python_floor.py:36 already reads `subprocess.run(steps.resolve_shell_argv(["bash", ...]))`. The probe runs only upgrade_steps' witness and never touches the new selftest arm, so AC5 is green before and after the build and cannot observe S3. §7's arm line (spec:390) claims it 'covers AC5'. The only other check on the arm is AC6, a label grep. | sound | - |
| 3 | coherence | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-90.md:section 3 Edges and section 4 Rollout (with TOOL-dSafePassage-91 section 3 Edges) | low | low | confirmed | The 91 spec at lines 66-67 says that 90's S1 'edits the same `renamed` write arm'. 91 cites govkit.py only at :10746 / :10745-10747 (the snapshot `_paths` block, spec:30, 78, 414) and never cites the write arm at :11062-11114. The 90 spec at 71-72 and 302-303 says 91 edits 'the same govkit.py snapshot block'. 90 cites the snapshot only in its rejected fork (a) (spec:83), while its S1 edits :11073-11079 and :11109 (spec:136, 396). sed of govkit.py:10744-10748 shows the snapshot block, which is separate from the renamed arm. Neither edge names a govkit.py region the two units actually share. The real overlap is the selftest block. Only the stated reason is wrong; behaviour is unaffected. | sound | - |
| 4 | grounding | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 6 AC4 (against section 4 "S2: the plant-root grader") | medium | medium | confirmed | Both spec blobs match their pins. In the 91 spec, line 187 tells the builder to write `def derive_policy_adopter(t) -> pathlib.Path:`. Line 195 has the call `derive_policy_adopter(t).as_posix()` in build_release_tree, and line 210 has `pol = derive_policy_adopter(t)` in the grader. All three contain the fixed string that AC4 greps for (`git grep -n -F "derive_policy_adopter(t)"`). AC4 at :368-369 says the grep prints two lines. Built exactly as section 4 says, it prints three, so a correct build reads AC4 red. The second grep in AC4 is unaffected. The effect is contained to a criterion that misreads a correct build. | sound | - |
| 5 | grounding | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-90.md:section 3 Edges and section 4 Rollout (and TOOL-dSafePassage-91 section 3 Edges) | low | low | confirmed | The 90 spec at :302-303 says 91 edits 'the same `govkit.py` snapshot block'. At :71 it says 91's L1 fix edits 'the same snapshot block'. But 90's S1 (:30-37) edits only the renamed write arm: own_file at govkit.py:11078 and :11109, plus the comment at :11073-11076. 90 only names the snapshot at :10745-10747 in a rejected alternative (:83). The 91 spec at :66 says 90's S1 'edits the same `renamed` write arm'. But 91's S1 (:78-83) edits the snapshot at govkit.py:10746, which `sed -n 10740,10750p` confirms is the `_paths.append(a["c"]["renamed_to"][1])` line. So the two specs share no govkit.py block, only the selftest block. The effect is that the ordering prose misleads; behaviour is unaffected. | sound | - |
| 6 | grounding | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 4 S3 (the check's comment) and section 4 Alternatives rejected (L2) | low | low | confirmed | tools/govkit/steps/python_floor.py:38 passes `["bash", ...]` through resolve_shell_argv. The resolve_bash docstring at upgrade_steps.py:372-376 records that on Windows the loader finds C:/Windows/System32/bash.exe, the WSL launcher, before PATH, whatever PATH holds. That is why the spec measured WSL's rc 127 and not a FileNotFoundError. So the comment at 91:249 ('what bare `bash` finds on this PATH') and the rationale at :327-329 ('none on `PATH` raises a `FileNotFoundError`') are wrong for a Windows node with WSL installed. The check's assertion only looks at the tail, so it holds either way, and the effect stays in the comment and the rationale. | sound | - |
| 7 | reuse | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 4 "S3: the floor stub's fallback" (and section 10's claim that S3 extends check_step_isolation by reuse) | low | low | confirmed | The spec file hashes to the pinned blob 7bb7372e. I grepped tools/govkit/*.py for `held = {k: os.environ.get(k)` and found three existing copies, at selftest.py:3766, :4409 and :4437. selftest.py has no local contextmanager or set_env helper. Spec §4 S3 (lines 250-258) types the same held/update/finally-restore loop as :4437 with the same three keys. §10 says S3 extends check_step_isolation 'reusing its fake PATH' and does not mention the re-typed restore block. The claim is true. The consequence is duplication only, and behaviour does not change, so the grade is low. | sound | - |
| 8 | blast-radius | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 6 AC4 (against section 4 "S2: the plant-root grader") | medium | medium | confirmed | §4 S2 puts three lines into upgrade_walk.py that contain the fixed string `derive_policy_adopter(t)`. They are spec line 187 `def derive_policy_adopter(t) -> pathlib.Path:`, line 195 `derive_policy_adopter(t).as_posix()` in build_release_tree, and line 210 `pol = derive_policy_adopter(t)`. AC4 (line 368) says the git grep prints two lines, so a build done exactly as S2 writes it prints three and fails AC4. The second grep still catches the inline regression, so the damage stays inside the criterion. | sound | - |
| 9 | blast-radius | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 2 S2 / section 4 "S2: the plant-root grader" (and its Inventory) | low | low | confirmed | upgrade_walk.py:976-980 holds the check_graders docstring. It lists 77 S7's graders, 86's derive_release_engine and 87's check_shim_paths, and then says 'returns the reds'. Grepping the spec for 'docstring' finds nothing, and §4 S2 adds the plant-root grader without telling the build to update that docstring. Once built, the docstring under-describes what the grader loop covers. That is a comment-only drift, so the grade is low. | sound | - |
| 10 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 6 AC4 | medium | medium | confirmed | The spec file hashes to the pinned blob 7bb7372e. `grep -n -F "derive_policy_adopter(t)"` on it matches the designed `def derive_policy_adopter(t) -> pathlib.Path:` (spec :187), the argv call in build_release_tree (:195) and `pol = derive_policy_adopter(t)` in check_grade_plant_root (:210). §4 S2 puts the def in upgrade_walk.py next to derive_release_engine. So a correct build prints three lines in that file, and AC4 (:368-369) says it prints two. AC4 fails on a correct build. Only this criterion is affected. | unsound | - |
| 11 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 2 S3 / section 4 "S3: the floor stub's fallback" | medium | medium | confirmed | I read tools/govkit/steps/python_floor.py:31-35. When resolve_kit_dir raises LookupError the stub writes `python_floor.py: {e}` and returns 2, and it never reaches the resolve_shell_argv/bare-bash line at :36. The [dSP-91 L2] check in spec §4 S3 is only `"upgrade_steps.Refusal" not in tail and "Set GOV_BASH" not in tail`, which §2 S3 also states, with no positive term. That stub exit, a stub spawn or import failure, or a stale witness argv would each leave a tail without those strings, so the check reads green while the label says the stub 'falls back to bare bash'. The harm is contained: one check over-certifies. | sound | - |
| 12 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 2 S2 / section 4 "S2: the plant-root grader" | medium | medium | confirmed | upgrade_walk.py:140 chooses troot per kind, and read_fixture_rows serves plant (:149), condition (:157), arm (:162) and gov_plant. arms.toml:50 has a nested shim with `{prefix}` from/to, and :70 has a nested plant path. The designed check_grade_plant_root (spec §4 S2) samples only the engine-edit plant, the withdraw-one gov_plant and the policy adopter. Its red table stages only whole-expression forms of :140. The existing shim-root grader (:1086-1097) exercises check_shim_paths with its own row, not arm fixture rows. So a split such as `kind in ("gov_plant","arm")` would pass every grader. This is a narrow regression path, and the effect is contained. | sound | - |
| 13 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-90.md:section 2 S1 / section 4 "S1" (the `_alias` message) | medium | medium | confirmed | Both blobs match their pins. Spec 90 section 4 S1 computes `_alias = ndp.exists() and _own.exists() and ndp.samefile(_own)` with no case-only guard, and govkit.py:11072 has `ndp = (target / new_dest).resolve()`. `samefile` compares os.stat identity in any case. So a symlink or hard link at new_dest that points to the row's file sets `_alias` on any filesystem, and so does a macOS NFC/NFD alias. The refusal then prints the unconditional case-only text from S1 ('as a case-only rename is on a case-insensitive filesystem ... run `update` from a checkout on a case-sensitive filesystem') and leaves out the occupied-destination remedy. The refusal still fires and no bytes are lost. The only defect is the guidance in the message, so it is contained, and the path is narrow. | unsound | - |
| 14 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-91.md:section 4 "S2: the plant-root grader" / section 5 error states | low | low | confirmed | Spec 91 section 4 S2 lines 207-208 read the two rows with bare `next(...)` and no default. The grader itself catches only LookupError, and StopIteration is not a LookupError. The grader loop at upgrade_walk.py:1107 catches (Stop, OSError, KeyError, ValueError), and the only outer handler, at :1207, catches Stop. So a fixture without `engine-edit` or `withdraw-one` raises StopIteration and ends in a traceback rather than the `grader · plant-root · RED` line. That contradicts section 5's claim that the grader returns a red string 'rather than raising past the loop'. The leg still fails, so only diagnosis suffers. | sound | - |
