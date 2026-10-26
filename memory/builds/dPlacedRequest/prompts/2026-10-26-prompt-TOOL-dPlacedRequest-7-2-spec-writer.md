**Serves:** journal TOOL-dPlacedRequest-7

# gov-spec-writer handoff — TOOL-dPlacedRequest-7

<!-- gov:handoff role=gov-spec-writer build=dPlacedRequest unit=TOOL-dPlacedRequest-7 path=memory/builds/dPlacedRequest/prompts/2026-10-26-prompt-TOOL-dPlacedRequest-7-2-spec-writer.md role-sha=06b14b1ac42a task-sha=7f03851933f3 -->

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

This handoff is for build `dPlacedRequest`, unit `TOOL-dPlacedRequest-7`.
Not supplied, optional: `card:route`.

### brief:goal

Revise the 10 dPlacedRequest specs that the cross-check record names under "For the re-ground". Each
one should state dDeclaredLoop's and dOrderedCharter's surfaces the way their specs now spell them:
dDeclaredLoop at its re-ground commit `783f1ad3a`, and dOrderedCharter at `462d20f35`. Each spec keeps
its own design, and only its assumptions about the two parents change.

### brief:items

Read the cross-check record first,
`memory/builds/dPlacedRequest/build/2026-10-26-build-TOOL-dPlacedRequest-1-parents-crosscheck.md`.
Its summary table numbers every assumption (rows 1 to 80), and "The mismatches, both sides quoted"
gives both sides of each MISMATCH. Read each parent spec the record cites, at the lines it cites. This
brief summarises them, and where the two differ, the specs win. Before you edit for a row, re-read
both sides. A row the parent's text does not bear out is not edited: return it as refused, with the
line that refutes it.

Facts every revision uses:

