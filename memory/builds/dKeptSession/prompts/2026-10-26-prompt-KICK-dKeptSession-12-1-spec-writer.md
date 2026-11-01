**Serves:** journal KICK-dKeptSession-12

# gov-spec-writer handoff — KICK-dKeptSession-12

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=KICK-dKeptSession-12 path=memory/builds/dKeptSession/prompts/2026-10-26-prompt-KICK-dKeptSession-12-1-spec-writer.md role-sha=06b14b1ac42a task-sha=59cb22a1118e -->

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

This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-12`.
Not supplied, optional: `card:route`.

### brief:goal

Revise the 15 dKeptSession specs that the cross-check record names under "For the re-ground". Each one
should state dDeclaredLoop's and dPlacedRequest's surfaces the way their specs now spell them on
origin/main at `c8d46e188`: dDeclaredLoop as its re-ground `783f1ad3a` left it, dPlacedRequest as its
re-ground `2740f0a3d` left it. Each spec keeps its own design, and only its assumptions about the
parents change.

### brief:items

Read the cross-check record first,
`memory/builds/dKeptSession/build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`. Its
summary table numbers every assumption (rows 1 to 116), and "The mismatches, both sides quoted" gives
both sides of each MISMATCH. Read each parent spec the record cites, at the lines it cites. This brief
summarises them, and where the two differ, the specs win. Before you edit for a row, re-read both
sides. A row the parent's text does not bear out is not edited: return it as refused, with the line
that refutes it.

Facts every revision uses:

- **A sibling kit.** A kit imports no sibling kit (TOOL-dGroundRules-1 §4; oc7:202-205; dl12 S4 and
  dl18 at rev-3; dl27:158; dl26:70-71). Code in one kit reaches another kit's verb by subprocess, found
  through an inline `resolve_kit_dir` block (dl12:53-55 carries the loop kit's one block in
  `loop_lib.py`). A policy key is read by running `policy.py get <key>` as a subprocess, "the one seam a
  sibling kit may reach" (oc7:379-380); ks6 S2 and ks9 S4 already read so. Where the verb a spec needs
  does not exist, write a §8 fork open for the owner. The options are an ask to the parent for the
  verb, or a declared `requires_if` row like `tools/memory-tree/kit.toml:8`, with the reason the rule
  admits it. Recommend one. dDeclaredLoop's specs 12 F5, 18 F5 and 26 F5 and dWitnessedBar's spec 3
  F6 are the precedent.
- **A typed record kind.** dOrderedCharter unit 42 S2 and S3 make `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` the record factory's kind list, and read a `-<kind>-<n>.md` file
  whose Serves kind differs as malformed. dKeptSession's spec 39 joins `mailbox-message` to it
  (ks39:33-43); a record of that kind serves as `mailbox-message`, never `journal`. dDeclaredLoop's
  `transition` and dPlacedRequest's `card` and `probe` kinds grew the same tuple.
- **dPlacedRequest's lease witness.** pr1 S8 at rev-5 renews on a commit that records a transition of
  the build on the channel `transitions.record` (pr1:100-102, :239-249), the trailer or the
  `-transition-<n>.md` log record, and `--claims` prints only fields 1 to 5 (pr1:206-208).
- **dDeclaredLoop's row rules.** `returns` names a `record-kind.<name>@<n>` tag (dl12:113,
  dl24:144-145); `on-deadline` names the route a wait takes past its deadline (dl33:58-59).
- **An ask.** No dKeptSession spec files a row in another build's `BACKLOG.md`. Where a fix needs a
  parent change, write a §8 fork open for the owner, with its options and a recommendation, and name
  the ask the build run would file.

Groups, one writer each. The spec your handoff's `input:spec` names leads one group. Revise every
spec of that group, and no other:

- **Group A, sibling kits and the driver, led by spec 1:** specs 1, 8, 20, 36, 44 and 56.
- **Group B, loop-kit reads and records, led by spec 7:** specs 5, 7, 9, 10, 11 and 13.
- **Group C, the card, the claim and the wait row, led by spec 12:** specs 12, 18 and 25.

The spec files are `memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-<n>.md`. Write
probe copies, such as a `GIT_INDEX_FILE` index copy, only under
`C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-silly-jang-ffa5af/b141ae93-c1d4-4429-8ac9-f3aa88a427dc/scratchpad/ks-w<group letter>/`,
and delete nothing else there. Return, per spec: the rev it now reads; the sections moved; each fork
you added or re-resolved, with its mark; each record row you refused, and why; its byte count; and
any parent spec that looks wrong.

Per spec, by the record's rows:

1. **Spec 1** (row 3). `presets.py` reaches the loop kit's `check_expansion_value` by subprocess; dl2's
   guard has only `--staged`, `--push-range` and `--fixture` (dl2:272), so write the fork: an ask to
   dDeclaredLoop for a verb printing the verdict, or a `requires_if` row naming `loop` in
   `tools/policy/kit.toml`.
2. **Spec 8** (row 33). `scratch-guard.js` reads `actions.free` without requiring the policy kit's
   `policy-mirror.js` in process: either a declared `requires_if` row naming `policy` in
   `tools/hooks/kit.toml`, which `agent-cap.js:465-469` would then share, or `policy.py get` by spawn.
   Recommend one in a fork if the choice is not derivable.
3. **Spec 20** (rows 73, 74). S4's `read_scenario_value` reaches the build's placed scenarios through a
   `tools/loop/scenario.py` verb run as a subprocess; dl27 offers only `members`, `new` and `select`
   (dl27:212, :272), so write the fork for a slots-per-build verb or a `requires_if` row. S2's
   `check_scenario_policy` reaches `never` membership and `check_value` through a policy-kit verb by
   subprocess, as ks44 S41 already does for the pair rule (ks44:157-160).
4. **Spec 36** (row 100). S2 names `<driver>` as `resolve_kit_dir("unattended", "unattended.sh", here)`
   from `loop_lib.py`'s inline block (dl52:43-44); S3's "absent driver" is that block's `LookupError`
   (`tools/lib/resolve_kit_dir.py:23,49`), the `isfile` test applied only to the resolved path; AC4's
   plant removes the kit from every place the block searches.
5. **Spec 44** (row 105). S9's `mail-notice.js` binds its build without requiring
   `tools/hooks/scratch-guard.js`. ks56 S23 already carries `readCard` and `extractRouteUnits` inline
   (ks56:105-107): align S9 with it, or name the spawn of `manifest-check.sh --card --path --session
   <sid>` (pr2 S10).
6. **Spec 56** (row 108). S3's `run_driver` finds `<driver>` once through `loop_lib.py`'s inline
   `resolve_kit_dir` and turns its `LookupError` into the callers' unarmed outcome; AC3's stub records
   `argv[1]` as the resolved path.
7. **Spec 5** (rows 13, 16). The disposal's `mailbox-message` records are written at or after dl3's
   writer step 5, beside the transition record, so step 4's dirty-index refusal (dl3:185-189) never
   sees them; or write the fork for a dl3 hook that stages extra records after step 4. S12 serves the
   record as `mailbox-message <anchor id>`, naming the tuple and HYGIENE joins by reference to ks39.
8. **Spec 7** (rows 23, 24, 26).
   - The parent lease's `witness` (pr1:206, field 15) is not on `--claims`: name the reader, as a fork
     for an ask to dPlacedRequest for a `--claims` field or holder verb.
   - S4 takes its listing at the transition commit `write_transition` just made, the commit pr1 S8
     records as `witness`, not at `--witness`; state the `micro-format`-only case, where no commit
     witnesses (pr1:249).
   - `resolve("deps.coordination")` becomes `policy.py get deps.coordination` by subprocess.
9. **Spec 9** (row 36). runlog's `extract.py` reads the transition channel by `git`, as pr1 F8 (a)
   does (pr1:444-452), or writes the fork for `loop_transition.py read` and a `loop_lib.py` steps verb;
   `check_cap` is reached through a budgets verb by subprocess, or the same fork.
10. **Specs 10 and 11** (rows 39, 43). `resolve("mailbox.reads")` and `resolve("notify.owner")` become
    `policy.py get <key>` by subprocess through the inline `resolve_kit_dir`.
11. **Spec 13** (row 49). S3 and F3 read the extended token tuple (`RECORD_KIND_TOKENS` plus
    `TYPED_RECORD_KINDS`, oc42:35-39), and re-derive the `records —` line's bound against
    `CARD_CAP_BYTES` for the grown set, or select a declared subset of kinds.
12. **Spec 12** (row 45). The `tree —` cell is read from the stored build card before pr2 S6's lookup
    re-keys it (pr2:87-89), or the fork for an ask that pr2 keep the publisher's tree in a tail field.
13. **Spec 18** (row 65). §10 restates that pr3 S3 declares `item.entry.claim` with the outcomes
    `claimed`, `slug-taken`, `awaiting` and `refused` (pr3:58-64), and that the S2 join is still owed
    for the `disposition` its rows carry.
14. **Spec 25** (rows 82, 83, 87, 90).
    - §4's evidence and F4's ask name the channel source (the trailer or the `-transition-<n>.md` log
      record), not a trailer only.
    - S4 passes the question commit as `--witness` only once the landed lease verb admits it, by a
      version gate or capability probe; until then it passes the transition witness pr1:252-254 names.
      The Rollout and AC5 say so.
    - `returns` names a `record-kind.<name>@<n>` tag, or the fork for an ask that dl12 admit a prose
      `returns`.
    - `on-deadline` names the `defaulted` route's target, `stand-in:tools/unattended/unattended.sh`,
      and F3's deferral goes.

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
- For each record row your spec answers, `grep -n` for the sentence the row quotes from `ksN:L`
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
- No file of dOrderedCharter, dDeclaredLoop, dPlacedRequest, dSafePassage or dGroundRules. A parent
  spec that looks wrong is a line in your return, not an edit.
- No change to what a unit builds beyond what the re-ground forces.

### input:spec

memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-12.md

### task:reuse

the last wave's procedure: memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md and 2026-10-26-...-parents-reground.md, its record build/2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck.md, its deviation records; tools/roles/handoff.py render for every handoff.

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
