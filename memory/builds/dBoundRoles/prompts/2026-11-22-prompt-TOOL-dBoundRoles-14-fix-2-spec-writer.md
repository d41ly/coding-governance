**Serves:** journal TOOL-dBoundRoles-14

# gov-spec-writer handoff — TOOL-dBoundRoles-14

<!-- gov:handoff role=gov-spec-writer build=dBoundRoles unit=TOOL-dBoundRoles-14 path=memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-fix-2-spec-writer.md role-sha=91ec0ce505aa task-sha=2c9b21e5737a -->

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
- build: dBoundRoles
- unit: TOOL-dBoundRoles-14 · spec memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md
- brief: memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-fix-2-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dBoundRoles`, unit `TOOL-dBoundRoles-14`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 14's second builder (run `wf_37ac53bc-1d1`) stopped before its code
on rev-6 and returned one divergence against §4 "The binding join": the index carries no grouping of a unit's selector
rows. Its return is `memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-14-2-builder-return.md`.

### brief:goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md` to rev-7 so §4 "The binding join", S5
and AC2 state a join the code at HEAD can build.

### brief:items

1. Record the fork as §8 F7 with the return's three options, RESOLVED (agent, 2026-11-22, delegated): (a),
   `check_role_bindings` re-parses each indexed unit manifest's blob through `instruction_units.parse_unit_rows`, which
   `gov_tag.py` already imports, rung 3, reuse of a seam already imported, with `widens: none · relaxes: none`. (b)
   loses for widening Files touched into `instruction_units.py` and moving the red locations `check_namespace_joins`
   prints for every selector; (c) names no key the code carries.
2. Rewrite §4 "The binding join", S5 and AC2 to that resolution: where the unit rows come from, how a unit's `role.` and
   `practice.` selectors are grouped, and what AC2 observes. Keep AC2's number; keep it passable on a correct build at
   HEAD and red on the break it names. Files touched and §10 agree with it.
3. Change nothing else. Keep the status `INPROGRESS`. One revision-log line names this brief by its file stem and the
   return by its file stem.
4. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### brief:acceptance

The spec is rev-7 with F7 marked resolved as item 1 states; §4, S5 and AC2 agree with it; both checks exit 0.

### brief:gates

memory hygiene · spec tokens (a spec's own names resolve)

### brief:non-goals

No other spec. No product code. No change beyond the binding join and what it forces.

### task:reuse

each spec's §10 names its seam (tools/roles/, tools/hooks/agent-cap.js, tools/workflows/); recall returned TOOL-dBoundRoles-6, TOOL-dWitnessedBar-23.

### card:route

- build: dBoundRoles
- unit: TOOL-dBoundRoles-14 · spec memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md
- brief: memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-build-brief.md
[/memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-fix-2-spec-writer.md]
