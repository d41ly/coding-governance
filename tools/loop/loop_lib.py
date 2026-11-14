#!/usr/bin/env python3
"""loop_lib — the one reader of the loop's definition, `loop.toml` beside this file (TOOL-dDeclaredLoop-1).

    python loop_lib.py --check                    # read the definition, print what was read
    python loop_lib.py --scopes                   # each item's instruction scope, derived
    python loop_lib.py --fixture --plant <case>   # read it with one break planted in memory
    python loop_lib.py --grade-site <site> <entry>...   # grade one declaration site's witness entries

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
one of which meets it. `check_program` grades the rows as one needs graph, ordered by the needs-graph
helper below: every need declared, no cycle, each outcome set closed through `derive_outcome_set`, the
rule `read_outcome_set` applies, each outcome routed once to a target that resolves, each input's text
before its first `:` a layer tag `read_layer_tags` reads from the playbook kit's `layers.toml`, and each
step's `exit` an item of that step. `read_items` returns the rows once both checks hold. `--scopes`
prints each item's instruction scope, `derive_item_scope` running that kit's `load_sets.py derive` once
per item as a subprocess, so this module imports no sibling kit. Where the playbook kit does not
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
order, or `loop: inputs unarmed` and why before them where no layer tags resolve, then one `loop: item`
line per item in file order, each field's source or `pending` or `unarmed`, and `loop: items · <n>
read · <p> pending · <u> unarmed`. It then prints the witness classes, one line per witness alias and per witness, one
line per list row with its build and the list's base line, the base or `no comparison` and why, the
builds line, the folder or `foreign` and why, one `loop: computed-witness <name> · serves <tag> · class
<class> · writer <writer> · armed by <build>` line per computed witness, and each refusal of the items,
the list and the computed witnesses as `loop: refused · ...`, exit 1. `--fixture --plant <case>` reads the shipped
definition and list with the named break made in memory, never on disk, the list's base being the
shipped list as read, and exits 1 on the refusal the break must draw, 0 if the reader accepted it. The
plants are `PLANTS`. `--grade-site <site> <entry>...` prints `loop: site <site> · <item> · <word> ·
<class>` per entry, `· until <build>` on a `DOD_CORE` actor entry, `· adopter-declared, not on the
shipped list` on a `DOD_EXTRA` one, then each refusal, and exits 0, or 1 on a refusal. `--scopes` prints `loop: scope <tag> · <derive's item line> · <the tags it lists, or none>` per
item and exits 0, or 1 on a refused definition or a derive that exits non-zero. Exit 2 is a usage
error, a site outside `DECLARATION_SITES` included.

WHAT THIS DOES NOT CHECK: that a workflow row names a workflow the roles kit holds, which is that kit's
catalogue check, both ways; that a step tag or an item tag is registered in its namespace, which is the
tag index's; what a `state` word means; that a `command:` name names a real command, a `hook:` event
exists, or a pending role's slot is the stem a later build ships; a non-role item's allowance beyond
being non-empty; a need on an item outside the five programs; that
a `stand-in:` path exists or a `transition` route reaches a transition table; that a disposition record's
`Item` names a declared item, which reads None; or that a writer resolved an alias before it wrote. An
unknown key on a row is not read and not refused. That a witness's `by` is true. Stdlib only, but for
`read_actor_base` and `read_builds_dir`, which import the memory-tree kit's compare base and its conf
reader inside the function, and `read_role_defaults`, which imports the roles kit's library there, so a
reader calling `load_loop` never reaches them.
"""
import pathlib
import re
import sys
import tempfile
import tomllib

KIT_LOOP_VERSION = "1.0"

DEFINITION = "loop.toml"
#: The shrink-only list of actor witnesses beside the definition, `<site>\t<witness>\t<build>` per row.
ACTOR_LIST = "actor-witnesses.txt"
#: The gov steps, in the loop's order. A definition holds exactly these `[[step]]` rows, in this order.
STEP_TAGS = ("step.plan", "step.design", "step.build", "step.test", "step.deploy")
#: A workflow's `step` when its work sits in no gov step.
NO_STEP = "none"
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
          "computed-unserved": "the acceptance computed witness set to serve item.build.acceptanc"}