- **A typed record kind.** dOrderedCharter unit 42 S2 makes `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the record factory's kind list. `build_records.py` refuses at import
  any kind table that differs from it (oc42:40-44). Under S3, a `-<kind>-<n>.md` file whose Serves
  kind is not `<kind>` is malformed (oc42:45-49). S5 keeps the closed kind list in
  `tools/memory-tree/HYGIENE.template.md`. A unit that adds a kind adds it to all three in its own pass,
  and its records serve as `<kind> <id>`. One criterion observes the record bind:
  `gen_build_index.py --print-bindings` names it. dDeclaredLoop's specs 3 and 17 read this way at
  rev-3: copy their wording.
- **The record factory's door.** dDeclaredLoop's spec 16 at rev-3 claims no `new disposition` verb. A
  writer passes the factory `--build <slug> --unit <id> --item <tag> --disposition <word>
  --channel <channel>`, and the build run re-grounds the call on the landed factory (dl16:52-56). The
  same holds for every kind: name the flags, and claim no door.
- **A new leg's `enforces`.** dOrderedCharter unit 7 S3 reds a leg with no `enforces`, and the
  pending list only shrinks (oc7:58-63, :228). dDeclaredLoop's re-ground gave each of its new legs
  `enforces` with the principle whose v2 `[enforcement]` row names the unit's clause. It writes a §8
  fork where no row names it (dl3 F7). Do the same.
- **dDeclaredLoop's program rules.** At `783f1ad3a`:
  - An item's outcome set is a closed list or the reference `dispositions` (dl12:39-40).
  - The loop check prints `unarmed` and passes when the playbook kit is absent (dl12:50-52, AC7).
  - Its one inline `resolve_kit_dir` block is in `loop_lib.py` (dl12:53-56).
  - dl33's `counted` rule sets aside only counted edges and owner edges (dl33:50-56).
  - dl3 S2 reads the transition channels from `transitions.record` (dl3:52-58).
- **The overlay.** dOrderedCharter unit 32 S1 reads the overlay at the landed revision, never the
  working tree (oc32:49). An overlay edit stales the policy mirror, which the landing regenerates or a
  second commit writes with `policy.py mirror --write` (oc32:84-90, :271-273). Unit 36 S4 reads a key
  as tag-valued when its row's `allowed` is a table whose `type` is `set`, `list` or `name`, and v2's
  `none` for a set is `[]` (oc36:59, :183).
- **An ask.** No dPlacedRequest spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every
spec of that group, and no other:

- **Group A, loop rows and records, led by spec 3:** specs 1, 2, 3, 4 and 5.
- **Group B, probes, claims and the overlay, led by spec 7:** specs 6, 7, 9, 21 and 34.

The spec files are `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-<n>.md`.
Write probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-amazing-roentgen-42b269/e5868d60-4c6d-4ccd-a640-f987e8390bd7/scratchpad/pr-w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and
any parent spec that looks wrong.

Per spec, by the record's rows:

1. **Spec 1** (row 2). S8 and §4's witness under `progress` read through dl3 S7's
   `read_transitions(build, repo)`, or through the log record where `trailer` is not selected. Add a
   criterion case with `transitions.record` planted to `["log"]`.
2. **Spec 2** (row 5). The `card` record serves as `card <anchor id>`, joined to `TYPED_RECORD_KINDS`
   and the HYGIENE kind list, with the binding criterion. Name no `new card` door.
3. **Spec 3** (rows 13, 15, 20, 22).
   - `item.entry.place` types its outcomes as the nine words plus `probe`, with AC3 checking that
     list, or drops `probe` and says where its probe route lives.
   - The owner row's witness names the factory's flags, not a `new disposition` verb.
   - §3 states that dl24's `[[fixed-row]]` trigger names dPlacedRequest while dWellOiledMachine
     declares `entry.intake`, and writes the fork for who owns that fixed row.
   - The `awaiting` self-route gains a `draws` cause, or the fork for an ask that dl33 set aside an
     edge carrying `deadline`. AC6 gains the matching case.
4. **Spec 4** (row 31). The leg `loop placement fixtures` carries `enforces`, observed by a criterion.
   Specs 5 and 10 ride the same leg.
5. **Spec 5** (row 32). S4, §4's flow and §10 name the factory's flags for the declaration, not a
   `new disposition` verb, and AC4 re-grounds on the landed factory.
6. **Spec 6** (row 39). S3 and AC4 state which rule wins when the playbook kit is absent, named
   against dl12 AC7: the namespace arm reds only when a row declares `unfolds`, or it follows dl12's
   unarmed-but-passing rule.
7. **Spec 7** (rows 45, 46, 48).
   - `probe.points`' catalogue row takes `allowed` as a `{ type = "set", … }` table with default `[]`.
   - The `probe` and `probe-trigger` kinds join `TYPED_RECORD_KINDS` and the HYGIENE kind list, and
     serve as their own kinds, with the binding criterion. Files touched gains `tree_lib.py`, the
     HYGIENE template and `memory/HYGIENE.md`.
   - The leg `loop probe fixtures` carries `enforces`.
8. **Spec 9** (rows 58, 59). Files touched and §4 Migration name `.governance/policy.json`,
   regenerated in its own commit after the step's commit, or state that the landing regenerates it.
   AC1's and AC3's plants commit `up`'s write before `pockets` runs, and S3 states that `pockets`
   shows units only once their commit is `HEAD`.
9. **Spec 21** (rows 73, 78).
   - S6 states the unit id the ratification record carries before the patch build has a spec, or
     moves the ratification after the first spec exists.
   - The leg `loop claim fixtures` carries `enforces`.
   - AC1's plant writes the record as `disposition <unit id>`.
10. **Spec 34** (row 80). AC34 says S34's point: no `tools/loop/` module but `loop_lib.py` names
    `resolve_kit_dir` for a memory-tree module. Its grep narrows to `resolve_kit_dir("memory-tree"`,
    or lists the expected hits. S31's leg list gains `enforces` for `loop placement fixtures` and
    `loop claim fixtures`. It is at 48198 bytes, so replace text and do not append.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-26, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record, with its row numbers.
- Replace each now-false sentence where it stands.
- A resolved fork whose chosen option a parent now rules out is re-resolved on rung 1, naming the
  parent, and marked `RESOLVED (agent, 2026-10-26, delegated)`. A fork this brief tells you to leave
  open for the owner stays open, with its recommendation. Re-open no other fork.
- Spell a `tools/` path inside an acceptance criterion as the spec already does.
- Stay under the class cap of 49152 bytes.

### brief:acceptance

- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `prN:L`
  prints nothing, or prints only the corrected sentence.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures belong to the main loop:
  name them and leave them.

### brief:gates

Only the memory hygiene gate and the naming lexicon, as the role allows. The main loop runs the rest
and renders the index.

### brief:non-goals

- No file outside the spec files of your group. No commit, no stage into the real index, no
  deviation record: the main loop writes those.
- No file of dDeclaredLoop, dOrderedCharter, dSafePassage or dGroundRules. A parent spec that looks
  wrong is a line in your return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### input:spec

memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md

### task:reuse

the dOrderedCharter re-ground (`555e623a7`, its brief `memory/builds/dOrderedCharter/prompts/2026-10-24-prompt-PLAY-dOrderedCharter-1-parents-reground.md`) and the dSafePassage cross-check record as the precedent; `tools/roles/handoff.py render|agents` for handoffs and the ledger; `bash tools/push-main.sh --prepare|--land` for landing.

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
