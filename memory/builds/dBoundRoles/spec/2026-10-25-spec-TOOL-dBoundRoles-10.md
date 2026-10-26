# TOOL-dBoundRoles-10 — `driver.reads`, `prompts.author` and `roles.no-spawn`, each read and enforced at its seam

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 4ed9e567 · streams tooling · order 16 · advances TOOL-dBoundRoles-27

**Carries:** cl-dClosedLoop-0175@0d300fb9 whole
**Carries:** node:policy-key.driver.reads
**Carries:** node:policy-key.prompts.author
**Carries:** node:policy-key.roles.no-spawn

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-reuse-scout-b.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-17 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 |
| [2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dBoundRoles-1-spec-stage-returns.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-build-TOOL-dBoundRoles-10-deviation-101.md](../build/2026-10-25-build-TOOL-dBoundRoles-10-deviation-101.md) | deviation | — |
| [2026-10-25-build-TOOL-dBoundRoles-10-deviation-102.md](../build/2026-10-25-build-TOOL-dBoundRoles-10-deviation-102.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 |
| [2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-spec-fix-return.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dBoundRoles-1-spec-fix-brief.md) | research | TOOL-dBoundRoles-1 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-11 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 |
| [2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-1-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-1 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-2 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 |

<!-- /gen:spec-records -->

## 1. Goal

The owner settled three defaults for how the main session and its roles meet (`roles.md:351-381`):
the main session reads only cheap state (RL-5), a prompt writer writes every worker's task (RL-4), and
an item a role must perform is never done inline when no agent can be spawned (RL-8). v2 makes each a
policy key with its values (v2:1179, :1180, :1182). This unit reads the three keys through the policy
reader and enforces each value where a seam exists: `driver.reads` at a new main-loop read arm of the
write gate's hook, `prompts.author` at the spawn guard's rule 6, and `roles.no-spawn` at the stand-in
render. Where a value has no seam at base, the spec says what stands in and who takes it over.

## 2. Scope (IN)

- **S1** — `driver.reads`, values `none-scout-only`, `state-reads-only` and `read-only-probes`,
  default `state-reads-only`. `checkDriverRead(data, env)` in `tools/hooks/scratch-guard.js`, run for a
  `Read`, `Grep` or `Glob` payload: a payload carrying an `agent_type` is admitted (workers keep their
  read-only probes, RL-5's settlement); for the main loop, `read-only-probes` admits all three,
  `state-reads-only` refuses `Grep` and `Glob` and admits `Read`, and `none-scout-only` refuses all
  three. Observed by AC1 and AC2.
- **S2** — The hook's matcher widens to `Read|Grep|Glob` beside its write tools, in
  `tools/hooks/scratch-guard.fragment.json`, and `.claude/settings.json` is re-merged by
  `settings-merge.py --fragment`; `main` dispatches the three tools to S1 before its write-gate branch.
  Observed by AC3.
- **S3** — `prompts.author`, values `prompt-writer` and `requesting-worker-rendered`, default
  `prompt-writer`. `resolvePromptsAuthor(root)` in `tools/hooks/agent-cap.js` reads it once per `Agent`
  call in rule 6 (`checkHandoffSpawn`, `agent-cap.js:2089`). Under `requesting-worker-rendered`, rule 6
  is today's check, every task a rendered handoff the requesting session made; under `prompt-writer`,
  rule 6 also applies the framing requirement TOOL-dBoundRoles-4 defines. Every rule-6 refusal names
  the value in force. Observed by AC4.
- **S4** — `roles.no-spawn`, values `executor-role-session`, `recorded-stand-in` and `refuse`, default
  `executor-role-session`, read by `handoff.py render --stand-in` (`tools/roles/handoff.py:1034-1041`).
  `recorded-stand-in` keeps today's waiver-backed stand-in (`load_stand_in_waivers`,
  `roles_lib.py:488`; R15). `refuse` refuses every `--stand-in`, naming the key. `executor-role-session`
  refuses `--stand-in` too, naming the route that is always open, a role spawned through `Agent` or a
  listed harness, and the hand-over: the executor that starts a role session for the item is
  dWellOiledMachine's. R15's join of waiver rows and declarations (`check_roles.py:360-372`) is unchanged.
  Observed by AC5.
- **S5** — Every key is read through the policy reader, never with `tomllib` over
  `.governance/policy.toml` (shared interface I8): the two hooks through TOOL-dGroundRules-5 S5's
  `readPolicy`, located as that section states for a hook, and `handoff.py` through TOOL-dGroundRules-2
  S6's `resolve`, located through `roles_lib.resolve_kit_dir`. A key the file leaves unset reads its
  catalogue default. Where the policy kit is not installed, each check is unarmed: S1 admits with one
  witness line, S3 runs today's rule 6, and S4 keeps today's stand-in. The three catalogue rows are
  TOOL-dGroundRules-1 S3's, written from v2's rows; this unit adds none. Observed by AC2 and AC6.
- **S6** — Every refusal names the key, its value, and the remedy with its actor: the driver, which
  dispatches a scout through a rendered handoff (S1), renders the handoff the value requires (S3), or
  spawns the role (S4); or the owner, who may set another value in the guarded policy file.
  Observed by AC1, AC4 and AC5.
- **S7** — The user page `help/roles.md`: "When no role agent can be spawned" (`:93`) states the three
  `roles.no-spawn` values and the default's refusal, and "What the hooks refuse" (`:103`) gains the
  main loop's `Grep` and `Glob` under the default `driver.reads`. Observed by AC7.

## 3. Non-goals (OUT)

- The framing requirement under `prompts.author = prompt-writer`, and the prompt writer itself:
  TOOL-dBoundRoles-4's, which reads this unit's key.
- The executor that starts a role session for an item no agent can take: dWellOiledMachine's. Until
  it lands, `executor-role-session` refuses the stand-in (§8 F3).
- Restricting the main loop's `Read` to records it was handed under `state-reads-only`. No record of
  what was handed exists at base; the driver's binding record is dWellOiledMachine's (§8 F1).
- The main loop's Bash: `grep`, `find` and `cat` run through Bash are not seen by S1, which reads the
  three read tools only; act binding of the driver's shell is dWellOiledMachine's
  (`layer-runtime.md:530-531`).
- The catalogue rows and the reader: dGroundRules'.

### Edges

- **hands-off** `TOOL-dBoundRoles-4` — `prompts.author` and its reader `resolvePromptsAuthor`, the switch under which rule 6 applies the prompt writer's framing requirement
- **consumes-from** external — TOOL-dGroundRules-2 S6's `resolve` and TOOL-dGroundRules-5 S5's `readPolicy`, and the three catalogue rows of TOOL-dGroundRules-1 S3; the build run re-grounds on each and stops the unit if one is still absent
- **hands-off** `TOOL-dBoundRoles-43` — `checkDriverRead`, `roles.no-spawn` and AC6, which unit 43 gives a verdict on a policy refusal, a stand-in fixture and a falsifiable grep (ids 12, 27, 31 and 60 of the round-1 spec audit)
- **hands-off** `TOOL-dBoundRoles-44` — `checkDriverRead`'s refusal of the search tool, which unit 44's kickoff line stops naming (id 28 of the round-1 spec audit)

## 4. Design

### The three keys

| Key | Values (v2) | Default | Read at | Enforced as |
|---|---|---|---|---|
| `driver.reads` | `none-scout-only`, `state-reads-only`, `read-only-probes` | `state-reads-only` | `checkDriverRead`, `scratch-guard.js` | the main loop's `Read`, `Grep`, `Glob` (S1) |
| `prompts.author` | `prompt-writer`, `requesting-worker-rendered` | `prompt-writer` | `resolvePromptsAuthor`, `agent-cap.js` rule 6 | today's rule 6, plus TOOL-dBoundRoles-4's framing under `prompt-writer` |
| `roles.no-spawn` | `executor-role-session`, `recorded-stand-in`, `refuse` | `executor-role-session` | `handoff.py render --stand-in` | the stand-in's admission (S4) |

### The read arm

```
checkDriverRead(data, env)            tool_name in Read | Grep | Glob
 1. agent_type non-empty             -> null   (a worker's probe)
 2. readPolicy("driver.reads") at the payload cwd's toplevel
      the policy kit not installed   -> { witness: "driver.reads unarmed — …" }
 3. read-only-probes                 -> null
    state-reads-only, Read           -> null
    state-reads-only, Grep | Glob    -> deny
    none-scout-only                  -> deny
```

A payload whose `cwd` lies in no repository is not this arm's. The hook's write-gate branch is
untouched: `main` routes the three read tools to S1 and exits, so a read never reaches `checkRouted`
or the Bash checks.

`state-reads-only` is RL-5's "cheap state reads only", and its settlement names what that is: `next`,
a record the driver was handed, a short git state command; "anything exploratory is a scout's task"
(`roles.md:377-378`). `Grep` and `Glob` are the two read tools whose every use is a search; a `Read`
names its one file, and the record it was handed is a file it reads, so the arm admits `Read` under
this value (§8 F1). BUILD-METHOD M7's regrounding reads by `Read` and Bash only, so the default keeps
it whole; under `none-scout-only`, the owner's strictest value, M7's reads are refused too, which §5
states.

### The stand-in under each value

```
handoff.py render --stand-in
  roles.no-spawn = recorded-stand-in     -> today: a waiver row admits, its absence refuses (R15)
  roles.no-spawn = refuse                -> refuse: "roles.no-spawn is refuse …"
  roles.no-spawn = executor-role-session -> refuse: spawn the role through Agent or a listed harness;
                                            the executor's role session is dWellOiledMachine's
```

### Inventory

Minted: `checkDriverRead`, `resolvePromptsAuthor`; the read-tool dispatch in `scratch-guard.js`'s
`main`; the widened matcher; the `--stand-in` branch on `roles.no-spawn`; the fixture plants of §7's
arms (`main-grep-default`, `main-read-default`, `main-read-none`, `worker-grep`, `policy-absent`,
`author-requesting`, `nospawn-refuse`, `nospawn-executor`, `nospawn-recorded`). Each function name is
asked of `python tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

None stored. An adopter without the policy kit sees no change (S5). With it, the defaults bind at the
landing: the main loop's `Grep` and `Glob` refuse, and `--stand-in` refuses until the owner sets
`roles.no-spawn = "recorded-stand-in"`.

### Rollout

Live at landing where the policy kit is installed; each key is the owner's switch, the guarded policy
file its one write path.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/scratch-guard.fragment.json`
- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/README.md`
- `tools/roles/handoff.py`
- `tools/roles/README.md`
- `help/roles.md`
- `.claude/settings.json`

### Alternatives rejected

- **A separate read hook.** A second hook file for three tools duplicates the hook's toplevel and
  payload readers; the matcher on the one hook costs one dispatch.
- **Leaving `driver.reads` as a recorded value no check reads.** A key nothing enforces is the prose
  limit gap-roles-03 counts; the read tools are reachable by a matcher today.

## 5. Production-readiness checklist

- security — narrows the main loop's read surface and the stand-in path; deny-by-default only where the
  owner's key is in force, and unarmed, never refusing, where the reader is absent.
- perf / scale — one hook launch per `Read`, `Grep` or `Glob` in every session; a typed payload returns
  at step 1 with no file read, and the main loop reads the policy value once per call.
- error / empty / loading states — the policy kit absent: each check unarmed with a witness; a value
  outside the row's set is refused by the catalogue's schema arm before it reaches a hook.
- observability — each refusal names key, value, remedy and actor (S6).
- risks — under the default, an owner's attended main session loses `Grep` and `Glob` (RL-5's
  answer); under `none-scout-only` it loses `Read` too, M7's regrounding included. `--stand-in`
  refuses by default (RL-8's answer).
- testing — the plants of §4's inventory through `node -e` and the `handoff.py` verb over fixture
  repositories; the arms in §7 are observed RED then GREEN by the main loop at the close.
- migration — none, as §4 says.
- user docs — `help/roles.md` (S7), with `tools/hooks/README.md` and `tools/roles/README.md`.

## 6. Acceptance criteria

The hook criteria run the exported functions of `tools/hooks/scratch-guard.js` and
`tools/hooks/agent-cap.js` through `node -e` over a fixture repository under `%TEMP%` whose policy
file, `policy.toml`, sets the value named.

- **AC1** — When `checkDriverRead` reads a `Grep` payload with no `agent_type` and `driver.reads` unset,
  it returns a `deny` naming `driver.reads`, `state-reads-only` and a scout as the driver's remedy; a
  `Read` payload returns null; with `read-only-probes` the `Grep` returns null; with `none-scout-only`
  the `Read` returns a `deny`.
  Red when: the main loop's search tools are admitted under the default, as at base.
- **AC2** — When the same `Grep` payload carries `agent_type` `gov-researcher`, it returns null under
  every value; and when the fixture has no policy kit, the main loop's `Grep` returns a `witness` naming
  `driver.reads unarmed`.
  Red when: a worker's probe is refused, or a missing reader refuses every read.
- **AC3** — When `grep -c "Read|Grep|Glob" tools/hooks/scratch-guard.fragment.json` runs, it prints 1,
  and `.claude/settings.json` carries the same matcher on the hook's `PreToolUse` group.
  Red when: the matcher stays the write tools', so no read ever reaches S1.
- **AC4** — When `resolvePromptsAuthor` reads a fixture with `prompts.author` unset, it returns
  `prompt-writer`; set to `requesting-worker-rendered`, it returns that, and a rule-6 refusal of a
  freeform prompt names `prompts.author` and the value.
  Red when: the value is a literal in the hook, or the refusal does not say which value is in force.
- **AC5** — When `python tools/roles/handoff.py render --role gov-builder --build x --stand-in` runs over
  a fixture with `roles.no-spawn = "refuse"`, it exits non-zero naming `roles.no-spawn`; unset, it exits
  non-zero naming the `Agent` route and dWellOiledMachine; with `recorded-stand-in` and a waiver row for
  `gov-builder` in build `x`, it writes the `-stand-in` file as at base.
  Red when: `--stand-in` ignores the key, so the default admits an inline stand-in.
- **AC6** — When `git grep -n "tomllib" tools/hooks/scratch-guard.js tools/hooks/agent-cap.js` runs, it
  prints nothing, and `git grep -n "\.governance" tools/roles/handoff.py` prints no line that opens
  the policy file.
  Red when: a key is read by parsing the policy file beside the reader.
- **AC7** — When `grep -n "roles.no-spawn" help/roles.md` and `grep -n "driver.reads" help/roles.md`
  run, each names its key in the section S7 gives it.
  Red when: the page still says a waiver alone admits a stand-in.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `check-wiring self-test` · `lexicon naming predicates` · `roles catalogue` · `roles render selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 · the `main-grep-default`, `main-read-none` and `policy-absent` plants stage the failing case against a copy of the hook whose read dispatch is cut from `main` · none
New arm: tools/hooks/agent-cap.test.sh · covers AC4 · the `author-requesting` plant, staged by a rule 6 that reads no key · none
New arm: tools/roles/render_agents.py · covers AC5 · its self-test renders `--stand-in` under the `nospawn-refuse`, `nospawn-executor` and `nospawn-recorded` plants, staged by a render that skips the key · none

## 8. Open questions

- **F1 — What does `state-reads-only` refuse when no record says what the driver was handed?**
  Options: (a) the main loop's `Grep` and `Glob`, `Read` admitted; (b) every main-loop `Read` outside
  the build's record folder as well; (c) nothing, the value recorded only. (b) types a list of
  readable paths beside the method that needs them, and refuses BUILD-METHOD M7's read of the method
  and of the current spec, a governance carrier's procedure, which veto 2 keeps from this run; (c) is
  a limit no check reads. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich
  option no veto refuses; it departs from the value's full reach, recorded in
  `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-10-deviation-101.md`.
  widens: none · relaxes: none
- **F2 — Where does `prompts.author` take effect, given that the framing it requires is
  TOOL-dBoundRoles-4's?** Options: (a) this unit reads the key at rule 6 and leaves the `prompt-writer`
  branch's added requirement to TOOL-dBoundRoles-4, which follows it in the build order; (b) this unit
  defines the framing requirement too. (b) specs the prompt writer's output before the unit that
  defines the prompt writer. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the order the
  brief's edge `10 → 4` sets. widens: none · relaxes: none
- **F3 — `roles.no-spawn = executor-role-session` with no executor at base.** Options: (a) refuse the
  stand-in, naming the spawn route and the executor's build; (b) behave as `recorded-stand-in`; (c)
  start a role session by hand from `handoff.py`. (b) admits the inline work RL-8 asked to eliminate
  under the value that names its opposite; (c) is dWellOiledMachine's executor built here, outside the
  clause. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3; the owner's RL-8 answer says a harness
  "that can ALWAYS spawn subagents" exists in the repository, so the refusal names a route that is
  open. Recorded as a stand-in in
  `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-10-deviation-102.md`.
  widens: none · relaxes: none
- **F4 — The Carries pin of an amended clause: v2's baseline hash or the as-built view's?**
  `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-10-deviation-101.md` and
  `memory/builds/dBoundRoles/build/2026-10-25-build-TOOL-dBoundRoles-10-deviation-102.md` amend
  `cl-dClosedLoop-0175`, so the as-built view hashes it `0d300fb9` where v2 hashes it `79a1c7d0`.
  Options: (a) pin the view's hash, which the spec-tokens leg's carries join reads; (b) pin v2's
  baseline hash, which the packet's `carries.py --exit` reads. No pin satisfies both: (b) reds the merge
  bar's carries join as a stale pin, and (a) reds the packet instrument's Design-exit carries arm on
  this clause, the disagreement `PLAY-dClosedLoop-30` records. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 1, the spec fix brief's F3; the instrument's red on this clause is `PLAY-dClosedLoop-30`'s
  until its pin moves by the owner's `packet.py --repin`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 10, v2's `[policies]` rows 1179, 1180 and
  1182, RL-4, RL-5 and RL-8 with their settlement, scout B's row for cl-0175, and the hooks and the
  handoff renderer at base `4ed9e567`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the **hands-off** bullets mirroring the edges of TOOL-dBoundRoles-43, TOOL-dBoundRoles-44, promoted by the round-1 spec audit of the 26 unit specs; nothing else moved.

## 10. Reuse audit

The seams extended are the write gate's hook `tools/hooks/scratch-guard.js` (its `main` dispatch,
`:1529-1611`, and its fragment's matcher), the spawn guard's rule 6 (`checkHandoffSpawn`,
`tools/hooks/agent-cap.js:2089-2148`), and the stand-in render (`tools/roles/handoff.py:1034-1048`,
`load_stand_in_waivers` at `roles_lib.py:488`). the probe `reuse_lookup.py` over the phrase "read a policy key value to gate a spawn or a read" ranked `read_conf_key`, `readConfKey` and `load_policy`;
the first two read `.memory-tree.conf` and the third the roles kit's house file, and none reads a
`.governance` key, so the reader is dGroundRules' and no existing seam in this tree fits for it. For
reads, no hook sees `Read`, `Grep` or `Glob` at base (the fragment's matcher is
`Bash|PowerShell|Edit|Write|MultiEdit|NotebookEdit`), which scout B states and source confirms; the
matcher is the seam this unit opens. Scout B's row agreed with source; its stand-in reference
`:1034-1041` covers the waiver check, and the tail write runs to `:1048`.

Recall terms used: `python tools/memory-recall/query.py "which policy keys govern driver reads prompt authorship and no-spawn" --terms "driver.reads prompts.author roles.no-spawn stand-in waiver main loop read probes catalogue"`
