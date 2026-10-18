# Research: unattended as the core flow's default state

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 100's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-4-researcher.md`, and its use is in `build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass.md`.

---

I couldn't run the build-time tests, so some of this rests on reading the records rather than running code. I ran only read-only probes (one was `check-playbook.sh --counts`, a census leg) and wrote nothing.

## 1. Verdict

The design already holds most of point 1. `autonomy: plan-only` with `plan.ratification: request` means no owner turn by default. But the design still lets attended change who drives and what is enforced. The owner's session drives when attended (layer-runtime:300-301, 311, 346), and act binding does not apply to it (layer-runtime:501-504). Today's code shows the cost: in attended mode, `unattended-build.js` loses five checks the driver makes (`tools/workflows/unattended-build.js:49-61`).

Playbook mode has no home in any chain row.

**Recommendation (C1):** one driver, the supervisor, in every mode. Attendance only places owner breakpoints, extending the `autonomy` seam. The owner's session becomes a client. Playbooks become a design record kind, reached through a `repeat` placement disposition.

## 2. Today

**Probes**

```
$ grep -oE '^[A-Z_]+=' .unattended.conf | wc -l            → 63
$ grep -n '^VERBS_SLUG=\|^VERBS_INLINE=' unattended.sh      → 111: 24 slug verbs; 114: 6 inline verbs (30)
$ grep -h '^mode:\|^phase:' RUN*.md | uniq -c (98 files)    → prompt 54 · slug 32 · (none) 12 · recipe 0
                                                              LANDED 57 · LANDING 18 · ABORTED 13 · HELD 8 · BUILDING 2
$ grep -h '^authorized-by:' builds/*/README.md | uniq -c    → prompt 62 · slug 2 ; READMEs with asks: 2
$ journal verbs across RUN*.md                              → dispatch 1297 · brief 757 · rescope 398 · review 356 ·
                                                              decision 237 · hold 29 · override 27 · resume 23 · handoff 16 · abort 16
$ grep -c 'keepalive-reaped: yes' RUN*.md                   → 96 of 98
$ stop.*.log decisions (8 logs, 184 lines)                  → allow: background-tasks 118 · terminal 57 · held 3 · unreadable 1
                                                              block: run-open 3 · landing-unstamped 2
$ stall.*.log (1 log, 115 lines)                            → rate_limit 112 · server_error 3
$ find .git -name 'resume.*.log' -path '*unattended*'       → 0   (the resume tick has never launched)
$ check-playbook.sh --counts                                → population 1 playbook (the kit fixture) · pieces 2
```

| Function | What it does | Measured use | file:line |
|---|---|---|---|
| Position ladder (`--plan`, `--status`, `--phase`) | grades units and phase | the seed of `next`; byte-stable | unattended.sh:5785, 8038, 5998 |
| Authorization (`--preflight`, `--authorization`; ANCHOR_SCOPE, AUTH_PARAM) | the build folder or prompt record is the mandate | 98 runs | unattended.sh:7204, 10602; PROTOCOL:19 |
| Dispatch, brief, rescope | pass write set, handed brief, roster amendment | 1297 / 757 / 398 | unattended.sh:13447, 12858, 13159 |
| Review rounds (`--review`) | audit and closing-review round record | 356 | unattended.sh:12532 |
| Definition of Done (`--close`, `dod_met`), override, waive | 13-item exit, with overrides and waivers | override 27; waive 79 hits | unattended.sh:10624, 10957; PROTOCOL:340 |
| Park, attest, propose | owner-call parking, typed attestations, playbook amendments | ## Parked in 98/98 (0 entries); attest 10; propose 8 | unattended.sh:12731, 12436, 12799 |
| Hold, resume, abort, handoff, settle, landed | stop and terminal controls | 29 / 23 / 16 / 16 / 24 hits / 75 | unattended.sh:6711, 9008, 6541, 6988, 7070, 6179; STOPS:15-674 |
| Lease and liveness (`--liveness`, `--beat`, `--claims`, `--overlaps`; RUN_CLAIMS) | session lease, remote claim, overlap warning | claim-lost 1 | unattended.sh:8671, 2469, 3523; STOPS:170 |
| Task register and audit | heartbeats for background tasks, STALLED detection | 4 tasks.tsv | unattended.sh:8435, 8313 |
| Keepalive (CronCreate) | in-session idle-wake | 96/98 runs | SKILL.md:16; PROTOCOL:379 |
| Durable restart (RESUME_SCHEDULE_*) | desktop restart task | conf `on` | STOPS:356 |
| resume-tick.sh | OS-scheduled out-of-process resumer | 0 launches | resume-tick.sh:1-40, 385 (`--dangerously-skip-permissions`) |
| gate-guard.js | refuses the flagged bar and self-tests before VERIFYING; refuses AskUserQuestion from the lease holder | no journal of its own | gate-guard.js:4-5, 128, 131 |
| stop-guard.js | blocks a turn end on an open run | 5 blocks / 184 | stop-guard.js:1-38 |
| stall-recorder.js | records StopFailure | 115 lines | stall-recorder.js:19 |
| run-lease.js | binds a session to RUN.md | shared by the three hooks | run-lease.js:21 |
| Recipe: `--record-piece`, `--record-set`, check-playbook leg | piece and set records, playbook canon | 0 recipe runs; population 1 | unattended.sh:13113, 13090; check-playbook.sh |
| Legs: kit gate, pass-order, brief-recorded, skill wiring | repository checks | on the bar | kit.toml `[[gate_leg]]` |
| Run record (`write_run_record`) | renders the run record at close | every terminal run | unattended.sh:14048 |
| Asks routing | mandated asks, discovery filing | 2 READMEs | ASKS:17-173 |
| Directive set, adoption rule, driven pass sequence | M-rule handles; discoveries join the build | 17 handles | PROTOCOL:597, 640, 692; SKILL.md:39-57 |

