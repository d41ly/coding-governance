**Serves:** journal TOOL-dPavedRoad-2

# gov-spec-writer handoff — TOOL-dPavedRoad-2

<!-- gov:handoff role=gov-spec-writer build=dPavedRoad unit=TOOL-dPavedRoad-2 path=memory/builds/dPavedRoad/prompts/2026-11-10-prompt-TOOL-dPavedRoad-2-3-spec-writer.md role-sha=7382e69776f4 task-sha=553d4ba3d5c4 -->

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
- You may run the memory hygiene gate and the naming lexicon over your specs, and, where this
  repository has it, `python tools/check-spec-tokens.py --spec <path>` over each spec you wrote,
  fixing every hit it names before you return. You run no other gate.
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

This handoff is for build `dPavedRoad`, unit `TOOL-dPavedRoad-2`.

### brief:goal

DIVERGENCE: spec section 4, "Rollout", says `tools/gate-legs.json` is watched by the kickoff manifest and that "its re-audit falls to the main loop at the close. This pass does not do it." But S6 makes this pass edit `tools/gate-legs.json`, and the pre-commit hook refuses that commit. The refusal is `skills/session-kickoff/manifest-check.sh` check 5, staged leg, around lines 1776-1790. It reads: "staged changes touch watched files: tools/gate-legs.json but the staged manifest's audit block does not update last-audit … bundle the re-stamp into THIS commit". The code's own comment calls the bundle "the only green path here". So a pass that ships S6 cannot also leave the re-audit to the close. The only ways through are a re-stamp of `memory/guides/SESSION-KICKOFF.md`'s manifest-audit block, which the spec forbids and which is outside this unit's Files touched, or `--no-verify`, which would route around the refusal.

To fix it, the spec must say one of two things:
(a) The pass re-verifies the section-B claims fed by `tools/gate-legs.json` and bundles the `last-audit` re-stamp into its build commit. Then `memory/guides/SESSION-KICKOFF.md` joins Files touched and the Rollout sentence is removed.
(b) S6 leaves this unit for one that the close or a follow-up commits together with the re-stamp.

The same commit also needs `memory/builds/dPavedRoad/README.md` re-rendered with `python tools/memory-tree/gen_build_index.py --write`. The hook reported it as DRIFT once the CLOSED flip was staged. That file is generated, and Files touched should list it.

### brief:items

1. **TOOL-dPavedRoad-1 — writers self-check spec tokens.** `tools/check-spec-tokens.py --spec <path>` grades that one spec as if it were live, whatever its status, and `tools/roles/house/policy.toml` adds the spec-tokens leg to `gov-spec-writer`'s gates. About 17 of dSafePassage's 37 corrections to agents were "fix spec-token hits" that a writer could not see, because the role may not run the checker and the checker grades no DEFERRED spec.
2. **TOOL-dPavedRoad-2 — format-guard prints the lines it wants.** `tools/hooks/format-guard.js`'s block message includes, verbatim, the `agent`/`returned` lines `handoff.py agents` derives for each agent it names, and the `committed` line for each new commit it names. About 33 turn ends were refused for those lines, each costing a re-send.
3. **TOOL-dPavedRoad-3 — the handoff carries the brief's prompt.** `tools/roles/handoff.py` renders the brief's `## The prompt` into the Task section as a `brief:prompt` field. Three writers needed the finding, its log path or the owner's ruling sent separately by SendMessage, because the Task section dropped it.
4. **TOOL-dPavedRoad-4 — `--staged` grades the staged joins.** `tools/memory-tree/check-memory-hygiene.sh --staged` grades check 12's edge reciprocity and check 23's ledger joins for the staged specs and ledgers only. Both are held under `--staged` today, so 6 one-way edges and 10 unjoined ledger lines surfaced only at the close and cost two adopted units.

### brief:acceptance

Each unit's own probe: (1) a spec holding a known false-positive token reds under `--spec` while DEFERRED, and the role allowlist admits the leg; (2) a Stop payload missing an agent line yields a block message containing that agent's exact derived line; (3) a rendered handoff's Task section holds the brief's prompt; (4) a staged spec with a one-way edge and a staged ledger with an unjoined line each red under `--staged`, and an unstaged one does not.

### brief:gates

`bash tools/run-gates/run-gates.sh`, legs from `tools/gate-legs.json`.

### brief:non-goals

No change to what any check grades on the full run; no change to the spec-audit policy, the dispatch order gate, the packet regen or the manifest ratchet; no new role.

### input:spec

memory/builds/dPavedRoad/spec/2026-11-10-spec-TOOL-dPavedRoad-2.md

### task:reuse

check-spec-tokens' live-spec walk; format-guard.js's defect list and `handoff.py agents`; handoff.py `extract_task_fields`; check-memory-hygiene.sh's `--staged` selection.

### card:route

- build: dPavedRoad
- unit: TOOL-dPavedRoad-2 · spec memory/builds/dPavedRoad/spec/2026-11-10-spec-TOOL-dPavedRoad-2.md
- brief: memory/builds/dPavedRoad/prompts/2026-11-10-prompt-TOOL-dPavedRoad-1-brief.md

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
