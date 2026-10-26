---
slug: dWellOiledMachine
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44 TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-62
spec-audit: 2026-10-21
parents: dBoundRoles dTotalRecall dKeptSession
may: PLAY-dClosedLoop-3
---

# dWellOiledMachine — the Runtime build of the dClosedLoop chain

## The problem this build exists to solve

dWellOiledMachine owns 63 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-rt-01 to
gap-rt-21, gap-found-06, gap-flow-10, gap-tool-03, gap-orient-08, gap-orient-12, gap-orient-14, gap-conc-03,
gap-deploy-07, gap-rt-22, gap-rt-23, gap-rt-24, gap-orient-16, gap-orient-17, gap-orient-18, gap-rt-25, gap-rt-26,
gap-rt-27, gap-rt-28, gap-rt-29, gap-rt-30, gap-rt-31, gap-orient-19, gap-tool-14, gap-tool-16, gap-tool-18,
gap-rt-32, gap-rt-33, gap-conc-11, gap-rt-35, gap-mem-46, gap-rt-36, gap-rt-37, gap-rt-38, gap-rt-39, gap-conc-16,
gap-rt-40, gap-rt-41, gap-rt-42, gap-rt-43, gap-rt-44, gap-rt-45, gap-rt-46. Closing every one is this build's goal
bound.

## Expected improvements

- Each of the 61 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 63 owned gaps above close.

## Detriments if this is not built

