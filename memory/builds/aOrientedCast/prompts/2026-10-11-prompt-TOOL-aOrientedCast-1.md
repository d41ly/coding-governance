# The owner's prompt, verbatim, the brief it authorized, and what orientation found

**Serves:** research KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8

Handed to `/unattended` as the `--prompt` value on 2026-10-11, node `a`, in the session named
"Deterministic workflows for attended builds". The value carried whitespace and named no readable
file, so by the Skill's routing table it is the prompt itself and is taken verbatim. It names no
tracked id of this repo.

## The prompt

```text
The unattended kit includes several valuable workflows and tools to build higher quality code - build-oriented spec-writer agents, and builder agents/workflows that build from specs directly. These workflows are specific build-oriented and do not (presumable) run with non-essential context, allowing for better quality code to be built as a result. The owner has noticed that running attended does not follow the same workflows and wants them extended to attended builds/sessions as well. The owner has identified that even running through /session-kickoff, building the kickoff/ready cards, gathering additional orientation details in the attended builds results in non-deterministic workflows - specs are written inline with uncertain and unclear orientation details, builds can run before their specs, etc. 

Need: Any repo governed by CG, including itself, should enforce and run fully deterministic, oriented workflows. This should become one of the central features of this repo, spanning all of its tools - gov itself and its adopters should run LLM sessions through a set of its own agents/workflows/harnesses covering prompt writing (including handoffs to the agents, other sessions), orientation, bookkeeping, spec writing, code building, reviews, and gate bars. Each one of these should be established as a specific workflow, and governed by the kit across any LLM/build type. These workflows should run automatically and seamlessly throughout any build (attended or unattended) where necessary, converging around orientation and build's purpose.

Observations: 

* Regardless of whether its an attended or unattended session/build, orientation must go through the flow of writing/updating and ENFORCING a kickoff/ready card to keep the build on-point must be - in-scope, out-of-scope, to do, reuse, acceptance criteria, gates. 
* Prompts handed to the agents should always be build-oriented by the kickoff/ready card.
* Prompts should not simply be freeform, even when written by an agent, but follow a templated constant block relevant to its agents purpose (spec writer/spec reviewer/reuse agent/code builder/reviewer/anything else in the future) to improve its performance, for example: 'You're a code architect, writing a feature specification. You are not writing any code right now, just single unit of a larger build, that will a code will be built from. Your purpose is to carefully design this part of the build to ensure it's functional, concise, flexible and seamlessly integrates into the current product codebase...' + a variable block that contains additional details specific to the task, written at the handoff time. This should be easily owner-adjustable.
* Regardless of what build-type it is, spec writing/reviewing should always be delegated to the oriented/well-instructed agent(s) and shouldn't be done inline.
* Same applies to spec reviews, code building, closing reviews. Agents should always focus only on the specifics relevant to their task and leave any irrelevant output/owner prose out.


Research, design, and implement this as a larger architecture of this product.
```

## The brief

### Goal

Every session in a repository this kit governs, gov included, attended or unattended, runs its LLM
work through declared workflows. Orientation writes and enforces a complete card. Every agent prompt
is a rendered handoff: a constant role block the owner can edit, plus a variable task block rendered
from the card. Spec writing, spec review, building and closing review run only in their role agents,
and an attended code build runs the same harness pipeline an unattended one does.

### Items

