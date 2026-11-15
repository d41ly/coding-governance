**Serves:** journal TOOL-aMeasuredDrag-12

# gov-spec-writer handoff — TOOL-aMeasuredDrag-12

<!-- gov:handoff role=gov-spec-writer build=aMeasuredDrag unit=TOOL-aMeasuredDrag-12 path=memory/builds/aMeasuredDrag/prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-12-1-spec-writer.md role-sha=a3bc1199e30f task-sha=8200f4b9429b -->

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
- build: aMeasuredDrag
- unit: TOOL-aMeasuredDrag-1 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-1.md
- unit: TOOL-aMeasuredDrag-3 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-3.md
- unit: TOOL-aMeasuredDrag-4 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-4.md
- unit: TOOL-aMeasuredDrag-5 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-5.md
- unit: TOOL-aMeasuredDrag-6 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-6.md
- unit: TOOL-aMeasuredDrag-7 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-7.md
- unit: TOOL-aMeasuredDrag-8 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-8.md
- unit: TOOL-aMeasuredDrag-9 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-9.md
- unit: TOOL-aMeasuredDrag-10 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-10.md
- unit: TOOL-aMeasuredDrag-11 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-11.md
- brief: memory/builds/aMeasuredDrag/prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aMeasuredDrag/prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-12-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aMeasuredDrag`, unit `TOOL-aMeasuredDrag-12`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> Build quick wins

The closing diff review of this build, round 1 (`memory/builds/aMeasuredDrag/reviews/2026-11-15-review-TOOL-aMeasuredDrag-1-11-closing-diff-round1.md`), exited CONVERGED and CLEAN WITH FIXES, with 0 blockers, 0 highs and 7 confirmed minor findings forming 6 items. BUILD-METHOD M4 (owner ruling, DIFF 2026-10-04) promotes every minor into one batched unit.

### brief:goal

`TOOL-aMeasuredDrag-12` closes the six items of the round-1 closing review, each fix being the one the review's skeptic judged sound or class-level, with no verdict, refusal or printed line moved for a correct input.

### brief:items

1. Item 2 (finding 1): only an ABSOLUTE launcher enters `GATE_RESOLVED_PY`. Fix it in `tools/run-gates/run-gates.sh`'s export and in the shared resolver block `tools/lib/resolve-python.sh#resolve_python` (re-synced to every inline copy the TOOL-aMeasuredDrag-11 S2 grep finds). A relative or bare-name launcher is never exported, so every leg re-probes as before.
2. Item 1 (findings 2 and 6): arm 1m in `tools/run-gates/run-gates.test.sh` tells a memo hit from a re-probe, using the skeptic's counting-wrapper fix from the review record, and goes red when the export no leg can match.
3. Item 3 (finding 3): `FLOOR_ASSERTIONS` in `tools/run-gates/run-gates.test.sh` rises by arm 1m's assertions (and item 1's), with a dated ledger line.
4. Item 4 (finding 4): an arm in the instructions-edit selftest pins both sides of `check_tree`'s `tags` switch: the write path runs the tag checks, the `check` verb does not.
5. Item 5 (finding 5): an arm in `.githooks/pre-commit.test.sh` goes red when the rewritten template-size trigger of TOOL-aMeasuredDrag-10 breaks.
6. Item 6 (finding 7): unit 11's AC5 red case (the export ahead of the digest) gets a lasting gate, or the spec §7 claim is narrowed to what arm 1m discharges, whichever the review record recommends.

### brief:acceptance

Per item, the observation the review record's fix names, and for each new arm a `New arm:` line whose RED-first observation is the main loop's at the close.

### brief:gates

The pass legs after the unit commit; the bar once, at the close.

### brief:non-goals

- Any change beyond the six items, and any other unit's spec.
- ANY SELF-TEST SUITE OR BAR INSIDE THE PASS, a sliced suite included.

### task:reuse

each fix edits the function the review cites in place; recall returns TOOL-dDerivedDocket-61 (one lease record) and TOOL-aBriskPreflight-9; the asks probe names TOOL-aTrimmedHook-8 (pre-commit cost after a one-file RUN.md commit) for unit 10.

### card:route

- build: aMeasuredDrag
- unit: TOOL-aMeasuredDrag-1 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-1.md
- unit: TOOL-aMeasuredDrag-3 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-3.md
- unit: TOOL-aMeasuredDrag-4 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-4.md
- unit: TOOL-aMeasuredDrag-5 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-5.md
- unit: TOOL-aMeasuredDrag-6 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-6.md
- unit: TOOL-aMeasuredDrag-7 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-7.md
- unit: TOOL-aMeasuredDrag-8 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-8.md
- unit: TOOL-aMeasuredDrag-9 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-9.md
- unit: TOOL-aMeasuredDrag-10 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-10.md
- unit: TOOL-aMeasuredDrag-11 · spec memory/builds/aMeasuredDrag/spec/2026-11-15-spec-TOOL-aMeasuredDrag-11.md
- brief: memory/builds/aMeasuredDrag/prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md
[/memory/builds/aMeasuredDrag/prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-12-1-spec-writer.md]
