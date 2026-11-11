**Serves:** journal PLAY-dOrderedCharter-83

# gov-spec-writer handoff — PLAY-dOrderedCharter-83

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-83 path=memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-83-1-spec-writer.md role-sha=90b89c43f238 task-sha=00f9a4f136bc -->

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
- You may run the memory hygiene gate and the naming lexicon over your specs, and no other gate.
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
- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-82 · spec memory/builds/dOrderedCharter/spec/2026-11-11-spec-PLAY-dOrderedCharter-82.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-83-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-83`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:goal

Write spec PLAY-dOrderedCharter-83, the Tier-2 spec for one unit at order 45 that makes the `--no-ff` merge of `47ed57fab`
into `branch/unattended-dorderedcharter-725f52`, resolving every conflict by its kind. Model it on main's precedent,
`TOOL-aSmoothedDispatch-22` (read it with `git show origin/main:memory/builds/aSmoothedDispatch/spec/2026-11-11-spec-TOOL-aSmoothedDispatch-22.md`).

### brief:items

1. **Where you write.** Write the new spec only at
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/fold83/2026-11-11-spec-PLAY-dOrderedCharter-83.md`;
   write nothing under the repository. Follow `memory/TEMPLATE-SPEC.md`; carry the `**Derived:**` binding line spec 82
   carries; status line `DEFERRED · rev-1 · 2026-11-11 · node a · Tier-2 · base <HEAD short sha> · streams playbook · order 45
   · advances PLAY-dOrderedCharter-38`.
2. **The conflict set.** Take it with `git merge-tree --write-tree --name-only HEAD 47ed57fab` (merge base `8bec4cefd`): fifty
   files, every one a content conflict, most one region. State the command and the tree it prints, and tell the builder to
   re-take it at the merge and record any difference.
3. **Dispositions by kind.** Read each region on both sides and the commits that moved it; give each file one disposition:
   - **Kit version markers** (`<!-- gov:kit <kit>@<v> -->` beside this build's level envelope line, in the unattended,
     memory-tree, roles and workflows templates): keep this branch's envelope line and main's higher version. The lander's
     mint re-bumps after landing; say whether any kit this branch touched owes a bump past main's.
   - **Rendered or generated outputs** (`AGENTS.md`, `.claude/agents/*.md`, `.claude/skills/*/SKILL.md`, `memory/guides/*.md`,
     `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `help/roles.md` if generated, `memory/backlog/PLAY.md`,
     `memory/map/generated/*`, `.governance/policy.json`'s `catalogue_blob`): re-rendered by their own generators after the
     sources are resolved, never hand-merged. Name each generator and the order they run in. Check whether `AGENTS.md` and
     `.governance/policy.json` are owner-only for an agent's commit under the policy guard, and what the builder does if so.
   - **Product sources with real two-sided edits** — `coding-governance-agents.template.md` (main's v4.5 marker and its
     retired memory-tree lookup line, against this branch's restructured charter), `tools/check-playbook-parity.sh` (main
     moved the lens bound to `check-verifier-fanout.js`, this branch moved the verify-total source to `practices.toml`),
     `tools/check-spec-tokens.py` (main's `--spec` mode against this branch's `check_live_header`), `tools/roles/handoff.py`,
     `tools/roles/render_agents.py` (two regions: docstring and main's arm 19 beside this branch's shape and ranked arms),
     `tools/workflows/tier2-review.js` and its template (two regions each), `tools/workflows/REVIEW-PROTOCOL.template.md` (two),
     `tools/workflows/kit.toml` (this branch's drive rows beside main's `lf_pin`), `.lexicon.conf` (the verb pin, re-measured
     over the merged tree): keep both sides' intent, and say for each what the merged lines are.
   - **Suite floors** (`tools/check-spec-tokens.test.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`,
     `tools/lib/resolve-python.test.sh`): keep both sides' arms and RAISED lines, add one MERGED line naming this unit, the
     floor recounted by reading.
   - **Records** (`memory/builds/dIndexedDesign/README.md`, `memory/builds/dShippedRelease/README.md` and its spec 78, the two
     `memory/gotchas/*.md`): additive, per `[reconcile]`; a generated region is re-rendered.
4. **After the merge.** The kickoff manifest re-stamp if a watched file moved; the build index, LIVE, the ledger and the
   codebase map re-rendered; the spec-token check over the merged tree. Main's commits may have added legs or checks that
   now grade this branch's files: name the ones the merge must leave green, and which legs the main loop runs afterwards.
5. Criteria observe: no conflict marker in the merged tree, two parents, each product file's merged lines present, the
   generators writing nothing on a second run. The spec-token check grades a live spec's acceptance bullets word by word: no
   acceptance command whose words include an untracked path, no `path#symbol`, no suite as the observation, each backticked
   span on one line, every tripped leg on the gates line. Every new fact pinned.

### brief:acceptance

- Spec 83 builds as written over HEAD, every conflicted file has a disposition, and no fork is left open.

### brief:gates

None run on the repository: this is a scratch write.

### brief:non-goals

- No code, no merge. No edit outside the scratch copy. No change past what the reconcile needs.

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-82 · spec memory/builds/dOrderedCharter/spec/2026-11-11-spec-PLAY-dOrderedCharter-82.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-build-brief.md
[/memory/builds/dOrderedCharter/prompts/2026-11-11-prompt-PLAY-dOrderedCharter-83-1-spec-writer.md]
