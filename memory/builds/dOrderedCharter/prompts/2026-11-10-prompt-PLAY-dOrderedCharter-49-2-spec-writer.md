**Serves:** journal PLAY-dOrderedCharter-49

# gov-spec-writer handoff — PLAY-dOrderedCharter-49

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-49 path=memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-2-spec-writer.md role-sha=90b89c43f238 task-sha=c08c619cfbf2 -->

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
[memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-2-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-49`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:goal

Revise spec 49's AC26 so its command runs over HEAD and observes the code input.

### brief:items

1. **Where you write.** Edit only the scratch copy at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold49/2026-10-24-spec-PLAY-dOrderedCharter-49.md`;
   write nothing under the repository.
2. **The defect, observed at `8a9c55b65`:** AC26's command, run with `--input prompt=` and no `--input spec=`, prints
   `handoff: input:spec — not supplied; pass --input spec=<value>` and renders nothing, so the criterion can never observe
   `input:code`. With `--input spec=` naming spec 49's tracked path and `--input prompt=` naming
   `memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-precheck-brief.md`, the render carries
   `### input:code`, and without `--input code=` it prints the `Not supplied, optional` line naming it. Confirm both.
3. Restate AC26 so its command names every input the render requires, each backticked span on one line and every path tracked.
4. The spec-token check grades a live spec's acceptance bullets word by word: no acceptance command whose words include an untracked
   path, no `path#symbol` in an acceptance bullet, no suite as the observation.

Bump the **Status:** rev to rev-9, dated 2026-11-10, status kept `DEFERRED`, with a revision-log line naming this brief and AC26.

### brief:acceptance

- AC26's command, as written, renders over HEAD and its output carries `input:code`.

### brief:gates

None run on the repository: this is a scratch edit. The main loop sweeps the spec and runs the spec-token check with it live.

### brief:non-goals

- No code. No edit outside the scratch copy. No other criterion changes.

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-31 · spec memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-02-prompt-PLAY-dOrderedCharter-31-build-brief.md
[/memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-49-2-spec-writer.md]
