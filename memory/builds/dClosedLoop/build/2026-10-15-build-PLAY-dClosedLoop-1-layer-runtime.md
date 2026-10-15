# Layer review: the runtime layer

**Serves:** research PLAY-dClosedLoop-1

The fifth round of the owner's layer-by-layer review: the runtime layer. Layers round one made Runtime
a core layer: "Instruction says, Runtime enforces, Flow witnesses, Memory proves." v2's `[owed]` gives
it a chain build of its own, once this review settles what that build holds.

Four researchers measure the runtime in parallel: dispatches 30 to 33. Their returns are saved
verbatim beside this record, and the design is written here once they return.

## [words] The owner's words, 2026-10-15

> Let's review the Runtime layer next

The owner gave no framing this time, so the scope below is the main loop's. It is drawn from the
layer model and from what earlier rounds left owed.

## [settled] What the design already fixes

- **The layer** (layers round one) is what executes the cycle:
  - the executor and its checklist engine;
  - the `next` CLI;
  - the always-spawn harness;
  - the hooks that enforce at the tool boundary;
  - isolation;
  - process supervision.

  The core never depends on an expansion. Observability reads the runtime's signals, integrations
  supply hosts (`run.host`), and distribution installs it.
- **Settled elsewhere, and executed by Runtime:**

  | Mechanism | Settled in | Owned by |
  |---|---|---|
  | the loop definition, its items, and `next` deriving position from witnessed state | flow, P24 | dDeclaredLoop |
  | leases on the shared remote (acquire, renew, release, take over by compare-and-swap), the mailbox ref per build, fleet identity, offline acquisition, dependency coordination | coordination record | dDeclaredLoop, with `gap-conc-01`, `gap-conc-02` and `gap-flow-06` |
  | the item cycle: work order, spawn guard, schema-forced returns, retries (`roles.retries`), no-spawn fallback (`roles.no-spawn`), write gates by allowance, return validation at subagent stop | roles round, flow-roles `[cycle]` | dBoundRoles |
  | P29's keyed handed facts, the answered-call hook, separation of duties at spawn | layers round three | dBoundRoles |
  | the card as a ref per build, the per-worktree card file, re-rendered by every session-start hook | orientation round | dOrderedCharter, dDeclaredLoop |
  | context on full (`context.on-full`, compact with the card), `context.threshold`, `card.pointers`, `resume.context`, `resume.partial` | orientation round, compaction CX-1 to CX-3 | dDeclaredLoop |
  | the lander (`push-main.sh`) and the turnstile landing queue | flow-roles FR-6, deferred to the lower-level design | Deploy |
