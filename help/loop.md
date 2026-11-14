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

## Each step's program

Each step is a program of items, one `[[item]]` row per item, and `--check` prints how many each
step holds. A row names who does the work, what it waits for, what it reads, what it may
write, the words it can answer with, and where each answer goes:

```toml
[[item]]
tag = "item.plan.place"
step = "step.plan"
actor = "command:plan.place"             # <kind>:<name>, one actor
needs = ["item.plan.record"]             # the items it waits for
inputs = ["layer.memory:the plan record and the plan view"]
allowance = "the plan view"              # what it may write
returns = "record-kind.plan-view"        # the record kind it writes
outcomes = ["placed", "unplaced"]        # its closed set of answers
witness = { class = "history", by = "the placement predicate" }
owner = "dRankedPlan"
routes = { placed = "item.plan.lease", unplaced = "transition" }
```

A `needs` entry is one item, or a list of items where any one of them is enough:

```toml
needs = [["item.design.inventory", "item.design.reentry", "item.design.seams"]]
```

Each outcome has exactly one route. A route goes to another item, to `transition` when the build
moves to another step, or to `stand-in:{prefix}/<kit>/<file>`, the tool that does that work today
when the item that will do it belongs to a later build. `{prefix}` stands for the folder your kits
are installed under. Each input starts with a layer tag from the playbook kit's `layers.toml`, such
as `layer.memory` or `layer.flow`.

Each item has exactly one actor, one string. Its kind is `role`, `command`, `executor`, `hook` or
`owner`, written `<kind>:<name>`, or the bare word `executor` or `owner`. A list of actors, a comma
or a second colon is refused: an item done by different actors is one item per actor. A command,
executor, hook or owner item writes its own `inputs`, `allowance` and `returns`, and each must be
there and not empty.

A role actor names its role by the role file's stem, such as `role:gov-builder` for
`gov-builder.agent.md`. Its row leaves out `inputs`, `allowance` and `returns`, and takes them from
the role file in the roles kit: `inputs` from its `reads`, `allowance` from its `writes`, and `returns`
from its `returns`. If a role row writes one of them anyway with the role's own value, it is refused
as a copy. A role row may write `allowance = "none"` to narrow its role, and no other allowance.
A role the roles kit does not hold yet prints `pending`, and if the roles kit is not installed every
role item prints `unarmed`. Neither is refused, and neither counts as checked.

An item's instruction scope, the instruction units it loads, is never typed on its row. It is
derived from the units whose `scope` names the item; `--scopes` below prints it.

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
refused when the witness it names is no `actor` witness, or when its site is neither a step nor
`DOD_CORE`. A row whose build has no `<MEMORY_ROOT>/builds/<build>/README.md` is refused only in a
tree whose `.memory-tree.conf` sets `DESIGN_RECORD`, the tree that owns the chain's builds. Anywhere
else, `--check` prints each row ending `foreign build, not graded`, and says why on its builds line.

**Upgrading.** If your `.unattended.conf` declares a `DOD_EXTRA` entry with no class, check 53 of the
unattended leg refuses it, naming the entry. Append `:machine` or `:agent` to it. An `:agent` entry
is admitted and printed `adopter-declared`, because `DOD_EXTRA` holds your own items and the actor
list only governs the ones gov ships. Check 53's report line names each one.

## Computed witnesses

Some witnesses are computed by a tool rather than typed by the agent they judge. The file declares
each kind as a `[[computed-witness]]` row:

```toml
[[computed-witness]]
name = "acceptance"
serves = "item.build.acceptance"                    # the item it witnesses, or "none"
writer = "stand-in:{prefix}/loop/loop_witness.py"   # what writes it today
armed-by = "dWellOiledMachine"                      # the build that writes it for real
```

Three rows ship: `acceptance`, a unit's acceptance commands re-run at its commit; `probe-rerun`, a
probe's commands re-run at the commit it pinned, which serves `none` because its item belongs to a
later build; and `red-attribution`, the bar runner's attribution of each red leg, serving
`item.test.route`. A row has no `class`: its class is the witness class of the item it serves. `--check`
refuses a row whose name is not one word or is given twice, a `serves` that is neither `none` nor a
declared item, a served item whose witness class is `actor`, a `writer` that is neither a
`stand-in:` path nor an actor, and an empty `armed-by`.

The `acceptance` and `probe-rerun` witnesses are written today by `tools/loop/loop_witness.py`.
Each re-run checks the commit out into a temporary worktree, runs every command there through the
shell with the git location variables unset, and keeps its exit code and the first twelve hex digits
of the SHA-256 of its output. The worktree is removed afterwards, even after a failure. Output is
hashed exactly as printed, so a command that prints the time never re-runs equal.

