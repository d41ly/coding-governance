---
slug: aSmoothedDispatch
node: a
opened: 2026-11-10
streams: tooling
roster: TOOL
status: OPEN
ids: TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6
---

# aSmoothedDispatch — five mechanical refusals that cost every unattended run turns and re-dispatches

## The problem this build exists to solve

The driver journal across 38 runs logs 287 `--dispatch` refusals from the spec-token checker (947 min
of check time) and 197 "unknown argument" refusals, most of them bare paths after `--writes`. In
dFairHearing, builders' product edits were blocked 63 times by a card route still naming a closed unit.
Agents also declared the run-state file and asked for `--help`, and both were refused. Each refusal costs
a turn, a spec rewrite or a fresh builder. The analysis is in the brief under `prompts/`.

## Expected improvements

- `--dispatch` refuses only on this build's own spec-token reds, and re-checks only when its inputs move.
- `--writes a b c` and a quoted list declare every path.
- A dispatched unit's builder can write without a hand-appended route.
- `--help` answers, and a declared run-state file is dropped with a note.

## Detriments if this is not built

- Every run keeps paying ~12 min per spec-token refusal and a re-dispatch per miss.
- Agents keep losing turns to argument-shape refusals that carry no information.

## Build-level rules

- **Classification (M2)**: six units, each MISSING at open, Tier-2: each changes a shipped kit's contract.
- Units 1, 2, 3, 4 and 6 edit `tools/unattended/unattended.sh`, so they build one at a time; unit 5 is disjoint.
- Kit versions move through the lander's `mint`, never by hand.
- No spec audit: the owner declined one.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aSmoothedDispatch-1` | `--writes` takes every path up to the next flag, and a whitespace-joined value splits into its paths |
| 2 | `TOOL-aSmoothedDispatch-2` | `--dispatch` drops the run-state file from its declared writes with a note instead of refusing |
| 3 | `TOOL-aSmoothedDispatch-3` | `unattended.sh --help` prints the verb list and exits 0 |
| 4 | `TOOL-aSmoothedDispatch-4` | `--dispatch`'s spec-token check grades the dispatching build's specs, and skips when its inputs match the last green check |
| 5 | `TOOL-aSmoothedDispatch-5` | scratch-guard lets `gov-spec-writer` run the spec-token checker over the spec it wrote |
| 6 | `TOOL-aSmoothedDispatch-6` | a dispatched unit counts as routed, so its builder's product writes are not refused on a stale card route |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-11-10 · streams tooling
ids TOOL-aSmoothedDispatch-1 TOOL-aSmoothedDispatch-2 TOOL-aSmoothedDispatch-3 TOOL-aSmoothedDispatch-4 TOOL-aSmoothedDispatch-5 TOOL-aSmoothedDispatch-6

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
