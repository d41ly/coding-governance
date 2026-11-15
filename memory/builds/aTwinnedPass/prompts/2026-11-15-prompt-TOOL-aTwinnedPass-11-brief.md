# Brief — aTwinnedPass: the Workflow runtime's worktree spelling, admitted at both ends of the handoff

**Serves:** research TOOL-aTwinnedPass-11

## The prompt

> Make the unattended build harness able to build two or more units of one build at the same time, as gov work: `/session-kickoff` first, a build of its own with a spec, a gov-builder for the code, landing on main through `bash tools/push-main.sh` on a green bar only under the charter's [land] rule.

> Design target: each parallel pass builds in its own worktree on its own branch cut from the run's tip; product files are checked disjoint by `--dispatch` as now, while generated files are left to the main loop, which merges each pass back (`--no-ff`, or a cherry-pick, your call in the spec) and regenerates the shared indexes once.

> Done looks like: a spec with its forks, the change built and its arms seen red then green, a measured before and after of two disjoint units built serially versus in parallel on a frozen clone, and the work landed on main or left on its branch with a line saying what is left.

The task came from the session that started this one, on the owner's request. It is quoted in part; the passages above are the ones this build serves.

## The brief

### Goal
A parallel pass the unit harness spawns inside a Workflow merges back. Today it cannot: the shapes `TOOL-aTwinnedPass-4` built admit only the Agent tool's worktree spelling, and the Workflow runtime cuts another, so the harness blanks the pass's branch and worktree and `pass-tree.sh` refuses the branch.

### Items
1. `TOOL-aTwinnedPass-11`, order 5, consuming from `TOOL-aTwinnedPass-4`: one mechanism, the runtime's two observed worktree spellings admitted wherever unit 4 admits one. Observed on node a, 2026-11-15, in `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-2-measurement.md`: inside a Workflow, `agent()` with `isolation: 'worktree'` cuts `<primary>/.claude/worktrees/wf_<run id>-<n>` on the branch `worktree-wf_<run id>-<n>`, the run id spelled like `wf_0d688c69-edb` (so `wf_0d688c69-edb-1`); the Agent tool cuts `<primary>/.claude/worktrees/agent-<id>` on `worktree-agent-<id>`. In both the branch is `worktree-` plus the worktree's last segment.
2. `tools/workflows/unattended-unit.js`: `BRANCH_SHAPE` and `TREE_SHAPE` admit both spellings and still refuse every hostile value unit 4's arms feed them; nothing else in the harness moves. `tools/unattended/pass-tree.sh`: `check_pass_branch` admits both branch spellings, and `check_pass_holder` keeps its rule, the holder exactly `<primary>/.claude/worktrees/<branch less worktree->`, for both. The pattern is stated once per file; the spec says how the two files' copies are held to one another, or names the parity arm as owed under the ask `TOOL-aTwinnedPass-7` already filed.
3. Arms: in `tools/workflows/unattended-build.test.sh`, a return with a `wf_` branch and worktree comes back unchanged and `nextAction` names the worktree; in `tools/unattended/pass-tree.test.sh`, a pass cut as `worktree-wf_<id>-1` at `.claude/worktrees/wf_<id>-1` merges back, and one whose holder sits at another `wf_` name is refused. Each arm names its staged break.
4. Spec Tier-2, status SPECCED, rev-1, node a, base the build's tip, streams tooling, order 5, its Edges naming `TOOL-aTwinnedPass-4` and the measurement record. Spec 4 is CLOSED and stays frozen: this spec states which of spec 4's lines it supersedes. Name new functions through the lexicon; a choice not derivable is a fork with a recommendation, among them whether to admit any `worktree-<name>` whose holder is `.claude/worktrees/<name>` rather than the two observed prefixes.

### Acceptance
- Through the build harness suite's runner, a `wf_` return is carried, and every hostile value unit 4's arms feed is still refused.
- In the pass-tree suite's fixture, a `wf_`-spelled pass merges back and a mismatched `wf_` holder is refused.
- Every new arm is observed red, then green, by the main loop at the close.

### Gates
The new arms, run directly by the main loop at the close. `check-arms` over the driver suite and the unit harness's suite. The lexicon and codebase-map legs the change owes. The merge bar once at the close, without the self-test suites.

### Non-goals
- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`: the live run's branch rewrote them, and any change there conflicts when it merges main.
- `memory/builds/dDeclaredLoop/`, its run's worktree, its branch and its run-state file.
- A change to the build harness `unattended-build.js`, to the unattended Skill's loop, or to how a main loop picks which units go together: the build order and M6 already say which may.
- Resolving a conflict on any path that is neither an effective generated output nor a gen-region-only change.
- A cap on how many passes run at once: that is the review protocol's fan-out bound, unchanged.
- ANY SELF-TEST SUITE OR BAR INSIDE A BUILD PASS, A SLICED SUITE INCLUDED. A pass runs only direct checks: `bash -n`, `node --check`, `check-arms`, the lexicon, the changed code invoked over a hand-built fixture, the spec-token checker, and `gen_map.py --write`. New arms are written and checked with `bash -n`; the main loop observes each red and then green at the close.
- A pass commit without its acceptance ledger: each pass commit carries `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-<n>-1-acceptance-ledger.md`, one `**Evidences:** TOOL-aTwinnedPass-<n>` block naming each criterion with the backticked token the criterion itself spells, and the arms' red-then-green named as owed to the main loop.
- An edit after the commit that sets a spec CLOSED: every edit lands first, and the status flip is the last change of the pass.

