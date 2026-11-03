**Serves:** journal TOOL-dTotalRecall-1

# gov-spec-writer handoff — TOOL-dTotalRecall-1

<!-- gov:handoff role=gov-spec-writer build=dTotalRecall unit=TOOL-dTotalRecall-1 path=memory/builds/dTotalRecall/prompts/2026-11-03-prompt-TOOL-dTotalRecall-1-1-spec-writer.md role-sha=dcd8416ea3d2 task-sha=858755bcea7f -->

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

This handoff is for build `dTotalRecall`, unit `TOOL-dTotalRecall-1`.
Not supplied, optional: `card:route`.

### brief:goal

TOOL-dTotalRecall-2 stops asking dPlacedRequest for a new holder verb. It reads the build lease's
holder through the read-only verb TOOL-dPlacedRequest-34 S22 already specs. TOOL-dTotalRecall-1 stops
promising a door its sibling never registers. Nothing else in either design changes.

### brief:items

Items 1-4 revise spec 2, `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-2.md`.
Item 5 revises spec 1, `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md`.

1. **§8 F6's resolution.** S22 specs `unattended.sh --lease status <kind> <name> [<sub>]` as
   read-only. It prints one TAB line, `<tail> <fleet tag> <session> <status> <verdict> <epoch>`, or
   `lease — none · <tail>` (`dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md:106-109`,
   with AC22 at `:468-470`). That covers three of the four fields F6 (a) asks a new verb for:
   `fleet-tag`, `session` and `epoch`. It lacks one, the `lease`-mode class, `mine` or foreign.
   Re-mark F6 `RESOLVED (owner, 2026-11-03): (a), served by TOOL-dPlacedRequest-34 S22's --lease
   status`, keeping the 2026-11-02 pick's history in a clause after the mark. Then change the fork's
   last paragraph in three ways:
   - The holder verb is S22's `--lease status build <slug>`.
   - The ask narrows to one column: a seventh TAB field holding the `lease`-mode class (`mine` or
     foreign, TOOL-dPlacedRequest-1:90-92), appended after `<epoch>`. The six-field prefix stays as
     it is, because `read_lease_epoch` (DEPL-dShippedRelease-138 S48) reads the sixth field.
   - Replace the row text the build run files with: "a seventh TAB field on TOOL-dPlacedRequest-34
     S22's `--lease status`, the lease's `lease`-mode class (`mine` or foreign), the six-field prefix
     kept".

   Keep the rest of the fork's content as it reads now: one ask, filed once by this build's run,
   serving TOOL-dWellOiledMachine-58 S4 (c) and S5, TOOL-dWellOiledMachine-41 S2's driver check, and
   TOOL-dWellOiledMachine-6 S6 and S7. The `widens:` value changes from the verb's `epoch` field to
   the `--lease status` class column.
2. **F6's served-sections list.** tr2:352 says the ask "serves this unit's S2 and S9". Neither reads a
   lease: S2 reads the kind's row and S9 rewrites registry `writer` cells. The lease read is S6, by §4
   "Minting". Re-point the clause to S6 and §4 "Minting".
3. **§4 "Minting" and §3's external edge (lines 129-131 and 193-194).** Both describe the holder as
   read "through the read-only holder verb §8 F6 (a) asks dPlacedRequest for". Change both to read
   through TOOL-dPlacedRequest-34 S22's `--lease status build <slug>`, §8 F6's pick. "Minting" keeps
   its four named fields; the class is the column F6 asks for. Keep every other sentence of the
   authority rung, including the `--claims` reasoning and the remote fetch.
4. Fix any other sentence in spec 2 that names a new holder verb, so it reads as item 1 decides.
   Leave the forks of TOOL-dTotalRecall-18 and -20 alone: their "F6 (a)" is a different fork.

5. **tr1:193-194.** "`hand` is legal until TOOL-dTotalRecall-2 registers a door" contradicts
   TOOL-dTotalRecall-2 S9. S9 moves only `fields`-form `hand` rows onto `gov_record.py new <kind>`.
   A `hand` row of any other form keeps `hand`, and the pass names its door's owner in a `Decided:`
   trailer. Restate the rule so `hand` stays legal for any row S9 does not move, and drop "until".
   The cross-check that found this is
   `memory/builds/dMindYourWords/build/2026-11-03-build-TOOL-dMindYourWords-1-parents-crosscheck.md`
   (row 2, where TOOL-dMindYourWords-11 rev-3 already reads tr2 S9 that way).

### brief:acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads the new rev, and §9 holds the new line.
- Spec 2: `grep -n "asks dPlacedRequest for" <spec>` prints no line of §3 or §4.
  `grep -n "this unit's S2 and S9" <spec>` prints nothing. `grep -n -- "--lease status" <spec>`
  prints lines in §3, §4 and §8 F6.
- Spec 1: `grep -n "until TOOL-dTotalRecall-2 registers a door" <spec>` prints nothing.
- Run `bash tools/memory-tree/check-memory-hygiene.sh --staged` over a copy of the index with only
  your spec staged into it through `GIT_INDEX_FILE`. It names none of your spec's lines. A finding
  that only a `gen_build_index.py --write` render cures belongs to the main loop: name it and leave it.

### brief:gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### brief:non-goals

- No file outside your one spec. No commit, no staging into the real index, no deviation record and
  no `BACKLOG.md` row: the main loop writes those, and the build run files the ask.
- No edit to TOOL-dPlacedRequest-34 or any other dPlacedRequest spec. The column is an ask, not a
  revision of S22.
- No change to what either unit builds beyond the surface the holder is read through.

### input:spec

memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md

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
