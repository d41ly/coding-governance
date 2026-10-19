**Serves:** diff-review TOOL-dRenderedAnchor-2 TOOL-dRenderedAnchor-3

# Closing diff review, round 3: dRenderedAnchor unit 3, the round-2 fix batch and the C4 citation split

2026-10-19 · Tier-2 · on `branch/frosty-feistel-42acd4` · adversarial fan through `tier2-review.js`: 5 finder lenses, then 4 skeptic batches, then this synthesis. This round reads the FIX for the 9 round-2 items (record `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-2-closing-diff-round2.md`). M4 promoted all of them into one batch unit, TOOL-dRenderedAnchor-3 (spec rev-2, owner fork F1 resolved as C4). It was built at a8d836483, with a ledger fix at 052b43a24.

**Reviewed range:** `c66a3663d7ed06a92cca8dc32bc81c17fa54dfec...66ccdb26de56187068205b5c7a02a35eca610b66`. **ROUND 3.**

## Verdict: CLEAN WITH FIXES

No confirmed finding is a blocker or a high, and none says a round-2 item is still open. Nothing renders wrong at the tip. One medium item needs fixing before the close: the harness branch of the C4 split is guarded by nothing. The two low items are documentation wording that this fold introduced.

## Review shape

Intensity **full** · raw **7** · confirmed **6** · refuted **1** · unverified **0** (0 uncertain) · precision **0.86**.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 0 | 0 | 0 | 0 | 0 | - |
| correctness | yes | 2 | 1 | 1 | 0 | 0 | 0.50 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| verification | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |
| intent | yes | 1 | 1 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: **3 items**: 0 blocker, 0 high, 1 medium, 2 low. By raw confirmed finding: 0 blocker, 0 high, 3 medium (ids 1, 3, 5), 3 low (ids 4, 6, 7).

Refuted: id 2 (an arm-18 comment in `render_agents.py`). The same text is already present at base c66a3663, so it is outside this fold.

Run integrity: lenses 5/5 returned, 0 DIED. Skeptic batches 4/4 returned, 0 DIED. 0 contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there were 0 duplicates. Fixes on confirmed findings: 6 judged sound, 0 judged UNSOUND, 0 with none proposed, 0 NOT JUDGED. Severity on confirmed findings: 0 UNGRADED, 0 RE-GRADED by the skeptic. Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict. Lens notes: none were supplied, so every lens ran on the kit's generic brief. The run is complete.

Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer. Intent: 3 spec documents were supplied as `specs`, beside the range's commit messages. Checklist: 11 items, each assigned to exactly one of 5 lenses (security 3, correctness 2, seams 2, verification 2, intent 2). By design: the caller's byDesign.

## Items

### M1 [MEDIUM]: the harness branch of the C4 split has no check that can fail (ids 1, 3, 5)

**Where:** `tools/roles/roles_lib.py:626`, `here = kit.parent if m.groups() in harnesses else kit`, inside `resolve_cited_paths`.

**What is wrong:** If this line becomes `here = kit` for every citation, which is fork C2 and is rejected in spec section 4, arms 14, 15 and 16 of `adopt-roles.test.sh` and AC1 and AC13 all stay green. From the kit dir, `resolve_kit_dir` probes `tools/roles/<home>` and then `tools/<home>`. From the tool root it probes `tools/<home>` and then `<repo>/<home>`. So the two values of `here` give different answers in only one case: a harness held at `<repo>/<home>/<file>`, with the kit nested under `tools/` and no receipt row. No guard builds that case:
- Arm 14 places every harness pair through a `rendered` receipt row. The receipt is found by the `.git` walk, which reaches the same root from either `here`.
- Arm 15 skips every HARNESS_PAIRS_READ pair, and its fixture holds no harness.
- Arm 16 lists nothing under either value. The shipped call reaches the sibling and drops it on ValueError. The mutant never reaches it and raises LookupError.
- AC1 and AC13 hold the harnesses under `tools/workflows/`, which both values of `here` reach.

Spec S1 says AC1 and AC13 observe this branch. Neither can tell the two calls apart.

