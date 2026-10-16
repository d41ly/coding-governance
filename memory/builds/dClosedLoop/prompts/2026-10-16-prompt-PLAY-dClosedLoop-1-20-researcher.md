**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-20-researcher.md role-sha=51b61c49e522 task-sha=bdc59816de51 -->

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
integrations and distribution, with one question per layer. Yours is **integrations**: design it to fit the
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

**Your part: integrations.** Its definition: adapters to outside services: remote CI, notifications,
cloud hosts, trackers, and deploy engines that promote a landed tree through environments.

Settled for this layer:
- **P3.** The local hook is the default and first-built verdict path, because remote CI is not
  available. A peer-node verifier ships as a switchable backend, and remote CI is a designed slot.
  Since 2026-10-14, remote CI has been unavailable to gov, and the local hook is the verdict.
- **Test's contract** (v2 `[contracts]`). Test hands out a runner-written verdict per tree, read by the
  pre-push hook, and its witness is the verdict from the declared backend. Its chain build is
  dWitnessedBar.
- **Deploy holds two processes** (flow walk, FL-DP1 and FL-DP2):
  - the landing, which belongs to the build and closes it under the default `build.closes:
    at-landing`;
  - the release, recorded per SHA, which promotes landings through the declared environments. Under
    the default, a failed verify after its build closed is new work, filed as an ask.
- **Deploy's core items** (flow-steps `[deploy]`), all commands, in order: `deploy.current`,
  `deploy.mandate`, `deploy.parents`, `deploy.land`, `deploy.core` (the post-merge bar on the landed
  SHA), `deploy.record` (the landing record), `deploy.distill`, `deploy.recommend`, `deploy.notify`
  (posts `landed` to the dependents' mailboxes), `deploy.snapshot`, `deploy.release` (deletes the
  build's lease refs and closes its mailbox) and `deploy.close`.
- **Owed to this round** (flow-steps `[expansions]`): promotion through environments, with a verify per
  SHA and `deploy.on-verify-fail`, from integrations.
- **Runtime's adapters** (layer-runtime `[schedule]` and `[extend]`). `cloud-routine` is an
  integrations host adapter, used once a routine has shown a green bar. The os-scheduler and
  requesting-node hosts are the node tick. CI's schedule stays, for read-only verdicts. Notification
  adapters carry an owner request to the owner: the terminal, or a push notification.
- **Keys already in the catalogue:**

  | Key | Allowed values | Default |
  |---|---|---|
  | `verdict` | local-hook, peer-node, remote-ci | local-hook |
  | `run.host` | requesting-node, os-scheduler, cloud-routine | requesting-node |
  | `maintain.host` | session-start, os-scheduler, cloud-routine | session-start |
  | `notify.owner` | turn-micro-formats, park-and-landing, every-transition, park-only | turn-micro-formats |
  | `deploy.runs` | landing-node, adopter-ci, operator | landing-node |
  | `deploy.promotion` | owner-approves-prod, auto-on-green, owner-approves-each | auto-on-green |
  | `deploy.on-verify-fail` | rollback-and-ask, halt-and-alert, roll-forward | roll-forward |
  | `build.closes` | at-landing, after-release-verifies, at-landing-maintain-owns | at-landing |

- **The register's gaps this layer touches**, each owned by the build named. dShippedRelease's
  planned units include the deploy engine, an adapter for one adopter's deploy target, and optional
  emitted CI.

  | Gap | Owner | What is missing |
  |---|---|---|
  | `gap-deploy-01` | dShippedRelease | An adopter's own release, environments, rollout, rollback and post-deploy verification are not addressed; one adopter built all of it outside gov. |
  | `gap-deploy-02` | dShippedRelease | The post-landing verdict is inert: `GATE_POST_MERGE` declared in 0 of 3 trees, `refs/gov/bar-red` absent, CI cannot publish. Its verdict sits in one last-verdict file a later landing overwrites, with no record keyed by the landed SHA. |
  | `gap-deploy-03` | dShippedRelease | No CI job is emitted into adopters; one adopter's six workflows never call the bar. |
  | `gap-deploy-05` | dShippedRelease | Outbox orders are graded by nothing (one adopter holds 16, five of them rollbacks). |

You may read, from `memory/builds/dClosedLoop/build/`:
- the Deploy research, `2026-10-14-build-PLAY-dClosedLoop-1-research-deploy.md`;
- the Test research, `2026-10-14-build-PLAY-dClosedLoop-1-research-test.md`;
- flow-steps' `[deploy]` and `[test]` sections, in `2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`;
- layer-runtime's `[schedule]`, `[extend]` and `[harness]` sections, in
  `2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

Outside that build you may read `memory/builds/aDeployScout/spec/governance-deployer-research.md`.

Answer, with measurements:
1. **One adapter contract, or several.** List the adapter kinds this layer holds: verdict backends,
   host adapters, notification adapters, deploy engines, tracker adapters, and any other. For each,
   name the core extension point it registers at and the section that declares it. Say which have no
   declared point today, such as a verdict backend slot in Test, an environment-promotion point in
   Deploy, or a tracker point in Plan or memory.
2. **Remote CI as a verdict backend.** Measure what `.github/workflows/` runs today and what it can
   publish. Say what a remote verdict must carry to stand as a witness: keyed by the tree's SHA,
   written by a runner, and trusted by key and source.
3. **Deploy engines and the release record.** Design the release as items after the landing: the
   promotion per environment, a verify per SHA, `deploy.on-verify-fail`'s routes, and the release
   record's schema. Say how `deploy.release`, which deletes lease refs, and the release process are
   named apart.
4. **Notifications and trackers.** Measure what reaches the owner today, and how; and whether any
   tracker is used, and for what. Design both adapter kinds, or argue one away.
5. **Grants and secrets.** Every adapter to an outside service needs a credential. Design how an
   adapter declares the grant it needs, where its secret lives, and how a check proves the secret is
   not in files, memory or chat.
6. **Absent.** The core's fallback for each adapter kind, slot by slot.

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
