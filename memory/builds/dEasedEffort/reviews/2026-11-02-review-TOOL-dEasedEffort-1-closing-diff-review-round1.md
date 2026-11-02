**Serves:** diff-review TOOL-dEasedEffort-1

# Closing diff review, round 1: build dEasedEffort (TOOL-dEasedEffort-1, the agent effort levels)

2026-11-02 · Tier-2 · on `branch/agent-effort-levels-062fb2` · adversarial fan: five finder lenses (gov-diff-reviewer), five skeptic batches (gov-skeptic), synthesis by gov-synthesizer. The subject is the cumulative diff landing on main: the four role levels moved in `tools/roles/house/policy.toml`, the four rendered agent types under `.claude/agents/`, the stage-override sentence in `tools/roles/README.md`, and the build's records.

**Reviewed range:** `94188878323ef3b20e96b769791de73453b09909...918a954369715a372360fdd58c901af0891c1a52`. **ROUND 1.**

## Verdict: CLEAN WITH FIXES

There are no blockers, highs or mediums. Two low items hold the 2 confirmed findings. Both are defects in the acceptance ledger's audit trail, and no code or effort level is wrong. Re-run at the reviewed head, both criteria print the expected result. Both fixes are records commits. 5/5 lenses and 5/5 skeptic batches returned, and none died. The run-integrity list below carries one non-zero count, so this report does not call the run complete.

## Review shape

Intensity full, raw 5, confirmed 2, refuted 3, unverified 0 (0 uncertain), precision 0.40.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 1 | 0 | 1 | 0 | 0 | 0.00 |
| correctness | yes | 1 | 0 | 1 | 0 | 0 | 0.00 |
| seams | yes | 0 | 0 | 0 | 0 | 0 | - |
| verification | yes | 1 | 0 | 1 | 0 | 0 | 0.00 |
| intent | yes | 2 | 2 | 0 | 0 | 0 | 1.00 |

Adjudicated tally by item: 0 BLOCKER, 0 HIGH, 0 MEDIUM, 2 LOW (2 items). By raw confirmed finding: 0 blocker, 0 high, 0 medium, 2 low (2 findings). No findings were merged, so the two tallies match.

**Run integrity.**
- Lenses 5/5 returned, 0 died. Skeptic batches 5/5 returned, 0 died.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- Fixes on confirmed findings: 2 judged sound, 0 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 1 RE-GRADED by the skeptic. The re-grade is finding 4, from the finder's medium to the skeptic's low. That count is the one non-zero count.
- Unverified findings: 0 answered UNCERTAIN by a skeptic, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Roles: finders gov-diff-reviewer, skeptic batches gov-skeptic, synthesis gov-synthesizer.
- Intent: 2 spec documents supplied as `specs`, beside the range's commit messages.
- Checklist: 10 items, each assigned to exactly one of 5 lenses (security 2, correctness 2, seams 2, verification 2, intent 2).
- By design: none supplied, with no caller byDesign and no block.

## Blockers

None.

## High

None.

## Medium

None.

## Low

### L1 — The AC3 ledger line records a command that could not have printed its result (finding 4)

- **What is wrong:** The AC3 evidence says `git diff --name-only 2a6f3975 HEAD -- .claude` "printed exactly those four paths on the render's commit". That line was committed inside the render's commit, e74ef35e8. When the line was written, HEAD was 00866ea0a, and the same command there prints 0 lines (probed). The reflog shows a plain `commit:` entry for e74ef35e8, with no amend or reset. No dangling commit from this build's window carries the render. No later commit touches the ledger, so no re-run was recorded either.
- **Where:** `memory/builds/dEasedEffort/build/2026-11-02-build-TOOL-dEasedEffort-1-1-acceptance-ledger.md:21`. The cause sits in the spec: AC3's HEAD form (`memory/builds/dEasedEffort/spec/2026-11-02-spec-TOOL-dEasedEffort-1.md:183`) with Rollout step 2 (line 121), which observes, adds the line and then commits, makes that ordering unavoidable.
- **Consequence:** A skeptic or the close reads this ledger as AC3's observation, and this clause is the one that catches a render moving another file under `.claude`. The recorded command on the recorded commit was not what was observed. The result itself holds: at e74ef35e8 and at 918a95436 the command prints exactly the four paths. No code or level is wrong and nothing executes on the line, so the binding grade is low, down from the finder's medium.
- **Fix (skeptic judged SOUND):** In a later records commit, re-run AC3's form and record the commit it ran at, for example "at e74ef35e8 and at the close". Otherwise state the form actually run, such as `git diff --cached --name-only 2a6f3975 -- .claude` before the commit. For this class of criterion, write the spec's AC with a form that can be observed before its own commit, or assign the ledger line to the commit after the one it observes.
- **Left-shift gate:** The class is C5, `memory/gotchas/criterion-asserts-what-its-own-command-cannot-show.md`, which records that no machine gate fits it. So the left-shift is a checklist entry: add this as a new form in the gotcha's Symptom list, a criterion graded on `HEAD` whose ledger line lands in the commit it observes. A spec audit then asks of each such criterion which commit its ledger line lands in.

