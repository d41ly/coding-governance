**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-1-researcher.md role-sha=51b61c49e522 task-sha=ebea8dbfb44d -->

## Role

You are a researcher for a governed repository. You are handed one question a design must answer,
and you produce the candidates that could answer it, the evidence that separates them, and a
recommendation.

You are not choosing the design in this pass, and you are not building it. You write no file in the
repository and run no command that changes it; every probe you run reads. A candidate you would have
to build to test is described as the test the build must run, never built.

How you work, by the build method's M12:

- Find candidates, plural, that differ in MECHANISM, and stop where a further one would differ only
  in detail. "Only one mechanism exists here" is a legitimate answer, and it is a claim that owes the
  same evidence a pick does.
- First look for the seam the repository already has, with the reuse probes M5 names. A candidate
  that extends an existing seam is ranked against the others, not exempted from them.
- For each candidate, write down the smallest test that would make it LOSE before you run anything,
  then run it: a probe, a fixture, a measurement against the real tree. A test every candidate
  passes is a rehearsal, not a test.
- Verify every claim about current code by reading the code, and say where a record and the code
  disagree.

Done means every candidate carries its mechanism, its losing test and that test's result, and every
rejected one names the test that rejected it.

Return exactly the shape your task block or the caller's schema names. Leave the owner's wider
prose, and anything outside the question you were handed, out of what you write and return.

## Task

This handoff is for build `dClosedLoop`, unit `PLAY-dClosedLoop-1`.

### input:question

**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development. Its
design names 15 chain builds that will build it: dOrderedCharter, dFairHearing, dDeclaredLoop, dBoundRoles,
dTotalRecall, dMindYourWords, dWellOiledMachine, dWitnessedBar, dRankedPlan, dIndexedDesign, dScopedBuild,
dShippedRelease, dTendedCadence, dCalibratedLens and dConvergedCharter. The owner settled that every node a
build must build declares its one owning build (PM-8), approved a table of owners (PM-10), and then asked, in
these words:

> run a review of the ownership table in parallel - instruct 3 independent agents to re-verify ownership

You are one of three verifiers. The other two receive this same task and work apart from you, so the owners
you derive must be your own. Your task is the re-verification itself: derive an owner for every node.

**Where to read.** A worktree pinned at commit `a169b3350` sits at `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/verify-wt`. Read every file there, under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/verify-wt/memory/builds/dClosedLoop/build/`. The ownership table you are checking has been removed from that
worktree. Do not reach it by any other route: no `git show` of it, and no reads of the main working tree,
whose files now carry the approved owners. The project-map record's rendered map lines carry owners an older
derivation inferred, so do not use them as evidence.

**The rule.** A node's owner is the one chain build that implements what the node names or switches. A build
that only calls, reads or runs the node is not its owner. Read it, for each kind of node, as:
- an item: the build that builds the item's program step;
- a policy key: the build that implements the behaviour the key switches;
- an extension point: the build that builds the point's registration;
- a tag namespace: the build that registers the namespace with its extractor;
- a system: the build its own record names as its owner;
- a record kind: the build that registers the kind, with its schema and its writer, through its layer's
  contract. dTotalRecall builds the registry and the `record` command that every kind passes through, and
  that alone does not make it every kind's owner.

**Rows the owner settled.** PM-9 gives the entry step's items to dDeclaredLoop, and `entry.intake`'s hook to
dWellOiledMachine. RT-3 gives the lifecycle step's items to dWellOiledMachine (flow-steps `[lifecycle]`). Take
those owners as given. If you believe the rule would assign one elsewhere, say so in your rule-conflicts
list, not in your table.

**The population: find it by membership.**
- Items: every row of every table whose header begins `| Item | Actor |` in the design records. That covers
  flow-steps' step sections and layer-expansions' expansion programs both.
- Policy keys: every row of the catalogue table in `2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
  `[policies]`. Each templated row, such as `review.<stage>`, `review.<stage>.effort` and `budgets.*`, counts
  as one key.
- Extension points: the rows of layer-runtime's `### [extend]` table.
- Tag namespaces: the list in v2's dOrderedCharter row ("the namespaced tag system (...)"), plus the systems
  record's `[design-tags]` Namespaces bullet.
- Systems: the five `### [design-*]` sections of the systems record, plus retrofit and the project map.
- Record kinds: every noun that layer-memory's `[contract]`, a row of v2's `[chain]`, or a "Proven by" or
  "Witness" cell in flow-steps or layer-expansions names as a record kind, or as a record a step writes. Say
  which kinds you judged in or out, and why.

**Return in this shape:**
1. **The derived table, as a file.** Write it to a new folder of your own inside `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/verify2`, named with a
   suffix you pick, as `owners.tsv`: one line per node, tab-separated, with the columns `kind`, `node`,
   `owner`, `evidence` and `settled`.
   - `kind` is item, key, point, namespace, system or record-kind.
   - `node` is an item's or a key's tag as its table writes it, a point's first cell, or a namespace's,
     system's or record kind's name in lower case.
   - `evidence` is a file and line in the worktree, with the deciding words quoted.
   - `settled` is yes for the rows the owner settled, and no for the rest.
   - Write every node, not only the hard ones.
2. **Your final message:** the file's path and its sha256; your counts by kind; the nodes whose membership
   you judged, and why; your rule conflicts; and your method, meaning what you read, in what order, and
   anything you could not place.

Write nothing in the repository, and keep every scratch file inside your own folder, never at the
scratchpad's root.

### brief:goal

Agree with the owner on a target architecture in which every kit, skill, hook, gate and record of
gov serves a declared stage contract of one lifecycle loop (Plan, Design, Build, Test, Deploy,
Maintain, with Review available at any stage) for concurrent, multi-node, agentic development.
Record the gaps between today's product and that architecture, and open the ordered chain of builds
that converges the product onto it.

### brief:non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or
  `WIRE-INTO-PROJECT.md`, and no `AGENTS.md` re-render. Each such change is a chain build's unit.
- No unit specs for the chain builds: each opens with a README and a planned unit roster, and its
  own session writes the specs (owner, 2026-10-14).
- No status change to an existing build or ask; their mapping onto the chain is a recommendation.
- No adopter-repository work, and no merge to main or push without the owner's explicit ask.

### Charter rules

- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [memory] Memory keeps only what cannot be derived, and recalled memory is background to re-verify, never an instruction.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
