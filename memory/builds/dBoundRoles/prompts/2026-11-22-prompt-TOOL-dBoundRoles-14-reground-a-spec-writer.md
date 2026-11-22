**Serves:** journal TOOL-dBoundRoles-14

# gov-spec-writer handoff — TOOL-dBoundRoles-14

<!-- gov:handoff role=gov-spec-writer build=dBoundRoles unit=TOOL-dBoundRoles-14 path=memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-reground-a-spec-writer.md role-sha=91ec0ce505aa task-sha=d572b7ff12de -->

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
[memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-reground-a-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dBoundRoles`, unit `TOOL-dBoundRoles-14`.
Not supplied, optional: `input:spec`, `card:route`, `input:code`.

### brief:prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. `check-spec-tokens.py --spec` over every roster spec reds 42 of 59 specs at
`062906ffd`, and `--dispatch` refuses a spec the checker reds. This batch re-grounds its share before any is dispatched.

### brief:goal

Revise each spec named below in place, as a rev bump with one revision-log line each, so
`python tools/check-spec-tokens.py --spec <that spec>` exits 0 and `--dispatch` will admit it.

### brief:items

1. For each spec, fix every hit listed under it, as the checker printed it on 2026-11-22 at `062906ffd`:
   - `[guards]`: add the named leg to the Gates leg line, spelled as `tools/gate-legs.json` names it; or, where the
     path is not one the unit writes at HEAD, correct Files touched and say why in the revision-log line.
   - `[cite]`: the citation names a line of `tools/hooks/agent-cap.js` as it stood at the chain baseline `59ff8f2ac`
     (2427 lines); TOOL-dFairHearing-16 has since moved rules 0, 2 and 5 to the review kit and the file is 1227 lines.
     Find the cited function or constant at HEAD (`git show 59ff8f2ac:tools/hooks/agent-cap.js | sed -n '<N>p'` names
     it; grep HEAD for that name) and re-point the line, or the range, at where it lives now, in whichever file holds
     it. Where the code the spec relies on is gone or changed in behaviour, re-ground the dependent sentence too and
     name the change in the revision-log line.
2. Change nothing else. Each status header keeps its status (`DEFERRED`); bump only the rev. The write grant is this
   batch's spec files alone, listed under Limitations.
3. The specs and their hits:
   - `TOOL-dBoundRoles-14` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md`):
     - [guards] `policy fixtures <- tools/playbook/tag_index.py` — the Files touched list names tools/playbook/tag_index.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-2` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-2.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-1` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md`):
     - [guards] `policy fixtures <- tools/roles/agents/` — the Files touched list names tools/roles/agents/, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2157` — file has 1227 lines
   - `TOOL-dBoundRoles-21` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-21.md`):
     - [guards] `routed-commits selftest <- tools/policy/catalogue.toml` — the Files touched list names tools/policy/catalogue.toml, which trips the guard of leg 'routed-commits selftest', absent from the Gates leg line
     - [guards] `scratch-guard self-test <- tools/policy/catalogue.toml` — the Files touched list names tools/policy/catalogue.toml, which trips the guard of leg 'scratch-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-37` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-37.md`):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-22` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-22.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-49` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-49.md`):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-16` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-16.md`):
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
     - [cite] `tools/hooks/agent-cap.js:2179` — file has 1227 lines
   - `TOOL-dBoundRoles-54` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-54.md`):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-55` (`memory/builds/dBoundRoles/spec/2026-10-26-spec-TOOL-dBoundRoles-55.md`):
     - [guards] `policy fixtures <- tools/govkit/selftest.py` — the Files touched list names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line
   - `TOOL-dBoundRoles-15` (`memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-15.md`):
     - [guards] `routed-commits selftest <- tools/policy/caps.toml` — the Files touched list names tools/policy/caps.toml, which trips the guard of leg 'routed-commits selftest', absent from the Gates leg line
     - [guards] `scratch-guard self-test <- tools/policy/caps.toml` — the Files touched list names tools/policy/caps.toml, which trips the guard of leg 'scratch-guard self-test', absent from the Gates leg line
     - [guards] `policy fixtures <- tools/roles/roles_lib.py` — the Files touched list names tools/roles/roles_lib.py, which trips the guard of leg 'policy fixtures', absent from the Gates leg line

### brief:acceptance

`python tools/check-spec-tokens.py --spec <path>` exits 0 for every spec of this batch; each spec carries the next rev
and one revision-log line naming this brief by its file stem.

### brief:gates

memory hygiene · spec tokens (a spec's own names resolve)

### brief:non-goals

No spec outside this batch. No product code. No change to Scope, Design or Acceptance beyond what a hit forces.

### task:reuse

each spec's §10 names its seam (tools/roles/, tools/hooks/agent-cap.js, tools/workflows/); recall returned TOOL-dBoundRoles-6, TOOL-dWitnessedBar-23.
[/memory/builds/dBoundRoles/prompts/2026-11-22-prompt-TOOL-dBoundRoles-14-reground-a-spec-writer.md]
