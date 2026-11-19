#!/usr/bin/env python3
"""loop_lib — the one reader of the loop's definition, `loop.toml` beside this file (TOOL-dDeclaredLoop-1).

    python loop_lib.py --check                    # read the definition, print what was read
    python loop_lib.py --scopes                   # each item's instruction scope, derived
    python loop_lib.py --fixture --plant <case>   # read it with one break planted in memory
    python loop_lib.py --selftest                 # every plant, each held to the exit and line it owes
    python loop_lib.py --grade-site <site> <entry>...   # grade one declaration site's witness entries
    python loop_lib.py seed <item tag> [--build <slug>] [--unit <id>] [--question <text>]   # its seed's paths

The definition holds the gov steps as `[[step]]` rows and one `[[workflow]]` row per workflow of the roles
kit: its build order, the step its work sits in and, where it differs from that step's own word, the reach
word its work orders load practices under. Every other kit reads those facts through this module:
`load_loop` returns the definition whole, `read_steps` its step rows, `read_workflow_order` each workflow's
order and `read_workflow_reach` each workflow's reach word.

The definition also holds the one closed disposition set (TOOL-dDeclaredLoop-16): `[dispositions]` with its
`set`, the words a placing item returns, and `[[disposition-alias]]` rows mapping a legacy `word` to the
member it `means`. `read_dispositions` returns the members, `resolve_disposition` a member for a member or
an alias, `read_outcome_set` the closed outcome set of one `[[item]]` row, the set above where the row
declares `outcomes = "dispositions"` and the row's own list otherwise, and `check_disposition_record`
joins an owner's disposition record to its item's set: True for a member, LoopError for any other word,
None for an item the definition does not declare, which a caller prints as `unarmed` and never as green.
The join compares the word as written, never through an alias.

The definition also classes every witness (TOOL-dDeclaredLoop-5): `[witnesses]` with its `classes`, the
facts the acting agent cannot type, and its `refused` class `actor`, a fact it typed; `[[witness-alias]]`
rows mapping the unattended driver's checker words onto a class, `machine` to `history` and `agent` to
`actor`; and a `witness = { class, by }` on every `[[step]]` row. `read_witness_classes` returns the two
lists and `check_witness_classes` grades the three. Neither runs inside `load_loop`, so a reader that
copies this module and a definition with no witness keeps reading. `actor-witnesses.txt` beside this
file is the shrink-only list of actor witnesses, `<site>\\t<witness>\\t<build>` per row, the build being
the one whose computed witness takes its place: `check_actor_list` grades it both ways against the
definition, against itself at the compare base `read_actor_base` reads, and against each build's
folder under the builds folder `read_builds_dir` reads, only in a tree whose memory-tree conf sets
`DESIGN_RECORD`; elsewhere each row prints `foreign build`. The list's one declaration site is
`DOD_CORE`. `--grade-site` joins a declaration site outside the definition, `DOD_CORE` or `DOD_EXTRA`
of the unattended driver, to the aliases, and `DOD_CORE` to the list both ways; `DOD_EXTRA` is the
adopter's own, its actor entries admitted and printed `adopter-declared`.

The definition also holds each gov step's program (TOOL-dDeclaredLoop-12): one `[[item]]` row per item,
its `tag` `item.<step>.<name>`, its `step`, `actor`, `needs`, `inputs`, `allowance`, `returns`, closed
`outcomes`, `witness`, `owner` and `routes`, an inline table naming one target per outcome: a declared
item, `transition`, or `stand-in:{prefix}/<home>/<file>`. A `needs` entry is a tag, or a list of tags any
one of which meets it. The breakpoint program's rows, tagged `item.review.<name>`, carry the step
`none` and sit in no step (TOOL-dDeclaredLoop-50). `check_program` grades the rows as one needs graph,
ordered by the needs-graph helper below: every need declared, no cycle, each outcome set closed
through `derive_outcome_set`, the rule `read_outcome_set` applies, each outcome routed once to a
target that resolves, each input's text before its first `:` a layer tag `read_layer_tags` reads from
the playbook kit's `layers.toml`, and each step's `exit` an item of that step. `read_items` returns the
rows once both checks hold. `--scopes` prints each item's instruction scope, `derive_item_scope`
running that kit's `load_sets.py derive` once per item as a subprocess, so this module imports no sibling kit. Where the playbook kit does not
resolve, the inputs print `unarmed` and every scope line too; the loop kit declares no edge to it.

Each item declares one actor of one kind (TOOL-dDeclaredLoop-9): `<kind>:<name>`, the kind in
`ACTOR_KINDS`, or the bare `executor` or `owner`. A non-role item carries its own `inputs`, `allowance`
and `returns`. A `role:<slot>` item, the slot a role file's stem, takes each absent one from its role:
`read_role_defaults` reads the roles kit's catalogue through its `roles_lib.load_roles`, the kit found
by `resolve_kit_dir` and imported inside the function, and `resolve_item_declaration` gives the item
its role's `reads`, `writes` and `returns`, naming each field's source. `check_item_declarations`
refuses an actor that is not one string of a declared kind, a non-role item missing a field, a role
item's explicit field equal to its role's (a copy), and a role item's explicit `allowance` other than
`none`. A slot the catalogue lacks prints `pending`, and every role item `unarmed` where the roles
kit does not resolve; neither is a refusal, and the loop kit declares no edge to that kit. Every
item's `witness` is graded by `check_witness_classes` beside the steps', and joins the actor list.

A role item also declares its code seed (TOOL-dPlacedRequest-8): `seed`, what its work order's `code`
slot is computed from, one of the `widens` order of the item kind's schema row `seed` in
`item-schema.toml` beside this file, which `read_seed_values` reads: `none`, absent reading the same,
`write-set`, `question-paths` or `scope-paths`. `check_item_seeds` refuses a value outside that set and
a value other than `none` on an item whose actor is no role. `resolve_item_seed` turns a declared seed
into repository-relative paths, normalised by `resolve_seed_path` and deduplicated in first-seen order,
or one `unarmed — <source>: <why>` line: `write-set` the unit spec's Files touched and `question-paths`
the question's backticked paths, each through the unattended driver's `--path-tokens`, the one path-token
rule, run as a subprocess where that driver resolves; `scope-paths` reads unarmed until a plan record
carries a scope. `seed <item tag>` prints it.

The definition also declares the computed witness kinds (TOOL-dDeclaredLoop-17): one
`[[computed-witness]]` row per witness a tool computes rather than the acting agent typing it, its
`name`, the item it `serves` (or `none`), its `writer` today, a stand-in or an actor, and the build
`armed-by` that writes it for real. `check_computed_witnesses` grades the rows and derives each one's
class from its served item's witness, never typed on the row; `read_computed_witnesses` returns them.
Neither runs inside `load_loop`. The re-run stand-in, `loop_witness.py` beside this file, writes two.

The definition also maps each handle of the unattended driver's two core registries onto the declared
item whose witness its check reads (TOOL-dDeclaredLoop-11): one `[[checklist]]` row per handle, its
`registry` of `CHECKLIST_REGISTRIES`, its `handle` and its `item` tag, and no other key, so no row stores
a position. `read_checklist_rows` returns the rows and `check_checklist_rows` grades them both ways
against the registries and the declared items. Neither runs inside `load_loop` or `--check`: the command
is `loop_checklist.py` beside this file, which reads the driver's registry lines.

The definition also holds one transition table per level (TOOL-dDeclaredLoop-13): `[states]`, and the
`[[transition]]`, `[[stand-in]]` and `[[owed-row]]` rows. `loop_table.py` beside this file reads and
checks them, and answers each move; nothing here reads them.

The definition also pins each typed record kind an item returns or reads at a version
(TOOL-dDeclaredLoop-24): one `[[record-version]]` row per kind, its `kind`, its `version` and its `fields`,
the hash of the kind's row in the memory-tree kit's record table. `loop_items.py` beside this file reads
and checks them with the composed items; nothing here reads them. `read_memory_tree` finds that kit for
this module's two callers, `loop_witness.py` and `loop_items.py`. `run_selftest_cases` is the in-process case
loop that command and `loop_checklist.py` share for `check --selftest`: each case run through the
command's `main`, its output captured, graded by its exit and a line by its opening and a needle.

A definition that does not hold is refused with `LoopError`, a `ValueError` naming the file and the row: a
file that does not read or is no TOML; a `step` or `workflow` table that is no array of tables; the gov
steps missing, repeated or out of order, a tag that is no gov step, or an `order` that is not the step's
place; a step row without a `state` or an `exit`; a workflow row with no name or named twice, an `order`
that is not an integer at or above 0, a `step` that is absent or is neither a step tag nor `none`, or a
`reach` outside `REACH_WORDS`; a `[dispositions]` table whose `set` is not a non-empty array of words
of the `SEG` shape, or holds a word twice; a `[[disposition-alias]]` row whose `word` is a member or
repeats an earlier row's, or whose `means` is no member. The table is graded where the definition holds
it; `read_dispositions` and `--check` refuse a definition that declares no set.

`--check` prints one line per step and per workflow, the set and one line per alias, then a count, and exits 0; a refused definition is one
line and exit 1. It prints each step's program, `loop: program <step> · <n> item(s) · <tags>` in needs
order, then the breakpoint program's as `loop: program review`, or `loop: inputs unarmed` and why
before them where no layer tags resolve, then one `loop: item` line per item in file order, each field's source or `pending` or `unarmed`, and `loop: items · <n>
read · <p> pending · <u> unarmed`, then one `loop: seed <tag> · <value>` line per item and `loop: seeds · <n>
declared · <m> none`. It then prints the witness classes, one line per witness alias and per witness, one
line per list row with its build and the list's base line, the base or `no comparison` and why, the
builds line, the folder or `foreign` and why, one `loop: computed-witness <name> · serves <tag> · class
<class> · writer <writer> · armed by <build>` line per computed witness, then `review_bounds.py`'s
`check_review_bounds` over the policy file at HEAD as `loop: review bounds · <bounds>`, or `loop: review
bounds unarmed · <why>` where the policy kit does not resolve (TOOL-dDeclaredLoop-21), and each refusal of
the items, the list, the computed witnesses and the review bounds as `loop: refused · ...`, exit 1. `--fixture --plant <case>` reads the shipped
definition and list with the named break made in memory, never on disk, the list's base being the
shipped list as read, and exits 1 on the refusal the break must draw, 0 if the reader accepted it. The
plants are `PLANTS`. `--selftest` runs every plant in process through `run_selftest_cases`, each owed the
exit and line `PLANT_OWED` declares beside it, one PASS or FAIL line per plant and a summary, exit 0 only
when every one holds (TOOL-dDeclaredLoop-67 S30); the `loop definition fixtures` leg runs it. `--grade-site <site> <entry>...` prints `loop: site <site> · <item> · <word> ·
<class>` per entry, `· until <build>` on a `DOD_CORE` actor entry, `· adopter-declared, not on the
shipped list` on a `DOD_EXTRA` one, then each refusal, and exits 0, or 1 on a refusal. `--scopes` prints `loop: scope <tag> · <derive's item line> · <the tags it lists, or none>` per
item and exits 0, or 1 on a refused definition or a derive that exits non-zero. `seed <item tag>`
prints the item's seed as `resolve_item_seed` answers it, one path per line or its `unarmed` line, and
exits 0, 1 on a refused definition, or 2 naming an item no row declares or the resolver's refusal. Its
plants, `SEED_PLANTS` and `seed-bad`, run `seed` as a process in a scratch repository and break the
definition's seeds. Exit 2 is a usage error, a site outside `DECLARATION_SITES` included.

WHAT THIS DOES NOT CHECK: that a workflow row names a workflow the roles kit holds, which is that kit's
catalogue check, both ways; that a step tag or an item tag is registered in its namespace, which is the
tag index's; what a `state` word means; that a `command:` name names a real command, a `hook:` event
exists, or a pending role's slot is the stem a later build ships; a non-role item's allowance beyond
being non-empty; a need on an item outside the five programs; that
a `stand-in:` path exists; that a `transition` route reaches a row of the build's transition table,
which `loop_table.py` beside this file checks, both ways (TOOL-dDeclaredLoop-13); that a disposition record's
`Item` names a declared item, which reads None; or that a writer resolved an alias before it wrote. An
unknown key on a row is not read and not refused. That a witness's `by` is true. That a seed path exists,
stays inside the repository, or is the write set a builder really wrote: the seed is what was declared,
read from a spec at HEAD, and a CLOSED or WONTDO spec declares none, as the driver's reader skips it.
Stdlib only, but for
`read_actor_base` and `read_builds_dir`, which import the memory-tree kit's compare base and its conf
reader inside the function, `read_role_defaults`, which imports the roles kit's library there, and
`read_driver_conf`, which sources the unattended driver's `.unattended.conf` in the bash `loop_witness.py`'s
`resolve_bash` finds, imported inside the function (TOOL-dDeclaredLoop-70), and `resolve_item_seed`,
which imports the memory-tree kit's `parse_spec_h1` and runs the unattended driver there, so a reader
calling `load_loop` never reaches them.
"""
import contextlib
import io
import pathlib
import re
import sys
import tempfile
import tomllib

KIT_LOOP_VERSION = "1.1"

