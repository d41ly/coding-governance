#!/usr/bin/env python3
"""loop_table.py — one transition table per level, and the engine that refuses a move it lacks (TOOL-dDeclaredLoop-13).

    python loop_table.py move --level <level> --from <state> --item <tag> --outcome <word> [--fact k=v]...
    python loop_table.py check [--selftest]
    python loop_table.py --fixture --plant <case>

The loop definition beside this file holds `[states]`, each level's open states, and one `[[transition]]`
row per move of the build, feature and unit tables: its `level`, `from` (states, `none` for the level's
entry, or `@open`), the `item` whose `outcome` fires it, by tag, its `to` (a state, `@prior` or
`@reentry`), its `witness`, and optionally a `disposition` and `when = "before-push"`. `[[stand-in]]`
names the owner of each row item whose owning build has not landed, and `[[owed-row]]` each cross-step
route whose build row another unit or build writes. `read_transition_rows` and `read_stand_ins` read
them from a parsed definition, so a plant is made in memory.

`derive_move` answers a move from the rows alone: the matching row and its resolved `to`, or
`TransitionRefused` naming the level, state, item and outcome. The match is exact on the level, the state
in the row's expanded `from`, the item, the outcome, and the `disposition` fact where the row declares
one; a `before-push` row matches only with the `pushed` fact `no`. `@prior` takes the `prior` fact, an
open state of the level, and `@reentry` the state of the step whose item the `reenters` fact names. An
unknown level or state, an absent or malformed fact a matching row needs, or two matching rows is a
ValueError, never a default.

`move` prints `move — <level> · <from> → <to> · <item>`, with `· stand-in <owner>` after it where the
item is a stand-in, and exits 0; `refused — <level> · <from> · <item> · <outcome>: no row`, exit 1; and
`unanswered — <level> · <from> · <item> · <outcome>: <why>`, exit 2, on a ValueError. `check` prints one
`loop: table <level> · <n> row(s) · <m> state(s)` line per level, one `loop: owed <item> · <outcome> ·
<by>` line per owed row, one `loop: stand-in <item> · <owner>` line per stand-in, and each refusal as
`loop: refused · ...`, exit 1. Both exit 2 where the definition does not read or holds no
`[[transition]]` row, never admitting a move. `--fixture --plant <case>` runs `check` with one break of
`PLANTS` made in memory by `write_table_plant`, never on disk. `check --selftest` runs `check`, every
plant and the moves of each answer through `loop_lib.run_selftest_cases`, exit 0 when every case holds.

The route join (S7) reads each `[[item]]` row's routes: a cross-step route is an outcome routed to
`transition`, or to a declared item of another step. Forward, each has a build row for its item and
outcome, or an owed row; backward, every build row on a declared item fires on a cross-step route, and
where that route names an item the row enters that item's step's state. An owed row on no cross-step
route, or on one a build row covers, is stale. Each step's exit fires a build row out of its state, or
stands on the owed list.

WHAT THIS DOES NOT CHECK: whether a witness holds; whether a stand-in's owner has landed; that every row
item owned by an unlanded build has a stand-in row; reachability, termination and counted edges; the
feature rows' last-unit rule; the routes of the feature and unit rows, which the join reads for the build
table alone; that an owed row's `by` names a real unit or build.
"""
import argparse
import pathlib
import re
import sys

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import (ROUTE_TRANSITION, SEG, LoopError, check_loop, derive_outcome_set,  # noqa: E402
                      read_definition, read_item_rows, read_items, run_selftest_cases)

SAY = "loop"
#: A level's entry in a row's `from`, never a state.
ENTRY = "none"
#: A row's `from` standing for every open state of its level.
OPEN = "@open"
#: The one row item that is no tag: the re-entry row, its item named by the `reenters` fact.
ANY_ITEM = "@any"
#: A row's `to` read from the move's facts.
DYNAMIC_TO = ("@prior", "@reentry")
#: A row's `when`: it holds only while the build's landing is unpushed.
BEFORE_PUSH = "before-push"
#: A row item: `item.<seg>.<seg>`.
ITEM_TAG = re.compile(r"item\.%s\.%s" % (SEG.pattern, SEG.pattern))
#: A `[[transition]]` row's required keys.
ROW_KEYS = ("level", "from", "item", "outcome", "to", "witness")
#: `--plant`'s cases, each a break made in memory on the rows as read, and the text its refusal must name.
PLANTS = {"bad-state": ("a unit row entering reviewing, no unit state", "reviewing"),
          "two-rows": ("a second row for B7's move", "matched by two rows"),
          "bad-exit": ("three unit rows: one on the bare plan.exit, one on item.plan.nosuch, one on an "
                       "outcome outside item.plan.exit's set", "item.plan.nosuch"),
          "dropped-row": ("B7 deleted, item.build.exit still routing recorded to transition", "item.build.exit"),
          "unrouted-row": ("a build row on item.build.acceptance's pass, routed inside its own step",
                           "item.build.acceptance"),
          "owed-stale": ("an owed row for item.build.exit's recorded, which B7 covers", "owed-row item.build.exit"),
          "stand-in": ("a stand-in row for item.plan.input, which no row names, and item.design.exit's "
                       "owner set to dRankedPlan", "item.plan.input")}