- Its 63 owned gaps stay open.
- Its 4 child builds wait on it: dMindYourWords, dScopedBuild, dShippedRelease, dTendedCadence.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dWellOiledMachine` green before the first pass; a moved instrument
  blob is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dWellOiledMachine`, a record per member "recorded by nobody", the same with `--write`
  (commit it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again
  after a re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-15.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dWellOiledMachine-1` | `cl-dClosedLoop-0279@3b20f1d6` | the platform spike first: a role-typed Workflow agent run inside a headless act session |
| 2 | `TOOL-dWellOiledMachine-2` | `cl-dClosedLoop-0280@62ada92d` | the `next` verb over the loop kit's position function |
| 3 | `TOOL-dWellOiledMachine-3` | `cl-dClosedLoop-0281@b4f7b233` | the owner's pause |
| 4 | `TOOL-dWellOiledMachine-4` | `cl-dClosedLoop-0282@328da93b` | the prompt-submit hook writing each owner prompt verbatim to the session's intake log |
| 5 | `TOOL-dWellOiledMachine-5` | `cl-dClosedLoop-0283@b08404fd` | Plan's ratification and the placement dispositions re-pointed to the intake record where dRankedPlan has landed first |
| 6 | `TOOL-dWellOiledMachine-6` | `cl-dClosedLoop-0284@8ad94483` | the supervisor: `resume-tick.sh` grown |
| 7 | `TOOL-dWellOiledMachine-7` | `cl-dClosedLoop-0285@d2c4cd28` | act binding and the epoch check at the Workflow |
| 8 | `TOOL-dWellOiledMachine-8` | `cl-dClosedLoop-0286@459158b1` | the persisted-return store |
| 9 | `TOOL-dWellOiledMachine-9` | `cl-dClosedLoop-0287@1aa49fdd` | agent slots reserved under `runtime.agents-in-flight` |
| 10 | `TOOL-dWellOiledMachine-10` | `cl-dClosedLoop-0288@c845fe18` | the one enforcement surface: the kits' fragments as packs |
| 11 | `TOOL-dWellOiledMachine-11` | `cl-dClosedLoop-0289@dc7da053` | workspaces by `build.worktree` |
| 12 | `TOOL-dWellOiledMachine-12` | `cl-dClosedLoop-0290@b1905801` | sessions bound on every source |
| 13 | `TOOL-dWellOiledMachine-13` | `cl-dClosedLoop-0291@80055ca5` | the scheduler's host adapters and per-period cadence witnesses |
| 14 | `TOOL-dWellOiledMachine-14` | `cl-dClosedLoop-0292@7eaaf1a6` | harness adapters with capability tables |
| 15 | `TOOL-dWellOiledMachine-15` | `cl-dClosedLoop-0293@8132ebad` | the node registry's runtime facts |
| 16 | `TOOL-dWellOiledMachine-16` | `cl-dClosedLoop-0294@41b6d311` | the journal grammar moved into the core |
| 17 | `TOOL-dWellOiledMachine-17` | `cl-dClosedLoop-0295@2b8dd6cc` | the grant enforced on every adapter row |
| 18 | `TOOL-dWellOiledMachine-18` | `cl-dClosedLoop-0296@6f945b2c` | event waits woken by their record |
| 19 | `TOOL-dWellOiledMachine-19` | `cl-dClosedLoop-0297@c082d7d0` | act binding against the resolved shape's digest |
| 20 | `TOOL-dWellOiledMachine-20` | `cl-dClosedLoop-0298@0b701ed6` | the `hook` and `point` tag namespaces |
| 21 | `TOOL-dWellOiledMachine-21` | `cl-dClosedLoop-0299@1be73e25` | the hook-message and harness-prompt templates |
| 22 | `TOOL-dWellOiledMachine-22` | `cl-dClosedLoop-0300@8c17038e` | hook and point purposes |
| 23 | `TOOL-dWellOiledMachine-23` | `cl-dClosedLoop-0301@29109ea6` | the session-start hook loading the set `memory.default-load` names |
| 24 | `TOOL-dWellOiledMachine-24` | `cl-dClosedLoop-0302@0a747a85` | the journal's count of map reads outside a slice |
| 25 | `TOOL-dWellOiledMachine-25` | `cl-dClosedLoop-0303@b32fa809` | the supervisor the only driver in every mode |
| 26 | `TOOL-dWellOiledMachine-26` | `cl-dClosedLoop-0304@498bf1e8` | the `step —` announcement before each act while attended |
| 27 | `TOOL-dWellOiledMachine-27` | `cl-dClosedLoop-0305@f0329aee` | intake for a prompt that reaches no owner session |
| 28 | `TOOL-dWellOiledMachine-28` | `cl-dClosedLoop-0306@a3aa83b5` | the unattended kit dissolved into the loop kit and the runtime's own kit: its hooks repacked |
| 29 | `TOOL-dWellOiledMachine-29` | `cl-dClosedLoop-0307@7b420e28` | a measured `browser` row in each harness adapter's capability table |
| 30 | `TOOL-dWellOiledMachine-30` | `cl-dClosedLoop-0308@afc642fa` | act binding and shape-run rows for an experiment's acts (night pass |
| 31 | `TOOL-dWellOiledMachine-31` | `cl-dClosedLoop-0309@3da1a616` | a hook pack's refusal text |
| 32 | `TOOL-dWellOiledMachine-32` | `cl-dClosedLoop-0310@6e643d4a` | the act as the key: minted at launch with the harness session id |
| 33 | `TOOL-dWellOiledMachine-33` | `cl-dClosedLoop-0311@d9f33c79` | the commit queue writing the `Gov-*` trailers from the act binding |
| 34 | `TOOL-dWellOiledMachine-34` | `cl-dClosedLoop-0312@60d68fcb` | `gov trace <key>` and `gov why <key>` over the one index |
| 35 | `TOOL-dWellOiledMachine-35` | `cl-dClosedLoop-0313@ab83255b` | the session node derived from bindings |
| 36 | `TOOL-dWellOiledMachine-36` | `cl-dClosedLoop-0314@12a43ed3` | the harness conformance fixture: launch by a program |
| 37 | `TOOL-dWellOiledMachine-37` | `cl-dClosedLoop-0315@b5839378` | preflight refusing a launch that skips hooks or permissions |
| 38 | `TOOL-dWellOiledMachine-38` | `cl-dClosedLoop-0316@8f48a4b0` | the per-session orientation card retired into the session binding: the write gate's card and route reads |
| 39 | `TOOL-dWellOiledMachine-39` | `cl-dClosedLoop-0317@9d62f0b1` | every act's minimal binding record (act id |
| 40 | `TOOL-dWellOiledMachine-40` | `cl-dClosedLoop-0318@800a78ec` | the commit queue committing each role return into the build's trail at its item's witness and pushing the build's branch as `build.push` says |
| 41 | `TOOL-dWellOiledMachine-41` | `cl-dClosedLoop-0319@2ffabe1b` | a unit of a leased build offered at placement to another session or node as `build.unit-holders` says |
| 42 | `TOOL-dWellOiledMachine-42` | `cl-dClosedLoop-0320@2dda5d80` | `gov-session` retired with an upgrade step: a hand-off to another session becomes an `intake` message or a unit offered at placement |
| 43 | `TOOL-dWellOiledMachine-43` | `cl-dClosedLoop-0321@f02a952d` | the in-flight ledger: a hook pack claiming a slot keyed by agent id at SubagentStart and releasing it at SubagentStop |
| 44 | `TOOL-dWellOiledMachine-44` | `cl-dClosedLoop-0322@a00b6c23` | the memory-mirror point: an adapter registered there |
| 45 | `TOOL-dWellOiledMachine-45` | `cl-dClosedLoop-0323@eafe421b` | the admission queue: every agent spawn and Workflow call a driver |
| 46 | `TOOL-dWellOiledMachine-46` | `cl-dClosedLoop-0324@1b8963c8` | the progress ledger per item instance: each act recording a new witness |
| 47 | `TOOL-dWellOiledMachine-47` | `cl-dClosedLoop-0325@54802c5c` | every wait the supervisor holds given its deadline and outcome: the session-limit hold releasing every lease the supervisor holds for the build |
| 48 | `TOOL-dWellOiledMachine-48` | `cl-dClosedLoop-0326@9cee3bd1` | owner items |
| 49 | `TOOL-dWellOiledMachine-49` | `cl-dClosedLoop-0327@e342bb96` | the refusal breaker: every refusal journaled with its rule |
| 50 | `TOOL-dWellOiledMachine-50` | `cl-dClosedLoop-0328@ff7cfaee` | the wait graph across builds |
| 51 | `TOOL-dWellOiledMachine-51` | `cl-dClosedLoop-0329@4e8f519b` | each build's spend recorded from its `trace.cost` rows and trended |
| 52 | `TOOL-dWellOiledMachine-52` | `cl-dClosedLoop-0330@9b33b8bb` | the node beat: the supervisor's beat |
| 53 | `TOOL-dWellOiledMachine-53` | `cl-dClosedLoop-0331@df99638c` | admission under `runtime.admission-scope` |
| 54 | `TOOL-dWellOiledMachine-54` | `cl-dClosedLoop-0332@aef236e5` | discovery and the pick: one read giving a project's claimable ready set across its builds |
| 55 | `TOOL-dWellOiledMachine-55` | `cl-dClosedLoop-0333@dce4872c` | the transport points in Runtime's `[extend]`: a lease store |
| 56 | `TOOL-dWellOiledMachine-56` | `cl-dClosedLoop-0334@4fe16106` | `runtime.act-harness` and `runtime.act-auth` resolved per role through Roles' resolver |
| 57 | `TOOL-dWellOiledMachine-57` | `cl-dClosedLoop-0335@523e4c44` | the secret scan covering lease |
| 58 | `TOOL-dWellOiledMachine-58` | `cl-dClosedLoop-0505@d65ddfae` | the record door |
| 59 | `TOOL-dWellOiledMachine-59` | `cl-dClosedLoop-0336@cd3fcb78` | a cadence run |
| 60 | `TOOL-dWellOiledMachine-60` | `cl-dClosedLoop-0337@91e18a60` | the commit queue and the lander pushing through dPlacedRequest's fenced effect push |
| 61 | `TOOL-dWellOiledMachine-61` | `cl-dClosedLoop-0338@3c1ea0eb` | the node profile |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 30 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-2 TOOL-dWellOiledMachine-3 TOOL-dWellOiledMachine-4 TOOL-dWellOiledMachine-5 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-7 TOOL-dWellOiledMachine-8 TOOL-dWellOiledMachine-9 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11
ids TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-18 TOOL-dWellOiledMachine-19 TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22
ids TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-24 TOOL-dWellOiledMachine-25 TOOL-dWellOiledMachine-26 TOOL-dWellOiledMachine-27 TOOL-dWellOiledMachine-28 TOOL-dWellOiledMachine-29 TOOL-dWellOiledMachine-30 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33
ids TOOL-dWellOiledMachine-34 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38 TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-41 TOOL-dWellOiledMachine-42 TOOL-dWellOiledMachine-43 TOOL-dWellOiledMachine-44
ids TOOL-dWellOiledMachine-45 TOOL-dWellOiledMachine-46 TOOL-dWellOiledMachine-47 TOOL-dWellOiledMachine-48 TOOL-dWellOiledMachine-49 TOOL-dWellOiledMachine-50 TOOL-dWellOiledMachine-51 TOOL-dWellOiledMachine-52 TOOL-dWellOiledMachine-53 TOOL-dWellOiledMachine-54 TOOL-dWellOiledMachine-55
ids TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-59 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61 TOOL-dWellOiledMachine-62

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dWellOiledMachine-1 — the platform spike, the runtime kit it founds, and the one act launcher](spec/2026-10-26-spec-TOOL-dWellOiledMachine-1.md) | 1 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-16 — the journal grammar moved into the core, its runtime producer, and its retention by `runtime.journal`](spec/2026-10-26-spec-TOOL-dWellOiledMachine-16.md) | 2 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-61 — the node profile at the node's home: read whole, schema-checked both ways, written only by the owner's guarded command](spec/2026-10-26-spec-TOOL-dWellOiledMachine-61.md) | 3 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-20 — the `hook` and `point` tag namespaces, and the point registry they read](spec/2026-10-26-spec-TOOL-dWellOiledMachine-20.md) | 4 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-22 — hook and point purposes: a field on every member, and every existing member reviewed](spec/2026-10-26-spec-TOOL-dWellOiledMachine-22.md) | 5 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-17 — the grant enforced on every adapter row, and the secret value scan at every publishing boundary with its shape report beside it](spec/2026-10-26-spec-TOOL-dWellOiledMachine-17.md) | 6 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-14 — harness adapters with capability tables, measured and never claimed, and their install targets](spec/2026-10-26-spec-TOOL-dWellOiledMachine-14.md) | 7 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-13 — the scheduler's host adapters, the OS scheduler first, and per-period cadence witnesses](spec/2026-10-26-spec-TOOL-dWellOiledMachine-13.md) | 8 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-15 — the node registry's runtime facts, the clock offset measured at each beat and correcting a holder's stamp where a lease's expiry is judged](spec/2026-10-26-spec-TOOL-dWellOiledMachine-15.md) | 9 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-36 — the harness conformance fixture: each binary's rows measured into the capability table and the node registry, read by `runtime.binary`, `runtime.owner-harness` and `runtime.act-harness`](spec/2026-10-26-spec-TOOL-dWellOiledMachine-36.md) | 10 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-10 — the one enforcement surface: the kits' fragments as packs behind one dispatcher entry per event, failing closed](spec/2026-10-26-spec-TOOL-dWellOiledMachine-10.md) | 11 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-31 — a hook pack's refusal text: its rule, remedy and actor declared in the pack contract and checked at registration](spec/2026-10-26-spec-TOOL-dWellOiledMachine-31.md) | 12 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-21 — the hook-message and harness-prompt templates: hook text and Workflow prompts as slot-line templates over registered units](spec/2026-10-26-spec-TOOL-dWellOiledMachine-21.md) | 13 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-2 — the `next` verb over the position function, the `next —` micro-format, and every declared command ending with one](spec/2026-10-26-spec-TOOL-dWellOiledMachine-2.md) | 14 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-32 — the act as the key: minted at launch with the harness session id, its record, its cost and duration, and the identity committed records may carry](spec/2026-10-26-spec-TOOL-dWellOiledMachine-32.md) | 15 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-39 — every act's minimal binding record pushed to `refs/gov/bindings`, and one reader over `<current default>..HEAD` that never passes a binding it cannot find](spec/2026-10-26-spec-TOOL-dWellOiledMachine-39.md) | 16 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-12 — sessions bound on every source, a card never silently undelivered, and each compaction flushed, journaled and re-oriented](spec/2026-10-26-spec-TOOL-dWellOiledMachine-12.md) | 17 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-38 — the per-session orientation card retired into the session binding, with the write gate's card and route reads re-pointed in the same unit](spec/2026-10-26-spec-TOOL-dWellOiledMachine-38.md) | 18 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-23 — the session-start hook loading the set `memory.default-load` names, ending with `next`'s line, held under the hook channel's measured cap](spec/2026-10-26-spec-TOOL-dWellOiledMachine-23.md) | 19 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-11 — workspaces by `build.worktree`: the allocator, the commit queue, integration before release, and a sweep that reaps only what it allocated](spec/2026-10-26-spec-TOOL-dWellOiledMachine-11.md) | 20 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-33 — the `Gov-*` trailers written from the binding at every commit site, and the commit-key check at the push and in `commit-msg`](spec/2026-10-26-spec-TOOL-dWellOiledMachine-33.md) | 21 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-35 — the session node derived from bindings: `runs-in` and `after`, acts and sessions as native-id classes, the live inbox and the card's session list](spec/2026-10-26-spec-TOOL-dWellOiledMachine-35.md) | 22 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-40 — the commit queue pushes the build's branch as `build.push` says, taking no lander lock and running no bar but a declared branch bar](spec/2026-10-26-spec-TOOL-dWellOiledMachine-40.md) | 23 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-55 — the transport points in Runtime's `[extend]`: a lease store with git refs its only adapter and its conformance probes, a doorbell, and an offer source](spec/2026-10-26-spec-TOOL-dWellOiledMachine-55.md) | 24 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-60 — the landing, its lease beat and its `landed` notice in one atomic push, and the commit queue's push through the same fence](spec/2026-10-26-spec-TOOL-dWellOiledMachine-60.md) | 25 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-58 — the record door: every coordination write bound to its writer's session binding, and the two closing items it admits](spec/2026-10-26-spec-TOOL-dWellOiledMachine-58.md) | 26 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-57 — the secret scan over coordination payloads and adapter boundaries, the door's token-shape refusal, and the request record bound to its intake](spec/2026-10-26-spec-TOOL-dWellOiledMachine-57.md) | 27 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-6 — the supervisor: `resume-tick.sh` grown into the executor's seam, one act session per role act, relaunch by policy, and a reconcile before the first beat](spec/2026-10-26-spec-TOOL-dWellOiledMachine-6.md) | 28 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-37 — the launch preflight: no hook- or permission-skipping launch, trusted hooks by hash, an allowlisted environment, the credential order, and relative worktree pointers](spec/2026-10-26-spec-TOOL-dWellOiledMachine-37.md) | 29 | 2 | OPEN | rev-1 | 2026-10-26 |
| [TOOL-dWellOiledMachine-56 — the act's harness and credential resolved per role through Roles' resolver, a harness row for how it reads the credential, and the launch pinned out of bare mode](spec/2026-10-26-spec-TOOL-dWellOiledMachine-56.md) | 30 | 2 | OPEN | rev-1 | 2026-10-26 |
<!-- /gen:build-units -->

Records: 11 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dWellOiledMachine-1 TOOL-dWellOiledMachine-10 TOOL-dWellOiledMachine-11 TOOL-dWellOiledMachine-12 TOOL-dWellOiledMachine-13 TOOL-dWellOiledMachine-14 TOOL-dWellOiledMachine-15 TOOL-dWellOiledMachine-16 TOOL-dWellOiledMachine-17 TOOL-dWellOiledMachine-2
TOOL-dWellOiledMachine-20 TOOL-dWellOiledMachine-21 TOOL-dWellOiledMachine-22 TOOL-dWellOiledMachine-23 TOOL-dWellOiledMachine-31 TOOL-dWellOiledMachine-32 TOOL-dWellOiledMachine-33 TOOL-dWellOiledMachine-35 TOOL-dWellOiledMachine-36 TOOL-dWellOiledMachine-37 TOOL-dWellOiledMachine-38
TOOL-dWellOiledMachine-39 TOOL-dWellOiledMachine-40 TOOL-dWellOiledMachine-55 TOOL-dWellOiledMachine-56 TOOL-dWellOiledMachine-57 TOOL-dWellOiledMachine-58 TOOL-dWellOiledMachine-6 TOOL-dWellOiledMachine-60 TOOL-dWellOiledMachine-61.

Ids whose spec moved past its audited revision: none — 0 of 30 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dWellOiledMachine's 61 clause(s) and 69 owned node(s), over 30 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 30
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 31 (cl-dClosedLoop-0281, cl-dClosedLoop-0282, cl-dClosedLoop-0283, cl-dClosedLoop-0285, cl-dClosedLoop-0286, cl-dClosedLoop-0287, cl-dClosedLoop-0296, cl-dClosedLoop-0297, cl-dClosedLoop-0302, cl-dClosedLoop-0303, cl-dClosedLoop-0304, cl-dClosedLoop-0305, cl-dClosedLoop-0306,
  cl-dClosedLoop-0307, cl-dClosedLoop-0308, cl-dClosedLoop-0312, cl-dClosedLoop-0319, cl-dClosedLoop-0320, cl-dClosedLoop-0321, cl-dClosedLoop-0322, cl-dClosedLoop-0323, cl-dClosedLoop-0324, cl-dClosedLoop-0325, cl-dClosedLoop-0326, cl-dClosedLoop-0327, cl-dClosedLoop-0328, cl-dClosedLoop-0329,
  cl-dClosedLoop-0330, cl-dClosedLoop-0331, cl-dClosedLoop-0332, cl-dClosedLoop-0336)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.entry.intake, item.life.close, item.life.notify, item.life.request, item.life.snapshot, point.actor-kinds, point.cadence-items, point.memory-mirrors, point.notification-adapters, point.role-harnesses, policy-key.attendance.scope, policy-key.build.spend-cap,
  policy-key.build.unit-holders, policy-key.memory.mirror, policy-key.notify.channel, policy-key.notify.owner-items, policy-key.roles.shape-enforce, policy-key.run.on-owner-silence, policy-key.run.owner-deadline, policy-key.runtime.act-ceiling, policy-key.runtime.admission-scope,
  policy-key.runtime.hold-ceiling, policy-key.runtime.no-progress, policy-key.runtime.refusal-repeats, policy-key.runtime.restarts, policy-key.trace.rows, record-kind.attendance-override, record-kind.intake, record-kind.lifecycle-request, record-kind.node-ledger, record-kind.return
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0283, cl-dClosedLoop-0285, cl-dClosedLoop-0286, cl-dClosedLoop-0290, cl-dClosedLoop-0291, cl-dClosedLoop-0292, cl-dClosedLoop-0296, cl-dClosedLoop-0299, cl-dClosedLoop-0300, cl-dClosedLoop-0302, cl-dClosedLoop-0308, cl-dClosedLoop-0309,
  cl-dClosedLoop-0330, cl-dClosedLoop-0335, cl-dClosedLoop-0337, cl-dClosedLoop-0338
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dWellOiledMachine-1` | no |
| 2 | `TOOL-dWellOiledMachine-16` | no |
| 3 | `TOOL-dWellOiledMachine-61` | no |
| 4 | `TOOL-dWellOiledMachine-20` | no |
| 5 | `TOOL-dWellOiledMachine-22` | no |
| 6 | `TOOL-dWellOiledMachine-17` | no |
| 7 | `TOOL-dWellOiledMachine-14` | no |
| 8 | `TOOL-dWellOiledMachine-13` | no |
| 9 | `TOOL-dWellOiledMachine-15` | no |
| 10 | `TOOL-dWellOiledMachine-36` | no |
| 11 | `TOOL-dWellOiledMachine-10` | no |
| 12 | `TOOL-dWellOiledMachine-31` | no |
| 13 | `TOOL-dWellOiledMachine-21` | no |
| 14 | `TOOL-dWellOiledMachine-2` | no |
| 15 | `TOOL-dWellOiledMachine-32` | no |
| 16 | `TOOL-dWellOiledMachine-39` | no |
| 17 | `TOOL-dWellOiledMachine-12` | no |
| 18 | `TOOL-dWellOiledMachine-38` | no |
| 19 | `TOOL-dWellOiledMachine-23` | no |
| 20 | `TOOL-dWellOiledMachine-11` | no |
| 21 | `TOOL-dWellOiledMachine-33` | no |
| 22 | `TOOL-dWellOiledMachine-35` | no |
| 23 | `TOOL-dWellOiledMachine-40` | no |
| 24 | `TOOL-dWellOiledMachine-55` | no |
| 25 | `TOOL-dWellOiledMachine-60` | no |
| 26 | `TOOL-dWellOiledMachine-58` | no |
| 27 | `TOOL-dWellOiledMachine-57` | no |
| 28 | `TOOL-dWellOiledMachine-6` | no |
| 29 | `TOOL-dWellOiledMachine-37` | no |
| 30 | `TOOL-dWellOiledMachine-56` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBoundRoles](../dBoundRoles/README.md), [dKeptSession](../dKeptSession/README.md), [dTotalRecall](../dTotalRecall/README.md)
- **Child builds:** [dMindYourWords](../dMindYourWords/README.md), [dScopedBuild](../dScopedBuild/README.md), [dShippedRelease](../dShippedRelease/README.md), [dTendedCadence](../dTendedCadence/README.md)
<!-- /gen:build-edges -->
