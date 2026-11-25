#!/usr/bin/env python3
"""adapt.py — a build's own flow changes, proposed by its role, applied at its next step boundary, and its
walked path held to its composition (TOOL-dDeclaredLoop-28).

    python adapt.py propose --build <slug> --flow <row tag> --act add|amend|exclude|supersede --item <unit id>
                            [--row <path>] --reason <r> [--ban <flag>]
    python adapt.py --fixture --plant <case>
    python adapt.py --selftest

THE PROPOSAL. `propose` (`write_flow_proposal`) runs at the repository's top level, the unattended
driver's `--rescope <slug> --flow <row tag>` form its adapter. It refuses, exit 1 and writing nothing, a
field holding an LF, a CR or the separator ` · `, or spelling `--ban`'s value; a `--flow` that is no tag
and an `--item` that is no unit id; `--row` absent on `add`, `amend` or `supersede`, or given on
`exclude`; a row file that is not exactly one array of one table, `[[<kind>]]`, whose `tag` is `--flow`;
an act the row's `edges` key disagrees with, an `add` holding none, an `amend` `amends=<gov tag>@<hash8>`
and a `supersede` `supersedes=<gov tag>@<hash8>`; and a build with no `RUN.md`. An `add`, `amend` or
`supersede` writes one change record through the memory-tree kit's `write_change`, `Unit` the row's tag,
`Action` `add`, `Before` `none`, `After` `<tag>@<hash8>` by `policy_edit.py`'s `derive_blob_pin` over the
row's text, `Mark` `semantic`, `Proof` `none — flow proposal`, `Caused-by` the unit, its lines the row's
text in a TOML fence, and stages it. Every act then appends one LF-ended row to the build's `RUN.md`:

    <ts> rescope · flow <act> <row tag>[ · change <record stem>] · reason <r>

and prints `unchanged`, exit 0, where a row of the same act, tag, reason and pin is already there.

THE CLASS. `derive_change_class(act, operations)` reads `additive` for an `add` and for an `amend` whose
every operation the composition's `operations` lists for the row reads `narrows`; `loosening` for an
`exclude`, a `supersede`, and an `amend` with any operation read `widens`. Never typed by the proposer.

THE BOUNDARY. `loop_transition.py`'s writer runs `write_flow_states(root, build, mode)` on a forward or
backward move, before any record is written, `mode` the value `flow.adapt` resolves to at HEAD through the
policy kit (`read_adapt_mode`). A pending row, one no state row follows or whose newest state row reads
`held`, is composed first through `loop_items.py`'s `read_composition` with its kind and, on `--rows -`, the
build's layer plus the row: an answer other than 0, a fence the record's `After` pin does not match, or a
kind the verb answers unarmed is `refused · class none`. Then `off` refuses every change, a held row is
released by the newest disposition record whose `Item` is its tag and whose stem no state row of that tag
names, `continue` applying it and `none` refusing it, under `additive-recorded` an additive change is
`applied` and a loosening one `held`, and under `owner-approves` every change is `held`. Each answer is one
row appended to `RUN.md`, which rides the move's commit:

    <ts> rescope · flow-state <row tag> · applied|held|refused · class <class> · flow.adapt <value>[ · recommend decline][ · disposition <record stem>]

A held loosening's row recommends the decline, which the termination check's `decline` rule reads, and
an applied state row is followed by that check over the build's composition (TOOL-dDeclaredLoop-33).

THE LAYER. `read_flow_layer(root, build, kind)` answers the build's applied changes of `kind` as the
elements of the `compose --kind <kind> --rows -` array: each applied record's fenced row, oldest first, its
`source` the record's stem, then `{"exclude": "<tag>"}` per applied exclusion of a `kind` tag. `position.py`
appends it to the item rows a build's scenarios activate, so a held, refused or pending row never reaches
the position.

THE PATH. On a forward move the writer runs `write_path_orders`: with the driver's hand-over in
`GOV_POSITION_STATES` it reads `position.py`'s `derive_position`, and `derive_path_deviations(pos, state)`
answers, where the position's step is the step of the move's from-state, a `skip` per item of that step
the engine reads `unheld` but the step's exit, which this move witnesses, and an `extra` per tag a move out
of that state named that the composition at the pin lacks. Each files one `flow-deviation` order through
`composition.py`'s `write_loop_order`, printed `loop: order · <path>`, and one `loop: path · <build> ·
<step> · <n> unread` line counts the items whose witness the engine does not read, never a skip. Where the
hand-over is unset, the position does not read or its step is another, the line reads `loop: path ·
<build> · unread — <why>` and the move records.

`--fixture --plant <case>` runs one plant over `composition.py`'s scratch base, `loop_items.py`'s
`build_scratch_tree` with the build `tFix`, its README, one spec and `.memory-tree.conf` naming its family,
and a `RUN.md`; `--selftest` runs every plant through `loop_lib.py`'s `run_selftest_cases` over one base,
reset per plant. Each prints its observations and closes `loop: fixture · <case> · held` or `· MISSED
<why>`. The cases are `PLANTS`. Exit 0 held, 1 missed, 2 where the scratch could not be built.

WHAT THIS DOES NOT CHECK: a raise of a loop bound, which the termination check reads, `termination.py`
beside this file; that a disposition
record was written by the owner, which its channel states; a `role` row, whose kind the compose verb
answers unarmed until the roles kit registers a schema, so its boundary refuses it; a witness the position
engine does not read, which stays `unread`; and a build's `stage` layer beyond the boundary's compose.
"""
import argparse
import datetime
import os
import pathlib
import re
import subprocess
import sys
import tomllib

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_items import read_composition  # noqa: E402
from loop_lib import read_definition, read_memory_tree, resolve_memory_root, run_selftest_cases  # noqa: E402
from loop_parents import read_policy_kit  # noqa: E402
from loop_witness import read_git, remove_tree, run_fixture_git, write_fixture_files  # noqa: E402
from policy_edit import derive_blob_pin  # noqa: E402