1. A role catalogue: one owner-editable agent-definition file per role (orienter, researcher, the reuse-scout's slot, spec-writer, spec-reviewer, builder, diff-reviewer, skeptic, synthesizer, session-handoff), each declaring the workflow it serves, the card fields it reads, the path class it writes and what it returns, graded by a checker. [planned TOOL-aOrientedCast-1]
2. The card's `## task` gains To-do and Reuse, and `--card --append` refuses a READY body with an empty task field. [planned KICK-aOrientedCast-1]
3. A handoff renderer composes a role's constant block with a task block rendered from the card, the brief and the unit's spec into a prompt file, and refuses a card missing a field the role reads. [planned TOOL-aOrientedCast-2]
4. The catalogue renders native agent types under `.claude/agents/` with a freshness check, and role agents drop the charter where the CLI honours it. [planned TOOL-aOrientedCast-3]
5. The build harnesses take their role text and agent type from the catalogue. [planned TOOL-aOrientedCast-4]
6. The review harness takes its role text and agent type from the catalogue. [planned TOOL-aOrientedCast-5]
7. The write gate admits a spec write only from the spec-writer role and a product write only from the builder role, so the main loop is refused both. [planned TOOL-aOrientedCast-6]
8. A spawn guard refuses an Agent or Workflow call that carries no rendered handoff. [planned TOOL-aOrientedCast-7]
9. An attended router: kickoff's hand-back for a code build drives the same harness pipeline an unattended run uses. [planned KICK-aOrientedCast-2]
10. The charter states that agents are handed rendered roles and that the main loop delegates. [planned PLAY-aOrientedCast-1]
11. The kit is an adopter default, wired at install through govkit. [planned TOOL-aOrientedCast-8]

### Acceptance

Each mechanism is observed RED on a staged break and GREEN once restored. An attended dry run renders
a handoff from a card, and the write gate refuses an inline spec write from the main loop.

### Gates

The merge bar at the close (`GATE_FULL=1`), `govkit selfcheck`, and the memory hygiene gate.

### Non-goals

Rebuilding aRoutedQuill's mechanisms. Its routed-against-raw trial. Opting this build into the spec
audit. Adapters for tools other than Claude Code, beyond the rendered prompt file any tool can read.
The reuse-scout's content and the card's `## reuse` section, which belong to aScoutedSeam.

### Limitations

- aRoutedQuill's card route, write gate, subagent route context, routed-commits leg and brief
  skeleton are landed. This build extends them and does not respecify them.
- The reuse-scout's content and the card's `## reuse` section are aScoutedSeam's. This build edits
  no reuse file under `tools/codebase-map/`.
- Native agent types and `omitClaudeMd` were measured on Claude Code 2.1.292. That is the floor.
- This session read its agent registry before `.claude/agents/` existed, so it cannot spawn the
  types it renders.
- Its hooks run from the primary tree, so its own enforcement units bind it only after landing.
- No pass runs the merge bar or a self-test suite. The bar runs once, at the close.
- Only the owner opts a build into the spec audit (`TOOL-aWardedAudit-4`), and this one is not.
- The charter template stays within its gated size. A kit file names nothing outside itself by
  literal.

### Reuse

- **Seams extended:**
  - `checkRouted` and `readConfKey` in the hooks kit's scratch guard (aRoutedQuill's write gate);
  - the `Workflow|Agent` PreToolUse rule set in `agent-cap.js`;
  - `TASK_SKELETON` and `add_card_body` in the kickoff checker;
  - the `mode` and `workerType` arguments of the three harnesses (`TOOL-aStagedLane-2`,
    `TOOL-aMendedFleet-67`);
  - the kits' existing `*.agent.md` convention;
  - govkit's `seed` role.
- **Probe:** `reuse_lookup.py` found no existing renderer.
- **Recall:** the query surfaced `TOOL-aMendedFleet-67`, `TOOL-aMendedFleet-93`,
  `TOOL-aGraftedHelix-42`, `TOOL-dBriefedPass-2` and `TOOL-aStagedLane-2`.

## Drawn from the session

> aRoutedQuill is actually landing right now, its session is called 'Unattended aRoutedQuill'

— owner, 2026-10-11, a message sent mid-turn during orientation

> aScoutedSeam (node a) now owns reuse discovery, and here is my write set plus a proposed contract with your catalogue.

> (a) the reuse-scout role's CONTENT, the block text inside your catalogue slot;

> (d) the kickoff side: an owner opt-in and a `## reuse` section on the orientation/READY card, in skills/session-kickoff/.

> aScoutedSeam: agreed. My kickoff unit comes after your KICK units land, and it adds only the opt-in trigger and the `## reuse` section. That section also turns your interim `Reuse:` field into a pointer to it.

