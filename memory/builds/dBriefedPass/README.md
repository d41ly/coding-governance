---
slug: dBriefedPass
node: d
opened: 2026-09-01
streams: tooling
roster: TOOL
status: OPEN
authorized-by: prompt
ids: TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5
---

# dBriefedPass — the harness that orders a build's passes, and the refusal that makes the order real

## The problem this build exists to solve
An unattended build is told to spec a unit before building it, and nothing refuses it when it does
not. `plan_state` computes the M2 classification at exactly two call sites — `--plan`, which only
reports, and `--close`, which runs after every commit has landed — so a run that builds first and
writes the spec afterwards passes `build-complete`, because by close time the spec exists. The
ordering rule is carried entirely by an agent's memory across a context that compacts. Nothing
records what a building agent was handed either, so "which instructions produced this diff" has no
answer on disk.

## Expected improvements
- A build pass on an unspecced, THIN or out-of-order unit is REFUSED at the moment of the act.
- A unit whose build commit predates its spec reds the merge bar, so postfactum speccing is caught
  in history rather than trusted at close.
- What each building agent was handed becomes a tracked record joined to its spec.
- `plan_state` stops grading Tier-1 specs on the wrong three sections.

## Detriments if this is not built
- Every unattended build keeps carrying its own pass ordering in an agent's recollection.
- The THIN predicate stays blind on Tier-1 specs: it reads Gates as acceptance, so a Tier-1 spec
  stating no acceptance criterion at all is graded READY.
- A diff's governing instructions stay unreconstructable after the run that produced them ends.

## Build-level rules
- **Convergence stays; no review-round cap.** Owner ruling, 2026-09-01, at this run's one turn. The
  prompt proposed "two review passes at most"; the shipped `--review` loop refuses a cap with a
  measurement and the owner kept it. The harness calls `--review` and obeys its verdict.
- **Mandatory, plus a history-based gate.** Owner ruling, same turn. The harness is the declared
  route AND a merge-bar leg refuses a unit built before its spec existed. Carrier edits are in scope
  because the owner's prompt asks for them.
- **The harness cannot read the tree, and no unit may pretend otherwise.** A `Workflow` script has no
  filesystem: every observation it makes is a claim its own agent returned. It buys pass ORDER by
  control flow; enforcement lives in the driver, where the tree is readable.
- **`plan_state` is a prerequisite, not a side-quest.** Unit 1 lands before any unit gates on it.

## Parked decisions
- None yet.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dBriefedPass-1` | OPEN | `plan_state` grades a spec by heading TITLE, not by ordinal |
| 2 | `TOOL-dBriefedPass-2` | OPEN | the unit BRIEF — a tracked record of what a building agent was handed |
| 3 | `TOOL-dBriefedPass-3` | OPEN | a build pass on an unspecced, THIN or out-of-order unit is REFUSED |
| 4 | `TOOL-dBriefedPass-4` | OPEN | the harness — one Workflow script driving spec, audit, fold and build in order |
| 5 | `TOOL-dBriefedPass-5` | OPEN | the carriers declare the harness the route, and the gate leg reads history |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-09-01 · streams tooling
ids TOOL-dBriefedPass-1 TOOL-dBriefedPass-2 TOOL-dBriefedPass-3 TOOL-dBriefedPass-4 TOOL-dBriefedPass-5

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

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
