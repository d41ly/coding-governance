**Serves:** journal TOOL-dSettledStage-1

# gov-spec-writer handoff — TOOL-dSettledStage-1

<!-- gov:handoff role=gov-spec-writer build=dSettledStage unit=TOOL-dSettledStage-1 path=memory/builds/dSettledStage/prompts/2026-11-19-prompt-TOOL-dSettledStage-1-1-spec-writer.md role-sha=91ec0ce505aa task-sha=be33c6143ac4 -->

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
- You may run the naming lexicon over your specs, and grade each spec you wrote with memory
  hygiene's spec-format check as `check-memory-hygiene.sh --only 12 --spec <path>`. The whole-tree
  gate reads tracked files only, so it never grades a spec you have not committed, and it grades
  every other spec for minutes. Where this repository has it, run the spec-token checker as
  `check-spec-tokens.py --spec <path>` over each spec you wrote. Fix every finding either check
  names before you return. You run no other gate.
- When your task names the unattended driver's `--check-specs` command, run it before you return;
  it prints each refusal `--dispatch` would make from your specs, in its words, and you fix every
  one naming a unit of yours.
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
- build: dSettledStage
- unit: TOOL-dSettledStage-1 · spec memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-1.md
- brief: memory/builds/dSettledStage/prompts/2026-11-19-prompt-TOOL-dSettledStage-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/dSettledStage/prompts/2026-11-19-prompt-TOOL-dSettledStage-1-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dSettledStage`, unit `TOOL-dSettledStage-1`.
Not supplied, optional: `input:code`.

### brief:prompt

> pinned-facts: red · memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-1.md · unpinned fact `2 records`: pin it on its line (an id, a path:line, PINNED or DERIVED)

### brief:goal

Clear the one `writing practice (records and units)` hit the pass legs printed on this spec after unit 1's build
commit `864d85d42`, changing nothing else.

### brief:items

1. §3's line 56, "there, unit 2 records it as a follow-up.", reads "2 records" as a count. It is not a fact:
   reword it so no number sits before a counted noun, for example "TOOL-dSettledStage-2 registers it as a
   follow-up", keeping its meaning.
2. Bump the spec to rev-2 with one §9 line naming this record and the hit.

### brief:acceptance

`bash tools/run-gates/pass-legs.sh --base 6daf04180` prints no `pinned-facts` line naming this spec. That run is
the main loop's; the writer confirms with the writing-practice reader its role admits.

### brief:gates

`writing practice (records and units)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

### brief:non-goals

No change to any other section's meaning, the status, the date or any other spec. Do not commit and do not stage.

### input:spec

memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-1.md

### task:reuse

the regen arms 24–33 in `tools/push-main.test.sh` (aPrimedIndex) for the fixture shape · `sh_hygiene.py`'s class registry and shrink-only counted registry for the gate · `reuse_lookup.py` named no seam that checks a staged diff.

### card:route

- build: dSettledStage
- unit: TOOL-dSettledStage-1 · spec memory/builds/dSettledStage/spec/2026-11-19-spec-TOOL-dSettledStage-1.md
- brief: memory/builds/dSettledStage/prompts/2026-11-19-prompt-TOOL-dSettledStage-1-brief.md
[/memory/builds/dSettledStage/prompts/2026-11-19-prompt-TOOL-dSettledStage-1-1-spec-writer.md]
