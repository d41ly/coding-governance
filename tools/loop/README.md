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
as `ratified` and `rejected`. `check_disposition_record` is that join. It answers `None` for an item
the definition does not declare, which a caller prints as `unarmed`.

## The item programs

Each gov step is a program of items (TOOL-dDeclaredLoop-12): one `[[item]]` row per item, after every
table above, transcribed from the flow-steps record's five step tables.

| key | what it holds |
|---|---|
| `tag` | `item.<step>.<name>`, a member of the `item` namespace |
| `step` | the `[[step]]` tag its tag opens |
| `actor` | `<kind>:<name>`, one actor of one kind in `ACTOR_KINDS`, or the bare `executor` or `owner`; a role's name is its role file's stem |
| `needs` | the items it waits for: each entry a tag, or a list of tags any one of which meets it; `[]` for none |
| `inputs` | `<layer tag>:<what it reads>`, the layer a tag of the playbook kit's `layers.toml` |
| `allowance` | what it may write |
| `returns` | its return template, the record kind it writes |
| `outcomes` | its closed outcome set, a list of words, or `"dispositions"` for the set above |
| `witness` | `{ class, by }`, as a step's |
| `owner` | the build that owns it |
| `routes` | an inline table, one target per outcome: a declared item, `transition`, or `stand-in:{prefix}/<home>/<file>` |

**The actor and the role defaults** (TOOL-dDeclaredLoop-9). `check_item_declarations(items, roles,
why)` grades each row's actor: one string fullmatching `ACTOR_FORM`, `<kind>:<name>`, its kind in
`ACTOR_KINDS` (`role`, `command`, `executor`, `hook`, `owner`), or the bare `executor` or `owner`; a
list, a comma, whitespace or a second colon is refused, naming the item and the value. A non-role
item carries a non-empty `inputs`, `allowance` and `returns`. A `role:<slot>` item's slot is a role
file's stem under the roles kit's `agents/`, such as `gov-builder`, and `resolve_item_declaration`
gives its absent `inputs` the role's `reads` split on commas, its absent `allowance` the role's
`writes` and its absent `returns` the role's `returns`, naming each field's source. The catalogue is
`read_role_defaults(kit_dir)`: the roles kit found by `resolve_kit_dir` from this directory, its
`roles_lib` imported inside the function and `load_roles` of that directory returned, or None and
why. A role item's explicit field equal to its role's is refused as a copy, and its explicit
`allowance` may only be `none`, a narrowing: the role item's write set is its role's or nothing. A
slot the catalogue lacks prints `pending`; where the roles kit does not resolve, every role item
prints `unarmed`. Neither is a refusal, neither is green, and both are counted. The descriptor
declares no edge to the roles kit, which requires this one. Every item's `witness` is graded by
`check_witness_classes` after the steps', and joins the actor list as a step's does.

A role actor's absent `inputs`, `allowance` and `returns` are its role's. A `needs` phrase in the
step tables naming no item, such as "a select", is the any-of list of the items routing into the row;
a need on an item outside the five programs is left to the unit declaring that program. A route into
a later build names today's stand-in under `{prefix}`, which keeps the row clear of the install-prefix
ban. `routes` is inline, never an `[item.routes]` table, so the tag index reads one span per row.

`check_program(data, where, layers)` grades the rows as one needs graph, an any-of entry an edge to
each of its tags. It refuses a tag opening no `item.<step>.` of a gov step or a `step` other than
that one, a tag declared twice, a need naming no declared item, and a needs cycle, each cycle named
once and a self-need a cycle of one. Per item it refuses an outcome set `derive_outcome_set` refuses,
empty or with a word twice; routes that are not exactly the outcomes; a target that is no declared
item, `transition` or a stand-in; and, where `layers` is not `None`, an input whose text before its
first `:` is no layer tag. Each `[[step]]` row's `exit` must be a declared item of that step. It
returns `{step tag: [item tags in needs order]}`, one order filtered per step. The order and the
cycles come from the needs-graph helper, `derive_needs_order` and `scan_cycles`, the `needs_graph_py`
block this module carries inline beside govkit's and the memory-tree kit's backlog copies.

An item's instruction scope is derived, never typed: `derive_item_scope` runs the playbook kit's
`load_sets.py derive --reader reader.every --item <tag>` once per item, as a subprocess found through
`resolve_kit_dir`, so this module imports no sibling kit. While no unit's `scope` names an item tag,
each line reads `item — 0 unit(s)`. The kit's descriptor declares no edge to the playbook kit: both
reads print `unarmed` where it does not resolve.

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
takes its place. A site is a step tag or `DOD_CORE`, the one declaration site the list grades. It
is seeded with the two `agent` entries of `DOD_CORE`: `keepalive-reaped` until `dWellOiledMachine`
and `parked-decisions-surfaced` until `dShippedRelease`. A row's build folder is tested only in a
tree whose `.memory-tree.conf` sets `DESIGN_RECORD`, under `<MEMORY_ROOT>/builds/`; in any other
tree each row prints `foreign build, not graded`. `DOD_EXTRA` is the adopter's own: its actor entries
need no row and are admitted, printed `adopter-declared`.

## The computed witnesses

One `[[computed-witness]]` row per witness a tool computes rather than the acting agent typing it
(TOOL-dDeclaredLoop-17): its `name`, one word; the item it `serves`, a declared `[[item]]` tag or
`none`; its `writer` today, `stand-in:{prefix}/<home>/<file>` or an actor `<kind>:<name>`; and the
build `armed-by` that writes it for real. Its class is the served item's witness class, derived and
never typed, `none` for a row serving `none`, and a served item whose class is refused is refused.
Three ship: `acceptance` serving `item.build.acceptance` and `probe-rerun` serving `none`, both written
today by `loop_witness.py` beside this file, and `red-attribution` serving `item.test.route`, written
by the bar runner.