DEFINITION = "loop.toml"
#: The shrink-only list of actor witnesses beside the definition, `<site>\t<witness>\t<build>` per row.
ACTOR_LIST = "actor-witnesses.txt"
#: The gov steps, in the loop's order. A definition holds exactly these `[[step]]` rows, in this order.
STEP_TAGS = ("step.plan", "step.design", "step.build", "step.test", "step.deploy")
#: A workflow's `step` when its work sits in no gov step.
NO_STEP = "none"
#: The breakpoint program: its rows' tag segment, `item.review.<name>`, each at step `NO_STEP`, and its
#: key in `check_program`'s return (TOOL-dDeclaredLoop-50).
REVIEW_PROGRAM = "review"
#: The reach words that are no gov step: the entry step and the review breakpoint.
REACH_WORDS = ("entry", "review")
#: One word of a disposition set or an outcome set: the segment a tag is composed of.
SEG = re.compile(r"[a-z0-9][a-z0-9-]*")
#: An `[[item]]` row's `outcomes` when its closed outcome set is the `[dispositions]` set.
OUTCOMES_REF = "dispositions"
#: An item's route target for a cross-step move, whose transition table is its own unit's.
ROUTE_TRANSITION = "transition"
#: An item's route target into a later build: today's stand-in tool, spelled under the install prefix.
ROUTE_STAND_IN = re.compile(r"stand-in:\{prefix\}/[^/\s]+/\S+")
#: The reader whose load set `--scopes` asks `load_sets.py derive` for, beside each item.
SCOPE_READER = "reader.every"
#: `--plant`'s cases, each a break made in the definition as read, and what it does.
PLANTS = {"missing-step": "the step.deploy row taken out",
          "reordered": "the step.test row moved before step.build",
          "bad-step": "the build workflow's step set to step.ship",
          "bad-reach": "the spec-review workflow's reach set to revew",
          "disposition-unknown": "the disposition ask given twice in the set",
          "disposition-alias": "the defer alias's means set to postpone",
          "witness-no-class": "step.plan's witness given no class",
          "witness-bad-class": "step.plan's witness class set to agent-said",
          "witness-actor-unlisted": "step.plan's witness class set to actor",
          "witness-actor-listed": "step.plan's witness class set to actor, and listed in the list and its base",
          "actor-list-grown": "a list row the base lacks",
          "actor-list-stale": "a row for step.design, whose witness is history, in the list and its base",
          "actor-list-no-build": "a row naming dNoSuchBuild in the list and its base",
          "actor-list-foreign": "the builds folder read as a tree whose conf sets no DESIGN_RECORD reads it",
          "needs-cycle": "item.plan.dedupe given a need on item.plan.triage-rule, which needs it",
          "step-none-outside-review": "item.plan.place's step set to none, the breakpoint program's step",
          "review-step-named": "item.review.pin's step set to step.design",
          "needs-unresolved": "item.plan.triage-oracle added to item.plan.record's any-of need",
          "outcome-unrouted": "item.plan.place's route for unplaced taken out",
          "route-unresolved": "item.plan.place's placed outcome routed to item.plan.leas",
          "input-no-layer": "item.plan.input's input read from layer.memry",
          "exit-missing": "step.plan's exit set to item.design.exit, an item of another step",
          "scope-selected": "each item's scope derived over a scratch manifest scoping one unit to item.plan.record",
          "scope-no-kit": "the layer tags and each item's scope resolved from a scratch directory with no playbook kit",
          "actor-two": "item.build.unit-pass's actor set to the list role:gov-builder and command:build.unit-pass",
          "actor-bad-kind": "item.build.unit-pass's actor set to agent:x",
          "witness-missing": "item.build.unit-pass's witness taken off",
          "allowance-missing": "item.plan.place's allowance taken off",
          "role-copy": "item.build.unit-pass given allowance product, its role's writes",
          "role-widen": "item.design.seams, a role:gov-reuse-scout item, given allowance product",
          "role-pending": "item.build.unit-pass's actor set to role:gov-no-such-role",
          "roles-no-kit": "the roles kit resolved from an empty scratch directory",
          "computed-actor": "the acceptance computed witness's served item given witness class actor",
          "computed-unserved": "the acceptance computed witness set to serve item.build.acceptanc",
          "conf-readers-declared": "this module's functions that open a conf compared both ways with its declared "
                                   "readers and routes, no definition read",
          "conf-opener-literal": "a scratch copy of this module given a function, declared nowhere, that opens "
                                 "the memory tree's conf by its literal name",
          "conf-opener-constant": "a scratch copy of this module given a module constant naming the driver's conf "
                                  "and a function, declared nowhere, that opens it",
          "conf-opener-local": "a scratch copy of this module given a function, declared nowhere, that binds the "
                               "memory tree's conf name to a local and opens it",
          "conf-route-opens-none": "a scratch copy of this module whose resolve_memory_root_source returns None",
          "conf-openers-none": "a scratch copy of this module whose read_driver_conf and resolve_memory_root_source "
                               "each return None",
          "conf-module-unparsable": "a scratch copy of this module given a definition that does not parse",
          "seed-bad": "item.build.unit-pass's seed set to diff, and item.plan.place, a command item, given seed "
                      "write-set",
          "seed-write": "seed item.build.unit-pass run in a scratch repository whose unit spec declares one path "
                        "twice, plain and with a leading ./",
          "seed-question": "seed item.plan.research run with a question naming two backticked paths, then with no "
                           "question",
          "seed-scope": "seed item.design.inventory run in a scratch repository, its scope-paths source armed by "
                        "no plan record"}
#: `--selftest`'s owed answer of each plant (TOOL-dDeclaredLoop-67 S30): its exit, the opening of a line
#: it prints and a needle that line holds, each pair found by running the plant alone at the pass's base.
#: A definition the reader refuses prints `loop: <path>: <why>`, a graded refusal `loop: refused · <why>`.
PLANT_OWED = {"missing-step": (1, "loop: ", "the step step.deploy is missing"),
              "reordered": (1, "loop: ", "the step step.test is out of order"),
              "bad-step": (1, "loop: ", "step 'step.ship' is neither a declared step tag nor none"),
              "bad-reach": (1, "loop: ", "reach 'revew' is not one of"),
              "disposition-unknown": (1, "loop: ", "the disposition ask is given twice"),
              "disposition-alias": (1, "loop: ", "means 'postpone', which is no member of the set"),
              "witness-no-class": (1, "loop: ", "the step step.plan carries a witness with no class"),
              "witness-bad-class": (1, "loop: ", "witness class 'agent-said' is no class and not refused"),
              "witness-actor-unlisted": (1, "loop: refused · ", "the actor witness step.plan step.plan has no list row"),
              "witness-actor-listed": (0, "loop: actor witness step.plan · step.plan · until ", ""),
              "actor-list-grown": (1, "loop: refused · ", "is absent from the list at its compare base"),
              "actor-list-stale": (1, "loop: refused · ", "the list row step.design step.design names no actor witness"),
              "actor-list-no-build": (1, "loop: refused · ", "names the build dNoSuchBuild"),
              "actor-list-foreign": (0, "loop: actor witness ", "foreign build, not graded"),
              "needs-cycle": (1, "loop: ", "the item needs form a cycle"),
              "step-none-outside-review": (1, "loop: ", "the item item.plan.place step 'none' is not step.plan"),
              "review-step-named": (1, "loop: ", "the item item.review.pin step 'step.design' is not none"),
              "needs-unresolved": (1, "loop: ", "needs item.plan.triage-oracle, which no [[item]] row declares"),
              "outcome-unrouted": (1, "loop: ", "the item item.plan.place outcome unplaced has no route"),
              "route-unresolved": (1, "loop: ", "routes placed to 'item.plan.leas'"),
              "input-no-layer": (1, "loop: ", "names no layer tag"),
              "exit-missing": (1, "loop: ", "the step step.plan exit 'item.design.exit' is no declared item"),
              "scope-selected": (0, "loop: fixture · unit.loop-fixture listed on item.plan.record", ""),
              "scope-no-kit": (0, "loop: scope ", " · unarmed · "),
              "actor-two": (1, "loop: refused · ", "one actor per item"),
              "actor-bad-kind": (1, "loop: refused · ", "actor kind agent is not one of"),
              "witness-missing": (1, "loop: ", "carries no witness"),
              "allowance-missing": (1, "loop: refused · ", "carries no allowance"),
              "role-copy": (1, "loop: refused · ", "copies its role gov-builder's writes"),
              "role-widen": (1, "loop: refused · ", "widens its role gov-reuse-scout"),
              "role-pending": (0, "loop: item item.build.unit-pass · role:gov-no-such-role · pending", ""),
              "roles-no-kit": (0, "loop: item ", " · unarmed · no roles kit holding"),
              "computed-actor": (1, "loop: refused · ", "whose witness class actor is refused"),
              "computed-unserved": (1, "loop: refused · ", "serves 'item.build.acceptanc'"),
              "conf-readers-declared": (0, "loop: conf readers declared · ", " opener(s) · "),
              "conf-opener-literal": (1, "loop: refused · ", "read_literal_conf opens a conf and is in neither "
                                                             "CONF_READERS nor CONF_ROUTES"),
              "conf-opener-constant": (1, "loop: refused · ", "read_constant_conf opens a conf and is in neither "
                                                              "CONF_READERS nor CONF_ROUTES"),
              "conf-opener-local": (1, "loop: refused · ", "read_local_conf opens a conf and is in neither "
                                                           "CONF_READERS nor CONF_ROUTES"),
              "conf-route-opens-none": (1, "loop: refused · ", "resolve_memory_root_source is in CONF_ROUTES and "
                                                               "opens no conf"),
              "conf-openers-none": (1, "loop: refused · ", "no conf opener found in loop_lib.py"),
              "conf-module-unparsable": (1, "loop: refused · ", "cannot be read as the conf constants' module"),
              "seed-bad": (1, "loop: refused · ", "the item item.plan.place seed 'write-set' sits on the actor"),
              "seed-write": (0, "loop: fixture · seed-write held · ", "fx/seed-plant.txt"),
              "seed-question": (0, "loop: fixture · seed-question held · ", "fx/y.sh fx/z.sh"),
              "seed-scope": (0, "loop: fixture · seed-scope held · ", "unarmed — scope-paths:")}
#: The plants whose break is in what the scope verb reads rather than in the definition, so `--check`
#: runs whole and the scope verb runs after it.
SCOPE_PLANTS = ("scope-selected", "scope-no-kit")
#: The plants that read no definition and run `check_conf_readers_plant`, over this file for
#: `conf-readers-declared` and over the scratch copy `write_conf_plant` writes for each other one
#: (TOOL-dDeclaredLoop-117 S2).
CONF_PLANTS = ("conf-readers-declared", "conf-opener-literal", "conf-opener-constant", "conf-opener-local",
               "conf-route-opens-none", "conf-openers-none", "conf-module-unparsable")
#: The `scope-selected` plant's unit: one scratch manifest row scoped to one item.
PLANT_SCOPE_UNIT = ("unit.loop-fixture", "item.plan.record")
#: The item kind's row schema beside the definition, whose `seed` row's `widens` order is the value set of
#: an item's declared code seed (TOOL-dPlacedRequest-8).
ITEM_SCHEMA = "item-schema.toml"
#: An item's `seed` where it declares none: the value that hands no path.
SEED_NONE = "none"
#: The line a `scope-paths` seed resolves to until a plan record carries a scope.
SEED_SCOPE_UNARMED = "unarmed — scope-paths: no plan record carries a scope; dRankedPlan's plan.record arms it"
#: A `--build` value the seed resolver takes: one path segment, so it never walks out of the builds folder.
SEED_BUILD = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*")
#: The bound on the driver's `--path-tokens` call, in seconds (PINNED 2026-11-20: a bound chosen, not measured).
SEED_DRIVER_BOUND = 120
#: The resolver's plants: each runs the `seed` command in a scratch repository, never a break in the definition.
SEED_PLANTS = ("seed-write", "seed-question", "seed-scope")
#: The one path the `seed-write` plant's spec declares twice, plain and with a leading `./`: the plant's own,
#: under its scratch repository.
PLANT_SEED_PATH = "fx/seed-plant.txt"
#: The `seed-question` plant's question and the two paths it names backticked.
PLANT_SEED_QUESTION = ("is `fx/y.sh` racing with `fx/z.sh`?", ["fx/y.sh", "fx/z.sh"])
#: The declaration sites outside the definition whose entries `--grade-site` grades: the unattended
#: driver's core Definition of Done and the conf's extra one, each a set of `<item>:<word>` entries.
DECLARATION_SITES = ("DOD_CORE", "DOD_EXTRA")
#: An item's actor kinds, closed (TOOL-dDeclaredLoop-9): one actor per item, of one kind.
ACTOR_KINDS = ("role", "command", "executor", "hook", "owner")
#: An item's actor, `<kind>:<name>`, fullmatched; the bare `executor` and `owner` are the other form.
ACTOR_FORM = re.compile(r"([a-z]+):([^\s,:]+)")
#: The unattended driver's two core handle registries a `[[checklist]]` row maps from (TOOL-dDeclaredLoop-11).
CHECKLIST_REGISTRIES = ("DOD_CORE", "DIRECTIVES_CORE")
#: A `[[checklist]]` row's keys, and its only keys: a row never stores a position.
CHECKLIST_KEYS = ("registry", "handle", "item")


class LoopError(ValueError):
    """The definition does not hold; the message is `<where>: <what>`, the file and the row."""

    def __init__(self, where, what):
        super().__init__("%s: %s" % (where, what))


def check_loop(data, where):
    """`data`, a parsed definition, returned as `{"step": [...], "workflow": [...], "dispositions": [...]}`
    once every row holds, `dispositions` the members of the set and empty where the definition holds no
    `[dispositions]` table; LoopError naming `where` and the first row that does not."""
    tables = {}
    for table in ("step", "workflow", "disposition-alias"):
        rows = data.get(table, [])
        if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
            raise LoopError(where, "'%s' is not an array of tables" % table)
        tables[table] = rows
    tags = [r.get("tag") for r in tables["step"]]
    for tag in tags:
        if tag not in STEP_TAGS:
            raise LoopError(where, "step row %r names no gov step; the gov steps are %s" % (tag, " ".join(STEP_TAGS)))
        if tags.count(tag) > 1:
            raise LoopError(where, "the step %s is repeated" % tag)
    for tag in STEP_TAGS:
        if tag not in tags:
            raise LoopError(where, "the step %s is missing" % tag)
    for n, (row, want) in enumerate(zip(tables["step"], STEP_TAGS), 1):
        if row["tag"] != want:
            raise LoopError(where, "the step %s is out of order: row %d is %s's place" % (row["tag"], n, want))
        if row.get("order") != n or isinstance(row.get("order"), bool):
            raise LoopError(where, "the step %s carries order %r, and its place is %d" % (want, row.get("order"), n))
        for key in ("state", "exit"):
            if not isinstance(row.get(key), str) or not row[key]:
                raise LoopError(where, "the step %s carries no %s" % (want, key))
    seen = set()
    for n, row in enumerate(tables["workflow"], 1):
        name = row.get("name")
        at = "workflow row %d (%s)" % (n, name if isinstance(name, str) and name else "unnamed")
        if not isinstance(name, str) or not name:
            raise LoopError(where, "%s carries no name" % at)
        if name in seen:
            raise LoopError(where, "%s repeats the name of an earlier row" % at)
        seen.add(name)
        order = row.get("order")
        if not isinstance(order, int) or isinstance(order, bool) or order < 0:
            raise LoopError(where, "%s order %r is not an integer at or above 0" % (at, order))
        if "step" not in row:
            raise LoopError(where, "%s carries no step" % at)
        if row["step"] != NO_STEP and row["step"] not in STEP_TAGS:
            raise LoopError(where, "%s step %r is neither a declared step tag nor %s" % (at, row["step"], NO_STEP))
        if "reach" in row and row["reach"] not in REACH_WORDS:
            raise LoopError(where, "%s reach %r is not one of %s" % (at, row["reach"], " ".join(REACH_WORDS)))
    members = []
    if "dispositions" in data:
        members = data["dispositions"].get("set") if isinstance(data["dispositions"], dict) else None
        if not isinstance(members, list) or not members:
            raise LoopError(where, "'dispositions' carries no non-empty set")
        for word in members:
            if not isinstance(word, str) or not SEG.fullmatch(word):
                raise LoopError(where, "the disposition %r is not one word of the shape %s" % (word, SEG.pattern))
            if members.count(word) > 1:
                raise LoopError(where, "the disposition %s is given twice" % word)
    check_alias_rows(tables.pop("disposition-alias"), members, "disposition-alias", where)
    tables["dispositions"] = list(members)
    return tables


def check_alias_rows(rows, members, table, where):
    """Each row of the alias table `table`: its `word` is no member and no earlier row's, and its
    `means` is a member; LoopError naming `where` and the first row that does not."""
    words = set()
    for n, row in enumerate(rows, 1):
        word, means = row.get("word"), row.get("means")
        at = "%s row %d (%s)" % (table, n, word if isinstance(word, str) and word else "unnamed")
        if not isinstance(word, str) or not word:
            raise LoopError(where, "%s carries no word" % at)
        if word in members:
            raise LoopError(where, "%s names a member of the set, which needs no alias" % at)
        if word in words:
            raise LoopError(where, "%s repeats the word of an earlier row" % at)
        words.add(word)
        if means not in members:
            raise LoopError(where, "%s means %r, which is no member of the set: %s" % (at, means, " ".join(members)))


