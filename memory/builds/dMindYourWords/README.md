---
slug: dMindYourWords
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-18 TOOL-dMindYourWords-19 TOOL-dMindYourWords-20 TOOL-dMindYourWords-21
spec-audit: 2026-10-21
parents: dWellOiledMachine dWitnessedBar dLinkedLibrary dFurnishedOrders
may: PLAY-dClosedLoop-3
---

# dMindYourWords — the Lexicon build of the dClosedLoop chain

## The problem this build exists to solve

dMindYourWords owns 11 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-mem-10,
gap-lex-01, gap-lex-02, gap-lex-03, gap-lex-04, gap-lex-05, gap-lex-06, gap-lex-07, gap-lex-08, gap-lex-09,
gap-lex-10. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 17 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 11 owned gaps above close.

## Detriments if this is not built

- Its 11 owned gaps stay open.
- Its 1 child build waits on it: dConvergedCharter.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dMindYourWords` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dMindYourWords`, a record per member "recorded by nobody", the same with `--write` (commit
  it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
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
| 1 | `TOOL-dMindYourWords-1` | `cl-dClosedLoop-0262@8be7fb04` | the definition classes (conforming |
| 2 | `TOOL-dMindYourWords-2` | `cl-dClosedLoop-0263@bab0ffd1` | forced names recognised by what forces them (`lexicon.forced`): packs keyed by base member |
| 3 | `TOOL-dMindYourWords-3` | `cl-dClosedLoop-0264@a1b36116` | gov's own contract-forced names declared in a table the instruction write path owns |
| 4 | `TOOL-dMindYourWords-4` | `cl-dClosedLoop-0265@a234cd84` | override markers verified against the packs |
| 5 | `TOOL-dMindYourWords-5` | `cl-dClosedLoop-0266@db50d898` | a reasoned site suppression as the owner's counted fallback |
| 6 | `TOOL-dMindYourWords-6` | `cl-dClosedLoop-0267@06ce7948` | `--suggest` made forced-aware |
| 7 | `TOOL-dMindYourWords-7` | `cl-dClosedLoop-0268@2d14651f` | the packs |
| 8 | `TOOL-dMindYourWords-8` | `cl-dClosedLoop-0269@f2bbdcc2` | packs detected from the import census and manifests and declared by the owner |
| 9 | `TOOL-dMindYourWords-9` | `cl-dClosedLoop-0270@01096b8c` | enforcement: the work order's vocabulary slice and forced-aware answers |
| 10 | `TOOL-dMindYourWords-10` | `cl-dClosedLoop-0271@09fb0fff` | drift beyond verbs (`lexicon.drift`): one verb per declared family per object |
| 11 | `TOOL-dMindYourWords-11` | `cl-dClosedLoop-0272@aac8dd76` | the vocabulary changed only through the instruction write path |
| 12 | `TOOL-dMindYourWords-12` | `cl-dClosedLoop-0273@e1bd67f4` | one extraction primitive in `tools/lib` |
| 13 | `TOOL-dMindYourWords-13` | `cl-dClosedLoop-0274@5185348f` | the tag-name vocabulary check |
| 14 | `TOOL-dMindYourWords-14` | `cl-dClosedLoop-0275@f7d892e0` | the kit's defects fixed: repeated block headers refused |
| 15 | `TOOL-dMindYourWords-15` | `cl-dClosedLoop-0276@c565a516` | records kept out by the path selector |
| 16 | `TOOL-dMindYourWords-16` | `cl-dClosedLoop-0277@11ec04ed` | the two lexicon drift signals as the lexicon's own leg pack |
| 17 | `TOOL-dMindYourWords-17` | `cl-dClosedLoop-0278@3bd5d4af` | the overloaded terms settled: attended as a session kind and as a mode |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 17 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13
ids TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-18 TOOL-dMindYourWords-19 TOOL-dMindYourWords-20 TOOL-dMindYourWords-21

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dMindYourWords-1 — the definition classes and one shrink-only debt pin held by name](spec/2026-10-29-spec-TOOL-dMindYourWords-1.md) | 1 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-14 — the lexicon kit's own defects: repeated headers, non-names, dead modes, one pin story](spec/2026-10-29-spec-TOOL-dMindYourWords-14.md) | 2 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-15 — build records kept out of the graded population by a path selector](spec/2026-10-29-spec-TOOL-dMindYourWords-15.md) | 3 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-12 — the definition context the lexicon reads through the `tools/lib` extraction primitive](spec/2026-10-29-spec-TOOL-dMindYourWords-12.md) | 4 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-11 — the vocabulary changed only with the write path's record, which takes over from `ratified`](spec/2026-10-29-spec-TOOL-dMindYourWords-11.md) | 5 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-5 — a reasoned site suppression, recorded and counted, as the owner's fallback](spec/2026-10-29-spec-TOOL-dMindYourWords-5.md) | 6 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-7 — the packs: their file, their loader and the four generators](spec/2026-10-29-spec-TOOL-dMindYourWords-7.md) | 7 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-2 — forced names recognised by what forces them, under `lexicon.forced`](spec/2026-10-29-spec-TOOL-dMindYourWords-2.md) | 8 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-3 — gov's own contract-forced names in a table, with a stale arm](spec/2026-10-29-spec-TOOL-dMindYourWords-3.md) | 9 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-4 — override markers verified against the packs](spec/2026-10-29-spec-TOOL-dMindYourWords-4.md) | 10 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-6 — `--suggest` made forced-aware](spec/2026-10-29-spec-TOOL-dMindYourWords-6.md) | 11 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-8 — packs detected from the import census and manifests and declared by the owner](spec/2026-10-29-spec-TOOL-dMindYourWords-8.md) | 12 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-10 — drift beyond verbs: one verb per declared family per object, and a noun canon](spec/2026-10-29-spec-TOOL-dMindYourWords-10.md) | 13 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-9 — enforcement: the work order's vocabulary slice, staged names at commit, offenders by name at the bar](spec/2026-10-29-spec-TOOL-dMindYourWords-9.md) | 14 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-16 — the lexicon's drift signals as its own leg pack, out of drift-audit's engine](spec/2026-10-29-spec-TOOL-dMindYourWords-16.md) | 15 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-13 — the tag-name vocabulary check: a tag's verbs and nouns graded, its name answered by `--suggest`, and no namespace word in `.lexicon.conf`](spec/2026-10-29-spec-TOOL-dMindYourWords-13.md) | 16 | 2 | OPEN | rev-1 | 2026-10-29 |
| [TOOL-dMindYourWords-17 — the overloaded terms settled: attended, playbook and baseline each keep one sense, defined once and reworded where a carrier spends it on another](spec/2026-10-29-spec-TOOL-dMindYourWords-17.md) | 17 | 2 | OPEN | rev-1 | 2026-10-29 |
<!-- /gen:build-units -->

