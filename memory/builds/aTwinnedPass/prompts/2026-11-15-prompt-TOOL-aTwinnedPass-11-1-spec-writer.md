**Serves:** journal TOOL-aTwinnedPass-11

# gov-spec-writer handoff — TOOL-aTwinnedPass-11

<!-- gov:handoff role=gov-spec-writer build=aTwinnedPass unit=TOOL-aTwinnedPass-11 path=memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-11-1-spec-writer.md role-sha=a3bc1199e30f task-sha=07db94c9b4cb -->

## Role

[.claude/agents/gov-spec-writer.md · Level 5 · This role's static instructions; yields to levels 0 to 4]
You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite it by `path#symbol` or the
  blob-pinned line `<path>@<oid>:<n>`. A claim you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the memory hygiene gate and the naming lexicon over your specs, and, where this
  repository has it, the spec-token checker as `check-spec-tokens.py --spec <path>` over each spec
  you wrote, fixing every hit it names before you return. You run no other gate.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns. At a spec audit's disposal, a correction to an unbuilt sibling's spec
rewrites that sibling's text, with a rev bump and a revision-log line naming the repair unit and
the review record by its file stem, and a CLOSED sibling stays frozen.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## House rules

A `check-spec-tokens.py --spec` run that finds a miss exits 1. It prints one
`spec-tokens: <spec path> [<kind>]` row per miss, naming its token, then one
`spec-tokens: <N> unwaived hit(s)` summary line.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.

### Drive

- spec-write · gov-spec-writer — a build whose units lack a spec or hold a thin one: `Workflow <prefix>/workflows/unattended-build.js`
[/.claude/agents/gov-spec-writer.md]

## Task

[AGENTS.md#practices-at-design · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them; the override is recorded]
### Practices at design

- [yagni] no extension point, option or layer the unit does not use
- [reuse] a kind's second instance extracts its factory
- [core] logic and authorization live in one core, each surface a thin adapter
- [contract] one source, generated copies, a parity gate against a live re-derivation
- [derive] status, counts, inventories and indexes are generated or declared
- [one-fact] each value has one owning source
- [gate] state what a gate does not check
- [class] a guard shares no state with what it guards
- [cost] declare a wall-clock ceiling for each suite
- [migrations] every migration is reversible
- [security] deny by default and give automation the narrowest grant
- [bound] a fan-out declares its bound
[/AGENTS.md#practices-at-design]

## Card

[.claude/orientation-card.md · Level 1 · the build's card: where this session stands; level 0 outranks it]
- build: aBenchedTwin
- unit: TOOL-aBenchedTwin-1 · spec memory/builds/aBenchedTwin/spec/2026-11-15-spec-TOOL-aBenchedTwin-1.md
- unit: TOOL-aBenchedTwin-2 · spec memory/builds/aBenchedTwin/spec/2026-11-15-spec-TOOL-aBenchedTwin-2.md
- brief: memory/builds/aBenchedTwin/prompts/2026-11-15-prompt-TOOL-aBenchedTwin-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-11-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aTwinnedPass`, unit `TOOL-aTwinnedPass-11`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> Make the unattended build harness able to build two or more units of one build at the same time, as gov work: `/session-kickoff` first, a build of its own with a spec, a gov-builder for the code, landing on main through `bash tools/push-main.sh` on a green bar only under the charter's [land] rule.

> Design target: each parallel pass builds in its own worktree on its own branch cut from the run's tip; product files are checked disjoint by `--dispatch` as now, while generated files are left to the main loop, which merges each pass back (`--no-ff`, or a cherry-pick, your call in the spec) and regenerates the shared indexes once.

> Done looks like: a spec with its forks, the change built and its arms seen red then green, a measured before and after of two disjoint units built serially versus in parallel on a frozen clone, and the work landed on main or left on its branch with a line saying what is left.

The task came from the session that started this one, on the owner's request. It is quoted in part; the passages above are the ones this build serves.

### brief:goal

A parallel pass the unit harness spawns inside a Workflow merges back. Today it cannot: the shapes `TOOL-aTwinnedPass-4` built admit only the Agent tool's worktree spelling, and the Workflow runtime cuts another, so the harness blanks the pass's branch and worktree and `pass-tree.sh` refuses the branch.

### brief:items

1. `TOOL-aTwinnedPass-11`, order 5, consuming from `TOOL-aTwinnedPass-4`: one mechanism, the runtime's two observed worktree spellings admitted wherever unit 4 admits one. Observed on node a, 2026-11-15, in `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-2-measurement.md`: inside a Workflow, `agent()` with `isolation: 'worktree'` cuts `<primary>/.claude/worktrees/wf_<run id>-<n>` on the branch `worktree-wf_<run id>-<n>`, the run id spelled like `wf_0d688c69-edb` (so `wf_0d688c69-edb-1`); the Agent tool cuts `<primary>/.claude/worktrees/agent-<id>` on `worktree-agent-<id>`. In both the branch is `worktree-` plus the worktree's last segment.
2. `tools/workflows/unattended-unit.js`: `BRANCH_SHAPE` and `TREE_SHAPE` admit both spellings and still refuse every hostile value unit 4's arms feed them; nothing else in the harness moves. `tools/unattended/pass-tree.sh`: `check_pass_branch` admits both branch spellings, and `check_pass_holder` keeps its rule, the holder exactly `<primary>/.claude/worktrees/<branch less worktree->`, for both. The pattern is stated once per file; the spec says how the two files' copies are held to one another, or names the parity arm as owed under the ask `TOOL-aTwinnedPass-7` already filed.
3. Arms: in `tools/workflows/unattended-build.test.sh`, a return with a `wf_` branch and worktree comes back unchanged and `nextAction` names the worktree; in `tools/unattended/pass-tree.test.sh`, a pass cut as `worktree-wf_<id>-1` at `.claude/worktrees/wf_<id>-1` merges back, and one whose holder sits at another `wf_` name is refused. Each arm names its staged break.
4. Spec Tier-2, status SPECCED, rev-1, node a, base the build's tip, streams tooling, order 5, its Edges naming `TOOL-aTwinnedPass-4` and the measurement record. Spec 4 is CLOSED and stays frozen: this spec states which of spec 4's lines it supersedes. Name new functions through the lexicon; a choice not derivable is a fork with a recommendation, among them whether to admit any `worktree-<name>` whose holder is `.claude/worktrees/<name>` rather than the two observed prefixes.

### brief:acceptance

- Through the build harness suite's runner, a `wf_` return is carried, and every hostile value unit 4's arms feed is still refused.
- In the pass-tree suite's fixture, a `wf_`-spelled pass merges back and a mismatched `wf_` holder is refused.
- Every new arm is observed red, then green, by the main loop at the close.

### brief:gates

The new arms, run directly by the main loop at the close. `check-arms` over the driver suite and the unit harness's suite. The lexicon and codebase-map legs the change owes. The merge bar once at the close, without the self-test suites.

### brief:non-goals

- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`: the live run's branch rewrote them, and any change there conflicts when it merges main.
- `memory/builds/dDeclaredLoop/`, its run's worktree, its branch and its run-state file.
- A change to the build harness `unattended-build.js`, to the unattended Skill's loop, or to how a main loop picks which units go together: the build order and M6 already say which may.
- Resolving a conflict on any path that is neither an effective generated output nor a gen-region-only change.
- A cap on how many passes run at once: that is the review protocol's fan-out bound, unchanged.
- ANY SELF-TEST SUITE OR BAR INSIDE A BUILD PASS, A SLICED SUITE INCLUDED. A pass runs only direct checks: `bash -n`, `node --check`, `check-arms`, the lexicon, the changed code invoked over a hand-built fixture, the spec-token checker, and `gen_map.py --write`. New arms are written and checked with `bash -n`; the main loop observes each red and then green at the close.
- A pass commit without its acceptance ledger: each pass commit carries `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-<n>-1-acceptance-ledger.md`, one `**Evidences:** TOOL-aTwinnedPass-<n>` block naming each criterion with the backticked token the criterion itself spells, and the arms' red-then-green named as owed to the main loop.
- An edit after the commit that sets a spec CLOSED: every edit lands first, and the status flip is the last change of the pass.

### task:reuse

lib-unattended.sh resolve_generated_indexes, check_gen_region_only, covers; unattended.sh check_commit_message's generated exemption; push-main.sh run_regen and regen.py --write; unattended-unit.js prebuild and passLegs key shape; lib-attribute.sh add_scratch_worktree.

### card:route

- build: aBenchedTwin
- unit: TOOL-aBenchedTwin-1 · spec memory/builds/aBenchedTwin/spec/2026-11-15-spec-TOOL-aBenchedTwin-1.md
- unit: TOOL-aBenchedTwin-2 · spec memory/builds/aBenchedTwin/spec/2026-11-15-spec-TOOL-aBenchedTwin-2.md
- brief: memory/builds/aBenchedTwin/prompts/2026-11-15-prompt-TOOL-aBenchedTwin-1-brief.md
[/memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-11-1-spec-writer.md]
