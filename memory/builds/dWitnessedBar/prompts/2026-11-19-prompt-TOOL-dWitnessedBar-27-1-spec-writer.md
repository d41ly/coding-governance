**Serves:** journal TOOL-dWitnessedBar-27

# gov-spec-writer handoff — TOOL-dWitnessedBar-27

<!-- gov:handoff role=gov-spec-writer build=dWitnessedBar unit=TOOL-dWitnessedBar-27 path=memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-27-1-spec-writer.md role-sha=91ec0ce505aa task-sha=50291e4cff0d -->

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
[memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-27-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dWitnessedBar`, unit `TOOL-dWitnessedBar-27`.
Not supplied, optional: `input:spec`, `card:route`, `input:code`.

### brief:prompt

> /unattended dWitnessedBar

— owner, 2026-11-19, starting this build run. Its first `--dispatch` refused at check 49 because the spec-token checker
reds on a spec once it is live, and `check-spec-tokens.py --spec` over every remaining roster spec reds 101 hits in 48
specs. This batch re-grounds its share before any of them is dispatched.

### brief:goal

Revise each spec named below in place, as a rev bump with one revision-log line each, so
`python tools/check-spec-tokens.py --spec <that spec>` exits 0 and `--dispatch` will admit it.

### brief:items

1. For each spec, fix every hit listed under it, as the checker printed it on 2026-11-19 at `c6df3e901`:
   - `[guards]`: add the named leg to the §7 leg line, spelled as `tools/gate-legs.json` names it; or, where the path
     is not one the unit writes at HEAD, correct §4 Files touched and say why in the revision-log line.
   - `[leg]`: the token is not a leg name in `tools/gate-legs.json`; replace it with the leg that now carries that
     check, found by reading `tools/gate-legs.json`, or drop it when none does.
   - `[path]`: the cited path is not tracked; re-point it at the tracked file that holds the fact, or rewrite the
     citation so it no longer reads as a path.
   - `[bar]`: an acceptance observation spells a suite; rewrite it as the staged break, `--selftest` flag or fixture
     observation the checker names, keeping the suite on a `New arm:` line.
   - `[source]`: a shell file sourced by bare name; spell the sourcing through the kit-relative path the kit uses.
2. Change nothing else. Each status header keeps its status (`DEFERRED`); bump only the rev. The write grant is this batch's spec files alone, each `memory/builds/dWitnessedBar/spec/2026-10-25-spec-<id>.md`: TOOL-dWitnessedBar-27, TOOL-dWitnessedBar-48, TOOL-dWitnessedBar-49, TOOL-dWitnessedBar-50, TOOL-dWitnessedBar-12, TOOL-dWitnessedBar-22, TOOL-dWitnessedBar-19, TOOL-dWitnessedBar-11, TOOL-dWitnessedBar-14, TOOL-dWitnessedBar-16, TOOL-dWitnessedBar-46, TOOL-dWitnessedBar-54.
3. The specs and their hits:
   - `TOOL-dWitnessedBar-27` (order 2):
     - [guards] `routed-commits selftest <- tools/policy/check_policy.py` — the Files touched list names tools/policy/check_policy.py, which trips the guard of leg 'routed-commits selftest', absent from the §7 leg line
     - [guards] `branch-guard self-test <- tools/memory-tree/check-memory-hygiene.sh` — the Files touched list names tools/memory-tree/check-memory-hygiene.sh, which trips the guard of leg 'branch-guard self-test', absent from the §7 leg line
     - [guards] `playbook render selftest <- tools/memory-tree/corpus_ids.py` — the Files touched list names tools/memory-tree/corpus_ids.py, which trips the guard of leg 'playbook render selftest', absent from the §7 leg line
     - [guards] `policy fixtures <- tools/govkit/govkit.py` — the Files touched list names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-48` (order 2):
     - [bar] `python measure_legs.py --selftest` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete; this spells the manifest leg `measure-legs selftest`, a suite by its declared ceiling of 500 s (PINNED, tools/gate-legs.json)
     - [guards] `policy fixtures <- tools/memory-tree/row_grammar.py` — the Files touched list names tools/memory-tree/row_grammar.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-49` (order 2):
     - [bar] `python measure_legs.py --selftest` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete; this spells the manifest leg `measure-legs selftest`, a suite by its declared ceiling of 500 s (PINNED, tools/gate-legs.json)
   - `TOOL-dWitnessedBar-50` (order 3):
     - [guards] `policy fixtures <- tools/check-line-length.sh` — the Files touched list names tools/check-line-length.sh, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-12` (order 5):
     - [leg] `agent-instructions self-test` — not a name in tools/gate-legs.json
     - [guards] `policy fixtures <- tools/gate-legs.json` — the Files touched list names tools/gate-legs.json, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-22` (order 6):
     - [leg] `agent-instructions self-test` — not a name in tools/gate-legs.json
     - [guards] `policy fixtures <- tools/gate-legs.json` — the Files touched list names tools/gate-legs.json, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-19` (order 7):
     - [leg] `agent-instructions self-test` — not a name in tools/gate-legs.json
     - [guards] `policy fixtures <- tools/gate-legs.json` — the Files touched list names tools/gate-legs.json, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-11` (order 8):
     - [leg] `agent-instructions self-test` — not a name in tools/gate-legs.json
     - [path] `json;L=json.load(open('tools/gate-legs.json',encoding='utf-8'));print(sum(1` — not tracked by git ls-files
     - [guards] `policy fixtures <- tools/gate-legs.json` — the Files touched list names tools/gate-legs.json, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-14` (order 9):
     - [guards] `policy fixtures <- tools/memory-tree/kit.toml` — the Files touched list names tools/memory-tree/kit.toml, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-16` (order 10):
     - [path] `memory/map/baseline.txt` — not tracked by git ls-files
     - [path] `memory/map/baseline.txt` — not tracked by git ls-files
     - [guards] `branch-guard self-test <- tools/memory-tree/check-memory-hygiene.sh` — the Files touched list names tools/memory-tree/check-memory-hygiene.sh, which trips the guard of leg 'branch-guard self-test', absent from the §7 leg line
     - [guards] `playbook render selftest <- tools/lexicon/lexicon-suffix-waivers.txt` — the Files touched list names tools/lexicon/lexicon-suffix-waivers.txt, which trips the guard of leg 'playbook render selftest', absent from the §7 leg line
   - `TOOL-dWitnessedBar-46` (order 10):
     - [guards] `branch-guard self-test <- tools/memory-tree/check-memory-hygiene.sh` — the Files touched list names tools/memory-tree/check-memory-hygiene.sh, which trips the guard of leg 'branch-guard self-test', absent from the §7 leg line
     - [guards] `policy fixtures <- tools/memory-tree/kit.toml` — the Files touched list names tools/memory-tree/kit.toml, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
   - `TOOL-dWitnessedBar-54` (order 10):
     - [guards] `policy fixtures <- tools/govkit/govkit.py` — the Files touched list names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line

### brief:acceptance

`python tools/check-spec-tokens.py --spec <path>` exits 0 for every spec of this batch; each spec carries the next rev
and one revision-log line naming this brief by its file stem.

### brief:gates

memory hygiene · spec tokens (a spec's own names resolve)

### brief:non-goals

No spec outside this batch. No product code. No change to Scope, Design or Acceptance beyond what a hit forces.

### task:reuse

each spec's §10 names its seam; build-level recall terms below.
[/memory/builds/dWitnessedBar/prompts/2026-11-19-prompt-TOOL-dWitnessedBar-27-1-spec-writer.md]