Records: 17 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dMindYourWords-1 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3
TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9.

Ids whose spec moved past its audited revision: none — 0 of 17 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dMindYourWords's 17 clause(s) and 6 owned node(s), over 17 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 17
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0264, cl-dClosedLoop-0265, cl-dClosedLoop-0266, cl-dClosedLoop-0275, cl-dClosedLoop-0277
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dMindYourWords-1` | no |
| 2 | `TOOL-dMindYourWords-14` | no |
| 3 | `TOOL-dMindYourWords-15` | no |
| 4 | `TOOL-dMindYourWords-12` | no |
| 5 | `TOOL-dMindYourWords-11` | no |
| 6 | `TOOL-dMindYourWords-5` | no |
| 7 | `TOOL-dMindYourWords-7` | no |
| 8 | `TOOL-dMindYourWords-2` | no |
| 9 | `TOOL-dMindYourWords-3` | no |
| 10 | `TOOL-dMindYourWords-4` | no |
| 11 | `TOOL-dMindYourWords-6` | no |
| 12 | `TOOL-dMindYourWords-8` | no |
| 13 | `TOOL-dMindYourWords-10` | no |
| 14 | `TOOL-dMindYourWords-9` | no |
| 15 | `TOOL-dMindYourWords-16` | no |
| 16 | `TOOL-dMindYourWords-13` | no |
| 17 | `TOOL-dMindYourWords-17` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dFurnishedOrders](../dFurnishedOrders/README.md), [dLinkedLibrary](../dLinkedLibrary/README.md), [dWellOiledMachine](../dWellOiledMachine/README.md), [dWitnessedBar](../dWitnessedBar/README.md)
- **Child builds:** [dConvergedCharter](../dConvergedCharter/README.md)
<!-- /gen:build-edges -->
