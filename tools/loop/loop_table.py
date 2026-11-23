#!/usr/bin/env python3
"""loop_table.py — one transition table per level, and the engine that refuses a move it lacks (TOOL-dDeclaredLoop-13).

    python loop_table.py move --level <level> --from <state> --item <tag> --outcome <word> [--fact k=v]...
    python loop_table.py check [--selftest]
    python loop_table.py phase --from <PHASE> [--to <PHASE>] [--fact k=v]... [--extra "<phases>"]
    python loop_table.py --fixture --plant <case>

The loop definition beside this file holds `[states]`, each level's open states, and one `[[transition]]`
row per move of the build, feature and unit tables: its `level`, `from` (states, `none` for the level's
entry, or `@open`), the `item` whose `outcome` fires it, by tag, its `to` (a state, `@prior` or
`@reentry`), its `witness`, and optionally a `disposition`, `when = "before-push"` and `draws = "none"`,
which the transition writer reads to record a backward ending with no draw. `@any` fires a row entering
`@reentry`, or one whose outcome is one of `ENDING_OUTCOMES`, a build's ending once its rework budget is
spent (TOOL-dDeclaredLoop-31). `[states]`'s
`terminal` key is no level: it lists the build level's terminal states (TOOL-dDeclaredLoop-15), which a
build row may enter and no row may leave. Each `<level>-terminal` key, `feature-terminal` and
`unit-terminal`, is no level either: it lists that level's terminal set, members of its own states,
which no row of the level may leave (TOOL-dDeclaredLoop-54); `read_terminal_set(tables, level)` reads
any level's set, a ValueError naming the level and its key where the set is absent. `[[stand-in]]` names the owner of each row item whose owning
build has not landed, and `[[owed-row]]` each cross-step route whose build row another unit or build
writes. `read_transition_rows` and `read_stand_ins` read them from a parsed definition, so a plant is
made in memory.

`derive_move` answers a move from the rows alone: the matching row and its resolved `to`, or
`TransitionRefused` naming the level, state, item and outcome, as it does for any move asked from a
build terminal. The match is exact on the level, the state
in the row's expanded `from`, the item, the outcome, and the `disposition` fact where the row declares
one; a `before-push` row matches only with the `pushed` fact `no`. `@prior` takes the `prior` fact, an
open state of the level, and `@reentry` the state of the step whose item the `reenters` fact names. An
unknown level or state, an absent or malformed fact a matching row needs, or two matching rows is a
ValueError, never a default.

`derive_direction` answers a resolved build move's direction from the rows' step orders, never typed:
`forward` into a terminal or a later step, `backward` into an earlier one, `lateral` where an end has no
step, so a move back is recorded through the same writer and channels as a move forward.

THE PHASE MAP (TOOL-dDeclaredLoop-52). One `[[phase]]` row per phase of the unattended driver's
`PHASES_CORE`, carrying `step`, the `[[step]]` tag whose state the phase reads, or `state`, a build
state, a terminal or `none`, where the phase has no step; a qualified row adds `QUALIFIERS`, each matched
against the run's fact of that key. `read_phase_map` reads the rows, `derive_phase_position` answers a
phase's `(state, step)` from the first qualified row whose every qualifier matches, else the unqualified
one, and `derive_crossed_exits` the step exits a move between two steps crosses: each step's from the
first step's own, the first step where it is `none`, up to the target step's, none where the target is
`none`. `phase` prints `phase <PHASE> · state <state> · step <tag|none>`, with `· to <PHASE> · crosses
<tags|none>` after it given `--to`, whose phase reads its unqualified row, and exits 0; `refused —
phase <PHASE>: no row`, exit 1. An adopter phase (TOOL-dDeclaredLoop-63), a member of `--extra`, the
driver's `PHASES_EXTRA`, that no row reads, reads `state none · step none` with `· adopter phase` after
the reading it qualifies, so a move into it crosses nothing and a move out counts from the first step;
`crosses` stays the line's last field. Run without `--extra`, `phase` reads `PHASES_EXTRA` from the
`.unattended.conf` at the top of the work tree it runs in, through `loop_lib.read_driver_conf`, sourced as
the driver sources it, only for a phase no row reads; a conf that does not source prints `loop: refused ·
driver conf unreadable: <conf> — <reason>`, exit 1. `--extra=` reads no conf (TOOL-dDeclaredLoop-70). Of
`check --selftest`'s cases, those opening `tree <name>` run in one of four scratch work trees it builds:
`extra`, whose conf sets `PHASES_EXTRA="STAGING"`, `broken`, whose conf exits 3, `bare`, with none, and
`leak`, whose conf sets neither name, its case run with `MEMORY_ROOT` and `PHASES_EXTRA` exported. `check` grades the rows by `check_phase_rows` and joins the unqualified
rows with the driver's `PHASES_CORE` line both ways, read through `loop_checklist.py`'s
`read_core_registries`, printing the join `unarmed` where the driver does not resolve; every plant
passes the shipped rows' unqualified phases in its place, taken before the break.

`move` prints `move — <level> · <from> → <to> · <item>`, with `· stand-in <owner>` after it where the
item is a stand-in, then `· <direction>` last for a build move, and exits 0; `refused — <level> · <from> · <item> · <outcome>: no row`, exit 1; and
`unanswered — <level> · <from> · <item> · <outcome>: <why>`, exit 2, on a ValueError. `check` prints one
`loop: table <level> · <n> row(s) · <m> state(s)` line per level, then one `loop: terminal <level> ·
<states>` line per level, the build's first, and refuses a level declaring no terminal set, a row whose
`from`, `@open` expanded, holds a state of its own level's set, and a terminal also listed among the
build's open states, the refusal that keeps `@open` off a build terminal. It prints one `loop: owed <item> · <outcome> ·
<by>` line per owed row, one `loop: stand-in <item> · <owner>` line per stand-in, and each refusal as
`loop: refused · ...`, exit 1. Both exit 2 where the definition does not read or holds no
`[[transition]]` row, never admitting a move. `--fixture --plant <case>` runs `check` with one break of
`PLANTS` made in memory by `write_table_plant`, never on disk. `check --selftest` runs `check`, every
plant, the moves of each answer and direction, and `direction-order`, the rows with two steps' orders
swapped, through `loop_lib.run_selftest_cases`, exit 0 when every case holds.

The route join (S7) reads each `[[item]]` row's routes: a cross-step route is an outcome routed to
`transition`, or to a declared item of another step. Forward, each has a build row for its item and
outcome, or an owed row; backward, every build row on a declared item fires on a cross-step route, and
where that route names an item the row enters that item's step's state. An owed row on no cross-step
route, or on one a build row covers, is stale. Each step's exit fires a build row out of its state, or
stands on the owed list.

The entry rows' join (KICK-dKeptSession-18) reads the claim's `FIRST_MOVES`, each disposition a claim
admits and its first move from `none`, `(item, outcome)`, imported from `claim.py` inside
`check_transition_tables`, and joins it with the graded build rows from `none` by `check_entry_rows`.
A row fires a key's first move when its item and outcome are the move's and its `disposition`, where it
carries one, is that key. Forward, each key is a member of `[dispositions]` and exactly one row fires its
first move; backward, every build row from `none` fires a key's first move. `check` prints `loop: entry
rows · <key> → <to> · ...`, each key sorted with the `to` of the row firing it, `?` where no single row
does, and each refusal opens `entry rows · <key> · forward: ` or `entry rows · <disposition> · backward:
`, `-` for a row carrying none; an import of `claim.py` that fails is the one refusal `entry rows ·
FIRST_MOVES unread: <why>` and no line.

WHAT THIS DOES NOT CHECK: whether a witness holds; whether a stand-in's owner has landed; that every row
item owned by an unlanded build has a stand-in row; reachability, termination and counted edges; the
feature rows' last-unit rule; the routes of the feature and unit rows, which the join reads for the build
table alone; that an owed row's `by` names a real unit or build; that every terminal is entered by a row,
which four are not yet; a phase row's qualifier value against the driver's halt and hold codes; that
an explicit `--extra` is the driver's `PHASES_EXTRA`, which the caller passes and wins over the conf; that each
member of a level's terminal set is a state of that level, or that a `-terminal` key names a level: a
misspelt key leaves its level with no set, which `check` refuses, and a member no state reaches reds the
termination check; an entry row's `to`, which the entry rows' line prints and the table's source rows
decide.
"""
import argparse
import pathlib
import re
import sys

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_checklist import read_core_registries  # noqa: E402
from loop_lib import (ROUTE_TRANSITION, SEG, LoopError, check_loop, derive_outcome_set,  # noqa: E402
                      read_definition, read_driver_conf, read_item_rows, read_items, run_selftest_cases)

