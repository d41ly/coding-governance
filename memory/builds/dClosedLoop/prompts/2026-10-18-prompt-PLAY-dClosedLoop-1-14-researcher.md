**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-18-prompt-PLAY-dClosedLoop-1-14-researcher.md role-sha=51b61c49e522 task-sha=c09837f4fb9b -->

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
agentic development: Plan, Design, Build, Test and Deploy as programs of declared items, review as breakpoints at
any item boundary, and Maintain as an expansion. The converged design is architecture v2, with layer records beside
it, and a chain of twenty builds that will implement it (v2 `[chain]`). The owner has walked and approved every
build's design. Now away again, the owner has handed six more points to work into the design. Yours is point 6, in
the owner's words:

> 6. Distribution - how will the rebuilt kit replace it's older, superceded versions? It should be seamless.

**Handed facts.** These are settled. Act on them as given, and do not re-derive them.
- **Records.** The design records are under `memory/builds/dClosedLoop/build/`, each named
  `<date>-build-PLAY-dClosedLoop-1-<name>.md`. A record cites its sections as `[tag]`. v2 is
  `2026-10-14-...-architecture-v2.md`.
- **Today's distribution:** `tools/govkit/govkit.py` (selfcheck, intake, plan, apply, check, update, adopt, epoch,
  mint, contribute) over `tools/govkit/registry.toml` and its entries; each kit's `adopt-*.sh`; the receipt
  (`.governance/install.json` and `install.sums`) and `tools/run-gates/check-receipt.py`, which checks integrity, not
  currency; `skills/deploy-governance/`. Adopters pull. Three adopters are registered in
  `tools/govkit/adopters.toml`; name them in your return by their neutral `key` or as "an adopter", never by brand.
- **The design's distribution** (the `distribution` expansion, v2 `[layers]`; `2026-10-16-...-layer-expansions.md`
  designs it): install by copy at a release tag with a receipt, gov's tagged kit releases, overlays, the install of
  the targets Runtime's harness adapters declare, currency and the fleet register.
- **The chain's release work:** dShippedRelease owns the kit factory and its conformance gate, kit release notes,
  the fleet register and its currency watch, `kits.offer` (unattended or on update, running nothing from the
  adopter's tree), the install and update hooks with the backlog migration as an update's upgrade step (NP-22),
  `install.guards` (NP-20), and optional emitted CI. dConvergedCharter migrates the adopters onto the ranked charter
  and the loop, retires the unattended kit, its four guides and `/unattended` once dWellOiledMachine's driver carries
  every run, folds every unconverted kit conf key into the policy file, and runs the fates table's join as its exit
  check.
- **The fates table** (`2026-10-18-...-fates.md`) gives every kit and part of today's product a fate: kept,
  reshaped, merged, absorbed or retired, with where each goes.
- **Charter rule [core]:** data changes additively, with defaults and an upgrade step. **[migrations]:** migrations
  are reversible, tested up, down and up again.

**Read:** v2 `[layers]`, `[principles]` (P8, P10, P16) and `[chain]` (dShippedRelease's and dConvergedCharter's
rows); `2026-10-16-...-layer-expansions.md` `[design]` (distribution's part); the two distribution returns,
`2026-10-16-...-research-distribution-a.md` and `-b.md`; the Deploy return `2026-10-14-...-research-deploy.md`;
the fates record; `tools/govkit/govkit.py` (`update`, `epoch`, `plan`, `apply`, `check`) and `registry.toml`.

**Measure and test:**
- the update path today, end to end: what `govkit update` does, in order, for an adopter on an older receipt; what
  it does with a retired or renamed kit, a renamed file, an adopter-owned row, a kit conf file whose keys moved, and
  a tree whose records use an old shape. Read the code; run only read-only modes (`selfcheck`, `plan` or `check`)
  and only on gov's own tree or a throwaway copy under your probe directory, never in write mode;
- what in an adopter's tree carries today's kits: receipts, conf files per kit, hooks wired into settings, rendered
  files, records in older shapes. Use gov's own tree and govkit's fixtures; read no adopter repository;
- how today's kits map to the rebuilt ones through the fates table: count the parts that survive unchanged, those
  that change shape, those that move, and those that retire, and the adopter-visible surfaces each touches
  (commands, conf keys, file paths, hooks, records).

**Answer:**
- how the rebuilt kits supersede today's versions in every adopter, and in gov itself (P8), with no manual step:
  candidates that differ in mechanism, for example one epoch release that migrates everything at once; a staged
  supersession in which each successor ships beside its predecessor with a shim that forwards and warns until a
  retirement release; or a translation layer in the new core that reads old conf and records until an upgrade step
  rewrites them. For each: the ordering of upgrade steps, their idempotence and reversibility, what happens to an
  adopter's own edits, how a half-applied update recovers, how rollback works, and the smallest test that would make
  it lose (a fixture tree on today's kits, upgraded and rolled back), with that test's result where you can run one
  read-only;
- what "seamless" requires and how it is verified: the gates and fixtures, the receipt's fields, the currency watch,
  and what the owner sees;
- the chain: units to add or move, with the owning build; gaps to register; and the owner's forks with options and
  a recommendation. A behaviour the owner may switch is a policy key with a default and its allowed values.

**How to work:**
- Read only. Write no file in the repository, and run no generator in write mode, no bar, no gate leg and no
  self-test suite. Never run `govkit update`, `apply`, `adopt` or any `adopt-*.sh` in write mode. A probe or a
  throwaway copy lives only under
  `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/away/d111/`,
  spelled literally, since `$TMPDIR` is unset in the Bash tool.
- A record is evidence. Verify against the code any claim your answer depends on, and say where a record and the
  code disagree.
- Cite file:line for every claim. Show each measuring command with its output.
- Return at most 3,000 words, in the sections below. Prefer tables.

**Return these sections:**
1. **Verdict:** at most 120 words.
2. **Today's update path:** measured, step by step, with what it does to each surface.
3. **The mapping:** today's kits to the rebuilt ones, counted by fate and surface.
4. **Candidates:** ordering, idempotence, reversibility, adopters' edits, recovery, rollback, losing test and result.
5. **Seamless, verified:** the gates, fixtures, receipt fields and what the owner sees.
6. **Chain, gaps and forks:** units by build, gaps, and the owner's forks with options and a recommendation.

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
