**Serves:** log TOOL-dTotalRecall-45

# gov-spec-writer handoff — TOOL-dTotalRecall-45

<!-- gov:handoff role=gov-spec-writer build=dTotalRecall unit=TOOL-dTotalRecall-45 path=memory/builds/dTotalRecall/prompts/2026-11-22-prompt-TOOL-dTotalRecall-45-reground-2-spec-writer.md role-sha=91ec0ce505aa task-sha=e6265f9e790a -->

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
- build: dTotalRecall
- unit: TOOL-dTotalRecall-4 · spec memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-4.md
- brief: memory/builds/dTotalRecall/README.md
[/.claude/orientation-card.md]
[memory/builds/dTotalRecall/prompts/2026-11-22-prompt-TOOL-dTotalRecall-45-reground-2-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dTotalRecall`, unit `TOOL-dTotalRecall-45`.
Not supplied, optional: `input:code`.

### brief:prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The spec run wrote every spec DEFERRED at base `462d20f3`; 4140
commits (DERIVED, `git log --oneline 462d20f3..8b8b1374c | wc -l`) have landed since, the three parent builds
dDeclaredLoop, dWitnessedBar and dPlacedRequest among them, so each spec is re-grounded before its dispatch.

### brief:goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem,
so a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### brief:items

1. Read the spec whole against the code at HEAD and settle every claim the landed code has moved: every path,
   symbol, line citation, section name, count, population and edge, and every parent spec it leans on (the
   PLAY-dOrderedCharter, TOOL-dWitnessedBar, TOOL-dPlacedRequest, TOOL-dSafePassage and TOOL-dDeclaredLoop ids it
   cites): read what each parent actually landed, not what its spec planned. Re-derive each PINNED count with the
   command the spec states and re-pin it with today's date. A population the spec enumerates is re-derived, every
   new member listed in Files touched with the legs its guard names on the gates section's leg line. Cite moved
   code-file lines as `path#symbol` or blob-pinned at a commit HEAD holds, never a bare `path:line`; leave a
   carried clause token (`**Carries:**` lines) byte-identical.
   What is built so far, CLOSED: TOOL-dTotalRecall-1 (the record-kind registry and `record_kinds.py`, leg `record-kinds`), -13
   (the `extract_code` block), -18 (`tree_lib.py#resolve_kind`, `journal` renamed `log`), -16 (the `purpose` column), -25 (the
   `stream-plan` kind), -5 (`202a354a4`, fixed up in `e556566b4` and `fc5c593c6`: the slug grammar derived once in
   `tools/memory-tree/id_grammar.py#derive_slug_grammar`, bound per root into `tree_lib.py#build_id_token_re`, printed by the
   hygiene script, a `{{SLUG_CLASS}}` token for JavaScript renders, every refused fixture slug re-spelled), -54 (`74af3faa4`:
   `id_grammar.py#parse_id_parts(ident, root, *, alt=None)` and `#load_sibling`, its arm in `tools/memory-recall/selftest.py`)
   and -38 (`2f59e5acb`: every split id reader parses through `parse_id_parts`, `backlog.ANY_FAMILY`, the split census in
   `id_grammar.py#scan_readers` and its flip-probe check). TOOL-dTotalRecall-4 (order 8, the last of that step) builds now
   from its rev-6 spec: read its spec where this spec consumes from it. `id_grammar.py` still has no selftest of its own
   and no leg. TOOL-dTotalRecall-8 and -37 are DEFERRED to owner ask TOOL-dTotalRecall-109 (no code record; policy reads go
   through `tree_lib.py#read_policy_value`). This spec was re-grounded once before units 5, 54 and 38 were built: re-check
   every claim it makes about them against their code at HEAD, not their specs. This unit is build order 9; its siblings
   TOOL-dTotalRecall-40, -44, -45, -46, -6, -63 and -64 are being re-checked by their own writers now, so edit no
   order-9 spec but yours, and name in your return any edge you need from a sibling. Units 63 and 64 amend spec 46 in
   their own build passes, never in a re-ground.
2. Trace behaviour, not only text: (a) run or read each acceptance criterion's command for its real exit codes and
   output; (b) grep every caller of a function the unit changes and every suite that copies the files it touches;
   (c) check each new rule against the fallback its reader takes on an invalid or absent file; (d) where the spec
   names a seam (a factory, a ledger, a leg row, a class row), confirm the seam exists at HEAD with the shape the
   spec uses, and re-point the spec where a parent landed it differently.
3. Settle every unwaived spec-token hit that names this spec (`python
   tools/check-spec-tokens.py --spec <path>` lists them), each by naming the tripped leg on the gates section's leg
   line or by correcting Files touched.
4. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return. A fork whose only survivor needs a new
   external dependency or a governance-carrier change is parked, not decided: name it in your return.
5. A `[[ledger]]` home spelled under `tools/<kit>/` reds `install-prefix (shipped surface)`; keep every home under
   `memory/project/`. A spec over its ceiling of 49152 B (PINNED 2026-11-20 by the spec size check) is tightened
   in prose you touch, never by dropping a criterion. Name every new function the spec introduces with a verb from
   `.lexicon.conf`'s VERBS table, nested helpers included. A new leg's `ceiling` clears its evidenced maximum by max(120 s, 1.0x) (PINNED 2026-11-22)
   (`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-1-deviation-15.md`), and a new surface
   class needs its `[[class]]` row in `tools/govkit/usage.toml`; every number the spec states carries an id, a
   path:line, PINNED or DERIVED on its line (`python tools/playbook/writing_practice.py check pinned-facts`).

6. A `consumes-from` edge to an unbuilt sibling needs that sibling's matching `hands-off`, or hygiene check 12 refuses both. Where the sibling's spec (DEFERRED, not CLOSED) lacks it, add that one bullet to the sibling's edges as a rev bump with a revision-log line naming this brief; that sibling spec joins your write grant for that bullet alone. A CLOSED sibling stays frozen: state the dependency in Scope and name it in your return.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-45` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### brief:acceptance

Both commands exit 0 for the spec; it carries the next rev and one revision-log line naming this brief.

### brief:gates

memory hygiene · spec tokens (a spec's own names resolve)

### brief:non-goals

No spec outside TOOL-dTotalRecall-45. No product code. No change to Goal or Scope intent beyond what the tree forces.

### input:spec

memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-45.md

### task:reuse

each unit's §10 names its seam; build-level seams are `tools/memory-tree/` (tree_lib, gen_build_index, gov_record), `tools/lib/` and `tools/govkit/` per the reuse-scout records under `build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-{a,b,c}.md`.

### card:route

- build: dTotalRecall
- unit: TOOL-dTotalRecall-4 · spec memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-4.md
- brief: memory/builds/dTotalRecall/README.md
[/memory/builds/dTotalRecall/prompts/2026-11-22-prompt-TOOL-dTotalRecall-45-reground-2-spec-writer.md]
