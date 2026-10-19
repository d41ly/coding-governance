# Layer review: the runtime layer

**Serves:** research PLAY-dClosedLoop-1

The fifth round of the owner's layer-by-layer review: the runtime layer. Layers round one made Runtime
a core layer: "Instruction says, Runtime enforces, Flow witnesses, Memory proves." v2's `[owed]` gives
it a chain build of its own, once this review settles what that build holds.

Four researchers measure the runtime in parallel: dispatches 30 to 33. Their returns are saved
verbatim beside this record, and the design is written here once they return.

Revised: 2026-10-15, after two independent Tier-2 rounds on blob `767187aa`, as the owner asked:
- each of their 59 distinct defects is folded here;
- `build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md` compares the two rounds and
  maps every finding to its fold;
- `[reviews]` keeps what was re-read rather than taken whole.

The design keeps its shape (decide, supervise, act, enforce). It changes in five places:
- deciding is Flow's position function, and Runtime owns the `next` verb that asks it (RT-3);
- a session the runtime launches lives for one act;
- returns survive any death, through a store the executor hands back;
- binding happens at the call a hook can see;
- every key that duplicated an existing carrier is gone.

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
  | the lander (`push-main.sh`) and the landing queue dShippedRelease builds (`gap-flow-08`; revised 2026-10-16: the turnstile is a bar semaphore, so no landing queue exists yet) | flow-roles FR-6, deferred to the lower-level design | Deploy |
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

Some facts below were corrected after the reviews. Each correction names the defect from the comparison
record's map.

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
  - a schema-forced agent ends on a `StructuredOutput` tool call with no text block, so
    `last_assistant_message` does not carry its return (`structured-output`);
  - 20 concurrent subagents per session; 16 concurrent agents and 1,000 per Workflow run.
- **The resumer skips permissions:** `tools/unattended/resume-tick.sh:385` launches `claude -p
  --resume <id> --dangerously-skip-permissions --max-turns <n>`.

**Enforcement, isolation and supervision** (dispatch 32):
- **The hooks:** 13 entries from 6 owners, wired two ways (12 fragments and one hard-coded arm).
  Nothing sets `onFailure`, so every enforcement hook fails open.
- **The fail-open burst.** On 2026-10-14, resource exhaustion crashed the guards 31 times, and every
  failure admitted the call.
- **The fail-closed switch** (`onFailure: "block"`) needs CLI 2.1.295, which the changelog confirms.
  This node's PATH CLI is 2.1.292, and it ignores the key without a warning. The switch has no effect on
  Stop or SubagentStop.
- **Failing closed without the switch** was re-verified for RT-2 by dispatch 36:
  - on 2.1.292, an ask rule on each gated tool, answered by a PermissionRequest hook, denied the call
    under every burst failure class, read-only commands included;
  - a PreToolUse hook as the allow path fails open in auto mode.
- **The git hooks:**
  - `pre-commit`, `commit-msg` and `pre-rebase` trap no signal, so a killed hook reads as success;
  - `core.hooksPath` is absolute and resolves into the primary tree's checkout, so every worktree runs
    whatever that checkout holds. WIRE-INTO-PROJECT prescribes an out-of-tree copy under the git
    common dir, so that a branch cannot render its guard inert. TOOL-aWeldedTribunal-7 reports a
    divergence, and the open TOOL-aWeldedTribunal-10 asks the push boundary to refuse one (`hookspath`).
- **Parallel units are cleared on proof** (`parallel-cleared`):
  - two passes committing on one index failed, and the harness ruled "parallelism route: none";
  - TOOL-dUnstalledConvoy-7 then measured one worktree per pass and recorded `parallelism route:
    cleared`, provided no pass writes a shared mutable record;
  - TOOL-aHoistedPass-10 made BUILD-METHOD's rule on passes and parallelism parallel-on-proof;
  - TOOL-dDerivedDocket-31 narrowed that to delegated passes.
- **Leftovers:**
  - 13 worktrees, 8 of them merged orphans;
  - 497 temp directories older than 7 days;
  - no port or database allocator.
- **Supervision reaps only by hand:**
  - procmon-hook runs `reap.py --sweep --dry-run` at session start and after shell calls, and prints
    the command;
  - `PROCMON_REAP_MODE` is reap-orphans here, but nothing runs the sweep;
  - 44 idle processes were flagged in 60 days, and 4 were killed by hand;
  - claims never expire, a `held` claim is immortal, and terminal refs are never pruned.

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
  - `# Compact instructions` in the instruction file are honoured, and gov has none. Whether a section
    reached through `@AGENTS.md` is honoured is unverified (`compact-target`);
  - PreCompact exists and can run a command, but cannot inject;
  - after a compaction, up to 5 recently read files return, each under about 5,000 tokens;
  - root `CLAUDE.md` returns, and path-scoped rules do not;
  - a subagent re-receives only its SubagentStart context.
- **Scheduling** (`resume-tick-seed`):
  - in-session cron is session-scoped and expires after 7 days;
  - out of session, three actors run today:
    - the OS-scheduled resume tick (`gov-resume-tick`, every 10 minutes, registered by hand per node);
    - the desktop durable-restart task (`RESUME_SCHEDULE_*`);
    - remote CI's cron, a read-only held bar;
  - no declared cadence item runs out of session.
- **Harnesses** (`codex-events`):
  - Codex ships five hook events: PreToolUse, SubagentStart, SubagentStop, PreCompact and SessionEnd;
  - it has no Workflow tool (unverified), and no fail-closed switch is shown;
  - its docs call its hooks "not a complete enforcement boundary";
  - gov wires none of them.
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
| Defaults by mechanism, not by agent discretion (the lexicon) | enforcement at every boundary, failing closed, with every exception recorded (`core.exceptions`) and every bypass paid for (`core.bypass`) |
| Every behaviour owner-switchable, every layer extendable by contract | every runtime behaviour a policy key, and every runtime part an adapter or a pack |

**In one line: the other layers declare. Flow's position function decides from what they declared. Runtime executes
each decision through mechanisms it supervises, enforces at every boundary, and records that it did.**

## [design] The mechanism

```text
 declarations (read-only): instruction units · loop (items, deps, witnesses) · role registry ·
 record kinds · policy file · hook packs · gate packs · adapters · cadence items
                                     │
                                     ▼
 Flow's position function (dDeclaredLoop), asked through Runtime's next verb: a pure function of
 declaration, witnesses and policy, answering act · awaiting · blocked · terminal · stuck ·
 invalid-input · stale-remote
                                     │ asked on every beat
                                     ▼
 ┌───────── THE SUPERVISOR: the executor as a process, no model (resume-tick grown) ─────────┐
 │ started and restarted by the node tick · holds each build lease and its epoch · cuts each  │──► journal
 │ work order fresh · runs command items · raises owner items · launches one act session per  │
 │ role act · reserves agent slots · queues and merges commits · allocates and sweeps         │
 │ workspaces · holds on limits · wakes cadence items                                         │
 └───────┬────────────────────────────┬──────────────────────────────────┬──────────────────┘
         │ command items              │ role acts                         │ owner items
         ▼                            ▼                                   ▼
  command adapters             an act session: claude -p for one     the mailbox and the
  (the bar, the lander,        act, in its workspace, under its      notification adapter, or
  record, the instruction      schema and epoch, making one call     run.on-owner-question
  command), each idempotent    to the role harness: prompt writer,
  or reconciling               work order, role agents
         │                            │ returns persisted at SubagentStop, through record
         └──────────── witnesses (memory) ◄──┘
 every tool call, write, spawn, return, stop, commit and push passes ONE enforcement surface:
 one dispatcher entry per event rendered from the kits' fragments, packs from every layer, failing
 closed on every CLI version through ask rules only the dispatcher answers, and a witness with a
 named reader behind every event that cannot
 attended or not: the supervisor drives, and the owner's session is its client; it hosts the driver only
 until dWellOiledMachine lands, or if its spike fails, each role act it hosts act-bound (night pass, point 1)
```

### [terms] The sibling layers' words, mapped

The flow and roles records name Runtime's parts in their own words. This is the one map:

| Their word | Where | Runtime's part |
|---|---|---|
| the executor | flow-steps; roles `[cycle]`, `[trust]` and the matrix | the supervisor, together with the role harness it launches. It keys and cuts each work order fresh at the spawn, through dBoundRoles' renderer. It runs command items such as acceptance re-runs and the core checks, reads the mailbox at item boundaries, and queues commits. It is launched where `run.host` says. |
| the driver | roles `[cycle]`: "The main session is the driver … The executor drives when no one attends." | the supervisor, in every mode (night pass, point 1). The owner's session is its client: it shows the announcements, takes the owner's dispositions and issues the owner's controls. The owner's session hosts the driver only until dWellOiledMachine lands, or if its platform spike fails (v2 `[owed]`), under its owner binding, each role act it hosts act-bound with that act's epoch. No model session drives. |
| an act session | this record only | a headless `claude -p` session that the supervisor launches to host one role act's harness call. It decides nothing. The first draft called it a "driver session", a name the roles layer already uses. |
| the actor kinds | the roles matrix: role, command, hook, executor, owner | a role item becomes a role act. The supervisor runs command and executor items. A hook item is awaited: its hook writes the witness when its event fires inside another act, and `next` reports it as awaiting that event. The supervisor raises an owner item. |

### [decide] Deciding is Flow's; Runtime asks through `next` and acts on the answer

