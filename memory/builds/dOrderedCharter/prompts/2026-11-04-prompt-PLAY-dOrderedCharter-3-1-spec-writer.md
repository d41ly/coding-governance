**Serves:** journal PLAY-dOrderedCharter-3

# gov-spec-writer handoff — PLAY-dOrderedCharter-3

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-3 path=memory/builds/dOrderedCharter/prompts/2026-11-04-prompt-PLAY-dOrderedCharter-3-1-spec-writer.md role-sha=07ad6a5d06b8 task-sha=e2301f3b6917 -->

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
- Verify every claim about current code by reading that code, and cite it by `path#symbol` or the
  blob-pinned line `<path>@<oid>:<n>`. A claim you did not verify is a claim you do not make.
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

This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-3`.

### brief:goal

Revise spec 3 so the unit builds with fork F5 still open: BUILD-METHOD's envelope is held, its row and its prose stay untouched,
and the hold is visible, never read as coverage.

### brief:items

1. **Where you write.** A unit is building in the tree, so edit only this scratch copy:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold5/2026-10-23-spec-PLAY-dOrderedCharter-3.md`. Its base is the tracked spec at rev-7. Write nothing under the repository.
2. **F5 stays OPEN.** Its options, vetoes and recommendation stay. Add the run's interim ruling under it, recorded as an interim,
   never as the fork's resolution. The owner's choice among (a) to (e) stays theirs.
3. **The hold.** `memory/guides/BUILD-METHOD.md` keeps its registry row and carries no envelope.
   - Its source `tools/memory-tree/BUILD-METHOD.template.md` and its row in `tools/template-size-limits.txt` are unchanged by this unit.
   - The row declares the hold, in a field the reader validates. Pick the shape by the fork rule, and record the loser in section 8.
4. **The gate states it.** Every `envelopes --check` run prints the held path and that it is NOT checked, and its count of
   covered documents leaves the held one out. Say in the spec what the gate does not check, because a skip is never coverage.
5. **The hold retires itself.** The gate reds, naming the path, when any of these holds:
   - the held document carries an envelope;
   - the document plus its envelope now fits its row, so the owner has moved it;
   - a second row declares a hold.

   One commit then lands the owner's ruling: the row's move, the envelope, and the hold's deletion. Say so.
6. **Every clause that reads the old state moves with it.** At least S2, S5, S6, S7, section 3's Edges where needed, section 4's
   Inventory, section 5's risks, AC1, AC4, AC5 and AC7, and the sentence ending F5 that says the unit does not build. Add the
   planted cases to `tools/playbook/instruction_units.py#PLANTS`, and an acceptance bullet with its Red when line for each red
   in item 5.
7. **Downstream readers.** Read specs 2, 4, 5, 8, 29 and 49 for anything assuming every registered row carries an envelope. Do not
   edit them. Name each one affected in your return, with what it assumes.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-04, with the status kept `DEFERRED`.
- Add one history line naming this brief, with the S and AC ids it touched.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance
  bullets. An acceptance bullet spells a plain tracked path, with no `#` and no `HEAD:` prefix.
- New text names a section in words, and names a check by what it checks.
- Avoid retirement words in section 2, or add the Readers clause they owe.

### brief:acceptance

- The scratch copy's rev is 8, F5 still reads OPEN, and the interim is recorded under it.
- Nothing in the scratch copy has the unit moving BUILD-METHOD's row, source or prose.
- Each red in item 5 has an acceptance bullet and a named plant.
- `python tools/memory-tree/check-spec-tokens.py` semantics hold for new tokens: plain tracked paths in acceptance bullets.

### brief:gates

None run: this is a scratch edit. The main loop live-sweeps the spec before its dispatch.

### brief:non-goals

- No raise, no trim, and no decision among F5's options.
- No edit outside the scratch copy.
- No code.

### input:spec

memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-1 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-1.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-1-build-brief.md

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