SAY = "loop"
#: A level's entry in a row's `from`, never a state.
ENTRY = "none"
#: A row's `from` standing for every open state of its level.
OPEN = "@open"
#: The one row item that is no tag: the re-entry row, its item named by the `reenters` fact, and the ending rows.
ANY_ITEM = "@any"
#: The outcomes an `@any` row may record besides a re-entry: the endings of a spent budget (TOOL-dDeclaredLoop-31).
ENDING_OUTCOMES = ("close-incomplete", "park-for-owner", "descope", "disposed")
#: A row's `to` read from the move's facts.
DYNAMIC_TO = ("@prior", "@reentry")
#: A row's `when`: it holds only while the build's landing is unpushed.
BEFORE_PUSH = "before-push"
#: The `[states]` key listing the build level's terminal states, read beside the levels and never as one.
TERMINAL = "terminal"
#: The tail of a `[states]` key listing another level's terminal set, `<level>-terminal`, never a level.
TERMINAL_SUFFIX = "-terminal"
#: A row item: `item.<seg>.<seg>`.
ITEM_TAG = re.compile(r"item\.%s\.%s" % (SEG.pattern, SEG.pattern))
#: A `[[transition]]` row's required keys.
ROW_KEYS = ("level", "from", "item", "outcome", "to", "witness")
#: A `[[phase]]` row's keys, and the qualifiers a row matches against the run's facts (TOOL-dDeclaredLoop-52).
PHASE_KEYS = ("phase", "state", "step")
QUALIFIERS = ("halt-code", "hold-code", "ending")
#: The step a `HELD` row reads: the step of the phase its run was held from, named by the `held-from` fact
#: the driver writes at the hold (TOOL-dDeclaredLoop-67 S13). No other phase's row may read it.
HELD_IN, HELD, HELD_FROM = "held-in", "HELD", "held-from"
#: A phase, as the unattended driver spells one.
PHASE_WORD = re.compile(r"[A-Z][A-Z_]*")
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
                       "owner set to dRankedPlan", "item.plan.input"),
          "terminal-from": ("a build row whose from is landed", "leaves landed, a terminal"),
          "terminal-open": ("landed appended to the build's open states", "landed is both"),
          "unit-terminal-from": ("a unit row from @open into designed", "leaves deployed, a terminal"),
          "level-no-terminal": ("unit-terminal taken out of [states]", "the level unit declares no terminal set"),
          "any-unending": ("an @any row from testing on the outcome lap, entering building",
                           "only a row entering @reentry"),
          "phase-missing": ("the REVIEWING phase row taken out", "REVIEWING"),
          "phase-stale": ("a phase row for DRAFTING on step.design", "DRAFTING"),
          "phase-shape": ("the REVIEWING phase row given state designing beside its step", "both state and step"),
          "phase-twice": ("a second unqualified BUILDING phase row", "two unqualified rows"),
          "held-in-elsewhere": ("the BUILDING phase row given the step held-in", "(BUILDING) reads the step held-in"),
          "phase-row-unknown": ("a phase row for STAGING, an adopter phase, with no PHASES_EXTRA passed",
                                "names no member of PHASES_CORE or PHASES_EXTRA"),
          "entry-row-missing": ("the build row from none carrying repeat taken out",
                                "entry rows · repeat · forward: no build row"),
          "entry-set-missing": ("repeat taken out of [dispositions]", "entry rows · repeat · forward: no member"),
          "entry-row-extra": ("a build row from none on item.entry.claim's claimed carrying ask, into planning",
                              "entry rows · ask · backward: "),
          "entry-row-twice": ("the build row from none carrying repeat appended a second time",
                              "entry rows · repeat · forward: 2 build rows")}