### L2 — AC1's ledger line records a different command, and the reason lives only in a commit trailer (finding 5)

- **What is wrong:** Spec AC1 names `git diff --numstat 2a6f3975 HEAD -- tools/roles/house/policy.toml`. The ledger records `git diff --cached --numstat 2a6f3975` over the staged file. The `--cached` spelling is visible in the ledger, but the reason for it is not. The trailer on 00866ea0a says the exact form "is run after the commit and reported in the return". A return is not a kept record, and the agent ledger's return line holds only a commit sha. The later ledger edit in e74ef35e8 added the AC3 line and left AC1's form as it was. Spec section 9 has only rev-1, so nothing was amended.
- **Where:** `memory/builds/dEasedEffort/build/2026-11-02-build-TOOL-dEasedEffort-1-1-acceptance-ledger.md:19`, against AC1 at `memory/builds/dEasedEffort/spec/2026-11-02-spec-TOOL-dEasedEffort-1.md:168`.
- **Consequence:** No kept record shows AC1 observed as written, and the class's own rule says a criterion found wrong at build time is amended where its spec allows, never only in a commit trailer. The effect stops at the audit trail. AC1's form at HEAD prints `4 4` (probed), and `--cached` over the pre-commit staged bytes measures the same delta.
- **Fix (skeptic judged SOUND):** Add the HEAD-form output to the AC1 evidence in a records commit before the close, naming the commit it ran at. Alternatively, record a spec revision that names the `--cached` form for the pass and the HEAD form for the close.
- **Left-shift gate:** The class is C5, the same gotcha, whose fix section already states the rule and which has no machine gate. So the left-shift is a checklist entry for the close: compare each criterion's command in the spec with the form its ledger line records, and require a spec amendment or an observation of the named form wherever they differ. Add this finding to the gotcha's "Where it bit" section as another deviation kept only in a trailer.