SAY = "loop"
KEY = "flow.adapt"
MODES = ("additive-recorded", "owner-approves", "off")
ACTS = ("add", "amend", "exclude", "supersede")
#: The `edges` type each record act's row carries; an `add` carries none.
EDGE_OF = {"add": None, "amend": "amends", "supersede": "supersedes"}
SEP = " · "
TAG = re.compile(r"[a-z0-9][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+")
UNIT_ID = re.compile(r"[A-Za-z]+-[A-Za-z0-9]+-\d+")
FLOW_ROW = re.compile(r"^\S+ rescope · flow (add|amend|exclude|supersede) (\S+)(?: · change (\S+))? · reason (.*)$")
STATE_ROW = re.compile(r"^\S+ rescope · flow-state (\S+) · (applied|held|refused) · class (\S+) · flow\.adapt (\S+)"
                       r"(?: · recommend (\S+))?(?: · disposition (\S+))?$")
FENCE = ("```toml", "```")
ORDER_KIND = "flow-deviation"
HANDOVER = "GOV_POSITION_STATES"
FX_BUILD, FX_UNIT = "tFix", "TOOL-tFix-1"
FX_ADD, FX_EXCLUDE = "item.build.adopter.lint-pass", "item.review.cost"
FX_ROW = "flow-row.toml"
PLANTS = {"additive": "an add of item.build.adopter.lint-pass under additive-recorded, then a forward move",
          "owner-approves": "the same under owner-approves, a move, a continue disposition, a second move",
          "off": "the same under off, then a move",
          "loosening": "an exclude of item.review.cost under additive-recorded, a move, a continue disposition, a "
                       "second move",
          "unrecorded-skip": "a forward move out of building with the hand-over set and item.build.acceptance unheld",
          "act-mismatch": "propose --act add with a row whose edges amends a gov row",
          "unit-row": "the flow row and the unit row rescope · item add FIX-dAdapt-2 in one RUN.md",
          "mid-step": "an additive proposal, then a position read before any move"}
#: The moves the plants record, each an argv tail for `record` before its witness.
FX_MOVES = (("--from", "planning", "--item", "item.plan.exit", "--outcome", "recorded"),
            ("--from", "designing", "--item", "item.design.exit", "--outcome", "recorded"),
            ("--from", "building", "--item", "item.build.exit", "--outcome", "recorded"))


class Refused(ValueError):
    """A proposal refused at the write boundary: exit 1, nothing written; a row file or fence that does not
    read, wherever it is read."""


# ------------------------------------------------------------------------------------------ the reads
def read_adapt_mode(root):
    """The value `flow.adapt` resolves to at HEAD of `root`. ValueError naming the key on a policy refusal or
    a value outside `MODES`; LookupError where the policy kit does not resolve."""
    policy, _guard = read_policy_kit()
    try:
        value = policy.resolve(KEY, str(root), "HEAD").value
    except policy.Refusal as e:
        raise ValueError("%s does not resolve at HEAD: %s" % (KEY, e)) from None
    if value not in MODES:
        raise ValueError("%s reads %r, none of %s" % (KEY, value, ", ".join(MODES)))
    return value


def read_run_file(root, build):
    """The path of `build`'s run-state file under `root`, whether or not it exists."""
    return pathlib.Path(root, resolve_memory_root(root), "builds", build, "RUN.md")


