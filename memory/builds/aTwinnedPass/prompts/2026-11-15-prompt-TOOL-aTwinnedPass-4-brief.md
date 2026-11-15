# Brief — aTwinnedPass: the closing review's round-1 items, promoted to two units

**Serves:** research TOOL-aTwinnedPass-4 TOOL-aTwinnedPass-5

## The prompt

> Make the unattended build harness able to build two or more units of one build at the same time, as gov work: `/session-kickoff` first, a build of its own with a spec, a gov-builder for the code, landing on main through `bash tools/push-main.sh` on a green bar only under the charter's [land] rule.

> Design target: each parallel pass builds in its own worktree on its own branch cut from the run's tip; product files are checked disjoint by `--dispatch` as now, while generated files are left to the main loop, which merges each pass back (`--no-ff`, or a cherry-pick, your call in the spec) and regenerates the shared indexes once.

> Done looks like: a spec with its forks, the change built and its arms seen red then green, a measured before and after of two disjoint units built serially versus in parallel on a frozen clone, and the work landed on main or left on its branch with a line saying what is left.

The task came from the session that started this one, on the owner's request. It is quoted in part; the passages above are the ones this build serves.

## The brief

### Goal
Close every confirmed item of the closing review's round 1, `memory/builds/aTwinnedPass/reviews/2026-11-15-review-TOOL-aTwinnedPass-1-2-3-closing-diff-round1.md`, by severity as `doc.build-method#m8-closing-the-build` disposes them: its three HIGH items become units whose mechanism closes them, and its MEDIUM and LOW items are batched. The pass's identity, the branch and worktree a builder returns and the sha the main loop merges from, crosses every handoff only in the spelling the runtime cuts; and every suite arm this build added can go red on the regression it names.

### Items
Two units. Read the review report whole first; each item below names its finding by the report's label, and the report's Fix and corrected-fix text is the starting design, to be verified against the code at the build's tip.

1. `TOOL-aTwinnedPass-4`, order 3, closing H1, H2, M1 and M3: one mechanism, the pass identity held to the runtime's spelling at both ends of the handoff. `tools/workflows/unattended-unit.js`: BRANCH_SHAPE becomes `^worktree-agent-[A-Za-z0-9]+$`; TREE_SHAPE admits only an absolute path whose last two segments are `.claude/worktrees/agent-<id>` (either separator), drawn from a class with no shell metacharacter, and no `..` segment, as the build harness refuses one for `scratch` and `repo`; a value failing either shape returns `''`, as today. `tools/unattended/pass-tree.sh`: `check_pass_branch` refuses a branch outside `^worktree-agent-[A-Za-z0-9]+$`; `remove_pass_tree` refuses unless the holder `derive_holder_where` finds sits at `<primary tree>/.claude/worktrees/agent-*`, keeping `--force` for that confined holder; `--from` accepts 7 to 64 lower-case hex digits, as COMMIT_SHAPE does, with its refusal text and spec 2's lines naming 40 made true. Arms: in `tools/workflows/unattended-build.test.sh`, hostile returns (`$(id)`, a double quote, `;`, a `..` segment, a backtick, a newline, each after a valid prefix) come back `''` and `nextAction` names none of them; in `tools/unattended/pass-tree.test.sh`, `--remove` naming a fully pushed branch held by a worktree outside `.claude/worktrees/agent-*` exits 1 with that worktree still present, a `--merge` naming such a branch is refused the same way, and a 64-digit `--from` is admitted by the shape check.
2. `TOOL-aTwinnedPass-5`, order 4, consuming from unit 4 because both edit the two suites, closing H3, M2, M4, M5, M6, L1 and L2, and the arms `T2 branch agent-p4 remains` and `T5 branch agent-p7 remains`: one mechanism, every arm of this build's three suites able to go red on the regression it names. H3: the T3 absence needle becomes text the subject emits, and spec 1's T3 line says so. M2: the own-side arm after B6. M4: the three `check_pass_tree_run` refusals. M5: the exit-2 usage paths. M6: a render that creates a generated file fresh and one that leaves a non-generated file. L1: drop the vacuous `--check-commit` arm or pair it with the negative control the report gives. L2: B1's note read from stdout alone. The two `remains` arms read the branch through `git rev-parse --verify -q refs/heads/<b>` or strip git's `+` worktree marker, since the tool is correct and both arms are red at the tip. Every floor the arms raise is raised with its RAISED line, and each new arm names the staged break that turns it red.
3. Each spec, Tier-2, status SPECCED, rev-1, node a, base `c40c39fb6`, streams tooling, names its review ids on its status line or in its Edges as the house shape does, and states what it does not check. The report's left-shift gates (a hostile-string class arm, an absence-needle rule, a refusal-site rule, an exit-code rule, a two-sided skip rule, a stream rule, a sha-shape parity arm) are not built here: each spec lists them for the main loop to file as asks, which is M8's left-shift disposition where a unit does not build the gate.
4. Verify every line the report cites at `c40c39fb6` against the build's tip before relying on it; the report pins `c40c39fb`. Name each new function through `python tools/lexicon/lexicon.py --suggest`. A choice not derivable is a fork in section 8 with a recommendation.

### Acceptance
- Unit 4: through the build harness suite's runner, each hostile `worktree` or `branch` return comes back `''` and no `nextAction` carries it; in a fixture repository, `--remove` and `--merge` refuse a branch or holder outside the runtime's spelling and leave that worktree in place; a 64-digit `--from` passes the shape check.
- Unit 5: each corrected or added arm is green at the tip and red under the staged break its spec names; `pass-tree.test.sh` runs with no FAIL line.
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

