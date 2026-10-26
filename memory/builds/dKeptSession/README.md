---
slug: dKeptSession
node: d
opened: 2026-10-21
streams: kickoff
roster: KICK
ids: KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-29 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65
spec-audit: 2026-10-21
parents: dDeclaredLoop dPlacedRequest
may: PLAY-dClosedLoop-3
---

# dKeptSession — the Session build of the dClosedLoop chain

## The problem this build exists to solve

dKeptSession owns 8 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-flow-06,
gap-orient-06, gap-flow-16, gap-spine-10, gap-conc-04, gap-conc-05, gap-conc-09, gap-conc-15. Closing every one is
this build's goal bound.

## Expected improvements

- Each of the 28 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 8 owned gaps above close.

## Detriments if this is not built

- Its 8 owned gaps stay open.
- Its 2 child builds wait on it: dWellOiledMachine, dIndexedDesign.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dKeptSession` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dKeptSession`, a record per member "recorded by nobody", the same with `--write` (commit it
  as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `KICK-dKeptSession-1` | `cl-dClosedLoop-0139@065e06ab` | the named presets and their completeness check |
| 2 | `KICK-dKeptSession-2` | `cl-dClosedLoop-0140@6531184d` | the preset step added to dGroundRules's reader |
| 3 | `KICK-dKeptSession-3` | `cl-dClosedLoop-0141@4d07a3de` | the charter's preset section |
| 4 | `KICK-dKeptSession-4` | `cl-dClosedLoop-0142@816ff525` | policy at govkit intake |
| 5 | `KICK-dKeptSession-5` | `cl-dClosedLoop-0143@cafeb575` | the mailbox per build |
| 6 | `KICK-dKeptSession-6` | `cl-dClosedLoop-0144@c41201f3` | live delivery where the harness has it |
| 7 | `KICK-dKeptSession-7` | `cl-dClosedLoop-0145@b38efe3e` | dependency coordination by the parent's lease as `deps.coordination` says |
| 8 | `KICK-dKeptSession-8` | `cl-dClosedLoop-0146@a9c32df5` | `actions.free` at the tool call |
| 9 | `KICK-dKeptSession-9` | `cl-dClosedLoop-0147@9a464fcd` | orientation cost recorded per stage and held as `orient.budget` says |
| 10 | `KICK-dKeptSession-10` | `cl-dClosedLoop-0148@ab3d7b8c` | the mailbox read at every item boundary by `mailbox.reads` |
| 11 | `KICK-dKeptSession-11` | `cl-dClosedLoop-0149@d9aa0a3a` | progress reported by `notify.owner` |
| 12 | `KICK-dKeptSession-12` | `cl-dClosedLoop-0150@1c3b5ca1` | a fresh session in the build's worktree recommended until the card-import fixture passes |
| 13 | `KICK-dKeptSession-13` | `cl-dClosedLoop-0151@32b6ed5a` | the card's pointers updated as the build progresses |
| 14 | `KICK-dKeptSession-14` | `cl-dClosedLoop-0152@da455c7f` | what a session does as its window fills |
| 15 | `KICK-dKeptSession-15` | `cl-dClosedLoop-0153@9a9b7d43` | a compaction's summary read as a lead |
| 16 | `KICK-dKeptSession-16` | `cl-dClosedLoop-0154@62e72743` | the policy namespaces' purposes |
| 17 | `KICK-dKeptSession-17` | `cl-dClosedLoop-0155@6d913746` | the attendance rule: `attendance` places owner breakpoints and has owner questions asked live |
| 18 | `KICK-dKeptSession-18` | `cl-dClosedLoop-0156@c935df77` | the `repeat` disposition in the placement set and its `none` row in the transition table |
| 19 | `KICK-dKeptSession-19` | `cl-dClosedLoop-0157@7d569b91` | the catalogue's reader join: every key named by a unit on its owner build's row |
| 20 | `KICK-dKeptSession-20` | `cl-dClosedLoop-0158@19d3fbd9` | a scenario's preset slot: a named preset and overrides scoped to the builds placed under the scenario |
| 21 | `KICK-dKeptSession-21` | `cl-dClosedLoop-0159@ad40c608` | news shown as `mailbox.notice` says |
| 22 | `KICK-dKeptSession-22` | `cl-dClosedLoop-0160@3e3e0128` | each message's id derived from its build |
| 23 | `KICK-dKeptSession-23` | `cl-dClosedLoop-0161@10c6cad1` | every mail write appended to the change feed once its ref update lands |
| 24 | `KICK-dKeptSession-24` | `cl-dClosedLoop-0162@6ce67958` | a message awaiting an answer declaring `flow.wait-ceiling` as its deadline |
| 25 | `KICK-dKeptSession-25` | `cl-dClosedLoop-0504@b051ecfa` | `mailbox.answer`: a `question` addressed to a build answered by the role that owns the asked interface or item |
| 26 | `KICK-dKeptSession-26` | `cl-dClosedLoop-0163@709e57f9` | the card showing the build's remaining rework budget beside its pointers |
| 27 | `KICK-dKeptSession-27` | `cl-dClosedLoop-0164@148f5fda` | each message carrying its session's sequence number |
| 28 | `KICK-dKeptSession-28` | `cl-dClosedLoop-0165@8c92ee12` | a mailbox recipient naming a node by its fleet tag |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** DEFERRED · 64 unit(s) · node d · opened 2026-10-21 · streams kickoff
ids KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14
ids KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28
ids KICK-dKeptSession-29 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42
ids KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56
ids KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [KICK-dKeptSession-1 — the named presets as data, their completeness check, pair rules and core-only load](spec/2026-10-26-spec-KICK-dKeptSession-1.md) | 1 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-19 — the catalogue's reader join, and the shrink-only list factory it extracts](spec/2026-10-26-spec-KICK-dKeptSession-19.md) | 2 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [KICK-dKeptSession-33 — the preset store's rule for the derived-default rows: unassigned where v2 restates the default, literal where a preset differs](spec/2026-10-26-spec-KICK-dKeptSession-33.md) | 2 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-2 — the preset step in dGroundRules' reader](spec/2026-10-26-spec-KICK-dKeptSession-2.md) | 3 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-3 — the charter's preset section: the posture and only the keys that differ](spec/2026-10-26-spec-KICK-dKeptSession-3.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-34 — the reader's preset step answers None for a row the preset leaves unassigned, so a derived default reads with source default under every preset](spec/2026-10-26-spec-KICK-dKeptSession-34.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-40 — the preset store a recorded input of the JSON mirror, so a changed preset reads the mirror stale](spec/2026-10-26-spec-KICK-dKeptSession-40.md) | 4 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-4 — the preset asked once at govkit intake and written into the scaffolded policy file](spec/2026-10-26-spec-KICK-dKeptSession-4.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-49 — the JS mirror reader takes the inputs it compares from its own code, so a mirror missing the preset store reads stale](spec/2026-10-26-spec-KICK-dKeptSession-49.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-50 — the mirror's upgrade path observed on a pre-unit mirror: re-rendered by the kit's update, and refused by its check where the update skips it](spec/2026-10-26-spec-KICK-dKeptSession-50.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-54 — an unassigned derived row keeps dGroundRules' refusal in `get`, and its value is read through the caps module](spec/2026-10-26-spec-KICK-dKeptSession-54.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-20 — a scenario's preset slot, scoped to the builds placed under it](spec/2026-10-26-spec-KICK-dKeptSession-20.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-32 — the scaffold writes only the keys the named preset leaves unassigned, so a preset answered at intake is the posture the adopter reads](spec/2026-10-26-spec-KICK-dKeptSession-32.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-58 — the derived cap's row compared on its value and source, its mode read as strict sets it](spec/2026-10-26-spec-KICK-dKeptSession-58.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-59 — the JS reader's kit inputs held equal to the Python mirror's by a parity case](spec/2026-10-26-spec-KICK-dKeptSession-59.md) | 6 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [KICK-dKeptSession-60 — the policy kit's rule for a new mirror input names both lists and the case that holds them equal](spec/2026-10-26-spec-KICK-dKeptSession-60.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-16 — the policy namespaces' purposes, reviewed as `memory.map-purpose`'s default says](spec/2026-10-26-spec-KICK-dKeptSession-16.md) | 7 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-12 — a fresh session in the build's worktree recommended until the card-import fixture passes](spec/2026-10-26-spec-KICK-dKeptSession-12.md) | 8 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-13 — the card's pointers, updated at every item boundary by `card.pointers`](spec/2026-10-26-spec-KICK-dKeptSession-13.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-37 — the card-fixture verdict records the version of the claude binary the fixture launched, never the session's environment](spec/2026-10-26-spec-KICK-dKeptSession-37.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-38 — the card-fixture verdict passes only while the tested binary is both PATH's and the session's, and an unknown version is red](spec/2026-10-26-spec-KICK-dKeptSession-38.md) | 9 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-26 — the card showing the build's remaining rework budget beside its pointers](spec/2026-10-26-spec-KICK-dKeptSession-26.md) | 10 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [KICK-dKeptSession-15 — a compaction's summary read as a lead, never a source](spec/2026-10-26-spec-KICK-dKeptSession-15.md) | 11 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [KICK-dKeptSession-14 — what a session does as its window fills, by `context.on-full` and `context.threshold`](spec/2026-10-26-spec-KICK-dKeptSession-14.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-30 — the context window derived per model from the node's observed usage, never pinned at 200000](spec/2026-10-26-spec-KICK-dKeptSession-30.md) | 13 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-9 — orientation cost recorded per stage and held as `orient.budget` says](spec/2026-10-26-spec-KICK-dKeptSession-9.md) | 13 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [KICK-dKeptSession-28 — a mailbox recipient names a build, a unit, a node by its fleet tag, or the whole project](spec/2026-10-26-spec-KICK-dKeptSession-28.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-45 — the window scan's default root resolved by `resolve_projects_root`, never a literal profile path](spec/2026-10-26-spec-KICK-dKeptSession-45.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-46 — every fill reader passes the projects root it already resolved, so the window is derived under the tree the reader reads](spec/2026-10-26-spec-KICK-dKeptSession-46.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-47 — a compaction counts towards a model's window only when the session's last main usage before it is on that model](spec/2026-10-26-spec-KICK-dKeptSession-47.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-48 — the mixed-window limit stated, and a 200k session on a 1M-observed model read against its own window by the harness's variable](spec/2026-10-26-spec-KICK-dKeptSession-48.md) | 14 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-22 — each message's id derived from what it says, never from its sender's session, and a retried post refused across the build's session refs](spec/2026-10-26-spec-KICK-dKeptSession-22.md) | 15 | 2 | DEFERRED | rev-5 | 2026-10-26 |
| [KICK-dKeptSession-31 — the message id derived over its recipient and its content key, so two legitimate notices never share one id](spec/2026-10-26-spec-KICK-dKeptSession-31.md) | 16 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-5 — the mailbox per build: one append-only ref per writing session, closed kinds, read and disposed at every transition](spec/2026-10-26-spec-KICK-dKeptSession-5.md) | 16 | 2 | DEFERRED | rev-7 | 2026-10-26 |
| [KICK-dKeptSession-23 — every mail write appended to the change feed once its ref update lands, inside the feed's census](spec/2026-10-26-spec-KICK-dKeptSession-23.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-36 — the transition guard runs the driver through a bash that shares this filesystem, never the bare name, and an unresolved shell refuses](spec/2026-10-26-spec-KICK-dKeptSession-36.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-39 — `mailbox-message` a typed record kind, served as itself and joined to its file name both ways](spec/2026-10-26-spec-KICK-dKeptSession-39.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-51 — the act's place in the message id is the ninth field, after the recipient and the content key, in every text that states it](spec/2026-10-26-spec-KICK-dKeptSession-51.md) | 17 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [KICK-dKeptSession-27 — each message carrying its session's sequence number, a take-over its predecessor, and an interface notice its content key](spec/2026-10-26-spec-KICK-dKeptSession-27.md) | 18 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [KICK-dKeptSession-24 — a mail deadline judged by the observer clock: `flow.wait-ceiling` declared on each message, the asker's default past it](spec/2026-10-26-spec-KICK-dKeptSession-24.md) | 19 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [KICK-dKeptSession-10 — the mailbox read at every item boundary: `mailbox.reads` arming the position engine's mail interrupt, with the `intake` kind](spec/2026-10-26-spec-KICK-dKeptSession-10.md) | 20 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-25 — `mailbox.answer`: a `question` to a build answered by its owning role, or by the asker's default until `next` dispatches it, the waiting build's lease renewed](spec/2026-10-26-spec-KICK-dKeptSession-25.md) | 21 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-21 — news shown as `mailbox.notice` says: one bounded fetch at each item boundary, a tool-call hook reading the local copy, and the live ring's payload](spec/2026-10-26-spec-KICK-dKeptSession-21.md) | 22 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-6 — live delivery where the harness has it: the post's tail rings the channels `deps.messaging` picks, with only the ref and the id](spec/2026-10-26-spec-KICK-dKeptSession-6.md) | 23 | 2 | DEFERRED | rev-1 | 2026-10-26 |
| [KICK-dKeptSession-7 — dependency coordination: `deps.coordination` switching the dependency gate by the parent's lease, `deps.early-build` admitting Build, and the `confirmed`, `changed` and `landed` notices](spec/2026-10-26-spec-KICK-dKeptSession-7.md) | 24 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-35 — every dependency notice posted per dependent and per Design exit, so each one lands as its own message](spec/2026-10-26-spec-KICK-dKeptSession-35.md) | 25 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-42 — a dependent's transition acknowledges the notices it has consumed, so a parent's notice never holds the dependent until the wait ceiling](spec/2026-10-26-spec-KICK-dKeptSession-42.md) | 25 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-8 — `actions.free` at the tool call: every write, spawn, commit or push belongs to the item in flight](spec/2026-10-26-spec-KICK-dKeptSession-8.md) | 25 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-11 — progress reported by `notify.owner`: one `progress —` line at the events the value selects](spec/2026-10-26-spec-KICK-dKeptSession-11.md) | 26 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-43 — the `actions.free` arm reads every form of the item pointer, a skipped pointer leaving it unarmed and saying so](spec/2026-10-26-spec-KICK-dKeptSession-43.md) | 26 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-52 — the per-exit pass observed on a repeated interface, so dropping `--pass` prints a duplicate](spec/2026-10-26-spec-KICK-dKeptSession-52.md) | 26 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-53 — a consumed interface notice supersedes the parent's earlier rows by content key and by the session chain, never by arrival](spec/2026-10-26-spec-KICK-dKeptSession-53.md) | 26 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [KICK-dKeptSession-55 — the transition writer acknowledges notices only when the guard would then pass, and prints each one it consumed](spec/2026-10-26-spec-KICK-dKeptSession-55.md) | 26 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-17 — the attendance rule: `attendance` adds only the owner's interactions, its arm refusing any that swaps an actor](spec/2026-10-26-spec-KICK-dKeptSession-17.md) | 27 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-61 — the session chain read over every row on the parent's refs, so a parent with two dependents is placed](spec/2026-10-26-spec-KICK-dKeptSession-61.md) | 27 | 2 | DEFERRED | rev-4 | 2026-10-26 |
| [KICK-dKeptSession-18 — the `repeat` disposition and its `none` row, joined both ways to what the claim admits](spec/2026-10-26-spec-KICK-dKeptSession-18.md) | 28 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-41 — the three catalogue rows that already stand given their summary and usage, one row per name, never a second minted beside them](spec/2026-10-26-spec-KICK-dKeptSession-41.md) | 29 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-44 — the round-1 spec audit's 42 minor findings, closed after every unit they land on is built](spec/2026-10-26-spec-KICK-dKeptSession-44.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-56 — the round-1 promotions' audit's 45 minor findings, closed after every unit they land on is built](spec/2026-10-26-spec-KICK-dKeptSession-56.md) | 31 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-57 — the batch's pass-bound items observed at a pass that runs after them, never at an earlier unit's commit](spec/2026-10-26-spec-KICK-dKeptSession-57.md) | 32 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-62 — the round-2 promotions' audit's 32 minor findings, closed after every unit they land on is built](spec/2026-10-26-spec-KICK-dKeptSession-62.md) | 33 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [KICK-dKeptSession-63 — the round-3 promotions' audit's 26 minor findings, closed after every unit they land on is built](spec/2026-10-26-spec-KICK-dKeptSession-63.md) | 34 | 2 | DEFERRED | rev-3 | 2026-10-26 |
| [KICK-dKeptSession-64 — the round-4 minors batch's audit's 20 minor findings, closed after the batch they land on is built](spec/2026-10-26-spec-KICK-dKeptSession-64.md) | 35 | 2 | DEFERRED | rev-2 | 2026-10-26 |
| [KICK-dKeptSession-65 — the round-5 minors batch's audit's 26 minor findings, closed after the batch they land on is built](spec/2026-10-26-spec-KICK-dKeptSession-65.md) | 36 | 2 | DEFERRED | rev-1 | 2026-10-26 |
<!-- /gen:build-units -->

