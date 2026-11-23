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
from its `return`, the role's typed return template, such as `outcome:committed|returned, commit:sha?`.
If a role row writes one of them anyway with the role's own value, it is refused
as a copy. A role row may write `allowance = "none"` to narrow its role, and no other allowance.
A role the roles kit does not hold yet prints `pending`, and if the roles kit is not installed every
role item prints `unarmed`. Neither is refused, and neither counts as checked.

An item's instruction scope, the instruction units it loads, is never typed on its row. It is
derived from the units whose `scope` names the item; `--scopes` below prints it.

Four more fields say how an item's loops end, and the termination check below reads them. Each is
optional, and each is fixed, so your overlay can set them on its own rows but never patch gov's:

```toml
draws = { fail = "fix-pass" }            # a route that draws on the rework budget, by its cause
waits = ["waiting"]                      # the outcomes on which it waits on another party
deadline = "policy.flow.wait-ceiling"    # whole hours, or policy.<key> of a deadline
on-deadline = "refused"                  # the outcome it takes once the deadline passes
```

A `draws` cause is one of `route-back`, `fix-pass`, `review-round`, `re-dispatch` and `research`. An
item with `waits`, or with an owner actor, declares both `deadline` and `on-deadline`, and its
`on-deadline` is an outcome outside `waits`.

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
A tree whose two confs name two records roots prints each row `foreign build, not graded` too, its
builds line carrying the `records root:` reason.

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
Each re-run checks the commit out into a temporary worktree, runs every command there as
`bash -c "<command>"` with the git location variables unset, `GIT_OPTIONAL_LOCKS=0` set and no
inherited `PWD`, as the run-gates kit's regeneration runs its commands, and keeps its exit code and the
first twelve hex digits of the SHA-256 of its output. Bash runs every command, on Windows too, so a
criterion's `[[ ]]` and pipes work as written; where no bash can be found the re-run is refused.
Output goes to a file, never a pipe, so a command that leaves a background process behind cannot
keep the re-run waiting. A command that runs past its time limit is recorded as `timeout`, and after
every command, timed out or not, the processes it started are stopped before its output is read: on
Linux and macOS its whole process group, a background process included; on Windows the process tree
Windows records, which does not reach a process Git Bash started in the background once its own bash
has exited, so such a survivor is the stated limit there, and the worktree it holds is named as
leaked. The worktree is removed afterwards, even after a failure, and one
still on disk is named on stderr as `loop-witness: leaked <path>`. Before it is hashed, the output
is normalised by the run-gates kit's program, its `write_normaliser`, run once in bash in the
worktree: it strips the worktree's path, its real path, the worktree as bash's `pwd` prints it (under
Git Bash a `/tmp/` path) and the repository's path, each in its forward-slash, backslash and `/c/`
spelling, then `tmp.` directory names, durations such as `1.5s` or `20ms`, carriage returns and
trailing spaces. So a command that prints its working directory or how long it took re-runs equal,
while one that prints the time of day still does not. Where the run-gates kit is not installed, or
the normaliser fails, the re-run is refused with `witness: normaliser unavailable — <reason>`.

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
  differs, and `inconclusive` on a timeout, a commit that does not resolve or a refused re-run, whose
  reason it prints on stderr as `loop-witness: inconclusive · <reason>`. It exits 0 only when
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

## Transition tables

A build moves between states only along a declared row. The file holds one table per level, build,
feature and unit, as `[[transition]]` rows, and the states of each level in `[states]`:

```toml
[states]
build = ["planning", "designing", "building", "testing", "deploying", "paused", "parked"]
feature = ["decomposed", "designed", "built", "tested", "deployed"]
unit = ["designed", "built", "tested", "deployed"]
terminal = ["landed", "withdrawn", "superseded", "incomplete", "deferred", "retired", "refused", "merged", "answered"]
feature-terminal = ["deployed"]
unit-terminal = ["deployed"]

[[transition]]
level = "build"           # build, feature or unit
from = ["planning"]       # the level's states, "none" for its entry, or "@open" for every open state
item = "item.plan.exit"   # the item whose outcome fires the row, by tag
outcome = "recorded"      # one word of that item's closed outcome set
to = "designing"          # a state, "@prior" or "@reentry"
witness = "the transition record"
# disposition = "new"     # optional: the move's disposition fact must be this member
# when = "before-push"    # optional: the row holds only while the landing is unpushed
```

A row names its item by tag, never by a position; `check` prints each table's row and state counts.

`terminal` is not a level. It lists a build's terminal states, where a build ends: a build row may
enter one, and no row may leave one, so a move asked from landed is refused. Five rows enter one
today: triage's refuse enters refused, the Deploy exit's closed enters landed, and the owner's request
to close the build, withdrawn or superseded, enters that state from any open state while the landing
is unpushed. The close request has no item row of its own yet, so it is a stand-in:

```text
item.life.close · withdrawn → withdrawn · superseded → superseded · stand-in dWellOiledMachine
```

`feature-terminal` and `unit-terminal` are not levels either. Each lists where a feature or a unit
ends, `deployed`, which is also one of that level's own states: no feature or unit row may leave it,
written by name or through `@open`, which holds it. Every level declares its set, and `check`
refuses a level that does not.

No row enters incomplete, deferred, retired, merged or answered yet: those rows belong to later units
and builds.

- **Ask for a move:** `python tools/loop/loop_table.py move --level build --from planning --item item.plan.exit --outcome recorded` <!-- usage: script:tools/loop/loop_table.py#move a9f6141c -->
  answers from the rows alone, with one of three answers:
  - `move` with the state it enters, exit 0, and `stand-in <owner>` after it when the item's own
    build has not landed yet, so a fixture witness stands in for it. A build move ends with its
    direction: `forward` into a later step or a terminal, `backward` into an earlier step, testing
    to building say, and `lateral` into or out of a state with no step, such as paused. The direction
    is worked out from the steps' order every time, never typed into a row;
  - `refused`, exit 1, when no row holds the move, for instance a build in planning asking to leave
    on Design's exit: stage order alone never admits a move;
  - `unanswered`, exit 2, when the level or state is unknown or a fact the row needs is missing.

  Some rows read facts, each passed as `--fact k=v`. A row entering `@prior`, the resume after a
  pause, takes `prior`, the state the pause left. The re-entry row, written with item `@any`, takes
  `reenters`, the item being re-entered, and enters that item's step's state; it holds only before the
  landing push, so it takes `pushed`, `yes` or `no`. A row with a `disposition` takes `disposition`.
  None of them defaults.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/loop_table.py move --level build --from planning --item item.plan.exit --outcome recorded
  python tools/loop/loop_table.py move --level build --from paused --item item.life.request --outcome resume --fact prior=testing
  python tools/loop/loop_table.py move --level build --from building --item @any --outcome admitted --fact reenters=item.plan.input --fact pushed=no
  ```

  ```text
  move — build · planning → designing · item.plan.exit · stand-in dRankedPlan · forward
  move — build · paused → testing · item.life.request · stand-in dWellOiledMachine · lateral
  move — build · building → planning · @any · backward
  ```

- **Check the tables:** `check` prints one `loop: table` line per level with its row and state <!-- usage: script:tools/loop/loop_table.py#check 0011b11d -->
  counts, one `loop: terminal <level>` line per level naming its terminal states, the build's first and
  `loop: terminal unit · deployed` among them, one `loop: owed` line per owed
  row and one `loop: stand-in` line per stand-in, and exits 0. It exits 1, naming the row, on a level
  missing its terminal set, a row leaving a terminal of its own level, a terminal also listed as an open build state, a state the level does not declare, two rows for one move, an
  item that is no tag or resolves to nothing, an outcome outside its item's set, or a disposition
  outside the set. It also joins every item's cross-step routes, an outcome sent to `transition` or
  to an item of another step, with the build table both ways: a route with no row, a row on no
  route, and a row entering another state than the routed item's step are each refused. It exits 2
  when the file holds no transition row, so it never admits a move over nothing. `check --selftest`
  runs `check`, every case below and each kind of answer, and the `loop transition tables` gate
  runs it on every push and landing.

- **The owed rows:** some cross-step routes enter states other units' or builds' rows write, such as
  placement's unplaced. Each stands on an `[[owed-row]]` naming its item, outcome and the unit or
  build that writes the row, and `check` prints it. The list only shrinks: once a row covers a route,
  its owed row is refused as stale until it is deleted.

- **The stand-ins:** every row item is a stand-in until its own build lands, each a `[[stand-in]]` row
  naming the item and its owner. The owning build deletes its row in the landing that arms the item's
  witness. A stand-in row for an item no row names, or naming another owner than the item declares,
  is refused.

- **See a refusal:** `--fixture --plant <case>` runs `check` with one break made in memory and exits <!-- usage: script:tools/loop/loop_table.py 6513b6ba -->
  1 on the refusal it must draw. The cases are `bad-state` (a row entering reviewing), `two-rows` (a
  second row for building's exit), `bad-exit` (rows naming the bare plan.exit, an undeclared item and
  an outcome outside the item's set), `dropped-row` (the building exit's row deleted while its route
  stays), `unrouted-row` (a row on an outcome routed inside its own step), `owed-stale` (an owed row a
  build row covers), `stand-in` (a stale and a mis-owned stand-in row), `terminal-from` (a row leaving
  landed), `terminal-open` (landed added to the open states), `unit-terminal-from` (a unit row from
  `@open`, so leaving deployed) and `level-no-terminal` (`unit-terminal` taken out of `[states]`). The
  files on disk are never changed.

The tables do not judge whether a move's witness holds, which is the writer's precondition, or
whether a state is reachable or a cycle terminates. The feature and unit rows are not joined to the
routes, and a feature's state, its least-advanced unit's, is the mover's call.

## Which state and step each run phase reads

An unattended run moves through phases, `PREFLIGHT` to `LANDED` or `ABORTED`. The file maps each one
to the build state and step it stands for, one `[[phase]]` row per phase of the driver's `PHASES_CORE`:

```toml
[[phase]]
phase = "REVIEWING"
step = "step.design"        # its state is the step's, designing, never typed here

[[phase]]
phase = "ABORTED"
state = "withdrawn"         # a phase with no step names its state: a build state, a terminal or "none"

[[phase]]
phase = "ABORTED"
halt-code = "budget-exhausted"
state = "incomplete"
```

A row may add qualifiers, `halt-code`, `hold-code` and `ending`, matched against the run's facts of
those names: an aborted run whose rework budget ran out reads incomplete, and a run held for the
owner's decision whose budget ending is `park-for-owner` reads parked. Every other aborted run reads
withdrawn, and every other held run paused. That paused row reads the step `held-in`: a held run reads the
step of the phase it was held from, which the driver writes as the run's `held-from` fact at the hold, so
`--fact held-from=BUILDING` reads `step step.build`, and with no such fact the step reads `none`. Only the
`HELD` row may read `held-in`.

- **Read a phase:** `python tools/loop/loop_table.py phase --from REVIEWING` prints the phase's state <!-- usage: script:tools/loop/loop_table.py#phase 01f88f39 -->
  and step. Each `--fact k=v` qualifies the `--from` phase. With `--to <PHASE>` it also names the step
  exits the move between the two crosses, in step order, or `none`; a move out of `PREFLIGHT`, which
  has no step, counts from the first step, so it crosses the plan step's exit. A phase with no row
  is refused by name, exit 1. An adopter phase, a member of PHASES_EXTRA, has no row in the loop kit's
  phase map: named in `--extra "<phases>"`, as the driver passes it, it reads state none and step none,
  marked `adopter phase`, a move into it crosses no step exit, and a move out of it counts from the
  first step, as a move out of PREFLIGHT does.
  Run without --extra, the phase verb reads PHASES_EXTRA from the .unattended.conf at the top of the work tree
  it runs in, sourced in bash as the driver sources it; a conf that does not source refuses the reading of a
  phase the map holds no row of, and a phase the map holds a row of never reads the conf.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/loop_table.py phase --from ABORTED --fact halt-code=budget-exhausted
  python tools/loop/loop_table.py phase --from HELD --fact held-from=BUILDING
  python tools/loop/loop_table.py phase --from SPECCING --to BUILDING
  python tools/loop/loop_table.py phase --from STAGING --to BUILDING --extra STAGING
  ```

  ```text
  phase ABORTED · state incomplete · step none
  phase HELD · state paused · step step.build
  phase SPECCING · state designing · step step.design · to BUILDING · crosses item.design.exit
  phase STAGING · state none · step none · adopter phase · to BUILDING · crosses item.plan.exit item.design.exit
  ```

- **The check:** `check` prints `loop: phase map` with the row and qualified counts and joins the
  rows with the driver's `PHASES_CORE` both ways, refusing a phase with no row and a row naming a
  phase in neither `PHASES_CORE` nor the `PHASES_EXTRA` your `.unattended.conf` declares, so an adopter
  phase needs no row and a row for one is admitted. It refuses as well a row with both a state and a
  step or neither, `held-in` on any row but `HELD`'s, an unknown step or state, and two rows for one
  phase without qualifiers. Where the driver is not installed beside this kit, the join prints
  `unarmed` and grades nothing. The cases `phase-missing`, `phase-stale`, `phase-shape`,
  `phase-twice`, `held-in-elsewhere` and `phase-row-unknown` show each refusal.

- **The hold:** the driver's `--phase` asks this map which step exits a move crosses. When an owner
  gate sits at one of them and still reads `held`, the move is refused before anything is written,
  naming the gate and how to release it, as `--close` is held. A move that crosses no exit, or only
  exits no gate holds, goes through as before. Under the default `autonomy`, the only owner gate is the
  plan gate, which the authorization releases, so nothing new is held.

## When a parent build is withdrawn

A build whose README front matter names `parents:` depends on them. When a parent is withdrawn, the
policy key `deps.on-parent-withdrawn` says what the dependent build does, and the loop kit answers it
as a route. Until a parent's withdrawal is posted, a parent reads withdrawn when its run-state file,
`RUN.md` in its build folder, holds a `phase` that the definition's phase rows map to the state
`withdrawn`, read with its `halt-code` and `hold-code` where set: `phase: ABORTED` does, but an
`ABORTED` parent halted `budget-exhausted` reads `incomplete` and fires no route. The file is read
where the parent's run branch publishes it, at `refs/remotes/<remote>/<run-branch>`, the branch
named by the `run-branch:` fact of your tree's copy, so a parent that aborted on its own node is seen
once you fetch; otherwise your tree's copy is read. A parent with no run-state file anywhere prints
`parent <p> · not withdrawn (no run record)` before the route, and a phase no row maps exits 2
naming the parent.

- **`replan`**, the default: the build goes back to planning by the parent row, which moves a build in
  designing, building or deploying on `item.deploy.parents`'s withdrawn.
- **`adopt-parent-work`**: the same move, and the route names each withdrawn parent's kept branch tip,
  the commit its `run-branch:` fact names, else `branch-ref:`, as the input your design inventory takes
  the parent's kept units from. A parent with neither fact, or a ref naming no commit, exits 2
  `no kept branch`.
- **`withdraw-too`**: the route proposes the build's withdrawal to you as an owner item and moves
  nothing. Only your disposition record withdraws it.

In testing or planning, which the parent row does not admit, the route answers `held` and the build
waits for its next row.

- **Ask for the route:** `python tools/loop/loop_parents.py route --build <slug> --state <state>` <!-- usage: script:tools/loop/loop_parents.py#route c1e3f183 -->
  reads the build's parents in the repository at `--root`, the current directory by default, and the
  policy value at the landed revision, and prints one answer. It writes nothing: you record the move,
  or file the owner item, yourself.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/loop_parents.py route --build tChild --state designing
  ```

  ```text
  route replan · parent tParent · move designing → planning · item.deploy.parents
  route adopt-parent-work · parent tParent · move designing → planning · item.deploy.parents
  inventory tParent <sha>
  route withdraw-too · parent tParent · owner-item · propose item.life.close withdrawn · left by record-kind.disposition
  route replan · parent tParent · held: testing admits no parent row
  route none
  ```

  It prints `route none` when no parent reads withdrawn or the README has no `parents:` key. It exits
  2 on a `parents:` slug naming no build folder, a state outside the build's open states, a policy
  value outside the key's set, or no kept branch, and 2 `unarmed` where the policy kit is not
  installed beside the loop kit, never falling back to a default.

- **See it on a scratch repository:** `--fixture --plant <case>` builds a scratch repository holding a <!-- usage: script:tools/loop/loop_parents.py 5ff32d7b -->
  child build and its parent, runs the route there, prints whether the tree changed, and removes it.
  The cases are `withdrawn-parent` (the parent aborted, its kept branch present), `no-kept-branch`
  (aborted, its kept branch deleted), `live-parent`, `no-parents`, `incomplete-parent` (aborted,
  halted `budget-exhausted`), `aborted-on-run-branch` (building in the tree, aborted at its run
  branch's tracking tip), `no-run-record` (no `RUN.md` at all) and `parent-in-extra-phase` (the parent
  in `STAGING`, an adopter phase the scratch's own `.unattended.conf` declares, read against the
  repository at `--root`, so the route is `route none`). `--value` commits the scratch's
  policy value and `--state` sets the child's state, `designing` by default. `--selftest` runs every
  case, and gov's own `loop parent routes` gate runs it.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/loop_parents.py --fixture --plant withdrawn-parent --value adopt-parent-work
  python tools/loop/loop_parents.py --selftest
  ```