def resolve_alias(rows, word):
    """The `means` of the alias row whose `word` is `word`, None where no row holds it."""
    return next((row["means"] for row in rows if row.get("word") == word), None)


def check_witness_classes(data, where):
    """`data`'s witnesses graded: `[witnesses]`, then every `[[witness-alias]]` row, then every `[[step]]`
    row's `witness` and every `[[item]]` row's after them (TOOL-dDeclaredLoop-9); `[(site, class, by)]`
    per witness, a step's or an item's site its tag. LoopError naming `where` and the table and row that
    does not hold, a definition declaring no `[witnesses]` included."""
    table = data.get("witnesses")
    if not isinstance(table, dict):
        raise LoopError(where, "declares no witness classes, a [witnesses] table with classes and refused")
    for key in ("classes", "refused"):
        words = table.get(key)
        if not isinstance(words, list) or not words:
            raise LoopError(where, "'witnesses' carries no non-empty %s" % key)
        for word in words:
            if not isinstance(word, str) or not SEG.fullmatch(word):
                raise LoopError(where, "the witness class %r is not one word of the shape %s" % (word, SEG.pattern))
            if words.count(word) > 1:
                raise LoopError(where, "the witness class %s is given twice" % word)
    both = sorted(set(table["classes"]) & set(table["refused"]))
    if both:
        raise LoopError(where, "the witness class %s is both a class and refused" % " ".join(both))
    members = table["classes"] + table["refused"]
    aliases = data.get("witness-alias", [])
    if not isinstance(aliases, list) or not all(isinstance(r, dict) for r in aliases):
        raise LoopError(where, "'witness-alias' is not an array of tables")
    check_alias_rows(aliases, members, "witness-alias", where)
    witnesses = []
    sites = [("step", r) for r in data.get("step", [])] + [("item", r) for r in read_item_rows(data, where)]
    for kind, row in sites:
        tag, witness = row.get("tag"), row.get("witness")
        if witness is None:
            raise LoopError(where, "the %s %s carries no witness, an inline table { class, by }" % (kind, tag))
        if not isinstance(witness, dict) or not isinstance(witness.get("class"), str):
            raise LoopError(where, "the %s %s carries a witness with no class" % (kind, tag))
        if not isinstance(witness.get("by"), str) or not witness["by"].strip():
            raise LoopError(where, "the %s %s carries a witness with no by, what witnesses it" % (kind, tag))
        if witness["class"] not in members:
            raise LoopError(where, "the %s %s witness class %r is no class and not refused: %s" % (
                kind, tag, witness["class"], " ".join(members)))
        witnesses.append((tag, witness["class"], witness["by"]))
    return witnesses


def check_computed_witnesses(data, where):
    """`data`'s `[[computed-witness]]` rows graded (TOOL-dDeclaredLoop-17 S7), returned in file order as
    `{"name", "serves", "class", "writer", "armed-by"}`, `class` the served item's witness class, derived
    and never typed, `none` for a row serving `none`. LoopError naming `where` and the row: a `name`
    outside `SEG` or given twice; a `serves` neither `none` nor a declared `[[item]]` tag; a served item
    whose witness class is refused; a `writer` neither `ROUTE_STAND_IN` nor `<kind>:<name>` of
    `ACTOR_KINDS`; an empty `armed-by`. A definition with no such table holds no row."""
    rows = data.get("computed-witness", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise LoopError(where, "'computed-witness' is not an array of tables")
    items = {r.get("tag"): r for r in read_item_rows(data, where)}
    table = data.get("witnesses")
    refused = table.get("refused", []) if isinstance(table, dict) else []
    out, names = [], set()
    for n, row in enumerate(rows, 1):
        name, serves, writer, armed = row.get("name"), row.get("serves"), row.get("writer"), row.get("armed-by")
        at = "computed-witness row %d (%s)" % (n, name if isinstance(name, str) and name else "unnamed")
        if not isinstance(name, str) or not SEG.fullmatch(name):
            raise LoopError(where, "%s name %r is not one word of the shape %s" % (at, name, SEG.pattern))
        if name in names:
            raise LoopError(where, "%s repeats the name of an earlier row" % at)
        names.add(name)
        if serves == NO_STEP:
            cls = NO_STEP
        elif serves in items:
            witness = items[serves].get("witness")
            cls = witness.get("class") if isinstance(witness, dict) else None
            if cls in refused:
                raise LoopError(where, "%s serves %s, whose witness class %s is refused: a computed witness "
                                       "replaces a fact the acting agent typed, never serves one" % (at, serves, cls))
        else:
            raise LoopError(where, "%s serves %r, which is neither %s nor a declared [[item]] tag" % (
                at, serves, NO_STEP))
        form = ACTOR_FORM.fullmatch(writer) if isinstance(writer, str) else None
        if not (isinstance(writer, str) and ROUTE_STAND_IN.fullmatch(writer)) and not (
                form and form.group(1) in ACTOR_KINDS):
            raise LoopError(where, "%s writer %r is neither stand-in:{prefix}/<home>/<file> nor <kind>:<name> of "
                                   "%s" % (at, writer, " ".join(ACTOR_KINDS)))
        if not isinstance(armed, str) or not armed.strip():
            raise LoopError(where, "%s carries no armed-by, the build that writes it for real" % at)
        out.append({"name": name, "serves": serves, "class": cls, "writer": writer, "armed-by": armed})
    return out


def read_computed_witnesses(kit_dir):
    """The `[[computed-witness]]` rows of the definition in `kit_dir`, graded by `check_computed_witnesses`,
    each with its derived `class`; LoopError where the definition or a row does not hold."""
    return check_computed_witnesses(*read_definition(kit_dir))


def read_checklist_rows(kit_dir):
    """The `[[checklist]]` rows of the definition in `kit_dir`, in file order, ungraded; LoopError where
    the definition does not read or `checklist` is no array of tables."""
    data, where = read_definition(kit_dir)
    rows = data.get("checklist", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise LoopError(where, "'checklist' is not an array of tables")
    return rows


def check_checklist_rows(rows, registries, items):
    """`(lines, refusals)` of the `[[checklist]]` `rows` against `registries`, each of
    `CHECKLIST_REGISTRIES` mapped to its handles in order, and `items`, the declared `[[item]]` rows. A
    refusal per row carrying a key outside `CHECKLIST_KEYS` or missing one, naming a registry outside
    `CHECKLIST_REGISTRIES`, a handle its registry lacks or one an earlier row maps, or an item that opens
    no `item.<step>.` of a gov step or that no declared row holds; and per core handle no row maps. A
    `loop: checklist <registry> · <handle> · <item>` line per row, then a count line per registry."""
    declared = {r.get("tag") for r in items}
    shape = re.compile(r"item\.(%s)\.%s" % ("|".join(t.split(".", 1)[1] for t in STEP_TAGS), SEG.pattern))
    lines, refusals, mapped = [], [], {}
    for n, row in enumerate(rows, 1):
        reg, handle, item = (row.get(k) for k in CHECKLIST_KEYS)
        at = "checklist row %d (%s)" % (n, handle if isinstance(handle, str) and handle else "no handle")
        extra = [k for k in row if k not in CHECKLIST_KEYS]
        if extra:
            refusals.append("%s carries the key %s, outside %s: a row stores no position" % (
                at, " ".join(extra), " ".join(CHECKLIST_KEYS)))
        missing = [k for k in CHECKLIST_KEYS if not (isinstance(row.get(k), str) and row.get(k))]
        if missing:
            refusals.append("%s carries no %s" % (at, " and no ".join(missing)))
            continue
        if reg not in CHECKLIST_REGISTRIES:
            refusals.append("%s names the registry %s, neither of %s" % (at, reg, " ".join(CHECKLIST_REGISTRIES)))
            continue
        if handle not in registries.get(reg, []):
            refusals.append("%s maps %s %s, a handle %s does not hold" % (at, reg, handle, reg))
        elif (reg, handle) in mapped:
            refusals.append("%s maps %s %s, which row %d maps already: one row per handle" % (
                at, reg, handle, mapped[(reg, handle)]))
        else:
            mapped[(reg, handle)] = n
        if not shape.fullmatch(item):
            refusals.append("%s maps onto %s, which opens no item.<step>. of a gov step" % (at, item))
        elif item not in declared:
            refusals.append("%s maps onto %s, which no [[item]] row declares" % (at, item))
        lines.append("loop: checklist %s · %s · %s" % (reg, handle, item))
    for reg in CHECKLIST_REGISTRIES:
        handles = registries.get(reg, [])
        for handle in handles:
            if (reg, handle) not in mapped:
                refusals.append("%s %s has no [[checklist]] row mapping it onto an item" % (reg, handle))
        lines.append("loop: checklist-count %s · %d handle(s) · %d mapped" % (
            reg, len(handles), sum(1 for r, _h in mapped if r == reg)))
    return lines, refusals


def read_witness_classes(kit_dir):
    """`{"classes": [...], "refused": [...]}` of the definition in `kit_dir`, its witnesses graded;
    LoopError for a definition that declares no `[witnesses]` table or whose witnesses do not hold."""
    data, where = read_definition(kit_dir)
    check_witness_classes(data, where)
    return {"classes": list(data["witnesses"]["classes"]), "refused": list(data["witnesses"]["refused"])}


def check_actor_list(rows, base_rows, sites, builds_dir):
    """One refusal per row of the actor-witness list `rows`, its lines as read, that is not three
    tab-separated fields; that `base_rows`, the list at the compare base, lacks (None is no comparison);
    whose site is a definition site holding no actor witness of that name, or neither such a site nor
    `DOD_CORE`; or, where `builds_dir` is a path, whose build has no `<builds_dir>/<build>/README.md`.
    With `builds_dir` None, the tree declares no chain and no row's build is tested. And one per actor
    witness of a definition site no row lists. `sites` maps each definition site to `{witness: class}`."""
    refusals, listed = [], set()
    for line in rows:
        fields = line.split("\t")
        if len(fields) != 3 or not all(f.strip() for f in fields):
            refusals.append("the list row %r is not three tab-separated fields, <site> <witness> <build>" % line)
            continue
        site, witness, build = fields
        listed.add((site, witness))
        if base_rows is not None and line not in base_rows:
            refusals.append("the list row %s %s %s is absent from the list at its compare base, and the list "
                            "only shrinks" % (site, witness, build))
        if site in sites:
            if sites[site].get(witness) != "actor":
                refusals.append("the list row %s %s names no actor witness: %s's witness %s is %s" % (
                    site, witness, site, witness, sites[site].get(witness, "absent")))
        elif site != "DOD_CORE":
            refusals.append("the list row %s %s names a site that is neither a definition site nor DOD_CORE, "
                            "the one declaration site the list grades" % (site, witness))
        readme = pathlib.Path(builds_dir) / build / "README.md" if builds_dir is not None else None
        if readme is not None and not readme.is_file():
            refusals.append("the list row %s %s names the build %s, which has no %s" % (
                site, witness, build, readme.as_posix()))
    for site, named in sites.items():
        for witness, cls in named.items():
            if cls == "actor" and (site, witness) not in listed:
                refusals.append("the actor witness %s %s has no list row naming the build that computes it" % (
                    site, witness))
    return refusals


# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


# The order a needs graph allows, and its cycles: `check_program` orders the items through it.
# >>> needs_graph_py -- canonical copy: needs_graph.py in the gov lib dir (byte-identical; gated)
class NeedsCycle(ValueError):
    """No order exists. `stuck` holds the nodes left unplaced, sorted: every node on a cycle and every
    node that needs one, so `scan_cycles` is what names the cycles themselves."""

    def __init__(self, stuck):
        super().__init__("a needs cycle among %s" % ", ".join(stuck))
        self.stuck = stuck


def derive_needs_order(nodes, needs):
    """`nodes` in an order where each follows every node `needs[node]` names: Kahn, each ready tier
    sorted, so the order is sorted order wherever no edge applies. A need outside `nodes` constrains
    nothing, and a node needing itself is a cycle. NeedsCycle where no order exists."""
    want = set(nodes)
    deps = {n: {d for d in needs.get(n, ()) if d in want} for n in nodes}
    out, placed = [], set()
    while len(out) < len(nodes):
        ready = sorted(n for n in nodes if n not in placed and deps[n] <= placed)
        if not ready:
            raise NeedsCycle(sorted(n for n in nodes if n not in placed))
        out.extend(ready)
        placed.update(ready)
    return out


def scan_cycles(edges, live=None):
    """Every cycle of `edges`, `{node: the nodes it points at}`, each reported ONCE and rotated to its
    smallest member, in sorted order; a node pointing at itself is a cycle of one. `live`, a predicate
    over a node, leaves out each node it answers False for, as a start and as a step; None keeps all.
    Once and rotated, because a cycle found from each of its members is one finding."""
    keep = live if live is not None else (lambda node: True)
    found = {}
    for start in [a for a in sorted(edges) if keep(a)]:
        stack = [(start, (start,))]
        while stack:
            node, path = stack.pop()
            for nxt in sorted(edges.get(node, ())):
                if not keep(nxt):
                    continue
                if nxt == start:
                    low = path.index(min(path))
                    key = path[low:] + path[:low]
                    found.setdefault(key, key)
                elif nxt not in path:
                    stack.append((nxt, path + (nxt,)))
    return [found[k] for k in sorted(found)]
# <<< needs_graph_py


def read_memory_tree(anchor):
    """The memory-tree kit's directory holding `anchor`, found from this kit and put on `sys.path`;
    LookupError naming where it looked."""
    mt_dir = resolve_kit_dir("memory-tree", anchor, pathlib.Path(__file__).absolute().parent)
    if str(mt_dir) not in sys.path:
        sys.path.insert(0, str(mt_dir))
    return mt_dir


def read_actor_base(kit_dir):
    """`(rows or None, why)`: the actor-witness list's lines at the compare base and the base, or None
    and why there is no comparison: no work tree, no memory-tree kit, no base, or no list at the base."""
    import subprocess

    def read(*args):
        try:
            p = subprocess.run(["git", "-C", str(kit_dir), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
        except OSError:
            return None
        return p.stdout if p.returncode == 0 else None

    top, prefix = read("rev-parse", "--show-toplevel"), read("rev-parse", "--show-prefix")
    if top is None or prefix is None:
        return None, "the loop kit sits in no git work tree"
    try:
        mt_dir = resolve_kit_dir("memory-tree", "coverage_join.py", kit_dir)
    except LookupError as e:
        return None, str(e)
    if str(mt_dir) not in sys.path:
        sys.path.insert(0, str(mt_dir))
    from coverage_join import resolve_compare_base
    base, why = resolve_compare_base(top.strip())
    if not base:
        return None, why
    text = read("show", "%s:%s%s" % (base, prefix.strip(), ACTOR_LIST))
    if text is None:
        return None, "the list is absent at the base %s" % base
    return [ln for ln in text.splitlines() if ln.strip()], base


def read_builds_dir(kit_dir, root):
    """`(builds_dir, why)`: `<root>/<records root>/builds`, the root `resolve_memory_root` answers, where the
    memory tree's conf at `root` sets `DESIGN_RECORD`, the mark of the tree that owns the chain's build
    names, or None and why: no memory-tree kit, no `DESIGN_RECORD` in the conf, a missing conf included,
    or a records root that does not resolve, the two confs naming two roots among them, its `records
    root:` reason as the why (TOOL-dDeclaredLoop-116). The memory-tree kit's `read_design_conf` is
    imported inside the function, as `read_actor_base` imports its compare base."""
    try:
        mt_dir = resolve_kit_dir("memory-tree", "design_lib.py", kit_dir)
    except LookupError as e:
        return None, str(e)
    if str(mt_dir) not in sys.path:
        sys.path.insert(0, str(mt_dir))
    from design_lib import read_design_conf
    conf = read_design_conf(root)
    if not str(conf.get("DESIGN_RECORD") or "").strip():
        return None, "%s sets no DESIGN_RECORD, or is absent, so the chain's builds are not this tree's" % (
            (pathlib.Path(root) / ".memory-tree.conf").as_posix())
    try:
        memory_root = resolve_memory_root(root)
    except (LookupError, ValueError) as e:
        return None, str(e)
    return pathlib.Path(root) / memory_root / "builds", ""


#: The driver conf's answers held for the process, keyed by the conf and the names read (TOOL-dDeclaredLoop-70).
DRIVER_CONF_READS = {}
#: The pair the conf subshell prints last, the read's verdict, as the unattended kit gate imports a conf.
CONF_SENTINEL = "__CONF_IMPORT_OK__\0\0"
#: A name `read_driver_conf` reads: a shell variable's shape, held before it reaches `eval`.
CONF_NAME = re.compile(r"[A-Z][A-Z0-9_]*")


def read_driver_conf(tree, names):
    """`{name: value}` for each of `names` the unattended driver's `.unattended.conf` sets, the conf at the
    top of `tree`'s work tree, the first of `tree` and its parents holding `.git`, else `tree`: sourced in
    bash with the top as the working directory, as the driver sources it, each value read back with a
    sentinel after them. Each name is unset before the source, so a value the caller's environment
    exports never reads as the conf's, and `ROOT` and `CONF` are set to the top and its conf, as the
    driver sets them (TOOL-dDeclaredLoop-79). `{}` where the file is absent; each answer held for the process. ValueError on a
    name outside `[A-Z][A-Z0-9_]*`, before any bash starts; LoopError `driver conf unreadable` naming the
    conf and why, where no bash sees it, it does not start, exits non-zero or prints no sentinel
    (TOOL-dDeclaredLoop-70). `loop_witness.py`'s `resolve_bash` is imported inside the function, since
    that module imports this one."""
    import subprocess
    names = tuple(names)
    bad = [n for n in names if not CONF_NAME.fullmatch(str(n))]
    if bad:
        raise ValueError("read_driver_conf: %s is no variable name" % bad[0])
    tree = pathlib.Path(tree).absolute()
    top = next((d for d in (tree, *tree.parents) if (d / ".git").exists()), tree)
    conf = top / ".unattended.conf"
    if not conf.is_file():
        return {}
    key = (str(conf), names)
    if key not in DRIVER_CONF_READS:
        from loop_witness import resolve_bash
        bash = resolve_bash(conf.as_posix())
        if bash is None:
            raise LoopError("driver conf unreadable", "%s — no bash that can see it" % conf.as_posix())
        # TOOL-dDeclaredLoop-79 S1, S2: each requested name unset, so a caller's export never reads as the
        # conf's, then ROOT and CONF set as the driver's load_driver_conf sets them before its source
        script = ('__rdc_conf=$1; __rdc_root=$2; shift 2; __rdc_names=("$@")\n'
                  'for __rdc_n in "${__rdc_names[@]}"; do unset "$__rdc_n"; done\n'
                  'ROOT=$__rdc_root; CONF="$ROOT/.unattended.conf"\n'
                  '. "$__rdc_conf" >/dev/null 2>&1 || exit 9\n'
                  'for n in "${__rdc_names[@]}"; do eval "v=\\${$n-__UNSET__}"; printf "%s\\0%s\\0" "$n" "$v"; done\n'
                  'printf "__CONF_IMPORT_OK__\\0\\0"')
        try:
            p = subprocess.run([bash, "-c", script, "_", conf.as_posix(), top.as_posix(), *names], cwd=str(top),
                               stdin=subprocess.DEVNULL, capture_output=True)
        except OSError as e:
            raise LoopError("driver conf unreadable", "%s — %s" % (conf.as_posix(), e)) from None
        if p.returncode != 0:
            raise LoopError("driver conf unreadable", "%s — exit %d" % (conf.as_posix(), p.returncode))
        out = p.stdout.decode("utf-8", "replace")
        if not out.endswith(CONF_SENTINEL):
            raise LoopError("driver conf unreadable", "%s — no __CONF_IMPORT_OK__ sentinel" % conf.as_posix())
        fields = out[:-len(CONF_SENTINEL)].split("\0")[:-1]
        DRIVER_CONF_READS[key] = {n: v for n, v in zip(fields[::2], fields[1::2]) if v != "__UNSET__"}
    return dict(DRIVER_CONF_READS[key])


#: The driver's root `resolve_memory_root` took, held per resolved tree and the bytes of its conf (TOOL-dDeclaredLoop-72).
DRIVER_ROOTS = {}


def resolve_memory_root_source(tree):
    """`(root, source)`: the root a build's records sit under in `tree` and the conf it came from. The
    `MEMORY_ROOT` the driver's `.unattended.conf` sets, read through `read_driver_conf`, `memory` where it
    leaves the key unset, wherever that conf is a file, source `.unattended.conf`; else the `MEMORY_ROOT`
    of `.memory-tree.conf`, `memory` where it leaves the key unset, wherever that conf is a file, source
    `.memory-tree.conf` (TOOL-dDeclaredLoop-82 S15); else `memory`, source `default`. Each value
    stripped of whitespace and slashes, a blank one unset. ValueError `records root:` where both confs
    name a root and the two differ; LookupError where the memory-tree kit does not resolve
    (TOOL-dDeclaredLoop-72, TOOL-dDeclaredLoop-76). The kit's `read_design_conf` is imported inside the
    function, as `read_builds_dir` imports it."""
    read_memory_tree("design_lib.py")
    from design_lib import read_design_conf
    mt = (read_design_conf(tree).get("MEMORY_ROOT") or "").strip().strip("/")
    conf = pathlib.Path(tree).resolve() / ".unattended.conf"
    if not conf.is_file():
        if mt or (pathlib.Path(tree) / ".memory-tree.conf").is_file():
            return mt or "memory", ".memory-tree.conf"
        return "memory", "default"
    key = (str(conf), conf.read_bytes())
    if key not in DRIVER_ROOTS:
        # ponytail: read_driver_conf holds its answer per conf path, so a conf rewritten in this process is
        # dropped there before it is read again
        for held in [k for k in DRIVER_CONF_READS if k[1] == ("MEMORY_ROOT",)]:
            del DRIVER_CONF_READS[held]
        ua = (read_driver_conf(tree, ["MEMORY_ROOT"]).get("MEMORY_ROOT") or "").strip().strip("/")
        DRIVER_ROOTS[key] = ua or "memory"
    ua = DRIVER_ROOTS[key]
    if mt and mt != ua:
        raise ValueError("records root: .unattended.conf says %s, .memory-tree.conf says %s — the driver writes "
                         "under %s" % (ua, mt, ua))
    return ua, ".unattended.conf"


def resolve_memory_root(tree):
    """The root of `resolve_memory_root_source`'s pair: the one reader every loop module takes the root from."""
    return resolve_memory_root_source(tree)[0]


def derive_fixture_boundary(tree):
    """The fixture code of a parsed module, sorted by line: every `def` and `async def`, nested ones
    included, whose name split on `_` holds the whole token `fixture` or `plant`, case-sensitive; a
    class, a module constant and a name holding neither token stay out (TOOL-dDeclaredLoop-80 S1)."""
    import ast
    return sorted((f for f in ast.walk(tree) if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef))
                   and {"fixture", "plant"} & set(f.name.split("_"))), key=lambda f: f.lineno)


def derive_import_aliases(tree):
    """`{local name: dotted name}` for each name an absolute `import` or `from ... import` of a parsed
    module binds, aliased or not: `import a.b as c` binds `c` to `a.b`, `import a.b` binds `a` to `a`,
    `from m import n` binds `n` and `from m import n as c` binds `c`, each to `m.n`. A relative import
    and a star import bind none (TOOL-dDeclaredLoop-82 S10)."""
    import ast
    aliases = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                aliases[a.asname or a.name.split(".")[0]] = a.name if a.asname else a.name.split(".")[0]
        elif isinstance(node, ast.ImportFrom) and not node.level and node.module:
            for a in node.names:
                if a.name != "*":
                    aliases[a.asname or a.name] = "%s.%s" % (node.module, a.name)
    return aliases


def check_conf_name(node, docs=()):
    """True where the syntax subtree of `node` holds anywhere a str constant containing
    `.memory-tree.conf` or `.unattended.conf`, an f-string's literal part included, whose `id()` is not in
    `docs`: the one conf-name predicate `derive_conf_constants` and `derive_conf_rebinds` call
    (TOOL-dDeclaredLoop-87 S1, TOOL-dDeclaredLoop-89 S1)."""
    import ast
    return any(isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs
               and any(c in n.value for c in (".memory-tree.conf", ".unattended.conf")) for n in ast.walk(node))


# The parts of a definition Python evaluates in module scope when the definition runs, each a dotted
# attribute path keyed by the `ast` class name, the only parts of a definition `derive_conf_rebinds`'s
# module-level walk reads (TOOL-dDeclaredLoop-91 S2): a position added later is one entry here.
_MODULE_SCOPE_PARTS = {
    "FunctionDef": ("decorator_list", "args.defaults", "args.kw_defaults"),
    "AsyncFunctionDef": ("decorator_list", "args.defaults", "args.kw_defaults"),
    "Lambda": ("args.defaults", "args.kw_defaults"),
    "ClassDef": ("decorator_list", "bases", "keywords"),
}


def derive_conf_rebinds(tree, docs):
    """The module names a parsed `loop_lib.py` binds outside an assignment's own value, from two passes
    (TOOL-dDeclaredLoop-89 S1, TOOL-dDeclaredLoop-91 S1, S2). Global loaders: each `def`, `async def` or
    `class` at any depth whose subtree holds a conf name outside the docstring ids `docs` answers every
    name a `global` statement in that subtree declares and a `Name` in a store context there binds, so a
    `global` in a class body is read. Module-level targets: each walrus, `for`, `async for`, `with` or
    `async with` reached from the module body answers every `Name` in its target where its source holds
    a conf name: the walrus's value, the loop's iterable, the same `with` item's context expression. The
    walk never enters the body of a `def`, a `class` or a `lambda`; of each it reads only the parts
    `_MODULE_SCOPE_PARTS` names, the ones Python evaluates in module scope, and again inside them: a
    decorator, a default argument, a keyword-only one included, a class base and a class keyword. Each
    test is `check_conf_name`.

    The global-loader rule over-matches on the fail-closed side: a function or a class whose subtree
    holds a conf name anywhere, nested functions included, answers every global it rebinds, whichever
    function the constant belongs to.

    NOT SEEN, each binding a module name of `loop_lib.py` outside both passes (TOOL-dDeclaredLoop-89 S5):
    an import, whose name would have to be followed to its source (TOOL-dDeclaredLoop-87 F2); an
    `except ... as` name, unbound when its handler ends; a `match` capture pattern, of which no kit module
    holds a module-level instance; a `def` or `class` name, read through a call as a `reader call`; a name
    bound through `globals()` or `setattr`, which no parse can see; a `type` statement, which binds a
    type alias whose value is evaluated lazily and never a path (TOOL-dDeclaredLoop-91 S5)."""
    import ast
    names = set()
    for f in ast.walk(tree):
        if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and check_conf_name(f, docs):
            sub = list(ast.walk(f))
            declared = {g for n in sub if isinstance(n, ast.Global) for g in n.names}
            names |= declared & {n.id for n in sub if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}
    todo = list(tree.body)
    while todo:
        n = todo.pop()
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Lambda)):
            for part in _MODULE_SCOPE_PARTS.get(type(n).__name__, ()):
                got = n
                for attr in part.split("."):
                    got = getattr(got, attr)
                todo.extend(p for p in got if p is not None)
            continue
        if isinstance(n, ast.NamedExpr) and check_conf_name(n.value, docs):
            names.add(n.target.id)
        elif isinstance(n, (ast.For, ast.AsyncFor)) and check_conf_name(n.iter, docs):
            names.update(t.id for t in ast.walk(n.target) if isinstance(t, ast.Name))
        elif isinstance(n, (ast.With, ast.AsyncWith)):
            for item in n.items:
                if item.optional_vars is not None and check_conf_name(item.context_expr, docs):
                    names.update(t.id for t in ast.walk(item.optional_vars) if isinstance(t, ast.Name))
        todo.extend(ast.iter_child_nodes(n))
    return names


