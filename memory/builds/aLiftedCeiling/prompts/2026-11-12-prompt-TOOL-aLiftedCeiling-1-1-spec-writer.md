**Serves:** journal TOOL-aLiftedCeiling-1

# gov-spec-writer handoff — TOOL-aLiftedCeiling-1

<!-- gov:handoff role=gov-spec-writer build=aLiftedCeiling unit=TOOL-aLiftedCeiling-1 path=memory/builds/aLiftedCeiling/prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-1-spec-writer.md role-sha=a3bc1199e30f task-sha=24ea6116766d -->

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
[memory/builds/aLiftedCeiling/prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aLiftedCeiling`, unit `TOOL-aLiftedCeiling-1`.
Not supplied, optional: `input:spec`, `card:route`, `input:code`.

### brief:prompt

> Yes, raise it

— owner, 2026-11-12, answering "Raise instruction edits' 180 s ceiling so the wait stops costing a retry?". The build's brief
is `memory/builds/aLiftedCeiling/prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-brief.md`; read it whole first.

### brief:goal

Write spec TOOL-aLiftedCeiling-1, a Tier-1 micro-spec for one unit at order 1 that raises the `instruction edits (manifest
checks)` leg's declared ceiling in `tools/gate-legs.json` to cover its wait on the other tag-index writer.

### brief:items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/foldal1/2026-11-12-spec-TOOL-aLiftedCeiling-1.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md` for a Tier-1 micro-spec; status line `DEFERRED · rev-1 ·
   2026-11-12 · node a · Tier-1 · base <HEAD short sha> · streams tooling · order 1`. Write no open fork: where a choice remains,
   take your recommendation and mark it resolved in its own span.
2. **The value.** The leg is the second writer of the shared tag index since aQueuedIndex (landed `aa8f08000`): it now waits for
   the tags leg's tree build instead of failing, and timed out at its 180 s ceiling and passed on retry at both of that build's
   bars. Its partner `tags (the resolver's checks)` declares 420 s. Read the run-gates kit's ceiling rules (its README's ceiling
   sections and `tools/run-gates/derive-ceilings.py --help`), the leg's readings in the runner's records and the evidence file,
   and size the new ceiling from them; say why that value and not another.
3. **The evidence.** Say whether the raise owes an evidence row in `tools/run-gates/ceiling-evidence.txt` (a generated file, never
   hand-edited) and how it is written, and which kit checks grade a ceiling against its evidence.
4. **Watched file.** `tools/gate-legs.json` is on the kickoff manifest's `watch:` list; the unit re-stamps the manifest.
5. Criteria observe the manifest's new value, the evidence the kit reads for it, and the leg finishing inside its new ceiling in a
   race of the two tag-index checks on a fresh index in a scratch clone. The spec-token check grades a live spec's acceptance
   bullets word by word: no acceptance command whose words include an untracked path, no `path#symbol`, no suite as the
   observation, each backticked span on one line, every tripped leg on the gates line. Every new fact pinned, every new `path:line`
   blob-pinned.

### brief:acceptance

- Spec TOOL-aLiftedCeiling-1 builds as written over HEAD, and its criteria observe the leg run once inside its new ceiling.

### brief:gates

None run on the repository: this is a scratch write.

### brief:non-goals

- No code. No edit outside the scratch copy. No other leg's ceiling, and no change to the tag index or its busy timeout.

### task:reuse

the leg's ceiling key in tools/gate-legs.json and tools/run-gates/derive-ceilings.py.
[/memory/builds/aLiftedCeiling/prompts/2026-11-12-prompt-TOOL-aLiftedCeiling-1-1-spec-writer.md]
