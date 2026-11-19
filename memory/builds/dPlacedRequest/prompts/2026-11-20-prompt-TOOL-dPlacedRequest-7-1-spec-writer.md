**Serves:** journal TOOL-dPlacedRequest-7

# gov-spec-writer handoff — TOOL-dPlacedRequest-7

<!-- gov:handoff role=gov-spec-writer build=dPlacedRequest unit=TOOL-dPlacedRequest-7 path=memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-7-1-spec-writer.md role-sha=91ec0ce505aa task-sha=fe25252f1a44 -->

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
- build: dPlacedRequest
- unit: TOOL-dPlacedRequest-7 · spec memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md
- brief: memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-7-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dPlacedRequest`, unit `TOOL-dPlacedRequest-7`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dPlacedRequest

### brief:goal

TOOL-dPlacedRequest-7's builder returned a DIVERGENCE (run `wf_060498d5-d58`) and committed nothing. At rev-7 the
command actors fail `tools/loop/loop_lib.py#ACTOR_FORM`; the probe's method has no home, grammar or writer and the
`design` verb no flags; a `claimed` judgment has no place in the closed `Verdict` set; AC6's visual kind is outside
S4's closed `--kind`; and `pin` cannot commit an entry-time trigger's record, which lives outside the worktree. Revise
the spec to the main loop's rulings, each a fork in §8 marked
`RESOLVED (agent, 2026-11-20, delegated): <option>, rung 3; <reason>. widens: none · relaxes: none`.

### brief:items

1. F-actor: the §4 table spells the command actors `command:probe.trigger`, `command:probe.pin`, `command:probe.judge` and `command:probe.return`, as the review program spells `command:review.trigger` and `command:review.pin` in `tools/loop/loop.toml`. Reason: the loop's one actor grammar stands, and the sibling program is the precedent.
2. F-method: the method lives in the `probe` record itself, in a section of its own (one record, one fact), one entry per line holding the command and its predicted `<exit>:<hash>`, with the optional marks `judge claimed` and `visual` spelled as trailing ` · `-separated fields on that entry. `probe.py design` is the method's one writer: it appends one entry per call, takes the record's address and the entry's command, prediction and marks as flags you name from the tree's flag vocabulary, and refuses once the record is pinned. Amend S5 (what `run` reads), S6 (the method section in the `probe` record's shape) and §4 Inventory (the `design` verb's flags), and add one acceptance criterion observing `design` append an entry and refuse after `pin`. Reason: the method is part of the record the probe pins, so it is written before the pin and frozen by it.
3. F-judged: S6 gains a field `Judged: computed|claimed` beside `Verdict`, and `Verdict`'s closed set stays as it is; a `claimed` judgment, or an `unrunnable` verdict, routes to an owner item as S5 already says. Reason: the verdict and the way it was reached are two facts.
4. F-visual: "visual" is the method entry's mark (item 2), not a `--kind`; S4's closed `--kind` stays, and AC6's plant pins a verification whose method carries a `visual` entry.
5. F-entry: for an entry-time trigger, `pin` writes `<key>.probe.md` into the git-common-dir `requests/` store and commits nothing, the store being outside the tree; S4's "commits it alone before any command runs" becomes "records it, committed where the record lives in the tree, before any command runs", and AC4's red condition reads "a command runs before the losing outcome is recorded".
6. Stale citations: S7 cites `tools/loop/request.py#derive_request_content_key`; S10's reader line names `tools/playbook/core.py#run_meta_check` and the `core-pending.txt` row it reads; the new leg's argv is `python {prefix}/loop/probe.py --selftest`, as `loop request fixtures` runs `request.py --selftest`, printing the count line the `testsuite counts` leg reads; and §4 says the `[[computed-witness]] probe-rerun` row in `tools/loop/loop.toml` switches its `serves` to `item.probe.run`.
7. §4 Files touched lists only paths (no command words), and gains `tools/govkit/registry.toml` and `tools/run-gates/selftest-budgets.txt` for the new leg, as `loop request fixtures` is registered.

### brief:acceptance

Spec 7 at rev-8 carries the five resolved forks, S4 to S7, S10, §4 and AC4/AC6 amended, the new `design` criterion,
`path#symbol` citations, and one §9 line naming this brief and the divergence; `check-memory-hygiene.sh --only 12,25
--spec` and the spec-token checker over it report nothing.

### brief:gates

The memory hygiene gate (`--only 12,25 --spec`), the spec-token checker and the naming lexicon; no other.

### brief:non-goals

No product code, no commit, no index render, no status flip (it stays INPROGRESS), no spec other than
TOOL-dPlacedRequest-7. Pin every figure you write with DERIVED or PINNED, never let a section sign or a section
number stand before a unit word, never write a bare file-stem section reference, and never quote a check's hit
literally in prose.

### task:reuse

each spec's §10 names its seam (the `write_claim`/`read_claims` CAS ref writer in tools/unattended/unattended.sh becomes the governance-ref factory); recall probe below.

### card:route

- build: dPlacedRequest
- unit: TOOL-dPlacedRequest-7 · spec memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-7.md
- brief: memory/builds/dPlacedRequest/prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md
[/memory/builds/dPlacedRequest/prompts/2026-11-20-prompt-TOOL-dPlacedRequest-7-1-spec-writer.md]