<!-- run: no — needs a build folder and a committed unit in the adopter, which a scratch adopter does not hold -->
```bash
python tools/loop/loop_witness.py acceptance --build <slug> --unit <id> --sha <commit> --cmd "<command>" --cmd "<command>"
python tools/loop/loop_witness.py rerun --sha <pinned> --cmd "<command>" --expect <exit>:<hash>
```

- **`acceptance`** re-runs each `--cmd` at `--sha` and writes the record <!-- usage: script:tools/loop/loop_witness.py#acceptance 55bc486e -->
  `<date>-build-<unit id>-acceptance-<n>.md` in the build's `build/` folder, through the memory-tree
  kit's record writer, with `Writer: stand-in`, the full commit, and one
  `run · <exit> · <hash> · <command>` line per command. `--root` names the repository, the current one by default. It exits 2
  when no `--cmd` is given or `--sha` names no commit, and 1 when the writer refuses, writing nothing.
  Commit the record yourself. No flag types a run line: the record's lines are always computed.
- **`rerun`** pairs each `--cmd` with the `--expect` in the same place, and prints one line per <!-- usage: script:tools/loop/loop_witness.py#rerun 016ed8f7 -->
  command: `confirmed` when the exit and hash at the pinned commit match, `refuted` when either
  differs, and `inconclusive` on a timeout or a commit that does not resolve. It exits 0 only when
  every command is `confirmed`, and 2 on an unpaired `--cmd`.

**Holding on an inherited red.** `--hold --code inherited-red` in the unattended driver is admitted
only when the attribution record of the bar its `gates-run` fact names reads every red leg
`INHERITED`, as `--handoff --code owner-landing` already is. A close that prints the inherited-red hold
also records which paths it staged, so committing them before holding keeps the bar tied.

## Checklist handles and their items

The unattended driver names each Definition of Done item and each method directive by a handle,
such as `gates-green` or `reuse-first`, in its two core registries, `DOD_CORE` and `DIRECTIVES_CORE`.
The file maps every one of those handles onto the declared item whose witness the handle's check
reads, one `[[checklist]]` row each:

```toml
[[checklist]]
registry = "DOD_CORE"          # DOD_CORE or DIRECTIVES_CORE
handle = "gates-green"         # as the registry spells it before its first ":"
item = "item.test.verdict"     # the declared item whose witness the check reads
```

A row holds those three keys and no other, so it never stores a position: an item is reached by its
tag, and the registry's word order is only the order the driver shows. Several handles may map onto
one item, such as `item.deploy.record`.

- **Find a handle's item:** `python tools/loop/loop_checklist.py show reuse-probed` reads the rows <!-- usage: script:tools/loop/loop_checklist.py#show 8af12fd7 -->
  alone and prints the handle's registry and item. A handle no row maps exits 2.

  ```text
  DOD_CORE item.design.seams
  ```

- **Check the map:** `check` reads the two registry lines from the unattended driver and checks the <!-- usage: script:tools/loop/loop_checklist.py#check a625a5c2 -->
  rows both ways. It prints one `loop: checklist` line per row and a `loop: checklist-count` line per
  registry, and exits 0. It exits 1, naming the row, the handle or the key, when a core handle has
  no row, a row names a handle its registry does not hold, a handle has two rows, a row's item is no
  `item.<step>.<name>` tag the file declares, a row carries a key beyond the three, or a row's
  registry is neither core registry. It exits 2 when the driver is not installed, or a registry line
  is missing or empty, so it is never green over nothing. `check --selftest` runs `check`, every
  case below and `show`, and the `loop checklist tags` gate runs it on every push and landing.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and reads the unattended driver beside it -->
  ```bash
  python tools/loop/loop_checklist.py check
  python tools/loop/loop_checklist.py --fixture --plant missing-handle
  ```

  ```text
  loop: checklist DOD_CORE · gates-green · item.test.verdict
  loop: checklist-count DIRECTIVES_CORE · 17 handle(s) · 17 mapped
  ```

- **See a refusal:** `--fixture --plant <case>` runs `check` with one break made in memory and exits <!-- usage: script:tools/loop/loop_checklist.py d6167c09 -->
  1 on the refusal it must draw. The cases are `missing-handle` (a handle added to `DOD_CORE` that no
  row maps), `stale-row` (a row whose handle no registry holds), `two-rows` (a second row for
  `gates-green`), `undeclared-item` (a row mapping onto an item the file does not declare),
  `bare-item` (a row mapping onto an item tag without its `item.` opening), `numbered-row` (a row
  carrying a `number` key) and `bad-registry` (a row whose registry is `DOD_EXTRA`). The files on
  disk are never changed.