- **Two owners, one piece each** (RT-3, the owner's answer):
  - dDeclaredLoop owns the position function: what position means, computed from witnesses;
  - Runtime owns the `next` verb that asks it, the `next —` micro-format, the check that every declared
    command ends with one, and the owner's controls below.

  The supervisor asks on every beat and acts on the answer, and never derives position itself. v2's
  `[chain]` now holds each piece in one row, which ends the duplicate claim both review rounds found.
- **The answers Runtime needs.** The position function returns a closed set of answers, which `next`
  prints. Each is a declared supervisor transition:

  | Answer | What it carries | What the supervisor does |
  |---|---|---|
  | `act` | the frontier's items, each with its act: the item, its actor kind, its work order's key and `task-sha`, its harness, and the outcome table it routes on | runs each act |
  | `awaiting` | each awaited item, with the event or record it waits on | holds, and asks again when that event fires. A build that still holds its lease renews it; one whose lease `deploy.unlease` deleted holds none, and its wait belongs to its event wake and the ceiling sweep (`[schedule]`). It raises no owner item itself: a wait with a ceiling is raised by the supervisor's sweep (`[supervise]`) |
  | `blocked` | each blocked item, with what blocks it | raises an owner item once nothing the item waits on is in flight |
  | `terminal` | all work terminal | closes the run; the two runs left at BUILDING were this case |
  | `stuck` | no frontier, while the build is not terminal | raises an owner item at once |
  | `invalid-input` | a malformed declaration, policy value or witness, named with its path | refuses to act, and journals it |
  | `stale-remote` | lease or ref witnesses that cannot be read | holds and retries, and parks once `leases.expiry-hours` passes |
- **Item instances.** An item's witness is keyed by the item, its round or pass, and its inputs' SHAs. A
  route back mints a new instance. Routes back include:
  - a failed check returning to `entry.place`;
  - a fix pass after acceptance fails;
  - a review's next round;
  - a backward transition.

  So "never runs again" holds per instance, and the flow's loops still loop.
- **Clients.** Runtime's verbs are the whole client surface (RT-3):
  - `next`, which prints the position function's answer, ending with its `next —` line;
  - `run <build>`, which takes the build lease and registers the build with the node's supervisor, attended
    or not, the owner's session becoming its client (night pass, point 1);
  - the owner's pause, resume, withdraw and supersede (`gap-flow-10`), through dDeclaredLoop's guarded
    command. They extend unattended's `--hold`, `--resume` and `--abort`; supersede is new. The
    supervisor honours each at its next beat.

  The `/build` and `/unattended` skills become clients of these verbs, and `/unattended` retires with the kit at
  dConvergedCharter (night pass, point 1).

### [supervise] The supervisor: the executor, as a process outside any session

- **Its seam is `resume-tick.sh`, grown.** The supervisor generalises `tools/unattended/resume-tick.sh`
  and keeps what that seam already proves:
  - the index-read lease, and the stand-off from a foreign lease;
  - login before kill, and killing only what it launched;
  - the attempt cap (`RESUME_ATTEMPTS`) and `run_detached`;
  - `--liveness` as the only stale or terminal verdict, and `--beat`.

  It replaces only the launch: `--resume --dangerously-skip-permissions`, at `resume-tick.sh:385`.
- **Its host is the node tick.**
  - The OS-scheduled `gov-resume-tick` registration runs every 10 minutes (`tools/unattended/README.md`).
    It starts the supervisor when none beats under a live lease, and restarts it after a crash or a
    reboot.
  - Preflight refuses a node that declares itself a run host without that registration.
  - A desktop scheduled task wakes a model session, so it can host an act but never the supervisor.
  - The desktop durable-restart task (`RESUME_SCHEDULE_*`) retires.
- **Each beat:** read the owner's controls, ask `next`, act on its answer, renew the lease, and journal.
- **Act sessions.** For each role act, the supervisor first cuts the work order fresh through
  dBoundRoles' renderer (P29). Then it launches one `claude -p`:
  - in the act's workspace (`[isolate]`), since a launch fixes its working directory;
  - with `--session-id` recorded beside the lease epoch, `--output-format json`, `--json-schema` set to
    the act's return schema, and `--max-turns` from `RESUME_TURNS`;
  - under `--permission-mode auto`, as the owner ruled for unattended runs (TOOL-aMendedFleet-116, built
    by TOOL-aMendedFleet-117). Gated tools carry ask rules, and only the dispatcher answers them, by the
    act's allowance (`[enforce]`);
  - with the `claude` binary the supervisor resolved. The node registry records each binary's path,
    version and capabilities, such as `onFailure`. Any version may launch, because the permission
    baseline fails closed without the switch (`[enforce]`, RT-2);
  - registered with process-monitor under `runtime.act-ceiling`.

  The harness call runs in the foreground, so the session waits for its Workflow. The existing
  launcher's `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS=0` would cut a backgrounded run off.
- **Relaunch.**
  - An act session that dies, hits a session limit or exhausts `--max-turns` is relaunched as
    `runtime.relaunch` says. The default is fresh.
  - A fresh relaunch loses nothing returned. The supervisor hands the act's persisted returns into its
    harness, which spawns only the agents with none (`[spawn]`).
  - Relaunches of one act stop at `RESUME_ATTEMPTS`, with a backoff between them. Past the cap, the item
    parks with a journaled reason and an owner item.
- **Session limits.**
  - stall-recorder's StopFailure record is the limit signal.
  - The supervisor parses the reset time from the limit message, holds new launches until then, and
    keeps renewing its lease.
  - A weekly limit can hold for days. So once the hold passes `runtime.hold-ceiling`, the supervisor
    raises an owner item and keeps holding.
- **Fencing.** Revised: 2026-10-17, the debt round's fold.
  - Each lease carries an epoch in dDeclaredLoop's lease grammar, bumped at every take-over. One name
    per lease: the build lease (which the first draft also called the run lease), the unit lease, and
    the cadence lease, which an event wake takes for its instance (`[schedule]`).
  - Each act session's `--session-id` is recorded with the epoch it serves.
  - The commit queue and the lander's prepare refuse a stale epoch at once, since each re-reads the
    lease from the remote. The dispatcher's PermissionRequest decision refuses a gated call once the
    lease ref it reads shows the epoch stale, which across nodes is no later than the refresh below
    (`[act]`). Revised 2026-10-17, the folds' closing review: this bullet once claimed the dispatcher refused at once.
  - **Where the epoch is read.** The dispatcher reads the lease ref in its clone, which the supervisor
    refreshes from the remote at each beat, since `next` reads the lease witnesses. A supervisor that
    finds its lease taken over kills the act sessions it launched under the old epoch. With no
    supervisor beating there, the node tick restarts one within its period, and that one does the
    same. Until then an old session's gated calls touch only its own workspace: the commit queue and
    the lander's prepare re-read the epoch from the remote before they commit or push.

  So a take-over is safe while the old node's act sessions still run. It is safe under clock skew too
  (node d runs 8 to 13 s slow), because correctness rests on the epoch, never on two clocks agreeing.
  On the same node, a take-over kills the old process tree first. Across nodes, an old session stops at
  its next refused call.
- **Every command item is idempotent, or it reconciles.** Each command adapter's witness contract
  declares which. A reconcile probe detects an effect that landed without its witness:
  - the lander checks whether origin already holds the expected sha;
  - `record` is content-addressed;
  - a bar run is re-runnable.

  So a take-over never pushes twice.
- **Agents in flight.**
  - The bound is `runtime.agents-in-flight`, one key, 6 by default, that the owner raises or lowers by a policy write (revised
    2026-10-19, the night pass two, point 7, the owner's NT-27 and NT-28). It was agent-cap's lower-only
    `FANOUT_CAP` in `.agent-cap.conf`, never above 5 (TOOL-aRepatriatedFork-7), which counted claims per
    prompt, never agents in flight. Runtime adds no second carrier for it.
  - Before a launch, the supervisor reserves the act's declared fan, its harness's static maximum,
    against a counter under the lease. When slots are short, it queues the act.
  - It releases the slots when the act session exits, or when the reap kills its tree.
  - In the owner's session, while it hosts the driver, the PreToolUse entry on Workflow and Agent reserves
    the same way, and queues the call instead of refusing it (the owner's NT-28). Both calls run in the background, so the reservation is released when the call's work
    ends: at SubagentStop for an Agent call, and at the run's saved result for a Workflow call. A sweep
    keyed to the session's liveness frees what a dead session held.
  - agent-cap's per-prompt total retires with agent-cap (revised 2026-10-19, the night pass two, point 7).
    The harness's own concurrency settings, rendered from the key, bound one session's direct spawns and
    one Workflow run. A hook pack claiming a slot at SubagentStart and releasing it at SubagentStop bounds
    the session's total, once the spike shows SubagentStop firing for every way an agent ends. A Workflow
    agent's claim converts one slot of its call's reservation, matched by its run, so it is never counted
    twice (the night pass two's review).
- **Supervision.** On each beat, the supervisor:
  - runs `reap.py --sweep` under `PROCMON_REAP_MODE` (reap-orphans here);
  - reaps act sessions past `runtime.act-ceiling`;
  - expires leases past `leases.expiry-hours` and prunes terminal run claims (`refs/gov/runs/*`),
    through dDeclaredLoop's coordination verbs. It never prunes `refs/gov/claims/*`, where a slug's
    claim lives (layer-memory `[contract]`);
  - raises the release hold's owner item for each `deploy.released` wait that has outlived
    `build.release-ceiling`, counted from the landing record or from the owner's last keep-waiting
    answer, through the notification adapter. The item is keyed by (build, landed SHA), and the sweep
    opens it only when none is open, as every producer of that item does (flow-steps'
    `deploy.released` and `life.quiesce`). The sweep reads `build.closes` and `build.release-ceiling`;
  - names holders by fleet tag.
- **Shared records.**
  - Under the supervisor, only it writes a build's shared mutable records: decision rows, the run
    record, backlog rows. It writes them through `record`, in a commit of their own.
  - TOOL-dUnstalledConvoy-7 cleared parallel passes on exactly that condition, and unattended's
    `--dispatch` already refuses those records in a pass commit.
  - Roles return the rows. They never write them.
- **Its own death** loses only the beat in flight. The node tick restarts it, and a take-over on any node
  reads the same witnesses under a new epoch.

### [act] Acts, and how each is bound

- **A role act is the roles cycle, in one call.** The act session, or the owner's session while it
  hosts the driver, its role act act-bound with that act's epoch, makes exactly one call (night pass, point 1): the registered role harness, with the act's work order and any persisted
  returns as its args. Inside that call the harness:
  - spawns the prompt writer;
  - wraps its task in the work order;
  - spawns the role agent (roles `[cycle]`).
- **Binding happens at the granularity the platform lets a hook see.**
  - **The call.** Revised: 2026-10-17, the debt round's fold. The dispatcher's PermissionRequest entry
    decides every gated call, and it is the one entry that fails closed below 2.1.295 (`[enforce]`). In
    an act session it compares the call (the registered harness, and its args digest) with the act
    `next` named for this session, and the session's epoch with the lease's (`[supervise]`). It
    refuses:
    - a Workflow, Agent or transition call the act did not name;
    - any gated call from a session whose epoch is stale.

    The PreToolUse entry repeats the comparison to refuse early and to journal. It decides nothing, so
    a PreToolUse crash below 2.1.295 opens no path.
  - **The decision, by binding.** An act session's gated call is approved on its binding and its
    allowance. Who judges an attended or unbound session's gated call is `runtime.attended-judge`'s
    (RT-4, 2026-10-17):
    - **`classifier-or-person`, the default.** The session loads no ask rule. Its guard packs refuse
      what they refuse, the write gate included, and auto mode's classifier or the person judges
      every other call, as today.
    - **`allowance`.** The session loads the ask rules. The dispatcher approves only a call inside
      `runtime.attended-allowance`, and makes no decision on any other, so it goes to the person.
    - **`person`.** The session loads the ask rules, and the dispatcher approves none. The person
      answers every gated call, and an unbound headless session's gated calls are denied.
    - **What the first text did.** It approved those calls once the guard packs passed. None of the
      packs judges whether a command is dangerous, so nothing judged them (the folds' closing
      review's H1).
  - **Inside an admitted script.** No hook sees `agent()` or a nested `workflow()`, so these are bound
    statically and reconciled afterwards:
    - each registered harness declares its spawn sites and its maximum fan, which agent-cap's script
      rules already scan for, and the merge bar's harness checks scan once agent-cap retires (the night
      pass two, point 7);
    - SubagentStart and SubagentStop journal each agent, with its spawn marker;
    - at the act's end, the supervisor reconciles the journal against the declaration. An agent outside
      the declaration voids the act's witness, so the item re-runs.

    One thing stays unchecked, stated plainly: the runtime count of `agent()` calls between those
    journal entries.
  - **The shell.** An act session's allowance names the commands it may run, and act binding refuses a
    Bash or PowerShell call outside it. That binds the class behind the 25 ad-hoc scripts in
    `[current]`. Each role act the owner's session hosts is act-bound with that act's epoch, under the
    session's owner binding. Outside role acts it reads and orients, and its product-code writes still pass the write gate (night pass, point 1).
  - **Session binding.**
    - SessionStart writes a binding record: the build, plus either the act and its epoch or
      "owner", the session the owner types in, attended or not (night pass, point 1).
    - Act binding requires that record, so a crashed SessionStart makes the first gated call refuse.
    - A session outside every build's workspace is unbound. Act binding then does not apply, and the
      write gate still refuses product code that no specced unit owns.
    - The orientation scout's spawn at session start is a bound act of the owner binding.
- **Owner items need no session.** The supervisor raises them through the mailbox and the notification
  adapter, or resolves them as `run.on-owner-question` says, never a ratification (FH1).
- **Hook items** are awaited, never dispatched (`[terms]`).
- **An act session's lifetime is structural.** It lives for one act. The platform fixes the schema and
  the working directory per launch, so a session serving many acts could neither schema-force each one
  nor enter each unit's worktree. The lifetime is therefore no policy key, since the alternative is not
  feasible.

### [spawn] Spawning, and returns that survive any death

- **Two backends, one contract.** `runtime.spawn-backend` names a registered backend:
  - **`in-session`:** the hosting session's Workflow runtime, `agent()` with schemas. Multi-agent harness
    acts, such as a review's fan, always run here, where their scripts live.
  - **`headless`:** one lean `claude -p` per agent, launched by the supervisor, whose return is the
    process's `structured_output`. No hook needs to see the spawn, since the supervisor launched it.

  The spike (`[tests]` `spike`) runs one single-agent act both ways. The build builds the cheaper
  feasible backend for single-agent acts, and the other stays a contract slot. Until the spike runs,
  the default is `in-session`.
- **Returns are persisted from where they live:**
  - a SubagentStop entry writes each agent's return through `record`, under the return-record kind;
  - it keys the return by the item instance, the work order's `task-sha`, and the spawn site and index
    the harness declares (`[act]`). All are stable across sessions, unlike `agent_id`. SubagentStop
    reads the spawn site from the spawn marker it journals, so a relaunch can tell which agents of one
    fan returned;
  - for a schema-forced agent, the return is the input of the last `StructuredOutput` call in
    `agent_transcript_path`. Such an agent ends on that call with no text block: the roles research
    counted 2,588 such endings against 226 text endings. So `last_assistant_message` is read only for
    free-text roles;
  - a byte cap and the item's schema are checked before the write;
  - under the headless backend, the supervisor persists the process's `structured_output` the same way.
- **A failing return** is held with exit 2, at most `roles.retries` times. After that it is persisted as a
  refusal and routed by the item's outcome table.
  - An empty, unparseable or oversized return is a failing return.
  - A SubagentStop entry that crashes persists nothing, because `onFailure` has no effect there. The item
    then stays unwitnessed and re-dispatchable, so the cost is a re-spend, never a wrong result.
- **Who owns what.** The return contract and its validation are dBoundRoles' (`gap-roles-04`), and run as
  a roles pack. Runtime builds the store, its keying and its write path.
- **A relaunch re-pays only what is missing.**
  - The supervisor hands an act's persisted returns into its harness's args, since the Workflow runtime
    reads no store. The harness then spawns only the agents without a return.
  - `resumeFromRunId` is not relied on: it replays only in the same session or after `--resume`.
  - For a harness with no SubagentStop, `runtime.relaunch=resume` is the fallback, at a resume's price.
- **One deferral shape.**
  - A null `agent()` result is `deferred-platform`, never `committed:false`.
  - That is the shape `tier2-review.js` already returns (`exit`, `key`, `pending`, `durable`), and
    `unattended-build.js` already holds on it under `--code platform-limit`.
  - It extends to `unattended-unit.js`'s null path. It is carried as a byte-identical block under a
    parity gate, since Workflow scripts import nothing.
  - A partial fan persists its returns and defers its nulls, and the relaunch re-pays only the nulls.
- **Role agents stay write-less.** Three harnesses tell their agents to write DURABILITY files, and those
  writes retire. The guard's state stays apart from what it guards.
- **"Always" holds by construction.** The supervisor launches every act itself, so no item depends on a
  parent's ability to spawn.

### [enforce] One enforcement surface, failing closed

- **One dispatcher entry per event, rendered from the kits' fragments:**
  - a hook pack is today's `*.fragment.json` (event, matcher, marker, hook path), extended with its
    owner, decision class (refuse, warn, record), failure mode, latency budget and policy key;
  - dDeclaredLoop's hook factory makes the packs;
  - settings-merge.py renders one dispatcher entry per event from the fragments, writes `onFailure`,
    and compares both in `--check`;
  - the class check "every enforcement entry fails closed" is a new arm of check-wiring.sh, over its one
    fragment reader. It also fails when a gated tool's ask rule has no PermissionRequest dispatcher
    entry;
  - agent-cap's hard-coded arm becomes a fragment, then retires as its rules move to their homes (the
    night pass two, point 7).
- **The events:**
  - PreToolUse and PostToolUse;
  - PermissionRequest, the gated tools' one allow path;
  - SessionStart, from every source: startup, resume, clear, compact and fork;
  - SubagentStart and SubagentStop;
  - Stop and StopFailure;
  - PreCompact, PostCompact and SessionEnd;
  - the git hooks.
- **Every live hook has an owner pack.** A gate compares this table with `settings.json` both ways: an
  entry with no row turns it red, and so does a row with no entry.

  | Hook today | Event | Kit | Pack |
  |---|---|---|---|
  | agent-cap | PreToolUse: Workflow, Agent | hooks | roles: the spawn guard and harness admission; runtime: the slot reservation, from SubagentStart and SubagentStop, and binding's early refusal; the review kit: the verifier total, the join ban and the spec-audit opt-in; agent-cap itself retired (the night pass two, point 7) |
  | the dispatcher's permission entry, new | PermissionRequest: the gated tools | hooks | runtime: the permission baseline, act binding and the epoch check |
  | scratch-guard | PreToolUse: shell and edits; SubagentStart | hooks | roles: write gates |
  | gate-guard | PreToolUse: shell, AskUserQuestion | unattended | runtime: the run guard |
  | manifest-check, writing and replaying the card | SessionStart | session-kickoff | runtime: session binding and the card |
  | check-wiring `--session` | SessionStart | check-wiring | runtime: the wiring check |
  | procmon-hook | SessionStart; PostToolUse: shell | process-monitor | runtime: supervision |
  | recall-opened | PostToolUse: Read | memory-recall | memory, an optional component (KN-1): the recall journal |
  | stop-guard | Stop | unattended | runtime: run continuation, retired for act sessions |
  | format-guard | Stop | hooks | instruction: the micro-formats |
  | stall-recorder | StopFailure | unattended | runtime: the limit signal |
- **Failing closed, on every CLI version, with no floor** (RT-2, re-verified by dispatch 36):
  - **The permission baseline.** Under `runtime.hook-failure=closed`, every gated tool carries an ask
    rule in every act session. The gated tools are Bash, PowerShell, Write, Edit, MultiEdit,
    NotebookEdit, Agent and Workflow.
    - **Where it lives.** The supervisor launches each act session with the baseline as an extra
      settings source, so the baseline is never in tracked settings under
      `runtime.attended-judge: classifier-or-person`. Under `allowance` or `person`, tracked
      settings carry it for every session (RT-4).
    - Only the dispatcher's PermissionRequest entry answers the rule, with a JSON decision made by the
      session's binding (`[act]`).
    - A dispatcher that cannot run leaves the call unapproved. In an act session the call is denied.
      In the owner's session under `allowance` or `person`, it goes to the person.
    - Dispatch 36 saw every burst failure class denied this way on 2.1.292, read-only commands
      included.
  - **One checking hook is the allow path.**
    - A crashed guard sitting beside a healthy allowing hook lets the call run, which is why the
      dispatcher is a single entry.
    - An allow rule on a gated tool would bypass the dispatcher, and so would a second
      PermissionRequest hook. A class check refuses either in tracked settings. The supervisor's
      preflight reads every hook and permission source an act session loads: the managed, user,
      project and local settings, each enabled plugin's hook files, and the hooks in agent and skill
      frontmatter. It refuses the launch while any holds one. check-wiring's session arm warns on
      either in every one of those sources (Revised 2026-10-17, the folds' closing review: the list once said settings only).
    - This repo's `.claude/settings.local.json` allows `Bash(git fetch *)` today.
  - **Auto mode stays, as the owner ruled** (TOOL-aMendedFleet-116).
    - The classifier still judges ungated tools.
    - An ask rule resolves before the classifier, so in an act session the dispatcher decides gated
      tools instead, by its binding.
    - Under `runtime.attended-judge: classifier-or-person`, the default (RT-4), the owner's session
      loads no ask rule, so the classifier still judges its gated calls too.
    - **What fails closed where.** Act sessions fail closed on every CLI version, through the
      baseline. The owner's session under the default fails closed where the CLI carries
      `onFailure`, from 2.1.295. Below that, a crashed guard lets the call reach the classifier or the
      person without that guard's check. The node registry's capability record says so per binary.
  - **The switch, where the CLI carries it.** Revised: 2026-10-17, the debt round's fold.
    - Under `runtime.hook-failure=closed`, settings-merge writes `onFailure: "block"` on every entry,
      since one tracked settings file serves every node.
    - The node registry records per binary whether the key takes effect, from 2.1.295. That
      capability decides only what the supervisor journals and what `fail-closed` claims for the node.
    - 2.1.292 ignores the key without a warning, so the switch is never assumed.
    - Where it takes effect, every enforcement entry also fails closed, ungated tools included.
  - **No version is refused or degraded.** TOOL-aMendedFleet-61's launch-version pin stands, and
    `read_cli_version` with the pinned `cli-version` fact reads the running session's version.
  - **What stays open below 2.1.295:** rules on ungated tools, such as the answered-call rule on reads.
    None of them guards safety, so a failure there costs tokens, not safety.
  - **The events that cannot fail closed each have a witness with a named reader:**

    | Event | Witness | Its reader |
    |---|---|---|
    | SessionStart | the binding record | act binding, at the first gated call's PermissionRequest decision |
    | SubagentStart | the journal entry, with the spawn marker | the supervisor's reconciliation at the act's end. Enforcement sits on the ask rule for Agent and Workflow |
    | SubagentStop | the persisted return | the supervisor, which counts an item done only on it |
    | Stop | the act's outcome record, which the supervisor writes through `record` from the process's JSON result at exit | the supervisor |
    | pre-commit, commit-msg | a witness per commit, keyed by its tree and message | the supervisor, which counts a commit item done only with it. An attended commit without one meets the lander's core re-check (K1) and is reported (`core.bypass=with-hooks-report`). |
    | pre-push | the allow record | push-main, as today |
  - **Signal traps.** Git hooks trap signals and exit non-zero when killed. That closes the class behind
    `gap-deploy-07`.
- **Hooks come from a trusted copy.**
  - `core.hooksPath` points every worktree at an out-of-tree copy under the git common dir.
  - check-wiring's session arm refreshes that copy from main; a branch never does.
  - This is WIRE-INTO-PROJECT's documented position: a branch can neither lack its own guard nor weaken
    it.
  - Today's absolute path resolves into the primary tree's checkout (the
    `hookspath-resolves-into-another-checkout` gotcha). The trusted copy ends that, and it is the fix
    the open TOOL-aWeldedTribunal-10 asks for.
  - Its readers change with it:
    - check-wiring's Check H refuses a path that resolves into a checkout;
    - run-gates' KF3 attribution and pre-push's rollout and straggler fallbacks follow the copy;
    - govkit's matrix writes it.
- **Bypasses and exceptions follow the owner's rulings:**
  - `hooks.bypass` is allowed until gate reliability is fixed, and `core.bypass=with-hooks-report` (K1,
    "the violator pays") stands. A bypass is journaled, and its commit meets the lander's re-check.
  - A rule a session cannot satisfy is excepted through the exception register (`core.exceptions`, K4).
    The exception is journaled and audited by the Loop Review.
  - A dispatcher that cannot start leaves every gated call denied in an act session, the call that
    records an exception included, and puts it to the person in the owner's session. An act session's repair
    therefore happens outside the agent: from the owner's terminal, or by the supervisor parking the
    run with the error. The repair is recorded in the same register.
- **User-level guards are outside the surface.** The node's own hooks, such as `git_dash_c_guard`, are
  recorded in the node registry. check-wiring's session arm warns on one that lacks
  `onFailure: "block"`.
- **Latency is measured, never promised.**
  - One guard costs 57 ms today.
  - The research projects about 85 ms for an in-process dispatcher, unless rules load lazily.
  - The `latency` fixture's first run sets the dispatcher's budget, and every later run is held to it.

### [isolate] Workspaces by `build.worktree`

- **The supervisor's allocator implements v2's `build.worktree`** (per-unit, parallel-only, shared;
  default shared):
  - **shared:** the build's one worktree. Parallel passes, proven disjoint under BUILD-METHOD's rule on
    passes and parallelism, stage their write sets. The commit queue then commits them one at a time,
    so no two passes share an index lock.
  - **per-unit, or parallel-only for parallel passes:** a worktree per unit lease, branched from the
    build branch's tip and never from origin's default. This is the route TOOL-dUnstalledConvoy-7
    measured and cleared.
- **Every workspace gets:**
  - the trusted hooks path (`[enforce]`);
  - a scratch directory, with one per agent inside it, since this round lost a probe to a shared name;
  - its environment;
  - line endings set from the node registry, so a fresh worktree starts clean. A dirty fresh tree
    blocks `--preflight`.

  Ports and databases are allocated only where an adopter's isolation pack declares services.
- **Integration before release.**
  - The supervisor merges each unit branch into the build branch, in declared order, before it releases
    the unit's lease.
  - It refuses release while the unit branch holds commits the build branch lacks
    (`git merge-base --is-ancestor`).
  - Shared records never ride a unit branch (`[supervise]`).
- **The sweep reaps only what the supervisor allocated:**
  - lease-marked directories under a gov-owned scratch root;
  - the worktrees it created, and those only when clean and merged.

  Merged branches and worktrees beyond leased workspaces stay with branch-reconcile. That kit is an
  expansion, so the core depends on nothing it does not ship.
- **The primary tree belongs to the lander.**
  - Act sessions never run there, and preflight refuses one that starts there.
  - The owner's session enters it only to land.

### [sessions] Sessions and context

- **Every SessionStart source binds the session.** The sources are startup, resume, clear, compact and
  fork; no matcher covers fork today.
  - The owner's session also gets the card. The resume misses (7 of 14, `gap-orient-12`) are diagnosed and
    fixed first.
  - Act sessions bind to their act and skip the card, since the work order carries every fact.
- **A PreCompact command hook flushes the item in flight** (commit or checkpoint) before an automatic
  compaction. It is a safety net, not the plan.
- **The compaction keep-list.**
  - It holds the card's pointers, the build, the item and the open asks.
  - It is an instruction unit, written through the instruction command.
  - The `sessions` fixture decides where it renders: into the charter if a section reached through
    `@AGENTS.md` is honoured, otherwise into root `CLAUDE.md`.
- **The owed CX-3 checks, disposed:**
  - **the re-attachment cap:** a file returns only under about 5,000 tokens, so a size check holds the
    card under it;
  - **a subagent's own compaction, and a PreCompact flush inside a subagent:** out of scope, since 0 of
    2,708 agent transcripts compacted. A journaled detector reports the first one;
  - **the executor holding no model context:** true by construction (`[invariants]`);
  - **compacting against starting fresh:** settled by RT-1. The owner's session starts fresh at an item
    boundary by default.
- **Context, by kind of session:**
  - the owner's session follows `context.on-full`, which now defaults to `fresh-at-boundary` (RT-1), and
    `context.threshold`;
  - act sessions read neither, since each serves one act, bounded by `--max-turns` and
    `runtime.act-ceiling`.

### [schedule] The scheduler

- **Runtime runs the cadence items that their layers declare.** These are Maintain's detectors, the
  weekly Loop Review, distribution's kit release, currency probe and fleet reading, lease and claim
  sweeps, and the nightly held bar. Each runs where its owner's key says:
  - `maintain.host` (session-start, os-scheduler, cloud-routine) for Maintain's items and the Loop
    Review;
  - `kits.host` (the same names) for distribution's programs;
  - `run.host` (requesting-node, os-scheduler, cloud-routine) for runs.

  Runtime adds no host key.
- **Journal retention.** The node tick prunes each journal past `runtime.journal`. Under `all`,
  nothing is pruned.
- **Host adapters:**
  - os-scheduler and requesting-node are the node tick (`[supervise]`);
  - session-start fires at the next session's binding;
  - cloud-routine is an integrations adapter, used once a routine has shown a green bar;
  - CI's schedule stays, for read-only verdicts.
- **Each cadence instance is keyed by its period** (ISO week or date).
  - The supervisor consults that witness before it takes the cadence lease, and again after. A
    witness that appeared in between releases the lease without a run.
  - So a node that wakes late, after another has run the period, skips it.
  - A missed period runs at the next wake.
- **An item can wait on an event.** `deploy.released` waits for the release slot's exit record. The
  record's event fans out to one instance per waiting build whose landed SHA the record's SHA
  contains, each keyed by (event, the exit record's id, build) and witnessed by build, so a skipped key
  never skips a second build, and a second pass over one SHA, whose exit record is a new one, wakes
  the build again (Revised 2026-10-17, the debt round's fold). The supervisor runs each under its instance's cadence lease, so it needs no build lease,
  and its records mint under the build's claim ref. A wait with no record is watched by the
  supervisor's sweep (`[supervise]`), which raises its owner item once `build.release-ceiling` passes.
  An owner request on a build whose lease is gone is an event too: the guarded command's record wakes
  one instance, keyed by (request, build), and `life.quiesce` runs under its cadence lease.
- **In-session cron is retired for cadence.**
  - It is session-scoped, expires after 7 days, and fires only while its session is open and idle.
  - The unattended skill's CronCreate keepalive and stop-guard's `session_crons` retire with it.

### [harness] Harnesses and nodes

- **One guard core, with per-harness wiring.** `runtime.harnesses` selects from the registered harness
  adapters.
- **Each harness adapter carries a capability table, measured and never claimed:**
  - **Claude Code:** every event in `[enforce]`, the Workflow tool, ask rules answered by PermissionRequest
    as measured on 2.1.292 and 2.1.295, and `onFailure` from 2.1.295.
  - **Codex:**
    - it has PreToolUse (Bash, apply_patch, MCP), SubagentStart, SubagentStop, PreCompact and
      SessionEnd;
    - as of Codex CLI 0.139 it documents twelve hook events, SessionStart, PermissionRequest, UserPromptSubmit, Stop
      and PostCompact among them, each project hook trusted by hash before it runs; whether PostToolUse is among them is
      unmeasured;
    - it has no Workflow tool (unverified), and no fail-closed switch is shown;
    - its own docs call its hooks "not a complete enforcement boundary".
    - Revised 2026-10-18, the away pass (`build/2026-10-18-build-PLAY-dClosedLoop-1-research-harness-cli.md` section
      3): the twelve events replace the five measured before, which named no SessionStart, PostToolUse, Stop or
      PostCompact. The conformance fixture re-measures the row (P36).

  Under Codex, the binding, return and fail-closed invariants hold only at the git boundary and through
  witnesses. So Codex runs instructions plus guards until a spawn backend is registered for it.
- **The git boundary is the floor for every harness.** Harnesses with instructions only (Gemini,
  Copilot, Cursor, Windsurf) keep that floor.
- **The node registry gains runtime facts,** which the supervisor reads before it launches:
  - each `claude` binary, with its path and version, whether `onFailure` takes effect on it, and whether
    its PermissionRequest can approve each gated tool;
  - the clock offset, and `autocrlf`;
  - the process-start cost class;
  - the user-level guards.

### [extend] Every extension is a registered adapter or pack

| Extension point | What registers there | Examples | Owner |
|---|---|---|---|
| actor kinds | a kind of actor an item can name | role, command, hook, executor, owner | dWellOiledMachine |
| command adapters | a command, with its witness contract and its idempotence or reconcile probe | the bar, the lander, `record`, the instruction command | dWellOiledMachine |
| spawn backends | a way to start a role agent | in-session Workflow, headless per agent, another harness's spawner | dWellOiledMachine |
| role harnesses | a Workflow script, with its declared spawn sites and fan | the role cycle, the Tier-2 review | dWellOiledMachine |
| hook packs | a fragment, with its owner, class, failure mode, budget and key | the spawn guard, act binding, the lexicon's commit check | dWellOiledMachine |
| harness adapters | how a harness loads instructions, spawns, hooks and compacts, with its capability table and its install targets | Claude Code, Codex | dWellOiledMachine |
| host adapters | where the supervisor and its sessions run | the node tick, a cloud host | dWellOiledMachine |
| notification adapters | how an owner request reaches the owner | the terminal, a push notification | dWellOiledMachine |
| journal readers | what reads the journal | runlog, observability's store | dWellOiledMachine |
| cadence items | a program with its host key, its period, its lease and its events | Maintain and the Loop Review; gov's kit release and the currency probe | dWellOiledMachine |
| memory mirrors | a backend that receives the change feed in real time and answers other nodes' reads, git staying the store of record | a cloud relational database | dWellOiledMachine |

- The keys that select an extension (`runtime.harnesses`, `runtime.spawn-backend`, `verdict`, `run.host`,
  `maintain.host`, `kits.host`, `notify.channel`, `release.environments` and `memory.mirror`) take registered names.
  This is the one list of them, and other records point here.
  They are validated against the registry, never against a literal enumeration. A name no installed
  layer registers is refused, or falls back to the built-in with a report, as
  `policy.on-missing-expansion` says.
- Added by the expansion round (`build/2026-10-16-build-PLAY-dClosedLoop-1-layer-expansions.md`):
  - cadence items, the tenth point above. Each event a cadence item names is produced by a core
    record, such as `landed` by the landing record;
  - a command adapter carries a class: an act, a reading or a fix. A reading carries its scope
    (repo, node or outside), pin, events, fix and liveness, and its owner is derived from the memory
    contract;
  - every adapter row carries a grant: the service it reaches, the scopes it needs, and its secret by
    reference, never by value, or `anonymous`. Runtime enforces it, whichever layer registers the
    adapter: registration probes the scopes granted and refuses wider than declared, and the secret
    lives where `runtime.secret-home` says;
  - a harness adapter declares its install targets: where a rendered Skill, agent, rule, hook or
    settings fragment lands.
- **The secret value scan** is Runtime's gate, as `runtime.secret-scan` says. Each adapter's runner,
  the one principal holding the value, scans for the value and its encodings, so the value never
  leaves its process. It binds at every boundary that publishes, over what that boundary publishes:
  - the lander's prepare, over the commits in the pushed range and the tracked files and `memory/`
    they carry;
  - the core's one ref-push path, over each `refs/gov/*` object it pushes (mailbox, card, leases and
    claims), whenever it pushes one, before the landing and after it alike.

  A hit refuses that push. The journal and the transcripts never leave the node, so the node tick
  scans them as a node-local population, and a hit there is an owner item. Each witness names what it
  read: whether the value resolved (yes, no or `anonymous`), each population's count, and the
  matches, as a count and a salted id only. Each population declares what it expects from a source the
  scanner does not enumerate (Revised 2026-10-17, the debt round's fold). The prepare takes it from the
  push's own ref update, its old and new SHAs, so a push that carries commits expects at least one,
  whatever the scanner's range reads; the ref-push path takes the one ref it pushes; and the node tick
  takes the journal entries and transcripts modified since its last scan, by their modification times.
  An unresolved value, or a zero against a non-empty expected population, is a dead probe, never
  green; an empty expected population reads "none carried", and `anonymous` reads not applicable, not
  zero. The `secret-scan` fixture in
  `[tests]` plants the value in every population named here.
- A new step, role, record kind, rule, harness, backend or host is a filled contract, so Runtime gains
  no code.
- The `extension` fixture proves this once, by registering a stub adapter with no edit to Runtime's code
  or schema.

### [invariants] What Runtime guarantees, and what observes each

| Tag | Guarantee | Observed by |
|---|---|---|
| `pure-position` | Position is a pure function of the declaration, the witnesses and the policy, the same in every mode. It is Flow's, and Runtime relies on it. | `next` |
| `named-acts` | Every act was named by `next`. An unnamed Workflow, Agent or transition call is refused, and so is a shell call outside the act's allowance. An unnamed agent inside an admitted script voids its act's witness. A stale epoch is refused at the commit queue and the lander at once, and at the dispatcher once its lease ref refreshes, within one node-tick period across nodes. | `binding`, `fencing` |
| `once-per-instance` | An item instance whose witness is current never runs again, and an unwitnessed one can always be dispatched again. Every command is idempotent or reconciles. | `relaunch`, `idempotence`, `act-ceiling`, `coverage` |
| `persisted-returns` | No result exists only in memory: every return is persisted through `record` before its item counts as done. | `spike`, `returns` |
| `no-model-context` | Neither the decider nor the supervisor holds model context. | by construction: both are programs |
| `one-door` | Records change only through `record`, instructions only through the instruction command, and main only through the lander. | `coverage` |
| `fail-closed` | Under `runtime.hook-failure=closed`, on every CLI version, a gated tool call in an act session runs only on the dispatcher's approval, since preflight refuses a launch whose settings allow a gated tool or add a second permission hook. Attended, either is warned about at session start. A dispatcher that cannot run leaves the call denied in an act session. An attended or unbound session's gated calls are judged as `runtime.attended-judge` says: by default it loads no ask rule, and auto mode's classifier or the person judges each (RT-4). Where the CLI carries `onFailure`, every enforcement entry fails closed too. Every event that cannot fail closed has a witness with a named reader. A bypass or an exception is journaled and re-checked, as K1 and K4 set. Under `open`, the class check reports the policy in force on every run. | `fail-closed`, `git-witness` |
| `no-skip` | No session the runtime launches skips permissions. | `no-skip` |
| `policy-and-journal` | Every runtime behaviour is a policy key with a reader, and every runtime event is journaled. | `coverage` |
| `grants-and-secrets` | An adapter acts only within the scopes it declared, its secret never leaves its process, and no push publishes a secret value; a journal is pruned past `runtime.journal`. | `grant`, `secret-scan`, `journal-retention` |
| `event-waits` | A wait on a record is woken by that record's event once per waiting party, runs under its own lease, and mints under the build's claim ref; a wait with no record raises one owner item past its ceiling. | `event-wait`, `lifecycle` |

### [contract] Runtime's layer contract

| Contract field | Runtime's entry |
|---|---|
| tag and definition | `layer.runtime`: asks Flow's position function through `next`, executes each answer through mechanisms it supervises, enforces at every boundary, and records that it did |
| instruction units | the act session's static block (make the one call your act names, nothing else); the supervisor's run rules; the compaction keep-list |
| engine kits | unattended: the supervisor (resume-tick grown, act sessions, the commit queue), whose verbs become `next`, `run` and the owner's controls; workflows: the role harnesses and the deferral block; hooks: the dispatcher, the fragments as packs through settings-merge, and check-wiring's class arm; process-monitor: reaping; and the journal grammar, moved from runlog into the core, so the core writes what observability reads |
| record kinds | return records, and act records (launch, epoch, outcome). Flow's witnesses and leases are written through `record` too |
| extension points declared | the eleven in `[extend]`, the memory-mirror point added by the owner's NT-14 |
| extension points used | none. Integrations fill the host, notification and memory-mirror adapters. Observability and memory's optional components register packs and read the journal |
| policies | the `runtime.*` keys in `[policies]`, and the existing keys it reads |
| gates | the build's fixtures in `[tests]`, the `grant`, `secret-scan` and `journal-retention` fixtures among them |

## [policies] Runtime's keys, set under the owner's delegation

The owner handed this layer to the main loop, so these defaults are the main loop's. Every one is
switchable, and the default is the `standard` preset's value. The six settled keys joined v2's catalogue
and presets on 2026-10-15, and v2 is canonical from then on. RT-2 retired `runtime.below-floor`, since
no floor exists. `runtime.journal` joined them on 2026-10-16 from the expansion round, and
`runtime.secret-home` and `runtime.secret-scan` from its review's fold, which moved them from
integrations because the grant they serve is Runtime's field.

| Key | Allowed values | Default | velocity | standard | strict | guarded |
|---|---|---|---|---|---|---|
| `runtime.spawn-backend` | in-session, headless, or a registered spawn backend | in-session, until the spike decides | in-session | in-session | in-session | in-session |
| `runtime.relaunch` | fresh, resume | fresh | fresh | fresh | fresh | fresh |
| `runtime.act-ceiling` | hours | 1.5 | 1.5 | 1.5 | 1.5 | 1.5 |
| `runtime.hold-ceiling` | hours | 6 | 6 | 6 | 6 | 6 |
| `runtime.hook-failure` | closed, open | closed | closed | closed | closed | closed |
| `runtime.attended-judge` | classifier-or-person, allowance, person | classifier-or-person (RT-4) | classifier-or-person | classifier-or-person | classifier-or-person | classifier-or-person |
| `runtime.attended-allowance` | a set of named tools and command patterns, read under `allowance` | none | none | none | none | none |
| `runtime.harnesses` | a set of named harness adapters | claude-code | claude-code | claude-code | claude-code | claude-code |
| `runtime.journal` | days, or all, bounded by v2's pair rule | 60 | 60 | 60 | 90 | 60 |
| `runtime.secret-home` | os-keychain, env-injected | os-keychain | os-keychain | os-keychain | os-keychain | os-keychain |
| `runtime.secret-scan` | value-gate, value-gate+shape-report | value-gate+shape-report | value-gate | value-gate+shape-report | value-gate+shape-report | value-gate+shape-report |

**Existing keys Runtime reads, without re-declaring them:**

| Behaviour | Key | Carrier |
|---|---|---|
| workspaces | `build.worktree` | v2's catalogue |
| where runs and cadence run | `run.host`, `maintain.host`, `kits.host` | v2's catalogue |
| the owner's channel | `notify.channel` | v2's catalogue |
| agents in flight | `runtime.agents-in-flight`, raised or lowered by the owner (revised 2026-10-19, the night pass two, point 7; it was `FANOUT_CAP`, lower-only, never above 5) | v2's catalogue |
| reaping | `PROCMON_REAP_MODE` | `.process-monitor.conf` |
| the relaunch cap and the turn cap | `RESUME_ATTEMPTS`, `RESUME_TURNS` | `.unattended.conf` |
| return retries | `roles.retries` | v2's catalogue |
| lease expiry | `leases.expiry-hours` | v2's catalogue |
| bypasses and exceptions | `hooks.bypass`, `core.bypass`, `core.exceptions` | v2's catalogue |
| attended context | `context.on-full`, `context.threshold` | v2's catalogue |
| owner questions | `run.on-owner-question` | v2's catalogue |
| the release wait: which builds wait, and its ceiling | `build.closes`, `build.release-ceiling` | v2's catalogue |

v2 says every key lives in `.governance/policy.toml`, but never says whether the kit confs fold into it.
That question is owed in v2's `[owed]`.

**Retired from the first draft:**
- `runtime.driver-lifetime` and `runtime.driver-refresh`, because one act session per act is structural;
- `runtime.cli-floor` and `runtime.below-floor`, because no floor exists (RT-2): every version fails
  closed through the permission baseline;
- `runtime.fanout`, `runtime.isolation`, `runtime.reap` and `runtime.scheduler`, because the existing
  keys above answer them;
- `runtime.journal` was retired here, because the run record is observability's. The expansion
  round restored it on 2026-10-16 as the journal's retention, now in the table above.

## [build] Runtime's own chain build

Settled by RT-3: the owner chose "Runtime takes `next` and the controls too".

- **The build:** `dWellOiledMachine`, a child of dBoundRoles and dTotalRecall, which are both children
  of dDeclaredLoop. It needs:
  - from dDeclaredLoop: the position function, the declarations, the guarded command, the hook factory
    and the lease grammar;
  - from dBoundRoles: the work-order renderer, the spawn marker and the return contract;
  - from dTotalRecall: `record`.
- **Its units, in order:**
  1. the spike (`[tests]` `spike`), before any other unit;
  2. the client surface:
     - the `next` verb over the position function, the `next —` micro-format, and the check that every
       declared command ends with one, with the readers of `--plan` and `--status` re-pointed:
       `model.py`, `stop-guard.js`, `unattended-build.js` and its template, `gen_build_index.py`, and
       the build and unattended skills;
     - the owner's controls, mapped onto unattended's verbs;
  3. the supervisor:
     - `resume-tick.sh` grown, started and restarted by the node tick;
     - the act's outcome record, written from the process's JSON result at exit;
     - act sessions, relaunch and its cap, limit holds and fencing;
     - command adapters that are idempotent or reconcile;
     - acting on the position function's answers;
     - writing the shared records itself;
  4. act binding and the epoch check, decided in the dispatcher's PermissionRequest entry, a runtime pack;
  5. the persisted-return store, and the deferral block;
  6. the slot reservation, under `runtime.agents-in-flight` (revised 2026-10-19, the night pass two, point 7);
  7. the enforcement surface:
     - the fragments as packs, settings-merge's dispatcher entries, and check-wiring's class arm;
     - the permission baseline: ask rules on gated tools, the dispatcher's PermissionRequest entry as the
       only allow path, and the allow-rule class check;
     - `onFailure: "block"` on every entry, its effect recorded per binary in the node registry;
     - the owner-pack table;
     - the witnesses and their readers;
     - signal traps on every git hook;
     - the trusted hooks copy;
     - lander hardening: the lander a versioned command adapter, with its dependency on the bar's kit
       declared;
  8. workspaces by `build.worktree`: the commit queue, integration, and the sweep;
  9. sessions: binding on every source, the resume card fix, the PreCompact flush, the keep-list, and
     the card's size check;
  10. the scheduler's host adapters, and per-period cadence witnesses;
  11. harness adapters with capability tables, with Codex's at its measured floor;
  12. the node registry's runtime facts;
  13. the journal grammar, moved into the core, with the supervisor and the dispatcher declared as
      producers.
- **What it takes from other builds.** Each moved phrase is quoted from the v2 `[chain]` row it left:

  | From | v2 text that moved | Gaps that moved |
  |---|---|---|
  | dDeclaredLoop | "the `next` verb over the loop's state, the `next —` micro-format, and the check that every declared command ends with one or declares itself terminal, laggards on a shrink-only list owned by their stage's build"; "the owner's pause, resume, withdraw and supersede through the guarded command"; "the executor launched where `run.host` says, its liveness its build lease's beat"; "a resume that delivers no card diagnosed and closed"; "the compact hook re-injecting the build's current card, never the kickoff's" | `gap-found-06`, `gap-flow-10`, `gap-tool-03`, `gap-orient-12`, `gap-orient-14` |
  | dScopedBuild | "worktrees by policy"; "parallel units' commits queued by the executor in the shared worktree" | `gap-conc-03` |
  | dShippedRelease | "lander hardening": a killed hook detected, hooks-path drift refused, and the lander kit versioned with its dependency on the bar's kit declared (walkthrough) | `gap-deploy-07` |

  `gap-found-06` ("No tool names the next step") and `gap-flow-10` follow the `next` verb and the
  owner's controls. The terminal states that `gap-flow-10` also names stay dDeclaredLoop's, and they
  land first, since that build is an ancestor.
- **What stays where it is, and what each of those builds gains:**
  - **dDeclaredLoop** keeps:
    - the position engine, which gains the closed answer set and instance keys (`[decide]`);
    - the guarded command, the terminal states and `deps.on-parent-withdrawn`;
    - the coordination feature (`gap-conc-01`, `gap-conc-02`), and the hook factory.
  - **dBoundRoles** keeps the return contract and its validation (`gap-roles-04`), and the spawn marker.
    Runtime runs both.
  - **dScopedBuild** keeps the exit contract and the core checks at Build's exit, and gains
    dWellOiledMachine as a parent.
  - **dTendedCadence** keeps its cadence, `gap-maint-01` and `gap-maint-07`. Its "three hosts and the
    cadence" became the cadence on Runtime's hosts, and it gains dWellOiledMachine as a parent.
  - **dShippedRelease** keeps the landing record, the landing queue it builds and the lander's core
    re-check (K1). Revised 2026-10-16: the turnstile is a bar semaphore, so no landing queue exists yet.
- **The chain's builds are v2's `[chain]` rows.** Revised: 2026-10-17: this line once counted
  fourteen, which v2 outgrew.
- **An ordering consequence.** Every stage build whose commands must end with a `next —` line now
  depends on dWellOiledMachine. v2's `[owed]` gives that ordering to the re-cut.
- **Retired or rewritten, each with its consumers:**
  - resume-tick's launch, and the arms in `resume-tick.test.sh` that assert its flag;
  - the unattended skill's CronCreate keepalive;
  - stop-guard's `session_crons`, and its block while a run is open, since an act session stops when its
    act is done;
  - the desktop durable-restart task (`RESUME_SCHEDULE_*`);
  - the DURABILITY writes in three harnesses;
  - `unattended-unit.js`'s `committed:false`.
- **A scoping fact.** UNATTENDED-PROTOCOL.md and the unattended skill sit at their size ceilings, so the
  build budgets its prose against those two size legs.

## [tests] Fixtures the build owes, each able to make the design lose

Each fixture names what turns it red, and `[invariants]` cites them by these tags.

- **`spike`**, the first unit. A `claude -p --json-schema` act session runs one role-typed Workflow
  `agent()` in the foreground. It is red if any of these fails:
  - SubagentStart and SubagentStop fire with `agent_type`;
  - SubagentStop fires for a Workflow agent, for an agent the owner stopped, for one failed after six stalls
    and for a killed session, each a red case of its own, since the in-flight ledger arms on them (the
    night pass two's review);
  - the persisted return byte-matches what `agent()` resolved to;
  - the session's `structured_output` carries the act's return;
  - on 2.1.292, an ask rule on the Workflow tool sends the call to the dispatcher's PermissionRequest
    entry, as dispatch 36 showed for Agent.

  The same act also runs through the headless backend. The cheaper feasible backend becomes the default
  for single-agent acts.
- **`next`:**
  - its answers are byte-identical on one build folder, attended and unattended, with `.unattended.conf`
    absent;
  - an empty frontier with all work terminal answers `terminal`, and one with work open answers `stuck`;
  - a corrupt witness answers `invalid-input`, naming its path;
  - a frontier holding only a hook item answers `awaiting`;
  - an unleased build waiting at `deploy.released` answers `awaiting`, and no lease ref is written;
  - a blocked item whose blocker is in flight raises no owner item until the blocker ends, then raises
    exactly one;
  - an unreadable lease ref answers `stale-remote`, and the item parks once `leases.expiry-hours`
    passes;
  - a failed check routed back to `entry.place` mints a new instance key and is dispatched again, while
    the old instance stays witnessed.

  The last four are each seen red against a stub supervisor.
- **`binding`:**
  - in an act session, each of these is refused when `next` did not name it: a Workflow call, an Agent
    call, a `--phase` transition and a Bash script;
  - an admitted script that calls `agent()` beyond its declared fan voids its act's witness;
  - the prompt-writer and role spawns inside the bound harness call are admitted;
  - on 2.1.292 in auto mode, with only the PreToolUse entry crashed (out of memory, and a missing path)
    and PermissionRequest healthy, an unnamed Workflow call and a stale-epoch call are each denied.
    It is seen red first against today's split, where PreToolUse alone binds;
  - under `runtime.attended-judge: classifier-or-person`, the owner's session loads no ask rule. A
    planted `rm -rf` of a scratch path reaches auto mode's classifier or the person, and the
    dispatcher never approves it. The arm is seen red first against the first text, under which the
    dispatcher approved it once the guard packs passed (RT-4);
  - under `allowance`, a call outside `runtime.attended-allowance` goes to the person. Under
    `person`, every gated call does, and an unbound headless session's is denied;
  - declaration coverage is measured separately, over the main-session transcripts: every Workflow,
    Agent and Bash act, with hook-issued verbs excluded. It is seen red first on session b710e9c3's 17
    inline workflows, and its population is asserted non-empty.
- **`relaunch`:** kill a review fan's act session after some of its agents return. The fresh relaunch
  spawns only the agents without a persisted return, checked by spawn counts and the journals'
  `totalTokens`. With SubagentStop disabled, the relaunch follows `runtime.relaunch`. A five-agent fan
  killed after two returns respawns exactly three agents, each for a named spawn site.
- **`limits`:**
  - in a partial fan where some of k agents return null, the returns persist, the nulls become
    `deferred-platform`, and the relaunch re-pays only the nulls;
  - on a StopFailure limit record, the supervisor parses the reset time, holds, renews its lease, and
    raises an owner item once `runtime.hold-ceiling` passes.
- **`in-flight`:**
  - with `runtime.agents-in-flight` at 3 (`FANOUT_CAP=3` until the night pass two's point 7), the supervisor queues an act whose declared fan exceeds the free slots, and the
    attended PreToolUse entry queues the same call (the owner's NT-28);
  - killing an act session that holds slots releases them once the reap runs;
  - an attended Workflow call's slots are freed when its run ends, and a dead session's by the sweep;
  - with the limit at 3, two direct spawns and a two-agent Workflow admit one Workflow agent until a slot
    frees, and a three-agent Workflow under a limit of 5 still admits two direct spawns (the night pass
    two's review).
- **`returns`:**
  - a schema-forced agent's persisted return byte-matches what `agent()` resolved to;
  - a payload whose final text is valid JSON, while its `StructuredOutput` call is not, is refused;
  - a malformed or oversized return is held `roles.retries` times, then persisted as a refusal;
  - a SubagentStop entry pointed at a missing path leaves the item unwitnessed and re-dispatchable.
- **`fail-closed`:**
  - on 2.1.292, with no switch, every burst failure class in the dispatcher leaves a gated call denied in
    an act session, read-only commands included. Dispatch 36's probes are the seed;
  - on 2.1.295 and later, the same replay under `onFailure: "block"` refuses every repo-wired entry,
    ungated tools included;
  - in an attended 2.1.292 session, a missing dispatcher puts a gated call to the person and never runs
    it. Dispatch 36 could not run this case, because it needs a terminal;
  - an allow rule matching a gated tool fails the class check, and so does a settings file with the
    PermissionRequest entry removed;
  - a crashed SessionStart dispatcher makes the first gated call refuse, planted as a Bash or Workflow
    call;
  - kill the PermissionRequest host after its first healthy answer in a running act session, and the
    next gated call is denied. It is seen red against a stub that admits;
  - a dead dispatcher refuses the exception-record call, and the repair is recorded from outside the
    agent;
  - a user-level `Bash(*)` allow rule, and a user-level always-allow PermissionRequest hook beside a
    crashed dispatcher, each refuse an act session's launch at preflight and are warned about
    attended. So does an always-allow PermissionRequest hook in an enabled plugin, planted beside a
    crashed dispatcher. Each is seen red first;
  - under `runtime.hook-failure=open`, every run's journal and the class check's output name the
    policy in force, seen red when that line is dropped;
  - a `hooks.bypass` commit and a `core.exceptions` entry each leave a journal line, and the lander's
    re-check reports the bypass;
  - the burst's user-level guards are reported, not counted.
- **`workspaces`:**
  - under per-unit, two units commit concurrently in their own worktrees, and after release the build
    branch holds every unit's commits;
  - release is refused while a unit branch holds an unmerged commit;
  - under shared, two disjoint passes commit through the queue with no index lock;
  - in a run that touches shared records, only the supervisor writes them;
  - a dirty worktree and a foreign temp directory survive the sweep;
  - an edited `.githooks` in a worktree does not run;
  - on a node registry whose `autocrlf` differs from the tree's, a fresh worktree is clean and
    `--preflight` passes.
- **`sessions`:**
  - a `fork` and a resume each deliver the card;
  - a PreCompact hook flushes an item's work before an automatic compaction;
  - after a manual compaction, the summary names the build, the item and the open asks;
  - the card stays under the re-attachment cap.
- **`cadence`:** node A runs a period's item, and node B, waking late, skips it. A missed period runs at
  the next wake. Two supervisors released together on one period make one run and one witness.
- **`act-ceiling`:** a stub act session sleeping past a lowered `runtime.act-ceiling` is reaped,
  journaled and relaunched under the cap.
- **`grant`:** an adapter whose granted scope is wider than its declared one is refused at registration,
  seen red on a probe stubbed to accept it.
- **`journal-retention`:** under `runtime.journal: N`, entries planted at N-1 and N+1 days: the node
  tick prunes the older and keeps the younger, and under `all` it prunes nothing. It is seen red
  against a pruner stubbed to delete everything.
- **`secret-scan`:** one plant per population `[extend]` names: a removed commit, a tracked file, a
  `memory/` record, a mailbox ref written after the landing, a card ref, a lease ref and a claim ref at
  the push boundaries, and the journal and a transcript at the node tick, with one encoding of the
  value among them. Each plant turns its boundary red. Four witness cases are each seen red against a
  scanner stubbed to return zero: an unresolved value reads a dead probe and blocks; a prepare whose ref
  update carries commits, its scanner's enumerator stubbed empty, reads a dead probe; a node tick whose
  enumerator returns nothing while a journal entry changed reads a dead probe; and an `anonymous`
  adapter reads not applicable. A
  code-only landing and a lease-only push, whose expected populations hold no `memory/` path and no
  mailbox, card or claim object, both read green.
- **`event-wait`:** under `close-only`, unlease a build, then write the release slot's exit record:
  the wake runs `deploy.released` and `deploy.close` under its instance's cadence lease, the close
  minted under the claim ref. Two builds landed at two SHAs, both contained in a later SHA, both close
  on one exit record for that later SHA. A held pass, then a verified pass over the same SHA, closes
  the build on the second exit record. With no exit record, one owner item opens once
  `build.release-ceiling` passes, and only one; a wait still under the ceiling, or answered before it,
  opens none; after the owner keeps waiting, a second ceiling opens a second item; and an item a
  withdraw already opened is not opened again. Each case is seen red against a supervisor stub that
  keys the wake by SHA alone and raises the ceiling's item without looking for an open one.
- **`lifecycle`:** a pause of a landed build is refused; a withdraw of a landed build at
  `deploy.notify` under `at-landing` is refused; a withdraw of a build waiting at `deploy.released`
  opens the release hold's one owner item; and after `deploy.unlease`, a withdraw runs under its
  request's wake. Each is seen red against a stub `life.quiesce` that sends every withdraw to
  `life.notify`.
- **`extension`:**
  - a stub harness adapter registers with no edit to Runtime's code or schema;
  - the owner-pack table and `settings.json` are compared both ways, seen red on an entry with no row
    and on a row with no entry;
  - Codex's capability table is checked against the dispatcher's required events, PermissionRequest
    among them;
  - a crashing Codex hook is refused, or recorded as one that cannot be.
- **`start-cost`:** a lean act session's first turn on Windows stays under the 84k-token median of a
  fresh session. If it is red, the remedy is a leaner launch, since one session per act is structural.
- **`no-skip`:** a class check over every launcher's argv fails on `--dangerously-skip-permissions`. It
  is seen red on today's `resume-tick.sh:385`.
- **`fencing`:** run across two nodes, or with the old act session outside the killed tree. Kill only the
  supervisor mid-act, and let a second supervisor take over with a new epoch. Until the old node's tick
  restarts a supervisor, the old act session's gated calls are approved in its own workspace, and its
  commit and push are each refused, the refusal the one in its journal. Once the restarted supervisor
  reads the take-over, it kills the old session, and a gated call made after the refresh is refused.
  One witness and one commit result. Revised 2026-10-17, the folds' closing review: this fixture once asserted the next gated call refused at once.
- **`idempotence`:** kill the supervisor after the lander's push and before its witness. The take-over's
  reconcile probe finds origin at the expected sha, and nothing pushes twice.
- **`relaunch-cap`:** a stub CLI that always exits at `--max-turns` parks the item after
  `RESUME_ATTEMPTS` launches, with a journaled reason and an owner item.
- **`host`:**
  - kill the supervisor, then reboot the node, and the node tick restarts it within one period;
  - preflight refuses a run-host node without the tick's registration.
- **`binary`:** with a stub `claude` printing 2.1.292 first on PATH, the supervisor launches it, records
  in the node registry that `onFailure` has no effect on it, and journals that. The entries still carry
  the key, and a gated call made while the dispatcher is missing is still denied.
- **`git-witness`:** a SIGKILL to pre-commit lands no witness. The supervisor does not count that commit
  item done, and the lander reports the commit. TERM and INT sent mid-run to pre-commit, commit-msg,
  pre-rebase and pre-push each make the hook exit non-zero and leave no witness, seen red first on
  today's pre-commit.
- **`coverage`:**
  - re-running the supervisor on a witnessed item dispatches nothing;
  - a direct write to a record, to an instruction file and to main is each refused;
  - an act session started in the primary tree is refused;
  - every `runtime.*` key in v2's catalogue, a population asserted non-empty, has a reader call site in
    dWellOiledMachine's code, found through the one policy reader's key registry. It is seen red on a
    planted catalogue key with no reader;
  - every event class leaves a journal line.
- **`latency`:** ten dispatcher runs on a benign Bash payload. The first measurement's p50, against
  today's 57 ms, sets the dispatcher's declared budget. From then on the fixture is red when the p50
  exceeds it, seen red once against a dispatcher stub with an injected sleep.

## [gaps-proposed] Gaps, registered 2026-10-15

The register (`build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md`) is canonical. It holds a new
area, `Runtime`, keyed `gap-rt-NN`, and dWellOiledMachine owns every one:

| Key | Sev | Gap |
|---|---|---|
| `gap-rt-01` | HIGH | a model session decides every next act |
| `gap-rt-02` | HIGH | every enforcement hook fails open |
| `gap-rt-03` | HIGH | spawned work dies with its session |
| `gap-rt-04` | HIGH | the headless resumer skips permissions |
| `gap-rt-05` | MED | fan-out is bounded per prompt, not in flight |
| `gap-rt-06` | MED | workspaces are neither allocated nor reclaimed |
| `gap-rt-07` | LOW | session hooks miss events |
| `gap-rt-08` | LOW | node facts go unrecorded |
| `gap-rt-09` | LOW | gov wires none of Codex's hook events |
| `gap-rt-10` | LOW | runtime records contradict the code |

**Two proposed gaps were not registered.** They restated rows the register already held:
- "no declared cadence item runs out of session" is `gap-maint-01`;
- "supervision reaps only by hand" is `gap-maint-07`'s third clause.

Both rows took the corrected facts instead. dTendedCadence keeps both, and Runtime's scheduler and beat
close them, since dWellOiledMachine is now its parent.

**Registered gaps that take a fix designed here,** with their owners after RT-3:
- `gap-roles-04` (returns uncontracted): dBoundRoles;
- `gap-conc-02` (claims never age): dDeclaredLoop;
- `gap-found-06`, `gap-flow-10`, `gap-tool-03`, `gap-orient-12`, `gap-orient-14`, `gap-conc-03` and
  `gap-deploy-07`: moved to dWellOiledMachine;
- `gap-maint-01` and `gap-maint-07`: dTendedCadence.

The trusted hooks copy also fixes what the open ask TOOL-aWeldedTribunal-10 asks for. That ask's status
is unchanged.

## [reviews] The two Tier-2 rounds, folded

- **The rounds.** The owner asked for two independent medium-effort rounds, and both ran on blob
  `767187aa`:
  - run A, in `reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-a.md`: 56 of 60 findings confirmed;
  - run B, in `reviews/2026-10-15-review-PLAY-dClosedLoop-1-runtime-b.md`: 57 of 61 confirmed.

  Both returned CLEAN WITH FIXES.
- **The map.** `build/2026-10-15-build-PLAY-dClosedLoop-1-runtime-reviews-compared.md` places every
  finding on one of 59 defects, and names where each defect is folded above.
- **Re-read rather than taken whole:**
  - **`hookspath`.** Run A read today's absolute path as the decided position, and run B read it as the
    defect. WIRE-INTO-PROJECT's documented position, an out-of-tree copy under the git common dir,
    settles it (`[enforce]`).
  - **`next-readers`.** Run A confirmed this defect, and run B's skeptic refuted it as unit-level. With
    the `next` verb moved to Runtime (RT-3), re-pointing its readers is Runtime's client-surface unit
    (`[build]`).
  - **`permission-mode`.** The owner's ruling, TOOL-aMendedFleet-116, is applied rather than re-asked.
- **The refuted findings.** All eight stand refuted. A45's size ceilings are kept as a scoping fact in
  `[build]`.
- **The fold itself is unreviewed.** The declared spec audit of PLAY-dClosedLoop-1 will review it.

## [questions] To put to the owner

- **RT-1.** `context.on-full`, for attended sessions:
  - the owner's CX-1 answer assumed that a resume is cached input;
  - measured, a resume's first turn is 503k tokens, mostly cache creation;
  - a compaction reads about 970k cached tokens and takes about 117 s;
  - a fresh start's first turn is 84k.

  Act sessions read neither key.
- **RT-2.** `runtime.below-floor`, narrowed by the fold. The supervisor first launches any binary at or
  above the derived floor, and on node d the desktop's 2.1.295 qualifies. The question is what happens
  on a node with no such binary. The provisional answer is refuse.
- **RT-3.** dWellOiledMachine, and the chain edits in `[build]`.
- **RT-4,** asked 2026-10-17 from the folds' closing review's H1: who judges an attended or unbound
  session's gated calls (`build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews.md` `[answers]`).

## [answers] The owner's answers, 2026-10-15

- **RT-1:** "Fresh at an item boundary (Recommended)".
  - `context.on-full` now defaults to `fresh-at-boundary` in every preset, in v2.
  - The option read: "The default becomes `fresh-at-boundary`. Once `context.threshold` is crossed,
    the session ends at the next item boundary, and a fresh one reorients from the card and the keyed
    records."
- **RT-2:** the owner chose neither option and wrote, verbatim: "Reverify that this version or above is
  actually needed. Older claude binaries should be perfectly capable running the same functionality
  without refusal/degradation."
  - Dispatch 36 re-verified it in `build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-floor.md`, with its probes beside it.
    - The switch is new in 2.1.295, and 2.1.292 ignores it without a warning.
    - But 2.1.292 already fails closed on gated calls, when one PermissionRequest hook answers an ask
      rule on each.
  - The owner was right: no floor is needed.
    - `[enforce]` now fails closed on every version through that baseline, and adds the switch where
      the CLI carries it.
    - No version is refused.
    - `runtime.below-floor` and the derived floor are retired.
  - Two cases are untested and stay as losing tests in `[tests]`: an attended 2.1.292 session's
    fallback to the person, and a permission host that crashes mid-run.
  - **Revised: 2026-10-17, the debt round.** `[tests]` `fail-closed` now holds both cases. The
    mid-run case had no arm until this fold.
- **RT-3:** "Runtime takes `next` and the controls too", not the recommended option.
  - The `next` verb, its micro-format and the owner's controls moved to dWellOiledMachine, with
    `gap-found-06` and `gap-flow-10`.
  - dDeclaredLoop keeps the position function.
  - `[build]` holds the settled re-cut.
- **RT-4,** 2026-10-17: "Classifier or you (Recommended)".
  - `runtime.attended-judge` defaults to `classifier-or-person`. `allowance` and `person` are its
    allowed values, and `runtime.attended-allowance` is the list `allowance` reads.
  - Only act sessions load the permission baseline, as an extra settings source at launch.
  - Attended sessions work as today: their guard packs refuse, and auto mode's classifier or the
    person judges each gated call.
  - The cost, as the option stated it: on a CLI older than 2.1.295, a crashed guard in an attended
    session no longer blocks, so the call reaches the classifier without that guard's check.
  - `[act]`, `[enforce]`, `[policies]` and `[tests]` carry it.

**Revised 2026-10-16, after the expansion round's two reviews**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-a.md` and `-b.md`): `[extend]`'s selecting
keys keep their validation clause and name every key that takes registered names; Runtime enforces
the grant on every adapter row and runs the secret value scan over everything a push publishes;
`[schedule]` names `kits.host` and journal retention; and `[policies]` carries `runtime.journal`,
`runtime.secret-home` and `runtime.secret-scan`. The comparison record's `[folded]`
(`build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md`) names each defect and
where it went.

**Revised again, 2026-10-16, after the fold's closing review**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold.md`): `[extend]` holds the one list of
keys that take registered names, `release.environments` among them; the secret value scan binds at the
lander's prepare and at the core's ref-push path, and scans the journal and transcripts as a node-local
population; `[schedule]` runs an item's event wait under its wake's own lease; and `[tests]` and
`[invariants]` gain the `grant`, `secret-scan` and `journal-retention` fixtures. The comparison record's
`[closing-review]` names each item and where it went.

**Revised a third time, 2026-10-16, after the follow-up round** (`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-followup.md`): the
event wait fans out per waiting build and mints under the claim ref, the supervisor's sweep raises a
wait past `build.release-ceiling`, the secret scan's boundaries declare their expected populations, and
`[tests]` and `[invariants]` gain `event-wait` and a two-sided `journal-retention`. The comparison
record's `[follow-up]` names each item and where it went.

**Revised a fourth time, 2026-10-17, after the debt round's runtime-fold pair**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-runtime-fold-a.md` and `-b.md`): act binding and the
epoch check are decided in the dispatcher's PermissionRequest entry, the one that fails closed below
2.1.295; returns are keyed per spawn site; the epoch's reading is stated, with one name per lease;
PermissionRequest joins the events and the owner-pack table; `onFailure` is written on every entry;
`next` gains `awaiting`; and every claim the pair found untested gains its fixture arm. The debt
comparison record's `[fold-runtime-fold]` names each defect and where it went.

**Revised a fifth time, 2026-10-17, after the debt round's expansion pair**
(`reviews/2026-10-16-review-PLAY-dClosedLoop-1-expansions-fold-round3-a.md` and `-b.md`): the sweep
opens the release hold's one owner item only when none is open, and restarts its ceiling after a
keep-waiting answer; a wake is keyed by the exit record's id, so a second pass over one SHA wakes it
again; an owner request on an unleased build is an event wake; each secret-scan population takes its
expectation from a source the scanner does not enumerate, the node tick's included; the reader table
lists the release keys the sweep reads; and `[tests]` gains a fuller `event-wait` and a `lifecycle`
fixture. The debt comparison record's `[fold-expansions-fold-round3]` names each defect and where it
went.

## [revised-night] Revised 2026-10-18, the night pass

The owner's point 1 (`build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md` `[p1-unattended]`): unattended is the default state, and attendance changes only the
owner's interactions, never the flow or role use. Amended in place:
- `[terms]`: the supervisor is the driver in every mode, and the owner's session is its client;
- the diagram, `[decide]`'s `run <build>` and its clients: the owner's session hosts the driver only until
  dWellOiledMachine lands, or if its platform spike fails, under its owner binding, each role act it hosts act-bound
  with that act's epoch (the closing review's M6), and `/unattended` retires with the kit;
- `[act]`: the owner's session is bound the same way for every role act it hosts, and its binding record reads
  "owner", since attendance is a mode and not a kind of session. Its design text says "the owner's session" for what
  it called an attended session; `runtime.attended-judge` and `runtime.attended-allowance` keep their names until the
  lexicon settles the term (gap-lex-09).

The night pass's other runtime additions are units in v2's dWellOiledMachine row: the attend and unattend controls,
the `step —` announcement, intake for a prompt that reaches no owner session, the browser capability and the visual
capture adapter, the default load replayed at a compaction with `next`'s line, compactions journaled, and a hook
pack's refusal text checked.