— agent, the session "Deterministic reuse workflows for agents", 2026-10-11, cross-session messages

## Owner confirmation

Asked: Accept this brief for build aOrientedCast? It layers on aRoutedQuill's card route, write gate and subagent hand-off, and I'll cut the branch once aRoutedQuill has landed on main. Use Other to edit it.

The brief shown with that question carried the same goal, the same eleven items, acceptance, gates
and non-goals as `## The brief` above, the last non-goal excepted, which the fourth answer added.

Answer: Accept as written

Asked: How should roles reach the agents?

Answer: Native agent types (Recommended)

Asked: Should role agents drop the 60 KB charter from their context?

Answer: Trim where it works (Recommended)

Asked: The session 'deterministic-reuse-workflows-f70c33-7f' started 3 minutes ago, and my message to it was held undelivered. What does it own?

Answer: It owns reuse

## What orientation found, before the roster was written

- **aRoutedQuill is built and lands first.** Its run is HELD for the owner's landing, with every
  unit CLOSED but its trial. It supplies the card's `## route`, the product-path write gate
  (`checkRouted` and `ROUTED_PATHS` in the hooks kit's scratch guard), a `SubagentStart` route
  context, a push leg grading routed commits, and `manifest-check.sh --brief-skeleton`. This build
  extends the gate and the card. It re-specs none of them.
- **The harnesses already run attended** (`TOOL-aStagedLane-2`, a `mode` argument). What is missing
  is that nothing routes an attended session into them, and their role text is inline JavaScript:
  `GROUND` and the spec writer in `unattended-build.template.js`, `PROMPT` in `unattended-unit.js`,
  and the lens sets, skeptic and synthesis in `tier2-review.template.js`. A workflow script has no
  filesystem, so role text must arrive in `args`, and in `tier2-review` it must join the resume
  print or a reused lens answers for a stale prompt.
- **Hooks can see which agent is writing, and the charter can be trimmed.** Measured before the
  roster, in [the agent-type probe](../build/2026-10-11-build-TOOL-aOrientedCast-3-agent-type-probe.md)
  on CLI 2.1.292. A custom agent type reports its own name as `agent_type` in every hook payload,
  for an `Agent` spawn and for a `Workflow` `agent()` given `agentType`. Without `agentType` a
  Workflow agent reads `workflow-subagent`. `omitClaudeMd: true` kept a codeword planted in the
  charter out of the agent's context, and both control arms saw it. That reverses what
  `TOOL-aMendedFleet-67` measured on 2026-10-04.
- **Agent definitions load from the project.** Creating the first `.claude/agents/` directory needs
  a session restart, and a definition copied in mid-session was measured not spawnable
  (`TOOL-aReplayedCard-5`). This session's settings resolve from the primary tree.
- **Kits already ship agent definitions** as `*.agent.md`: the orientation measurement arm in the
  workflows kit and the reuse-lookup instruction in the codebase-map kit.
- **The owner-editable layer for an adopter** is govkit's `seed` role: copied once, then the
  target's. An `engine` file is overwritten on every update.
- **Prior rulings that bind:** aReplayedCard's decision 1 of 2026-09-13, which this build supersedes
  for role agents by the owner's answer above; aRoutedQuill's no bypass and no warn phase;
  `TOOL-aWardedAudit-4`, the spec-audit opt-in is the owner's alone.
- **Recall terms used:** `role preamble GROUND brief spec writer builder lens skeptic synthesis
  handoff agentType workerType`. They surfaced `TOOL-aMendedFleet-67` and `TOOL-aMendedFleet-93`
  (judges spawn as `Plan`), `TOOL-aGraftedHelix-42`, `TOOL-dBriefedPass-2` and `TOOL-aStagedLane-2`.
- **Reuse probe:** `reuse_lookup.py` over "compose an agent prompt from a constant role template
  and a variable task block rendered from the kickoff card" found no renderer seam. It ranked
  `renderPromptLine` in the review harness, `add_card_body` in the kickoff checker and the
  `agent-cap.js` PreToolUse key, which are the seams the units extend.