# Every `tree_lib` name this module reads on what `load_tree_lib` answers, tested there in this order
# (TOOL-dDeclaredLoop-90 S4): a name read on the loaded module joins this tuple, never a check of its own.
TREE_LIB_SYMBOLS = ("derive_docstring_ids", "derive_constant_charges")


def load_tree_lib():
    """The memory-tree kit's `tree_lib`, found through `read_memory_tree` and imported inside the call,
    never at this module's import: the one route by which this module reaches it, which
    `derive_conf_reads` and `derive_conf_constants` call. One LoopError naming the loaded file, every
    name of `TREE_LIB_SYMBOLS` the module lacks, in tuple order joined by `, `, and
    `govkit update --kits memory-tree` (TOOL-dDeclaredLoop-86 S21, TOOL-dDeclaredLoop-89 S6,
    TOOL-dDeclaredLoop-90 S4, TOOL-dDeclaredLoop-94 S21), so a memory-tree kit older than the charge
    walk refuses by name, never by an AttributeError; LoopError naming the same command where
    `read_memory_tree` cannot locate the kit, keeping its message and the places it looked, or where
    the import raises any other exception, naming its class (TOOL-dDeclaredLoop-88 S33,
    TOOL-dDeclaredLoop-94 S21)."""
    try:
        read_memory_tree("tree_lib.py")
        import tree_lib
    except LookupError as e:
        raise LoopError("memory-tree kit", "%s — govkit update --kits memory-tree" % e) from None
    except Exception as e:   # noqa: BLE001  a damaged tree_lib.py raises anything at import; named, never a traceback
        raise LoopError("memory-tree kit", "%s: %s — govkit update --kits memory-tree" % (
            type(e).__name__, e)) from None
    missing = [name for name in TREE_LIB_SYMBOLS if not hasattr(tree_lib, name)]
    if missing:
        raise LoopError(pathlib.Path(tree_lib.__file__).as_posix(),
                        "has no %s — govkit update --kits memory-tree" % ", ".join(missing))
    return tree_lib