class TransitionRefused(Exception):
    """No row of the table holds the move; the message names the level, state, item and outcome."""

    def __init__(self, level, state, item, outcome):
        super().__init__("%s · %s · %s · %s: no row" % (level, state, item, outcome))


def read_transition_rows(data, where):
    """`{"states": {level: [states]}, "terminal": [states], "level-terminal": {level: [states]},
    "transition": [rows], "owed-row": [rows], "item-states": {item tag: its step's state}, "step-order":
    {step's state: its order}}` of a parsed definition, the rows ungraded. `[states]`'s `terminal` key is
    split out as the build level's terminal states, never a level, absent reading as none, and each
    `<level>-terminal` key as that level's terminal set under `level-terminal` (TOOL-dDeclaredLoop-54).
    LoopError for a `[states]` that is no table of non-empty lists of words, the terminal keys included,
    or a `transition` or `owed-row` table that is no array of tables."""
    states = data.get("states", {})
    if not isinstance(states, dict) or not all(
            isinstance(v, list) and v and all(isinstance(s, str) and SEG.fullmatch(s) for s in v)
            for v in states.values()):
        raise LoopError(where, "'states' is not a table of levels, each a non-empty list of state words")
    out = {"states": {k: v for k, v in states.items() if k != TERMINAL and not k.endswith(TERMINAL_SUFFIX)},
           "terminal": states.get(TERMINAL, []),
           "level-terminal": {k[:-len(TERMINAL_SUFFIX)]: v for k, v in states.items() if k.endswith(TERMINAL_SUFFIX)}}
    for table in ("transition", "owed-row"):
        rows = data.get(table, [])
        if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
            raise LoopError(where, "'%s' is not an array of tables" % table)
        out[table] = rows
    steps = check_loop(data, where)["step"]
    step_states = {r.get("tag"): r.get("state") for r in steps}
    out["item-states"] = {r.get("tag"): step_states.get(r.get("step")) for r in read_item_rows(data, where)}
    out["step-order"] = {r.get("state"): r.get("order") for r in steps}
    return out


def derive_direction(state, to, tables):
    """'forward', 'backward' or 'lateral' for one resolved build move, from tables["step-order"]
    and tables["terminal"], both of what read_transition_rows returns: forward into a terminal, lateral
    where either end has no step or both share one, else as the two steps' orders compare."""
    if to in tables["terminal"]:
        return "forward"
    order = tables["step-order"]
    if state not in order or to not in order or order[state] == order[to]:
        return "lateral"
    return "forward" if order[to] > order[state] else "backward"


def read_terminal_set(tables, level):
    """`level`'s terminal set from `tables`, what read_transition_rows returns: `terminal` for the build
    level, its `<level>-terminal` key otherwise. ValueError naming the level and its key where the set is
    absent or empty (TOOL-dDeclaredLoop-54)."""
    ends = tables["terminal"] if level == "build" else tables.get("level-terminal", {}).get(level)
    if not ends:
        raise ValueError("the level %s declares no terminal set: [states] holds no %s" % (
            level, TERMINAL if level == "build" else level + TERMINAL_SUFFIX))
    return list(ends)


