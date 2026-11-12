**Serves:** journal PLAY-dOrderedCharter-87

# gov-spec-writer handoff — PLAY-dOrderedCharter-87

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-87 path=memory/builds/dOrderedCharter/prompts/2026-11-12-prompt-PLAY-dOrderedCharter-87-1-spec-writer.md role-sha=a3bc1199e30f task-sha=1590fb32aa5b -->

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
- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-84 · spec memory/builds/dOrderedCharter/spec/2026-11-12-spec-PLAY-dOrderedCharter-84.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-12-prompt-PLAY-dOrderedCharter-84-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dOrderedCharter/prompts/2026-11-12-prompt-PLAY-dOrderedCharter-87-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-87`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> take forks' recommendations, land it

— owner, 2026-11-10. The close's bar over the prepared merge `c7d7f75f1` red the `instruction edits (manifest checks)` leg with
18 findings, all `instruction-units: red · repo.rule-NN-… · a directive opens with no modal` and `… a directive carries no
trigger`, for all nine adopter rules. The lander's prepare had just applied the upgrade step `playbook/adopter-rules-to-overlay`
(PLAY-dOrderedCharter-31 S4) on gov's own tree for the first time, so no earlier bar could see the rows it writes.

### brief:goal

Write spec PLAY-dOrderedCharter-87, the Tier-2 spec for one unit at order 48 that makes the step's rows pass the instruction-unit
grammar, so the next `--prepare` writes an overlay the close's bar accepts, without changing what the adopter rules SAY.

### brief:items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold87/2026-11-12-spec-PLAY-dOrderedCharter-87.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md`; carry the `**Derived:**` binding line spec 86 carries;
   status line `DEFERRED · rev-1 · 2026-11-12 · node a · Tier-2 · base <HEAD short sha> · streams tooling · order 48 · advances
   PLAY-dOrderedCharter-38`.
2. **The mismatch.** The step `tools/govkit/steps/adopter_rules_to_overlay.py` writes each `- ` line of `[charter]
   adopter_rules` as `type = "directive"` with the line as `text` and no `trigger`. `tools/playbook/instruction_units.py`'s row
   grader demands a directive open with a modal and carry a trigger; the other typed kinds each demand their own form, and
   `fact` and `policy-value` take no text. Reproduce the 18 reds by applying the step to a scratch copy of HEAD and running the
   leg's own reader there. Read how the project block renders these units into `AGENTS.md`, so the fix keeps the rendered text
   byte-identical; and read whether any other adopter of the step (the govkit fixture plants, an adopter's own rules) sees the
   same reds.
3. **The design.** Choose where the fix lives: in the step (which type and which fields it writes), in the grammar (a kind or an
   exemption for project rules carried as written), or both. A choice no seam decides is a fork with options and a
   recommendation; the run takes recommendations on the owner's standing ruling. The step's DOWN and WITNESS must still hold, and
   a repository that already applied the old step must converge, so say whether the step needs a new id or a version.
4. **After the unit.** The main loop re-runs `push-main.sh --prepare` and the close; name the legs this unit trips.
5. Criteria observe the instruction-units reader going green over a tree the step was applied to, and the rendered rules unchanged.
   The spec-token check grades a live spec's acceptance bullets word by word: no acceptance command whose words include an untracked
   path, no `path#symbol`, no suite as the observation, each backticked span on one line, every tripped leg on the gates line. Every
   new fact pinned; every minted function passes the lexicon's `--suggest`.

### brief:acceptance

- Spec 87 builds as written over HEAD, and after it the step's output passes the instruction-unit grammar.

### brief:gates

None run on the repository: this is a scratch write.

### brief:non-goals

- No code. No edit outside the scratch copy. No change to the adopter rules' wording.

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-84 · spec memory/builds/dOrderedCharter/spec/2026-11-12-spec-PLAY-dOrderedCharter-84.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-12-prompt-PLAY-dOrderedCharter-84-build-brief.md
[/memory/builds/dOrderedCharter/prompts/2026-11-12-prompt-PLAY-dOrderedCharter-87-1-spec-writer.md]
