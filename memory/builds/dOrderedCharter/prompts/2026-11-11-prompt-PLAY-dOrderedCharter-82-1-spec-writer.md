**Serves:** journal PLAY-dOrderedCharter-82

# gov-spec-writer handoff — PLAY-dOrderedCharter-82

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-82 path=memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-1-spec-writer.md role-sha=90b89c43f238 task-sha=23d983a64100 -->

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
- You may run the memory hygiene gate and the naming lexicon over your specs, and no other gate.
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
- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-81 · spec memory/builds/dOrderedCharter/spec/2026-11-11-spec-PLAY-dOrderedCharter-81.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-81-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-82`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:goal

Write spec PLAY-dOrderedCharter-82, a micro-spec for one mechanical fix unit at order 44 that clears the python-reads guard red.

### brief:items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold82/2026-11-11-spec-PLAY-dOrderedCharter-82.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md` for a Tier-1 micro-spec, as PLAY-dOrderedCharter-81 is
   written; carry its `**Derived:**` binding line; status line `DEFERRED · rev-1 · 2026-11-11 · node a · Tier-1 · base <HEAD short
   sha> · streams playbook · order 44 · advances PLAY-dOrderedCharter-38`.
2. **The red.** The `python reads (a name never bound, an import outside its guard)` leg prints fourteen lines of the form
   `py-reads: RED guard · govkit acceptance matrix · tools/memory-tree/<module>.py is imported and outside its guard`. The
   `govkit acceptance matrix` leg's guard in `tools/gate-legs.json` is `{prefix}/govkit/`, `{prefix}/playbook/`,
   `{prefix}/check-microformats.sh`, `{prefix}/check-line-length.sh` and `.lexicon.conf`; since PLAY-dOrderedCharter-78 the
   matrix's scratch install carries the renderer's requirement closure, so the leg imports memory-tree modules. Confirm the
   fourteen at HEAD by running the reads checker's own reader, and whether any other kit directory (the policy kit's) is imported
   too; name the narrowest guard addition that covers them, read the guard grammar the other legs use, and say whether the
   matrix leg's ceiling or a guard-parity row moves with it.
3. Criteria observe the reads leg's verdict line going green over the tree. The spec-token check grades a live spec's acceptance
   bullets word by word: no acceptance command whose words include an untracked path, no `path#symbol`, no suite as the
   observation, each backticked span on one line, every tripped leg on the gates line. Every new fact pinned.

### brief:acceptance

- Spec 82 builds as written over HEAD, and its criterion observes the python-reads leg going green.

### brief:gates

None run on the repository: this is a scratch write.

### brief:non-goals

- No code. No edit outside the scratch copy. Nothing outside this red.

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-81 · spec memory/builds/dOrderedCharter/spec/2026-11-11-spec-PLAY-dOrderedCharter-81.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-81-build-brief.md
[/memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-1-spec-writer.md]
