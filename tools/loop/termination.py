#!/usr/bin/env python3
"""termination.py — the static termination check on every composition a build can run, at the push and at
each step boundary that applies a build's change (TOOL-dDeclaredLoop-33).

    python termination.py check [--build <slug>] [--selftest]
    python termination.py --fixture --plant <case>

THE COMPOSITION. `read_termination_inputs(root, build=None)` reads one composition. Without a build it is
gov's at HEAD: the definition beside this file, its build table spliced with the composed repository
stages (`splice.py`'s `derive_spliced_table`), the composed items (`loop_items.py`'s
`read_composed_items`) and the programs `loop_lib.py`'s `check_program` returns, with `gov`, the
definition's own item and build rows and the builds the policy kit's `derive_landed_owners` reads landed.
With a build it is that build's at its pin (`composition.py`'s `read_step_composition` over
`loop_transition.py`'s `read_transitions`): its items through `position.py`'s `read_build_items`, its
stages at the pin with the stages its scenarios activate and its applied stage changes, and its flow rows
through `adapt.py`'s `read_flow_rows`. A program `check_program` refuses is a refusal of the read.

THE RULES. `check_termination(composition)` runs one function per rule and returns every finding,
`(rule, subject, why)`:

    terminal   every state of a level reaches the level's own terminal set, by reverse reachability over
               its rows, a row into @prior or @reentry reaching every open state; an empty state set is a
               finding.
    reachable  one walk from every program's entries, its items with no needs, along every route to a
               declared item and along a need only between two items of one program, reaches every item.
    counted    with every set-aside edge left out, the build table and the item routes between declared
               items are acyclic; each cycle `scan_cycles` finds is one finding unless a pending row
               names it. Set aside: an ending row, a row into @prior or @reentry, an owner edge, a
               counted build row (backward by `derive_direction`, not `draws = "none"`), an item route
               whose outcome the item's `draws` maps to a cause of `budget.py`'s `CAUSES`, a route into
               another step's item whose build row is set aside, and an item's route to itself on an
               outcome its `waits` lists.
    wait       an item with `waits` or an owner actor declares `deadline`, whole hours or `policy.<key>`
               naming a catalogue row of a `DEADLINE_TYPES` type, and `on-deadline`, an outcome outside
               `waits`, unless a pending `wait` row names it. Over gov's composition alone, a pending row
               is stale once its build has landed, its item declares its deadline or is gone, or its cycle
               no longer holds in gov's counted graph.
    raise      a build's state row reading `applied · class loosening` names a disposition.
    decline    a build's state row reading `held · class loosening` recommends `decline`.

THE PENDING LIST, `termination-pending.txt` beside this file, shrink-only: `wait · <item> · <deadline key>
· <build that lands it>` and `cycle · <node> -> ... -> <node> · <owner build of the re-entering item>`,
each cycle rotated as `scan_cycles` rotates it. Staleness is graded only by `check` without `--build`;
every other composition reads the rows only to excuse the cycles and waits they name.

`check` prints one composition's header, `raise` and `decline` as `0 build(s)` over
gov's, the pending counts, the value `flow.wait-ceiling` resolves to, each finding as `loop: termination ·
<rule> · <subject> · <why>` and the summary; exit 0 clean, 1 on a finding, 2 where a read is refused or a
kit does not resolve, never 0. `check --selftest` checks gov's composition and every live build's, a slug
a `Gov-Transition` trailer reachable from HEAD or a transition record names whose newest move enters no
terminal, then runs every plant through `loop_lib.py`'s `run_selftest_cases`. `--fixture --plant <case>`
runs one of `PLANTS`, each made in memory over the definition's own rows but `deadline-patch` and
`boundary`, which build a scratch repository; it prints its observations and closes `loop: fixture ·
<case> · held` or `· MISSED <why>`, exit 0 held, 1 missed, 2 where it could not be built.

THE BOUNDARY. `loop_transition.py`'s writer runs `check_termination` over the build's composition at HEAD
after `adapt.py`'s `write_flow_states` writes a state row reading `applied`, and refuses the move on a
finding or a refused read, cutting `RUN.md` back to its length.

WHAT THIS DOES NOT CHECK: that a `draws` or `waits` mark is true, which the acceptance ledger's per-cycle
line answers; the scenario successor chains, `scenario.py`'s `check_scenarios`; the code-level waits outside the
composition, which the kit's README lists; a raise of a policy bound, the policy guard's; a run-time
stall, which no static check sees.
"""
import argparse
import contextlib
import copy
import io
import pathlib
import subprocess
import sys

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from budget import CAUSES  # noqa: E402
from composition import read_composition_at, read_step_composition  # noqa: E402
from loop_items import OVERLAY, read_composed_items, read_composition, render_item_row  # noqa: E402
from loop_lib import (LoopError, check_loop, check_program, derive_outcome_set, read_definition,  # noqa: E402
                      read_item_rows, read_memory_tree, resolve_memory_root, run_selftest_cases, scan_cycles)