def read_stand_ins(data, where):
    """The `[[stand-in]]` rows of a parsed definition, ungraded; LoopError for a table that is no array of
    tables."""
    rows = data.get("stand-in", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise LoopError(where, "'stand-in' is not an array of tables")
    return rows


def derive_from_states(row, open_states):
    """The states a row's `from` holds, `@open` expanded to `open_states`, its level's open states: the
    one spelling of the expansion, which `derive_move` and `check_recorded_move` both read."""
    return sum((list(open_states) if s == OPEN else [s] for s in row.get("from", [])), [])


def check_recorded_move(move, tables):
    """Whether a build row holds a recorded move, `move` carrying `from`, `to` and `item`: a row whose
    `item` is the move's, whose expanded `from` holds the move's `from`, and whose `to` is the move's,
    `@prior` or `@reentry`. A record holds no outcome and no facts, so this matches the row and never
    resolves its guard. `tables` is what read_transition_rows returns (TOOL-dDeclaredLoop-7)."""
    open_states = tables["states"].get("build", [])
    return any(row.get("level") == "build" and row.get("item") == move.get("item")
               and move.get("from") in derive_from_states(row, open_states)
               and row.get("to") in (move.get("to"),) + DYNAMIC_TO
               for row in tables["transition"])


def derive_move(level, state, item, outcome, facts, tables=None):
    """The row the table holds for this move, and its resolved `to`. `tables` is what
    read_transition_rows returns, the shipped definition's when None. Raises TransitionRefused when
    no row matches; raises ValueError on an unknown level, state, or a fact a row's guard needs."""
    if tables is None:
        tables = read_transition_rows(*read_definition(KIT))
    states = tables["states"]
    if level not in states:
        raise ValueError("the level %s is none of %s" % (level, " ".join(states)))
    if level == "build" and state in tables["terminal"]:
        raise TransitionRefused(level, state, item, outcome)  # no row leaves a terminal
    if state != ENTRY and state not in states[level]:
        raise ValueError("the state %s is no %s state, nor %s: %s" % (state, level, ENTRY, " ".join(states[level])))
    hits = []
    for row in tables["transition"]:
        if (row.get("level"), row.get("item"), row.get("outcome")) != (level, item, outcome):
            continue
        if state not in derive_from_states(row, states[level]):
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


def check_entry_rows(rows, members, first_moves):
    """`(line, refusals)` of the build rows from `none`, `rows` their `(n, row)` pairs as graded, joined both
    ways with `first_moves`, the claim's `{disposition: (item, outcome)}`, and `members`, the
    `[dispositions]` set: forward, each key is a member and exactly one row fires its first move, the row's
    `disposition`, where it carries one, being that key; backward, every row fires the first move of a key.
    Each key and each row draws at most one refusal; the line names each key, sorted, with the `to` of the
    one row firing it, `?` where no single row does (KICK-dKeptSession-18)."""
    said, refusals = [], []
    for key in sorted(first_moves):
        item, outcome = first_moves[key]
        hits = [(n, r) for n, r in rows
                if (r["item"], r["outcome"]) == (item, outcome) and r.get("disposition", key) == key]
        said.append("%s → %s" % (key, hits[0][1]["to"] if len(hits) == 1 else "?"))
        if key not in members:
            refusals.append("entry rows · %s · forward: no member of [dispositions]" % key)
        elif not hits:
            refusals.append("entry rows · %s · forward: no build row from %s fires %s · %s" % (key, ENTRY, item, outcome))
        elif len(hits) > 1:
            refusals.append("entry rows · %s · forward: %d build rows from %s fire %s · %s: rows %s" % (
                key, len(hits), ENTRY, item, outcome, ", ".join(str(n) for n, _r in hits)))
    for n, r in rows:
        if not any((r["item"], r["outcome"]) == tuple(move) and r.get("disposition", key) == key
                   for key, move in first_moves.items()):
            refusals.append("entry rows · %s · backward: build row %d (%s · %s) fires no first move of FIRST_MOVES" % (
                r.get("disposition", "-"), n, r["item"], r["outcome"]))
    return "%s: entry rows · %s" % (SAY, " · ".join(said)), refusals


def check_transition_tables(data, where, items):
    """`(lines, refusals)` of the transition tables of a parsed definition, against `items`, the declared
    `[[item]]` rows. LoopError where a table does not read."""
    t, stand = read_transition_rows(data, where), read_stand_ins(data, where)
    loop = check_loop(data, where)
    members, states, terminal = loop["dispositions"], t["states"], t["terminal"]
    declared = {r.get("tag"): r for r in items}
    sets = {tag: derive_outcome_set(r, members, where) for tag, r in declared.items()}
    stand_owner = {r.get("item"): r.get("owner") for r in stand}
    lines, refusals, graded, ends = [], [], [], {}
    for level in states:
        try:
            ends[level] = read_terminal_set(t, level)
        except ValueError as e:
            refusals.append(str(e))
            ends[level] = []
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
        for s in derive_from_states(row, states[level]):
            if s in ends[level]:
                refusals.append("%s leaves %s, a terminal: no move leaves one" % (at, s))
            elif s != ENTRY and s not in states[level]:
                refusals.append("%s leaves %s, no %s state" % (at, s, level))
        if to not in states[level] and to not in DYNAMIC_TO and not (level == "build" and to in terminal):
            refusals.append("%s enters %s, no %s state nor %s" % (at, to, level, " ".join(DYNAMIC_TO)))
        if item == ANY_ITEM:
            if to != "@reentry" and outcome not in ENDING_OUTCOMES:
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
    for level in sorted(states, key=lambda v: v != "build"):
        if ends[level]:
            lines.append("%s: terminal %s · %s" % (SAY, level, " ".join(ends[level])))
    for s in terminal:
        if s in states.get("build", []):
            refusals.append("%s is both an open build state and a terminal" % s)
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
    # KICK-dKeptSession-18, the entry rows joined with the claim's first moves; imported here, since
    # claim.py imports loop_parents.py, which imports this module at its top
    try:
        from claim import FIRST_MOVES
    except Exception as e:   # any failure to read the admitted set is one refusal, never a pass
        refusals.append("entry rows · FIRST_MOVES unread: %s" % e)
    else:
        line, more = check_entry_rows([(n, r) for n, r, f in build if ENTRY in f], members, FIRST_MOVES)
        lines.append(line)
        refusals += more
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


def read_phase_map(data, where):
    """`{"rows": the [[phase]] rows ungraded, "steps": the [[step]] rows check_loop grades}` of a parsed
    definition; LoopError where `phase` is no array of tables."""
    rows = data.get("phase", [])
    if not isinstance(rows, list) or not all(isinstance(r, dict) for r in rows):
        raise LoopError(where, "'phase' is not an array of tables")
    return {"rows": rows, "steps": check_loop(data, where)["step"]}


def derive_phase_position(phase, facts, phase_map=None, extra=None, tree="."):
    """`(state, step)` of `phase`: its first row carrying a qualifier whose every qualifier equals the fact
    of that key in `facts`, else its row carrying none; `step` the row's, else "none", and `state` the
    row's, else its [[step]] row's. `phase_map` is what read_phase_map returns, the shipped definition's
    when None. Where no row reads it, `("none", "none")` for a member of `extra`, the adopter's phases
    (TOOL-dDeclaredLoop-63), else LookupError naming the phase. `extra` None reads `PHASES_EXTRA` from the
    driver conf of `tree`'s work tree through `loop_lib.read_driver_conf`, only for a phase no row reads,
    and its LoopError passes through (TOOL-dDeclaredLoop-70). A row's step `held-in` answers the step of
    the phase `facts`' `held-from` names, read by a second call with the same map and the default
    population, and "none" where `facts` carries no `held-from` other than `HELD`; the state is the
    row's (TOOL-dDeclaredLoop-67 S13)."""
    if phase_map is None:
        phase_map = read_phase_map(*read_definition(KIT))
    rows = [r for r in phase_map["rows"] if r.get("phase") == phase]
    row = next((r for r in rows if any(q in r for q in QUALIFIERS)
                and all(facts.get(q) == r[q] for q in QUALIFIERS if q in r)), None)
    row = row or next((r for r in rows if not any(q in r for q in QUALIFIERS)), None)
    if row is None:
        if extra is None:
            extra = read_driver_conf(tree, ("PHASES_EXTRA",)).get("PHASES_EXTRA", "").split()
        if phase in extra:
            return "none", "none"
        raise LookupError("phase %s: no row" % phase)
    step = row.get("step") or "none"
    if step == HELD_IN:
        held = facts.get(HELD_FROM)
        step = derive_phase_position(held, {}, phase_map, tree=tree)[1] if held and held != HELD else "none"
        return row.get("state"), step
    state = row.get("state") or next((s.get("state") for s in phase_map["steps"] if s.get("tag") == step), None)
    return state, step


def derive_crossed_exits(from_step, to_step, steps):
    """The `exit` of each [[step]] row of `steps`, in step order, whose order is at least `from_step`'s, 1
    where it is "none", and below `to_step`'s; [] where `to_step` is "none". LookupError on a step tag
    `steps` lacks."""
    if to_step == "none":
        return []
    order = {s.get("tag"): s.get("order") for s in steps}
    for tag in (from_step, to_step):
        if tag != "none" and tag not in order:
            raise LookupError("step %s: no [[step]] row" % tag)
    low = 1 if from_step == "none" else order[from_step]
    return [s.get("exit") for s in sorted(steps, key=lambda s: s.get("order")) if low <= s.get("order") < order[to_step]]


def check_phase_rows(phase_map, core, states, terminal, extra=()):
    """`(lines, refusals)` of the [[phase]] rows of `phase_map`, what read_phase_map returns, against
    `states`, the build level's open states, and `terminal`, its terminal states; the unqualified rows
    joined both ways with `core`, the driver's PHASES_CORE members, or the join printed unarmed where
    `core` is None. A row naming a phase in neither `core` nor `extra`, the driver's PHASES_EXTRA
    members, is refused; an adopter phase needs no row, and a row for one is admitted
    (TOOL-dDeclaredLoop-67 S23). The step `held-in` is admitted on a `HELD` row beside its state, and
    refused on any other (S14)."""
    tags = {s.get("tag") for s in phase_map["steps"]}
    lines, refusals, plain, named = [], [], {}, set()
    rows = phase_map["rows"]
    for n, row in enumerate(rows, 1):
        phase = row.get("phase")
        at = "phase row %d (%s)" % (n, phase)
        if not (isinstance(phase, str) and PHASE_WORD.fullmatch(phase)):
            refusals.append("%s names no phase, a word of [A-Z][A-Z_]*" % at)
            continue
        named.add(phase)
        unknown = sorted(k for k in row if k not in PHASE_KEYS + QUALIFIERS)
        if unknown:
            refusals.append("%s carries %s, no key of a phase row" % (at, " ".join(unknown)))
        held_in = row.get("step") == HELD_IN
        if held_in and phase != HELD:
            refusals.append("%s reads the step %s, which only a %s row reads: the step its run was held from" % (
                at, HELD_IN, HELD))
        elif held_in and row.get("state") not in list(states) + list(terminal) + ["none"]:
            refusals.append("%s reads the step %s and the state %r, no build state, terminal nor none" % (
                at, HELD_IN, row.get("state")))
        elif held_in:
            pass
        elif "state" in row and "step" in row:
            refusals.append("%s carries both state and step: a stepped phase's state is its step's" % at)
        elif "state" not in row and "step" not in row:
            refusals.append("%s carries neither state nor step" % at)
        elif "step" in row and row["step"] not in tags:
            refusals.append("%s reads the step %r, no [[step]] tag" % (at, row["step"]))
        elif "state" in row and row["state"] not in list(states) + list(terminal) + ["none"]:
            refusals.append("%s reads the state %r, no build state, terminal nor none" % (at, row["state"]))
        quals = [q for q in QUALIFIERS if q in row]
        refusals += ["%s qualifies on %s, which is no non-empty string" % (at, q) for q in quals
                     if not (isinstance(row[q], str) and row[q])]
        if not quals and phase in plain:
            refusals.append("%s and phase row %d are two unqualified rows of %s: one per phase" % (
                at, plain[phase], phase))
        elif not quals:
            plain[phase] = n
    lines.append("%s: phase map · %d row(s) · %d qualified" % (
        SAY, len(rows), sum(1 for r in rows if any(q in r for q in QUALIFIERS))))
    if core is None:
        lines.append("%s: phase join · unarmed · the unattended driver's PHASES_CORE line does not resolve beside "
                     "this kit, so no phase is joined" % SAY)
        return lines, refusals
    refusals += ["the phase %s of PHASES_CORE has no unqualified phase row" % p for p in core if p not in plain]
    refusals += ["the phase row of %s names no member of PHASES_CORE or PHASES_EXTRA" % p
                 for p in sorted(named - set(core) - set(extra))]
    lines.append("%s: phase join · PHASES_CORE · %d phase(s)" % (SAY, len(core)))
    return lines, refusals


def write_table_plant(case, data):
    """`data`, a parsed definition, with the break `case` names made in its rows, in place."""
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
    elif case == "terminal-from":
        rows.append({"level": "build", "from": ["landed"], "item": "item.life.request", "outcome": "resume",
                     "to": "@prior", "witness": "planted"})
    elif case == "terminal-open":
        data["states"]["build"].append("landed")
    elif case == "unit-terminal-from":
        rows.append({"level": "unit", "from": [OPEN], "item": "item.plan.exit", "outcome": "recorded",
                     "to": "designed", "witness": "planted"})
    elif case == "level-no-terminal":
        del data["states"]["unit" + TERMINAL_SUFFIX]
    elif case == "any-unending":
        rows.append({"level": "build", "from": ["testing"], "item": ANY_ITEM, "outcome": "lap", "to": "building",
                     "witness": "planted"})
    elif case == "phase-missing":
        data["phase"][:] = [r for r in data["phase"] if r.get("phase") != "REVIEWING"]
    elif case == "phase-stale":
        data["phase"].append({"phase": "DRAFTING", "step": "step.design"})
    elif case == "phase-shape":
        next(r for r in data["phase"] if r.get("phase") == "REVIEWING")["state"] = "designing"
    elif case == "phase-twice":
        data["phase"].append({"phase": "BUILDING", "step": "step.build"})
    elif case == "held-in-elsewhere":
        next(r for r in data["phase"] if r.get("phase") == "BUILDING")["step"] = HELD_IN
    elif case == "phase-row-unknown":
        data["phase"].append({"phase": "STAGING", "state": "none"})
    elif case in ("entry-row-missing", "entry-row-twice"):
        repeat = next(r for r in rows if r.get("level") == "build" and ENTRY in r.get("from", [])
                      and r.get("disposition") == "repeat")
        if case == "entry-row-missing":
            rows.remove(repeat)
        else:
            rows.append(dict(repeat))
    elif case == "entry-set-missing":
        data["dispositions"]["set"].remove("repeat")
    elif case == "entry-row-extra":
        rows.append({"level": "build", "from": [ENTRY], "item": "item.entry.claim", "outcome": "claimed",
                     "disposition": "ask", "to": "planning", "witness": "planted"})


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
    ph = sub.add_parser("phase", help="a phase's build state and step, and the step exits a move crosses")
    ph.add_argument("--from", dest="phase_from", required=True)
    ph.add_argument("--to")
    ph.add_argument("--fact", action="append", default=[], help="k=v, a fact a qualified row matches")
    ph.add_argument("--extra", default=None, help="the adopter's phases, the driver's PHASES_EXTRA, space-separated; "
                    "absent, read from the .unattended.conf of the work tree it runs in")
    chk = sub.add_parser("check", help="check the tables, their route join, the stand-ins and the phase map")
    chk.add_argument("--selftest", action="store_true", help="check, every plant, and the moves")
    args = ap.parse_args(argv)
    if args.fixture != bool(args.plant) or (args.fixture and args.verb):
        ap.error("--fixture takes --plant <case> and no verb")
    if not args.fixture and not args.verb:
        ap.error("a verb, move, phase or check, or --fixture --plant <case>")
    if args.verb == "check" and args.selftest:
        move = ["move", "--level", "build", "--from"]
        cases = [("check", ["check"], 0, "%s: table build" % SAY, ""),
                 ("terminal", ["check"], 0, "%s: terminal build · landed withdrawn superseded incomplete deferred "
                                            "retired refused merged answered" % SAY, ""),
                 ("terminal unit", ["check"], 0, "%s: terminal unit · deployed" % SAY, ""),
                 ("owed place", ["check"], 0, "%s: owed item.plan.place · unplaced · dRankedPlan" % SAY, ""),
                 ("stand-in close", ["check"], 0, "%s: stand-in item.life.close · dWellOiledMachine" % SAY, "")]
        cases += [("phase join", ["check"], 0, "%s: phase join · " % SAY, "")]
        # KICK-dKeptSession-18: the entry rows' join, each key's `to` read from the rows
        cases += [("entry rows", ["check"], 0,
                   "%s: entry rows · new → planning · patch → designing · repeat → designing" % SAY, "")]
        cases += [(p, ["--fixture", "--plant", p], 1, "%s: refused · " % SAY, PLANTS[p][1]) for p in PLANTS]
        cases += [("phase step", ["phase", "--from", "REVIEWING"], 0,
                   "phase REVIEWING · state designing · step step.design", ""),
                  ("phase halt", ["phase", "--from", "ABORTED", "--fact", "halt-code=budget-exhausted"], 0,
                   "phase ABORTED · state incomplete · step none", ""),
                  ("phase other halt", ["phase", "--from", "ABORTED", "--fact", "halt-code=fork-unresolvable"], 0,
                   "phase ABORTED · state withdrawn · step none", ""),
                  # TOOL-dDeclaredLoop-70: --extra= reads no conf of the tree the leg runs in
                  ("phase no row", ["phase", "--from", "DRAFTING", "--extra="], 1,
                   "refused — phase DRAFTING: no row", ""),
                  ("phase parked", ["phase", "--from", "HELD", "--fact", "hold-code=owner-decision", "--fact",
                                    "ending=park-for-owner"], 0, "phase HELD · state parked · step none", ""),
                  ("phase one qualifier", ["phase", "--from", "HELD", "--fact", "hold-code=owner-decision"], 0,
                   "phase HELD · state paused · step none", ""),
                  # TOOL-dDeclaredLoop-67 S13: a held run reads the step of the phase it was held from
                  ("phase held-in", ["phase", "--from", "HELD", "--fact", "held-from=BUILDING"], 0,
                   "phase HELD · state paused · step step.build", ""),
                  ("phase crosses design", ["phase", "--from", "SPECCING", "--to", "BUILDING"], 0,
                   "phase SPECCING · state designing · step step.design · to BUILDING · crosses item.design.exit", ""),
                  ("phase crosses plan", ["phase", "--from", "PREFLIGHT", "--to", "SPECCING"], 0,
                   "phase PREFLIGHT · state none · step none · to SPECCING · crosses item.plan.exit", ""),
                  ("phase crosses back", ["phase", "--from", "VERIFYING", "--to", "BUILDING"], 0,
                   "phase VERIFYING · state testing · step step.test · to BUILDING · crosses none", "")]
        # TOOL-dDeclaredLoop-63: an adopter phase, a member of --extra with no row, reads ungated
        cases += [("phase adopter", ["phase", "--from", "STAGING", "--extra", "STAGING"], 0,
                   "phase STAGING · state none · step none · adopter phase", ""),
                  ("phase adopter misspelt", ["phase", "--from", "STAGNG", "--extra", "STAGING"], 1,
                   "refused — phase STAGNG: no row", ""),
                  ("phase into adopter", ["phase", "--from", "REVIEWING", "--to", "STAGING", "--extra", "STAGING QA"], 0,
                   "phase REVIEWING · state designing · step step.design · to STAGING · adopter phase · crosses none",
                   ""),
                  ("phase out of adopter", ["phase", "--from", "STAGING", "--to", "BUILDING", "--extra", "STAGING"], 0,
                   "phase STAGING · state none · step none · adopter phase · to BUILDING · crosses item.plan.exit "
                   "item.design.exit", ""),
                  # ponytail: --to REVIEWING puts `crosses` after both readings, so a marker at either breaks
                  # the opening; a case is a prefix match and cannot see a marker at the line's end
                  ("phase row over extra", ["phase", "--from", "REVIEWING", "--to", "REVIEWING", "--extra",
                                            "REVIEWING"], 0,
                   "phase REVIEWING · state designing · step step.design · to REVIEWING · crosses none", "")]
        # TOOL-dDeclaredLoop-70: no --extra reads PHASES_EXTRA from the scratch work tree the case runs in
        cases += [("tree adopter", ["tree", "extra", "phase", "--from", "STAGING"], 0,
                   "phase STAGING · state none · step none · adopter phase", ""),
                  ("tree into adopter", ["tree", "extra", "phase", "--from", "REVIEWING", "--to", "STAGING"], 0,
                   "phase REVIEWING · ", "adopter phase · crosses none"),
                  ("tree misspelt", ["tree", "extra", "phase", "--from", "STAGNG"], 1,
                   "refused — phase STAGNG: no row", ""),
                  ("tree explicit empty", ["tree", "extra", "phase", "--from", "STAGING", "--extra="], 1,
                   "refused — phase STAGING: no row", ""),
                  ("tree broken conf", ["tree", "broken", "phase", "--from", "STAGING"], 1,
                   "%s: refused · driver conf unreadable: " % SAY, "exit 3"),
                  ("tree broken row", ["tree", "broken", "phase", "--from", "REVIEWING"], 0,
                   "phase REVIEWING · state designing · step step.design", ""),
                  ("tree bare", ["tree", "bare", "phase", "--from", "STAGING"], 1,
                   "refused — phase STAGING: no row", ""),
                  # TOOL-dDeclaredLoop-79 S3: the caller's exports never read as the conf's
                  ("tree leak", ["tree", "leak", "phase", "--from", "BOGUS"], 1,
                   "refused — phase BOGUS: no row", "")]
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
                   "move — build · planning → designing · item.plan.exit", "stand-in dRankedPlan"),
                  ("move landed", move + ["deploying", "--item", "item.deploy.close", "--outcome", "closed"], 0,
                   "move — build · deploying → landed · item.deploy.close · stand-in dShippedRelease", ""),
                  ("move refused", move + ["planning", "--item", "item.plan.triage-judge", "--outcome", "refuse"], 0,
                   "move — build · planning → refused", ""),
                  ("move withdrawn", move + ["building", "--item", "item.life.close", "--outcome", "withdrawn",
                                             "--fact", "pushed=no"], 0, "move — build · building → withdrawn", ""),
                  ("move withdrawn pushed", move + ["building", "--item", "item.life.close", "--outcome", "withdrawn",
                                                    "--fact", "pushed=yes"], 1, "refused — ", ""),
                  ("move parent", move + ["designing", "--item", "item.deploy.parents", "--outcome", "withdrawn"], 0,
                   "move — build · designing → planning · item.deploy.parents", ""),
                  ("move ending", move + ["building", "--item", "@any", "--outcome", "close-incomplete", "--fact",
                                          "pushed=no"], 0, "move — build · building → incomplete", ""),
                  ("move ending landed", move + ["landed", "--item", "@any", "--outcome", "close-incomplete",
                                                 "--fact", "pushed=no"], 1, "refused — build · landed", ""),
                  ("move ending parked", move + ["testing", "--item", "@any", "--outcome", "park-for-owner"], 0,
                   "move — build · testing → parked", ""),
                  ("move disposed", move + ["parked", "--item", "@any", "--outcome", "disposed", "--fact",
                                            "disposition=continue", "--fact", "prior=testing"], 0,
                   "move — build · parked → testing", ""),
                  ("move descope", move + ["testing", "--item", "@any", "--outcome", "descope"], 0,
                   "move — build · testing → building", " · backward"),
                  ("move from terminal", move + ["landed", "--item", "item.life.request", "--outcome", "resume",
                                                 "--fact", "prior=testing"], 1, "refused — build · landed", ""),
                  ("direction forward", move + ["building", "--item", "item.build.exit", "--outcome", "recorded"], 0,
                   "move — build · building → testing · item.build.exit", " · forward"),
                  ("direction backward", move + ["testing", "--item", "item.test.attribute", "--outcome",
                                                 "code-miss"], 0, "move — build · testing → building", " · backward"),
                  ("direction lateral", move + ["building", "--item", "item.life.request", "--outcome", "pause"], 0,
                   "move — build · building → paused", " · lateral"),
                  ("direction-order", ["direction-order"], 0,
                   "%s: direction-order · building → testing · backward" % SAY, "")]

        def run_table_case(argv):
            """`main(argv)`, or for `direction-order` the shipped rows with building's and testing's step
            orders swapped, so a direction read from anything but the rows still prints forward; an argv
            opening `tree <name>` runs the rest with the scratch work tree `<name>` as the working directory,
            the environment that tree declares set for the case and the prior values put back after."""
            if argv[:1] == ["tree"]:
                here, put = os.getcwd(), envs.get(argv[1], {})
                prior = {k: os.environ.get(k) for k in put}
                os.environ.update(put)
                os.chdir(scratch / argv[1])
                try:
                    return main(argv[2:])
                finally:
                    os.chdir(here)
                    for k, v in prior.items():
                        if v is None:
                            os.environ.pop(k, None)
                        else:
                            os.environ[k] = v
            if argv != ["direction-order"]:
                return main(argv)
            tables = read_transition_rows(*read_definition(KIT))
            order = tables["step-order"]
            swapped = dict(tables, **{"step-order": dict(order, building=order["testing"], testing=order["building"])})
            print("%s: direction-order · building → testing · %s" % (
                SAY, derive_direction("building", "testing", swapped)))
            return 0
        import os
        import tempfile
        from loop_witness import remove_tree, run_fixture_git, write_fixture_files
        scratch = pathlib.Path(tempfile.mkdtemp(prefix="loop-table-"))
        envs = {"leak": {"MEMORY_ROOT": "elsewhere", "PHASES_EXTRA": "BOGUS"}}
        try:
            for name, conf in (("extra", 'PHASES_EXTRA="STAGING"\n'), ("broken", "exit 3\n"), ("bare", None),
                               ("leak", "# a conf that sets neither MEMORY_ROOT nor PHASES_EXTRA\n")):
                (scratch / name).mkdir()
                run_fixture_git(scratch / name, "init", "-q", "--template=")
                if conf is not None:
                    write_fixture_files(scratch / name, {".unattended.conf": conf})
            return run_selftest_cases(run_table_case, cases, "%s: table selftest" % SAY)
        finally:
            remove_tree(scratch)
    try:
        data, where = read_definition(KIT)
    except LoopError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    if not data.get("transition"):
        print("%s: unarmed · %s holds no [[transition]] row: no move is admitted" % (SAY, where))
        return 2
    facts = {}
    for fact in getattr(args, "fact", None) or []:
        k, eq, v = fact.partition("=")
        if not (k and eq):
            ap.error("--fact takes k=v, and %r is not" % fact)
        facts[k] = v
    if args.verb == "phase":
        try:
            phase_map = read_phase_map(data, where)
        except LoopError as e:
            print("%s: refused · %s" % (SAY, e))
            return 1
        # absent --extra is None: the population is read from the working directory's tree (TOOL-dDeclaredLoop-70)
        extra = None if args.extra is None else set(args.extra.split())
        mapped = {r.get("phase") for r in phase_map["rows"]}
        try:
            state, step = derive_phase_position(args.phase_from, facts, phase_map, extra)
            said = "phase %s · state %s · step %s" % (args.phase_from, state, step)
            if args.phase_from not in mapped:
                said += " · adopter phase"
            if args.to is not None:
                to_step = derive_phase_position(args.to, {}, phase_map, extra)[1]
                said += " · to %s%s · crosses %s" % (
                    args.to, " · adopter phase" if args.to not in mapped else "",
                    " ".join(derive_crossed_exits(step, to_step, phase_map["steps"])) or "none")
        except LookupError as e:
            print("refused — %s" % e)
            return 1
        except LoopError as e:
            print("%s: refused · %s" % (SAY, e))
            return 1
        print(said)
        return 0
    if args.verb == "move":
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
        print("move — %s · %s → %s · %s%s%s" % (
            args.level, args.state, to, args.item, " · stand-in %s" % owner if owner else "",
            " · %s" % derive_direction(args.state, to, tables) if args.level == "build" else ""))
        return 0
    try:
        items = read_items(KIT)
        read_transition_rows(data, where)
        read_stand_ins(data, where)
        phase_map = read_phase_map(data, where)
    except LoopError as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    extra = ()
    if args.plant:
        core = [r.get("phase") for r in phase_map["rows"] if not any(q in r for q in QUALIFIERS)]
        print("%s: fixture · plant %s · %s" % (SAY, args.plant, PLANTS[args.plant][0]))
        write_table_plant(args.plant, data)
    else:
        try:
            core = read_core_registries(KIT, ("PHASES_CORE",))["PHASES_CORE"]
        except LookupError:
            core = None
        try:   # TOOL-dDeclaredLoop-67 S23: the adopter phases the driver's conf declares, joined beside the core
            extra = read_driver_conf(".", ("PHASES_EXTRA",)).get("PHASES_EXTRA", "").split()
        except LoopError as e:
            print("%s: refused · %s" % (SAY, e))
            return 1
    lines, refusals = check_transition_tables(data, where, items)
    tables = read_transition_rows(data, where)
    more = check_phase_rows(read_phase_map(data, where), core, tables["states"].get("build", []), tables["terminal"],
                            extra)
    lines, refusals = lines + more[0], refusals + more[1]
    for line in lines:
        print(line)
    for why in refusals:
        print("%s: refused · %s" % (SAY, why))
    return 1 if refusals else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