The route does not read a parent's planning ending, such as refused or deferred, or a parent held
past its wait ceiling, and a parent aborted for a reason it later resumes from reads withdrawn until
its next run.

## Recording a build's move

When a build moves from one stage to the next, the move is recorded in up to three places, and the
policy key `transitions.record` in `.governance/policy.toml` says which:

- **`trailer`**: the move's commit carries
  `Gov-Transition: <from> -> <to> · build=<slug> · item=<tag> · sha=<sha8>`, with any extra field, such
  as `stand-in=<owner>`, `composition=<sha8>`, `scenario=<tags>` and `scenario-settled=<entries>`,
  after it. The rework budget's `budget=` and `draw=` are derived fields too: the writer adds them,
  and a `--field` giving either is refused.
- **`log`**: a record in the build's `build/` folder, `<date>-build-<id>-transition-<n>.md`, holding
  the same fields as `- **Build:**`, `- **From:**`, `- **To:**`, `- **Item:**` and `- **Sha:**` lines,
  where `<id>` is the lowest unit id a spec under the build defines.
- **`micro-format`**: the line `transition — <slug> · <from> → <to> · <item tag> · <sha>`, printed
  after the commit for your final message, and never stored.

All three are on by default. To opt out of a channel, set the ones you keep; the set is never empty,
and a file setting `[]` is invalid:

```toml
[transitions]
record = ["trailer", "micro-format"]
```

The trailer is the source: the log record is held to it field by field. With `trailer` opted out, the
log record is the source; with only `micro-format` selected, nothing is stored and the check says
`unstored`.

- **Record a move:** `python tools/loop/loop_transition.py record --build <slug> --from <state> --item <tag> --outcome <o> --witness <sha>` <!-- usage: script:tools/loop/loop_transition.py#record 51794820 -->
  answers the move from the build's transition table first, so a move no row holds prints `refused`
  and exits 1 writing nothing. The witness is the commit the exit item's witness was read at, HEAD or
  an ancestor of it. It refuses, exit 2, when your index holds staged changes, since the move's commit
  carries its own records alone. `--fact k=v` passes a fact a row reads, `--field k=v` a registered
  extra field, and `--root` the repository, the current directory by default.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries placeholders the shell reads as redirects -->
  ```bash
  python tools/loop/loop_transition.py record --build <slug> --from planning --item item.plan.exit --outcome recorded --witness HEAD
  ```

  ```text
  loop: wrote memory/builds/<slug>/build/<date>-build-<id>-transition-1.md
  loop: recorded · planning -> designing · forward · commit <sha8>
  transition — <slug> · planning → designing · item.plan.exit · <sha8>
  ```

  A move made before the build has its first spec writes the trailer and no record; the next move
  after the first spec writes the missing records first, in move order.

  A backward move, such as testing back to building on a code miss, is recorded through the same
  writer and channels as a forward one, with the same trailer fields and record lines, and the check
  holds it the same way. The `loop: recorded` line names the move's direction, `forward`, `backward`
  or `lateral`; it is worked out from the steps' order when printed or read, and never stored in the
  trailer or the record.

- **Check a build's moves:** `check --build <slug>` holds each log record to its move's trailer, names <!-- usage: script:tools/loop/loop_transition.py#check 53beaa6b -->
  a record no trailer backs, and holds the `transition` definition in your `AGENTS.md` to the line the
  writer prints. It exits 0 clean and 1 on a finding, printing
  `pending — <n> move(s) before the build's first spec` while moves wait on a spec, or `unstored`
  where the set stores nothing. Both
  verbs exit 2 when `transitions.record` does not resolve, and 2 `unarmed` where the policy kit is not
  installed beside the loop kit, never falling back to a default.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries a placeholder the shell reads as a redirect -->
  ```bash
  python tools/loop/loop_transition.py check --build <slug>
  ```

- **See it on a scratch repository:** `--fixture --plant <case>` builds a scratch repository holding <!-- usage: script:tools/loop/loop_transition.py 930359dc -->
  the build `tFix`, records a move there, runs the check and removes it. The cases are `default`,
  `subset-trailer-line`, `subset-log`, `empty-set`, `log-drift`, `orphan-log`, `no-row`, `line-drift`,
  `pre-spec`, `field`, `backward-rows` (three moves forward and three back, each trailer and read
  printed with its direction) and `skip-backward` (the same six moves, the last one's record deleted,
  so the check names the move back that owes it). `check --selftest` runs every case, and gov's own
  `loop transition record` gate runs it.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/loop_transition.py --fixture --plant default
  python tools/loop/loop_transition.py check --selftest
  ```

Only build-level moves are recorded; nothing calls the writer yet, until the executor that moves a
build at each item boundary lands.

Each move is also a step boundary for the build's own changes, described next. Before it writes its
records, `record` runs two steps: on a forward move it holds the path the build walked against its
composition, printing `loop: path · ...` and filing a `flow-deviation` order per deviation; on a
forward or backward move it gives each pending change of the build its state row in the build's
`RUN.md`, which rides the move's commit and is cut back where the move does not record.

## A build's own changes to its flow

A role can change its own build's flow mid-build without moving any other build: it proposes a row
for its own build, and the change takes effect at the build's next step boundary, never inside the
step it was proposed in. A change that only adds applies there on its own and is recorded; one that
takes away or loosens waits for you, while the build carries on without it.

- **Propose a change:** `bash tools/unattended/unattended.sh --rescope <slug> --flow <tag> --act add --item <unit-id> --row <path> --reason <text>` <!-- usage: verb:unattended.sh:--rescope a2a815d5 -->
  records one proposal through the loop kit's `adapt.py propose`. `--act` is `add` (a new row of your
  own, tagged with `adopter`, no `edges`), `amend` (a patch row whose `edges` reads
  `amends=<gov tag>@<hash8>`), `supersede` (a replacing row whose `edges` reads
  `supersedes=<gov tag>@<hash8>`) or `exclude` (gov's tag as `--flow`, no `--row`). The row file holds
  exactly one table, such as `[[item]]`, whose `tag` is `--flow`. An `add`, `amend` or `supersede`
  writes one change record in the build's `build/` folder holding the row in a TOML fence, its `After`
  pinning the row's bytes; every act appends `rescope · flow <act> <tag>[ · change <record>] · reason
  <text>` to `RUN.md`. A field holding a line end or ` · `, an act its row's `edges` disagrees with, and
  a missing or extra `--row` are refused, writing nothing; the driver prints the loop kit's line.

  <!-- run: no — runs the driver over a live run's state file, which a scratch adopter does not hold -->
  ```bash
  bash tools/unattended/unattended.sh --rescope <slug> --flow item.build.adopter.lint-pass --act add --item <unit-id> --row lint-pass.toml --reason "the lint gate needs a pass item"
  ```

**What decides.** The policy key `flow.adapt` in `.governance/policy.toml` takes three values:

- `additive-recorded`, the default: an additive change applies at the next boundary, and a loosening
  one waits for you.
- `owner-approves`: every change waits for you.
- `off`: every change is refused at the boundary.

The class is derived, never typed: an `add` is additive, and so is an `amend` whose every operation
the composition reads as narrowing; an `exclude`, a `supersede` and an `amend` with any widening
operation are loosening. At the boundary each pending change is composed with the build's applied
changes first, so a change the composition refuses, whose record's pin no longer matches its row, or
whose kind the compose verb answers unarmed is refused with `class none`. Each answer is a row in
`RUN.md`: `rescope · flow-state <tag> · applied|held|refused · class <class> · flow.adapt <value>`.

**Releasing a held change.** A held change waits until you write a disposition record whose `Item` is
the change's tag, as [the owner's disposition record](#the-owners-disposition-record) describes:
`continue` applies it at the next boundary and `none` refuses it, and the state row names the record.
The build's moves still record while a change is held.

**Where the changes go.** A build's applied changes are the last layer of its composition, after the
rows its scenarios activate: the position engine composes them through `compose --rows -`, an added or
replacing row as a row and an exclusion as an `{"exclude": "<tag>"}` element. A held, refused or
pending change is never part of it.

**The walked path.** On a forward move, where the driver hands the position engine its unit states in
`GOV_POSITION_STATES`, the writer reads the build's position and, for the step the move leaves, files
one order, `.governance/outbox/loop-flow-deviation-<build>-<item>.md`, per `skip`, an item of the step
the engine reads unheld but the step's exit, and per `extra`, an item a move out of that step named
that the composition lacks. An item whose witness the engine does not read is never a skip: the line
`loop: path · <build> · <step> · <n> unread` counts them. Without the hand-over, or where the position
reads another step, the line reads `loop: path · <build> · unread — <why>` and the move records.

- **See it on a fixture:** `python tools/loop/adapt.py --fixture --plant <case>` builds a scratch <!-- usage: script:tools/loop/adapt.py 36358c6c -->
  repository holding gov's kits and the build `tFix`, plays the case and ends `loop: fixture · <case> ·
  held` or `· MISSED <why>`. The cases are `additive`, `owner-approves`, `off`, `loosening`,
  `unrecorded-skip`, `act-mismatch`, `unit-row` and `mid-step`. `--selftest` runs every case, and gov's
  own `loop adapt fixtures` gate runs it.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/adapt.py --fixture --plant additive
  python tools/loop/adapt.py --selftest
  ```

## When a build moves to a newer composition

A build runs each step under the composition it entered that step with, and moves to a newer one only
at its next step boundary. An update to gov or a change to your overlay that lands mid-step never
changes what the build is doing until it records its next move.

**The pin.** Every move the writer records carries a `composition` field: the first eight hex digits of
the commit `HEAD` named when the move was recorded, as `composition=<sha8>` on the trailer and a
`- **Composition:**` line on the log record. The writer sets it; `--field composition=<value>` is
refused, exit 2, because the value is derived. The position engine reads the build's items at the pin
of its newest move, so `python tools/loop/position.py <slug>` lists `composition@<sha8> · pinned` among
its reads. A build whose newest move carries no pin, recorded before this field existed, or a build
with no move, reads the current `HEAD` and lists `composition@<sha8> · unpinned`; its next move pins it.

**An item that ended under a build.** When gov renames an item with a change record, a witness the
build holds under the old tag carries to the new one, as long as the record names exactly one
successor and the new composition holds it. Where the item was removed, or split into several, nothing
carries: at the build's next move the writer files one order, `.governance/outbox/loop-item-ended-<build>-<tag>.md`,
naming the build, the item, both revisions and the successors read, and prints
`loop: order · <path>`. Decide where that work goes. Where the composition at the move does not read,
the move records anyway and prints `loop: composition · unread · <why>`.

**A policy value naming a renamed boundary.** A tag-valued key such as `review.breakpoints` that names a
renamed item is read as its successor from the boundary the build moved at, so the breakpoint keeps
firing. Each redirected value files one order, `.governance/outbox/loop-policy-renamed-<key>-<tag>.md`,
asking you to re-pin the key in `.governance/policy.toml`, which only you edit.

- **See it on a fixture:** `python tools/loop/composition.py --fixture --plant <case>` builds a scratch <!-- usage: script:tools/loop/composition.py cd4da641 -->
  repository holding gov's kits, records a build's moves across a commit that re-tags an item, prints
  each observation and ends `loop: fixture · <case> · held` or `· MISSED <why>`. The cases are
  `rename`, `ended`, `split`, `policy-rename` and `unpinned`. `--selftest` runs every case, and gov's
  own `loop composition fixtures` gate runs it.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/composition.py --fixture --plant rename
  python tools/loop/composition.py --selftest
  ```

## Choosing a build's scenario

A build records what kind of work it is, and the flow it runs follows. That kind is a scenario: a row of
the `scenario` kind, `kind.scenario`, which says which request facts admit it, the step a build placed
under it enters at, and the rows of other kinds it activates for that build alone. Gov ships five, in
`tools/loop/scenarios.toml`:

- `scenario.feature`, admitted by the fact `entry=feature`, entering at `step.plan`;
- `scenario.amendment`, by `entry=amendment`, at `step.plan`;
- `scenario.patch`, by `entry=patch`, at `step.design`, the step a patch build enters;
- `scenario.playbook-run`, by `entry=playbook-run`, at `step.plan`;
- `scenario.design-only`, by `entry=feature` together with `design-only=true`; it extends
  `scenario.feature`.

None of gov's five activates a row or hands over to another, so a gov build's flow does not move.

**Admission.** A build is placed under every scenario whose facts all hold, in the composition's order,
gov's five before yours. Where none holds, it is placed under the default, `scenario.<value>` for the
value of `flow.scenario-default` in `.governance/policy.toml`, `feature` when unset. A default naming no
scenario the composition holds, one your `instructions.exclude` leaves out for instance, and a value the
policy kit refuses are each refused, naming the key and the value. A request's facts come from its
placement, where the scout names them and the check re-runs this selection (see "Placing a request"
below); `select` and the transition writer take them as `--fact <name>=<value>` flags.

**Your own scenario.** Add a `[[scenario]]` row to your overlay, `.governance/instructions.toml`, tagged
with `adopter` at its second segment. `extends` names the scenario whose facts, entry step, activated
rows and hand-overs it starts from, each key you set standing in place of the parent's whole. Its
`activates` holds, per kind tag, the rows it adds to that kind's composition for a build placed under
it, each meeting every refusal an overlay row of that kind meets:

```toml
[[scenario]]
tag = "scenario.adopter.mobile"
extends = "scenario.feature"
admits = { entry = ["feature"], platform = ["mobile"] }
entry = "step.plan"
activates = { "kind.item" = [ { tag = "item.test.adopter.device-farm", step = "step.test", actor = "command:device-farm", needs = ["item.test.verdict"], inputs = ["layer.flow:the verified tree"], allowance = "the farm's report", returns = "record-kind.device-farm", outcomes = ["done"], witness = { class = "history", by = "the farm's report" }, owner = "your-build", routes = { done = "item.test.exit" } } ] }
then = []
```

**Conflicts.** Two scenarios a build is placed under that set one field of one activated row to
different values conflict. Under `flow.scenario-conflict = "refuse"`, the default, the selection and the
move are refused, naming both scenarios, the row and the field. Under `"declared-order"` the later
scenario in the declared order wins, and the settlement `<row tag>:<field>:<winner>:<loser>` is recorded
on the move as `scenario-settled=<entries>`, so the record says which variant ran.

**The switch at a step boundary.** The transition writer records the scenarios on every move as
`scenario=<tags>`, joined by `+`; you never give it, and `--field scenario=...` is refused, exit 2. A
build's first move to carry the field places it from that move's facts. Every later move carries the
previous move's scenarios, and a scenario whose `then` holds `{ at = "<step>", scenario = "<tag>" }`
gives way to that scenario when the build leaves that step. Between boundaries the build reads its
scenarios' rows at its pin, so a change to a scenario landing mid-step reaches the build at its next
move, and two builds placed under different scenarios each read their own composition at once:
`python tools/loop/position.py <slug>` lists `scenario=<tags> · <n> activated` among its reads, `<n>`
the activated item rows. Where your tree has no scenario composition, the move records neither field and
prints `loop: scenario · unread · <why>`.

- **See where a request goes:** `python tools/loop/scenario.py select --fact entry=patch` prints the <!-- usage: script:tools/loop/scenario.py#select de95f97d -->
  scenarios on one line, one `loop: settled · <entry>` line per settlement and the facts it read. It
  exits 1 on a conflict under `refuse` or a refused default.
- **Check the scenarios:** `python tools/loop/scenario.py check` holds every scenario row, gov's pack <!-- usage: script:tools/loop/scenario.py#check eb5f8807 -->
  and yours: its keys, its parent, its facts, its entry step, the kinds it activates (every kind the
  register lists with a schema but the scenario kind itself), its hand-overs, the parent and hand-over
  chains free of cycles, and each activated kind's composition with its rows. It prints each refusal as
  `loop: refused · <scenario> · ...`, then `loop: scenarios composed · <n> scenario(s) · <m> repository`,
  and exits 2 `unarmed` where the playbook or policy kit is not installed beside the loop kit.
- **See it on a fixture:** `python tools/loop/scenario.py --fixture --plant <case>` builds a scratch <!-- usage: script:tools/loop/scenario.py 0cdf3527 -->
  repository holding gov's kits, plants the case and ends `loop: fixture · <case> · held` or
  `· MISSED <why>`. The cases are `two-builds`, `drops-stage`, `reorders-stage`, `replaces-stage`,
  `conflict`, `conflict-ordered`, `bad-default`, `default-excluded`, `then`, `mid-step-switch`,
  `derived-field`, `then-cycle` and `extends-cycle`. `check --selftest` runs `check` and `select` over
  your tree, then every case, and gov's own `loop scenario fixtures` gate runs it.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/scenario.py select --fact entry=feature --fact design-only=true
  python tools/loop/scenario.py check
  python tools/loop/scenario.py --fixture --plant two-builds
  ```

What `check` does not check: that placement will supply a fact your scenario's predicate names, so a
scenario no request ever admits passes; that the first move enters at the scenario's entry step; an
activated row repeating a tag of your overlay, which composes as two rows; and the item and stage
kinds' own checks over activated rows, beyond their compositions.

## Claim keys

A stored claim, such as a cell of your orientation card or a run claim on the remote, carries a key
over what it was derived from, so a session can tell a fresh claim from a stale one without deriving
it again. A key is `k1:` and sixteen hex digits over the claim's sources: `<name>=<value>` facts such
as `commit=`, `base=`, `toplevel=`, `branch=`, `dirty=` and `runstate=`, and refs spelled
`<ref>@<sha>`. A source that could not be read is spelled `?`, and its key opens `k1:?`, which never
reads as fresh. The age is not part of the key: it is stored beside it as `at`.

