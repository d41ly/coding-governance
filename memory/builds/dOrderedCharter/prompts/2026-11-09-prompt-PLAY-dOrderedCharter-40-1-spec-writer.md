**Serves:** journal PLAY-dOrderedCharter-40

# gov-spec-writer handoff — PLAY-dOrderedCharter-40

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-40 path=memory/builds/dOrderedCharter/prompts/2026-11-09-prompt-PLAY-dOrderedCharter-40-1-spec-writer.md role-sha=90b89c43f238 task-sha=5f67208646e7 -->

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
- unit: PLAY-dOrderedCharter-31 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-31-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dOrderedCharter/prompts/2026-11-09-prompt-PLAY-dOrderedCharter-40-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-40`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:goal

Revise spec 40 so a builder can build it as written over this tree, once unit 37 lands as its spec rev-7 says.

### brief:items

1. **Where you write.** A unit is building, so edit only this scratch copy and write nothing under the repository:
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold40/2026-10-24-spec-PLAY-dOrderedCharter-40.md`
2. **Unit 37's hand-off changed.** Spec 37 rev-7, committed in this tree, lands three reference pages at its pass and moves the units
   reference row, its page and every row's `unit` field to a later commit after this unit's gov unit rows are tracked. Spec 40's scope,
   its criterion that says the reference check exits 0 over four pages, and its consumes-from text naming the four reference rows no
   longer hold at this unit's pass; `tools/playbook/references.toml` may leave Files touched if this unit only reads it. Fold them, and
   mirror the edge.
3. **Unit 33's later commit.** Unit 33's fork F5 lands the `unit` class row in `tools/govkit/surface-classes.toml` and the `unit` row in
   `tools/govkit/usage.toml` once a gov unit row is tracked, which this unit writes first. Say whether this unit's pass or a commit right
   after it carries those two rows, under whose dispatch, and with which of unit 33's criteria they let the close observe.
4. **Pre-check every claim against HEAD.** For every symbol, file, row, signature, return shape, key or count the spec names, read the
   code; probe with `python -I` in a scratch folder of your own where a read cannot settle it. Units landed since the spec's last
   revision include 29, 23, 32, 33, 46, 35, 36 and 34, which changed the overlay, its readers, the composer, the renderer and the charter.
   PLAY-dOrderedCharter-31 is parked and will not land in this run, so nothing in this spec may rest on it.
5. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

Resolve each choice under the fork rule and record it in section 8.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte unless an item above corrects it, and new text cites code as `path#symbol`,
  outside the acceptance bullets, which spell plain tracked paths and never a file not yet tracked. New text names a section in words,
  and a check by what it checks. A sha written in section 2 stays out of backticks, and a Readers clause names readers only, never the
  command that found them. Every new fact is pinned, keyed or marked PINNED or DERIVED; name a unit by its id. Every function name it
  mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- Any retirement word in section 2 owes its Readers clause.

### brief:acceptance

- Spec 40 builds as written over HEAD with unit 37 landed, every edge it gains is named in your return for the main loop, and each
  change has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### brief:gates

None run: this is a scratch edit. The main loop sweeps the spec before its dispatch.

### brief:non-goals

- No code. No edit outside the scratch copy.

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-31 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-31-build-brief.md
[/memory/builds/dOrderedCharter/prompts/2026-11-09-prompt-PLAY-dOrderedCharter-40-1-spec-writer.md]
