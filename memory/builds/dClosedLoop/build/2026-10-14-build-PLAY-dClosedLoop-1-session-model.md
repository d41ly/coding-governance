# A session modelled: one build through every step of the flow, as designed, and the holes the model found

**Serves:** research PLAY-dClosedLoop-1

The owner asked: "now model an agent session running a build through all the steps for me - what
happens?" This record walks one realistic build from the owner's first message to Maintain and the
Loop Review, applying only what the design has settled (architecture v2, the flow, the flow
interactions, the coordination and orientation records) under the `standard` preset. Where the design
is silent or contradicts itself, the trace says so in place and collects it under `[holes]`. Agent
roles per item are not yet designed, so the actors named are today's roles, marked as placeholders.

## [setup] The example

- **The repository**: gov itself. Two nodes are live: `d`, the owner's machine, and `a`.
- **The request**, typed by the owner on node `d`: "Make the drift audit fleet-aware: every node
  publishes its readings, and the card shows the fleet's worst drift."
- **Other live work**: `xCardPolish` (node `d`, higher plan priority) holds a lease on
  `skills/session-kickoff/`; `xMaintainProbe` (node `a`) is planned with `parents: xFleetDrift`,
  because it will consume the readings. All slugs and unit names here are illustrative.
- **The preset**: `standard`, no overrides: autonomy `plan-only`, so the owner's ratification is the
  mandate and everything after Plan runs unattended.

At a glance:

| Step | Who acts | The owner's part | What it leaves behind |
|---|---|---|---|
| Entry | the attended session | types the request | an intake record, the build's card |
| Plan | the session, with the owner | answers scope questions; runs one ratify command | the plan record, the build lease, the ratification |
| Design | the executor and role agents | nothing | features, specs, interfaces confirmed to a dependent |
| Build | the executor and builders | optionally asks for an amendment | commits per unit, the closing review, new units from its findings |
| Test | the executor and the bar | nothing | a verdict for the prepared merge, after one fix pass and one re-verify |
| Deploy | the executor and the lander | nothing | the landing, kit versions, released leases, the closed build |
| Maintain | the next day's cadence run | opens a session | pruned branches, an ask, gov's tagged release |
| Review | at every transition; weekly | reads the proposals | recommendations, one closing review, Loop Review proposals |

## [entry] The session opens

1. **The harness loads the instructions** in rank order: its own system prompt (rank 0), then the
   charter's entry file, which imports the charter and the per-worktree card file (rank 1). No build is
   bound yet, so the card holds only the repository and session cells:

   ```text
   [CARD · Priority 1 · session 7c41… · node d · keyed HEAD 4c1e9a2 · remote 77d0e1f]
   tree — C:/projects/coding-governance · primary · main · base 4c1e9a2 · clean
   preset — standard · overrides none
   plan — 9 placed builds; top three: xCardPolish (P1) …
   leases — 6 held on the remote · on your node: xCardPolish (skills/session-kickoff/)
   mailbox — no build bound
   next — place the request: gov next --place "<request>"
   ```

2. **The session-start hook re-renders that file in the session's own tree** and prints one key line;
   nothing is re-derived by the agent, because every cell carries its key.
3. **The owner types the request.** *Hole: nothing writes the owner's words verbatim except the agent
   itself (H2).*
4. **Placement**, one call: `gov next --place` lists candidates: no live build's goal or design index
   covers fleet drift, and one open ask (per-node drift only) matches. The agent places it alone
   (`placement: agent-places`): disposition `new`, absorbing the ask, reason recorded. The check
   (`placement.check: refuse`) passes: a `new` needs a Plan intake record with the owner's words, and
   it writes one now.
5. **No READY card exists for this build, so the full kickoff runs** (`kickoff.runs: no-ready-card`):
   the manifest ratchet, the slug minted and checked against the remote's leases and branches
   (`xFleetDrift`), the build's branch and worktree opened, and the card gains its build slice at
   Plan, item 1. The card is saved: the remote ref (the truth), the clone's cache, the imported file.
   *Hole: the session was launched in the primary tree, so the card it imported at launch is that
   tree's, unbound, until the worktree's file is read (H14).*
6. **Orientation cost, recorded** (`orient.budget: record-only`): three calls before the first item
   action, against today's median of 35.

## [plan] Plan: attended, about forty minutes

The session works the Plan checklist; `next` names each item, and reads and probes are free inside it
(`actions.free: read-only-probes`).