**Where a record and the code disagree**
- `README.md:57` and `.claude/rules/product.md:30` say "four-verb driver". The code declares 30 verbs (unattended.sh:111, 114). layer-runtime:124 says 30, which matches the code.
- layer-runtime:142-149 counts 75 landed and 13 aborted. That matches the code (57 LANDED + 18 LANDING).

## 3. Homes

| Function | Home: build · carrier |
|---|---|
| Position ladder | dDeclaredLoop · position engine; dWellOiledMachine · `next` (layer-runtime:315-352) |
| Authorization | dRankedPlan · `plan.ratification` through the intake record; dWellOiledMachine · `entry.intake`. ANCHOR_SCOPE and AUTH_PARAM: **no home** (retire) |
| Dispatch, brief | dBoundRoles · work order and allowance; dWellOiledMachine · act binding (layer-runtime:459-504) |
| Rescope | dDeclaredLoop · Design re-entry and amend, P19 new units |
| Review rounds | dDeclaredLoop and dFairHearing · `review.*` breakpoint items (flow-steps:444-453) |
| Definition of Done | dDeclaredLoop · step exit items (gap-spine-03) |
| Override, waive | dDeclaredLoop · `core.exceptions` register |
| Park | dBoundRoles · `run.on-owner-question`, owner item |
| Attest | **no home**. It is an agent-typed witness, which P2 forbids, so it retires |
| Propose | **no home** (see §6) |
| Hold, resume, abort | dWellOiledMachine · `life.*` (flow-steps:469-486) |
| Handoff | dShippedRelease · the landing owner gate (`three-gates`) or the release hold. **Partial** |
| Settle, landed | dDeclaredLoop · `terminal` answer; dShippedRelease · landing record |
| Lease, liveness, claims, overlaps | dDeclaredLoop · lease grammar; dWellOiledMachine · supervisor beat |
| Task register and audit | dWellOiledMachine · `runtime.act-ceiling` and reap |
| Keepalive, durable restart, stop-guard | retired (layer-runtime:783-785, 1026-1033, 600) |
| resume-tick | dWellOiledMachine · the supervisor's seam (layer-runtime:356-363) |
| gate-guard | dWellOiledMachine · run-guard pack (layer-runtime:595) |
| stall-recorder | dWellOiledMachine · limit signal |
| run-lease.js | dWellOiledMachine · session binding record |
| Recipe verbs, check-playbook | **no home in the chain**. v2:1198 says "never a recipe-mode playbook" |
| Legs | pass-order and brief-recorded: dBoundRoles' shape-run and work-order hash. Kit gate: split across the stage coverage gates. Skill wiring: kit factory (dShippedRelease) |
| Run record | dWellOiledMachine · journal grammar; observability |
| Asks routing | dRankedPlan · triage (flow-steps:92-95) |
| Directives, adoption rule | dOrderedCharter · practice catalogue; P18 and `design.forks` |
| Protocol, VERBS, STOPS and ASKS guides | dConvergedCharter · protocol derived to facts, retired by ratified proposal |
| `.unattended.conf` (63 keys) | 10 `*_CUTOFF` keys retire with their checks; 8 keepalive and schedule keys retire; RESUME_ATTEMPTS, RESUME_TURNS → Runtime; REVIEW_ROUNDS retired by dDeclaredLoop; the gate and lander keys → command adapters. The rest stay on dGroundRules' shrink-only list until dConvergedCharter |

memory's `[tools]` map (layer-memory:858) says "flow ladder extracted into the loop kit". That is right but incomplete: the hooks, the supervisor and the controls go to dWellOiledMachine, and the recipe half has no home.