**Consequence:** Spec section 4, table row 2, covers exactly this layout. Three finders and their skeptics reproduced it independently in a scratch fixture: `.git`, `tools/roles/`, and both cited harnesses only at `<repo>/workflows/`. The shipped lib returned `[('{{TOOL_ROOT}}workflows/unattended-build.js','workflows/unattended-build.js'), ('{{TOOL_ROOT}}workflows/tier2-review.js','workflows/tier2-review.js')]`. The `here = kit` mutant returned `[]`, so the Skill would fall back to the plain `tools/workflows/<file>`. Meanwhile `resolve_harness_path`, and so `.claude/roles.json`, lists `<repo>/workflows/<file>`. That is two answers to one question, the class this build exists to close. A change that collapses the branch would pass the whole suite. The output is correct today. This is a gate gap, so medium.

**Fix (judged SOUND by the skeptic):**
1. Add one floored assertion to arm 14, or add a new arm 17, and raise FLOOR_ASSERTIONS by 1.
2. Build the fixture with `build_fixture`: a prefixed kit, each HARNESS_PAIRS_READ pair written only at `$FX/<home>/<file>`, no receipt, and nothing under `tools/<home>/`.
3. After `--scaffold`, assert that the Skill names each pair as backticked `` `<home>/<file>` `` and never as `tools/<home>/<file>`. Also assert that `resolve_harness_path` and `roles.json` name the same path.
4. The main loop must observe the assertion RED with line 626 staged as `here = kit` (the C2 break), then GREEN on the shipped line. A reviewer runs no gate.

**Left-shift gate:** the new assertion is itself the gate for this class. Add a checklist entry: "each branch of a conditional resolver needs a fixture whose answer depends on that branch, observed RED against the collapsed branch".

### L1 [LOW]: the docs say a repository-root file never answers a non-harness citation, which is false at a root install (ids 4, 6)

**Where:**
- `help/roles.md:134`: "a file at the repository root never answers it"
- `tools/roles/README.md:321`: "an adopter's file at the repository root is never named"
- `tools/roles/adopt-roles.sh:37`: the same claim

All three sentences are new in this fold. Base c66a3663 has no "repository root" wording in any of the three files.

**What is wrong:** At a root install the kit is `<repo>/roles`, so the tool root is the repository. The non-harness call, `here = kit`, probes `<repo>/roles/<home>/<file>` and then `<repo>/<home>/<file>`. A repository-root file therefore does answer. A skeptic's probe with `run-gates/run-gates.sh` at the root of a root-install fixture returned `[('{{TOOL_ROOT}}run-gates/run-gates.sh', 'run-gates/run-gates.sh')]`. The opening clause in the README and in the adopter comment ("its probes stop at `<tool root>/<home>/`") is accurate. Only the absolute conclusion drawn from it is wrong.

**Consequence:** None in behaviour. At a root install that file is the kit's correct location, and the result equals the plain-prefix substitution. A reader who relies on the stated predicate is misled. Arm 15 runs only the nested fixture, so nothing checks the claim at a root install.

**Fix (judged SOUND by the skeptic):** Reword all three carriers to the shipped predicate. Suggested text: "its probes stop at `<tool root>/<home>/`, so at a prefixed install a file at the repository root never answers it". Grep for `repository root` across the three files so they change together.

**Left-shift gate:** add a checklist entry: "a docs claim about resolver reach states the install shape it holds for (prefixed or root)".

### L2 [LOW]: "a harness of the workflow table" leaves the table's own merge-bar harness out (id 7)

**Where:**
- `help/roles.md:130`
- `tools/roles/README.md:316`
- the `adopt-roles.sh` header at line 33 (the finding cited :247)
- the second sentence of the `resolve_cited_paths` docstring, `tools/roles/roles_lib.py:611`

**What is wrong:** The new wording reads "Only a harness of the workflow table resolves as the role index does ... Every other tool-root citation, the merge bar's among them". But `tools/roles/workflows.toml:74-75` gives the merge bar its own entry in that table: `driver = "program"`, `harness = "bash {prefix}/run-gates/run-gates.sh"`. The predicate that shipped is `driver == "workflow"`, in `roles_lib.extract_workflow_harnesses`. The docstring's first sentence already says "`workflow`-driver" correctly. Unit 3 introduced the inaccurate text.

**Consequence:** None in behaviour. The extractor returns only the four workflow-driver values, and run-gates resolves from the kit dir. The page contradicts the table it cites, though, so a reader or the next builder cannot tell from the docs which predicate decides the branch.

