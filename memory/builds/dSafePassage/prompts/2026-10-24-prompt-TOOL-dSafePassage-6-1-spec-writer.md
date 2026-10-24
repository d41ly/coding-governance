**Serves:** journal TOOL-dSafePassage-6

# gov-spec-writer handoff — TOOL-dSafePassage-6

<!-- gov:handoff role=gov-spec-writer build=dSafePassage unit=TOOL-dSafePassage-6 path=memory/builds/dSafePassage/prompts/2026-10-24-prompt-TOOL-dSafePassage-6-1-spec-writer.md role-sha=06b14b1ac42a task-sha=eb7a79486b50 -->

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

This handoff is for build `dSafePassage`, unit `TOOL-dSafePassage-6`.
Not supplied, optional: `card:route`.

### brief:goal

Revise the eight dSafePassage specs that the cross-check record names under "For the build run's
re-ground", so each one names dGroundRules' policy surfaces the way dGroundRules' landed specs spell
them. Each spec's design stays its own; only its assumptions about dGroundRules change.

### brief:items

Read the cross-check record first,
`memory/builds/dSafePassage/build/2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`.
Its summary table numbers every assumption (rows 1 to 42), and
"The mismatches, both sides quoted" gives both sides of each one with `file:line`. Its U1 to U8 are
dGroundRules surfaces the specs do not name yet. dGroundRules' specs are under
`memory/builds/dGroundRules/spec/`. Read the unit the record cites at each line it cites: this brief
summarises them, and the specs win where the two differ.

Facts every revision uses:

- **The reader.** `read_policy_key` stays the bash `KEY=value` parser for the legacy homes, and never
  parses TOML (dGroundRules unit 2, S8 and AC8). The TOML reader is `resolve(key, repo, rev)` and its
  CLI, `python <prefix>/policy/policy.py get <key> [--rev <rev>] [--explain] [--json]` (unit 2 S6,
  S7; unit 5 S7). It reads the committed revision, by default the landed one (the remote ladder's
  `<remote>/<branch>`, else local `main`), or `--rev`. It never opens the working-tree file (unit 2
  S2). A kit may not import a sibling kit (unit 1, `:105`), so govkit and the shared `tools/lib`
  blocks reach the reader as a subprocess, or through the inlined `resolve_kit_dir` with the kit
  declared in `requires` (unit 9, `:180-181`; unit 21, S26). An unset key reads the catalogue default
  with its reason (unit 3).
- **Caps.** Each cap is read by `tools/policy/budgets.py`: `resolve_caps(requests, repo, rev)` and
  `python <prefix>/policy/budgets.py resolve <cap>` (unit 9, S2). That module is the only reader of
  `template-size-limits.txt`, through its census `tools/policy/caps.toml`, whose seven `limits:`
  rows name that file as their home. `check-template-size.sh` and `check-spec-tokens.py` stop
  parsing it (unit 9, S5 and the data model). A cap held in both the policy file and the limits file
  refuses at resolution (unit 9, S3). `arm_limits_readers` reds on any tracked script outside
  `tools/policy/` that reads the limits file (unit 9, S7; unit 21, S20 and S29).
- **The agent limit.** `read_legacy_fanout(repo, rev)` in `tools/policy/policy.py` reads
  `.agent-cap.conf` at the revision `resolve` reads. Its grammar: `FANOUT_CAP=<n>` or `"<n>"`, a BOM
  and a trailing CR tolerated, the last such line winning. It only lowers the key (unit 10, S1). The
  lowering sits in `resolve_read`, so `get` and the mirror both answer the lowered value (unit 15,
  S1). Unit 10 retires agent-cap.js's own conf read and `--print-cap`.
