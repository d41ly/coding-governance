# TOOL-cBriefedPilot-21 — the parallelism mechanism hunt, and what would settle it

**Status:** CLOSED · rev-2 · 2026-08-16 · node c · Tier-2 · base 37c05e1b · streams tooling · ratified 2026-08-15

## 1. Goal

Establish by measurement whether ANY route dispatches a build pass concurrently without voiding the
eleven directives this build installs. The answer decides unit 15's shape. This unit builds no
mechanism and edits no rule; it produces a recording, and "no route survives" is a legitimate result
it ships as a finding rather than an excuse.

## 2. Scope (IN)

- **S1** — a route inventory of six named candidates, R1 to R6, each with the claim it rests on and
  the source that states the claim.
- **S2** — one TEST per route, written before it is run, naming the command or the file whose
  contents decide it. A route is not tested by reasoning about it.
- **S3** — a four-part evidence standard, E1 to E4, that a route must satisfy WHOLE to be marked
  surviving. A route meeting three of four is recorded as failing, with the one it missed named.
- **S4** — one recording under this build's own `build` folder, named with the tail
  `-build-cBriefedPilot-2-parallelism-routes.md` and dated by hygiene check 5's grammar on the day it
  is written. It carries per-route OBSERVATIONS — what was run, what came back — not conclusions.
- **S5** — a verdict line in a fixed spelling, `parallelism route: <R-id>` or `parallelism route:
  none`, so unit 15 reads a token rather than interpreting prose.
- **S6** — the research pass writes that one file and nothing else, which is the disjointness
  property the build README claims for this unit.

## 3. Non-goals (OUT)

- **Building the mechanism.** A surviving route is a finding, not a harness. If one survives and is
  worth wiring, that is a follow-up build with its own spec, not a widening of this one.
- **Editing M6 or M10.** Units 15 and 16 own the method's text. This unit hands them an input.
- **Any row in `memory/DECISIONS.md` or `memory/backlog/TOOL.md`.** Unit 20 derives both from this
  recording. Writing either here would cost S6's property, since both are named verbatim in M6's
  condition (3) and both are written by units sequenced after this one.
- **Re-opening the ≤5 verify-agent cap or the concurrency ceiling.** `memory/guides/REVIEW-PROTOCOL.md`
  owns those numbers and this unit measures against them, never at them.
- **A gate over the finding.** Nothing here becomes a leg. The recording is read by unit 15 and by a
  human; a gate that graded a research verdict would be grading an opinion.

## 4. Design

### Inventory

| # | Route | The claim it rests on |
|---|---|---|
| R1 | direct `Agent` spawn from the main loop | the spawn is hooked and the subagent carries the project instruction file, but the budget is keyed per prompt |
| R2 | a `Workflow` sidechain | `memory/guides/REVIEW-PROTOCOL.md` states a sidechain inherits no hooks and no `CLAUDE.md` |
| R3 | a headless child process started from a backgrounded shell | a fresh process RE-ESTABLISHES the layer instead of inheriting it |
| R4 | the keepalive tick as a budget-resetting turn | the budget key includes a prompt id, so a new turn mints a new key |
| R5 | one git worktree per concurrent pass | M6 requires a commit per pass, and two passes in one checkout share one index |
| R6 | no route — sequence and park | M6's existing fallback already covers it |

R5 is not an agent-dispatch route. It is the checkout shape any of R1 to R4 would need, and it is
listed because a route that dispatches two passes into one working tree fails E4 whatever else it
does.

### The evidence standard

A route SURVIVES only when all four hold, each answered by an observation:

- **E1 — the layer reaches the pass.** The agent performing the pass has the eleven directives and
  the run's recorded waivers, by inheritance or by priming. Answered by asking the dispatched agent
  to report a string it could only have if the layer reached it.
- **E2 — the budget resets, or is not spent.** The dispatch does not consume an allowance that cannot
  be replenished inside a run with no further owner turn.
- **E3 — M6's three conditions can still be met for the pair**, condition (3) included. The run-state
  file is named verbatim there, so a route whose passes each move the phase fails on its own terms.
