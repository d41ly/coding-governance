---
slug: dOrderedCharter
node: d
opened: 2026-10-21
streams: playbook
roster: PLAY
ids: PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-38 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-56 PLAY-dOrderedCharter-57 PLAY-dOrderedCharter-58 PLAY-dOrderedCharter-59 TOOL-dOrderedCharter-7
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
**Build status:** DEFERRED · 54 unit(s) · node d · opened 2026-10-21 · streams playbook
ids PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12
ids PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24
ids PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36
ids PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-38 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48
ids PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-56 PLAY-dOrderedCharter-57 PLAY-dOrderedCharter-58 PLAY-dOrderedCharter-59 TOOL-dOrderedCharter-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [PLAY-dOrderedCharter-18 — the moved grammar: every name the core imports from the recall kit moved into memory-tree, and every by-path reader re-pointed in the same unit](spec/2026-10-23-spec-PLAY-dOrderedCharter-18.md) | 1 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-16 — the layer register, the layer contract and the check that the core never depends on an expansion or an optional component](spec/2026-10-23-spec-PLAY-dOrderedCharter-16.md) | 2 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-17 — every edge the layer check finds today made a declared optional slot with a named fallback, or moved into the core](spec/2026-10-23-spec-PLAY-dOrderedCharter-17.md) | 3 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [PLAY-dOrderedCharter-19 — the tag grammar, its namespace registry, the derived SQLite tag index and its one resolver, and the join factory moved to the core](spec/2026-10-23-spec-PLAY-dOrderedCharter-19.md) | 4 | 2 | DEFERRED | rev-5 | 2026-10-25 |
| [PLAY-dOrderedCharter-10 — the namespaced tag system: this build's eight namespaces registered, joined both ways, shape-checked in the core, and their words handed to the lexicon](spec/2026-10-23-spec-PLAY-dOrderedCharter-10.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-44 — the tag index keys freshness on each extractor as well as each blob, so a newly registered extractor reads old blobs](spec/2026-10-24-spec-PLAY-dOrderedCharter-44.md) | 5 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-22 — the namespace row's purpose-source and owner fields, and the chain registry's purpose field](spec/2026-10-23-spec-PLAY-dOrderedCharter-22.md) | 6 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-51 — the shared tag index keeps each extractor version's rows apart, and each worktree reads only its own](spec/2026-10-24-spec-PLAY-dOrderedCharter-51.md) | 6 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [PLAY-dOrderedCharter-24 — the edge-type registry and the edge grammar: one closed set of typed edges, inverses derived, selectors open](spec/2026-10-23-spec-PLAY-dOrderedCharter-24.md) | 7 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-28 — the shared edge grammar at every site the memory plan names: twelve new types, native-id classes and the two pinned forms](spec/2026-10-23-spec-PLAY-dOrderedCharter-28.md) | 8 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-26 — file:line citations held in the positional population, new text citing a symbol or a pinned line](spec/2026-10-23-spec-PLAY-dOrderedCharter-26.md) | 9 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [PLAY-dOrderedCharter-25 — gov tag bundle, a tag's members, regions and instructions in one call, and the two edge checks](spec/2026-10-23-spec-PLAY-dOrderedCharter-25.md) | 10 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [PLAY-dOrderedCharter-47 — a record written on a branch that never held the positional check is graded print-only, by its adding commit's ancestry](spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-48 — the sources that tell a writer to cite path and line are a query over the directive sources, every hit re-pointed or kept by name](spec/2026-10-24-spec-PLAY-dOrderedCharter-48.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-50 — the rows a new leg, key or retirement owes are written by the pass that creates them, through one owed-rows probe](spec/2026-10-24-spec-PLAY-dOrderedCharter-50.md) | 10 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-53 — a file:line citation is grandfathered by the commit that wrote its line, never by the age of its file](spec/2026-10-24-spec-PLAY-dOrderedCharter-53.md) | 11 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [PLAY-dOrderedCharter-7 — the core: principle registry, meta-check, kinds register, exception register and the core policies](spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md) | 11 | 2 | DEFERRED | rev-5 | 2026-10-25 |
| [PLAY-dOrderedCharter-13 — the ladder renumbered: levels 0 to 7, the charter at level 0, the platform above it](spec/2026-10-23-spec-PLAY-dOrderedCharter-13.md) | 12 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-42 — the bindings reader admits every kind the record factory mints, joined to its file name both ways](spec/2026-10-24-spec-PLAY-dOrderedCharter-42.md) | 12 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-12 — the statement grammar, its check, and render provenance in a sidecar lock](spec/2026-10-23-spec-PLAY-dOrderedCharter-12.md) | 13 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-9 — the instruction-unit registry: one row per unit in each kit's manifest, its one reader, and documents rendered from units](spec/2026-10-23-spec-PLAY-dOrderedCharter-9.md) | 14 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [PLAY-dOrderedCharter-20 — the unit schema, the one renderer of record and its templates, the render gate with its legacy list, and one fact in one unit](spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md) | 15 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [PLAY-dOrderedCharter-15 — the instruction manifest and its guarded write command, each change recorded, and the pack catalogue](spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md) | 16 | 2 | DEFERRED | rev-5 | 2026-10-25 |
| [PLAY-dOrderedCharter-1 — the practice catalogue and `charter.practices`](spec/2026-10-23-spec-PLAY-dOrderedCharter-1.md) | 17 | 2 | DEFERRED | rev-5 | 2026-10-25 |
| [PLAY-dOrderedCharter-45 — the merge driver's TOML-table class states its whole conflict envelope and proves its output parses](spec/2026-10-24-spec-PLAY-dOrderedCharter-45.md) | 17 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-3 — envelopes rendered for every registered document, and the gate over them](spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md) | 18 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [PLAY-dOrderedCharter-41 — the `cross-os` block stays live, so every v4 template renders after the practice catalogue lands](spec/2026-10-24-spec-PLAY-dOrderedCharter-41.md) | 18 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-52 — the TOML-table merge envelope is total: every base, ours and theirs state has a row, and an unlisted one is a conflict](spec/2026-10-24-spec-PLAY-dOrderedCharter-52.md) | 18 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [PLAY-dOrderedCharter-6 — the drive section composed from each adopted kit's drive table, and the charter held inside 32 KiB](spec/2026-10-23-spec-PLAY-dOrderedCharter-6.md) | 19 | 2 | DEFERRED | rev-5 | 2026-10-25 |
| [PLAY-dOrderedCharter-2 — the charter re-founded in its level-0 envelope, with the override rule and its record](spec/2026-10-23-spec-PLAY-dOrderedCharter-2.md) | 20 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [PLAY-dOrderedCharter-11 — load sets derived per reader and item, budgeted, and refused when a required unit is missing](spec/2026-10-23-spec-PLAY-dOrderedCharter-11.md) | 21 | 2 | DEFERRED | rev-4 | 2026-10-25 |
| [PLAY-dOrderedCharter-27 — each role's load set budgeting the `code` slot](spec/2026-10-23-spec-PLAY-dOrderedCharter-27.md) | 22 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-21 — each practice's reach per step rendered as step-scoped units handed in work orders](spec/2026-10-23-spec-PLAY-dOrderedCharter-21.md) | 23 | 2 | DEFERRED | rev-1 | 2026-10-23 |
| [PLAY-dOrderedCharter-5 — ranked envelopes in every subagent handoff, the charter carried once](spec/2026-10-23-spec-PLAY-dOrderedCharter-5.md) | 24 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-4 — the instruction map re-injected on compact and resume through the existing replay fragment](spec/2026-10-23-spec-PLAY-dOrderedCharter-4.md) | 25 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-8 — the build's card at level 1, through an ignored per-worktree card file the charter's entry file imports](spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md) | 26 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-14 — memory instructing nothing: the auto-memory index measured at session start, its directives detected, a standing directive promoted into a unit](spec/2026-10-23-spec-PLAY-dOrderedCharter-14.md) | 27 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-43 — the card import written and checked by the one renderer's entry-files scope, never by a second writer](spec/2026-10-24-spec-PLAY-dOrderedCharter-43.md) | 27 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-30 — the portable practice: a role per language, one rule set, each rule paired with its named leg, absorbing `[cross-os]` and `[bytes]`](spec/2026-10-23-spec-PLAY-dOrderedCharter-30.md) | 28 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [PLAY-dOrderedCharter-29 — the one writing practice's checks over records as well as units](spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md) | 29 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-23 — a build run unattended by default from its request, said in the drive section, and the `[land]` rule read through the request's mandate](spec/2026-10-23-spec-PLAY-dOrderedCharter-23.md) | 30 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-32 — the repository's instruction overlay: `.governance/instructions.toml`, its `repo.` units, pinned edges into gov's units, derived classes and the repository's own policy keys](spec/2026-10-23-spec-PLAY-dOrderedCharter-32.md) | 31 | 2 | DEFERRED | rev-4 | 2026-10-25 |
| [PLAY-dOrderedCharter-33 — pins and drift: each gov change record marked `editorial` or `semantic`, a stale pin acting as `instructions.stale` says, successors re-pointing or orphaning an edge](spec/2026-10-23-spec-PLAY-dOrderedCharter-33.md) | 32 | 2 | DEFERRED | rev-4 | 2026-10-25 |
| [PLAY-dOrderedCharter-46 — the overlay's landed revision defined, its unborn-HEAD outcome stated, and a write door rendering the rows it just wrote](spec/2026-10-24-spec-PLAY-dOrderedCharter-46.md) | 32 | 2 | DEFERRED | rev-4 | 2026-10-25 |
| [PLAY-dOrderedCharter-35 — the overlay's row mechanism for every registered kind: adopter-segment tags, field patches, whole-row replacements, exclusions, row pins and stale rows](spec/2026-10-23-spec-PLAY-dOrderedCharter-35.md) | 33 | 2 | DEFERRED | rev-5 | 2026-10-25 |
| [PLAY-dOrderedCharter-36 — the row checks over every registered kind: the fixed set, the exclusion refusals and the widening classifier](spec/2026-10-23-spec-PLAY-dOrderedCharter-36.md) | 34 | 2 | DEFERRED | rev-5 | 2026-10-25 |
| [PLAY-dOrderedCharter-34 — composition and its report: the project block and marked parts from the overlay, budgets and harness limits at render, one composition for every harness, the delta report, and the practice census](spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md) | 35 | 2 | DEFERRED | rev-5 | 2026-10-25 |
| [PLAY-dOrderedCharter-31 — this build's own upgrade steps: the agent-instructions wiring to the one renderer, adopter rules into the overlay, the seeded template's succession row, the census's change records and the `map_lib` deprecation](spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md) | 36 | 2 | DEFERRED | rev-5 | 2026-10-25 |
| [PLAY-dOrderedCharter-37 — the help pages: reference pages rendered from each registry's rows, concept, task and tutorial pages beside them, every shown command run, each page linked to its unit by tag](spec/2026-10-23-spec-PLAY-dOrderedCharter-37.md) | 37 | 2 | DEFERRED | rev-4 | 2026-10-24 |
| [PLAY-dOrderedCharter-39 — the card import survives the agent-instructions kit's retirement, with the wiring leg kept by name](spec/2026-10-24-spec-PLAY-dOrderedCharter-39.md) | 37 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-40 — gov's first instruction unit rows, one per reference page, and the pages' registry tags declared](spec/2026-10-24-spec-PLAY-dOrderedCharter-40.md) | 38 | 2 | DEFERRED | rev-2 | 2026-10-24 |
| [PLAY-dOrderedCharter-49 — the round-1 spec audit's 73 minors: criteria that can pass, rows a new leg owes, one reader per fact, and seams in build order](spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md) | 39 | 2 | DEFERRED | rev-3 | 2026-10-24 |
| [PLAY-dOrderedCharter-54 — the card file's owner is live only while its transcript moves, and a dead owner's card is taken over](spec/2026-10-24-spec-PLAY-dOrderedCharter-54.md) | 40 | 2 | DEFERRED | rev-1 | 2026-10-24 |
| [PLAY-dOrderedCharter-55 — the round-2 spec audit's 31 minors: criteria observed where they can pass, one reader per fact, and seams that hold in any order](spec/2026-10-24-spec-PLAY-dOrderedCharter-55.md) | 41 | 2 | DEFERRED | rev-2 | 2026-10-24 |
<!-- /gen:build-units -->

Records: 175 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55.

Ids whose spec moved past its audited revision: PLAY-dOrderedCharter-1@rev-1 PLAY-dOrderedCharter-10@rev-1 PLAY-dOrderedCharter-11@rev-1 PLAY-dOrderedCharter-12@rev-1 PLAY-dOrderedCharter-13@rev-1 PLAY-dOrderedCharter-14@rev-1 PLAY-dOrderedCharter-15@rev-1 PLAY-dOrderedCharter-16@rev-1
PLAY-dOrderedCharter-18@rev-1 PLAY-dOrderedCharter-19@rev-1 PLAY-dOrderedCharter-2@rev-1 PLAY-dOrderedCharter-20@rev-1 PLAY-dOrderedCharter-22@rev-1 PLAY-dOrderedCharter-23@rev-1 PLAY-dOrderedCharter-24@rev-1 PLAY-dOrderedCharter-25@rev-1 PLAY-dOrderedCharter-26@rev-1 PLAY-dOrderedCharter-27@rev-1
PLAY-dOrderedCharter-28@rev-1 PLAY-dOrderedCharter-29@rev-1 PLAY-dOrderedCharter-3@rev-1 PLAY-dOrderedCharter-30@rev-1 PLAY-dOrderedCharter-31@rev-1 PLAY-dOrderedCharter-32@rev-1 PLAY-dOrderedCharter-33@rev-1 PLAY-dOrderedCharter-34@rev-1 PLAY-dOrderedCharter-35@rev-1 PLAY-dOrderedCharter-36@rev-1
PLAY-dOrderedCharter-37@rev-1 PLAY-dOrderedCharter-4@rev-1 PLAY-dOrderedCharter-5@rev-1 PLAY-dOrderedCharter-6@rev-1 PLAY-dOrderedCharter-7@rev-1 PLAY-dOrderedCharter-8@rev-1 PLAY-dOrderedCharter-9@rev-1 PLAY-dOrderedCharter-39@rev-1 PLAY-dOrderedCharter-40@rev-1 PLAY-dOrderedCharter-41@rev-1
PLAY-dOrderedCharter-42@rev-1 PLAY-dOrderedCharter-43@rev-1 PLAY-dOrderedCharter-44@rev-1 PLAY-dOrderedCharter-45@rev-1 PLAY-dOrderedCharter-46@rev-1 PLAY-dOrderedCharter-47@rev-1 PLAY-dOrderedCharter-48@rev-1 PLAY-dOrderedCharter-49@rev-1.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dOrderedCharter's 37 clause(s) and 30 owned node(s), over 54 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 37
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: `spec/2026-10-24-spec-PLAY-dOrderedCharter-39.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-40.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-41.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-PLAY-dOrderedCharter-42.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-43.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-44.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-45.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-PLAY-dOrderedCharter-46.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-47.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-48.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-49.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-PLAY-dOrderedCharter-50.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-51.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-52.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-53.md` (PLAY-dClosedLoop-2),
  `spec/2026-10-24-spec-PLAY-dOrderedCharter-54.md` (PLAY-dClosedLoop-2), `spec/2026-10-24-spec-PLAY-dOrderedCharter-55.md` (PLAY-dClosedLoop-2)
- clauses the token arm cannot see: cl-dClosedLoop-0033, cl-dClosedLoop-0034, cl-dClosedLoop-0035, cl-dClosedLoop-0038, cl-dClosedLoop-0042, cl-dClosedLoop-0043, cl-dClosedLoop-0044, cl-dClosedLoop-0050, cl-dClosedLoop-0051, cl-dClosedLoop-0067
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `PLAY-dOrderedCharter-18` | no |
| 2 | `PLAY-dOrderedCharter-16` | no |
| 3 | `PLAY-dOrderedCharter-17` | no |
| 4 | `PLAY-dOrderedCharter-19` | no |
| 5 | `PLAY-dOrderedCharter-10`, `PLAY-dOrderedCharter-44` | no |
| 6 | `PLAY-dOrderedCharter-22`, `PLAY-dOrderedCharter-51` | no |
| 7 | `PLAY-dOrderedCharter-24` | no |
| 8 | `PLAY-dOrderedCharter-28` | no |
| 9 | `PLAY-dOrderedCharter-26` | no |
| 10 | `PLAY-dOrderedCharter-25`, `PLAY-dOrderedCharter-47`, `PLAY-dOrderedCharter-48`, `PLAY-dOrderedCharter-50` | no |
| 11 | `PLAY-dOrderedCharter-53`, `PLAY-dOrderedCharter-7` | yes |
| 12 | `PLAY-dOrderedCharter-13`, `PLAY-dOrderedCharter-42` | yes |
| 13 | `PLAY-dOrderedCharter-12` | no |
| 14 | `PLAY-dOrderedCharter-9` | no |
| 15 | `PLAY-dOrderedCharter-20` | no |
| 16 | `PLAY-dOrderedCharter-15` | no |
| 17 | `PLAY-dOrderedCharter-1`, `PLAY-dOrderedCharter-45` | yes |
| 18 | `PLAY-dOrderedCharter-3`, `PLAY-dOrderedCharter-41`, `PLAY-dOrderedCharter-52` | no |
| 19 | `PLAY-dOrderedCharter-6` | no |
| 20 | `PLAY-dOrderedCharter-2` | no |
| 21 | `PLAY-dOrderedCharter-11` | no |
| 22 | `PLAY-dOrderedCharter-27` | no |
| 23 | `PLAY-dOrderedCharter-21` | no |
| 24 | `PLAY-dOrderedCharter-5` | no |
| 25 | `PLAY-dOrderedCharter-4` | no |
| 26 | `PLAY-dOrderedCharter-8` | no |
| 27 | `PLAY-dOrderedCharter-14`, `PLAY-dOrderedCharter-43` | yes |
| 28 | `PLAY-dOrderedCharter-30` | no |
| 29 | `PLAY-dOrderedCharter-29` | no |
| 30 | `PLAY-dOrderedCharter-23` | no |
| 31 | `PLAY-dOrderedCharter-32` | no |
| 32 | `PLAY-dOrderedCharter-33`, `PLAY-dOrderedCharter-46` | no |
| 33 | `PLAY-dOrderedCharter-35` | no |
| 34 | `PLAY-dOrderedCharter-36` | no |
| 35 | `PLAY-dOrderedCharter-34` | no |
| 36 | `PLAY-dOrderedCharter-31` | no |
| 37 | `PLAY-dOrderedCharter-37`, `PLAY-dOrderedCharter-39` | yes |
| 38 | `PLAY-dOrderedCharter-40` | no |
| 39 | `PLAY-dOrderedCharter-49` | no |
| 40 | `PLAY-dOrderedCharter-54` | no |
| 41 | `PLAY-dOrderedCharter-55` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dSafePassage](../dSafePassage/README.md)
- **Child builds:** [dDeclaredLoop](../dDeclaredLoop/README.md)
<!-- /gen:build-edges -->