- **Owed with no owner** (v2 `[owed]`):
  - the executor and its checklist engine;
  - the harness that can always spawn the subagents an item needs (RL-8: "a built-in harness should
    be used that can ALWAYS spawn subagents as necessary");
  - the compaction checks: a pre-compaction flush, a subagent's brief re-injected after its own
    compaction, the re-attachment cap, the executor holding no model context, and the cost of
    compacting against starting fresh.
- **Gaps already registered that a Runtime build would naturally own:**
  - `gap-tool-03`: the hook surface spans five kits. It sits with dDeclaredLoop until Runtime gets its
    build.
  - `gap-conc-03`: `[isolate]` has no mechanism.
  - `gap-orient-12`: a resume delivered no card.
  - `gap-orient-14`: compaction is ungoverned.
  - `gap-deploy-07`: a killed hook on Windows still lands an ungated push.
  - `gap-maint-01`: no cadence, since nothing runs on a schedule.

## [scope] What this round reviews

1. **The executor and `next`:** what drives a build today, what is decided by code and what by a
   model, whether position is deterministic, and how runs end.
2. **The spawn harness:** every way an agent is spawned, how spawns and returns fail, what the
   platform offers for an always-spawn guarantee, and the fan-out bound.
3. **Hooks, isolation and supervision:** the enforcement surface, its failure modes and bypasses;
   worktrees, ports and databases; process supervision and stale claims.
4. **Sessions, context, scheduling, harnesses and nodes:** the session lifecycle, the owed compaction
   checks, what can run on a schedule, which agent harnesses gov runs under, and what differs per node.

**Boundaries:**
- Runtime executes and enforces. It declares nothing a step or a role owns.
- Flow declares the items and their order.
- Roles define the actors.
- Memory holds the records.
- Instruction states the rules Runtime enforces.

## [research] Dispatched, 2026-10-15

| # | Part | Handoff |
|---|---|---|
| 30 | the executor and `next` | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-11-researcher.md` |
| 31 | the spawn harness | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-12-researcher.md` |
| 32 | hooks, isolation and supervision | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-13-researcher.md` |
| 33 | sessions, context, scheduling, harnesses and nodes | `prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-14-researcher.md` |

### Returned, 2026-10-15

| # | Part | Return | Wall | Out |
|---|---|---|---|---|
| 30 | the executor and `next` | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-executor.md` | 7m21s | 30.8k |
| 31 | the spawn harness | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-spawn.md` | 11m10s | 41.5k |
| 32 | hooks, isolation and supervision | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-hooks.md` | 9m00s | 30.1k |
| 33 | sessions, context, scheduling, harnesses and nodes | `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-sessions.md` | 8m02s | 33.7k |

Their probe scripts are kept in `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-instruments.md`.
One probe was lost: two researchers wrote a `tx.py` into the shared scratchpad, and the second
overwrote the first.

**The owner's words when the round reopened, 2026-10-15:**

> Runtime framing and its architecture falls entirely to you as a technical mechanism that makes the
> rest of the architecture revolve holistically. Based on my other layer framing design and outline a
> flexible, extensible mechanism. Once we've reviewed the layer, let's run two rounds on medium effort
> tier2 reviews of it and compare results to spot any gaps.

## [current] What the runtime is and does today, measured 2026-10-15

**Deciding and acting** (dispatch 30):
- **Who decides.** A model session decides when to call each of the unattended kit's 30 verbs, and with
  what arguments. Code only checks each transition after the session asks for it.
- **How it goes:**
  - unattended sessions made a median of 44 main-session calls per unit, 75% of them Bash;
  - after a compaction, 19 of 20 sessions resumed from the summary instead of re-reading state;
  - the driver refused 47 malformed or out-of-order transitions;
  - one session improvised 17 inline workflows, and another more than 25 ad-hoc scripts.
- **Position is computed three ways, and they disagree:**
  - `--plan` grades the run's pinned base or HEAD;
  - `--status` names the first open README row;
  - run phases contradict spec position: a LANDED run still shows a READY unit.

  The attended path has no position answer without `.unattended.conf`. The harnesses hand position
  back as prose (`nextAction`).
- **Where determinism already holds:** `--plan` is byte-stable across runs, at about 1 s a read. That
  ladder is the seed of `next`.
- **The constraint that shapes everything:** the Workflow runtime has no shell
  (`check-workflow-syntax.js:41`), so a harness pays a model call just to run a CLI verb.
- **How 98 runs ended:**

  | Outcome | Runs |
  |---|---|
  | landed | 75 |
  | aborted | 13 |
  | parked | 8 |
  | stalled at BUILDING with all work terminal | 2 |

**Spawning** (dispatch 31):
- **Four spawn paths:**
  - direct Agent calls, guarded by `task-sha` (not `role-sha`, as an earlier record said), with a
    budget of 5 that resets on every notification;
  - Workflow `agent()` calls, which no hook sees;
  - nested `workflow()` calls;
  - one headless resumer that has never fired on this node.
- **Losses in 60 days:**
  - 4 background agents died with their parent process;
  - session or weekly limits killed 57 agents in 16 runs, and the whole fan in 10 of them;
  - 7 of 12 runs where every agent errored still report `completed`;
  - `unattended-unit` turns a null into `committed:false` with no reason;
  - 0 compactions happened inside an agent, in 2,708 agent transcripts.
- **The platform:**
  - Workflow replay needs the same session, or `--resume`;
  - `claude -p` offers `--output-format json`, `--json-schema`, `--session-id` and `--max-turns`;
  - SubagentStop hands over `last_assistant_message`, and exit 2 holds the agent;
  - 20 concurrent subagents per session; 16 concurrent agents and 1,000 per Workflow run.
- **The resumer skips permissions:** `tools/unattended/resume-tick.sh:385` launches `claude -p
  --resume <id> --dangerously-skip-permissions --max-turns <n>`.

**Enforcement, isolation and supervision** (dispatch 32):
- **The hooks:** 13 entries from 6 owners, wired two ways (12 fragments and one hard-coded arm).
  Nothing sets `onFailure`, so every enforcement hook fails open.
- **The fail-open burst.** On 2026-10-14, resource exhaustion crashed the guards 31 times, and every
  failure admitted the call.
- **The fail-closed switch** (`onFailure: "block"`) needs CLI 2.1.295; this node's PATH CLI is 2.1.292.
  It has no effect on Stop or SubagentStop.
- **The git hooks:**
  - `pre-commit`, `commit-msg` and `pre-rebase` trap no signal, so a killed hook reads as success;
  - `core.hooksPath` is absolute, so every worktree runs the primary tree's hooks.
- **No parallel units.** Units share one worktree: two passes committing on one index failed, so the
  harness ratified "parallelism route: none".
- **Leftovers:**
  - 13 worktrees, 8 of them merged orphans;
  - 497 temp directories older than 7 days;
  - no port or database allocator.
- **Supervision reports and never reaps.** 44 idle processes were flagged in 60 days and 4 killed by
  hand. Claims never expire, a `held` claim is immortal, and terminal refs are never pruned.

**Sessions, context, scheduling, harnesses and nodes** (dispatch 33):
- **The first turn's input tokens, by how the session started:**

  | Start | Median |
  |---|---|
  | fresh session | 84k |
  | after a resume | 503k, mostly cache creation |
  | after a compaction | 101k |
  | a subagent | 13k |
- **Compaction:**
  - a compaction reads about 970k tokens and takes about 117 s;
  - no session under 1,000 turns compacted (0 of 48);
  - no subagent has ever compacted.
- **Card delivery:**
  - startup and compact deliver the card every time;
  - resume missed it 7 of 14 times since 2026-09-15, this session's four resumes among them;
  - no matcher covers the `fork` source;
  - PreCompact, PostCompact and SessionEnd are unwired.
- **The compaction checks owed since CX-3:**
  - `# Compact instructions` in the instruction file are honoured, and gov has none;
  - PreCompact exists and can run a command, but cannot inject;
  - after a compaction, up to 5 recently read files return, each under about 5,000 tokens;
  - root `CLAUDE.md` returns, and path-scoped rules do not;
  - a subagent re-receives only its SubagentStart context.
- **Scheduling:** in-session cron is session-scoped and expires after 7 days. Desktop scheduled tasks
  survive restarts, and CI's schedule is read-only.
- **Harnesses:** Codex now ships PreToolUse, SubagentStart, SubagentStop, PreCompact and SessionEnd
  hooks, and gov wires none of them.
- **Node d:**
  - its clock runs 8 to 13 s slow;
  - its git `autocrlf` differs from CI's;
  - a process start costs about 12 ms;
  - the registry records none of this.

## [framing] Runtime, framed from the owner's other layers

The owner handed Runtime's framing to the main loop. The owner's framings of the other layers repeat
six demands, and Runtime is built to satisfy each of them for every layer at once:

| What the owner asked of every other layer | What Runtime must therefore be |
|---|---|
| Declared once, rendered everywhere: instructions from a manifest, records from templates, roles from one definition | an engine with no layer knowledge of its own, which reads the declarations and executes them |
| Deterministic, enforced mechanically "to the fullest extent possible" (the flow) | deciding done by a program, never by a model's judgment |
| Clear roles, each doing only its job, trusting what it is handed (roles, P29) | the one place that spawns a role, hands it its work order, and validates what comes back |
| Precise load and no read-path inflation (instruction, memory) | the one place that assembles what each session and agent loads |
| Defaults by mechanism, not by agent discretion (the lexicon) | enforcement at every boundary, failing closed, with no hand-held exception path |
| Every behaviour owner-switchable, every layer extendable by contract | every runtime behaviour a policy key, and every runtime part an adapter or a pack |

**In one line: the other layers declare; Runtime decides from what they declared, acts through
mechanisms it supervises, enforces at every boundary, and records that it did.**

## [design] The mechanism

```text
 declarations (read-only): instruction units · loop (items, deps, witnesses) · role registry ·
 record kinds · policy file · hook packs · gate packs · adapters · cadence items
                                     │ read on every tick
                                     ▼
 ┌─────────────── DECIDE ───────────────┐      owner and attended sessions use the same
 │ next: a pure function of declaration,│◄──── client verbs: next, run, why, ask, answer,
 │ witnesses and policy                 │      pause, resume, withdraw
 └───────────────────┬──────────────────┘
                     │ names exactly one act per item
                     ▼
 ┌────────────── SUPERVISE (a process, no model) ──────────────┐
 │ holds the run lease · runs command items itself ·            │──► journal (every event)
 │ launches and relaunches driver sessions · counts agents in   │
 │ flight · allocates workspaces · reaps · expires · schedules   │
 └──────────┬───────────────────────────────┬──────────────────┘
            │ command items                  │ role and owner items
            ▼                                ▼
   command adapters              ┌──────── ACT (a thin session) ────────┐
   (the bar, the lander,         │ a headless driver session that runs   │
    record, the instruction      │ exactly the act next named, through   │
    command)                     │ the role harness (Workflow agent()    │
            │                    │ with schemas); returns persisted by   │
            │                    │ the subagent-stop hook                │
            │                    └──────────────────┬───────────────────┘
            └────────────── witnesses (memory) ◄────┘
 every tool call, write, spawn, return, stop, commit and push passes ONE enforcement surface:
 a dispatcher per event, hook packs from every layer, failing closed, with a witness behind
 every act that cannot fail closed
```

### [decide] `next`: deciding is a program

- **Owners.** The loop kit, which is Flow's (dDeclaredLoop), owns the position function: what
  position means. Runtime owns asking it and acting on the answer: the `next` CLI and everything
  below it. This settles the layer model's two placements of `next`.
- **One derivation.** `next` is a pure function of the loop declaration, the build's witnesses (records,
  refs, verdicts, leases, run state, review rounds, holds) and the effective policy. It replaces
  today's three derivations: `--plan`, `--status` and the run phase. The same tree is graded in every
  mode, and the pinned base is an explicit input. `--plan`'s byte-stable ladder
  (`unattended.sh:5745-5783`) is its seed.
