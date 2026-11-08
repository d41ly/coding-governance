**Serves:** journal TOOL-dFairHearing-25

# gov-spec-writer handoff — TOOL-dFairHearing-25

<!-- gov:handoff role=gov-spec-writer build=dFairHearing unit=TOOL-dFairHearing-25 path=memory/builds/dFairHearing/prompts/2026-11-03-prompt-TOOL-dFairHearing-25-3-spec-writer.md role-sha=dcd8416ea3d2 task-sha=dea565f7124c -->

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

This handoff is for build `dFairHearing`, unit `TOOL-dFairHearing-25`.

### brief:goal

Revise `memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md` so replay 1's two runs can be admitted. Pass (a) is `d3c98d523` (its return is `memory/builds/dFairHearing/build/2026-11-03-build-TOOL-dFairHearing-25-1-builder-return.md`): it built S8 and S9 and made clones `fhr1a` and `fhr2a` by S2's placement. The main loop then made the S1 call, `tier2-review.js` with `repo` the clone, `reviewDir` `memory/builds/dFairHearing/reviews` and the one subject `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-runtime.md`. The live agent-cap hook denied both calls before any agent ran, through `tools/workflows/spec-audit-optin.js:158-164`: a spec-audit call whose `subjects` name a path outside `builds/<reviewDir's build>/` is refused. So S2 and AC2 cannot pass as written: AC2's own red case is the state the tree is in. Commit nothing; the main loop commits.

### brief:items

1. Read `tools/workflows/spec-audit-optin.js` from its argument read through the README and `RUN.md` reads (about `:118-215`), and state in §4 what the pack needs from a replay call: the subject's build folder, the README it reads in the clone, the `RUN.md` branch, and the front-matter key. Cite the lines.
2. Settle the placement as a §8 fork marked by M3 and resolved `RESOLVED (agent, 2026-11-03, delegated)` with M3's reason. The owner's opt-in is the `spec-audit:` key in this build's README at base `3708a705`; a key the run writes into another build's README is the self-opt-in the pack's own comments refuse (TOOL-aWardedAudit-4), so name that veto if you discard such an option. The candidate the main loop sees is: the placement commit also adds the subject's blob `767187aa` at a path under `memory/builds/dFairHearing/`, the call names that path as its subject, and the sibling `specs` stay at their dClosedLoop paths. Check the known-set scoring (spec 1 S3, the `[tag]` address) and spec 1 AC4's blindness against it, and reject it if either breaks.
3. Carry the choice through S1, S2, S8 (the placement step in `tools/workflows/README.md`, which pass (b) may now edit), AC1 (the clone's `diff --name-only` line), AC2 and AC8, so every criterion agrees with the chosen placement.
4. S10's attempts: say whether `fhr1a` and `fhr2a`, made but never run because the call was refused, count as attempts. A clone that no agent read is not a void run; if the new placement needs new clones, name them so no clone serves two attempts.
5. Pass (b) builds the rest. Say in §4 that the main loop runs the two calls between pass (b)'s placement change and its verdict commit, or split the remaining work so the S7 rule still holds: the commit that adds the verdict record has the orchestrating commit as its first parent.
6. Rev bump and one §9 line per change, each naming a section, scope or acceptance id, and this brief. Leave the status header's state as it is.

### brief:acceptance

Every criterion a correct build can pass on today's tree and hook; the §8 fork in the shape README rule 5 states; the return names the lines item 1 read.

### brief:gates

None you run.

### brief:non-goals

No change to the known set, the bars, the scorer, the pack, or any spec but this one. No code.

### input:spec

memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md

### task:reuse

each unit's spec §10 names its seam; the review harness tools/workflows/tier2-review.template.js and tools/hooks/agent-cap.js are the main seams.

### card:route

- build: dFairHearing
- unit: TOOL-dFairHearing-25 · spec memory/builds/dFairHearing/spec/2026-10-23-spec-TOOL-dFairHearing-25.md
- brief: memory/builds/dFairHearing/prompts/2026-11-03-prompt-TOOL-dFairHearing-25-pass-a-build-brief.md

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