def derive_conf_constants(loop_lib_path):
    """The module-level names the file at `loop_lib_path` binds, the class and never a list of shapes:
    the rule-2, module-qualified slice of the memory-tree kit's one charge walk, `derive_constant_charges`,
    its needle `check_conf_name` over a str constant's value (TOOL-dDeclaredLoop-88 S13), the whole of
    charge rule 2's predicate (TOOL-dDeclaredLoop-90 S1). That is every `Name` in the targets, a tuple or
    subscript target's included, of an `Assign`, an `AnnAssign`, one with no value included, or an
    `AugAssign` that no function and no class encloses, every module-level compound statement descended,
    one nested in a module-level `if`, `try`, `with`, `for` or `while` body included, where a str
    constant containing `.memory-tree.conf` or `.unattended.conf`, an f-string's literal part included,
    sits anywhere under that statement: in a target, in the annotation or in the value. The value's
    shape is never tested, so a join of any operands and any call are inside the class; a value that
    only names another binding is not (TOOL-dDeclaredLoop-87 S1). NOT SEEN: a conf name composed at
    run time from pieces, such as `".unattended" + ".conf"`, holds no single constant naming a conf and
    is outside the class, as the memory-tree kit's `scan_glob_readers`, the walk's other reader, records
    for a pathspec composed from pieces (TOOL-dDeclaredLoop-90 S20). It also answers the names
    `derive_conf_rebinds` answers over the same parse, a global loader's and a module-level walrus, `for`
    or `with` target's, the docstring ids from `load_tree_lib` (TOOL-dDeclaredLoop-89 S2). Read by
    `ast.parse`, never an import. LoopError naming the path where the file is missing or does not parse,
    raised before any `tree_lib` load (TOOL-dDeclaredLoop-86 S13), and `load_tree_lib`'s refusal."""
    import ast
    path = pathlib.Path(loop_lib_path)
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), str(path))
    except (OSError, UnicodeDecodeError, SyntaxError, ValueError) as e:
        raise LoopError(path.as_posix(), "cannot be read as the conf constants' module: %s" % e) from None
    tl, stem = load_tree_lib(), path.stem
    names = {owner[len(stem) + 1:] for owner, rule in tl.derive_constant_charges(
        tree, stem, lambda s: check_conf_name(ast.Constant(s))) if rule == 2 and "." not in owner[len(stem) + 1:]}
    return names | derive_conf_rebinds(tree, tl.derive_docstring_ids(tree))


# Every callee `derive_conf_reads` answers as a `reader call` (TOOL-dDeclaredLoop-97 S1): a conf
# reader the rule must answer joins this tuple, never a literal of its own.
CONF_READERS = ("read_design_conf", "read_driver_conf", "parse_conf")


def derive_conf_reads(path):
    """`[(line, kind)]` sorted by line, one per conf read in the module at `path`, graded on its syntax
    tree: kind `reader call` for a call whose callee is a member of `CONF_READERS`, read when the call
    runs (TOOL-dDeclaredLoop-97 S2), an attribute by its name and a name by the last segment of what
    `derive_import_aliases` binds it to; kind `conf name` for a string constant holding
    `.memory-tree.conf` or `.unattended.conf` anywhere, an f-string's literal part included, that is
    not a docstring `derive_docstring_ids` answers (TOOL-dDeclaredLoop-82 S8, S10); kind
    `conf constant` for a name or attribute reaching a name `derive_conf_constants` answers over the
    `loop_lib.py` beside `path`, through `import loop_lib` or `from loop_lib import`, aliased or not,
    a `from loop_lib import *` binding every such name (TOOL-dDeclaredLoop-82 S1, TOOL-dDeclaredLoop-86
    S13, S15). A comment is not in the tree. Every node a definition of `derive_fixture_boundary`
    encloses, its decorators and signature included, is passed over (TOOL-dDeclaredLoop-80).
    SyntaxError where the module does not parse (TOOL-dDeclaredLoop-76); LoopError where that
    `loop_lib.py` is missing or does not parse, or where the memory-tree kit's `tree_lib`, which
    `load_tree_lib` loads inside the call and never at this module's import, lacks a name of
    `TREE_LIB_SYMBOLS` (TOOL-dDeclaredLoop-86 S21, TOOL-dDeclaredLoop-89 S6, TOOL-dDeclaredLoop-90 S4),
    cannot be located or does not import (TOOL-dDeclaredLoop-88 S33)."""
    import ast
    path = pathlib.Path(path)
    confs = (".memory-tree.conf", ".unattended.conf")
    tree = ast.parse(path.read_text(encoding="utf-8"), str(path))
    docs = load_tree_lib().derive_docstring_ids(tree)
    bounded = {id(n) for f in derive_fixture_boundary(tree) for n in ast.walk(f)}
    aliases = derive_import_aliases(tree)
    consts = derive_conf_constants(path.parent / "loop_lib.py")
    if any(isinstance(n, ast.ImportFrom) and not n.level and n.module == "loop_lib"
           and any(a.name == "*" for a in n.names) for n in ast.walk(tree)):
        for name in consts:
            aliases.setdefault(name, "loop_lib." + name)
    hits = []
    for node in ast.walk(tree):
        if id(node) in bounded:
            continue
        if isinstance(node, ast.Call):
            callee = node.func
            name = (aliases.get(callee.id, callee.id).rsplit(".", 1)[-1] if isinstance(callee, ast.Name)
                    else getattr(callee, "attr", None))
            if name in CONF_READERS:
                hits.append((node.lineno, "reader call"))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str) \
                and any(c in node.value for c in confs) and id(node) not in docs:
            hits.append((node.lineno, "conf name"))
        elif (isinstance(node, ast.Name) and aliases.get(node.id, "").startswith("loop_lib.")
              and aliases[node.id][len("loop_lib."):] in consts) or (
                isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name)
                and aliases.get(node.value.id) == "loop_lib" and node.attr in consts):
            hits.append((node.lineno, "conf constant"))
    return sorted(hits)


# The functions of this module that open a conf and answer a resolved root, never a conf's values: the
# sanctioned route the no-own-conf-read rule never grades, declared beside `CONF_READERS` for the
# `conf-readers-declared` plant (TOOL-dDeclaredLoop-99 S2).
CONF_ROUTES = ("resolve_memory_root_source",)


def derive_conf_openers(loop_lib_path):
    """The sorted names of the module-level `def` and `async def` nodes of the file at `loop_lib_path`,
    outside `derive_fixture_boundary`, whose own body, a nested `def`, `async def` or `class` excluded,
    both builds a conf path and opens content (TOOL-dDeclaredLoop-99 S1, TOOL-dDeclaredLoop-117 S1). A
    conf path is an expression `check_conf_name` answers, a name or attribute naming a member of
    `derive_conf_constants`' answer, or a name the function's own body binds to a conf path: the `Name`
    target of an `Assign`, an `AnnAssign` with a value or a walrus whose value is a conf path, read to a
    fixpoint so a re-bound name carries. It builds one where a conf path is an operand of `/`, a
    positional or keyword argument of a `join`, `Path`, `PurePath`, `open` or `parse_conf` call, or the
    receiver of an `open`, `read_bytes` or `read_text` attribute call; an open is a call of
    `parse_conf`, `open`, `read_bytes` or `read_text`, or of an attribute of the name `subprocess`. A
    callee is a name by its id and an attribute by its attr. Read by `ast.parse`, never an import;
    `derive_conf_constants`' refusals are this one's. NOT SEEN: a path built in one function and opened
    in another; a conf name composed at run time; `subprocess` reached under another name; and a path
    carried through an attribute, a subscript, a container, or a conf-path name wrapped in a call that
    is none of `join`, `Path`, `PurePath`, `open` and `parse_conf`, such as `open(str(p))`."""
    import ast
    consts = derive_conf_constants(loop_lib_path)
    path = pathlib.Path(loop_lib_path)
    tree = ast.parse(path.read_text(encoding="utf-8"), str(path))
    bounded = {id(f) for f in derive_fixture_boundary(tree)}
    found = []
    for f in tree.body:
        if not isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)) or id(f) in bounded:
            continue
        body, todo = [], list(f.body)
        while todo:
            n = todo.pop()
            if not isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                body.append(n)
                todo.extend(ast.iter_child_nodes(n))
        calls = [(c, c.func.id if isinstance(c.func, ast.Name) else getattr(c.func, "attr", None))
                 for c in body if isinstance(c, ast.Call)]
        local = set()
        conf = lambda o: check_conf_name(o) or (isinstance(o, ast.Name) and (o.id in consts or o.id in local)) \
            or (isinstance(o, ast.Attribute) and o.attr in consts)   # noqa: E731
        binds = [(t.id, n.value) for n in body if isinstance(n, ast.Assign) for t in n.targets
                 if isinstance(t, ast.Name)] + [(n.target.id, n.value) for n in body
                                                if isinstance(n, (ast.AnnAssign, ast.NamedExpr))
                                                and n.value is not None and isinstance(n.target, ast.Name)]
        grown = True
        while grown:
            grown = {name for name, value in binds if name not in local and conf(value)}
            local |= grown
        operands = [o for n in body if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Div)
                    for o in (n.left, n.right)] + [
            a for c, callee in calls if callee in ("join", "Path", "PurePath", "open", "parse_conf")
            for a in (*c.args, *(k.value for k in c.keywords))] + [
            c.func.value for c, callee in calls
            if isinstance(c.func, ast.Attribute) and callee in ("open", "read_bytes", "read_text")]
        builds = any(conf(o) for o in operands)
        opens = any(callee in ("parse_conf", "open", "read_bytes", "read_text") or (
            isinstance(c.func, ast.Attribute) and isinstance(c.func.value, ast.Name)
            and c.func.value.id == "subprocess") for c, callee in calls)
        if builds and opens:
            found.append(f.name)
    return sorted(found)