- **It names exactly one act per frontier item:**
  - the item;
  - its actor kind;
  - its work order's path and `task-sha`;
  - the outcome table it routes on.

  A harness never hands position back as prose again: it re-reads `next`.
- **Client verbs, for the owner and attended sessions alike:**
  - `next`;
  - `run <item|step|build>`;
  - `why <item>`;
  - `ask` and `answer`;
  - `pause`, `resume` and `withdraw`, the controls `gap-flow-10` found missing.

### [supervise] The supervisor: a process, outside any session

- **Where it runs.** One supervisor runs per node, under the build's run lease. It holds no model
  context, which answers the owed question by construction.
- **Each tick:**
  - it asks `next`;
  - it runs command items itself, through their command adapters (the bar, the lander, `record`, the
    instruction command), and writes the witnesses they declare;
  - it hands each role or owner item to a driver session;
  - it records transitions.
- **Driver sessions are launched headless** (`claude -p`) with:
  - `--output-format json` and `--json-schema` set to the item's return schema;
  - `--session-id` and `--max-turns`;
  - an explicit permission allowlist.

  **No session the runtime launches skips permissions.** The `--dangerously-skip-permissions` launch at
  `resume-tick.sh:385` is retired.
- **Relaunch.** A driver session that dies, hits a session limit, or reaches `context.threshold` is
  relaunched fresh, never resumed. A fresh start costs 84k input tokens; a resume costs 503k, mostly
  cache creation. The new session asks `next`, so it loses nothing that was witnessed.
