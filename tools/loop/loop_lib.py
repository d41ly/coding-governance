#!/usr/bin/env python3
"""loop_lib — the one reader of the loop's definition, `loop.toml` beside this file (TOOL-dDeclaredLoop-1).

    python loop_lib.py --check                    # read the definition, print what was read
    python loop_lib.py --fixture --plant <case>   # read it with one break planted in memory

The definition holds the gov steps as `[[step]]` rows and one `[[workflow]]` row per workflow of the roles
kit: its build order, the step its work sits in and, where it differs from that step's own word, the reach
word its work orders load practices under. Every other kit reads those facts through this module:
`load_loop` returns the definition whole, `read_steps` its step rows, `read_workflow_order` each workflow's
order and `read_workflow_reach` each workflow's reach word.

A definition that does not hold is refused with `LoopError`, a `ValueError` naming the file and the row: a
file that does not read or is no TOML; a `step` or `workflow` table that is no array of tables; the gov
steps missing, repeated or out of order, a tag that is no gov step, or an `order` that is not the step's
place; a step row without a `state` or an `exit`; a workflow row with no name or named twice, an `order`
that is not an integer at or above 0, a `step` that is absent or is neither a step tag nor `none`, or a
`reach` outside `REACH_WORDS`.

`--check` prints one line per step and per workflow, then a count, and exits 0; a refused definition is one
line and exit 1. `--fixture --plant <case>` reads the shipped definition with the named break made in
memory, never on disk, and exits 1 on the refusal the break must draw, 0 if the reader accepted it. The
plants are `PLANTS`. Exit 2 is a usage error.

WHAT THIS DOES NOT CHECK: that a workflow row names a workflow the roles kit holds, which is that kit's
catalogue check, both ways; that a step tag or an exit item is registered in its namespace, which is the
tag index's; that the item an `exit` names exists, since the item rows are not in this file yet; or what
a `state` word means. An unknown key on a row is not read and not refused. Stdlib only.
"""
import pathlib
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
#: `--plant`'s cases, each a break made in the definition as read, and what it does.
PLANTS = {"missing-step": "the step.deploy row taken out",
          "reordered": "the step.test row moved before step.build",
          "bad-step": "the build workflow's step set to step.ship",
          "bad-reach": "the spec-review workflow's reach set to revew"}


class LoopError(ValueError):
    """The definition does not hold; the message is `<where>: <what>`, the file and the row."""

    def __init__(self, where, what):
        super().__init__("%s: %s" % (where, what))


def check_loop(data, where):
    """`data`, a parsed definition, returned as `{"step": [...], "workflow": [...]}` once every row holds;
    LoopError naming `where` and the first row that does not."""
    tables = {}
    for table in ("step", "workflow"):
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
    """The definition in `kit_dir`, checked: `{"step": [rows], "workflow": [rows]}`, each in file order."""
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


def write_loop_plant(data, case):
    """`data` with the break `case` names made in it, in place."""
    steps, workflows = data.get("step", []), {w.get("name"): w for w in data.get("workflow", [])}
    if case == "missing-step":
        data["step"] = [r for r in steps if r.get("tag") != "step.deploy"]
    elif case == "reordered":
        data["step"] = sorted(steps, key=lambda r: {"step.test": 2.5}.get(r.get("tag"), r.get("order", 0)))
    elif case == "bad-step":
        workflows["build"]["step"] = "step.ship"
    else:
        workflows["spec-review"]["reach"] = "revew"


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
    except LoopError as e:
        print("loop: %s" % e)
        return 1
    for s in loop["step"]:
        print("loop: step %s · order %d · state %s · exit %s" % (s["tag"], s["order"], s["state"], s["exit"]))
    for w in loop["workflow"]:
        print("loop: workflow %s · order %d · step %s · reach %s" % (w["name"], w["order"], w["step"], derive_reach(w)))
    print("loop: %d step(s) and %d workflow(s) read from %s" % (len(loop["step"]), len(loop["workflow"]), where))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