#: The plants whose break is in what the scope verb reads rather than in the definition, so `--check`
#: runs whole and the scope verb runs after it.
SCOPE_PLANTS = ("scope-selected", "scope-no-kit")
#: The `scope-selected` plant's unit: one scratch manifest row scoped to one item.
PLANT_SCOPE_UNIT = ("unit.loop-fixture", "item.plan.record")
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
    """`(builds_dir, why)`: `<root>/<MEMORY_ROOT>/builds` where the memory tree's conf at `root` sets
    `DESIGN_RECORD`, the mark of the tree that owns the chain's build names, or None and why: no
    memory-tree kit, or no `DESIGN_RECORD` in the conf, a missing conf included. The memory-tree kit's
    `read_design_conf` is imported inside the function, as `read_actor_base` imports its compare base."""
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
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    return pathlib.Path(root) / memory_root / "builds", ""


def read_actor_rows(kit_dir):
    """The actor-witness list's lines in `kit_dir`, blank lines dropped; LoopError where it does not read."""
    path = pathlib.Path(kit_dir) / ACTOR_LIST
    try:
        return [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    except (OSError, UnicodeDecodeError) as e:
        raise LoopError(path.as_posix(), "cannot be read: %s" % e)


def check_site_witnesses(kit_dir, site, entries):
    """`(lines, refusals)` of the declaration site `site`'s `entries`, each `<item>` or `<item>:<word>`:
    a line per entry whose word resolves through `[[witness-alias]]`; a refusal per entry with no word,
    a word no alias row holds, or an actor word with no `<site> <item>` list row, and per list row of
    `site` whose item is no actor entry. The list is the one in `kit_dir`, read without a base.
    `DOD_EXTRA` is the adopter's own: no list row is read for it, and an actor entry there is admitted,
    its line ending `· adopter-declared, not on the shipped list`."""
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
    lines, refusals, actors = [], [], set()
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
                refusals.append("%s %s is an actor witness and the list holds no row %s %s naming the build "
                                "that computes it" % (site, entry, site, item))
        lines.append(line)
    for item in listed:
        if item not in actors:
            refusals.append("the list row %s %s names no actor entry of %s" % (site, item, site))
    return lines, refusals


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


def check_program(data, where, layers):
    """`data`'s `[[item]]` rows graded as each gov step's program, returned as `{step tag: [item tags in
    needs order]}`. `layers` is the set of layer tags an input may name, or None where none resolved,
    which leaves the inputs unchecked. LoopError naming `where`, the item and the field that does not
    hold: a tag opening no `item.<step>.` of a gov step, a `step` other than that one, or a tag given
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
        if len(parts) != 3 or parts[0] != "item" or parts[1] not in steps or not parts[2]:
            raise LoopError(where, "item row %d tag %r opens no item.<step>. of a gov step: %s" % (
                n, tag, " ".join(steps)))
        if row.get("step") != steps[parts[1]]:
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
    return {s: [t for t in order if declared[t]["step"] == s] for s in STEP_TAGS}


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
        else:
            plan["exit"] = "item.design.exit"


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    kit_dir = pathlib.Path(__file__).absolute().parent
    plant = argv[2] if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] else None
    if argv[:1] == ["--grade-site"] and len(argv) >= 2 and argv[1] in DECLARATION_SITES:
        try:
            lines, refusals = check_site_witnesses(kit_dir, argv[1], argv[2:])
        except LoopError as e:
            print("loop: %s" % e)
            return 1
        for line in lines:
            print(line)
        for r in refusals:
            print("loop: refused · %s" % r)
        return 1 if refusals else 0
    if argv not in (["--check"], ["--scopes"]) and plant not in PLANTS:
        print("usage: python loop_lib.py --check | --scopes | --fixture --plant <%s> | --grade-site <%s> <entry>..." % (
            "|".join(PLANTS), "|".join(DECLARATION_SITES)), file=sys.stderr)
        return 2
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
    try:
        computed = check_computed_witnesses(data, where)
    except LoopError as e:
        computed, refusals = [], refusals + [str(e)]
    for c in computed:
        print("loop: computed-witness %s · serves %s · class %s · writer %s · armed by %s" % (
            c["name"], c["serves"], c["class"], c["writer"], c["armed-by"]))
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


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
