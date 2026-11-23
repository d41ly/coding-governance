---
slug: aHastenedSweep
node: a
opened: 2026-11-15
streams: tooling
roster: TOOL
ids: TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4 TOOL-aHastenedSweep-5 TOOL-aHastenedSweep-6 TOOL-aHastenedSweep-7
authorized-by: prompt
---

# aHastenedSweep — the memory-hygiene runner's per-item rescans removed, every verdict byte-identical

## The problem this build exists to solve

The `memory hygiene` leg is the bar's costliest leg on node a, and every `--only 12` or `--only 25` a
spec writer runs pays the same cost. An analysis on 2026-11-15 found most of it in rescans repeated
once per item where once in total would do: check 25's by-name pass copies every reader line per
unresolved token, `gotchas.py` recomputes basenames per anchor and path pair, and `corpus_ids.py`
rebuilds its roots per citation and re-enters the shell for a set its parent already holds. The
prompt and its brief are in `prompts/`.

## Expected improvements

- Check 25's by-name pass skips a line that cannot hold the token before copying it.
- Checks 13 to 19 compute each basename and root set once, and share one corpus walk.
- The shell hands `corpus_ids` the index set it already computed.

## Detriments if this is not built

- Every full bar and push keeps paying minutes of the hygiene leg for repeated work.
- Spec writers keep spending hours on `--only 12,25` reruns.

## Build-level rules

- **Classification (M2)**: four units, MISSING at open, Tier-2: each changes a shipped kit's checker in `tools/memory-tree/`.
- Every verdict stays byte-identical: no check weakened, no population skipped, no exemption added.
- `memory/builds/dDeclaredLoop/`, the live run's worktree `unattended-declared-loop-d56bf0`, its branch and its run-state file are not touched.
- No spec audit: not declared (owner, at kickoff).
- R5 (the commit recipe and the render stamp), R6 and the spec-writer prompt scope are out: owner decisions.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aHastenedSweep-1` | check 25's by-name END loop tests `index()` before `test_whole_token` |
| 2 | `TOOL-aHastenedSweep-2` | `gotchas.selectable` computes basenames once, and `corpus_ids.walk` computes `_roots` once per walk |
| 3 | `TOOL-aHastenedSweep-3` | the hygiene shell hands `corpus_ids.py --check` its index set when checks 1 to 5 recorded no failure |
| 4 | `TOOL-aHastenedSweep-4` | checks 13 to 16 and 17 to 19 run in one Python process over one frozen, memoized walk |
| 5 | `TOOL-aHastenedSweep-5` | the memory-tree kit contract names every `gotchas.py` verb the hygiene shell launches (closing review round 1: H1) |
| 6 | `TOOL-aHastenedSweep-6` | every arm this build added can go red on its regression, and every comment and map line describes the one-process launch (closing review round 1: M1 to M4, L1 to L4) |
| 7 | `TOOL-aHastenedSweep-7` | the hygiene suite's assertion floor pinned to the count the close measured, so a stranded block of arms reds it (adopted at the close) |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 7 unit(s) · node a · opened 2026-11-15 · streams tooling
ids TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4 TOOL-aHastenedSweep-5 TOOL-aHastenedSweep-6 TOOL-aHastenedSweep-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aHastenedSweep-1 — check 25's by-name pass tests `index()` before `test_whole_token`](spec/2026-11-15-spec-TOOL-aHastenedSweep-1.md) | 1 | 2 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aHastenedSweep-2 — `selectable` computes each basename once, and `walk` derives its roots once](spec/2026-11-15-spec-TOOL-aHastenedSweep-2.md) | 1 | 2 | CLOSED | rev-1 | 2026-11-15 |
| [TOOL-aHastenedSweep-3 — the hygiene shell hands `corpus_ids.py --check` its index set when checks 1 to 5 ran clean](spec/2026-11-15-spec-TOOL-aHastenedSweep-3.md) | 2 | 2 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aHastenedSweep-4 — checks 13 to 16 and 17 to 19 run in one Python process over one frozen, memoized walk](spec/2026-11-15-spec-TOOL-aHastenedSweep-4.md) | 3 | 2 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aHastenedSweep-5 — the memory-tree kit contract names every `gotchas.py` verb the hygiene shell launches](spec/2026-11-16-spec-TOOL-aHastenedSweep-5.md) | 4 | 2 | CLOSED | rev-1 | 2026-11-16 |
| [TOOL-aHastenedSweep-6 — every arm this build added can go red on its regression, and every comment and map line describes the one-process launch](spec/2026-11-16-spec-TOOL-aHastenedSweep-6.md) | 5 | 1 | CLOSED | rev-2 | 2026-11-16 |
| [TOOL-aHastenedSweep-7 — the hygiene suite's assertion floor pinned to the count the close measured, so a stranded block of arms reds it](spec/2026-11-16-spec-TOOL-aHastenedSweep-7.md) | 6 | 1 | CLOSED | rev-1 | 2026-11-16 |
<!-- /gen:build-units -->

Records: 11 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aHastenedSweep-1 TOOL-aHastenedSweep-2 TOOL-aHastenedSweep-3 TOOL-aHastenedSweep-4 TOOL-aHastenedSweep-5 TOOL-aHastenedSweep-6 TOOL-aHastenedSweep-7.

Ids whose spec moved past its audited revision: none — 0 of 7 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aHastenedSweep-1`, `TOOL-aHastenedSweep-2` | yes |
| 2 | `TOOL-aHastenedSweep-3` | no |
| 3 | `TOOL-aHastenedSweep-4` | no |
| 4 | `TOOL-aHastenedSweep-5` | no |
| 5 | `TOOL-aHastenedSweep-6` | no |
| 6 | `TOOL-aHastenedSweep-7` | no |

A step's `Parallel` yes means its units share an order; BUILD-METHOD M6 still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| run state | `RUN.md` |
| the units | the units table above |
| briefs | `2026-11-16-prompt-TOOL-aHastenedSweep-7-brief.md`, `2026-11-16-prompt-TOOL-aHastenedSweep-5-brief.md` and 1 more under prompts/ |
| reviews | `2026-11-16-review-TOOL-aHastenedSweep-1-2-3-4-diff-review-round1.md` (CLEAN WITH FIXES) |
| logs | `2026-11-16-build-TOOL-aHastenedSweep-7-1-acceptance-ledger.md`, `2026-11-16-build-TOOL-aHastenedSweep-6-1-acceptance-ledger.md` and 5 more under build/ |
| card ref | `refs/gov/builds/aHastenedSweep/card` |
<!-- /gen:build-routes -->
