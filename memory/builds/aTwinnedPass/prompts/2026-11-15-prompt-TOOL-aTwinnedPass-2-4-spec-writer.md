**Serves:** journal TOOL-aTwinnedPass-2

# gov-spec-writer handoff — TOOL-aTwinnedPass-2

<!-- gov:handoff role=gov-spec-writer build=aTwinnedPass unit=TOOL-aTwinnedPass-2 path=memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-2-4-spec-writer.md role-sha=a3bc1199e30f task-sha=5d4c8f2a3a7a -->

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
- build: aTwinnedPass
- unit: TOOL-aTwinnedPass-1 · spec memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-1.md
- unit: TOOL-aTwinnedPass-2 · spec memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-2.md
- unit: TOOL-aTwinnedPass-3 · spec memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-3.md
- brief: memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-2-4-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aTwinnedPass`, unit `TOOL-aTwinnedPass-2`.
Not supplied, optional: `input:code`.

### brief:prompt

> Make the unattended build harness able to build two or more units of one build at the same time, as gov work: `/session-kickoff` first, a build of its own with a spec, a gov-builder for the code, landing on main through `bash tools/push-main.sh` on a green bar only under the charter's [land] rule.

> Design target: each parallel pass builds in its own worktree on its own branch cut from the run's tip; product files are checked disjoint by `--dispatch` as now, while generated files are left to the main loop, which merges each pass back (`--no-ff`, or a cherry-pick, your call in the spec) and regenerates the shared indexes once.

> Done looks like: a spec with its forks, the change built and its arms seen red then green, a measured before and after of two disjoint units built serially versus in parallel on a frozen clone, and the work landed on main or left on its branch with a line saying what is left.

The task came from the session that started this one, on the owner's request. It is quoted in part; the passages above are the ones this build serves.

### brief:goal

The session's worktree lock refuses every write to the pass worktree dazzling-jackson-b895c0-p1, and the brief forbids writes anywhere else; getting around the refusal through Bash would break the [tools] rule. Start the builder with its working directory in the pass worktree, or redo the pass brief so the pass worktree is the session's own.

### brief:items

Revision items, R1 to R6, come first and bind units 1 and 2; the original items follow them and still bind where no revision item replaces them.

R1. Observed 2026-11-15 on node a: two gov-builders spawned by the Agent tool from a session bound to worktree `dazzling-jackson-b895c0`, each told to work in a hand-cut worktree `dazzling-jackson-b895c0-p1` or `-p3`, both had their first Edit refused by the harness with "belongs to a different worktree. Do not write to other worktrees' files from this session." Writing through Bash would route around that refusal, which the charter's [tools] rule forbids, so both returned committed:false with nothing written. A path handed to a builder in its prompt therefore cannot be where it builds.
R2. Observed the same day: an Agent call with `isolation: "worktree"` gets a worktree the runtime cuts at `<primary tree>/.claude/worktrees/agent-<agentId>` on a new branch `worktree-agent-<agentId>`, at `aebbb4a72`, the default branch's tip, not the dispatching session's branch tip `8397ac8ca`; the agent's session is bound to that worktree, so its writes there are admitted. The workflow runtime's `agent()` takes the same option, `isolation: 'worktree'`, and its reference says such a worktree "is auto-removed if unchanged". `TOOL-dDerivedDocket-55` recorded the same base and its remedy, a hard reset to the group commit.
R3. Unit 1 (`TOOL-aTwinnedPass-1`): replace the `tree` path key with a key naming the commit the pass starts from (name it through the lexicon or by the harness's key conventions). With it, the one `agent()` call carries `isolation: 'worktree'`, and the prompt's first order is to run `git reset --hard <that commit>` in the agent's own worktree and confirm `git rev-parse HEAD` prints it, before any other command; `writes` and the unattended driver-steps change stay as specified. The builder returns the worktree's branch and top-level path, which the return carries after a shape check, as `sha` and `base` are checked before `nextAction` spells them. Without the key, everything is byte-identical, as now.
R4. Unit 2 (`TOOL-aTwinnedPass-2`): the runtime now does the cut, so drop `--cut` and the derived `<run tree>-p<seq>` names. `--merge` takes the pass's branch, as the unit harness returned it, and keeps every other step: the run check, the clean test, `--no-ff --no-commit`, the conflict resolution through `check_generated_output` and `check_gen_region_only`, the regeneration, the `Pass: none` commit. It refuses a branch whose merge base with `HEAD` is not the commit the pass was dispatched from, since a builder that skipped the reset would carry the default branch's history in. After the commit it removes that branch's worktree, found by `git worktree list --porcelain`, and deletes the branch. `--remove` takes a branch too, for a pass that returned committed:false.
R5. The header and the verbs guide state the revised order: `--dispatch` and `--brief` per unit, one records commit carrying the rows and the brief files, then one `unattended-unit.js` call per unit with the commit key and `writes`, run concurrently, then `--merge` per committed pass in turn, `--remove` per uncommitted one.
R6. Keep every fork already RESOLVED unless a revision item contradicts it, and say in section 9 which items this revision changed.

Items as briefed, numbered as before:
Three units, one mechanism each. Items 1 to 4 are `TOOL-aTwinnedPass-1`'s, 5 to 10 are `TOOL-aTwinnedPass-2`'s, 11 to 13 are `TOOL-aTwinnedPass-3`'s, and 14 to 18 bind all three.

1. `tools/workflows/unattended-unit.js` takes an optional `tree` key: the absolute path of the worktree this one pass builds in. Absent, the prompt, the spawn options, the log and the return are byte-identical to the file without it. Present, it is refused unless it is a non-empty single-line string with no backtick and an absolute path, graded as `prebuild` and `passLegs` are graded, because it is spelled into the prompt.
2. With `tree`, the prompt orders every read, write, shell command and the commit to happen in that worktree: every shell call runs with its working directory there, and every file path the agent writes resolves under it. The `base` the builder returns is that worktree's `HEAD` before its first write.
3. With `tree` in unattended mode, the driver steps change: the main loop declared this pass's write set with `--dispatch` and recorded its brief with `--brief` on the run's branch, at the commit the tree was cut from, so the builder calls neither. Both write the run-state file, which M6 condition 3 forbids a concurrent pass to touch and which this tree's branch would only carry back as a conflict. The prompt names the declared write set, which arrives as a second optional key, `writes`, a single-line space-separated path list graded like `prebuild`, required whenever `tree` is given in unattended mode. In attended mode `tree` changes only item 2's sentence.
4. With `tree`, the return carries `tree`, and the `nextAction` that `passLegs` produces names the worktree the pass legs run in, since the pass commit is `HEAD` there and not in the run's tree. The `meta.version` moves to 1.2 and the header comment states the key beside `prebuild`, `roles`, `efforts` and `passLegs`. Arms in `tools/workflows/unattended-build.test.sh`, through its existing runner: the refusals, the byte-identical default, the unattended driver steps with `tree`, and the `nextAction` naming the tree.
5. A new kit tool in `tools/unattended/` (the spec decides the file name through the lexicon; the recommendation is a shell script sourcing `tools/unattended/lib-unattended.sh`, because the two predicates it needs live there and a copy is two answers to one question) with two verbs, run by the main loop in the run's own tree.
6. The cut verb, given the build slug and a unit id: refuses unless the current tree is the run's (the run-state file binds this branch, read as `--check-commit` reads it), the tree is clean, and the unit has an open dispatch row; then `git worktree add -b <branch> <path> HEAD` and prints the path on stdout and nothing else there. The branch and path names are derived from the run's branch, its tree and the unit's sequence number, short enough for MAX_PATH on node `a`; the spec states the derivation. Cutting a unit that already has a tree is refused, naming it.
7. The merge verb, given the build slug and a unit id: refuses unless the current tree is the run's and clean and the unit's branch exists and is ahead of `HEAD`'s merge base with it; then `git merge --no-ff --no-commit` of that branch. Every conflicted path is resolved to this side only when it is covered by an effective generated output (`resolve_generated_indexes`), or when the pass changed it only inside gen regions (`check_gen_region_only` over the merge base's blob against the branch's blob). Any other conflicted path aborts the merge, `git merge --abort`, and refuses with exit 1 naming each path: the two passes were not disjoint, and that is never resolved here.
8. After resolution the merge verb runs `regen.py --write` from the run-gates kit, found as `push-main.sh`'s `run_regen` finds it, stages every tracked change and every new file under an effective generated output, and commits. The subject names the unit, `merge(<slug>): <unit-id>'s pass tree`, so the routed-commits leg reads it; the message ends with a `Pass: none` trailer so neither `--check-commit`, check 23 nor `pass_commit` reads the merge as the pass commit, which stays the builder's own commit on the second parent. Then it removes the worktree and deletes the branch, and prints the merge sha.
9. The tool states, in its header, the order the main loop runs it in: for a group of units the build order marks parallel, `--dispatch` and `--brief` for each on the run's branch, one `records` commit carrying their rows with `Pass: none`, then the cut verb for each, then one `unattended-unit.js` call per unit with `tree` and `writes`, run concurrently, then the merge verb for each committed pass in turn. A pass that returns `committed:false` has its tree removed and its branch deleted by the merge verb's sibling cleanup, or the spec names how; the spec decides and states which.
10. The tool's suite, `tools/unattended/` beside it, through a fixture repository with a run-state file: cut and merge of two disjoint passes with a conflicting generated output and a conflicting gen region, both resolved, the regenerated output committed and the second parent the pass commit; a product-path conflict aborted with exit 1 and the tree left as before the merge; each refusal. The kit's `kit.toml`, version and README name the tool; the verbs guide's "Drive the build as ONE program" paragraph names the parallel route, at the guide's source in the unattended kit; the help page covering unattended passes, if one exists, says so too, else the spec decides whether `help/` owes one by the docs leg's rule.
11. `verb_dispatch` in `tools/unattended/unattended.sh`, condition 1: a declared path covered by an effective generated output (`${GENERATED_INDEXES}`, the index half of each pair, through `covers`, as `check_commit_message` already reads it) is not compared against the siblings, on either side. Every other refusal, condition 3's generator pairing included, is unchanged, and the declaration row still records every path declared.
12. One `stderr` note per call naming the paths left out of the sibling comparison, beside the run-state file's existing note, so a reader of the run log sees the narrowing.
13. Arms in `tools/unattended/unattended.test.sh`: two siblings declaring one generated output both admitted; two siblings declaring one product path still refused; the note printed. Re-key `tools/unattended/unarmed-branches.txt` if a `fail 49` ordinal moves.
14. One spec per unit under `memory/builds/aTwinnedPass/spec/`, Tier-2, status SPECCED, rev-1, node a, base `aebbb4a72`, streams tooling. Order: units 1 and 3 at order 1, unit 2 at order 2 with a `consumes-from` edge on unit 1, because its header documents unit 1's keys. Shape: `memory/TEMPLATE-SPEC.md`; `memory/builds/aBriskDeclaration/spec/2026-11-14-spec-TOOL-aBriskDeclaration-1.md` is the worked example of a change to `--dispatch`. Work only in this worktree.
15. Each spec's `closes` names the ask it closes: unit 1 `TOOL-dDerivedDocket-55`, unit 2 `TOOL-dDerivedDocket-57`; unit 3 closes none. Read both asks in `memory/builds/dDerivedDocket/BACKLOG.md` and the routes record `memory/builds/cBriefedPilot/build/2026-08-15-build-TOOL-cBriefedPilot-15-2-parallelism-routes.md` (its R5) before designing.
16. Verify every claim this brief makes about current code by reading that code: `unattended-unit.js`, `verb_dispatch` condition 1 and condition 3, `check_commit_message`, `resolve_generated_indexes`, `check_gen_region_only`, `covers`, `overlaps`, `pass_commit`, `push-main.sh#run_regen`, `tools/run-gates/regen.py`, the `merge=ours` rows of `.gitattributes`, and `tools/hooks/scratch-guard.js#checkOriented` (a subagent's commit is not orientation-gated). Report anything here that is wrong.
17. Decide each new function's, file's and key's name through `python tools/lexicon/lexicon.py --suggest`, and state what each unit owes beyond its code: the codebase map, the symbols index, the kit version, the verbs guide, a `help/` page.
18. Each spec states what its design does not check, and a choice that is not derivable is a fork in its open questions with a recommendation the builder can take. Two forks to state at least: `--no-ff` merge against a cherry-pick (recommend `--no-ff`: it keeps the builder's commit and its `Pass:` trailer reachable unchanged, which `pass_commit` walks without `--first-parent`); and whether the merge verb lives in the driver `unattended.sh` or in its own file (recommend its own file, per item 5).

### brief:acceptance

- Unit 1: through the suite's runner, a `tree` call's prompt orders the work into the tree, names the declared write set, carries no `--dispatch` or `--brief` order, and its return names the tree; a call without `tree` is byte-identical to today's; every malformed `tree` or `writes` is refused.
- Unit 2: in a fixture repository, two passes cut from one tip, each committing a disjoint product file and both rewriting one generated output and one gen region, merge back in turn with the generated output re-rendered and the run branch's log showing each pass commit on a merge's second parent; a third pass touching a product file the first touched is aborted with exit 1, naming the file, and the tree is clean at the pre-merge `HEAD`.
- Unit 3: two sibling `--dispatch` calls declaring one generated output are both admitted with the note printed, and two declaring one product file are still refused with today's message.
- Every new arm is observed red, then green, by the main loop at the close.
- The main loop's measurement: two disjoint units built serially through the harness in one tree, against the same two built in parallel through `tree`, cut and merge, on a frozen clone, wall clock per phase.

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

### input:spec

memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-2.md

### task:reuse

lib-unattended.sh resolve_generated_indexes, check_gen_region_only, covers; unattended.sh check_commit_message's generated exemption; push-main.sh run_regen and regen.py --write; unattended-unit.js prebuild and passLegs key shape; lib-attribute.sh add_scratch_worktree.

### card:route

- build: aTwinnedPass
- unit: TOOL-aTwinnedPass-1 · spec memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-1.md
- unit: TOOL-aTwinnedPass-2 · spec memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-2.md
- unit: TOOL-aTwinnedPass-3 · spec memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-3.md
- brief: memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-1-brief.md
[/memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-2-4-spec-writer.md]
