---
slug: aTrimmedWait
node: a
opened: 2026-11-14
streams: tooling
roster: TOOL
ids: TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7
---

# aTrimmedWait — builds stop waiting on checks that grade more than the caller needs, without moving any verdict

## The problem this build exists to solve

Session `db957487` ran dFairHearing and aSmoothedDispatch: 334 agents and 72 h of agent wall time.
Its largest reworkable costs were waits, not work. Units were re-dispatched after `--dispatch`
refused specs it could have refused before the spec commit. Hygiene check 12 graded every spec to
check one. The pre-commit hook refused commits on a stale build index the commit could have
rendered. The idle-wake `--resume` re-ran the whole audit when nothing had moved. Builders polled
their own background work. `handoff.py agents` re-parsed a 51 MB transcript on every call. The <!-- PINNED 2026-11-14 -->
measurements and their scripts are recorded in the brief under `prompts/`.

## Expected improvements

- A spec defect `--dispatch` would refuse is refused before the spec commit.
- One spec or one build is graded by check 12 in seconds, not 376 s. <!-- PINNED 2026-11-14 -->
- A commit renders its own index instead of being refused on check 9.
- An idle-wake `--resume` tick hashes every brief in one git call, not one per brief.
- A role agent cannot poll; it waits on the notification.
- `handoff.py agents` reads only a transcript's appended bytes.

## Detriments if this is not built

- Every build keeps paying for re-dispatched units: about 30 h in the measured session.
- Spec writers keep spending 4-6 min per hygiene run, and commits keep costing 66-110 s.
- The main loop keeps blocking for 51 s per idle tick, and builders keep idling on `tail -f`. <!-- PINNED 2026-11-14 -->

## Build-level rules

- **No verdict moves.** Each unit's acceptance is one command timed before and after on node a,
  plus a fixture showing the same refusals, reds and greens. A speed-up that moves a verdict is out.
- **Reuse the owner's predicates** ([one-fact]): a pre-check calls the driver's own reader, never a copy.
- **The full run and the bar keep grading everything**; only the caller-scoped paths narrow.
- **Re-verified at open, against main `846d51d39`**: R4 shrank to `--resume`, because a refused
  `--release-task` took 4.7 s, not 47 s. R5 shrank to the polling refusal and the `-eo pipefail` <!-- PINNED 2026-11-14 -->
  option gap, because G3 already refuses every plain suite launch the probe tried.
- No spec audit: the owner declined it at kickoff.
- Kit versions move once, after the last code move.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aTrimmedWait-1` | R1: one pre-commit spec validation that runs `--dispatch`'s cheap refusals through the driver's own predicates, wired into the spec stage and the writer's instructions |
| 2 | `TOOL-aTrimmedWait-2` | R2: hygiene check 12 graded over one named spec or build, with the writer told to use it |
| 3 | `TOOL-aTrimmedWait-3` | R3: the pre-commit hook renders the staged builds' index before check 9 grades it, and stages what it wrote |
| 4 | `TOOL-aTrimmedWait-4` | R3: `gen_build_index.py --write` writes only the artifacts whose rendered bytes moved (owner, 2026-11-14) |
| 5 | `TOOL-aTrimmedWait-5` | R4: `--resume` and `--status` hash every brief in one `git hash-object --stdin-paths` call, every line byte-identical (owner, 2026-11-14) |
| 6 | `TOOL-aTrimmedWait-6` | R5: the scratch guard refuses a role agent's polling wait, and G3 reads past `-o pipefail` |
| 7 | `TOOL-aTrimmedWait-7` | R6: `handoff.py agents` caches parsed calls per transcript and parses only appended bytes |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 7 unit(s) · node a · opened 2026-11-14 · streams tooling
ids TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTrimmedWait-1 — `unattended.sh --check-specs` refuses, before the spec commit and through `--dispatch`'s own predicates, every spec defect `--dispatch` refuses from the spec files alone](spec/2026-11-14-spec-TOOL-aTrimmedWait-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aTrimmedWait-2 — hygiene check 12 grades one named spec or one build on request, and the spec writer is told to run it that way](spec/2026-11-14-spec-TOOL-aTrimmedWait-2.md) | 2 | 2 | CLOSED | rev-4 | 2026-11-14 |
| [TOOL-aTrimmedWait-3 — a commit refused on build-index drift renders its own index, stages it and is graded again](spec/2026-11-14-spec-TOOL-aTrimmedWait-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aTrimmedWait-4 — `gen_build_index.py --write` writes only the artifacts whose bytes moved](spec/2026-11-14-spec-TOOL-aTrimmedWait-4.md) | 4 | 2 | INPROGRESS | rev-3 | 2026-11-14 |
| [TOOL-aTrimmedWait-5 — the holder's idle-wake `--resume` stops paying one git process per briefed unit](spec/2026-11-14-spec-TOOL-aTrimmedWait-5.md) | 5 | 2 | SPECCED | rev-3 | 2026-11-14 |
| [TOOL-aTrimmedWait-6 — the role gate refuses a role agent's polling wait, and steps past an option cluster such as `-eo pipefail`](spec/2026-11-14-spec-TOOL-aTrimmedWait-6.md) | 6 | 2 | SPECCED | rev-2 | 2026-11-14 |
| [TOOL-aTrimmedWait-7 — `handoff.py agents` keeps its parsed session calls per transcript and parses only the bytes appended since](spec/2026-11-14-spec-TOOL-aTrimmedWait-7.md) | 7 | 2 | SPECCED | rev-3 | 2026-11-14 |
<!-- /gen:build-units -->

Records: 27 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7.

Ids whose spec moved past its audited revision: none — 0 of 7 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aTrimmedWait-1` | no |
| 2 | `TOOL-aTrimmedWait-2` | no |
| 3 | `TOOL-aTrimmedWait-3` | no |
| 4 | `TOOL-aTrimmedWait-4` | no |
| 5 | `TOOL-aTrimmedWait-5` | no |
| 6 | `TOOL-aTrimmedWait-6` | no |
| 7 | `TOOL-aTrimmedWait-7` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
