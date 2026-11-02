**Serves:** spec-audit TOOL-dSafePassage-84@rev-2

# Tier-2 review: TOOL-dSafePassage-84 spec audit, round 1

Provenance: a round-1 adversarial spec audit of TOOL-dSafePassage-84 (rev-2). The unit was adopted at dSafePassage's close because TOOL-dSafePassage-78 (460ffb587) made `govkit update --write` walk no step over a receipt below schema 3, while the read-only preview still prints `would walk`. Unit 84 makes both sites read one predicate, `derive_walk_hold`, defined once inside `_cmd_update` in tools/govkit/govkit.py. It builds before TOOL-dSafePassage-81, which renames last. Roles: the finders were gov-spec-reviewer, the skeptic batches gov-skeptic, and the synthesis gov-synthesizer.

Reviewed: memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md@39de3d49b85c8ce582476881326932f3fecc3fb2

ROUND: 1

## Verdict: CLEAN WITH FIXES

There are no blockers and no highs. One medium item and five low items remain, and each is a spec edit to make before the build. The tally is 6 items by item and 8 raw confirmed findings (medium 1, low 7). Two merges account for the difference: ids 2 and 8 are one defect, and so are ids 3 and 7.

Review shape: intensity full, raw 9, confirmed 8, refuted 1, unverified 0 (0 uncertain), precision 0.89.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| coherence | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| grounding | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| reuse | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |
| blast-radius | yes | 3 | 2 | 1 | 0 | 0 | 0.67 |
| failure-envelope | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |

Run integrity:
- Lenses: 5/5 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Demotions and discards: 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 6 judged sound, 2 judged unsound, 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 1 re-graded by the skeptic (id 5, medium to low).
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: no spec was supplied as intent. `context` was the caller's statement.
- By design: the caller's byDesign.
- Move check: no checked subject moved.
- Checklist: none was swept, because none exists. A zero count here is not evidence that the project's recurring bug classes are absent.

## Medium

### M1. No criterion watches the findings branch the predicate takes over (id 1)

- **Where:** the spec, section 2 S1 and S3, read against section 6 (AC1 to AC5) and the section 7 New arm.
- **What is wrong:** S1 moves the write run's findings hold (`if findings: return f"this run already has {findings} finding(s)"`) into `derive_walk_hold`, and S3 passes it `len(r.problems)`. No criterion and no existing arm checks that branch:
  - AC1 only counts call sites.
  - AC2 and AC3 plant no finding.
  - AC4 and AC5 are greps.
  - The S4 arm covers only the schema-2 case.
  - The only line that produces `this run already has <n> finding(s)` is govkit.py:11718, and nothing outside govkit.py asserts on it.
- **Consequence:** S3 rewrites the guard from TOOL-dSafePassage-2 S4 §8 F3: a write run that already has a finding must walk no step. A build could drop the findings test, put it in the wrong place, or pass 0 at the write site. Then `update --write` walks upgrade steps over a run that already has a finding, and every criterion and gate stays green.
- **Fix (skeptic judged it sound):** Add a criterion, or extend the S4 arm, that runs `update --write` over a schema-4 receipt with one non-refusal finding planted. A drifted row that records a problem without exiting early would do. The check asserts that the run prints `steps: not walked — this run already has 1 finding(s)` and spawns no step. It goes red when S3 passes 0 or the predicate skips `findings`. The build stages that red by changing the S3 call to `derive_walk_hold(0)` and watching the arm fail.
- **Left-shift gate:** add a bug-class checklist entry: when a spec moves an existing guard into a shared helper, each branch of the moved guard needs a criterion that goes red when that branch is dropped.

## Low

### L1. AC1's third grep cannot match as written (ids 2, 8)

