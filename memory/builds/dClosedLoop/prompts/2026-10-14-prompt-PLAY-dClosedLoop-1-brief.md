# Brief — dClosedLoop: gov re-architected onto one lifecycle loop

**Serves:** research PLAY-dClosedLoop-1

node d · 2026-10-14 · authorized-by prompt. The owner invoked `/session-kickoff` with the text
below as its arguments; its bytes are copied here so the build's authorization cannot move.

## The prompt

```text
Gov (Coding Governance) - is a 'Development Lifecycle Governance Product' and an architecture - an environment of converged methodologies, practices and deterministic processes that govern and direct a production LOOP of six primary steps in any REPO: 'Plan' - 'Design' - 'Build' - 'Test' - 'Deploy' - 'Maintain'. There is a supplementary 'Review' stage that exists at any stage of the loop as necessary with instructions particular to that stage to review and adjust the loop itself. Gov is intended for concurrent, multi-node, agentic development and is built to ensure high-quality agentic product development cycle. These are the basic foundations that determine everything that happens in this repo. Manual, owner use of the tools is in scope but its not the primary focus of this product.

Gov does not yet converge into the described architecture - there are several gaps at all stages that need to be closed.

Objective this session: Develop and detail a plan to rearchitecture this product towards the outlined goal, with the owner's goals in mind. Test, suggest, and iterate on ideas to reach a consistent, systemic outcome.

Steps:

* Review what currently exists in the product and how its parts interact with one another. Outline the gaps.
* Together with the owner, define what the final converged architecture should be by asking questions, suggesting and iterating ideas. How should this repo govern? What should it enforce? How should the workflows and processes be designed? Etc., these are example questions and are not limited to. Ask all questions necessary for a holistic design.
* Open a **chain of builds** to cover each step of the loop that ultimately must converge into a single product.


Technicals:

* This is primarily a THINKING exercise to improve and transform this product.
* This session itself runs the expensive 'Max' effort. Any workflows and agents spawned by it must run the effort defined by the ROLES of this repo.
```

## The brief

### Goal

Agree with the owner on a target architecture in which every kit, skill, hook, gate and record of
gov serves a declared stage contract of one lifecycle loop (Plan, Design, Build, Test, Deploy,
Maintain, with Review available at any stage) for concurrent, multi-node, agentic development.
Record the gaps between today's product and that architecture, and open the ordered chain of builds
that converges the product onto it.

### Items

1. Review what exists and how its parts interact, and outline the gaps per stage.
2. With the owner, define the converged architecture: how gov governs, what it enforces, and how
   its workflows and processes are designed, by questions, suggestions and iteration.
3. Open a chain of builds covering every stage of the loop, converging into one product.

### Acceptance

- The owner's ratified answers exist as decision rows that `tools/memory-recall/query.py` returns.
- The regenerated `memory/LIVE.md` lists every chain build as non-terminal, and each chain README
  names its stage and its predecessor.
- A join of the gap register against the chain READMEs shows every gap owned by exactly one build
  and every build owning at least one gap, seen red on a planted orphan row before it is trusted.
- The spec audit's synthesized report sits under `reviews/`, every finding folded or rejected with
  its reason.

### Gates

Per pass on the staged tree: `kickoff-manifest ratchet`, `memory hygiene`, `build README slot
contract`, and no stale generated output (`bash tools/run-gates/run-gates.sh --regen`). The full
bar, `bash tools/run-gates/run-gates.sh`, runs before any landing.

### Non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or
  `WIRE-INTO-PROJECT.md`, and no `AGENTS.md` re-render. Each such change is a chain build's unit.
- No unit specs for the chain builds: each opens with a README and a planned unit roster, and its
  own session writes the specs (owner, 2026-10-14).
- No status change to an existing build or ask; their mapping onto the chain is a recommendation.
- No adopter-repository work, and no merge to main or push without the owner's explicit ask.

### Limitations

- A thinking exercise first: the deliverable is the ratified design and the opened chain.
- The session runs at max effort; every agent and workflow it spawns runs the effort its role
  declares, never an override.
- Spec writing and review run in role agents, per the charter's `[roles]` rule.
- Agentic, multi-node use is the primary audience; manual owner use is in scope but secondary.

### Reuse

The derived inventory is `memory/map/` and `tools/gate-legs.json`; gap evidence comes from
`tools/drift-audit/drift_report.py`; the Deploy stage inherits `DEPL-aDeployScout-1`; the Build
stage inherits `memory/guides/BUILD-METHOD.md`; the audit runs on `tools/workflows/tier2-review.js`;
`tools/memory-tree/gen_build_index.py` opens builds and renders `memory/LIVE.md`. Recall terms
used: charter template kit govkit deployer bar legs build-method unattended roles kickoff spec
lifecycle.

## Drawn from the session

> Declare `spec-audit:` for this planning build — Yes, declare it (Recommended).
— owner, kickoff question 1, 2026-10-14

> How far should opening the chain of builds go in this session? — README + unit roster
> (Recommended).
— owner, kickoff question 2, 2026-10-14

## Owner confirmation

Asked: Ready. Say go and I'll start, or change any field.
Answer: Go

<!-- the card's route: once every spec it names is tracked, pipe from the heading down to --card --append --session <sid>; append again when that set changes -->
## route
- build: dClosedLoop
- unit: PLAY-dClosedLoop-1 · spec memory/builds/dClosedLoop/spec/2026-10-20-spec-PLAY-dClosedLoop-1.md
- brief: memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-brief.md
