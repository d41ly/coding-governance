**Serves:** journal TOOL-dPlacedRequest-28

# gov-spec-writer handoff — TOOL-dPlacedRequest-28

<!-- gov:handoff role=gov-spec-writer build=dPlacedRequest unit=TOOL-dPlacedRequest-28 path=memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-28-1-spec-writer.md role-sha=91ec0ce505aa task-sha=7191918f232e -->

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
- unit: TOOL-dPlacedRequest-28 · spec memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md
- brief: memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-28-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dPlacedRequest`, unit `TOOL-dPlacedRequest-28`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dPlacedRequest

### brief:goal

TOOL-dPlacedRequest-28's builder returned a DIVERGENCE (run `wf_2cdc917a-db6`) and committed nothing: at rev-3 the
spec's AC5 checks a call no code makes, so it can never go red; S2 names the driver's run-claim create without its
refusal shape, the read's home or a criterion; and the §4 refusal line names a holder nothing supplies. Revise the
spec to the main loop's three rulings so it can be built as written.

### brief:items

1. F2, the read's home. Add to §8, resolved: "Where does the create's feed read live, when every lease commit is built in `tools/unattended/unattended.sh#write_claim`?" (a) in `write_claim`, once, for every create with an empty parent, the `--lease` verbs and the driver's own claims alike; (b) at each caller. Mark `RESOLVED (agent, 2026-11-19, delegated): (a), rung 3; one commit builder, one read, and no caller can skip it. widens: none · relaxes: none`. Amend S1, S4 and §4 so the read sits in `write_claim` and the inline TOOL-dPlacedRequest-16 S5 read in `run_lease_verb` moves into it. Rewrite AC5 as a behaviour probe: `write_claim` with a create over a feed whose newest event names the ref builds no parentless commit (the commit's parent is the feed's commit), red on a staged copy whose `write_claim` skips the read.
2. F3, the driver's create on a feed tombstone. Resolved: `write_claim` returns a code of its own for a tombstone, distinct from rc 1's lost race, and the driver's callers map it exactly as TOOL-dPlacedRequest-16 §4 "The class order" maps a tombstone: the preflight and take-over columns fail check 107, the holder column check 108, each message carrying `tombstone`; the status column announces one line carrying `tombstone`, writes nothing and leaves the exit status unchanged; the `--lease` verbs print `lease refused — tombstone` and exit 1. Mark `RESOLVED (agent, 2026-11-19, delegated): a distinct return code mapped as unit 16's class order maps a tombstone, rung 3; one refusal vocabulary for a tombstone wherever it is met. widens: none · relaxes: none`. Add one acceptance criterion: `--preflight` of a slug whose feed's newest event is a build tombstone (no remote ref) exits 1 with check 107 and `tombstone`, and the remote gains no ref.
3. The refusal line: §4 Design's line keeps the tree's wording, naming the feed commit (this node's feed last saw its tombstone at that commit) and no holder; drop `<holder in the feed's record>`.
4. Cite code as `path#symbol` throughout the revised sections.

### brief:acceptance

Spec 28 at rev-4 carries F2 and F3 resolved, S1, S2, S4, §4 and AC5 amended to them, the new preflight criterion,
the refusal line corrected, and one §9 line naming this brief and the divergence; `check-memory-hygiene.sh --only
12,25 --spec` and the spec-token checker over it report nothing.

### brief:gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### brief:non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-28. Pin every figure you write with DERIVED or PINNED, never let a section sign stand before a
unit word, and never quote a check's hit literally in prose.

### task:reuse

each spec's §10 names its seam (the `write_claim`/`read_claims` CAS ref writer in tools/unattended/unattended.sh becomes the governance-ref factory); recall probe below.

### card:route

- build: dPlacedRequest
- unit: TOOL-dPlacedRequest-28 · spec memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-28.md
- brief: memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
[/memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-28-1-spec-writer.md]
