**Serves:** journal TOOL-aLightenedLoop-8

# gov-spec-writer handoff — TOOL-aLightenedLoop-8

<!-- gov:handoff role=gov-spec-writer build=aLightenedLoop unit=TOOL-aLightenedLoop-8 path=memory/builds/aLightenedLoop/prompts/2026-11-15-prompt-TOOL-aLightenedLoop-8-1-spec-writer.md role-sha=3db8c2a485df task-sha=fac8a5031b38 -->

## Role

[.claude/agents/gov-spec-writer.md · Level 5 · This role's static instructions; yields to levels 0 to 4]
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
- Verify every claim about current code by reading that code, and cite where you read it in the
  form the spec format's writing rules give. A claim you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the memory hygiene gate and the naming lexicon over your specs, and, where this
  repository has it, the spec-token checker as `check-spec-tokens.py --spec <path>` over each spec
  you wrote, fixing every hit it names before you return. You run no other gate.
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

## House rules

A `check-spec-tokens.py --spec` run that finds a miss exits 1. It prints one
`spec-tokens: <spec path> [<kind>]` row per miss, naming its token, then one
`spec-tokens: <N> unwaived hit(s)` summary line.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.

### Drive

- spec-write · gov-spec-writer — a build whose units lack a spec or hold a thin one: `Workflow <prefix>/workflows/unattended-build.js`
[/.claude/agents/gov-spec-writer.md]

## Task

[AGENTS.md#practices-at-design · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them; the override is recorded]
### Practices at design

- [yagni] no extension point, option or layer the unit does not use
- [reuse] a kind's second instance extracts its factory
- [core] logic and authorization live in one core, each surface a thin adapter
- [contract] one source, generated copies, a parity gate against a live re-derivation
- [derive] status, counts, inventories and indexes are generated or declared
- [one-fact] each value has one owning source
- [gate] state what a gate does not check
- [class] a guard shares no state with what it guards
- [cost] declare a wall-clock ceiling for each suite
- [migrations] every migration is reversible
- [security] deny by default and give automation the narrowest grant
- [bound] a fan-out declares its bound
[/AGENTS.md#practices-at-design]

## Card

[.claude/orientation-card.md · Level 1 · the build's card: where this session stands; level 0 outranks it]
- build: aLightenedLoop
- unit: TOOL-aLightenedLoop-7 · spec memory/builds/aLightenedLoop/spec/2026-11-15-spec-TOOL-aLightenedLoop-7.md
- brief: memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-7-cadence-drop.md
[/.claude/orientation-card.md]
[memory/builds/aLightenedLoop/prompts/2026-11-15-prompt-TOOL-aLightenedLoop-8-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aLightenedLoop`, unit `TOOL-aLightenedLoop-8`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> Reconcile and land

> The reconcile with origin/main conflicts in `run_spec_token_check`: aBriskDeclaration split it into an async start half and a read half, keyed before the run, while aLightenedLoop unit 3 re-keyed its cache on the checker's recorded inputs, with a stability bracket after the run. How should the reconcile resolve it?

Answer: "Port unit 3, run driver suite (Recommended)"

### brief:goal

Merge `origin/main` into `branch/alightenedloop-eb7b8b` and resolve every conflict. In `tools/unattended/unattended.sh`, port TOOL-aLightenedLoop-3's spec-token cache, as TOOL-aLightenedLoop-6 repaired it, onto aBriskDeclaration's split of `run_spec_token_check` into `init_spec_token_check` and the read half (TOOL-aBriskDeclaration-1 S3, S4). The merge's own changes stay as main shipped them, and unit 3's verdicts stay as its spec states them.

### brief:items

1. The merge: `git merge --no-ff origin/main`. A trial merge at `aebbb4a72` conflicted in five files:
   - `memory/project/readme-contract.txt`: keep every row from both sides.
   - `memory/guides/SESSION-KICKOFF.md`: a `last-audit` re-stamp at this branch's HEAD, as the manifest's stamp rule says.
   - `tools/template-size-limits.txt`: the protocol row becomes the merged render's measured bytes, with both raises named in its comment. A run's raise is allowed on the file's own terms, with a `memory/DECISIONS.md` row.
   - `tools/check-spec-tokens.test.sh`: `FLOOR_ASSERTIONS` becomes the reconciled sum, both sides' additions over their common base, each named. The two sides' comments disagree on that base, 245 against 247, so measure it.
   - `tools/unattended/unattended.sh`: item 2.
2. The port. In the merged split:
   - The start half derives the lookup key over the existing input record (`derive_spec_token_key` with the record argument, unit 3's three-argument form, which the merge keeps), compares it with the recorded key, and skips on a match.
   - The start half also reads the tree state before the checker starts, and starts the checker with `SPEC_TOKENS_INPUTS` set to the record path, removing the stale record first.
   - The read half, after an admitted verdict, derives the key over the new record and only then re-reads the tree state, exactly as unit 6 S3 ordered it. It records the key only when the two states match and the record replays. Otherwise it prints the same one-line not-recorded reasons unit 3 and unit 6 print.
   - The start/read split, its silence, `remove_spec_token_check` and main's refusal order all stay exactly as main has them.
   - The comment block states the merged design once.
3. The suites: `tools/unattended/unattended.test.sh` holds main's split arms (aBriskDeclaration A1 to A6) and this build's cache arms (unit 3's inverted steps a, b and c, and unit 6's raced and popen stubs). Each must still say what it says against the merged driver. Reconcile `FLOOR_ASSERTIONS` and its shard floors as sums, each named.
4. Every other auto-merged file in the merge must keep both sides' intent. In particular: `tools/unattended/stop-guard.js`, `check-unattended.sh`'s allow-list, the unattended templates (re-render the copies with the kit's adopter), `tools/check-spec-tokens.py` and `tools/policy/check_policy.py`. Regenerate the generated outputs (`bash tools/run-gates/run-gates.sh --regen`, `gen_build_index.py --write`, `gen_map.py --write`).

### brief:acceptance

- The merge commit has both parents and no conflict markers (`git grep -n '^<<<<<<< '` prints nothing).
- `bash -n tools/unattended/unattended.sh` passes.
- A scratch-fixture probe of the merged `run_spec_token_check` shows:
  - a skip on an unchanged input record;
  - a re-run when an input moves;
  - no recorded key when the tree moves inside the bracket;
  - the "cannot be replayed" line on a popen record;
  - main's start-before-read ordering.
- The unattended driver suite, pooled, and the merge bar are the main loop's, after this pass.

### brief:gates

The merge bar, and `bash tools/unattended/run-unattended-gates.sh --pooled`, at the main loop.

### brief:non-goals

No change to aBriskDeclaration's behaviour beyond what the port needs, and no change to unit 3's or unit 6's verdicts or line texts.

### task:reuse

`tools/memory-tree/gen_build_index.py#check_staged_render` · `tools/memory-tree/gen_build_index.py#check_index_input` · `tools/unattended/unattended.sh#derive_spec_token_key` + gate-fingerprint.sh · `tools/unattended/stop-guard.js#runLiveness` · `tools/workflows/unattended-unit.js#DRIVER_STEPS` · reuse_lookup found no generic caching seam

### card:route

- build: aLightenedLoop
- unit: TOOL-aLightenedLoop-7 · spec memory/builds/aLightenedLoop/spec/2026-11-15-spec-TOOL-aLightenedLoop-7.md
- brief: memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-7-cadence-drop.md
[/memory/builds/aLightenedLoop/prompts/2026-11-15-prompt-TOOL-aLightenedLoop-8-1-spec-writer.md]