| # | Item | Actor | What happens | Witness |
|---|---|---|---|---|
| 1 | intake recorded verbatim | the session | done at placement | the intake record |
| 2 | duplicates and overlaps | a command | none duplicate; `xCardPolish`'s live spec touches the card file, noted | the dupes record, its index key |
| 3 | triage by rules | a command | severity MED, acceptance drafted, the rule named | the triage record |
| 4 | disposition | the session | `new`, from placement | the intake record |
| 5 | the plan record | the planner (placeholder: the main loop) | problem, goal, cut-line (no new drift signals), three acceptance observations, priority P3; the owner answers two scope questions | the plan record's fields check |
| 6 | each practice's Plan reach | the planner | `[yagni]`: the need is measured today (the card's drift cell reads other shas) | the reach fields |
| 7 | the plan view | a command | regenerated; `xMaintainProbe` now shows this build as its parent | the placement predicate |
| 8 | the build lease | a command | `refs/gov/leases/xFleetDrift/build` taken by compare-and-swap; the write set `tools/drift-audit/`, `skills/session-kickoff/` overlaps `xCardPolish`'s lease, so it warns on the card, in the transition record and in `xCardPolish`'s mailbox | the lease ref |
| 9 | the review recommendation | a command, then the session | score low (small, one plan); advice: no Plan review | the recommendation line |
| 10 | ratification | the owner | the owner runs `gov plan ratify xFleetDrift` in a terminal, which stamps the ratification; the chat's "go" alone cannot witness it (H1) | the ratification trailer |
| 11 | Plan to Design | a command | every witness checked; the transition committed three ways; the card re-rendered and saved; the mailbox read: empty | the transition trailer |

**The hand-off to unattended work.** The mandate is active, so the build no longer needs this
session. *Hole: nothing yet says who starts the executor, on which node, under which host, or how its
liveness is seen (H3).* The model assumes the session launches it on node `d` and ends; if the owner
returns to this idle session later, `next` recommends a fresh one (`resume.context: fresh-when-idle`).

## [design] Design: unattended, about an hour

The executor is code: it calls `next --json`, runs the item's actor, resolves the witness, and repeats.
Every role item runs in a fresh agent whose brief is rendered from the item: the facts it needs at
their source SHAs, its write set, its tools and its return schema. No agent orients itself.

1. **The input**: the ratified plan record, pinned by its SHA.
2. **Reuse and precedent probes**: a reuse scout returns two seams, the drift report's signal table
   and the run-claim ref writer, with each probe's output digest, which the executor re-derives.
3. **Decomposition** (placeholder actor: the designer role does not exist yet, H4):
   - Feature F1, publish: U1 the reading schema and local writer; U2 the remote publisher.
   - Feature F2, show: U3 a gate leg over the schema; U4 the card's fleet cell; U5 the help page.
   - F1's feature design declares the interface `drift-reading v1`, produced by U2 and consumed by U4
     and by `xMaintainProbe`.
   - Order: U1, U2, then U3 and U4 in parallel (disjoint write sets), then U5.
4. **Specs**: one spec writer per unit, in parallel up to the fan-out bound, each returning
   `authored` with the spec's path and SHA; the executor checks the file and its format.
5. **Each practice's Design reach**, per unit, inside the spec's fields.
6. **A fork**: publish readings as a ref per node, or as a committed file? A preference, not a fact,
   so `design.forks` resolves it: the ref, the more expandable option, fully recorded.
7. **Overlaps**: the design index shows `xCardPolish`'s spec on the card's renderer; U4's boundaries
   acknowledge it (`design.overlap: warn`).
   - **An interrupt arrives**: `xMaintainProbe`, on node `a`, posts a `confirm-request` for
     `drift-reading v1`. Disposal is owed before the next transition; the executor acknowledges it,
     since the frozen feature design will confirm it at Design's exit.
8. **The review recommendation**: the score is high (a new remote write path, two kits, an interface),
   so the line recommends the spec audit. Under `standard` the recommendation is advice and
   `review.design` is opt-in, so no audit runs; `strict` or `guarded` would run it.
9. **Every unit derived READY**: specs committed, no open fork, none thin.
10. **Design to Build**: transition recorded, card saved, and the mailbox disposed: `confirmed` for
    `drift-reading v1` at the frozen revision goes to `xMaintainProbe`'s mailbox (node `a`, so mailbox
    only). `xMaintainProbe` may now build the units that consume it (`deps.early-build`).

## [build] Build: unattended, about three hours

1. **The base** is pinned from history, and the mandate recorded.
2. **Unit leases** for U1 to U5 with their write sets; U4's warns against `xCardPolish` again.
3. **Passes**: one fresh builder per unit, briefed with its spec at its SHA. It runs no gate legs, and
   returns a structured result whose commit the executor resolves before the next item.
   - **U1** is built in one pass, with its acceptance observations (item 4) and bug-class trailer
     (item 5).
   - **U2 diverges**: its builder finds the ref name collides with the lease namespace, and returns
     `diverged: spec-wrong` as an enum, not free text. U2 is unbuilt, so its spec may still change: a
     unit-level re-entry to Design (the clash is internal, not the declared interface), a revised spec,
     READY again, then built (item 6).
   - **U3 and U4 run in parallel.** *Hole: under `build.worktree: shared`, two builders commit in one
     worktree and contend for git's index lock (H6).*
   - **U5**, the help page, closes the roster.
