# KICK-dKeptSession-8 — `actions.free` at the tool call: every write, spawn, commit or push belongs to the item in flight

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 25 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0146@a9c32df5 whole
**Carries:** node:policy-key.actions.free

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-c.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-26 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

About 63% of main-loop tool calls follow no protocol step (orientation OR-3), and nothing ties a Bash
write, a commit, a push or a spawn to the work item that owns it: the write gate ties an Edit or a
Write to a routed unit (`checkRouted`, `tools/hooks/scratch-guard.js:1113`) and a commit to a READY
card (`checkOriented`, :758), never to an item. This unit carries `actions.free` at the tool call, as
the owner settled it: off-item acts are read-only probes by default, free inside the current item;
every write, spawn, commit or push belongs to an item, and anything else is filed as an intake
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-orientation.md:310-312`;
v2:1175, strict's `item-reads-only` at v2:1500).

## 2. Scope (IN)

- **S1** — The catalogue row `actions.free`, allowed `read-only-probes`, `item-reads-only`,
  `recorded-anything`, default `read-only-probes` (v2:1175), through
  `python tools/playbook/core.py new policy-key actions.free --allowed <toml> --default <toml> --summary <text> --usage <text> --owner dKeptSession`
  (TOOL-dDeclaredLoop-6 S4), and the JSON mirror `.governance/policy.json` regenerated by
  `policy.py mirror --write` in its own commit, so the hook's reader holds the key. Observed by AC8.
- **S2** — The act class, `classifyAct(data)` in `tools/hooks/scratch-guard.js`: `spawn` for an `Agent`
  or `Workflow` call; `write` for a `WRITE_TOOLS` call (:794) or a Bash or PowerShell command for which
  `scanWriteTargets` (:339) finds a target; `commit` where `COMMIT_SHAPED` (:592) matches the command
  view; `push` where `PUSH_SHAPED`, its sibling over the same token grammar with `push` for `commit`,
  matches; `read` otherwise. The strongest class wins in the order `push`, `commit`, `write`, `spawn`,
  `read`. Observed by AC1 and AC5.
- **S3** — The item in flight, `readItemPointer(data, env)`: the session card through `readCard` (:667),
  its `## route` `- build:` slug through `extractRouteUnits` (:839), that build's card through
  `manifest-check.sh --card --path --build <slug>`, TOOL-dPlacedRequest-2 S10's one path reader, under the
  same bound `readCard`'s call takes there, and the `item —` line of its `## pointers` section,
  KICK-dKeptSession-13's I11 shape: an instance key, or `none`. The arm never derives an item boundary;
  KICK-dKeptSession-13 rewrites the pointer at each boundary `derive_item_boundary` finds. Observed by AC2
  and AC6.
- **S4** — The decision, `checkFreeAction(data, env)`, by the table of §4: an act while the pointer names an
  item is admitted under every value; with `item — none`, `read-only-probes` admits a `read` and refuses
  the rest, `item-reads-only` refuses every act but a boundary command (`BOUNDARY_HEADS`, §4), and
  `recorded-anything` admits every act, appending each one `read-only-probes` would refuse to
  `<git-common-dir>/gov-free-actions.log`. A refusal exits 2 naming `actions.free`, its value, the class,
  the tool and `item none`, and its remedy: run the act inside the item that owns it, or file it as an
  intake. Observed by AC1, AC2, AC3 and AC4.
- **S5** — The value, read once per armed call through dGroundRules' JS reader
  `readPolicy("actions.free", { repo })` (TOOL-dGroundRules-5 S5, I8), located by `resolvePolicyHelper()`:
  the policy kit's `policy-mirror.js` beside the hooks kit, the location rule 7 of `tools/hooks/agent-cap.js`
  reads as its `POLICY_HELPER` (TOOL-dGroundRules-10 S5). This is that rule's second instance, so
  `resolvePolicyHelper` is exported from `scratch-guard.js` and agent-cap's constant is re-pointed to it.
  The value is read only when the pointer reads `none`. With no helper, or a `PolicyRefusal`, the arm reads
  the catalogue default `read-only-probes` and prints one `NOTE` naming why. Observed by AC7.
- **S6** — The wiring. In `main` (:1529) the arm runs after `checkRouted` admits a write-tool call and
  after `checkRoleGate` on a Bash or PowerShell call; in `tools/hooks/agent-cap.js` it runs as rule 8 on
  every `Agent` and `Workflow` call, after rule 6, outside any `--only=` selector, required from
  `scratch-guard.js` as that hook already requires `loadRoleIndex`. Observed by AC1 and AC5.
