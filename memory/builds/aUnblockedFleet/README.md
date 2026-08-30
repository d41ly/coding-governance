---
slug: aUnblockedFleet
node: a
opened: 2026-08-31
streams: tooling
roster: TOOL
ids: TOOL-aUnblockedFleet-1
status: OPEN
authorized-by: prompt
---

# aUnblockedFleet — unattended runs stop blocking each other out

## The problem this build exists to solve
`--preflight` refuses to start a run while ANY other build in the tree holds a non-terminal
run-state file, and the merge bar's leg check 7 reds for the same reason. The two checks are the
driver's `check_single_live()` and `check-unattended.sh`'s check 7, and both carry one stated
justification: that otherwise "the run" is not well-defined for anything keyed on it.

**Measured before this folder was written: nothing is keyed on it.** All fourteen driver verbs take a
`<slug>`. All three of the leg's tree-wide loops over `builds/*/RUN*.md` grade each file
independently. No code path in this repository resolves "the run" without being told which build, so
the population the rule makes singular is a population nobody reads. The invariant's only consumers
are the two checks that enforce it.

The cost of that is not theoretical and is already on the record three times. `TOOL-aFusedCharter-4`
measured three builds wedged at `LANDING` on 2026-08-19, resolvable only by marking two honest runs
`ABORTED`. `TOOL-aBoundedVerdict-24` records a run that closed but could not land reddening every
later run's bar. `TOOL-aReapedTicket-5` records that a run dying in `BUILDING` blocks every future run
on the repository forever, with no override on that check — and notes the asymmetry that makes it a
liveness bug rather than bookkeeping: the phase is ASSERTED by the run itself, so a run that cannot
assert leaves the strongest possible claim standing.

One patch already exists for one phase. `TOOL-aPrimedKeepalive-4`/`-7` excludes a `LANDING` record
whose witness is an ancestor of the observed remote anchor. It works, it is the reason this very run
could preflight at all, and it is a special case for one of the twelve phases.

## Expected improvements
- A run starts when the repository is ready for it, not when every other node has finished.
- A dead run's abandoned record stops being an un-overridable, tree-wide, permanent refusal.
- The `LANDING`-witness special case stops being load-bearing, because the population it rescues one
  member of is no longer counted tree-wide at all.
- Concurrent unattended runs across nodes become the ordinary case the charter's §3 stream model
  already assumes, rather than a state two gates refuse.
- One guard the tree-wide rule never provided is GAINED: a second `--preflight` against a slug whose
  own record is live is currently a silent clobber (`TOOL-aBranchedMandate-8`, OPEN, reproduced on a
  real run's own record).

## Detriments if this is not built
- Every unattended run on this fleet is serialized behind every other one, on a repository whose
  stated purpose is concurrent multi-node coding.
- The fleet's recorded remedy for the wedge is falsifying run records, which it has now done twice.
- Each new non-terminal phase added to the vocabulary needs its own bespoke exclusion, and eleven of
  the twelve currently have none.

## Build-level rules
- **The load-bearing claim is TESTED, not argued.** "Nothing keys on tree-wide singularity" is what
  the whole build rests on. Unit 1 refutes-or-confirms it by construction — a fixture tree with two
  live records, every driver verb and the full leg run over it — and the result is recorded whichever
  way it falls. A test that cannot fail is the defect the merge bar is full of gates against.
- **Scoping is not deletion.** The per-slug rule must REFUSE what the tree-wide rule refused within a
  slug, and the clobber guard is proven by a staged break, not inferred from the code reading.
- **A new gate is not landed until its failing case has been observed** (template §7). Both halves
  stage the break, confirm RED, and unstage.
- **Two carriers state this rule and they may not disagree.** `UNATTENDED-PROTOCOL.md` §3 and the
  kit's `SKILL.template.md` are rendered from the kit; a change to one that skips the other ships a
  repository whose contract and whose instructions differ.
- **The governance-carrier change is the GOAL, not a fork.** M3's veto 2 bars a run from resolving a
  fork by changing a governance carrier. This build's carrier change is the owner's stated
  instruction, so the veto does not reach it. Nothing else in the protocol is touched.
- **What this build does NOT claim to fix**, named here so no reader infers it: the lander-marker
  race between two runs landing from one clone. That is a separate defect, it fails CLOSED today
  (`--landed` refuses on a marker/HEAD mismatch and names both shas), and admitting concurrency makes
  it reachable rather than creating it. It gets a backlog row, not a unit.

## Parked decisions
*(none yet — this section is where a refused decision lands, with its question, the options seen,
and why the run refused it.)*

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aUnblockedFleet-1` | 2 | the driver: `check_single_live()` counts within the run's own slug instead of the tree |
| 2 | `TOOL-aUnblockedFleet-2` | 2 | the leg: check 7 grades per build folder instead of tree-wide |
| 3 | `TOOL-aUnblockedFleet-3` | 1 | the carriers: protocol §3 and the kit `SKILL.template.md` state the scoped rule |
| 4 | `TOOL-aUnblockedFleet-4` | 1 | the test arms for both halves, each with its failing case observed |
| 5 | `TOOL-aUnblockedFleet-5` | 1 | the records: three OPEN backlog rows closed or re-scoped, one decision row, the marker-race row filed |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-08-31 · streams tooling
ids TOOL-aUnblockedFleet-1

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
