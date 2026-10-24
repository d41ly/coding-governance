**Serves:** journal PLAY-dOrderedCharter-32

# gov-spec-writer handoff — PLAY-dOrderedCharter-32

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-32 path=memory/builds/dOrderedCharter/prompts/2026-10-24-prompt-PLAY-dOrderedCharter-32-1-spec-writer.md role-sha=06b14b1ac42a task-sha=df73786e4399 -->

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

This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-32`.
Not supplied, optional: `card:route`.

### brief:goal

Revise the 27 dOrderedCharter specs that the cross-check record names under "For the build run's
re-ground", so each one names dSafePassage's and dGroundRules' surfaces the way their landed specs
spell them. Each spec's design stays its own; only its assumptions about the two parents change.

### brief:items

Read the cross-check record first,
`memory/builds/dOrderedCharter/build/2026-10-24-build-PLAY-dOrderedCharter-1-parents-crosscheck.md`.
Its summary table numbers every assumption (rows 1 to 52), "The mismatches, both sides quoted" gives
both sides of each with `file:line`, and U1 to U9 are parent surfaces no spec names yet. The parents'
specs are under `memory/builds/dSafePassage/spec/` and `memory/builds/dGroundRules/spec/`. Read each
unit the record cites at the lines it cites: this brief summarises them, and the specs win where the
two differ.

Facts every revision uses:

- **The policy reader.** `python <prefix>/policy/policy.py get <key> [--rev <rev>] [--explain]`
  (dGroundRules unit 2, S7). It reads the committed revision, by default the landed one (the remote
  ladder's `<remote>/<branch>`, else the local branch), and `HEAD` only with `--rev HEAD`; it never
  opens the working tree (unit 2, S1 and S2). An unset key answers the catalogue default with its
  reason (unit 3, S2). A row whose default is `{ derived = "..." }` refuses, exit 2, "a derived default
  no reader computes yet", and the mirror omits it (unit 21, S12 and F4). An invalid file falls back
  whole to its last valid revision (unit 4, S5). The chain lands dGroundRules' build run before this
  build's, so no "until the reader lands" fallback is ever reached: delete that wording and any code
  it implies, and say instead what the unit does on the reader's exit 2.
- **Kits.** A kit may not import a sibling kit (dGroundRules unit 1, `:105-106`). Code under
  `tools/playbook/` or `tools/roles/` runs `policy.py get` as a subprocess, finding the policy kit
  through its inlined `resolve_kit_dir` (`tools/playbook/render_playbook.py:78-79`). A module under
  `tools/govkit/` calls `govkit.read_policy_value(key, root)`, which dSafePassage specs 6 and 9 define
  once in `govkit.py` (dSafePassage unit 9, `:154-158`), with `root` the tree whose committed policy
  is read: the target's when the choice is the adopter's.
- **The catalogue.** `tools/policy/catalogue.toml` already holds one `[[key]]` row per v2
  `[policies]` row, owner included (dGroundRules unit 1, S3). Every one of dOrderedCharter's 16 keys
  (`charter.override`, `charter.practices`, `core.bypass`, `core.exceptions`, `instructions.checks`,
  `instructions.edit`, `instructions.proof`, `instructions.exclude`, `instructions.stale`,
  `instructions.legacy`, `tags.slice`, `tags.retired-cites`, `tags.positional`, `tags.bare-refs`,
  `tags.bundle`, `tags.bundle-rows`) lands there with no `summary` and no `usage`, named on the
  shrink-only `tools/policy/unsummarised-keys.txt` (unit 1, S6). The unit that reads a key fills that
  row's `summary` and `usage` (a `usage` line its row admits) and drains the name in the same commit
  with `python <prefix>/policy/policy.py lists --write`. It never adds a row. A catalogue edit stales
  the mirror, so `policy.py mirror --write` lands in a second commit, as dSafePassage specs 6, 9, 11
  and 13 now say.
- **Reader coverage.** Once every dOrderedCharter spec is terminal, each of the 16 keys needs a reader
  in tracked code in one of two shapes: in `.py` or `.js`, a call whose first argument is the key as a
  string literal, `ident("key"`; in `.sh` or under `.githooks/`, `policy.py get <key>` (dGroundRules
  unit 8, the Readers table). `.toml` files are not scanned.
- **Caps.** `tools/template-size-limits.txt` leaves gov in dSafePassage unit 1's commit: every row
  moves under `[budgets]` in `.governance/policy.toml`, the four raise conditions above the table and
  each row's comment above its key (dSafePassage unit 1, S7 and S8). A cap is read with
  `python <prefix>/policy/budgets.py resolve <cap>[=legacy:<n>|=default:<n>]`, named as the census
  `tools/policy/caps.toml` names it: `AGENTS.md`, `coding-governance-agents.template.md`,
  `skills/session-kickoff/SKILL.md`, `memory/builds/*/spec/`, `role-body` (a family cap: the enforcer
  asks only its mode), `one-line-rule`, `codex-instructions` (class `consumer`, home `CODEX_MAX`)
  (dGroundRules unit 9, S1, S2 and the Inventory). In the policy file a path-named cap is quoted:
  `"AGENTS.md" = 20480`. A `budgets.<cap>` with no census row is refused (unit 9, S4), and
  `arm_cap_census` joins the census to the tree both ways (unit 9, S7).
- **The minimal guard.** gov's pre-commit only, over `.governance/policy.toml`, `.governance/policy.json`,
  `.governance/instructions.toml` and `.governance/deploy.toml` (dGroundRules unit 6, S1). It admits an
  agent's commit when no guarded blob changed, or for one shape: one `budgets` leaf raised, a
  `RAISED <old> -> <new>` comment directly above it, and a `memory/DECISIONS.md` row added (unit 6,
  S3). The owner's proof is `[ -t 2 ]` written inline in `.githooks/pre-commit` (unit 6, S4 and F3);
  no callable implementation exists. The lander never fires pre-commit (unit 6, `:105-107`), so a step
  walked in the prepared merge writes guarded files with no guard, and no admission ask is owed for it.
- **dSafePassage's surfaces** (re-read the specs; these are the record's AGREES and MISMATCH rows):
  the `[[upgrade]]` and `[[retired]]` grammar and `upgrade_steps.py` (unit 1); the step gate,
  `tools/govkit/surface-classes.toml`, class readers `reader(root) -> set[str]`, a plant, an optional
  own-record witness, and exit 2 for a registered class whose population is empty (unit 10); the
  legs `step-gate`, `step-rows-frozen` (every byte of a program a landed argv names is frozen, unit 1
  S9) and `upgrade-walk` (unit 5); `write_row_order(outbox, kind, row, to_commit, body)` with `row` a
  receipt row whose `path` keys the order file (unit 9 and `tools/govkit/govkit.py:10760`); the docs
  leg, whose `usage.toml` takes one `[[class]]` row per class registered in `surface-classes.toml`,
  anchors each member on exactly one page, and keeps the shrink-only
  `memory/project/docs-undocumented.txt` (unit 13, S1, S3, S6 and S8); a `[[shim]]` row's window,
  counted per row (unit 6, S5).

Groups, one writer each. The unit your handoff names leads one group, and you revise every spec of
that group, and no other:

- **Group A, caps, led by unit 11:** specs 2, 3, 6, 11 and 34.
- **Group B, keys, led by unit 1:** specs 1, 4, 7, 9, 14, 20 and 27.
- **Group C, overlay and update, led by unit 32:** specs 15, 32, 33, 35, 36 and 46.
- **Group D, tags and steps, led by unit 31:** specs 19, 25, 26, 30 and 31.
- **Group E, help and batches, led by unit 37:** specs 37, 49, 50 and 55.

The spec files are `memory/builds/dOrderedCharter/spec/2026-10-2?-spec-PLAY-dOrderedCharter-<n>.md`.
Write probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-thermostat-power-issue-370c51/784b9d4d-3d6b-441c-87c6-b603e2cf2649/scratchpad/d<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads, the sections moved, each fork
you added or re-resolved with its mark, its byte count, and any parent spec that looks wrong.

Per spec, by the record's rows:

1. **Spec 1** (rows 29, 30; U3, U4). Read `charter.practices` with `policy.py get`. On the
   derived-default refusal the unit computes the `foundation` set itself and prints that it did; any
   other exit 2 refuses. Row 30: state, as a §8 fork with a recommendation, how a set of practice tags
   passes dGroundRules' value check (its unit 1, `:69-71`, `:145`); recommend the build run reads the
   landed row's `allowed` first and files an ask to dGroundRules if it refuses a practice tag. Fill and
   drain the row.
2. **Spec 2** (row 39; U1, U3, U4). S9 measures `AGENTS.md` through `budgets.py resolve AGENTS.md`, and
   a crossing is raised in the guard's one admitted shape on `budgets."AGENTS.md"`. Files touched:
   `.governance/policy.toml` and `memory/DECISIONS.md` in place of `tools/template-size-limits.txt`.
   Fill and drain `charter.override`.
3. **Spec 3** (U1). S7 measures against the document's `budgets.*` cap through `budgets.py resolve`; a
   document with no census row states what happens (no cap declared, or a census row this unit adds).
   Add the external consumes-from edges for dSafePassage unit 1 and dGroundRules unit 9.
4. **Spec 4** (row 31). The preset line stops restating the resolution order: it names the hand-over
   to dKeptSession and points at `policy.py get --explain` for each key's source.
5. **Spec 6** (row 37; U1, U2). S6 reads both caps through `budgets.py resolve`, and the rows move by
   dSafePassage's step, not dGroundRules. S7's sentence cannot go into a file that no longer exists,
   and an agent cannot write a comment into the guarded policy file: write a §8 fork, recommending the
   sentence on `help/charter.md` (S8's page) with the policy file left as dSafePassage's step writes it.
6. **Spec 7** (row 40; U3, U4). `core.exceptions: owner-only-expiring` uses the owner proof spec 15's
   fork settles; point at that fork rather than repeating it. Fill and drain `core.bypass` and
   `core.exceptions`.
7. **Spec 9** (row 32; U4). `policy_reader` is a callable that runs `policy.py get <key>` as a
   subprocess; a list value renders as `get` prints it, one member per line; an exit 2 refuses the
   render naming the key. State that a `policy:<key>` unit in a `.toml` manifest is no reader for
   reader coverage.
8. **Spec 11** (row 33; U1 to U4). Each load point's cap is read with `budgets.py resolve`, named as
   the census names it; the role block reads `role-body`'s mode. The reuse audit's limits-file line and
   §8 F2's "does not exist yet" are re-grounded on rung 1: `budgets.enforce` is in gov's policy file at
   `warn` (dGroundRules unit 1, S1). `CODEX_MAX` is read where spec 31 moves it, through its census
   row. Fill and drain `instructions.checks`.
9. **Spec 14** (row 48). Read `memory.load-budget` with `policy.py get`; drop `LOAD_BUDGET_DEFAULT`.
   Convert `k` as spec 27 does (1,000 bytes, the systems record `:570`), and say in §9 that the
   default moves from 8192 to 8000 bytes; if that unit of `k` is wrong for this key, write a fork.
10. **Spec 15** (row 40; U3, U4). Write the owner-proof fork here, open for the owner, with options:
    (a) dOrderedCharter's own proof, testing stderr as the guard's hook does, stated as the second
    implementation; (b) an ask to dGroundRules to move the hook's test into a callable in
    `tools/policy/`; (c) wait for dDeclaredLoop's TTY CLI and refuse every write until then. Recommend
    (a). Whichever stream the spec tests, it says stderr or stdin once. Fill and drain
    `instructions.edit` and `instructions.proof`.
11. **Spec 19** (rows 11, 46; U3, U4). S8 fills the three landed `tags.*` rows and drains them. The
    edge "dSafePassage's shim" follows spec 31's re-export fork; until the owner answers it, S9 says the
    hold is spec 31's open fork.
12. **Spec 20** (U3, U4): fill and drain `instructions.legacy`.
13. **Specs 25 and 26** (U3, U4): fill and drain `tags.bundle`, `tags.bundle-rows` and
    `tags.positional`.
14. **Spec 27** (row 47). `memory.code-budget` is already a catalogue row; read it with `policy.py get`
    and drop the wait. Its row is dFurnishedOrders' to fill.
15. **Spec 30** (U6). The `.governance/deploy.toml:28` comment edit cannot land in an agent's commit.
    Re-resolve on rung 1 to spec 32's F4 route (the step's prepared-merge write), or drop the edit and
    record the comment as a kept hit; recommend spec 32's route.
16. **Spec 31** (rows 3, 6, 10, 12, 16; U1, U2, U7, U9).
    - Row 16: the leg is `upgrade-walk`.
    - Row 6: AC3's first half observes the succession row through a command dSafePassage unit 1
      states (its `list` prints step rows; `read_retired` or `update`'s carry reads the other).
    - Row 10: write the re-export window fork, open for the owner: (a) the `module-export` class row
      stays, and the window is counted by dConvergedCharter from that row's landing commit, with an ask
      to dSafePassage to drop its unit 6's mention of this re-export as a first shim row (`:89-91`);
      (b) an ask to dSafePassage for a shim kind that forwards named re-exports. Recommend (a).
    - Row 12: write the seed-row fork, open for the owner: (a) an ask to dSafePassage to route a
      retired seed row through its unit 9's `retired-edited` arm; (b) this unit extends that arm
      itself; (c) AC9 states the verdict the parent gives. Recommend (a).
    - U1: S1's Readers drop `tools/template-size-limits.txt`. U2: S1 re-points `caps.toml`'s
      `codex-instructions` row's `enforcer` and `home` in the commit that moves `CODEX_MAX`.
    - U7: move `read_charter_keys` and `write_charter_key_plant` out of the step program, into a module
      no landed argv names, so a later edit to them does not red `step-rows-frozen`.
    - U9: §5 risks says the commit removing the last re-export also removes the `module-export` row.
    - F4: drop "files the admission ask": the guard never fires at a landing.
17. **Spec 32** (row 43; U5). S7's extension lives inside `tools/policy/`: it reads the `[[policy]]`
    rows from `.governance/instructions.toml`'s blob at the revision the reader reads, through the
    policy kit's own blob reader, never importing `tools/playbook/`, and its rows are seen by the
    key-to-row matcher, `validate`, `arm_schema` and the mirror. Keep spec 32 as the overlay
    grammar's owner and say which part the policy kit parses.
18. **Spec 33** (row 18; U3, U4, U5). `tools/playbook/pins.py` cannot import govkit: its drift verb
    returns the orders as data, run as a subprocess by `cmd_update`, which writes each with
    `write_row_order(outbox, "unit", row, to_commit, body)`, `row` a mapping whose `path` keys the
    order (for example `.governance/instructions.toml#<repository tag>`). `instructions.stale` is read
    with `govkit.read_policy_value("instructions.stale", target)`, the target's committed policy.
    Fill and drain `instructions.stale`.
19. **Spec 34** (row 36; U2). The cap is `budgets."AGENTS.md"`, read through `budgets.py resolve`; the
    harness limit through `CODEX_MAX`'s census row.
20. **Spec 35** (rows 18, 45; U3, U4). S5 fills the landed `instructions.exclude` row and drains it;
    AC12's red is `policy.py lists --check`, not a schema refusal. Orders go through spec 33's handler.
21. **Spec 36** (row 49). State that the check reads `instructions.exclude`'s landed `allowed`, and how
    the build run's first probe confirms dGroundRules' value check admits a set of gov tags.
22. **Spec 37** (rows 21, 50, 51; U8).
    - Row 21: the drive and kinds registries each register a class in `surface-classes.toml`, with a
      reader and a plant, before `usage.toml` names them; re-resolve on rung 1 by dSafePassage unit 13,
      S1 and S8.
    - Row 50: the policy page renders the rows that carry both fields and lists the rest, counted,
      instead of refusing; the other registries keep the refusal.
    - Row 51: the policy schema's reader parses `tools/policy/catalogue.toml` with `tomllib`.
    - U8: a key already anchored on another page under `help/` is linked from the policy page, not
      anchored twice; a key the page anchors leaves `memory/project/docs-undocumented.txt` in that
      commit.
23. **Spec 46** (row 44). The policy reader reads the landed ref, not `HEAD`. Keep the overlay's `HEAD`
    rule, and re-resolve on rung 1: every `policy.py get` the composition makes passes `--rev HEAD`, so
    the overlay and the policy values read one revision. Replace the "dGroundRules has no spec yet"
    evidence with its landed specs.
24. **Spec 49** (row 50; U1, U7). S1 follows spec 37's policy-page rule. `:147` measures against the
    file's `budgets.*` cap. The `census` verb goes in its own program file, never added to the step
    program a landed argv names.
25. **Specs 50 and 55** (U1). Each `tools/template-size-limits.txt` row reference becomes the
    `budgets.<cap>` cap read through `budgets.py resolve`.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-24, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record.
- Replace each now-false sentence where it stands. Drop "the parent is unbuilt" and "until it lands"
  wording only where it is now false.
- Spell a `tools/policy/` path inside an acceptance criterion as dGroundRules' own criteria do,
  quoted or by bare name, because none is tracked until dGroundRules builds.
- A resolved fork whose chosen option a parent now rules out is re-resolved on rung 1 naming the
  parent, and marked `RESOLVED (agent, 2026-10-24, delegated)`. The three forks this brief says are
  open for the owner (spec 15's proof, spec 31's re-export window and seed rows) stay open with their
  recommendation. Re-open no other fork.
- Stay under the class cap of 49152 bytes; spec 49 is at 48112, so replace text and do not append.

### brief:acceptance

- For each spec you revise, `grep -n -e 'until it lands' -e 'template-size-limits' <spec>` prints only
  lines that name history or the removal itself.
- `wc -c <spec>` is under 49152.
- The **Status:** line reads `rev-<N+1>`, and §9 holds the new line.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only
  your specs staged into it through `GIT_INDEX_FILE`, names none of your specs. Delete the copy
  after. Findings that only a `gen_build_index.py --write` render cures are the main loop's: name
  them and leave them.

### brief:gates

Only the memory hygiene gate and the naming lexicon, as the role allows. The main loop runs the rest
and renders the index.

### brief:non-goals

- No file outside the spec files of your group. No commit, no stage into the real index, no
  deviation record: the main loop writes those.
- No dSafePassage or dGroundRules file. A parent spec that looks wrong is a line in your return, not
  an edit.
- No change to what a unit builds beyond what the re-ground forces.

### input:spec

memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-32.md

### task:reuse

dSafePassage's re-ground brief memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-1-dgroundrules-reground.md as the precedent, and the parents' specs as the interface.

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
