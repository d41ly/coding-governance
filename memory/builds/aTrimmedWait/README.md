---
slug: aTrimmedWait
node: a
opened: 2026-11-14
streams: tooling
roster: TOOL
status: OPEN
ids: TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7
---

# aTrimmedWait — builds stop waiting on checks that grade more than the caller needs, without moving any verdict

## The problem this build exists to solve

Session `db957487` ran dFairHearing and aSmoothedDispatch: 334 agents and 72 h of agent wall time.
Its largest reworkable costs were waits, not work. Units were re-dispatched after `--dispatch`
refused specs it could have refused before the spec commit. Hygiene check 12 graded every spec to
check one. The pre-commit hook refused commits on a stale build index the commit could have
rendered. The idle-wake `--resume` re-ran the whole audit when nothing had moved. Builders polled
their own background work. `handoff.py agents` re-parsed a 51 MB transcript on every call. The
measurements and their scripts are recorded in the brief under `prompts/`.

## Expected improvements

- A spec defect `--dispatch` would refuse is refused before the spec commit.
- One spec or one build is graded by check 12 in seconds, not 376 s.
- A commit renders its own index instead of being refused on check 9.
- An unmoved run's `--resume` tick returns its last verdict.
- A role agent cannot poll; it waits on the notification.
- `handoff.py agents` reads only a transcript's appended bytes.

## Detriments if this is not built

- Every build keeps paying for re-dispatched units: about 30 h in the measured session.
- Spec writers keep spending 4-6 min per hygiene run, and commits keep costing 66-110 s.
- The main loop keeps blocking for 51 s per idle tick, and builders keep idling on `tail -f`.

## Build-level rules

- **No verdict moves.** Each unit's acceptance is one command timed before and after on node a,
  plus a fixture showing the same refusals, reds and greens. A speed-up that moves a verdict is out.
- **Reuse the owner's predicates** ([one-fact]): a pre-check calls the driver's own reader, never a copy.
- **The full run and the bar keep grading everything**; only the caller-scoped paths narrow.
- **Re-verified at open, against main `846d51d39`**: R4 shrank to `--resume`, because a refused
  `--release-task` took 4.7 s, not 47 s. R5 shrank to the polling refusal and the `-eo pipefail`
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
| 4 | `TOOL-aTrimmedWait-4` | R3: `gen_build_index.py --write` re-renders only the regions its changed inputs reach |
| 5 | `TOOL-aTrimmedWait-5` | R4: `--resume` prints its last verdict when HEAD, the run-state file and the task registry are unchanged |
| 6 | `TOOL-aTrimmedWait-6` | R5: the scratch guard refuses a role agent's polling wait, and G3 reads past `-o pipefail` |
| 7 | `TOOL-aTrimmedWait-7` | R6: `handoff.py agents` caches parsed calls per transcript and parses only appended bytes |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-14 · streams tooling
ids TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.

Ids whose spec moved past its audited revision: none — 0 of 0 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