- **Agents in flight are counted under the lease** (`runtime.fanout`), across every Workflow call and
  every headless launch. Today's per-burst budget resets on each notification and sees neither.
- **The supervisor also:**
  - allocates and reclaims workspaces (`[isolate]`);
  - reaps orphans and stalls;
  - expires leases past `leases.expiry-hours` and prunes terminal claim refs;
  - names holders by fleet tag;
  - wakes cadence items (`[schedule]`);
  - journals every event to runlog.
- **The supervisor's own death** loses only the tick in flight. A take-over on any node reads the same
  witnesses.

### [act] The driver session: acting is thin and bound

- **A driver is a session for one act.** It receives one act from `next` and performs exactly that
  act:
  - for a role item, it calls the role harness, which spawns the role agent through the Workflow
    runtime's `agent()` with the item's schema;
  - for an owner item, it raises the request through the mailbox and the notification adapter, or
    resolves it as `run.on-owner-question` says.
- **An act-binding rule** in the enforcement surface refuses any spawn, Workflow call or transition
  that `next` did not name for this driver. An improvised workflow is refused, not merely discouraged.
- **Lifetime.** A driver lives one build by default and is relaunched fresh. It can be one per item
  (`runtime.driver-lifetime`). Its context stays thin, since a few calls per act fit hundreds of acts
  below the 1,000-turn compaction distance.