The check does not judge whether a pairing is the right item, which is a review's call, or whether a
handle's checker word agrees with its item's witness class. `DOD_EXTRA` and `DIRECTIVES_EXTRA`, your
own handles, are not mapped here.

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
write a member and never an alias. For an item the file declares it answers true, or refuses a word
outside that item's outcomes. For an item the file does not declare it answers `None`, which reads as
unarmed and never as a pass.

## How to use it

- **Read the loop:** `python tools/loop/loop_lib.py --check` prints one line per step and per <!-- usage: script:tools/loop/loop_lib.py 8a025e56 -->
  workflow with its order, step and reach word, then the dispositions and one line per alias. It
  prints one `loop: program` line per step, with its items in an order where each comes after the
  items it needs. Where the playbook kit is not installed, a `loop: inputs unarmed` line comes first
  and the inputs go unchecked. Then it prints one `loop: item` line per item, saying where each of
  its fields comes from, or `pending` or `unarmed`, and a `loop: items` count line. Then it
  prints the witness classes, one line per witness alias and per step's and item's witness, one line per
  actor-list row with its build, and the base it compared the list against, or `no comparison` and
  why. A `loop: actor-list builds` line follows, naming the builds folder, or `foreign` and why, then
  one `loop: computed-witness` line per computed witness with the item it serves, its class, its
  writer and the build that arms it. It exits 0, or 1 when an item, the list or a computed witness is
  refused.

  ```text
  loop: step step.build · order 3 · state building · exit item.build.exit
  loop: workflow spec-review · order 4 · step step.design · reach review
  loop: dispositions continue amend new patch repeat unit breakpoint ask none
  loop: disposition-alias defer · means ask
  loop: program step.test · 10 item(s) · item.test.merge item.test.select item.test.verdict ...
  loop: item item.plan.place · command:plan.place · inputs from item · allowance the plan view from item · returns from item
  loop: item item.build.unit-pass · role:gov-builder · inputs from role:gov-builder · allowance product from role:gov-builder · returns from role:gov-builder
  loop: item item.design.inventory · role:gov-architect · pending · the roles kit holds no gov-architect role
  loop: items · 61 read · 9 pending · 0 unarmed
  loop: witness classes history hook-record remote-verdict · refused actor
  loop: witness step.build · class history · by the transition record into the next step
  loop: actor witness DOD_CORE · keepalive-reaped · until dWellOiledMachine
  loop: computed-witness acceptance · serves item.build.acceptance · class history · writer stand-in:{prefix}/loop/loop_witness.py · armed by dWellOiledMachine
  ```

- **Grade a Definition of Done:** `python tools/loop/loop_lib.py --grade-site DOD_CORE gates-green:machine keepalive-reaped:agent parked-decisions-surfaced:agent`
  prints one `loop: site` line per entry with its word and class, and `until <build>` on an actor
  entry. The site is `DOD_CORE` or `DOD_EXTRA`. It exits 1, with a `loop: refused` line, for an entry
  with no class word and for a word no alias holds. The list joins `DOD_CORE` alone: there it also
  exits 1 for an actor entry the list does not hold, and for a list row that no actor entry matches.
  A `DOD_EXTRA` actor entry is admitted, its line ending `adopter-declared, not on the shipped list`.
  Check 53 of the unattended leg runs it over the driver's `DOD_CORE` and your conf's `DOD_EXTRA`.

- **See each item's scope:** `python tools/loop/loop_lib.py --scopes` checks the file as `--check` does,
  then prints one line per item with the instruction units scoped to it. It runs the playbook kit's
  `load_sets.py derive` once per item, so it takes some seconds, and `--check` does not run it.

  ```text
  loop: scope item.plan.record · item — 0 unit(s) · none
  ```

  Where the playbook kit is not installed, every line says `unarmed` and names where it looked, and
  the command still exits 0. A `derive` that fails stops it with exit 1, naming the item.

- **Check an install:** `bash tools/loop/adopt-loop.sh --check` runs the same read through the <!-- usage: script:tools/loop/adopt-loop.sh a5990311 -->
  resolved python. The kit renders nothing, so there is nothing to scaffold.
