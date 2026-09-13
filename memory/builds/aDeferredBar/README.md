---
slug: aDeferredBar
node: a
opened: 2026-09-13
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 TOOL-aDeferredBar-3 TOOL-aDeferredBar-4 TOOL-aDeferredBar-5 TOOL-aDeferredBar-6
---

# aDeferredBar — no merge bar and no self-test suite inside a build pass

## The problem this build exists to solve

Unattended builds tell the agents that build their units to run the merge bar — often the full
one, or a kit's self-test suite — inside the unit, and a unit then stalls for hours. Three carriers
instruct it: a spec whose acceptance criterion names `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`
as the observation, the build method's "diff-scoped gates" sentence that has no spelling narrower
than the bar, and nothing at the act that refuses. The trace and the corpus counts are under `build/`.

## Expected improvements

- A unit pass runs the one direct check its spec names, in seconds, and never a bar or a suite.
- A spec cannot name a full bar or a suite as an acceptance observation; the memory gate reds it.
- The act is refused inside every agent, sidechain included, while the run is before `VERIFYING`.
- The full bar runs once, after the build is complete, where the owner ruled it belongs.

## Detriments if this is not built

- Every unattended unit keeps paying one to four hours of wall clock for a verdict the close repeats.
- Two runs on one host keep contending on the turnstile from inside their units.
- The instruction keeps being re-derived per spec by a writer who cannot see the ledger.

## Build-level rules

- **Three mechanisms, three units, sequential.** The instruction (every carrier a build agent
  reads), the spec gate, the act refusal. Classified at opening: all three MISSING.
- **The owner's three sentences are the acceptance, verbatim.** Full gates not until the build is
  complete; if necessary, scoped; unattended self-tests and gates never inside build agents.
- **Scoped means the plain bar, no flag**, on the run's branch, at the main loop, at most once per
  pass whose files a leg guards. That is the manifest's own definition and nothing new is built for it.
- **The governance carriers named by the mandate are in scope**, and the method's byte budget is
  NOT raised: the M6 edit fits under it or the sentence is trimmed elsewhere in M6.
- **Every gate here has its failing case observed RED before it lands**, by the direct invocation
  of the checker or the hook on a fixture — never by the suite, which is what this build forbids.
- **This build's own units obey the rule from unit 1 onward**: a child that needs a suite verdict
  returns it to the main loop, which runs the owed `GATE_SELFTESTS=1` bar at `VERIFYING`.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aDeferredBar-1` | MISSING | the instruction: no bar and no suite inside a pass, stated at every carrier a build agent reads |
| 2 | `TOOL-aDeferredBar-2` | MISSING | the spec gate: a bar or suite invocation as a §6 observation or §7 leg token is a refusal |
| 3 | `TOOL-aDeferredBar-3` | MISSING | the act refusal: a PreToolUse hook denies a full bar or a suite while the run is before VERIFYING |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 3 unit(s) · node a · opened 2026-09-13 · streams tooling
ids TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 TOOL-aDeferredBar-3 TOOL-aDeferredBar-4 TOOL-aDeferredBar-5 TOOL-aDeferredBar-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aDeferredBar-1 — the instruction: no bar and no suite inside a pass, at every carrier a build agent reads](spec/2026-09-13-spec-TOOL-aDeferredBar-1.md) | 1 | 2 | CLOSED | rev-4 | 2026-09-14 |
| [TOOL-aDeferredBar-2 — the spec gate: a bar or suite invocation is not an acceptance observation](spec/2026-09-13-spec-TOOL-aDeferredBar-2.md) | 2 | 2 | SPECCED | rev-3 | 2026-09-14 |
| [TOOL-aDeferredBar-3 — the act refusal: a PreToolUse hook denies a flagged bar or a suite before VERIFYING](spec/2026-09-13-spec-TOOL-aDeferredBar-3.md) | 3 | 2 | SPECCED | rev-3 | 2026-09-14 |
<!-- /gen:build-units -->

Records: 10 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aDeferredBar-1` | no |
| 2 | `TOOL-aDeferredBar-2` | no |
| 3 | `TOOL-aDeferredBar-3` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