- **Where:** the spec, section 6 AC1, third grep.
- **What is wrong:** AC1 says `git grep -c -F "a --kits run walks no step" -- tools/govkit/govkit.py` prints `1`, and its red-when clause says `2`. With a pathspec, `git grep -c` prints `<path>:<count>`. At HEAD the command prints `tools/govkit/govkit.py:2`, so a correct build prints `tools/govkit/govkit.py:1`.
- **Consequence:** read literally, the criterion can never pass. A builder or verifier then reads a correct build as red, or loosens the check by hand. What the check is meant to test (one copy of the reason) is unaffected.
- **Fix (skeptic judged both proposals sound):** State the expected output as `tools/govkit/govkit.py:1` and the red as `tools/govkit/govkit.py:2`. Alternatively, use `git grep -h -c`, which prints a bare count, or pipe the output through `cut -d: -f2`.
- **Left-shift gate:** have the spec-token checker run each criterion's command at the base and compare the form of its output with the stated expectation.

### L2. The help bullet's opening sentence stays unconditional (ids 3, 7)

- **Where:** the spec, section 2 S5 and section 4 "The page" (the read-only bullet at help/upgrade-steps.md:227-234).
- **What is wrong:** S5 only adds a sentence after :233-234. The opening sentence at :228-229 still says, without exception, that `update` without `--write` "prints `would walk <id>` for each pending step". After the build, that is false for a receipt below schema 3.
- **Consequence:** the user-facing page contradicts itself within one bullet. AC4 only checks that the new sentence exists, so it passes while the false lead sentence stays. This affects the docs only. The bullet already follows a rule-then-exception pattern for `--kits`, which softens the contradiction.
- **Fix:** the skeptic judged id 3's fix sound and rejected id 7's fix. The corrected fix below covers both:
  - Have S5 also narrow the lead sentence at help/upgrade-steps.md:228-229, e.g. "prints `would walk <id>` for each pending step a write run would walk". Keep that phrase on one source line.
  - Extend AC4 with a positive check: `git grep -n -F "for each pending step a write run would walk" -- help/upgrade-steps.md` prints one line, and is red when it prints nothing.
- **Left-shift gate:** add a checklist entry: a spec that appends an exception to a prose rule must also re-read and narrow the rule's own sentence.

### L3. AC2's `--kits` clause is already green at the base (id 4)

- **Where:** the spec, section 6 AC2, second clause (`preview_probe.py 2 --kits check-wiring`).
- **What is wrong:** at HEAD, the preview's `elif kits:` arm (govkit.py:10603-10605) and the write branch (:11715-11721) print the same reason text with the same `· N pending` suffix. That half of AC2 passes before any of S1 to S3 is built, so it cannot fail. AC2's own red-when clause names only the schema-2 run.
- **Consequence:** the clause looks like evidence that the `--kits` path now goes through the shared predicate, but it passes whether or not the preview calls `derive_walk_hold`. Only AC1's greps can go red for the `--kits` site. AC1's first two greps catch a preview that keeps its `elif kits:` arm inline, so the gap is contained.
- **Fix (skeptic judged it sound):** Mark AC2's `--kits` clause as a regression check that is green at the base, and say that AC1's greps are what can go red for the `--kits` site. Or drop the clause and leave the `--kits` case to AC1. If the clause stays, the build runs it once with a staged preview that keeps its own `elif kits:` arm, sees it still pass, and records in §7 that AC2 does not cover this case.
- **Left-shift gate:** require every criterion's red to be staged and observed at the base before the build. A clause that is green at the base without any staging is then flagged.

### L4. A scratch probe stands in for the gated update fixture (id 5)

