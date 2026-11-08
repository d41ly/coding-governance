**Serves:** journal TOOL-dCalibratedLens-9

# gov-spec-writer handoff — TOOL-dCalibratedLens-9

<!-- gov:handoff role=gov-spec-writer build=dCalibratedLens unit=TOOL-dCalibratedLens-9 path=memory/builds/dCalibratedLens/prompts/2026-11-04-prompt-TOOL-dCalibratedLens-9-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=543dd0ed478b -->

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

This handoff is for build `dCalibratedLens`, unit `TOOL-dCalibratedLens-9`.
Not supplied, optional: `card:route`.

### brief:goal

Fold every item of that review record into the specs it touches. The verdict is CLEAN WITH FIXES:
no blocker, no high, twelve medium (M1-M12) and nine low (L1-L9). Every item's fix amends spec text
and adds no document, gate, adopter, generated artifact, verb or write path outside its unit's own
Scope. Each is therefore LOCAL under BUILD-METHOD M4's nature rule, and folds at the disposal with a
rev bump and a revision-log line naming the record and the item. Nothing is promoted, and the chain
stops here: no blocker or high, nothing promoted.

### brief:items

Read the review record first. Each item quotes its finding, its consequence and the fix a skeptic
judged sound. Its appendix carries every finding with its `ref`. Apply the fix as the item states it.
Where an item offers options, take the one this brief names below. Where the brief names none, take
the one that conforms to the cited parent text with the smaller change.

Decisions this brief makes for the items that offer options:

- **M2 (cl14):** widen `compare_path` in this build. Record a new §8 item, PRIMITIVE GAP, with the
  item's three options, marked `RESOLVED (agent, 2026-11-04, delegated)` with the in-build widening.
  The reason is the owner's rule that no plan counts on a foreign build for functionality it can fold
  in. Its rung is the one the spec's other primitive gaps carry. Add `tools/loop/adapt.py` and the
  widening to F8's `grants:`, and fix §4 "Waits on".
- **M4 (cl9):** the widened `read_act_records` reads the window's rows in one batch, so the 60 s
  bound stands as sized. If the parent text gives the door no batch read, re-derive the bound for one
  `show` per act instead, and say so.
- **M7 (cl1):** run `--trigger` only for a review breakpoint, by the parent's own review names and
  the `placement` cause. Pass `--cause` from the line's `cause` field. Also state the outcome for a
  step outside `REVIEW_STAGES`.
- **M8 (cl1):** state that a `REVIEW_STAGES` member with no literal read raises a `RolesError` naming
  the stage, and add that case to the adopt-roles arm. Add no parity gate.
- **M9 (cl10):** take option (b), cl46's and cl47's two-case form, so the three specs fold the
  `leg_factory.py` presence one way.
- **M10 (cl1):** state in S5 how `--trigger` finds `handoff.py` (inline `resolve_kit_dir`) and what
  it prints with roles absent. Add no kit edge.
- **M11 (cl1):** parse the `^REVIEW_STAGES = ` line as text. Name each failure class with its
  message, and extend AC8.
- **L5 (cl9, cl7):** re-word to the `find --all` and `show` route the owner's wm32 F6 (b) pick
  names, in both specs.

Groups, one writer each. The spec your task block's `input:spec` names leads one group. Edit only
that group's specs:

- **Group D1, led by spec 1:** specs 1 and 24. Items M7, M8, M10, M11 and L9 on cl1, and L1 on
  cl24. cl1 is 48632 bytes. No gate caps a spec's size, but keep the fold tight.
- **Group D2, led by spec 3:** specs 3, 2, 5 and 19. Items:
  - M1 on cl3.
  - M5 on cl3 and cl2, one wording in both.
  - M6 on cl5 and cl19, naming the dTotalRecall BACKLOG row filed 2026-11-03 for the record-kind
    check, ask 108.
  - L4 on cl2.
- **Group D3, led by spec 16:** specs 16, 12 and 17. Items M3, M12 and L2 on cl16, and L2's
  alignment on cl12 and cl17.
- **Group D4, led by spec 14:** specs 14, 10, 15 and 8. Items:
  - M2 and L8 on cl14;
  - M9 and L3 on cl10;
  - L6 on cl15;
  - L7 on cl8.
- **Group D5, led by spec 9:** specs 9 and 7. Items M4 and L5 on cl9, and L5 on cl7.

Each revision:

- bumps the **Status:** line by one rev, with date `2026-11-04`, leaving every other field;
- adds one §9 line in the spec's existing form: `- rev-<n> · 2026-11-04 · <sections> · the
  cross-check folds' spec audit disposed, <what moved>, by the brief
  prompts/2026-11-04-prompt-TOOL-dCalibratedLens-1-crosscheck-audit-disposal.md (review
  2026-11-04-review-TOOL-dCalibratedLens-1-crosscheck-spec-audit, items <ids>)`;
- keeps any line it moves in the parent's spelling, quoting the parent's surface names exactly;
- writes no list item or table cell that opens with another build's unit id followed by a separator,
  because hygiene check 13 reads that shape as defining the id. Lead with a word, or with the short
  alias.

Return, in this shape and nothing else:

1. One bullet per item you were given: the item id and spec, `folded`, `refused` or `parked`, the
   sections it moved, and for a refused or parked item the line that decides it.
2. One line per spec edited: its new rev and its byte count.
3. The hygiene run's command and what it printed.
4. Parent text that looks wrong, one line each with `file:line`.

### brief:acceptance

- Each edited spec's **Status:** line carries its new rev, and §9 holds the new line.
- For each item you fold, the text the item quotes as the defect no longer stands: a `grep -n` of the
  quoted phrase, or a re-read of the section where the phrase was a paraphrase.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs over a copy of the index with only
  your group's specs staged into it through `GIT_INDEX_FILE`, and names nothing of your specs. Delete
  the copy after. Findings that only a `gen_build_index.py --write` render cures belong to the main
  loop: name them and leave them.

### brief:gates

Only the memory hygiene gate, as the role allows. The main loop runs the rest and renders the index.

### brief:non-goals

- No file outside your group's specs. No commit, no stage into the real index, no deviation record,
  no BACKLOG row: the main loop writes those.
- No file of any parent or ancestor build.
- No item outside your group, no new unit, and no change beyond what the item's fix states.
- No owner-resolved §8 mark changed.

### input:spec

memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-9.md

### task:reuse

the precedent cross-check shape (memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md, commit 9b3ace4c7); tools/roles/handoff.py render/agents.

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
