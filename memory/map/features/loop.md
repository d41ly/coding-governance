# loop — the loop's definition: the gov steps, and where each workflow sits in them

```toml
feature = "loop"
title = "The loop definition: the five gov steps as data, each roles workflow's build order, step and reach word, and the one reader every other kit takes them from"
status = "building"
streams = ["tooling"]
decisions = ["TOOL-dDeclaredLoop-1"]

[claims]
gate-legs = ["loop definition", "loop computed witness", "loop checklist tags", "loop transition tables"]
kits = ["loop"]
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = ["tools/loop/**", "help/loop.md"]
```

No kit declared the stage it served, and the loop existed only as an integer column in the roles
kit's workflow table (`gap-spine-01`). This kit writes the loop down once: `loop.toml` holds the five
gov steps and one row per roles workflow, and `loop_lib.py` is its one reader. The roles kit's
`stage` and `step` keys moved here in the unit that made the kit, and their readers were re-pointed
in the same unit: the roles catalogue checker and adopter, the playbook's drive section and its
load-set check (TOOL-dDeclaredLoop-1).

## Constraints & why

**The loop kit owns WHAT runs and in which step; the roles kit keeps WHO.** A kit with no agent in it
reads its step here without depending on the roles kit. The harness stage keys of the roles
workflow table map a harness stage to a role slot, which is WHO, and stay there.

**One home per fact.** A workflow's order and step are written in `loop.toml` alone. The roles
catalogue refuses a `stage` or `step` key as unknown, and joins its workflow names with the loop's
rows both ways, so neither file can name a workflow the other lacks.

**A step tag and a reach word are two facts.** `step` says where a workflow's work sits in the loop
and is a gov step tag or `none`. The reach word says which reach of each practice its work orders
load; `entry` and `review` are no gov step, so they are written as `reach` on the three rows where
the word is not the step's own.

**The gov steps are closed in the reader.** `STEP_TAGS` names the five, and a definition missing
one, repeating one or holding them out of order is refused whole. A reader that took rows in file
order would let a reordered file reorder every consumer.

**The requires edge runs roles to loop, never back.** The loop kit requires nothing. The playbook
kit declares no edge: with no loop kit its drive rows keep kit and row order and a work order's
reach reads unarmed.

## Shared seams

- `loop_lib.load_loop` and `check_loop` — the read and the row checks every other function goes
  through; `check_loop` takes parsed data, so a plant is made in memory.
- `resolve_kit_dir("loop", "loop_lib.py", <here>)` followed by an import — how a sibling kit reaches
  the reader: `roles_lib.read_workflow_order` and the playbook's `load_loop_kit`.

## Reuse affordance

seam: `loop_lib.read_steps` — reuse for any tool that needs the gov steps, their order, state or exit
item; extend via a new key on the `[[step]]` row graded in `check_loop`, never a second step list.

seam: `loop_lib.read_workflow_order` — reuse for anything that sorts or numbers work by workflow;
extend via a new key on the `[[workflow]]` row and a reader beside this one.

seam: `loop_lib.read_workflow_reach` — reuse for picking what a role's work order loads at its step.

## Gaps

- The `exit` items are named and not yet rows: nothing checks that an item a step names exists.
- The phase-and-stage mapping of unattended's run positions onto build states is design data in the
  unit's spec, section 4, and no file here carries it.
- An unknown key on a row is neither read nor refused.
