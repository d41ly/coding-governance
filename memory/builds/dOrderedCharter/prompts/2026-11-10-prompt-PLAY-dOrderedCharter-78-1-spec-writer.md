**Serves:** journal PLAY-dOrderedCharter-78

# gov-spec-writer handoff — PLAY-dOrderedCharter-78

<!-- gov:handoff role=gov-spec-writer build=dOrderedCharter unit=PLAY-dOrderedCharter-78 path=memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-78-1-spec-writer.md role-sha=90b89c43f238 task-sha=b9ae49ba74f4 -->

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
- unit: PLAY-dOrderedCharter-77 · spec memory/builds/dOrderedCharter/spec/2026-11-10-spec-PLAY-dOrderedCharter-77.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-78-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dOrderedCharter`, unit `PLAY-dOrderedCharter-78`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:goal

Write spec 78, a Tier-2 unit whose pass leaves the govkit acceptance matrix and the harness-arms leg green over the tree, and an
adopter's tags check green in a scratch install, by the three picks below.

### brief:items

1. **Where you write.** `memory/builds/dOrderedCharter/spec/2026-11-10-spec-PLAY-dOrderedCharter-78.md`; no builder is running. Header:
   `**Status:** DEFERRED · rev-1 · 2026-11-10 · node a · Tier-2 · base <HEAD's short sha> · streams playbook · order 37 · advances
   PLAY-dOrderedCharter-38`, plus the `**Derived:**` binding line every promoted unit of this build carries. Edges `none`, its
   dependencies on CLOSED units named in prose.
2. **The acceptance matrix.** A scratch install of the playbook kits cannot render the charter, because readers this build added look up
   the memory-tree and policy kits: `tools/govkit/govkit.py` or the readers it reaches print `looked in ... install.json, ... memory-tree`
   and `... policy` in the matrix's log. The pick: the playbook entry (`tools/govkit/entries/playbook.kit.toml`, and the playbook-render
   entry if it is the reader's owner) declares the kits it reads in `requires`, and `tools/govkit/matrix.py`'s scratch install carries
   them. Confirm which entry owns each lookup at HEAD before naming it.
3. **An adopter's tags check.** In a scratch install, `python tools/playbook/gov_tag.py check` reds where `tools/playbook/namespaces.toml`
   names `dOrderedCharter` as each namespace's owner, which the adopter's chain registry does not hold. The pick: the purpose arm skips
   an owner the target's own chain registry does not hold, printing an unarmed line, rather than each row being edited. Find the arm in
   `tools/playbook/tag_index.py` or its caller, state what it no longer checks, and give it a plant. Also say whether the family-id
   native's "resolves nothing" line in the same install is a red, and fix it by the same rule if it is.
4. **The A25r arm.** `tools/check-template-size.test.sh`'s arm for `tools/check-template-size.sh`'s check 8 branch 1 asserts the remedy
   sentence without the leading `).` that `python tools/memory-tree/check-arms.py --emit-pin` prints as the branch's signature. Assert the
   whole signature, and remove the pin row this build added for it to `memory/project/unarmed-branches.txt` in the same pass.
5. **The spec-token check grades a live spec's acceptance bullets word by word**: no acceptance command whose words include a path that
   is not a tracked file, never a test suite or the self-test runner as the observation, each backticked span on one line, every leg
   the files touched trip on the leg line. Cite code as `path#symbol` or a blob-pinned line, never a bare `path:line`.
6. Every section 8 fork carries a resolution mark; every new fact is pinned, keyed or marked DERIVED on its own line, outside backticks;
   every function name it mints passes `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### brief:acceptance

- Spec 78 builds as written over HEAD and passes the pinned-facts check, memory hygiene's spec-shape check and the positional check.

### brief:gates

Run the pinned-facts check, memory hygiene's spec-shape check and the positional check over the spec, and report each.

### brief:non-goals

- No code. No edit to any other spec or file.

### task:reuse

each spec's section 10 names its seam; recall terms below.

### card:route

- build: dOrderedCharter
- unit: PLAY-dOrderedCharter-77 · spec memory/builds/dOrderedCharter/spec/2026-11-10-spec-PLAY-dOrderedCharter-77.md
- brief: memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-77-build-brief.md
[/memory/builds/dOrderedCharter/prompts/2026-11-10-prompt-PLAY-dOrderedCharter-78-1-spec-writer.md]