Each source belongs to one of five classes, strongest first: `history` (commits and their trailers),
`view` (the card's cells and other generated views), `remote` (run claims, leases and mailbox
entries), `provenance` (your own words and the policy file) and `typed` (status words an agent typed).
A claim takes the weakest class among its sources. Its verdict is `fresh` when the stored key and a
recomputed one are equal and, for a `remote` claim, its age is inside the bound you pass; `re-derived`
when the key moved, so the claim is derived again; and `evidence` for a `typed` claim or one with
nothing to recompute.

Your orientation card's second line is the `keys —` cell:
`keys — view <k> · remote <k> · at <time>`. The `overlaps —` and `claims —` cells are read by the
`remote` key, every other cell by the `view` key. Where the loop kit is not installed the cell reads
`keys — skipped: no loop kit resolves in this tree` and the card still writes. When the card is
replayed, the view key is recomputed in the session's own tree: unchanged, the stored card prints as
it is; moved, the startup cells are rendered again, keeping the stored header, the `overlaps —` and
`claims —` cells, the remote key, and everything from the kickoff's READY line down. The replay's
`now —` line names the tree and ends `keys view fresh` or `keys view re-derived`, then
`remote evidence`, since a replay reads no remote. The `cli —`, `worktrees —`, `drift —`, `memory —`
and `health —` cells read inputs no key covers, so a fresh view key says nothing about them.

The unattended driver's `--claims` rows carry five fields, and `bash tools/unattended/unattended.sh --claims --with-key` adds the claim's key as a sixth, over the claim's ref <!-- usage: verb:unattended.sh:--claims 946a3549 -->
and its run record at the default branch's tracking ref. The card asks for the key, and its
`claims —` rows end ` · key ` and the key's first eight characters after `k1:`, or ` · key -` where
the driver is older than the flag and prints five fields. A row is a run's claim or any lease: its name is
the slug of a build lease, or the tail of a unit or cadence lease, and its second field the lease's fleet
tag, or a legacy `refs/gov/runs/<slug>` claim's node. A `released` row, a build handed over at its run's
end, shows on the card as a `terminal` one does: sorted with them, and hidden once a day old.

The build card's ref on the remote, `refs/gov/builds/<slug>/card`, is written by the driver, never by the kickoff engine itself: at a READY append or a stage follow the engine's `remote-ref` card store runs `bash tools/unattended/unattended.sh --card-ref write <slug> --message <file>`, bounded by its card publish bound, `CARD_PUBLISH_BOUND`, above the write's own worst case, with the card's commit message in the file. It is dark behind `RUN_CLAIMS`: while that is not `on` the verb prints `card-ref — off` and reads and writes nothing, and the append says `card — remote-ref not written: RUN_CLAIMS is off` while the clone cache and the build folder are still written, so a project that leaves the switch off never publishes a governance ref. With it on it prints `card-ref — builds/<slug>/card · <sha8>` (exit 0), `card-ref lost — <sha8>` when another write moved the ref first (exit 1; the engine re-renders once and tries again) or `card-ref not written — <why>` (exit 2); a write that does not answer within that bound leaves `card — remote-ref unknown: no answer within <n>s` and the rest of the append standing, since the write may have landed before it was stopped, and a landed one reaches the change feed at the next read of the remote; a lookup that does not answer wrote nothing and leaves `card — remote-ref not written: no answer within <n>s`. The engine reads the card through the driver too, never by a fetch of its own: `bash tools/unattended/unattended.sh --card-ref lookup <slug>` fetches the ref from the clone's one remote, whatever its name, into this node's cache `refs/gov/remote/builds/<slug>/card`, writing no `FETCH_HEAD`, and prints `card-ref — <commit>` and the commit's message, `card-ref — none` where the remote holds no card, `card-ref — off`, or `card-ref not read — <why>` (exit 2). That cache ref is the one name the engine reads, so a route to a build whose card a terminal follow marked is refused at once, and a lookup that does not answer leaves the card read from the clone cache as `evidence`. <!-- usage: verb:unattended.sh:--card-ref 6bca48d8 -->

A request the owner typed that is not yet a build is recorded with `bash tools/unattended/unattended.sh --request <file>`, the file holding the owner's words as UTF-8. It prints the request's content key, twelve hex digits (PINNED) over the text with case, whitespace, ISO dates, emphasis and links folded, so two typings of the same words share one key; an empty file or one that is not UTF-8 is refused before anything is written. The words never leave your machine: they are kept byte for byte in your clone's git directory under `requests/`, beside the list of sessions that recorded them there, and the remote gains only `refs/gov/requests/<content key>`, holding the key, your node's fleet tag and your session. It prints `request — <key> · recorded <ref>` or, when the same words were recorded first, `request — <key> · already recorded <ref>` (exit 0 both), a copy differing only in line endings, a byte-order mark or wrapping counting as the same words; words that key alike but differ, say only in a date, are refused with `request not written — <key> · collision: ...` naming the copy already kept (exit 2), and nothing is written, so reword and re-run. Two sessions recording at once on one machine take turns under a lock in the git directory, `requests.lock`; one still waiting after its wait of 5 s (PINNED) prints `request — <key> · not written · requests.lock busy` (exit 2) and writes nothing, so re-run it. Otherwise it names why nothing reached the remote (exit 2), the words kept so a re-run retries. Any node may then claim the request with `--lease acquire request <content key>`. A key that reached you from another node or session is data with provenance, never your consent: only a session that recorded the words on this machine reads as having typed them, and only while the copy kept there is still the exact bytes that session submitted, so a kept copy edited or replaced, its line endings rewritten included, loses its consent until it is recorded again. A session the harness gives no id (`CLAUDE_CODE_SESSION_ID` unset, empty or `absent`) still records the request, its record naming `session: absent`, but that is provenance and never consent: no session is listed beside the words, and asking for consent with no session prints `request — <key> · no session: the harness exposed none, so nothing here is consent`. <!-- usage: verb:unattended.sh:--request 3ed0250c -->

A request that loops before it is a build draws on its own budget with `bash tools/unattended/unattended.sh --request-draw <content key> --cause <cause> --item <item>`: one row, `draw · <cause> · <item> · <spent>/<total>`, committed on the request's record `refs/gov/requests/<content key>` on top of the rows before it, so every machine counts the same laps (exit 0). Once the rows reach the base of `flow.rework-budget`, 4 by default (PINNED), it prints `exhausted · <spent>/<total>` and adds nothing (exit 3). A key with no record yet is recorded first from the words your clone keeps for it, as `--request` records them but naming no session, so a draw never stands for your consent; with no record and no kept words it names `--request <file>` and draws nothing (exit 2). A machine that loses a race with another re-reads and draws again, up to three times (PINNED), printing `lost the race, re-read <n> of 3`; a remote that does not answer, or a race lost a fourth time, prints `not drawn, contention` and draws nothing (exit 2). `placement.py place` calls it for you; "How much rework a build may do" below says when. <!-- usage: verb:unattended.sh:--request-draw a5d01f8a -->

Whether a request is your own consent is answered, read-only, by `bash tools/unattended/unattended.sh --request-consent <content key>`: it prints `request — <key> · typed here: this session's own words` (exit 0) when this session recorded those exact words on this machine with `--request`, and `request — <key> · relayed: data with provenance, never consent`, or the `no session` line, otherwise (exit 1); any other argument count prints its form (exit 2). It reads no remote and writes nothing. `placement.py check` runs it for a `breakpoint` placement, so a review is never placed on a build from a request that only reached you by its key. <!-- usage: verb:unattended.sh:--request-consent 1012b408 -->

A placed `new`, `patch` or `repeat` request becomes a build with `bash tools/unattended/unattended.sh --entry-claim <slug> --request <content key> [--pieces <n>]`, the claim. It reads the request's passed placement through `placement.py record` and refuses any other disposition (exit 1), a slug `--new-build` would refuse, and on a `repeat` a missing or non-positive `--pieces`, the count of pieces you asked for, written to the README so the run's recipe mode can read it (one line naming `--pieces`, exit 2), all before it reads your remote. It then reads `refs/gov/claims/<slug>`: where no claim exists it runs the same local slug check `--new-build` runs and creates the claim, one commit holding your claimant key (`<fleet tag>:<session>`), session, the request's content key, the disposition, the placement's redacted reason, scenarios and facts, and on a patch the origin build and its newest default-branch commit, never the request's words; where the claim is yours it resumes at the first step not yet done and skips the slug check, which would find your own commits; where another key holds it, it draws `route-back` on `item.entry.claim` from the request's pre-claim budget and exits 5 (PINNED), so you pick a fresh slug, or 3 once that budget is spent. A remote that does not answer follows `leases.offline`: `refuse` exits 1, any other value prints `claim not written — offline` and exits 4 (PINNED); no claim is queued and no build folder is written. A `patch` or `repeat` then takes its build lease, and a stale build lease is taken over: where the refusal says the holder's lease is stale, unseen beating by this machine for longer than `leases.expiry-hours`, the claim runs `--lease take-over` once, prints its `take-announced` line and goes on as though it had acquired the lease, a take-over refused being routed by its own cause as below, so a holder that came back is waited on, and one not written exits 2. Otherwise the lease's refusal is routed by its cause: `tombstone`, `terminal` and `epoch-fence` print one `ask:` line for you to file and exit 1, never retried however lenient `leases` is; `live-holder`, `offered`, and `overlap` under `leases: refuse`, add `wait-since:` to the claim and exit 4 while you wait, then once `flow.wait-ceiling`, 72 hours by default (PINNED), has passed by this machine's clock, print an owner item and exit 1; an overlap under `leases: warn` adds `overlap:` to the claim and goes on. It commits the derived plan record in a commit of its own, `records(<slug>): entry.claim's derived plan record`, holding the README `gen_build_index.py --placed-build` writes (`parents: <origin>` on a patch; `authorized-by: recipe`, `playbook:` and `pieces:` on a repeat) and its contract row, and refuses when anything else is staged; then it writes the build's first transition record: a `new` into planning and a `repeat` into designing as `item.entry.claim` `claimed`, a `patch` into designing as `item.plan.dedupe` `patch`. Under `patch.ratify: owner` (the default is `auto`) a patch prints `owner item: ratify <slug>` and its record into designing is refused, naming `patch.ratify`, until your disposition record of `item.entry.claim` `ratified` sits in the build's `build/` folder under the unit id `<FAMILY>-<slug>-1`, and `rejected` holds it for good. It does nothing while `RUN_CLAIMS` is off. <!-- usage: verb:unattended.sh:--entry-claim 2cb559fb -->

A decision or a problem is filed once on the remote with `bash tools/unattended/unattended.sh --register decision <build> <item> <fork> <file>` or `--register problem <subject> <item> <file>`. A decision is keyed by the item that raised the question and its fork, never by its wording, so a second session deciding the same slot is refused with exit 1 and shown the first one's record; a problem's id comes from your session, the item, the subject and the text, so two different problems on one path both land and a retried filing is refused. The text file is capped at 4096 bytes (PINNED) of plain text. It prints `register — written <ref>` (exit 0), `register — exists <ref>` (exit 1) or names why nothing was written (exit 2), and does nothing while `RUN_CLAIMS` is off. <!-- usage: verb:unattended.sh:--register 371297d7 -->

A build, a unit of a build, a cadence run or a recorded request is leased on the remote with `bash tools/unattended/unattended.sh --lease acquire build <slug>` (or `unit <slug> <id>`, `run <cadence> <period>`, `request <content key>`, the last refused `no-record` where the remote holds no `refs/gov/requests/<content key>`, and the slug `request` reserved for it as `run` is); `renew` takes `--witness <sha>`, `release` with no `--as` hands the lease over as `released`, which anyone takes at the next epoch, while `--as landed|withdrawn` leaves a build or unit lease a tombstone (a cadence run lease takes `--as landed|aborted`), `take-over` takes a stale foreign lease and raises its epoch, `offer <kind> <name> [<sub>] --to <tag>` (or `--to <tag>/<session>`) offers an absent or released lease to one node, or one session of it, without assigning it, every other caller refused `offered` until `leases.offer-seconds` after its first sighting of the offer, `acquire build <slug> --for draw` holds a closed build's tombstone for a patch build's draw, `--lease flush` pushes the writes this node queued while the remote did not answer, refusing one whose last fetch is older than `leases.queued-claim-days`, and `--lease prune` deletes the run leases and legacy run claims terminal that long, never a build's; `fence build <slug> [--after <tip>]` prints the fence the lander's push carries and writes nothing, `--after` re-fencing a move of the lease by its own holder at the same epoch. Each prints one line, `lease — <tail> · <act> · epoch <n>`, or names the refusal: `live-holder`, `tombstone`, `epoch-fence`, `overlap`, `offline`, `offered`, `terminal` or `no-record`. With no session id from the harness (`CLAUDE_CODE_SESSION_ID` unset, empty or `absent`) the acts that write a holder, `acquire`, `take-over`, `renew`, `release` and `offer`, print `lease not written — no session: CLAUDE_CODE_SESSION_ID is unset and no keepalive identifies this holder` and exit 2 before reading anything, because an absent session would name every id-less session on your node; `flush`, `prune` and `fence` name no holder and run as they do with a session, so a headless supervisor still prunes and a fence from a terminal or CI still answers. A run's own claim, identified by its keepalive, is unaffected. `--lease status <kind> <name> [<sub>]` reads one lease and writes nothing: one TAB-separated line, its tail, fleet tag, session, status, verdict and epoch, or `lease — none · <tail>`; it is how a reader tells two sessions of one node apart, which `--claims` cannot. With `RUN_CLAIMS` off every act but `fence` prints `lease — off · <tail>` and exits 0 having written nothing, and `fence` prints `fence — none · leases are off`. An offer is refused `offered` over an offer still open, whoever it names, and when `--to` names your own tag or your own session on it; another session on your tag is a hand-over and lands. An offer over a build or unit tombstone is refused `tombstone`, and `terminal` stays a cadence or legacy claim's. A create whose last commit this node's feed holds but git can no longer read, after a `git prune` say, is refused `epoch-fence` for a build or unit lease, whose epoch it cannot continue, and is a plain create at epoch 1 for a cadence run. An offline write whose ref's newest queued line is not a readable queued commit, a commit this clone does not hold or a line of another shape, prints `lease not written — <tail> · queued commit unreadable; nothing queued` and exits 2, queueing nothing, rather than building on that line, an older one or the cached tip. The `leases.*` policy keys shape it: `memory/guides/UNATTENDED-STOPS.md` section 7. <!-- usage: verb:unattended.sh:--lease f067f09f -->

Each node also keeps a change feed of every governance ref write it made or saw, in `gov-feed.log` under its git common dir. `bash tools/unattended/unattended.sh --feed check` holds that feed to the governance refs the clone holds and names each `missing`, `duplicate`, `extra`, `order` or `torn` line with exit 1; `--feed rebuild` writes the feed from those refs on a node that has none, and `--feed print --from <seq>` replays it from a sequence number. <!-- usage: verb:unattended.sh:--feed 4f313579 -->

- **Key some sources:** `python tools/loop/claims.py key commit=<sha> base=<sha>` prints one key; <!-- usage: script:tools/loop/claims.py#key d36ca5b8 -->
  `key --stdin` prints one key per input line, the line's sources separated by TABs.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries placeholders the shell reads as redirects -->
  ```bash
  python tools/loop/claims.py key commit=<sha> base=<sha> toplevel=<path> branch=main dirty=0
  ```

- **Judge a stored key:** `python tools/loop/claims.py verdict --stored <k> --class view --recomputed <k>` <!-- usage: script:tools/loop/claims.py#verdict 641f7922 -->
  prints `fresh`, `re-derived` or `evidence`. `--class` takes a class or several joined by commas,
  read as the weakest; a `remote` claim needs `--at` and `--bound`, its age bound in seconds, to read
  fresh. It exits 2 naming a class outside the five.

- **Read the card's keys:** `python tools/loop/claims.py card-keys` prints `view <k>`, `remote <k>`, <!-- usage: script:tools/loop/claims.py#card-keys 909e8102 -->
  `at <time>` and `remote-cells overlaps claims` for the repository you run it in, and nowhere else.

- **See it on a fixture:** `--fixture --plant <case>` runs one case and prints a line ending `held` or <!-- usage: script:tools/loop/claims.py 89c0ee14 -->
  `MISSED`: `key-stable`, `key-moves`, `key-unread`, `typed-evidence`, `remote-aged` and
  `card-keys-worktree`, the last in a scratch repository with a bare remote and a worktree, removed
  after. `--selftest` runs every case, and gov's own `loop claims fixtures` gate runs it.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/claims.py --fixture --plant key-moves
  python tools/loop/claims.py --selftest
  ```

## Where a build is, and what runs next

The position engine answers "where is this build, and what next" from witnesses alone. A unit's step
is `none`, then `designed` once its spec is committed and grades READY, `built` once a pass commit
names it in its `Pass:` trailer and an acceptance record names that commit, `tested` once the bar's
`gates-run` fact in the run-state file graded a tip containing that commit, and `deployed` once the
default branch's remote-tracking tip contains it. Until an executor writes acceptance records, the
shipped `acceptance` computed witness names the stand-in writer, and while it does a unit no
acceptance record names reads `built` from its pass commit alone, its `unit —` line ending
`· acceptance unarmed`; a unit a record names still needs that record to name its pass commit. The
executor's build, which gives the row an actor writer, lifts the tag, and so does a definition with no
`acceptance` row. A status word typed in a spec header or the build README never moves a step. The build's step is the step its least-advanced unit works in next, and
the next item is the first item of that step whose witness does not hold and whose needs are
witnessed. Only three kinds of item have a witness reader today: a step's exit, the unit table's four
forward items, and an item a recorded move names. Every other item prints as an `evidence` claim and
counts as not yet done.