class TransitionRefused(Exception):
    """No row of the table holds the move; the message names the level, state, item and outcome."""

    def __init__(self, level, state, item, outcome):
        super().__init__("%s · %s · %s · %s: no row" % (level, state, item, outcome))


def read_transition_rows(data, where):
    """`{"states": {level: [states]}, "transition": [rows], "owed-row": [rows], "item-states": {item tag:
    its step's state}}` of a parsed definition, the rows ungraded; LoopError for a `[states]` that is no
    table of non-empty lists of words, or a `transition` or `owed-row` table that is no array of tables."""
    states = data.get("states", {})
    if not isinstance(states, dict) or not all(
            isinstance(v, list) and v and all(isinstance(s, str) and SEG.fullmatch(s) for s in v)
            for v in states.values()):
        raise LoopError(where, "'states' is not a table of levels, each a non-empty list of state words")
    out = {"states": states}
    for table in ("transition", "owed-row"):
        rows = data.get(table, [])
        if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
            raise LoopError(where, "'%s' is not an array of tables" % table)
        out[table] = rows
    step_states = {r.get("tag"): r.get("state") for r in check_loop(data, where)["step"]}
    out["item-states"] = {r.get("tag"): step_states.get(r.get("step")) for r in read_item_rows(data, where)}
    return out


