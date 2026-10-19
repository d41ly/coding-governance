**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-28-researcher.md role-sha=51b61c49e522 task-sha=f5e2fe8bbd9a -->

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

**Context.** dClosedLoop is a design-only build that re-architects gov (coding-governance), a kit set that ships project-agnostic governance to repositories that adopt it, gov's own repository among them. Its converged design is architecture v2 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`, 1,784 lines), at `930120e45` on this branch, with its layer, system and round records beside it under `memory/builds/dClosedLoop/build/` (172 records, the research returns among them) and its reviews under `memory/builds/dClosedLoop/reviews/` (50), each section cited as `[tag]`. The design plans 21 chain builds, one row each in v2 `[chain]`, whose planned units are the clauses of the row's units cell split on "; " (484 in all), with 40 principles, 261 policy keys, 378 gaps each owned by one build, and some 80 record kinds (layer-memory `[contract]`). No chain build has a unit spec yet: the owner ruled on 2026-10-14 that this build writes none, so speccing is the next phase, done build by build with today's tools, before the product the design describes exists. The owner closes the design pass with five questions, in the owner's words:

> We're wrapping this design pass, final questions to resolve:
>
> 1. Can we run a thorough adversarial workflow to review the entire design step by step and ensure no critical gaps were left, before we move on to speccing it?
> 2. How are we going to control and verify that the entire design was specced as planned? There have been numerous precedents before - agents can lose the chain of thought and start deviating from design. A control mechanism is required.
> 3. How are we going to ensure that the specs are not deviated from without reason and any deviation is accurately logged and reflected in the final artifact.
> 4. Human-readable help - the product needs to be fully documented (for human owners) and should not be a black box when the build is complete. What is the current plan in this regard?
> 5. Once the build is fully complete, another version of the Atlas should be maintained _in the repo_ (not an online artifact) alongside help pages to visualize product's design and architecture, and should be maintained through all the future updates.

Nothing is built or specced now: the answer is a design the owner can approve, saying what must exist before speccing starts and what the chain builds must carry.

**Handed facts, to re-verify, never to act on unread.** Today's speccing and building path: `/session-kickoff` (it orients, derives a closed scope and writes the kickoff card), the write gate (it refuses a product-code write no specced unit owns), `memory/TEMPLATE-SPEC.md` (the spec's shape), `memory/guides/BUILD-METHOD.md`, the `gov-spec-writer`, `gov-spec-reviewer` and `gov-builder` role agents (`tools/roles/`), spec audits and closing reviews through `tools/workflows/tier2-review.js`, `/build` for an attended code build, the unattended kit (`tools/unattended/`, its `--check-commit` and `--dispatch`), `tools/memory-tree/` (the hygiene checks, check 21 and check 23 among them, and `gen_build_index.py`, which renders each build README's roster and `memory/LIVE.md`), `spec-tokens` (seven joins over a live spec's tokens), the merge bar `tools/run-gates/run-gates.sh` (its legs in `tools/gate-legs.json`), and `help/` (two pages) under the charter's `[docs]` rule (`AGENTS.md` section 1). The design's planned mechanisms, to find and cite rather than trust: dIndexedDesign (the Design stage: roster, inventory, seams, feature design, the design index), dScopedBuild (the Build stage: `build.scope`, `build.acceptance`, `build.reuse-check`), dFairHearing (the review harness and the spec audit's design-audit preset), dDeclaredLoop (the loop, its breakpoints and the static termination check), dConvergedCharter (`help/` rendered from each user-facing unit's `usage` field, and a docs leg, SA-5), dTotalRecall (the project map and `gov map`), this build's atlas generator (`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`) and design map generator (`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-map.py`), and the instruments it runs over its own records: the gap join, the reconciliation probe, the clause scan, the preset check and the critical path (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-night-pass-instruments.md` `[final]`; that record quotes its recorder's source, headings included, so read from the LAST `## [final]` heading). Principles that bind any answer: P12 (specs are structured contracts), P17 (features carry the design between units), P19 (built work is never rewritten in place), P22 (position is derived, never remembered), P25 (role functions live only in role agents), P26 (every exchange between roles is a typed record), P30 (memory is declared once and written through one door) and P35 (every record names its cause), in v2 `[principles]`, and the charter's `[derive]`, `[one-fact]`, `[spec]`, `[gate]`, `[docs]` and `[left-shift]` rules. The owner's standing rule: every behaviour is a switchable policy, the recommended answer its default and the other options its allowed values, structural choices excepted. Precedents the owner names, agents losing the chain of thought and deviating from the design, live in this repository's build folders, reviews, comparison records, `memory/gotchas/` and `memory/DECISIONS.md`.

