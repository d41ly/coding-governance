**Serves:** journal KICK-dKeptSession-1

# gov-spec-writer handoff — KICK-dKeptSession-1

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=KICK-dKeptSession-1 path=memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-2-spec-writer.md role-sha=91ec0ce505aa task-sha=64f7642a6961 -->

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
- build: dKeptSession
- unit: KICK-dKeptSession-1 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-2-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-1`.
Not supplied, optional: `input:code`.

### brief:prompt

> /unattended dKeptSession

### brief:goal

KICK-dKeptSession-1's builder returned a DIVERGENCE (run `wf_c7d6ba36-6f3`) at rev-5 and committed nothing. Two gaps
the design depends on: (1) the fixture cases that reach the loop kit (`presets-core-only`, and the load halves of
`presets-complete` that need `guard.py`) copy the loop and playbook kits into the scratch repository inside the
`--fixture` process, so the guard trace records each read, and the `policy fixtures` guard in `tools/gate-legs.json`
covers neither `tools/loop/` nor `tools/playbook/layers.toml`, so every such read grades WRONG; the spec's Files
touched calls the `tools/gate-legs.json` edits already satisfied, and they are not. (2) Nothing says what
`arm_presets` does where the loop kit does not resolve, as in `adopter-fresh-target`, whose install closure holds
policy, run-gates and memory-tree only: under S4 the load there exits 2 naming the kit, and with `empty = "finding"`
the arm would red that adopter's `policy check`. Revise the spec to the main loop's rulings below.

### brief:items

1. F-guard: Files touched gains `tools/gate-legs.json`: the `policy fixtures` guard gains the paths the fixture's copy reads, the loop kit and the playbook kit's `layers.toml` (the narrowest entries that cover every read the guard trace records; a whole-kit entry where the copy is the whole kit). Correct the rev-5 claim that the edit is already satisfied, and name the leg line's legs this path trips.
2. F-unresolved-loop: add to the open-questions section, resolved by the main loop at rung 3: where `resolve_kit_dir("loop", ...)` misses, the arm's two load halves print an announced skip in the shape the loop kit's own cross-kit reads use (`not graded · the loop kit does not resolve`), never a finding, so an adopter without the loop kit reads its `policy check` clean with the halves announced. S5, the readiness checklist and the README's "Each arm in an adopter" row say so, and a criterion observes it in the fresh target.
3. Re-cite every line you change as `path#symbol`, keep the spec within the live-spec size cap, pin every figure with DERIVED or PINNED, and leave no fork open.

### brief:acceptance

The spec at rev-6 carries both rulings and one revision-log line naming this brief by its file stem;
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-1` report nothing.

### brief:gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### brief:non-goals

No product code, no commit, no index render, no status flip (the spec stays INPROGRESS), and no spec other than
KICK-dKeptSession-1's. Other writers are re-grounding later orders' specs at the same time: read them, never write them.

### input:spec

memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md

### task:reuse

each spec's §10 names its seam; probes run: `reuse_lookup.py` per spec at re-ground; recall terms below.

### card:route

- build: dKeptSession
- unit: KICK-dKeptSession-1 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-1.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md
[/memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-1-2-spec-writer.md]