def read_actor_rows(kit_dir):
    """The actor-witness list's lines in `kit_dir`, blank lines dropped; LoopError where it does not read."""
    path = pathlib.Path(kit_dir) / ACTOR_LIST
    try:
        return [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    except (OSError, UnicodeDecodeError) as e:
        raise LoopError(path.as_posix(), "cannot be read: %s" % e)


def check_site_witnesses(kit_dir, site, entries, root="."):
    """`(lines, refusals)` of the declaration site `site`'s `entries`, each `<item>` or `<item>:<word>`:
    a line per entry whose word resolves through `[[witness-alias]]`; a refusal per entry with no word,
    a word no alias row holds, or an actor word with no `<site> <item>` list row, and per list row of
    `site` whose item is no actor entry. The list is the one in `kit_dir`, read without a base.
    `DOD_EXTRA` is the adopter's own: no list row is read for it, and an actor entry there is admitted,
    its line ending `· adopter-declared, not on the shipped list`. An actor word with no list row is
    reported, not refused, where `floor.no-actor-witness` reads `off` at `root`'s landed revision
    (TOOL-dDeclaredLoop-2 S14), read only when such an entry is met."""
    data, where = read_definition(kit_dir)
    check_witness_classes(data, where)
    refused, aliases = data["witnesses"]["refused"], data.get("witness-alias", [])
    words = " or ".join(":" + r["word"] for r in aliases)
    own = site == "DOD_EXTRA"
    listed = {}
    for line in [] if own else read_actor_rows(kit_dir):
        fields = line.split("\t")
        if len(fields) == 3 and fields[0] == site:
            listed[fields[1]] = fields[2]
    lines, refusals, actors, floor_off = [], [], set(), None
    for entry in entries:
        item, _sep, word = entry.partition(":")
        if not word:
            refusals.append("%s %s declares no witness class; append %s" % (site, entry, words))
            continue
        cls = resolve_alias(aliases, word)
        if cls is None:
            refusals.append("%s %s: %r is no witness word; the words are %s" % (site, entry, word, words))
            continue
        line = "loop: site %s · %s · %s · %s" % (site, item, word, cls)
        if cls in refused and own:
            line += " · adopter-declared, not on the shipped list"
        elif cls in refused:
            actors.add(item)
            if item in listed:
                line += " · until %s" % listed[item]
            else:
                why = ("%s %s is an actor witness and the list holds no row %s %s naming the build that computes "
                       "it" % (site, entry, site, item))
                floor_off = check_floor_off("no-actor-witness", root) if floor_off is None else floor_off
                if floor_off:
                    line += " · floor: no-actor-witness off · reported · %s" % why
                else:
                    refusals.append(why)
        lines.append(line)
    for item in listed:
        if item not in actors:
            refusals.append("the list row %s %s names no actor entry of %s" % (site, item, site))
    return lines, refusals


def check_floor_off(member, root):
    """Whether the floor member `member` reads `off` at `root`'s landed revision (TOOL-dDeclaredLoop-2 S14),
    through floor.py beside this file, imported here since it imports this module; LoopError where the
    floor does not hold."""
    from floor import read_floor
    return read_floor(root)[member] == "off"


def read_definition(kit_dir):
    """`(parsed TOML, the file's path as printed)` of the definition in `kit_dir`, unchecked; LoopError
    when the file does not read or is no TOML."""
    path = pathlib.Path(kit_dir) / DEFINITION
    try:
        with open(path, "rb") as fh:
            return tomllib.load(fh), path.as_posix()
    except OSError as e:
        raise LoopError(path.as_posix(), "cannot be read: %s" % e.strerror)
    except (tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
        raise LoopError(path.as_posix(), "not valid TOML: %s" % e)


def load_loop(kit_dir):
    """The definition in `kit_dir`, checked: `{"step": [rows], "workflow": [rows], "dispositions":
    [members]}`, each in file order."""
    return check_loop(*read_definition(kit_dir))


def read_steps(kit_dir):
    """The gov steps' rows, in the loop's order."""
    return load_loop(kit_dir)["step"]


def read_workflow_order(kit_dir):
    """`{workflow name: order}`, in file order: the build order, 0 for an any-time workflow."""
    return {w["name"]: w["order"] for w in load_loop(kit_dir)["workflow"]}


def derive_reach(row):
    """A checked workflow row's reach word: its `reach`, else its step's last segment, else `none`."""
    return row.get("reach") or row["step"].rsplit(".", 1)[-1]


def read_workflow_reach(kit_dir):
    """`{workflow name: reach word}`: the row's `reach` where it carries one, else the last segment of
    its `step` tag, else `none`."""
    return {w["name"]: derive_reach(w) for w in load_loop(kit_dir)["workflow"]}


def read_dispositions(kit_dir):
    """The members of the one closed disposition set, in file order; LoopError for a definition that
    declares none."""
    data, where = read_definition(kit_dir)
    members = check_loop(data, where)["dispositions"]
    if not members:
        raise LoopError(where, "declares no disposition set, a [dispositions] table with its set")
    return members


def resolve_disposition(kit_dir, word):
    """The member `word` is or, through a `[[disposition-alias]]` row, means; LoopError for any other word."""
    data, where = read_definition(kit_dir)
    members = read_dispositions(kit_dir)
    if word in members:
        return word
    means = resolve_alias(data.get("disposition-alias", []), word)
    if means is not None:
        return means
    raise LoopError(where, "%r is no disposition and no alias of one; the set is %s" % (word, " ".join(members)))


def derive_outcome_set(row, members, where):
    """The closed outcome set of one `[[item]]` row: `members`, the disposition set, for a row declaring
    `outcomes = "dispositions"`, the row's own list otherwise. LoopError naming `where` and the item for
    a row whose `outcomes` is neither, is empty or gives a word twice, or that names the disposition set
    where the definition declares none."""
    item, outcomes = row.get("tag"), row.get("outcomes")
    if outcomes == OUTCOMES_REF:
        if not members:
            raise LoopError(where, "declares no disposition set, a [dispositions] table with its set")
        return list(members)
    if not isinstance(outcomes, list) or not outcomes or not all(isinstance(w, str) for w in outcomes):
        raise LoopError(where, "the item %s carries no outcomes, a list of words or %r" % (item, OUTCOMES_REF))
    for word in outcomes:
        if outcomes.count(word) > 1:
            raise LoopError(where, "the item %s gives the outcome %s twice" % (item, word))
    return list(outcomes)


def read_item_rows(data, where):
    """`data`'s `[[item]]` rows; LoopError for an `item` table that is no array of tables."""
    rows = data.get("item", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise LoopError(where, "'item' is not an array of tables")
    return rows


def read_outcome_set(kit_dir, item):
    """The closed outcome set of the `[[item]]` row whose `tag` is `item`, by `derive_outcome_set`'s
    rule; None for an item the definition does not declare. LoopError for an `item` table that is no
    array of tables, or a row found whose outcomes do not hold."""
    data, where = read_definition(kit_dir)
    members = check_loop(data, where)["dispositions"]
    for row in read_item_rows(data, where):
        if row.get("tag") == item:
            return derive_outcome_set(row, members, where)
    return None


def check_program(data, where, layers, stages=()):
    """`data`'s `[[item]]` rows graded as each gov step's program, returned as `{step tag: [item tags in
    needs order]}`. `layers` is the set of layer tags an input may name, or None where none resolved,
    which leaves the inputs unchecked. `stages` are the composed repository stage tags,
    `step.adopter.<name>` (TOOL-dDeclaredLoop-25): an item tagged `item.adopter.<name>.<item>` whose
    `step.adopter.<name>` is one of them is that stage's, and the stage's program is returned beside the
    five. An item tagged `item.review.<name>` is the breakpoint program's, its `step` `none`, and that
    program is returned under the key `review` (TOOL-dDeclaredLoop-50). LoopError naming `where`, the item
    and the field that does not hold: a tag opening no `item.<step>.` of a gov step, no
    `item.adopter.<stage>.` of a composed stage and no `item.review.`, a `step` other than that one, or a
    tag given
    twice; a need naming no declared item, or a needs cycle, each cycle named once; an outcome set that
    does not hold; routes that are not exactly the outcomes, or a target that is no declared item,
    `transition` or `stand-in:{prefix}/<home>/<file>`; an input naming no layer tag; and a step whose
    `exit` is no declared item of that step."""
    members = check_loop(data, where)["dispositions"]
    rows, steps = read_item_rows(data, where), {t.split(".", 1)[1]: t for t in STEP_TAGS}
    declared = {}
    for n, row in enumerate(rows, 1):
        tag = row.get("tag")
        parts = tag.split(".", 2) if isinstance(tag, str) else []
        if len(parts) == 3 and parts[:2] == ["item", "adopter"]:
            name, _dot, rest = parts[2].partition(".")
            stage = "step.adopter.%s" % name
            if stage not in stages or not rest:
                raise LoopError(where, "item row %d tag %r opens no item.adopter.<stage>.<name> of a composed "
                                       "stage: %s" % (n, tag, " ".join(stages) or "none composed"))
            if row.get("step") != stage:
                raise LoopError(where, "the item %s step %r is not %s, the stage its tag opens" % (
                    tag, row.get("step"), stage))
        elif len(parts) == 3 and parts[:2] == ["item", REVIEW_PROGRAM] and parts[2]:
            if row.get("step") != NO_STEP:
                raise LoopError(where, "the item %s step %r is not %s, the breakpoint program's step" % (
                    tag, row.get("step"), NO_STEP))
        elif len(parts) != 3 or parts[0] != "item" or parts[1] not in steps or not parts[2]:
            raise LoopError(where, "item row %d tag %r opens no item.<step>. of a gov step: %s" % (
                n, tag, " ".join(steps)))
        elif row.get("step") != steps[parts[1]]:
            raise LoopError(where, "the item %s step %r is not %s, the step its tag opens" % (
                tag, row.get("step"), steps[parts[1]]))
        if tag in declared:
            raise LoopError(where, "the item %s is declared twice" % tag)
        declared[tag] = row
    needs = {}
    for tag, row in declared.items():
        entries = row.get("needs")
        if not isinstance(entries, list):
            raise LoopError(where, "the item %s carries no needs, a list of tags and any-of lists, [] for none" % tag)
        needs[tag] = []
        for entry in entries:
            group = entry if isinstance(entry, list) else [entry]
            if not group or not all(isinstance(t, str) for t in group):
                raise LoopError(where, "the item %s needs %r, which is neither a tag nor a list of tags" % (tag, entry))
            for t in group:
                if t not in declared:
                    raise LoopError(where, "the item %s needs %s, which no [[item]] row declares" % (tag, t))
                needs[tag].append(t)
    try:
        order = derive_needs_order(list(declared), needs)
    except NeedsCycle:
        cycles = scan_cycles({t: set(n) for t, n in needs.items()})
        raise LoopError(where, "the item needs form a cycle: %s" % "; ".join(
            " -> ".join(c + (c[0],)) for c in cycles)) from None
    for tag, row in declared.items():
        outcomes = derive_outcome_set(row, members, where)
        routes = row.get("routes")
        if not isinstance(routes, dict):
            raise LoopError(where, "the item %s carries no routes, an inline table of outcome = target" % tag)
        for word in outcomes:
            if word not in routes:
                raise LoopError(where, "the item %s outcome %s has no route" % (tag, word))
        for word, target in routes.items():
            if word not in outcomes:
                raise LoopError(where, "the item %s routes %s, which is no outcome of its set: %s" % (
                    tag, word, " ".join(outcomes)))
            if target not in declared and target != ROUTE_TRANSITION and not (
                    isinstance(target, str) and ROUTE_STAND_IN.fullmatch(target)):
                raise LoopError(where, "the item %s routes %s to %r, which is no declared item, %s or "
                                       "stand-in:{prefix}/<home>/<file>" % (tag, word, target, ROUTE_TRANSITION))
        inputs = row.get("inputs", [])
        if not isinstance(inputs, list) or not all(isinstance(i, str) for i in inputs):
            raise LoopError(where, "the item %s inputs are not a list of <layer tag>:<what it reads>" % tag)
        for text in inputs if layers is not None else ():
            if text.split(":", 1)[0] not in layers:
                raise LoopError(where, "the item %s input %r names no layer tag of the playbook kit's layers.toml" % (
                    tag, text))
    for row in data.get("step", []):
        exit_tag = row.get("exit")
        if exit_tag not in declared or declared[exit_tag]["step"] != row.get("tag"):
            raise LoopError(where, "the step %s exit %r is no declared item of that step" % (row.get("tag"), exit_tag))
    program = {s: [t for t in order if declared[t]["step"] == s] for s in (*STEP_TAGS, *stages)}
    program[REVIEW_PROGRAM] = [t for t in order if declared[t]["step"] == NO_STEP]
    return program


def read_role_defaults(kit_dir):
    """`(roles, "")`, the roles kit's catalogue as its `roles_lib.load_roles` reads it, the kit found
    from `kit_dir` through `resolve_kit_dir` and its library imported inside the function, as
    `read_builds_dir` reaches the memory-tree kit; or `(None, why)` where the kit does not resolve, its
    library does not import or its catalogue does not read."""
    try:
        roles_dir = resolve_kit_dir("roles", "roles_lib.py", kit_dir)
        if str(roles_dir) not in sys.path:
            sys.path.insert(0, str(roles_dir))
        import roles_lib  # the roles kit's reader, found above
    except (LookupError, ImportError) as e:
        return None, str(e)
    try:
        return roles_lib.load_roles(roles_dir), ""
    except roles_lib.RolesError as e:
        return None, str(e)


def resolve_item_declaration(item, roles):
    """`{"inputs", "allowance", "returns", "source"}` of one `[[item]]` row, `source` naming each
    field's: `item` where the row declares it, which a non-role item always does; for a `role:<slot>`
    item's absent field, its role's `reads` split on commas, `writes` or `returns`, sourced
    `role:<slot>`, or None sourced `pending` where `roles` holds no such slot and `unarmed` where
    `roles` is None."""
    actor = item.get("actor")
    slot = actor[len("role:"):] if isinstance(actor, str) and actor.startswith("role:") else None
    out, source = {}, {}
    for field, key in (("inputs", "reads"), ("allowance", "writes"), ("returns", "returns")):
        if field in item or slot is None:
            out[field], source[field] = item.get(field), "item"
        elif roles is None or slot not in roles:
            out[field], source[field] = None, "unarmed" if roles is None else "pending"
        else:
            value = roles[slot]["keys"].get(key)
            if field == "inputs" and isinstance(value, str):
                value = [v.strip() for v in value.split(",") if v.strip()]
            out[field], source[field] = value, actor
    out["source"] = source
    return out


def check_item_declarations(items, roles, why):
    """`(lines, refusals)` of the `[[item]]` rows `items`: one `loop: item` line per item in file order
    and the count line, and one refusal per field that does not hold. The actor is one string,
    `ACTOR_FORM` with its kind in `ACTOR_KINDS`, or the bare `executor` or `owner`. A non-role item
    carries a non-empty `inputs` list, `allowance` and `returns`; a role item's absent ones are its
    role's through `resolve_item_declaration`, an explicit one equal to its role's is refused as a copy,
    and its explicit `allowance` may only be `none`. A role the catalogue `roles` lacks prints `pending`,
    and every role item `unarmed` with `why` where `roles` is None; neither is a refusal."""
    lines, refusals, pending, unarmed = [], [], 0, 0
    for row in items:
        tag, actor = row.get("tag"), row.get("actor")
        form = ACTOR_FORM.fullmatch(actor) if isinstance(actor, str) else None
        kind = actor if actor in ("executor", "owner") else form.group(1) if form else None
        if kind is None:
            refusals.append("the item %s actor %r is not one string <kind>:<name>, executor or owner: one "
                            "actor per item" % (tag, actor))
        elif kind not in ACTOR_KINDS:
            refusals.append("the item %s actor kind %s is not one of %s" % (tag, kind, " ".join(ACTOR_KINDS)))
            kind = None
        got = resolve_item_declaration(row, roles)
        if kind is not None and kind != "role":
            for field in ("inputs", "allowance", "returns"):
                value = got[field]
                if field == "inputs":
                    ok = isinstance(value, list) and value and all(isinstance(v, str) and v.strip() for v in value)
                else:
                    ok = isinstance(value, str) and value.strip()
                if not ok:
                    refusals.append("the item %s carries no %s, which a %s actor declares" % (tag, field, kind))
        elif kind == "role":
            slot = form.group(2)
            role = roles.get(slot) if roles is not None else None
            for field, key in (("inputs", "reads"), ("allowance", "writes"), ("returns", "returns")):
                if field not in row or role is None:
                    continue
                theirs = role["keys"].get(key)
                if field == "inputs" and isinstance(theirs, str):
                    theirs = [v.strip() for v in theirs.split(",") if v.strip()]
                if row[field] == theirs:
                    refusals.append("the item %s %s copies its role %s's %s; leave it out and the role's "
                                    "applies" % (tag, field, slot, key))
            allowance = row.get("allowance", "none")
            if allowance != "none" and (role is None or allowance != role["keys"].get("writes")):
                refusals.append("the item %s allowance %r widens its role %s: a role item's allowance may only "
                                "be none" % (tag, allowance, slot))
            if roles is None:
                unarmed += 1
                lines.append("loop: item %s · %s · unarmed · %s" % (tag, actor, why))
                continue
            if role is None:
                pending += 1
                lines.append("loop: item %s · %s · pending · the roles kit holds no %s role" % (tag, actor, slot))
                continue
        src = got["source"]
        lines.append("loop: item %s · %s · inputs from %s · allowance %s from %s · returns from %s" % (
            tag, actor, src["inputs"], got["allowance"], src["allowance"], src["returns"]))
    lines.append("loop: items · %d read · %d pending · %d unarmed" % (len(items), pending, unarmed))
    return lines, refusals


def read_seed_values(kit_dir):
    """The value set of an item's `seed`, narrowest first: the `widens` order of the `seed` `[[field]]` row
    of the item kind's schema in `kit_dir` (TOOL-dPlacedRequest-8 S1). LoopError naming the schema where it
    does not read, is no TOML, or holds no `seed` row whose `widens` is an order of words."""
    path = pathlib.Path(kit_dir) / ITEM_SCHEMA
    try:
        with open(path, "rb") as fh:
            data = tomllib.load(fh)
    except OSError as e:
        raise LoopError(path.as_posix(), "cannot be read: %s" % e.strerror)
    except (tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
        raise LoopError(path.as_posix(), "not valid TOML: %s" % e)
    row = next((f for f in data.get("field", []) if isinstance(f, dict) and f.get("name") == "seed"), {})
    widens = row.get("widens")
    if not isinstance(widens, list) or not widens or not all(isinstance(v, str) and SEG.fullmatch(v) for v in widens):
        raise LoopError(path.as_posix(), "holds no [[field]] row seed whose widens is an order of words")
    return list(widens)


def check_item_seeds(items):
    """`(lines, refusals)` of the `[[item]]` rows `items` (TOOL-dPlacedRequest-8 S3): one `loop: seed <tag>
    · <value>` line per item in file order, an absent `seed` read `none`, then `loop: seeds · <n> declared
    · <m> none`. A value outside `read_seed_values` over the schema beside this file is refused naming the
    item and the value, and so is a value other than `none` on an item whose actor is no `role:`, since
    only a role's work order carries a `code` slot. LoopError where the schema does not read."""
    values = read_seed_values(pathlib.Path(__file__).absolute().parent)
    lines, refusals, declared, none = [], [], 0, 0
    for row in items:
        tag, actor, seed = row.get("tag"), row.get("actor"), row.get("seed", SEED_NONE)
        lines.append("loop: seed %s · %s" % (tag, seed))
        if seed not in values:
            refusals.append("the item %s seed %r is not one of %s" % (tag, seed, " ".join(values)))
        elif seed == SEED_NONE:
            none += 1
        elif not (isinstance(actor, str) and actor.startswith("role:")):
            refusals.append("the item %s seed %r sits on the actor %r, which is no role: only a role's work order "
                            "carries a code slot" % (tag, seed, actor))
        else:
            declared += 1
    lines.append("loop: seeds · %d declared · %d none" % (declared, none))
    return lines, refusals


def resolve_seed_path(value):
    """One seed path in the form the asks join compares paths in, the memory-tree kit's `resolve_ask_path`
    restated so this kit imports no sibling for it: a backslash folded to a slash, a trailing `:<line>`, a
    leading `./` and a trailing `/` dropped."""
    out = re.sub(r":\d+$", "", value.strip().replace("\\", "/"))
    while out.startswith("./"):
        out = out[2:]
    return out.rstrip("/")


def resolve_item_seed(item, *, build=None, unit=None, question=None):
    """The paths an `[[item]]` row's declared `seed` hands its `code` slot (TOOL-dPlacedRequest-8 S4), in the
    repository the working directory sits in: a list of repository-relative paths, deduplicated in
    first-seen order after `resolve_seed_path`, or one str, the line `unarmed — <source>: <why>`.

    `none`, or no `seed`, is the empty list. `scope-paths` is `SEED_SCOPE_UNARMED` until a plan record
    carries a scope. `write-set` finds the unit's spec as the file under `<records root>/builds/<build>/spec/`
    whose H1's first token is `unit`, the memory-tree kit's `parse_spec_h1` deciding, and hands its path to
    the unattended driver's `--path-tokens --files-touched HEAD <spec>`; `question-paths` hands `question`
    to that verb's stdin form. The driver is an optional sibling found by `resolve_kit_dir` and run by the
    bash `loop_witness.py`'s `resolve_bash` finds, both imported inside the function: where neither
    resolves, the source is `unarmed`. ValueError naming why on a missing `unit` or `build` for `write-set`,
    a `build` that is no one path segment, a missing or empty `question` for `question-paths`, an unknown
    value, a working directory in no git work tree, no spec or two specs defining `unit`, and a driver
    call that exits non-zero or does not answer within `SEED_DRIVER_BOUND` seconds."""
    import subprocess
    tag, seed = item.get("tag"), item.get("seed", SEED_NONE)
    if seed == SEED_NONE:
        return []
    if seed == "scope-paths":
        return SEED_SCOPE_UNARMED
    if seed == "write-set":
        if not unit:
            raise ValueError("the item %s seeds write-set, which takes --unit <id>" % tag)
        if not build:
            raise ValueError("the item %s seeds write-set, which takes --build <slug>" % tag)
        if not SEED_BUILD.fullmatch(build):
            raise ValueError("--build %r is no build slug, one path segment of letters, digits, _ and -" % build)
    elif seed == "question-paths":
        if not question:
            raise ValueError("the item %s seeds question-paths, which takes --question <text>" % tag)
    else:
        raise ValueError("the item %s seed %r is no seed value" % (tag, seed))
    from loop_witness import read_clean_env, resolve_bash
    env = read_clean_env()
    try:
        p = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, encoding="utf-8",
                           errors="replace", env=env)
    except OSError as e:
        raise ValueError("git does not run: %s" % e) from None
    if p.returncode != 0 or not p.stdout.strip():
        raise ValueError("the working directory sits in no git work tree")
    top = pathlib.Path(p.stdout.strip())
    argv = ["--path-tokens"]
    if seed == "write-set":
        try:
            read_memory_tree("tree_lib.py")
            from tree_lib import parse_spec_h1
            memory_root = resolve_memory_root(top)
        except LookupError as e:
            raise ValueError(str(e)) from None
        folder = top / memory_root / "builds" / build / "spec"
        hits = []
        for path in sorted(folder.rglob("*.md")) if folder.is_dir() else []:
            rel = path.relative_to(top).as_posix()
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            got = parse_spec_h1(rel, text, memory_root, [unit.split("-", 1)[0]])
            if got and got[1] == unit:
                hits.append(rel)
        if len(hits) != 1:
            raise ValueError("%d spec(s) under %s/builds/%s/spec/ define %s, where one owes it%s" % (
                len(hits), memory_root, build, unit, (": " + " ".join(hits)) if hits else ""))
        argv += ["--files-touched", "HEAD", hits[0]]
    try:
        driver = resolve_kit_dir("unattended", "unattended.sh", pathlib.Path(__file__).absolute().parent)
    except LookupError:
        return "unarmed — %s: no unattended driver resolves" % seed
    driver = driver / "unattended.sh"
    bash = resolve_bash(driver)
    if bash is None:
        return "unarmed — %s: no bash that can see %s" % (seed, driver.as_posix())
    try:
        p = subprocess.run([bash, str(driver), *argv], cwd=str(top), input=question if seed == "question-paths" else "",
                           capture_output=True, text=True, encoding="utf-8", errors="replace", env=env,
                           timeout=SEED_DRIVER_BOUND)
    except subprocess.TimeoutExpired:
        raise ValueError("the unattended driver's --path-tokens did not answer within %d seconds" % (
            SEED_DRIVER_BOUND)) from None
    if p.returncode != 0:
        said = (p.stdout.strip().splitlines() or p.stderr.strip().splitlines() or ["no output"])[0]
        raise ValueError("the unattended driver's --path-tokens exited %d: %s" % (p.returncode, said))
    paths = []
    for line in p.stdout.splitlines():
        path = resolve_seed_path(line)
        if path and path not in paths:
            paths.append(path)
    return paths


def run_seed_command(kit_dir, args):
    """`seed <item tag> [--build <slug>] [--unit <id>] [--question <text>]`: the item's declared seed through
    `resolve_item_seed`, one path per line or its one `unarmed` line, exit 0. Exit 1 on a definition that
    does not hold; 2 on a usage error, an item no row declares, or the resolver's ValueError, each named."""
    opts, tag = {"--build": None, "--unit": None, "--question": None}, None
    if args and not args[0].startswith("--"):
        tag, rest = args[0], args[1:]
        while rest:
            if rest[0] not in opts or len(rest) < 2 or opts[rest[0]] is not None:
                tag = None
                break
            opts[rest[0]], rest = rest[1], rest[2:]
    if tag is None:
        print("usage: python loop_lib.py seed <item tag> [--build <slug>] [--unit <id>] [--question <text>]",
              file=sys.stderr)
        return 2
    try:
        rows = {r.get("tag"): r for r in read_items(kit_dir)}
    except LoopError as e:
        print("loop: %s" % e)
        return 1
    if tag not in rows:
        print("loop: seed · no [[item]] row declares %s" % tag)
        return 2
    try:
        got = resolve_item_seed(rows[tag], build=opts["--build"], unit=opts["--unit"], question=opts["--question"])
    except ValueError as e:
        print("loop: seed · %s" % e)
        return 2
    for line in [got] if isinstance(got, str) else got:
        print(line)
    return 0


def read_layer_tags(kit_dir):
    """The layer tags of the playbook kit's `layers.toml`, each `[[layer]]` row's `tag`, the kit found
    from `kit_dir` through `resolve_kit_dir`; LookupError where it does not resolve. LoopError where the
    file does not read or is no TOML."""
    path = resolve_kit_dir("playbook", "layers.toml", kit_dir) / "layers.toml"
    try:
        with open(path, "rb") as fh:
            data = tomllib.load(fh)
    except OSError as e:
        raise LoopError(path.as_posix(), "cannot be read: %s" % e.strerror)
    except (tomllib.TOMLDecodeError, UnicodeDecodeError) as e:
        raise LoopError(path.as_posix(), "not valid TOML: %s" % e)
    return {row.get("tag") for row in data.get("layer", []) if isinstance(row, dict)}


def read_items(kit_dir):
    """The `[[item]]` rows of the definition in `kit_dir`, in file order, once `check_loop` and
    `check_program` hold; the inputs are graded where the playbook kit's layer tags resolve."""
    data, where = read_definition(kit_dir)
    check_loop(data, where)
    try:
        layers = read_layer_tags(kit_dir)
    except LookupError:
        layers = None
    check_program(data, where, layers)
    return read_item_rows(data, where)


def derive_item_scope(kit_dir, root, tags, units=None):
    """One `loop: scope <tag> · <derive's item line> · <the tags it lists, or none>` line per item of
    `tags`: the playbook kit's `load_sets.py derive --reader reader.every --item <tag>` over the
    repository at `root`, `--units <units>` added where given, run once per item as a subprocess, so
    this module imports no sibling kit. Where that kit does not resolve from `kit_dir`, every line is
    `unarmed`, naming the LookupError. LoopError naming the item, the exit and derive's first output
    line where a derive exits non-zero."""
    import os
    import subprocess
    try:
        script = resolve_kit_dir("playbook", "load_sets.py", kit_dir) / "load_sets.py"
    except LookupError as e:
        return ["loop: scope %s · unarmed · %s" % (tag, e) for tag in tags]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    lines = []
    for tag in tags:
        argv = [sys.executable, str(script), "derive", "--reader", SCOPE_READER, "--item", tag, "--root", str(root)]
        if units is not None:
            argv += ["--units", str(units)]
        p = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
        out = p.stdout.splitlines()
        if p.returncode != 0:
            first = next(iter(out + p.stderr.splitlines()), "no output")
            raise LoopError(script.as_posix(), "derive for the item %s exited %d: %s" % (tag, p.returncode, first))
        said = next((ln for ln in out if ln.startswith("item —")), "item — no line")
        listed = [ln.strip() for ln in out if ln.startswith("  ") and ln.strip()]
        lines.append("loop: scope %s · %s · %s" % (tag, said, " ".join(listed) or "none"))
    return lines


def check_disposition_record(kit_dir, record):
    """The value join of an owner's disposition record, `record` a mapping holding `Item` and
    `Disposition`: True where the word, as written and never through an alias, is a member of the item's
    closed outcome set; LoopError naming the item and its set for any other word; None for an item the
    definition does not declare, which is `unarmed` and never green."""
    item, word = record["Item"], record["Disposition"]
    outcomes = read_outcome_set(kit_dir, item)
    if outcomes is None:
        return None
    if word not in outcomes:
        raise LoopError((pathlib.Path(kit_dir) / DEFINITION).as_posix(),
                        "the disposition %r is outside the outcome set of %s: %s" % (word, item, " ".join(outcomes)))
    return True


def write_loop_plant(data, case, rows, base_rows):
    """`data`, the actor-witness list's `rows` and its `base_rows` with the break `case` names made in
    them, in place."""
    steps, workflows = data.get("step", []), {w.get("name"): w for w in data.get("workflow", [])}
    plan = next((r for r in steps if r.get("tag") == "step.plan"), {})
    if case == "witness-no-class":
        plan.get("witness", {}).pop("class", None)
    elif case == "witness-bad-class":
        plan.get("witness", {})["class"] = "agent-said"
    elif case in ("witness-actor-unlisted", "witness-actor-listed"):
        plan.get("witness", {})["class"] = "actor"
        if case == "witness-actor-listed":
            rows.append("step.plan\tstep.plan\tdWellOiledMachine")
            base_rows.append("step.plan\tstep.plan\tdWellOiledMachine")
    elif case == "actor-list-grown":
        rows.append("DOD_CORE\treuse-probed\tdWellOiledMachine")
    elif case == "actor-list-stale":
        rows.append("step.design\tstep.design\tdWellOiledMachine")
        base_rows.append("step.design\tstep.design\tdWellOiledMachine")
    elif case == "actor-list-no-build":
        rows.append("DOD_CORE\tkeepalive-reaped\tdNoSuchBuild")
        base_rows.append("DOD_CORE\tkeepalive-reaped\tdNoSuchBuild")
    elif case == "actor-list-foreign":
        pass  # its break is the builds folder, which `main` sets after the read
    elif case == "missing-step":
        data["step"] = [r for r in steps if r.get("tag") != "step.deploy"]
    elif case == "reordered":
        data["step"] = sorted(steps, key=lambda r: {"step.test": 2.5}.get(r.get("tag"), r.get("order", 0)))
    elif case == "bad-step":
        workflows["build"]["step"] = "step.ship"
    elif case == "bad-reach":
        workflows["spec-review"]["reach"] = "revew"
    elif case == "disposition-unknown":
        data["dispositions"]["set"].append("ask")
    elif case == "disposition-alias":
        next(r for r in data["disposition-alias"] if r.get("word") == "defer")["means"] = "postpone"
    elif case in ("computed-actor", "computed-unserved"):
        row = next(r for r in data.get("computed-witness", []) if r.get("name") == "acceptance")
        if case == "computed-unserved":
            row["serves"] = "item.build.acceptanc"
        else:
            served = next(r for r in data.get("item", []) if r.get("tag") == row.get("serves"))
            served["witness"]["class"] = "actor"
    elif case in PLANTS and case not in SCOPE_PLANTS:
        items = {r.get("tag"): r for r in data.get("item", [])}
        if case == "needs-cycle":
            items["item.plan.dedupe"]["needs"].append("item.plan.triage-rule")
        elif case == "step-none-outside-review":
            items["item.plan.place"]["step"] = NO_STEP
        elif case == "review-step-named":
            items["item.review.pin"]["step"] = "step.design"
        elif case == "needs-unresolved":
            items["item.plan.record"]["needs"][0].append("item.plan.triage-oracle")
        elif case == "outcome-unrouted":
            items["item.plan.place"]["routes"].pop("unplaced")
        elif case == "route-unresolved":
            items["item.plan.place"]["routes"]["placed"] = "item.plan.leas"
        elif case == "input-no-layer":
            inputs = items["item.plan.input"]["inputs"]
            inputs[0] = "layer.memry:" + inputs[0].split(":", 1)[1]
        elif case == "actor-two":
            items["item.build.unit-pass"]["actor"] = ["role:gov-builder", "command:build.unit-pass"]
        elif case == "actor-bad-kind":
            items["item.build.unit-pass"]["actor"] = "agent:x"
        elif case == "witness-missing":
            items["item.build.unit-pass"].pop("witness")
        elif case == "allowance-missing":
            items["item.plan.place"].pop("allowance")
        elif case == "role-copy":
            items["item.build.unit-pass"]["allowance"] = "product"
        elif case == "role-widen":
            items["item.design.seams"]["allowance"] = "product"
        elif case == "role-pending":
            items["item.build.unit-pass"]["actor"] = "role:gov-no-such-role"
        elif case == "roles-no-kit":
            pass  # its break is the roles kit's directory, which `main` resolves from a scratch directory
        elif case == "seed-bad":
            items["item.build.unit-pass"]["seed"] = "diff"
            items["item.plan.place"]["seed"] = "write-set"
        else:
            plan["exit"] = "item.design.exit"


def run_selftest_cases(main, cases, label):
    """Each case `(name, argv, owed exit, opening, needle)` run through `main(argv)` in process with its
    output captured, and held when it exits as owed and prints a line opening with `opening` that holds
    `needle`. One `<label> · PASS` or `· FAIL` line per case, then the summary line; 0 when every case
    holds, else 1. The shared case loop of `loop_checklist.py` and `loop_table.py` beside this file."""
    failed = []
    for name, case_argv, owed, opening, needle in cases:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = main(case_argv)
        said = out.getvalue()
        line = next((ln for ln in said.splitlines() if ln.startswith(opening) and needle in ln), None)
        if rc == owed and line:
            print("%s · PASS %s · exit %d · %s" % (label, name, rc, line[:200]))
        else:
            failed.append(name)
            print("%s · FAIL %s · exit %d, owed %d and a line %r naming %r: %s" % (
                label, name, rc, owed, opening, needle, said[-400:]))
    print("%s · %s · %d case(s) · %d failed%s" % (
        label, "FAIL" if failed else "PASS", len(cases), len(failed), (": " + " ".join(failed)) if failed else ""))
    return 1 if failed else 0


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):   # a selftest case runs in process with its output captured
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    kit_dir = pathlib.Path(__file__).absolute().parent
    if argv == ["--selftest"]:   # TOOL-dDeclaredLoop-67 S30: every plant, each held to what PLANT_OWED says
        return run_selftest_cases(main, [(p, ["--fixture", "--plant", p], *PLANT_OWED[p]) for p in PLANTS],
                                  "loop: definition selftest")
    plant = argv[2] if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] else None
    if argv[:1] == ["--grade-site"] and len(argv) >= 2 and argv[1] in DECLARATION_SITES:
        try:
            lines, refusals = check_site_witnesses(kit_dir, argv[1], argv[2:])
        except ValueError as e:   # LoopError, the floor's copy of it included where this file runs as __main__
            print("loop: %s" % e)
            return 1
        for line in lines:
            print(line)
        for r in refusals:
            print("loop: refused · %s" % r)
        return 1 if refusals else 0
    if argv[:1] == ["seed"]:   # TOOL-dPlacedRequest-8 S4: an item's declared seed, resolved to paths
        return run_seed_command(kit_dir, argv[1:])
    if argv not in (["--check"], ["--scopes"]) and plant not in PLANTS:
        print("usage: python loop_lib.py --check | --scopes | --selftest | --fixture --plant <%s> | --grade-site <%s> "
              "<entry>... | seed <item tag> [--build <slug>] [--unit <id>] [--question <text>]" % (
            "|".join(PLANTS), "|".join(DECLARATION_SITES)), file=sys.stderr)
        return 2
    if plant in SEED_PLANTS:   # TOOL-dPlacedRequest-8 AC4 to AC6: the resolver in a scratch repository
        print("loop: fixture · plant %s · %s" % (plant, PLANTS[plant]))
        refusals = check_seed_plant(plant)
        for r in refusals:
            print("loop: refused · %s" % r)
        return 1 if refusals else 0
    if plant in CONF_PLANTS:   # TOOL-dDeclaredLoop-99 S3, TOOL-dDeclaredLoop-117 S2: conf openers, no definition read
        print("loop: fixture · plant %s · %s" % (plant, PLANTS[plant]))
        if plant == "conf-readers-declared":
            refusals = check_conf_readers_plant(pathlib.Path(__file__))
        else:   # the copy sits under the host temp directory and is removed after
            with tempfile.TemporaryDirectory() as scratch:
                refusals = check_conf_readers_plant(write_conf_plant(plant, scratch))
        for r in refusals:
            print("loop: refused · %s" % r)
        return 1 if refusals else 0
    root = next((d for d in (kit_dir, *kit_dir.parents) if (d / ".git").exists()), kit_dir)
    if argv == ["--scopes"]:
        try:
            lines = derive_item_scope(kit_dir, root, [r["tag"] for r in read_items(kit_dir)])
        except LoopError as e:
            print("loop: %s" % e)
            return 1
        for line in lines:
            print(line)
        return 0
    # A scope plant's or roles-no-kit's scratch directory sits under the host temp directory and is
    # removed after.
    scratch = tempfile.TemporaryDirectory() if plant in SCOPE_PLANTS + ("roles-no-kit",) else None
    layer_dir = scratch.name if plant == "scope-no-kit" else kit_dir
    try:
        data, where = read_definition(kit_dir)
        rows = read_actor_rows(kit_dir)
        if plant:
            base_rows, base_why = list(rows), "the shipped list as read"
            print("loop: fixture · plant %s · %s" % (plant, PLANTS[plant]))
            write_loop_plant(data, plant, rows, base_rows)
        loop = check_loop(data, where)
        if not loop["dispositions"]:
            raise LoopError(where, "declares no disposition set, a [dispositions] table with its set")
        witnesses = check_witness_classes(data, where)
        try:
            layers, layers_why = read_layer_tags(layer_dir), ""
        except LookupError as e:
            layers, layers_why = None, str(e)
        program = check_program(data, where, layers)
    except LoopError as e:
        print("loop: %s" % e)
        return 1
    if not plant:
        base_rows, base_why = read_actor_base(kit_dir)
    builds_dir, builds_why = read_builds_dir(kit_dir, root)
    if plant == "actor-list-foreign":
        builds_dir, builds_why = None, PLANTS[plant]
    for s in loop["step"]:
        print("loop: step %s · order %d · state %s · exit %s" % (s["tag"], s["order"], s["state"], s["exit"]))
    for w in loop["workflow"]:
        print("loop: workflow %s · order %d · step %s · reach %s" % (w["name"], w["order"], w["step"], derive_reach(w)))
    print("loop: dispositions %s" % " ".join(loop["dispositions"]))
    for a in data.get("disposition-alias", []):
        print("loop: disposition-alias %s · means %s" % (a["word"], a["means"]))
    print("loop: %d step(s) and %d workflow(s) read from %s" % (len(loop["step"]), len(loop["workflow"]), where))
    if layers is None:
        print("loop: inputs unarmed · %s" % layers_why)
    for step, tags in program.items():
        print("loop: program %s · %d item(s) · %s" % (step, len(tags), " ".join(tags)))
    roles, roles_why = read_role_defaults(scratch.name if plant == "roles-no-kit" else kit_dir)
    item_lines, item_refusals = check_item_declarations(read_item_rows(data, where), roles, roles_why)
    for line in item_lines:
        print(line)
    try:   # TOOL-dPlacedRequest-8 S3: each item's declared seed
        seed_lines, seed_refusals = check_item_seeds(read_item_rows(data, where))
    except LoopError as e:
        seed_lines, seed_refusals = [], [str(e)]
    for line in seed_lines:
        print(line)
    item_refusals = item_refusals + seed_refusals
    print("loop: witness classes %s · refused %s" % (" ".join(data["witnesses"]["classes"]),
                                                      " ".join(data["witnesses"]["refused"])))
    for a in data.get("witness-alias", []):
        print("loop: witness-alias %s · means %s" % (a["word"], a["means"]))
    sites = {}
    for site, cls, by in witnesses:
        print("loop: witness %s · class %s · by %s" % (site, cls, by))
        sites.setdefault(site, {})[site] = cls
    for line in rows:
        fields = line.split("\t")
        if len(fields) == 3:
            print("loop: actor witness %s · %s · until %s" % tuple(fields) + (
                "" if builds_dir is not None else " · foreign build, not graded"))
    if base_rows is None:
        print("loop: actor-list base · no comparison · %s" % base_why)
    else:
        print("loop: actor-list base · %s" % base_why)
    if builds_dir is None:
        print("loop: actor-list builds · foreign · %s" % builds_why)
    else:
        print("loop: actor-list builds · %s" % builds_dir.as_posix())
    refusals = item_refusals + check_actor_list(rows, base_rows, sites, builds_dir)
    # TOOL-dDeclaredLoop-2 S14: an actor witness no list row names is reported, not refused, where
    # floor.no-actor-witness reads off at the landed revision; the floor is read only when one is met.
    unlisted = [r for r in refusals if r.startswith("the actor witness ") and r.endswith(" has no list row naming "
                                                                                       "the build that computes it")]
    if unlisted:
        try:
            if check_floor_off("no-actor-witness", root):
                print("floor: no-actor-witness off")
                for r in unlisted:
                    print("loop: reported · %s" % r)
                refusals = [r for r in refusals if r not in unlisted]
        except ValueError as e:   # LoopError, the floor's copy of it included where this file runs as __main__
            refusals.append(str(e))
    try:
        computed = check_computed_witnesses(data, where)
    except LoopError as e:
        computed, refusals = [], refusals + [str(e)]
    for c in computed:
        print("loop: computed-witness %s · serves %s · class %s · writer %s · armed by %s" % (
            c["name"], c["serves"], c["class"], c["writer"], c["armed-by"]))
    if not plant:
        # TOOL-dDeclaredLoop-21 S2: the review bounds of the tree's policy file at HEAD, refused here so the
        # refusal holds with no unattended kit; an install without the policy kit grades nothing.
        from review_bounds import check_review_bounds
        try:
            bounds, bound_refusals = check_review_bounds(root)
        except LookupError as e:
            print("loop: review bounds unarmed · %s" % e)
        else:
            if bounds:
                print("loop: review bounds · %s" % bounds)
            refusals = refusals + bound_refusals
    if plant in SCOPE_PLANTS and not refusals:
        refusals = check_scope_plant(plant, layers, pathlib.Path(scratch.name), kit_dir, root,
                                     [r["tag"] for r in data.get("item", [])])
    if scratch is not None:
        scratch.cleanup()
    for r in refusals:
        print("loop: refused · %s" % r)
    return 1 if refusals else 0


def check_scope_plant(plant, layers, scratch, kit_dir, root, tags):
    """Run the scope verb under a scope plant, printing its lines, and return the refusals: under
    `scope-selected`, a scratch manifest in `scratch` scoping one unit to one item, which must appear
    on that item's line alone; under `scope-no-kit`, `scratch` as the kit directory, so the inputs and
    every scope line must read `unarmed`."""
    unit, item = PLANT_SCOPE_UNIT
    try:
        if plant == "scope-selected":
            manifest = scratch / "units.toml"
            manifest.write_text('[[unit]]\ntag = "%s"\nscope = ["%s"]\n' % (unit, item), encoding="utf-8")
            lines = derive_item_scope(kit_dir, root, tags, manifest)
        else:
            lines = derive_item_scope(scratch, root, tags)
    except LoopError as e:
        return [str(e)]
    for line in lines:
        print(line)
    if plant == "scope-selected":
        hits = [ln.split(" · ", 1)[0][len("loop: scope "):] for ln in lines if (" %s" % unit) in ln]
        print("loop: fixture · %s listed on %s" % (unit, " ".join(hits) or "no item's line"))
        return [] if hits == [item] else ["the planted unit %s scoped to %s is listed on %s" % (
            unit, item, " ".join(hits) or "no item's line")]
    armed = [ln for ln in lines if " · unarmed · " not in ln]
    return ([] if layers is None else ["the inputs read layer tags with no playbook kit"]) + [
        "a scope line with no playbook kit is armed: %s" % ln for ln in armed]


def write_seed_plant(scratch):
    """The scratch repository the resolver plants run `seed` in, `scratch` itself (TOOL-dPlacedRequest-8): a
    `.unattended.conf` the unattended driver loads, and the build `tFix`'s unit spec, `loop_witness.py`'s
    `FX_UNIT`, whose Files touched declares `PLANT_SEED_PATH` twice, plain and with a leading `./`, committed.
    No path is spelled with backslashes, since the one token rule reads none (its spec's F3)."""
    from loop_witness import FX_UNIT, run_fixture_git, write_fixture_files
    run_fixture_git(scratch, "init", "-q", "--template=")
    write_fixture_files(scratch, {
        ".unattended.conf": "MEMORY_ROOT=memory\n",
        "memory/builds/tFix/spec/2026-01-01-spec-%s.md" % FX_UNIT:
            "# %s — a unit\n\n**Status:** INPROGRESS · rev-1 · 2026-01-01 · node a · Tier-2 · base 0123abcd\n\n"
            "### Files touched (estimate)\n\n- `%s`\n- `./%s`, the same path again\n" % (
                FX_UNIT, PLANT_SEED_PATH, PLANT_SEED_PATH)})
    run_fixture_git(scratch, "add", "-A")
    run_fixture_git(scratch, "commit", "-q", "-m", "the seed plant's unit")
    return FX_UNIT


def check_seed_plant(plant):
    """The refusals of one resolver plant (TOOL-dPlacedRequest-8 AC4, AC5, AC6), each `seed` call it makes
    printed with its exit and output lines: this file run as a process in the scratch repository
    `write_seed_plant` writes under the host temp directory, removed after. `seed-write` owes
    `PLANT_SEED_PATH` once, without its `./`; `seed-question` owes the question's two paths, then exit 2
    naming `--question` with none; `seed-scope` owes the one `unarmed — scope-paths:` line naming
    dRankedPlan. Each holding plant prints `loop: fixture · <plant> held · <what it printed>`."""
    import subprocess
    from loop_witness import read_clean_env, remove_tree
    scratch = tempfile.mkdtemp(prefix="seed-")
    refusals, held = [], ""
    try:
        unit = write_seed_plant(scratch)
        question, asked = PLANT_SEED_QUESTION
        runs = {"seed-write": [(["item.build.unit-pass", "--build", "tFix", "--unit", unit], 0, [PLANT_SEED_PATH])],
                "seed-question": [(["item.plan.research", "--question", question], 0, asked),
                                  (["item.plan.research"], 2, ["loop: seed · the item item.plan.research seeds "
                                                               "question-paths, which takes --question <text>"])],
                "seed-scope": [(["item.design.inventory", "--build", "tFix"], 0, [SEED_SCOPE_UNARMED])]}[plant]
        for args, owed, want in runs:
            p = subprocess.run([sys.executable, str(pathlib.Path(__file__).absolute()), "seed", *args], cwd=scratch,
                               capture_output=True, text=True, encoding="utf-8", errors="replace",
                               env=read_clean_env(PYTHONIOENCODING="utf-8"), timeout=SEED_DRIVER_BOUND * 2)
            out = p.stdout.splitlines()
            print("loop: fixture · seed %s · exit %d" % (" ".join(args), p.returncode))
            for line in out:
                print("loop: fixture ·   %s" % line)
            if p.returncode != owed or out != want:
                refusals.append("seed %s exited %d printing %r, owed exit %d printing %r" % (
                    " ".join(args), p.returncode, out, owed, want))
            elif owed == 0:
                held = " ".join(out)
    except (OSError, subprocess.SubprocessError) as e:
        refusals.append("the plant %s did not run: %s" % (plant, e))
    finally:
        remove_tree(scratch)
    if not refusals:
        print("loop: fixture · %s held · %s" % (plant, held))
    return refusals


def write_conf_plant(plant, scratch):
    """The path of a copy of this file with the one change the conf plant `plant` names, written as
    `loop_lib.py` into the directory `scratch` (TOOL-dDeclaredLoop-117 S2): an opener case appends a
    function that opens a conf and is declared nowhere, `conf-module-unparsable` a definition that does
    not parse, and a body case reduces the named functions' bodies to `return None` through `ast` and
    `ast.unparse`, never a tuple, since the plant's third arm reads this module's `globals()`. The
    appended texts sit here and never at module scope, so `derive_conf_constants` stays empty."""
    import ast
    text = pathlib.Path(__file__).read_text(encoding="utf-8")
    appended = {"conf-opener-literal": 'def read_literal_conf():\n    return open(".memory-tree.conf").read()\n',
                "conf-opener-constant": 'SEED_CONF = ".unattended.conf"\n\n\ndef read_constant_conf():\n'
                                        '    return open(SEED_CONF).read()\n',
                "conf-opener-local": 'def read_local_conf():\n    name = ".memory-tree.conf"\n'
                                     '    return open(name).read()\n',
                "conf-module-unparsable": "def read_broken_conf(:\n"}
    emptied = {"conf-route-opens-none": ("resolve_memory_root_source",),
               "conf-openers-none": ("read_driver_conf", "resolve_memory_root_source")}
    if plant in appended:
        text += "\n\n" + appended[plant]
    else:
        tree = ast.parse(text)
        for f in tree.body:
            if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef)) and f.name in emptied[plant]:
                f.body = [ast.Return(ast.Constant(None))]
        text = ast.unparse(tree)
    path = pathlib.Path(scratch) / "loop_lib.py"
    path.write_text(text, encoding="utf-8")
    return path


