**Serves:** journal TOOL-aCarriedStop-10

# gov-spec-writer handoff — TOOL-aCarriedStop-10

<!-- gov:handoff role=gov-spec-writer build=aCarriedStop unit=TOOL-aCarriedStop-10 path=memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-1-spec-writer.md role-sha=a3bc1199e30f task-sha=ef5536a36e2f -->

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
- build: aCarriedStop
- unit: TOOL-aCarriedStop-1 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md
- unit: TOOL-aCarriedStop-2 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-2.md
- unit: TOOL-aCarriedStop-3 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-3.md
- unit: TOOL-aCarriedStop-9 · spec memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-9.md
- brief: memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aCarriedStop`, unit `TOOL-aCarriedStop-10`.
Not supplied, optional: `input:spec`.

### brief:prompt

> raise the routed-commits ceiling and land it

### brief:goal

The leg `install-prefix (shipped surface)` exits 0 on this build's tree, so the close's bar and the push bar can land it.

### brief:items

1. `tools/chain-packet.py` reaches the memory-tree kit's `tree_lib.py` through the canonical `resolve_kit_dir` block, never through a spelled `"memory-tree"` path segment [planned TOOL-aCarriedStop-10]
2. `tools/chain-packet.test.sh` loads `tree_lib` through the door's resolved kit directory, never through a spelled `"memory-tree"` path segment [planned TOOL-aCarriedStop-10]

### brief:acceptance

- `bash tools/check-install-prefix.sh` exits 0 and lists no line of `tools/chain-packet.py` or `tools/chain-packet.test.sh`.
- The same checker run at the parent's tree lists the three lines and exits 1.
- With the kit absent from beside the door, the door still prints its `shortcuts off` line and runs the instrument as it stands.

### brief:gates

The merge bar at the close; `bash tools/check-install-prefix.sh` in the pass.

### brief:non-goals

- No change to what the door reads, batches or prints, beyond how it finds the kit.
- No change to `tools/check-install-prefix.sh` or to any other kit's spellings.
- No path under `memory/builds/aBatchedPacket/` or `memory/builds/dDeclaredLoop/`.

### task:reuse

write_chain_round, derive_chain_verdict and check_chain_dispatch in tools/unattended/unattended.sh.

### card:route

- build: aCarriedStop
- unit: TOOL-aCarriedStop-1 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md
- unit: TOOL-aCarriedStop-2 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-2.md
- unit: TOOL-aCarriedStop-3 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-3.md
- unit: TOOL-aCarriedStop-9 · spec memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-9.md
- brief: memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-brief.md

### input:code

# Brief — aCarriedStop: unit 10, the chain-packet door's kit-path spellings routed through the resolver

**Serves:** research TOOL-aCarriedStop-10

Adopted at once under M10 on the third close of 2026-11-14, which the install-prefix leg blocked; the owner's order "raise the routed-commits ceiling and land it" stands as the mandate.

## The prompt

> raise the routed-commits ceiling and land it

## The brief

### Goal
The leg `install-prefix (shipped surface)` exits 0 on this build's tree, so the close's bar and the push bar can land it.

### Items
1. `tools/chain-packet.py` reaches the memory-tree kit's `tree_lib.py` through the canonical `resolve_kit_dir` block, never through a spelled `"memory-tree"` path segment [planned TOOL-aCarriedStop-10]
2. `tools/chain-packet.test.sh` loads `tree_lib` through the door's resolved kit directory, never through a spelled `"memory-tree"` path segment [planned TOOL-aCarriedStop-10]

### Acceptance
- `bash tools/check-install-prefix.sh` exits 0 and lists no line of `tools/chain-packet.py` or `tools/chain-packet.test.sh`.
- The same checker run at the parent's tree lists the three lines and exits 1.
- With the kit absent from beside the door, the door still prints its `shortcuts off` line and runs the instrument as it stands.

### Gates
The merge bar at the close; `bash tools/check-install-prefix.sh` in the pass.

### Non-goals
- No change to what the door reads, batches or prints, beyond how it finds the kit.
- No change to `tools/check-install-prefix.sh` or to any other kit's spellings.
- No path under `memory/builds/aBatchedPacket/` or `memory/builds/dDeclaredLoop/`.

### Limitations
- The red is inherited: `bash tools/check-install-prefix.sh` at origin/main `0578adb73` lists the same three lines and exits 1.
- The bar reads it OWN only because its grader sits directly under `tools/`, so this build's edit to `tools/gate-legs.json` touches its comparator.

### Reuse
- The `resolve_kit_dir` block, byte-identical to `tools/lib/resolve_kit_dir.py` and gated, as `tools/check-spec-tokens.py` carries it for the same kit.

## Drawn from the session

- The third close's bar at `1f732d9ba` and the checker's run at `0578adb73`, both taken by the main loop of this session.

## Owner confirmation

The order is the owner's own words in chat; nothing else was asked.
[/memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-1-spec-writer.md]
