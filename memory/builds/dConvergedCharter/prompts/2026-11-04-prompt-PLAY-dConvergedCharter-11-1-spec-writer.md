**Serves:** journal PLAY-dConvergedCharter-11

# gov-spec-writer handoff — PLAY-dConvergedCharter-11

<!-- gov:handoff role=gov-spec-writer build=dConvergedCharter unit=PLAY-dConvergedCharter-11 path=memory/builds/dConvergedCharter/prompts/2026-11-04-prompt-PLAY-dConvergedCharter-11-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=5b55a6b7adc8 -->

## Role

You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite it by path and line. A claim
  you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the memory hygiene gate and the naming lexicon over your specs, and no other gate.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns. At a spec audit's disposal, a correction to an unbuilt sibling's spec
rewrites that sibling's text, with a rev bump and a revision-log line naming the repair unit and
the review record by its file stem, and a CLOSED sibling stays frozen.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dConvergedCharter`, unit `PLAY-dConvergedCharter-11`.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dConvergedCharter specced and built, so that each of the 23 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 1 owned nodes (Owned nodes) is built, and each of its 15 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0475@2b542935` · now `2b542935`, as at the baseline · tokens: none, so the token arm cannot see this clause — protocol text derived to facts only, each document in its envelope
2. `cl-dClosedLoop-0476@46c25c62` · now `46c25c62`, as at the baseline · tokens: none, so the token arm cannot see this clause — every remaining positional reference migrated to tags
3. `cl-dClosedLoop-0477@47475290` · now `47475290`, as at the baseline · tokens: none, so the token arm cannot see this clause — records merged by evidence
4. `cl-dClosedLoop-0478@5ccb9b38` · now `5ccb9b38`, as at the baseline · tokens: none, so the token arm cannot see this clause — superseded parts retired through ratified proposals
5. `cl-dClosedLoop-0479@8dc7a199` · now `8dc7a199`, as at the baseline · tokens: none, so the token arm cannot see this clause — adopters migrated onto the ranked charter and the loop
6. `cl-dClosedLoop-0480@7f73d023` · now `7f73d023`, as at the baseline · tokens: none, so the token arm cannot see this clause — every record kind on dTotalRecall's registry, the record-kind factory, and through its conformance gate (P16)
7. `cl-dClosedLoop-0481@a6574329` · now `a6574329`, as at the baseline · tokens: `help`, `help.explanation`, `help/` — protocols and templates rendered as tag-sliced views from the loop's checklists, the roles, the record schemas and the policies, the hand-written guides retired and their rationale moved into their units' `help` fields, never into `help/`'s feature pages, rendered into a tree of its own under `help/` as `help.explanation` says, which no agent loads, and no guide retired while a section of it maps to no unit's rationale, seen red on a planted retirement of such a guide (the owner's FQ-6)
8. `cl-dClosedLoop-0482@c8b56d3a` · now `c53ca182` by deviation `2026-11-03-build-PLAY-dConvergedCharter-8-deviation-81` · tokens: `--check` — the remaining renderers absorbed, each retired with its last document: kit/dogfood doc parity, review-protocol parity's document pair, each kit's skill wiring `--check` and govkit's placeholder render, review-protocol parity kept as the check of the workflows kit's four harness pairs, which render no document
9. `cl-dClosedLoop-0483@5b53c82b` · now `5b53c82b`, as at the baseline · tokens: `/gov-cleanup`, `/gov-drift`, `/gov-lexicon`, `/gov-recall`, `/gov-runlog`, `gov trace`, `gov why`, `gov-<name>`, `install.deprecation-window`, `pattern`, `probe`, `record find`, `to` — Skills converged to level-4 thin entries, each generated from the drive row of the command it runs and never hand-written, described "Use when …, runs …", installed with that command, and named `gov-<name>` where gov renders it: `/gov-recall` over `gov why` and `record find` and `/gov-runlog` over `gov trace`, both core, and `/gov-lexicon`, `/gov-drift` and `/gov-cleanup` with their kits, each rename shipped as an upgrade step with the old name forwarded for `install.deprecation-window` releases and its readers inventoried by path and by value and re-pointed in the rename's unit, each kit's `to`, `probe` and `pattern` rows, the adopt scripts and the self-tests' line-ending rows among them, a planted stale probe path seen red, and the Skill kind's conformance gate refusing a gov-rendered Skill without the prefix, seen red on a planted one (SK-2)
10. `cl-dClosedLoop-0484@7e1eaeeb` · now `7e1eaeeb`, as at the baseline · tokens: none, so the token arm cannot see this clause — the protocol slices and Skill entries rendered from units
11. `cl-dClosedLoop-0485@dde21704` · now `43490b62` by deviation `2026-11-03-build-PLAY-dConvergedCharter-11-deviation-111` · tokens: `*_keys`, `.githooks/pre-push`, `.githooks/pre-push --decide`, `INHERITED_RED=park`, `[effort]`, `[gates]`, `check_roles.py`, `handoff.py`, `land`, `park`, `read_policy_key`, `render_agents.py`, `roles.effort.*`, `roles_lib.load_policy`, `tools/push-main.sh`, `tools/run-gates/held_halves.py`, `tools/run-gates/post-merge.sh`, `tools/unattended/unattended.sh`, `transition_audit.read_modes` — `roles_lib.load_policy`'s house-file fallback retired with the seed, its `[effort]` readers, `check_roles.py`, `handoff.py` and `render_agents.py` among them, put on the `roles.effort.*` keys by TOOL-dBoundRoles-21 S1 and S7 through `read_policy_setting`, a build-run precondition of this unit, and its `[gates]` readers on each role definition's gate grant by TOOL-dBoundRoles-21 S6; the house-file arm `arm_house_readers` grades gov's tree once the seed file is absent, printing `house-file arm: unarmed` before, and is seen red on a planted reader of the house file in a fixture tree with no seed
12. `cl-dClosedLoop-0486@36def3b5` · now `36def3b5`, as at the baseline · tokens: `/unattended`, `AGENTS.md`, `README.md`, `[[exempt_leg]]`, `[[retired]]`, `fork-ceilings.txt`, `method-carriers.txt`, `tools/unattended/` — the unattended kit, its four guides and `/unattended` retired once dWellOiledMachine's driver carries every run, its readers inventoried by path and by value over the tree and each re-pointed or retired with it: the gate legs that reference the kit, the template-size and `[[exempt_leg]]` rows, the registry's `[[retired]]` row, the charter template's protocol line and its renders, `AGENTS.md` and the docs' pointers, `fork-ceilings.txt`'s and `method-carriers.txt`'s rows, root `README.md`'s two lines and the product rule's "four-verb driver", and the spawn-budget leg run on a scratch clone with `tools/unattended/` removed (night pass, point 1)
13. `cl-dClosedLoop-0487@ff29708d` · now `ff29708d`, as at the baseline · tokens: none, so the token arm cannot see this clause — feature-specific guide prose migrated into feature-scoped units (night pass, point 4)
14. `cl-dClosedLoop-0488@7cf98c51` · now `7cf98c51`, as at the baseline · tokens: `.claude`, `.githooks`, `.github`, `git ls-files`, `help`, `kept`, `memory/guides/`, `skills`, `tools` — every part in the fates table at its fate, the table's join run as convergence's exit check over a population derived from `git ls-files` across `tools`, `skills`, `.githooks`, `.claude`, `.github`, `help`, the runbook and the template, and every path a fates row names outside them, `memory/guides/` and the root's kit confs among them, every path matched by a row's path glob, a planted unlisted file and a planted surviving `memory/guides/` file each seen red, and a declined retirement amending its part's row through the ratification record to `kept` or a new fate, which the join reads, a planted declined proposal passing on the amended row and red on an unamended one (night pass, point 8)
15. `cl-dClosedLoop-0489@74c9a546` · now `74c9a546`, as at the baseline · tokens: `README.md`, `help/` — the hand-written `help/` pages, the kit READMEs, root `README.md` and the agent runbook migrated, each with its fates row, its reference half generated from its registry by dOrderedCharter's renderer, the runbook's taken as dShippedRelease derives it, and its how-to half written as a page under the docs leg, a hand edit to a rendered page red at render parity (SA-5, the owner's FQ-5)
16. `cl-dClosedLoop-0490@166e1002` · now `0c938e1f` by deviation `2026-11-03-build-PLAY-dConvergedCharter-16-deviation-161` · tokens: `.claude/settings.json`, `/session-kickoff`, `[[retired]]`, `install.deprecation-window`, `kickoff.runs`, `manifest-check.sh`, `memory/guides/SESSION-KICKOFF.md`, `skills/session-kickoff/` — the same, and the engine's procedure, the Skill's body below its front matter, moved with them into the kit home as `KICKOFF-ENGINE.md`, shipped by the `kickoff-manifest` entry to each repository at `{prefix}/KICKOFF-ENGINE.md`, which the orientation scout and an inline orientation read in place of the Skill.
17. `cl-dClosedLoop-0491@3aafd2a1` · now `3aafd2a1`, as at the baseline · tokens: `/build`, `[[retired]]`, `install.deprecation-window` — the `/build` Skill retired once dWellOiledMachine's supervisor drives attended builds: a `[[retired]]` row with its readers inventoried by value, the charter's attended-build line, the roles kit's skill template, its install row and probe, and its harness wiring, and the kickoff card's hand-off to it, the client dWellOiledMachine left kept for `install.deprecation-window` releases, then removed (SK-1)
18. `cl-dClosedLoop-0492@a532274c` · now `a532274c`, as at the baseline · tokens: `[cycle]` — the owner's cycle walked by key: from a planted build's intake, every hop of the memory plan's `[cycle]` resolved by a key, red on any hop resolved by search or prose, the walk run as convergence's acceptance once every hop's build has landed (the shape audit)
19. `cl-dClosedLoop-0493@0d92d2e3` · now `67838f7a` by deviation `2026-11-03-build-PLAY-dConvergedCharter-19-deviation-191` · tokens: none, so the token arm cannot see this clause — the per-directory line-ending pins retired into class pins, in gov's `.gitattributes` and in the kits' `[[lf_pin]]` rows alike, so an adopter's govkit block pins every tracked `*.md`, `*.txt`, `*.toml`, `*.sh`, `*.js` and `*.json` file it holds, a kit's own or not, and the upgrade step `govkit/lf-pins-to-class` renormalizes the CRLF ones
20. `cl-dClosedLoop-0494@eb095d63` · now `4e004b72` by deviation `2026-11-03-build-PLAY-dConvergedCharter-20-deviation-201` · tokens: none, so the token arm cannot see this clause — the exit check widened: every row of the adopter register, a registered adopter at the converged release passing with no step pending or on an open owner item for that adopter, and an unregistered one passing only on an open owner item for it; an empty register is not graded.
21. `cl-dClosedLoop-0495@53f4c9b2` · now `53f4c9b2`, as at the baseline · tokens: `[gates]`, `adopt.declarations`, `default`, `roles.effort.*`, `roles.effort.default`, `tools/roles/house/policy.toml` — `tools/roles/house/policy.toml` retired as a seed: a repository's efforts folded into the `roles.effort.*` policy keys, only those the owner has not ruled on through `adopt.declarations`, a declined proposal read as a drop, seen on a planted declined effort the fold leaves unwritten, its `default` into `roles.effort.default`, its `[gates]` into each role definition's gate grant, gov's default efforts and grants shipped in the role definitions every release updates, and the readers dBoundRoles re-pointed losing their house-file fallback, with an upgrade step (FA-6, P38, the flow adoption's review)
22. `cl-dClosedLoop-0496@a94b54b6` · now `a94b54b6`, as at the baseline · tokens: none, so the token arm cannot see this clause — the census of gov's own flow and role settings: the legs no descriptor declares, gov's efforts and grants, and its run conf and gate environment values, each ruled by the owner, the gov-only ones moved to gov's own overlay and policy file, and the run conf's extension keys retired with the unattended kit (IA-6, FA-1)
23. `cl-dClosedLoop-0502@fbfa8f4f` · now `fbfa8f4f`, as at the baseline · tokens: `[design-observability]`, `release-verify-failed`, `release.route`, `seen` — the release asks' join: Maintain's `release-verify-failed` ask and `release.route`'s keyed alike by (reading, (SHA, E)), so a red verify under roll-forward leaves one open ask with a `seen` row, not two, dTendedCadence and dShippedRelease each building its half against a stand-in for the other's, seen red on a planted red verify that files two asks (layer-expansions `[design-observability]`, the whole-design audit's fold, B5-F14)

### brief:acceptance

- At the Design exit, `carries.py --build dConvergedCharter --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dConvergedCharter` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dConvergedCharter --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 486 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dConvergedCharter by <decision>` line.
- Any path outside `memory/builds/dConvergedCharter/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.

### input:spec

memory/builds/dConvergedCharter/prompts/2026-11-04-prompt-PLAY-dConvergedCharter-41-split-brief.md

### task:reuse

tools/workflows/unattended-build.js and tier2-review.js as the harness; the sibling spec runs (dMindYourWords 7fba335c5..f4597719e) as precedent for the record shapes.

### Charter rules

- [yagni] YAGNI: build what this unit needs now, never scaffolding for later, and delete rather than disable.
- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [core] One shared core with thin adapters, so logic and authorization live once; data changes additively, with defaults and an upgrade step.
- [contract] A contract two parties share lands first, as one source with generated copies and a parity gate against a live re-derivation; deployables sharing one artifact release together.
- [derive] Derive over author: status, counts, inventories and indexes are generated or declared and checked both ways, never typed beside what they describe.
- [one-fact] One fact in one place: a document points at the source that owns a value, or a gate compares the two.
- [spec] Spec before code: every product-code unit commits its spec first, a micro-spec for a mechanical change and a full design pass for a substantive one.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [gate] A gate never seen red is not a gate: observe its failing case, state what it does not check, and never read a skip, an unmovable probe, an exemption or an empty population as coverage.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [small] Work in small units, one stream each, merged to local main often; risky behaviour lands dark behind a default-off switch.
- [docs] A user-facing change is not done until its page under `help/` is current.
- [security] Security first: validate once at the write boundary, deny by default, give automation the narrowest grant, and keep secrets out of files, memory and chat.

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