- **E4 — each pass can commit at its own end**, per M6, without the two commits racing one index.

### Per-route test

- **R1.** The budget is a directory, so read it. `tools/hooks/agent-cap.js` claims a numbered slot with
  `O_EXCL` at `<git-common-dir>/agent-cap/<session_id>__<prompt_id>/slot-N`, `MAX_VERIFIERS = 5`,
  verified at that file. List the directory before and after a spawn; the count decides E2 with no
  inference. E1 is already indicated: a subagent of this session received the project instruction
  file's contents.
- **R2.** Three observations, because the protocol's one sentence conflates three different hook
  events: does the dispatched agent carry the project instruction file; does a `SubagentStart` hook
  fire for it; does a `PreToolUse` hook deny a deliberately banned call the agent makes from inside
  the sidechain. **The blanket claim needs re-measuring before it is relied on again.** Observed while
  this spec was written: an agent dispatched by a workflow orchestration script carried the project
  instruction file's contents AND a `SubagentStart` hook's added context. That does not refute the
  `PreToolUse` half, which is the half `REVIEW-PROTOCOL.md`'s enforcement section actually depends on,
  and it is one observation on one host — which is exactly why it is a test to run rather than a fact
  to cite.
- **R3.** Is the CLI on PATH in the run's environment; does a child process read `AGENTS.md` on its
  own; does the child key a separate budget. Then the three hazards: the child is a second session
  with its own keepalive store that no other session can reap, `tools/unattended/check-unattended.sh`
  refuses a second live run, and the cost is paid per child.
- **R4.** The cheapest test in the set and it decides R1's bound. Note the newest
  `<session>__<prompt>` directory name under the budget root, wait one keepalive interval — the
  project declares every ten minutes in `.unattended.conf` — spawn one agent, and see whether a NEW
  directory appeared.
- **R5.** Whether `.githooks/pre-commit`'s branch guard admits a commit from a secondary worktree, and
  whether two worktrees on one branch can both hold the run-state file without breaking condition (3).
  A two-worktree dry run committing two disjoint files and merging is what settles it.
- **R6.** No test. It is the result of the other five failing, and it is reported as a result.

### What a null result ships

`parallelism route: none` is a complete answer to this unit. It is what unit 15 reads, and unit 15's
branch B is written for it. The recording then also names, per route, the ONE thing that would have to
change for that route to survive — which is the difference between a finding and a shrug.

### Files touched (estimate)

One new recording under `memory/builds/cBriefedPilot/build`. No source file, no conf, no gate.

### Alternatives rejected

- **Folding the hunt into unit 15.** Rejected by the owner on 2026-08-14 (P2): an inversion that
  ships with an excusing clause and no mechanism is a rule nothing can follow. Separating them also
  buys the one unit in this build whose write set lets it run beside the 1 to 14 chain.
- **Deciding R2 from the protocol's sentence alone.** That sentence is the whole basis of P2's "both
  known routes are bad", and the observation above already qualifies it. A design decision resting on
  an unmeasured claim is the class this repo keeps catching.

## 5. Production-readiness checklist

- security — a test that dispatches a child process runs with the operator's own credentials; R3's
  test is read-only and starts no run.
- perf / scale — R1 and R4 cost one spawn each; R3 costs one child process.
- a11y · i18n — N/A, no user surface.
- error / empty / loading states — a test that cannot be run is recorded as NOT RUN with the reason,
  never as a negative result. The two are different findings and the recording keeps them apart.
- observability — the recording IS the observability; there is nothing else to watch.
- risks — the measurements are one host, one CLI version, and none of them is gated, so a route that
  works today can stop working silently. Stated in the recording rather than implied away.
- testing + left-shift gates — none. This unit adds no leg, so the four-gates-at-once hazard that
  applies to units 12 to 14 does not apply here.
- migration / rollback — nothing to migrate; deleting the recording rolls it back.
- user docs — N/A until a route survives and something is built on it.

## 6. Acceptance criteria

- **AC1** — When the recording lands, `bash tools/memory-tree/check-memory-hygiene.sh` is green,
  including check 5's filename grammar and check 15's dead-path pin, which is 0 with no slack.