## 4. Attended as an override

**Places where design text lets attended change flow or role use**

| Where | What changes |
|---|---|
| layer-runtime:300-301, 311, 346; roles:135; v2:593-595 (P25) | **The driver.** Attended, the owner's session drives; unattended, the supervisor |
| layer-runtime:501-504 | **Role use.** The attended session "keeps its freedom". Act binding and allowances do not bind it, so P25 is unenforced when attended |
| layer-runtime:433-436 | Slot reservation refuses rather than queues |
| flow-steps:71, 78 | Intake only in "attended-bound" sessions |
| recut:197 | Before dWellOiledMachine lands, the attended session carries the build into Design |

**The same difference in today's code:** attended mode loses the review round record, the dispatch spec-state and order refusal, the write-set record, the brief record and the rescope row (`unattended-build.js:49-61`). Also:
- `/build` has the main loop flip INPROGRESS and run the bar (`.claude/skills/build/SKILL.md:61-62, 97-99`).
- The bar-before-VERIFYING guard binds only runs (`gate-guard.js:4`).
- Attended pieces get no Definition of Done (VERBS:657-668).
- The closing review ran on 29 of 59 attended builds against 86 of 89 unattended ones (gap-build-02).

**What changes**

| Kind | Change |
|---|---|
| Keys | `autonomy` becomes the attendance switch. It may only place owner breakpoints and never select an owner-actor value. Add `notify.owner: announce-acts`. `run.on-owner-question` gains an attended reading: ask in the session, with best effort as the fallback. Rename `runtime.attended-judge` and `memory.default-load`'s "attended session" to "owner session" |
| Presets | Standard, velocity and guarded stay unattended. Strict's `every-stage` stays as a posture choice |
| Items | `life.request` gains attend and unattend. `entry.intake` is bound to the owner session, not to attendance. A new `entry.announce` hook item, or the micro-format below |
| Principles | P4 adds "attendance never changes items, actors or the driver". P20 changes to "unattended from entry". P25 changes to "the supervisor drives every build; the owner's session is a client" |
| Records | An attendance override record, written through the guarded command or an intake keyword. Charter `[land]` (AGENTS.md:31) drops "explicit ask or the unattended protocol" |

## 5. The announcement

| What exists | Where | What it gives |
|---|---|---|
| `next` answer | layer-runtime:329 | item, actor kind, work-order key, harness |
| Card `next —` cell | session-model:54 | the next command |
| Stage-exit recommendation | flow-steps:53-56 | score and reason, at step exits only |
| `notify.owner` | v2:792 | transitions and parks only |
| `agent —` and `BUILD —` micro-formats | AGENTS.md:61-65 | the role and step, reported after dispatch |

**Missing:**
1. A before-act explanation of step, item, role, why, write set and the owner's options, rendered from `next` and the item declaration and never typed by a model.
2. A per-act `notify.owner` value.
3. A micro-format, for example `step — <build> · <step> · <item> · <role> · <why> · writes <set>`.
4. In attended mode, an optional hold until the owner's disposition. This is the owner breakpoint.

## 6. Modes

| Mode | Start today | Decided by | What a prompt-driven driver must decide | Design carrier |
|---|---|---|---|---|
| slug | owner-landed README (32 runs) | owner | that the request continues a build | `entry.place` → `continue` (flow-steps:73) |
| prompt | prompt record, push, preflight (54 runs) | agent and one ask | new build, slug, brief, roster | `new` → `entry.claim` → Plan |
| ask (ids) | scaffold, owner lands README (2) | owner | triage of asks | Plan triage (flow-steps:92-95) |
| recipe | playbook and `pieces:` (0 runs) | owner | which playbook, how many pieces, where they go | **missing** |

**What the entry step and the driver already do:** they place, check, claim and route every prompt (flow-steps:65-90). The dDeclaredLoop row already says "an unattended prompt placed the same way" (v2:1188).

**What is missing:**
1. A `repeat` disposition.
2. Intake for a prompt that reaches no owner session, for example through the mailbox or a cadence.
3. Retiring ANCHOR_SCOPE and AUTH_PARAM.

**Playbook mode's place in the flow:**
- Authoring a playbook is an ordinary build. Its product is a playbook record kind owned by dIndexedDesign.
- Following one is placed as `repeat`. It enters Design as a patch build does, and the playbook supplies the feature design. The spec writer instantiates one unit per piece, and Test runs the set check.
- A cyclic playbook is a cadence item that files `repeat` intakes.