review-shape kind=diff-review round=1 intensity=full at=synth raw=5 confirmed=2 refuted=3 unverified=0 blocker=0 high=0 medium=0 low=2 agents=11 out-tokens=80862

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | memory/builds/dEasedEffort/README.md:38 | medium | - | refuted | Out of scope, because the defect is pre-existing. `git show 94188878:memory/builds/dEasedEffort/README.md` has the same sentence at lines 39-40, and the merge-base is that same commit. The README diff touches only the front matter and the generated regions, so README:38-39 is unchanged at the base. The sentence itself is false as the finder says: the loop near unattended.sh:13944-13962 fires fail 49 only when a path overlaps an output and another overlaps that output's declared generator, tools/roles/kit.toml:125-127 pairs `.claude/agents` with render_agents.py, not policy.toml, and the other `--writes` refusals I read do not catch that pair. But this diff did not introduce the false claim. It added the correct reading in spec §4 'Who renders', and §10 names the disagreement and says §4 states the source's reading, so the landed record flags the conflict. A residual slip is new in this diff and true: spec §10 says the brief carries the claim, while the brief says only 'The render is the main loop's second pass', and grep finds no `--dispatch` under prompts/. That is a low, wording-only misattribution with no behavioural effect, and it is not the finding's defect. | sound | C1 |
| 2 | correctness | memory/builds/dEasedEffort/README.md:38 | medium | - | refuted | The claim is factually true, but the defect is PRE-EXISTING, so it is out of scope. The false sentence is byte-identical at base: `git show 941888783...:memory/builds/dEasedEffort/README.md` has it at lines 39-40, and it sits at 38-39 only because this diff dropped the front-matter `status:` line. The README's hunks touch only that key and the generated regions, so the diff neither introduced the false reason nor made it reachable. A reader of the README inherits the same wrong reason at base. What the diff adds is the spec's correction. Spec section 4 says 'No refusal forces it', and section 10 names the README as carrying the wrong reading forward, so the disagreement is recorded, not silent. For the record, the substance checks out. `verb_dispatch` at unattended.sh:13944-13965 refuses only a declared GENERATED_INDEXES output with its generator. kit.toml:125-127 pairs `.claude/agents` with `render_agents.py`, not `house/policy.toml`, and commit 175f86981 ran the render and the policy edit in one pass. The defect is a stale reason in a build record, with no effect on any level. | sound | C2 |
| 3 | verification | tools/roles/README.md:184 | low | - | refuted | Pre-existing, so out of scope. The factual claim holds: `git grep` finds no reader of the sentence outside tools/roles/README.md:184. check_roles.py has no effort text and reads the README only for the catalogue region (R11), and render_agents.py has no stage comparison. But the defect is not new. At the base, the same line 184 read 'That is how `gov-skeptic` runs at `medium` in spec review and `high` in closing review', with the same two hard-coded levels and the same missing gate. The diff swapped the role name and changed nothing about the prose being hard-coded or unguarded, so it neither introduced nor exposed this exposure to drift. The sentence is also true at the reviewed head: `handoff.py stage-efforts` prints synthesis=medium for spec-review and synthesis=high for closing-review. The finding's wrong result therefore needs a hypothetical later policy edit, and no wrong output exists on this diff. The manual fix it cites (S3) corrected a sentence this build's own policy move made false, and that is done. | sound | - |
| 4 | intent | memory/builds/dEasedEffort/build/2026-11-02-build-TOOL-dEasedEffort-1-1-acceptance-ledger.md:21 | medium | low | confirmed | The record claim holds. Ledger line 21 was added by e74ef35e8, the same commit that adds the four `.claude/agents` changes, and it says the command printed the four paths 'on the render's commit'. Re-run: `git diff --name-only 2a6f3975 00866ea0a -- .claude` prints 0 lines, so HEAD before that commit could not have shown the paths. The same form at e74ef35e8 and at 918a95436 prints exactly the four. I tried three ways out. The reflog shows plain `commit:` entries for 00866ea0a, e74ef35e8 and 918a95436, with no amend or reset after 941888783. Among the 854 dangling commits, none dated in this build's window carries the render; the only ones are the abandoned 0434b8dd2 open-build commit and gov-claim commits. e74ef35e8 is the only commit after 00866ea0a that touches the ledger, so no later edit recorded a re-run. The recorded command on the recorded commit was therefore not observed when the line was written, and the spec's Rollout step 2 (observe, add the line, commit) with AC3's HEAD form makes that ordering unavoidable. It is confirmed as a record defect only. The result is true, so no code or level is wrong and nothing executes on the line, which grades it low under the rubric rather than the finder's medium. | sound | C5 |
| 5 | intent | memory/builds/dEasedEffort/build/2026-11-02-build-TOOL-dEasedEffort-1-1-acceptance-ledger.md:19 | low | low | confirmed | Spec AC1 (spec line 168) names `git diff --numstat 2a6f3975 HEAD -- tools/roles/house/policy.toml`. Ledger line 19 records `git diff --cached --numstat 2a6f3975` over the staged file. The trailer on 00866ea0a says the exact form 'is run after the commit and reported in the return'. `git grep numstat` under memory/builds/dEasedEffort finds only those two lines. e74ef35e8 added the AC3 line but left AC1's form as it was, and the agent ledger's return line holds only a commit sha, so no kept record shows the HEAD form observed. Spec section 9 has only rev-1, so nothing was amended, and the line is not in HYGIENE's AMENDED form. The gotcha's rule ('never only in a commit trailer') applies to the reason for the deviation. One nuance: the --cached spelling itself is visible in the ledger, so only the reason and the promised HEAD run are trailer-only. I re-ran AC1's form at HEAD and it prints `4 4`, so the result holds. --cached over the pre-commit staged bytes also measures the same delta. The effect is confined to the audit trail, with no effect on behaviour. | sound | C5 |