`loop_witness.py` is the re-run stand-in. `run_witness_commands(repo, sha, commands, timeout)` adds a
detached worktree of `sha` under the host temp directory, runs each command there as `bash -c <command>`
with the memory-tree kit's `GIT_ENV_LEAKS` unset, keeps each exit, or `timeout`, and the first twelve
hex digits of the SHA-256 of its combined output, and removes the worktree on every exit path. The bash
is the inline `resolve_bash`'s, one that can see this file, and a call with none raises `LookupError`.
Each command's output goes to `cmd-<n>.out` beside the worktree, never a pipe, read once the wait
returns; on the timeout the inline `run_tree_kill`, the `run_tree_kill_py` block the run-gates kit's
`regen.py` carries too, kills the command's tree. A worktree still on disk after the teardown is named
on stderr, `loop-witness: leaked <path>`, never raised.
`acceptance --build --unit --sha --cmd... [--root]` writes the memory-tree kit's acceptance record
through its `write_acceptance`, `Writer: stand-in`; `rerun --sha --cmd --expect...` answers each command
`confirmed`, `refuted` or `inconclusive`. Its plants are `acceptance`, `acceptance-malformed`,
`probe-rerun`, `bash-syntax`, a command only bash runs, `timeout-grandchild`, a grandchild outliving
the bound, and `hold-inherited`, the last running the unattended driver, found by
`resolve_kit_dir` and run through the inline `resolve_bash`, with no edge to that kit, since it requires
this one; a kit that does not resolve exits 2, never a pass. `--selftest` runs them and this reader's
`computed-actor` and `computed-unserved` plants, and is gov's `loop computed witness` gate.

## The checklist map

One `[[checklist]]` row per handle of the unattended driver's `DOD_CORE` and `DIRECTIVES_CORE`
(TOOL-dDeclaredLoop-11): its `registry`, its `handle` as the registry spells it before its first `:`,
and the `item` tag whose witness the handle's check reads, and no other key, so no row stores a
position. `read_checklist_rows` returns the rows and `check_checklist_rows` grades them both ways.

`loop_checklist.py` is the command. `check` reads the two registry lines from the driver, found by
`resolve_kit_dir` with no edge to that kit, since it requires this one, as that kit's checker reads
them: the first `<NAME>="<members>"` line once trailing whitespace is stripped, each handle the text
before a member's first `:`. It prints a `loop: checklist` line per row and a `loop: checklist-count`
line per registry, and exits 1 on a refusal, 2 where the driver does not resolve or a registry line
is absent or empty. `show <handle>` prints `<registry> <item>` from the rows alone, exit 2 for an
unmapped handle. `--fixture --plant <case>` runs `check` with one break of `PLANTS` made in memory:
`missing-handle`, `stale-row`, `two-rows`, `undeclared-item`, `bare-item`, `numbered-row` and
`bad-registry`. `check --selftest` runs `check`, every plant and `show`, and is gov's
`loop checklist tags` gate, on every automatic bar.

```bash
python <prefix>/loop/loop_checklist.py check
python <prefix>/loop/loop_checklist.py check --selftest
python <prefix>/loop/loop_checklist.py --fixture --plant missing-handle
python <prefix>/loop/loop_checklist.py show reuse-probed
```

## The transition tables

One table per level, build, feature and unit (TOOL-dDeclaredLoop-13): `[states]` holds each level's
open states, and its `terminal` key, which is no level, the build's nine terminal states
(TOOL-dDeclaredLoop-15): a build row may enter one and no row may leave one. Each `[[transition]]` row is a move, its `level`, `from` (states, `none` for the level's
entry, or `@open`), the `item` tag and `outcome` that fire it, its `to` (a state, `@prior` or
`@reentry`), its `witness`, and optionally a `disposition` and `when = "before-push"`. `[[stand-in]]`
names the owner of each row item whose build has not landed, and `[[owed-row]]` each cross-step route
whose build row another unit or build writes; both lists only shrink. `loop_lib.py` does not read
them: `loop_table.py` does, through `read_transition_rows` and `read_stand_ins` over the parsed
definition, `read_transition_rows` splitting `terminal` out of the levels and adding `step-order`, each
step's state to its order, and `derive_move` answers a
move from the rows alone, raising `TransitionRefused` where no row holds it or the state asked is a
terminal, and ValueError on an unknown level or state or a missing fact a row reads (`prior`,
`reenters`, `pushed`, `disposition`), never a default.

The rows into a terminal are T1 and T2, triage's `refuse` into refused, T3, the Deploy exit's
`closed` into landed, and T4 and T5, the owner's close request's `withdrawn` and `superseded`, each
from any open state while the landing is unpushed. That request's item, spelled below, has no
`[[item]]` row yet and stands on a stand-in row:

```text
item.life.close · dWellOiledMachine
```

P1 moves a build in designing, building or deploying back to planning on `item.deploy.parents`'s
`withdrawn`. No row enters incomplete, deferred, retired, merged or answered yet; those states stay in
the set.

`derive_direction(state, to, tables)` answers a resolved build move's direction from `step-order` and
`terminal`, never typed: `forward` into a terminal or a later step, `backward` into an earlier one, and
`lateral` where an end has no step (`none`, `paused`, `parked`) or both share one. A backward move is
recorded through the same writer and channels as a forward one.

