**Serves:** journal TOOL-dPlacedRequest-33

# gov-spec-writer handoff — TOOL-dPlacedRequest-33

<!-- gov:handoff role=gov-spec-writer build=dPlacedRequest unit=TOOL-dPlacedRequest-33 path=memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-33-1-spec-writer.md role-sha=91ec0ce505aa task-sha=6454ece3b7dc -->

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
- unit: TOOL-dPlacedRequest-33 · spec memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md
- brief: memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-33-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dPlacedRequest`, unit `TOOL-dPlacedRequest-33`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dPlacedRequest

### brief:goal

TOOL-dPlacedRequest-33's builder returned a DIVERGENCE (run `wf_699065b9-988`) and committed nothing: S3 deletes both
inline blocks from `skills/session-kickoff/manifest-check.sh` and AC4 greps for neither, but
`skills/session-kickoff/manifest-check.sh#read_card_ref` (called by `#resolve_build_card` and `#write_build_card`)
calls `add_feed_sightings`, defined only in the inline `gov_feed_sh` block, and §3 rules out changing the lookup's
fetch; AC5's stub cannot log no call while the driver's conf load runs git; and the card-store fixture has no
unattended kit and no conf, so S2's dark switch would make every existing remote-ref case miss. Revise the spec to
the main loop's rulings.

### brief:items

1. F-blocks. Add to §8, resolved: "Which inline block leaves the engine, when the card read still sights the feed through `add_feed_sightings`?" (a) only `gov_ref_sh` leaves; `gov_feed_sh` stays until TOOL-dPlacedRequest-34 routes `read_card_ref` through the driver's card-ref verbs; (b) this unit also moves the card read to the driver; (c) both leave and the sighting is dropped. Mark `RESOLVED (agent, 2026-11-20, delegated): (a), rung 3; the smallest change that keeps §3's lookup untouched and every card read sighted, and (b) takes TOOL-dPlacedRequest-34's items, (c) loses the sightings `read_first_seen` reads. widens: none · relaxes: none`. Amend S3 so it deletes `gov_ref_sh` alone and says the engine keeps one feed copy for its reads until TOOL-dPlacedRequest-34; AC4 greps for the `gov_ref_sh` opening marker alone; name `run_card_git`, left with no caller, as deleted.
2. F-stub: AC5 observes that the stubbed git logged no fetch and no push (the driver's conf load always runs one `rev-parse`), rather than no call at all.
3. F-fixture: §4 Files touched's line for `skills/session-kickoff/card-store.fixture.sh` also says the fixture copies the unattended kit into its scratch repository, found through `resolve_kit_file` (never a spelled kit path), and writes a `.unattended.conf` with `RUN_CLAIMS` on for every existing case, so the remote-ref cases keep reading `$REF`; AC1's wording follows.
4. Note in §4 that the engine keeps the local `refs/gov/builds/<slug>/card` and the cache's full sha by reading `refs/gov/remote/builds/<slug>/card` after the driver answers, since the driver prints an abbreviated sha; and that the new verb refuses by printing its line and exiting 2, with no new numbered refusal, the driver being at its refusal ceiling.
5. Re-cite the moved line citations (`derive_claims_line`, the `RUN_CLAIMS` resolution, `print_claims`, `resolve_claim_remote`, the conf's `RUN_CLAIMS` line) as `path#symbol` citations.

### brief:acceptance

Spec 33 at its next rev carries the resolved fork, S3, AC1, AC4, AC5 and §4 amended, `path#symbol` citations, and one
§9 line naming this brief and the divergence; `check-memory-hygiene.sh --only 12,25 --spec` and the spec-token
checker over it report nothing.

### brief:gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### brief:non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-33. Pin every figure you write with DERIVED or PINNED, never let a section sign or a section
number stand before a unit word, never write a bare file-stem section reference, and never quote a check's hit
literally in prose.

### task:reuse

each spec's §10 names its seam (the `write_claim`/`read_claims` CAS ref writer in tools/unattended/unattended.sh becomes the governance-ref factory); recall probe below.

### card:route

- build: dPlacedRequest
- unit: TOOL-dPlacedRequest-33 · spec memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md
- brief: memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
[/memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-33-1-spec-writer.md]
