# The systems round: tags, code annotations, instruction writing, role workflow shapes and memory structure

**Serves:** research PLAY-dClosedLoop-1

The owner opened five systems that cut across every layer, after all eight layers were designed,
reviewed and folded. This record holds the round: the owner's words, what the design already settles for
each system, the research and its method, and, once the runs return, what they agree on and the design.

## [words] The owner's words, 2026-10-16

> More systems need to be included for design/review:
>
> * Tag system. How will tagging work, what will make it efficient across all layers?
> * Code annotations/commentary - what is the design that ties in with the instruction layer to make code
>   commentary as efficient orientation point as possible?
> * Instruction layer writing system - what will make it more efficient than the current prose? Will there
>   be an instruction templating system, that will be enforced across the entire design?
> * Role workflow shapes - what are the most efficient workflow shapes to drive work by role?
> * Memory structure - how to make it more efficient compared to the current implementation? Reduce
>   unnecessary load on the read path? What does memory system currently lack?

## [scope] Each system, and what the design already holds

| System | What the design already settles | Handoff | Dispatches |
|---|---|---|---|
| Tags | P11 names sections, checklist items and layers by tags, never by numbers or `§`. Section tags take dOrderedCharter's grammar and resolver; items are `<step>.<name>`; roles are `role.<name>`; stages key the loop kit; instruction units are tagged by scope; code carries `gov:feature` and `gov:note`. `layer-instruction` `[uncovered]`: only roles join to rule tags, and checklist items are numbered | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-22-researcher.md` | 73, 74 |
| Code annotations | `layer-memory` `[annotations]`: the `gov:note` head line, `gov:feature` anchors checked both ways with reuse entries, a generated index queried by tag, and a resolve gate whose three planted reds are owed; the read hook is a pack of memory's optional components (KN-1) | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-23-researcher.md` | 75, 76 |
| Instruction writing | `layer-instruction`: levels 0 to 7, units registered and enveloped, render refusals per role and item, P11's six statement types and P12's structured specs. Its `[uncovered]`: protocols, templates and guides are still hand-written whole documents, each read whole | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-24-researcher.md` | 77, 78 |
| Role workflow shapes | v2 `[owed]` and gap-roles-18: the roles layer's mechanical shape, owed since round four, with aScoutedSeam's evidence. The agent set, the effort and the checklist are declared as data today; the orientation template and the merge are declared nowhere | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-25-researcher.md` | 79, 80 |
| Memory structure | `layer-memory` `[design]` and `layer-library` `[design]`: the trail and the library, the record-kind registry, one door, generated views, and optional components with named fallbacks; EX-2's homes | `prompts/2026-10-16-prompt-PLAY-dClosedLoop-1-26-researcher.md` | 81, 82 |

## [research] Dispatched, 2026-10-16

- **The method** is the expansion round's: one researcher per system, each run twice from the same
  handoff at the researcher's declared effort, medium, and the design based on what the two runs agree
  on.
- **The handoffs** share the context, the handed facts, the way of working and the return shape, and
  differ only in each system's part. The script below assembles them, and `handoff.py render` renders
  each; `handoff.py check` passes all five.
- **The order.** Two waves of five: the five A runs, then the five B runs once the first wave returns, so
  no more than five agents run at once. The owner opened the round while dispatch 62 ran, so the waves
  run between dispatches 62 and 63, and the review queue resumes after the second wave.
- **The returns** are filed verbatim as `build/2026-10-16-build-PLAY-dClosedLoop-1-research-<system>-<run>.md`.

### [instrument] The script that assembles the questions

```python
"""Assemble each system's research question from the shared blocks and its own part, for the systems round
the owner opened on 2026-10-16.

Usage: python assemble.py <dir>
Writes <dir>/question-<system>.md for the five systems. The context, the handed facts, the way of working
and the return shape are identical in all five, so the two runs of one question and the five questions
differ only where their parts do.
"""
import pathlib
import sys

d = pathlib.Path(sys.argv[1])
head = (d / "head-expansions.md").read_text(encoding="utf-8").rstrip("\n") + "\n" + \
    (d / "head-more.md").read_text(encoding="utf-8")
tail = (d / "shared-tail.md").read_text(encoding="utf-8")
SYSTEMS = {"tags": "the tag system", "annotations": "code annotations and commentary",
           "instruction-writing": "the instruction writing system", "role-shapes": "role workflow shapes",
           "memory-structure": "memory structure"}
CONTEXT = (
    "**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development.\n"
    "The owner reviews the design layer by layer. All eight layers, the five core and the three expansions,\n"
    "are designed, reviewed and folded. The owner now opens five systems that cut across every layer, in\n"
    "these words:\n\n"
    "> More systems need to be included for design/review:\n>\n"
    "> * Tag system. How will tagging work, what will make it efficient across all layers?\n"
    "> * Code annotations/commentary - what is the design that ties in with the instruction layer to make code\n"
    ">   commentary as efficient orientation point as possible?\n"
    "> * Instruction layer writing system - what will make it more efficient than the current prose? Will there\n"
    ">   be an instruction templating system, that will be enforced across the entire design?\n"
    "> * Role workflow shapes - what are the most efficient workflow shapes to drive work by role?\n"
    "> * Memory structure - how to make it more efficient compared to the current implementation? Reduce\n"
    ">   unnecessary load on the read path? What does memory system currently lack?\n\n"
    "Yours is **{name}**. Design it to fit the architecture handed below, across all eight layers. Measure\n"
    "what today's product does, say what the current design already settles and what it lacks, and say what\n"
    "makes your pick efficient, in numbers a check could hold it to. The other four systems are researched at\n"
    "the same time, so name what yours needs from them and what it gives them.\n")
for key, name in SYSTEMS.items():
    part = (d / f"part-{key}.md").read_text(encoding="utf-8")
    text = "\n".join([CONTEXT.format(name=name), head, part, tail]).rstrip("\n") + "\n"
    if "\r" in text:
        sys.exit("a carriage return reached the question")
    (d / f"question-{key}.md").write_text(text, encoding="utf-8", newline="\n")
    print(f"question-{key}.md: {len(text.split())} words, {len(text.encode('utf-8'))} bytes")
```

## [agreement] What each system's two runs agree on

Each table sets a system's run A beside its run B, question by question. "Both runs" holds only what each
run found on its own, with each run's line cited. The returns are filed verbatim as
`research-<system>-a.md` and `-b.md` in `build/`.

### [agree-tags] Tags, dispatches 73 and 74

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| Grammar | one namespaced grammar, `<ns>.<seg>`, with a section tag scoped to its document and ids keeping memory's own grammar (`research-tags-a.md:13`, `research-tags-b.md:13`) | B caps a tag at 64 B | both |
| Where a tag is declared | once, in place, at the site its owning layer already writes, with no authored registry (`research-tags-a.md:15`, `research-tags-b.md:13`) | A rejects a central `tags.toml` on one fact in one place; B on 956 restated rows | both |
| The index | derived by extractors each namespace's owner registers, cached by tree id, never committed and never loaded whole (`research-tags-a.md:15`, `research-tags-b.md:13`) | A: 0.90 s over all of `memory/`; B: 0.18 s for 735 rows from seven sources | both, as one index with memory's (`[cross]`) |
| Resolution | one call returns the smallest slice, a 2.2 KB median section where today an agent reads a whole file in three calls (`research-tags-a.md:19`, `research-tags-b.md:15`) | A measures a 35.9 KB median file; B 25 KB | both |
| Renames and retirement | a retired tag keeps a forward pointer and is never reused (`research-tags-a.md:145`, `research-tags-b.md:141`) | A appends an alias row beside the source; B derives the redirect from the source's write-path change record | B's derivation, with A's never-reuse |
| Rejected: one authored registry | it restates what every declaring site already holds (`research-tags-a.md:104`, `research-tags-b.md:106`) | — | rejected |
| Rejected: grep at query time | a line grep cannot tell a definition from a citation, so it needs the per-source parsers an index has anyway (`research-tags-a.md:106`, `research-tags-b.md:107`) | — | rejected |
| Populations with no tag | gate legs are free text: 139 of 140 fail the tag shape (`research-tags-a.md:167`, `research-tags-b.md:198`) | A adds `section`, `doc`, `feature`, `bug-class`, `leg`, `check`, `ext`, `command` and `pack`; B adds `section`, `unit`, `field`, `leg`, `point`, `hook`, `command`, `feature` and `class` | the union, in `[design-tags]` |
| Positional references | they stay a defect the grammar replaces, held while Convergence migrates them (`research-tags-a.md:56`, `research-tags-b.md:196`) | A: their defect is overload, not reordering, so numbers become alias rows; B: they have no gap and no ratchet, so a shrink-only ratchet | both |
| Step or stage | one namespace, `step` (`research-tags-a.md:224`, `research-tags-b.md:210`) | — | `step` |
| Index location | an untracked cache keyed by tree id (`research-tags-a.md:222`, `research-tags-b.md:206`) | — | the cache |
| The join engine | `compute_coverage` is the one both-ways join today, and it sits in an optional component (`research-tags-a.md:159`, `research-tags-b.md:31`) | A extracts it to `tools/lib` as the join factory | A's extraction |

