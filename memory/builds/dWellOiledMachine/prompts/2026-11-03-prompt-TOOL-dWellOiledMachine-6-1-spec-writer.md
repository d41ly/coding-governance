**Serves:** journal TOOL-dWellOiledMachine-6

# gov-spec-writer handoff — TOOL-dWellOiledMachine-6

<!-- gov:handoff role=gov-spec-writer build=dWellOiledMachine unit=TOOL-dWellOiledMachine-6 path=memory/builds/dWellOiledMachine/prompts/2026-11-03-prompt-TOOL-dWellOiledMachine-6-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=daf4a78dfcbe -->

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

This handoff is for build `dWellOiledMachine`, unit `TOOL-dWellOiledMachine-6`.
Not supplied, optional: `card:route`.

### brief:goal

TOOL-dWellOiledMachine-6 reads the build lease's epoch through the surface tr2 F6 now picks, cites
that fork by name rather than by line, and names the surface on its consumes-from edge. S6 and S7
keep their design.

### brief:items

All in `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-6.md`.

1. **§8 F4's citation.** F4 cites tr2 F6 as `tr2:337-354`. F6 now runs from line 340 and moves again
   with tr2's rev-8. Cite it as `TOOL-dTotalRecall-2 §8 F6` with no line range. Restate F4's last
   sentence so the verb that serves F4 is TOOL-dPlacedRequest-34 S22's `--lease status build
   <slug>`. That verb already prints `<epoch>` as its sixth TAB field, and tr2 F6 picked it on
   2026-11-03. Keep F4's `RESOLVED (owner, 2026-10-29)` mark as it reads. This build still files no
   epoch row of its own.
2. **S6 and S7 (lines 97-109).** "the holder verb TOOL-dTotalRecall-2 §8 F6 (a) picked" stays true.
   Name `--lease status`'s sixth TAB field as the epoch S6 compares and S7 re-reads each beat. S7
   still reads fleet tag and status through `--claims`, unless `--lease status` already carries both
   in one read. If it does, say so in the return and leave S7's `--claims` read as it is: changing it
   is a design change, and this pass makes none.
3. **The consumes-from external edge (line 179).** "the epoch read §8 F4 asks for" names no surface.
   Make it "TOOL-dPlacedRequest-34 S22's `--lease status`, the holder verb TOOL-dTotalRecall-2 §8 F6
   picked, for the lease's epoch". Keep it inside that one external bullet. Add no new edge bullet to
   a unit id: that would need a mirror in dPlacedRequest, and this pass edits no dPlacedRequest spec.

### brief:acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-6`, and §9 holds the new line.
- `grep -n "tr2:337-354" <spec>` prints only the rev-5 line in §9, which is history.
- `grep -n -- "--lease status" <spec>` prints lines in §2, §3's edge and §8 F4.
- Run `bash tools/memory-tree/check-memory-hygiene.sh --staged` over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`. It names none of your spec's lines. A finding
  that only a `gen_build_index.py --write` render cures belongs to the main loop: name it and leave it.

### brief:gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### brief:non-goals

- No file outside spec 6. No commit, no staging into the real index and no deviation record.
- No edit to TOOL-dWellOiledMachine-58 or -41. Both cite tr2 F6 (a) by name, so the pick reaches them
  through that one fact.
- No edit to any dTotalRecall or dPlacedRequest spec.

### input:spec

memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-6.md

### task:reuse

memory/builds/dWellOiledMachine/build/2026-10-28-build-TOOL-dWellOiledMachine-1-parents-crosscheck.md and its prompts (the record and brief shapes); tools/roles/handoff.py render and agents (handoffs and ledger lines); tools/memory-tree/gen_build_index.py --write (indexes).

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
