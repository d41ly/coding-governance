# TOOL-dWellOiledMachine-7 — act binding and the epoch check at the Workflow, Agent and shell call, decided in the dispatcher's PermissionRequest entry, with in-script spawns declared and reconciled

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 32 · advances TOOL-dWellOiledMachine-62

**Carries:** cl-dClosedLoop-0285@d2c4cd28 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-1-reuse-scout-a.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-56 |
| [2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dWellOiledMachine-8-spec-stage-returns.md) | journal | TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-59 |
| [2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dWellOiledMachine-1-spec-brief.md) | research | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 |
| [2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 |

<!-- /gen:spec-records -->

## 1. Goal

Work is bound to no checklist item: one session improvised 17 inline workflows and another more than
25 ad-hoc scripts (gap-rt-01, gap-orient-08), and today's PreToolUse guard checks a call's role and
task digest but neither the act nor an epoch (`tools/hooks/agent-cap.js:1735`). This unit binds every
gated call of an act session to the one call its act names and to the epoch the node holds, decided in
the dispatcher's `PermissionRequest` entry, the one entry that fails closed on the pinned binary,
repeated at `PreToolUse` to refuse early; and it reconciles the agents an admitted script spawned,
which no hook sees, against what the harness declares (layer-runtime `[act]`, :495-540).

## 2. Scope (IN)

- **S1** — The named call. `write_named_call(act, build, work_order)` in the new
  `tools/runtime/act_binding.py` writes `<git-common-dir>/gov/acts/<act>.named.json` once, before the
  act session starts: `act`, `build`, `tool` (`Workflow` when the work order carries `script`, else
  `none`, the headless form), `target` (the script's path from the repository top), `workflow` (the
  `tools/roles/workflows.toml` entry whose `harness` names `target`, read through `load_workflows`,
  `tools/roles/roles_lib.py:364`), `args-sha` (the first 12 hex of the SHA-256 of the args' JSON,
  sorted keys and compact separators, `returns` left out), `task-sha` and `allow`, the work order's
  list of permission-rule entries, empty where it carries none. It returns the harness args with
  `act` added, which `supervise.py` passes unchanged at each S4 launch of TOOL-dWellOiledMachine-6, so
  the args the act names and the args it hashes are one object. Observed by AC1.
- **S2** — The epoch the node holds. `supervise.py` writes `epoch: <n>` into its pid file
  `<git-common-dir>/gov/supervisors/<slug>.pid` at start and at each beat's fence read, and clears the
  file when the fence moves (TOOL-dWellOiledMachine-6 S1, S7). `read_held_epoch(slug)` returns that
  value, or `none` when no pid file names one. Observed by AC2.
- **S3** — The facts, read once per call. `python act_binding.py facts <session id> <act>` prints one
  JSON object: the session binding's `act` through `session_binding.py read`
  (TOOL-dWellOiledMachine-12 S2), the act's binding through `read_binding`
  (TOOL-dWellOiledMachine-39 S6) with its source, `read_held_epoch` for the named call's `build`, the
  named call, and whether `<act>.admitted` exists. Observed by AC2, AC3.
- **S4** — The decision, `resolveActCall(payload, facts)` in the new `tools/runtime/act-binding.js`,
  for a session whose launch environment carries `GOV_SESSION_KIND=act` and `GOV_ACT`; in any other
  session it makes no decision. In order, the first rule that applies answers:
  1. a session binding that is absent or names another act: `deny`, since a crashed SessionStart must
     refuse the first gated call;
  2. a binding that reads `not-local` or `malformed`, or whose `epoch` differs from the held epoch:
     `deny` for every gated tool, subagents' calls included;
  3. a call whose payload carries `agent_id`, made by an agent inside the admitted call: `allow`, the
     guard packs having judged it at `PreToolUse`;
  4. a main-loop `Workflow` call: `allow` once, when `tool` is `Workflow`, `scriptPath` resolves to
     `target`, `args.act` is the act and the args hash to `args-sha`, the first `allow` creating
     `<act>.admitted` exclusively; otherwise `deny` naming each field that differs;
  5. a main-loop `Agent` call: `deny`, since no act names one;
  6. a main-loop `Bash` or `PowerShell` call: `allow` only when an `allow` entry matches it, matched
     by the dispatcher's own permission-rule matcher (TOOL-dWellOiledMachine-10 S8), else `deny`;
  7. a main-loop `Write`, `Edit`, `MultiEdit` or `NotebookEdit` call: `allow` when `tool` is `none`,
     where the act session is the role agent, else `deny`.
  Each deny is `BLOCKED by act-binding: <rule> · <act> · <what differs>`. Observed by AC2 to AC5.
- **S5** — The packs. `tools/runtime/act-binding.fragment.json` registers
  `act-binding.js PermissionRequest` (I9: class `refuse`, failure `closed`, `budget-ms` 5000, key `none`) with the
  gated tools of `tools/runtime/baseline.settings.json` as matcher, so its `allow` or `deny` is the
  dispatcher's answer (TOOL-dWellOiledMachine-10 S8); `act-binding-early.fragment.json` registers
  `act-binding.js PreToolUse` with the same matcher, class `refuse`, failure `open`, which answers
  only S4's denies, never allows, and never creates `<act>.admitted`, so a crashed `PreToolUse` opens
  no path. `act-binding.js` reaches S3 through `pyrun.sh` (TOOL-dWellOiledMachine-8 S3) and exports
  `resolveActCall`. Observed by AC4, AC6.
- **S6** — In-script spawns declared. An admitted harness's declaration is its `workflow` entry's stage
  rows, each naming its `role` and `fan` (TOOL-dBoundRoles-22 S1), read through `load_workflows`. A
  harness with no stage rows declares no spawn. Observed by AC7.
- **S7** — Reconciled at the act's end. `python act_binding.py reconcile <act>` reads the act
  session's Workflow run directories through `resolve_session_tree` (`tools/runlog/extract.py:266`),
  each run's agents through `load_run_journal` (`tools/roles/handoff.py:686`) and each agent's
  `agentType` from its `.meta.json`. It answers `void` when an agent's type is no stage's role, when a
  role's agents outnumber the sum of its stages' `fan`, or when the session holds more than one run;
  else `clean`. It prints `reconcile — <act> · <clean|void> · <n> agent(s) · <reason>`.
  `supervise.py` runs it before each `act-exit` line and writes `witness=void` on a void, so the act's
  commits are never counted as its item's witness and the item re-runs. Observed by AC7.
- **S8** — `help/runtime.md` gains act binding, the named call, the held epoch, the seven rules and
  the reconcile. Observed by AC8.

## 3. Non-goals (OUT)

- Binding a call to the resolved shape's digest and the shape-run row: TOOL-dWellOiledMachine-19
  extends S4 and S7.
- The count of `agent()` calls between the journal's entries, which no hook sees: stated unchecked by
  the layer (`[act]`), and S7 reads what the platform journaled.
- An attended or unbound session's gated call: `runtime.attended-judge`'s, TOOL-dWellOiledMachine-10.
- Journaling each refusal and counting repeats: TOOL-dWellOiledMachine-49's breaker, over I11.
- Rendering the work order's `allow` list: dBoundRoles' work-order renderer (TOOL-dBoundRoles-3); an
  act with none admits no main-loop shell call.
- The owner's session hosting a role act under its owner binding: TOOL-dWellOiledMachine-25, the only
  driver, launches every act through the supervisor.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-10` — `dispatch.js`, whose `PermissionRequest` run the act-binding pack registers on, and its permission-rule matcher
- **consumes-from** `TOOL-dWellOiledMachine-39` — `refs/gov/bindings`, the act's binding and its `epoch`, read through `read_binding`
- **consumes-from** `TOOL-dWellOiledMachine-12` — `session-bindings`: S4's first rule reads the caller's binding through `session_binding.py read`
- **consumes-from** `TOOL-dWellOiledMachine-6` — `supervise.py`, which writes the named call at launch, the held epoch at each fence read, and runs the reconcile before `act-exit`
- **consumes-from** `TOOL-dWellOiledMachine-8` — `pyrun.sh`, through which `act-binding.js` reads its facts
- **hands-off** `TOOL-dWellOiledMachine-25` — `act_binding.py`'s `write_named_call`, `read_held_epoch` and `resolveActCall`, which the only-driver unit calls and extends for a call the owner's session hosts
- **hands-off** `TOOL-dWellOiledMachine-19` — `act_binding.py`, whose call check and reconcile that unit extends with the shape digest and the shape-run row
- **consumes-from** external — TOOL-dBoundRoles-22's stage rows and `load_workflows`; TOOL-dBoundRoles-3's work order and its `allow` list
- **hands-off** `TOOL-dWellOiledMachine-66` — the act-binding packs and `act-binding.js`'s denies, which that unit gives refusal rows and `rule —` lines (finding 5)

## 4. Design

### Evidence

- No `PermissionRequest` entry exists (`git grep PermissionRequest -- tools` is empty at this base),
  and the one spawn check is `PreToolUse` on `Workflow|Agent` (`.claude/settings.json:3-9`).
- `checkHarnessCall` resolves a `scriptPath` against the declared harnesses
  (`tools/hooks/agent-cap.js:1735`), the rule TOOL-dBoundRoles-25 S2 moves into
  `tools/roles/spawn-guard.js`; S4's fourth rule resolves `target` the same way.
- A Workflow run's agents are journaled by the platform in `journal.jsonl`, one `started` line per
  agent, and each agent's type is in its `.meta.json` (measured on this node on 2026-10-26, run
  `wf_7c0507f0-43d`; PINNED, re-measured by TOOL-dWellOiledMachine-1's spike).
- Only `PermissionRequest` fails closed below 2.1.295 (layer-runtime `[enforce]`), so the deciding
  entry is that one and the `PreToolUse` twin only refuses early.

### The decision, per caller

| Caller | Workflow | Agent | Bash, PowerShell | Write family |
|---|---|---|---|---|
| act session, `tool = Workflow` | the named call, once | deny | `allow` list | deny |
| act session, `tool = none` | deny | deny | `allow` list | allow |
| agent inside the admitted call | allow | allow | allow | allow |
| any session, stale epoch or no binding | deny | deny | deny | deny |
| attended or unbound session | no decision | no decision | no decision | no decision |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `act_binding.py` with `facts`, `reconcile`, `--fixture` | runtime kit file | none |
| `write_named_call`, `read_held_epoch` | Python functions | `write`, `read`, OK |
| `act-binding.js`, `resolveActCall` | runtime kit file, JS function | `resolve`, OK |
| `act-binding.fragment.json`, `act-binding-early.fragment.json` | hook packs | none |
| `<act>.named.json`, `<act>.admitted` | node-local files | none |

### Files touched (estimate)

- `tools/runtime/act_binding.py`, `tools/runtime/act-binding.js`,
  `tools/runtime/act-binding.fragment.json`, `tools/runtime/act-binding-early.fragment.json` (new)
- `tools/runtime/supervise.py`: the named call at launch, the pid file's `epoch`, the reconcile
- `tools/runtime/dispatch.js`: the permission-rule matcher exported
- `tools/runtime/kit.toml`
- `help/runtime.md`

### Alternatives rejected

- **The epoch read from the lease ref at each call.** `read_claims` fetches the remote
  (`tools/unattended/unattended.sh:2118`), and a second parser of the lease record is what
  TOOL-dPlacedRequest-1 S2 refuses; the supervisor already re-reads the lease each beat and dies with
  its fence.
- **SubagentStart and SubagentStop journal lines as the reconcile's population.** The platform's
  `journal.jsonl` already names every agent an admitted script started, including one whose stop
  never fires.

## 5. Production-readiness checklist

- security — deny by default in an act session: no binding, a stale epoch, an unnamed call or a shell
  command outside the act's list is refused; the deciding entry fails closed; the early twin can only
  refuse.
- perf / scale — one Python start per gated main-loop call in an act session, about 0.3 s on this
  node, UNVERIFIED; nothing runs outside act sessions.
- error / empty / loading states — a missing named file denies; a missing run directory reconciles
  `clean` with 0 agents, since the act made no call.
- observability — every deny names the rule, the act and the differing field; every reconcile prints
  one line the supervisor journals.
- risks — a fence moved on another node while this node's supervisor is dead admits calls at the old
  epoch until the node tick's reconcile kills the act (TOOL-dWellOiledMachine-6 S6); stated, not closed.
- testing — the fixture cases of §6 and the arms of §7.
- migration — none: attended sessions are untouched, and only acts the supervisor launches are bound.
- user docs — `help/runtime.md`.

## 6. Acceptance criteria

The fixture is `python act_binding.py --fixture --plant <case>`: a scratch repository under `%TEMP%`
with a short name, a session binding, a binding ref, a supervisor pid file, a named call, and a
payload piped through `node act-binding.js <Event>` with `GOV_SESSION_KIND=act` and `GOV_ACT` set.

- **AC1** — When `--plant named` runs `write_named_call` for a Workflow work order, the named file
  carries `tool` `Workflow`, the script's `target`, its `workflow` and a 12-hex `args-sha`; for a work
  order with no `script` it carries `tool` `none`.
  Red when: a field is missing or `returns` changes `args-sha`.
- **AC2** — When `--plant stale-epoch` moves the pid file's `epoch` past the binding's, a main-loop
  `Bash` call inside the `allow` list and a subagent's `Edit` are each denied naming `stale epoch`;
  with the pid file removed, each is denied too.
  Red when: any gated call is allowed under a stale or absent epoch.
- **AC3** — When `--plant no-binding` deletes the session binding, the first `Workflow` call is denied
  naming `no binding`.
  Red when: an unbound act session's call is allowed.
- **AC4** — When `--plant named-call` sends the named `Workflow` call twice, `PermissionRequest`
  allows the first and creates the admitted marker, and `PreToolUse` denies the second; a call to
  another declared harness, one with `args.act` changed and one with an extra argument are each denied
  naming the field.
  Red when: an unnamed or repeated call is allowed.
- **AC5** — When `--plant shell` sends `Bash` with `git status` against an `allow` of
  `Bash(git status:*)` it is allowed, `Bash` with `rm -rf x` is denied, and an `Agent` call is denied.
  Red when: a command outside the list runs.
- **AC6** — When `--plant early-crash` makes the `PreToolUse` twin exit 1 on an unnamed `Workflow`
  call, the `PermissionRequest` pack still denies it; and the twin never answers `allow` on any plant.
  Red when: a crashed early entry admits the call, which is today's split where `PreToolUse` alone binds.
- **AC7** — When `--plant reconcile` plants a run whose agents match its stage rows, the reconcile
  prints `clean`; with one extra agent of a declared role past its `fan`, one agent of an undeclared
  type, or two run directories, it prints `void` naming each, and
  `supervise.py --fixture --plant void-exit` writes `act-exit` with `witness=void`.
  Red when: an undeclared agent leaves the witness standing.
- **AC8** — When `grep -n "act binding\|held epoch\|reconcile" runtime.md` runs over the help page,
  each is named.
  Red when: the page omits one.

## 7. Gates

`check-wiring self-test` · `lexicon naming predicates` · `policy fixtures` · `memory hygiene`

The broad guard `{prefix}/` leaves the line by the checker's floor; the bar at the close runs it.

New arm: tools/runtime/act_binding.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · each plant staged against a decision with the epoch compare removed, the admitted marker removed, and a reconcile that reads no `.meta.json` · none
New arm: tools/runtime/supervise.py · covers AC7 · the void-exit plant staged against a supervisor that skips the reconcile · none

## 8. Open questions

- **F1 — Which epoch is "the lease's" at a call?** (a) The epoch the node's supervisor last read at
  its fence, from its pid file; (b) the lease ref read at each call through `read_claims`, which
  fetches the remote. (b) puts a network fetch on every gated call and adds a lease reader beside the
  one parser. Rung 3, the option meeting every criterion with the fewest open questions; its limit is
  §5's risks line. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — Where is the decision written?** (a) In JavaScript beside the dispatcher, with one Python
  read of the facts per call; (b) wholly in Python. (b) needs a second copy of the dispatcher's
  permission-rule matcher. Rung 3, reuse of the seam. RESOLVED (agent, 2026-10-26, delegated): (a).
  widens: none · relaxes: none
- **F3 — What does a role act name for the shell?** (a) The work order's `allow` list, empty by
  default; (b) every command, judged only by the guard packs. (b) leaves the 25 ad-hoc scripts the
  layer binds unbound. Rung 1, layer-runtime `[act]` "an act session's allowance names the commands it
  may run". RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit round 1's
  promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-66.

## 10. Reuse audit

The seams extended: the dispatcher's `PermissionRequest` run and its permission-rule matcher
(TOOL-dWellOiledMachine-10 S8); the published binding through `read_binding`
(TOOL-dWellOiledMachine-39 S6); the session binding's one reader (TOOL-dWellOiledMachine-12 S2); the
supervisor's pid file and fence read (TOOL-dWellOiledMachine-6 S1, S7); the platform's run journal
through `load_run_journal` (`tools/roles/handoff.py:686`) and `resolve_session_tree`
(`tools/runlog/extract.py:266`); and the declared stage rows through `load_workflows`
(`tools/roles/roles_lib.py:364`, cited by scout C at `:339` on an older base). The probe
`python tools/codebase-map/reuse_lookup.py "bind a Workflow or Agent call to the act and refuse a
stale epoch"` ranked `load_workflows`, `CensusRefused`, `ScopeRefused` and `read_bindings`; the first
is read here, and `read_bindings` (`tools/memory-tree/tree_lib.py`) parses Serves lines, not acts.

Recall terms used: `python tools/memory-recall/query.py "how is a role act's Workflow call bound to
its act and epoch at PermissionRequest" --terms "act binding epoch PermissionRequest dispatcher
Workflow Agent spawn guard task-sha in-script reconcile"`
