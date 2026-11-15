**Serves:** journal TOOL-aClearedLedger-14

# gov-spec-writer handoff — TOOL-aClearedLedger-14

<!-- gov:handoff role=gov-spec-writer build=aClearedLedger unit=TOOL-aClearedLedger-14 path=memory/builds/aClearedLedger/prompts/2026-11-14-prompt-TOOL-aClearedLedger-14-1-spec-writer.md role-sha=a3bc1199e30f task-sha=130a9ce5a8d2 -->

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
- build: aClearedLedger
- unit: TOOL-aClearedLedger-13 · spec memory/builds/aClearedLedger/spec/2026-11-14-spec-TOOL-aClearedLedger-13.md
- brief: memory/builds/aClearedLedger/prompts/2026-11-14-prompt-TOOL-aClearedLedger-13-brief.md
[/.claude/orientation-card.md]
[memory/builds/aClearedLedger/prompts/2026-11-14-prompt-TOOL-aClearedLedger-14-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aClearedLedger`, unit `TOOL-aClearedLedger-14`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> follow `memory/guides/BUILD-METHOD.md` for specs, builders and the closing review.

The owner's prompt is recorded whole in `memory/builds/aClearedLedger/prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md`.

### brief:goal

Round 3 of the closing diff review, `memory/builds/aClearedLedger/reviews/2026-11-14-review-TOOL-aClearedLedger-11-12-13-diff-review-round3.md`, confirmed two LOW items and no BLOCKER, HIGH or MEDIUM; the build method batches them into one unit. Write the spec of TOOL-aClearedLedger-14, order 14, from the record's items L1 and L2, each with the fix the record states; for L2 the skeptic's class-level fix is the design.

### brief:items

1. L2: `readTokenAt` of `tools/unattended/gate-guard.js` reads on past `>` or `<` only while the word read so far is made entirely of unquoted characters matching the operator pattern, so a quoted `&`, `>` or digit glued before a `>` ends the word as bash does. Two `run_planted` arms in `tools/unattended/gate-guard.test.sh`, one with a quoted `&` and one with a quoted `>`, each glued before a `>`, each with a `New arm:` line naming its failing case; the floor moves by their count, DERIVED from 217, the value TOOL-aClearedLedger-13 left at 64673441a.
2. L1: TOOL-aClearedLedger-13's spec is CLOSED and frozen, so its table cell is not edited. This unit's spec restates that unit's quoted-read regex in a fenced block, as the correction of record, and says why the frozen cell renders split.
3. The status header carries no `closes`. Tier-2, because it changes the hook's contract. Every figure beside a unit or a counted noun carries PINNED or a sha on its line; no bare path with a line number.
4. Section 5 numbers only criteria a builder's pass can observe with a probe of the changed code. Each suite run, leg run and RED-first observation the main loop owes is stated in the Gates section, on the `New arm:` lines and in prose there, never as a numbered criterion: hygiene check 23 wants a ledger line for every criterion a CLOSED spec numbers, and a builder cannot observe a suite.

### brief:acceptance

`python tools/check-spec-tokens.py --spec` over the new spec exits 0, and each of the two items maps to a numbered scope item and at least one criterion.

### brief:gates

The spec-token checker over this one spec.

### brief:non-goals

Any change to `tools/check-spec-tokens.py` or its suite; any edit to a CLOSED spec; any sibling spec, any commit, any index render, any floor lowered.

### task:reuse

`tools/unattended/gate-guard.js`, `tools/check-spec-tokens.py` (`BAR`), `tools/hooks/scratch-guard.js`, `tools/memory-tree/check-memory-hygiene.sh`, `tools/policy/check_policy.py`, `tools/memory-tree/build_records.py`, `tools/run-gates/derive-ceilings.py`, `tools/run-gates/pass_legs.py`.

### card:route

- build: aClearedLedger
- unit: TOOL-aClearedLedger-13 · spec memory/builds/aClearedLedger/spec/2026-11-14-spec-TOOL-aClearedLedger-13.md
- brief: memory/builds/aClearedLedger/prompts/2026-11-14-prompt-TOOL-aClearedLedger-13-brief.md
[/memory/builds/aClearedLedger/prompts/2026-11-14-prompt-TOOL-aClearedLedger-14-1-spec-writer.md]