- **AC2** — Every one of R1 to R6 carries an observation naming the command run or the file read, or
  the explicit NOT RUN disposition with its reason.
- **AC3** — The recording's last line is `parallelism route: <R-id>` or `parallelism route: none`, and
  nothing else matches that prefix, so unit 15 reads one token.
- **AC4** — R4's result is reported as the budget directory listing before and after the interval,
  not as a claim about how the budget behaves.
- **AC5** — No route is marked surviving unless E1 to E4 are each answered for it; a route missing one
  is recorded as failing and names which.
- **AC6** — `git status --porcelain` after the research pass shows exactly one new path, under this
  build's `build` folder.

## 7. Gates

`memory hygiene (20 checks)` — check 5 for the recording's name, check 15's dead-path pin, check 12
for this spec. The full bar at the push boundary. No new leg, so `tools/gate-legs.json`, the charter's
gate-suite list, the map dossiers and the map re-render are all untouched.

## 8. Open questions

none — the fork below is RESOLVED (agent, 2026-08-15, delegated): option (b) — a PRIMED agent is under the directive layer when the priming is MECHANICAL.

  On precedent, and the precedent is binding rather than merely apt: M4 already mandates dispatching
  a pass kind — a spec review — into a `Workflow` sidechain and calls those agents primed. Option (a)
  would make M4's own instruction a violation of the layer M4 belongs to. **This resolution does NOT
  pre-decide the hunt.** It fixes what 'under the directives' MEANS; whether a mechanical priming
  route actually exists, and survives testing, is what this unit still has to establish, and
  no-route-exists remains a legitimate finding. §8 delegated this to the agent under a mandate.

**Does a PRIMED agent count as being under the directives, or only an agent that INHERITS them?** It
decides R2, and R2 is the route most likely to survive. Options: (a) inheritance only — a sidechain
agent is outside the layer however well briefed, and R2 dies; (b) priming counts when it is
MECHANICAL — the dispatching script reads the registry and the run's parked waivers and puts them in
the prompt, so what the agent got is derived from the record rather than composed by the dispatcher.
Recommendation: (b), on precedent — M4 already mandates dispatching a pass kind, a spec review, into a
`Workflow` sidechain, and calls those agents primed rather than ungoverned. Option (a) would make M4's
own instruction a violation of the layer M4 belongs to. Resolver: owner, or the agent under the
standing mandate if the owner does not take it.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the owner's P2 resolution recorded in the build README and
  from the design panel at `build/2026-08-14-build-cBriefedPilot-1-design-pass.md` §5. Carries one
  correction to that pass: its C6 rejection treats "a sidechain inherits no hooks and no `CLAUDE.md`"
  as settled, and the R2 test exists because it is not.

- rev-2 · 2026-08-15 · §8 resolved under the standing mandate for `cBriefedPilot`; the pick and the reasoning are in §8. Header gains the ratified pointer.

## 10. Reuse audit

- **`memory/guides/REVIEW-PROTOCOL.md`, its enforcement section** — the seam this unit reads. It
  already separates the static half (the hook on the tool call) from the runtime half (the slot
  claim) and already states where enforcement does not reach. R2's three observations are that split
  turned into three tests rather than a fourth opinion.
- **`tools/hooks/agent-cap.js`** — the budget is on disk as numbered slot files under a
  session-and-prompt-keyed directory, which is why R1 and R4 are directory listings rather than
  inferences. No code is changed; the file is the instrument.
- **`memory/builds/aDeployScout/spec/governance-deployer-research.md`** — prior art for R3. Its phase
  3 already specifies a headless runtime contract with the working directory set to a target worktree
  and the fan-out bounded, which is R3 and R5 combined and already argued once.
- **`memory/guides/BUILD-METHOD.md` M4** — the precedent that decides §8: a pass kind is already
  dispatched into a sidechain on purpose.

Recall terms used: parallelism concurrency pass dispatch agent spawn budget workflow sidechain hooks
directive mandate unattended write-set disjoint.

No seam exists for the research itself — this repo has no route inventory to extend, which is the
gap the unit fills.