- **Where:** the spec, section 4 "The probe", section 6 AC2 and AC3, and section 10.
- **What is wrong:** the preview's `--kits` hold is checked only by a scratch `preview_probe.py`. An existing gated fixture family already covers this kind of check: `upgrade_steps.py fixture update` (`run_update_fixture`, upgrade_steps.py:4369), driven by the plant table in the govkit selftest. Section 10 does not name it. Its `scoped` plant runs `--kits demo --write`, so it reaches only the write site.
- **Consequence:** once the unit lands, no gate covers a read-only `--kits` update's steps line. A preview-local arm placed ahead of the predicate call could then break the `--kits` hold with every gate green. Shipped behaviour is unaffected; only regression coverage is thin.
- **Grade:** low, as the skeptic re-graded it (the finder said medium). The read-only walking case is already gated: the `read-only` plant asserts `would walk fx/s1` and `would walk fx/s2` (upgrade_steps.py:4426-4429, selftest row :4521). The new [dSP-84 AC2] arm also forces the preview to call the predicate.
- **Fix:** the skeptic rejected the finder's fix. The corrected fix:
  - Add one plant, `scoped-read-only`, to `UPDATE_PLANTS` (upgrade_steps.py:3627).
  - In `run_update_fixture`, give it its own branch, or widen the `plant in ("read-only", "scoped")` branch, so that `--kits demo` is passed without `--write`.
  - The plant expects a line that starts `govkit update — steps: not walked — a --kits run walks no step` and ends `· 2 pending`, with no `would walk` and no canaries.
  - Add the matching `("update", "scoped-read-only", 0, (...))` row to the table at selftest.py:4520-4535.
  - Restate AC2's `--kits` half against `python tools/govkit/upgrade_steps.py fixture update --plant scoped-read-only`.
  - Name `run_update_fixture` in section 10, and add tools/govkit/upgrade_steps.py to Files touched.
  - Leave the walking case to the existing gated `read-only` plant.
  - Leave the schema-2 case to S4's [dSP-84 AC2] arm, because `build_update_gov` has no below-3 option.
  - Stage the red by placing a preview arm ahead of the predicate call, with no `elif kits:` hold of its own, and watch the new plant fail.
- **Left-shift gate:** add a checklist entry: a spec whose criteria run a scratch harness must name the gated fixture family it considered extending, or say why none fits.

### L5. The page and the docstring promise parity that F1-A does not deliver (id 9)

- **Where:** the spec, section 4 "The page" (S5), section 4 "S1: the predicate" (its docstring), and section 1 ("the two cannot drift again").
- **What is wrong:** S5's sentence ("A read-only run over such a receipt prints the same `steps: not walked` line") and the docstring ("so the preview cannot list a step the write run would not walk") are both false under the spec's own §8 F1-A, where the preview passes `derive_walk_hold(0)`. Two cases break them:
  - A schema-1 receipt that trips the role-distrust arm. It records its finding at govkit.py:10067-10070, before the preview at :10586. The preview then prints the schema reason. The write run prints `this run already has 1 finding(s)`, and because the run has a finding it does not re-stamp the receipt (:12726-12730).
  - A receipt at schema 3 or above with a finding. The preview still prints `would walk`, while the write run walks nothing.
- **Consequence:** the help page and the code comment both say the preview and the write run match, and on the findings path they do not. The operator sees two different lines while the page says they are the same. The next unit that reads the docstring trusts a guarantee the code does not give. The effect is limited to the docs and a comment. The difference between preview and write run is itself F1-A, by design, and is not the defect here.
- **Fix (skeptic judged it sound):** Narrow all three texts to what F1-A delivers:
  - S5: "A read-only run over such a receipt with no finding prints the same `steps: not walked` line, and no `would walk`." Alternatively, say that the read-only line names the schema even when a write run would name its findings first.
  - The docstring: "…so the preview cannot list a step the write run would not walk for `--kits` or for the schema; the preview passes no findings (§8 F1)."
  - Section 1's "the two cannot drift again": the same qualifier.
- **Left-shift gate:** add a checklist entry: when a spec chooses a by-design divergence (an F-option), sweep its prose, page text and docstrings for claims that deny that divergence.