def read_flow_rows(root, build):
    """The build's flow rows in `RUN.md` order, each `{act, tag, change, reason, states}`, `states` the state
    rows that follow it for its tag, each `{state, class, mode, recommend, disposition}`; a state row belongs to the
    newest flow row of its tag above it. `[]` where the build has no `RUN.md`."""
    run = read_run_file(root, build)
    if not run.is_file():
        return []
    rows = []
    for ln in run.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n").split("\n"):
        m = FLOW_ROW.match(ln)
        if m:
            rows.append({"act": m[1], "tag": m[2], "change": m[3], "reason": m[4], "states": []})
            continue
        s = STATE_ROW.match(ln)
        owner = next((r for r in reversed(rows) if s and r["tag"] == s[1]), None)
        if owner is not None:
            owner["states"].append({"state": s[2], "class": s[3], "mode": s[4], "recommend": s[5],
                                    "disposition": s[6]})
    return rows


def read_pending_rows(root, build):
    """The flow rows no state row follows or whose newest state row reads `held`."""
    return [r for r in read_flow_rows(root, build) if not r["states"] or r["states"][-1]["state"] == "held"]


def read_fenced_row(root, build, stem):
    """`(kind, row, text, after)` of the change record `stem` of `build`: the one `[[<kind>]]` table its TOML
    fence holds, the fence's text LF-joined, and its `After` field. ValueError naming the record where it
    does not read."""
    path = pathlib.Path(root, resolve_memory_root(root), "builds", build, "build", "%s.md" % stem)
    if not path.is_file():
        raise ValueError("the change record %s is no file of %s's build folder" % (stem, build))
    lines = path.read_bytes().decode("utf-8", "replace").replace("\r\n", "\n").split("\n")
    after = next((ln.partition(":** ")[2].strip() for ln in lines if ln.startswith("- **After:** ")), None)
    if FENCE[0] not in lines or FENCE[1] not in lines[lines.index(FENCE[0]) + 1:]:
        raise ValueError("the change record %s holds no %s fence" % (stem, FENCE[0]))
    start = lines.index(FENCE[0]) + 1
    body = lines[start:lines.index(FENCE[1], start)]
    text = "\n".join(body) + "\n"
    kind, row = read_proposal_row(text, None, stem)
    return kind, row, text, after


def read_proposal_row(text, tag, where):
    """`(kind, row)` of a row file's text: exactly one array of one table, `[[<kind>]]`, whose `tag` is `tag`
    where one is given. Refused naming `where` otherwise."""
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError as e:
        raise Refused("the row %s is no TOML: %s" % (where, e)) from None
    tables = [(k, v) for k, v in data.items()]
    if len(tables) != 1 or not isinstance(tables[0][1], list) or len(tables[0][1]) != 1 \
            or not isinstance(tables[0][1][0], dict):
        raise Refused("the row %s holds %s, not exactly one array of one table [[<kind>]]" % (
            where, ", ".join(k for k, _v in tables) or "nothing"))
    kind, row = tables[0][0], tables[0][1][0]
    if tag is not None and row.get("tag") != tag:
        raise Refused("the row %s is tagged %s, not --flow %s" % (where, row.get("tag"), tag))
    return kind, row


def read_flow_layer(root, build, kind):
    """The build's applied changes of `kind` as `compose --rows -` elements: each applied record's fenced
    row of `kind`, oldest first, its `source` the record's stem, then `{"exclude": <tag>}` per applied
    exclusion of a `kind` tag; `[]` where nothing is applied. ValueError where an applied record does not
    read."""
    rows, excluded = [], []
    for r in read_flow_rows(root, build):
        if not r["states"] or r["states"][-1]["state"] != "applied":
            continue
        if r["act"] == "exclude":
            excluded += [{"exclude": r["tag"]}] if r["tag"].partition(".")[0] == kind else []
            continue
        rkind, row, _text, _after = read_fenced_row(root, build, r["change"])
        if rkind == kind:
            rows.append(dict(row, source=r["change"]))
    return rows + excluded


def read_newest_dispositions(root, build, named=()):
    """{tag: record} of `build`: per `Item`, the newest well-formed tracked disposition record whose stem is
    not in `named`, newest by the stem's date and then `n`. A value is `read_disposition`'s whole record."""
    read_memory_tree("build_records.py")
    from build_records import read_disposition, read_records
    newest = {}
    for r in read_records(root, {"MEMORY_ROOT": resolve_memory_root(root)}, "disposition", read_disposition):
        if r["build"] != build or r["malformed"] or r["id"] in named:
            continue
        held = newest.setdefault(r.get("Item", "").strip("`"), r)
        if (r["id"][:10], r["n"] or 0) > (held["id"][:10], held["n"] or 0):
            newest[r["Item"].strip("`")] = r
    return newest


