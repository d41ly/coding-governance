**Serves:** journal PLAY-dOrderedCharter-34

# gov-spec-writer handoff — PLAY-dOrderedCharter-34

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-34 path=memory/builds/dOrderedCharter/prompts/2026-11-09-prompt-PLAY-dOrderedCharter-34-1-spec-writer.md role-sha=90b89c43f238 task-sha=f65df8edd8ce -->

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
- unit: PLAY-dOrderedCharter-34 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-34-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dOrderedCharter/prompts/2026-11-09-prompt-PLAY-dOrderedCharter-34-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-34`.
Not supplied, optional: `input:code`.

### brief:goal

Revise spec 34 so a builder can build it as written over this tree.

### brief:items

1. **The census and the core meta-check.** The practice catalogue reads a row's `rules` as `<tag>.<rule>` tags that a leg's `enforces`
   pairs with, and `tools/playbook/core.py#check_meta` joins them. Read that way, the census predicate rules `practice.writing` gov-only:
   its line names no path, every leg enforcing its rules is an exempt leg in `tools/govkit/registry.toml`, and no role cites it. S8 then
   moves its row, leaving its rule tags in `tools/gate-legs.json` that no row holds, which the meta-check reds, and that check refuses an
   `enforces` tag outside the principle and practice namespaces. Say which reading of "a leg names its tag in `enforces`" the census uses,
   exact tag or tag plus its rule tags; under the second, what happens to a moved row's rule tags and its pending rows, with
   `tools/gate-legs.json` among S8's readers. Under the first, say why a row whose rules four legs enforce reads as having no evidence.
2. **The project block and `adopter_rules`.** Any moved row becomes a level-0 `repo.` unit in gov's overlay, and composition step 2 stops
   rendering `[charter] adopter_rules` once the overlay holds one. Gov's adopter rules reach the overlay only through unit 31, which
   builds after this unit, so they would drop out of gov's charter, against AC1 and S1. Say either that the project block renders the
   adopter rules beside the level-0 units until unit 31 converts them, or that this unit converts gov's own adopter rules itself.
3. **Level-3 placement.** No template holds a unit slot or a repo marker pair; S2 and step 3 do not say which level-3 document a level-3
   `repo.` unit renders into, nor how the marked part avoids printing a unit twice. `tools/playbook/overlay.py#derive_slot_units` already
   places an edge-free `repo.` unit into any slot its scope selects; say whether this unit reuses it.
4. **Every reader claim is a grep**, at HEAD, for anything this revision moves or retires.

Resolve each choice under the fork rule and record it in section 8.

In the spec:

- Bump the **Status:** rev by one, dated 2026-11-09, status kept `DEFERRED`, with one history line naming this brief.
- Each listed `path:line` citation stays byte for byte, and new text cites code as `path#symbol`, outside the acceptance bullets, which
  spell plain tracked paths and never a file not yet tracked. New text names a section in words, and a check by what it checks. A sha
  written in section 2 stays out of backticks. Every new fact a record states is pinned, keyed or marked PINNED or DERIVED; a number
  beside a unit or spec number reads as a fact, so name a unit by its id. Every function name it mints passes
  `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.
- Any retirement word in section 2 owes its Readers clause.

### brief:acceptance

- Spec 34 builds as written over HEAD, and each change has a history line.
- Your return names the pick for each item, and any fork left open because its surviving option trips the second or third veto.

### brief:gates

Memory hygiene, as your role runs it.

### brief:non-goals

- No code. No edit to another spec, except a mirrored edge on spec 31 if a pick hands it work.

### input:spec

memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-34 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-34.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-34-build-brief.md
[/memory/builds/dOrderedCharter/prompts/2026-11-09-prompt-PLAY-dOrderedCharter-34-1-spec-writer.md]