from loop_parents import read_policy_kit  # noqa: E402
from loop_table import (DYNAMIC_TO, ENDING_OUTCOMES, derive_direction, derive_from_states,  # noqa: E402
                        read_terminal_set, read_transition_rows)
from loop_transition import TRAILER_KEY, read_transitions  # noqa: E402
from loop_witness import read_git, remove_tree, run_fixture_git, write_fixture_files  # noqa: E402
from position import read_build_items  # noqa: E402
from scenario import read_activated_rows  # noqa: E402
from splice import derive_spliced_table, derive_stage_state, read_split_row  # noqa: E402

SAY = "loop"
LEAD = "%s: termination" % SAY
PENDING = "termination-pending.txt"
SEP = " · "
RULES = ("terminal", "reachable", "counted", "wait", "raise", "decline")
#: The stage the stage plants splice between testing and deploying, and its two items.
FX_STAGE = {"tag": "step.adopter.lint", "after": "step.test", "before": "step.deploy", "exit": "item.adopter.lint.exit"}
FX_RUN, FX_EXIT = "item.adopter.lint.run", "item.adopter.lint.exit"
FX_LOOP = "item.build.adopter.spin"
PLANTS = {"stage-self-loop": "a repository stage whose exit routes pass to transition and retry back to its first item",
          "stage-self-loop-drawn": "the same stage, its retry route under draws = { retry = \"route-back\" }",
          "dead-end": "a build state stuck one row enters, each @open row narrowed to the other open states",
          "unit-dead-end": "a unit state reviewed one row from built enters, and no row leaves",
          "orphan-item": "a build item needing item.test.merge that no route names",
          "empty-states": "a build level declaring no states",
          "wait-no-deadline": "item.build.unit-lease waiting on waiting with no deadline",
          "wait-declared": "the same with deadline policy.flow.wait-ceiling and on-deadline refused",
          "wait-stale": "a pending wait row whose build the planted landed set names, over gov",
          "stale-build": "a pending cycle row over a build's composition whose own rows break the cycle, gov unset",
          "raise-unattended": "a build's applied loosening naming no disposition",
          "raise-released": "the same naming a disposition",
          "raise-held": "the same row held",
          "decline": "a held loosening recommending apply, then decline, then nothing",
          "deadline-patch": "an overlay amending item.build.unit-lease's deadline to 96, in a scratch repository",
          "boundary": "a forward move applying an additive change whose item routes back into itself, then none, "
                      "then the change with no outcomes, in a scratch repository"}


# ------------------------------------------------------------------------------------------ the reads
def read_termination_pending(path=None):
    """The rows of the pending list, `path` or the one beside this file, each `{kind, subject, key, build}`,
    `key` None on a `cycle` row. ValueError naming the line that is no row of either grammar."""
    path = pathlib.Path(path) if path is not None else KIT / PENDING
    rows = []
    for n, line in enumerate(path.read_bytes().decode("utf-8").replace("\r\n", "\n").split("\n"), 1):
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split(SEP)
        if parts[0] == "wait" and len(parts) == 4 and all(parts):
            rows.append({"kind": "wait", "subject": parts[1], "key": parts[2], "build": parts[3]})
        elif parts[0] == "cycle" and len(parts) == 3 and all(parts):
            rows.append({"kind": "cycle", "subject": parts[1], "key": None, "build": parts[2]})
        else:
            raise ValueError("%s line %d is no `wait · <item> · <key> · <build>` or `cycle · <nodes> · <build>` "
                             "row: %r" % (path.name, n, line))
    return rows


def derive_stage_rows(code, payload, lines):
    """The composed stage rows of one stage-kind answer: its rows on 0, none where unarmed on 2, and a
    ValueError naming its first line on a refusal."""
    if code == 2:
        return []
    if code != 0:
        raise ValueError("the stage composition does not read: %s" % (lines[0] if lines else "exit %d" % code))
    return [{k: v for k, v in r.items() if k not in ("origin", "source")} for r in payload["rows"]]