- **The catalogue.** `tools/policy/catalogue.toml` holds one `[[key]]` row per v2 `[policies]` row,
  in v2's order and with v2's owner (unit 1, S3 and AC2), so all five dSafePassage keys land with
  dGroundRules: `help.enforce`, `platforms.provision`, `install.deprecation-window`,
  `install.on-shim-call` and `install.retired-edits`. They land with no `summary` and no `usage`, and
  sit on the shrink-only `tools/policy/unsummarised-keys.txt` (unit 1, S6). A unit that owns one of
  them fills in its `summary` and `usage` and drains the list in the same commit, with
  `python <prefix>/policy/policy.py lists --write`. It never adds a row. The catalogue's loader is
  `load_catalogue(kit)`; it takes no revision argument.
- **The mirror.** `.governance/policy.json` is read only through `readPolicy` in
  `tools/policy/policy-mirror.js` (unit 5, S5). `arm_mirror_readers` reds any tracked code file
  outside `tools/policy/` that names the mirror (unit 5, S9), and Python and shell call the reader
  (unit 5, non-goals). A policy-file edit stales the mirror, and the bar reds until the mirror is
  regenerated. The guard admits a mirror commit only when the policy file and the catalogue equal
  HEAD (unit 19, S1), so the regenerated mirror goes in its own second commit.
- **The guard.** It runs in gov's pre-commit only. The lander never fires pre-commit (unit 6,
  `:105-107`). It admits one agent shape, a single measured-file cap raised (unit 6, S3). The ask
  TOOL-dGroundRules-13 is DEFERRED until unit 6 (`memory/builds/dGroundRules/BACKLOG.md:6`, `:21`).
- **Reader coverage.** Once a build's specs are all terminal, each key it owns needs a reader in
  tracked code in one of two shapes. In `.py` or `.js`: a call whose first argument is the key as a
  string literal, `ident("key"`. In `.sh` or `.githooks/`: `policy.py get <key>` (unit 8, the Readers
  table). A subscript into JSON matches neither shape.

Per spec, by the record's rows:

1. **Spec 1** (rows 3, 4, 6, 8, 9, 11, 13; U1 to U4):
   - Re-point every read that names `read_policy_key` as the TOML or caps reader: the edges, S6, S7,
     the up text, the writer paragraph, AC10 and §8 F9. Caps go through `budgets.py resolve`; any
     other key goes through `policy.py get`.
   - State how the step reads before its commit: the reader reads revisions only. The record's row 4
     offers parsing the step's own text with `tomllib` for the read-back and the witness, and reading
     the target's HEAD through the reader for the pre-write check. A choice you cannot derive is a §8
     fork with a recommendation.
   - S6's conf parse cites `read_legacy_fanout`'s grammar, and says how the step reads the target's
     file.
   - S6's Readers re-derive at the build run's base, by the spec's own `git grep`.
   - S5: define the window's population and its join to a step's `surfaces` against
     `tools/policy/legacy-homes.txt` (`<home> <key> <mark>`, gov-only, withheld from installs; units
     7 and 17). Or state that neither step closes a member and drop S5's tie to the list. A fork if
     neither follows.
   - S7, S8: retire `budgets.py`'s `limits:` branch, re-point `caps.toml`'s seven homes, and handle
     `arm_limits_readers` against the step program (U1, U2). Say what a resumed up does under the
     two-homes refusal (U3). S8 lands as two commits, the policy file and then the regenerated mirror
     (U4). Update Files touched.
   - §8 F8 keeps its resolution. Add one sentence: the build run's first pass reads whether the
     landed guard grants TOOL-dGroundRules-13's shape, and stops S8 if it does not.
   - The spec is 44847 bytes and the class cap is 49152. Stay under it: replace text, do not append.
2. **Spec 5** (rows 17, 18): the `fanout-cap` plant's `policy` observation reads
   `runtime.agents-in-flight` through gov's `policy.py get --rev <the walked commit>`, run in the
   target, so no target-side kit is needed. Pair it with `.agent-cap.conf` absent, since a
   `FANOUT_CAP=2` conf reads 2 whether or not the step ran.
