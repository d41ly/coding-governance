**Serves:** journal KICK-dKeptSession-50

# gov-spec-writer handoff — KICK-dKeptSession-50

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=KICK-dKeptSession-50 path=memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-50-1-spec-writer.md role-sha=91ec0ce505aa task-sha=7f5fd62da204 -->

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
- build: dKeptSession
- unit: KICK-dKeptSession-50 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-50.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-50-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-50-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-50`.
Not supplied, optional: `input:code`.

### brief:prompt

> /unattended dKeptSession

### brief:goal

KICK-dKeptSession-50's builder (run `wf_b0c09fd2-3f3`) returned a DIVERGENCE before any edit. S4 says its answer to
unit 40's superseded Migration and risks lines goes in unit 40's acceptance ledger. Unit 40 is CLOSED, and that
ledger is in neither this unit's Files touched nor its write set. This is the same divergence KICK-dKeptSession-49
returned and its rev-6 resolved. A grep finds six more specs that answer in an earlier unit's acceptance ledger:
47 and 48 (unit 30's), 51 (unit 22's), 53 and 55 (unit 42's), and 61 (unit 53's). Each of those earlier units
builds first, so each later builder would diverge the same way. Revise all seven to the main loop's ruling.

### brief:items

1. F-own-ledger: in each spec, every sentence that answers in another unit's acceptance ledger moves its answer to this unit's own ledger (`memory/builds/dKeptSession/build/2026-11-21-build-<this unit's id>-1-acceptance-ledger.md`). That ledger quotes the other unit's spec text it supersedes, and joins Files touched; where it trips a guarded leg, that leg joins section 7's leg line. Record the fork in each spec's open-questions section as resolved by the main loop: `RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a CLOSED unit's records are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled.` Rejected: (a), writing the earlier unit's ledger. Add a criterion, or extend an existing one, that observes the quoted passages in this unit's ledger.
2. F-ac3 (spec 50 only): AC3's grep for `rendered before` already matches `tools/policy/README.md` at this base, in unit 49's sentence about a mirror rendered before the store joined. AC3 must grep for a phrase only S3 adds, so its red side is observable at the pass base. Correct the rev-3 log's claim with a new line rather than editing the old one.
3. F-selfcheck (spec 50 only): govkit selfcheck 7l scans every tracked file under `tools/policy/`, docstrings included. Any sentence S3 or a new case adds that says `update` and `re-render` must also name `GOVKIT_RERENDER`. Say so where the spec describes the README and docstring text.
4. F-behaviour: run or read each changed criterion's command against the verb and fixture it relies on, and confirm the exit and output it names. No `path:number` token stands unless it is a blob pin. Re-cite every changed line as `path#symbol`. Keep within the live-spec size cap, pin every figure, and leave no fork open.

### brief:acceptance

Each spec is at a new rev, carrying the ruling and one revision-log line that names this brief by its file stem.
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession <its id>` report nothing for each.

### brief:gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### brief:non-goals

No product code, no commit, no index render, and no status flip: spec 50 stays INPROGRESS and the others stay
DEFERRED. No spec outside these seven. Another writer may be checking specs 22, 31 and 5, and unit 54 may be
building: read them, never write them.

### input:spec

memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-50.md

### task:reuse

each spec's §10 names its seam; probes run: `reuse_lookup.py` per spec at re-ground; recall terms below.

### card:route

- build: dKeptSession
- unit: KICK-dKeptSession-50 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-50.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-50-build-brief.md
[/memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-50-1-spec-writer.md]