def derive_termination_composition(label, data, where, items, stages, flow, pending, gov=None):
    """One composition (§4 Data model) of `data`, a parsed definition, with the composed `items` and
    `stages`: its states, each spliced stage's state among the build level's, each level's terminal set
    through `read_terminal_set` (TOOL-dDeclaredLoop-54), the step orders, the spliced rows, the items with
    each outcome set resolved, the programs `check_program` returns, `flow`, `pending` and `gov`.
    LoopError where a program does not hold; ValueError, `read_terminal_set`'s, where a level's set is absent."""
    tables = read_transition_rows(data, where)
    tags = [s.get("tag") for s in stages if isinstance(s.get("tag"), str)]
    programs = check_program(dict(data, item=list(items)), where, None, tags)
    members = check_loop(data, where)["dispositions"]
    spliced = [s for s in stages if read_split_row(s, data) is not None]
    states = {level: list(v) for level, v in tables["states"].items()}
    states["build"] = states.get("build", []) + [derive_stage_state(s["tag"]) for s in spliced]
    terminal = {level: read_terminal_set(tables, level) for level in tables["states"]}
    return {"label": label, "states": states, "terminal": terminal,
            "step-order": dict(tables["step-order"]), "rows": derive_spliced_table(spliced, data),
            "items": [dict(r, outcomes=derive_outcome_set(r, members, where)) for r in items],
            "programs": programs, "flow": flow, "pending": pending, "gov": gov}


def read_termination_inputs(root, build=None, moves=None):
    """The composition `check` reads at `root`: gov's at HEAD without `build`, with `gov` set; the build's
    at its pin with it, `moves` its moves newest first where the caller holds them, the step boundary's
    newest the move it records. ValueError or LoopError where a read is refused; LookupError where a kit
    does not resolve."""
    root = pathlib.Path(root).absolute()
    data, where = read_definition(KIT)
    pending = read_termination_pending()
    if build is None:
        items = read_composed_items(root)
        stages = derive_stage_rows(*read_composition(root, "stage"))
        policy, _guard = read_policy_kit()
        import check_policy
        try:
            landed = check_policy.derive_landed_owners(str(root))
        except policy.Refusal as e:
            raise ValueError("the landed builds do not read: %s" % e) from None
        members = check_loop(data, where)["dispositions"]
        gov = {"items": [dict(r, outcomes=derive_outcome_set(r, members, where)) for r in read_item_rows(data, where)],
               "rows": list(data.get("transition", [])), "landed": set(landed)}
        return derive_termination_composition("gov", data, where, items, stages, [], pending, gov)
    from adapt import read_flow_layer, read_flow_rows   # it imports loop_transition, so here
    moves = read_transitions(build, root) if moves is None else moves
    pin, _state = read_step_composition(root, moves)
    items = read_build_items(root, build, moves, pin)
    placed = moves[0].get("scenario") if moves else None
    activated = read_activated_rows(root, pin, placed.split("+")).get("kind.stage", []) if placed else []
    layer = read_flow_layer(root, build, "stage")
    stages = derive_stage_rows(*read_composition_at(root, pin, "stage", (activated + layer) or None))
    return derive_termination_composition("%s@%s" % (build, pin[:8]), data, where, items, stages,
                                          read_flow_rows(root, build), pending)


def read_deadline_keys():
    """`{key: type}` of each catalogue row the policy kit's `derive_bounds` selects whose type is one of its
    `DEADLINE_TYPES`. LookupError where the policy kit does not resolve; ValueError where its catalogue does
    not read."""
    policy, _guard = read_policy_kit()
    try:
        rows = policy.load_catalogue(pathlib.Path(policy.__file__).parent)
    except (OSError, ValueError) as e:
        raise ValueError("the policy catalogue does not read: %s" % e) from None
    return {r["name"]: r["allowed"]["type"] for r in policy.derive_bounds(rows)
            if r["allowed"].get("type") in policy.DEADLINE_TYPES}


def read_live_builds(root):
    """The slugs a `Gov-Transition` trailer reachable from HEAD or a transition record names whose newest
    move enters no terminal, sorted."""
    read_memory_tree("commit_trailers.py")
    from commit_trailers import read_commits
    slugs = set()
    for c in read_commits(str(root), ["--grep=^%s: " % TRAILER_KEY, "HEAD"], [TRAILER_KEY]):
        for value in c["trailers"][TRAILER_KEY]:
            slugs.update(p[len("build="):] for p in (value or "").split(SEP) if p.startswith("build="))
    builds = pathlib.Path(root, resolve_memory_root(root), "builds")
    slugs.update(p.parent.parent.name for p in builds.glob("*/build/*-transition-*.md"))
    terminal = read_transition_rows(*read_definition(KIT))["terminal"]
    return sorted(s for s in slugs if (read_transitions(s, root) or [{"to": terminal[0]}])[0].get("to") not in terminal)