def check_conf_readers_plant(loop_lib_path):
    """The `conf-readers-declared` plant's refusals (TOOL-dDeclaredLoop-99 S3): `derive_conf_openers` over
    `loop_lib_path` compared both ways with `CONF_READERS` and `CONF_ROUTES`, one refusal per mismatch,
    in this order: an empty answer; a derived opener in neither tuple; a member of either tuple this
    module binds as a function that the answer lacks. A member this module does not bind is outside the
    comparison and named on the pass line; a LoopError is one refusal, its text."""
    try:
        derived = derive_conf_openers(loop_lib_path)
    except LoopError as e:
        return [str(e)]
    tuples = (("CONF_READERS", CONF_READERS), ("CONF_ROUTES", CONF_ROUTES))
    declared = [m for _, members in tuples for m in members]
    refusals = [] if derived else ["no conf opener found in loop_lib.py"]
    refusals += ["%s opens a conf and is in neither CONF_READERS nor CONF_ROUTES" % d
                 for d in derived if d not in declared]
    refusals += ["%s is in %s and opens no conf" % (m, label) for label, members in tuples for m in members
                 if callable(globals().get(m)) and m not in derived]
    if not refusals:
        print("loop: conf readers declared · %d opener(s) · %s · outside this module %s" % (
            len(derived), " ".join(derived),
            " ".join(m for m in declared if not callable(globals().get(m))) or "none"))
    return refusals


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
