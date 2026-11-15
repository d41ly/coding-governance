**Serves:** journal TOOL-aPiecewiseGrade-1

# gov-spec-writer handoff — TOOL-aPiecewiseGrade-1

<!-- gov:handoff role=gov-spec-writer build=aPiecewiseGrade unit=TOOL-aPiecewiseGrade-1 path=memory/builds/aPiecewiseGrade/prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-1-1-spec-writer.md role-sha=a3bc1199e30f task-sha=5080df5d06c5 -->

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
[memory/builds/aPiecewiseGrade/prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-1-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aPiecewiseGrade`, unit `TOOL-aPiecewiseGrade-1`.
Not supplied, optional: `input:spec`, `card:route`, `input:code`.

### brief:prompt

> Open a new build in coding-governance, through `/session-kickoff`, for an incremental, per-spec `tools/check-spec-tokens.py` mode. It must let `--dispatch` (`run_spec_token_check` in `tools/unattended/unattended.sh`) grade only what a pass commit moved, without changing any verdict. Build aLightenedLoop, unit TOOL-aLightenedLoop-3, found that scoping the check to the dispatching build moves cross-build joins: stale waiver rows, chain carries findings and packet runs. The owner therefore declined scoping there. Read `memory/builds/aLightenedLoop/spec/2026-11-14-spec-TOOL-aLightenedLoop-3.md`, §4 "Why the check is not scoped" and §3. Done means a READY card and specs that state how per-spec inputs are keyed and how cross-build joins stay whole. Stop at READY for the owner's go.

> aLightenedLoop (branch `branch/alightenedloop-eb7b8b`, not yet landed) re-keyed `--dispatch`'s spec-token cache on a digest of the inputs the checker read (`--input-key`, `SPEC_TOKENS_INPUTS`), replacing HEAD. A pass that moves any input the whole-tree checker reads still misses the cache and pays the full check, which runs for about a minute. The next step is a checker that re-grades only the specs whose inputs moved, with identical verdicts, refusal text and bytes. Wait for aLightenedLoop to land before basing on it.

The task came from the session that started this one, on the owner's behalf. Both passages are quoted whole.

### brief:goal

A `--dispatch` after a pass commit runs the spec-token checker in a mode that re-grades only the specs whose own inputs moved, and rebuilds every cross-build join whole from the full set of per-spec findings, so its stdout bytes and exit status equal the whole-tree run's on every tree.

### brief:items

1. aLightenedLoop is not on main. Read its checker and driver at its head `d9f84ee14`, through `git show d9f84ee14:<path>` or its worktree `C:/projects/coding-governance/.claude/worktrees/alightenedloop-eb7b8b`, and main's at `aebbb4a72`, where aBriskDeclaration has split `run_spec_token_check` into a start half and a read half. Both files differ between the two; the design is for the tree after aLightenedLoop reconciles onto main, and each spec names what it read at which sha. Cite by blob-pinned line `<path>@<oid>:<n>` or `path#symbol`.
2. Read TOOL-aLightenedLoop-3 at `d9f84ee14`, `memory/builds/aLightenedLoop/spec/2026-11-14-spec-TOOL-aLightenedLoop-3.md`: §3, §4 "Why the check is not scoped", "When the cache hits" and "What the key does not check". This build is the follow-up its §3 names.
3. Split the whole-tree run of `main` in `tools/check-spec-tokens.py` into two classes, by reading the code: per-spec grading, whose result is a function of one spec and the inputs it reads; and cross-spec joins, whose result depends on several specs, such as the live and terminal sort, the stale waiver rows, the carries join, the packet join, the supersede and handoff scans, the size high-water mark and the uid set. Give every step a row: its function, its class, and every input it reads, files, listings and git answers.
4. Measure first, at `d9f84ee14` on node a: the whole-tree wall, and how it divides between per-spec grading and the joins. If the joins cost most of the run, say so plainly, with the figure, as the spec's first finding; the build is then not worth building as briefed, and that is a fork for the owner.
5. Unit 1, TOOL-aPiecewiseGrade-1: the checker's incremental mode. State how each spec's inputs are keyed: what one cache entry holds (a spec's raw findings before any waiver or join is applied), what its key digests (that spec's bytes, every file, listing and git answer its grading read, the checker, its kit modules and the conf keys it read), and how those inputs are recorded. Reuse aLightenedLoop's tracer, `arm_input_trace` and `read_open_py`, and its replay, `derive_input_digest`, per spec rather than per run, unless the code shows a better seam; say which. A key derivation that cannot be replayed means a re-grade, never a hit.
6. State how every cross-build join stays whole: each join runs on every incremental run over the full finding set, cached and fresh alike, and the spec shows for each join why its answer equals the whole-tree run's. The stale waiver rows, the carries finding that names a chain build bare and the packet runs are named one by one.
7. The incremental run's stdout lists every finding in the whole-tree run's order and spelling, and ends with the same summary line and exit status. A cache entry is written only when the tree and HEAD did not move while the checker ran, as TOOL-aLightenedLoop-3 S6 records its key.
8. Unit 2, TOOL-aPiecewiseGrade-2: `run_spec_token_check` runs the incremental mode on a miss of aLightenedLoop's whole key, with the per-spec cache under the sidecar root `resolve_sidecar_dir` names; the skip line, the cache-off line and every refusal keep their bytes; the verbs guide states the new run in both copies.
9. Acceptance rests on a differential arm: the plain and the incremental checker run over the same sequence of fixture trees, and their stdout and exit status are compared byte for byte at every step. Plants: a spec flipped CLOSED so a waiver row turns stale; a waiver whose only hit is retired; a chain carries finding naming a chain build bare; a live chain run with a packet; an edit to a file one spec cites; a tracked file appearing at a path probed only by `is_file`; a kit module edit; a conf cutoff moved. Plus one count: after a commit that moves one spec, the incremental run re-grades one spec.
10. Name each new function, flag, variable and file through `python tools/lexicon/lexicon.py --suggest`, and state what the change owes beyond the code: the codebase map, the symbols index, the kit version, the verbs guide, a `help/` page.
11. Each spec states what its design does not check, starting from TOOL-aLightenedLoop-3's "What the key does not check".
12. A choice that is not derivable is a fork in the spec's open questions with options and a recommendation. Where a per-spec cache is shared between slugs, and whether the bar's spec-tokens leg may later use the mode, are candidates.
13. Write two specs, `memory/builds/aPiecewiseGrade/spec/2026-11-15-spec-TOOL-aPiecewiseGrade-1.md` and `-2.md`, Tier-2, status SPECCED, rev-1, node a, base `aebbb4a72`, streams tooling, orders 1 and 2, in the shape `memory/TEMPLATE-SPEC.md` states. Work only in this worktree.
14. Before returning, stage both specs and clear `python tools/check-spec-tokens.py --spec` over each and `python tools/playbook/positional.py check`. Run no whole-tree hygiene, no merge bar and no self-test suite, and do not commit. Return each spec's path and status line, each criterion's id with one line, every fork with its recommendation, the item-4 measurement, and the checker's final line.

### brief:acceptance

- The differential arm's every step prints byte-identical stdout and the same exit status from the plain and the incremental checker, and each plant is one the arm can be seen red on.
- After a commit that moves one spec, the incremental run re-grades exactly one spec.
- A timed `--dispatch` on node a after a sequential pass commit, base against built, on one frozen clone.

### brief:gates

The spec-tokens self-test and the driver suite's dispatch arms, run directly. `check-arms` over the driver suite. The lexicon and codebase-map legs the change owes. The merge bar once at the close, without the self-test suites.

### brief:non-goals

- Scoping the check to the dispatching build.
- Any change to a verdict, a refusal line, the summary line or an exit status of the checker or of `--dispatch`.
- The bar's spec-tokens leg, which keeps the plain whole-tree run.
- aLightenedLoop's whole-key cache, except what runs on its miss.
- The unattended Skill.
- A kit version bump by hand.

### task:reuse

aLightenedLoop's input tracer (`arm_input_trace`, `read_open_py`) and `--input-key`'s `derive_input_digest`, per spec instead of per run; the sidecar root `resolve_sidecar_dir` for the cache; the `--spec` mode's per-spec walk. Probe: `reuse_lookup.py` named no seam closer than these.
[/memory/builds/aPiecewiseGrade/prompts/2026-11-15-prompt-TOOL-aPiecewiseGrade-1-1-spec-writer.md]
