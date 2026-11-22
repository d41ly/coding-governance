**Serves:** journal KICK-dKeptSession-69

# gov-spec-writer handoff — KICK-dKeptSession-69

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=KICK-dKeptSession-69 path=memory/builds/dKeptSession/prompts/2026-11-22-prompt-KICK-dKeptSession-69-1-spec-writer.md role-sha=91ec0ce505aa task-sha=1e2a158d547f -->

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
- unit: KICK-dKeptSession-37 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-37.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-37-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dKeptSession/prompts/2026-11-22-prompt-KICK-dKeptSession-69-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-69`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dKeptSession

### brief:goal

`origin/main` has moved 634 commits (DERIVED, `git rev-list --count c2a407b0..8b8b1374`) past this run's BASE `c2a407b0`. dWitnessedBar landed at `8b8b1374`. Since then the
pre-commit leg set has refused every commit that stages a kickoff-engine or policy-kit path. Seven of its 100 legs (DERIVED, the hook's `gates RED — 7/100` line) are
red on the run head:

- Tied to `origin/main`:
  - `drift-audit records`: RATCHET WEAKENED against origin/main's pins.
  - `policy check`: `arm_reader_coverage` finds 20 keys dWitnessedBar landed with no reader in this tree.
- Left by this run's own units:
  - `shell hygiene (a location probe asked from a moved directory)`, at three sites in `skills/session-kickoff/card-store.fixture.sh`.
  - `shell hygiene (a stage committed with no staged-diff test)`, at one site in the same file.
  - `shell hygiene (a fork spent on builtin work)`: `pure-fn-subst` in `skills/session-kickoff/manifest-check.sh` measures 5 against a registry
    of 2, and `cat-file` in `tools/hooks/scratch-guard.test.sh` measures 20 against 11.
  - `python reads`: the build-index selftest, gotchas selftest, memory-recall kit selftest and recall floor legs import
    `tools/policy/presets.py` and `tools/memory-tree/design_lib.py` outside their guards.
  - `step-rows-frozen`: KICK-dKeptSession-4 changed `tools/govkit/steps/kickoff_facts_to_overlay.py`, the program a landed
    step's argv names. The leg says to ship the correction as a new step.

A trial `git merge --no-commit --no-ff origin/main` on the run branch conflicts in 13 files (DERIVED, `git diff --name-only --diff-filter=U`):

- Product code:
  - `tools/policy/policy.py` (6 hunks), `tools/policy/check_policy.py` (2), `tools/policy/kit.toml` (2), `tools/policy/README.md` (4).
- Generated:
  - `.governance/policy.json`, `help/reference/policy.md`, `memory/map/generated/symbols.json`.
- Row registries:
  - `memory/project/positional-refs.txt`, `memory/project/unpinned-facts.txt`, `memory/project/docs-undocumented.txt`,
    `tools/playbook/core-pending.txt`, `tools/run-gates/selftest-budgets.txt`.
- The kickoff manifest stamp: `memory/guides/SESSION-KICKOFF.md`.

The product conflicts are one design collision. TOOL-dWitnessedBar-20 moved the legacy-homes list into a ledger population
at `memory/project/legacy-homes.txt`, graded and written by the baseline ledger factory and registered in govkit's registry.
KICK-dKeptSession-19 built a shrink-list factory (`read_shrink_base`, `write_shrink_file`) over that same list. It also put
the unscanned-readers list, KICK-dKeptSession-19's unnamed-keys list and KICK-dKeptSession-16's unpurposed-namespaces list
through it. `[reuse]` allows one factory per kind.

Write the spec of KICK-dKeptSession-69 as a new file, `memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-69.md`,
to `memory/TEMPLATE-SPEC.md`:

- Header: `INPROGRESS`, rev-1, 2026-11-22, node d, Tier-2, base the run head, streams tooling, order 9, advances
  KICK-dKeptSession-29.
- Second line: `**Derived:** PLAY-dClosedLoop-2`, the binding KICK-dKeptSession-67 carries.

### brief:items

1. F-merge: every commit in this worktree runs the PRIMARY tree's hooks (`core.hooksPath` names
   `C:\projects\coding-governance\.githooks`), and the primary tree now sits at `origin/main` `8b8b1374`. So every commit,
   a records-only one included, now meets main's hooks over this branch's pre-main tree, and is refused. No dispatch row,
   brief or spec can be committed first, and a pass worktree is not reachable. The reconcile is therefore ONE commit on the
   run branch, made the way `push-main.sh`'s conflict refusal says: the main loop runs `git merge --no-ff --no-commit
   origin/main` in the run worktree, the unit's builder resolves the conflicts and makes this unit's fixes in that
   worktree, and the main loop commits the merge, with this spec, its records and `Pass: KICK-dKeptSession-69`, once
   main's hooks pass over it. State the resolution for each of the 13 files (DERIVED, as above):
   - Generated outputs are re-rendered, never hand-merged.
   - Row registries are unioned, then shrunk or re-derived by their own verbs.
   - The kickoff manifest is re-stamped.
   - Each product hunk follows F-factory.
2. F-factory: decide how the two factories meet, with the alternatives in §4's rejected list. The default is the
   feature-rich, single-factory one: legacy-homes is the ledger population as main has it, and this run's other lists move
   onto main's baseline ledger factory, with the shrink-list factory deleted. If you keep the shrink-list factory, give the
   reason main's factory cannot carry those lists. Name every caller that changes (KICK-dKeptSession-19's and -16's arms and
   cases, `cmd_lists`, `check_policy.py`'s fixtures), and every CLOSED unit's spec text this supersedes. That superseded
   text is answered in this unit's own acceptance ledger, as KICK-dKeptSession-49 rev-6 ruled.
3. F-own-reds: name the fix for each of the five red legs this run left, and the criterion that observes each leg green:
   - Shell hygiene: scrub the three location probes; test the stage before the fixture's commit; bring each `$(f …)` and
     `$(cat …)` count back to its registry row through the no-fork forms.
   - `python reads`: widen each named leg's guard in `tools/gate-legs.json` to the module it imports.
   - `step-rows-frozen`: restore the landed step program's bytes, and ship KICK-dKeptSession-4's scaffold change as a new
     step row, as the leg's remedy says.
   Read `tools/govkit/upgrade_steps.py#check_frozen` and the step registry for how a new step is declared.
