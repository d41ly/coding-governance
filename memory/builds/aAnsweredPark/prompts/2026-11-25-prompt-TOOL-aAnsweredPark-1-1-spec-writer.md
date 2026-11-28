**Serves:** journal TOOL-aAnsweredPark-1
**Caused-by:** TOOL-aAnsweredPark-1

# gov-spec-writer handoff — TOOL-aAnsweredPark-1

<!-- gov:handoff role=gov-spec-writer build=aAnsweredPark unit=TOOL-aAnsweredPark-1 path=memory/builds/aAnsweredPark/prompts/2026-11-25-prompt-TOOL-aAnsweredPark-1-1-spec-writer.md role-sha=91ec0ce505aa task-sha=e9162e39d792 -->

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
- build: aAnsweredPark
- unit: TOOL-aAnsweredPark-1 · spec memory/builds/aAnsweredPark/spec/2026-11-25-spec-TOOL-aAnsweredPark-1.md
- brief: memory/builds/aAnsweredPark/prompts/2026-11-25-prompt-TOOL-aAnsweredPark-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aAnsweredPark/prompts/2026-11-25-prompt-TOOL-aAnsweredPark-1-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aAnsweredPark`, unit `TOOL-aAnsweredPark-1`.
Not supplied, optional: `input:code`.

### brief:prompt

> The unit harness's builder (run `wf_5a7a9476-d1a`) returned `diverged: true` before committing any code, with the `why` quoted whole below as the Goal.

### brief:goal

DIVERGENCE: spec section 4 "Files touched (estimate)". The design builds as written. The file list cannot be committed in the one commit the task requires, the one that also flips the spec to CLOSED.

I found this late, at my one commit attempt: the pre-commit hook refused it. I missed it in the pre-edit check. Two paths the hook needs are undeclared.

(1) ACCEPTANCE LEDGER. Hygiene check 23 refuses a CLOSED Tier-2 spec whose AC1 to AC10 no journal record evidences. Section 4 would have to list `memory/builds/aAnsweredPark/build/2026-11-25-build-TOOL-aAnsweredPark-1-1-acceptance-ledger.md`. It is a journal record with one line per AC1 to AC10, each sharing a backticked token with its criterion. The dKeptSession specs (44, 56, 62, 63, 79, 89) all name theirs.

(2) KEEP ROWS. This unit is the build's only unit, so its CLOSED makes the build CLOSED. Verdict V10 then reds hygiene check 9 on TOOL-aAnsweredPark-2, -3 and -4, which derive OPEN with no status row. `memory/builds/aAnsweredPark/BACKLOG.md` needs a `- KEEP · <id> · <why>` row for each under its Dispositions heading. Either the main loop commits those first, as 642e16c9d did for dKeptSession, or section 4 lists the file and says what each row reads. Disposing asks is not a builder's call under this spec.

The hook itself renders `memory/LIVE.md`, `memory/builds/aAnsweredPark/README.md` and the spec's gen:spec-records block; section 4 may name those as generated. No kickoff re-stamp is needed.

That list is complete. In a throwaway clone, the built change plus the ledger and the three KEEP rows committed with rc=0 and every pre-commit leg ok (GOV_DEFAULT_BRANCH set there only because a clone is a primary tree). Nothing else in the spec failed. AC1 to AC10 were each observed as stated, and the base-tree claims I checked held.

### brief:items

1. Add to section 4's files touched `memory/builds/aAnsweredPark/build/2026-11-25-build-TOOL-aAnsweredPark-1-1-acceptance-ledger.md`,
   the journal record evidencing AC1 to AC10, one line each. The three KEEP rows are committed by the main loop,
   so `memory/builds/aAnsweredPark/BACKLOG.md` is not listed.
2. Name `memory/LIVE.md`, `memory/builds/aAnsweredPark/README.md` and the spec's records block as rendered by the hook.
3. Bump the rev and add the section 9 line naming this record. Nothing else changes.

### brief:acceptance

Fixture cases of `position.py --fixture --plant`, seen red before and green after: an answered decision acts;
an unanswered one awaits; a record of another row, of another word, or with no Reason does not settle; two rows
of one second settle apart; a `rescope` and a `handoff` row do not interrupt; a resumed hold does not interrupt
and a HELD one does. A read of dBoundRoles at its committed tip says what it answers.

### brief:gates

`loop position fixtures` and every leg the spec's files trip.

### brief:non-goals

`actions.free`, `.governance/policy.toml`, any hook, the card's read bound, `tools/memory-tree/routed_commits.py`,
the unattended kit, the disposition grammar, and any dBoundRoles file. The read's cost is an ask, not a fix.
A `flow.on-exhausted` or owner-gate row is a decision row as any other: its own item's disposition does not
settle the parked row.

### input:spec

memory/builds/aAnsweredPark/spec/2026-11-25-spec-TOOL-aAnsweredPark-1.md

### task:reuse

`tools/loop/adapt.py` `read_disposition_release` and `tools/memory-tree/build_records.py new disposition`, prototyped this session.

### card:route

- build: aAnsweredPark
- unit: TOOL-aAnsweredPark-1 · spec memory/builds/aAnsweredPark/spec/2026-11-25-spec-TOOL-aAnsweredPark-1.md
- brief: memory/builds/aAnsweredPark/prompts/2026-11-25-prompt-TOOL-aAnsweredPark-1-brief.md
[/memory/builds/aAnsweredPark/prompts/2026-11-25-prompt-TOOL-aAnsweredPark-1-1-spec-writer.md]
