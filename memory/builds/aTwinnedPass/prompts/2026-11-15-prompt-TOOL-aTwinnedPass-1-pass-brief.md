# Pass brief — aTwinnedPass: TOOL-aTwinnedPass-1's build pass, in its own worktree

**Serves:** research TOOL-aTwinnedPass-1

## The prompt

> Make the unattended build harness able to build two or more units of one build at the same time, as gov work: `/session-kickoff` first, a build of its own with a spec, a gov-builder for the code, landing on main through `bash tools/push-main.sh` on a green bar only under the charter's [land] rule.

> Design target: each parallel pass builds in its own worktree on its own branch cut from the run's tip; product files are checked disjoint by `--dispatch` as now, while generated files are left to the main loop, which merges each pass back (`--no-ff`, or a cherry-pick, your call in the spec) and regenerates the shared indexes once.

> Done looks like: a spec with its forks, the change built and its arms seen red then green, a measured before and after of two disjoint units built serially versus in parallel on a frozen clone, and the work landed on main or left on its branch with a line saying what is left.

The task came from the session that started this one, on the owner's request. It is quoted in part; the passages above are the ones this build serves.

## The brief

### Goal
A main loop can build two or more disjoint units of one build at once: each pass builds and commits in its own worktree on its own branch cut from the run's tip, and the main loop merges each back into the run's branch `--no-ff`, re-rendering the generated outputs, so neither pass stages into the other's commit and neither is refused for a generated output both rewrite.

### Items
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

### Acceptance
- Unit 1: through the suite's runner, a `tree` call's prompt orders the work into the tree, names the declared write set, carries no `--dispatch` or `--brief` order, and its return names the tree; a call without `tree` is byte-identical to today's; every malformed `tree` or `writes` is refused.
- Unit 2: in a fixture repository, two passes cut from one tip, each committing a disjoint product file and both rewriting one generated output and one gen region, merge back in turn with the generated output re-rendered and the run branch's log showing each pass commit on a merge's second parent; a third pass touching a product file the first touched is aborted with exit 1, naming the file, and the tree is clean at the pre-merge `HEAD`.
- Unit 3: two sibling `--dispatch` calls declaring one generated output are both admitted with the note printed, and two declaring one product file are still refused with today's message.
- Every new arm is observed red, then green, by the main loop at the close.
- The main loop's measurement: two disjoint units built serially through the harness in one tree, against the same two built in parallel through `tree`, cut and merge, on a frozen clone, wall clock per phase.

### Gates
The new arms, run directly by the main loop at the close. `check-arms` over the driver suite and the unit harness's suite. The lexicon and codebase-map legs the change owes. The merge bar once at the close, without the self-test suites.

### Non-goals
- ANY READ, WRITE, SHELL COMMAND OR COMMIT OUTSIDE YOUR SESSION'S OWN WORKTREE. You start in a fresh worktree the runtime cut for this pass, which may sit on another commit. Before any other command, run `git reset --hard branch/dazzling-jackson-b895c0` in it, so the tree starts at the commit this pass was dispatched from, and confirm `git log --oneline -1` names this unit's builder handoff commit. Build and commit there, on the worktree's own branch, and name in your summary that branch (`git branch --show-current`, or the commit when it prints nothing), the worktree's path (`git rev-parse --show-toplevel`), and the commit `git log --oneline -1` named before the reset. `TOOL-aTwinnedPass-2` is built after this unit merges back. The main loop merges your branch back. Never touch another worktree.
- The spec of any unit but `TOOL-aTwinnedPass-1`, and the product files the other unit's spec names.
- `pass_commit`, `read_attribution_tokens`, `check_pass_open` and `read_open_passes`: the live run's branch rewrote them, and any change there conflicts when it merges main.
- `memory/builds/dDeclaredLoop/`, its run's worktree, its branch and its run-state file.
- A change to the build harness `unattended-build.js`, to the unattended Skill's loop, or to how a main loop picks which units go together: the build order and M6 already say which may.
- Resolving a conflict on any path that is neither an effective generated output nor a gen-region-only change.
- A cap on how many passes run at once: that is the review protocol's fan-out bound, unchanged.
- ANY SELF-TEST SUITE OR BAR INSIDE A BUILD PASS, A SLICED SUITE INCLUDED. A pass runs only direct checks: `bash -n`, `node --check`, `check-arms`, the lexicon, the changed code invoked over a hand-built fixture, the spec-token checker, and `gen_map.py --write`. New arms are written and checked with `bash -n`; the main loop observes each red and then green at the close.
- A pass commit without its acceptance ledger: the pass commit carries `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-1-1-acceptance-ledger.md`, one `**Evidences:** TOOL-aTwinnedPass-1` block naming each criterion with the backticked token the criterion itself spells, and the arms' red-then-green named as owed to the main loop.
- An edit after the commit that sets a spec CLOSED: every edit lands first, and the status flip is the last change of the pass.

### Limitations
- A spec's acceptance criteria cite no path the unit has not built yet: cite a new file by its basename in section 6.
- Every spec line stating a figure with a unit carries the word PINNED or a commit sha on that line.
- The merge verb never passes `--no-verify` and never edits a hook's verdict: a refused merge commit is the main loop's to read.

### Reuse
- `tools/unattended/lib-unattended.sh#resolve_generated_indexes`, `#check_gen_region_only`, `#covers` and `#overlaps`: the generated set and the gen-region predicate the merge verb and condition 1 read, never copied.
- `tools/unattended/unattended.sh#check_commit_message` already exempts an effective generated output from a pass's declaration; condition 1 asks the same question the same way.
- `tools/push-main.sh#run_regen` and `tools/run-gates/regen.py --write`: the one regeneration, found the way the lander finds it.
- `tools/workflows/unattended-unit.js`'s `prebuild` and `passLegs` keys: the shape of an optional, single-line, backtick-free key and its byte-identical default.
- `tools/run-gates/lib-attribute.sh#add_scratch_worktree` and `#remove_scratch_worktree`: the reuse probe's only worktree seam; read it for its MSYS handling before writing the cut and the removal.
- Records: `TOOL-dDerivedDocket-55` and `-57` (the two asks), `TOOL-cBriefedPilot-15` R5 (one worktree per concurrent pass is a viable checkout shape), `TOOL-aGraftedHelix-27` (`resolve_generated_indexes` under a hook's `GIT_DIR`).
- Recall terms used: `parallel-when-disjoint dispatch worktree pass merge generated index regen check 23 sibling`.

## Drawn from the session

> The owner runs a 99-unit unattended build, dDeclaredLoop, on node a (Windows, Git-Bash, slow process spawns: about 0.75 s per git spawn). Units are built one at a time by the unit harness `tools/workflows/unattended-unit.js`, each taking 15 to 50 minutes, plus 10 to 25 minutes of spec re-grounding and commit hooks.
— the session that started this one, its task message, 2026-11-15 (PINNED)

> 2026-11-14T23:06:16Z dispatch · item b5fa5e1e TOOL-dDeclaredLoop-10 · reason tools/loop/loop_table.py tools/loop/loop_transition.py tools/loop/README.md help/loop.md memory/map/generated/symbols.json memory/map/generated/MAP.md memory/map/generated/CARDS.md memory/map/generated/inventories.json
— agent, read from the live run's run-state file at `b357a7e82`, 2026-11-15: a pass declaring generated outputs by hand, which condition 1 then compares against every sibling

## Owner confirmation

Asked: not asked. The session that started this one handed over the owner's request as the task above, which asks for exactly this build.
Answer: the task's own words, quoted under The prompt.
