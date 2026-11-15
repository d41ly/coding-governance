**Serves:** journal TOOL-aLightenedLoop-7

# gov-spec-writer handoff — TOOL-aLightenedLoop-7

<!-- gov:handoff role=gov-spec-writer build=aLightenedLoop unit=TOOL-aLightenedLoop-7 path=memory/builds/aLightenedLoop/prompts/2026-11-15-prompt-TOOL-aLightenedLoop-7-1-spec-writer.md role-sha=3db8c2a485df task-sha=ec77d1cd6624 -->

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
- unit: TOOL-aLightenedLoop-2 · spec memory/builds/aLightenedLoop/spec/2026-11-14-spec-TOOL-aLightenedLoop-2.md
- brief: memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-2-bar-fix.md
[/.claude/orientation-card.md]
[memory/builds/aLightenedLoop/prompts/2026-11-15-prompt-TOOL-aLightenedLoop-7-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aLightenedLoop`, unit `TOOL-aLightenedLoop-7`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> Unit 2's new `KEEPALIVE_TRACKED_INTERVAL` conf key reds the policy check: a new key must be a policy-catalogue key, not a new `.unattended.conf` legacy home, and that list is shrink-only. How should the tracked idle-wake cadence be declared?

Answer: "Drop the tracked cadence"

### brief:goal

Retire the longer-cadence half of TOOL-aLightenedLoop-2 and keep its cheap `--wake` tick. The merge bar at `9347f5848` redded two legs on unit 2's changes. Unit 2's fix pass diverged on the first, because moving the key to the policy catalogue is a redesign: `memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-2-bar-fix.md`. The owner chose to drop the key instead. Unit 2's spec is CLOSED and frozen, so this unit corrects it on top.

### brief:items

1. Remove `KEEPALIVE_TRACKED_INTERVAL` from everything that carries it: the driver's init block and every reader in `tools/unattended/unattended.sh`, `tools/unattended/.unattended.conf.example`, `tools/unattended/kit.toml`'s optional keys, this repository's `.unattended.conf`, the protocol §8 row, the Skill, verbs and protocol templates and their rendered copies, `help/idle-wake.md`, and the feature dossier. Afterwards `git grep KEEPALIVE_TRACKED_INTERVAL` names only records under `memory/builds/`.
2. `--wake` keeps its HEALTHY/FULL verdicts, reasons and order exactly as unit 2's first acceptance ledger records them. Its cadence field always names the base `KEEPALIVE_INTERVAL`, or `undeclared` when that is blank. The spec states the line's exact new form and arms it.
3. The suite arms that set or read the tracked key are retired or rewritten to the base-cadence answer, with the assertion floor moved by the measured count.
4. `help/idle-wake.md`'s command block is marked as the other help pages mark a block that runs a kit by its path in gov's checkout, e.g. `<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->` (as on `help/agent-limit.md`).
5. Any size row unit 2 raised that now has headroom is left as it is. Lowering a row is the owner's, per `tools/template-size-limits.txt`.

### brief:acceptance

The `policy check` leg's `arm_legacy_homes` prints no finding. The `help page commands` leg prints no finding for `help/idle-wake.md`. `git grep -n KEEPALIVE_TRACKED_INTERVAL -- tools help .claude .unattended.conf memory/guides memory/map` prints nothing. `--wake`'s verdict lines are unchanged in unit 2's setups, apart from the cadence field the spec states. Every touched pre-existing check keeps its verdict and bytes.

### brief:gates

The merge bar at the close.

### brief:non-goals

No change to `--wake`'s verdicts, reasons or their order. No new key anywhere. `KEEPALIVE_INTERVAL` stays as it is.

### task:reuse

`tools/memory-tree/gen_build_index.py#check_staged_render` · `tools/memory-tree/gen_build_index.py#check_index_input` · `tools/unattended/unattended.sh#derive_spec_token_key` + gate-fingerprint.sh · `tools/unattended/stop-guard.js#runLiveness` · `tools/workflows/unattended-unit.js#DRIVER_STEPS` · reuse_lookup found no generic caching seam

### card:route

- build: aLightenedLoop
- unit: TOOL-aLightenedLoop-2 · spec memory/builds/aLightenedLoop/spec/2026-11-14-spec-TOOL-aLightenedLoop-2.md
- brief: memory/builds/aLightenedLoop/prompts/2026-11-14-prompt-TOOL-aLightenedLoop-2-bar-fix.md
[/memory/builds/aLightenedLoop/prompts/2026-11-15-prompt-TOOL-aLightenedLoop-7-1-spec-writer.md]
