**Serves:** journal TOOL-aBriskDeclaration-1

# gov-spec-writer handoff — TOOL-aBriskDeclaration-1

<!-- gov:handoff role=gov-spec-writer build=aBriskDeclaration unit=TOOL-aBriskDeclaration-1 path=memory/builds/aBriskDeclaration/prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-3-spec-writer.md role-sha=a3bc1199e30f task-sha=50f56d3200f4 -->

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
- Verify every claim about current code by reading that code, and cite it by `path#symbol` or the
  blob-pinned line `<path>@<oid>:<n>`. A claim you did not verify is a claim you do not make.
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
- build: aBriskDeclaration
- unit: TOOL-aBriskDeclaration-1 · spec memory/builds/aBriskDeclaration/spec/2026-11-14-spec-TOOL-aBriskDeclaration-1.md
- brief: memory/builds/aBriskDeclaration/prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aBriskDeclaration/prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-3-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aBriskDeclaration`, unit `TOOL-aBriskDeclaration-1`.
Not supplied, optional: `input:code`.

### brief:prompt

> F1 rollout: Live, no switch (Recommended)

> F2 arm: Add its own arm

The owner's answers, 2026-11-14, to the two questions the session's question tool put from the spec's §8.

### brief:goal

The owner answered the spec's two open questions on 2026-11-14, asked through the session's question tool. F1, "Does this land live, or dark behind a default-off switch?": "Live, no switch (Recommended)". F2, "Does the generator-pairing refusal owe a behavioural arm of its own?": "Add its own arm". Mark both forks RESOLVED with the owner's pick, and make F2's arm part of the spec: a traced driver-suite arm in which the dispatch is refused by the index-declared-with-its-generator refusal after the checker has started, showing the checker's `init_bounded` line, the refusal, a `read_bounded` line after it and no `kill`, and the refusal text with no spec-token line. Bump the spec's rev and add a revision-log line naming this record by its file stem. The code built at `4fed38fe1` and `fc4c62bfa` already follows F1's pick and stays as it is; only the new arm, its `New arm:` line and the criterion it covers are added.

### brief:items

1. In `memory/builds/aBriskDeclaration/spec/2026-11-14-spec-TOOL-aBriskDeclaration-1.md`, F1 and F2 each carry `RESOLVED (owner, 2026-11-14): <the pick>` in their own span.
2. A criterion for the generator-pairing arm, in the shape of AC4, and its `New arm:` line under §7, with the fixture it needs: a `GENERATED_INDEXES` pair declared for the suite's fixture, and a dispatch whose `--writes` names the index while a sibling or the same declaration names its generator.
3. The status stays INPROGRESS; the builder sets CLOSED after the arm lands.
4. Stage the spec and clear `python tools/check-spec-tokens.py --spec` over it. Do not commit.

### brief:acceptance

- The spec's two forks read RESOLVED with the owner's picks, its rev is 2, and its revision log names this record.
- The new criterion names an observation of the driver suite's traced dispatch, and its `New arm:` line names the base at which it reds.

### brief:gates

`check-spec-tokens.py --spec` over the spec.

### brief:non-goals

- Any change to the code at `4fed38fe1` and `fc4c62bfa` beyond the arm and its fixture.
- A conf key or switch: F1 is live.
- `memory/builds/dDeclaredLoop/`, its run's worktree and its branch.

### input:spec

memory/builds/aBriskDeclaration/spec/2026-11-14-spec-TOOL-aBriskDeclaration-1.md

### task:reuse

tools/unattended/unattended.sh#init_bounded and #read_bounded, the seam TOOL-aBriskPreflight-4 split; #read_preflight_probes as the discard precedent.

### card:route

- build: aBriskDeclaration
- unit: TOOL-aBriskDeclaration-1 · spec memory/builds/aBriskDeclaration/spec/2026-11-14-spec-TOOL-aBriskDeclaration-1.md
- brief: memory/builds/aBriskDeclaration/prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-brief.md
[/memory/builds/aBriskDeclaration/prompts/2026-11-14-prompt-TOOL-aBriskDeclaration-1-3-spec-writer.md]
