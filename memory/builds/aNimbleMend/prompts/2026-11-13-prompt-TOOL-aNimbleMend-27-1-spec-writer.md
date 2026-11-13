**Serves:** journal TOOL-aNimbleMend-27

# gov-spec-writer handoff — TOOL-aNimbleMend-27

<!-- gov:handoff role=gov-spec-writer build=aNimbleMend unit=TOOL-aNimbleMend-27 path=memory/builds/aNimbleMend/prompts/2026-11-13-prompt-TOOL-aNimbleMend-27-1-spec-writer.md role-sha=a3bc1199e30f task-sha=cf1d32f49229 -->

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
- build: aNimbleMend
- unit: TOOL-aNimbleMend-1 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-1.md
- unit: TOOL-aNimbleMend-2 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-2.md
- unit: TOOL-aNimbleMend-3 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-3.md
- unit: TOOL-aNimbleMend-4 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-4.md
- unit: TOOL-aNimbleMend-5 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-5.md
- unit: TOOL-aNimbleMend-6 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-6.md
- unit: TOOL-aNimbleMend-7 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-7.md
- unit: TOOL-aNimbleMend-8 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-8.md
- unit: TOOL-aNimbleMend-9 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-9.md
- unit: TOOL-aNimbleMend-10 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-10.md
- unit: TOOL-aNimbleMend-11 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-11.md
- unit: TOOL-aNimbleMend-12 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-12.md
- unit: TOOL-aNimbleMend-13 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-13.md
- unit: TOOL-aNimbleMend-14 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-14.md
- unit: TOOL-aNimbleMend-15 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-15.md
- unit: TOOL-aNimbleMend-27 · spec memory/builds/aNimbleMend/spec/2026-11-13-spec-TOOL-aNimbleMend-27.md
- brief: memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aNimbleMend/prompts/2026-11-13-prompt-TOOL-aNimbleMend-27-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aNimbleMend`, unit `TOOL-aNimbleMend-27`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> gates = the full bar once at the close with GATE_FULL=1, without self-tests and without the unattended kit gate leg

The owner's prompt is recorded whole in `memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md`; this unit serves the passage above.

### brief:goal

The close ran the full bar once on the prepared landing merge `b61832752`, and three legs went red. Each red is this build's: the same leg is green at `cac14c195`, the default branch's tip before this build merged. This unit repairs the three so the close's bar can read green. Every spec of the build is CLOSED, so the repair is a new unit on top.

### brief:items

1. `shell hygiene (a fork spent on builtin work)` reports five findings. Three are product code: `tools/run-gates/pass-legs.sh` holds two `date-fmt` sites, the two `$(date -u ...)` substitutions under its section 5 to 7, and one `path-subst` site, the `$(dirname "$0")` of its `KITDIR` line, and no registry row declares them. Convert each to the no-fork form the leg names, `printf -v v '%(FMT)T' -1` and `${p%/*}`, keeping the bytes each variable held.
2. The other two kinds of finding are counts that rose in three suites this build added arms to, against rows of `memory/project/spawn-idiom-sites.txt`: `tools/run-gates/run-gates.evidence.test.sh` at `var-pipe` declares 43 and measures 72, `tools/run-gates/run-gates.test.sh` at `var-pipe` declares 141 and measures 156, and `tools/workflows/unattended-build.test.sh` at `printf-subst` declares 66 and measures 74. (PINNED, 2026-11-13) The main loop decided these: the three rows are re-declared at the measured counts with a reason naming this build, as the row of `run-gates.evidence.test.sh` at `printf-subst` already does for an earlier reconcile, and an ask files the drain. Converting the sites would owe a whole run of each of the three suites, about two hours of suite time on node a. The spec states this as a decision made, and the registry file is in the unit's write set.
3. `python reads (a name never bound, an import outside its guard)` reports five guards: `tools/memory-tree/backlog.py` is imported and outside the guard of `memory-recall kit selftest`, `recall floor`, `recall floor arms` and `drift-audit selftest`, and `tools/memory-tree/id_grammar.py` outside the guard of `policy fixtures`. Find the import this build added that put each module into those legs' reach, then either add the module to each leg's guard in `tools/gate-legs.json` or remove the reach, and say which and why. A change to that manifest owes `python tools/run-gates/pass_legs.py --apply` and `python tools/run-gates/pass_legs.py --check` after it.
4. `spawn budget (forks per hot entrypoint)` reports two rows of `memory/project/fork-ceilings.txt`: `memory-hygiene` measured 192 against a ceiling of 191, and `manifest-check` 82 against 76. (PINNED, 2026-11-13) This build added check 31 to `tools/memory-tree/check-memory-hygiene.sh` and added lines to `memory/guides/SESSION-KICKOFF.md`, which the `manifest-check` row's fixture copies; `skills/session-kickoff/manifest-check.sh` itself is unchanged by this build. For each row, find the sites that grew with `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only <id> --sites`, then either remove the added forks or raise the row's ceiling to the measured count with its reason, and say which and why. A fork that grades a manifest line this build added is a cost of that line, so a raise is acceptable there; the added fork in the hygiene gate is removed when a builtin form exists.
5. Write the spec at `memory/builds/aNimbleMend/spec/2026-11-13-spec-TOOL-aNimbleMend-27.md`, Tier-1 if the spec format admits a micro-spec for a mechanical repair and Tier-2 otherwise, status SPECCED, order 16, with `memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-13.md` as the worked example of a repair unit's shape. Units 1 to 15 are CLOSED and frozen, so declare edges only as `external`, and state each correction in this spec itself.
6. The exact red lines are in the failure record `gate-last-failure.txt` of this worktree's git directory, `C:/projects/coding-governance/.git/worktrees/inline-bar-fixes-pass-legs-1a64f7`. Each acceptance criterion names the leg's own command over the tree, which a builder may run because none of the three is a self-test or a gate runner; a criterion that needs a pass-leg run or the bar is the main loop's, and the spec says so in that criterion.
7. Every spec line stating a figure with a unit carries the word PINNED or a commit sha on the same line. The acceptance section cites no path the unit has not built yet. Before returning, stage the spec and clear `python tools/check-spec-tokens.py --spec` over it and `python tools/playbook/positional.py check`; do not run the whole-tree memory hygiene, and do not commit.

### brief:acceptance

- `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'` exits 0, and the same command without the two exclusions prints no finding for the three suites.
- `python tools/run-gates/py_reads.py` prints no line opening `py-reads: RED`.
- `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt .` prints `0 red`.
- `bash tools/run-gates/pass-legs.sh --base <rev>` still writes its run record with a `started` stamp and a run id of the same shape as before the conversion.

### brief:gates

The full bar once more at the close, with `GATE_FULL=1`, without the self-tests and without the unattended kit gate leg.

### brief:non-goals

- Draining the three suites' fork idioms, which an ask files.
- Any change to `skills/session-kickoff/manifest-check.sh`.
- Any kit version, which the lander's mint moves.

### task:reuse

tools/gate-legs.json, tools/run-gates/run-gates.sh, tools/unattended/gate-guard.js, tools/hooks/scratch-guard.js, tools/memory-tree/routed_commits.py, tools/memory-tree/build_records.py, tools/policy/catalogue.toml

### card:route

- build: aNimbleMend
- unit: TOOL-aNimbleMend-1 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-1.md
- unit: TOOL-aNimbleMend-2 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-2.md
- unit: TOOL-aNimbleMend-3 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-3.md
- unit: TOOL-aNimbleMend-4 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-4.md
- unit: TOOL-aNimbleMend-5 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-5.md
- unit: TOOL-aNimbleMend-6 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-6.md
- unit: TOOL-aNimbleMend-7 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-7.md
- unit: TOOL-aNimbleMend-8 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-8.md
- unit: TOOL-aNimbleMend-9 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-9.md
- unit: TOOL-aNimbleMend-10 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-10.md
- unit: TOOL-aNimbleMend-11 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-11.md
- unit: TOOL-aNimbleMend-12 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-12.md
- unit: TOOL-aNimbleMend-13 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-13.md
- unit: TOOL-aNimbleMend-14 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-14.md
- unit: TOOL-aNimbleMend-15 · spec memory/builds/aNimbleMend/spec/2026-11-12-spec-TOOL-aNimbleMend-15.md
- brief: memory/builds/aNimbleMend/prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md
[/memory/builds/aNimbleMend/prompts/2026-11-13-prompt-TOOL-aNimbleMend-27-1-spec-writer.md]