3. **Spec 6** (rows 19 to 22; U5 to U7): S7 and AC9 fill the two existing rows and drain the list.
   - The `sh` forwarder reads through `policy.py get`, or the policy kit's `policy-shim.sh get`
     (unit 5, S6).
   - The `js` forwarder reads through `readPolicy`, and the `py` forwarder through `policy.py get`.
     No forwarder names the mirror. Keep the read-fails-to-`warn` prelude.
   - The window value is read with `policy.py get install.deprecation-window` at gov's landed
     revision.
   - Each key keeps a reader in a shape unit 8 counts.
   - §8 F2's resolution is re-grounded: rung 1, the parent's landed spec decides. Mark it
     `RESOLVED (agent, 2026-10-24, delegated)`.
4. **Spec 8** (row 27): the guard never fires at a landing. Fix §3 Edges' external line, the risks
   line in §5 and the note under §7. The guard binds spec 1's unit-pass commit, where spec 1's F8 (a)
   writes gov's policy file. At the landing the lander's walk finds that step's witness holding.
5. **Spec 9** (rows 29 to 31; U5, U6): S6 and AC10 fill the existing `install.retired-edits` row and
   drain the list. The mode is read with gov's `policy.py get install.retired-edits`, run in the
   target, so it reads the target's committed policy at its landed revision, and `order` is the
   catalogue default where the target sets none. The read keeps a shape unit 8 counts.
6. **Spec 10** (rows 33, 34): the `policy` class reads each `[[key]]` `name` of
   `tools/policy/catalogue.toml` at the base and at the tip, by `git show <rev>:<path>` and `tomllib`.
   It never reads them through `read_policy_key`. Fix §8 F6 and every line that names
   `read_policy_key` as the catalogue's reader.
7. **Spec 11** (rows 35 to 37; U5, U6, U8): S11 and AC13 fill the existing `platforms.provision` row
   and drain the list.
   - The reader is Python only. The block runs `<candidate> <prefix>/policy/policy.py get
     platforms.provision` with the newest candidate that ran, never `policy-shim.sh`, which runs
     `resolve_python` itself (unit 5, S6).
   - Pick one revision: `get`'s default, the landed one, or `--rev HEAD`. Write it in S4, in the
     design and in AC3.
   - Say how the block finds the policy kit.
   - S5's parity population gains `tools/policy/policy-shim.sh`, which carries the block inline.
     Derive the count at the base rather than typing a new one.
8. **Spec 13** (row 39; U5, U6): S7 and AC8 fill the existing `help.enforce` row and drain the list.
   `help.enforce` is read with `policy.py get` in a shape unit 8 counts.

In every spec you revise:

- Bump the **Status:** line's `rev-N` to `rev-N+1`, dated 2026-10-24, the status kept `DEFERRED`.
- Add one §9 line naming the sections moved and the cross-check record.
- Replace each now-false sentence where it stands, and drop "the parent is unbuilt" wording only
  where it is now false.
- Spell a `tools/policy/` path inside an acceptance criterion as dGroundRules' own criteria do,
  quoted or by bare name, because none is tracked until dGroundRules builds. Unit 1 says why in §6.
- A resolved fork whose chosen option the parent now rules out is re-resolved on rung 1 with the
  parent's name, and marked `RESOLVED (agent, 2026-10-24, delegated)`. Re-open no other fork.

### brief:acceptance

- For each spec you revise, `grep -n read_policy_key <spec>` prints only lines that name it as the
  legacy `KEY=value` parser.
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

- No file outside the spec files you were handed. No commit, no stage into the real index, no
  deviation record: the main loop writes those.
- No dGroundRules file. A dGroundRules spec that looks wrong is a line in your return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### input:spec

memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-6.md

### task:reuse

no seam fits: a one-off research record in the house grammar (memory/HYGIENE.md, record bindings).

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