The answer is one of `act`, `awaiting`, `blocked`, `terminal`, `stuck`, `invalid-input` and
`stale-remote`. A remote-tracking tip last fetched longer ago than the unattended kit's
`RESUME_STALE_BOUND`, or a remote the ladder cannot choose, answers `stale-remote` before anything
else. The last fetch is the newest of three readings: the time of each `FETCH_HEAD` git wrote, in
the repository's own git directory or under any of its worktrees, so a fetch that finds nothing new
still counts, but only when it holds a line for the default branch fetched from the remote's own
URL, as `git remote get-url` spells it past every trailing `/` and one `.git`, so a failed fetch, which
leaves the file empty, or a fetch of another branch or remote is not a fetch; the tracking ref's
newest reflog entry; and, only where neither is there, as on a fresh clone, the clone itself. The tracking ref's `read —` line says which, ending `fetched <n>s ago · from
FETCH_HEAD`, `from reflog` or `from clone`, or `fetched never`, which adds `· core.logAllRefUpdates=false`
where your repository's setting reads false, the reason no reflog was written, and each `FETCH_HEAD` it
skipped prints its own line after it, `read — FETCH_HEAD · skipped — empty` or `skipped — no line for
<branch> of <remote>`, naming the remote and never its URL. git leaves a URL's user part out of what
it writes into `FETCH_HEAD`, so an SSH remote, in the scp form or `ssh://` with a user, or a URL carrying a user
and a token, compares without it on both sides; a URL git rewrote through `url.<base>.insteadOf`
still reads skipped. With no remote at all, or no tracking ref of the default branch, the remote reads absent: the
engine answers on your local witnesses, so no unit reads `deployed`, and prints
`interrupt — remote · none` with no remote-tip claim. A tracking ref you deleted reads the same. An owed parked decision or an unpassed hold answers
`awaiting`; a `parents:` build that has not landed answers `blocked`; an undecided ask answers
`awaiting` only when no item can run.

The frontier is every item of the build's step whose witness does not hold and whose needs are
witnessed, in the order the composition lists them; the next item is its first entry. A refused item
stays on it, because its witness still does not hold, so one refusal never leaves the build with
nowhere to go. Record a refusal with the unattended driver's `--refused <slug> --item <tag> --key
<instance key> --reason <text>`: it writes one `refusal` row to the run-state file, and only where
the engine holds the tag as one your composition declares and the key as that tag's instance shape. <!-- usage: verb:unattended.sh:--refused 0b91a77d -->
To record a typed refusal, add `--rule <the rule that refused> --remedy <one line> --actor <who can
perform it>`, all three together: the row's reason then ends ` · rule <r> · remedy <m> · actor <a>`.
The actor is one of `self`, `producer`, `driver`, `owner` or `build:<slug>`; any other actor, a
missing one of the three, or a rule or remedy holding ` · ` is refused and nothing is written. The
position engine reads the three back beside the reason, and its `refusal —` line still prints the
reason alone. The roles page says where each actor's refusal goes.

The unattended driver's `--plan` prints the engine's answer as its `next:` line, in the same five
shapes it always printed, and beneath it a `frontier:` line naming the frontier's tags, or
`frontier: none`. `--status` prints the engine's lines after its status line.

- **Read a build's position:** `python tools/loop/position.py <slug>` prints a `position —` line with <!-- usage: script:tools/loop/position.py 8d078234 -->
  the state, the step, the answer and its reason, one `unit —` line per unit, the `next —` item with
  its actor and its instance key, a `frontier —` line, one `refusal —` line per refusal the run
  recorded with its item, key and reason, each `interrupt —`, then every file and ref it read as
  `read —` lines and every claim it used with its key and verdict as `claim —` lines. Where the runlog
  kit is not installed it prints `refusal — unarmed` with the reason and still prints the frontier.
  `--json` prints the same fields as one object, each unit carrying `acceptance_armed`, false exactly
  where its `unit —` line ends `· acceptance unarmed`, and `--next-line` the `next:` shape alone, with
  `--frontier` adding the frontier's tags, or `none`, on a second line. It exits 2 on
  `invalid-input`, else 0. Run in a repository with the unattended kit installed, it asks the driver's
  `--plan` for each unit's spec state.
- **Check a refusal before recording it:** `--check-refusal <tag> <key>` prints `loop: refusal
  held`, exit 0, `loop: refused` with the reason, exit 1, or `loop: unarmed`, exit 2, where your
  composition does not read. With no composition it checks against gov's own items. The driver's
  `--refused` runs it and records nothing unless it exits 0.
- **See it on a fixture:** `--fixture --plant <case>` builds a scratch repository with a bare remote,
  but none for `no-remote`, plants one case, prints the engine's lines and one line ending `held` or
  `MISSED`, and removes it: `steps`, `typed-status`, `idempotent`, `owner-decision`, `parent-unlanded`,
  `terminal`, `stale-remote` (its tracking tip's reflog entry aged past the bound), `no-remote`,
  `fresh-clone` (a clone read from clone), `quiet-remote` (a fetch from a linked worktree after the
  aged reflog, read from `FETCH_HEAD`), `offline-stale` (a clone's `FETCH_HEAD` dated past the bound), `failed-fetch` (the
  aged reflog, then a fetch from a path that does not exist, its empty `FETCH_HEAD` skipped), `bad-transition`, `deadlock`, `bar-wait`, `frontier-chain`, `frontier-parallel`,
  `frontier-refused`, `frontier-bad-key`, `frontier-none`, `plan-frontier`, `built-unarmed` (one unit
  tested and one built with no acceptance record under the stand-in writer, which `--json` reads
  `acceptance_armed` false and the driver's `--status` names as the next unit),
  `built-unheld`, `built-armed`, `fetch-other-branch` (the aged reflog, then a fetch of another
  branch, its `FETCH_HEAD` skipped as holding no line for `main`), `clone-without-reflog` (a clone
  under `core.logAllRefUpdates=false`, read `fetched never` with the setting named), `scp-remote` and
  `ssh-userinfo-remote` (the aged reflog, then a fetch over an ssh shim from a URL with a user part,
  read from `FETCH_HEAD`), `url-forms` (a fetch failing at connect from a URL carrying a password,
  which no line prints, then one row per configured and written URL pair, `equal` or `unequal`),
  `plan-line` and `status-line`; `frontier-refused`,
  `frontier-bad-key`, `plan-frontier`, `built-unarmed` and the last two run the unattended driver. Every
  case runs with an empty global and system git config, so no setting of your machine's reaches it. `--selftest` runs every case, and gov's own `loop position fixtures` gate runs it.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries placeholders the shell reads as redirects -->
  ```bash
  python tools/loop/position.py <slug> --json
  python tools/loop/position.py --fixture --plant steps
  python tools/loop/position.py --selftest
  ```

## The item kind, `kind.item`

Items are a registered kind: the kinds register's `kind.item` row names a factory, a row schema,
`tools/loop/item-schema.toml`, and a gate, so your repository can add an item to a gov step, or patch
or exclude one of gov's, from its own overlay, `.governance/instructions.toml`, the way it changes any
registered kind's row (see [overlay rows](overlay-rows.md)). Every check reads the composition of gov's
items with yours at your last commit, never the overlay's text, so a patch that closes a needs cycle is
caught even though no row you wrote holds one.

**Your own item** is an `[[item]]` table with every field a gov item carries, its tag holding `adopter`
at the third segment, item.test.adopter.smoke for instance:

```toml
[[item]]
tag = "item.test.adopter.smoke"
step = "step.test"
actor = "command:smoke"
needs = ["item.test.verdict"]
inputs = ["layer.flow:the verified tree"]
allowance = "the smoke record"
returns = "record-kind.smoke"
outcomes = ["done"]
witness = { class = "history", by = "the smoke record" }
owner = "your-build"
routes = { done = "item.test.exit" }
```

**What you may change on gov's items.** The schema says, field by field:

- `needs` is open, and removing a need widens it; adding one narrows it.
- `upstream` is open, and removing an entry widens it, since the item then answers fewer rows. No gov
  item carries it, so an `amends` adding it to one is held: write it on your own item, or in a
  `supersedes`.
- `inputs` and `routes` are open, and adding widens them. An `amends` writes `routes` whole, so every
  changed route reads as a widening, with gov's old table as a narrowing beside it.
- `seed` and `map` are open along their order of values, a later value widening: `seed` runs `none`,
  `write-set`, `question-paths`, `scope-paths`, and `map` runs `none`, `base`. `unfolds` is open, and
  adding widens it. An absent `seed` or `map` reads `none`, an absent `unfolds` reads empty.
- `actor` is open to a repository role and admitted by the actor-patch check alone. The schema opens it
  on the direction `changes`, any value other than gov's reading as a widening, so the patch composes,
  and `check` then judges it, naming the item, your row and the value: a repository role,
  `role:adopter.<name>`, by the roles kit's `check_roles.py --check-actor-patch`, which `check` runs and
  which refuses a role whose `return` lacks gov's role's template, whose `writes` lacks its class or
  whose `shapes` lacks the kind the item runs in; and any other value, a gov role or a command, is
  refused because an actor patch names a repository role.
- `step`, `witness` and `outcomes` are fixed by a principle, and `allowance`, `returns` and `owner` stay
  fixed because they declare no direction. Patching one is refused, naming the field and what fixes it.
- Each step's exit item and the floor item `item.test.verdict`, whose verdict the runner writes, are
  fixed rows: an `amends`, a `supersedes` or an exclusion of one is refused.
- An exclusion is refused while another item still needs the excluded one, naming that item, or while
  a policy key such as review.breakpoints names it, naming the key.

**Records at a version.** An input that reads a record is written `<layer tag>:record-kind.<name>`, or
with `@<n>` for a version, and a `returns` names the record kind it writes the same way. The definition
pins each typed record kind an item returns at its current version with a `[[record-version]]` row,
whose `fields` is a hash of the kind's required and closed fields. If the kind's fields change while its
version does not, `check` refuses it: the meaning moved with no bump. An input without `@<n>` reads the
current version. One with it must be met by an item in its needs closure returning that kind at that
version, so after a bump an input still pinned at the old version is refused until it moves.

- **Check the composed items:** `python tools/loop/loop_items.py check` composes your repository <!-- usage: script:tools/loop/loop_items.py#check 3c7c7c39 -->
  through the playbook kit and prints `loop: items composed · <n> row(s) · <m> repository`, one
  `loop: patch` line per classified patch operation of your overlay, one `loop: record-version` line
  per version row and `loop: record inputs · <n> joined`, and exits 0. It exits 1 on a refusal: the
  composition's, an actor patch, a needs cycle (each named), a need no item declares, a step exit or the floor item
  with no fixed row, a version row whose hash moved, or a record input no needed item produces. It
  exits 2, `unarmed`, where the playbook kit is not installed, the schema is absent, or your last
  commit holds no definition yet, as right after a first install, before its commit.
  `check --selftest` runs `check` and every case below. Gov's own `loop item kind` gate runs it; an
  install does not carry that gate, since the check reaches the playbook kit, which the loop kit does
  not require.

- **Add a gov item:** `new` appends one gov item to the definition, routing its `done` to the step's <!-- usage: script:tools/loop/loop_items.py#new 967f4049 -->
  exit item, `python tools/loop/loop_items.py new <name> --step <step> --actor <actor> --witness-by <text> --owner <build>`, with `--input`, `--allowance` and `--returns` owed by every actor but a
  `role:` one, which takes them from its role. It grades the file as written with the definition's own
  checks and restores its bytes and exits 1 when they refuse it. A name that is not one tag segment,
  the name `adopter`, a tag the definition already declares, a step that is no gov step and a missing
  flag each exit 2 before any write. The kinds register runs it as the item kind's factory:

  ```text
  python <prefix>/playbook/core.py new item <name> --step <step> --actor <kind:name> --witness-by <text> --owner <build> [--input <layer:what> --allowance <text> --returns <record>]
  ```

- **See a refusal:** `--fixture --plant <case>` builds a scratch repository holding a copy of the kits <!-- usage: script:tools/loop/loop_items.py 461a5b05 -->
  `check` reaches, commits one plant there, runs `check` and relays its output and exit. The cases:
  `factory` (the register's factory adds an item, `check` reads it, and the same add again exits 2),
  `repo-cycle`, `repo-unresolved-need`, `repo-input-unproduced`, `repo-input-produced`,
  `version-unbumped`, `version-bumped`, `version-stale-input`, `patch-witness`, `patch-outcomes`,
  `patch-actor-repo`, `patch-actor-gov`, `patch-allowance`, `supersede-floor`, `supersede-exit`, `exclude-needed`, `exclude-breakpoint`, `patch-remove-need`,
  `patch-add-need`, `patch-routes`, `amended-cycle` (an `amends` whose added need closes a cycle the
  overlay text does not hold), `exit-unfixed`, `schema-absent` and `definition-uncommitted` (a
  first install's state, where the render composes no item and refuses nothing).

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/loop_items.py check
  python tools/loop/loop_items.py --fixture --plant amended-cycle
  python tools/loop/loop_items.py new smoke --step step.test --actor command:smoke --input "layer.flow:the verified tree" --allowance "the smoke record" --returns record-kind.smoke --witness-by "the smoke record" --owner your-build
  ```

`check` does not tell whether a `fields` hash re-pinned with no version bump was meant: the rule
compares each row with the record table and reads no earlier revision, so that edit is the review's to
see. A role item's record kind comes from its role and is not joined. The step gate's `item` class
grades a gov item that disappears between a landing's base and its tip, as it does any member.

## The code an item is handed: its seed

A role's work order will carry a `code` slot, the code its item touches. Which code is computed from
the item's `seed`, one of four values, from the narrowest neighbourhood to the broadest:

- `none`, the default and every non-role item's: no code is handed.
- `write-set`: the paths the unit's spec declares under `### Files touched`, read from the spec at your
  last commit. The builder, tester and spec-writer items take it.
- `question-paths`: the backticked paths in the question a researcher was asked.
- `scope-paths`: the paths of the design's scope. No plan record carries a scope yet, so this one prints
  `unarmed — scope-paths: no plan record carries a scope; dRankedPlan's plan.record arms it`, never an
  empty list. The architect's items and the design's reasoning item take it.

`python tools/loop/loop_lib.py --check` prints one `loop: seed <tag> · <value>` line per item and a
`loop: seeds` count, and refuses a value outside those four and a seed other than `none` on an item
whose actor is not a role, naming the item and the value.

**Resolve an item's seed:** the definition's reader takes a `seed` command,
`loop_lib.py seed <item tag> [--build <slug>] [--unit <id>] [--question <text>]`, run from inside your
repository. It prints one path per line, relative to the repository, with forward slashes, a leading
`./` and a trailing `/` dropped and each path once, in the order first seen; or the one `unarmed`
line naming the source and why. `write-set` takes `--build` and `--unit` and finds the spec whose
heading names that unit; `question-paths` takes `--question`. A missing one exits 2 naming it, as do an
item no row declares and a unit with no spec, or two. Where the unattended kit is not installed,
`write-set` and `question-paths` print `unarmed — <source>: no unattended driver resolves`. A spec at
CLOSED or WONTDO still declares its paths to `write-set`, which reads a spec of any status, and a spec
listing none prints `unarmed — write-set: <spec> lists no path`; a path spelled with backslashes is prose, not a path. The paths
are what was declared, not what was written. `--fixture --plant seed-bad`, `seed-write`, `seed-question`
and `seed-scope` show a refusal and each source.

**Read one item's declaration:** `python tools/loop/loop_lib.py declaration --item item.build.unit-pass --json` <!-- usage: script:tools/loop/loop_lib.py#declaration f5755a0f -->
prints that item as one line of JSON: its `tag`, `actor`, `step`, `outcomes` (the disposition set
where the row names it), `witness`, and its `inputs`, `allowance` and `returns`, a role item's
absent ones taken from its role, with `source` saying where each came from. The roles kit's handoff
renderer runs it to cut a work order for one item. An item no row declares exits 1 naming the tag,
and so does a definition that does not read; both print on stderr.

**The one path-token rule.** Both sources read paths through the unattended driver, so one rule decides <!-- usage: verb:unattended.sh:--path-tokens ee31c658 -->
what a path is: `bash tools/unattended/unattended.sh --path-tokens` prints each backticked span of the
text on its standard input that is one word of letters, digits, dots, underscores, slashes and dashes
holding a `/` or ending in an extension, one per line. With `--files-touched <rev> <spec> ...` it prints
instead the paths each spec declares under `### Files touched` at that revision, exactly what the
driver's own overlap and dispatch reads take, skipping a CLOSED or WONTDO spec unless `--any-status`
comes first, as `write-set` asks. It writes nothing and
exits 0, or 2 with one `path-tokens not read` line on a malformed call or a revision or spec git cannot
read.

