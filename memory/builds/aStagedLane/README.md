---
slug: aStagedLane
node: a
opened: 2026-09-04
streams: tooling
roster: TOOL
parents: dBriefedPass
ids: TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3 TOOL-aStagedLane-4
---

# aStagedLane — the deterministic route for spec work, and the gate that binds a session which never takes it

## The problem this build exists to solve
Spec-before-build is enforced for unattended runs and for nothing else.
`tools/unattended/check-pass-order.sh` states at its line 25 that it checks nothing about a build
with no run-state file, so the merge-bar leg refusing a unit built before its spec covers unattended
builds only. The harness that orders the three stages is bound to the same driver: `--dispatch`
refuses without a run-state file, measured on this node against a build that never had one. An
ordinary session therefore has no fixed route. Spec work happens inline against the whole session
context, or through an Agent, or through a Workflow, and which of the three is a per-session
accident. The classifier that would ground it already runs without a run-state file, and
`memory/guides/BUILD-METHOD.md` names it once, qualified to a mandate.

## Expected improvements
- A unit built before its spec reds the merge bar on any build, not only one carrying a run-state
  file.
- The three-stage order becomes available to a session working without a mandate.
- Each spec writer receives its own brief rather than the session's accumulated context.
- The detect step names the classifier that already answers it.

## Detriments if this is not built
- Attended builds keep carrying pass order in an agent's recollection, which is the defect
  `TOOL-dBriefedPass-4` closed for unattended runs alone.
- One agent keeps writing every spec of a build from one context, so a late unit is written with
  the earlier units' debris still in scope.
- The classifier stays reachable only to runs under a mandate, while working for every other run.

## Build-level rules
- **The gate lands first and binds hardest.** Only `TOOL-aStagedLane-1` reaches a session that never
  invokes a harness. Units 2 and 3 make the good route available; unit 1 makes the bad route fail.
- **Attended mode is WEAKER than unattended mode, and every unit says so.** `--dispatch` refuses at
  the moment of the act and records the write sets. `--plan` only reports. An attended stage-three
  refusal is an agent's claim about that report, and no unit may describe the two as equivalent.
- **No second harness file.** Splitting spec-writing from spec-building into separate scripts
  rebuilds the defect `tools/workflows/unattended-build.js` exists to close, where a unit is built
  and its spec written afterwards. The mode is an argument, never a file.
- **No unit restates a gate's rules inside a prompt.** The scratchpad script that motivated this
  build carried sixty lines of spec rules retyped from `memory/TEMPLATE-SPEC.md`, and its account of
  the placeholder scan was already wrong on the day it was typed. Briefs point at the format.
- **Units 2 and 3 are sequenced, not concurrent.** Their write sets intersect at
  `tools/workflows/unattended-build.js`, so clause 1 of the parallelism rule is unsatisfied.

## Parked decisions
- **The harness cannot detect its own mandate.** The owner ruled that attended mode WARNS rather
  than refuses when a run-state file exists, and a workflow script has no filesystem, so the
  detection is the caller's and a caller that supplies nothing gets no warning. Unit 2 names the
  limit in its scope rather than implying the warning is reliable.
- **The harness self-test is on no bar.** `TOOL-dBriefedPass-7` is open:
  `tools/workflows/unattended-build.test.sh` is a 21-arm suite in no manifest, so units 2 and 3 add
  arms to a suite nobody runs. That row says registering it belongs to a unit that specs it, and no
  unit here does.
- **The pass-order leg is already over its ceiling.** `TOOL-dSealedTally-2` records it at 134
  seconds against a declared 90. Unit 1 enlarges its population, so a re-declaration is owed with
  the reading behind it.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aStagedLane-1` | OPEN | the pass-order leg grades builds that carry no run-state file |
| 2 | `TOOL-aStagedLane-2` | OPEN | an attended mode on the harness, so the stage order needs no mandate |
| 3 | `TOOL-aStagedLane-3` | OPEN | the spec stage fans over slices, each writer holding only its brief |
| 4 | `TOOL-aStagedLane-4` | WONTDO | the carriers name the classifier and the attended route — RETIRED, does not fit the method's byte budget; parked for the owner |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 4 unit(s) · node a · opened 2026-09-04 · streams tooling
ids TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3 TOOL-aStagedLane-4

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aStagedLane-1 — the pass-order leg grades builds that carry no run-state file](spec/2026-09-04-spec-TOOL-aStagedLane-1.md) | 1 | 2 | SPECCED | rev-4 | 2026-09-04 |
| [TOOL-aStagedLane-2 — an attended mode on the harness, so the stage order needs no mandate](spec/2026-09-04-spec-TOOL-aStagedLane-2.md) | 2 | 2 | SPECCED | rev-4 | 2026-09-04 |
| [TOOL-aStagedLane-3 — the spec stage fans over slices, each writer holding only its brief](spec/2026-09-04-spec-TOOL-aStagedLane-3.md) | 3 | 2 | SPECCED | rev-4 | 2026-09-04 |
| [TOOL-aStagedLane-4 — the carriers name the classifier and the attended route](spec/2026-09-04-spec-TOOL-aStagedLane-4.md) | 4 | 2 | WONTDO | rev-4 | 2026-09-04 |
<!-- /gen:build-units -->

Records: 2 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aStagedLane-1` | no |
| 2 | `TOOL-aStagedLane-2` | no |
| 3 | `TOOL-aStagedLane-3` | no |
| 4 | `TOOL-aStagedLane-4` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dBriefedPass](../dBriefedPass/README.md)
<!-- /gen:build-edges -->