- **Attended sessions are drivers too.** The owner's session runs acts from `next` and answers owner
  items inline. Its context follows the owner's `context.on-full`.

### [spawn] The spawn harness: an item always gets its agent

- **Role agents spawn as subagents through the Workflow harness.** Hooks then see them (SubagentStart
  and SubagentStop carry `agent_id` and `agent_type`), schemas are forced, and a run replays from its
  journal (`resumeFromRunId`). This is RL-8's harness that "already exists", improved.
- **Returns are persisted and validated by a SubagentStop hook**, not by the agent's own writes:
  - it writes `last_assistant_message`, keyed by `agent_id`, under the run's area;
  - it checks the return against the item's schema;
  - exit 2 holds an agent whose return fails.

  Role agents stay write-less, and the guard's state stays apart from what it guards. If SubagentStop
  does not fire for Workflow sidechain agents, the fallback is the run journal, plus the driver's
  session-level `--json-schema`.
- **One deferral factory:** a null `agent()` result becomes `deferred-platform`, never
  `committed:false`. It is shared by every harness, the unit harness included.
- **"Always" holds by construction.** The supervisor launches sessions itself, so no item depends on a
  parent's ability to spawn. A session limit defers the item, the supervisor holds until the reset,
  and then it relaunches.

### [enforce] One enforcement surface, failing closed

- **One dispatcher entry per event.** That covers PreToolUse, PostToolUse, SessionStart (startup,
  resume, clear, compact, fork), SubagentStart, SubagentStop, Stop, PreCompact, PostCompact and
  SessionEnd, plus one per git hook. Rule modules load lazily per tool, to stay within the 57 ms that
  one guard costs today.
- **Rules come in packs, from the layers and kits that own them:**
  - roles: the spawn guard, write gates, the answered-call rule, act binding;
  - memory: the `record` write boundary;
  - instruction: the instruction-edit guard;
  - lexicon: the commit check;
  - flow: the transition verifier;
  - observability: journaling.
- **Each rule declares:** its event and matcher, its owner, its decision class (refuse, warn, record),
  its failure mode, its latency budget and its policy key.
- **Failing closed:**
  - **Enforcement entries set `onFailure: "block"`** (`runtime.hook-failure`). That makes 1 entry to
    check per event instead of 13, and the class check "every enforcement entry fails closed" becomes
    one line.
  - **It needs a declared CLI floor** (`runtime.cli-floor`, 2.1.295), checked at session start. A
    session below it is handled as `runtime.below-floor` says.
  - **Where the platform cannot fail closed,** a witness record stands behind the act: Stop,
    SubagentStop and every git hook. The supervisor trusts the witness, never an exit code, as
    push-main already trusts its allow record.
  - **Git hooks trap signals,** and `core.hooksPath` becomes per-worktree.
- **An out-of-agent escape.** A guard that cannot start must not lock the session out of its own
  repair. A broken guard is disabled only by an owner command outside the agent, and that act is
  journaled.

