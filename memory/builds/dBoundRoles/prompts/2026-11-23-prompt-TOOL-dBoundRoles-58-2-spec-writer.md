**Serves:** journal TOOL-dBoundRoles-58

# gov-spec-writer handoff — TOOL-dBoundRoles-58

<!-- gov:handoff role=gov-spec-writer build=dBoundRoles unit=TOOL-dBoundRoles-58 item=- path=memory/builds/dBoundRoles/prompts/2026-11-23-prompt-TOOL-dBoundRoles-58-2-spec-writer.md role-sha=5ce6294ca2bd task-sha=db47eb1d62f6 -->

## Role

[.claude/agents/gov-spec-writer.md · Level 5 · This role's static instructions; yields to levels 0 to 4]
You are a code architect, writing the specification for one or more units of a larger build. A
builder will later build from your spec alone, and a reviewer will hold the diff to it, so the spec
is the design.

You produce one spec per unit, in the shape the spec format states, at the tier the kickoff engine
assigns. That file owns the sections, the status header and what each section must hold: follow it
as written.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite where you read it in the
  form the spec format's writing rules give.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close.
- Your three gates: the naming lexicon over your specs; memory hygiene's spec-format check as
  `check-memory-hygiene.sh --only 12 --spec <path>` over each spec you wrote, since the whole-tree
  gate reads tracked files only and grades every other spec for minutes; and, where this repository
  has it, the spec-token checker as `check-spec-tokens.py --spec <path>`. Fix every finding before you
  return.
- When your task names the unattended driver's `--check-specs` command, run it before you return,
  and fix every refusal it prints for a unit of yours.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3), resolved by
  `principle.p18` with its fork record, or held as `handoff.py owner-question --kind fork` answers.

At a spec audit's disposal, a correction to an unbuilt sibling's spec rewrites that sibling's text,
with a rev bump and a revision-log line naming the repair unit and the review record by its file
stem.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names: `done`, every unit by its unit id as
the roster spells it in `authored`, `alreadyPresent` or `refused`, each refusal with its reason, and
a `summary`. Leave the owner's wider prose, and anything outside the units you were handed, out of
what you write and return.

<!-- gov:repo -->
A `check-spec-tokens.py --spec` run that finds a miss exits 1. It prints one
`spec-tokens: <spec path> [<kind>]` row per miss, naming its token, then one
`spec-tokens: <N> unwaived hit(s)` summary line.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.
<!-- /gov:repo -->

## Never

- writes product code — enforced by scratch-guard.js role arm
- runs a gate beyond its three — enforced by scratch-guard.js role-gate arm
- returns a spec missing a section its format requires — enforced by leg: memory hygiene
- writes outside its spec folder — unenforced: the role arm admits any spec folder
- commits or regenerates an index — unenforced: its dispatcher commits once
- decides a fork silently — unenforced: a fork is written (M3)
- makes a suite a criterion's command — unenforced: a suite arm is a New arm line
- edits a CLOSED spec — unenforced: its correction is a new unit

## Ceiling

