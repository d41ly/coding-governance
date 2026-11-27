**Serves:** journal TOOL-aPrunedIndex-3
**Caused-by:** TOOL-aPrunedIndex-3

# gov-spec-writer handoff — TOOL-aPrunedIndex-3

<!-- gov:handoff role=gov-spec-writer build=aPrunedIndex unit=TOOL-aPrunedIndex-3 path=memory/builds/aPrunedIndex/prompts/2026-11-25-prompt-TOOL-aPrunedIndex-3-1-spec-writer.md role-sha=91ec0ce505aa task-sha=a0472e8f4d54 -->

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
[memory/builds/aPrunedIndex/prompts/2026-11-25-prompt-TOOL-aPrunedIndex-3-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aPrunedIndex`, unit `TOOL-aPrunedIndex-3`.
Not supplied, optional: `card:route`, `input:code`.

### brief:prompt

> Keep until --gc (Recommended)

The owner's answer in the building session, 2026-11-25, to the question quoted whole under the last heading below.

### brief:goal

Revise TOOL-aPrunedIndex-3: the overlay releases nothing. When a worktree's dirty rows are replaced, the rows only the old
edit held stay until `--gc`'s full sweep. So the window finding 16 named does not open, and everything that exists for it
goes: `check_view_held`, the refusal, its five call sites, the `moved-view` plant, the help sentence, and the edits to
`edge_grammar.py`, `instruction_units.py` and the read verbs. The build's sweep stays bounded to what it drops, and `--gc`
keeps the full sweep. The spec says plainly what it leaves: rows of replaced edits, and any legacy orphan. Correct each
sibling spec's mention of the removed names and of the overlay's release (rev bump and revision-log line), and nothing else
in them.

### brief:items

3. A build's sweep deletes only rows that the trees and the dirty rows of gone worktrees it drops held and nothing else holds; `build_overlay` is unchanged in what it deletes; `--gc` keeps the full sweep. [planned TOOL-aPrunedIndex-3]

Also, in units 1, 3 and 4, section 4's files touched name the acceptance ledger, the journal record under `memory/builds/aPrunedIndex/build/` with one line per criterion, where it is not named yet: hygiene check 23 refuses a CLOSED Tier-2 spec without one.

### brief:acceptance

`check`'s output on one index is byte-equal before and after. A plant pads a fixture's index with dead versions and reds on
each of: a read that scans every version's rows, a probe that walks them, a sweep that walks them. Each is seen red on its
staged break. Wall and CPU before and after are recorded, alternating on one private copy of one index. For item 4, a plant
with a worktree at a commit before the registry collects, and one with the registry deleted from its working tree refuses.

### brief:gates

`tags (the resolver's checks)`, `instruction edits (manifest checks)`, `edges (every declared edge parses, is registered and resolves)`,
`lexicon naming predicates`, `spec tokens (a spec's own names resolve)`, and the full bar at the close.

### brief:non-goals

No ceiling change. No change to what a row holds, how a version is derived, the schema number or the file's name. No
write-ahead log. No held copy of the view in a temporary table. `positional.py` and its `git blame` are left. No automatic
collection in a plain build. No run of `--gc`, VACUUM or a deletion on either live index file.

### input:spec

memory/builds/aPrunedIndex/spec/2026-11-25-spec-TOOL-aPrunedIndex-3.md

### task:reuse

tag_index.py SCHEMA, VIEW_JOIN, remove_unheld_rows, read_live_versions; gov_tag.py --fixture plants; adopt-playbook.sh's plant table
[/memory/builds/aPrunedIndex/prompts/2026-11-25-prompt-TOOL-aPrunedIndex-3-1-spec-writer.md]