4. **The owner checks in.** A new session on node `d` opens with no binding. The owner asks "how far is
   the fleet-drift build?", placed `none` (read-only). `next --build xFleetDrift` answers in one call:
   Build, U3 and U4 in progress, U2 re-designed once.
5. **The owner asks for more**: "also show each reading's age". The agent places it `amend
   xFleetDrift`, in the goal. The placement check refuses this session, though: the executor's session
   holds the build's lease. *Hole: an amendment from a session without the lease must reach the holder
   through the mailbox, which has no `intake` message kind, and the executor reads its mailbox only at
   transitions, hours apart (H5, H9).* The model posts it to the build's mailbox anyway.
   - At the next item boundary the executor disposes it: U4 is already built, so its spec is frozen.
     The age becomes a new unit, U6, designed at unit level and built.
6. **The scope check** (item 7): U4's builder also touched a file in `tools/drift-audit/`, outside its
   write set. `build.scope: warn-and-ask` warns, and files an ask for the owner.
7. **The closing review** (item 8, owed once per build): diff reviewers by lens, a skeptic on every
   finding, then the synthesizer's report under the build's `reviews/`.
   - One HIGH finding: U2's publisher does not handle an unreachable remote.
   - Two MED findings.
   - `review.findings: blocker-high-own` makes the HIGH its own unit, U7, and batches the MEDs into U8.
   - U2's spec stays frozen; U7 and U8 walk Design at unit level and are built. *Hole: whether the
     closing review runs again over U6 to U8 is undefined (H8).*
8. **No core red** from the build's own commits (item 9). *Hole: which checks witness this, when units
   run no gates and the bar belongs to Test, is undefined (H11).*
9. **Build to Test**: transition recorded; the mailbox holds `xCardPolish`'s acknowledgment of the
   overlap notice.

## [test] Test: unattended, about an hour

1. **The tree**: the prepared merge of the build onto main's tip, in Test's own worktree: tree T1.
2. **Selection**: the legs the build's paths claim (drift-audit, session-kickoff, run-gates) and the
   declared levels (unit, integration).
3. **The bar** on the local hook writes a verdict for T1. It is red:
   - The drift-audit leg fails; attribution says OWN: U1's writer drops an optional field the spec
     requires.
   - The code misses the spec, so `verdict.red-route` sends a fix pass of U1 back to Build, leaving
     U1's spec untouched. The build's step is Build again, its least-advanced unit's; it returns to Test.
4. **The second run** is green. A held leg is skipped on demand, and recorded. One leg passes only on
   retry, so a flake is recorded (`verdict.flakes: quarantine` once past the threshold).
5. **Seen red**: U3 added a gate leg, and its acceptance included the planted failure, so the
   seen-red record exists.
6. **The review recommendation**: advice; the gate review is opt-in and does not run.
7. **The tip moves**: `xCardPolish` lands first, under plan priority (`landing.order`), so T1's
   verdict is stale (an interrupt). Test re-verifies on the new tip as tree T2; the bar reuses every
   leg whose declared reads did not move. Green.
8. **Test to Deploy**: transition recorded.

## [deploy] Deploy: unattended, about fifteen minutes

1. **The verdict is current**: T2 is still main's tip plus the build.
2. **The authority** is the plan's mandate: the ratification trailer.
3. **The lander**: a `--no-ff` merge and a push, reusing Test's verdict for the same tree. *Hole: the
   lander needs the node's primary tree, which every landing on that node shares, and nothing
   serializes it (H7).*
4. **The landing record**: the SHA, the build, its eight units, the verdict.
5. **Kit versions** minted, with release notes, for drift-audit and session-kickoff. Gov's tagged
   release waits for Maintain's weekly cadence.
6. **The review recommendation**: advice; no landing review.
7. **Leases released**: the build's and the units'; `xCardPolish`'s overlap clears.
8. **Deploy to Maintain**: the build closes at landing (`build.closes: at-landing`).
   - The card's terminal snapshot is committed to the build's folder (`card.snapshot: terminal-only`).
   - `landed` goes to `xMaintainProbe`'s mailbox. *Hole: nothing yet stops a dependent landing before
     its parent; the prepared merge would red, but no rule says so (H13).*
9. **The owner's part**: none. *Hole: nothing tells the owner a run landed, or parked, until a session
   opens (H12).*

## [maintain] Maintain: the next morning

1. **The owner opens a session on node `d`.** Maintenance is due (`maintain.host: session-start`,
   `daily`), and this node takes the period's lease (`refs/gov/leases/run/maintain/<date>`); another
   node holding it would skip.