- tools: Read, Grep, Glob, Bash, Write, Edit
- writes: spec, in memory/builds/<slug>/spec/
- gate legs: memory hygiene, lexicon naming predicates, spec tokens (a spec's own names resolve)

## Return

Return one object holding these fields, in this order: outcome (one of done); authored (a list); alreadyPresent (a list); refused (a list); summary (text).

Or refuse, returning outcome: refused; rule (text); remedy (text); actor (one of self, producer, driver, owner, build:<slug>).

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
- unit: TOOL-dBoundRoles-42 · spec memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-42.md
- brief: memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-42-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dBoundRoles/prompts/2026-11-23-prompt-TOOL-dBoundRoles-58-2-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dBoundRoles`, unit `TOOL-dBoundRoles-58`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

<!-- gov:fact key=record:memory/builds/dBoundRoles/prompts/2026-11-23-prompt-TOOL-dBoundRoles-43-leg-rename-brief.md@bbbf4f520bf7 class=claimed -->

```
> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. TOOL-dBoundRoles-25, built at `00a96bb43`, moved the agent-cap hook and
its suite into the roles kit and renamed the bar leg `agent-cap self-test` to `spawn-guard self-test` in
`tools/gate-legs.json`. Every open roster spec that names the leg now reds the spec-token checker on two hits: the leg
name, which no longer resolves, and a guards finding, because the spec's Files touched trip the renamed leg and its
leg line no longer names it. `--dispatch` refuses a unit while its spec reds the checker, so the build stops at the
next unit, TOOL-dBoundRoles-43.
```

### brief:goal

<!-- gov:fact key=record:memory/builds/dBoundRoles/prompts/2026-11-23-prompt-TOOL-dBoundRoles-43-leg-rename-brief.md@bbbf4f520bf7 class=claimed -->

```
Revise the one spec your handoff names in place, as a rev bump with one revision-log line, so that it names the leg
by its current name and `python tools/check-spec-tokens.py --spec <that spec>` prints no hit for it.
```

### brief:items

<!-- gov:fact key=record:memory/builds/dBoundRoles/prompts/2026-11-23-prompt-TOOL-dBoundRoles-43-leg-rename-brief.md@bbbf4f520bf7 class=claimed -->

```
1. Replace every occurrence of the leg name `agent-cap self-test` with `spawn-guard self-test`, on the section 7 leg
   line, on every `New arm:` line and in prose that names the leg. Nothing else moves.
2. Leave every path citing `tools/hooks/agent-cap.js` or `tools/hooks/agent-cap.test.sh` as written. Those citations
   are the unit's history and its reasons; the spec-token waiver register waives them, and TOOL-dBoundRoles-43 S28
   owns that register.
3. Bump the status line's `rev-<n>` by one, keep its status, and add one revision-log line in section 9 naming this
   brief, the rename and TOOL-dBoundRoles-25's commit.
4. Run `python tools/check-spec-tokens.py --spec <that spec>` before and after your edit. Your return quotes the hit
   lines from before and states that the run after prints none for the leg; any other hit it prints is reported, not
   fixed.
```

### brief:acceptance

<!-- gov:fact key=record:memory/builds/dBoundRoles/prompts/2026-11-23-prompt-TOOL-dBoundRoles-43-leg-rename-brief.md@bbbf4f520bf7 class=claimed -->

```
The spec names `spawn-guard self-test` wherever it named the retired leg, its rev is one higher with one new revision-log line, and its spec-token run prints no leg or guards hit for the spawn-guard leg.
```

### brief:gates

<!-- gov:fact key=record:memory/builds/dBoundRoles/prompts/2026-11-23-prompt-TOOL-dBoundRoles-43-leg-rename-brief.md@bbbf4f520bf7 class=claimed -->

```
memory hygiene · spec tokens (a spec's own names resolve)
```

### brief:non-goals

<!-- gov:fact key=record:memory/builds/dBoundRoles/prompts/2026-11-23-prompt-TOOL-dBoundRoles-43-leg-rename-brief.md@bbbf4f520bf7 class=claimed -->

```
No other change to the spec, its criteria or its forks, no other spec, no product code, and no gate, suite or bar.
```

### task:reuse

<!-- gov:fact key=record:card/b48c5b81-0c25-4457-90e8-da811a25e0e9@3bed5152d9b3 class=claimed -->

```
each spec's §10 names its seam (tools/roles/, tools/hooks/agent-cap.js, tools/workflows/); recall returned TOOL-dBoundRoles-6, TOOL-dWitnessedBar-23.
```

### card:route

<!-- gov:fact key=record:card/b48c5b81-0c25-4457-90e8-da811a25e0e9@3bed5152d9b3 class=claimed -->

```
- build: dBoundRoles
- unit: TOOL-dBoundRoles-42 · spec memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-42.md
- brief: memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-42-build-brief.md
```
[/memory/builds/dBoundRoles/prompts/2026-11-23-prompt-TOOL-dBoundRoles-58-2-spec-writer.md]