**The map slot and its unfolds.** An item's `map` says whether its work order's `map` slot is filled:
`none`, the default, or `base`, the project map. The items where the project map is delivered to the
planner, the architect, the reuse scout, the spec writer and the researcher declare `base`, as
`--check` lists them; the unit workers, the builder and the tester among them, get no map. An item's
`unfolds` lists the namespace words, each the `ns` of a row of the playbook kit's `namespaces.toml`,
whose nodes its map slot spells out one by one; `item.design.inventory` unfolds `kit`
and `policy`. `loop_lib.py --check` prints one `loop: map <tag> · map <value>` line per item, ending
`· unfolds <words>` where it unfolds, and refuses a `map` outside `none` and `base`, an `unfolds` beside
`map = "none"`, and an unfold word no namespace row registers, naming the item and the value or word.
Where the playbook kit is not installed it prints `loop: unfolds · unarmed — no namespace registry
resolves`, checks no unfold word, and the rest of the check runs; a registry that resolves and does not
read is refused. `--fixture --plant map-bad`, `unfold-unregistered`, `unfold-no-map`, `unfold-not-list`,
`no-registry` and `registry-bad` show each.

## Handing an item what its upstream items established

An item can name the items whose commitments it must honour, its upstream items, in an `upstream`
field. Each upstream item's return lists what it establishes; those rows are handed to the item, and
its return answers every one. The field is a list of one-line entries, the gate `record` where an
entry gives none:

```toml
[[item]]
tag = "item.test.adopter.smoke"
# ... the row's other keys ...
outcomes = ["done", "finding"]
routes = { done = "item.test.exit", finding = "item.test.exit" }
upstream = [
  { item = "item.test.select", gate = "record" },
  { item = "item.test.merge", gate = "measured", measured-by = "memory/builds/your-build/build/2026-11-16-build-FIX-your-build-1-measurement.md", measured-line = "## Verdict: CLEAN" },
]
```

**What an upstream item writes.** Its return carries a `## Establishes` section, one row per line,
`- <row id> · <kind> · <text>`. The kind is one of `seam`, `criterion`, `interface`, `fork`, `finding`
and `repair`, and the row id is one tag segment, unique in that return.

**What the item answers.** Its return carries a `## Upstream` section answering every row it was handed
exactly once, `- <row id> · <answer> · <reason>`. The answer is one of three: `used` (the work honours
the row), `bypassed` (the work departs from it) or `not-applicable` (the row does not bear on the work),
and every answer carries a reason. A `bypassed` answer is always a finding, and the item's `finding`
outcome takes it, so an item with an `upstream` list must route `finding`.

**When an edge gates.** Every edge records its answers; only a `measured` edge refuses a return. An
entry is `measured` once a measurement shows its rows are worth gating: `measured-by` names a record
your last commit holds, and `measured-line` a line that record holds whole. Until then, keep the edge
at `record`. On a `record` edge a row left unanswered (`dropped`), answered twice (`doubled`), answered
with an id nobody handed (`invented`), with a word other than the three (`bad-answer`) or with no reason
(`no-reason`) is a finding and the return stands. On a `measured` edge each of those refuses the return.
An invented id that names no edge of the item is graded on the item's strictest gate.

**What `check` refuses.** `python tools/loop/loop_items.py check` prints
`loop: upstream edges · <n> record · <m> measured` and refuses an entry carrying another key or a gate
other than the two, an upstream item no item declares or one named twice, a measurement key on a
`record` entry, a `measured` entry whose record your last commit does not hold or whose line that record
lacks, and an item with an `upstream` list and no `finding` outcome. Each refusal names the item, the
upstream item and the key at fault.

- **Hand the rows on:** `python tools/loop/upstream.py rows <item> --return <upstream item>=<path>` <!-- usage: script:tools/loop/upstream.py#rows e6e7132d -->
  prints the rows of every upstream item's return, one per line, each id written
  `<upstream item>#<row id>`. Write them to a file and pass it to the roles kit's handoff renderer with
  `--upstream <rows file>`: the agent's task then lists the rows and the line telling it how to answer.
  An upstream item handed no return, or whose return has no `## Establishes` section, exits 1, naming it.

- **Join the answers:** `python tools/loop/upstream.py join <item> --rows <rows file> --return <return path>` <!-- usage: script:tools/loop/upstream.py#join 142cdaaa -->
  prints one line per answered row, one `upstream · finding · <class> · <row id> · <why>` line per
  finding and `upstream · verdict · clean`, `finding` or `refused` last. It exits 1 on `refused`, or
  where `check` would refuse the composition, and 0 otherwise. With `--write --build <slug> --unit <id>`
  it also writes every line into a new journal record under the build's `build/` folder and prints its
  path. Either verb exits 2 on a bad argument, a path outside your repository, or a composition that
  does not read.

- **See it on a fixture:** `--fixture --plant <case>` builds a scratch repository holding a measurement <!-- usage: script:tools/loop/upstream.py c8a893f4 -->
  record, gives gov's `item.design.unit-spec`, in memory, an edge from `item.design.seams`, and runs one
  case: `clean`, `drop-gating`, `drop-recorded`, `bypassed`, `invented`, `doubled`, `bad-answer`,
  `no-reason`, `measured-unproven`, `measured-untracked`, `no-establishes`, `no-finding-route` and
  `record-written`. `--selftest` runs every case. Gov's own `loop upstream fixtures` gate runs it.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries placeholders the shell reads as redirects -->
  ```bash
  python tools/loop/upstream.py rows <item> --return <upstream item>=<path> > rows.txt
  python tools/loop/upstream.py join <item> --rows rows.txt --return <return path>
  python tools/loop/upstream.py --fixture --plant drop-gating
  ```

The checks do not tell whether an upstream item comes before the item in the needs graph, whether a
row's text is true or a `bypassed` reason a good one, or whether the measurement record measured the
edge it names: they read one line of it. Nothing tells a role to write its `## Establishes` section;
that is your build's prompt.

## Adding a stage of your own

Your repository may add a stage of its own between two adjacent gov stages, a security review between
Test and Deploy, say. Gov's five stages stay whole and in order: a stage of yours can neither remove,
reorder nor replace one. Stages are a registered kind: the kinds register's `kind.stage` row names a
factory, a row schema, `tools/loop/stage-schema.toml`, and a gate, so your stage is a `[[stage]]` table of
your overlay, `.governance/instructions.toml`, tagged step.adopter.<name>, with its exit item an
`[[item]]` tagged item.adopter.<name>.<item>:

```toml
[[stage]]
tag = "step.adopter.security-review"
after = "step.test"
before = "step.deploy"
pin = "3f1c9a20"
exit = "item.adopter.security-review.exit"

[[item]]
tag = "item.adopter.security-review.exit"
step = "step.adopter.security-review"
actor = "command:security-review"
needs = []
inputs = ["layer.flow:the verified tree"]
allowance = "the review record"
returns = "record-kind.security-review"
outcomes = ["recorded"]
witness = { class = "history", by = "the review record" }
owner = "your-build"
routes = { recorded = "transition" }
```

**What the splice does.** The build's transition table moves from Test to Deploy on one row: from
`testing`, on `item.test.exit` and `recorded`, into `deploying`. Your stage splits that row in two:
from `testing` into your stage's state, `adopter-security-review`, and from that state on your exit item
into `deploying`, each with the split row's witness. The state is derived from the tag; you never type
it. `pin` is the split row's eight-hex pin, so a gov update that changes that row turns your stage stale,
and `check` refuses it until you re-pin. Every other row stays as gov ships it, so a route back from
Deploy to an earlier gov stage passes over yours.

**What is refused**, each naming the stage, the rule and the tag:

- a tag that is not step.adopter.<name>, one name of its own, or whose name is a gov step's;
- a gov stage in `instructions.exclude`;
- an `after` and `before` that are not two gov stages next to each other in order, so a stage before
  Plan, after Deploy, or between two stages that are not neighbours;
- a second stage between the same two gov stages;
- a `pin` that is not the split row's;
- an `exit` that is no item of your stage routing the split row's outcome to `transition`;
- an item of your stage with no witness, and an item.adopter.<name>.<item> of no stage you declare.

A gov stage gov renames beside your stage leaves a change record naming its successor; `check` follows
it and prints one line naming your stage, the old tag and the new, so your stage keeps its place. The
boundaries your stage creates, the gov exit item before it and your exit item, are item tags
review.breakpoints may name as it names any other.

- **Check your stages:** `python tools/loop/splice.py check` composes your repository's stages and <!-- usage: script:tools/loop/splice.py#check db341368 -->
  items at your last commit and prints `loop: splices composed · <n> splice(s)`, one line per re-point
  and per derived row, and each refusal. It exits 0 green, 1 on a refusal, and 2, `unarmed`, where the
  playbook, policy or memory-tree kit is not installed. `check --selftest` runs `check` and every case
  below. Gov's own `loop splice check` gate runs it; an install does not carry that gate, since the
  check reaches kits the loop kit does not require.

- **Add a stage:** `new` writes your stage and its exit item to your overlay, the pin derived from the <!-- usage: script:tools/loop/splice.py#new ac81e02f -->
  split row, `python tools/loop/splice.py new <name> --after <step> --before <step> --actor <actor> --witness-by <text> --owner <build>`, with `--input`, `--allowance` and `--returns` owed by every actor but a
  `role:` one. A name that is not one tag segment, is `adopter` or is a gov step's, two gov stages that
  are not neighbours, a pair your last commit already splices and a missing flag each exit 2 before any
  write. It grades both rows before writing and exits 1, writing nothing, when they are refused. The
  kinds register runs it as the stage kind's factory:

  ```text
  python <prefix>/playbook/core.py new stage <name> --after <step> --before <step> --actor <kind:name> --witness-by <text> --owner <build> [--input <layer:what> --allowance <text> --returns <record>]
  ```

- **See a refusal:** `--fixture --plant <case>` runs `check` with one plant made in memory over gov's <!-- usage: script:tools/loop/splice.py 3e214874 -->
  definition, and prints its output and exit. The cases: `between-test-deploy`, `removes`, `reorders`,
  `replaces`, `before-plan`, `after-deploy`, `non-adjacent`, `two-splices`, `gov-rename` (a stage naming
  a renamed gov stage, re-pointed through its change record), `stale-pin`, `exit-elsewhere`,
  `exit-unwitnessed`, `orphan-item`, and `factory`, which adds a stage in a scratch repository, checks
  it, and adds it again to see the second refused.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/splice.py check
  python tools/loop/splice.py --fixture --plant non-adjacent
  python tools/loop/splice.py new security-review --after step.test --before step.deploy --actor command:security-review --input "layer.flow:the verified tree" --allowance "the review record" --returns record-kind.security-review --witness-by "the review record" --owner your-build
  ```

`check` does not move a build into your stage yet: the position engine and the transition record read
gov's table as shipped, so the derived rows are checked here and nothing moves on them. It does not
check that your stage's actor exists or its witness holds, nor where breakpoints sit. The step gate's
`stage` class grades a gov stage tag that disappears between a landing's base and its tip, so a gov
rename always leaves the record your stage follows; a stage tag of yours that disappears is not graded.

## Making a new part

Six kinds of the kinds register have a factory in this kit: a command, a policy key, a hook, a role,
a workflow and a scenario. A factory writes a new instance that already conforms, then runs the kind's gate over
the whole population. You reach each one through the register's one verb, which appends your name and
flags to the factory its row names:

```text
python <prefix>/playbook/core.py new command <verb> --kit <id> --run <path>
python <prefix>/playbook/core.py new policy-key <name> --allowed <toml> --default <toml> --summary <text> --usage <text> --owner <build>
python <prefix>/playbook/core.py new hook <name> --kit <id> --event <event> [--matcher <m>]
python <prefix>/playbook/core.py new role <slot> --workflow <name> --writes <class> --description <text> --reads <keys> --never <entries> --return <template> --output <text> --ceiling <bytes> --layer <layer tag> --acts-as item|cycle
python <prefix>/playbook/core.py new workflow <name> --driver <driver> --harness <path|none> --roles <slots> --enforced-by <text> --trigger <text> --order <n> --step <step tag|none>
python <prefix>/playbook/core.py new scenario <name> --extends <tag|none> --admit <fact>=<value> --entry <step tag>
```

Every factory works the same way. A bad argument exits 2, naming the flag, before anything is written.
Each file it writes is held at its prior bytes, so when the gate is red the factory prints the gate's
output, puts every file back, removes every file it created, and exits 1. When the gate is green it
prints the gate's output and each path it wrote, and exits 0. A kit that is not installed exits 2,
naming it.

- **A command:** `python tools/loop/factories.py command <verb> --kit <id> --run <path>` appends a <!-- usage: script:tools/loop/factories.py#command a0688757 -->
  `[[command]]` row, `verb` and `run`, to the kit descriptor whose `id` is `--kit`. `run` is a path
  relative to that descriptor's directory. Its gate is `check-commands`.
- **A policy key:** `python tools/loop/factories.py policy-key <name> --allowed <toml> --default <toml> --summary <text> --usage <text> --owner <build>` <!-- usage: script:tools/loop/factories.py#policy-key b76eed28 -->
  appends a `[[key]]` row to the policy catalogue. Its gate is four arms of `policy check`, run in
  process: `arm_schema`, `arm_shape`, `arm_summaries` and `arm_direction`, each printed as a
  `policy-check:` line. A default the row's own `allowed` refuses is red on `arm_shape`. A loop bound or
  deadline key is red on `arm_direction`, since the factory writes no `direction`. It writes the
  catalogue only, never `.governance/policy.toml` or the mirror `.governance/policy.json`.
- **A hook:** `python tools/loop/factories.py hook <name> --kit <id> --event <event> --matcher <m>` <!-- usage: script:tools/loop/factories.py#hook 7f9371c9 -->
  writes `<name>.js` and `<name>.fragment.json` beside the descriptor whose `id` is `--kit`, and a
  `[[files]]` row shipping each one where no `include` of that descriptor already does. `--matcher`
  is `*` when you leave it out. Its gate is `hook destinations (every declared hook path ships)`. That
  gate reads tracked fragments only, so the factory runs it against a throwaway copy of your index
  holding the new files, and deletes the copy afterwards. Your own index is never written: nothing is
  staged for you.
- **A role:** `python tools/loop/factories.py role <slot> --workflow <name> --writes <class> --description <text> --reads <keys> --never <entries> --return <template> --output <text> --ceiling <bytes> --layer <layer tag> --acts-as item|cycle` <!-- usage: script:tools/loop/factories.py#role 50224b14 -->
  writes `<slot>.agent.md` under the roles kit's `agents/`, its `never` list of `<limit> — <enforcer>`
  entries and its `return` template as the flags give them, lists the slot in its workflow's `roles`,
  gives the role `--ceiling` as its `budget`, the byte ceiling of its whole static block, its
  `## Charter` included, which the roles checker grades, and re-renders the roles README's
  catalogue. Its gate is `roles catalogue`.
- **A workflow:** `python tools/loop/factories.py workflow <name> --driver <driver> --harness <path|none> --roles <slots> --enforced-by <text> --trigger <text> --order <n> --step <step>` <!-- usage: script:tools/loop/factories.py#workflow d7b86fbb -->
  appends its row to the roles kit's `workflows.toml`, its `name`, `order` and `step` row to this
  kit's `loop.toml`; the roles checker reads the workflow names from the composed registry, so no
  closed set in code moves. Its gate is `roles catalogue`, then `python tools/loop/loop_lib.py --check`.
- **A scenario:** `python tools/loop/factories.py scenario <name> --extends <tag|none> --admit <fact>=<value> --entry <step tag>` <!-- usage: script:tools/loop/factories.py#scenario 490958b5 -->
  appends a gov `[[scenario]]` row to this kit's `scenarios.toml`, with `activates` and `then` empty;
  repeat `--admit` for each value a fact admits. The name `adopter`, a tag the pack already holds and an
  `--admit` not shaped `<fact>=<value>` exit 2 before anything is written. Its gate is
  `python tools/loop/scenario.py check`. A scenario of your own goes in your overlay by hand, as the
  section on choosing a build's scenario shows, never through this factory.
- **Check the commands:** `python tools/loop/factories.py check-commands` reads every kit descriptor <!-- usage: script:tools/loop/factories.py#check-commands dfaea29d -->
  and refuses, exit 1, a `[[command]]` row whose verb is not one tag segment or repeats in its
  descriptor, a row whose `run` names no tracked file under the descriptor's directory, and a
  descriptor that holds rows but no string `id`. With no row anywhere it prints `unarmed` and exits 0,
  which is not coverage. Gov's `loop command conformance` gate runs it.
- **See each gate red and green:** `python tools/loop/factories.py --fixture --plant <case>` runs one <!-- usage: script:tools/loop/factories.py c96f4991 -->
  case in a scratch clone of your working tree. Each `-new` case runs the factory and expects green:
  `command-new`, `policy-key-new`, `hook-new`, `role-new` and `workflow-new`. Each `-hand` case writes
  a hand-made instance that does not conform and expects the same gate red: `command-hand`,
  `policy-key-hand`, `hook-hand`, `role-hand` and `workflow-hand`. `scenario-new` and `scenario-hand`
  do the same for a scenario, the hand row naming an entry step that does not exist. `factory-restores` gives a policy
  key a default its own row refuses, and expects exit 1 with the clone left clean.
  `factory-restores-create` runs the hook factory, which creates its files, after committing a hand
  fragment that holds the hook gate red, and expects exit 1 with no created file left on disk and the
  clone clean. `factory-interrupt` runs the role factory's writes with the second held file's rename
  interrupted by `KeyboardInterrupt`, and expects every held file at its prior bytes, the role file
  absent and the clone clean; it then leaves a stray temp beside a held file and expects it named. Before
  its first write every factory names each temp an interrupted write left beside a file it holds, one
  `factories: leftover · <path>` line each, and writes on: delete what it names. `--selftest` runs
  `check-commands` and every case. Gov's `loop factories fixtures` gate runs it.