# ------------------------------------------------------------------------------------------ the rules
def check_owner_actor(row):
    """Whether an item row's actor is the owner: `owner` or `owner:<name>`."""
    actor = (row or {}).get("actor")
    return isinstance(actor, str) and (actor == "owner" or actor.startswith("owner:"))


def render_cycle(cycle):
    """One cycle as a pending row spells it: its nodes, the first again last, joined by ` -> `."""
    return " -> ".join(tuple(cycle) + (cycle[0],))


def render_finding(finding):
    """`<rule> · <subject> · <why>`."""
    return SEP.join(finding)


def derive_row_class(row, state, composition, items):
    """The class of one build row moving out of `state`: `ending`, `dynamic`, `owner`, `counted`, or None
    for an edge the counted rule keeps."""
    if row.get("outcome") in ENDING_OUTCOMES:
        return "ending"
    if row.get("to") in DYNAMIC_TO:
        return "dynamic"
    if check_owner_actor(items.get(row.get("item"))):
        return "owner"
    tables = {"step-order": composition["step-order"], "terminal": composition["terminal"]["build"]}
    if derive_direction(state, row.get("to"), tables) == "backward" and row.get("draws") != "none":
        return "counted"
    return None


def derive_counted_graphs(composition, view=None):
    """`(build edges, item edges)`, each `{node: {node}}`, of the composition's build table and its item
    routes between declared items, every set-aside edge left out (§4 The edges). `view`, where given,
    supplies the `items` and `rows` read instead, gov's own over the composition's states."""
    view = view or composition
    items = {r.get("tag"): r for r in view["items"]}
    rows = [r for r in view["rows"] if r.get("level") == "build"]
    open_states = composition["states"].get("build", [])
    build = {}
    for row in rows:
        for state in derive_from_states(row, open_states):
            if derive_row_class(row, state, composition, items) is None:
                build.setdefault(state, set()).add(row.get("to"))
    item_edges = {}
    for tag, row in items.items():
        if check_owner_actor(row):
            continue
        draws, waits = row.get("draws") or {}, row.get("waits") or []
        for outcome, target in (row.get("routes") or {}).items():
            if target not in items or draws.get(outcome) in CAUSES or (target == tag and outcome in waits):
                continue
            if items[target].get("step") != row.get("step"):
                fired = [(r, s) for r in rows if (r.get("item"), r.get("outcome")) == (tag, outcome)
                         for s in derive_from_states(r, open_states)]
                if fired and all(derive_row_class(r, s, composition, items) for r, s in fired):
                    continue
            item_edges.setdefault(tag, set()).add(target)
    return build, item_edges


def check_terminal(composition):
    """The `terminal` rule: each state of a level declaring a terminal set from which no row path reaches
    one, by reverse reachability, and an empty state set."""
    out = []
    for level, terminal in composition["terminal"].items():
        states = composition["states"].get(level) or []
        if not states:
            out.append(("terminal", level, "the level declares the empty state set, which no walk grades and "
                                           "which never passes"))
            continue
        rows = [r for r in composition["rows"] if r.get("level") == level]
        good, grew = set(terminal), True
        while grew:
            grew = False
            for row in rows:
                ahead = states if row.get("to") in DYNAMIC_TO else [row.get("to")]
                if any(t in good for t in ahead):
                    for state in derive_from_states(row, states):
                        if state not in good:
                            good.add(state)
                            grew = True
        out += [("terminal", "%s %s" % (level, s), "no row path from it reaches a terminal: %s" % " ".join(terminal))
                for s in states if s not in good]
    return out


def check_reachable(composition):
    """The `reachable` rule: each item of a program that one walk from every program's entries misses, the
    walk following every route to a declared item and a need only within one program."""
    items = {r.get("tag"): r for r in composition["items"]}
    program_of = {t: p for p, tags in composition["programs"].items() for t in tags}
    ahead = {t: set() for t in items}
    for tag, row in items.items():
        ahead[tag].update(t for t in (row.get("routes") or {}).values() if t in items)
        for entry in row.get("needs") or []:
            for need in entry if isinstance(entry, list) else [entry]:
                if need in items and program_of.get(need) == program_of.get(tag):
                    ahead[need].add(tag)
    seen = {t for t, r in items.items() if not r.get("needs")}
    todo = list(seen)
    while todo:
        for nxt in ahead[todo.pop()]:
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return [("reachable", t, "no walk from a program's entry reaches it: no route names it, and no need inside "
                             "the program %s leads to it" % p)
            for p, tags in composition["programs"].items() for t in tags if t not in seen]