Five researchers serve the owner's five questions, one each: the whole-design audit, the control that the whole design is specced as planned, spec deviation and its log, human-readable help, and the in-repo atlas. Yours is THE WHOLE-DESIGN AUDIT; stay inside it, and name a finding that belongs to another only in one line.

**Your question.** The owner's first question: can a thorough adversarial workflow review the entire design step by
step and ensure no critical gaps were left, before speccing? Design that workflow.
1. **What earlier audits covered.** Measure every review this build ran over its design: the declared whole-design
   audit and its fold, the shape audit's pair, and each paired closing review since (`reviews/`, the
   `*-reviews-compared.md` records, the session log's dispatch rows). For each: its subject, the records it read, its
   lenses and slicing, its raw and confirmed findings, its recall estimate where a comparison computed one (Chapman),
   its cost (agents, out-tokens, wall), and what it could not see. Then map that coverage onto the design's parts: per
   stage step (`step.*` in the design map: entry, plan, design, build, test, deploy, breakpoint, probe, lifecycle,
   adopt), per layer, per chain build and per principle, how many confirmed findings each audit raised there, and
   which parts no audit read end to end. The session model (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-session-model.md`,
   holes H1 to H16) walked one build through every step: compare what that walk found with what lens reviews found.
2. **Define a critical gap** for this design so the audit can be graded. Candidates: a step item with no actor,
   input, witness or outcome; a scenario that cannot reach a terminal; a record kind with no writer or no reader; a
   key no item reads; a principle no clause enforces; a clause reading what no ancestor build registers; a bootstrap
   hole, where a chain build needs a mechanism only a later build provides. Say which classes an instrument already
   checks mechanically, and which only an adversarial reader can find.
3. **Survey** adversarial design-review methods with evidence of what each catches: scenario-based architecture
   reviews (ATAM and its descendants), failure-mode and effects analysis, pre-mortems, threat-modelling walkthroughs
   (STRIDE per data flow), red teaming, model checking and table-driven completeness checks, inspections with
   checklists (Fagan), and multi-agent LLM review where it has been measured.
4. **Propose the workflow:** its slicing (by step, by scenario, by build, by principle, or a mix); the scenario set
   to walk, at least a solo attended build, an unattended build across nodes, a patch build of a landing, an
   adopter's update, a withdrawal and a failure at every stage; its lenses; finder and skeptic counts inside the
   bounds (at most 5 verify agents in total; the owner's workflow size guideline keeps one workflow near 10 agents;
   effort medium, the owner's NT-12); pairing, two independent runs as the paired closing reviews ran; what each
   agent reads; how findings are graded critical; what witnesses "no critical gap left", such as a coverage table in
   which every step, layer, build and principle was read by a finder with its verdict; its cost; how its recall is
   tested, such as gaps planted in a copy of the records that it must find; and when it runs relative to the folds the
   other four questions will add. Use `tools/workflows/tier2-review.js` where it fits, and say where it does not.

**Return.** The coverage table of past audits; the critical-gap classes, each with its existing check or none; the
methods table with sources; the proposed workflow with its cost and its recall test. Each candidate names the test it could lose, its owning chain build, what must exist before speccing starts, and any policy key with its values and default.

**Bounds.** Write nothing in this repository. A probe works only in your own scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/d155/`, which you create and delete when you finish; write or delete nothing anywhere else, the parent session's scratch folder included. Make no model call: no `claude -p`, no API call, no Workflow and no agent spawn. Cite every claim about an outside method, tool or standard to its source (URL and the date you read it). Cite every claim about the records as `<record> [<tag>]` and every claim about code as `path:line`, quote commands and their outputs as measured, and say where a source is ambiguous. Another agent may be reading this tree while you work: modify nothing in it. Run no gate leg and no test suite.

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