What is still yours to do, as it would be for a part made by hand. A role needs its agent file
rendered under `.claude/agents/`. A hook needs wiring into your settings, then its `[[hook]]` stage
row. A new policy key needs its mirror: commit the catalogue, then run `policy.py mirror --write` at
that commit. Until then the full `policy check` is red on `arm_mirror_parity`. A key whose owner build
has landed also needs a reader, and every key needs its section of `help/reference/policy.md`. The
kit's version marker moves when its shipped bytes do, and the codebase map needs regenerating.

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
```bash
python tools/loop/factories.py check-commands
python tools/loop/factories.py --fixture --plant hook-new
python tools/loop/factories.py policy-key review.example --allowed '["a", "b"]' --default '"a"' --summary "An example." --usage 'review.example = "b"' --owner your-build
```

## Stage claims

Every part of the product declares the build stage it serves, so the loop is written on the parts as
well as in the definition. A claim is a non-empty list of the definition's step tags, such as
`["step.build", "step.test"]`, or `["none"]` for a part that serves no build stage. Any other value,
an empty list, a tag the definition does not declare, or `none` beside a tag, is no claim. Where each
kind keeps its claim:

- a feature dossier of the codebase map: a top-level `stage` key in its fence, above `[claims]`;
- a gate leg: a `stage` key, the last key of its row in the gate manifest;
- a workflow: the `step` of its `[[workflow]]` row in the definition;
- a role: derived from its role file's `workflow:` through that workflow's row, never typed on the role;
- a hook: one `[[hook]]` row of the definition per key of the map's `git-hooks` and `harness-hooks`
  inventories, with `key` and `stage`. A key naming a script under the tool root spells that root
  `{prefix}/`, which the check expands before it joins.

```toml
[[hook]]
key = "PreToolUse {prefix}/hooks/scratch-guard.js"
stage = ["step.plan", "step.design", "step.build", "step.test", "step.deploy"]
```

- **Check the claims:** `python tools/loop/stage_coverage.py` joins every dossier, leg, workflow, <!-- usage: script:tools/loop/stage_coverage.py 2f7dd348 -->
  role and hook both ways to its claim, then reads each step's exit item and its witness class. It
  prints one line per kind and per role, then one line per step, then each finding, and exits 0, or
  1 on a finding:

  ```text
  stage-coverage: part · leg · <n> parts · <u> unclaimed · <s> stale
  stage-coverage: role gov-builder · workflow build · step.build
  stage-coverage: stage · step.build · exit item.build.exit · witness history
  stage-coverage: unclaimed leg <name> · no claim
  stage-coverage: stale hook <key>
  stage-coverage: refused · <the definition reader's refusal>
  ```

  A part with no claim, or one carrying an invalid value, is `unclaimed` and the value is printed. A
  `[[hook]]` row naming a hook the map no longer holds is `stale`. A kind with no parts in the tree
  prints `unarmed` and exits 1, never green. A step whose exit item declares no witness is the
  definition reader's refusal, printed as it words it. It exits 2 `unarmed` where the codebase-map,
  roles or memory-tree kit does not resolve. It does not judge whether a claimed stage is the right
  one, nor whether a dossier's stage agrees with the stages of the parts it claims.
- **See a refusal:** `--fixture --plant <case>` reads the tree with one break made in memory:
  `unclaimed-leg`, `unclaimed-hook`, `stale-hook`, `bad-tag` (the first dossier claiming step.ship),
  `stage-no-witness` and `no-legs` each exit 1 naming the break; `role-derived` (the `build` workflow
  moved to `step.test`) exits 0 with `gov-builder` reading `step.test`. `--selftest` runs the tree,
  then every case, and gov's own `loop stage coverage` gate runs it.

  <!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter -->
  ```bash
  python tools/loop/stage_coverage.py --fixture --plant stale-hook
  python tools/loop/stage_coverage.py --selftest
  ```

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

## How many rounds a review takes

Every review loop stops at a bound you set in `.governance/policy.toml`, under four keys:

- `review.max-rounds`, default 3: the ceiling of every loop. A round one past it reads `CEILING`.
- `review.design.rounds`, default `one`: how many rounds a spec audit takes. `one` is one round,
  `fixed-count` is `review.design.round-count` rounds, and each `until-*` value runs to
  `review.max-rounds`.
- `review.design.round-count`, default 2: the count `fixed-count` reads.
- `review.follow-up`, default `after-high`: whether the closing review takes follow-up rounds. `never`
  gives it one round. `after-high` and `while-finding` run to `review.max-rounds`.

From these the loop kit derives two bounds: the spec bound, which a spec audit stops at with
`BOUNDED`, and the closing bound, which the closing review stops at. A `review.design.round-count`
equal to `review.max-rounds` is admitted, and the audit reaches it as `BOUNDED`. A count above it is
refused, naming both keys, and so is any value below 1. Raising any of the four is yours, the owner's:
an agent's run never writes the policy file, and the unattended leg's check 19 fails a run commit that
moves the spec bound.

Each loop also has a target: the count that ends it as `CONVERGED` when it reads zero. A spec audit's
target follows `review.design.rounds`: `highs` under `until-no-high`, `all` under `until-clean`, and
`blockers` under the other three. The closing review's follows `review.follow-up`: `highs` under
`after-high`, `all` under `while-finding` and `blockers` under `never`. `blockers` counts the round's
blockers, `highs` adds its highs, and `all` adds its mediums and lows too. A round's count is its
blockers plus its highs. The closing review also stops `NON-CONVERGENT` when that count does not fall,
or once its rounds pass `flow.route-backs`, default 3. A spec audit runs to its target or its bound.

- **See the bounds:** `python tools/loop/review_bounds.py show` prints <!-- usage: script:tools/loop/review_bounds.py#show e8e581b9 -->
  `max-rounds=<n> spec-bound=<n> closing-bound=<n> follow-up=<value> spec-target=<word>
  closing-target=<word> route-backs=<n> findings=<value> unverified=<value> left-shift=<value>
  blocks=<value>` from the policy file at your default branch's landed
  revision, or at `--rev <rev>`. It exits 2, printing `review-bounds: refused`
  and why, on a refused bound, or `review-bounds: unarmed` where the policy kit is not installed. The
  unattended driver's `--review` reads the same line, and refuses the round on a refusal. Where the
  module or the policy kit is not installed, the driver uses the defaults above and prints a NOTE.
  `python tools/loop/loop_lib.py --check` refuses a bad bound in your committed policy file too.

- **See it on a fixture:** `python tools/loop/review_bounds.py --fixture` runs every case, each in a <!-- usage: script:tools/loop/review_bounds.py f9f7e230 -->
  scratch repository with a policy file of its own: `defaults`, `count-equal`, `count-above`,
  `count-zero`, `max-zero`, `until`, `never`, `while-finding`, `no-driver`, `no-policy-kit`,
  `targets`, `disposal-keys`, `pin` and `opt-in-set`.
  `--plant <case>` runs one. Gov's own `loop review bounds fixtures` gate runs them all.

The bounds do not tell whether a round's recorded counts are true, or whether a raise of a bound was
yours; check 19 grades only a run's own commits.

## How a review fires and what its findings become

A review breakpoint fires through the unattended driver, and four more keys in `.governance/policy.toml`
decide what its findings become. `review_bounds.py show` prints each after `route-backs=`:

- `findings=`, the key `review.findings`, default `blocker-high-own`: how many units the promoted
  findings become. `blocker-high-own` gives each blocker and each high its own unit and batches the
  mediums and lows into one; `all-own` gives every finding its own unit; `blocker-own` gives each
  blocker its own unit and batches everything else.
- `unverified=`, the key `review.unverified`, default `ask`: what happens to a finding no skeptic could
  judge. `ask` files it as an ask in the build's backlog with its evidence, and never makes it a unit;
  `block` has the disposal read the code and promote it at the severity it finds, or refute it; `record`
  lists it in the disposal's summary and files nothing.
- `left-shift=`, the key `review.left-shift`, default `second-occurrence`: which bug classes the review
  disposed earn a gate. `second-occurrence` earns a class an earlier review record already disposed;
  `every-class` earns every class the review named; `owner-selects` names each one as yours to choose.
  The disposal counts them with the workflows kit's `review_dispose.py classes` and files each earned
  gate as an ask.
- `blocks=`, the key `review.blocks`, default `every-review`: whether the build waits for the review.
  `every-review` holds the roster until the review's loop ends; `owed-only` holds it only for a review
  the method owes; `none` never holds it, and the review runs alongside the build.

- **Fire a review:** `bash tools/unattended/unattended.sh --trigger <slug> --subject <s> --cause <cause> --pin <path>` <!-- usage: verb:unattended.sh:--trigger 8ab2e327 -->
  prints one line per review call, the call's preset from the pinned spec or design paths, your
  `review.unclassed` and `review.twin` values, `"trigger"` and a `"reviewPolicy"` of the four keys, its
  `blocks` already `yes` or `no` for this cause. The cause is `owed`, `opt-in`, `recommendation` or
  `placement`. With no `--pin`, a closing diff review's call, it prints one line with no preset. It
  refuses a cause outside the four, a subject whose review loop already ended, and a policy file it cannot
  read, among them a non-empty `review.opt-in`, which no lens map turns into a lens swap yet. It writes
  nothing to the run's record. The build harness takes `trigger` and `reviewPolicy` as its arguments.

A closing review's exit under a `review.findings` value other than the default records the value on its
row, and the unattended leg's check 2 counts the units owed by it. The review's record line carries
`trigger=` with the cause, and `shape=`, `efforts=` and `role-sha=`, which read `-` until a role's shape
supplies them.

## Whether a stage's work should be reviewed

At each stage's exit a command scores whether the stage's work should be reviewed, and for Design the
role that produced the work then answers the same question, why included. Both answers are
`recommendation` records in the build's `build/` folder, named under the build's lowest-numbered unit,
and two keys in `.governance/policy.toml` say what they mean:

- `review.recommendation`, default `advice`: `advice` never binds; `binding` binds every
  recommendation; `binding-above-tier` binds only a build whose units include a Tier-2 spec.
- `review.recommendation.source`, default `scored-signals-and-reasoning`: what decides. Under it the
  score decides Build, and Design's reason decides Design. `agent-judgment` leaves Design's score
  `none`, so the reason alone decides. `signals-only` takes no reason, and the score decides.

The score reads your build README's generated units region. Design scores `review` when the build has
two or more units or a spec with an unresolved open question, and Build when it has two or more units
or a Tier-2 spec; otherwise `no-review`. Plan, Test and Deploy score `unarmed`, never `no-review`,
because nothing they produce is read for a signal yet. One `[review]` table cannot set both keys, so
`binding` under `signals-only` cannot be declared until the catalogue renames one of them.

- **Score a stage:** `bash tools/unattended/unattended.sh --recommend <slug> --stage <stage>` writes <!-- usage: verb:unattended.sh:--recommend 7c91eefd -->
  the score record and stages it, and prints one line: the stage, the score, the signals, the source,
  whether it binds and the record. The stage is `plan`, `design`, `build`, `test` or `deploy`. Where
  Design's reason decides, it names the next step: spawn `gov-spec-writer` through
  `handoff.py render --role gov-spec-writer`, hand it that line and the question, and record its answer.
- **Record Design's reason:** `bash tools/unattended/unattended.sh --recommend <slug> --stage design --reason <why> --verdict review`
  writes a reason record answering the newest Design score, with `review` or `no-review` as its score.
  Where the deciding record reads `review` and binds, the verb prints the `--trigger` call that fires the
  review, with the subject `<slug>-specs` for Design and `<slug>` for Build.

It writes nothing, and exits 1, for a stage outside the five, a `--reason` without `--verdict` or the
reverse, a verdict other than `review` or `no-review`, a reason for any stage but Design or under
`signals-only`, and a reason with no Design score to answer. It exits 1 too when the policy kit or the
record kit is not installed, or refuses a value, such as a reason holding a line break. A build whose
units region names no unit gets the line and no record. The answer is recorded and never acted on: the
spec audit's opt-in stays yours.

## Where a build stops for a review or for you

A breakpoint is a place at an item boundary where a build stops, before, at or after an item, for a
reviewer or for you, the owner. Reviews and owner gates are one list, and four keys in
`.governance/policy.toml` place them:

- `review.<stage>`, one per stage: `off` places no review, `opt-in` places one only where the build opts
  in, `owed` always places it, and `owed-above-tier` places it where one of the build's specs is
  Tier-2. Plan's review sits before `item.plan.exit`, Design's spec audit after `item.design.reason`,
  Build's closing review after `item.build.recommend`, Test's gate review before `item.test.exit` and
  Deploy's landing review before `item.deploy.notify`. Build defaults to `owed` and the others to
  `opt-in`. Only Design has an opt-in of its own, the build README's `spec-audit:` key, which
  [the spec audit page](spec-audit.md) describes.
- `autonomy`, default `plan-only`: an owner gate at `item.plan.exit`. `three-gates` adds one at
  `item.design.exit` and one before `item.deploy.mandate`; `every-stage` adds one at each stage's exit
  item besides.
- `review.breakpoints`, default empty: each item tag you list places a review before that item. A tag
  the build's items do not declare is refused, naming the key and the tag, and a renamed tag follows
  its item.
- `decisions.major`, default `author-rubric`: under `author-owner-ratifies`, a build whose specs carry
  a fork an agent resolved under delegation, marked `RESOLVED (agent, <date>, delegated)`, gets an owner
  item at `item.build.ratify`. No fork records its class yet, so every such fork counts as major.

