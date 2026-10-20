---
slug: dOrderedCharter
node: d
opened: 2026-10-21
streams: playbook
roster: PLAY
ids: PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-38
status: OPEN
spec-audit: 2026-10-21
parents: dSafePassage
may: PLAY-dClosedLoop-3
---

# dOrderedCharter — the Foundation build of the dClosedLoop chain

## The problem this build exists to solve

dOrderedCharter owns 31 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-found-01,
gap-found-02, gap-found-03, gap-found-04, gap-found-05, gap-found-07, gap-found-08, gap-flow-02, gap-orient-13,
gap-found-09, gap-found-10, gap-found-11, gap-found-14, gap-found-15, gap-found-17, gap-found-18, gap-found-19,
gap-found-20, gap-found-21, gap-found-22, gap-found-23, gap-found-24, gap-found-25, gap-found-26, gap-mem-35,
gap-tool-19, gap-found-29, gap-found-30, gap-found-31, gap-found-33, gap-found-34. Closing every one is this build's
goal bound.

## Expected improvements

- Each of the 37 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 31 owned gaps above close.

## Detriments if this is not built

- Its 31 owned gaps stay open.
- Its 1 child build waits on it: dDeclaredLoop.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dOrderedCharter` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dOrderedCharter`, a record per member "recorded by nobody", the same with `--write` (commit
  it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-12.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `PLAY-dOrderedCharter-1` | `cl-dClosedLoop-0031@419dfa75` | the practice catalogue and `charter.practices` |
| 2 | `PLAY-dOrderedCharter-2` | `cl-dClosedLoop-0032@e38b0cb6` | the charter re-founded in its level-0 envelope (front door |
| 3 | `PLAY-dOrderedCharter-3` | `cl-dClosedLoop-0033@756303be` | envelopes rendered for every registered document and the gate over them |
| 4 | `PLAY-dOrderedCharter-4` | `cl-dClosedLoop-0034@06f1afc5` | the instruction map re-injected on compact and resume |
| 5 | `PLAY-dOrderedCharter-5` | `cl-dClosedLoop-0035@0d7d32c8` | ranked envelopes in every subagent handoff |
| 6 | `PLAY-dOrderedCharter-6` | `cl-dClosedLoop-0036@3667f2f3` | the drive section composed from a drive table in each adopted kit's descriptor |
| 7 | `PLAY-dOrderedCharter-7` | `cl-dClosedLoop-0037@0b2c8bff` | the core: the principle registry |
| 8 | `PLAY-dOrderedCharter-8` | `cl-dClosedLoop-0038@1bd5b757` | the build's card delivered at level 1 through an ignored per-worktree card file the charter's entry file imports |
| 9 | `PLAY-dOrderedCharter-9` | `cl-dClosedLoop-0039@ee1a0e99` | the instruction-unit registry (per unit: tag |
| 10 | `PLAY-dOrderedCharter-10` | `cl-dClosedLoop-0040@25b6d46b` | the namespaced tag system (reader |
| 11 | `PLAY-dOrderedCharter-11` | `cl-dClosedLoop-0041@29cae3c8` | load sets derived per reader and item |
| 12 | `PLAY-dOrderedCharter-12` | `cl-dClosedLoop-0042@9958d12b` | the statement grammar and its check |
| 13 | `PLAY-dOrderedCharter-13` | `cl-dClosedLoop-0043@536226d0` | the ladder renumbered |
| 14 | `PLAY-dOrderedCharter-14` | `cl-dClosedLoop-0044@0104c89b` | memory instructing nothing |
| 15 | `PLAY-dOrderedCharter-15` | `cl-dClosedLoop-0045@f345dc78` | the instruction manifest and its guarded write command (`instructions.edit` |
| 16 | `PLAY-dOrderedCharter-16` | `cl-dClosedLoop-0046@bd068162` | the layer register |
| 17 | `PLAY-dOrderedCharter-17` | `cl-dClosedLoop-0047@9b2f4330` | the edges that check finds today each made a declared optional slot with a named fallback |
| 18 | `PLAY-dOrderedCharter-18` | `cl-dClosedLoop-0048@aab14736` | the moved grammar's by-path consumers re-pointed in the move's own unit |
| 19 | `PLAY-dOrderedCharter-19` | `cl-dClosedLoop-0049@a87d159d` | the tag grammar |
| 20 | `PLAY-dOrderedCharter-20` | `cl-dClosedLoop-0050@13d9192b` | the instruction unit's schema and grammar |
| 21 | `PLAY-dOrderedCharter-21` | `cl-dClosedLoop-0051@44bf9720` | each practice's reach per step rendered as step-scoped units handed in work orders |
| 22 | `PLAY-dOrderedCharter-22` | `cl-dClosedLoop-0052@e3506c61` | the namespace row's `purpose-source` and `owner` fields and the chain registry's purpose field |
| 23 | `PLAY-dOrderedCharter-23` | `cl-dClosedLoop-0053@8f756a97` | a build run unattended by default from its request |
| 24 | `PLAY-dOrderedCharter-24` | `cl-dClosedLoop-0054@1e793db7` | the edge-type registry and the `edge` grammar: one closed set of typed edges |
| 25 | `PLAY-dOrderedCharter-25` | `cl-dClosedLoop-0055@dc43d502` | `gov tag bundle` |
| 26 | `PLAY-dOrderedCharter-26` | `cl-dClosedLoop-0056@a91f3d50` | file:line citations joined to the positional population `tags.positional` holds |
| 27 | `PLAY-dOrderedCharter-27` | `cl-dClosedLoop-0057@ec297ae3` | each role's load set budgeting the `code` slot (night pass |
| 28 | `PLAY-dOrderedCharter-28` | `cl-dClosedLoop-0058@bc160feb` | the shared edge grammar at every site the memory plan names |
| 29 | `PLAY-dOrderedCharter-29` | `cl-dClosedLoop-0059@0e668fff` | the one writing practice's checks over records as well as units: address |
| 30 | `PLAY-dOrderedCharter-30` | `cl-dClosedLoop-0060@83e8c234` | the portable practice: a role per language |
| 31 | `PLAY-dOrderedCharter-31` | `cl-dClosedLoop-0061@bf1a53b5` | its own upgrade steps: agent-instructions' wiring moved to the one renderer |
| 32 | `PLAY-dOrderedCharter-32` | `cl-dClosedLoop-0062@fe903e93` | the repository's instruction overlay: `.governance/instructions.toml` |
| 33 | `PLAY-dOrderedCharter-33` | `cl-dClosedLoop-0063@a1361320` | pins and drift: each gov change record marked `editorial` or `semantic` |
| 34 | `PLAY-dOrderedCharter-34` | `cl-dClosedLoop-0064@8b8552ab` | composition and its report: the project block from the repository's level-0 units and its level-3 to level-5 units in a marked part of their documents |
| 35 | `PLAY-dOrderedCharter-35` | `cl-dClosedLoop-0065@35e9932a` | the overlay's row mechanism for every kind a later build registers: `owned` admitting the `adopter` segment in a registered namespace (the owner's tag-grammar answer) |
| 36 | `PLAY-dOrderedCharter-36` | `cl-dClosedLoop-0066@dcfb4bb2` | the row checks over every registered kind |
| 37 | `PLAY-dOrderedCharter-37` | `cl-dClosedLoop-0067@90e357b7` | the help pages: reference pages rendered by the one renderer from each registry's rows |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams playbook
ids PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12
ids PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24
ids PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36
ids PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-38

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dSafePassage](../dSafePassage/README.md)
- **Child builds:** [dDeclaredLoop](../dDeclaredLoop/README.md)
<!-- /gen:build-edges -->