### [agree-annotations] Code annotations, dispatches 75 and 76

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| The head line | one inline `gov:note` head line per annotated block, holding a definition and pointers (`research-annotations-a.md:15`, `research-annotations-b.md:13`) | A caps a block at 8 lines (`research-annotations-a.md:143`); B at 12, on touched blocks (`research-annotations-b.md:145`) | 12 lines, on touched blocks |
| Its place in the instruction layer | not an instruction unit and no level of its own; a directive stays in the unit the line points at (`research-annotations-a.md:15`, `research-annotations-b.md:13`) | A calls it level-7 evidence; B calls it levelless | levelless pointers |
| History and measurements | they move out of comments into the record the line's `refs=` names (`research-annotations-a.md:15`, `research-annotations-b.md:13`) | — | both |
| Delivery | a work-order slot of at most 2 KB and a query by tag, with no read hook (`research-annotations-a.md:17`, `research-annotations-b.md:15`) | — | both, superseded by AN-2's read hook under `pushed-at-read` (revised 2026-10-17, the audit's M8) |
| Why no read hook | the Read tool carries a small share of the calls that read code: 5.4% (`research-annotations-a.md:17`) and 3.1% (`research-annotations-b.md:15`) | the two windows differ | fork AN-2, which kept `pushed-at-read` and redefined it for shell reads; this row's retirement is superseded (revised 2026-10-17, the audit's M8) |
| Comment volume | about 41% of code bytes are comments (`research-annotations-a.md:47`, `research-annotations-b.md:23`) | A: 51.6% of comment lines sit in blocks of 8 or more; B: 22.9% of comment bytes narrate in long blocks | both |
| Pointers followed | agents rarely follow a comment's pointer: 7.6% within 3 calls (`research-annotations-a.md:76`) and 5.0% within 5 reads (`research-annotations-b.md:48`) | — | the comment carries the orientation itself |
| Dangling citations | a comment cites a gotcha path that never existed, and no check sees it (`research-annotations-a.md:70`, `research-annotations-b.md:27`) | A also counts 2 real dangling ids; B files the same ids among fixtures and foreign families | re-measured at arming |
| Where tags are found | — | A: a map-built index beside a core marker scan (`research-annotations-a.md:113`); B: an on-demand marker query in core, with no index (`research-annotations-b.md:184`) | fork AN-1 |

### [agree-instruction-writing] Instruction writing, dispatches 77 and 78

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| The source | every loaded instruction is a typed unit, one TOML row in its kit's manifest, and every instruction document is a render (`research-instruction-writing-a.md:13`, `research-instruction-writing-b.md:13`) | — | both |
| Templates | one template per document kind, holding slot selectors and no prose (`research-instruction-writing-a.md:13`, `research-instruction-writing-b.md:13`) | B adds the harness prompt module as a kind | both, with B's kind |
| Enforcement | a gate refuses any instruction file whose bytes differ from its render (`research-instruction-writing-a.md:13`, `research-instruction-writing-b.md:13`) | B arms the refusal at dOrderedCharter with a shrink-only legacy list (`research-instruction-writing-b.md:222`); A has each chain build migrate its own step's guides | fork IW-1 |
| Unrendered load points | instruction text loads that no render produces: A's five hand-written load-path documents, 60 KB (`research-instruction-writing-a.md:24`); B's harness prompt literals, 38 KB (`research-instruction-writing-b.md:28`) | each found a different population | both populations |
| Duplication | the charter blocks load twice per spawn, in 48 handoffs (`research-instruction-writing-a.md:64`, `research-instruction-writing-b.md:53`) | — | one carry per spawn |
| Rejected: documents stay the source | a unit several load points need must be copied, and a section holds many units (`research-instruction-writing-a.md:95`, `research-instruction-writing-b.md:103`) | — | rejected |
| Rejected: fully generated text | it loses as the whole system and survives as a unit's `source` field (`research-instruction-writing-a.md:96`, `research-instruction-writing-b.md:103`) | — | both |
| Source format | TOML rows (`research-instruction-writing-a.md:230`, `research-instruction-writing-b.md:221`) | — | TOML |

### [agree-role-shapes] Role workflow shapes, dispatches 79 and 80

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| The declaration | each role item names a shape declared as data, of a registered harness kind (`research-role-shapes-a.md:15`, `research-role-shapes-b.md:16`) | A extends `workflows.toml`, B adds `shapes.toml`; A's kinds are single, per-unit, scout-pass and find-verify-synth, B's single, scout-judge, panel and twin | a per-item registry, `[design-role-shapes]` |
| Effort | it stays in `policy.toml` (`research-role-shapes-a.md:15`, `research-role-shapes-b.md:150`) | — | both |
| Enforcement today | the spawn guard admits an undeclared shape: a builder reviewing at low effort exits 0 (`research-role-shapes-a.md:93`, `research-role-shapes-b.md:62`) | — | the guard binds the call to its shape |
| Twins | on design records only (`research-role-shapes-a.md:15`, `research-role-shapes-b.md:20`) | — | fork RS-1 |
| Twin merge | grouping by cited address finds the true pairs and many false ones, so a synthesizer judges them (`research-role-shapes-a.md:103`, `research-role-shapes-b.md:118`) | A: 40% of cross-defect pairs would merge wrongly; B: 92.7% of shared-address pairs are different defects | a synthesizer over address-grouped candidates |
| Ranking | verified results per 100k out-tokens, with recall checked against a twin union (`research-role-shapes-a.md:15`, `research-role-shapes-b.md:22`) | B ranks recall first, within 2 sd, then grade-weighted yield | B's order |
| The reuse scout | one M1c scout with the house index handed first, never twinned (`research-role-shapes-a.md:140`, `research-role-shapes-b.md:161`) | — | both |
| Yield by review shape | spec audits at medium yield the most, 21.4 confirmed per 100k out-tokens over 12 runs (`research-role-shapes-a.md:42`, `research-role-shapes-b.md:46`) | — | both |
| The review-shape line | nothing reads it, and it lacks the effort and the shape (`research-role-shapes-a.md:184`, `research-role-shapes-b.md:223`) | — | `review.cost` writes a shape-run record |
| Efforts nothing measured | the orientation scout stays at xhigh until a trial says otherwise (`research-role-shapes-a.md:192`, `research-role-shapes-b.md:232`) | — | fork RS-2 |
| Rejected mechanisms | — | A rejects escalating on the first run's output, which fires on 37 of 43 runs; B rejects choosing shapes adaptively from the ledger, which needs 10.8 runs per arm (`research-role-shapes-a.md:83`, `research-role-shapes-b.md:93`) | both rejected |

### [agree-memory-structure] Memory structure, dispatches 81 and 82

