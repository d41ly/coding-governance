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