`move` prints `move — <level> · <from> → <to> · <item>`, with `· stand-in <owner>` for a stand-in item
and `· <direction>` last for a build move, exit 0; `refused — ...: no row`, exit 1; `unanswered — ...: <why>`, exit 2. `check`, by
`check_transition_tables`, prints a `loop: table` line per level, `loop: terminal build · <states>`, a
`loop: owed` line per owed row and a `loop: stand-in` line per stand-in, and refuses a row leaving a
terminal, a terminal also listed among the build's open states, an undeclared level or state, two rows for one move,
a row item that is no tag or resolves to neither an `[[item]]` row nor a stand-in, an outcome outside
its item's set, a disposition outside the set, and a stale or mis-owned stand-in. It joins every
cross-step route, an outcome routed to `transition` or to an item of another step, with the build
table both ways, an owed row standing for a row another unit writes and refused once a row covers it,
and each step's exit to a build row out of its state. Both verbs exit 2 where the definition does not
read or holds no transition row. `--fixture --plant <case>` runs `check` with one break of `PLANTS`
made in memory by `write_table_plant`: `bad-state`, `two-rows`, `bad-exit`, `dropped-row`,
`unrouted-row`, `owed-stale`, `stand-in`, `terminal-from` (a build row leaving landed) and
`terminal-open` (landed appended to the build's open states). `check --selftest` runs `check`, every
plant, each kind of move and direction, and `direction-order`, the shipped rows with building's and
testing's orders swapped, through `run_selftest_cases`, the case loop `loop_checklist.py` shares,
and is the kit's `loop transition tables` gate leg.

```bash
python <prefix>/loop/loop_table.py move --level build --from designing --item item.design.exit --outcome recorded
python <prefix>/loop/loop_table.py check
python <prefix>/loop/loop_table.py check --selftest
python <prefix>/loop/loop_table.py --fixture --plant dropped-row
```

## The parent route

`loop_parents.py` (TOOL-dDeclaredLoop-15) answers a dependent build's route when a parent its README's
`parents:` front matter names reads withdrawn. Until a parent's `withdrawn` post lands, the stand-in
is the parent's run-state file holding the run fact `phase: ABORTED`. `read_withdrawn_parents` reads
the front matter through the memory-tree kit's `parse_front_matter`, the builds folder from its
`read_design_conf`, and the run facts through the policy kit's `read_run_fact`. `derive_parent_route`
reads `deps.on-parent-withdrawn` through the policy kit's `resolve` at the landed revision, its
default `replan`, and takes the move from P1 by `derive_move`, so a state P1 does not admit answers
`held`:

```text
route replan · parent <p> · move <state> → planning · item.deploy.parents
route adopt-parent-work · parent <p> · move <state> → planning · item.deploy.parents
inventory <p> <sha>
route withdraw-too · parent <p> · owner-item · propose item.life.close withdrawn · left by record-kind.disposition
route <value> · parent <p> · held: <state> admits no parent row
route none
```

`adopt-parent-work` names each withdrawn parent's kept branch tip, the ref its `run-branch:` fact
names, else `branch-ref:`, as the input the design inventory takes its kept units from; a parent with
neither, or a ref naming no commit, exits 2 `no kept branch`. `withdraw-too` proposes the build's
withdrawal to the owner and moves nothing. The route writes nothing. It exits 2 on an unreadable
`parents:` slug, a state outside the build's open states or a policy refusal, and 2 `unarmed` where
the policy kit does not resolve, since this kit takes no edge to it. `--fixture --plant <case>` runs
the route over a scratch repository: `withdrawn-parent`, `no-kept-branch`, `live-parent` and
`no-parents`, with `--value` committing the scratch's one policy revision and `--state` the child's
state, `designing` by default. `--selftest` runs every case, and is gov's `loop parent routes` leg.

```bash
python <prefix>/loop/loop_parents.py route --build <slug> --state <state> [--root <path>]
python <prefix>/loop/loop_parents.py --fixture --plant withdrawn-parent --value adopt-parent-work
python <prefix>/loop/loop_parents.py --selftest
```

## The transition record

`loop_transition.py` (TOOL-dDeclaredLoop-3) records a build's stage move three ways, the channels the
policy key `transitions.record` selects, any non-empty subset and all three by default, read through the
policy kit's `resolve` at one revision per move: HEAD for the writer, each trailer's commit for the check.

```text
Gov-Transition: <from> -> <to> · build=<slug> · item=<tag> · sha=<sha8>[ · <name>=<value>]...
<date>-build-<anchor id>-transition-<n>.md   Build · From · To · Item · Sha · then each extension field
transition — <slug> · <from> → <to> · <item tag> · <sha>
```

The trailer is the source. The log record is the memory-tree kit's typed `transition` kind, written
through its `write_record` under the lowest unit id a spec H1 under the build defines; a move made
before the build's first spec writes none, and the next move after it back-fills one per earlier
trailer. The micro-format line is printed, never stored, by `render_transition_line` from
`TRANSITION_LINE`, and the charter's micro-format block defines it. An extension field's name is one of
`TRANSITION_FIELDS`, which holds `stand-in`, written where the item has a `[[stand-in]]` row.

`record` (`write_transition`) answers the move by `derive_move` first, so a move no row holds prints
`refused` and writes nothing; it resolves the witness to HEAD or its ancestor, refuses a staged index,
and commits the records, or an empty commit, as `loop transition(<slug>): <from> -> <to>` with the
trailer where selected. `check` (`check_transition_channels`) holds each record to its trailer field by
field, names a record no trailer backs, prints `pending` while moves wait on the first spec and
`unstored` where the set stores nothing, and holds the definition in `AGENTS.md` to `TRANSITION_LINE`.
`read_transitions(build, repo)` returns the build's moves newest first, each with its `direction`
derived on read by `derive_direction` over this kit's definition. A backward move goes through the same
writer, channels and fields as a forward one, and `record` prints its direction on its
`loop: recorded · <from> -> <to> · <direction> · commit <sha8>` line; no trailer or record stores it. Both verbs exit 2 on a policy
refusal naming `transitions.record`, and 2 `unarmed` where the policy kit does not resolve, since this
kit takes no edge to it. `--fixture --plant <case>` runs both over a scratch repository: `default`,
`subset-trailer-line`, `subset-log`, `empty-set`, `log-drift`, `orphan-log`, `no-row`, `line-drift`,
`pre-spec`, `field`, and the two over `BACKWARD_MOVES`, three moves forward and three back:
`backward-rows`, printing each trailer and read with its direction, and `skip-backward`, the newest
record deleted so the check names the move back owing it. `check --selftest` holds the tree's own definition, then runs every plant, and
is gov's `loop transition record` leg.

```bash
python <prefix>/loop/loop_transition.py record --build <slug> --from <state> --item <tag> --outcome <o> --witness <sha>
python <prefix>/loop/loop_transition.py check --build <slug> [--root <path>]
python <prefix>/loop/loop_transition.py --fixture --plant default
python <prefix>/loop/loop_transition.py check --selftest
```

## The policy file's guard

Contract: TOOL-dDeclaredLoop-2. Three modules, each reading the policy kit through `read_policy_kit`,
its directory put first on `sys.path` so its `guard` is never this kit's file of that name:

- `floor.py`: `FLOOR_INVARIANTS`, the floor's four members, `verdict-before-move`, `record-changes`,
  `guard-self` and `no-actor-witness`, and `read_floor(repo, rev=None)`, which reads the `[floor]`
  table at the landed revision through the policy kit's `read_revision`, every absent member `on`, an
  unknown member or a value other than `on` and `off` a `LoopError`, and every member `on`, the reason
  printed once, where the policy kit does not resolve or refuses. `floor.py get <member>` prints it.
  Its readers report at `off` instead of refusing: the pre-push hook's `gate RED` line, the guard's
  record step and push arm, `loop_transition.py`'s check, the guard's guard-self step, and
  `loop_lib.py`'s two refusals of an actor witness no list row names, `--grade-site`'s and `--check`'s.
- `guard.py`: the commit verdict, `--staged`, which the pre-commit block runs in place of the policy
  kit's minimal guard wherever this kit resolves; the push arm, `--push-range <base>..<tip>`, which
  the pre-push hook runs over a default-branch update; and the expansion rule,
  `check_expansion_value(key, value, points)`, over this definition's `[[selects]]` rows, each a key,
  a value and the layer point that value needs. The verdict reads its rule from the landed revision:
  guard-self before the value's rule, the live run's admission before guard-self, a change record for
  every change, then `policy-file.guard`, the minimal guard run as a subprocess for every shape it
  admits. The help page's section "Who may change the policy file" is the user's statement.
- `policy_edit.py`: the policy file's one write path, `set`, `raise` and `propose`, each write through
  the guarded write, the block `guarded_write_py` it carries inline, writing the file and its change
  record, both staged, and printing the `Gov-Policy:` trailer line.

`guard.py --fixture --plant <case>` runs one plant's scenarios in a scratch repository under the host
temp directory, this tree's kits found beside this one, and prints each scenario `held` or `MISSED`;
`--selftest` runs every plant and is gov's `loop guard fixtures` leg.

```bash
python <prefix>/loop/guard.py --staged
python <prefix>/loop/guard.py --push-range <base>..<tip>
python <prefix>/loop/guard.py --fixture --plant raise-admitted
python <prefix>/loop/guard.py --selftest
python <prefix>/loop/floor.py get guard-self
python <prefix>/loop/policy_edit.py set review.max-rounds 4 --build <slug> --unit <id>
```

## The claim keys

`claims.py` (TOOL-dDeclaredLoop-8) keys a stored claim over its sources and trusts it by that key and
by its weakest source. `derive_claim_key` is `k1:` and the first sixteen hex digits of the SHA-1 of the
sources sorted bytewise and joined by NUL, `k1:?` before the digits where a source is spelled `?`.
`CLAIM_CLASSES` holds the five source classes strongest first, and `derive_claim_verdict` answers
`evidence`, `fresh` or `re-derived`; the `remote` class's age bound is the caller's, never this
module's. `derive_card_keys` is the orientation card's view and remote keys over the working directory
git runs in, and `CARD_CELL_CLASSES` joins each card cell to one of them. The card's `keys —` cell, its
replay's re-key and the unattended driver's sixth `--claims` field each find the module beside them by
`resolve_kit_dir`; it reads git alone, through its inline copy of the remote ladder, so it takes no
edge. `--fixture --plant <case>` runs one of `PLANTS`, and `--selftest` runs every case through
`run_selftest_cases`; it is gov's `loop claims fixtures` leg.

```bash
python <prefix>/loop/claims.py key commit=<sha> base=<sha>
python <prefix>/loop/claims.py verdict --stored <k> --class view --recomputed <k>
python <prefix>/loop/claims.py card-keys
python <prefix>/loop/claims.py --selftest
```

## The position engine

`position.py` (TOOL-dDeclaredLoop-7) answers where a build is and what runs next from witnesses alone.
`derive_position(repo, slug, definition=None)` reads the run branch's `--first-parent` commits and
their `Pass:` trailers through the memory-tree kit's `read_commits` and `derive_attribution` in the
`replace` view, the build's moves through `read_transitions`, each held by a build row through
`loop_table.check_recorded_move`, the tables through `read_transition_rows`, the items through
`read_composition`, gov's own rows where that composition is unarmed in the tree, the acceptance
records through `read_records` with `read_acceptance`, the run-state file's facts through the policy
kit's `read_run_fact`, and the default branch's remote-tracking tip. A parsed `definition` replaces the
shipped one and the composition for that call, which is how the plants are made in memory.
`check_recorded_move` matches a move to a build row by its item, its `from` through the expansion
`derive_from_states` shares with `derive_move`, and its `to`, `@prior` or `@reentry`, since a record
holds no outcome to replay.

Each unit's M2 state is the unattended driver's: `--plan` hands its rows over in
`GOV_POSITION_STATES` with the first undecided ask, each parent's derived phase, `RESUME_STALE_BOUND`
and the owed park sets, and the engine run standalone asks `--plan` with the variable set empty, which
answers with those lines in place of `next:`. A unit is `designed` on a READY spec, `built` on a pass
commit an acceptance record names, or, while the `acceptance` computed witness's writer has the
`ROUTE_STAND_IN` form, on its pass commit alone where no record names it, its `unit —` line then
ending `· acceptance unarmed` (TOOL-dDeclaredLoop-45), `tested` on the `gates-run` tip containing it, `deployed` on the
remote-tracking tip containing it. The build's step is its least-advanced unit's next step, and the
next item the first of that step whose witness does not hold and whose needs are witnessed, keyed
`<item>@<unit>#<inputs>` by `derive_instance_key`. The answer is one of `ANSWERS` by the spec's
precedence, `render_next_line` maps it onto `--plan`'s five shapes in `NEXT_SHAPES`, and every claim
prints with its key and verdict through `claims.py`. The driver's `--plan` prints that line as `next:`
and `--status` prints the engine's lines after its own; both find the module by `resolve_kit_dir`.
`--fixture --plant <case>` runs one of `PLANTS` over a scratch repository and bare remote, the last two
over the unattended driver, and `--selftest` runs every case through `run_selftest_cases`; it is gov's
`loop position fixtures` leg.

```bash
python <prefix>/loop/position.py <slug> [--json | --next-line]
python <prefix>/loop/position.py --fixture --plant steps
python <prefix>/loop/position.py --selftest
```

## The stage claims

`stage_coverage.py` (TOOL-dDeclaredLoop-4) joins every part of the product both ways to the stage it
serves. A claim is a non-empty list of the `[[step]]` tags `check_loop` admits, or `["none"]`; any other
value is no claim. A dossier keeps its claim in its fence's top-level `stage` key, read through the
codebase-map kit's `load_map_tree`; a gate leg in its manifest row's last key `stage`; a workflow in
its `[[workflow]]` row's `step`; a role through its `workflow:` front-matter key, read by
`read_role_defaults`, and that row; and a hook in a `[[hook]]` row of the definition, one per key of the
map's `git-hooks` and `harness-hooks` inventories, its `{prefix}/` expanded to the tool root's
repo-relative path. `derive_part_claims` feeds the five populations and one owner, `stage-claims`, to
the memory-tree kit's `compute_coverage` with an empty baseline, so an unclaimed part and a stale claim
are each red; an empty population prints `unarmed` and is red. `derive_stage_witnesses` prints each
step's exit item and its witness class through `check_loop` and `check_witness_classes`, whose refusal
is the red. The codebase-map and roles kits are found by `resolve_kit_dir` with no edge, and the
module exits 2 `unarmed` where either does not resolve. `--fixture --plant <case>` runs one of
`PLANTS` in memory, and `--selftest` runs the tree, then every case, through `run_selftest_cases`; it
is gov's `loop stage coverage` leg.

```bash
python <prefix>/loop/stage_coverage.py
python <prefix>/loop/stage_coverage.py --fixture --plant stale-hook
python <prefix>/loop/stage_coverage.py --selftest
```

## The item kind

The items are a registered kind (TOOL-dDeclaredLoop-24): the kinds register's `kind.item` row names
`loop_items.py new` as its factory, `item-schema.toml` beside this file as its row schema, and the leg
`loop item kind` as its gate. A repository adds an item, or patches or excludes one of gov's, from its
overlay, `.governance/instructions.toml`, as it does any registered kind's row; its own item's tag holds
`adopter` at the schema's owner seat, segment 2. The schema declares each key of a gov item but `tag` as
a field: `needs` an open set widened by removing a need, `inputs` and `routes` open sets widened by
adding, `routes` patched whole; `step`, `witness` and `outcomes` fixed by a principle, and `actor`,
`allowance`, `returns` and `owner` fixed by their undeclared class. Its `[[fixed-row]]` set is each
step's exit item and the floor item `item.test.verdict`, which no repository row amends, supersedes or
excludes.

`check` composes the repository through the playbook kit's `overlay_rows.py compose --kind item`, run as
a subprocess, so this kit imports no playbook module; it exits 2, `unarmed`, where that kit does not
resolve, the schema is absent, or HEAD holds no definition. It then grades the definition holding the
composed rows: `check_program`, `check_witness_classes` and `check_item_declarations` above; the
`[[fixed-row]]` set joined with the step exits and the floor item, both ways; each `[[record-version]]`
row of the definition, its `fields` the hash of its kind's row in the memory-tree kit's record table,
refused when the hash moved while the `version` did not; and each record input of a composed item,
`<layer tag>:record-kind.<name>` or `...@<n>`, joined to an item of its needs closure returning that
kind at that version, an unversioned value reading the kind's current version. `new` appends one gov
item to the definition, grades the file as written and restores its bytes on a refusal.
`read_item_members` and `write_item_plant` are the step gate's `item` class. `--fixture --plant <case>`
runs `check` in a scratch repository holding a copy of the kits it reaches, with one plant committed,
and `check --selftest` runs `check` and every plant through `run_selftest_cases`.

```bash
python <prefix>/loop/loop_items.py check
python <prefix>/loop/loop_items.py check --selftest
python <prefix>/loop/loop_items.py --fixture --plant amended-cycle
python <prefix>/playbook/core.py new item <name> --step <step> --actor <kind:name> --witness-by <text> --owner <build>
```

## The stage kind

A repository's own stage is spliced between two adjacent gov stages (TOOL-dDeclaredLoop-25): the kinds
register's `kind.stage` row names `splice.py new` as its factory, `stage-schema.toml` beside this file as
its row schema, owner seat 1, and the leg `loop splice check` as its gate. The stage is a `[[stage]]` row
of the overlay tagged `step.adopter.<name>`, its `after` and `before` two adjacent gov steps A and B, its
`pin` the pin of the build row R from A's state on A's exit into B's state, and its `exit` an overlay
`[[item]]` tagged `item.adopter.<name>.<item>`, which the item schema's owner seats `[2, 1]` and
`check_program`'s `stages` argument admit. `derive_splice_rows` splits R into R1, from A's state into
`adopter-<name>`, and R2, from there on the stage's exit into B's state, each with R's outcome and
witness; every other row stays as shipped, and gov's `loop.toml` is never edited.

`check_splices` holds the frame: a stage naming a gov step tag a change record succeeds is re-pointed
through its `Successor` first; then the tag, no excluded gov step, adjacency in order, one stage per
pair, R held and pinned by `derive_row_pin`, the exit an item of the stage routing R's outcome to
`transition`, each stage item witnessed, and `check_program` over the composed items. `check` composes
both kinds at HEAD through `loop_items.read_composition` and reads `instructions.exclude` and the change
records; `new` validates, derives both rows through `loop_items.derive_new_item_row`, grades them in
memory and appends them to the overlay. Every plant but `factory` runs in memory over the definition.
`read_stage_members` and `write_stage_plant` are the step gate's `stage` class: gov's `[[step]]` tags,
witnessed by the change records, as the `item` class is. The move engine does not read the spliced table
yet.

```bash
python <prefix>/loop/splice.py check
python <prefix>/loop/splice.py check --selftest
python <prefix>/loop/splice.py --fixture --plant two-splices
python <prefix>/playbook/core.py new stage <name> --after <step> --before <step> --actor <kind:name> --witness-by <text> --owner <build>
```

## The upstream field, `upstream.py`

An `[[item]]` row may carry `upstream` (TOOL-dDeclaredLoop-29), a list of one-line inline tables `{ item =
"<tag>", gate = "record" | "measured" }`, a `measured` entry with `measured-by`, a path HEAD holds, and
`measured-line`, a line that blob holds whole; `item-schema.toml` declares the field a set that widens by
removal, with no `ref`, and no gov row carries it. `check_upstream_rows` holds every composed row to that
shape, reads the measured entries' blobs in one `read_blobs_at` batch, and refuses an item with an
`upstream` list whose outcome set lacks `finding`; `loop_items.py check` calls it after its own grades and
prints `loop: upstream edges · <n> record · <m> measured`. `derive_upstream_rows` turns each upstream
item's return's `## Establishes` rows into handed rows `<upstream item>#<row id> · <kind> · <text>`, and
`check_upstream_answers` joins them with the item's `## Upstream` answers: each handed id answered,
`dropped` or `doubled`, an unhanded id `invented`, an answer `bad-answer` or `no-reason`, and `bypassed`
a finding on either edge, every finding graded on its edge's gate so only a `measured` edge refuses.
`write_upstream_record` writes the join as a journal record under the build's `build/` folder. Both
verbs read the composition through `loop_items.read_composed_items`, which `position.py` reads too.

```bash
python <prefix>/loop/upstream.py rows <item> --return <upstream item>=<path>
python <prefix>/loop/upstream.py join <item> --rows <rows file> --return <return path> [--write --build <slug> --unit <id>]
python <prefix>/loop/upstream.py --fixture --plant drop-gating
python <prefix>/loop/upstream.py --selftest
```

## The factories, `factories.py`

Five more kinds of the register take their factory from `factories.py` (TOOL-dDeclaredLoop-6): the
rows `kind.command`, `kind.policy-key`, `kind.hook`, `kind.role` and `kind.workflow` each name one of
its subcommands, so `core.py new <kind> <name> ...` runs it. Each validates its arguments first and exits
2 on a bad one, before any write; holds every path it writes, and the path a renderer it runs writes,
through `write_guarded` from `policy_edit.py`, one call per path, nested; and runs the kind's gate as the
innermost record step, so a red gate puts every byte back and removes every created path, prints the
gate's output and exits 1. The gates are the existing ones, wrapped, never copied: `check-commands`
here for a command, a `[[command]]` row of a kit descriptor; `POLICY_KEY_ARMS`, the four arms of the
policy kit's `check_policy.py` that read no render at a revision, run in process through its `run_arm`,
for a policy key, a `[[key]]` row of its catalogue, the mirror left to the caller's next commit;
`check-hook-destinations.sh` for a hook, run with `GIT_INDEX_FILE` naming a throwaway copy of the
caller's index holding the written files, since it grades tracked fragments only; and the roles kit's
`check_roles.py`, through its `--write` render, for a role and a workflow, the workflow's loop row also
graded by `loop_lib.py --check`. A role and a workflow join the two sets the roles kit closes in code,
`BODY_CEILINGS` and `WORKFLOW_NAMES`, by one anchored insertion each. The preset kind is pending for
dKeptSession, and the stage kind for TOOL-dDeclaredLoop-25's repository stage. `--fixture --plant
<case>` runs one of eleven plants, each factory's instance green and a hand-made one red under the same
gate plus the restore, in a scratch clone of the working tree the policy kit's `build_source_snapshot`
builds, and `--selftest` runs `check-commands` and every plant over one such clone through
`run_selftest_cases`.

```bash
python <prefix>/loop/factories.py check-commands
python <prefix>/loop/factories.py --fixture --plant hook-new
python <prefix>/loop/factories.py --selftest
```

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
| `check_computed_witnesses(data, where)` | each `[[computed-witness]]` row graded, `{name, serves, class, writer, armed-by}`, its class derived from the served item |
| `read_computed_witnesses(kit_dir)` | the definition's computed witnesses, graded |
| `read_checklist_rows(kit_dir)` | the `[[checklist]]` rows in file order, ungraded |
| `check_checklist_rows(rows, registries, items)` | `(lines, refusals)`: the rows checked both ways against the two core registries' handles and the declared items |
| `read_witness_classes(kit_dir)` | `{"classes": [...], "refused": [...]}`, the definition's witnesses graded |
| `check_witness_classes(data, where)` | `(site, class, by)` per witness, after grading `[witnesses]`, the witness aliases, every step's `witness` and every item's |
| `check_alias_rows(rows, members, table, where)` | nothing; refuses an alias row of either table whose `word` is a member or repeats, or whose `means` is no member |
| `resolve_alias(rows, word)` | the `means` of the row holding `word`, or `None` |
| `read_actor_rows(kit_dir)` | the actor list's non-blank lines, the list's one reader |
| `read_actor_base(kit_dir)` | `(rows, base)` of the list at the compare base, or `(None, why)` for no comparison |
| `read_builds_dir(kit_dir, root)` | `(builds_dir, "")` where the conf at `root` sets `DESIGN_RECORD`, or `(None, why)`: no memory-tree kit, or no `DESIGN_RECORD` |
| `check_actor_list(rows, base_rows, sites, builds_dir)` | one refusal per list row not three fields, absent at the base, naming no actor witness of its site or a site that is neither a step nor `DOD_CORE`, or, with a `builds_dir`, naming a build with no folder there; and per actor witness no row lists |
| `check_site_witnesses(kit_dir, site, entries)` | `(lines, refusals)` for one declaration site's `<item>:<word>` entries, joined to the aliases, and for `DOD_CORE` to the list both ways; a `DOD_EXTRA` actor entry is admitted, `adopter-declared` |
| `derive_outcome_set(row, members, where)` | one item row's closed outcome set, `members` for `"dispositions"`; the rule `read_outcome_set` and `check_program` share |
| `check_program(data, where, layers)` | `{step tag: [item tags in needs order]}` once the item rows hold as each step's program |
| `read_layer_tags(kit_dir)` | the playbook kit's layer tags; `LookupError` where that kit does not resolve |
| `read_items(kit_dir)` | the `[[item]]` rows in file order, once `check_loop` and `check_program` hold |
| `read_role_defaults(kit_dir)` | `(roles, "")`, the roles kit's catalogue as its `load_roles` reads it, or `(None, why)` where that kit does not resolve or read |
| `resolve_item_declaration(item, roles)` | `{inputs, allowance, returns, source}` of one item row, a role item's absent fields its role's, `source` per field `item`, `role:<slot>`, `pending` or `unarmed` |
| `check_item_declarations(items, roles, why)` | `(lines, refusals)`: one `loop: item` line per item and the count line, and a refusal per actor, missing field, copy or widened allowance |
| `derive_item_scope(kit_dir, root, tags, units=None)` | one `loop: scope` line per item, its load set as `load_sets.py derive` lists it, or `unarmed` |

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
imports that kit's `resolve_compare_base` inside the function. `read_builds_dir` finds the same kit
the same way and imports its `read_design_conf` inside the function, and `read_role_defaults` finds
the roles kit the same way and imports its `roles_lib` there. Those three are the only reaches
outside the standard library.

A kit reads it by finding this kit's directory with its own `resolve_kit_dir` and importing the
module from there. Three readers do today: the roles kit's `roles_lib.read_workflow_order`, which its
catalogue checker joins with the workflow table both ways (rule R6) and its adopter binds the
Skill's stage headings to; and the playbook kit's drive section and load-set check, which sort the
drive rows by `order` and pick each role's practices by its reach word.

## The commands

- `python loop_lib.py --check` reads the definition and prints one line per step and per workflow,
  the disposition set on one line and one line per alias, then the witness classes, one line per
  witness alias and per witness, one line per actor-list row with its build, and the list's base line:
  the base it compared against, or `no comparison` and why, never read as an empty list. Then
  `loop: actor-list builds · <folder>`, or `loop: actor-list builds · foreign · <why>`, each row's line
  ending `foreign build, not graded` in that case, then one `loop: computed-witness <name> · serves
  <tag> · class <class> · writer <writer> · armed by <build>` line per computed witness. Exit 0 read,
  1 refused with the reason on one line or each list refusal as `loop: refused · ...`. It prints
  `loop: program <step> · <n> item(s) · <tags>` per step, after `loop: inputs unarmed` and why where
  the playbook kit's layer tags do not resolve. Then one line per item in file order and the count,
  before the witness lines:

  ```text
  loop: item <tag> · <actor> · inputs from <source> · allowance <value> from <source> · returns from <source>
  loop: item <tag> · <actor> · pending · the roles kit holds no <slot> role
  loop: item <tag> · <actor> · unarmed · <why>
  loop: items · <n> read · <p> pending · <u> unarmed
  ```

  Each item refusal prints `loop: refused · ...` beside the list's, exit 1. It is the
  `loop definition` gate leg, and it runs no scope derivation.
- `python loop_lib.py --scopes` reads and checks the definition as `--check` does, then prints
  `loop: scope <tag> · <derive's item line> · <the tags it lists, or none>` per item. Exit 0, every
  line `unarmed` included; 1 on a refused definition, or on a derive that exits non-zero, naming the
  item, the exit and derive's first line.
- `python loop_lib.py --fixture --plant <case>` reads the shipped definition and list with one break
  made in memory, the list's base being the shipped list as read, so nothing runs git, and exits 1 on
  the refusal that break must draw. The cases are `missing-step`, `reordered`, `bad-step`,
  `bad-reach`, `disposition-unknown` (`ask` given twice in the set), `disposition-alias` (the
  `defer` row meaning no member), `witness-no-class`, `witness-bad-class` (class `agent-said`),
  `witness-actor-unlisted` (step.plan's class `actor`), `witness-actor-listed` (that, and listed, which
  reads clean), `actor-list-grown` (a row the base lacks), `actor-list-stale` (a row for step.design,
  whose witness is `history`), `actor-list-no-build` (a row naming `dNoSuchBuild`) and
  `actor-list-foreign` (the builds folder set to foreign after the read, which reads clean). The program
  cases are `needs-cycle`, `needs-unresolved` (a missing tag inside an any-of entry),
  `outcome-unrouted`, `route-unresolved`, `input-no-layer` and `exit-missing`. The actor cases are
  `actor-two` (item.build.unit-pass given a list of two actors), `actor-bad-kind` (its actor
  `agent:x`), `witness-missing` (its witness taken off), `allowance-missing` (item.plan.place's
  allowance taken off), `role-copy` (item.build.unit-pass given its role's `writes`, `product`),
  `role-widen` (item.design.seams, a `role:gov-reuse-scout` item, given `product`), each exiting 1;
  `role-pending` (item.build.unit-pass's actor `role:gov-no-such-role`, printed `pending`) and
  `roles-no-kit` (the roles kit resolved from an empty scratch directory under the host temp
  directory, every role item printed `unarmed`), each exiting 0. `scope-selected` and
  `scope-no-kit` run the read and then the scope verb, exiting 0 when it behaves: the first over a
  scratch manifest under the host temp directory scoping one unit to one item, which must be listed
  on that item's line alone; the second with a scratch directory as the kit directory, where the
  inputs and every scope line must read `unarmed`. `computed-actor` (the item the `acceptance`
  computed witness serves given class `actor`) and `computed-unserved` (that row serving
  `item.build.acceptanc`) each exit 1 naming the row. `PLANTS` names what each breaks. Nothing on disk
  changes but the scratch, which is removed after.
- `python loop_lib.py --grade-site <site> <entry>...` grades one declaration site, `DOD_CORE` or
  `DOD_EXTRA`, whose entries are `<item>` or `<item>:<word>`. The word resolves through
  `[[witness-alias]]` alone. It prints `loop: site <site> · <item> · <word> · <class>` per entry,
  `· until <build>` on a listed actor entry, then each refusal: an entry with no word, a word no alias
  row holds, and for `DOD_CORE` an actor entry the list does not hold and a list row no actor entry
  holds. A `DOD_EXTRA` actor entry reads no list row; its line ends `· adopter-declared, not on the
  shipped list`, and check 53's report names it.
  Exit 0, 1 on a refusal, 2 on usage or a site outside `DECLARATION_SITES`. It reads the list in this
  directory and runs no git. The unattended kit's check 53 calls it, which is why that kit requires
  this one.
- `bash adopt-loop.sh --check` runs the first through the resolved python. The kit renders
  nothing, so its adopter has no `--scaffold`.

## What it does not check

That a workflow row names a workflow the roles kit holds: the roles catalogue checker joins the two
both ways. That a step tag or an item tag is registered: the tag index reads the `[[step]]` rows as
the `step` namespace. That a `command:` name names a real command, that a `hook:` event exists, or
that a pending role's slot is the stem a later build ships. A non-role item's allowance beyond being
non-empty: the allowance vocabulary of a role's `writes` is the roles kit's. A need on an item outside the five programs; that a stand-in path
exists. The transition tables check no witness, no stand-in owner's landing, no reachability or
termination, and no feature or unit row against the routes, nor that every terminal is entered by
a row. The parent route reads no parent planning ending, no hold past the wait ceiling, and no
`withdrawn` post. The transition record judges no witness beyond resolving it and records no feature or
unit move, and it pairs records with trailers by order. That a disposition
record's `Item` names a declared item, which reads `None`, or that a writer resolved an alias before
it wrote. An unknown key on a row is neither read nor refused. That a witness's `by` is true. That
the build an actor-list row names will compute its witness. The guard does not see a change to the
list of guarded paths alone, which the pre-commit block never hands it; a live run's own switch of the
floor, which only its change record and the push arm witness; a pty wrapper giving an agent a
terminal, `--no-verify`, or that a change record's argument is true.
