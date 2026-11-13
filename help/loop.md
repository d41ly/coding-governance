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

The file also holds the one closed set of dispositions, the words that say where a request goes:

```toml
[dispositions]
set = ["continue", "amend", "new", "patch", "repeat", "unit", "breakpoint", "ask", "none"]

[[disposition-alias]]
word = "defer"            # a legacy word, no member of the set
means = "ask"             # the member it means
```

Three alias rows map older words onto members: `attach` means `amend`, `defer` means `ask`, and
`refuse-as-duplicate` means `continue` on the build the request duplicates. Three other vocabularies
look alike and are not this set: a review round's exit (`fold` or `promote`), the `class:`, `new:`,
`gate:` and `none` lines of a review finding, and triage's verdicts on a build in planning.

## The owner's disposition record

When the owner answers a held item, the answer is one record in the build's `build/` folder, written
by the memory-tree kit: <!-- usage: script:tools/memory-tree/build_records.py#new 3cae4d5e -->

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries a placeholder the shell reads as a redirect -->
```bash
python tools/memory-tree/build_records.py new disposition --build <slug> --unit <id> --item item.plan.exit --disposition continue --channel terminal --reason "<why>"
```

It writes `<date>-build-<unit id>-disposition-<n>.md` with the item, the one word of the answer, the
channel the owner answered on (`mailbox`, `terminal` or `prompt`), the reason where one is given, and
the unit. It writes nothing, and exits 1, when `--item` is no tag opening `item.`, when
`--disposition` is not one word, or when `--channel` is not one of the three. An item no unit owns is
recorded under the build's first unit.

Which words an item accepts is the item's own: a placing item takes the set above, and an owner gate
lists its own outcomes, such as `ratified` and `rejected`. The loop reader's
`check_disposition_record` joins a record to its item's outcomes and reads the word as written, so
write a member and never an alias. Until the item rows land in the file it answers `None` for every
item, which reads as unarmed and never as a pass.

## How to use it

- **Read the loop:** `python tools/loop/loop_lib.py --check` prints one line per step and per <!-- usage: script:tools/loop/loop_lib.py 9755b4d6 -->
  workflow with its order, step and reach word, then the dispositions and one line per alias, and
  exits 0.

  ```text
  loop: step step.build · order 3 · state building · exit item.build.exit
  loop: workflow spec-review · order 4 · step step.design · reach review
  loop: dispositions continue amend new patch repeat unit breakpoint ask none
  loop: disposition-alias defer · means ask
  ```

- **Check an install:** `bash tools/loop/adopt-loop.sh --check` runs the same read through the <!-- usage: script:tools/loop/adopt-loop.sh a5990311 -->
  resolved python. The kit renders nothing, so there is nothing to scaffold.
- **See a refusal:** `python tools/loop/loop_lib.py --fixture --plant reordered` reads the file with
  one break made in memory and exits 1 on the refusal it must draw. The cases are `missing-step`,
  `reordered`, `bad-step`, `bad-reach`, `disposition-unknown` (a word given twice in the set) and
  `disposition-alias` (an alias meaning no member); the file on disk is never changed.

## What stops a read

The reader refuses the whole file, naming the row, when the five steps are not all there once each
and in order, when a workflow is named twice, when an `order` is not an integer at or above 0, when
a `step` is absent or is neither a step tag nor `none`, when a `reach` is neither `entry` nor
`review`, when the disposition set is missing, empty or holds a word twice, or when an alias row's
`word` is a member or its `means` is not one. The `loop definition` gate runs the read on every push and landing.

The roles kit's `roles catalogue` gate joins the two files by workflow name, both ways: a workflow
in `workflows.toml` with no row here, or a row here naming no workflow there, is one `R6` line.

## Who owns it

The file is gov's and an update overwrites it: the steps and each workflow's place are not an
adopter's to seed. The loop kit is in the default selection, so a default install takes it, and
`update` installs it into a tree whose receipt predates it, as a default-gained kit. The roles kit
requires the loop kit: a `--kits` selection naming `roles` names `loop` too or is refused.
