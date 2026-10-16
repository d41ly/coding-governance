**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-21-researcher.md role-sha=51b61c49e522 task-sha=66c85df64873 -->

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

**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development.
The owner reviews the design layer by layer. The five core layers, instruction, flow, roles, memory and
runtime, are designed, reviewed and folded. This pass opens the three expansion layers, observability,
integrations and distribution, with one question per layer. Yours is **distribution**: design it to fit the
architecture handed below. Say what it owns, where it attaches to the core, what it adds to the flow,
and what the core does when it is absent.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **The layers** (architecture v2 `[layers]`). A layer is a capability named by a tag, and a kit
  implements layers and declares which. The core alone carries one build from request to landing,
  and an expansion is never needed for that.

  | Layer | Kind | What it is |
  |---|---|---|
  | `instruction` | core | everything an agent is told, levelled 0 to 7 and tagged by scope |
  | `flow` | core | a build's lifecycle: Plan, Design, Build, Test and Deploy as programs of items, review as breakpoints, with the verdict engine and the lander |
  | `roles` | core | the bound workers, and the driver |
  | `memory` | core | the trail, what happened in a build: records, transitions, witnesses, the card's truth; and the library, what generalizes beyond one: major decisions, reuse entries, bug classes, research. Its optional components, the map, recall and the lexicon, are what agents consult to decide |
  | `runtime` | core | what executes the cycle: the supervisor and its checklist engine, act sessions and the spawn harness, the `next` verb and the owner's controls, the hooks, isolation, process supervision |
  | `observability` | expansion | signals about the loop and the runtime, and the cadence steps that act on them: Maintain and the Loop Review |
  | `integrations` | expansion | adapters to outside services: remote CI, notifications, cloud hosts, trackers, and deploy engines that promote a landed tree through environments |
  | `distribution` | expansion | the product's delivery: govkit, the adopt scripts, overlays, the install of the render targets Runtime's harness adapters define, currency |

- **P28.** The core never depends on an expansion. An expansion attaches only at an extension point a
  core layer declares. Every layer, core or expansion, fills one layer contract:
  - its tag and definition;
  - its instruction units;
  - its engine kits;
  - its record kinds;
  - the extension points it declares, and those it uses;
  - its policies and its gates.
- **The optional slot.** A work-order field, or any part of a core render, that an expansion fills is
  an optional slot. It renders filled, searched with nothing found, or not installed with the core's
  fallback named, never empty. `policy.on-missing-expansion` (`refuse` or `fallback-reported`, default
  `refuse`) governs a preset value whose expansion is absent.
- **Items, witnesses, policies and records.**
  - Every action that changes state belongs to an item, tagged `<step>.<name>`. An item has one actor
    (a command, a role, a hook, the owner or the executor), what it needs, what it does, its witness
    and its routes (P24).
  - A witness is computed from committed history, a hook-written record or a verifier's verdict, never
    from state an agent typed (P2).
  - Every behaviour is a policy key. Its default is the owner's answer, and its allowed values are the
    options offered (P10). Structural choices are decisions, not keys.
  - Every record kind is declared once in the memory contract (tag, layer, home, id rule, schema,
    writer, readers, lifecycle, check), and written through one door, the `record` command (P30).
- **Runtime's extension points** (layer-runtime `[extend]`). Runtime declares nine and uses none.
  Integrations fill the host and notification adapters. Observability and memory's optional
  components register packs and read the journal. A key that selects an extension takes registered
  names, validated against the registry.

  | Extension point | What registers there | Examples |
  |---|---|---|
  | actor kinds | a kind of actor an item can name | role, command, hook, executor, owner |
  | command adapters | a command, with its witness contract and its idempotence or reconcile probe | the bar, the lander, `record`, the instruction command |
  | spawn backends | a way to start a role agent | in-session Workflow, headless per agent, another harness's spawner |
  | role harnesses | a Workflow script, with its declared spawn sites and fan | the role cycle, the Tier-2 review |
  | hook packs | a fragment, with its owner, class, failure mode, budget and key | the spawn guard, act binding, the lexicon's commit check |
  | harness adapters | how a harness loads instructions, spawns, hooks and compacts, with its capability table | Claude Code, Codex |
  | host adapters | where the supervisor and its sessions run | the node tick, a cloud host |
  | notification adapters | how an owner request reaches the owner | the terminal, a push notification |
  | journal readers | what reads the journal | runlog, observability's store |

- **The chain.** Every gap in the register is owned by exactly one chain build, and the expansions'
  work lands in those builds.

**Your part: distribution.** Its definition: the product's delivery: govkit, the adopt scripts,
overlays, the install of the render targets Runtime's harness adapters define, and currency.

Settled for this layer:
- **P8.** Every adopter is an adopter, gov included. The charter is the shared foundation, and each
  repository's own rules render from its own overlay as a separate project block.
- **Releases and currency** (flow walk, FL-DP2). Gov's kits reach adopters as tagged releases. Kits
  still mint a version at each landing, and Maintain's run cuts a tagged release with notes when
  `release.cadence` is due. Adopters' currency is measured in releases behind.
- **Deploy's contract** (v2 `[contracts]`) hands out kit release notes and adopter currency, among
  others, and its witnesses include the currency probe. Its chain build is dShippedRelease.
- **Owed to this round** (flow-steps `[expansions]`): kit versions and release notes, from
  distribution.