def check_counted(composition):
    """The `counted` rule: one finding per cycle of the build table or the item routes that passes no
    set-aside edge and no pending `cycle` row names."""
    excused = {p["subject"] for p in composition["pending"] if p["kind"] == "cycle"}
    out = []
    for label, edges in zip(("build table", "item routes"), derive_counted_graphs(composition)):
        for cycle in scan_cycles(edges):
            if render_cycle(cycle) not in excused:
                out.append(("counted", render_cycle(cycle), "a cycle of the %s passing no counted edge, owner "
                                                            "edge, ending, dynamic return or declared wait" % label))
    return out


def check_stale_rows(composition):
    """The pending rows gov's definition no longer owes, graded over `composition["gov"]` alone: a `wait`
    row whose build has landed or whose item declares its deadline or is gone, and a `cycle` row whose
    cycle gov's counted graph no longer holds."""
    gov = composition["gov"]
    items = {r.get("tag"): r for r in gov["items"]}
    held = {render_cycle(c) for edges in derive_counted_graphs(composition, gov) for c in scan_cycles(edges)}
    out = []
    for p in composition["pending"]:
        row = "%s %s" % (p["kind"], p["subject"])
        if p["build"] in gov["landed"]:
            out.append(("wait", row, "stale: its build %s has landed; delete the row" % p["build"]))
        elif p["kind"] == "wait" and p["subject"] not in items:
            out.append(("wait", row, "stale: gov declares no item %s; delete the row" % p["subject"]))
        elif p["kind"] == "wait" and "deadline" in items[p["subject"]]:
            out.append(("wait", row, "stale: the item declares its deadline; delete the row"))
        elif p["kind"] == "cycle" and p["subject"] not in held:
            out.append(("wait", row, "stale: gov's counted graph no longer holds the cycle; delete the row"))
    return out


def check_wait(composition):
    """The `wait` rule: each item waiting on another party, by `waits` or an owner actor, that declares no
    `deadline` of a whole number of hours or `policy.<key>` of a deadline type, or no `on-deadline` of its
    outcomes outside `waits`, unless a pending `wait` row names it; and, over gov, each stale pending row."""
    excused = {p["subject"] for p in composition["pending"] if p["kind"] == "wait"}
    keys, out = None, []
    for row in composition["items"]:
        tag, waits, outcomes = row.get("tag"), row.get("waits"), row.get("outcomes") or []
        if (not waits and not check_owner_actor(row)) or tag in excused:
            continue
        if waits is not None and not (isinstance(waits, list) and all(w in outcomes for w in waits)):
            out.append(("wait", tag, "waits %r is no list of its outcomes: %s" % (waits, " ".join(outcomes))))
            continue
        waits, deadline = waits or [], row.get("deadline")
        if deadline is None:
            out.append(("wait", tag, "it waits on another party and declares no deadline, whole hours or "
                                     "policy.<key>"))
        elif not (isinstance(deadline, int) and not isinstance(deadline, bool) and deadline >= 0):
            keys = read_deadline_keys() if keys is None else keys
            key = deadline[len("policy."):] if isinstance(deadline, str) and deadline.startswith("policy.") else None
            if key not in keys:
                out.append(("wait", tag, "deadline %r is of the wrong type: whole hours, or policy.<key> naming a "
                                         "catalogue row of a deadline type" % (deadline,)))
        if row.get("on-deadline") not in [o for o in outcomes if o not in waits]:
            out.append(("wait", tag, "on-deadline %r is no outcome of its set outside waits %s" % (
                row.get("on-deadline"), " ".join(waits) or "none")))
    return out + (check_stale_rows(composition) if composition.get("gov") else [])


def check_raise(composition):
    """The `raise` rule: each state row of the build reading `applied · class loosening` that names no
    disposition, a loosening applied unattended."""
    return [("raise", r["tag"], "an applied loosening names no disposition, so it was applied without the "
                                "owner's release")
            for r in composition["flow"] for s in r["states"]
            if (s["state"], s["class"]) == ("applied", "loosening") and not s.get("disposition")]


def check_decline(composition):
    """The `decline` rule: each state row of the build reading `held · class loosening` that recommends
    anything but `decline`, or nothing."""
    return [("decline", r["tag"], "a held loosening recommends %s, not decline" % (s.get("recommend") or "nothing"))
            for r in composition["flow"] for s in r["states"]
            if (s["state"], s["class"]) == ("held", "loosening") and s.get("recommend") != "decline"]


