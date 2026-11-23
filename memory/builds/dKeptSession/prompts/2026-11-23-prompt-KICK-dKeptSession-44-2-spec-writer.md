**Serves:** journal KICK-dKeptSession-44

# gov-spec-writer handoff — KICK-dKeptSession-44

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=KICK-dKeptSession-44 path=memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-44-2-spec-writer.md role-sha=91ec0ce505aa task-sha=e066b83a42df -->

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
- unit: KICK-dKeptSession-44 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-44-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-44-2-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-44`.
Not supplied, optional: `input:code`.

### brief:prompt

> /unattended dKeptSession

### brief:goal

KICK-dKeptSession-44's builder (run `wf_976362ba-48e`) stopped before its first edit and returned a DIVERGENCE. AC29,
and the §7 `New arm:` line for `tools/policy/check_policy.py` that covers it, says `python policy.py check` exits 1
once the `presets-repo` case commits `[presets.strict]`. `tools/policy/policy.py#cmd_check` exits only 0 or 2, and the
case's other refused scenarios in `tools/policy/check_policy.py#run_presets_repo` (`extends-lax`, `never-key`) assert
`rc == 2` and a stderr line opening `policy: refused · .governance/policy.toml:<n>`. The builder also found four stale
texts. Every other code claim held at the builder's base `6a7a6a052`. Revise the spec to the main loop's rulings below.

### brief:items

1. F-exit: resolved by the main loop. AC29 and its `New arm:` line read exit 2, with the stderr refusal line naming the
   `[presets.strict]` line and `strict`, graded the way the case's other refused scenarios are. `tools/policy/policy.py`
   stays out of Files touched. S32's check in `tools/policy/presets.py#check_repo_presets` reaches the CLI through that
   same Refusal.
2. F-dependents: resolved by the main loop. Unit 7 has landed `tools/loop/loop_transition.py#read_dependents`. It is
   called by `write_dependency_notices` and by the `dependents` verb, which `tools/govkit/usage.toml` declares
   (`script:{prefix}/loop/loop_transition.py#dependents`, flags `--build=` and `--root=`) and `help/loop.md` anchors.
   `tools/unattended/unattended.sh#write_landed_notices` runs that verb through `run_loop_verb`.
   - S20's Readers line is rewritten to name those readers.
   - The verb and its flags stay; the usage row does not move.
   - The function's source is re-pointed to the parent README's rendered `<!-- gen:build-edges -->` "Child builds"
     line, as S20 says.
   - Two fixture sets write only the dependent's `parents:` and never the parent's region: the unattended suite's
     `write_landed_dependent` (tRun, tDep), and `tools/loop/loop_transition.py#write_transition_plant` for the
     `deps-notices`, `notices-*` and `chain-two-dependents` plants. Name each in S20 and in Files touched, and say how
     each comes to hold the parent's region as the tree does, so the arms do not read zero dependents. Mind the class
     a double you wrote grades nothing: a fixture spelling the region by hand needs something that holds its shape
     to the render.
   - State the render lag as a limit, in §3 or in S20: a dependent opened after the parent's last
     `gen_build_index.py --write` is not notified until the next render.
3. F-met: S31 is already met. `tools/unattended/mail-notice.js#runDetachedFetch` spawns with `windowsHide: true`.
   Make S31 an observation only, and drop `mail-notice.js` from Files touched unless another clause still edits it.
4. F-figures: the §7 `New arm:` line's floors read `FLOOR_ASSERTIONS` 4180 and `FLOOR_SHARD_8` 1397 at this base.
   Pin each with DERIVED and its derivation, so the builder raises from the figure it reads.
5. F-bound: AC30's 12 s (PINNED 2026-11-23, the rev-6 AC30) bound on the whole `--landed` run leaves 2 s (PINNED
   2026-11-23) past `PROGRESS_BOUND=10` and `timeout -k 5s`,
   which covers the rest of `verb_landed`, including `observe_anchor`, and nothing has measured it. Derive the bound
   from `PROGRESS_BOUND`, the kill grace and a stated margin, rather than a typed 12.
6. F-decisions: S23 writes `memory/DECISIONS.md` only when the driver's census passes its `REFUSAL_CEILINGS` row.
   - `check 49` refuses a pass that declares that shared record.
   - The census reads 347/347 at this base (`python tools/memory-tree/check-arms.py --report`, PINNED 2026-11-23).
   - Say in S23 that a census past its ceiling stops the builder, and the main loop writes the dated decision row
     and both `.memory-tree.conf` rows.
   - Drop `memory/DECISIONS.md` and `.memory-tree.conf` from Files touched.
7. Bump the spec one rev, with one revision-log line naming this brief by its file stem.
   - Cite code by `path#symbol`, and pin every figure with DERIVED or PINNED.
   - Write no `[..](..)` link shape outside the generated records table.
   - Keep within the live-spec size cap, and leave no fork open.

### brief:acceptance

These all report nothing for the spec:
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`
- a plain `bash tools/memory-tree/check-memory-hygiene.sh --only 2`
- `python tools/check-spec-tokens.py --spec <path>`
- a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
- `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-44`

### brief:gates

Only these: the memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts
check and the driver's `--check-specs`.

### brief:non-goals

- No product code, no commit and no index render.
- No spec other than KICK-dKeptSession-44's. Other writers may be revising other specs at the same time: read them,
  never edit them.
- Read files freely; edit only the spec, in the run worktree.

### input:spec

memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md

### task:reuse

each spec's §10 names its seam; probes run: `reuse_lookup.py` per spec at re-ground; recall terms below.

### card:route

- build: dKeptSession
- unit: KICK-dKeptSession-44 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-44.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-44-build-brief.md
[/memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-44-2-spec-writer.md]