2. **Detectors run**, the new fleet readings among them: node `a`'s readings are three days old, a
   breach, filed as an ask for its owning stage (`maintain.on-breach: file-ask`).
3. **Safe fixes that change no tracked content**: stale processes reaped; the build's landed branch
   and worktree pruned; its mailbox ref pruned, its folder holding every message.
4. **A tracked fix**: a stale generated index becomes a patch build at Design, ratified automatically
   (`patch.ratify: auto`).
5. **The release**: Monday is the weekly cadence, so gov's tagged release is cut with notes carrying
   both kits' new versions.
6. **Adopter currency** probed; the maintenance record written; the period lease released.

## [review] Review: at every transition, and weekly

- Every transition carried a scored recommendation; the one review that ran, the closing review, blocked
  Build's exit until its findings were disposed (`review.blocks: every-review`).
- **A class on its second occurrence becomes a gate**: had the closing review's HIGH (an unhandled
  remote failure) already been a bug class, it would earn a gate now (`review.left-shift`).
- **The weekly Loop Review** reads the transitions, never typed numbers:
  - Plan took 40 minutes, attended.
  - Design 1 h, Build 3 h with one divergence and one amendment, Test 1 h with one fix pass and one
    stale re-verify, Deploy 15 minutes.
  - Review yield: three findings, two units. Plus one scope warning, one flake, and the orientation
    cost per stage.
  - Its proposal, for example "write sets at feature level, since U4 strayed into its sibling kit",
    is filed into Plan.

## [owner] What the owner did

They typed one request, answered two scope questions, ran one ratify command, asked one progress
question, asked for one amendment, and opened a session the next morning. Everything else ran
unattended under the plan's mandate.

## [holes] What the model exposed

Each is a place where the settled design is silent or does not hold together. None is decided here.

| # | Hole | Where it bit | Proposed resolution |
|---|---|---|---|
| H1 | **Ratification's witness.** The owner's "go" in chat reaches the records only through the agent, which is actor-typed state; the floor forbids a witness that reads it. | Plan item 10 | Ratification uses the policy guard's proof, an interactive-terminal command stamping a trailer (`policy.proof`) |
| H2 | **Verbatim intake.** The owner's words reach the intake record only through the agent. | Entry, Plan item 1 | A prompt-submit hook writes each prompt verbatim to a session intake log, which the record cites |
| H3 | **The executor's launch, host and liveness.** Nothing says who starts the run after ratification, on which node and host, or how its liveness shows. | Plan to Design | A `run.host` policy mirroring `maintain.host`; the run's liveness is its build lease's beat; the executor's home is the re-cut's |
| H4 | **Actors per item.** Decomposition, the plan draft and triage have no role; today's roles were used as placeholders. | Plan item 5, Design item 3 | The next layer: an actor table per step's checklist |
| H5 | **An amendment from a session without the lease.** The placement check refuses it, and the mailbox has no kind to carry it. | Build, step 5 | Add an `intake` message kind; the holder disposes it like any intake |
| H6 | **Parallel units in one worktree.** Disjoint units still contend for git's index lock under `build.worktree: shared`. | Build, U3 and U4 | The executor serialises commits, or parallel units default to their own worktrees (`parallel-only`) |
| H7 | **The node's primary tree at landing.** Every landing on a node needs it, and `landing.order` orders builds without serialising the tree. | Deploy item 3 | A node-local landing lease beside the build lease |
| H8 | **Review of units born from the closing review.** Whether the closing review runs again over U6 to U8 is undefined. | Build item 8 | A follow-up round over the new units' range, owed while it still finds, as today's practice does |
| H9 | **When the mailbox is read.** Read only at transitions, a mid-step message waits hours. | Build, step 5 | The executor reads the mailbox at every item boundary, one ref fetch each |
| H10 | **Backward transitions.** Test to Build and Build to Design happen (a fix pass, a divergence), but the transition record is written only forward. | Test step 3 | Transitions record both directions; only Plan is never re-entered |
| H11 | **Build's core check.** Item 9 needs a check, but units run no gates and the bar is Test's. | Build item 9 | The executor runs the core checks, cheap and leg-free, at the transition |
| H12 | **Telling the owner.** A landing, a park or a refusal reaches the owner only when they next open a session. | Deploy, unattended | A notification policy, for example on park and on land |
| H13 | **A dependent's landing.** A dependent could reach Deploy before its parent lands; only a red prepared merge would stop it. | Deploy step 8 | A dependency edge gates the dependent's Deploy until the parent has landed |
| H14 | **A session that moves into its build's worktree.** The card imported at launch is the launch tree's; the worktree's own card file is not loaded until a re-read, which is the fixture the adopted preservation design still owes. | Entry, step 5 | Until the fixture passes, `next` recommends a fresh session launched in the build's worktree, whose import is that worktree's card |
