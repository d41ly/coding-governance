**Serves:** journal TOOL-dDeclaredLoop-21

# Builder return — TOOL-dDeclaredLoop-21, dispatch 4: a landed step's program would change under the frozen-row rule, and the driver names no reading where the module or policy kit does not resolve

## Why

DIVERGENCE: rev-7 cannot be built as written. I found two problems, both probed read-only at base 12e930f8, and wrote nothing.

(1) §2 S8 and AC8 conflict with §7's `step-rows-frozen` leg.
- S8 has `tools/govkit/steps/fanout_cap.py` "re-pointed in this unit" to call the extracted `tools/govkit/steps/conf_to_policy.py`. AC8 requires that "the program imports `conf_to_policy`", and its "Red when" rules out leaving fanout_cap.py with its own copy.
- fanout_cap.py is the program that a landed `[[upgrade]]` row's argv names. That row is `agent-cap/fanout-cap-to-agents-in-flight` in tools/hooks/kit.toml, landed on main 2026-10-27 (dfcef45a7).
- Probe: `upgrade_steps.read_steps('.', <merge-base 5d48501d>, None)` returns that row with up = `['python', '{gov}/govkit/steps/fanout_cap.py', 'up', '{target}']`.
- tools/govkit/upgrade_steps.py#check_frozen compares that program's blob at the merge-base with HEAD's. Any byte edit appends "a landed step's program is frozen; ship the correction as a new step". Its docstring says the same: "an edited byte of a program a landed argv names reds".
- So building S8 as written turns `step-rows-frozen` red at the close.
- The spec has to choose one of:
  - (a) leave fanout_cap.py byte-identical, give conf_to_policy.py review_rounds.py as its only caller now, and drop AC8's import clause;
  - (b) re-point fanout through a new step row that retires the landed one to it, as the frozen-row rule asks;
  - (c) an owner ruling that exempts this edit. That is not a delegated resolver, because the frozen-row contract is the step kind's.

(2) §4 "How the shell reads it" and S4 do not say what `load_review_bounds` does when `review_bounds.py`, or the policy kit it reads through `resolve`, does not resolve beside the driver.
- tools/unattended/kit.toml requires the loop kit, but neither the unattended nor the loop kit.toml requires the policy kit. An adopter can therefore have unattended + loop without policy, and today it reads `REVIEW_ROUNDS` from its conf.
- The existing driver reader tools/unattended/unattended.sh#read_spec_audit_switch falls back to kit-default constants with a NOTE in that case. The spec names neither a fallback nor a refusal.
- The driver suite has a population S4 does not list:
  - tools/unattended/unattended.test.sh#write_switch_fixture copies only unattended.sh and lib-unattended.sh into `u/`, with the policy kit only on request and no loop kit at all.
  - `write_fold_fixture`, the TOOL-dFoldedAudit-14 left-shift block and `write_gate_fixture` build on it. Each appends `REVIEW_ROUNDS="1"` in a printf conf and runs `--review` (about 46 `run_fold`/`run_chain --review` call sites).
  - These fixtures have no remote, and they want bound 1, not the default 7.
- S4 sorts printf confs only into "runs no `--review`, line deleted" or "bounds a review, committed policy file at 7 before its own push". These match neither.
- Under a refusal they all fail 37 for want of the loop kit.
- The spec has to say:
  - whether an absent module or policy kit refuses, or reads the four catalogue defaults. The defaults would be a shell copy of four values, as the `SPEC_AUDIT_*_DEFAULT` constants are, and §4's "no shell copy" wording would have to admit them.
  - for refusal: S4 must list these fixtures and have them copy the loop and policy kits. Under no policy file they then read spec bound 1, so they need no policy commit.
  - for defaults: whether a refusal here adds a census site.

