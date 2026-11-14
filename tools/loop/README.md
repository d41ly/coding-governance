<!-- gov:kit loop@1.0 -->
# loop — the loop's definition: the gov steps, and where each workflow sits in them

A governed build runs one loop: Plan, Design, Build, Test, Deploy. This kit is where that loop is
written down. `loop.toml` holds it as data, `loop_lib.py` is its one reader, and every other kit that
needs a step or a workflow's place asks the reader. The roles kit keeps WHO does the work, its role
files and its workflow table; this kit holds WHAT runs and in which step. Contract: TOOL-dDeclaredLoop-1.

## The definition, `loop.toml`

One `[[step]]` row per gov step, in the loop's order:

| key | what it holds |
|---|---|
| `tag` | the step's tag, `step.plan` to `step.deploy`, a member of the `step` namespace |
| `order` | its place in the loop, counted from 1 |
| `state` | the build state a build holds while it is in the step |
| `exit` | the step's exit item, a tag of the `item` namespace |

One `[[workflow]]` row per workflow of the roles kit's `workflows.toml`:

| key | what it holds |
|---|---|
| `name` | the roles workflow, the join key |
| `order` | its build order, 0 for an any-time workflow; the `## Stage <n>` number in the `/build` Skill |
| `step` | the step its work sits in, a `[[step]]` tag, or `none` |
| `reach` | optional, `entry` or `review`: the word its work orders load practices under |

A workflow's `step` says where its work sits in the loop. Its reach word says which reach of each
practice its work orders carry: the row's `reach` where it has one, else the last segment of its
`step`, else `none`. The two differ on three rows: `orient` serves no gov step and loads the `entry`
reach, and the two review workflows sit in Design and Build and load the `review` reach.

## The disposition set

`[dispositions]` holds the one closed disposition set, the words a placing item returns for a
request: `continue`, `amend`, `new`, `patch`, `repeat`, `unit`, `breakpoint`, `ask` and `none`. Its
`set` is a non-empty array of single words, none given twice. Contract: TOOL-dDeclaredLoop-16.

One `[[disposition-alias]]` row per legacy word that means a member. A row's `word` is no member and
no earlier row's word, and its `means` is a member:

| `word` | `means` | why |
|---|---|---|
| `attach` | `amend` | attaching a request to a live build is its re-entry at Design |
| `defer` | `ask` | a deferred request is filed as an ask |
| `refuse-as-duplicate` | `continue` | a duplicate is re-placed onto the matched build, which carries on |

An alias hides a legacy word behind a member, so a writer resolves the word before it writes: a
record carries a member, and the join below reads the word as written.

Three vocabularies look like this set and are not it:

- the review round's exit, `fold` or `promote`: `REVIEW_DISPOSITIONS` in the unattended kit's driver;
- the per-finding report grammar of a review record: `class:`, `new:`, `gate:` and `none`;
- triage's verdicts, `select`, `defer`, `retire` and `refuse`, which move a build in planning to one
  of its terminal states. Triage's `defer` is that verdict; the alias `defer` above is Plan's draft
  word for a request filed as an ask.

**The owner's disposition record.** An owner's answer to a held item is a `disposition` record in the
build's `build/` folder, written through the memory-tree kit's door, `build_records.py new
disposition`. It carries one word, and which words are legal is the disposed item's: an `[[item]]`
row declaring `outcomes = "dispositions"` takes the set above, and any other row lists its own, such
as `ratified` and `rejected`. `check_disposition_record` is that join. The shipped definition holds
no `[[item]]` row yet, so the join answers `None` for every item, which a caller prints as `unarmed`.

## The witness classes

Every witness the definition declares names its class (TOOL-dDeclaredLoop-5). `[witnesses]` holds two
lists of single words, none in both: `classes`, the facts the acting agent cannot type, `history`,
`hook-record` and `remote-verdict`; and `refused`, `actor`, a fact it typed. Every `[[step]]` row
carries `witness = { class = "<class>", by = "<what>" }`; each step's exit is witnessed by its
transition record, class `history`.

One `[[witness-alias]]` row per checker word of the unattended driver's `DOD_CORE`, graded as the
disposition aliases are: `machine` means `history`, `agent` means `actor`.

`actor-witnesses.txt` beside the definition is the shrink-only list of actor witnesses, rows only,
`<site>`, `<witness>` and `<build>` separated by tabs, the build being the one whose computed witness
takes its place. A site is a step tag or one of `DECLARATION_SITES`, `DOD_CORE` and `DOD_EXTRA`. It
is seeded with the two `agent` entries of `DOD_CORE`: `keepalive-reaped` until `dWellOiledMachine`
and `parked-decisions-surfaced` until `dShippedRelease`.

## The reader, `loop_lib.py`

