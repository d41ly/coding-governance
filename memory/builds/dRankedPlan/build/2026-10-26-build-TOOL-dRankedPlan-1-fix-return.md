**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-13 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16

# The fix pass's return — dRankedPlan

The gov-spec-writer return for the handoff `memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-3-spec-writer.md`, over the fix brief `memory/builds/dRankedPlan/prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-fix-brief.md`, extracted from its transcript by script, never retyped.

I fixed all nine findings in place across six specs. No status header changed, and each `**Carries:**` line, §3 edge and §8 mark stands unless a finding said otherwise. I committed nothing, and I did not run `check-spec-tokens.py` because my role doesn't allow it. I checked its path, bar and guards rules by reading them and by re-running a copy of the guards join over the edited specs, which now reports nothing missing.

**Findings**

1. **TOOL-dRankedPlan-16, AC7 (check 12).** AC7 now names its witness in backticks. The fixture build is `tFix` with two plan records that both match the record's file pattern: `2026-10-26-build-TOOL-tFix-1-plan-1.md` and `2026-10-27-build-TOOL-tFix-1-plan-1.md`. `handoff.py render --stdout` exits 1, its refusal prints both names, and it writes nothing.
2. **TOOL-dRankedPlan-16, Files touched (`[guards]`).** The line now names the source, `tools/roles/agents/gov-spec-writer.agent.md`, as the edit and the harness's agent file as its copy. The copy has no path token now, because it does not change: `render_agent_file` (`tools/roles/render_agents.py:144-155`) writes the front matter from fixed keys and never from `reads:`, and the current render has no `reads:` line. With the render path gone, nothing in Files touched trips `check-wiring self-test` or `lexicon naming predicates`, so the §7 leg line is unchanged.
3. **TOOL-dRankedPlan-1, §6 (`[path]`).** AC4 now reads "the view `PLAN.md` tracked at the memory root", and AC8 reads "`PLAN.md` at the memory root, and a file planted beside it as `OTHER.md`". The full `memory/PLAN.md` stays in §2, §4 and Files touched.
4. **TOOL-dRankedPlan-13, AC1 and AC7 (`[path]`).** The planted paths are now described as planted in the fixture tree and named by basename: `a.py` in the `alpha` kit directory, the `beta` directory, `x.md` in a docs directory, and `new.py` in `alpha`. AC7 refers to "AC1's planted `a.py` and its docs directory". The expected output `alpha, beta, unkitted` is unchanged.
5. **TOOL-dRankedPlan-2, AC6 (`[bar]`).** AC6 now watches the hook itself in a scratch clone of the pass tip. The hooks path is set to `.githooks`, and `.governance/policy.toml` gets a `[plan]` table with `authority = "owner-orders"`, committed with `--no-verify` as setup.
   - Staging one README that adds `priority: 1` and running `git commit -m probe > out.txt 2>&1` must exit non-zero, and `grep "plan order — refused" out.txt` must show the line naming the build and `owner-orders`.
   - Staging only a file that is not a README, `grep -c "plan order" out.txt` must print 0.
   - I used `owner-orders` because that case does not depend on unit 9's ratification predicate. The suite was already declared on §7's `New arm: .githooks/pre-commit.test.sh` line.
6. **TOOL-dRankedPlan-6, AC3 (`[bar]`).** AC3 now greps the rendered `tier2-review.js` for `SPEC_SUBJECT_PATH` and `PIN_ID`, verified at :317 and :416, and tests both patterns with `node -e`. The planted plan record's path must not match `SPEC_SUBJECT_PATH`, so it is served bare with no `rev` (:428-434), and the id `TOOL-dX-1` must match `PIN_ID`. The stub-agent run of the whole review script, five finder spawns and the bare binding line, is now left to the existing `New arm: tools/workflows/tier2-review.test.sh` line.
7. **TOOL-dRankedPlan-5, Files touched (`[guards]`).** The bare `memory/builds/` is replaced by the record pattern `memory/builds/<slug>/build/<date>-build-<first-unit-id>-disposition-<n>.md`, following TOOL-dDeclaredLoop-16 S4's naming. That path still trips the `memory/` guard, so `recall floor` and `recall floor arms`, spelled as `tools/gate-legs.json` names them, are added to the §7 leg line.
8. **TOOL-dRankedPlan-2 → TOOL-dRankedPlan-15 (`[handoff]`).** Unit 15 does not read `plan.authority`. That policy governs the plan's order: the `priority:`/`parents:` front matter and the order of builds in `PLAN.md`, which unit 2's hook enforces. Unit 15 rewrites the plan record's fields, and its ratification goes through `plan.ratification` and units 9 and 10 (§2 S5, §8 F3). So I corrected unit 2's bullet to: "`gov-planner`, the slot that records a plan revision with `revise`, ratified as the plan is". Both of its backticked names already appear in unit 15, whose `consumes-from TOOL-dRankedPlan-2 — gov-planner` edge was already there. Unit 15 is unchanged.
9. **Hygiene re-run.** `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exits 0. Its only lines naming dRankedPlan files are check 25's "did not grade … READER NOT IN TREE" notes on specs 10, 16, 2 and 3, which are notes and not findings. However, check 12 also stayed silent on AC7 in a run before my edit, in this worktree. So its silence is not evidence that the AC7 fix is graded. AC7 now contains backticked text, which is all check 12's witness test looks for.

**Outside these findings:** TOOL-dRankedPlan-6 names the plan record `…-1-plan.md` in its §4 example and its AC3. TOOL-dRankedPlan-16 §8 F1 settled the name as `-1-plan-1.md`. I left spec 6's name as written because the brief limits me to the listed findings, but the two specs disagree.

Files changed, all in `C:\projects\coding-governance\.claude\worktrees\unattended-drankedplan-1fc3d7\memory\builds\dRankedPlan\spec\`:
- `2026-10-26-spec-TOOL-dRankedPlan-1.md`
- `2026-10-26-spec-TOOL-dRankedPlan-2.md` (its CRLF line endings kept)
- `2026-10-26-spec-TOOL-dRankedPlan-5.md`
- `2026-10-26-spec-TOOL-dRankedPlan-6.md`
- `2026-10-26-spec-TOOL-dRankedPlan-13.md`
- `2026-10-26-spec-TOOL-dRankedPlan-16.md`