| Question | Both runs | Where they differ | The design takes |
|---|---|---|---|
| The mechanism | keyed sections, read through one command and handed out by the work order (`research-memory-structure-a.md:13`, `research-memory-structure-b.md:15`) | A calls it a catalogue, B a section index | both, as one index with the tags' (`[cross]`) |
| The index | generated, keyed by tree hash, never tracked and never loaded whole (`research-memory-structure-a.md:119`, `research-memory-structure-b.md:18`) | A: JSONL, 0.9 s; B: TSV, 0.44 s | one JSON index, as `[cross]` names it (revised 2026-10-17, the audit's L3) |
| Default load | the card only, under a budget (`research-memory-structure-a.md:17`, `research-memory-structure-b.md:22`) | A: 6 KB or less; B: 8 KB | 8 KB |
| Why | reads run too wide rather than miss: an id grep returns a median 15.5 files (`research-memory-structure-a.md:56`), and a spec's median section is 715 B, 4% of its file (`research-memory-structure-b.md:81`) | different measures | both |
| Rejected: summaries and ranked retrieval | summaries drop identifiers, and recall's read-through is under 6% (`research-memory-structure-a.md:83`, `research-memory-structure-b.md:153`) | — | rejected |
| Recall's read-through | 33 of about 590 queries led to a read of a shown hit (`research-memory-structure-a.md:31`, `research-memory-structure-b.md:86`) | A also measures a 477 MB cache | both |
| Rejected: cold tiers | moving dormant builds out of the default path saves little (`research-memory-structure-a.md:103`, `research-memory-structure-b.md:145`) | — | rejected |
| Auto-memory | the harness's auto-memory index loads 14 KB every session, outside the contract, and its directives should be promoted through the instruction write path (`research-memory-structure-a.md:206`, `research-memory-structure-b.md:255`) | B then holds it to the load budget | fork MS-1 |
| Over budget | — | A refuses at render (`research-memory-structure-a.md:207`); B counts whole-file reads and refuses only under strict (`research-memory-structure-b.md:261`) | fork MS-2 |
| Legacy records | headings become derived anchors and are never rewritten (`research-memory-structure-a.md:208`, `research-memory-structure-b.md:252`) | — | derived |
| The gap | no index by key and no read budget (`research-memory-structure-a.md:195`, `research-memory-structure-b.md:238`) | A grades it HIGH, B MED | HIGH |

## [cross] Where the five systems meet

- **One grammar, one index, one resolver.** Both tag runs derive a tag index keyed by tree id, and both
  memory runs derive a section index keyed by tree hash. They index one population under one key, because
  memory's sections are the tag system's `section` namespace. So there is one derived index:
  - the tag system's engine builds it from the extractors each owning layer registers;
  - memory registers the `section` and `record` extractors, and `record find` and `record show` are its
    views over that index;
  - `gov tag show <address>` and `record show <id>#<tag>` resolve through one resolver.
  - **Where it lives** (revised 2026-10-17, the audit's M17 and L3).
    - The index is one JSON file per tree, at `<git-common-dir>/gov/index/<tree>.json`, shared
      across worktrees.
    - It is written atomically, with a temp file and a rename. So concurrent rebuilds on a cold
      cache race to one identical file, and a reader never sees a torn one.
  - **An uncommitted edit.** A working tree with uncommitted edits is served HEAD's tree, overlaid
    with the working-tree blobs of its modified tracked files. Those rows are marked `dirty`, and
    the freshness check exempts them.
  - **Probe:** five concurrent `gov tag show` calls on a cold cache, then a query after an
    uncommitted edit.

  dOrderedCharter builds the grammar, the engine and the resolver; dTotalRecall registers memory's
  extractors and its read verbs.
- **One work order, one budget per slot** (revised 2026-10-17, the audit's M1). A role item's work order carries its
  instruction units, its memory sections, its code-note rows and its legacy rows, each selected by tag.
  The instruction layer renders it (P27). Each slot has one key and one answer when it runs over:
  - **The instruction load set** is budgeted by P27. Over its budget, it is refused at render, as
    `instructions.checks` says, or routed back by the roles layer.
  - **The memory slices** are priced by `memory.item-budget`. Over it, they are answered by
    `memory.over-budget`: counted and reported under the default `report` (MS-3), never refused and
    never routed back.
  - **The code-notes slot** is capped at 2 KB, and the legacy slot by `retrofit.slot-bytes`. Rows
    past a cap are left to the query by tag.
  - **Why.** The first text named one byte budget per item with no key. That gave one over-budget
    work order three answers.
- **Annotations point at tags.** A `gov:note` line's tags and pointers resolve through the same resolver,
  and a directive in code points at the instruction unit that states it.
- **Shapes are data; their texts are units.** A shape never loads into an agent. Its checklist and
  orientation template are instruction units, `orient.*`, selected into the role's static block or work
  order by tag.
- **The order.** The grammar, the index engine and the unit schema come first, with dOrderedCharter at
  the chain's root. Memory's extractors, the role shapes and the annotation checks build on them.
- **Retrofit** (2026-10-17, `build/2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md`) is a sixth system
  across the layers. Its ledger holds the shrink-only populations these five name: the positional
  references, IW-1's legacy list, the resolve check's legacy, the untouched long blocks, and the `gov:`
  waiver markers. Its `[cross]` says
  how each system meets it.

## [design] The design, system by system

### [design-tags] Tags

- **Grammar.** `tag := <ns>.<seg>(.<seg>)*`, `seg := [a-z0-9][a-z0-9-]*`, at most 64 B. A section is
  `<doc> [<seg>]`, unique within its document. Ids keep memory's grammar: `FAMILY-<slug>-<seq>` and
  `gap-<area>-NN`. A first segment may not be a namespace word.
- **Map keys** (revised 2026-10-17, PM-11): a map line keys a node by its native id where one exists,
  as `chain.dTotalRecall` and `principle.P27`, and by its tag otherwise. The resolver accepts both.
- **Namespaces.** R-B's twelve, plus `section`, `doc`, `unit`, `field`, `leg`, `check`, `point`, `hook`,
  `command`, `pack`, `feature` and `class`, and `marker` (`[design-annotations]`). Each namespace is a row
  in its owning layer's contract: its declaring source, its extractor, and whether it selects or
  describes. An expansion mints only under its own prefix, at a core point.
- **A leg keeps its name** (revised 2026-10-17, the audit's M26).
  - A leg gains a `tag` field beside its free-text `name`. The shape check grades the tag, never the
    name.
  - The name stays the join key of every file keyed by leg name:
    - `tools/run-gates/ceiling-evidence.txt`, `selftest-budgets.txt` and `windows-only-legs.txt`;
    - `tools/roles/house/policy.toml`'s `[gates]`;
    - every kit.toml's `silenced_legs`;
    - the run-log history.
  - 139 of today's 140 leg names fail the tag shape.
- **Mint, rename, retire.** A tag is minted by writing its declaring site through that site's write path.
  A rename or retirement writes `retired → <new>` or `→ none` into that write path's change record, and
  the index derives the redirect from it. A retired name is never reused.
- **Index and resolver.** The index is the one derived JSON file `[cross]` places, keyed by tree id,
  rebuilt on a miss, never committed and never loaded whole. `gov tag show|where|refs|check <address>` returns the
  smallest leaf slice in one call.
- **Joins.** `compute_coverage` moves to `tools/lib` as the join factory, because the map that holds it
  today is optional.
- **Positional references.** Numbers that never moved, such as the M-steps and the hygiene checks, become
  alias rows to their tags. Live text migrates through Convergence, and frozen records resolve through the
  aliases. Meanwhile the live references are held by key, path and reference: dOrderedCharter keeps
  them as a keyed list, and dWitnessedBar's migration registers that list as a ledger population.
  They are never held as a count (revised 2026-10-17, the audit's M4).
- **Checks**, the `tags` leg pack, also run at render, softened only through `instructions.checks`:

  | Check | Red on |
  |---|---|
  | shape and registered namespace | `item.Build.Scope`; run over today's population when a namespace registers, reporting how many sites fail its shape |
  | unique | a second `plan.input` row, or a second `## [design]` in one record |
  | owned | an expansion declaring `item.build.x` |
  | resolves, with bare references as `tags.bare-refs` says | `layer-memory [nmes]`; under `unique`, a bare reference two namespaces match; under `never`, any bare reference outside the charter (revised 2026-10-17, the audit's M30) |
  | retired | new text citing a retired tag, or a retired name minted again |
  | joins (R-B), armed per population | a step with no unit; "unarmed" while a population is empty, never green |
  | positional | a new `§n`, `Mn` or `check n` in live text |
- **Owners.** The instruction layer, kit `playbook`, chain build dOrderedCharter. Each registration
  carries its extractor. Six namespaces gained an owner (revised 2026-10-17, the audit's M10):
  - dOrderedCharter registers `doc` and `unit`, and, declared at PM-10 (2026-10-17), `reader`, `level`, `layer`, `practice`, `principle`, `kind` and `kit`;
  - dDeclaredLoop `step`, `item`, `policy` and `command`;
  - dBoundRoles `role` and `field`;
  - dTotalRecall `section`, `record`, `feature`, `class` and `marker`;
  - dWitnessedBar `leg`, `check` and `pack`;
  - dWellOiledMachine `hook` and `point`.
- **Keys.**

  | Key | Values | Default |
  |---|---|---|
  | `tags.slice` | leaf, subtree | leaf |
  | `tags.retired-cites` | refuse-new, warn, allow | refuse-new |
  | `tags.positional` | shrink-only, refuse, report | shrink-only |
  | `tags.bare-refs` | charter-only, unique, never | charter-only |

### [design-annotations] Code annotations

- **The line.** `gov:note <tag>[,<tag>…] — <definition, at most 80 chars> → <unit tag|path|command>
  [refs=<id|path>[,…]]`, and `gov:feature <tag>`. It holds a definition and pointers. A body line holding
  MUST or NEVER needs `refs=` to the unit or record that states it. It has no level and never loads at a
  load point; in a work order its rows are data inside the task.
- **Markers** (revised 2026-10-17, the audit's M33).
  - `gov:` is a reserved prefix, and `note` and `feature` are its annotation words.
  - The 20 words gates already read are registered in the `marker` namespace, each with its reading
    check. `gov:kit`, `gov:fixed-verifiers` and `gov:bounded-fanout` are three of them, and together
    they mark 374 sites outside `memory/` at `51dfed5a5`.
  - A word a gate reads as a waiver is a ledger population of that check (retrofit `[ledger]`).
  - The grammar check runs per registered word, and an unregistered `gov:` word reds.
  - Probe: the marker query over today's tree classifies every site, with none unregistered.
- **What stays and what moves.** A comment keeps what its block implements, what would break without it,
  and its pointer. Dates, measurements and what a block used to do move to the record `refs=` names.
- **Budget.** A block a commit touches is at most 12 lines, and a head line at most 160 B.
  - Untouched legacy blocks over 12 lines, the touched-block cap, are a ledger population (retrofit
    `[ledger]`), keyed by path and block anchor.
  - The first design held a count over blocks of 9 or more, from run A's 8-line cap. A count lets a
    drained long block offset a newly grown one (revised 2026-10-17, the audit's M4).
- **Delivery** (revised 2026-10-17, the audit's M8):
  - the work order's code-notes slot, at most 2 KB, filled from the item's tags and write set;
  - a query by tag, through the marker query or the map's index as `annotations.lookup` says (AN-1);
  - and, only under `annotations.grammar: pushed-at-read`, the read hook (AN-2, as `[answers]`
    designs it). Under the default, nothing is pushed when a file opens.
- **Checks**, one `annotations` leg, each seen red on a planted case first:
  - grammar;
  - resolve, over every id and `memory/` path a comment cites, with exemption rows for fixtures and
    foreign families. It is red on day one on the gotcha path that never existed, which the arming unit
    fixes;
  - one anchor per feature tag;
  - the touched-block budget;
  - history inside a note's body;
  - the read hook, under `pushed-at-read`: it fires on a planted `cat <code path>` shell call, and
    injects once per session;
  - the lookup: with the map absent, the slot renders "not installed" and falls back to the marker
    query;
  - markers: no unregistered `gov:` word.
- **Owners.** The memory layer, kit memory-tree, chain build dTotalRecall. The tags come from
  dOrderedCharter's registry, and the slot from dBoundRoles' work order.
- **Keys.**

  | Key | Values | Default |
  |---|---|---|
  | `annotations.budget` | refuse, warn, record | refuse, on touched blocks |
  | `annotations.resolve-scope` | notes, every-comment-ref | every-comment-ref |
  | `annotations.delivery` | work-order, on-demand, off | work-order |
  | `annotations.lookup` | query-and-map, query, map-index | query-and-map (AN-1) |
  | `annotations.grammar` | voluntary, required, pushed-at-read | voluntary; `pushed-at-read` kept and redefined for shell reads (AN-2) |

### [design-instruction-writing] Instruction writing

- **The unit.** One TOML row in `tools/<kit>/instructions.toml`, the adopter's in
  `.governance/instructions.toml`, merged by row key. Its fields: `tag`, `type` (directive, constraint,
  definition, pointer, policy, fact), `level`, `select`, `when`, `text` (one line, at most 200 B) or
  `source` (derived), `required-by`, `enforced-by`, `budget`, `status` (`active` or
  `retired:<forward-tag>`), and `help` for the rationale, which never loads. `status` is derived from the
  `instructions.edit` change record that `[design-tags]` reads for every retirement, and is never typed
  (revised 2026-10-17, the audit's L7).
- **Per type.** A directive carries a modal. A constraint carries a value and its enforcer. A fact
  carries a source and never typed text. A pointer's target resolves to a unit, a slice or a command,
  never a whole document.
- **Templates.** One per document kind, holding slot selectors and no prose: the charter, the card's
  slots, a protocol slice, a Skill entry, a path rule, the role static block, the work order, a hook
  message, a harness prompt module, and the instruction fields of a spec.
  Rationale moves into each unit's `help` field, outside every load set.
  It never goes to `help/`, whose pages are user-facing features (`help/README.md:3`) under the
  playbook kit's adopter-set `HELP_DIR` (`playbook.kit.toml:252-255`) (revised 2026-10-17, the audit's L10).
- **The renderer and its gate.** One renderer, extending `render_charter_blocks` and the playbook's
  probes. One leg refuses any file at an instruction path whose bytes differ from its render, or that no
  registry row produces. Unmigrated documents sit on a shrink-only legacy list.
- **The renderers it absorbs** (revised 2026-10-17, the audit's M27). Each existing renderer and leg over instruction files has
  a disposition, and a check holds every instruction file to exactly one renderer of record.
  - **Absorbed at dOrderedCharter,** over the documents it renders first, the charter and the agent
    files: playbook parity, playbook render wiring and its selftest, roles render wiring and its
    selftest, and agent-instructions wiring.
  - **Kept beside the legacy list until their documents migrate,** each retired with its last
    document: kit/dogfood doc parity, review-protocol parity, each kit's skill wiring `--check`, and
    govkit's placeholder render in adopters.
- **Checks:** schema; grammar; positional references; one fact in one unit (two active units with one
  subject and value); render parity; unregistered files; the budget per load point both ways, too much
  and too little; the joins; a single carry, no unit twice in one spawn. The single-carry check reads
  `instructions.task-charter` and the harness kind, and refuses `always` on a backend that loads the
  static block, where it would carry the charter twice. The strict preset's value is now
  `when-not-static` (revised 2026-10-17, the audit's M29).
- **The saving, re-measured at landing.** A spawn's fixed text falls from about 8.7 KB to about 4.8 KB,
  and a builder item's from 35.6 KB to about 8.4 KB; whole-guide reads for triggers the item decides
  fall to none. The render ledger measures bytes per load point per spawn, before and after, on the same
  item tags.
- **Owners.** The instruction layer. dOrderedCharter builds the schema, the grammar, the renderer, the
  charter and work-order templates and the write command. dBoundRoles builds the role static block and
  the single carry. dWellOiledMachine builds the hook-message and harness-prompt templates.
  dConvergedCharter builds the protocol slices and Skill entries, and each step's guides migrate as
  IW-1 settles.
- **Keys.**

  | Key | Values | Default |
  |---|---|---|
  | `instructions.slices` | handed, pointer | handed |
  | `instructions.legacy` | shrink-only, refuse | shrink-only |
  | `instructions.task-charter` | when-not-static, always | when-not-static |

### [design-role-shapes] Role workflow shapes

- **The registry** (revised 2026-10-17, the audit's M18).
  - **One registry, extended.** Each `tools/roles/workflows.toml` entry gains its shape: its kind, its
    fan, its checklist and orientation template (both instruction unit tags), its merge, its twin
    rule, and its agent cap. A per-call intensity is a named variant row. That is run A's pick
    (`research-role-shapes-a.md:15,116`).
  - **The agent cap** is bounded by agent-cap's `FANOUT_CAP`, never a new value.
  - **Effort stays in `policy.toml`,** under `[effort.roles]` and `[effort.stages.<workflow>]`, which
    `resolve_stage_efforts` already reads (`roles_lib.py:561`).
  - **Why.** The first design added `tools/roles/shapes.toml` beside `workflows.toml`, which already
    declares each workflow's roles and stages (`workflows.toml:37-67`). That made two registries over
    one fact.
  - **The consumers dBoundRoles rewrites in the same unit:**
    - R12 and `resolve_stage_efforts` in roles_lib.py;
    - `handoff.py stage-efforts` and `harness-args`;
    - check_roles.py R6 to R9;
    - adopt-roles.sh, render_agents.py and check-wiring.sh;
    - agent-cap's `args.roles` refusal;
    - the build Skill's calls.
- **Kinds.** Four role harnesses registered at Runtime's role-harness point: `single`, `per-unit`,
  `panel` (finders, at most five skeptic batches, one synthesizer) and `twin` (two runs of one shape,
  merged).
- **Binding.** The work order carries the resolved shape's digest. Act binding refuses a Workflow call
  whose roles, efforts or fan differ from it, and the supervisor reconciles the journal against the shape
  afterwards. A verifier stage whose role wrote the artifact it verifies is refused.
- **Twins and their merge.** Twins run only on the owner's opt-in (RS-1). A synthesizer places both runs' findings on
  defects over candidate pairs grouped by address, and the comparison instrument refuses an unplaced id.
- **The metric.** Recall first, against a twin union or a known replay set, then grade-weighted verified
  results per 100k out-tokens. The shape-run record has two writers (revised 2026-10-17, the audit's M9 and L6).
  - **A review act's row:** `review.cost` extends the `review-shape` line that
    `tools/workflows/tier2-review.js:79` already emits, adding `shape`, `efforts` and `role-sha`. The
    shape-run record is that line's parsed view, and `tier2-review.test.sh`'s SHAPE_RE and the reader
    at README:265 move with it.
  - **Every other role act's row** comes from the supervisor's journal reconcile (dWellOiledMachine),
    which already binds each act's agents to its shape.
  - **The kind** is registered in `[design-memory-structure]`. The Loop Review prices shapes in the value ledger and proposes a change only past the
  measured noise between twins.
- **Per role:**

  | Role | Kind | Effort | Orientation template |
  |---|---|---|---|
  | orientation scout | single | medium (RS-2) | the card |
  | prompt writer | single | medium | the resolved work order |
  | planner, architect | single | high | `orient.producer` |
  | researcher | single (RS-1) | medium | the handed question |
  | reuse scout | single, never twinned | medium | the house index first, then a sketch and a census |
  | spec writer, builder | per-unit | high (RS-2) | `orient.producer` |
  | tester | single | medium | `orient.verifier-cold` |
  | reviewer, skeptic, synthesizer | panel | diff high; spec and design audits medium | `orient.verifier-cold` |
  | deployer, maintainer | single, registered by their expansions | medium | `orient.producer` |
- **Checks:** every role item names a shape and every stage a declared role; the binding, red on today's
  probe, a builder as reviewer at low effort; the journal reconcile, red on a planted extra agent; the
  separation of author and verifier; twin placement; a shape-run record for every role act, from
  `review.cost` for a review act and from the journal reconcile for every other.
- **Owners.** dBoundRoles extends `workflows.toml` with the shapes; dWellOiledMachine the binding, the
  reconcile and the non-review shape-run rows; dFairHearing the panel's internals and the twin merge; dCalibratedLens the ledger's shape
  rows.
- **Keys.**

  | Key | Values | Default |
  |---|---|---|
  | `review.twin` | never, design-records, design-and-landing, always | never (RS-1) |
  | `roles.shape-enforce` | refuse, record | refuse |
  | `roles.orientation.house-index` | handed, pointer, off | handed |

### [design-memory-structure] Memory structure

- **Sections.** Each record kind's registry entry declares its sections as `[tag]`s, each required or
  optional. Legacy headings get derived anchors: the spec template's numbered headings map to tags by a
  table, and no record is rewritten.
  - **A repeated heading** takes its parent's anchor plus an ordinal suffix, `-2` or `-3`, in
    document order (revised 2026-10-17, the audit's M35).
  - **Derived anchors are not graded for uniqueness.** That check grades only authored `[tag]`s.
  - **Probe:** derive anchors over the whole memory tree, and expect no collision. Today 13 tracked
    records repeat an H2 or H3 heading.
- **The index and the verbs.** Memory's rows live in the one index (`[cross]`): key, kind, layer, build,
  bytes, blob, tags, superseded-by and lifecycle. `record find --kind|--tag|--build|--paths` returns at
  most 40 rows and no content, with superseded rows hidden. When more match, its last line gives the
  total and a hint to narrow the query, held by a check on a planted 41-row case (revised 2026-10-17, the audit's L11). `record show <id>#<tag>[@blob]` returns one
  section.
- **Work orders hand sections.** A role item's read set is declared as `id#tag` keys. The executor inlines
  the slices under the item's byte budget and writes a slice manifest. A read outside it, through Read,
  a shell command or `record show`, is journaled and counted (revised 2026-10-17, the audit's H2).
- **Default load.** The charter and the card, the card at most 8 KB.
  - **An attended session also opens with the map** (PM-7, `build/2026-10-17-build-PLAY-dClosedLoop-1-project-map.md`): the level-0 project map, at
    most `memory.map-budget`. An act session loads its work order.
  - **The harness's auto-memory,** as MS-1 settles, is promoted, and what remains is held to
    `memory.load-budget` too. The card and the auto-memory's remainder each get the budget, not a
    share of it.
  - **A session-start check** reports the auto-memory's bytes against the budget. The session-start
    hook runs it, where the per-user store is readable, and it is seen red on a planted 9 KB index
    (revised 2026-10-17, the audit's M12).
- **The shape-run record** is a registered kind: the `review-shape` line's parsed view, with the
  journal's rows for non-review acts (`[design-role-shapes]`).
- **Homes.** Build folders stay. A record no build owns goes under `memory/<layer>/<kind>/`.
  `DECISIONS.md`, `gotchas/` and `map/` are declared homes at their paths.
- **Checks:**

  | Check | Red on |
  |---|---|
  | sections | a new spec headed `## Goal` |
  | keys resolve, both ways | a dangling `rec:` key, or one authored section tag twice in a record |
  | item budget, as `memory.over-budget` says | under `report`, a planted over-cap work order missing from the report with its role and bytes; under `refuse`, a fixture's over-cap work order rendered (revised 2026-10-17, the audit's M1) |
  | no default ingest | `@memory/DECISIONS.md` in `CLAUDE.md` |
  | superseded slices | a superseded decision handed to a builder |
  | index freshness | a row served without `@blob` whose blob is not the tree's, outside the rows marked `dirty` (revised 2026-10-17, the audit's L3 and M17) |
  | auto-memory | a session-start report missing a planted 9 KB index over `memory.load-budget` |
- **The acceptance re-measure** (revised 2026-10-17, the audit's H2).
  - **The target.** Thirty days after landing, the median memory bytes per agent that reads memory
    are below 33 KB.
  - **The measure counts every channel:**
    - the work order's inlined slices, from the slice manifest;
    - Read results on memory paths;
    - the output of shell commands that name a memory path or call `record show`, `record find` or
      `gov tag`.
  - **Why 33 KB.** Today's median under that measure is 57.2 KB, over 3,073 agents. 33 KB is the
    ratio research B's test set, 40 of 68.9 KB (`research-memory-structure-b.md:204`).
  - **Why the first measure could not fail.** It counted Read calls alone, which carry 40.0% of
    today's memory bytes. Moving reads into work orders and `record show` would have passed it by
    construction (`[ms2-instrument]`, its third run).
- **Owners.** The memory layer, kit memory-tree, chain build dTotalRecall. dBoundRoles renders the slices,
  and dRankedPlan sizes read sets at Plan.
- **Keys.**

  | Key | Values | Default |
  |---|---|---|
  | `memory.default-load` | card, card-and-live, card-and-map | card-and-map for attended sessions (PM-7) |
  | `memory.load-budget` | 4k, 8k, 16k | 8k |
  | `memory.item-budget` | measured, 96 or 128 for every role, or KB per role, a KB being 1,000 bytes, each role's the owner's to set | measured: 96 for every role until 30 sliced work orders per role are measured, then each role's own p90 (MS-2, asked a third time; the unit revised 2026-10-17, the audit's L5) |
  | `memory.over-budget` | refuse, report, off | report (MS-3) |
  | `memory.legacy-anchors` | derived, none | derived |
  | `memory.superseded-slices` | refuse, mark | refuse |

## [forks] To put to the owner

| Fork | The question | Options, the recommendation first |
|---|---|---|
| AN-1 | Where are annotation tags found? | an on-demand marker query in core memory-tree, 0.057 s with nothing to keep fresh; or the map's generated index, as layer-memory designed it |
| AN-2 | What happens to `pushed-at-read`, an allowed value of `annotations.grammar`? | retire it, since a Read hook sees 3 to 5% of code reads; or redefine it to fire on shell reads too |
| IW-1 | When does the render gate start refusing hand-written instruction documents? | at dOrderedCharter, with a shrink-only legacy list and each chain build migrating its own step's guides; or only at dConvergedCharter, the chain's last build |
| IW-2 | Where does each practice's reach per step live? | as step-scoped units handed in work orders, the charter keeping one line per practice; or inline in the charter, which leaves about 4% headroom under its 32 KiB cap |
| RS-1 | When do twin runs happen by default? | on design records; never; or on design records and at landing |
| RS-2 | What happens to the efforts no measurement backs, the orientation scout's and the builder's xhigh? | keep them until a matched trial says otherwise; or lower them now |
| MS-1 | What happens to the harness's auto-memory, 14 KB loaded every session? | promote its standing directives through the instruction write path, then hold it to the load budget; unload it; or leave it |
| MS-2 | What happens to a work order over its memory budget? | refuse it at render, since the retired global budget never trimmed; or count it and refuse only under strict |
| MS-3 | What happens to a work order over its role's cap, now 96 KB? | report, then refuse once the sliced loads are measured over 30 work orders per role; refuse at render now; report only; or refuse under strict only |

## [answers] The owner's answers, 2026-10-17

The first four forks, answered in one round. Each answer is quoted verbatim.

| Fork | The owner's answer | What it settles |
|---|---|---|
| AN-1 | "both Marker query and part of codebase map tool index" | `annotations.lookup`: `query-and-map` by default, with `query` and `map-index` allowed. The core marker query always answers, and the codebase map's index carries the annotations too where the map is installed |
| AN-2 | "Redefine for shell reads" | `pushed-at-read` stays an allowed value of `annotations.grammar`, redefined to fire on shell reads as well as Read; the default stays `voluntary` (F4-2) |
| IW-1 | "At dOrderedCharter (Recommended)" | the render gate is armed at dOrderedCharter, with a shrink-only list of today's documents; each chain build migrates its own step's guides |
| IW-2 | "Step units in work orders (Recommended)" | the charter keeps one line per practice, and each practice's reach per step renders as step-scoped units handed in work orders |
| RS-1 | "twin runs are only this rearchitecture design's measure, by default,  this does not apply to the actual product methods. However, this should be an owner opt-in option: a review step runs a two parallel review cadence in the normal flow instead of one (in the normal review flow)." | `review.twin`: `never` by default in the product; `design-records`, `design-and-landing` and `always` are the owner's opt-in, under which a review step runs two parallel reviews instead of one, merged by the synthesizer. Twin runs in this build stay the rearchitecture's own measure |
| RS-2 | "move orientation to medium, builder to high" | the orientation scout runs at `medium` and the builder at `high` |
| MS-1 | "Promote, then budget (Recommended)" | the auto-memory index's standing directives move into instruction units through `instructions.edit`, and what remains is held to `memory.load-budget` |
| MS-2 | the owner asked, verbatim: "Why was memory partitioned like that? Was there a reason for these caps?" | answered in `[ms2]` and asked again |
| MS-2, asked again | "set a default cap of 96K per role, but owner-adjustable per role" | `memory.item-budget`: 96 KB for every role by default, and each role's cap is the owner's to adjust. What happens to a work order over its cap is asked as MS-3 |
| MS-3 | "Report only" | `memory.over-budget` defaults to `report`: a work order over its role's cap is counted and reported, never refused |
| MS-2, asked a third time, 2026-10-17, after the audit's H2 corrected its measure | "Measure, then set" | `memory.item-budget` defaults to `measured`. Every role reports against 96 KB until 30 sliced work orders per role are measured. Then each role's default is that role's own p90 over them, which the Loop Review derives. The owner can still set any role's cap, and `96` and `128` for every role are the other allowed values |

- **AN-1, as designed.** The marker query in core memory-tree stays the path the core can always take
  (P28). The codebase map's lexer gains the annotation rows as part of its index: a shebang profile for
  extensionless files, docstrings, and string exclusion, which the plain marker query cannot do. With
  the map absent, the slot renders "not installed" and names the marker query as its fallback.
- **AN-2, as designed.** The read hook pack fires on PostToolUse Read and on PostToolUse Bash. On Bash it
  reads the command's path arguments for `sed`, `cat`, `head`, `tail` and `grep` over code paths, never
  the command's output, and injects each named file's anchored rows once per session. Its reach is
  re-measured after landing on the same transcript mix; today's Read-only hook reaches 3 to 5% of
  code-reading calls.

  **Revised 2026-10-17, the audit's M15.** The first text matched Read and Bash only, and parsed five
  commands.
  - **What the pack matches.** It matches `Bash|PowerShell`, as every shell hook in
    `.claude/settings.json` does, and the Grep tool's path argument too.
  - **What it parses,** by the commands' measured share: `grep` and `rg`, `sed -n`, `cat`, `git grep`,
    `git show <rev>:<path>`, PowerShell's `Get-Content` and `Select-String`, and `head` and `tail`.
  - **How it reads a path.**
    - It folds MSYS spellings (`/c/...`) and drive-letter spellings onto repo-relative paths, as
      `scratch-guard.js:161-162` and `:818` do.
    - It resolves a path against a leading `cd` or a `git -C`.
    - A directory argument injects the rows of its tracked files within the 2 KB slot, nearest
      first.
  - **Its carriers** are `.claude/settings.json` and the hook's settings fragment, under the
    `*.fragment.json` eol rule.
  - **Probe:** replay a sample of transcript shell reads through the parser, and count the share
    that resolves to a tracked file. A fixture holds it to a minimum share.
- **IW-2 amends v2's front door** at the fold: the charter's practice lines stay one each, and the reach
  table leaves the charter for step-scoped units.
- **RS-1, as designed.** No product step twins by default. `review.twin` opts a review step in, and an
  opted-in step runs two parallel reviews of one shape in place of one, merged by the synthesizer. The
  researcher runs single, since the owner opted review steps in and no other. The metric's recall is
  taken against a known replay set, or the twin union where twins run. The noise between twins that gates
  a shape change is this build's measured noise until opted-in twins re-measure it.
- **RS-2, as designed.** The orientation scout drops from `xhigh` to `medium` and the builder from `xhigh`
  to `high`. The spec writer stays at `high`.

## [ms2] Where the per-role memory budgets came from

- **Run A alone proposed them.** Its key `memory.item-budget` set builder 24 KB, reviewer 48 KB and
  researcher 64 KB (`research-memory-structure-a.md:172`). Run B named a read allowance per role as what
  role shapes need, with no figure (`research-memory-structure-b.md:141`). Its only budget is the card's,
  from the card's measured p90 of 6.1 KB and maximum of 7.8 KB (`research-memory-structure-b.md:224`).
- **No role was measured.** The figures rest on two measurements across all roles. The memory a subagent
  reads has a median of 52.7 KB and a p90 of 183.6 KB over 1,328 agents
  (`research-memory-structure-a.md:57`). A slice ratio of 29% was taken from one handoff
  (`research-memory-structure-a.md:86`). The builder's 24 KB is that ratio applied to the median, plus a
  margin (`research-memory-structure-a.md:144`). The reviewer's and researcher's figures carry no
  derivation.
- **Measured per role, 2026-10-17.** The same measure, split by the agent type each subagent's
  `meta.json` records, over 3,604 subagent transcripts (`[ms2-instrument]`, its first run; the
  researcher's and diff reviewer's rows moved in its second (revised 2026-10-17, the audit's L2)):

  | Agent type | Agents | Reading memory | Median | p90 |
  |---|---|---|---|---|
  | gov-builder | 38 | 38 | 78.6 KB | 128.4 KB |
  | gov-spec-writer | 76 | 66 | 72.3 KB | 225.7 KB |
  | gov-spec-reviewer | 90 | 90 | 64.3 KB | 149.0 KB |
  | gov-researcher | 54 | 30 | 55.0 KB | 138.7 KB |
  | gov-diff-reviewer | 43 | 33 | 48.1 KB | 115.2 KB |
  | gov-skeptic | 144 | 33 | 40.1 KB | 68.7 KB |
  | workflow-subagent | 2,608 | 1,002 | 49.6 KB | 199.3 KB |
  | all, pooled | 3,604 | 1,346 | 52.5 KB | 179.8 KB |

- **Run A's order is inverted.** It gave the builder the smallest budget, and builders read the most
  memory: a median of 78.6 KB, against 40.1 KB for skeptics. Roles differ by about two times at the
  median, so a per-role budget has a basis. Run A's figures do not.
- **What the measure cannot say.** Today's reads are whole files, and the design hands sections, so the
  table measures today's habit, not what a sliced work order would hand. The 2,608 workflow agents carry
  no role in their `meta.json`. Their roles are in each run's journal.
- **The design took one run's unmeasured figures as defaults.** `[design-memory-structure]` is corrected:
  each role's budget was to be derived from a measurement of that role, as `[forks]`' MS-2 was asked
  again. The answer settled one cap for every role, below (revised 2026-10-17, the audit's L2).
- **Settled, 2026-10-17 (MS-2).** A cap of 96 KB for every role by default, each role's cap the
  owner's to adjust. Today's whole-file loads sit under it at every role's median, and over it at every
  role's p90 except the skeptic's. 25.6% of the agents that read memory went over 96 KB: 39.5% of
  builders and 2.9% of skeptics (`[ms2-instrument]`, its second run).
- **Counted over every channel, 2026-10-17** (revised 2026-10-17, the audit's H2). Read carried only 40.0% of today's memory
  bytes. Shell commands carried 59.5%, and Grep 0.5%. Counted over all three (`[ms2-instrument]`, its
  third run):
  - **Three roles' medians are over the cap:** the builder's 124.1 KB, the spec reviewer's 113.7 KB
    and the spec writer's 110.5 KB.
  - **31.7% of the 3,073 agents that read memory went over 96 KB,** 65.8% of builders and 7.0% of
    skeptics.
  - **What the figures are.** They are still today's whole-file habit, as above.
  - **MS-2 went back to the owner.** The owner had chosen 96 KB from a table whose every median sat
    under it, so MS-2 was put to the owner again with these figures.
  - **The answer, 2026-10-17:** "Measure, then set". Every role reports against 96 KB until 30 sliced work
    orders per role are measured, and then each role's default is that role's own p90 over them
    (`[answers]`).

### [ms2-instrument] The per-role probe and its output

```python
"""Memory Read bytes per subagent, split by the agent's type: run A's memq3 measure (Read tool calls on a path
under /memory/, the result's UTF-8 bytes, summed per agent), grouped by the agentType each subagent's
meta.json records.

Usage: python memq_roles.py
Prints, per agent type: agents, agents that read memory at all, and the median and p90 of memory bytes
over the agents that read any. Run A's figures (1,328 agents, median 52,694, p90 183,553) pooled every type.
"""
import collections
import glob
import json
import os

root = os.path.expanduser("~/.claude/projects")
files = glob.glob(root + "/C--projects-coding-governance*/**/subagents/**/*.jsonl", recursive=True)
by = collections.defaultdict(list)
seen_all = collections.Counter()
for f in files:
    meta = f[:-len(".jsonl")] + ".meta.json"
    try:
        kind = json.load(open(meta, encoding="utf-8")).get("agentType") or "unknown"
    except (OSError, ValueError):
        kind = "no-meta"
    seen_all[kind] += 1
    pend, tot = {}, 0
    for line in open(f, encoding="utf8", errors="replace"):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        c = (r.get("message") or {}).get("content")
        if not isinstance(c, list):
            continue
        for b in c:
            if not isinstance(b, dict):
                continue
            if b.get("type") == "tool_use" and b.get("name") == "Read":
                p = str((b.get("input") or {}).get("file_path", "")).replace(chr(92), "/")
                if "/memory/" in p:
                    pend[b["id"]] = p
            elif b.get("type") == "tool_result" and b.get("tool_use_id") in pend:
                pend.pop(b["tool_use_id"])
                cc = b.get("content")
                t = cc if isinstance(cc, str) else "".join(x.get("text", "") for x in (cc or []) if isinstance(x, dict))
                tot += len(t.encode("utf8", "replace"))
    if tot:
        by[kind].append(tot)


def q(v, p):
    return v[min(len(v) - 1, int(len(v) * p))]


pooled = sorted(x for v in by.values() for x in v)
print(f"files {len(files)}; agents reading memory {len(pooled)}; pooled median {q(pooled, .5)} p90 {q(pooled, .9)}")
print(f"{'agent type':24}{'agents':>8}{'reading':>9}{'median B':>11}{'p90 B':>10}")
for kind, n in seen_all.most_common():
    v = sorted(by.get(kind, []))
    if len(v) >= 5:
        print(f"{kind:24}{n:8}{len(v):9}{q(v, .5):11}{q(v, .9):10}")
    else:
        print(f"{kind:24}{n:8}{len(v):9}{'-':>11}{'-':>10}")
```

```text
$ python -I memq_roles.py
files 3604; agents reading memory 1346; pooled median 52503 p90 179767
agent type                agents  reading   median B     p90 B
workflow-subagent           2608     1002      49583    199267
no-meta                      426        1          -         -
gov-skeptic                  144       33      40120     68691
gov-spec-reviewer             90       90      64266    148973
general-purpose               77       48      35347     91398
gov-spec-writer               76       66      72349    225729
gov-researcher                54       30      55018    138658
gov-diff-reviewer             43       33      48067    115213
gov-builder                   38       38      78616    128420
gov-synthesizer               29        3          -         -
Plan                          18        2          -         -
Explore                        1        0          -         -
```

The second run, later the same day over more transcripts, appends the share over 96 KB to the same probe:

```python
print()
CAP = 96000
print(f"share of memory-reading agents over {CAP} B, per type")
for kind, n in seen_all.most_common():
    v = by.get(kind, [])
    if len(v) >= 5:
        over = sum(1 for x in v if x > CAP)
        print(f"{kind:24}{over:5} of {len(v):5}  {100 * over / len(v):5.1f}%")
over = sum(1 for x in pooled if x > CAP)
print(f"{'all, pooled':24}{over:5} of {len(pooled):5}  {100 * over / len(pooled):5.1f}%")
```

```text
$ python -I memq_roles_96.py
files 3617; agents reading memory 1352; pooled median 52694 p90 179714
agent type                agents  reading   median B     p90 B
workflow-subagent           2609     1002      49583    199267
no-meta                      427        1          -         -
gov-skeptic                  149       34      40120     68691
gov-spec-reviewer             90       90      64266    148973
general-purpose               77       48      35347     91398
gov-spec-writer               76       66      72349    225729
gov-researcher                56       32      57097    124531
gov-diff-reviewer             46       36      67292    116914
gov-builder                   38       38      78616    128420
gov-synthesizer               30        3          -         -
Plan                          18        2          -         -
Explore                        1        0          -         -

share of memory-reading agents over 96000 B, per type
workflow-subagent         263 of  1002   26.2%
gov-skeptic                 1 of    34    2.9%
gov-spec-reviewer          26 of    90   28.9%
general-purpose             2 of    48    4.2%
gov-spec-writer            23 of    66   34.8%
gov-researcher              8 of    32   25.0%
gov-diff-reviewer           8 of    36   22.2%
gov-builder                15 of    38   39.5%
all, pooled               346 of  1352   25.6%
```

The third run, 2026-10-17, after the systems and retrofit audit's H2. It counts every channel a
memory read can take, and first checks itself on two planted transcripts:

```python
"""Memory bytes per subagent, by agent type, over every channel a read can take (revised 2026-10-17, after
the systems and retrofit audit's H2: the first version counted Read calls only).

A tool call reads memory when it is:
- a Read whose file_path holds `/memory/`;
- a Bash or PowerShell call whose command names a path under `memory/`, or calls one of the designed
  read verbs (`record show`, `record find`, `gov tag show|where|refs`);
- a Grep whose path is under `memory/`.
Its result's UTF-8 bytes are summed per agent and per channel. A shell command that names a memory path
may print more than memory, so the shell channel is an upper bound, held the same before and after.

Usage: python -I memq_roles_v3.py
First runs the measure on two planted transcripts and exits 1 unless it counts a `record show` read and
ignores a shell read of no memory path, and unless the Read-only measure misses the first. Then prints,
per agent type, the Read-only median and p90, the all-channel median and p90, and the share over 96,000 B;
and the bytes per channel.
"""
import collections
import glob
import json
import os
import re
import sys

MEM_PATH = re.compile(r"(^|[\s'\"=/\\:])memory[/\\]")
VERBS = re.compile(r"\b(record\s+(show|find)|gov\s+tag\s+(show|where|refs))\b")
SHELL = {"Bash", "PowerShell"}
CAP = 96000


def channels(lines, read_only=False):
    """Memory bytes per channel in one transcript's lines."""
    pend, tot = {}, collections.Counter()
    for line in lines:
        try:
            r = json.loads(line)
        except ValueError:
            continue
        c = (r.get("message") or {}).get("content")
        if not isinstance(c, list):
            continue
        for b in c:
            if not isinstance(b, dict):
                continue
            if b.get("type") == "tool_use":
                name, inp = b.get("name"), (b.get("input") or {})
                if name == "Read":
                    if "/memory/" in str(inp.get("file_path", "")).replace(chr(92), "/"):
                        pend[b["id"]] = "read"
                elif read_only:
                    continue
                elif name in SHELL:
                    cmd = str(inp.get("command", ""))
                    if MEM_PATH.search(cmd) or VERBS.search(cmd):
                        pend[b["id"]] = "shell"
                elif name == "Grep":
                    p = str(inp.get("path", "")).replace(chr(92), "/")
                    if "/memory/" in p or p.startswith("memory/") or p == "memory":
                        pend[b["id"]] = "grep"
            elif b.get("type") == "tool_result" and b.get("tool_use_id") in pend:
                ch = pend.pop(b["tool_use_id"])
                cc = b.get("content")
                t = cc if isinstance(cc, str) else "".join(x.get("text", "") for x in (cc or []) if isinstance(x, dict))
                tot[ch] += len(t.encode("utf8", "replace"))
    return tot


def planted(cmd, nbytes):
    use = {"type": "assistant", "message": {"content": [
        {"type": "tool_use", "id": "t1", "name": "Bash", "input": {"command": cmd}}]}}
    res = {"type": "user", "message": {"content": [
        {"type": "tool_result", "tool_use_id": "t1", "content": "x" * nbytes}]}}
    return [json.dumps(use), json.dumps(res)]


shown = planted("record show PLAY-dClosedLoop-1#design", 5000)
control = planted("ls tools/run-gates", 3000)
arms = {
    "a record show over Bash counts its bytes": sum(channels(shown).values()) == 5000,
    "the Read-only measure misses it": sum(channels(shown, read_only=True).values()) == 0,
    "a shell read of no memory path counts nothing": sum(channels(control).values()) == 0,
}
for arm, ok in arms.items():
    print(f"planted: {arm}: {'yes' if ok else 'NO'}")
if not all(arms.values()):
    sys.exit(1)


def q(v, p):
    return v[min(len(v) - 1, int(len(v) * p))] if v else 0


root = os.path.expanduser("~/.claude/projects")
files = glob.glob(root + "/C--projects-coding-governance*/**/subagents/**/*.jsonl", recursive=True)
old, new = collections.defaultdict(list), collections.defaultdict(list)
seen, by_channel = collections.Counter(), collections.Counter()
for f in files:
    try:
        kind = json.load(open(f[:-len(".jsonl")] + ".meta.json", encoding="utf-8")).get("agentType") or "unknown"
    except (OSError, ValueError):
        kind = "no-meta"
    seen[kind] += 1
    lines = open(f, encoding="utf8", errors="replace").read().splitlines()
    tot = channels(lines)
    by_channel.update(tot)
    if tot.get("read"):
        old[kind].append(tot["read"])
    if sum(tot.values()):
        new[kind].append(sum(tot.values()))

po, pn = sorted(x for v in old.values() for x in v), sorted(x for v in new.values() for x in v)
print(f"files {len(files)}; agents reading memory: Read only {len(po)}, any channel {len(pn)}")
print(f"{'agent type':20}{'agents':>7}{'Read':>6}{'med B':>9}{'p90 B':>9}{'any':>6}{'med B':>9}{'p90 B':>9}{'over 96000':>12}")
for kind, n in seen.most_common():
    vo, vn = sorted(old.get(kind, [])), sorted(new.get(kind, []))
    if len(vn) < 5:
        continue
    over = sum(1 for x in vn if x > CAP)
    print(f"{kind:20}{n:7}{len(vo):6}{q(vo, .5):9}{q(vo, .9):9}{len(vn):6}{q(vn, .5):9}{q(vn, .9):9}"
          f"{100 * over / len(vn):11.1f}%")
over = sum(1 for x in pn if x > CAP)
print(f"{'all, pooled':20}{sum(seen.values()):7}{len(po):6}{q(po, .5):9}{q(po, .9):9}{len(pn):6}{q(pn, .5):9}"
      f"{q(pn, .9):9}{100 * over / len(pn):11.1f}%")
total = sum(by_channel.values())
for ch in ("read", "shell", "grep"):
    print(f"bytes through {ch}: {by_channel[ch] / 1e6:.1f} MB, {100 * by_channel[ch] / total:.1f}%")
```

```text
$ python -I memq_roles_v3.py
planted: a record show over Bash counts its bytes: yes
planted: the Read-only measure misses it: yes
planted: a shell read of no memory path counts nothing: yes
files 3709; agents reading memory: Read only 1372, any channel 3073
agent type           agents  Read    med B    p90 B   any    med B    p90 B  over 96000
workflow-subagent      2617  1002    49583   199267  2430    54507   210916       31.2%
no-meta                 435     1    74976    74976     6   108795   232219       50.0%
gov-skeptic             189    34    40120    68691   186    46710    87913        7.0%
gov-spec-reviewer        95    95    65174   148010    95   113721   186958       68.4%
general-purpose          77    48    35347    91398    72    59710   154081       30.6%
gov-spec-writer          76    66    72349   225729    76   110457   295554       56.6%
gov-diff-reviewer        69    51    41394   115213    68    73992   150457       39.7%
gov-researcher           56    32    57097   124531    53    60239   161813       35.8%
gov-synthesizer          38     3     7247     8359    31     8955    13175        0.0%
gov-builder              38    38    78616   128420    38   124061   230023       65.8%
Plan                     18     2    13422    13422    17    12989    65126        0.0%
all, pooled            3709  1372    52381   179278  3073    57185   197563       31.7%
bytes through read: 104.5 MB, 40.0%
bytes through shell: 155.3 MB, 59.5%
bytes through grep: 1.4 MB, 0.5%
```

## [gaps-proposed] Gaps to register once the forks settle

| System | Gap | Severity | Owner |
|---|---|---|---|
| tags | no section-tag resolver and no citation check: 1,438 citations, 788 of them ambiguous | HIGH | dOrderedCharter |
| tags | populations with no tag (gate legs, points, hooks, commands, fields, units) and colliding spellings (`build.scope` is an item and a policy) | MED | dOrderedCharter |
| tags | positional references have no gap and no ratchet | MED | dOrderedCharter |
| tags | spec section numbers mean different sections by tier | LOW | dIndexedDesign |
| annotations | a comment can cite a record that never existed, and no check sees it | MED | dTotalRecall |
| annotations | comment load is unbudgeted: 41% of code bytes, and about 29% of commits add a long block | MED | dTotalRecall |
| annotations | `pushed-at-read` reaches 3 to 5% of code reads | MED | dTotalRecall |
| instruction writing | every role spawn carries the charter blocks twice | MED | dBoundRoles |
| instruction writing | Workflow harness prompts are a load point with no grammar, budget or parity | MED | dWellOiledMachine |
| instruction writing | the static block's budget covers its base body only | LOW | dBoundRoles |
| instruction writing | one fact in one place is policed per instance, never as a class | MED | dOrderedCharter |
| role shapes | the spawn guard admits any agent-true role in any stage at any effort | HIGH | dWellOiledMachine |
| role shapes | nothing reads the review-shape line, and it carries no effort or shape | MED | dCalibratedLens |
| role shapes | twin merges have no item, record kind or check | MED | dFairHearing |
| role shapes | the review harness spawns an untyped agent that no stage declares | LOW | dFairHearing |
| memory structure | no index by key or section | HIGH | dTotalRecall |
| memory structure | no read budget per item, and the global one was retired | MED | dTotalRecall |
| memory structure | recall's cache is 477 MB for a 67 MB memory tree | LOW | dTotalRecall |

### [instrument-agreement] The both-runs probe over `[agreement]`

The probe is the one `build/2026-10-16-build-PLAY-dClosedLoop-1-expansions-reviews-compared.md` `[follow-up]`
holds, with two lines changed: its layers are this round's five systems, and its subsection pattern reads
a hyphenated name, `[agree-([a-z]+(?:-[a-z]+)*)]`, so `instruction-writing`, `role-shapes` and
`memory-structure` are read as their own tables. Its run over this record:

```text
rows read: 51; rows the predicate matched: 48
findings: 0
```

Over a copy with one cited line struck from the `Twins` row:

```text
rows read: 51; rows the predicate matched: 48
[agreement] Twins: credits role-shapes A, role-shapes B; no line cited for role-shapes B
findings: 1
```

The three rows it reads and does not match hold a dash in "Both runs": they record where the runs differ.

Revised 2026-10-17, the debt round: the probe's revision reads its "re-measured here" exemption from the
crediting cell (`build/2026-10-16-build-PLAY-dClosedLoop-1-debt-reviews-compared-instruments.md`,
`[probes-expansions]`). Re-run here with that change and this record's five systems:

```text
rows read: 51; rows the predicate matched and checked: 48; exempt, their crediting cell re-measured: 0
findings: 0
```

Revised 2026-10-17, the folds' closing review: the probe now reads each table by the renderer's grammar, so an indented or pipe-less row is
read and checked (`memory/builds/dClosedLoop/build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews-instruments.md` `[probes-final]`). Re-run here, it reads the same 51 rows, 48 checked, with no finding.

## [open] What the round owes

- **The audit.** Dispatch 86 returned CLEAN WITH FIXES, and its fold is mapped item by item in
  `build/2026-10-17-build-PLAY-dClosedLoop-1-final-reviews.md` `[fold-systems-retrofit]`. MS-2 goes
  back to the owner with `[ms2]`'s third run.

- The owner's answers to `[forks]`.
- Then the fold: v2's catalogue and presets gain the new keys, the register gains `[gaps-proposed]`, and
  the chain rows gain the units `[design]` names. Revised 2026-10-17: folded, the gaps registered as
  `gap-found-20` to `gap-found-23`, `gap-design-10`, `gap-mem-17` to `gap-mem-22`, `gap-roles-19`,
  `gap-roles-20`, `gap-rt-20`, `gap-rt-21` and `gap-review-11` to `gap-review-13`.
- A Tier-2 review of the round, at the owner's word.