def read_disposition_release(root, build, tag, named):
    """`(stem, word)` of the newest disposition record of `build` whose `Item` is `tag` and whose stem is not
    in `named`, or None."""
    newest = read_newest_dispositions(root, build, named).get(tag)
    return (newest["id"], newest.get("Disposition", "").strip("`")) if newest else None


# ------------------------------------------------------------------------------------------ the class
def derive_change_class(act, operations):
    """`additive` for an `add` and for an `amend` whose every operation in `operations`, the composition's
    for the row, reads `narrows`; `loosening` for every other act and amendment."""
    if act == "add" or (act == "amend" and all(op.get("class") == "narrows" for op in operations)):
        return "additive"
    return "loosening"


# ------------------------------------------------------------------------------------------ the writes
def render_state_row(tag, state, klass, mode, stem=None):
    """One state row, timestamped now; a held loosening recommends the decline (TOOL-dDeclaredLoop-33)."""
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    advice = " · recommend decline" if (state, klass) == ("held", "loosening") else ""
    return "%s rescope · flow-state %s · %s · class %s · flow.adapt %s%s%s" % (
        now, tag, state, klass, mode, advice, " · disposition %s" % stem if stem else "")


def write_run_row(run, row):
    """Append `row` to the run-state file `run` as one LF-ended line, after an LF where the file lacks one."""
    data = run.read_bytes()
    with open(run, "ab") as fh:
        fh.write(("" if not data or data.endswith(b"\n") else "\n").encode("utf-8") + row.encode("utf-8") + b"\n")


def write_flow_states(root, build, mode):
    """Give each pending flow row of `build` its state row under `flow.adapt` = `mode`: `[state rows]`
    written, in order. Each row is composed with the build's layer before it is graded."""
    run = read_run_file(root, build)
    written = []
    for r in read_pending_rows(root, build):
        klass, stem, state = "none", None, None
        try:
            if r["act"] == "exclude":
                kind, element = r["tag"].partition(".")[0], {"exclude": r["tag"]}
            else:
                kind, row, text, after = read_fenced_row(root, build, r["change"] or "")
                element = dict(row, source=r["change"]) if derive_blob_pin(r["tag"], text.encode("utf-8")) == after \
                    else None
            if element is not None:
                rc, payload, _lines = read_composition(root, kind, read_flow_layer(root, build, kind) + [element])
                if rc == 0:
                    ops = [op for op in payload.get("operations") or [] if op.get("row") == r["tag"]]
                    klass = derive_change_class(r["act"], ops)
        except ValueError:   # a record or fence that does not read, Refused included
            klass = "none"
        if klass == "none" or mode == "off":
            state = "refused"
        elif r["states"]:
            named = {s["disposition"] for x in read_flow_rows(root, build) if x["tag"] == r["tag"]
                     for s in x["states"] if s["disposition"]}
            release = read_disposition_release(root, build, r["tag"], named)
            if release and release[1] in ("continue", "none"):
                stem, state = release[0], "applied" if release[1] == "continue" else "refused"
        if state is None:
            state = "applied" if mode == "additive-recorded" and klass == "additive" else "held"
        line = render_state_row(r["tag"], state, klass, mode, stem)
        write_run_row(run, line)
        written.append(line)
    return written


def check_proposal_fields(fields, ban):
    """Refused where a `(flag, value)` of `fields` holds a line end or the separator, or spells `ban`."""
    for flag, value in fields:
        if "\n" in value or "\r" in value:
            raise Refused("%s holds a line end, and RUN.md is read one row per line" % flag)
        if SEP in value:
            raise Refused("%s spells the row separator %r, which makes its row unparseable" % (flag, SEP.strip()))
        if ban and ban in value:
            raise Refused("%s spells the declared bypass flag, which no record may carry" % flag)