def check_termination(composition):
    """Every finding of the six rules over one composition, in `RULES` order, each `(rule, subject, why)`."""
    return [f for check in (check_terminal, check_reachable, check_counted, check_wait, check_raise, check_decline)
            for f in check(composition)]


# ------------------------------------------------------------------------------------------ the verb
def print_termination(composition):
    """Print one composition's check, each level walked against its own terminal set: its header, the
    build rules' population over gov, the pending counts, each finding and the summary. -> its findings."""
    found = check_termination(composition)
    label = composition["label"]
    print("%s · %s · %d build state(s) · %d row(s) · %d item(s) · %d program(s)" % (
        LEAD, label, len(composition["states"].get("build", [])), len(composition["rows"]),
        len(composition["items"]), len(composition["programs"])))
    for rule in ("raise", "decline"):
        print("%s · %s · %s" % (LEAD, rule, "0 build(s)" if label == "gov" else "1 build(s) · %d flow row(s)" % len(
            composition["flow"])))
    kinds = [p["kind"] for p in composition["pending"]]
    print("%s · pending · %d wait row(s) · %d cycle row(s)" % (LEAD, kinds.count("wait"), kinds.count("cycle")))
    for f in found:
        print("%s · %s" % (LEAD, render_finding(f)))
    print("%s · %s · %d finding(s)" % (LEAD, label, len(found)))
    return found


def run_check(root, build=None, live=False):
    """`check` over `root`: gov's composition, or `build`'s, and with `live` every live build's after gov's.
    -> 0 clean, 1 a finding, 2 a refused read."""
    try:
        policy, _guard = read_policy_kit()
    except LookupError as e:
        print("%s · unarmed · %s" % (LEAD, e))
        return 2
    try:
        ceiling = policy.resolve("flow.wait-ceiling", str(root), "HEAD").value
        slugs = [build] if build else [None] + (read_live_builds(root) if live else [])
        print("%s · wait · flow.wait-ceiling %s hour(s) · %d live build(s) checked" % (
            LEAD, ceiling, len([s for s in slugs if s])))
        rc = 0
        for slug in slugs:
            rc = max(rc, 1 if print_termination(read_termination_inputs(root, slug)) else 0)
        return rc
    except LookupError as e:
        print("%s · unarmed · %s" % (LEAD, e))
    except (ValueError, OSError, subprocess.SubprocessError, policy.Refusal) as e:
        print("%s · unreadable · %s" % (LEAD, e))
    return 2


# ------------------------------------------------------------------------------------------ the plants
def read_plant_base():
    """`(data, where, items)`: the definition beside this file, parsed, and its own item rows, copied."""
    data, where = read_definition(KIT)
    return data, where, copy.deepcopy(read_item_rows(data, where))


def derive_plant_state(state, klass, recommend=None, disposition=None):
    """One planted flow row of `item.review.cost`'s exclusion holding one state row."""
    return [{"act": "exclude", "tag": "item.review.cost", "change": None, "reason": "the plant",
             "states": [{"state": state, "class": klass, "mode": "additive-recorded", "recommend": recommend,
                         "disposition": disposition}]}]


def run_deadline_patch(misses):
    """The `deadline-patch` plant: `loop_items.py check` in a scratch repository whose overlay amends
    `item.build.unit-lease`'s `deadline` to 96, owed exit 1 naming the field as fixed."""
    from loop_items import build_scratch_tree, run_scratch_check
    top, _sha, pins = build_scratch_tree()
    try:
        write_fixture_files(top, {OVERLAY: render_item_row({
            "tag": "item.build.adopter.lease-deadline", "edges": "amends=item.build.unit-lease@%s" % pins[
                "item.build.unit-lease"], "deadline": 96})})
        run_fixture_git(top, "add", "-A")
        run_fixture_git(top, "commit", "-q", "-m", "the plant deadline-patch")
        rc, _payload, said = run_scratch_check(top)
    finally:
        remove_tree(top)
    hit = next((ln for ln in said if "field deadline" in ln and "fixed" in ln), None)
    print("%s: fixture · loop_items.py check · exit %d · %s" % (SAY, rc, hit or " | ".join(said)[-300:]))
    if rc != 1 or hit is None:
        misses.append("the check exited %d, owed 1 and a line naming the field deadline as fixed" % rc)


def write_boundary_change(top, row):
    """Propose `row`, an `[[item]]` of `FX_LOOP`, as the scratch build's additive flow change and commit it."""
    from adapt import FX_BUILD, FX_ROW, FX_UNIT, write_flow_proposal
    write_fixture_files(top, {FX_ROW: render_item_row(row)})
    write_flow_proposal(top, FX_BUILD, FX_LOOP, "add", FX_UNIT, FX_ROW, "the boundary plant")
    run_fixture_git(top, "add", "-A")
    run_fixture_git(top, "commit", "-q", "-m", "the proposal")