- **Runtime's harness adapters** (layer-runtime `[harness]` and `[extend]`) say how a harness loads
  instructions, spawns, hooks and compacts, each with a measured capability table: Claude Code and
  Codex. Distribution installs their render targets.
- **The instruction layer** (P13). Every instruction unit has a level, from 0 (the charter) to 7
  (records), and scope tags. Playbook renders the charter, and agent-instructions wires each
  harness's instruction files. Both are re-engineered into tag-sliced views.
- **Keys already in the catalogue:**

  | Key | Allowed values | Default |
  |---|---|---|
  | `release.cadence` | every-landing, daily, weekly, owner-cut | weekly |
  | `deploy.currency` | pull-and-watch, push-branches, pull-only | pull-and-watch |
  | `runtime.harnesses` | a set of named harness adapters | claude-code |

- **The tooling map's verdicts** (memory layer `[tools]`). govkit is re-engineered, with check-wiring
  and check-placeholders folded in, into one wiring verdict and one version check. lib's 73 inline
  `resolve_python` copies are to be generated, not hand-kept. The remaining checks regroup into
  Instruction and Distribution packs.
- **The register's gaps this layer touches**, each owned by the build named. dShippedRelease's
  planned units include kit release notes, the fleet register and currency watch, and the kit factory
  with its conformance gate.

  | Gap | Owner | What is missing |
  |---|---|---|
  | `gap-deploy-04` | dShippedRelease | Adopter currency is unwatched: receipts 990 commits behind after six days; `update` is pull-only; no fleet register. |
  | `gap-deploy-06` | dShippedRelease | Landing and release have no review, no role and no changelog. |
  | `gap-deploy-07` | dWellOiledMachine | A killed hook on Windows still lands an ungated push; hooks-path drift is only a note; the lander kit is unversioned with an undeclared dependency. |
  | `gap-deploy-08` | dShippedRelease | The runbook is 163 KB of narrative under an existence-only parity check; `[isolate]` ports and the `up —` line are stated only. |
  | `gap-tool-02` | dShippedRelease | Wiring is judged three ways (check-wiring, eleven `adopt-*.sh --check` legs, `govkit check`) and version lockstep four ways (check-kit-versions, check-placeholders, `govkit epoch`, check-verdict-epoch). |
  | `gap-tool-04` | dShippedRelease | 73 files carry hand-kept inline copies of `resolve_python`, though `tools/lib/resolve-python.sh` is the one resolver; the copy-install could generate them. |

You may read, from `memory/builds/dClosedLoop/build/`:
- the Deploy research, `2026-10-14-build-PLAY-dClosedLoop-1-research-deploy.md`;
- flow-steps' `[deploy]` section, in `2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`;
- layer-instruction's `[layers]` and `[recommendations]` sections, in
  `2026-10-15-build-PLAY-dClosedLoop-1-layer-instruction.md`;
- layer-runtime's `[harness]` and `[extend]` sections, in
  `2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

Outside that build you may read `memory/builds/aDeployScout/spec/governance-deployer-research.md`.

Answer, with measurements:
1. **What is core, and what is distribution.** The core must carry a build to landing in an adopter
   alone, yet something must put the core there. Draw the line: what a minimal install of the core
   is, and what distribution adds.
2. **The kit as the unit of delivery.** Measure today's `kit.toml` descriptors, version minting and
   lockstep, and govkit's verbs. Design the descriptor fields P28 needs (layers, extension points,
   record kinds, policies, gates), each kit's version and release notes, and the kit factory's
   conformance gate.
3. **Overlays and render targets.** Measure how the charter and each harness's instruction files are
   rendered and installed in an adopter today. Design the install of the render targets Runtime's
   harness adapters define, and the overlay that keeps each repository's own rules separate.
4. **Currency and the fleet register.** Measure how gov knows an adopter's version today. Design the
   fleet register, the currency probe as a witness, and each `deploy.currency` mode.
5. **One wiring verdict and one version check.** Measure today's wiring and version checks, and
   design their consolidation.
6. **Absent.** What the core does in a repository with no distribution installed, gov itself
   included.

**How to work:**
- Read only. Write no file, and run no generator in write mode, no selftest and no bar.
- From `memory/builds/dClosedLoop/`, read only the records and sections your part names. Measure the
  rest in the tree itself: `tools/`, `skills/`, `.claude/`, `.github/`, and `memory/` outside that
  build.
- A record is evidence. Verify against the code any claim your pick depends on, and say where a record
  and the code disagree.
- Cite file:line for every claim about code or records. Show each measuring command with its output.
- Return at most 3,000 words, in the eight sections below. Prefer tables.

**Return these eight sections:**
1. **Verdict:** the layer, in at most 120 words.
2. **Today:** each part of today's product that serves this layer: what it does, its measured use,
   and file:line.
3. **Attach points:** each core extension point, item or optional slot the layer attaches to, the
   section that declares it, and what the core does without the layer. Name any attach point the
   layer needs that no core layer declares.
4. **Candidates:** two to four designs that differ in mechanism. For each, give the mechanism, the
   smallest test that would make it lose, and that test's result with its command and output.
5. **The contract, filled:** the six contract fields for your pick, as a table.
6. **Items and policies:** the items the layer adds or fills (tag, actor, does, witness, routes), and
   its policy keys (key, allowed values, default, why).
7. **Gaps:** the register's gaps your pick closes, by id, and any new gap it exposes, with its
   evidence.
8. **Forks:** the decisions only the owner can make, each with its options and your recommendation.

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