def read_stand_ins(data, where):
    """The `[[stand-in]]` rows of a parsed definition, ungraded; LoopError for a table that is no array of
    tables."""
    rows = data.get("stand-in", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise LoopError(where, "'stand-in' is not an array of tables")
    return rows


def derive_move(level, state, item, outcome, facts, tables=None):
    """The row the table holds for this move, and its resolved `to`. `tables` is what
    read_transition_rows returns, the shipped definition's when None. Raises TransitionRefused when
    no row matches; raises ValueError on an unknown level, state, or a fact a row's guard needs."""
    if tables is None:
        tables = read_transition_rows(*read_definition(KIT))
    states = tables["states"]
    if level not in states:
        raise ValueError("the level %s is none of %s" % (level, " ".join(states)))
    if state != ENTRY and state not in states[level]:
        raise ValueError("the state %s is no %s state, nor %s: %s" % (state, level, ENTRY, " ".join(states[level])))
    hits = []
    for row in tables["transition"]:
        if (row.get("level"), row.get("item"), row.get("outcome")) != (level, item, outcome):
            continue
        if state not in sum((states[level] if s == OPEN else [s] for s in row.get("from", [])), []):
            continue
        if "disposition" in row:
            if "disposition" not in facts:
                raise ValueError("the move needs the fact disposition, which its row %s matches on" % row["disposition"])
            if facts["disposition"] != row["disposition"]:
                continue
        if row.get("when") == BEFORE_PUSH:
            if facts.get("pushed") not in ("yes", "no"):
                raise ValueError("the move needs the fact pushed, yes or no, which a before-push row reads; "
                                 "it has %r" % facts.get("pushed"))
            if facts["pushed"] != "no":
                continue
        hits.append(row)
    if not hits:
        raise TransitionRefused(level, state, item, outcome)
    if len(hits) > 1:
        raise ValueError("two rows match the move, a table defect `check` refuses")
    row, to = hits[0], hits[0].get("to")
    if to == "@prior":
        if facts.get("prior") not in states[level]:
            raise ValueError("the move needs the fact prior, an open %s state; it has %r" % (level, facts.get("prior")))
        to = facts["prior"]
    elif to == "@reentry":
        to = tables["item-states"].get(facts.get("reenters"))
        if to is None:
            raise ValueError("the move needs the fact reenters, a declared item whose step has a state; it has "
                             "%r" % facts.get("reenters"))
    return row, to


def check_transition_tables(data, where, items):
    """`(lines, refusals)` of the transition tables of a parsed definition, against `items`, the declared
    `[[item]]` rows. LoopError where a table does not read."""
    t, stand = read_transition_rows(data, where), read_stand_ins(data, where)
    loop = check_loop(data, where)
    members, states = loop["dispositions"], t["states"]
    declared = {r.get("tag"): r for r in items}
    sets = {tag: derive_outcome_set(r, members, where) for tag, r in declared.items()}
    stand_owner = {r.get("item"): r.get("owner") for r in stand}
    lines, refusals, graded = [], [], []
    for n, row in enumerate(t["transition"], 1):
        level, src, item, outcome, to = (row.get(k) for k in ("level", "from", "item", "outcome", "to"))
        at = "transition row %d (%s · %s · %s · %s)" % (
            n, level, "/".join(map(str, src)) if isinstance(src, list) else src, item, outcome)
        missing = [k for k in ROW_KEYS if k == "from" and not (isinstance(src, list) and src and all(
            isinstance(s, str) for s in src)) or k != "from" and not (isinstance(row.get(k), str) and row.get(k))]
        if missing:
            refusals.append("%s carries no %s" % (at, " and no ".join(missing)))
            continue
        if level not in states:
            refusals.append("%s names the level %s, which [states] does not declare" % (at, level))
            continue
        for s in src:
            if s not in (ENTRY, OPEN) and s not in states[level]:
                refusals.append("%s leaves %s, no %s state" % (at, s, level))
        if to not in states[level] and to not in DYNAMIC_TO:
            refusals.append("%s enters %s, no %s state nor %s" % (at, to, level, " ".join(DYNAMIC_TO)))
        if item == ANY_ITEM:
            if to != "@reentry":
                refusals.append("%s fires on %s, which only a row entering @reentry may" % (at, ANY_ITEM))
        elif not ITEM_TAG.fullmatch(item):
            refusals.append("%s names %s, which is no item.<step>.<name> tag" % (at, item))
        elif item in declared:
            if outcome not in sets[item]:
                refusals.append("%s fires on %s, no outcome of %s's set: %s" % (at, outcome, item, " ".join(sets[item])))
        elif item not in stand_owner:
            refusals.append("%s names %s, which resolves to no [[item]] row and no [[stand-in]] row" % (at, item))
        if "disposition" in row and row["disposition"] not in members:
            refusals.append("%s matches the disposition %r, no member of [dispositions]" % (at, row["disposition"]))
        if "when" in row and row["when"] != BEFORE_PUSH:
            refusals.append("%s holds when %r, and the one guard is %s" % (at, row["when"], BEFORE_PUSH))
        graded.append((n, row, {x for s in src for x in (states[level] if s == OPEN else [s])}))
    for i, (n, a, a_from) in enumerate(graded):
        for m, b, b_from in graded[i + 1:]:
            if (a["level"], a["item"], a["outcome"]) != (b["level"], b["item"], b["outcome"]) or not a_from & b_from:
                continue
            if "disposition" in a and "disposition" in b and a["disposition"] != b["disposition"]:
                continue
            refusals.append("the move %s · %s · %s · %s is matched by two rows, %d and %d: one row per move" % (
                a["level"], "/".join(sorted(a_from & b_from)), a["item"], a["outcome"], n, m))
    for level, words in states.items():
        lines.append("%s: table %s · %d row(s) · %d state(s)" % (
            SAY, level, sum(1 for r in t["transition"] if r.get("level") == level), len(words)))
    # S7, the route join over the build table, both ways
    cross = {}
    for tag, r in declared.items():
        for word, target in (r.get("routes") or {}).items():
            if target == ROUTE_TRANSITION or target in declared and declared[target].get("step") != r.get("step"):
                cross[(tag, word)] = target
    build = [(n, r, f) for n, r, f in graded if r["level"] == "build"]
    covered = {(r["item"], r["outcome"]) for _n, r, _f in build}
    owed = {}
    for k, row in enumerate(t["owed-row"], 1):
        item, outcome, by = (row.get(x) for x in ("item", "outcome", "by"))
        if not all(isinstance(v, str) and v for v in (item, outcome, by)):
            refusals.append("owed-row %d carries no item, outcome and by" % k)
            continue
        owed[(item, outcome)] = by
        lines.append("%s: owed %s · %s · %s" % (SAY, item, outcome, by))
        if (item, outcome) not in cross:
            refusals.append("the owed-row %s · %s · %s is stale: no cross-step route of a declared item" % (
                item, outcome, by))
        elif (item, outcome) in covered:
            refusals.append("the owed-row %s · %s · %s is stale: a build row covers it; delete the owed row" % (
                item, outcome, by))
    for (tag, word), target in cross.items():
        if (tag, word) not in covered and (tag, word) not in owed:
            refusals.append("the item %s routes %s to %s, a cross-step route no build row and no [[owed-row]] "
                            "covers" % (tag, word, target))
    for n, r, _f in build:
        key = (r["item"], r["outcome"])
        if r["item"] not in declared:
            continue
        if key not in cross:
            refusals.append("build row %d (%s · %s) fires on no cross-step route: %s routes %s to %s" % (
                n, r["item"], r["outcome"], r["item"], r["outcome"], declared[r["item"]].get("routes", {}).get(
                    r["outcome"], "nothing")))
        elif cross[key] in declared and r["to"] != t["item-states"].get(cross[key]):
            refusals.append("build row %d (%s · %s) enters %s, while its route names %s, whose step's state is %s" % (
                n, r["item"], r["outcome"], r["to"], cross[key], t["item-states"].get(cross[key])))
    for step in loop["step"]:
        exit_tag = step["exit"]
        if not any(r["item"] == exit_tag and step["state"] in f for _n, r, f in build) and not any(
                i == exit_tag for i, _o in owed):
            refusals.append("the step %s exit %s fires no build row out of %s and stands on no owed row" % (
                step["tag"], exit_tag, step["state"]))
    # S8, the stand-ins
    row_items = {r.get("item") for r in t["transition"]}
    for k, row in enumerate(stand, 1):
        item, owner = row.get("item"), row.get("owner")
        if not (isinstance(item, str) and item and isinstance(owner, str) and owner):
            refusals.append("stand-in row %d carries no item and owner" % k)
            continue
        lines.append("%s: stand-in %s · %s" % (SAY, item, owner))
        if item not in row_items:
            refusals.append("the stand-in row %s · %s names no row item: stale, delete it" % (item, owner))
        elif item in declared and declared[item].get("owner") != owner:
            refusals.append("the stand-in row %s · %s names another owner than its [[item]] row's, %s" % (
                item, owner, declared[item].get("owner")))
    return lines, refusals


def write_table_plant(case, data):
    """`data`, a parsed definition, with the break `case` names made in its transition rows, in place."""
    rows = data["transition"]
    if case == "bad-state":
        rows.append({"level": "unit", "from": ["tested"], "item": "item.deploy.land", "outcome": "refused",
                     "to": "reviewing", "witness": "planted"})
    elif case == "two-rows":
        rows.append({"level": "build", "from": ["building"], "item": "item.build.exit", "outcome": "recorded",
                     "to": "testing", "witness": "planted"})
    elif case == "bad-exit":
        for item, outcome in (("plan.exit", "recorded"), ("item.plan.nosuch", "recorded"),
                              ("item.plan.exit", "approved")):
            rows.append({"level": "unit", "from": ["designed"], "item": item, "outcome": outcome,
                         "to": "built", "witness": "planted"})
    elif case == "dropped-row":
        rows[:] = [r for r in rows if (r.get("level"), r.get("item"), r.get("outcome")) !=
                   ("build", "item.build.exit", "recorded")]
    elif case == "unrouted-row":
        rows.append({"level": "build", "from": ["building"], "item": "item.build.acceptance", "outcome": "pass",
                     "to": "testing", "witness": "planted"})
    elif case == "owed-stale":
        data["owed-row"].append({"item": "item.build.exit", "outcome": "recorded", "by": "TOOL-dDeclaredLoop-15"})
    elif case == "stand-in":
        data["stand-in"].append({"item": "item.plan.input", "owner": "dRankedPlan"})
        next(r for r in data["stand-in"] if r.get("item") == "item.design.exit")["owner"] = "dRankedPlan"


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="loop_table.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run check with one plant made in memory")
    ap.add_argument("--plant", choices=list(PLANTS))
    sub = ap.add_subparsers(dest="verb")
    mv = sub.add_parser("move", help="answer one move from the rows alone")
    mv.add_argument("--level", required=True)
    mv.add_argument("--from", dest="state", required=True)
    mv.add_argument("--item", required=True)
    mv.add_argument("--outcome", required=True)
    mv.add_argument("--fact", action="append", default=[], help="k=v, a fact a row's guard or target reads")
    chk = sub.add_parser("check", help="check the tables, their route join and the stand-ins")
    chk.add_argument("--selftest", action="store_true", help="check, every plant, and the moves")
    args = ap.parse_args(argv)
    if args.fixture != bool(args.plant) or (args.fixture and args.verb):
        ap.error("--fixture takes --plant <case> and no verb")
    if not args.fixture and not args.verb:
        ap.error("a verb, move or check, or --fixture --plant <case>")
    if args.verb == "check" and args.selftest:
        move = ["move", "--level", "build", "--from"]
        cases = [("check", ["check"], 0, "%s: table build" % SAY, ""),
                 ("owed close", ["check"], 0, "%s: owed item.deploy.close · closed · TOOL-dDeclaredLoop-15" % SAY, "")]
        cases += [(p, ["--fixture", "--plant", p], 1, "%s: refused · " % SAY, PLANTS[p][1]) for p in PLANTS]
        cases += [("move by order", move + ["planning", "--item", "item.design.exit", "--outcome", "recorded"], 1,
                   "refused — build · planning · item.design.exit · recorded", "no row"),
                  ("move designing", move + ["designing", "--item", "item.design.exit", "--outcome", "recorded"], 0,
                   "move — build · designing → building · item.design.exit", ""),
                  ("move prior", move + ["paused", "--item", "item.life.request", "--outcome", "resume", "--fact",
                                         "prior=testing"], 0, "move — build · paused → testing", ""),
                  ("move no prior", move + ["paused", "--item", "item.life.request", "--outcome", "resume"], 2,
                   "unanswered — ", "prior"),
                  ("move unpushed", move + ["building", "--item", "@any", "--outcome", "admitted", "--fact",
                                            "reenters=item.plan.input", "--fact", "pushed=no"], 0,
                   "move — build · building → planning", ""),
                  ("move pushed", move + ["building", "--item", "@any", "--outcome", "admitted", "--fact",
                                          "reenters=item.plan.input", "--fact", "pushed=yes"], 1, "refused — ", ""),
                  ("move no pushed", move + ["building", "--item", "@any", "--outcome", "admitted", "--fact",
                                             "reenters=item.plan.input"], 2, "unanswered — ", "pushed"),
                  ("move stand-in", move + ["planning", "--item", "item.plan.exit", "--outcome", "recorded"], 0,
                   "move — build · planning → designing · item.plan.exit", "stand-in dRankedPlan")]
        return run_selftest_cases(main, cases, "%s: table selftest" % SAY)
    try:
        data, where = read_definition(KIT)
    except LoopError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    if not data.get("transition"):
        print("%s: unarmed · %s holds no [[transition]] row: no move is admitted" % (SAY, where))
        return 2
    if args.verb == "move":
        facts = {}
        for fact in args.fact:
            k, eq, v = fact.partition("=")
            if not (k and eq):
                ap.error("--fact takes k=v, and %r is not" % fact)
            facts[k] = v
        said = "%s · %s · %s · %s" % (args.level, args.state, args.item, args.outcome)
        try:
            tables = read_transition_rows(data, where)
            row, to = derive_move(args.level, args.state, args.item, args.outcome, facts, tables)
        except TransitionRefused as e:
            print("refused — %s" % e)
            return 1
        except ValueError as e:
            print("unanswered — %s: %s" % (said, e))
            return 2
        owner = {r.get("item"): r.get("owner") for r in read_stand_ins(data, where)}.get(args.item)
        print("move — %s · %s → %s · %s%s" % (args.level, args.state, to, args.item,
                                             " · stand-in %s" % owner if owner else ""))
        return 0
    try:
        items = read_items(KIT)
        read_transition_rows(data, where)
        read_stand_ins(data, where)
    except LoopError as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    if args.plant:
        print("%s: fixture · plant %s · %s" % (SAY, args.plant, PLANTS[args.plant][0]))
        write_table_plant(args.plant, data)
    lines, refusals = check_transition_tables(data, where, items)
    for line in lines:
        print(line)
    for why in refusals:
        print("%s: refused · %s" % (SAY, why))
    return 1 if refusals else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
