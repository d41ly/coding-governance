**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-5-researcher.md role-sha=51b61c49e522 task-sha=42eaf5b97638 -->

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

QUESTION (DEPLOY stage). What does "Deploy" mean in gov today in all three senses: (a) landing a change on the default branch and pushing it; (b) distributing gov's kits and charter into adopting repositories and keeping them updated; (c) releasing and deploying an adopting repository's OWN product. What should the Deploy stage's contract be? Cover: tools/push-main.sh and .githooks/pre-push; the charter's [land] [post-merge] [small] practices; remote CI; unattended landing; tools/govkit/ and skills/deploy-governance/; per-kit adopt-*.sh scripts and kit.toml descriptors; receipts, kit versions and kit epochs; tools/playbook/ rendering with deploy.toml answers; tools/agent-instructions/; WIRE-INTO-PROJECT.md (about 163 KB: read its outline and samples, never the whole file); memory/builds/aDeployScout/spec/governance-deployer-research.md; and whatever exists for an adopter's release, environments, rollout, rollback and post-deploy verification (the charter's `up —` micro-format, the [isolate] practice's ports and databases). Do NOT run govkit update, any adopt script in write mode, or any push. Deploy-stage Review: what reviews a landing, a kit release or an adopter's update today.

CONTEXT. Gov is being re-architected around ONE lifecycle loop of six stages (Plan, Design, Build, Test, Deploy, Maintain) plus a Review stage that can run at any stage, with instructions particular to that stage, and that reviews and adjusts the loop itself. The audience is concurrent, multi-node, agentic development in ANY adopting repository (gov dogfoods every kit on itself); manual owner use is in scope but secondary. Your question covers ONE stage and that stage's Review. Other researchers cover the other stages, so stay inside yours and name a hand-off to a neighbouring stage rather than researching it.

RETURN SHAPE: markdown, at most 1,800 words, exactly these six headings in order.
1. Inventory: every part serving this stage today (kit, skill, hook, gate leg, guide, record type, role), one line each: what it does, plus one path or file:line as evidence. Read the codebase-map dossier for a part first (memory/map/features/<feature>.md, cards in memory/map/generated/CARDS.md), and verify against code where a claim matters.
2. Flow: how the parts interact for this stage: inputs, mechanisms, outputs, and the hand-offs in from and out to neighbouring stages. Mark what is ENFORCED (a hook, gate or refusal, cited) versus only STATED in prose.
3. The implicit contract today: entry criteria, exit criteria, artifacts produced, who does the work (role, agent or owner), and how Review works at this stage, as they exist now.
4. Gaps: against a converged contract for this stage serving concurrent, multi-node, agentic development in any repository. One line each, severity HIGH, MED or LOW, and evidence: a file:line, a number measured by a read-only probe, or "absent: <what you searched>".
5. Candidates: two or three mechanisms for this stage's contract that would close the HIGH gaps, differing in mechanism rather than detail. For each: the mechanism, the existing seam it extends (path) or "no seam fits", the smallest test that would make it LOSE, and that test's result from a read-only probe you ran.
6. Pick: your recommended candidate and why, in at most five sentences.
You write no file and change nothing; every probe reads, and any temporary output is printed, never saved.

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