def run_boundary_plant(misses):
    """The `boundary` plant over `adapt.py`'s scratch base: a forward move applying an additive change
    whose item routes back into itself is refused naming the `counted` finding, `RUN.md` keeping its
    length; the move with no change records; the change with no outcomes is refused naming
    `check_program`'s refusal, `RUN.md` keeping its length."""
    import loop_transition
    from adapt import FX_BUILD, FX_MOVES, build_adapt_base, read_run_file
    top, sha = build_adapt_base()
    looping = {"tag": FX_LOOP, "step": "step.build", "actor": "command:spin", "needs": ["item.build.unit-pass"],
               "outcomes": ["again", "clean"], "routes": {"again": FX_LOOP, "clean": "transition"}}
    shapeless = {k: v for k, v in looping.items() if k != "outcomes"}
    try:
        for label, row, owed, needle in (("looping", looping, 2, "counted · %s -> %s" % (FX_LOOP, FX_LOOP)),
                                         ("none", None, 0, "recorded"),
                                         ("no outcomes", shapeless, 2, "carries no outcomes")):
            run_fixture_git(top, "reset", "-q", "--hard", sha)
            run_fixture_git(top, "clean", "-qfdx")
            if row is not None:
                write_boundary_change(top, row)
            run = read_run_file(top, FX_BUILD)
            size = run.stat().st_size
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rc = loop_transition.main(["record", "--build", FX_BUILD, "--root", str(top), *FX_MOVES[0],
                                           "--witness", "HEAD"])
            said = out.getvalue().strip().replace("\n", " | ")
            kept = run.stat().st_size == size
            print("%s: fixture · %s · exit %d · RUN.md %s · %s" % (SAY, label, rc, "kept" if kept else "grew",
                                                                   said[:400]))
            if rc != owed or needle not in said or (owed and not kept):
                misses.append("%s: exit %d, owed %d and a line naming %r%s" % (
                    label, rc, owed, needle, "" if kept or not owed else ", RUN.md cut back"))
    finally:
        remove_tree(top)


def run_termination_plant(case):
    """One plant: -> 0 held, 1 missed, 2 where it could not be built."""
    print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
    misses = []
    try:
        if case == "deadline-patch":
            run_deadline_patch(misses)
        elif case == "boundary":
            run_boundary_plant(misses)
        else:
            data, where, items = read_plant_base()
            pending, stages, flow, gov, label = read_termination_pending(), [], [], None, "gov"
            lease = next(r for r in items if r.get("tag") == "item.build.unit-lease")
            if case.startswith("stage-self-loop"):
                stages = [FX_STAGE]
                items += [{"tag": FX_RUN, "step": FX_STAGE["tag"], "actor": "command:lint", "needs": [],
                           "outcomes": ["done"], "routes": {"done": FX_EXIT}},
                          {"tag": FX_EXIT, "step": FX_STAGE["tag"], "actor": "command:lint", "needs": [FX_RUN],
                           "outcomes": ["pass", "retry"], "routes": {"pass": "transition", "retry": FX_RUN}}]
                if case.endswith("-drawn"):
                    items[-1]["draws"] = {"retry": "route-back"}
            elif case == "orphan-item":
                items.append({"tag": "item.build.orphan", "step": "step.build", "actor": "command:orphan",
                              "needs": ["item.test.merge"], "outcomes": ["done"], "routes": {"done": "transition"}})
            elif case in ("wait-no-deadline", "wait-declared"):
                lease.update({"waits": ["waiting"], "deadline": "policy.flow.wait-ceiling", "on-deadline": "refused"})
                if case == "wait-no-deadline":
                    del lease["deadline"]
            elif case == "wait-stale":
                pending.append({"kind": "wait", "subject": "item.build.ratify", "key": "run.owner-deadline",
                                "build": "dPlanted"})
                gov = {"items": copy.deepcopy(items), "rows": list(data.get("transition", [])), "landed": {"dPlanted"}}
            elif case == "stale-build":
                research = next(r for r in items if r.get("tag") == "item.plan.research")
                research["routes"] = {"answered": "item.plan.place"}
                label = "tPlant@0123abcd"
            elif case.startswith("raise-") or case == "decline":
                label = "tPlant@0123abcd"
                flow = {"raise-unattended": derive_plant_state("applied", "loosening"),
                        "raise-released": derive_plant_state("applied", "loosening", None, "2026-01-01-disposition"),
                        "raise-held": derive_plant_state("held", "loosening", "decline")}.get(case, [])
            comp = derive_termination_composition(label, data, where, items, stages, flow, pending, gov)
            if case == "dead-end":
                comp["states"]["build"].append("stuck")
                for row in comp["rows"]:
                    if "@open" in (row.get("from") or []):
                        row["from"] = [s for s in comp["states"]["build"] if s != "stuck"]
                comp["rows"].append({"level": "build", "from": ["planning"], "item": "item.plan.exit",
                                     "outcome": "recorded", "to": "stuck", "witness": "the plant"})
            elif case == "unit-dead-end":
                comp["states"]["unit"].append("reviewed")
                comp["rows"].append({"level": "unit", "from": ["built"], "item": "item.test.exit",
                                     "outcome": "recorded", "to": "reviewed", "witness": "the plant"})
            elif case == "empty-states":
                comp["states"]["build"] = []
            runs = [comp]
            if case == "decline":
                runs = [dict(comp, flow=derive_plant_state("held", "loosening", word)) for word in ("apply", "decline", None)]
            found = []
            for one in runs:
                got = print_termination(one)
                print("%s: fixture · %s · check exit %d" % (SAY, case, 1 if got else 0))
                found.append(got)
            check_plant_found(case, found, misses)
    except (subprocess.CalledProcessError, OSError, ValueError, LookupError, KeyError, StopIteration) as exc:
        print("%s: fixture · %s · UNARMED · the plant could not be built: %s %s" % (
            SAY, case, exc, (getattr(exc, "stderr", "") or "").strip()[:300]))
        return 2
    print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
    return 1 if misses else 0


