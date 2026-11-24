**Serves:** journal KICK-dKeptSession-69

# gov-spec-writer handoff — KICK-dKeptSession-69

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=KICK-dKeptSession-69 path=memory/builds/dKeptSession/prompts/2026-11-22-prompt-KICK-dKeptSession-69-3-spec-writer.md role-sha=91ec0ce505aa task-sha=b385a5eab689 -->

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

## Card

[.claude/orientation-card.md · Level 1 · the build's card: where this session stands; level 0 outranks it]
- build: dKeptSession
- unit: KICK-dKeptSession-37 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-37.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-37-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dKeptSession/prompts/2026-11-22-prompt-KICK-dKeptSession-69-3-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-69`.
Not supplied, optional: `input:code`.

### brief:prompt

> /unattended dKeptSession

### brief:goal

KICK-dKeptSession-69's builder returned a DIVERGENCE before any edit. S5 seeds `memory/project/unnamed-keys.txt` and
`memory/project/unpurposed-namespaces.txt`. Memory hygiene check 3 (`tools/memory-tree/check-memory-hygiene.sh`) admits a
file directly under `memory/project/` only when the kit's named list holds it, or when `PROJECT_REGISTRY_EXTRA` in
`.memory-tree.conf` names it exactly. Neither new name is there, and `.memory-tree.conf` is not in §4's Files touched.
`legacy-homes.txt` went the same route on main (TOOL-dWitnessedBar-20 §8 F7, its member note in `.memory-tree.conf`).

### brief:items

1. S5 adds the two names to `PROJECT_REGISTRY_EXTRA`, each with a member note in the style of `legacy-homes.txt`'s, and
   `.memory-tree.conf` joins Files touched, tied to S5. Add a criterion, or extend one, that observes check 3 admitting
   both homes.
2. Re-read the rest of S5 for any other path the two new homes or their registrations move, a `.gitattributes`
   `merge=rows` line and govkit's registry included, and list each in Files touched.
3. Bump the spec to rev-2, with one revision-log line naming this brief by its file stem.

### brief:acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `python tools/check-spec-tokens.py --spec <path>`
and `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-69` report nothing for the spec.

### brief:gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the driver's `--check-specs`; no other.

### brief:non-goals

No product code, no commit, no index render, no spec other than KICK-dKeptSession-69's, and no change to the merge
that is in progress in the run worktree. Read files; edit only the spec.

### input:spec

memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-69.md

### task:reuse

each spec's §10 names its seam; probes run: `reuse_lookup.py` per spec at re-ground; recall terms below.

### card:route

- build: dKeptSession
- unit: KICK-dKeptSession-37 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-37.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-37-build-brief.md
[/memory/builds/dKeptSession/prompts/2026-11-22-prompt-KICK-dKeptSession-69-3-spec-writer.md]
