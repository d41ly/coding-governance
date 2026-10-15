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
