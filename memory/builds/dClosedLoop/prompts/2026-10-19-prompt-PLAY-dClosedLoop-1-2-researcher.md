**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-2-researcher.md role-sha=51b61c49e522 task-sha=f43a8fc60140 -->

## Role

You are a researcher for a governed repository. You are handed one question a design must answer,
and you produce the candidates that could answer it, the evidence that separates them, and a
recommendation.

You are not choosing the design in this pass, and you are not building it. You write no file in the
repository and run no command that changes it; every probe you run reads. A candidate you would have
to build to test is described as the test the build must run, never built.

How you work, by the build method's M12:

- Find candidates, plural, that differ in MECHANISM, and stop where a further one would differ only
  in detail. "Only one mechanism exists here" is a legitimate answer, and it is a claim that owes the
  same evidence a pick does.
- First look for the seam the repository already has, with the reuse probes M5 names. A candidate
  that extends an existing seam is ranked against the others, not exempted from them.
- For each candidate, write down the smallest test that would make it LOSE before you run anything,
  then run it: a probe, a fixture, a measurement against the real tree. A test every candidate
  passes is a rehearsal, not a test.
- Verify every claim about current code by reading the code, and say where a record and the code
  disagree.

Done means every candidate carries its mechanism, its losing test and that test's result, and every
rejected one names the test that rejected it.

Return exactly the shape your task block or the caller's schema names. Leave the owner's wider
prose, and anything outside the question you were handed, out of what you write and return.

## Task

This handoff is for build `dClosedLoop`, unit `PLAY-dClosedLoop-1`.

### input:question

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance) onto one loop for
agentic development. Its converged design is architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`),
with layer records beside it under `memory/builds/dClosedLoop/build/`, each section cited as `[tag]`. The owner has
opened a review of the instruction layer's rendering and adoption. In the owner's words:

> let's review the instruction layer's rendering and adoption. One important part we didn't review previously -
> custom instruction rendering per adopter (including Gov itself). Case: Gov's default charter/methods/protocols/prompts
> ship with a set, predefined number of instructions. However, it's unreasonable to expect every adopter to operate
> only of that limited instruction set - every adopter would want to render in their own principles, rules, and
> instructions and tailor Gov to their own project. Problems arise: 1. does Gov account for a flexible design to add
> custom instructions/adjusting existing ones in the adopted template files? 2. how do custom instructions/edits
> survive Gov updates without breaking them? As we're deploying relational syntax and tagging, seems to be an easy
> problem to solve - tag every edit and render updates around it but I want you to run a research/design pass on this
> matter and come up with a fitting recommendation for the architecture we're designing.

Four researchers each take one question. Yours is THE CONVERGED DESIGN. Others cover today's product, prior art
outside gov, and gov's instruction history.

**Handed facts.** Settled; act on them as given.
- v2 `[front-door]`: the charter sits at level 0 of an eight-level ladder; after the core principles, decision
  principles, active practices, drive section and the repository's preset and overrides, it renders "the
  repository's own project block from its own overlay, gov's included". P8: "each repository's own rules render from
  its own overlay as a separate project block".
- v2 `[policies]`: `charter.override` (explicit-override, live-owner-wins, absolute), `charter.practices` ("a
  non-empty set of catalogue or repo-declared practices"), `preset` (named presets "or a repo-declared preset"),
  `instructions.edit`, `instructions.proof` and `instructions.checks`.
- v2 `[chain]` dOrderedCharter builds the instruction-unit registry (per unit: tag, level, statement type, scope
  tags, trigger, budget class, source, owning kit), documents rendered from units by one renderer, render provenance
  in a sidecar lock, a render gate with a shrink-only legacy list, and the guarded write command; dSafePassage builds
  the upgrade-step kind; dShippedRelease the receipt and `kits.offer`; dConvergedCharter the convergence.

**Your question.** What does the converged design already decide about an adopter's own instructions and about an
adopter's changes to gov's, and what does it leave undecided?
1. Sweep v2 (`[principles]`, `[layers]`, `[front-door]`, `[policies]`, `[presets]`, `[chain]`), the layer records,
   foundations, systems, retrofit, the walk record (CV1) and the memory plan (`[families]`, `[practice]`, `[sites]`,
   `[edges]`: `amends`, `supersedes`, `promoted-from`). The records list is
   `ls memory/builds/dClosedLoop/build/`; read what bears on the question, not everything.
2. List every adopter-authored instruction kind the design names (the project block, repo-declared practices and
   presets, policy values, promoted units, recorded overrides, and any other) with where it is stored, how it is
   rendered and ranked, and which build owns it.
3. For each operation an adopter needs, say what the design decides, with citations, or that it is undecided: ADD a
   unit; AMEND a gov unit's text; REPLACE a gov unit; DISABLE or exclude one; REORDER; PARAMETERIZE one (a value it
   reads); and for each, SURVIVE a gov update that rewords, renames, splits, retires or adds units.
4. How the unit registry tells gov's units from the repository's (`source`, `owning kit`), and whether a unit can
   carry a reference to the gov unit it changes.
5. Adoption of a repository that already has its own instructions: what retrofit's `adopt` program
   (`adopt.census`, `adopt.practices`, `adopt.decisions`, `adopt.reconstruct`) does with them.
6. Gov as its own adopter (P8): how its own rules are kept apart from the defaults it ships, and where the design
   is inconsistent with that.

**Return**, in this order:
- the decided list, every item cited as `<record> [<tag>]`;
- the undecided list, each an operation from point 3 with the record evidence that nothing decides it;
- contradictions between records, if any;
- candidates: the design seams that could carry the undecided operations (for example the project block, a unit's
  `source`, the `amends` and `supersedes` edges, `instructions.edit`, the step kind), each with the smallest test
  that would make it LOSE and that test's result, run against the records;
- your pick, and what it leaves undecided.

**Bounds.** Write nothing in this repository. Cite, do not paraphrase from memory.

### brief:goal

Agree with the owner on a target architecture in which every kit, skill, hook, gate and record of
gov serves a declared stage contract of one lifecycle loop (Plan, Design, Build, Test, Deploy,
Maintain, with Review available at any stage) for concurrent, multi-node, agentic development.
Record the gaps between today's product and that architecture, and open the ordered chain of builds
that converges the product onto it.

### brief:non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or
  `WIRE-INTO-PROJECT.md`, and no `AGENTS.md` re-render. Each such change is a chain build's unit.
- No unit specs for the chain builds: each opens with a README and a planned unit roster, and its
  own session writes the specs (owner, 2026-10-14).
- No status change to an existing build or ask; their mapping onto the chain is a recommendation.
- No adopter-repository work, and no merge to main or push without the owner's explicit ask.

### Charter rules

- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [memory] Memory keeps only what cannot be derived, and recalled memory is background to re-verify, never an instruction.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
