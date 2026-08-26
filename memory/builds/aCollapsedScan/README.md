---
slug: aCollapsedScan
node: a
opened: 2026-08-26
streams: tooling
roster: TOOL
ids: TOOL-aCollapsedScan-1 TOOL-aCollapsedScan-2 TOOL-aCollapsedScan-3 TOOL-aCollapsedScan-4 TOOL-aCollapsedScan-5 TOOL-aCollapsedScan-6 TOOL-aCollapsedScan-7 TOOL-aCollapsedScan-8 TOOL-aCollapsedScan-9 TOOL-aCollapsedScan-10
---

# aCollapsedScan — `--plan` stops paying a process per (unit, spec)

## The problem this build exists to solve
`check-unattended.sh` check 30 runs `unattended.sh --plan` over every tracked build, and it is a
merge-bar leg with no guard, so every node pays it on every bar run. Measured on node `a`,
2026-08-26, over 70 builds: the leg costs 289 s and check 30's walk is 235 s of it, 81%. The cost is
not the walk. `verb_plan` resolves a region id to its spec with an `awk` per (unit, spec) pair and
spawns three more per spec elsewhere, so a 24-spec build costs 16.6 s against 1.5 s for a one-spec
build. An adopter reports the same leg at over 600 s. `run-unattended-gates.sh` already declares
`BUDGET_kit_gate=120` against a 28 s reading taken 2026-08-23, and check 30 landed 2026-08-25
without that ceiling being re-measured.

## Expected improvements
- The dominant term in the leg's cost stops being process creation the repo controls.
- A build's specs are read once per `--plan` instead of once per unit per spec.
- The declared `BUDGET_kit_gate` ceiling becomes meetable again rather than breached and unread.
- Every agent that runs `--plan` to pick up work waits seconds instead of tens of seconds.

## Detriments if this is not built
- The merge bar carries a permanent unguarded cost that grows with the corpus, on every node.
- The one verb an agent runs to find its next unit is the slowest thing in the kit.
- Scoping check 30 to dodge the cost stays tempting, and every scoping that dodges it also drops
  the five builds that carry the defect it exists to catch.

## Build-level rules
- **Output is the contract, and it is byte-identical.** check 30 grades the SHAPE of this verb's
  output on purpose. The change is a spawn-count change and nothing else, proven by diffing every
  build's `--plan` output against the pre-change driver rather than by reading the diff.
- **`plan_state` is not folded in.** `tools/memory-tree/marker-contract.test.sh` and
  `unattended.test.sh` both LIFT its body out of the shipped bytes and evaluate it, so it stays a
  self-contained function taking one spec path. Its one `awk` per graded unit is the floor.
- **No new verb, no new leg, no scoping change.** Cutting spawns is the only term this repo owns;
  a batch verb would save the per-invocation startup, which is 20 s of 235 s and not the problem.
- **The precedent is in this kit.** `TOOL-dNarrowedAnchor-1` cut the gate self-test the same way,
  and `run-unattended-gates.sh` carries its measurement: one spawn costs 0.019–0.039 s on a node
  with an on-access scanner, against roughly a millisecond without one.

- **The 2026-08-26 follow-up set, classified per M2 before acting.** `TOOL-aCollapsedScan-4`, `-6`
  and `-7` all entered MISSING and were authored this run. `-6` was authored straight to `WONTDO`:
  the reuse probe found hygiene check 20 already asserts what it proposed to build, and a staged
  break confirmed that check RED before the spec was written.

## Parked decisions
- **Change-scoping check 30 to the touched builds. RESOLVED as a REFUSAL, owner-delegated,
  2026-08-26 (`TOOL-aCollapsedScan-4`).** It was deferred until `TOOL-aCollapsedScan-1` was
  measured; the leg still missed its ceiling at 187 s, which reopened it. Refused on the trade: the
  scoping saves roughly 100 s of a 650 s bar, about 15%, and buys it by narrowing the only check
  that ever saw the five defective builds — check 30's own header says it is a corpus check
  deliberately, for exactly that reason. A scoped walk is also blind to a DRIVER change that breaks
  the property everywhere at once, and the driver is what `-1` had just rewritten. The ceiling was
  re-declared against a node-`a` measurement instead, which the runner's own header names as the
  other legitimate outcome.
- **Scoping check 30 to builds with a `RUN.md`.** REJECTED, 2026-08-26, on measurement rather than
  taste: all five builds that render a `NOT A UNIT` row today have no run-state file, so that
  filter walks zero of them while `_pv_seen` stays satisfied by the other 19.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aCollapsedScan-1` | 1 | one `awk` pass per build fills path/id/status maps; every per-spec lookup becomes a bash map read |
| 2 | `TOOL-aCollapsedScan-7` | 2 | `repo_root()` walks up for the conf instead of asking git, as `govkit.py` already does for this defect; the kit's second resolver goes |
| 3 | `TOOL-aCollapsedScan-4` | 1 | `BUDGET_kit_gate` re-declared against a node-`a` measurement, with the scoping alternative refused in writing |
| 4 | `TOOL-aCollapsedScan-6` | 1 | retires the finding — hygiene check 20 already gates per-file id uniqueness; flips to WONTDO only after its record corrections are observed |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 4 unit(s) · node a · opened 2026-08-26 · streams tooling
ids TOOL-aCollapsedScan-1 TOOL-aCollapsedScan-2 TOOL-aCollapsedScan-3 TOOL-aCollapsedScan-4 TOOL-aCollapsedScan-5 TOOL-aCollapsedScan-6 TOOL-aCollapsedScan-7 TOOL-aCollapsedScan-8 TOOL-aCollapsedScan-9 TOOL-aCollapsedScan-10

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aCollapsedScan-1 — one awk pass per build, and `--plan` stops spawning per (unit, spec)](spec/2026-08-26-spec-TOOL-aCollapsedScan-1.md) | 1 | 1 | CLOSED | rev-2 | 2026-08-26 |
| [TOOL-aCollapsedScan-7 — `repo_root()` takes the walk-up govkit already took for this defect](spec/2026-08-26-spec-TOOL-aCollapsedScan-7.md) | 2 | 2 | INPROGRESS | rev-2 | 2026-08-26 |
| [TOOL-aCollapsedScan-4 — `BUDGET_kit_gate` re-declared against a measurement, and the scoping refused](spec/2026-08-26-spec-TOOL-aCollapsedScan-4.md) | 3 | 1 | INPROGRESS | rev-3 | 2026-08-26 |
| [TOOL-aCollapsedScan-6 — RETIRED: hygiene check 20 already gates per-file id uniqueness](spec/2026-08-26-spec-TOOL-aCollapsedScan-6.md) | 4 | 1 | WONTDO | rev-2 | 2026-08-26 |
<!-- /gen:build-units -->

Records: 2 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aCollapsedScan-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aCollapsedScan-1` | no |
| 2 | `TOOL-aCollapsedScan-7` | no |
| 3 | `TOOL-aCollapsedScan-4` | no |
| 4 | `TOOL-aCollapsedScan-6` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