Records: 72 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: KICK-dKeptSession-65.

Ids whose spec moved past its audited revision: KICK-dKeptSession-1@rev-1 KICK-dKeptSession-10@rev-1 KICK-dKeptSession-11@rev-1 KICK-dKeptSession-12@rev-1 KICK-dKeptSession-13@rev-1 KICK-dKeptSession-14@rev-1 KICK-dKeptSession-16@rev-1 KICK-dKeptSession-17@rev-1 KICK-dKeptSession-18@rev-1
KICK-dKeptSession-2@rev-1 KICK-dKeptSession-20@rev-1 KICK-dKeptSession-21@rev-1 KICK-dKeptSession-22@rev-1 KICK-dKeptSession-23@rev-1 KICK-dKeptSession-25@rev-1 KICK-dKeptSession-27@rev-1 KICK-dKeptSession-28@rev-1 KICK-dKeptSession-3@rev-1 KICK-dKeptSession-30@rev-1 KICK-dKeptSession-31@rev-1
KICK-dKeptSession-32@rev-1 KICK-dKeptSession-33@rev-1 KICK-dKeptSession-34@rev-1 KICK-dKeptSession-35@rev-1 KICK-dKeptSession-36@rev-1 KICK-dKeptSession-37@rev-1 KICK-dKeptSession-38@rev-1 KICK-dKeptSession-39@rev-1 KICK-dKeptSession-4@rev-1 KICK-dKeptSession-40@rev-1 KICK-dKeptSession-41@rev-1
KICK-dKeptSession-42@rev-1 KICK-dKeptSession-43@rev-1 KICK-dKeptSession-44@rev-1 KICK-dKeptSession-45@rev-1 KICK-dKeptSession-46@rev-1 KICK-dKeptSession-47@rev-1 KICK-dKeptSession-48@rev-1 KICK-dKeptSession-49@rev-1 KICK-dKeptSession-5@rev-1 KICK-dKeptSession-50@rev-1 KICK-dKeptSession-52@rev-1
KICK-dKeptSession-53@rev-1 KICK-dKeptSession-54@rev-1 KICK-dKeptSession-55@rev-1 KICK-dKeptSession-56@rev-1 KICK-dKeptSession-57@rev-1 KICK-dKeptSession-58@rev-1 KICK-dKeptSession-59@rev-1 KICK-dKeptSession-60@rev-1 KICK-dKeptSession-61@rev-1 KICK-dKeptSession-62@rev-1 KICK-dKeptSession-63@rev-1
KICK-dKeptSession-64@rev-1 KICK-dKeptSession-7@rev-1 KICK-dKeptSession-8@rev-1 KICK-dKeptSession-9@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dKeptSession's 28 clause(s) and 16 owned node(s), over 64 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 28
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-26-spec-KICK-dKeptSession-30.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-31.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-32.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-KICK-dKeptSession-33.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-34.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-35.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-36.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-KICK-dKeptSession-37.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-38.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-39.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-40.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-KICK-dKeptSession-41.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-43.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-44.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-KICK-dKeptSession-45.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-47.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-48.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-KICK-dKeptSession-49.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-51.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-52.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-KICK-dKeptSession-53.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-55.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-56.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-KICK-dKeptSession-57.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-58.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-59.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-60.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-KICK-dKeptSession-61.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-62.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-63.md` (PLAY-dClosedLoop-2), `spec/2026-10-26-spec-KICK-dKeptSession-64.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-26-spec-KICK-dKeptSession-65.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0141, cl-dClosedLoop-0142, cl-dClosedLoop-0144, cl-dClosedLoop-0153, cl-dClosedLoop-0157, cl-dClosedLoop-0158, cl-dClosedLoop-0160, cl-dClosedLoop-0161, cl-dClosedLoop-0163, cl-dClosedLoop-0165
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `KICK-dKeptSession-1` | no |
| 2 | `KICK-dKeptSession-19`, `KICK-dKeptSession-33` | yes |
| 3 | `KICK-dKeptSession-2` | no |
| 4 | `KICK-dKeptSession-3`, `KICK-dKeptSession-34`, `KICK-dKeptSession-40` | yes |
| 5 | `KICK-dKeptSession-4`, `KICK-dKeptSession-49`, `KICK-dKeptSession-50`, `KICK-dKeptSession-54` | yes |
| 6 | `KICK-dKeptSession-20`, `KICK-dKeptSession-32`, `KICK-dKeptSession-58`, `KICK-dKeptSession-59`, `KICK-dKeptSession-60` | yes |
| 7 | `KICK-dKeptSession-16` | no |
| 8 | `KICK-dKeptSession-12` | no |
| 9 | `KICK-dKeptSession-13`, `KICK-dKeptSession-37`, `KICK-dKeptSession-38` | yes |
| 10 | `KICK-dKeptSession-26` | no |
| 11 | `KICK-dKeptSession-15` | no |
| 12 | `KICK-dKeptSession-14` | no |
| 13 | `KICK-dKeptSession-30`, `KICK-dKeptSession-9` | yes |
| 14 | `KICK-dKeptSession-28`, `KICK-dKeptSession-45`, `KICK-dKeptSession-46`, `KICK-dKeptSession-47`, `KICK-dKeptSession-48` | yes |
| 15 | `KICK-dKeptSession-22` | no |
| 16 | `KICK-dKeptSession-31`, `KICK-dKeptSession-5` | yes |
| 17 | `KICK-dKeptSession-23`, `KICK-dKeptSession-36`, `KICK-dKeptSession-39`, `KICK-dKeptSession-51` | yes |
| 18 | `KICK-dKeptSession-27` | no |
| 19 | `KICK-dKeptSession-24` | no |
| 20 | `KICK-dKeptSession-10` | no |
| 21 | `KICK-dKeptSession-25` | no |
| 22 | `KICK-dKeptSession-21` | no |
| 23 | `KICK-dKeptSession-6` | no |
| 24 | `KICK-dKeptSession-7` | no |
| 25 | `KICK-dKeptSession-35`, `KICK-dKeptSession-42`, `KICK-dKeptSession-8` | yes |
| 26 | `KICK-dKeptSession-11`, `KICK-dKeptSession-43`, `KICK-dKeptSession-52`, `KICK-dKeptSession-53`, `KICK-dKeptSession-55` | yes |
| 27 | `KICK-dKeptSession-17`, `KICK-dKeptSession-61` | yes |
| 28 | `KICK-dKeptSession-18` | no |
| 29 | `KICK-dKeptSession-41` | no |
| 30 | `KICK-dKeptSession-44` | no |
| 31 | `KICK-dKeptSession-56` | no |
| 32 | `KICK-dKeptSession-57` | no |
| 33 | `KICK-dKeptSession-62` | no |
| 34 | `KICK-dKeptSession-63` | no |
| 35 | `KICK-dKeptSession-64` | no |
| 36 | `KICK-dKeptSession-65` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md), [dPlacedRequest](../dPlacedRequest/README.md)
- **Child builds:** [dIndexedDesign](../dIndexedDesign/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md)
<!-- /gen:build-edges -->
