# The loop definition, `tools/loop/loop.toml`

**What it is.** A governed build runs one loop of five steps: Plan, Design, Build, Test, Deploy. The
loop kit holds that loop as data in one file, `tools/loop/loop.toml` in this repository, and every <!-- usage: entry:loop -->
tool that needs a step or a workflow's place reads it from there. The roles kit says who does the
work; this file says what runs and in which step.

## What the file holds

Five `[[step]]` rows, in order, one per step:

```toml
[[step]]
tag = "step.build"        # the step's tag
order = 3                 # its place in the loop
state = "building"        # the state a build holds while it is in the step
exit = "item.build.exit"  # the item that ends the step
```

And one `[[workflow]]` row per workflow of the roles kit, such as `spec-review`:

```toml
[[workflow]]
name = "spec-review"
order = 4                 # its build order, 0 for a workflow that runs at any time
step = "step.design"      # the step its work sits in, or "none"
reach = "review"          # optional: the word its work orders load practices under
```

A workflow's `order` is the `## Stage <n>` number `/build` walks it at, and the order the charter's
drive lines come in. Its reach word picks the practices a work order carries
([the practices at the work order's step](roles.md)): the
row's `reach` where it has one, else the last word of its `step`, else `none`. Only `entry` and
`review` are written as a `reach`, since neither is a step.

## How to use it

- **Read the loop:** `python tools/loop/loop_lib.py --check` prints one line per step and per <!-- usage: script:tools/loop/loop_lib.py 9755b4d6 -->
  workflow with its order, step and reach word, and exits 0.

  ```text
  loop: step step.build · order 3 · state building · exit item.build.exit
  loop: workflow spec-review · order 4 · step step.design · reach review
  ```

- **Check an install:** `bash tools/loop/adopt-loop.sh --check` runs the same read through the <!-- usage: script:tools/loop/adopt-loop.sh a5990311 -->
  resolved python. The kit renders nothing, so there is nothing to scaffold.
- **See a refusal:** `python tools/loop/loop_lib.py --fixture --plant reordered` reads the file with
  one break made in memory and exits 1 on the refusal it must draw. The cases are `missing-step`,
  `reordered`, `bad-step` and `bad-reach`; the file on disk is never changed.

## What stops a read

The reader refuses the whole file, naming the row, when the five steps are not all there once each
and in order, when a workflow is named twice, when an `order` is not an integer at or above 0, when
a `step` is absent or is neither a step tag nor `none`, or when a `reach` is neither `entry` nor
`review`. The `loop definition` gate runs the read on every push and landing.

The roles kit's `roles catalogue` gate joins the two files by workflow name, both ways: a workflow
in `workflows.toml` with no row here, or a row here naming no workflow there, is one `R6` line.

## Who owns it

The file is gov's and an update overwrites it: the steps and each workflow's place are not an
adopter's to seed. An install takes the loop kit with the roles kit, which requires it.
