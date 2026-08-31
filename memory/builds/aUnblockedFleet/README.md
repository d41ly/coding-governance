---
slug: aUnblockedFleet
node: a
opened: 2026-08-31
streams: tooling
roster: TOOL
ids: TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 TOOL-aUnblockedFleet-6 TOOL-aUnblockedFleet-7 TOOL-aUnblockedFleet-8
authorized-by: prompt
---

# aUnblockedFleet — unattended runs stop blocking each other out

## The problem this build exists to solve
`--preflight` refuses to start a run while ANY other build in the tree holds a non-terminal
run-state file, and the merge bar's leg check 7 reds for the same reason. The two checks are the
driver's `check_single_live()` and `check-unattended.sh`'s check 7, and both carry one stated
justification: that otherwise "the run" is not well-defined for anything keyed on it.

**Measured before this folder was written: nothing is keyed on it.** The driver's verb population is
seventeen — `VERBS_SLUG` holds fourteen and `VERBS_INLINE` three more — and sixteen of them take a
`<slug>`; the seventeenth is `--version`, which resolves nothing. All three of the leg's tree-wide
loops over `builds/*/RUN*.md` grade each file independently. No code path in this repository resolves "the run" without being told which build, so
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
- **UNBLOCKING A START IS NOT UNBLOCKING A RUN, and the spec audit is what established that.** Round
  1 confirmed a second serialization the two run-state checks were hiding: `run-gates.sh` holds a
  repo-wide turnstile, and its queue wait is charged against the unattended run's own `GATE_BOUND`,
  so two concurrent CLOSES in one clone can make the second fail `gates-green` for pure contention.
  `TOOL-aUnblockedFleet-6` was added by `--rescope` to fix it — and round 2 refuted all three of its
  mechanisms, so it is RETIRED and the problem is PARKED for the owner with both rounds' evidence.
- **WHAT THAT MEANS FOR WHAT SHIPS, stated plainly because it is the build's one honest limitation.**
  This build removes the START-time block, which is what the owner asked about and which is the whole
  duration of a run. It does NOT remove the close-time turnstile contention, which is a pre-existing
  property of `run-gates.sh` that these units make REACHABLE rather than create, and which is a
  moment rather than a duration. Strictly better than today, and not the whole problem — the residual
  is documented in the protocol, parked in `RUN.md`, and carries a backlog row.
- **The build-wide landing order lives in unit 1 §7 and is pointed at, never restated.** The
  `drift-audit records` ratchet sits at its ceiling with zero headroom, so a source header citing a
  unit id must land in the same commit range as that unit's status flip, and raising the pin is
  forbidden.
- **Spec-audit round 2 was ATTEMPTED and DIED before it reviewed anything**, 2026-08-31 ~05:20 FLEDT:
  all four finder lenses failed with `You've hit your session limit`, so the harness returned
  `lensesRun 0 / lensesDead 4` and the explicit note *nothing was reviewed*. **No review round was
  recorded for it**, because a round with no verdict is not a round and `--review` would have written
  a convergence datapoint that no lens produced. It was re-launched after the limit reset. This is
  recorded here rather than in the transcript because a dead review that looks like a skipped one is
  the `green-by-absence` class applied to the review loop itself.

## Parked decisions
*(none yet — this section is where a refused decision lands, with its question, the options seen,
and why the run refused it.)*

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aUnblockedFleet-1` | 2 | the driver: `check_single_live()` announces concurrent runs instead of refusing on them |
| 2 | `TOOL-aUnblockedFleet-2` | 2 | the leg: check 7 reports concurrent runs instead of failing on them |
| 3 | `TOOL-aUnblockedFleet-3` | 1 | the carriers: the protocol, the Skill, and every one of the kit-version marker's carriers |
| 4 | `TOOL-aUnblockedFleet-4` | 1 | the test arms for both halves, each with its failing case observed |
| 5 | `TOOL-aUnblockedFleet-5` | 1 | the records: two backlog rows closed, one narrowed, two filed, one decision row |
| 6 | `TOOL-aUnblockedFleet-6` | 2 | RETIRED (WONTDO) — the turnstile bound; all three mechanisms refuted by spec-audit round 2, and the loop was non-convergent so no corrected design could be reviewed |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** SPECCED · 6 unit(s) · node a · opened 2026-08-31 · streams tooling
ids TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5 TOOL-aUnblockedFleet-6 TOOL-aUnblockedFleet-7 TOOL-aUnblockedFleet-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aUnblockedFleet-1 — the driver stops refusing a run because another build is live](spec/2026-08-31-spec-TOOL-aUnblockedFleet-1.md) | 1 | 2 | SPECCED | rev-2 | 2026-08-31 |
| [TOOL-aUnblockedFleet-2 — the merge bar stops reddening because two builds are live](spec/2026-08-31-spec-TOOL-aUnblockedFleet-2.md) | 3 | 2 | SPECCED | rev-3 | 2026-08-31 |
| [TOOL-aUnblockedFleet-6 — the merge bar's turnstile stops eating the unattended close's deadline](spec/2026-08-31-spec-TOOL-aUnblockedFleet-6.md) | 3 | 2 | WONTDO | rev-2 | 2026-08-31 |
| [TOOL-aUnblockedFleet-3 — the protocol and the Skill state the rule the code now runs](spec/2026-08-31-spec-TOOL-aUnblockedFleet-3.md) | 4 | 1 | SPECCED | rev-3 | 2026-08-31 |
| [TOOL-aUnblockedFleet-4 — the arms, each with its failing case observed](spec/2026-08-31-spec-TOOL-aUnblockedFleet-4.md) | 5 | 1 | SPECCED | rev-2 | 2026-08-31 |
| [TOOL-aUnblockedFleet-5 — the records this build closes, narrows and files](spec/2026-08-31-spec-TOOL-aUnblockedFleet-5.md) | 6 | 1 | SPECCED | rev-2 | 2026-08-31 |
<!-- /gen:build-units -->

Records: 3 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aUnblockedFleet-1` | no |
| 3 | `TOOL-aUnblockedFleet-2`, `TOOL-aUnblockedFleet-6` | yes |
| 4 | `TOOL-aUnblockedFleet-3` | no |
| 5 | `TOOL-aUnblockedFleet-4` | no |
| 6 | `TOOL-aUnblockedFleet-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
