# Coordination, designed in — the flow's leases, mailbox and dependencies, and no build outside the chain counted on

**Serves:** research PLAY-dClosedLoop-1

The owner's directive after the flow-interactions round, the audit it called for, and the design it
moved into the chain. Architecture v2 carries the result under its dated `Revised:` line; this record
holds the reasoning and the instruments.

## [directive] The owner's words

> "Session context got compacted, reorient in this session if necessary. dLeasedFleet is out of scope
> for this build, no foreign build should be counted on - bring any necessary functionality into this
> plan+design."

It answered the closing note of the flow-interactions turn: cross-node coordination "now depends on a
mailbox the Concurrency build (`dLeasedFleet`) has to provide. Until it lands, builds on different
nodes fall back to waiting for landings."

Read as three rules:
1. dLeasedFleet leaves the chain.
2. The design counts on no build outside the chain: not a separate concurrency build, and not any
   live build's close or deliverable.
3. Whatever the flow needs from either is designed here and built by a chain build.

## [audit] What the design counted on outside the chain

The census (`foreign_census.py`, its source under the session log's instruments) lists every build
slug a design record names that is not a chain build, with the chain read from v2's chain table. It
judges nothing: whether a hit is counted on is decided by reading it, below, and a reliance worded
without a slug ("after the roles build closes") is invisible to it. Run over the six design records,
2026-10-14, before any change:

| Record | Foreign slugs, with the lines naming them |
|---|---|
| architecture v2 | aOrientedCast 369; dPolishedVitrine 381 |
| walkthrough | aDeployScout 542; aOrientedCast 98, 105, 124; dNarrowedAnchor 388; dScriptedRepeat 616 |
| flow | aFusedCharter 167; dHashedPrelude 167; dNarrowedAnchor 195; dSweptBranches 400 |
| flow interactions, foundations | none |
| architecture v1 | 24 slugs, every one in the live-build mapping (lines 149 to 178), which v2 adopts by reference |

Each reliance, read:

| Build | Where | What was counted on | Disposition |
|---|---|---|---|
| dLeasedFleet | v2's chain table; the flow interactions' settled owners; the parent edges of dRankedPlan and dScopedBuild | leases, the mailbox and dependency coordination | leaves the chain; designed in below as dDeclaredLoop's coordination feature |
| aOrientedCast | v2's dDeclaredLoop roster, roles "re-pointed after aOrientedCast closes"; walk S1b's trade-off | the stage table's move waited on its close | the wait is removed: dDeclaredLoop moves the table and re-points its seven readers itself, and a concurrent change to `tools/roles/` is reconciled in Test's prepared merge (FI-3) |
| aRoutedQuill, dPinnedHandoff, dPolishedVitrine | v1's mapping, adopted by v2: the absorbing chain build acts "after it closes" | each absorption waited on a live build's close | the active builds finish on their own track (R3.3), and no chain build waits for them or relies on what they deliver |
| dScriptedRepeat | walk section 8's seams: Maintain's recipe rode recipe mode, whose build is SPECCED and dormant | Maintain's run | Maintain's run is its step checklist on the flow's executor; recipe mode is not a seam, and the mapping still re-homes the dormant build's asks to dTendedCadence |

The other hits are evidence, cited for a measurement, and stay: aDeployScout, aFusedCharter,
dHashedPrelude, dNarrowedAnchor, dSweptBranches. dPolishedVitrine in v2 is an action the Plan build
takes on it (confirming its track), not a reliance.

## [design] The coordination feature, built by dDeclaredLoop

**Why the flow's build.** The owner set the flow as the layer that governs what builds do and how the
steps interact (the flow record's `[layering]`); leases and messages are how builds interact, so they
are the flow's own mechanics, and dDeclaredLoop is the build that implements the flow. Its primitives
land before the step builds that call them (`[consistency]`), and as a feature of their own (P17) they
build beside the policy and transition features rather than after them.

**Seams it extends, verified 2026-10-14.**
- The run claim (`tools/unattended/unattended.sh:2070-2186`): `refs/gov/runs/<slug>`, a parentless
  commit over the empty tree carrying eight `key: value` lines (slug, node, host, session, keepalive,
  status, lease-utc, beat-utc), written by compare-and-swap, dark unless `RUN_CLAIMS=on`; 17 on the
  remote. Its node is the user name (`:2410`).
- The overlap probe `check_cross_run_overlap` (`unattended.sh:3409`), which always returns 0.
- `check_slug_claimed` (`tools/memory-tree/gen_build_index.py:3478`), reading local history only.
- The node registry `tools/playbook/fleet.toml`, four nodes, and its `--claim-node` verb.
- The `gov-session` role, which hands work to another session as a prompt file in the build's
  `prompts/`.
- The harness's own session messaging, where one exists: Claude Code reaches other sessions on one
  machine, and Remote Control sessions on other machines.

**Planned units.**
1. **The lease.** One ref grammar on the shared remote for every holder:
   `refs/gov/leases/<slug>/build`, `refs/gov/leases/<slug>/unit/<id>`, and
   `refs/gov/leases/run/<maintain|review>/<period>` for the cadence runs. The record extends the run
   claim's: holder kind, fleet tag, host, session, harness, branch, the write set at
   `leases.overlap`'s granularity, the build's step (derived from its transition record), its
   verified tree once Test exits, status, lease and beat times. Written by compare-and-swap; its
   history is the witness (P2). Run claims migrate onto build leases, so one mechanism remains.
2. **Acquire, renew, release, take over**, as CLI verbs the step checklists call: the build lease at
   Plan's exit and in a patch build's light five; unit leases at Build's start; a period lease at the
   start of a Maintain run and of a Loop Review; release at Deploy's item 9 and at any terminal
   status. Renewed at transitions and pass commits, never per tool call; expired after
   `leases.expiry-hours` unrenewed (`leases.renewal`); an expired lease may be taken over, the
   takeover recorded in its history and posted to the previous holder's mailbox.
3. **Overlap**, evaluated at acquisition and whenever a write set grows, against every live lease at
   `leases.overlap`'s granularity: under `warn` it is shown on the card, in the transition record and
   in the other holder's mailbox; under `refuse` the acquisition or the write is blocked. It replaces
   the probe that always returns 0.
4. **Fleet identity and uniqueness.** Leases and messages name the fleet tag, never a user name, and
   a node with no claimed tag cannot acquire. A new slug or id is checked against the remote's lease
   refs and unmerged branches, not local history.
5. **Offline**, as `leases.offline` says (warn by default): an acquisition made offline is recorded
   locally and pushed by compare-and-swap on reconnection; if another holder won meanwhile, the
   offline one yields, and the conflict is recorded and posted.
6. **The mailbox.** One ref per sender per build on the shared remote,
   `refs/gov/mail/<slug>/<fleet tag>` (revised 2026-10-19, the night pass two, point 3, pending NT-16: one
   ref per build took 4.5 times the ideal attempts at eight writers): an append-only
   chain of commits, one per message, appended by compare-and-swap. A message carries its id, its
   sender (fleet tag, session, build), its recipient (a build, or one of its units), its kind, its
   references (unit ids, interface names, SHAs), a body, and the id it answers. Its kind comes from a
   closed set the loop definition declares and the loop's schema checks on every write, so a new kind
   is a change to the loop kit, never an adopter's extension: `confirm-request`, `confirmed`,
   `changed` (additive or breaking), `overlap`, `takeover`, `landed`, `question`, `answer`, `ack`. Revised 2026-10-19 (the night pass two, point 4): the closed
   set is one list, declared once in the loop definition, the nine above with `intake` (flow-roles FR-8)
   and `withdrawn` and `superseded` (flow-steps `life.notify`). Completed work and decisions are not
   messages: `next` derives done-ness from witnesses, a decision is its register's entry, and a problem
   is the problem register's, keyed by its subject.
   Every transition reads the build's mailbox and is refused while a message addressed to the build
   is neither answered nor acknowledged, the reply being the witness; the card shows unread messages,
   and `next` lists them as next actions. Each transition writes the messages it disposed, with their
   replies, into the build's transition log, so every message is kept in the build's folder;
   Maintain prunes a closed build's mailbox ref once its folder holds every message.
7. **Live delivery.** Where the harness can message another session, the sender writes the mailbox
   first, then delivers live, citing the message id; any other harness, and the owner by hand, use
   the same CLI verbs on the mailbox. `deps.messaging` picks the channels. Revised 2026-10-19 (the night
   pass two, point 3, pending NT-17): the live message carries only the message's ref and id, never a
   fact, so a lost ring costs only latency. A session is also shown unread ids at every tool call, read
   from the node's local copy of the mail refs, which a detached fetch keeps fresh, because the read
   points, not the transport, set how late news arrives.
8. **Dependency coordination.** A build depends on its `parents:`. A parent is reachable while its
   build lease is live. At Design's exit a build posts each frozen feature's declared interfaces to
   every dependent's mailbox as `confirmed`; a dependent's unit that consumes an interface enters
   Build once that message, or the parent session's answer to its `confirm-request`, confirms it
   (`deps.early-build`). A later breaking change posts `changed`, which fires the dependent's
   interface-change re-entry for its consuming units; the landing posts `landed`. A dependent whose
   parent is unreachable enters Build for its consuming units only after the parent lands
   (`deps.coordination`).

**Callers, wired by their step's build.** Each lease call is an item of a step checklist, so the
build that owns the step wires it: Plan's build lease (dRankedPlan); Build's unit leases and write
sets (dScopedBuild); Deploy's release, and the landing order read from the leases' verified trees
(dShippedRelease); Maintain's period lease (dTendedCadence); the Loop Review's (dCalibratedLens). The
cross-build re-entry is dIndexedDesign's `design.reentry`, triggered by a `changed` message.

**Policies.** No new key. `leases`, `leases.granularity`, `leases.renewal`, `leases.expiry-hours`,
`leases.overlap` and `leases.offline` (R2.2, walk C1 to C4), and `deps.coordination`,
`deps.early-build` and `deps.messaging` (FI-2, FI-5, FI-6) cover every behaviour above; the
mechanisms that read settled answers are listed under `[interpretations]` for confirmation.

**Gaps owned.** gap-conc-01, gap-conc-02, gap-flow-06, moved from dLeasedFleet.

**Risks.**
- Every lease and mailbox write is a network round trip, so they ride transitions and passes only.
- A lease is state the holder's own session writes, so its witness is the remote ref's history,
  never the holder's word.
- The feature sits in the chain's second build, so the step builds' lease calls wait for it. Until
  it lands, the chain's own builds run under today's governance (run claims, the overlap probe, the
  owner): the product as it stands, not a foreign build.

## [chain] What changes in the chain

- dLeasedFleet's row leaves; the chain has ten builds.
- dDeclaredLoop gains the coordination feature and gap-conc-01, gap-conc-02 and gap-flow-06; its
  roles move no longer waits for a live build's close.
- dRankedPlan's parents become dDeclaredLoop alone. dScopedBuild's become dIndexedDesign and
  dWitnessedBar; dDeclaredLoop stays its ancestor through both.
- dTendedCadence's first unit is the Maintain step's checklist on the flow's executor, not a playbook
  in recipe mode.
- The live-build mapping keeps its rows without "after it closes": no chain build waits for a live
  build or relies on what it delivers.
- P5 is restated: leases and the mailbox are the flow's own mechanics.

## [owed] What the re-cut still owes inside the chain

- The flow's executor and checklist engine (P20: the unattended kit executing each stage's
  checklist) has no owning chain build yet. The re-cut assigns it to one, so no live build working on
  the unattended kit is counted on either.

Revised: 2026-10-16, the stale sweep: RT-3 gave the executor and its checklist engine to dWellOiledMachine, a chain
build (v2 `[owed]`; `build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`), so no live build is
counted on for it.

## [interpretations] For the owner to confirm at chain approval

Each reads a settled answer into a mechanism; v2's `[open]` lists them too.

1. **Reachability.** The bound FI-6's settlement names is the parent's build lease: live means
   reachable, absent or expired means not; there is no separate timeout.
2. **Confirmation without the parent's session.** Design's exit posts each frozen feature's declared
   interfaces to the dependents' mailboxes, which is how a frozen feature design confirms an
   interface (FI-5).
3. **Disposal.** A transition is refused while a message addressed to the build is neither answered
   nor acknowledged: the reading FI-6 settled at each transition.
4. **Landing order's input.** The lease carries the build's verified tree, and the lander orders the
   builds whose leases hold a current verdict (FI-7).
5. **Kept and pruned.** Each transition writes the messages it disposed into the build's transition
   log, the owner's rule that everything is kept in the build's folder; Maintain prunes a closed
   build's mailbox ref, with the landed branches, once the folder holds every message.
