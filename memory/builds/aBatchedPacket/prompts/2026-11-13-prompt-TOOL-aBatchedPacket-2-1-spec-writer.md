**Serves:** journal TOOL-aBatchedPacket-2

# gov-spec-writer handoff — TOOL-aBatchedPacket-2

<!-- gov:handoff role=gov-spec-writer build=aBatchedPacket unit=TOOL-aBatchedPacket-2 path=memory/builds/aBatchedPacket/prompts/2026-11-13-prompt-TOOL-aBatchedPacket-2-1-spec-writer.md role-sha=a3bc1199e30f task-sha=13ae873ad36e -->

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
- build: aBatchedPacket
- unit: TOOL-aBatchedPacket-1 · spec memory/builds/aBatchedPacket/spec/2026-11-13-spec-TOOL-aBatchedPacket-1.md
- brief: memory/builds/aBatchedPacket/prompts/2026-11-13-prompt-TOOL-aBatchedPacket-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aBatchedPacket/prompts/2026-11-13-prompt-TOOL-aBatchedPacket-2-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aBatchedPacket`, unit `TOOL-aBatchedPacket-2`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> every verdict and refusal either step produces today is still produced, shown by the existing fixtures and plants [...] and a cache, if you add one, is invalidated by the content it depends on and can never turn a red into a green. State what the new design does not check.

The task is recorded in `memory/builds/aBatchedPacket/prompts/2026-11-13-prompt-TOOL-aBatchedPacket-1-brief.md`; this unit serves the passage above.

### brief:goal

The closing review of `TOOL-aBatchedPacket-1`, round 1, confirmed one HIGH, six MEDIUM and one LOW item over the pass commit `d3ee4c149`. This unit repairs the HIGH and the six MEDIUM items, so that each arm of the front door's suite can fail on the read it names, the new leg clears the meta-gates a bar would red on, and the batched read never answers from another repository. Unit 1's spec is frozen once CLOSED, so each correction is stated in this unit's spec.

### brief:items

1. The report is `memory/builds/aBatchedPacket/reviews/2026-11-13-review-TOOL-aBatchedPacket-1-diff-review-round1.md`. Read it whole; each item below names its heading there, and its fix text and its "probe the build must run" are the starting design.
2. H1: fixture T's parent state must depend on the parent specs' text, with an arm that compares the door's cached answer for each kept parent path with git's own, one path holding a lone CR, and asserts the cache answered.
3. M1: the leg `chain-packet self-test` gets its `leg` row in `tools/playbook/core-pending.txt`, in the sibling `spec-tokens self-test` row's form.
4. M2: the four names the lexicon naming leg grades. Drop the proxy class's dunder, rename the nested helper to a declared verb, and name the suite's two helpers as the lexicon admits; move no pin. `python tools/lexicon/lexicon.py --measure` reads the result.
5. M3: an arm in `tools/check-spec-tokens.test.sh` that fails when the checker stops routing the packet join through a door that sits beside it, with a marker door, and the no-door arm forbidding the marker's line.
6. M4: the fast-path arms CP3, CP4 and CP5 refuse any `chain-packet:` line on stderr, so the report's own fallback cannot pass as a fast run.
7. M5: the leg's guard covers what a whole-tree clone can read, or the suite and the leg state the changed-mode skip by name; and the README insert in the suite's trim refuses a file whose first line is not the front-matter fence or that already holds a status key.
8. M6: the batched parent read is skipped when any git location variable `tree_lib.GIT_ENV_LEAKS` names is set, so the instrument's own git answers, with an arm that runs the door and the instrument under an exported `GIT_DIR` of another repository and compares stdout.
9. L1 is not taken: unit 1's spec states an untracked second file of an instrument's shape as outside what the door checks, with the result a hit or a slow run and never a pass, and the review's twin finding was refuted on that ground. Say so in the non-goals.
10. Write one spec, `memory/builds/aBatchedPacket/spec/2026-11-13-spec-TOOL-aBatchedPacket-2.md`, Tier-2, status SPECCED, rev-1, node a, base `d3ee4c149`, streams tooling, order 2, in the shape `memory/TEMPLATE-SPEC.md` states, with unit 1's spec beside it as the worked example. Each scope item names its criterion or the words NOT OBSERVED on one line. Every line stating a figure with a unit carries PINNED or a commit sha. The acceptance section cites no path the unit has not built.
11. Each repaired arm is declared on a `New arm:` line with the staged break that reds it, taken from the report's probe. The suite's budget row moves to its measured reading: the first run took 236 s on node `a` (PINNED 2026-11-13).
12. Before returning, stage the spec and clear `python tools/check-spec-tokens.py --spec` over it. Run no whole-tree hygiene, no bar and no self-test suite, and do not commit. Return the spec path, its status line, each criterion with one line, every fork with a recommendation the builder can take, and the checker's final line.

### brief:acceptance

- Each `New arm:` line's arm is red on its staged break and green without it, observed by the main loop.
- `python tools/lexicon/lexicon.py --measure` prints the pin `.lexicon.conf` holds.
- `git diff --quiet 8db6f4bef HEAD -- memory/builds/dClosedLoop/build/` exits 0.
- The door's `--check dDeclaredLoop` on the frozen clone still prints the instrument's eight lines and exits 1.

### brief:gates

The door's suite and the spec-token checker's suite, run directly by the main loop. No full bar while the dDeclaredLoop run is live.

### brief:non-goals

- L1, the door's working-tree glob against the checker's tracked list, which unit 1's spec states as outside the door's check.
- Any byte under `memory/builds/dClosedLoop/build/`, anything under `memory/builds/dDeclaredLoop/`, and `tools/unattended/unattended.sh`.
- The two parity arms of `tools/check-spec-tokens.test.sh` that are red at the base `8db6f4bef` and name `routed_commits.py --selftest` and the playbook fixture legs.
- The deferred class-level gate over leg guards that the report's M5 names.

### task:reuse

tools/memory-tree/tree_lib.py#read_blobs_at; tools/check-spec-tokens.py#scan_live_packets; ask TOOL-dGroundRules-112.

### card:route

- build: aBatchedPacket
- unit: TOOL-aBatchedPacket-1 · spec memory/builds/aBatchedPacket/spec/2026-11-13-spec-TOOL-aBatchedPacket-1.md
- brief: memory/builds/aBatchedPacket/prompts/2026-11-13-prompt-TOOL-aBatchedPacket-1-brief.md
[/memory/builds/aBatchedPacket/prompts/2026-11-13-prompt-TOOL-aBatchedPacket-2-1-spec-writer.md]
