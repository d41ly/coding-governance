---
slug: aWeldedTribunal
node: a
opened: 2026-09-04
streams: tooling
roster: TOOL
ids: TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8
authorized-by: prompt
---

# aWeldedTribunal — work the eleven backlog rows the owner named, and say which were already fixed

## The problem this build exists to solve

The owner named eleven OPEN `TOOL` rows. Four describe a defect the tree no longer has, so they are
closed on cited evidence rather than rebuilt; `TOOL-aWeldedTribunal-8` §4 tabulates the file and line
that closed each. The other seven are live and were re-measured against source before speccing.

Three are holes in the fan-out cap hook, which is this repo's only mechanical control against an
agent burst. The rest are a review harness that computes its own liveness counters and reports none
of them, a conf parser divergence that removes coverage instead of failing closed, a deploy verb
blind to a file gov started shipping, and a push boundary gated by another checkout's hook.

## Expected improvements

- The cap hook stops admitting four shapes, every one measured at exit 0 before this build.
- A degraded Tier-2 review can no longer write a confident record.
- One `.memory-tree.conf` parser, agreeing with the bash half that sources the same file.
- `govkit update` reports a source the adopter does not hold.
- The wiring check names the hooks that will actually run.
- Four rows stop being open.

## Detriments if this is not built

- Three of five hook rules stay bypassable by ordinary JavaScript.
- The next review whose lenses half die writes a record that cannot say so.
- The conf divergence fails OPEN on a gate, for every adopter.
- The four stale rows keep being re-triaged, which is what this build's first hour went on.

## Build-level rules

- **Classification (M2):** eight units, all MISSING at the start, so every spec is authored this run.
  `TOOL-aWeldedTribunal-7` was additionally FORKED; its fork is resolved in its own §8 before code.
- **Four rows close on EVIDENCE, not a rebuild.** `TOOL-aWeldedTribunal-8` §4 carries the table.
- **Unit 2 is sequenced AFTER unit 1 by measurement**, not preference: its defect is only reachable
  through unit 1's, so an arm written against the old tree would go green for the wrong reason. The
  four-spelling probe is in that unit's §4.
- **Three units write `tools/hooks/agent-cap.js`**, so M6 clause 1 makes 1, 2 and 3 a chain. Unit 8
  writes `memory/backlog/TOOL.md`, a shared mutable record, so M6 clause 3 puts it alone and last.
- **PARALLEL DISPATCH IS DECLARED AND NOT TAKEN — a stated deviation from M6.** Units 4 to 7 have
  proven-disjoint write sets, and this run is a single agent with no sanctioned build-pass fan-out
  primitive. The write sets are recorded through `--dispatch` anyway, so the disjointness claim is on
  disk and falsifiable; the cost is wall clock only.

## Parked decisions

None. Both spec-audit rounds came back BLOCKED and every finding was DISPOSED rather than parked.

Round 2 exited **NON-CONVERGENT** — 17 defects against round 1's 16 — so the loop stopped and the
recorded disposition is `fold`. Unit 4's scanner was DROPPED against the owner ruling at
`memory/DECISIONS.md:116`; unit 7's fork resolution STANDS with its scoping corrected. Both review
records are under `reviews/`, and each unit's §9 names the findings it folded.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aWeldedTribunal-1` | 2 | the loop walk recognises `for await` and `do`-blocks |
| 2 | `TOOL-aWeldedTribunal-2` | 2 | an identifier blessed from an empty literal is re-examined when grown |
| 3 | `TOOL-aWeldedTribunal-3` | 2 | rule 3's blanked view reports an unterminated scan and falls back |
| 4 | `TOOL-aWeldedTribunal-4` | 2 | the tier-2 synthesis prompt carries its run-integrity counters |
| 5 | `TOOL-aWeldedTribunal-5` | 2 | five memory-tree readers route through one conf parser |
| 6 | `TOOL-aWeldedTribunal-6` | 2 | `govkit update` reports a descriptor source with no receipt row |
| 7 | `TOOL-aWeldedTribunal-7` | 2 | the wiring check grades the resolved pre-push against the tracked blob |
| 8 | `TOOL-aWeldedTribunal-8` | 1 | four rows close on cited evidence rather than on a rebuild |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 8 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aWeldedTribunal-1 — one loop-header predicate, and it recognises `for await` and `do`-blocks](spec/2026-09-04-spec-TOOL-aWeldedTribunal-1.md) | 1 | 2 | CLOSED | rev-3 | 2026-09-04 |
| [TOOL-aWeldedTribunal-2 — a bounded array loses its bound when a later statement grows it](spec/2026-09-04-spec-TOOL-aWeldedTribunal-2.md) | 2 | 2 | CLOSED | rev-3 | 2026-09-04 |
| [TOOL-aWeldedTribunal-3 — the blanked view reports an unterminated scan, and its readers fall back](spec/2026-09-04-spec-TOOL-aWeldedTribunal-3.md) | 3 | 2 | CLOSED | rev-5 | 2026-09-04 |
| [TOOL-aWeldedTribunal-4 — the tier-2 synthesis prompt carries the liveness counters the run computed](spec/2026-09-04-spec-TOOL-aWeldedTribunal-4.md) | 4 | 2 | CLOSED | rev-3 | 2026-09-04 |
| [TOOL-aWeldedTribunal-5 — one `.memory-tree.conf` parser, read by every python reader](spec/2026-09-04-spec-TOOL-aWeldedTribunal-5.md) | 5 | 2 | CLOSED | rev-3 | 2026-09-04 |
| [TOOL-aWeldedTribunal-6 — `govkit update` reports a source gov started shipping instead of missing it](spec/2026-09-04-spec-TOOL-aWeldedTribunal-6.md) | 6 | 2 | CLOSED | rev-4 | 2026-09-04 |
| [TOOL-aWeldedTribunal-7 — the wiring check names the hooks that will actually run](spec/2026-09-04-spec-TOOL-aWeldedTribunal-7.md) | 7 | 2 | CLOSED | rev-3 | 2026-09-04 |
| [TOOL-aWeldedTribunal-8 — close the four rows whose defect the tree no longer has](spec/2026-09-04-spec-TOOL-aWeldedTribunal-8.md) | 8 | 1 | CLOSED | rev-2 | 2026-09-04 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aWeldedTribunal-1` | no |
| 2 | `TOOL-aWeldedTribunal-2` | no |
| 3 | `TOOL-aWeldedTribunal-3` | no |
| 4 | `TOOL-aWeldedTribunal-4` | no |
| 5 | `TOOL-aWeldedTribunal-5` | no |
| 6 | `TOOL-aWeldedTribunal-6` | no |
| 7 | `TOOL-aWeldedTribunal-7` | no |
| 8 | `TOOL-aWeldedTribunal-8` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
