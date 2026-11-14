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

## Witness classes

Every fact the loop reads as done has a witness, and every witness names its class. Three classes
count, because the agent doing the work cannot type them: `history` (a commit, its trailers, a file
at a commit, a ref), `hook-record` (a record a hook writes) and `remote-verdict` (a verdict the
remote's runner keys by tree). The fourth class, `actor`, is a fact the acting agent typed itself,
such as a status word or an attestation, and it is refused:

```toml
[witnesses]
classes = ["history", "hook-record", "remote-verdict"]
refused = ["actor"]

[[step]]
tag = "step.plan"
# ...
witness = { class = "history", by = "the transition record into the next step" }
```

Every `[[step]]` row carries a `witness`, and each step's exit is witnessed by its transition
record, class `history`.

The unattended driver's Definition of Done writes each entry as `<item>:machine` or `<item>:agent`.
Two `[[witness-alias]]` rows map those words onto classes: `machine` means `history` and `agent`
means `actor`. An entry with no `:<word>` is refused. It used to count as `machine` without saying so.

**The actor list.** The actor witnesses that still stand are rows of `tools/loop/actor-witnesses.txt`.
Each row is `<site>`, `<witness>` and `<build>`, separated by tabs, where the build is the one whose
computed witness replaces it. The list only shrinks: a row it did not hold at the compare base is
refused. The list holds two rows today, `keepalive-reaped` until dWellOiledMachine and
`parked-decisions-surfaced` until dShippedRelease, both from the driver's `DOD_CORE`. A row is also
refused when its build has no `memory/builds/<build>/README.md`, or when the witness it names is no
`actor` witness.

**Upgrading.** If your `.unattended.conf` declares a `DOD_EXTRA` entry with no class, check 53 of the
unattended leg refuses it, naming the entry. Append `:machine` or `:agent` to it. An `:agent` entry
also needs an actor-list row naming the build that computes its witness.

## The owner's disposition record

When the owner answers a held item, the answer is one record in the build's `build/` folder, written
by the memory-tree kit's record door, which [the charter page](charter.md) documents:

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

- **Read the loop:** `python tools/loop/loop_lib.py --check` prints one line per step and per <!-- usage: script:tools/loop/loop_lib.py 036bc6db -->
  workflow with its order, step and reach word, then the dispositions and one line per alias. Then it
  prints the witness classes, one line per witness alias and per step's witness, one line per
  actor-list row with its build, and the base it compared the list against, or `no comparison` and
  why. It exits 0, or 1 when the list is refused.

  ```text
  loop: step step.build · order 3 · state building · exit item.build.exit
  loop: workflow spec-review · order 4 · step step.design · reach review
  loop: dispositions continue amend new patch repeat unit breakpoint ask none
  loop: disposition-alias defer · means ask
  loop: witness classes history hook-record remote-verdict · refused actor
  loop: witness step.build · class history · by the transition record into the next step
  loop: actor witness DOD_CORE · keepalive-reaped · until dWellOiledMachine
  ```

- **Grade a Definition of Done:** `python tools/loop/loop_lib.py --grade-site DOD_CORE gates-green:machine keepalive-reaped:agent parked-decisions-surfaced:agent`
  prints one `loop: site` line per entry with its word and class, and `until <build>` on an actor
  entry. The site is `DOD_CORE` or `DOD_EXTRA`. It exits 1, with a `loop: refused` line, for an entry
  with no class word, for a word no alias holds, and for an actor entry the list does not hold. It
  also exits 1 for a list row of that site that no actor entry matches. Check 53 of the unattended leg
  runs it over the driver's `DOD_CORE` and your conf's `DOD_EXTRA`.

- **Check an install:** `bash tools/loop/adopt-loop.sh --check` runs the same read through the <!-- usage: script:tools/loop/adopt-loop.sh a5990311 -->
  resolved python. The kit renders nothing, so there is nothing to scaffold.
- **See a refusal:** `python tools/loop/loop_lib.py --fixture --plant reordered` reads the file with
  one break made in memory and exits 1 on the refusal it must draw. The cases are `missing-step`,
  `reordered`, `bad-step`, `bad-reach`, `disposition-unknown` (a word given twice in the set) and
  `disposition-alias` (an alias meaning no member). The witness cases are `witness-no-class`,
  `witness-bad-class`, `witness-actor-unlisted`, `witness-actor-listed` (which reads clean),
  `actor-list-grown`, `actor-list-stale` and `actor-list-no-build`. The files on disk are never
  changed.

## What stops a read

The reader refuses the whole file, naming the row, when the five steps are not all there once each
and in order, when a workflow is named twice, when an `order` is not an integer at or above 0, when
a `step` is absent or is neither a step tag nor `none`, when a `reach` is neither `entry` nor
`review`, when the disposition set is missing, empty or holds a word twice, or when an alias row's
`word` is a member or its `means` is not one. It also refuses a step with no `witness`, a witness with
no class or no `by`, and a class that is in neither witness list. The `loop definition` gate runs the read on every push and landing.

The roles kit's `roles catalogue` gate joins the two files by workflow name, both ways: a workflow
in `workflows.toml` with no row here, or a row here naming no workflow there, is one `R6` line.

## Who owns it

The file is gov's and an update overwrites it: the steps and each workflow's place are not an
adopter's to seed. The loop kit is in the default selection, so a default install takes it, and
`update` installs it into a tree whose receipt predates it, as a default-gained kit. The roles kit
requires the loop kit: a `--kits` selection naming `roles` names `loop` too or is refused. The
unattended kit requires the loop kit too, for check 53. The loop kit requires the memory-tree kit,
because `--check` reads the actor list at the compare base that kit resolves.
