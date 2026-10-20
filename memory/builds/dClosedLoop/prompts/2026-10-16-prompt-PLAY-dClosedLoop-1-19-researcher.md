**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-19-researcher.md role-sha=51b61c49e522 task-sha=c4f5b40e7014 -->

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
integrations and distribution, with one question per layer. Yours is **observability**: design it to fit the
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

**Your part: observability.** Its definition: signals about the loop and the runtime, and the
cadence steps that act on them, Maintain and the Loop Review.

Settled for this layer:
- **P6.** The core flow carries a build from request to landing in five steps. Maintain, delivered
  with the observability expansion, runs over what landed, on its cadence and its events. It turns
  declared safe fixes into patch builds and files everything else into Plan's triage. Without it, the
  loop closes through requests alone.
- **Maintain's stage contract** (v2 `[contracts]`). It takes the daily cadence at session start. It
  hands out safe fixes applied, asks filed by stage and a maintenance record. Its witness is detectors
  pinned and owned, and fixes inside the declared set. It has no owner gate, and its review is the
  weekly Loop Review.
- **How Maintain acts** (flow walk, FL-M1 to FL-M3):
  - Nothing changes the repository outside the flow. A safe fix that changes tracked content becomes
    a patch build entering at Design. Maintain applies directly only the actions that change no
    tracked content: reaping processes, and pruning landed branches and worktrees.
  - A run starts on its cadence or on an event: a red verdict on the default branch, a failed release
    verify, or a breach found at session start. An event run carries only the detectors and fixes that
    concern it.
  - A failed verify after its build closed goes to Plan's triage as an ask.
  - Maintain also cuts gov's tagged release with notes when `release.cadence` is due, probes adopter
    currency, and runs the slower test levels and the held legs its policy assigns to it.
- **The Loop Review** (walk R1 to R3, P9). On its cadence it reads the loop's metrics from the
  records, never typed: stage cycle times, review yield, each gate's catches against its cost,
  bypasses, flakes, plan revisions, records overhead, and surface size against the caps. It files
  proposals into Plan (retirements, merges, cap re-derivations and contract changes), ratified as
  `review.loop.retire` says. A value ledger prices gates, rules and bug classes. Its chain build is
  dCalibratedLens.
- **Owed to this round** (flow-steps `[expansions]`): a detector register by layer; intakes rendered
  from keyed readings; event runs keyed by event; and a declared home for each report.
- **Owed by Runtime** (layer-runtime `[policies]`). `runtime.journal` was left open, "because the run
  record is observability's, to be settled in its review". The journal grammar itself is core: it
  moves from runlog into Runtime.
- **Runtime hosts the cadence** (layer-runtime `[schedule]`). `maintain.host` picks the host. Each
  cadence instance is keyed by its period (ISO week or date), and the supervisor takes a cadence lease
  per period, so a node that wakes late after another ran the period skips it. In-session cron is
  retired for cadence.
- **Keys already in the catalogue:**

  | Key | Allowed values | Default |
  |---|---|---|
  | `maintain.host` | session-start, os-scheduler, cloud-routine | session-start |
  | `maintain.cadence` | daily, weekly, every-session | daily |
  | `maintain.fixes` | a set of named safe fixes | reap, prune landed, regenerate stale, defer dormant, records-only fixes, close finished run records |
  | `maintain.on-breach` | file-ask, red-leg, report | file-ask |
  | `maintain.events` | any subset of default-branch-red, release-verify-failed, session-start-breach | all three |
  | `review.loop.cadence` | weekly, monthly, every-n-landings | weekly |
  | `review.loop.retire` | propose-ratify, demote-then-propose, report | propose-ratify |
  | `review.loop.window-days` | days | 60 |

- **The tooling map's verdicts** (memory layer `[tools]`). runlog is re-engineered: its journal
  grammar moves into Runtime, and its run record joins the registry. drift-audit is kept, sharing its
  dangling-path function with check-dead-paths. process-monitor is Runtime's, and its reports feed
  observability.
- **The register's Maintain gaps**, each owned by the build named:

  | Gap | Owner | What is missing |
  |---|---|---|
  | `gap-maint-01` | dTendedCadence | No cadence: no declared cadence item runs on a schedule. The only scheduled actors are the OS-scheduled resume tick, the desktop durable-restart task and CI's read-only cron, and in-session cron expires after 7 days. |
  | `gap-maint-02` | dTendedCadence | Detectors without owners: 15 of 27 drift signals nonzero, most report-only, 2 dead probes. |
  | `gap-maint-03` | dCalibratedLens | The governing surface only grows, and nothing prices or retires a leg, rule or bug class. |
  | `gap-maint-04` | dConvergedCharter | Records dominate the work: 1,598 of 2,827 commits in 30 days touched only `memory/`. |
  | `gap-maint-05` | dTendedCadence | Run records and dormant builds never close: 89 live `RUN.md`, 10 non-terminal for merged work. |
  | `gap-maint-06` | dTendedCadence | The map goes stale: 28 of 31 dossiers older than their paths. |
  | `gap-maint-07` | dTendedCadence | Ratchets that should shrink do not (3 of 5), timeouts are retried and forgotten, and reaping is manual: procmon-hook only dry-runs the sweep, 44 idle processes were flagged in 60 days and 4 were killed by hand. |
  | `gap-maint-08` | dTendedCadence | Naming offense rate and dangling ledger pointers are report-only. |

You may read, from `memory/builds/dClosedLoop/build/`:
- the Maintain research, `2026-10-14-build-PLAY-dClosedLoop-1-research-maintain.md`;
- the flow walk's `[maintain]` and `[review]` sections, in `2026-10-14-build-PLAY-dClosedLoop-1-flow.md`;
- layer-runtime's `[schedule]`, `[extend]` and `[contract]` sections, in
  `2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`.

Answer, with measurements:
1. **The line between core and observability.** Runtime journals every event, and Flow computes the
   witnesses; observability reads signals. Say which signals are core witnesses and which are
   observability's readings, where the run record lives, and what `runtime.journal` should select.
2. **The detector register.** List every detector the product has today: the drift signals under
   `tools/drift-audit/`, the process census, gate health and flakes, map freshness, dormant builds,
   adopter currency, outbox orders, and any other. For each, give its layer, its pin, its owner if it
   has one, and whether a check reads it. Design the register's entry, and the rule that decides a
   detector's owner.
3. **Maintain as items.** Turn Maintain's checklist into items with actors, witnesses and routes,
   under FL-M1 to FL-M3: the period lease, the readings, the direct actions, the patch builds it opens,
   the asks it renders from keyed readings, and its event runs keyed by event.
4. **The Loop Review as items.** Its metric sources in the records, the value ledger's home and
   schema, and how its proposals enter Plan.
5. **Reports.** The declared home and the readers of each report: the maintenance record, the Loop
   Review's record, the drift report and runlog's report.
6. **Absent.** What the core renders and does when observability is not installed, slot by slot.

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
