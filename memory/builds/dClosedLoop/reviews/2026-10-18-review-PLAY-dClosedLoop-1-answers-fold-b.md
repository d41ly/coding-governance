**Serves:** diff-review PLAY-dClosedLoop-1

# Review B: the away pass's answers folded, round 1

Tier-2 adversarial diff review, run B of two independent runs on the same diff. Round 1. Finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.

Range: a9b00addda62eb4d3b3dd5fc77b9dff3139a9cc4...fe3d09aba3a34e46d1651a941af94f3772c99b0d

## Verdict: CLEAN WITH FIXES

There are no blockers. There is one high: the PEP 701 ban is retired at unit 14, while nothing outside `update` refuses a below-floor interpreter until unit 95. Eight medium findings and three low findings follow it. Every fix below is a record edit to the design, and none needs a code change before the chain builds start.

Review shape: intensity light, raw 17, confirmed 12, refuted 5, unverified 0 (0 uncertain), precision 0.71. Adjudicated tally by item: 11 items (0 blocker, 1 high, 7 medium, 3 low). By raw confirmed finding: 12 (0 blocker, 1 high, 8 medium, 3 low). Findings 8 and 13 describe one defect and form one item.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| correctness | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| seams | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| verification | yes | 5 | 2 | 3 | 0 | 0 | 0.40 |

## Run integrity

- Lenses: 3/3 returned, 0 died.
- Skeptic batches: 5/5 returned, 0 died.
- Verdicts: 0 contradictory demoted to unverified, 0 spurious discarded, 0 duplicates.
- Fixes on confirmed findings: 11 judged sound, 1 judged UNSOUND (finding 13, whose skeptic-corrected fix is written below), 0 none proposed, 0 not judged.
- Severity: 0 ungraded by the skeptic, 2 re-graded by the skeptic (findings 8 and 13, both high to medium).
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intensity is light. The security and intent lenses were NOT run. Their classes were swept only through the checklist shares, so this is not a full review.
- Intent: 27 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 19 items, each assigned to exactly one lens (correctness 7, seams 6, verification 6).
- By design: the caller's byDesign.

## Findings

### HIGH

#### H1. The PEP 701 ban is retired 81 units before anything refuses a below-floor interpreter (id 1)

- **Where:** memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1392 (dSafePassage clause 6), and interpretation 5 at memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:552.
- **What is wrong:** dSafePassage's floor step retires the PEP 701 text ban in `merge-rows.test.sh`. Interpretation 5 says every later build "may rely on 3.15". Outside `update`, the only clause that refuses an interpreter below the floor is the resolver arm in dWitnessedBar clause 24. dSafePassage finishes at unit 14 and dWitnessedBar at unit 95. The step's own preflight runs only on the node that runs `update`.
- **Consequence:** `tools/lib/resolve-python.sh` accepts any candidate whose `-c 'import sys'` exits 0, so it imposes no version floor. The research measured nodes at 3.12, 3.14 and WSL 3.10, and none at 3.15. Between units 14 and 95, code written to 3.15, or a PEP 701 escape in the merge driver, runs unrefused on a below-floor node. `merge-rows.test.sh:347-352` states what then happens: the driver exits non-zero without writing %A, and git leaves OURS-only content with no conflict markers. That is a silent loss of merge content.
- **Fix (judged sound by the skeptic):** Move the resolver's refusal below the declared floor into dSafePassage's floor step. It reads from the floor's one declaration and is seen red on a planted below-floor interpreter. Leave dWitnessedBar clause 24 its real-interpreter arm. If that is not done, keep the PEP 701 ban until dWitnessedBar lands, and narrow interpretation 5 so that later builds may rely on 3.15 only after the resolver refuses below it.
- **Left-shift gate:** add a chain-order check. When a clause retires a guard, the clause that replaces it must sit on the same build or on an ancestor that finishes no later.

### MEDIUM

#### M1. Gov's own remote CI bar never gets a Python at the 3.15 floor, and gap-tool-21's CI fact has no closing clause (ids 8, 13)