4. F-inherited: check whether the two legs tied to `origin/main` go green on the merged tree. Where one stays red, find
   whether it is red on `origin/main` itself, then either attribute it with `GATE_ATTRIBUTE` or fix it, and say which.
5. F-behaviour: every criterion names its command and the exit and output it observes. The pass legs
   (`bash tools/run-gates/pass-legs.sh`) and the policy fixtures are named in §7. No suite runs in the pass.
6. Hook paths, citations and size, as the build's other specs keep them:
   - Files touched names every path the merge and the fixes move, including `symbols.json`, `selftest-budgets.txt` where a
     `plants=` token moves, and the kickoff manifest re-stamp.
   - Cite code as `path#symbol`; leave no `path:number` token unless it is a blob pin.
   - Pin every figure, keep within the live-spec size cap, and leave no fork open except one that would change a
     governance carrier.

### brief:acceptance

The new spec exists. `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, `--only 29`,
`python tools/check-spec-tokens.py --spec <path>`, a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
and `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-69` report nothing for it.

### brief:gates

The memory hygiene gate, the spec-token checker, the pinned-facts check, the driver's `--check-specs` and the naming
lexicon; no other.

### brief:non-goals

No product code, no commit, no index render, and no spec other than the new one. Do not start the merge in the run
worktree. Read `origin/main` with `git show origin/main:<path>` and `git diff HEAD...origin/main -- <path>`.

### task:reuse

each spec's §10 names its seam; probes run: `reuse_lookup.py` per spec at re-ground; recall terms below.

### card:route

- build: dKeptSession
- unit: KICK-dKeptSession-37 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-37.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-37-build-brief.md
[/memory/builds/dKeptSession/prompts/2026-11-22-prompt-KICK-dKeptSession-69-1-spec-writer.md]
