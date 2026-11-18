**Serves:** journal TOOL-dDeclaredLoop-20

# gov-spec-writer handoff — TOOL-dDeclaredLoop-20

<!-- gov:handoff role=gov-spec-writer build=dDeclaredLoop unit=TOOL-dDeclaredLoop-20 path=memory/builds/dDeclaredLoop/prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-20-1-spec-writer.md role-sha=3db8c2a485df task-sha=c76176727537 -->

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
- unit: TOOL-dDeclaredLoop-31 · spec memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-31.md
- brief: memory/builds/dDeclaredLoop/README.md
[/.claude/orientation-card.md]
[memory/builds/dDeclaredLoop/prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-20-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dDeclaredLoop`, unit `TOOL-dDeclaredLoop-20`.
Not supplied, optional: `input:code`.

### brief:prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. This build's specs predate the code the parent builds and its own earlier units landed. This spec is
re-grounded before its builder is dispatched.

### brief:goal

Revise the spec of TOOL-dDeclaredLoop-20 in place, as a rev bump with one revision-log line, so a builder can build it as written
over HEAD. Where every claim already holds, change nothing and say so in your return.

### brief:items

1. Read the whole spec against the code at HEAD of branch/unattended-declared-loop-d56bf0 and settle every claim the landed
   code has moved. The branch has built every unit through build order 30 but unit 31, which is building now (each a CLOSED
   spec in this build's spec folder), and merged local main and origin/main. The review round bounds are policy keys read
   through `tools/loop/review_bounds.py` (unit 21); the rework budget lives in `tools/loop/budget.py` (unit 30), with homes under
   every transitions.record set (48), an advisory typed figure and union-merged transition records (49), a draw id on every row
   (61), every rotated run record read (60) and the parallel-append-uneven plant (62); unit 32 added the convergence routing,
   `--fix-pass`, `run_budget_verb` and a `budget.py target` verb, raising the driver's refusal census to 332. Unit 31 (rev-4,
   building) adds `--exhausted`, a `budget.py ending` verb and the ending rows, raising the census to 335 under its landed
   decision row: write on its committed spec. Unit 34 is deferred against ask TOOL-dDeclaredLoop-113. An item the built code
   already satisfies leaves the spec's scope, said so.
2. THE SWEEP, before you return: for every function, file, constant and fixture the revised body changes or removes, find every
   caller, reader, fixture, suite arm, test population and frozen or pinned contract (upgrade step rows, subject pins,
   verdict-epoch delegates, census and family ceilings, size caps, the lexicon pin, help anchors and usage rows, the new leg's
   companions with a `stage` key) at the branch tip, and say in section 5 what keeps each green, with the commands that
   re-derive the counts. Unit 21's builder diverged four times on gaps its spec writers had not swept.
3. Check the write set against what the change really touches: registry rows, usage rows, subject pins, the verdict-epoch
   gate's delegate list, the kickoff manifest's watch list, generated map files, any line the install-prefix ban flags, and
   every existing fixture or selftest arm the change could newly red; name each in section 5 with what keeps it green.
4. A choice between designs is a section 8 fork with its options and your recommendation, and the spec body is written on the
   recommendation: the run takes it under its mandate.
5. Keep the unit one mechanism, its carries, its order and its status. Write only that spec file. Do not commit and do not
   regenerate any index.
6. Run the spec-token checker with its spec flag over the revised spec and fix every hit it names. Do not run the whole-tree
   memory hygiene gate, and do not ask any checker for its help text. A figure before a unit word carries PINNED on its line,
   a code citation is a symbol citation, a scope item that takes something away carries its readers clause, and no sentence
   in section 2 uses a retirement word for something it keeps. A by-name reader in a Readers clause is a tracked path,
   never `path#symbol`; name the symbol in words after the path.
7. Never kill a process you did not start, and never match processes by a script's name to stop them: other sessions run the
   same scripts on this node.
8. Unit 20 builds alone at build order 31, and units 22 and 50 together at order 32; where this spec reads a sibling's code, write it on that sibling's committed spec and name the dependency in section 5. Your worktree may be cut from main, which lacks the
   loop kit: read every code claim from branch/unattended-declared-loop-d56bf0 through git show, and say which tree each
   check ran on.
   Never run check-memory-hygiene.sh, not even with --help. Keep each Readers clause's by name: and by value: halves each on
   one line, and name no unit id in a by name: half.
9. Four budgets and records stopped this build's earlier builders; name each the change reaches in section 5 with what
   keeps it green: the lexicon offender pin (every new function name through the lexicon's suggest verb), the shared
   records in `.unattended.conf`'s SHARED_RECORDS (a pass never writes `memory/DECISIONS.md`; spell out any decision row
   the run must land ahead), each script's refusal ceiling and its `.families.txt` families (measured with
   `tools/memory-tree/check-arms.py`'s own readers), and a help anchor for any new verb or flag.

### brief:acceptance

- Every claim the revised spec makes about current code is one you read at HEAD.

### brief:gates

- memory hygiene and spec tokens, at the close.

### brief:non-goals

- No product code, no sibling spec, no new unit.

### input:spec

memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-20.md

### task:reuse

each spec's section 10 names its seam

### card:route

- build: dDeclaredLoop
- unit: TOOL-dDeclaredLoop-31 · spec memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-31.md
- brief: memory/builds/dDeclaredLoop/README.md
[/memory/builds/dDeclaredLoop/prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-20-1-spec-writer.md]
