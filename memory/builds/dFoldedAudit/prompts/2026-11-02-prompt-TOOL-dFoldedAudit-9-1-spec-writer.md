**Serves:** journal TOOL-dFoldedAudit-9

# gov-spec-writer handoff — TOOL-dFoldedAudit-9

<!-- gov:handoff role=gov-spec-writer build=dFoldedAudit unit=TOOL-dFoldedAudit-9 path=memory/builds/dFoldedAudit/prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=44c20116b151 -->

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

This handoff is for build `dFoldedAudit`, unit `TOOL-dFoldedAudit-9`.
Not supplied, optional: `input:spec`.

### brief:goal

Resolve every open fork in units 9 and 15, carry the flagged seams, and cross-read the seven specs so none disagrees with another before the first build pass. The writers' returns are at `memory/builds/dFoldedAudit/build/2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md`. Commit nothing; the main loop commits.

### brief:items

1. TOOL-dFoldedAudit-9 §8: F1 RESOLVED to (a), F2 RESOLVED to (a). The main loop has already parked F2's decision row. Mark each `RESOLVED (agent, 2026-11-02, delegated)` in the shape `memory/TEMPLATE-SPEC.md` states.
2. TOOL-dFoldedAudit-15 §8: F1 is the FACT-QUESTION, RESOLVED to (c) by its stated probe. F2 RESOLVED to (b). F3 RESOLVED to (a), overruling that spec's recommendation: the owner-accepted brief's item 1 names M4's text, `tools/unattended/VERBS.template.md` and the protocol as this build's carriers, so aligning them is its stated change and M3's veto 2 does not reach them. Rewrite §3 and §4 to (a).
3. As a result unit 15 also writes, in its one batch: the `--record-round` refusal list in `tools/unattended/VERBS.template.md` and its render, gaining units 11 and 15's changes; the `--plan` bullet unit 13 left; `rev` in the `/build` Skill; and M4's first verdict test in `tools/memory-tree/BUILD-METHOD.template.md` and its render, so it states the case unit 10 adds. M4 stands at 30565 of 30720 bytes; measure the render and stay under. Add `memory/guides/SESSION-KICKOFF.md` to its write set. Turn units 11 and 13's `hands-off external` lines for these into `hands-off` edges to unit 15. M6's `--dispatch` sentence stays parked and is not written.
4. TOOL-dFoldedAudit-14's Edges line reads `hands-off external` while naming TOOL-dFoldedAudit-9. Make it `hands-off` so the pair joins.
5. TOOL-dFoldedAudit-10's fixture C and TOOL-dFoldedAudit-11's fixture R declare no cutoff, and unit 13 ships first and refuses `local` and `--sibling` rows under a blank cutoff. Give each fixture conf `SPEC_FOLD_CUTOFF="2000-01-01"`. Unit 11's `write_chain_fixture` move to rev-3 stays as its spec says.
6. `tools/check-spec-tokens.py` reports TOOL-dFoldedAudit-10: Files touched names `tools/unattended/lib-unattended.sh`, which trips the guard of leg `routed-commits selftest`, absent from §7. Add the leg. Then check every sibling touching that file the same way.
7. Accept TOOL-dFoldedAudit-14's F1 as written; no change.
8. Run M2's cross-read over the seven specs on its four axes. Fix each disagreement in exactly ONE spec, rev bump and §9 line naming what disagreed.

### brief:acceptance

Every folded spec carries a rev bump and a §9 line, and the return lists each by rev with each axis's result. `unattended.sh --plan dFoldedAudit` reads READY for all seven once committed.

### brief:gates

`tools/check-spec-tokens.py`, run by the main loop after this pass. Hygiene checks 5, 12 and 25 in a scratch clone.

### brief:non-goals

A choice beyond these rulings is reported, not decided. No code, no write outside this build's `spec/`.

### task:reuse

verb_review, the DISPOSAL stage, check 2's awk with a third cutoff, deviation_join.scan, derive_past_pin_ids.

### card:route

- build: dFoldedAudit
- unit: TOOL-dFoldedAudit-14 · spec memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-14.md
- unit: TOOL-dFoldedAudit-13 · spec memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-13.md
- unit: TOOL-dFoldedAudit-10 · spec memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-10.md
- unit: TOOL-dFoldedAudit-11 · spec memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-11.md
- unit: TOOL-dFoldedAudit-9 · spec memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-9.md
- unit: TOOL-dFoldedAudit-12 · spec memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-12.md
- unit: TOOL-dFoldedAudit-15 · spec memory/builds/dFoldedAudit/spec/2026-11-02-spec-TOOL-dFoldedAudit-15.md
- brief: memory/builds/dFoldedAudit/prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md

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