def write_flow_proposal(root, build, flow, act, item, row_path, reason, ban=None):
    """`propose`: check the proposal, write its change record and its `RUN.md` row. -> the lines to print;
    `Refused` naming the act and the row, nothing written."""
    root = pathlib.Path(root).absolute()
    check_proposal_fields([("--build", build), ("--flow", flow), ("--act", act), ("--item", item),
                           ("--row", row_path or ""), ("--reason", reason)], ban)
    if act not in ACTS:
        raise Refused("--act %s is none of %s" % (act, ", ".join(ACTS)))
    if not TAG.fullmatch(flow):
        raise Refused("--flow %s is no tag" % flow)
    if not UNIT_ID.fullmatch(item):
        raise Refused("--item %s is no unit id" % item)
    if not reason.strip():
        raise Refused("--reason is empty")
    if (act == "exclude") == bool(row_path):
        raise Refused("--act %s %s --row" % (act, "refuses" if act == "exclude" else "needs"))
    text = None
    if row_path:
        path = pathlib.Path(row_path)
        path = path if path.is_absolute() else root / path
        try:
            text = path.read_bytes().decode("utf-8").replace("\r\n", "\n")
        except (OSError, UnicodeDecodeError) as e:
            raise Refused("the row %s does not read: %s" % (row_path, e)) from None
        text = "\n".join(text.rstrip("\n").split("\n")) + "\n"
        _kind, row = read_proposal_row(text, flow, row_path)
        edges, want = row.get("edges"), EDGE_OF[act]
        held = isinstance(edges, str) and re.fullmatch(r"(amends|supersedes)=[a-z0-9.-]+@[0-9a-f]{8}", edges)
        if (want is None and edges is not None) or (want and not (held and edges.startswith(want + "="))):
            raise Refused("--act %s disagrees with the row %s, whose edges reads %s: an add holds none, an amend "
                          "amends=<gov tag>@<hash8> and a supersede supersedes=<gov tag>@<hash8>" % (
                              act, row_path, edges if edges is not None else "nothing"))
    run = read_run_file(root, build)
    if not run.is_file():
        raise Refused("the build %s has no RUN.md, so no run records the proposal" % build)
    pin = derive_blob_pin(flow, text.encode("utf-8")) if text is not None else None
    for r in read_flow_rows(root, build):
        if (r["act"], r["tag"], r["reason"]) != (act, flow, reason):
            continue
        if pin is None or (r["change"] and read_fenced_row(root, build, r["change"])[3] == pin):
            return ["%s: unchanged · flow %s %s is already recorded" % (SAY, act, flow)]
    stem, rel = None, None
    if text is not None:
        read_memory_tree("build_records.py")
        from build_records import write_change
        try:
            rel = write_change(root, build, item, flow, "add", "semantic", "none", pin, "none — flow proposal",
                               lines=[FENCE[0], *text.rstrip("\n").split("\n"), FENCE[1]])
        except ValueError as e:
            raise Refused("the change record is refused: %s" % e) from None
        stem = pathlib.PurePosixPath(rel).stem
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = "%s rescope · flow %s %s%s · reason %s" % (now, act, flow, " · change %s" % stem if stem else "", reason)
    try:
        if rel and read_git(root, "add", "--", rel)[0] != 0:
            raise Refused("git could not stage %s" % rel)
        write_run_row(run, line)
    except (OSError, Refused):
        if rel:
            read_git(root, "reset", "-q", "--", rel)
            pathlib.Path(root, rel).unlink()
        raise
    return (["%s: wrote %s" % (SAY, rel)] if rel else []) + ["%s: proposed · %s" % (SAY, line.split(" ", 1)[1])]


# ------------------------------------------------------------------------------------------ the path
def derive_path_deviations(pos, state):
    """`(deviations, unread, why)` of a forward move out of `state` against the position `pos`: each deviation
    `(item, skip|extra)`, `unread` the step's items whose witness is unread; `(None, 0, why)` where the
    position did not read or its step is not the step of `state`."""
    step = next((r for r in read_definition(KIT)[0].get("step", []) if r.get("state") == state), None)
    if pos.get("answer") == "invalid-input":
        return None, 0, pos.get("reason") or "the position does not read"
    if step is None or pos.get("build_step") != step.get("tag"):
        return None, 0, "the position's step is %s, not %s, the step of %s" % (
            pos.get("build_step"), step.get("tag") if step else "none", state)
    witnesses = pos.get("witnesses") or {}
    out = [(tag, "skip") for tag, w in witnesses.items() if w == "unheld" and tag != step.get("exit")]
    out += [(tag, "extra") for tag, states in sorted((pos.get("undeclared") or {}).items()) if state in states]
    return out, sum(1 for w in witnesses.values() if w == "unread"), None


