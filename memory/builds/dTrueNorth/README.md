---
slug: dTrueNorth
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7
status: OPEN
spec-audit: 2026-10-21
parents: dClosedLoop
may: PLAY-dClosedLoop-3 PLAY-dClosedLoop-2
---

# dTrueNorth — the Fidelity build of the dClosedLoop chain

## The problem this build exists to solve

dTrueNorth owns 3 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-design-13,
gap-build-07, gap-mem-47. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 6 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per clause.
- Each unit built and landed, so the 3 owned gaps above close.
- Its extra unit built: the carry-forward condition for every unit a spec run adds, once, and the starting-roster
  reading it rests on, which every later chain spec run closes with.

## Detriments if this is not built

- Its 3 owned gaps stay open.
- Its 1 child build waits on it: dGroundRules.

## Build-level rules

- Phase: one whole run specs, audits, builds and lands every unit, the extra unit last, and closes without
  carry-forward.
- Read in the packet's order, `packet.py --check dTrueNorth` green before the first pass; a moved instrument blob is a
  stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dTrueNorth`, a record per member "recorded by nobody", the same with `--write` (commit it as
  `…-departures-build.md`) and `--check`, then `--authorization` and `--close`; again after a re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-11.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dTrueNorth-1` | `cl-dClosedLoop-0001@83b6b117` | the clause ids: each clause of the design read with its minted `cl-` id and the hash of its text as the design's `[clause-ids]` section defines it |
| 2 | `TOOL-dTrueNorth-2` | `cl-dClosedLoop-0002@6acd9ea9` | the carries join |
| 3 | `TOOL-dTrueNorth-3` | `cl-dClosedLoop-0003@d2811290` | the coverage report rendered into each chain build's README beside its unit ids: the clauses carried whole and split |
| 4 | `TOOL-dTrueNorth-4` | `cl-dClosedLoop-0004@c374ccd0` | the deviation record |
| 5 | `TOOL-dTrueNorth-5` | `cl-dClosedLoop-0005@5417efbc` | every audit of a spec record pinning the revision it read as `@rev-N` on its Serves line |
| 6 | `TOOL-dTrueNorth-6` | `cl-dClosedLoop-0006@06ceb3cc` | the as-built view: the design at its baseline commit with each deviation's amends or supersedes row applied |
| 7 | `TOOL-dTrueNorth-7` | **Derived:** PLAY-dClosedLoop-2 | the carry-forward condition for every unit a spec run adds, once, and the starting-roster reading it rests on |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dTrueNorth-1 TOOL-dTrueNorth-2 TOOL-dTrueNorth-3 TOOL-dTrueNorth-4 TOOL-dTrueNorth-5 TOOL-dTrueNorth-6 TOOL-dTrueNorth-7

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

- **Parent builds:** [dClosedLoop](../dClosedLoop/README.md)
- **Child builds:** [dGroundRules](../dGroundRules/README.md)
<!-- /gen:build-edges -->