review-shape kind=spec-audit round=1 intensity=full at=synth raw=9 confirmed=8 refuted=1 unverified=0 blocker=0 high=0 medium=1 low=7 agents=11 out-tokens=72982

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | coherence | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md:section 2 S1 / S3 against section 6 (AC1-AC5) and section 7 New arm | medium | medium | confirmed | The spec blob is 39de3d49 as pinned. S1 moves the findings test into derive_walk_hold and S3 passes len(r.problems) into it. I read AC1-AC5: AC1 only greps for call sites and the --kits phrase, AC2 and AC3 run the probe with no finding planted, AC4 and AC5 are greps, and the S4/New arm covers only the schema-2 case. I ran `git grep -n -e "finding(s)" -e "not walked" -- tools/govkit/` without govkit.py. It found only selftest.py:4523 and upgrade_steps.py:4431-4432, which are both the --kits line, plus an unrelated shims.py line. Nothing checks `this run already has <n> finding(s)`. The only producer is govkit.py:11718. So a build that drops the findings branch, or passes 0 at the write site, passes every criterion and every gate. The write run would then walk steps over a run that already has a finding. That is a real regression on a contained path, so medium. | sound | - |
| 2 | coherence | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md:section 6 AC1, third grep | low | low | confirmed | I ran `git grep -c -F "a --kits run walks no step" -- tools/govkit/govkit.py`. It printed `tools/govkit/govkit.py:2`, so the output carries the path prefix and AC1's literal `1` (and its red `2`) can never match exactly. The intent is clear and behaviour is unaffected, so low. I also ran `git grep -h -c ...`, which printed a bare `2`, so either form of the fix gives a literal match. | sound | - |
| 3 | coherence | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md:section 2 S5 / section 4 "The page" | low | low | confirmed | I read help/upgrade-steps.md:227-234. The bullet opens with 'Without `--write`, `update` prints `would walk <id>` for each pending step and runs none of them', and 78's schema-3 sentence sits at :233-234. The spec's §4 'The page' (blob 39de3d4) only appends 'A read-only run over such a receipt prints the same `steps: not walked` line, and no `would walk`.' S5 does not change the opening sentence. After the build, the unconditional opening clause is no longer true for a receipt below schema 3. One mitigating point: the bullet already uses a rule-then-exception pattern for `--kits`, so a reader can take the new sentence as one more exception. This affects the docs only, so it is low. | sound | - |
| 4 | grounding | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md:section 6 AC2 (second clause, `preview_probe.py 2 --kits check-wiring`) | low | low | confirmed | I re-read tools/govkit/govkit.py:10603-10605. The preview's `elif kits:` prints 'steps: not walked — a --kits run walks no step, since a subset would run a later step before an earlier one · {len(_sw_pending)} pending'. At :11715-11721 the write branch checks `kits` first and prints the same text with the same suffix. Both sites set `_sw_pending` with the same expression (:10598, :11711). `git grep -c -F "a --kits run walks no step"` printed `tools/govkit/govkit.py:2`. `git diff --stat 460ffb587 HEAD` over govkit.py, selftest.py and the help page printed nothing. So at the base, the `--kits` run already prints no `would walk` and two equal `steps:` lines. AC2's second clause therefore cannot go red, and its own 'Red when' names only the schema-2 run. AC1's greps are what catch an inline `elif kits:`, so the effect is contained. | sound | - |
| 5 | reuse | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md:section 4 "The probe" / section 6 AC2-AC3 / section 10 | medium | low | confirmed | The claim mostly holds but the impact is overstated. Confirmed: section 10 of blob 39de3d49 names only derive_unclaimed_candidates, rs-ac2/run and build_target. AC2's --kits half rests only on the scratch preview_probe.py. Nothing gated covers a read-only --kits update's steps line. run_update_fixture (upgrade_steps.py:4369) runs the 'scoped' plant as `--kits demo --write` (:4423), so it reaches only the write site. The selftest's one read-only --kits run (selftest.py:17624) asserts scope lines and no steps line. Refuted part: the claim that 'a read-only run that still walks' is lost. The gated 'read-only' plant (upgrade_steps.py:4426-4429, selftest row :4521) runs over the fixture's schema-4 receipt and asserts both `would walk fx/s1` and `would walk fx/s2`. A preview that held a run it should walk would turn that row red. What is really left is narrow. Both sites call one shared predicate that tests kits first, and the new [dSP-84 AC2] arm forces the preview to call it. So only a preview-local arm placed ahead of the predicate could break the --kits hold with every gate green. Shipped behaviour is unaffected and only regression coverage is thin, so I grade it low. | unsound | - |
| 6 | blast-radius | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md:section 7 (Gates), joined against section 4 "Files touched" | medium | - | refuted | The legs are real, but section 7 does not owe them. My python join over tools/gate-legs.json against the three files touched found the same 11 legs (the finding says '12', then lists 11). Each one matches only through the guard `{prefix}/`. Every other guard on those legs is `{prefix}/lib/`, `.githooks/`, `.claude/` or `{prefix}/gate-legs.json`, and none of those trips a govkit or help path. `{prefix}/` is carried by 12 legs, above BROAD_LEG_FLOOR = 5 (tools/check-spec-tokens.py:368). memory/TEMPLATE-SPEC.md:264-275 excludes such a broad guard from what the leg line must name. It says 'a rule that owes a shared guard's every leg per spec is obeyed by paste', and derive_guarded_legs (check-spec-tokens.py:599-618) drops broad guards in code. So the leg line meets the template's rule, and the omission is the protocol's own design. Every leg named in section 7 resolves to a real leg. The bar still runs the guarded legs, so this names no defect the rubric grades (case 6). | unsound | - |
| 7 | blast-radius | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md:section 2 S5 / section 4 "The page" (help/upgrade-steps.md read-only bullet) | low | low | confirmed | I re-read help/upgrade-steps.md:228-229. It says without qualification that a read-only `update` "prints `would walk <id>` for each pending step". S5 (spec :48-49) and section 4 "The page" (:159-161) only add a sentence after :233-234, and AC4 (:292-295) only greps for that new sentence. Once built, the bullet's lead sentence is false for a receipt below schema 3, and the later sentence corrects it. The effect stays inside the help page, so this is low. | unsound | - |
| 8 | blast-radius | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md:section 6 AC1, third grep | low | low | confirmed | I ran `git grep -c -F "a --kits run walks no step" -- tools/govkit/govkit.py`. It printed `tools/govkit/govkit.py:2` (hits at :10604 and :11717), not a bare count. AC1 (spec :273) says the green state prints `1` and the Red-when clause (:275) says `2`, but the real output will be `tools/govkit/govkit.py:1`, so the criterion cannot match as literally written. The intended check is clear and nothing ships wrong, so this is low. | sound | - |
| 9 | failure-envelope | memory/builds/dSafePassage/spec/2026-10-29-spec-TOOL-dSafePassage-84.md:section 4 "The page" (S5) and section 4 "S1: the predicate" docstring | low | low | confirmed | I read the pinned blob and the cited code, and both claims hold. At govkit.py:10067-10070, with `schema < 2`, `r.fail(... a schema-1 receipt cannot be trusted about)` runs before the preview's `if not write:` at :10586. Under §8 F1-A the preview passes `derive_walk_hold(0)`, so for that receipt it prints the schema reason. The write run passes `len(r.problems)`, which is at least 1, so it prints `this run already has 1 finding(s)` (the order is kits, then findings, then schema). At :12730 a run with findings is NOT re-stamped. So S5's 'prints the same `steps: not walked` line' is false for a schema-1 receipt that has a role-distrust finding. The docstring's 'the preview cannot list a step the write run would not walk' is also false under F1-A: for a receipt at schema 3 or above with a finding, the preview still prints `would walk` (§8 F1 A says so itself: 'keeps `would walk` when it already has a finding') while the write run walks nothing. The same overclaim sits in §1 ('the two cannot drift again'). BY DESIGN covers the divergence, not the texts that deny it. The spec does not already qualify them: §3 and §8 state F1-A, but S5 and the docstring stay unqualified. AC2 checks equality only in the clean schema-2 case. The consequence is limited to a help page and a code comment, so the grade is low. | sound | - |
