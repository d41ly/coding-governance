---
slug: aSwiftRefusal
node: a
opened: 2026-11-10
streams: tooling
roster: TOOL
ids: TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3 TOOL-aSwiftRefusal-4
---

# aSwiftRefusal — `--dispatch` refuses cheaply first, and a deferral stops blocking

## The problem this build exists to solve

`--dispatch` runs the spec-token check over the whole live tree, about ten minutes on node a, before
the order gate and the sibling-overlap check, which need only the run-state file and the spec
headers. A unit set aside with `--rescope --act defer` also blocks every later order and keeps its
declared paths reserved for the rest of the run. In dOrderedCharter each of three refusals cost a
builder 10 to 18 minutes and up to 37k output tokens. The prompt is in `prompts/`.

## Expected improvements

- Order, overlap and every other cheap refusal arrive in seconds.
- A deferred unit stops blocking later orders and releases its open passes.

## Detriments if this is not built

- Every cheap refusal keeps costing a builder agent a full spec-token run.
- A run that defers one unit cannot dispatch past it without re-ordering specs.
- A deferred unit's paths stay reserved until a commit carrying its `Pass:` trailer lands.

## Build-level rules

- **Classification (M2)**: three units, MISSING at open, Tier-2: `unattended.sh` is a shipped kit
  file. One mechanism each: the reorder, the order gate's deferral, the open-pass release.
- A unit is deferred when its spec reads DEFERRED and its latest `rescope · item defer` row follows
  every dispatch row it has. One predicate, read by both the order gate and `read_open_passes`.
- Every refusal's text is unchanged.
- Kit versions move through the lander's `mint`, never by hand.
- No spec audit: not declared.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aSwiftRefusal-1` | `verb_dispatch` runs the spec-token check after every refusal decidable from the run-state file and the spec headers |
| 2 | `TOOL-aSwiftRefusal-2` | the order gate lets an earlier-order unit pass when the deferral predicate holds for it |
| 3 | `TOOL-aSwiftRefusal-3` | `read_open_passes` leaves out every key of a deferred unit, naming each on stderr |
| 4 | `TOOL-aSwiftRefusal-4` | promoted from the closing review: round 1's four mediums and three lows, batched — check 23 and `--rescope` read the deferral through the one predicate, the floors, the `--audit` arm, the positive control and the contract text |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node a · opened 2026-11-10 · streams tooling
ids TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3 TOOL-aSwiftRefusal-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aSwiftRefusal-1 — `--dispatch` runs the spec-token check after every cheap refusal](spec/2026-11-10-spec-TOOL-aSwiftRefusal-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-10 |
| [TOOL-aSwiftRefusal-2 — the order gate lets a deferred earlier-order unit pass](spec/2026-11-10-spec-TOOL-aSwiftRefusal-2.md) | 2 | 2 | CLOSED | rev-3 | 2026-11-10 |
| [TOOL-aSwiftRefusal-3 — `read_open_passes` leaves out every key of a deferred unit, naming each on stderr](spec/2026-11-10-spec-TOOL-aSwiftRefusal-3.md) | 3 | 2 | CLOSED | rev-3 | 2026-11-10 |
| [TOOL-aSwiftRefusal-4 — round 1's mediums and lows: one deferral answer for `--rescope` and check 23, the floors, the `--audit` arm, the positive control and the contract text](spec/2026-11-10-spec-TOOL-aSwiftRefusal-4.md) | 4 | 2 | CLOSED | rev-2 | 2026-11-10 |
<!-- /gen:build-units -->

Records: 16 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-2 TOOL-aSwiftRefusal-3 TOOL-aSwiftRefusal-4.

Ids whose spec moved past its audited revision: none — 0 of 4 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aSwiftRefusal-1` | no |
| 2 | `TOOL-aSwiftRefusal-2` | no |
| 3 | `TOOL-aSwiftRefusal-3` | no |
| 4 | `TOOL-aSwiftRefusal-4` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