def write_path_orders(root, build, state):
    """At a forward move of `build` out of `state`: the position read with the driver's hand-over, one
    `flow-deviation` order per deviation, and the lines to print."""
    if not os.environ.get(HANDOVER):
        return ["%s: path · %s · unread — %s is unset, so the position is not read" % (SAY, build, HANDOVER)]
    import position
    from composition import render_loop_order, write_loop_order
    pos = position.derive_position(root, build)
    deviations, unread, why = derive_path_deviations(pos, state)
    if deviations is None:
        return ["%s: path · %s · unread — %s" % (SAY, build, why)]
    said = []
    for item, klass in deviations:
        ask = ("The build %s left %s with %s read unheld and no recorded change touching it: record why, or "
               "propose the change." if klass == "skip" else
               "The build %s named %s, which its composition at the pin lacks: propose the change, or record "
               "why.") % ((build, pos["build_step"], item) if klass == "skip" else (build, item))
        text = render_loop_order(ORDER_KIND, [("Build", build), ("Step", pos["build_step"]), ("Item", item),
                                              ("Class", klass)], ask)
        said.append("%s: order · %s" % (SAY, write_loop_order(root, ORDER_KIND, "%s-%s" % (build, item), text)))
    return said + ["%s: path · %s · %s · %d unread" % (SAY, build, pos["build_step"], unread)]


# ------------------------------------------------------------------------------------------ the plants
def build_adapt_base():
    """`(top, base sha)`: `composition.py`'s scratch base with `tFix`'s `RUN.md` committed."""
    from composition import build_composition_base
    top, _sha = build_composition_base()
    try:
        write_fixture_files(top, {"memory/builds/%s/RUN.md" % FX_BUILD:
                                  "# %s run\n\n## Run facts\nphase: BUILDING\n\n## Parked\n" % FX_BUILD})
        run_fixture_git(top, "add", "-A")
        run_fixture_git(top, "commit", "-q", "-m", "the run state")
        return top, run_fixture_git(top, "rev-parse", "HEAD").strip()
    except BaseException:
        remove_tree(top)
        raise