- **See a refusal:** `python tools/loop/loop_lib.py --fixture --plant reordered` reads the file with
  one break made in memory and exits 1 on the refusal it must draw. The cases are `missing-step`,
  `reordered`, `bad-step`, `bad-reach`, `disposition-unknown` (a word given twice in the set) and
  `disposition-alias` (an alias meaning no member). The witness cases are `witness-no-class`,
  `witness-bad-class`, `witness-actor-unlisted`, `witness-actor-listed` (which reads clean),
  `actor-list-grown`, `actor-list-stale`, `actor-list-no-build` and `actor-list-foreign` (which reads
  the builds folder as foreign, prints each row `foreign build` and exits 0). The program cases are
  `needs-cycle`, `needs-unresolved`, `outcome-unrouted`, `route-unresolved`, `input-no-layer` and
  `exit-missing`. The actor cases are `actor-two` (two actors on one item), `actor-bad-kind`,
  `witness-missing` (an item with no witness), `allowance-missing` (a command item with no
  allowance), `role-copy` (a role item repeating its role's allowance), `role-widen` (a role item
  given a wider allowance), `role-pending` (a role the roles kit does not hold, which prints `pending`
  and exits 0) and `roles-no-kit` (the roles kit looked for in an empty scratch folder, so every role
  item prints `unarmed` and it exits 0). Two cases run `--scopes` after the read and exit 0 when it behaves:
  `scope-selected` scopes one unit to one item in a scratch file and shows it on that item's line
  alone, and `scope-no-kit` looks for the playbook kit in an empty scratch folder and shows every line
  `unarmed`. The computed-witness cases are `computed-actor` (the item the `acceptance` row serves
  given the `actor` class) and `computed-unserved` (the row serving an item the file does not
  declare). The files on disk are never changed.
- **Check the re-run stand-in:** `python tools/loop/loop_witness.py --fixture --plant acceptance` runs <!-- usage: script:tools/loop/loop_witness.py 6de87be4 -->
  one case in a scratch repository and exits 0 when it holds. The cases are `acceptance` (a unit's
  commands re-run at its commit while an uncommitted edit sits beside them), `acceptance-malformed`
  (records typed by hand, with no run line or a writer outside `executor` and `stand-in`, each read
  as malformed), `probe-rerun` (`confirmed` at the pinned commit, `refuted` at a later one,
  `inconclusive` at one that does not resolve) and `hold-inherited`, which preflights a run through
  the unattended driver and holds it under `inherited-red` over an `OWN` leg, an untied bar and an
  `INHERITED` one. `--selftest` runs every case and the two computed-witness cases above, and the
  `loop computed witness` gate runs it. A case whose kit is not installed exits 2, never a pass.

## What stops a read

The reader refuses the whole file, naming the row, when the five steps are not all there once each
and in order, when a workflow is named twice, when an `order` is not an integer at or above 0, when
a `step` is absent or is neither a step tag nor `none`, when a `reach` is neither `entry` nor
`review`, when the disposition set is missing, empty or holds a word twice, or when an alias row's
`word` is a member or its `means` is not one. It also refuses a step with no `witness`, a witness with
no class or no `by`, and a class that is in neither witness list. For the item rows it refuses a tag
that does not start `item.` and a step word, an item declared twice, a need naming no item, a cycle
of needs (each cycle named once), an empty outcome list or one with a word twice, an outcome with no
route or a route for no outcome, a route to anything but an item, `transition` or a stand-in, an
input whose layer tag is not in `layers.toml`, and a step whose `exit` is not one of its own items.
It refuses an item with no `witness`, as it does a step. `--check` also refuses an actor that is not
one string of a known kind, a non-role item missing its `inputs`, `allowance` or `returns`, and a
role item that copies its role or writes an allowance other than `none`.
The `loop definition` gate runs the read on every push and landing.

The roles kit's `roles catalogue` gate joins the two files by workflow name, both ways: a workflow
in `workflows.toml` with no row here, or a row here naming no workflow there, is one `R6` line.

## Who owns it

The file is gov's and an update overwrites it: the steps and each workflow's place are not an
adopter's to seed. The loop kit is in the default selection, so a default install takes it, and
`update` installs it into a tree whose receipt predates it, as a default-gained kit. The roles kit
requires the loop kit: a `--kits` selection naming `roles` names `loop` too or is refused. The
unattended kit requires the loop kit too, for check 53. The loop kit requires the memory-tree kit,
because `--check` reads the actor list at the compare base that kit resolves, and reads
`DESIGN_RECORD` and `MEMORY_ROOT` through that kit's conf reader. `--check` also reads the roles
kit's role files for the role items' defaults, without requiring that kit: where it is not
installed, each role item prints `unarmed`. `loop_witness.py` writes its records through the
memory-tree kit, and its `hold-inherited` case runs the unattended driver without requiring that kit,
since the unattended kit requires this one; its gate is gov's own and an install does not carry it.
`loop_checklist.py` reads the unattended driver's two registry lines the same way, and its
`loop checklist tags` gate is gov's own too.