**What carries over from dScriptedRepeat:**
- the closed template canon (12 sections), derived from the template;
- the declaration block (outputs globs, grain, records, legs);
- piece records hash-joined to their pieces;
- a set identity derived from the piece hashes;
- the measure-the-set finding;
- playbook-older-than-BASE;
- amendment by proposal, never by edit, filed to Plan's triage;
- empty population reds.

## 7. Candidates

| # | Mechanism | Losing test, written first | Result |
|---|---|---|---|
| C1 | One driver (the supervisor). Attendance places owner breakpoints on the `autonomy` seam (flow-steps:435-438). The owner session is a client | (a) With attendance toggled, every flow-steps item's actor and the transition path stay identical, and breakpoints only add disposition records. (b) No attendance value selects an owner-actor key value | **Passes on records.** Breakpoints sit outside the step programs (flow-steps:50-52, 427-433), and mid-item questions route through `run.on-owner-question`. Open risk: dWellOiledMachine's spike (headless role-typed Workflow, layer-runtime:962). If the spike fails, C1 loses; that is the test the build must run |
| C2 | Session-bound attendance (v2 today) | Does attended change the driver or the enforcement? | **Loses.** layer-runtime:311, 501-504; code at unattended-build.js:49-61; gap-build-02 |
| C3 | A preset-like bundle over the owner-valued keys | Does any bundled key swap an item's actor? | **Loses.** About 30 of the 188 catalogue keys carry an owner option. `placement: owner-places` swaps the scout (flow-steps:73) for the owner (:75), and `plan.authority`, `landing.order` and `decisions.major` do the same. Pruned to keys that only add breakpoints, C3 becomes C1 |

**Playbook placement**

| Option | Losing test | Result |
|---|---|---|
| `repeat` disposition and design record kind | Can Design's exit witnesses be met from a playbook? | Untested; it is the build's test (dIndexedDesign) |
| Role harness following a playbook | Is every piece a witnessed item (P24)? | **Loses.** Pieces would be invisible to `next` |
| Cadence item alone | Does it cover "N pieces on request"? | **Loses** for on-demand runs; it covers cyclic runs only |

## 8. Chain, gaps and forks

**Units by build**

| Build | Unit |
|---|---|
| dDeclaredLoop | the attendance rule on `autonomy`, with the arm "attendance selects no actor"; the `repeat` disposition |
| dBoundRoles | the attended reading of `run.on-owner-question` |
| dWellOiledMachine | the supervisor as the only driver and the owner-session binding (rewriting layer-runtime:300-311, 501-504); `life.request` attend and unattend; the announce micro-format and `notify.owner: announce-acts`; intake for non-session prompts; the unattended skill as a client of `run`, then the kit and its four hooks repacked |
| dIndexedDesign | the playbook record kind: canon, declaration block, and check-playbook as Design's pack |
| dScopedBuild | piece units and piece records; proposals filed as asks |
| dWitnessedBar | the set record and set check at Test |
| dTendedCadence | the cyclic-playbook cadence filer |
| dOrderedCharter | drive section "unattended by default"; `[land]` rewritten |
| dRankedPlan | drop "attended briefs gated" and the READY confirmation |
| dConvergedCharter | retire the four UNATTENDED guides and the kit |

**Gaps to register**
1. Attendance is not one rule. About 30 owner-valued keys exist and nothing forbids an actor swap.
2. Attended changes the driver and binding (the runtime text above).
3. No before-act announcement exists.
4. Playbook mode has no chain home.
5. The term "attended" is overloaded (session kind against mode), and so is "playbook" (the `tools/playbook/` charter renderer against playbook mode).
6. A non-session prompt gets no intake.
7. The "four-verb driver" text is stale (README.md:57).

**Forks for the owner**

| Fork | Options | Recommendation |
|---|---|---|
| F1 Who drives when attended | supervisor always; owner session; owner session for entry and Plan | Supervisor always, with recut:197's interim kept until dWellOiledMachine lands |
| F2 What attended does | announce each act and confirm at step exits; confirm each act; announce only | Announce each act, confirm at step exits |
| F3 The switch | extend `autonomy`; a new `attendance` key; override request only | Extend `autonomy` and add the request |
| F4 Override scope | session; build; repository | Build, with the policy as the default |
| F5 Forks when attended | ask live with a best-effort timeout; best effort always | Ask live with the timeout |
| F6 Playbook home | `repeat` disposition and record kind; role harness; program kind | `repeat` and record kind |
| F7 Fate of `/unattended` | thin alias of `run`; retire at once | Alias, retired at dConvergedCharter |

The records I relied on are in `C:/projects/coding-governance/.claude/worktrees/gov-architecture-plan-e34297/memory/builds/dClosedLoop/build/`: architecture-v2, layer-runtime, flow-steps, flow-roles and roles. The code is under `tools/unattended/` and `tools/workflows/unattended-build.js`.
