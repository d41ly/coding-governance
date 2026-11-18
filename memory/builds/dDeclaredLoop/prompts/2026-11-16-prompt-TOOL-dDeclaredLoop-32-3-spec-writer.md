**Serves:** journal TOOL-dDeclaredLoop-32

# gov-spec-writer handoff — TOOL-dDeclaredLoop-32

<!-- gov:handoff role=gov-spec-writer build=dDeclaredLoop unit=TOOL-dDeclaredLoop-32 path=memory/builds/dDeclaredLoop/prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-32-3-spec-writer.md role-sha=3db8c2a485df task-sha=1fd6a9b878fe -->

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
- build: dDeclaredLoop
- unit: TOOL-dDeclaredLoop-32 · spec memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md
- brief: memory/builds/dDeclaredLoop/README.md
[/.claude/orientation-card.md]
[memory/builds/dDeclaredLoop/prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-32-3-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dDeclaredLoop`, unit `TOOL-dDeclaredLoop-32`.
Not supplied, optional: `input:code`.

### brief:prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The first dispatch of TOOL-dDeclaredLoop-32 built rev-5 nearly whole, then returned a divergence: two of its
scope items change behaviour `tools/unattended/unattended.test.sh` already asserts, and §5's sweep names neither the arms nor how
each stays green. The no-fall rule for spec subjects makes a flat spec subject read CONVERGING under the suite's fixed-count-7
policy, so four arms that drive a spec subject to NON-CONVERGENT and promote (subjects `F1 (fork)`, `S1`, `D2`, `S8`) are
refused; and the promotion target on every promoting exit changes eight exact-row assertions. The return is
`memory/builds/dDeclaredLoop/build/2026-11-16-build-TOOL-dDeclaredLoop-32-1-builder-return.md`; the builder's work is saved as a
patch the next builder will reuse.

### brief:goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md` as rev-6, with one revision-log line naming
that return, so §5's sweep names every suite arm the change reaches and how each is kept green or re-planted.

### brief:items

1. Your worktree may be cut from main. First replace your copy of the spec with the branch's, through
   `git show branch/unattended-declared-loop-d56bf0:<path>`, and read every code claim from that branch the same way. Read the
   return whole.
2. Write the four spec-subject arms' re-plant as a section 8 fork. Options include re-planting each on the build slug (whose
   closing bound still reaches NON-CONVERGENT and promotes), planting a BOUNDED exit where the arm tests the row's shape, or
   retiring an arm whose path no longer exists, with its readers. Recommend by the ratify rule, preferring the option that
   keeps what each arm tests; mark it RESOLVED (agent, 2026-11-16, delegated) and write the body on it, naming each arm.
3. Name the eight exact-row assertions the return lists, each re-pointed to carry ` · to units` before the disposition, in §5
   and in §4 Files touched.
4. Re-run the sweep's `review_state` and `verb_review` rows over the suite at the branch tip and record every arm that drives
   either, with its fate.
5. Keep the unit one mechanism, its carries, its order and its INPROGRESS status. Write only that spec file. Do not commit and do
   not regenerate any index. Run the spec-token checker with its spec flag over the spec on the branch's tree and fix every
   hit. Do not run the whole-tree memory hygiene gate, and do not ask any checker for its help text. Keep the spec's
   `<!-- gen:spec-records -->` region and its closing marker exactly as the branch has them.
6. Never kill a process you did not start, never match processes by a script's name to stop them, and never run
   check-memory-hygiene.sh, not even with --help.

### brief:acceptance

- Every suite arm the change reaches is named in §5 with its fate, and the spec-token checker reports no unwaived hit.

### brief:gates

- memory hygiene and spec tokens, at the close.

### brief:non-goals

- No product code, no sibling spec, no new unit.

### input:spec

memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md

### task:reuse

each spec's section 10 names its seam

### card:route

- build: dDeclaredLoop
- unit: TOOL-dDeclaredLoop-32 · spec memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-32.md
- brief: memory/builds/dDeclaredLoop/README.md
[/memory/builds/dDeclaredLoop/prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-32-3-spec-writer.md]
