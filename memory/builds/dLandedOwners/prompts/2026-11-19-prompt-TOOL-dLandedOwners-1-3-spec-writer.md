**Serves:** journal TOOL-dLandedOwners-1

# gov-spec-writer handoff — TOOL-dLandedOwners-1

<!-- gov:handoff role=gov-spec-writer build=dLandedOwners unit=TOOL-dLandedOwners-1 path=memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-3-spec-writer.md role-sha=91ec0ce505aa task-sha=1bda2c0c5226 -->

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
- unit: TOOL-dLandedOwners-1 · spec memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-1.md
- brief: memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-3-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dLandedOwners`, unit `TOOL-dLandedOwners-1`.
Not supplied, optional: `input:code`.

### brief:prompt

> Fix the Ask 5, remove the ask TOOL-dTrackedAtlas-19

The owner's go for this build, of 2026-11-19; this record carries the builder's divergence back to the spec writer, its Goal the builder's `why` verbatim.

### brief:goal

DIVERGENCE: two places where the spec cannot be built as written. Both have to be revised before this unit is dispatched again.

(1) §4 "The fixture case" contradicts AC4 and §7. Its third bullet says to copy "every *.py of the resolved memory-tree kit" beside the kit copy. That copy runs inside run_fixture's process, where the audit hook (check_policy.py#add_source_read) records every source file it opens. check_policy.py#check_guard_trace then prints a `policy-fixture: guard-trace · WRONG <path> · not under the policy fixtures guard` line for each recorded read that trips no `policy fixtures` guard. I checked the seven files below with `python tools/check-spec-tokens.py --legs-for -`, and none of them trips that guard:
- tools/memory-tree/check-arms.py
- tools/memory-tree/commit_trailers.py
- tools/memory-tree/coverage_join.py
- tools/memory-tree/import_walk.py
- tools/memory-tree/merge-rows.py
- tools/memory-tree/migrate_backlog.py
- tools/memory-tree/transition_audit.py

tools/memory-tree/tree_lib.py, by contrast, trips it. So every `--fixture` run, AC4's single-case run included, would print seven WRONG lines. AC4 ("No line holds WRONG") would fail, and so would the `policy fixtures` leg. Fixing it means one of two spec changes:
- (a) Copy only the import closure that half 2 needs. That is tree_lib.py, gen_build_index.py, backlog.py, design_lib.py, row_grammar.py and id_grammar.py, which gen_build_index and row_grammar import lazily. All six are already in the guard.
- (b) Add the seven paths to the `policy fixtures` guard in tools/gate-legs.json. The spec would then have to add that file to Files touched.

(2) §4 "Files touched (estimate)" lists only tools/policy/check_policy.py, tools/policy/README.md and help/policy.md. It leaves out the acceptance ledger, memory/builds/dLandedOwners/build/2026-11-19-build-TOOL-dLandedOwners-1-ledger.md. Closing this spec needs that ledger: memory/HYGIENE.md "Acceptance ledger" grades every criterion a closed spec numbers. The brief says the spec's Files touched names a ledger, and it does not. The prior dTrackedAtlas unit specs (9, 12) list theirs.

Three smaller points the spec writer should settle in the same revision:
- AC4 says the run "prints five policy-fixture: lines". run_fixture always adds the guard-trace lines and the count line, so it should say five sub-case lines.
- In §4, `base-unresolved` says "both run records", but each planted repository holds one RUN.md. It should say which two it means.
- The brief tells the builder to "leave the spec's status flip to the main loop", while this dispatch says to set CLOSED. That contradiction is the brief's, not the spec's.

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

memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-1.md

### task:reuse

tools/policy/check_policy.py derive_landed_owners, check_reader_coverage, scan_reader_keys, READER_SHAPES; tree_lib TERMINAL; dTrackedAtlas build-state derive_landings.

### card:route

- build: dLandedOwners
- unit: TOOL-dLandedOwners-1 · spec memory/builds/dLandedOwners/spec/2026-11-19-spec-TOOL-dLandedOwners-1.md
- brief: memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-build-brief.md
[/memory/builds/dLandedOwners/prompts/2026-11-19-prompt-TOOL-dLandedOwners-1-3-spec-writer.md]
