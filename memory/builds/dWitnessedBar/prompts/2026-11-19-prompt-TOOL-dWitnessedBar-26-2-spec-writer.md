**Serves:** journal TOOL-dWitnessedBar-26

# gov-spec-writer handoff — TOOL-dWitnessedBar-26

<!-- gov:handoff role=gov-spec-writer build=dWitnessedBar unit=TOOL-dWitnessedBar-26 path=memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-26-2-spec-writer.md role-sha=91ec0ce505aa task-sha=26840fc48e0f -->

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
- build: dWitnessedBar
- unit: TOOL-dWitnessedBar-26 · spec memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md
- brief: memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-26-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-26-2-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dWitnessedBar`, unit `TOOL-dWitnessedBar-26`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Unit 26's first builder (run `wf_9a057cc8-2c5`) stopped at a divergence
before keeping any code; its return is `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-26-1-builder-return.md`.

### brief:goal

Revise the spec of TOOL-dWitnessedBar-26 in place, as a rev bump (rev-5) with one revision-log line naming the builder
return by its file stem, so a builder can build it as written over HEAD on node d.

### brief:items

1. Read the builder return whole; it measured each finding on node d. Its draft canonical, which runs every candidate
   after `GOV_BASH`, is at
   `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/u26/resolve_bash.draft.py`.
2. The probe (§4 "The rule"): name a probe whose first output line is `uname -s`'s own, so a WSL launcher run under any
   name answers `Linux` and AC1's `answered Linux` and AC3's posix case are reachable. State that the launcher drops the
   positional arguments, so `test -f "$1"` never refuses it and only the uname test does. Re-measure the probe you name
   against a copy of `C:/Windows/System32/bash.exe` outside System32 and against Git's `bin/bash.exe` before writing it.
3. The order (§4 versus AC1): state whether the resolver stops at the first candidate that passes or probes every
   candidate after `GOV_BASH` and reports each on a `tried:` line. This is a fork: decide it by the build method's M3
   (the most feature-rich option that survives the vetoes), mark it RESOLVED in §8, make §6 AC1 and §5's cost line
   agree with the choice, and say which in your return.
4. The sites: add `tools/loop/factories.py`'s `resolve_bash(...) or "bash"` and `tools/run-gates/regen.py`'s
   `shutil.which(run[0]) or run[0]` fall-back to the sites table, Files touched and the gates section's legs their guards name; say
   whether the S6 query should find each shape and, where it should, widen the query in §4 "The query".
5. The adapters: `loop_witness.resolve_bash` is imported by name by `tools/loop/breakpoints.py`, `budget.py`,
   `factories.py`, `loop_lib.py` and `position.py`, so it keeps its `path or None` contract through an adapter. State
   one rule for the name clash between the block's `resolve_bash` / `resolveBash` and every adapter that keeps that
   name (`profile_bar`, `upgrade_steps`, `corpus_ids`, the lexicon and runlog selftests, `handoff`, `loop_witness`), and
   rename `policy-mirror.js`'s internal `resolveBash`.
6. govkit selftest's `check_floor_bash` arms `[dSP-94]` and `[dSP-95]` assume no bash resolves once PATH is staged;
   with Git's `bin/bash.exe` as step 2 that premise fails on a Git for Windows node. State the staging that restores it,
   and the anchor the narrowed-catch arm reads once the block is inlined.
7. Run `bash tools/unattended/unattended.sh --check-specs dWitnessedBar TOOL-dWitnessedBar-26` and
   `python tools/check-spec-tokens.py --spec memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md`
   before returning, and fix every finding either names.

### brief:acceptance

Both commands in item 7 exit 0; the spec carries rev-5 and one revision-log line naming the builder return's file stem;
§8 carries the item-3 fork RESOLVED.

### brief:gates

memory hygiene · spec tokens (a spec's own names resolve)

### brief:non-goals

No other spec. No product code. Scope items unaffected by items 2 to 6 stay as written.

### task:reuse

each spec's §10 names its seam; build-level recall terms below.

### card:route

- build: dWitnessedBar
- unit: TOOL-dWitnessedBar-26 · spec memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-26.md
- brief: memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-26-build-brief.md
[/memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-26-2-spec-writer.md]
