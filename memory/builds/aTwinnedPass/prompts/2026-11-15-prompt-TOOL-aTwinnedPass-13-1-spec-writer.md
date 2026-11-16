**Serves:** journal TOOL-aTwinnedPass-13

# gov-spec-writer handoff — TOOL-aTwinnedPass-13

<!-- gov:handoff role=gov-spec-writer build=aTwinnedPass unit=TOOL-aTwinnedPass-13 path=memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-13-1-spec-writer.md role-sha=a3bc1199e30f task-sha=e5a2a9def81c -->

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
- build: aTwinnedPass
- unit: TOOL-aTwinnedPass-11 · spec memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-11.md
- brief: memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-11-brief.md
[/.claude/orientation-card.md]
[memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-13-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aTwinnedPass`, unit `TOOL-aTwinnedPass-13`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> merge to local main

The owner's word in this session, after the bar went green on `d8bda2e01`. A trial `git merge --no-ff` of `branch/dazzling-jackson-b895c0` onto local main at `a76c6afe7` (aLightenedLoop's landing, equal to `origin/main`) conflicted in four files. The scratch-guard refused the conflict resolution as a product write no buildable unit owns, so the trial was aborted, and the reconcile is this unit, as `TOOL-aLightenedLoop-8` was for that build.

### brief:goal

Merge local main at `a76c6afe7` into `branch/dazzling-jackson-b895c0` and resolve its four conflicts, so that the landing merge of the branch onto local main is conflict-free. Both sides' changes stay as each shipped them.

### brief:items

1. The merge: `git merge --no-ff a76c6afe7` on the branch, committed with both parents and no conflict marker. The trial conflicted in exactly these four files; every other file keeps the merge's own resolution:
   - `memory/project/readme-contract.txt`: keep both rows, `memory/builds/aLightenedLoop/README.md` then `memory/builds/aTwinnedPass/README.md`.
   - `tools/unattended/unattended.test.sh`: `FLOOR_ASSERTIONS` becomes 3348, the common base's 3329 plus main's 6 (`TOOL-aLightenedLoop-3` and `-8`) plus this branch's 13 (`TOOL-aTwinnedPass-3` and `-5`). Both sides' comment blocks stay, and one `MERGED` line names the sum. `FLOOR_SHARD_3` (main's) and `FLOOR_SHARD_4` (this branch's) auto-merge to 451 and 423; verify both against the merged suite rather than trusting the merge.
   - `tools/workflows/unattended-build.test.sh`: `FLOOR_ASSERTIONS` becomes 1043, the base's 950 plus main's 4 (`TOOL-aLightenedLoop-3`) plus this branch's 89 (`TOOL-aTwinnedPass-1`, `-4`, `-11`), comments kept and one `MERGED` line.
   - `tools/workflows/unattended-unit.js`, the `DRIVER_STEPS` ternary: keep this branch's `cfg.passBase !== undefined` branch unchanged, and in the remaining unattended branch take main's `TOOL-aLightenedLoop-3` text ("The main loop declared this unit's write set with ... before it spawned you ... Before you write a path outside that set, declare it with the same command ..."), not the base's "Declare the write set ... before you write anything".
2. The design question the merge raises: main's `TOOL-aLightenedLoop-3` moved the first `--dispatch` from the builder to the main loop (the build harness's `declare` return in `unattended-build.js`), which is what this build's `passBase` branch already assumed. State whether the merged `passBase` sentence and main's `declare` instruction agree, and whether any doc this build wrote (`tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`, `tools/unattended/README.md`, `help/pass-legs.md`) contradicts main's text after the auto-merge. A contradiction is resolved in this unit; none is a finding the spec records as checked.
3. `tools/unattended/unattended.sh` auto-merged: main's `verb_dispatch` hunk is comment-only (the spec-token window), and this branch's condition-1 change (`_c1_own`, `_c1_gen`, `check_generated_output`) sits inside that window. Verify the merged comment's claim that nothing in the window writes the tree still holds with `check_generated_output` in it.
4. Regenerate the generated outputs after the merge (`python tools/run-gates/regen.py --write`, `python tools/memory-tree/gen_build_index.py --write` after `git add`, `python tools/codebase-map/gen_map.py --write`) and commit them in the merge.

### brief:acceptance

- The merge commit has both parents, `a76c6afe7` among them, and `git grep -n '^<<<<<<< '` prints nothing.
- `bash -n` passes on both suites, and `node --check` on `tools/workflows/unattended-unit.js`.
- A trial `git merge --no-ff --no-commit` of the branch onto `a76c6afe7` reports no conflict.
- The four resolutions read as item 1 states, by grep.

### brief:gates

The merge bar once at the close, without the self-test suites, run by the main loop. The pass runs only direct checks.

### brief:non-goals

- Landing or pushing: the main loop makes the landing merge onto local main after the bar, and the owner asked for no push.
- Kit version bumps: `push-main.sh` mints them at the push boundary.
- Any behaviour change on either side beyond what a conflict forces.
- Asks `TOOL-aTwinnedPass-6` to `-10` and `-12`.
- ANY SELF-TEST SUITE OR BAR INSIDE THE PASS, A SLICED SUITE INCLUDED.
- A pass commit without its acceptance ledger: the pass commit carries `memory/builds/aTwinnedPass/build/2026-11-15-build-TOOL-aTwinnedPass-13-1-acceptance-ledger.md`.
- An edit after the commit that sets the spec CLOSED: the status flip is the last change of the pass.

### task:reuse

lib-unattended.sh resolve_generated_indexes, check_gen_region_only, covers; unattended.sh check_commit_message's generated exemption; push-main.sh run_regen and regen.py --write; unattended-unit.js prebuild and passLegs key shape; lib-attribute.sh add_scratch_worktree.

### card:route

- build: aTwinnedPass
- unit: TOOL-aTwinnedPass-11 · spec memory/builds/aTwinnedPass/spec/2026-11-15-spec-TOOL-aTwinnedPass-11.md
- brief: memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-11-brief.md
[/memory/builds/aTwinnedPass/prompts/2026-11-15-prompt-TOOL-aTwinnedPass-13-1-spec-writer.md]