**Fix (judged SOUND by the skeptic):** In all four carriers, write "a `workflow`-driver harness of the workflow table" in place of "a harness of the workflow table". Check with `grep -n 'harness of the workflow table' help/roles.md tools/roles/README.md tools/roles/adopt-roles.sh tools/roles/roles_lib.py`. It should print no line that lacks "`workflow`-driver".

**Left-shift gate:** add that grep as a checklist probe, or a docs-consistency row asserting that every carrier of the C4 predicate names the `workflow` driver.

review-shape kind=diff-review round=3 intensity=full at=synth raw=7 confirmed=6 refuted=1 unverified=0 blocker=0 high=0 medium=3 low=3 agents=10 out-tokens=125973

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/roles/roles_lib.py:626 | medium | medium | confirmed | roles_lib.py:626 picks `here = kit.parent` only for a harness citation. resolve_kit_dir (roles_lib.py:97-132) reads a receipt row first, then probes <here>/<home> and <here>/../<home>. With `here = kit` (tools/roles) those probes are tools/roles/<home> and tools/<home>; with kit.parent they are tools/<home> and <repo>/<home>. So the branch only matters for a harness found at <repo>/<home>/ with no receipt row. None of the guards builds that layout. Arm 14 (adopt-roles.test.sh:549-584) places every pair through a `rendered` receipt row, so the result does not depend on `here`. Arm 15 skips every HARNESS_PAIRS_READ pair. In arm 16 the shipped call hits the sibling and raises ValueError, while the mutated call raises LookupError; both are caught and both list nothing. AC1 puts the harnesses under tools/workflows/, which probe 2 from the kit dir also reaches, and AC13 runs over this repo, where they also sit under tools/workflows/. I reproduced this in a scratch fixture: .git, tools/roles copied, and each extracted harness written at <repo>/workflows/. Shipped resolve_cited_paths returned [('{{TOOL_ROOT}}workflows/unattended-build.js','workflows/unattended-build.js'), ('{{TOOL_ROOT}}workflows/tier2-review.js','workflows/tier2-review.js')]. An exec'd copy with line 626 changed to `here = kit` returned []. resolve_harness_path(tools, h) held every harness at <repo>/workflows/. So collapsing the branch would bring back the Skill-vs-index disagreement that S1 exists to prevent, and the suite would stay green. Nothing is wrong at the tip, though: this is a guard gap on a narrow layout, so medium. | sound | - |
| 2 | correctness | tools/roles/render_agents.py:638 | low | - | refuted | This is pre-existing. `git show c66a3663:tools/roles/render_agents.py` already has the same arm-18 comment, 'a namesake beside no mark of the harness's kit is the / adopter's own file', at lines 640-641. The fold's render_agents.py diff touches only the module docstring (36-41) and derive_harness_paths (158-165), not this comment. Round 2's L7 cited the help text and the docstring, and the fold fixed both. The gotcha line the finder quotes says 'TOOL-dRenderedAnchor-3 wrote what the scan counts into all four', meaning the help page, docstring, README and map it lists just before. That is true of those four and claims nothing about a self-test comment. The defect sits unchanged at the base, so it is out of scope for this fold review. | unsound | amendment-leaves-its-other-half-standing |
| 3 | seams | tools/roles/roles_lib.py:626 | medium | medium | confirmed | This fold added the branch at roles_lib.py:626, `here = kit.parent if m.groups() in harnesses else kit`. No arm checks its harness side. resolve_kit_dir reads the receipt first, from the root its .git walk finds. That root is the same whether `here` is kit or kit.parent, so the receipt rows in arm 14 decide its result either way. - Arm 15: build_fixture copies only the roles kit, so no harness exists at tools/workflows/ or at <repo>/workflows/. Both calls list nothing. - Arm 16: real code probes repo/../workflows, gets a ValueError, and lists nothing. The mutant probes repo/roles/workflows and then repo/workflows, finds neither, and lists nothing. Both return []. - AC1 and AC13: the harnesses are under tools/workflows/. The mutant's second probe, <kit>/../<home>, reaches the same file, and tools/roles/ holds no workflows directory (I listed it). I reproduced layout A in the scratchpad: a prefixed kit, .git, both harnesses only at <repo>/workflows/, and no receipt. The real lib returned both citations as `workflows/<file>`. A copy with line 626 set to `here = kit` returned []. resolve_harness_path, which the role index uses, lists <repo>/workflows/... as held. So the rule spec §4 uses to reject C2 is not gated. The spec's "Observed by AC1 and AC13" cannot tell the two calls apart. The effect is contained: a missing gate, not a wrong render today. | sound | - |
| 4 | seams | help/roles.md:134 | low | low | confirmed | The sentences are new in this fold. Grepping 'repository root' over the base c66a3663 versions of all three files finds nothing. At a root install the kit is <repo>/roles, so the tool root is the repository. The C4 call for a citation that is not a harness, `here = kit`, therefore probes <repo>/roles/<home>/<file> and then <repo>/<home>/<file>. A file at the repository root does answer it, and that is the kit's correct location. The absolute wording is false in these places: - help/roles.md:134, 'a file at the repository root never answers it' - README.md:321 and adopt-roles.sh:37, 'is never named' The behaviour is correct; only the docs are wrong. | sound | - |
| 5 | verification | tools/roles/roles_lib.py:626 | medium | medium | confirmed | In roles_lib.py:626, `here = kit.parent if m.groups() in harnesses else kit` differs from `here = kit` in only one case: a harness held at <repo>/<home>/<file> with the kit nested under tools/. The kit dir's two probes are tools/roles/<home> and tools/<home>. The tool root's two probes are tools/<home> and <repo>/<home>. No check builds that case. Arm 14 places its harnesses through receipt rows, and the receipt is found by walking up to .git, which gives the same answer from either `here`. Arm 15 skips every harness pair. Arm 16's fixture holds no harness under the tool root. Its only copies are in a sibling of the repo, which the shipped code reaches and then drops on ValueError, and which the mutant never reaches (LookupError), so both print []. AC1's fixture puts the harnesses at tools/workflows/, and so does AC13 in this repo, so both values of `here` reach them. No other suite calls resolve_cited_paths: grep finds only adopt-roles.sh:182 and arm 16. I re-ran the finder's probe in a scratch fixture with .git, tools/roles and workflows/{tier2-review,unattended-build}.js at the repo root. The shipped lib returned both `workflows/...` pairs. The sed mutant (`here = kit`) returned []. resolve_harness_path named fx/workflows/... as held in both runs. So the mutant gives two different answers to one question and still passes every arm, while spec S1 says AC1 and AC13 observe the branch. The effect is limited to a test gap on a code path that ships correct today, so medium. | sound | two-answers-to-one-question |
| 6 | verification | help/roles.md:134 | low | low | confirmed | These lines are new in this diff: `git show c66a3663:` finds no 'repository root' wording in any of the three files. They claim the repo-root file is never used, but at a root install it is. Carriers: help/roles.md:134 ('a file at the repository root never answers it'), tools/roles/README.md:321 (the finder wrote README.md:321, but the line is in tools/roles/README.md) and tools/roles/adopt-roles.sh:37 ('an adopter's file at the repository root is never named'). At a root install the kit dir is <repo>/roles, so resolve_kit_dir's second probe from here=kit is here.parent/<home> = <repo>/<home>, and a file at the repo root answers. Arm 16 shows root installs are a supported shape, and arm 15 runs only the nested fixture. The README and adopter's first clause ('probes stop at <tool root>/<home>/') is right. Only the conclusion drawn from it is wrong at a root install, where the tool root is the repo root. There the resolved path equals the plain-prefix substitution, so behaviour does not change: only the wording is wrong, so low. | sound | - |
| 7 | intent | help/roles.md:130 | low | low | confirmed | Checked, and it holds. In tools/roles/workflows.toml, lines 74-75 give the merge bar its own entry: driver = "program", harness = "bash {prefix}/run-gates/run-gates.sh". The predicate that shipped is roles_lib.extract_workflow_harnesses (roles_lib.py:356-357), which keeps only entries whose driver == "workflow". The new wording says 'Only a harness of the workflow table resolves as the role index does ... Every other tool-root citation, the merge bar's among them'. That classes the table's own run-gates harness as 'every other', which contradicts the table. Unit 3 introduced this text: help/roles.md:130-132 is a '+' line in the range diff, and the base c66a3663 has no such phrase. The same text appears in tools/roles/README.md:316, in the resolve_cited_paths docstring (roles_lib.py:611, whose first sentence correctly says '`workflow`-driver') and in the adopt-roles.sh header. The header sits at line 33, not :247 as the finding cites. Behaviour is unaffected, so this is low: the docs alone are inaccurate. | sound | - |