Every other rev-7 claim I probed holds at 12e930f8:
- driver census 326/326; check-unattended.sh 266/266; families 1/1, 11/11, 36/37
- the decision row `TOOL-dDeclaredLoop-21` is in memory/DECISIONS.md
- the REFUSAL_CEILINGS token and positional row stand at 326
- newest RUN*.md first-commit date is 2026-11-15, so ROUND_BOUND_CUTOFF would be 2026-11-16
- check-unattended.sh's `core_of FOLD_CUTOFF`, `rv_fc` and the single rv_bad `fail 2` are as cited
- the suite fixture's base commit and push to ORIGIN, and the bound-1 arm's region, are where the spec puts them
- the catalogue keys, defaults and allowed values are as S1 says (`round-count` min 0, so the module must refuse below 1 itself)
- `review_state`, `verb_review` and `RUNAWAY_CEILING` are as cited

## Summary

I committed nothing and changed nothing: TOOL-dDeclaredLoop-21 rev-7 can't be built as written. HEAD is still 12e930f80459a09d994750f0ccbfd6bac22d01b4, the tree is clean, and there is no patch file.

**Blocker 1 — the shared step extraction would turn the frozen-step check red.**
- §2 S8 and AC8 tell me to change `tools/govkit/steps/fanout_cap.py` so it imports the new `conf_to_policy.py`.
- That file is the program of a step that has already landed on main (`agent-cap/fanout-cap-to-agents-in-flight`).
- The `step-rows-frozen` check in §7 fails on any byte change to such a program. I confirmed the row is present at the merge-base and that the check compares the file's contents there with HEAD.
- The spec writer has three ways out:
  - leave `fanout_cap.py` untouched and drop AC8's import clause;
  - re-point it through a new step that retires the old one;
  - get an owner ruling exempting this edit.

**Blocker 2 — the spec doesn't say what the driver does when it can't reach the review-bounds module.**
- The unattended kit requires the loop kit, but neither the unattended kit nor the loop kit requires the policy kit, which `review_bounds.py` reads through.
- The driver's existing policy reader (`read_spec_audit_switch`) falls back to built-in defaults in that case. For the review bounds the spec says neither "fall back" nor "refuse".
- About 46 `--review` calls in `tools/unattended/unattended.test.sh` run on fixtures built by `write_switch_fixture`. Those fixtures copy only the driver, never the loop kit, have no remote, and set the round limit to 1. S4's list of fixtures to edit doesn't cover them.
- If an absent module means refusal, every one of those calls fails with check 37. The spec has to pick refuse or fall back, and say how these fixtures are treated.

`why` has the full detail, plus the list of rev-7 claims that still hold.

**What ran:**
- I read the build method, brief, spec and the second and third builder returns in full.
- I re-ran the earlier builder's census script, `C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/census21.py`, which uses `tools/memory-tree/check-arms.py`'s own readers. It reported the driver at 326 (its ceiling), `tools/unattended/check-unattended.sh` at 266, and families at 1/1, 11/11 and 36/37. It stands in for the census half of `harness arms (fail branches armed or pinned)`.
- A `python -c` call to `tools/govkit/upgrade_steps.py`'s row reader at the merge-base showed the fanout step's row there, and `git rev-parse` gave the program's identical blob at the merge-base and HEAD. Together with reading `check_frozen`'s code, that stands in for `step-rows-frozen`.
- No gate, suite or bar ran.

**Not done:**
- `--dispatch`: `memory/builds/dDeclaredLoop/RUN.md` has no dispatch row for this unit, despite what the task said, and a divergence declares nothing.
- `--brief`: `RUN.md` already has a brief row for this brief (03:05:42Z today), and a new one would have left `RUN.md` changed with nothing to commit it in.
- `gotchas.py --for-diff`: there's no commit to run it over.

**Owed at the close once the spec is revised and the unit is rebuilt:**
- the RED-first observation of the three `New arm:` lines: the review-bounds fixture plants (AC1–AC3), the govkit self-test arms (AC7–AC8), and the unattended and check-unattended suite arms (AC4, AC6), the last waived for this landing;
- a census read of the harness arms leg at 327 against the raised ceiling;
- `step-rows-frozen` over whichever S8 option is chosen.