The plan gate is released by the build README you landed, which authorizes the run. Every other owner
gate stays `held` until your disposition record names its item, written as
[the owner's disposition record](#the-owners-disposition-record) above shows with `--item` the gate's
tag. While one is held, the unattended driver's `--close` refuses, naming each held item and how to
hand the question to you. Under the defaults nothing new is held.

An owner gate holds only a build opened after the gate was placed. Where the commit that first added your
build's README does not contain the commit that first added the loop kit's `breakpoints.py`, every owner
gate of that build, the plan gate included, reads `passed before placement` instead, so a run already in
flight when the module landed is not held for positions it crossed before the gate existed. The owner item
and the review lines keep their answers. Where either commit cannot be found, a README not yet committed
for one, the gate holds as above. Where an owner gate reads `held` and no commit adds the README under the
memory root, the list ends with one more line,
`breakpoints: held · no commit adds <path> · root from <.unattended.conf|.memory-tree.conf|default>`, the
README path it looked for and the conf the root came from: your `.unattended.conf`'s `MEMORY_ROOT` where
that file exists, as the unattended driver reads it, else your `.memory-tree.conf`'s. A misread root
shows instead of reading as an ordinary hold; a build with no held gate prints no such line.

- **List a build's breakpoints:** `python tools/loop/breakpoints.py list --build <slug>` runs at your <!-- usage: script:tools/loop/breakpoints.py#list 74c047ff -->
  repository's top level and prints one line per breakpoint, in item order:
  `breakpoint: <name> · <before|at|after> <item tag> · <reviewer|owner> · <cause>`, and for an owner
  line ` · authorization`, ` · held`, ` · released <record> <word>` or ` · passed before placement`.
  `--spec-audit` lists Design's opted-in audit, and `--delegated-fork` the owner item. The unattended driver's `--plan <slug>` prints
  the same lines after its `frontier:` line. It exits 2 printing `breakpoints: refused` and why on a
  value outside its key's set or an undeclared tag, and `breakpoints: unarmed` where the policy or
  memory-tree kit is not installed.
- **Read one stage:** `python tools/loop/breakpoints.py stage --stage <stage> --build <slug>` prints <!-- usage: script:tools/loop/breakpoints.py#stage 1a9b01b0 -->
  `breakpoints: stage <stage> · <value> · <owed|opt-in|not-owed>`, read from the policy file at your
  default branch's landed revision, or at `--rev <rev>`. The unattended driver's preflight reads
  `design` this way to decide whether the build owes a spec audit.
- **See it on a fixture:** `python tools/loop/breakpoints.py --fixture --plant <case>` runs one case in <!-- usage: script:tools/loop/breakpoints.py bd781c1c -->
  a scratch repository: `values`, `placed`, `ratification`, `stage`, `driver-close`, `driver-optin`,
  `driver-plan`, `pre-placement`, `driver-pre-placement`, `pre-placement-records-root`, `unattended-root`,
  `confs-disagree`, `readded`, the module taken out of a scratch repository and committed back, its
  placement still the first commit that added it, or `no-own-conf-read`, the one that reads the module's own file and no scratch
  repository, naming each conf name or conf reader call in its code. `--selftest` runs them all, and gov's own `loop breakpoint fixtures` gate runs them.

The list does not fire a review: you, or the run, fire each review line through the driver's
`--trigger` with its cause. A run may still move past an owner gate before its close, and anyone who
can write a disposition record releases a gate.

## Placing a request: a disposition, its reason and its check

Every request a session or an unattended run receives gets one disposition from the loop's closed set,
`continue`, `amend`, `new`, `patch`, `repeat`, `unit`, `breakpoint`, `ask` or `none`, recorded with its
reason. The tool is `placement.py` in the loop kit, run in your repository, keyed by the request's
content key, the one `--request <file>` of the unattended driver prints. Each placement is a block
appended to `<key>.placement` in your git directory's `requests/` store, which is never pushed: the
newest block is the placement and the earlier ones are its history. Its `reason` and `evidence` are
redacted of secrets and cut to the module's `VALUE_CAP`, since those lines reach the claim commit.

Who places is the key `placement` in `.governance/policy.toml`:

- `agent-places`, the default: the orientation scout's return is the placement, given as
  `placement.py place --request <key> --return <file>`, a file of `disposition`, `build`, `playbook`,
  `reason`, `evidence`, `observations`, `scenarios` and `facts` lines, the fields of the scout's
  `return:` template under its `placed` outcome, and `breakpoint` for a `breakpoint` disposition.
- `declared-checked`: the request's own declaration is, `placement.py place --request <key> --declared
  <word> [<build>]`, and the scout's return is evidence only.
- `owner-places`: `place` writes no disposition and prints the scout's return as evidence and
  `placement: owner item — <key>`; your disposition record naming `item.entry.place-owner` is the
  placement, read by `placement.py place --request <key> --owner <record>`.

An alias is written as the member it means, `attach` as `amend`, and any other word is refused with no
block written. Where the return names an observation and `probe.observations` reads
`verify-before-place`, `place` opens a probe for it first, and the check below waits for its verdict.

**The check**, `placement.py check --request <key>`, re-reads every fact the disposition rests on from
its source, never from the scout's text: the build exists and is live, and its build lease is free or
yours, for `continue` and `amend`; the request's words are held for `new`; the build is terminal for
`patch`; the playbook is in the tree for `repeat`; the ask is filed for `ask`; your session card routes
no unit for `none`; and for `breakpoint`, the block's `breakpoint:` line names one review, `spec audit`,
`gate review`, `closing review` or `landing review`, or `item <tag>` for a tag the build's composed rows
declare, the build is live, and the request is your own words, typed in this session on this machine:
the unattended driver's `--request-consent` answers for it, and a request that reached you by its
record's id alone is refused `relayed`. `unit` is refused until units can be held apart from their
build's driver. The key `placement.check` says what a failed fact does:
`refuse`, the default, prints `placement: refused — <disposition> · <fact>` and exits 1, back to placing;
`record` writes the failure into the block and exits 0. A passed `new`, `amend`, `patch` or `repeat` is
then held for you, `placement: held-owner`, while the Plan or Design item it enters is unbuilt, and once
its claim exists the owner item names `refs/gov/claims/<slug>`; your disposition record of that build
naming `item.entry.place` with the placement's own word releases it, and any other word refuses it,
back to placing.

**The scenarios**, chosen once here. The scout's return names `scenarios`, each scenario it finds
admitted joined by `+` (`scenario.feature+scenario.design-only`), and `facts`, the request facts it read
as `<name>=<value>` pairs joined by `; ` (`design-only=true`), each name and value one lower-case word;
any other shape is refused at `place` with no block written. The `entry` fact is never taken from the
scout: `new` is `entry=feature`, `amend` `entry=amendment`, `patch` `entry=patch` and `repeat`
`entry=playbook-run`, and a typed `entry` that disagrees fails as `entry-mismatch <typed> <derived>`.
The check then re-runs the selection of "Choosing a build's scenario" above over those facts and your
composition at HEAD: a named scenario whose predicate fails is `scenario-predicate <tag>`, an admitted
one the scout left out `scenario-missing <tag>`, and the same scenarios in another order
`scenario-order`. Each failed fact prints its own line, so one round trip names them all, and
`placement.check` treats them as it treats the others; under `record` the block's `scenarios` is
rewritten to the selection. Where no scenario admits the request, the default is the selection,
written `scenarios: scenario.feature (default)`, and a return naming none passes. The other
dispositions open no build and select no scenario, so a return naming one for them fails as
`scenario-not-placed`. The check prints `placement: facts — <facts>`, the facts it evaluated, and where
your tree has no scenario composition it prints `placement: scenario · unread · <why>` and checks none;
a default naming no composed scenario refuses the check, exit 1.

**The record**, `placement.py record --request <key>`, prints the passed block's `disposition`,
`build`, `playbook`, `reason`, `scenarios` and `facts` lines, with `reenters` after `disposition` for an
owner's late answer, the lines the claim commit carries; a block whose check did not pass prints nothing
and exits 1.

**Asking for a review on a live build.** When you ask mid-build for a review, "audit the specs" say, the
request is placed as `breakpoint` with `build: <slug>` and `breakpoint: spec audit` in the scout's
return, and once its check passes, `placement.py breakpoint --request <key>` declares it on the build:
it writes your disposition record into the build's `build/` folder, `Item` `item.entry.place`,
`Disposition` `breakpoint`, `Channel` `prompt` and `Reason` `<name> · request <key>`, naming the request
by its key and none of its words, for you to commit, and prints `placement: declared — breakpoint <name>
· <slug> · <record>`. A build whose lease another machine holds is refused `live-holder` and nothing is
written. Once committed, `breakpoints.py list` and the driver's `--plan` list it beside the build's other
breakpoints: a placed `spec audit` after `item.design.reason` with cause `owed`, since it makes the
pre-code audit owed, the driver's preflight reading it at BASE as the source `placement`; the other
three reviews at their own positions and `item <tag>` before that tag, cause `placement`. The run fires
each at its position through `--trigger`. Where the build is already in a step past the position,
`breakpoint` fires it at once, `--trigger <slug> --subject <s> --cause placement`, the subject
`<slug>-specs` for `spec audit`, `<slug>` for `closing review` and the position's item tag otherwise.

**An unattended prompt is placed the same way.** Before its build folder is written, the prompt is
recorded, placed and checked, and the passed block is written under `## Placement` in the prompt record,
its `request: <key>` line first. A prompt-mode run's first preflight refuses at check 119 a record with
no such section, a disposition that opens no build, or a block the check refuses, so a prompt that
continues or amends a live build is sent there rather than opened as a new one. A README opened before
`PROMPT_BRIEF_CUTOFF` is not graded.

## The entry items: orienting, placing and claiming a request

Before any step, a request passes through the entry program: five items tagged `item.entry.<name>`, which
sit in no step, as the review and probe programs' items do, and which `--check` prints as
`loop: program entry`.

| Item | Actor | Needs | Its work today |
|---|---|---|---|
| `item.entry.orient` | `role:gov-orienter` | none | the `/session-kickoff` orientation and its card; where the card routes a build, that build's card |
| `item.entry.place` | `role:gov-orienter` | `item.entry.orient` | the scout's return, placed by `placement.py place --request <key> --return <file>` and checked by `placement.py check` |
| `item.entry.place-check` | `command:entry.place-check` | `item.entry.orient` | the request's own declaration, `placement.py place --request <key> --declared <word> [<build>]`, then `placement.py check` |
| `item.entry.place-owner` | `owner` | `item.entry.orient` | your disposition record naming `item.entry.place-owner`, read by `placement.py place --request <key> --owner <record>` |
| `item.entry.claim` | `command:entry.claim` | any one of the three placing items | the unattended driver's `--entry-claim`, which claims the build on `refs/gov/claims/<slug>` |

`item.entry.orient` answers the value of the policy key `placement`, `agent-places`, `declared-checked`
or `owner-places`, and each value routes to the placing item it names; its `probe` goes to the probe
tool's stand-in, as every role item's does. It reads the whole map (`map = "base"`).

The three placing items answer a disposition and share one route table. `new`, `patch` and `repeat` go
to `item.entry.claim`; `breakpoint` to `item.review.trigger`; `unit` back to `item.entry.place`,
drawing `route-back` on the rework budget; and the dispositions whose owners have not landed go to
today's tools: `amend` to `placement.py`, which holds it for you, `continue` to the unattended driver,
`ask` to `backlog.py` and `none` to the orientation scout. A failed `placement.py check` is the
item's refusal and goes back to it. Your placement waits on you until `run.owner-deadline` passes, and
then becomes an `ask`.

`item.entry.claim` answers one word per exit of `--entry-claim`: `claimed` moves the build, a `new` into
planning and a `repeat` into designing, while a `patch` moves through `item.plan.dedupe`'s `patch`;
`slug-taken` comes back to the claim for a fresh slug, drawing `route-back` on the request's pre-claim
budget; `awaiting` comes back to the claim while another party holds the build, drawing nothing, until
`flow.wait-ceiling` passes and it answers `refused`; and `refused` goes to `backlog.py`, the `ask:`
line or owner item the driver prints.

## Testing outside Test: the probe program

A probe is a test any item can ask for, outside the Test step: an owner's observation checked before it
is placed, a reported bug made red before its fix, or an experiment that sets a measured reference. Its
eight items, `item.probe.trigger`, `.pin`, `.design`, `.experiment`, `.run`, `.judge`, `.judge-claimed`
and `.return`, sit in no step, as the review program's do, and `--check` prints them as
`loop: program probe`.

A probe has two ways in. It is **placed** at an item boundary, by a point `probe.points` names or by
you; or it is **raised** by a role whose item answers `probe`, an outcome every role item outside the
probe program carries, routed to the probe tool. No role returns `probe` until the role templates
carry it, so today probes are placed, never raised. Four keys in `.governance/policy.toml` decide what
opens:

- `probe.points`, default empty: the item tags where a probe opens with the cause `point`. A tag the
  build's items do not declare is refused by `probe.py points --build <slug>`, naming the key.
- `probe.raise`, default `roles-and-owner`: `owner-only` refuses a raised probe, and `off` refuses
  yours as well.
- `probe.observations`, default `verify-before-place`: where an owner's observation is probed,
  at `item.entry.place` under `verify-before-place`, at `item.plan.input` under `verify-at-plan`, and
  nowhere under `on-request`, where you open the probe yourself with the cause `owner`.
- `probe.experiment.authority`, default `within-cap`: named, with its value, on the owner item an
  experiment routes to while the experiment shape is unbuilt; `within-cap` is the agent cap the hooks
  kit enforces.

A cause outside `point`, `owner`, `observation`, `raised` and `reproduction`, the rows of the
definition's `[[trigger-cause]]` table, is refused. A patch build's `reproduction` always opens.

The tool is `probe.py` in the loop kit, run in your repository, one verb per item it serves:

- **`trigger`**, `probe.py trigger --cause <cause> --asker <item tag> --subject <text>` with `--build <slug>
  --unit <id>` or `--request <content key>`, and `--at <item tag>` for a point or an observation, opens
  the probe and writes a `probe-trigger` record in the build's `build/` folder, or,
  given a request's content key before any build folder exists, `<key>.probe-trigger.md` beside the
  request's text in your git directory's `requests/` store, which is never pushed. A second
  observation of the same request joins its open probe and prints `probe — joined`; once that probe
  has returned, a later trigger opens the next one, `<key>.probe-trigger-2.md` with its probe
  `<key>.probe-2.md`, and the returned verdict is never written over. A refused cause writes
  nothing and prints `probe — not opened · <key>: <why> · to <asker>`.
- **`pin`**, `probe.py pin --trigger <record> --sha <commit> --kind verification|reproduction|experiment
  --question <text> --losing <text>`, writes the `probe` record's head, the commit, the kind, the question and the losing
  outcome, before anything runs, and commits it alone as `probe pin(<asker>): <kind>`; a request's
  head stays in the store, uncommitted, so its git blob is written to the trigger record as `Head`,
  and `run` refuses, exit 2, a head edited since. A commit that does not resolve exits 2. An experiment routes to the owner
  item naming dBoundRoles, which builds its shape.
- **`design`**, `probe.py design --probe <record> --cmd <command> --expect <exit>:<hash>`, with `--mark
  visual` or `--mark "judge claimed"`, appends one `- method · <exit>:<hash> · <command>` entry to the record's `## Method`
  section, the prediction made before anything runs. Once `run` has written a run line the method is
  frozen and `design` exits 2, leaving the record as it was.
- **`run`**, `probe.py run --probe <record>`, re-runs every entry at the pinned commit through `loop_witness.py rerun` and writes one
  `run · <exit> · <hash> · <command>` line each. An entry marked `visual` needs a capture adapter not
  yet built, so nothing runs and the record reads `Verdict: unrunnable`.
- **`judge`**, `probe.py judge --probe <record>`, computes the verdict from the run lines against the predictions: `confirmed`, `refuted`
  or `inconclusive`, with `Judged: computed`. An entry marked `judge claimed` is written
  `Judged: claimed` with no verdict, and goes to you rather than to a gate.
- **`return`**, `probe.py return --probe <record>`, writes `Writer: stand-in` and prints `probe — <verdict> · <record> · to <asker>`, the line
  the asking item is re-entered with; a claimed or unrunnable probe goes to you instead.

No probe verdict gates a landing: only Test's verdict does.

## How much rework a build may do

Every build has one rework budget, the policy key `flow.rework-budget`, and every repetition draws on
it: a route back to an earlier step, a fix pass, a review round after a subject's first, a unit
dispatched again, and the first round of each spec-set generation after the first. The value is
`<base>+<per-unit>`, default `4+2`, or a bare count such as `6`, which is a base with no per-unit share.
Any other shape is refused, naming the key. Raising it is yours, the owner's: the key loosens as it
rises, so an agent's run never writes it.

The budget freezes at Design's exit. When a build moves from `designing` to `building`, its total
becomes the base plus the per-unit share for each unit its specs define then, written once as
`budget · frozen · <units> unit(s) · <total>` in that move's transition record. A unit minted after
the freeze adds nothing, and a route back into building does not re-size it. A build that has recorded
no move freezes at its first draw made while it has a spec, counting its units then. Before that, its
total is the base.

Each draw is one row, `draw · <cause> · <item> · <spent>/<total> · <draw-id>`, in the build's newest
transition record, committed on its own. The draw id, a UTC time to the second then six random hex
digits, such as `20261024T153012Z-4fa1c9`, is minted once per draw and written on every place the row
goes, so two worktrees making the same draw on the same item still write two different rows. Rows
carrying one id count as one draw. A row written before draws carried an id counts as its own draw, and
a row whose last field is neither the figure nor a draw id is refused as outside the grammar. Before the build's first record, the rows go in its `RUN.md`, and the
first record copies them. Once spent equals the total, the next draw writes nothing and answers
`exhausted`; what the build does then is `flow.on-exhausted`'s. A spec audit's round is still recorded
when the budget is spent, and ends at its target or its bound; the closing review's round and a
dispatch are refused. A patch build draws on the build it patches, as `patch:<its slug>`.

A `transitions.record` set without `log` keeps the budget too. A build that already has a transition
record keeps drawing into its newest one, and a move that draws stages the row into its own commit. A
build with no record keeps a move's rows on that move's trailer where the set holds `trailer`, as
`budget=frozen@<units>@<total>` and `draw=<cause>@<item>@<spent>+<total>`, and otherwise in its
`RUN.md`, where a draw made through `budget.py draw` goes as well. The trailer's `draw=` carries no
draw id: its commit is its identity, and two such draws are two commits. A patch build's draw on a
build with no record goes in the patch build's own `RUN.md`, as the row, its draw id included,
followed by ` · budget <slug>`, and counts
for the patched build `<slug>` alone. These rows are read oldest first by their time, and the build's
first record copies them. A `RUN.md` that `--preflight` has rotated to `RUN.<phase>.<blob8>.md` keeps
counting, an aborted run's included, and so do a patch build's rows in its own rotated records.

A row's `<spent>` is what its writer counted when it wrote the row. Two worktrees drawing at once each
count their own, so after a merge two rows can both read `1/4`. The count is re-derived from the rows
alone, so it reads 2 there. A draw whose build holds such a row prints, after its verdict line, one
`loop: budget · disagrees · <row> · typed <a>, derived <b>` line per such row. The line refuses nothing,
and the verdict stays the first line, the one the unattended driver reads. Gov's own `.gitattributes`
merges transition records with git's built-in `union` driver, so both appended rows survive a merge
instead of conflicting. Union keeps two byte-identical rows once, and the draw id is what keeps two
parallel draws apart: their rows differ by the id, so the merge keeps both.

Contention draws nothing: a verdict staled by another build's landing, a merge conflicted by another
build's landing, a wait on a lease another build holds and an unreachable remote are re-run in their
turn and spend none of this build's budget. `flow.route-backs`, default 3, counts one item's draws:
past it, that item's loop is non-converging, though a spec subject's review rounds never end its loop.

**Before a build exists, a request has a budget of its own**, keyed to its content key, so a request
that loops at entry stops too. Its total is the base of `flow.rework-budget`, 4 by default (PINNED): a
request has no units and nothing freezes, and the build it becomes later starts a budget of its own.
Its rows live on the request's record `refs/gov/requests/<content key>` on your remote, one commit each,
so a request another machine takes over keeps its count. `placement.py place` draws one lap before it
writes a block that repeats an earlier placement: `route-back` once any of the request's blocks was
refused by its check, and `research` when the request's probe record has come back since its last
block; the claiming step draws `route-back` on `item.entry.claim` before each fresh slug. The draw
prints its row, and once the budget is spent `place` prints `placement: pre-claim budget exhausted —
<content key> · <spent>/<total>`, exits 3 and writes no block. Only you can place it then: a placement
under `--owner <record>` draws nothing and is written past a spent budget. A remote that does not
answer, or a race lost to another machine four times (PINNED), draws nothing, and `place` exits 2 with
no block, so you place again once it answers.

- **Draw on a budget:** `python tools/loop/budget.py draw --build <slug> --cause <cause> --item <item>` <!-- usage: script:tools/loop/budget.py#draw 7c651ac5 -->
  runs at your repository's top level. It prints `loop: budget · drawn · <row>` and exits 0,
  `loop: budget · exhausted · <slug> · <spent>/<total> · flow.on-exhausted` and exits 3, or
  `loop: budget · refused` and why, exit 2, for a cause outside `route-back`, `fix-pass`,
  `review-round`, `re-dispatch` and `research`, a `patch:` cause given, which is derived, a build with
  no record and no `RUN.md`, so no home for the row, or a patch build with no `RUN.md` of its own where
  the build it patches has no record and the set has no `log`. The unattended driver draws through it
  on `--review` and `--dispatch`. After a draw appended to a transition log record it reads that
  record's merge rule once, and where `git check-attr merge` answers anything but `union` it prints,
  after the verdict, `loop: budget · notice · <record> merges as <answer>, not union: add
  <MEMORY_ROOT>/builds/*/build/*-transition-*.md merge=union to .gitattributes`. Add that line to your
  `.gitattributes`: two worktrees drawing on one build each append a row, and only a union merge keeps
  both. The draw stands either way.
  For a request, `--request <content key>` or `--request-text <file>` takes the place of `--build`,
  with `--rows <file>` holding the request record's messages as the driver's `--request-draw` hands
  them over; the text form computes the key from the request's words, so it needs no record of them.
  It writes nothing, prints `draw · <cause> · <item> · <spent>/<total>` (exit 0) or `exhausted ·
  <spent>/<total>` (exit 3), names on stderr any row it cannot read and does not count it, and refuses
  a cause as above.

- **See a patch build's origin:** `python tools/loop/budget.py origin --build <slug>` runs at your <!-- usage: script:tools/loop/budget.py#origin 2f439620 -->
  repository's top level and prints `loop: budget · origin · <slug|none>`, the build whose budget a
  patch build's draws land on, `none` for any other build, exit 0. Before a patch build draws, the
  unattended driver reads the run claims and asks it of each live claim but its own; where another live
  run is a patch of the same origin, the draw is refused naming that run, its node and the origin, and
  nothing is drawn. A claim read that fails refuses the draw too, `budget: patch draw refused — claims
  unread: <why>`, since a run it could not see may be drawing on the same origin, and nothing is drawn; a
  claim whose origin does not read draws as before.

- **See the value:** `python tools/loop/budget.py value` prints `base <n> per-unit <n>` from the policy <!-- usage: script:tools/loop/budget.py#value 689b423c -->
  file at HEAD, or refuses a value of another shape naming the key.

- **See where open work goes:** `python tools/loop/budget.py target --build <slug> --item <item>` <!-- usage: script:tools/loop/budget.py#target d06981ab -->
  runs at your repository's top level and prints `loop: budget · target · unit` while the budget
  remains, or `loop: budget · target · on-exhausted` once it is spent. It draws nothing. The unattended
  driver reads it after a round's draw: a closing review's exit that promotes records ` · to units`,
  or ` · to asks` once the budget is spent, and files its findings as asks in the build's
  `BACKLOG.md`. A spec audit's exit always records ` · to units`.

- **Record a fix pass:** `bash tools/unattended/unattended.sh --fix-pass <slug> --unit <id> --reds <n>` <!-- usage: verb:unattended.sh:--fix-pass 3696cb6a -->
  records one fix pass against a unit's acceptance, `<n>` the count of its criteria still red after
  the pass. Two passes whose reds do not fall end the loop `NON-CONVERGENT`, and so does a pass past
  `flow.route-backs`. The ending pass records ` · to units` while the budget remains, or
  ` · to on-exhausted` once it is spent. A unit whose fix-pass loop ended takes no further fix pass and
  no dispatch.

Once the budget is spent, the build ends and never laps again. The policy key `flow.on-exhausted` says
how. `best-effort-ending`, the default, takes the ending your units support: `land-green` where every
unit not `WONTDO` is `CLOSED`, `descope` where some unit is `CLOSED`, and otherwise `close-incomplete`,
so a build with no units lands nothing. `park-for-owner` hands the build to you, and
`close-incomplete` closes it incomplete, its branch and records kept. Each ending is a row of the
build's transition table, on the item `@any` with the ending as its outcome, and none of them draws on
the budget:

| Row | From | Outcome | Fact | To |
|---|---|---|---|---|
| E1 | planning, designing, building, testing or deploying | `close-incomplete` | before the push | `incomplete` |
| E2 | the same five | `park-for-owner` | | `parked` |
| E3 | `parked` | `disposed` | your disposition `continue` | the state it was parked from |
| E4 | `parked` | `disposed` | your disposition `none`, before the push | `incomplete` |
| E5 | `testing` | `descope` | | `building` |

No ending raises `flow.rework-budget`: raising it stays yours.

- **See the ending:** `python tools/loop/budget.py ending --build <slug> [--explain]` runs at your repository's top <!-- usage: script:tools/loop/budget.py#ending f7f47c38 -->
  level and prints `loop: budget · ending · <ending|none> · <open|unfrozen|spent> <spent>/<total> ·
  open <ids|none> · disposed <word|unrecorded>`, exit 0. The ending is `none` until the budget is
  spent, the ids are the units whose status is neither `CLOSED` nor `WONTDO`, and `disposed` is the
  word of your newest disposition record of the build's exhaustion item. It refuses a value outside
  the three, exit 2. With `--explain` it first prints `loop: budget · root <root> · from
  <.unattended.conf|.memory-tree.conf|default>`, the records root and the conf it came from, then one
  `loop: budget · read <path>` line per file the rows were taken from, or `loop: budget · read none`,
  then one `loop: budget · no draw id · <row>` line per draw row written before draw ids, each counted as
  its own draw, so a count of zero read under the wrong root shows where it looked.

- **End a spent build:** `bash tools/unattended/unattended.sh --exhausted <slug>` records the ending <!-- usage: verb:unattended.sh:--exhausted 40c08fe9 -->
  once, as a `decision` row the wrap-up shows you, and prints what comes next: `close-incomplete`
  files each open unit with `--rescope <slug> --act defer` and then runs `--abort <slug> --code
  budget-exhausted`, which is refused while an open unit has no deferral; `park-for-owner` hands off
  with `--handoff <slug> --code owner-decision`; `land-green` and `descope` go on to `--close`. A second
  call prints the recorded ending and writes nothing, and a budget not yet spent is refused. Once the
  budget is spent, a refused review round or dispatch tells the run to call it.

A parked build resumes only after you record a disposition of its exhaustion item, `continue` to go
on, or `none`, after which the run ends it through the same abort:

<!-- run: no — runs a kit by its path in gov's checkout, absent from a scratch adopter, and carries a placeholder the shell reads as a redirect -->
```bash
python tools/memory-tree/build_records.py new disposition --build <slug> --unit <unit-id> --item item.flow.on-exhausted --disposition continue --channel terminal
```

- **See it on a fixture:** `python tools/loop/budget.py --fixture --plant <case>` runs one case in a <!-- usage: script:tools/loop/budget.py 8248cc63 -->
  scratch repository, and `--selftest` runs them all. Gov's own `loop budget fixtures` gate runs them.

The budget does not serialize two draws made at once, which are two rows. The ending reads each unit's
status header and not its derived state, and anyone who can write a disposition record releases a
parked build.

## Whether a build's flow can finish

Before a flow runs, one check asks whether it can finish. It reads the composition: gov's definition
with your overlay's items and stages, and for a build, the scenarios it was placed under and its own
applied flow changes. Six rules hold it:

- **`terminal`:** every state of the build, feature and unit levels reaches its own level's terminal
  set, `deployed` for a feature or a unit. A row into `@prior` or `@reentry` counts as reaching every
  open state. A level that declares no states is a finding.
- **`reachable`:** every item of every program is reached from some program's entry, an item with no
  needs. The walk follows every route, and follows a need only inside one program, so an item needing
  another program's item is reached only if some route names it.
- **`counted`:** every loop of the build table and of the item routes passes an edge that ends it.
  That is a backward build row, which draws on the rework budget, a route whose outcome `draws` names a
  budget cause, an ending row, a row into `@prior` or `@reentry`, an owner's item, or a wait an item
  declares on itself. A stage whose exit routes back to its own first item with no `draws` is a finding,
  even though every state still reaches a terminal.
- **`wait`:** an item that waits declares its `deadline` and `on-deadline`.
- **`raise`:** a loosening your build applied names your release, ` · disposition <stem>` on its
  `flow-state` row. One with none was applied without you.
- **`decline`:** a loosening held for you recommends the decline, ` · recommend decline` on its row.

A wait or a loop whose bound a build not yet landed will declare stands on the shrink-only list
`tools/loop/termination-pending.txt`, naming that build, and the check passes it. Checking gov's own
composition also reports a row on that list that is no longer owed: its build has landed, its item
now declares its deadline or is gone, or its loop no longer exists. The check runs at the push, through
gov's `loop termination` gate, and at every step boundary where your build applies a flow change.
There a finding refuses the move and names it, and nothing is recorded. A change that leaves a program
the definition's check refuses is refused the same way.

- **Check the flow:** `python tools/loop/termination.py check` checks gov's composition at your <!-- usage: script:tools/loop/termination.py#check 84d96b33 -->
  repository's top level, and `--build <slug>` checks that build's at its pinned composition. It prints
  the value of `flow.wait-ceiling`, the pending list's counts, each finding as
  `loop: termination · <rule> · <subject> · <why>`, and a summary. It exits 0 with no finding, 1 on a
  finding, and 2 where a composition does not read or a kit is not installed, naming why. `--selftest`
  also checks every live build, one whose newest move entered no terminal state, then runs every plant.

- **See it on a fixture:** `python tools/loop/termination.py --fixture --plant <case>` runs one planted <!-- usage: script:tools/loop/termination.py e4ce3401 -->
  break and prints `held` or `MISSED`: `stage-self-loop`, `stage-self-loop-drawn`, `dead-end`,
  `unit-dead-end` (a unit state no row leaves), `orphan-item`, `empty-states`, `wait-no-deadline`, `wait-declared`, `wait-stale`, `stale-build`,
  `raise-unattended`, `raise-released`, `raise-held` and `decline` in memory, and `deadline-patch` and
  `boundary` each in a scratch repository.

The check trusts `draws` and `waits` as written, so a wrong mark hides a loop. It does not see a wait
outside the flow, one that lives in code with a deadline of its own.

## How to use it

- **Read the loop:** `python tools/loop/loop_lib.py --check` prints one line per step and per <!-- usage: script:tools/loop/loop_lib.py a3a33b34 -->
  workflow with its order, step and reach word, then the dispositions and one line per alias. It
  prints one `loop: program` line per step, with its items in an order where each comes after the
  items it needs, then a `loop: program review` line for the review program, whose items are tagged
  `item.review.<name>`, carry the step `none` and sit in no step, and the same for the probe program
  and the entry program, `loop: program probe` and `loop: program entry`. Where the playbook kit is not installed, a `loop: inputs unarmed` line comes first
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
  loop: program review · 6 item(s) · item.review.trigger item.review.pin item.review.report item.review.cost item.review.dispose item.review.fold
  loop: item item.plan.place · command:plan.place · inputs from item · allowance the plan view from item · returns from item
  loop: item item.build.unit-pass · role:gov-builder · inputs from role:gov-builder · allowance product from role:gov-builder · returns from role:gov-builder
  loop: item item.design.inventory · role:gov-architect · pending · the roles kit holds no gov-architect role
  loop: items · 67 read · 8 pending · 0 unarmed
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
  `needs-cycle`, `step-none-outside-review` (a step's item given the review program's step `none`),
  `review-step-named` (a review item given a step), `needs-unresolved`, `outcome-unrouted`,
  `route-unresolved`, `input-no-layer` and `exit-missing`. The actor cases are `actor-two` (two actors on one item), `actor-bad-kind`,
  `witness-missing` (an item with no witness), `allowance-missing` (a command item with no
  allowance), `role-copy` (a role item repeating its role's allowance), `role-widen` (a role item
  given a wider allowance), `role-pending` (a role the roles kit does not hold, which prints `pending`
  and exits 0) and `roles-no-kit` (the roles kit looked for in an empty scratch folder, so every role
  item prints `unarmed` and it exits 0). Two cases run `--scopes` after the read and exit 0 when it behaves:
  `scope-selected` scopes one unit to one item in a scratch file and shows it on that item's line
  alone, and `scope-no-kit` looks for the playbook kit in an empty scratch folder and shows every line
  `unarmed`. The computed-witness cases are `computed-actor` (the item the `acceptance` row serves
  given the `actor` class) and `computed-unserved` (the row serving an item the file does not
  declare). The case `conf-readers-declared` reads no definition: it finds each function of the loop
  module that builds a conf path and opens it, and exits 1 naming one that is declared neither a
  conf reader nor a route, or a declared one that no longer opens a conf. Six more cases each run that
  comparison over a scratch copy of the loop module with one change, and each exits 1 on the refusal
  it must draw: `conf-opener-literal`, `conf-opener-constant` and `conf-opener-local` add a function,
  declared nowhere, that opens a conf by its literal name, through a module constant or through a
  local name; `conf-route-opens-none` empties the route; `conf-openers-none` empties every declared
  opener; and `conf-module-unparsable` adds a definition that does not parse. The files on disk are never changed. `python tools/loop/loop_lib.py --selftest` runs every
  case and holds each to the exit and line it owes, one `PASS` or `FAIL` line per case and a summary;
  gov's own `loop definition fixtures` gate runs it, with no guard, so every bar runs these cases.
- **Check the re-run stand-in:** `python tools/loop/loop_witness.py --fixture --plant acceptance` runs <!-- usage: script:tools/loop/loop_witness.py 6de87be4 -->
  one case in a scratch repository and exits 0 when it holds. The cases are `acceptance` (a unit's
  commands re-run at its commit while an uncommitted edit sits beside them), `acceptance-malformed`
  (records typed by hand, with no run line or a writer outside `executor` and `stand-in`, each read
  as malformed), `probe-rerun` (`confirmed` at the pinned commit, `refuted` at a later one,
  `inconclusive` at one that does not resolve), `hold-inherited`, which preflights a run through
  the unattended driver and holds it under `inherited-red` over an `OWN` leg, an untied bar and an
  `INHERITED` one, `bash-syntax` (a command only bash can run, re-run with exit 0 and the hash of its
  `0`) and `timeout-grandchild` (`sleep 30 & wait` under a two-second limit, which must come back
  as `timeout` within `GRANDCHILD_BOUND`, the limit plus the stop's ten-second reap wait plus the
  overhead measured on three runs, its worktree removed or named as leaked), `leak-env` (git location
  variables and a foreign `PWD` set by the caller, the command still reading the worktree's git,
  `GIT_OPTIONAL_LOCKS` as `0` and the worktree as `PWD`), `exit0-grandchild` (a command leaving
  `sleep 600` behind and exiting 0, the background process gone once the call returns on Linux and
  macOS, and on Windows the call bounded and its worktree removed or named as leaked), `normalise` (a command
  printing its working directory three ways and a duration that changes per run, re-run twice to one
  hash) and `normaliser-missing` (the run-gates kit looked for from an empty directory: the re-run is
  refused by name before it adds a worktree, and `rerun` answers `inconclusive` printing why) and
  `sed-fails` (a stub of that kit's library whose normaliser program `sed -E` refuses: the re-run is
  refused naming its `sed:` step, no hash taken, its worktree removed, and `rerun` answers
  `inconclusive`). `--selftest` runs every case and the two computed-witness cases above, and the
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

A loop command finds a build's records under the root the unattended driver writes them under. Where
the repository has a `.unattended.conf`, that root is its `MEMORY_ROOT`, read as the driver reads it,
or `memory` where the conf leaves it unset; with no such file, it is the `MEMORY_ROOT` of
`.memory-tree.conf`, or `memory`. Where both files name a root and the two differ, every loop command
that reads a build's records refuses and exits 2, its reason opening `records root:` and naming each
file with the root it says, then the root the driver writes under. Set the two files to the same root,
or drop the memory tree's line, to clear it.

The roles kit's `roles catalogue` gate joins the two files by workflow name, both ways: a workflow
in `workflows.toml` with no row here, or a row here naming no workflow there, is one `R6` line.

## Who owns it

The file is gov's and an update overwrites it: the steps and each workflow's place are not an
adopter's to seed. The loop kit is in the default selection, so a default install takes it, and
`update` installs it into a tree whose receipt predates it, as a default-gained kit. The roles kit
requires the loop kit: a `--kits` selection naming `roles` names `loop` too or is refused. The
unattended kit requires the loop kit too, for check 53. The loop kit requires the memory-tree kit,
because `--check` reads the actor list at the compare base that kit resolves, and reads
`DESIGN_RECORD` through that kit's conf reader, finding the builds folder under the records root the
section above states.
The loop kit requires the run-gates kit too, because loop_witness.py normalises each re-run's output
with that kit's normaliser before it hashes it. `--check` also reads the roles
kit's role files for the role items' defaults, without requiring that kit: where it is not
installed, each role item prints `unarmed`. `loop_witness.py` writes its records through the
memory-tree kit, and its `hold-inherited` case runs the unattended driver without requiring that kit,
since the unattended kit requires this one; its gate is gov's own and an install does not carry it.
`loop_checklist.py` reads the unattended driver's two registry lines the same way, and its
`loop checklist tags` gate is gov's own too. `claims.py` reads git alone and requires no other kit;
the orientation card and the unattended driver each find it beside them, and its `loop claims
fixtures` gate is gov's own.
