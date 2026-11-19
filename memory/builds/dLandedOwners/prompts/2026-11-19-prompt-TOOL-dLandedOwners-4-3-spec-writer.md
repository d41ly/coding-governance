**Serves:** journal TOOL-dLandedOwners-4

# gov-spec-writer handoff — TOOL-dLandedOwners-4

<!-- gov:handoff role=gov-spec-writer build=dLandedOwners unit=TOOL-dLandedOwners-4 path=memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-4-3-spec-writer.md role-sha=91ec0ce505aa task-sha=ce85a03e601c -->

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
- build: dLandedOwners
- unit: TOOL-dLandedOwners-4 · spec memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-4.md
- brief: memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-4-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-4-3-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dLandedOwners`, unit `TOOL-dLandedOwners-4`.
Not supplied, optional: `input:code`.

### brief:prompt

> Fix the Ask 5, remove the ask TOOL-dTrackedAtlas-19

The owner's go for this build, of 2026-11-19; this record carries the builder's divergence back to the spec writer, its Goal the builder's `why` verbatim.

### brief:goal

DIVERGENCE: the spec contradicts itself between §4 "The docs" (second bullet) and AC11 in §6. §4 says the module docstring's `arm_reader_coverage` clause should read "reds a catalogue key whose owner build has landed by `derive_landed_builds` (every spec terminal at the landed revision, or a build-kind run record with a first-parent landing merge, TOOL-dLandedOwners-1)". That text contains the exact substring "terminal at the landed revision". The same bullet then says `git grep` for "terminal at the landed revision" over tools/, help/ and README.md must find no copy of the old clause. AC11 requires its probe `'terminal at the landed revision' in d` to print False and that git grep to print nothing. I checked this with python: `'terminal at the landed revision' in <the prescribed clause>` prints True. So if the docstring is written as §4 says, AC11 stays red. The spec has to change one of two things. Option one: reword the parenthetical so the phrase is not in it, for example "every spec's status header terminal at L". Option two: point AC11 and §4's grep sentence at a phrase only the old clause holds, for example "every spec in its build folder terminal". Today that phrase appears only at tools/policy/check_policy.py:20-21. A smaller point for the same revision: the Files touched estimate does not list memory/LIVE.md or memory/builds/dLandedOwners/README.md. The commit hooks re-rendered both in unit 3's build commit b8297f701, so they should probably be listed. No other claim I probed failed.

### brief:items

1. `derive_landed_owners` in `tools/policy/check_policy.py` reads a build run that landed with a unit carried forward, DEFERRED against an ask, as landed, by the predicate the schedule's derivation took (its spec's fork F1, option g: a build-kind run record with a first-parent landing merge on the default branch), in a form a shipped kit can hold [planned TOOL-dLandedOwners-1]
2. The reader scan (`READER_SHAPES`, `scan_reader_keys`) reads a key passed to a reader call through a module-level constant, the shape the loop kit uses for seven dDeclaredLoop keys [planned TOOL-dLandedOwners-2]
3. A key whose only reader sits outside the scanned code, `deviation.approval`, read by a dClosedLoop instrument under the memory root, takes a declared disposition with its reason, never a silent pass [planned TOOL-dLandedOwners-3]
4. Ask TOOL-dTrackedAtlas-19 withdrawn on the owner's word [stale landed at `51971579a` before this build opened]

### brief:acceptance

At the build's tip, `derive_landed_owners` names dDeclaredLoop, dSafePassage, dFairHearing and dTrueNorth among the landed owners; reader coverage grades the keys of every landed owner and reports no finding; each new arm is observed red before green; the merge bar is green.

### brief:gates

The merge bar, `bash tools/run-gates/run-gates.sh`, once after the last unit; per unit, the direct check its spec names. The policy kit's own self-test arms are the owner's flagged bar, waived for this build as for dTrackedAtlas.

### brief:non-goals

Any other policy key; the loop kit's code, beyond what a reader shape needs to see; the chain builds' specs; the flagged bar.

### input:spec

memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-4.md

### task:reuse

tools/policy/check_policy.py derive_landed_owners, check_reader_coverage, scan_reader_keys, READER_SHAPES; tree_lib TERMINAL; dTrackedAtlas build-state derive_landings.

### card:route

- build: dLandedOwners
- unit: TOOL-dLandedOwners-4 · spec memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-4.md
- brief: memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-4-build-brief.md
[/memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-4-3-spec-writer.md]
