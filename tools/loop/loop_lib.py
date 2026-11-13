#!/usr/bin/env python3
"""loop_lib — the one reader of the loop's definition, `loop.toml` beside this file (TOOL-dDeclaredLoop-1).

    python loop_lib.py --check                    # read the definition, print what was read
    python loop_lib.py --fixture --plant <case>   # read it with one break planted in memory

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
line and exit 1. `--fixture --plant <case>` reads the shipped definition with the named break made in
memory, never on disk, and exits 1 on the refusal the break must draw, 0 if the reader accepted it. The
plants are `PLANTS`. Exit 2 is a usage error.

WHAT THIS DOES NOT CHECK: that a workflow row names a workflow the roles kit holds, which is that kit's
catalogue check, both ways; that a step tag or an exit item is registered in its namespace, which is the
tag index's; that the item an `exit` names exists, since the item rows are not in this file yet; what a
`state` word means; an `[[item]]` row beyond the `tag` and `outcomes` the outcome read asks of it, since
the item schema is its own unit's; that a disposition record's `Item` names a declared item, which reads
None; or that a writer resolved an alias before it wrote. An unknown key on a row is not read and not
refused. Stdlib only.
"""
import pathlib
import re
import sys
import tomllib

KIT_LOOP_VERSION = "1.0"

DEFINITION = "loop.toml"
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
#: `--plant`'s cases, each a break made in the definition as read, and what it does.
PLANTS = {"missing-step": "the step.deploy row taken out",
          "reordered": "the step.test row moved before step.build",
          "bad-step": "the build workflow's step set to step.ship",
          "bad-reach": "the spec-review workflow's reach set to revew",
          "disposition-unknown": "the disposition ask given twice in the set",
          "disposition-alias": "the defer alias's means set to postpone"}


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
    words = set()
    for n, row in enumerate(tables.pop("disposition-alias"), 1):
        word, means = row.get("word"), row.get("means")
        at = "disposition-alias row %d (%s)" % (n, word if isinstance(word, str) and word else "unnamed")
        if not isinstance(word, str) or not word:
            raise LoopError(where, "%s carries no word" % at)
        if word in members:
            raise LoopError(where, "%s names a member of the set, which needs no alias" % at)
        if word in words:
            raise LoopError(where, "%s repeats the word of an earlier row" % at)
        words.add(word)
        if means not in members:
            raise LoopError(where, "%s means %r, which is no member of the set: %s" % (at, means, " ".join(members)))
    tables["dispositions"] = list(members)
    return tables


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
    for row in data.get("disposition-alias", []):
        if row["word"] == word:
            return row["means"]
    raise LoopError(where, "%r is no disposition and no alias of one; the set is %s" % (word, " ".join(members)))


def read_outcome_set(kit_dir, item):
    """The closed outcome set of the `[[item]]` row whose `tag` is `item`: the disposition set for a row
    declaring `outcomes = "dispositions"`, the row's own list otherwise, None for an item the definition
    does not declare. LoopError for an `item` table that is no array of tables, or a row found whose
    `outcomes` is neither."""
    data, where = read_definition(kit_dir)
    check_loop(data, where)
    rows = data.get("item", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise LoopError(where, "'item' is not an array of tables")
    for row in rows:
        if row.get("tag") != item:
            continue
        outcomes = row.get("outcomes")
        if outcomes == OUTCOMES_REF:
            return read_dispositions(kit_dir)
        if not isinstance(outcomes, list) or not outcomes or not all(isinstance(w, str) for w in outcomes):
            raise LoopError(where, "the item %s carries no outcomes, a list of words or %r" % (item, OUTCOMES_REF))
        return list(outcomes)
    return None


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


def write_loop_plant(data, case):
    """`data` with the break `case` names made in it, in place."""
    steps, workflows = data.get("step", []), {w.get("name"): w for w in data.get("workflow", [])}
    if case == "missing-step":
        data["step"] = [r for r in steps if r.get("tag") != "step.deploy"]
    elif case == "reordered":
        data["step"] = sorted(steps, key=lambda r: {"step.test": 2.5}.get(r.get("tag"), r.get("order", 0)))
    elif case == "bad-step":
        workflows["build"]["step"] = "step.ship"
    elif case == "bad-reach":
        workflows["spec-review"]["reach"] = "revew"
    elif case == "disposition-unknown":
        data["dispositions"]["set"].append("ask")
    else:
        next(r for r in data["disposition-alias"] if r.get("word") == "defer")["means"] = "postpone"


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    kit_dir = pathlib.Path(__file__).absolute().parent
    plant = argv[2] if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] else None
    if argv != ["--check"] and plant not in PLANTS:
        print("usage: python loop_lib.py --check | --fixture --plant <%s>" % "|".join(PLANTS), file=sys.stderr)
        return 2
    try:
        data, where = read_definition(kit_dir)
        if plant:
            print("loop: fixture · plant %s · %s" % (plant, PLANTS[plant]))
            write_loop_plant(data, plant)
        loop = check_loop(data, where)
        if not loop["dispositions"]:
            raise LoopError(where, "declares no disposition set, a [dispositions] table with its set")
    except LoopError as e:
        print("loop: %s" % e)
        return 1
    for s in loop["step"]:
        print("loop: step %s · order %d · state %s · exit %s" % (s["tag"], s["order"], s["state"], s["exit"]))
    for w in loop["workflow"]:
        print("loop: workflow %s · order %d · step %s · reach %s" % (w["name"], w["order"], w["step"], derive_reach(w)))
    print("loop: dispositions %s" % " ".join(loop["dispositions"]))
    for a in data.get("disposition-alias", []):
        print("loop: disposition-alias %s · means %s" % (a["word"], a["means"]))
    print("loop: %d step(s) and %d workflow(s) read from %s" % (len(loop["step"]), len(loop["workflow"]), where))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
