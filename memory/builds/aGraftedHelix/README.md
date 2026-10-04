---
slug: aGraftedHelix
node: a
opened: 2026-10-04
streams: tooling+kickoff
roster: TOOL
authorized-by: prompt
spec-audit: 2026-10-04
status: OPEN
ids: TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-9
---

# aGraftedHelix — six helixir mechanisms, grafted onto the kits that own their surface

## The problem this build exists to solve

A review of helixir found six mechanisms gov lacks for concurrent, multi-node, unattended builds.
Two nodes can drive one build and learn it at merge. The review harness's by-design input has no
caller. Recall shows a superseded decision as current. Ceilings are raised from timings taken under
foreign load. A duplicate or contradicting record passes every leg. And memory pressure and
self-heals go unreported. The owner's prompt and the review are in `prompts/`.

## Expected improvements

- One build has one driver across nodes, decided by the remote.
- Reviewers are told what is by design without a caller typing it.
- Recall labels a superseded record.
- A contended timing cannot raise a ceiling.
- A duplicate record reds; a near one names its relation.
- A bar pauses under memory pressure, and every self-heal is visible.

## Detriments if this is not built

- Two nodes keep double-driving one slug until the merge shows it.
- Review precision keeps paying for re-reported intentional behaviour.
- A recalled superseded decision keeps steering new work.
- Ceilings keep absorbing contention, so a slow leg and a starved one read the same.
- Duplicate and contradicting records keep accumulating across nodes.

## Build-level rules

- Integrate into the kit that owns each surface; no new kit (the prompt record says why).
- Reuse first: run-lease, `--liveness`, `input_key`, `gate-run` leg files, `derive-ceilings.py`,
  the recall index, hygiene checks, `check-wiring.sh`, the orientation card.
- Every new arm is observed RED on a staged break before it lands, and its header says what it does
  not check.
- Spec audit declared (`spec-audit:` above), one round, then disposal by severity.
- Discoveries are adopted into this build, never filed as asks (prompt record).
- Passes run sequentially: one worktree, one git index, and the harness dispatches in order.

## Parked decisions

- None yet.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aGraftedHelix-1` | 2 | the unattended driver claims a run on the remote as a CAS-updated ref, heartbeats it, releases it at a terminal, and refuses a live foreign claim |
| 2 | `TOOL-aGraftedHelix-2` | 1 | the orientation card lists the remote run claims under a two-clock rule: live, stale, hidden |
| 3 | `TOOL-aGraftedHelix-3` | 2 | a declared invariants registry that the review harness reads as its default by-design list, every row's path and id gated |
| 4 | `TOOL-aGraftedHelix-4` | 1 | recall rows carry supersession status: demoted, tagged with the superseding id, under an evidence-not-instruction banner |
| 5 | `TOOL-aGraftedHelix-5` | 2 | each leg reading is stamped faithful or contended by a foreign-load census, and only faithful readings argue a ceiling |
| 6 | `TOOL-aGraftedHelix-6` | 2 | a content-key check reds a decision row or gotcha whose normalized text duplicates another |
| 7 | `TOOL-aGraftedHelix-7` | 2 | the gate runner stops dispatching legs above a declared memory fraction and records the pause |
| 8 | `TOOL-aGraftedHelix-8` | 1 | every automatic self-heal appends to one health log the orientation card surfaces |
| 9 | `TOOL-aGraftedHelix-9` | 2 | a newly added decision row or gotcha that recall ranks as a near match must declare its relation to it |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-10-04 · streams tooling+kickoff
ids TOOL-aGraftedHelix-1 TOOL-aGraftedHelix-9

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 2 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