### [isolate] Isolation by construction

- **A workspace per unit lease,** allocated by the supervisor (`runtime.isolation`):
  - a worktree branched from the build branch's tip, never origin's default;
  - the worktree's own hooks path;
  - a scratch directory, and one per agent inside it, since this round lost a probe to a shared name;
  - its environment.

  Ports and databases are allocated only where an adopter's isolation pack declares services.
- **Release reclaims all of it,** and a sweep reaps orphans: today, 8 merged worktrees and 497 stale
  temp directories.
- **The primary tree belongs to the lander.** No session works there, which ends the shared-index
  hazard.

### [sessions] Sessions and context

- **Every SessionStart source binds the session to its build and delivers the card:** startup, resume,
  clear, compact and fork. The resume misses (7 of 14) are diagnosed and fixed first.
- **A PreCompact command hook flushes the item in flight** (commit or checkpoint) before an automatic
  compaction. It is a safety net, not the plan.
- **The instruction file gains `# Compact instructions`:** a keep-list holding the card's pointers,
  the build, the item and the open asks.
- **Context, by kind of session:**
  - attended sessions follow `context.on-full` (the owner's CX-1 answer, revisited below);
  - driver sessions are relaunched fresh (`runtime.driver-refresh`), since every fact they need is
    witnessed.

### [schedule] The scheduler

- **Runtime runs cadence items that their layers declare:**
  - Maintain's detectors;
  - the weekly Loop Review;
  - lease and claim sweeps;
  - the nightly held bar.
- **Each cadence item fires `next`, under a lease,** so two nodes never run the same item.
- **Where it runs** (`runtime.scheduler`):
  - a desktop scheduled task on a node the registry declares; it survives restarts, and a missed fire
    runs at the next launch;
  - CI's schedule for read-only verdicts;
  - a cloud routine, once a routine has shown a green bar.
- **In-session cron is retired for cadence.** It is session-scoped, expires after 7 days, and fires
  only while its session is open and idle.

### [harness] Harnesses and nodes

- **One guard core, per-harness wiring** (`runtime.harnesses`). Claude Code wires `settings.json`;
  Codex wires `hooks.json`, whose events now match one for one.
- **The git boundary is the floor for every harness.** Harnesses with instructions only (Gemini,
  Copilot, Cursor, Windsurf) keep that floor.
- **The node registry gains runtime facts:** the CLI version against the floor, the clock offset,
  `autocrlf`, and the process-start cost class. The supervisor reads them before it runs.

### [extend] Every extension is a registered adapter or pack

| Extension point | What registers there | Examples |
|---|---|---|
| actor kinds | a new kind of actor an item can name | command, role, hook, owner |
| command adapters | a command with its witness contract | the bar runner, the lander, `record`, the instruction command |
| spawn backends | a way to start a role agent | Workflow subagents, a headless session, another harness |
| hook packs | rules per event, from any layer or kit | spawn guard, write gates, act binding, lexicon commit check |
| harness adapters | how a harness loads instructions, spawns, hooks and compacts | Claude Code, Codex |
| host adapters | where the supervisor and its sessions run | this node, a cloud host (`run.host`) |
| scheduler backends | how cadence items are woken | a desktop task, CI, a cloud routine |
| notification adapters | how an owner request reaches the owner | the terminal, a push notification |
| journal sinks | where runtime events go | runlog, observability's store |

A new step, role, record kind, rule, harness or host is a filled contract. Runtime gains no code.

### [invariants] What Runtime guarantees

1. Position is a pure function of the declaration, the witnesses and the policy, the same in every
   mode.
2. Every act was named by `next`: a spawn or transition it did not name is refused.
3. A witnessed item never runs again, and an unwitnessed one is always re-dispatchable.
4. No result exists only in memory: every return is persisted before its item counts as done.
5. Neither the decider nor the supervisor holds model context.
6. Records change only through `record`, instructions only through the instruction command, and main
   only through the lander.
7. Every enforcement rule fails closed, or has a witness behind its act.
8. No session the runtime launches skips permissions.
9. Every runtime behaviour is a policy key, and every runtime event is journaled.

### [contract] Runtime's layer contract

| Contract field | Runtime's entry |
|---|---|
| tag and definition | `layer.runtime`: decides from declared and witnessed state, acts through supervised mechanisms, enforces at every boundary, records that it did |
| instruction units | the driver's static block: ask `next`, run the named act, never improvise; the supervisor's run rules |
| engine kits | unattended (becomes the supervisor and client verbs), workflows (the role harness), hooks (the dispatcher and the core packs), process-monitor (supervision); branch-reconcile stays an expansion for housekeeping |
| record kinds | the run journal, the run record, item and transition witnesses, return records, workspace leases |
| extension points declared | the nine in `[extend]` |
| extension points used | none: integrations fill host, scheduler and notification adapters, and observability reads the journal |
| policies | the `runtime.*` keys below, with `leases.*`, `roles.retries`, `roles.no-spawn`, `run.*` and `context.*` |
| gates | the build's fixtures in `[tests]` |

## [policies] Runtime's keys, set under the owner's delegation

The owner handed this layer to the main loop. The defaults below are the main loop's, and every one
is switchable.

| Key | Allowed values | Default |
|---|---|---|
| `runtime.driver-lifetime` | build, item | build |
| `runtime.driver-refresh` | fresh, compact-with-card | fresh |
| `runtime.relaunch` | fresh, resume | fresh |
| `runtime.hook-failure` | closed, open | closed |
| `runtime.cli-floor` | a CLI version | 2.1.295 |
| `runtime.below-floor` | refuse, degrade | asked as RT-2 |
| `runtime.fanout` | an agent count | 5 |
| `runtime.isolation` | worktree-per-unit, shared | worktree-per-unit |
| `runtime.reap` | orphans, orphans-and-idle, report | orphans |
| `runtime.scheduler` | node-task, cloud-routine, ci-only | node-task |
| `runtime.harnesses` | claude-code, claude-code-and-codex, instructions-only | claude-code |
| `runtime.journal` | local-and-summary, local | local-and-summary |

## [build] Runtime's own chain build, as proposed

- **The build:** `dWellOiledMachine`, a child of dDeclaredLoop. It needs the loop kit's position function
  and declaration.
- **Its units:**
  - the `next` CLI over the loop kit's function, with the derivations merged;
  - the client verbs;
  - act binding;
  - the supervisor: headless driver sessions on an allowlist, fresh relaunch, agents in flight under
    the lease, journaling;
  - the role harness's durable returns (the subagent-stop hook) and the shared deferral factory;
  - the one enforcement surface: lazy packs, failing closed above the CLI floor, witnesses behind
    Stop, SubagentStop and git, signal traps, per-worktree hooks, the owner's escape;
  - per-unit workspaces with per-agent scratch;
  - supervision: reaping, stalls, lease expiry and pruning;
  - session binding on every source, the pre-compaction flush, `# Compact instructions`;
  - the scheduler on a declared node;
  - Codex wiring;
  - the node registry's runtime facts.
- **Gaps it would take from other builds:**

  | Gap | From | What it records |
  |---|---|---|
  | `gap-tool-03` | dDeclaredLoop | the hook surface |
  | `gap-orient-12` | dDeclaredLoop | resume delivers no card |
  | `gap-orient-14` | dDeclaredLoop | compaction is ungoverned |
  | `gap-conc-03` | dScopedBuild | no isolation mechanism |

- **Gaps that stay where they are:**
  - `gap-conc-01` and `gap-conc-02` stay with dDeclaredLoop, whose coordination feature the supervisor
    executes.
  - `gap-maint-01` stays with dTendedCadence, which declares the cadence the scheduler runs.
  - `gap-deploy-07` stays with dShippedRelease, whose lander the witness pattern already guards.
- **Its new gaps** are in `[gaps-proposed]`.

## [tests] Fixtures the build owes, each able to make the design lose

1. `next` gives byte-identical answers on one build folder attended and unattended, with
   `.unattended.conf` absent.
2. Replay every act in the journaled builds' `driver.log` against the declared loop. More than 5% of acts
   outside a declared item makes act binding lose.
3. Kill the driver's process tree mid-unit. The supervisor relaunches, and no completed agent is paid
   for twice.
4. With a stub CLI reporting a session limit, the unit comes back `deferred-platform` and the
   supervisor holds.
5. Two concurrent dispatches of 5 agents under one lease: the second queues.
6. SubagentStop fires for a role-typed Workflow sidechain agent. If not, the stated fallback.
7. Replay the 2026-10-14 burst against `onFailure: "block"`: all 31 are refused, and a missing-path
   guard does not lock out the owner's escape.
8. Two passes commit concurrently in their own worktrees with no index lock. After N units, worktree and
   temp-directory counts return to baseline, and each worktree resolves its own hooks path.
9. A `fork` and a resume each deliver the card. A PreCompact hook flushes an item's work before an
   automatic compaction.
10. A cadence item fires once across two nodes, and a missed fire runs at the next launch.
11. A Codex `apply_patch` PreToolUse payload is graded by the shared guard core.
12. The cost of one headless driver start on Windows, measured.

## [gaps-proposed] Gaps to register once the design settles

New area `Runtime`:
1. HIGH. A model session decides every next act:
   - 19 of 20 sessions resumed from a compaction's summary instead of state;
   - the driver refused 47 malformed or out-of-order transitions;
   - sessions improvised their own drivers: 17 inline workflows in one, 25+ scripts in another;
   - 2 runs were left at BUILDING with all work terminal.
2. HIGH. Every enforcement hook fails open:
   - no entry sets `onFailure`;
   - 31 failures in one burst on 2026-10-14 all admitted the call;
   - three git hooks trap no signal;
   - the switch needs CLI 2.1.295, and the PATH CLI is 2.1.292.
3. HIGH. Spawned work dies with its session:
   - 4 background agents died with their parent;
   - limits killed 57 agents in 16 Workflow runs, the whole fan in 10;
   - 7 of 12 all-errored runs report `completed`;
   - a null becomes `committed:false` with no reason.
4. HIGH. The headless resumer skips permissions (`resume-tick.sh:385`). With hooks failing open, a
   resumed session under resource exhaustion would run unguarded.
5. MED. Fan-out is bounded per burst, not in flight:
   - the direct budget resets on every notification;
   - Workflow calls and headless launches are outside the count.
6. MED. Workspaces are neither allocated nor reclaimed:
   - 8 merged worktrees and 497 stale temp directories remain;
   - the absolute `core.hooksPath` runs the primary tree's hooks in every worktree;
   - concurrent agents share one scratch directory.
7. MED. Supervision reports and never reaps: 44 idle processes flagged, 4 killed by hand.
8. MED. Runtime has no scheduler: cadence runs only as in-session cron, which expires after 7 days and
   fires only while its session is open.
9. LOW. Session hooks miss events: no matcher covers `fork`, and SessionEnd and PostCompact are unwired.
10. LOW. Node facts go unrecorded: node d's clock runs 8 to 13 s slow, its `autocrlf` differs from
    CI's, and no node records its CLI version against the floor.
11. LOW. gov wires no Codex hooks, though Codex now ships the matching events.
12. LOW. Runtime records contradict the code:
    - the "four-verb driver" has 30 verbs;
    - `/build` claims an identical spec review in both modes;
    - an earlier design record said the spawn guard compares `role-sha`;
    - the Facts line says "Worktrees: none yet", and 13 exist;
    - a keepalive comment says the cron store dies with its session.

Already registered and taking a fix designed here:
- `gap-roles-04`: returns uncontracted;
- `gap-conc-02`: claims never age;
- `gap-flow-10`: the owner's missing controls;
- `gap-deploy-07`: a killed hook lands a push.

Their owners stand.

## [questions] To put to the owner once the reviews are folded

- **RT-1.** `context.on-full` for attended sessions. The owner's CX-1 answer assumed that a resume is
  cached input. Measured, a resume's first turn is mostly cache creation (503k), while a compaction
  reads about 970k cached tokens and takes about 117 s.
- **RT-2.** `runtime.below-floor`: what happens on a node whose CLI is below the fail-closed floor.
- **RT-3.** Runtime's own chain build, `dWellOiledMachine`, and the four gaps it takes over.
