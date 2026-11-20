**Serves:** journal TOOL-dPlacedRequest-56

# gov-spec-writer handoff — TOOL-dPlacedRequest-56

<!-- gov:handoff role=gov-spec-writer build=dPlacedRequest unit=TOOL-dPlacedRequest-56 path=memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-56-1-spec-writer.md role-sha=91ec0ce505aa task-sha=dabf6024be08 -->

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
- build: dPlacedRequest
- unit: TOOL-dPlacedRequest-56 · spec memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md
- brief: memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-56-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dPlacedRequest`, unit `TOOL-dPlacedRequest-56`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dPlacedRequest

### brief:goal

Units 56 and 57 (order 29) and 58 and 60 (order 30), all DEFERRED, repair units this run has since built and
CLOSED, 52 to 55 among them. Spec 52 rev-10 moved its AC11 to AC14, AC17 and AC29 into spec 55, and spec 54 rev-6
dropped its AC3; these four specs still cite some of those labels. The charter's P19 keeps built work out of
in-place rewrites, and a builder writes no spec. The facts the tree now fixes:

- The version-bump oracle the close runs is the block in CLOSED spec 55's section 4 (exit 0 on a clean walk, 1 when a
  version line moved, 2 on a refusal); spec 44's block is superseded there. It is not product code.
- The placed request race is unit 48's region-eight block in `tools/unattended/unattended.test.sh` as unit 52
  rebuilt it: up to three attempts, each clearing its own handshake files, an overrun or a broken lock discarded.
- The base an observing run passes the oracle is the run's pinned BASE as RUN.md records it.

Re-ground all four specs so a builder can build each as written, each ruling a fork in that spec's §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### brief:items

1. F-fold: an amendment one of these four orders to another of the four (for example 58 and 60 on 56 or 57) is made once, now, in the target spec, and the ordering unit reduces to an observation of that text.
2. F-oracle: an item that corrects the oracle cannot edit CLOSED spec 55. Rule the home so the close still runs exactly one oracle: the recommended answer is that the last of these units to correct it carries the whole corrected block in its own section 4, names spec 55's block superseded there (never edited), and every earlier text names the new block. If an item's correction is already true of spec 55's block, mark the item satisfied and reduce it to its observation.
3. F-closed-specs: every item that edits, bumps or rewrites a CLOSED spec in place is re-scoped: a product change still needed is built and observed; a text-only finding on a closed spec is resolved in this spec's own §4, naming the closing mechanism, and the closed spec is untouched.
4. Probe every item against the tree and cite where it stands by `path#symbol`; replace every cite of a moved or dropped criterion with the criterion that now holds it (spec 55's AC labels for the oracle, unit 52's rebuilt race block for the race); an item a landed unit satisfies is marked so and reduced to its observation or dropped. Narrow each unit to what is left, and say what was narrowed.
5. Replace every line citation with a `path#symbol` citation or a blob pin and every bare file-stem section reference with its alias tag; keep each spec within the live-spec size cap; leave no fork open.

### brief:acceptance

Specs 56, 57, 58 and 60 each at a new rev carry their resolved forks, every amendment the re-grounding found,
`path#symbol` citations and one §9 line naming this brief; `check-memory-hygiene.sh --only 12,25 --spec`, the
spec-token checker, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dPlacedRequest <id>` report nothing for each.

### brief:gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker, the pinned-facts check, the driver's
`--check-specs` and the naming lexicon; no other.

### brief:non-goals

No product code, no commit, no index render, no status flip (all four stay DEFERRED), no spec other than these four.
Pin every figure you write with DERIVED or PINNED on its own line (the pinned-facts check's `--shrink` mode reads
green over reds, so read its plain run), never let a section sign or a section number stand before a unit word, and
never quote a check's hit literally in prose.

### task:reuse

each spec's §10 names its seam (the `write_claim`/`read_claims` CAS ref writer in tools/unattended/unattended.sh becomes the governance-ref factory); recall probe below.

### card:route

- build: dPlacedRequest
- unit: TOOL-dPlacedRequest-56 · spec memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-56.md
- brief: memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
[/memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-56-1-spec-writer.md]