| function | returns |
|---|---|
| `load_loop(kit_dir)` | the checked definition, `{"step": [...], "workflow": [...], "dispositions": [...]}` |
| `read_steps(kit_dir)` | the step rows, in the loop's order |
| `read_workflow_order(kit_dir)` | `{workflow name: order}` |
| `read_workflow_reach(kit_dir)` | `{workflow name: reach word}` |
| `read_dispositions(kit_dir)` | the members of the disposition set, in file order |
| `resolve_disposition(kit_dir, word)` | the member a member or an alias means |
| `read_outcome_set(kit_dir, item)` | the closed outcome set of the `[[item]]` row tagged `item`, or `None` |
| `check_disposition_record(kit_dir, record)` | `True` where the record's `Disposition` is in its `Item`'s outcome set, `None` for an undeclared item |
| `read_witness_classes(kit_dir)` | `{"classes": [...], "refused": [...]}`, the definition's witnesses graded |
| `check_witness_classes(data, where)` | `(site, class, by)` per witness, after grading `[witnesses]`, the witness aliases and every step's `witness` |
| `check_alias_rows(rows, members, table, where)` | nothing; refuses an alias row of either table whose `word` is a member or repeats, or whose `means` is no member |
| `resolve_alias(rows, word)` | the `means` of the row holding `word`, or `None` |
| `read_actor_rows(kit_dir)` | the actor list's non-blank lines, the list's one reader |
| `read_actor_base(kit_dir)` | `(rows, base)` of the list at the compare base, or `(None, why)` for no comparison |
| `check_actor_list(rows, base_rows, sites, root)` | one refusal per list row not three fields, absent at the base, naming no actor witness of its site, or naming a build with no folder; and per actor witness no row lists |
| `check_site_witnesses(kit_dir, site, entries)` | `(lines, refusals)` for one declaration site's `<item>:<word>` entries, joined to the aliases and the list both ways |

Each refuses a definition that does not hold with `LoopError`, a `ValueError` naming the file and
the row: the gov steps missing, repeated or out of order; a workflow named twice; an `order` that is
not an integer at or above 0; a `step` that is absent or is neither a step tag nor `none`; a `reach`
outside `REACH_WORDS`; a disposition set that is empty, holds a word twice or holds what is not one
word; an alias row whose `word` is a member or repeats, or whose `means` is no member.

The disposition table is graded where a definition holds it: `load_loop` returns an empty
`dispositions` for a definition with none, and `read_dispositions` and `--check` refuse it.
`resolve_disposition` raises `LoopError` for a word that is neither a member nor an alias, and
`check_disposition_record` for a word outside the item's set, naming the item and the set.

The witnesses are graded by `check_witness_classes` alone, called from `read_witness_classes`,
`check_site_witnesses` and `--check`, never from `load_loop`: a reader that copies this module with a
definition holding no witness keeps reading. `read_actor_base` takes the repository root and the
list's path from `git rev-parse`, finds the memory-tree kit with its inline `resolve_kit_dir`, and
imports that kit's `resolve_compare_base` inside the function, so nothing else here needs more than
the standard library.

A kit reads it by finding this kit's directory with its own `resolve_kit_dir` and importing the
module from there. Three readers do today: the roles kit's `roles_lib.read_workflow_order`, which its
catalogue checker joins with the workflow table both ways (rule R6) and its adopter binds the
Skill's stage headings to; and the playbook kit's drive section and load-set check, which sort the
drive rows by `order` and pick each role's practices by its reach word.

## The commands

- `python loop_lib.py --check` reads the definition and prints one line per step and per workflow,
  the disposition set on one line and one line per alias, then the witness classes, one line per
  witness alias and per witness, one line per actor-list row with its build, and the list's base line:
  the base it compared against, or `no comparison` and why, never read as an empty list. Exit 0 read,
  1 refused with the reason on one line or each list refusal as `loop: refused · ...`. It is the
  `loop definition` gate leg.
- `python loop_lib.py --fixture --plant <case>` reads the shipped definition and list with one break
  made in memory, the list's base being the shipped list as read, so nothing runs git, and exits 1 on
  the refusal that break must draw. The cases are `missing-step`, `reordered`, `bad-step`,
  `bad-reach`, `disposition-unknown` (`ask` given twice in the set), `disposition-alias` (the
  `defer` row meaning no member), `witness-no-class`, `witness-bad-class` (class `agent-said`),
  `witness-actor-unlisted` (step.plan's class `actor`), `witness-actor-listed` (that, and listed, which
  reads clean), `actor-list-grown` (a row the base lacks), `actor-list-stale` (a row for step.design,
  whose witness is `history`) and `actor-list-no-build` (a row naming `dNoSuchBuild`). Nothing on disk
  changes.
- `python loop_lib.py --grade-site <site> <entry>...` grades one declaration site, `DOD_CORE` or
  `DOD_EXTRA`, whose entries are `<item>` or `<item>:<word>`. The word resolves through
  `[[witness-alias]]` alone. It prints `loop: site <site> · <item> · <word> · <class>` per entry,
  `· until <build>` on a listed actor entry, then each refusal: an entry with no word, a word no alias
  row holds, an actor entry the list does not hold, and a list row of that site no actor entry holds.
  Exit 0, 1 on a refusal, 2 on usage or a site outside `DECLARATION_SITES`. It reads the list in this
  directory and runs no git. The unattended kit's check 53 calls it, which is why that kit requires
  this one.
- `bash adopt-loop.sh --check` runs the first through the resolved python. The kit renders
  nothing, so its adopter has no `--scaffold`.

## What it does not check

That a workflow row names a workflow the roles kit holds: the roles catalogue checker joins the two
both ways. That a step tag or an exit item is registered: the tag index reads the `[[step]]` rows as
the `step` namespace. That an exit item exists: the item rows are a later unit's. That a disposition
record's `Item` names a declared item, which reads `None`, or that a writer resolved an alias before
it wrote. An unknown key on a row is neither read nor refused. That a witness's `by` is true. That
the build an actor-list row names will compute its witness.