def run_adapt_plant(case, base):
    """One plant over the scratch `base`, `(top, sha)`, reset to its commit first: -> 0 held, 1 missed."""
    import loop_transition
    top, sha = base
    run_fixture_git(top, "reset", "-q", "--hard", sha)
    run_fixture_git(top, "clean", "-qfdx")
    print("%s: fixture · plant %s · %s" % (SAY, case, PLANTS[case]))
    misses = []
    run = read_run_file(top, FX_BUILD)
    # no hand-over inherited from the caller's shell: a plant sets it for the one read that owes it
    ambient = os.environ.pop(HANDOVER, None)

    def check_owed(label, held, said):
        print("%s: fixture · %s · %s" % (SAY, label, said))
        if not held:
            misses.append("%s: %s" % (label, said))

    def write_plant_commit(subject, policy=None):
        if policy:
            write_fixture_files(top, {".governance/policy.toml": "[flow]\nadapt = \"%s\"\n" % policy})
        run_fixture_git(top, "add", "-A")
        run_fixture_git(top, "commit", "-q", "--allow-empty", "-m", subject)

    def write_plant_move(n):
        rc = loop_transition.main(["record", "--build", FX_BUILD, "--root", str(top), *FX_MOVES[n], "--witness", "HEAD"])
        return rc

    def write_plant_proposal(act, tag, row=None):
        if row is not None:
            write_fixture_files(top, {FX_ROW: row})
        try:
            said = write_flow_proposal(top, FX_BUILD, tag, act, FX_UNIT, FX_ROW if row is not None else None,
                                       "the fixture's %s" % case)
        except Refused as e:
            return 1, "%s: refused · %s" % (SAY, e)
        return 0, " | ".join(said)

    def read_states():
        return [ln for ln in run.read_text(encoding="utf-8").splitlines() if " rescope · flow-state " in ln]

    def read_layer_tags():
        rc, payload, lines = read_composition(top, "item", read_flow_layer(top, FX_BUILD, "item"))
        return rc, ({r.get("tag") for r in payload["rows"]} if rc == 0 else set()), lines

    # its outcome routed, so the program the boundary's termination check reads holds (TOOL-dDeclaredLoop-33)
    add_row = ("[[item]]\ntag = \"%s\"\nstep = \"step.build\"\nactor = \"command:lint\"\nneeds = [\"item.build.unit-pass\"]\n"
               "outcomes = [\"clean\"]\nroutes = { clean = \"transition\" }\n" % FX_ADD)
    try:
        if case in ("additive", "owner-approves", "off"):
            if case != "additive":
                write_plant_commit("the plant's policy", case)
            check_owed("propose", write_plant_proposal("add", FX_ADD, add_row)[0] == 0, "exit 0")
            write_plant_commit("the proposal")
            rc, tags, _ = read_layer_tags()
            check_owed("inside the step", rc == 0 and FX_ADD not in tags, "%s in the composition: %s" % (FX_ADD, FX_ADD in tags))
            rc = write_plant_move(0)
            states = read_states()
            want = {"additive": " · applied · class additive", "owner-approves": " · held · class additive",
                    "off": " · refused · class additive"}[case]
            check_owed("move", rc == 0, "record exit %d" % rc)
            check_owed("state", len(states) == 1 and want in states[0], " | ".join(states) or "no state row")
            dirty = run_fixture_git(top, "status", "--porcelain", "--", str(run.relative_to(top).as_posix())).strip()
            check_owed("rides the move", not dirty, "RUN.md %s" % ("committed with the move" if not dirty else dirty))
            rc, tags, _ = read_layer_tags()
            check_owed("composition", rc == 0 and (FX_ADD in tags) == (case == "additive"),
                       "exit %d · %s in it: %s" % (rc, FX_ADD, FX_ADD in tags))
            if case == "owner-approves":
                read_memory_tree("build_records.py")
                from build_records import write_disposition
                rel = write_disposition(top, FX_BUILD, FX_UNIT, FX_ADD, "continue", "terminal")
                write_plant_commit("the owner's disposition")
                rc = write_plant_move(1)
                states = read_states()
                stem = pathlib.PurePosixPath(rel).stem
                check_owed("released", rc == 0 and len(states) == 2 and " · applied · " in states[1]
                           and states[1].endswith(" · disposition %s" % stem), " | ".join(states))
                rc, tags, _ = read_layer_tags()
                check_owed("composition after", rc == 0 and FX_ADD in tags, "%s in it: %s" % (FX_ADD, FX_ADD in tags))
        elif case == "loosening":
            check_owed("propose", write_plant_proposal("exclude", FX_EXCLUDE)[0] == 0, "exit 0")
            write_plant_commit("the proposal")
            rc = write_plant_move(0)
            states = read_states()
            check_owed("held", rc == 0 and len(states) == 1 and " · held · class loosening · " in states[0]
                       and states[0].endswith(" · recommend decline"), " | ".join(states) or "no state row")
            read_memory_tree("build_records.py")
            from build_records import write_disposition
            write_disposition(top, FX_BUILD, FX_UNIT, FX_EXCLUDE, "continue", "terminal")
            write_plant_commit("the owner's disposition")
            rc = write_plant_move(1)
            states = read_states()
            check_owed("released", rc == 0 and len(states) == 2 and " · applied · class loosening · " in states[1],
                       " | ".join(states))
            layer = read_flow_layer(top, FX_BUILD, "item")
            rc, tags, lines = read_layer_tags()
            check_owed("composition", layer == [{"exclude": FX_EXCLUDE}] and rc == 0 and FX_EXCLUDE not in tags,
                       "layer %s · exit %d · %s in it: %s %s" % (layer, rc, FX_EXCLUDE, FX_EXCLUDE in tags,
                                                                 " | ".join(lines)[:200]))
        elif case == "unrecorded-skip":
            import position
            for n in (0, 1):
                write_plant_move(n)
            before = os.environ.get(HANDOVER)
            os.environ[HANDOVER] = position.render_handover([(FX_UNIT, "READY")])
            try:
                rc = write_plant_move(2)
            finally:
                if before is None:
                    os.environ.pop(HANDOVER, None)
                else:
                    os.environ[HANDOVER] = before
            folder = top / ".governance" / "outbox"
            names = sorted(p.name for p in folder.glob("loop-%s-%s-*.md" % (ORDER_KIND, FX_BUILD))) if folder.is_dir() else []
            text = (folder / names[0]).read_text(encoding="utf-8") if names else ""
            check_owed("order", rc == 0 and names == ["loop-%s-%s-item.build.acceptance.md" % (ORDER_KIND, FX_BUILD)]
                       and "- **Class:** skip" in text and "item.build.acceptance" in text,
                       " ".join(names) or "no flow-deviation order")
        elif case == "act-mismatch":
            rc, payload, _ = read_composition(top)
            pin = (payload or {}).get("pins", {}).get("item.build.unit-pass", "0123abcd")
            before = (run.read_bytes(), sorted(p.name for p in run.parent.joinpath("build").glob("*")))
            rc, said = write_plant_proposal("add", FX_ADD, add_row + "edges = \"amends=item.build.unit-pass@%s\"\n" % pin)
            after = (run.read_bytes(), sorted(p.name for p in run.parent.joinpath("build").glob("*")))
            check_owed("refused", rc == 1 and "--act add" in said and FX_ROW in said, said)
            check_owed("nothing written", before == after, "RUN.md and build/ %s" % ("unchanged" if before == after else
                                                                                      "changed"))
        elif case == "unit-row":
            read_memory_tree("deviation_join.py")
            from deviation_join import RESCOPE
            unit = "2026-01-01T00:00:00Z rescope · item add FIX-dAdapt-2 · reason the fixture's unit row\n"
            write_run_row(run, unit.rstrip("\n"))
            alone = [m.groups()[:2] for m in RESCOPE.finditer(run.read_text(encoding="utf-8"))]
            check_owed("propose", write_plant_proposal("add", FX_ADD, add_row)[0] == 0, "exit 0")
            both = [m.groups()[:2] for m in RESCOPE.finditer(run.read_text(encoding="utf-8"))]
            check_owed("RESCOPE", alone == both == [("add", "FIX-dAdapt-2")], "alone %s · with the flow row %s" % (alone, both))
        elif case == "mid-step":
            import position
            os_before = os.environ.get(HANDOVER)
            os.environ[HANDOVER] = position.render_handover([(FX_UNIT, "READY")])
            try:
                first = position.derive_position(top, FX_BUILD)
                check_owed("propose", write_plant_proposal("add", FX_ADD, add_row)[0] == 0, "exit 0")
                write_plant_commit("the proposal")
                inside = position.derive_position(top, FX_BUILD)
                same = inside["witnesses"] == first["witnesses"] and \
                    [f["item"] for f in inside["frontier"]] == [f["item"] for f in first["frontier"]]
                check_owed("inside the step", same and bool(first["witnesses"]) and FX_ADD not in inside["witnesses"],
                           "%d item(s) read, unchanged: %s · %s read: %s" % (
                               len(inside["witnesses"]), same, FX_ADD, FX_ADD in inside["witnesses"]))
                write_plant_move(0)
                after = position.derive_position(top, FX_BUILD)
                check_owed("after the boundary", FX_ADD in after["witnesses"], "%s read: %s" % (
                    FX_ADD, after["witnesses"].get(FX_ADD, "absent")))
            finally:
                if os_before is None:
                    os.environ.pop(HANDOVER, None)
                else:
                    os.environ[HANDOVER] = os_before
    except (subprocess.CalledProcessError, OSError, ValueError, LookupError, KeyError) as exc:
        misses.append("the plant could not run: %s %s" % (exc, (getattr(exc, "stderr", "") or "").strip()[:300]))
    finally:
        if ambient is not None:
            os.environ[HANDOVER] = ambient
    print("%s: fixture · %s · %s" % (SAY, case, "held" if not misses else "MISSED " + "; ".join(misses)))
    return 1 if misses else 0