- **Where:** architecture-v2.md:1392 (dSafePassage's floor clause), architecture-v2.md:1404 (dWitnessedBar's row, which owns gap-tool-21), and memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:216.
- **What is wrong:** dSafePassage declares the floor once, at 3.15, at unit 14, and every reader reads that declaration. No clause anywhere in the chain sets up a 3.15 interpreter for `.github/workflows/remote-ci.yml`. That workflow runs `windows-latest` (lines 47, 88, 126, 277), has no setup-python step, and uses whatever `resolve-python.sh` finds.
  - gap-tool-21 is new in this diff. It records "remote CI sets up no Python" and is owned by dWitnessedBar. That build's floor arm runs a real interpreter but names no CI provisioning.
  - dShippedRelease's "Linux job in emitted CI" covers adopters' emitted CI, not gov's own workflow.
- **Consequence:** From unit 14 to unit 95, and with no clause that ends it, gov's merge bar runs below the floor gov has just declared for itself. Either the bar goes red on every push, or it passes gov's tree on an interpreter the floor refuses. This did not happen under the 3.11 floor.
- **Grade:** Both finders graded this high and the skeptics re-graded both to medium. Once readers refuse below the floor, a sub-floor runner turns the bar red loudly instead of certifying something wrong, and the gap is registered.
- **Fix (finding 8's fix judged sound; finding 13's judged UNSOUND, and this is its skeptic's corrected fix, not the rejected one):**
  1. Add a clause to dSafePassage's floor step: in the unit that raises the floor, the jobs in `remote-ci.yml` set up Python at the floor, read from its one declaration. The floor preflight runs as the bar's first step and is seen red on a planted below-floor interpreter.
  2. Split gap-tool-21's remote-CI fact into a new gap owned by dSafePassage, and leave the rest of gap-tool-21 with dWitnessedBar, so that each gap is still owned exactly once.
  3. Probe: re-run the gap-ownership join and check that every fact in each gap names a clause on its owner's row.
- **Left-shift gate:** make the gap-ownership join check facts, not only gaps. Each fact in a gap's text must cite a clause on the owner row that closes it.

#### M2. The AP-33 correction and gap-tool-20 leave out the stop guard's bare `bash` spawn (id 3)

- **Where:** away-pass.md:539 (the AP-33 correction), gap-register.md:215 (gap-tool-20), and dWitnessedBar clause 26 in architecture-v2.md.
- **What is wrong:** The correction and the gap both say the wrong-shell class reaches WSL only through govkit's fall-back and seven PATH-only resolver copies. That census covered `.py` files only.
  - `tools/unattended/stop-guard.js:111` runs `spawnSync('bash', [driver, '--liveness', slug], …)`.
  - Dispatch 113 measured that site (the `nodebash.js` row) at 5.1.16, WSL, under a clean PATH.
  - v2 never names the stop guard, and clause 26 scopes its fix as "replacing the seven copies of the loop".
- **Consequence:** On a fresh-terminal PATH, the liveness check keeps reaching WSL bash. The gap understates the class, and the correction narrows the owner's AP-33 question on an incomplete census.
- **Fix (judged sound by the skeptic):** Add `stop-guard.js:111`, and every other bare `bash` spawn that a census over tracked `.js` files finds, to gap-tool-20 and to the correction. Make clause 26's population every bare-bash launch site found by query, never a typed count of seven.
- **Left-shift gate:** add a bug-class checklist entry: a launch-site census covers every tracked language that spawns a shell, and a population is stated by query, never by a typed count.

#### M3. The records disagree on where api-key sits in `runtime.act-auth` (id 4)

- **Where:** architecture-v2.md:1076 (the `runtime.act-auth` Allowed cell) and dWellOiledMachine clause 37, against [folded-answers] at away-pass.md:488 and interpretation 2 at away-pass.md:547.
- **What is wrong:** The owner said "api-key as the last owner-selectable option" (away-pass.md:436), and [folded-answers] and interpretation 2 both say api-key is "tried last". v2's Allowed cell and clause 37 accept any ordered list and say only "api-key only when the owner adds it".
- **Consequence:** Under v2's schema, `api-key, setup-token` and `api-key` alone are both in-set. dGroundRules' out-of-set check would accept them, and the supervisor would try the API key first, against the owner's words. An empty list is also in-set, and with it no act can authenticate. The effect is contained because only the owner sets this key and no preset touches it.
- **Fix (judged sound by the skeptic):** State the constraint in the Allowed cell and in clause 37: a non-empty ordered list, with api-key only in last position. Add a schema arm that refuses an api-key that is not last, and one that refuses an empty list, each seen red on a planted policy file.
- **Left-shift gate:** for every catalogue key, check that each constraint in its Allowed cell maps to a schema arm with a planted red case.

#### M4. The atlas maps [planned] to a chain view that renders none of it (id 7)

- **Where:** memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:125, and the atlas line in [folded-answers] at away-pass.md:500.
- **What is wrong:** `V2_VIEWS` now maps `"planned": "chain"`. The chain view is built only from `section(v2, "chain")` (atlas.py:356-366), and nothing reads `section(v2, "planned")`. The rendered page contains "planned" 0 times. The claim in [folded-answers] that "The atlas shows v2's [planned] in its chain view" is false.
- **Consequence:** The coverage guard at atlas.py:545 compares section ids with map keys only, so a view that does not show the section satisfies it. This is the same "view that guessed instead of refusing" that a9b00addd's review had just closed. A reader sent to Chain finds no macOS or pwsh-launch plan.
- **Fix (judged sound by the skeptic):** Map `"planned"` to `"records"`, as [floor], [witnesses] and [front-door] already are, or extract [planned]'s bullets and render them in the chain view. Then correct the atlas line in [folded-answers]. Probe: grep the rendered page for `macOS` and confirm that the view the map names reaches the text.
- **Left-shift gate:** extend the guard at atlas.py:545 so that each mapped section's text must appear in the rendered view it names, not only in the map.

#### M5. "Gov runs it on itself first (AP-30)" cites a self-run that lands about 160 units later (id 9)

- **Where:** away-pass.md:474 ([folded-answers]), against architecture-v2.md:1392 (dSafePassage's row) and architecture-v2.md:1408 (dShippedRelease's row).
- **What is wrong:** The AP-30 mechanism belongs to dShippedRelease's lander unit: "the lander running each new upgrade step on gov's own tree in the prepared merge, recorded in the source-mode receipt". dShippedRelease's earliest finish is 176. dSafePassage, at 14, has no clause that runs its step on gov's tree or records it.
- **Consequence:** The next reader takes gov's floor raise as already witnessed on gov. Interpretation 5's "may rely on 3.15" leans on that missing witness.
- **Fix (judged sound by the skeptic):** Choose one of two:
  - Give dSafePassage a clause that applies its own floor step to gov's tree in its landing unit, with a witness.
  - Reword the line: gov's own raise is the build's direct edit, and the AP-30 self-run applies only from dShippedRelease on.

  Probe: name the clause on dSafePassage's row that the sentence cites.
- **Left-shift gate:** add a record check. A [folded-answers] sentence that attributes a mechanism to a build must cite a clause on that build's row or on an ancestor's row.

#### M6. The reason for dropping the TOML 1.0 arm and the floor-raise template does not hold (id 10)

- **Where:** away-pass.md:476-478, against architecture-v2.md:1392 and P38.
- **What is wrong:** The fold drops the research's TOML 1.0 arm and its floor-raise template because "every reader [is] at 3.15". dSafePassage's floor step has a down that restores the old declaration, and P38 records a rollback that lifts the downgrade refusal. After a down, readers at 3.11 to 3.14 are admitted again. The research measured 3.12.10 and 3.14.5 refusing a TOML 1.1 file that 3.15 accepts (research-python-floor.md:100). The template is about reusable raise steps, not about TOML dialects, and AP-35's detector exists to file the next raise.
- **Consequence:** Any TOML 1.1 syntax written while the floor is 3.15 makes `policy.toml` or `kit.toml` malformed after a rollback. The template decision rests on a reason that does not apply to it. The path is narrow, so the effect is contained.
- **Fix (judged sound by the skeptic):**
  1. Do one of these: keep a TOML 1.0 arm while any floor step has a down that can lower the floor, or make the floor step's down refuse when a tracked TOML file fails a 1.0 parse.
  2. Restate the template decision on its own grounds (for example, "dSafePassage's floor step is the template"), and name it on dSafePassage's row or dTendedCadence's row.
  3. Probe: plant one multi-line inline table, parse the repo's TOML files under 3.12, and observe the refusal the down path would meet.
- **Left-shift gate:** add a bug-class checklist entry: a decision justified by a floor value must also hold on that floor's down path.

#### M7. The instruments record's [final] reports the atlas run from before the commit (id 15)

- **Where:** memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md:9796.
- **What is wrong:** [final] ("Every check, re-run at the commit") records `atlas: derived — 167 records, 2869 sections, 190 decision sections`. Commit fe3d09aba changed that line from 189 to 190, while its message says the retitle makes the map read 189 again. The writer ran the atlas over its own record before writing it, so each commit's [final] records the tree as it stood before that commit.
- **Consequence:** The record the fold's witnesses cite as "all green" gives an output that is not the output at the commit, and it contradicts the commit message. A reader cannot tell from it whether the retitle worked. Every later [final] carries the same lag.
- **Fix (judged sound by the skeptic):** Have `record_instruments.py` write the record and re-run its checks until two passes give byte-identical output, and refuse if they never converge. Then regenerate [final]. Probe: `python -X utf8 2026-10-16-build-PLAY-dClosedLoop-1-atlas.py --check` at fe3d09aba prints 189 decision sections, rc 0.
- **Left-shift gate:** the fixed-point re-run inside `record_instruments.py` is the gate.

### LOW

#### L1. [planned]'s macOS trigger is wider than the owner's AP-34 answer (id 5)

- **Where:** architecture-v2.md:1425-1428.
- **What is wrong:** The trigger reads "a node registers darwin, or an adopter asks". The owner answered "On a registered node (Recommended)" (away-pass.md:457). The adopter arm comes from the research (research-python-floor.md:144). The owner's choice narrowed it, and [folded-answers] does not list the restored arm as an interpretation.
- **Consequence:** An adopter's request could start macOS work the owner did not schedule. This is record text, and no code runs from it.
- **Fix (judged sound by the skeptic):** Drop "or an adopter asks", or put it to the owner as an eighth interpretation.
- **Left-shift gate:** add a bug-class checklist entry: a folded answer's text is diffed against the chosen option's wording, and any widening is listed as an interpretation.

#### L2. gap-tool-22's "declared in eight files at 3.11" is neither the evidence's fact nor the tree's (id 6)

- **Where:** gap-register.md:217.
- **What is wrong:** The cited figure (research-python-floor.md:93) is "Edits: 8 files, 9 lines", which counts the edits a raise needs. `git grep -l '3\.11' -- ':!memory'` lists 7 files. Two of the hits are comments: `merge-rows.test.sh:351` and `settings-merge.py:158`.
- **Consequence:** A builder who takes this as dSafePassage's "declared once" population starts from a wrong count.
- **Fix (judged sound by the skeptic):** Restate the fact as measured (for example, "named in 7 tracked files outside memory, 5 of them declarations"), or cite the research's figure as an edit count. Derive the population by query in the floor step's census.
- **Left-shift gate:** add a gap-register check. Each count in a gap must quote its cited evidence's figure verbatim, or carry the query that reproduces it.

#### L3. A dropped separator mis-pairs a trailer with its edge in dDeclaredLoop's commit-node clause (id 12)

- **Where:** architecture-v2.md:1395.
- **What is wrong:** The clause now reads "`Gov-Unit` and `Gov-Item` mapped to `serves` `Gov-Act` to `made-by` and `Gov-Session` to `runs-in`". The separator after `serves` was lost in the AP-8 edit.
- **Consequence:** The clause reads as if `serves` pairs with `Gov-Act`. Clause counting is unaffected.
- **Fix (judged sound by the skeptic):** Restore the separator: "mapped to `serves`, `Gov-Act` to `made-by` and `Gov-Session` to `runs-in`".
- **Left-shift gate:** none fits. Add this to the project's bug-class checklist as "an edit inside a list-of-mappings sentence re-checks every separator".

review-shape kind=diff-review round=1 intensity=light at=synth raw=17 confirmed=12 refuted=5 unverified=0 blocker=0 high=1 medium=8 low=3 agents=9 out-tokens=129629

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1392 | high | high | confirmed | I read v2:1392. dSafePassage clause 6 says the floor's "up [is] a preflight refusing an interpreter below the floor" and that "the PEP 701 text ban in `merge-rows.test.sh` [is] retired". The only clause that makes the resolver refuse below the floor is dWitnessedBar's portability pack: "the resolver ... refusing below it with the install command". [folded-answers] lists the earliest finishes as dSafePassage 14 and dWitnessedBar 95. tools/lib/resolve-python.sh accepts any candidate whose `-c "import sys"` exits 0, so it sets no version floor. merge-rows.test.sh:347-352 records the consequence: a driver that fails to start exits without writing %A and leaves OURS-only content with no markers. Research line 171 measured a WSL node at Python 3.10. Interpretation 5 lets every later build rely on 3.15. So from unit 14 to unit 95 the design retires the ban without anything outside `update` refusing an old interpreter. The step's preflight runs only where `update` runs. This is a narrow path to silent loss of merge content, and it will mislead the builds that follow. | sound | - |
| 2 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:476 | medium | - | refuted | Research lines 100 and 217 show the dropped TOML 1.0 arm was aimed at the tomllib split across Python versions, where 3.15 accepts 1.1 and 3.12 and 3.14 refuse it. It was not aimed at awk readers. tools/roles/adopt-roles.sh:120 is a line-oriented awk scan of the kit's own workflows.toml, with its own block and dead-probe checks. It already limits that file to a narrow line format, stricter than TOML 1.0 itself, and would not be protected by the dropped arm any more than it is now. Its limits were there at the base and are not a split this fold opened. The one real gap left, Python readers below 3.15 before dWitnessedBar enforces the floor, is the same interim window as finding 1, so it is a duplicate. | unsound | - |
| 3 | correctness | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:539 | medium | medium | confirmed | tools/unattended/stop-guard.js:111 runs `spawnSync('bash', [driver, '--liveness', slug], ...)`. Research line 175 measured that exact site at 5.1.16, WSL, under a clean PATH. The correction (away-pass.md, Corrections) says the class reaches WSL only "through govkit's fall-back ... and through seven copies of a resolver loop", on a census of .py files only. gap-tool-20 (gap-register.md:215) repeats that scope. v2 never names stop-guard: grep finds 0 hits. dWitnessedBar's clause scopes itself to "replacing the seven copies of the loop". It does name a JavaScript twin, but no clause moves the stop guard's call onto it. The fold misstates its own research return and leaves a measured WSL path out of both the gap and the unit. The effect is contained to the liveness check. | sound | - |
| 4 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1076 | medium | medium | confirmed | v2:1076's Allowed cell for `runtime.act-auth` reads "an ordered list drawn from setup-token, oauth-shared and api-key, api-key only when the owner adds it". dWellOiledMachine's clause reads "an API key only when the owner adds it". Neither says where api-key sits. [folded-answers] ("an API key tried last") and interpretation 2 ("it is tried last") follow the owner's AP-14 words at away-pass.md:436: "api-key as the last owner-selectable option". As v2's schema stands, a list with api-key first passes the out-of-set check, so the records disagree on the rule a check would enforce. The impact is contained, because only the owner sets this key and it is never preset. | sound | - |
| 5 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1425 | low | low | confirmed | architecture-v2.md:1428 (the [planned] macOS bullet) reads 'Trigger: a node registers darwin, or an adopter asks'. The owner's AP-34 answer (away-pass.md:457) is 'On a registered node (Recommended)'. The option as it was put (away-pass.md:326) is 'on a registered node, after dWellOiledMachine dissolves `unattended/`'. The 'or an adopter asking' arm comes from dispatch 113's return (research-python-floor.md:144), which the owner's choice narrowed. The fold restored the research's wider trigger, and [folded-answers] does not list it as an interpretation. This is a record-text defect, and no code runs from it. | sound | - |
| 6 | correctness | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:217 | low | low | confirmed | gap-register.md:217 reads 'declared in eight files at 3.11' and cites research section 2. That section's figure (research-python-floor.md:93) is 'Edits: 8 files, 9 lines', a count of the edits a raise needs, not a count of declarations. `git grep '3\.11' fe3d09aba -- ':!memory'` returns 7 files: README.md, codebase-map README and map_lib.py, check_runbook_parity.py, and govkit.py with lines 108 and 1145; merge-rows.test.sh:351 and settings-merge.py:158 are comments. A search for '3, 11', '3_11' and '>=3.11' adds no declaration. So the stated fact matches neither the evidence it cites nor the tree. The effect is a wrong count in a design record. | sound | - |
| 7 | seams | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:125 | medium | medium | confirmed | atlas.py:125 now maps "planned": "chain" (the only change the diff makes to atlas.py). The chain data is built only from section(v2, "chain") (atlas.py:356-366): the [chain] table's Build, Stage, Parents, Units and Gaps. Nothing reads section(v2, "planned"). The coverage guard at atlas.py:545 compares only the set of v2's section ids with V2_VIEWS's keys, so it passes on a view that does not render the section. [folded-answers] (away-pass.md:500) says 'The atlas shows v2's [planned] in its chain view', which is false. The effect is contained to the atlas instrument and one record line. | sound | - |
| 8 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1392 | high | medium | confirmed | gap-tool-21 is new in this diff. Its text (gap-register.md:216) names three facts, one of them 'remote CI sets up no Python'. It is owned by dWitnessedBar (v2 [chain] row at line 1404, whose gaps cell ends 'gap-tool-20, gap-tool-21'). That row's only floor clause is 'an interpreter-floor arm that runs a real interpreter at the declared floor, with a feature census ... the resolver ... refusing below it'; it names no CI provisioning. dSafePassage's floor clause (line 1392) declares 3.15 once, with a preflight up and a restoring down, and says nothing about remote-ci.yml. dShippedRelease's 'Linux job in emitted CI that sets up Python at the floor' is for adopters' emitted CI. .github/workflows/remote-ci.yml still has only `runs-on: windows-latest` (lines 47, 88, 126, 277) and no setup-python step; its jobs source resolve-python.sh. So the gap's CI fact is filed as owned, but no clause closes it, and the raise at dSafePassage comes before dWitnessedBar. I grade it medium, not high: once readers refuse below the floor, a sub-floor runner turns the merge bar red loudly, so the failure would be noticed at once rather than certify something wrong. It is still a real misattribution in the design. | sound | - |
| 9 | seams | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:474 | medium | medium | confirmed | away-pass.md:474 is new in this diff and says of dSafePassage's floor step 'gov runs it on itself first (AP-30)'. AP-30's row (away-pass.md:322) assigns that mechanism to 'dShippedRelease's lander unit'. v2:1408 places 'the lander running each new upgrade step on gov's own tree in the prepared merge, recorded in the source-mode receipt' on dShippedRelease, whose earliest finish is 176 against dSafePassage's 14. dSafePassage's row (v2:1392) has no clause that runs the step on gov's tree or records it. The sentence cites a self-run that does not exist when the build lands. The harm stays inside the design prose, though the next reader would take gov's raise as already witnessed. | sound | - |
| 10 | seams | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:477 | medium | medium | confirmed | away-pass.md:476-478 drops the research's TOML 1.0 arm and its floor-raise template 'with every reader at 3.15'. The fold's own dSafePassage row (v2:1392) gives the floor step a down that restores the old declaration, and P38 records a rollback that lifts the downgrade refusal. Once that down runs, readers below 3.15 are admitted again. The research measured 3.12.10 and 3.14.5 refusing a TOML 1.1 file that 3.15 accepts (research-python-floor.md:100). Nothing in the design keeps gov's TOML at 1.0 for that path, so the premise fails there. The reason also does not cover the template: the research's floor-raise template (research-python-floor.md:218) is about reusable raise steps, not about which dialect 3.15 reads, and AP-35's detector exists to file the next raise. The path is narrow (a rollback after 1.1 syntax is written), so the effect is contained. | sound | - |
| 11 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:805 | low | - | refuted | P37 (v2:805-809) is a principle in a design-only record, not a product reader. The 'declared once' rule on dSafePassage's row (v2:1392) governs the product's floor declaration and the readers that consume it at runtime. A down step or a later raise acts on that declaration in the tree, not on v2's prose. A future raise is itself a design change that edits its principle text, as every prior fold does. Recording today's owner-chosen value in the principle beside its AP-31 citation does not create a second declaration that any reader or the step's inventory has to find. | sound | retirement-inventory-misses-readers-by-value |
| 12 | seams | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1395 | low | low | confirmed | At the base, v2 read "`Gov-Unit` and `Gov-Item` mapped to `serves` and `Gov-Act` to `made-by`". The AP-8 edit in this diff now reads "mapped to `serves` `Gov-Act` to `made-by` and `Gov-Session` to `runs-in`" (v2:1395). It dropped the separator after `serves`, so `serves` appears to pair with `Gov-Act`. This is a prose defect only: no '; ' changes, so clause counting is unaffected. | sound | - |
| 13 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1392 | high | medium | confirmed | Confirmed. dSafePassage's row (architecture-v2.md:1392) raises the floor to 3.15 as the step kind's first step. Its up step is a preflight run at update. Neither that row nor any other clause sets up a 3.15 interpreter for gov's own hand-written .github/workflows/remote-ci.yml. That file's jobs run on windows-latest with no setup-python step, and lines 163 and 314 take whatever Python resolve-python.sh finds. dShippedRelease's 'Linux job in emitted CI' covers adopters' emitted CI, not this file. One correction to the finding: the remote-CI half does have a named end. gap-tool-21 is new in this diff, and its text includes 'remote CI sets up no Python'. dWitnessedBar's Closes column lists it (line 1404), and that build's floor arm 'runs a real interpreter at the declared floor'. So the claim 'with no named end after that' is wrong. The defect is real but narrower: between dSafePassage (earliest finish 14) and dWitnessedBar (95), gov's merge bar runs below the floor gov has just declared for itself. That did not happen under the 3.11 floor. I grade it medium, not high: it is a design record, the gap is registered and owned, and the effect is confined to that window. | unsound | amendment-leaves-its-other-half-standing |
| 14 | verification | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-away-pass.md:476 | medium | - | refuted | The research's TOML 1.0 arm (research-python-floor.md:11, 100, 217, 230) guarded one split: a 3.15 node accepting TOML 1.1 files that a 3.11 floor refuses. With the floor at 3.15 by the owner's AP-31 ('3.15 now, all the nodes will upgrade'), TOML 1.1 is the floor's own dialect. A TOML 1.0 arm would ban syntax the floor admits, the same kind of ban the fold retires for PEP 701 in merge-rows.test.sh. So the arm's premise is gone, and dropping it follows from the owner's direction. What remains is a different defect: below-floor readers may run before dWitnessedBar's resolver refuses them. That is floor enforcement, the same window finding 13 covers, not a defect in dropping the arm. Graded medium and not established as a defect of this fold, so refuted. | unsound | - |
| 15 | verification | memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md:9796 | medium | medium | confirmed | Confirmed from the text. The instruments record's [final] ('Every check, re-run at the commit', around line 9796) records 'atlas: derived — 167 records, 2869 sections, 190 decision sections'. Commit fe3d09aba changed that line from 189 to 190, while its message says the retitle makes 'the map read 189 decision sections again'. At 50e6c38c1 the same line read 189, although the decision-titled [answers-fold] section was already in the record. So each commit's [final] records the atlas run over the record as it stood before the commit wrote it. That lag is the self-reference the finding describes. The record cited as proof that every check is green at the commit gives an output that contradicts the commit's own claim. I did not run the atlas, per the no-gates rule. | sound | two-answers-to-one-question |
| 16 | verification | memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py:509 | medium | - | refuted | Pre-existing. The decision filter at atlas.py:506 (`if rec["group"] in ("Reviews", "Research returns"): continue`) and DECISION_TITLE are byte-identical at a9b00addd. The diff's only change to atlas.py is adding "planned": "chain" to V2_VIEWS. Instruments records were already open to the decision pattern at the base, so this diff did not introduce the class defect or make it reachable. It hit one instance and fixed it by retitling. | sound | - |
| 17 | verification | memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md:1079 | medium | - | refuted | Part of this is pre-existing. At a9b00addd, v2:1057 already listed `trace.identity` as `act-only, session, salted` with `salted` undefined; the diff only changed the default to `session` (now v2:1069), as AP-8 directs. Asking for a per-value arm and a planted case for each value is unit-level detail, which this design-only build leaves to the chain builds on purpose ('a row's planned units are prose'). The catalogue holds no value to that standard: `maintain.on-breach: red-leg`, `maintain.node-readings: lease-holder` and `commits.squash: accept-loss` (v2:1000, 1003, 1068) have no clause arm either. Every new key does have an owner that reads it: `platforms.provision` is owned by dSafePassage, its routes are at v2:1392 and 1404, and its values `uv` and `off` are the AP-32 fork options the owner chose among (away-pass:324, 455). `maintain.interpreter-eol` is owned by dTendedCadence, and its values are AP-35's options (away-pass:327, 458). No contained defect remains that this diff introduced. | unsound | policy-value-with-no-route |
