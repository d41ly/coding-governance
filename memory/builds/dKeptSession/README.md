---
slug: dKeptSession
node: d
opened: 2026-10-21
streams: kickoff
roster: KICK
ids: KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-29
status: OPEN
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
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams kickoff
ids KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14
ids KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28
ids KICK-dKeptSession-29

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 9 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dKeptSession's 28 clause(s) and 16 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 28 (cl-dClosedLoop-0139, cl-dClosedLoop-0140, cl-dClosedLoop-0141, cl-dClosedLoop-0142, cl-dClosedLoop-0143, cl-dClosedLoop-0144, cl-dClosedLoop-0145, cl-dClosedLoop-0146, cl-dClosedLoop-0147, cl-dClosedLoop-0148, cl-dClosedLoop-0149, cl-dClosedLoop-0150, cl-dClosedLoop-0151,
  cl-dClosedLoop-0152, cl-dClosedLoop-0153, cl-dClosedLoop-0154, cl-dClosedLoop-0155, cl-dClosedLoop-0156, cl-dClosedLoop-0157, cl-dClosedLoop-0158, cl-dClosedLoop-0159, cl-dClosedLoop-0160, cl-dClosedLoop-0161, cl-dClosedLoop-0162, cl-dClosedLoop-0504, cl-dClosedLoop-0163, cl-dClosedLoop-0164,
  cl-dClosedLoop-0165)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.mailbox.answer, policy-key.actions.free, policy-key.attendance, policy-key.card.pointers, policy-key.context.on-full, policy-key.context.threshold, policy-key.deps.coordination, policy-key.deps.early-build, policy-key.deps.messaging,
  policy-key.mailbox.fetch-seconds, policy-key.mailbox.notice, policy-key.mailbox.reads, policy-key.notify.owner, policy-key.orient.budget, policy-key.preset, record-kind.mailbox-message
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0141, cl-dClosedLoop-0142, cl-dClosedLoop-0144, cl-dClosedLoop-0153, cl-dClosedLoop-0157, cl-dClosedLoop-0158, cl-dClosedLoop-0160, cl-dClosedLoop-0161, cl-dClosedLoop-0163, cl-dClosedLoop-0165
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md), [dPlacedRequest](../dPlacedRequest/README.md)
- **Child builds:** [dIndexedDesign](../dIndexedDesign/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md)
<!-- /gen:build-edges -->