def run_selftest():
    """Every plant over one scratch base through `run_selftest_cases`: -> 0 when every case holds."""
    try:
        base = build_adapt_base()
    except (LookupError, OSError, ValueError, subprocess.CalledProcessError) as exc:
        print("%s: adapt selftest · UNARMED · the scratch could not be built: %s" % (SAY, exc))
        return 2
    try:
        cases = [(c, ["--fixture", "--plant", c], 0, "%s: fixture · %s · held" % (SAY, c), "") for c in PLANTS]
        return run_selftest_cases(lambda argv: run_adapt_plant(argv[2], base), cases, "%s: adapt selftest" % SAY)
    finally:
        remove_tree(base[0])


def run_propose(args):
    """The `propose` verb: -> its exit."""
    try:
        said = write_flow_proposal(pathlib.Path.cwd(), args.build, args.flow, args.act, args.item, args.row,
                                   args.reason, args.ban)
    except Refused as e:
        print("%s: refused · %s" % (SAY, e))
        return 1
    except LookupError as e:
        print("%s: unarmed · %s" % (SAY, e))
        return 2
    except (ValueError, OSError) as e:
        print("%s: unanswered · %s" % (SAY, e))
        return 2
    for line in said:
        print(line)
    return 0


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if argv == ["--selftest"]:
        return run_selftest()
    if len(argv) == 3 and argv[:2] == ["--fixture", "--plant"] and argv[2] in PLANTS:
        try:
            base = build_adapt_base()
        except (LookupError, OSError, ValueError, subprocess.CalledProcessError) as exc:
            print("%s: fixture · UNARMED · the scratch could not be built: %s" % (SAY, exc))
            return 2
        try:
            return run_adapt_plant(argv[2], base)
        finally:
            remove_tree(base[0])
    if argv[:1] == ["propose"]:
        ap = argparse.ArgumentParser(prog="adapt.py propose", description="propose one flow change of a build")
        for flag in ("--build", "--flow", "--act", "--item", "--reason"):
            ap.add_argument(flag, required=True)
        ap.add_argument("--row")
        ap.add_argument("--ban")
        return run_propose(ap.parse_args(argv[1:]))
    print("usage: python adapt.py propose --build <slug> --flow <tag> --act <%s> --item <id> [--row <path>] "
          "--reason <r> [--ban <flag>] | --fixture --plant <%s> | --selftest" % ("|".join(ACTS), "|".join(PLANTS)),
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