def check_plant_found(case, found, misses):
    """Append to `misses` each way the in-memory plant `case`'s findings, `found` one list per run, miss
    what its criterion owes."""
    first = found[0]
    rules = [f[0] for f in first]
    owed = {
        "stage-self-loop": rules == ["counted"] and first[0][1] == render_cycle((FX_EXIT, FX_RUN)),
        "stage-self-loop-drawn": not first,
        "dead-end": [f[:2] for f in first if f[0] == "terminal"] == [("terminal", "build stuck")],
        "unit-dead-end": [f[:2] for f in first if f[0] == "terminal"] == [("terminal", "unit reviewed")],
        "orphan-item": [f[:2] for f in first if f[0] == "reachable"] == [("reachable", "item.build.orphan")],
        "empty-states": ("terminal", "build") in [f[:2] for f in first],
        "wait-no-deadline": ("wait", "item.build.unit-lease") in [f[:2] for f in first],
        "wait-declared": not [f for f in first if f[0] == "wait"],
        "wait-stale": any(f[0] == "wait" and "dPlanted" in f[2] and "stale" in f[2] for f in first),
        "stale-build": not [f for f in first if "stale" in f[2]],
        "raise-unattended": [f[:2] for f in first] == [("raise", "item.review.cost")],
        "raise-released": not first,
        "raise-held": not first,
        "decline": [len(f) for f in found] == [1, 0, 1] and found[0][0][0] == found[2][0][0] == "decline",
    }[case]
    if not owed:
        misses.append("the findings %s are not what the plant owes" % "; ".join(
            "[%s]" % ", ".join(render_finding(f) for f in got) for got in found)[:600])


def run_selftest(root):
    """`check` over gov's composition and every live build's, then every plant: -> 0 when all hold."""
    rc = run_check(root, live=True)
    cases = [(c, ["--fixture", "--plant", c], 0, "%s: fixture · %s · held" % (SAY, c), "") for c in PLANTS]
    plants = run_selftest_cases(main, cases, "%s · selftest" % LEAD)
    return rc or plants


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
        return run_termination_plant(argv[2])
    if argv[:1] == ["check"]:
        ap = argparse.ArgumentParser(prog="termination.py check", description="the static termination check")
        ap.add_argument("--build")
        ap.add_argument("--selftest", action="store_true")
        args = ap.parse_args(argv[1:])
        rc, top = read_git(".", "rev-parse", "--show-toplevel")
        root = pathlib.Path(top if rc == 0 and top else ".").absolute()
        if args.selftest and args.build:
            print("usage: --selftest checks gov's composition and every live build's, so it takes no --build",
                  file=sys.stderr)
            return 2
        return run_selftest(root) if args.selftest else run_check(root, args.build)
    print("usage: python termination.py check [--build <slug>] [--selftest] | --fixture --plant <%s>" % "|".join(
        PLANTS), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
