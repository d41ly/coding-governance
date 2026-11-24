**Serves:** journal KICK-dKeptSession-22

# gov-spec-writer handoff — KICK-dKeptSession-22

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=KICK-dKeptSession-22 path=memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-22-1-spec-writer.md role-sha=91ec0ce505aa task-sha=0e634c071402 -->

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
[memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-22-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-22`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dKeptSession

### brief:goal

Specs 22, 31, 5 were re-grounded on the run's tree, and every textual check passes on them. The units built so far
still diverged at build on behaviour no textual check reads: a criterion naming an exit its verb never gives, a
fixture copy lacking a kit or a file the new code imports, a fixture guard not covering what a fixture copies, a new
rule turning a reader's refusal into a silent fallback, a factory whose halves did not fit a caller, a write set
missing a path the commit hook moves. Since the re-ground, KICK-dKeptSession-1, -19, -33, -2, -3, -34, -40, -4 and -49 (the preset store, its checks and reader step in `tools/policy/`, the shrink-list factory, the derived-row rules, the charter's preset section, the preset asked at govkit intake, and the policy mirror's input list) have landed, KICK-dKeptSession-50 is being built, and
the specs ordered before yours build before them. Read the landed code and those specs for what they build. Check
each spec against the tree as it now stands, and fix what would make its builder diverge.

### brief:items

1. F-behaviour: for each criterion, run or read its command against the verb it calls and the fixture that seeds it, and confirm the exit, output and seed it names are the ones the code gives.
2. F-callers: grep every caller of each function the unit changes or adds a rule to, and every suite or fixture that copies a file the unit touches or imports; where one would break, the spec says how (a copy added, a guard widened, a refusal kept) and names its paths in Files touched.
3. F-landed: re-cite against KICK-dKeptSession-1's landed code (and every unit landed since, and the specs ordered before yours for what they build); an item unit 1 already built is reduced to its observation.
4. F-positional: no `path:number` token stands in the spec unless it is a blob pin; a quoted refusal line is described, not quoted with its line suffix.
5. F-hook-paths: Files touched names the paths the commit hook will need: a watched file's kickoff-manifest re-stamp (`memory/guides/SESSION-KICKOFF.md`), `memory/map/generated/symbols.json` for new code symbols, and any reference page or docs list a re-render moves.
6. Keep each spec within the live-spec size cap, pin every figure with DERIVED or PINNED, leave no fork open (a fork you rule is marked `RESOLVED (agent, 2026-11-21, delegated): <option>, rung <n>; <reason>. widens: <value|none> · relaxes: <value|none>`), and where you change nothing in a spec, say so and leave it at its rev.

### brief:acceptance

Each spec you changed is at a new rev with one revision-log line naming this brief by its file stem, and
`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`,
a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession <its id>` report nothing for it.

### brief:gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### brief:non-goals

No product code, no commit, no index render, no status flip, and no spec other than 22, 31, 5. Another writer may be
checking other specs, and KICK-dKeptSession-50 is being built: read them, never write them.

### task:reuse

each spec's §10 names its seam; probes run: `reuse_lookup.py` per spec at re-ground; recall terms below.

### card:route

- build: dKeptSession
- unit: KICK-dKeptSession-50 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-50.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-50-build-brief.md
[/memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-22-1-spec-writer.md]
