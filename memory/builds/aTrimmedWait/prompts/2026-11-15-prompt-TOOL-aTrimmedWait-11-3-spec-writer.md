**Serves:** journal TOOL-aTrimmedWait-11

# gov-spec-writer handoff — TOOL-aTrimmedWait-11

<!-- gov:handoff role=gov-spec-writer build=aTrimmedWait unit=TOOL-aTrimmedWait-11 path=memory/builds/aTrimmedWait/prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-3-spec-writer.md role-sha=6873fbf041ac task-sha=7085305e9862 -->

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
- build: aTrimmedWait
- unit: TOOL-aTrimmedWait-1 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-1.md
- unit: TOOL-aTrimmedWait-2 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-2.md
- unit: TOOL-aTrimmedWait-3 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-3.md
- unit: TOOL-aTrimmedWait-4 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-4.md
- unit: TOOL-aTrimmedWait-5 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-5.md
- unit: TOOL-aTrimmedWait-6 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-6.md
- unit: TOOL-aTrimmedWait-7 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-7.md
- unit: TOOL-aTrimmedWait-8 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-8.md
- unit: TOOL-aTrimmedWait-9 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-9.md
- unit: TOOL-aTrimmedWait-10 · spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-10.md
- unit: TOOL-aTrimmedWait-11 · spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md
- brief: memory/builds/aTrimmedWait/prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aTrimmedWait/prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-3-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aTrimmedWait`, unit `TOOL-aTrimmedWait-11`.
Not supplied, optional: `input:code`.

### brief:prompt

The main loop's commit of rev-2 was refused by the pre-commit hook's memory hygiene, quoted:

> memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md (§2 items that retire a named thing carry no **Readers:** clause; ...): S1

S1 says the function "drops every check 26 `cache recomputed` line", and the check reads that verb as
retiring a named thing. Nothing is retired: the lines are set aside inside one comparison, and check 26
still prints them.

The rev-2 spec writer also reported that §4's line `_hs_c26=("${_hs_c26[@]%$'\r'}")` does not strip
the trailing carriage return under this node's bash 5.3 (Cygwin). The main loop observed on
2026-11-15 that holding the pattern in a variable does: `cr=$'\r'; B=("${A[@]%"$cr"}")` left no
carriage return in `B`.

### brief:goal

Revise TOOL-aTrimmedWait-11 so its spec commits, with the fixture arm's strip correct on this node.

### brief:items

1. S1, and any other §2 item worded the same way, says the `cache recomputed` lines are set aside in
   the comparison, not dropped or removed, so no §2 item reads as retiring a named thing.
2. §4 "The fixture arm" strips the carriage return with the pattern held in a suite variable, and
   the sentence after it says why: the array expansion's `%$'\r'` leaves it on this node's bash.
   §4 "Inventory" names the variable.

Change nothing else. Bump the revision, keep the header SPECCED, and leave the spec uncommitted: the
main loop commits it.

### brief:acceptance

- `python tools/check-spec-tokens.py --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md` exits 0.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 25 --spec memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md` exits 0.
- `bash tools/unattended/unattended.sh --check-specs aTrimmedWait TOOL-aTrimmedWait-11` prints its clean line.

### brief:gates

Copied from the build's brief: the merge bar once at the close, with no self-test suite in it; each
kit's own arms for the units that touch it.

### brief:non-goals

No change to what is compared, the function, the floor or the files touched.

### input:spec

memory/builds/aTrimmedWait/spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md

### task:reuse

`verb_dispatch`/`plan_state`/`order_verb_of`/`scan_consumes_cycles`/`run_spec_token_check` (unattended.sh); check 12's loop and `--only` (check-memory-hygiene.sh); `--check --staged` render decision (gen_build_index.py, TOOL-aTrimmedHook-1); `derive_spec_token_key` key-then-record; `scanCommandHeads`/`checkRoleGate` (scratch-guard.js); `load_session_calls` (handoff.py).

### card:route

- build: aTrimmedWait
- unit: TOOL-aTrimmedWait-1 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-1.md
- unit: TOOL-aTrimmedWait-2 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-2.md
- unit: TOOL-aTrimmedWait-3 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-3.md
- unit: TOOL-aTrimmedWait-4 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-4.md
- unit: TOOL-aTrimmedWait-5 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-5.md
- unit: TOOL-aTrimmedWait-6 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-6.md
- unit: TOOL-aTrimmedWait-7 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-7.md
- unit: TOOL-aTrimmedWait-8 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-8.md
- unit: TOOL-aTrimmedWait-9 · spec memory/builds/aTrimmedWait/spec/2026-11-14-spec-TOOL-aTrimmedWait-9.md
- brief: memory/builds/aTrimmedWait/prompts/2026-11-14-prompt-TOOL-aTrimmedWait-1-brief.md
[/memory/builds/aTrimmedWait/prompts/2026-11-15-prompt-TOOL-aTrimmedWait-11-3-spec-writer.md]
