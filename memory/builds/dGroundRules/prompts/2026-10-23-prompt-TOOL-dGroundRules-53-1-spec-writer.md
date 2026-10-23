**Serves:** journal TOOL-dGroundRules-53

# gov-spec-writer handoff — TOOL-dGroundRules-53

<!-- gov:handoff role=gov-spec-writer build=dGroundRules unit=TOOL-dGroundRules-53 path=memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-53-1-spec-writer.md role-sha=06b14b1ac42a task-sha=97e415d3d8c0 -->

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
after every writer returns.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## Task

This handoff is for build `dGroundRules`, unit `TOOL-dGroundRules-53`.
Not supplied, optional: `card:route`.

### brief:goal

Every unit of dGroundRules specced and built, so that each of the 11 clauses of its row in v2's `[chain]` (Items) is carried by a spec pinned to its hash and built, each of its 5 owned nodes (Owned nodes) is built, and each of its 3 owned gaps (Gaps) is closed.

### brief:items

Each clause of the row, in its order: its id at its baseline hash, its hash now in the as-built view with the record behind any change, its tokens as `carries.py`'s token arm reads them, and its text.

1. `cl-dClosedLoop-0007@b0458b78` · now `b0458b78`, as at the baseline · tokens: `.governance/policy.toml` — `.governance/policy.toml`, its schema, its one reader and its JSON mirror, moved from dDeclaredLoop so that both roots read policy from a build ahead of them (RC-1), the schema refusing an empty value for every set-valued key whose Allowed cell says never empty, seen red on a planted empty value for each such key the catalogue holds, and a set-valued key that declares no empty-set rule refused (the shape audit), and each key's row carrying a summary and a usage, a key added without them refused and today's keys drained from a shrink-only list, seen red on a planted new key with no summary (the owner's FQ-5, P42)
2. `cl-dClosedLoop-0008@6598846f` · now `6598846f`, as at the baseline · tokens: `read_policy_key` — the reader extending `read_policy_key`'s contract, read at the landed revision, never from the working tree, parsed and never sourced (M7)
3. `cl-dClosedLoop-0009@7d93fce9` · now `7d93fce9`, as at the baseline · tokens: none, so the token arm cannot see this clause — each key resolved in one order: an override in the file, then the named preset's value once dKeptSession adds presets to this reader, then the catalogue default with the reason recorded, which is all an absent file or one naming no preset reads (H4, DA-M10)
4. `cl-dClosedLoop-0010@cd629be7` · now `cd629be7`, as at the baseline · tokens: `policy-file.on-invalid`, `refuse` — a malformed file or an out-of-set value read as `policy-file.on-invalid` says, by default the last valid landed revision with the reason recorded and, with none, the push and landing gates refusing and naming the line, `policy-file.on-invalid` itself read from the last valid landed revision whenever the current file is invalid and an out-of-set value of it counting as malformed, each failure class (absent, malformed, missing key, out-of-set value, and a valid revision setting `refuse` followed by a malformed one, which must refuse) planted with its stated outcome, and a planted repository whose last valid revision sets each guard-bearing key explicitly at strict's [presets] value reading those values from a later malformed revision, never the catalogue defaults (AF-2, DA-H6, FM2, FM9)
5. `cl-dClosedLoop-0011@8312590d` · now `8312590d`, as at the baseline · tokens: `policy-file.on-invalid` — the JSON mirror regenerated at each landing and pinned to the landed revision, every consumer reading the mirror from the landed revision's blob, or checking its hash against the TOML at that revision and else reading through the TOML reader, a parity leg red on a hand-edited mirror, an arm red when a hook enforces a hand-edited working-tree mirror's loosened value, and a stale or absent mirror read as `policy-file.on-invalid` says (AF-2, DA-M11, FM1)
6. `cl-dClosedLoop-0012@937c308e` · now `937c308e`, as at the baseline · tokens: `.governance/deploy.toml`, `.governance/instructions.toml`, `budgets.*`, `memory/DECISIONS.md`, `policy-file.guard`, `policy-file.proof`, `tools/template-size-limits.txt` — the minimal guard, enforcing the defaults of `policy-file.guard` and `policy-file.proof`, owner-only and the TTY proof, without reading either key, and refusing agent writes to the policy file, its JSON mirror, the instruction manifest, which is the repository's overlay `.governance/instructions.toml`, and `.governance/deploy.toml`, whose answers render into the charter's level 0, until dDeclaredLoop's guard lands, the minimal guard admitting one agent write shape meanwhile, a single measured-file cap under `budgets.*` raised, nothing else changed, with its change record attached, which at this build is today's rule from `tools/template-size-limits.txt`, the RAISED argument in place beside the cap and a `memory/DECISIONS.md` row in the same commit, the minimal guard checking for both, until dOrderedCharter's instruction change-record kind lands and re-points it, the file's other conditions left to the record's argument as today, and the guard once it lands admitting that raise alone, seen green on a planted raise of a single measured-file cap under `budgets.*`, nothing else changed and its change record attached, which must be admitted, the arm red if the guard refuses it, and red on a planted agent write of every other shape, a lowered cap, two caps raised, a class row raised, a raise beside another change and a raise with neither the RAISED argument nor the decision row, each refused, the arm red if the guard admits any (M11, FM1, SA-12, the owner's FK-7-1 and FK-9-2, the closing pair's guard-no-positive-arm and change-record-undefined)
7. `cl-dClosedLoop-0013@8ae02ac2` · now `8ae02ac2`, as at the baseline · tokens: `.githooks/gate-env.sh`, `GATE_DOC_PATHS`, `GATE_POST_MERGE`, `GATE_WSL_MIRROR_DEFAULT`, `GATE_WSL_PARITY_RUNS`, `GOV_KITROOT`, `INHERITED_RED`, `INHERITED_RED_MAX_AGE`, `REVIEW_ROUNDS`, `[effort]`, `[gates]`, `tools/roles/house/policy.toml` — the legacy homes on a shrink-only list derived by query from the files they guard, never typed, red on a planted row and green on today's files: every kit conf key the retrofit does not convert, `REVIEW_ROUNDS` among them until dDeclaredLoop's retirement removes its last reader (DA-M8, FM7), every key `.githooks/gate-env.sh` assigns, documents in its header or has a reader parse from it, each marked an owner policy dConvergedCharter folds (`INHERITED_RED`, `INHERITED_RED_MAX_AGE`, `GATE_DOC_PATHS`, `GATE_WSL_PARITY_RUNS`, and `GATE_POST_MERGE`, declared and unassigned as gap-deploy-02 records) or a mechanic that stays (`GOV_KITROOT`, `GATE_WSL_MIRROR_DEFAULT`, the gate commands, the Python and the self-test switch), and `tools/roles/house/policy.toml`'s `[effort]` and `[gates]` (M4, M7, DA-M5)
8. `cl-dClosedLoop-0014@28a178b1` · now `28a178b1`, as at the baseline · tokens: none, so the token arm cannot see this clause — an arm red when a key whose Owner build has landed has no reader, its population the catalogue's Owner column joined to the builds landed on the default branch, derived from history, a reader being a call site that consumes the key's value and never this reader's own default path, seen red on a key planted with a landed Owner and no consumer and green on the same key with an unlanded Owner (H4, DA-M1)
9. `cl-dClosedLoop-0015@8ce57bfb` · now `8ce57bfb`, as at the baseline · tokens: `CODEX_MAX`, `budgets.*`, `budgets.enforce`, `budgets.pinned`, `check-spec-tokens.py`, `check-template-size.sh`, `template-size-limits.txt`, `warn` — `budgets.enforce`, the one switch every gate enforcing a size cap on a document or record reads, warning by default as the owner set it, every cap the owner names in `budgets.pinned` refusing whatever the switch says, each cap's value read from its one declaration, `budgets.*`, through the policy reader, `template-size-limits.txt` kept as a legacy home the policy reader reads until dSafePassage's step moves its rows into the key, a cap holding a value in both homes refused, a run allowed to raise a measured-file cap once its row is under the key, through dDeclaredLoop's guarded policy command, and before it lands through the one write shape the minimal guard admits, on the four conditions `template-size-limits.txt` states, which the step carries into the key's declaration beside the rows' argued history, a class row, a lowering, a new row and a removal staying the owner's (the owner's FK-7-1 and FK-9-2), and every reader of a cap re-pointed to the policy reader in the same unit, `check-template-size.sh` and `check-spec-tokens.py`'s size join among them, seen red on a planted cap held in both homes and on a planted reader still reading the file for a cap the key holds, and a limit its consumer enforces by dropping what is over, or a check of correctness, left outside it, seen on every cap the caps research lists, each planted over its cap under each value and red where one ignores the switch, a pinned cap refusing under `warn`, a pinned name outside the switch, exempt from it or matching no listed cap refused at the schema (the answers' review), and on today's consumer limit, agent-instructions' `CODEX_MAX`, left outside the switch, a planted canonical over it answered the same under each value, the load set's and the composition's refusals seen in the dOrderedCharter units that build them (the night pass two, point 5, the owner's NT-22, made a census by the night pass two's review, the whole-design audit's C1-F14, the owner's FK-1-3)
10. `cl-dClosedLoop-0016@df63b6eb` · now `df63b6eb`, as at the baseline · tokens: `.agent-cap.conf`, `AGENT_CAP`, `FANOUT_CAP`, `FANOUT_CAP=2`, `parallel`, `pipeline`, `runtime.agents-in-flight` — `runtime.agents-in-flight`, the one carrier of the agent limit, which the owner raises or lowers by a policy write, rendered into the harness's own concurrency settings for one session's direct spawns and one Workflow run, agent-cap's slot ledger, its ban on raw `parallel` and `pipeline`, the concurrency half of its bound rule and its clamp of every bound to 1 to 5 retired in the same unit with its refusal of a set `AGENT_CAP` and its print mode, their readers re-pointed to the policy reader, `.agent-cap.conf` kept as a legacy home the policy reader reads, its `FANOUT_CAP` only ever lowering the limit, until dSafePassage's step moves it into the key (P38), seen on a fixture repository whose Workflow run of four agents overlaps at most two under a limit of two, whose three background Agents never run more than two at once under that limit, the third refused, and in which, under a limit of eight, a direct spawn and a registered harness call are both admitted, the rendered settings holding both values at the key and again after a policy write raises it to six, and two concurrent Workflow runs each held to the limit, the session's total left to the in-flight ledger, and a planted `FANOUT_CAP=2` still capping at 2 under the key's default of 6 (the night pass two, point 7, the owner's NT-27 and NT-28, completed by the night pass two's review, the whole-design audit's A4-F1 and C1-F5)
11. `cl-dClosedLoop-0017@c5b54ae9` · now `c5b54ae9`, as at the baseline · tokens: none, so the token arm cannot see this clause — each loop bound and deadline key declaring that raising it is a loosening, read by the schema, seen red on a planted loop bound with no declared direction (P39)

### brief:acceptance

- At the Design exit, `carries.py --build dGroundRules --exit` exits 0 over the build's specs: each clause in Items carried whole, or in parts 1/n to n/n, at its hash; each owned node named by a spec; each clause's tokens in its carriers.
- Each clause's own seen-red cases, stated in its text, observed as it states them.
- Every departure from a clause, or from a spec after its first pass, is a deviation record that `deviations.py` joins, and the build's departures report lists it (README rule 4).

### brief:gates

- `packet.py --check dGroundRules` green before the first pass. A red on a moved instrument blob is a stop, never re-rendered away (README rule 2).
- `carries.py --build dGroundRules --exit` at the Design exit while it is in service (the execution plan's `[phase-1]` retirement table).
- The close sequence of README rule 4, then the bar the driver owes at `--close`.

### brief:non-goals

- v2, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`: frozen at the baseline, so a change to a clause is a deviation record approved by its risk.
- The 498 clauses of the other 21 chain builds' rows: carrying one needs a `**Moved:** <clause id> to dGroundRules by <decision>` line.
- Any path outside `memory/builds/dGroundRules/`, but the product paths a build run's units record with `--dispatch --writes`, an ask row in another build's `BACKLOG.md`, and the shared renders a landing re-renders (README rule 7).
- Another build's packet, the instruments under `memory/builds/dClosedLoop/build/*.py`, and this packet's pin lines: only `packet.py --repin <instrument>`, the owner's, moves a pin.
- The surfaces of dSafePassage, dOrderedCharter, dDeclaredLoop, which this build's clauses use as stand-ins only (Later builds named).

### input:spec

memory/builds/dGroundRules/prompts/2026-10-23-prompt-TOOL-dGroundRules-53-task.md

### task:reuse

read_policy_key in tools/unattended/unattended.sh:9517 is the reader clause 0008 extends; tools/template-size-limits.txt, tools/roles/house/policy.toml, .githooks/gate-env.sh and tools/hooks/agent-cap.js are the legacy homes the clauses name.

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