- **S7** — Unarmed and failure. With no session card, no routed build, or a build card carrying no
  `## pointers`, the arm admits and prints `scratch-guard: actions.free unarmed — <why>`, never silent.
  Once armed, a throw anywhere in the arm refuses, as the write gate refuses (:1549-1556). Observed by AC6.
- **S8** — The fixture, `bash tools/hooks/actions-free.fixture.sh --plant <case>`: a scratch repository
  under `%TEMP%` with a session card routed to `tFix`, a build card whose `## pointers` the plant writes,
  copies of both hooks, a stub `policy-mirror.js` beside them answering the planted value and a stub
  kickoff checker answering `--card --path`; it pipes the case's payload to the hook and prints the exit
  code and stderr. Observed by AC1 to AC7.
- **S9** — The page `help/orientation-card.md` (TOOL-dPlacedRequest-9's) gains a section: the item pointer,
  what each value admits outside it, and the log. Observed by AC8.

## 3. Non-goals (OUT)

- Writing or deriving the `item —` pointer and the item boundary: KICK-dKeptSession-13's.
- Counting an act against its item, and orientation cost: KICK-dKeptSession-9's runlog reading.
- Filing the intake itself: the refusal names the remedy; the intake record kind and `item.entry.intake`
  are dWellOiledMachine's.
- Matching a read to the item's declared `inputs`: an input is a layer tag (TOOL-dDeclaredLoop-12 §4), which
  no tool call can be mapped to, so a read inside an item is taken as the item's.
- Writes an interpreter makes (`python -c`, a script), which `scanWriteTargets` does not see (the header
  at :86); the push-time leg keeps that guarantee.
- The `Read`, `Grep` and `Glob` tools: the hook's matcher (`tools/hooks/scratch-guard.fragment.json`) does
  not route them here, and every value admits a read inside an item.

### Edges

- **consumes-from** `KICK-dKeptSession-13` — `## pointers`, the build card section whose `item —` line is the item in flight this arm reads; without it the arm is unarmed
- **consumes-from** `KICK-dKeptSession-13` — `derive_item_boundary`, the boundary at which that unit rewrites the pointer, so this arm never derives one
- **consumes-from** external — dGroundRules' `readPolicy` (TOOL-dGroundRules-5 S5) and agent-cap's rule 7 location (TOOL-dGroundRules-10 S5); dPlacedRequest's `--card --path --build` (TOOL-dPlacedRequest-2 S10); the policy-key factory (TOOL-dDeclaredLoop-6 S4)
- **hands-off** `KICK-dKeptSession-41` — S1's `actions.free` row, which that unit grounds on the standing catalogue row (id 45)
- **hands-off** `KICK-dKeptSession-43` — `readItemPointer` and `checkFreeAction`, whose pointer parse that unit closes over the `skipped:` form (id 57)
- **hands-off** `KICK-dKeptSession-44` — the `actions.free` plants, run under both `card.pointers` values by the batch's S10 (id 11)

## 4. Design

### The decision

| Pointer | Class | `read-only-probes` | `item-reads-only` | `recorded-anything` |
|---|---|---|---|---|
| an item | any | admit | admit | admit |
| `none` | `read` | admit | refuse, unless a boundary command | admit |
| `none` | `write`, `commit`, `push`, `spawn` | refuse | refuse | admit, one log line |

`BOUNDARY_HEADS = ['position.py', 'manifest-check.sh']`: the two commands that move a session to its next
item, the position engine's answer (TOOL-dDeclaredLoop-7 S7) and the card's pointer writer
(KICK-dKeptSession-13), matched on each command head's base name through `scanCommandHeads` (:1279) and
`buildBaseName` (:1231). Without them `item-reads-only` could never leave `item — none`.

### The refusal

```
BLOCKED by scratch-guard: actions.free (item-reads-only) refuses this Bash read — the card of tFix reads item — none.
Run the act inside the item that owns it, or file it as an intake.
```

### The log

`<git-common-dir>/gov-free-actions.log`, one appended line per recorded act,
`<iso> · <session> · <class> · <tool> · item none`, beside `gov-feed.log` in the same directory. It is
evidence for KICK-dKeptSession-9's reading and nothing else reads it.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `classifyAct`, `readItemPointer`, `checkFreeAction`, `resolvePolicyHelper` | JS functions, `scratch-guard.js` | asked of `python tools/lexicon/lexicon.py --suggest <name>` at the pass |
| `PUSH_SHAPED`, `BOUNDARY_HEADS`, `FREE_ACTIONS_LOG` | JS constants | none declared |
| rule 8 | an agent-cap rule | none |
| `actions-free.fixture.sh` | fixture | none |

### Migration

None. A session with no build card pointers is unarmed and admitted, so no session outside the loop moves.

### Rollout

Live at landing, armed only where KICK-dKeptSession-13 writes a build card's `## pointers`.

### Files touched (estimate)

- `tools/hooks/scratch-guard.js`: the arm, its helpers, the wiring in `main`, `KIT_SCRATCH_GUARD_VERSION` moved
- `tools/hooks/agent-cap.js`: rule 8, and `POLICY_HELPER` re-pointed to `resolvePolicyHelper`; `KIT_AGENT_CAP_VERSION` moved
- `tools/hooks/actions-free.fixture.sh`
- `tools/hooks/kit.toml`: the fixture shipped
- `tools/hooks/scratch-guard.test.sh`: the arms the §7 line declares
- `tools/hooks/agent-cap.test.sh`: rule 8's arm
- `tools/policy/catalogue.toml`: one row, through the factory
- `.governance/policy.json`: the mirror, regenerated in its own commit
- `help/orientation-card.md`

### Alternatives rejected

- **A new hook file.** `scratch-guard.js` already reads the card and classifies writes and commits; a
  second hook would read both again and race the first on one call.
- **Deriving the item in the hook.** Running the position engine per tool call costs a Python spawn on
  every Bash call and gives two places the boundary is decided.
- **Refusing reads off-item under `item-reads-only` with no exception.** It leaves no act that can move the
  pointer, so a strict session deadlocks between items.

## 5. Production-readiness checklist

- security — deny by default once armed: a throw refuses; the policy value comes only from the landed
  mirror through the one reader; the log line carries the class and tool, never the command text.
- perf / scale — the pointer is one card read and one bounded checker call; the policy read runs only at
  `item — none`.
- error / empty / loading states — unarmed cases print their witness and admit; a policy refusal reads the
  default with a `NOTE`.
- observability — every refusal names the value, class, tool and the pointer; every recorded act is a log line.
- risks — a stale pointer refuses a write after an item ended; KICK-dKeptSession-13 rewrites it at each
  boundary, and `item-reads-only`'s boundary commands always run.
- testing — the fixture's plants by a pass; the arms in §7 observed RED then GREEN by the main loop.
- migration — none.
- user docs — `help/orientation-card.md`.

## 6. Acceptance criteria

- **AC1** — When `bash actions-free.fixture.sh --plant probes-none` runs under `read-only-probes` with
  `item — none`, `git status` exits 0, while `echo x > f`, `git commit -m x`, `git push` and an `Edit` the
  route admits each exit 2 naming `actions.free`, `item none` and the class `write`, `commit`, `push`,
  `write`.
  Red when: a write, commit or push passes with no item in flight, or a read is refused.
- **AC2** — When the plant `probes-item` writes `item — item.build.unit-pass@1·2#3f9c` into `## pointers`,
  the four calls of AC1 each exit 0 under each of the three values.
  Red when: an act inside the item in flight is refused.
- **AC3** — When the plant `reads-none` runs under strict's `item-reads-only` with `item — none`, `git status`
  exits 2 naming the class `read`, and `python position.py tFix` and `bash manifest-check.sh --card --pointers --build tFix` each exit 0.
  Red when: `item-reads-only` admits an off-item read, or refuses a boundary command.
- **AC4** — When the plant `anything-none` runs `echo x > f` and `git status` under `recorded-anything` with
  `item — none`, both exit 0 and the fixture's `gov-free-actions.log` gains exactly one line, naming the
  class `write` and the session.
  Red when: an off-item write is admitted unrecorded, or a read is logged.
- **AC5** — When the plant `spawn-none` pipes an `Agent` payload to `agent-cap.js` under `read-only-probes`
  with `item — none`, it exits 2 naming `actions.free` and the class `spawn`; with `spawn-item`, stderr
  carries no `actions.free` line.
  Red when: a spawn outside an item passes rule 8.
- **AC6** — When the plants `no-pointers` and `no-route` run AC1's `echo x > f`, each exits 0 printing
  `actions.free unarmed`; when the plant `throw` makes the stub checker answer bytes the pointer reader
  cannot parse, the call exits 2 naming the arm.
  Red when: an unarmed session is refused or admitted silently, or an armed throw admits.
- **AC7** — When the plants `no-helper` and `refusal` run AC1's `echo x > f`, each exits 2 as
  `read-only-probes` does and prints one `NOTE` naming the default.
  Red when: an unreadable value admits the write or reads another default.
- **AC8** — When `python -c "import tomllib, sys; r=[k for k in tomllib.load(open(sys.argv[1], 'rb'))['key'] if k['name'] == 'actions.free']; print(r[0]['owner'], r[0]['default'])" catalogue.toml`
  runs in the policy kit's directory, it prints `dKeptSession read-only-probes`, and
  `grep -c 'actions.free' orientation-card.md` in `help/` prints at least 1.
  Red when: the key has no row, or the page omits the values.
  fixture: the catalogue is dGroundRules', untracked at base until it builds.

## 7. Gates

`scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `govkit selftest` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/hooks/scratch-guard.test.sh · covers AC1 AC2 AC3 AC4 AC6 AC7 · the arm over each value and pointer, staged against the base hook, which admits a Bash write with no item in flight · none

New arm: tools/hooks/agent-cap.test.sh · covers AC5 · rule 8 on an `Agent` payload with `item — none`, staged against the base hook, which has no rule 8 · none

## 8. Open questions

- **F1 — What does `item-reads-only` admit with no item in flight?** OR-3's option reads "Only the item's
  declared reads", and an item's `inputs` are layer tags no tool call maps to. Options: (a) nothing, every
  call refused; (b) nothing but the two boundary commands that move the session to its next item; (c) the
  same as `read-only-probes`. (a) deadlocks a strict session at `item — none`, since the pointer can then
  never move; (c) leaves strict's value indistinguishable from the default, so AC3 cannot be met.
  RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the most feature-rich survivor.
- **F2 — Where does an off-item act under `recorded-anything` get recorded?** Options: (a) a stderr witness
  only; (b) one line in a log under the git common dir; (c) a record in the build folder. (a) leaves no
  durable record, so "recorded" is not met; (c) commits per tool call into the build's tree.
  RESOLVED (agent, 2026-10-26, delegated): (b), rung 3.

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 8, orientation OR-3 and its settled text,
  v2:1175 and :1500, and the hook read at base `462d20f3`.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-41`, `KICK-dKeptSession-43`,
  `KICK-dKeptSession-44` mirrored, the other ends of the edges the round-1 spec audit's promoted
  units declare; no other section moved.

## 10. Reuse audit

The seam extended is `tools/hooks/scratch-guard.js`'s ordered arms in `main` (:1529-1612), beside
`checkRouted` (:1113), `checkOriented` (:758) and `checkRoleGate` (:1421), all verified at base; the
classification reuses `scanWriteTargets` (:339), `COMMIT_SHAPED` (:592), `scanCommandHeads` (:1279) and
`buildBaseName` (:1231), and the card reads reuse `readCard` (:667) and `extractRouteUnits` (:839). The
spawn arm reuses agent-cap's existing require of `scratch-guard.js` (`tools/hooks/agent-cap.js:2278`). The
policy location is dGroundRules' `POLICY_HELPER`, read on `branch/unattended-dgroundrules-e47ae1` at
`tools/hooks/agent-cap.js:465` (cite GR); its second instance is extracted here. Scout C cited
`agent-cap.js:112-117` for `resolveHarnessName`; source puts it at :109-117. Scout C's ":1530-1612" for
`main` is :1529-1612 at base. `python tools/codebase-map/reuse_lookup.py "refuse a write or commit made
outside the current item at the tool call"` ranked name stems only (`write`, `write_text`, `build_commit`),
none a hook arm, so no further seam fits. `python tools/memory-recall/query.py` returned scout C's row,
the orientation record's settled text and TOOL-aOrientedCast-6's role arm on the same write gate, which
agrees with source.

Recall terms used: `python tools/memory-recall/query.py "what may a session do outside its current item, and which hook refuses a write that belongs to no item" --terms "actions.free read-only-probes item-reads-only recorded-anything scratch-guard checkRouted off-item intake tool call"`
