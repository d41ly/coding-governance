#!/usr/bin/env python3
"""record.py — one run's committed record: a closed-schema report and its JSON twin. gov:kit runlog@1.0

A run's model is machine-local, and most runs are made on some other node. This renders the model into
ONE tracked record in the build folder, under the declared memory root, that every node can read. The
repository is public, so the record is STRUCTURAL ONLY: every value in it is drawn from `RECORD_SCHEMA`,
a closed set of value classes. Some are shaped, such as a UTC timestamp, a duration or a sha. The rest
are closed vocabularies, such as the coverage states. No free text, absolute path, session id, host id
or command can reach the file, because nothing reaches it except through a class. A model value outside
its field's class is written `-`, which also stands for an absent value, and the summary's `values
withheld` line counts every one, so a model that grew a value the schema does not admit says so. An
UNKNOWN value is absent too: a count from a source the model never read is `-` rather than the zero
that reads clean.

THE SCHEMA IS DATA, SHARED. The renderer builds the record from `RECORD_SCHEMA`, and the schema leg
(TOOL-dLoggedFlight-10) re-validates the committed bytes against the same data rather than trusting this
code path. Its vocabularies are the model's own closed lists, held by reference, so the record and the
model cannot name two sets. Each section declares its fact lines as templates and its tables as column
classes, with the timeline's columns classed per event kind. The `Data` block at the end is the
markdown re-encoded as JSON: every fact and every shown row, so the two copies cannot disagree.

THE CAP IS REACHABLE FOR EVERY INPUT. Every section that grows is bounded: the timeline shows its first
and last `TIMELINE_EDGE` rows, and every list aggregates by kind past `LIST_BOUND` rows. A record still
over `RECORD_CAP_BYTES`, which cells of unusual width can cause, halves what it shows until it fits: the
timeline's rows first, then the lists' bound, in turn. Every elision and aggregation is stated in the
record itself.

THE COMMITMENT makes a later edit to the journal detectable on the node that holds it: the sha256 and
the line count of the journal lines the MODEL attributed to the run, read from its `journal_lines` and
never re-joined here. NO TIME OF A JOURNAL LINE IS COMMITTED (owner, 2026-09-16), so the committed
count is the whole anchor: `check_commitment` rebuilds the model and hashes that many lines from the
START of its time order. A line the run appends after the render sorts past them and is not an edit; an
edit, a deletion, or a line of the run inserted among them reads as a mismatch.

THE SCHEMA LEG (TOOL-dLoggedFlight-10) is `check_records`, run as `runlog.py check-records`. It reads
every committed record's STAGED bytes and refuses anything outside `RECORD_SCHEMA`, compiling the
schema's data itself rather than calling the renderer, so a renderer bug cannot vouch for itself. It
also derives every tracked run's start and window from git alone and refuses two runs of one build that
share a start or whose windows overlap. What it does not check is stated at `check_records`.

WHAT THIS DOES NOT DO. Rendering makes no git call: the model's calls are the whole cost, and rendering
is a pure function of the model. It does not judge whether a value is TRUE, only that it is in
its class. It does not choose when a record is rendered; the unattended Skill's step does. And it names
nothing outside this kit by literal: the memory root is resolved, and the build-index generator is found
beside this kit by its file name.
"""
from __future__ import annotations

import dataclasses
import datetime
import fnmatch
import hashlib
import itertools
import json
import os
import pathlib
import re
import sys
import time
from collections import Counter

HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import extract as ex  # noqa: E402
import model as mdl  # noqa: E402
import runlog_lib as rl  # noqa: E402

RECORD_CAP_BYTES = 24576
# The nominal bounds (spec S6, rev-5). The rev-4 figures, 60 and 40, did not fit the cap once the twin
# doubles each row: a timeline row pair measures about 140 bytes, so 120 of them were 17 KB alone.
TIMELINE_EDGE = 30
LIST_BOUND = 20
NONE = "-"
RECORD_TAG = "runlog"
TITLE = "# Run record"
SERVES_KIND = "journal"
INTRO = ("Rendered from the run model by the runlog kit's `record` command. Every value below is drawn "
         "from a closed schema, so no line carries free text. Re-render it rather than edit it.")
DATA_OPEN = "```json"
DATA_CLOSE = "```"

# TWO LISTS ANOTHER FILE OWNS, COPIED, because a kit reads no sibling at run time. The withheld
# self-test holds each to its owner in both directions where the owner is present: the spec status
# tokens to the spec template, and the review verdicts to the hygiene doc's check 22. A value outside
# a copy is withheld like any other, never guessed at. The pre-push hook's own decision list was a
# third until TOOL-dLoggedFlight-22 retired the `push` rows that carried it.
UNIT_STATUSES = ("OPEN", "SPECCED", "INPROGRESS", "BLOCKED", "DEFERRED", "CLOSED", "WONTDO")
REVIEW_VERDICTS = ("CLEAN", "CLEAN WITH FIXES", "BLOCKED")
# The timeline's event kinds, every one of which is timed by git or by the run-state file. `owner` is
# deliberately absent: owner turns are counts per position and never clock times, so the renderer drops
# them from the timeline before a row is built.
TIMELINE_EVENTS = ("phase", "commit", "merge", "dispatch", "brief")
# THE KINDS NO COMMITTED RECORD CARRIES (TOOL-dLoggedFlight-22 S1). Each is timed by the journal or by
# a transcript, and no journal or transcript time is committed (owner, 2026-09-16), so the renderer
# drops it before a row is built. It is NOT a value outside its class, so it is not counted in `values
# withheld`; `TOOL-dLoggedFlight-27`'s `withheld rows` fact counts these per kind from a declared
# source. The local model keeps every one of them.
RETIRED_EVENTS = ("verb", "push", "push-refused", "gate", "compact", "limit", "idle", "workflow")
EXCLUDED_KINDS = tuple(k for k in mdl.PARK_KINDS if k not in mdl.PARK_KINDS_OWED)
USAGE_FIELDS = ("requests", "in", "out", "cache_read", "cache_write")
# The transcripts' coverage states under which a count the model derives from them is KNOWN (spec S4).
# `partial` is a lower bound and says so in Coverage; under any other state the count is `-`.
COUNTED_STATES = ("present", "partial")
DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
RECORD_NAME_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}-build-([A-Z]+-[A-Za-z0-9]+-[0-9]+)-"
                            + RECORD_TAG + r"-([0-9a-f]{8})\.md")
UNIT_ID_RE = re.compile(r"([A-Z]+)-([A-Za-z0-9]+)-([0-9]+)")
PLACEHOLDER_RE = re.compile(r"\{([a-z-]+)\}")
COMMITMENT_RE = re.compile(r"sha256 ([0-9a-f]{64}) · lines ([0-9]+)")
# EVERY SUMMARY FACT WHOSE RENDERED VALUE A PARSER IN THIS KIT READS BACK, mapped to that parser
# (TOOL-dLoggedFlight-21 S5). A template and the parser that reads it back are ONE contract kept in
# two places: the commitment's template and `COMMITMENT_RE` were changed in two different specs, and
# every record rendered in between would have failed `verify`. The self-test's pair arm renders each
# mapped fact and re-parses it with its own parser, so the disagreement reds in code rather than
# waiting for a reader to cross-read two documents.
TEMPLATE_PARSERS = {"commitment": COMMITMENT_RE}

_PATH_SEG = r"[A-Za-z0-9][A-Za-z0-9._-]*"
_PATH = r"<root>/builds/<slug>/(?:" + _PATH_SEG + r"/)*" + _PATH_SEG + r"\.md"
_UNIT = r"[A-Z]+-<slug>-[0-9]+"
_WINDOW_USAGE = "requests {int} · in {int} · out {int} · cache-read {int} · cache-write {int}"
# Where a token starts: the line's start, or after a space, a quote, a bracket, a table bar, a comma or
# an equals sign. A root-shaped segment in the MIDDLE of a path class value is a folder name, not a root.
_TOKEN_START = r"(?:^|(?<=[\s\"'`(|,\[=]))"

# THE CLOSED SCHEMA (spec S4). `shaped` are regexes a value must match WHOLE; `<root>` and `<slug>` are
# the build's own declared memory root and slug, escaped when compiled. A `unit` must also be one of
# the build's own spec-defined unit ids. `vocab` are closed lists, the model's own where it owns one.
# `sections` declares, per heading, the fact lines as templates and the tables as column classes; the
# class `none` admits only `-`. The timeline's columns are classed per event kind, keyed on column 3.
RECORD_SCHEMA = {
    "schema": 1,
    "cap_bytes": RECORD_CAP_BYTES,
    "title": TITLE,
    "serves_kind": SERVES_KIND,
    "intro": INTRO,
    "none": NONE,
    "headings": ("Summary", "Timeline", "Units", "Decisions", "Conformance", "Anomalies", "Coverage",
                 "Data"),
    "shaped": {
        "utc": r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z",
        "int": r"[0-9]{1,15}",
        "duration": r"[0-9]{1,12}s",
        "sha": r"[0-9a-f]{7,40}",
        "digest": r"[0-9a-f]{64}",
        "phase": r"[A-Z]{3,12}",
        "unit": _UNIT,
        "units": _UNIT + r"(?: " + _UNIT + r")*",
        "path": _PATH,
        "ref": r"(?:" + _PATH + r"(?::[0-9]{1,7})?|[0-9a-f]{7,40})",
    },
    "vocab": {
        "yes-no": ("yes", "no"),
        "opened-by": ("git",),
        "closed-by": ("terminal-write", "terminal-pending", "last-activity"),
        "event": TIMELINE_EVENTS,
        "source": mdl.SOURCE_NAMES,
        "coverage-state": mdl.COVERAGE_STATES,
        "ledger-source": mdl.LEDGER_SOURCES,
        "owner-position": mdl.OWNER_POSITIONS,
        "conformance-item": mdl.CONFORMANCE_ITEMS,
        "conformance-state": mdl.CONFORMANCE_STATES,
        "anomaly-kind": mdl.ANOMALY_KINDS,
        "merged-subclass": mdl.MERGED_SUBCLASSES,
        "review-verdict": REVIEW_VERDICTS,
        "review-exit": mdl.REVIEW_EXITS,
        "unit-status": UNIT_STATUSES,
    },
    "sections": {
        "Summary": {
            "facts": (
                ("run-state", ("{path}",)),
                ("run", ("{int} of {int}",)),
                ("start", ("{sha}",)),
                ("phase", ("{phase}",)),
                ("terminal", ("{yes-no}",)),
                ("window", ("{utc} to {utc}",)),
                ("window opened by", ("{opened-by}",)),
                ("window closed by", ("{closed-by}",)),
                ("duration", ("{duration}",)),
                ("own commits", ("{int}",)),
                ("last own commit", ("{sha}",)),
                ("merged", ("{yes-no}",)),
                ("units served", ("{int}",)),
                ("sources present", ("{int} of {int}",)),
                ("owner turns", (" · ".join(f"{p} {{int}}" for p in mdl.OWNER_POSITIONS),)),
                ("usage main", (_WINDOW_USAGE,)),
                ("usage agent", (_WINDOW_USAGE,)),
                ("usage workflow", (_WINDOW_USAGE,)),
                ("attributed calls", ("{int} of {int}",)),
                ("values withheld", ("{int}",)),
                ("commitment", ("none", "sha256 {digest} · lines {int}")),
            ),
            "tables": (),
        },
        "Timeline": {
            "facts": (
                ("events", ("{int} · shown {int} · elided {int}",)),
                ("elided", ("{int} events from {utc} to {utc}",)),
            ),
            "tables": (
                {"name": "events", "header": ("UTC", "source", "event", "value", "phase", "rc", "more"),
                 "key": 2,
                 "rows": {
                     "phase": ("utc", "source", "event", "sha", "phase", "none", "none"),
                     "commit": ("utc", "source", "event", "sha", "none", "none", "units"),
                     "merge": ("utc", "source", "event", "sha", "none", "none", "units"),
                     "dispatch": ("utc", "source", "event", "unit", "none", "none", "none"),
                     "brief": ("utc", "source", "event", "unit", "none", "none", "none"),
                 }},
            ),
        },
        "Units": {
            "facts": (("units", ("{int} · shown {int} · aggregated {yes-no}",)),),
            "tables": (
                {"name": "units",
                 "header": ("order", "unit", "status", "commits", "dispatched", "briefed", "built"),
                 "cols": ("int", "unit", "unit-status", "int", "int", "int", "sha")},
                {"name": "by-status", "header": ("#", "status", "units"),
                 "cols": ("int", "unit-status", "int")},
            ),
        },
        "Decisions": {
            "facts": (
                ("entries", ("{int} · shown {int} · aggregated {yes-no}",)),
                ("trailer near-misses", ("{int}",)),
                ("decision-log rows the owner's", ("{int}",)),
                ("spec marks", ("owner-before {int} · owner-inside {int} · agent-before {int} · "
                                "agent-inside {int}",)),
                ("excluded rows", (" · ".join(f"{k} {{int}}" for k in EXCLUDED_KINDS),)),
                ("review rounds", ("{int} · shown {int} · aggregated {yes-no}",)),
            ),
            "tables": (
                {"name": "by-source", "header": ("#", "source", "entries"),
                 "cols": ("int", "ledger-source", "int")},
                {"name": "entries", "header": ("#", "source", "ref", "verdict"),
                 "cols": ("int", "ledger-source", "ref", "review-verdict")},
                {"name": "rounds", "header": ("#", "UTC", "verdict", "blockers", "exit"),
                 "cols": ("int", "utc", "review-verdict", "int", "review-exit")},
                {"name": "rounds-by-verdict", "header": ("#", "verdict", "exit", "rounds"),
                 "cols": ("int", "review-verdict", "review-exit", "int")},
            ),
        },
        "Conformance": {
            "facts": (("items", ("{int} · shown {int} · aggregated {yes-no}",)),),
            "tables": (
                {"name": "items", "header": ("#", "item", "unit", "state"),
                 "cols": ("int", "conformance-item", "unit", "conformance-state")},
                {"name": "by-state", "header": ("#", "item", "state", "count"),
                 "cols": ("int", "conformance-item", "conformance-state", "int")},
            ),
        },
        "Anomalies": {
            "facts": (("anomalies", ("{int} · shown {int} · aggregated {yes-no}",)),),
            "tables": (
                {"name": "anomalies", "header": ("#", "kind", "subclass"),
                 "cols": ("int", "anomaly-kind", "merged-subclass")},
                {"name": "by-kind", "header": ("#", "kind", "subclass", "count"),
                 "cols": ("int", "anomaly-kind", "merged-subclass", "int")},
            ),
        },
        "Coverage": {
            "facts": (
                ("journal starts", ("{int} joined of {int} record-creating",)),
                ("unjoined starts", ("{int}",)),
                ("sessions", ("{int} named · {int} extracted",)),
                # The model's `idle` entry (TOOL-dLoggedFlight-8 S6, rev-6): whether idle gaps were
                # judged at all, and how many were kept out beside an owner turn. `-` when not judged,
                # so an absent judgement never reads as a clean zero.
                ("idle gaps", ("judged {yes-no} · near an owner turn {int}",)),
            ),
            "tables": (
                {"name": "sources", "header": ("#", "source", "state", "lines", "bad"),
                 "cols": ("int", "source", "coverage-state", "int", "int")},
            ),
        },
        "Data": {"facts": (), "tables": ()},
    },
    # SHAPES NO RECORD MAY CARRY ANYWHERE, whatever class a value passed (TOOL-dLoggedFlight-10 S5).
    # The renderer withholds a value one of these finds, and the schema leg refuses a record in whose
    # bytes one is found. They are data here because a path class's file segment admits a lowercase
    # UUID — `_PATH_SEG` opens on `[A-Za-z0-9]` and continues over `[A-Za-z0-9._-]` — so a rule only
    # the leg knew would let the renderer write a record the leg refuses. An absolute path is a drive
    # letter, a `/Users/`, `/home/` or MSYS drive root at a token start, or a UNC prefix in either
    # slash.
    "forbidden": {
        "absolute-path": (r"(?<![A-Za-z0-9])[A-Za-z]:[\\/]"
                          + r"|" + _TOKEN_START + r"(?:/(?:[A-Za-z]|Users|home)/|//[A-Za-z0-9])"
                          + r"|\\\\[A-Za-z0-9._$-]"),
        "uuid": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}",
    },
}

# ---------------------------------------------------------------------------------- small helpers

def derive_view(model) -> dict:
    """The model as the dict `asdict` makes of it, so a `RunModel` and a fixture dict read alike."""
    return dataclasses.asdict(model) if dataclasses.is_dataclass(model) else model


def derive_short_sha(sha) -> str | None:
    return sha[:12] if isinstance(sha, str) and len(sha) >= 12 else sha


def derive_count(value) -> str | None:
    """A non-negative integer as text, else the value itself for its class to refuse."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return str(int(value)) if value >= 0 else str(value)
    return value


def derive_yes_no(value) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        return {"1": "yes", "0": "no"}.get(value, value)
    return "yes" if value else "no"


def derive_window_bounds(window) -> tuple:
    """`(start, closing time)` of a window as the record renders them (spec S2 of
    TOOL-dLoggedFlight-24), each a commit's own committer time, or `(None, None)` for no window.

    A window is HALF-OPEN, so a `last-activity` end is the last record commit's time plus the one
    second that a commit time's resolution adds, and no public source shows that value. The closing
    time takes that second back off, leaving the closing commit's own time: the first terminal
    write's where the phase moved there, else the last record commit's. `terminal-end` never reaches
    here, since `record_window` is derived with no `term_end`, and would be taken unchanged if it did:
    it is a journal time, which the committed record does not carry.
    """
    w = window or {}
    start, end = w.get("start"), w.get("end")
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) for v in (start, end)):
        return None, None
    return start, (end - 1.0 if w.get("end_from") == "last-activity" else end)


def derive_window_closer(window, terminal) -> str | None:
    """The `closed-by` the record renders for a window, or None where there is no window.

    A RENDER RIDES THE COMMIT THAT CARRIES THE TERMINAL WRITE (spec S1 of TOOL-dLoggedFlight-25), so
    at the `--landed` and `--abort` placements the run-state file in the working tree is already
    terminal while no record commit carrying that phase exists yet. `derive_window` then closes the
    window at the last record commit before it and calls that `last-activity` — which beside
    `terminal: yes` reads as a run that stopped by going quiet. `terminal-pending` names the write
    instead: the closing bound is the last committed one and the terminal write is still to land. A
    re-render once it has landed reads `terminal-write` with that commit's own time, which is the lag
    the kit README declares rather than hides.
    """
    end_from = (window or {}).get("end_from")
    if not end_from:
        return None
    return "terminal-pending" if terminal and end_from == "last-activity" else end_from


def build_matchers(slug, memory_root, own_ids) -> dict:
    """Every class of `RECORD_SCHEMA` as a predicate over text, bound to ONE build."""
    out = {}
    for name, pat in RECORD_SCHEMA["shaped"].items():
        rx = re.compile(pat.replace("<root>", re.escape(memory_root)).replace("<slug>", re.escape(slug)))
        out[name] = rx.fullmatch
    for name, members in RECORD_SCHEMA["vocab"].items():
        out[name] = frozenset(members).__contains__
    unit_rx, own = out["unit"], frozenset(own_ids)
    out["unit"] = lambda text: bool(unit_rx(text)) and text in own
    out["units"] = lambda text: all(t in own and unit_rx(t) for t in text.split(" ")) and bool(text)
    out["none"] = lambda text: False
    return out


def build_forbidden() -> tuple:
    """The schema's forbidden shapes, compiled for the renderer. The schema leg compiles the same data
    itself, in `scan_forbidden`, so neither reader vouches for the other."""
    return tuple(re.compile(p) for p in RECORD_SCHEMA["forbidden"].values())


def render_cell(ctx, cls, value) -> str:
    """ONE value through its class: itself when it belongs, `-` when it is absent or does not, and a
    value that does not belong, or that carries a forbidden shape, is counted as withheld."""
    if cls == "none" or value is None or value == "" or value == [] or value == NONE:
        return NONE
    text = str(value)
    if ctx["match"][cls](text) and not any(rx.search(text) for rx in ctx.get("forbidden", ())):
        return text
    ctx["withheld"] += 1
    return NONE


def render_fact(ctx, template, values) -> str:
    """A fact template with each `{class}` placeholder filled, in order, through `render_cell`."""
    parts = PLACEHOLDER_RE.split(template)
    vals = iter(values)
    return "".join(part if i % 2 == 0 else render_cell(ctx, part, next(vals, None))
                   for i, part in enumerate(parts))


def derive_fact_templates(section, label) -> tuple:
    for name, templates in RECORD_SCHEMA["sections"][section]["facts"]:
        if name == label:
            return templates
    raise KeyError(f"runlog: {section} declares no fact {label!r}")


def derive_table(section, name) -> dict:
    for table in RECORD_SCHEMA["sections"][section]["tables"]:
        if table["name"] == name:
            return table
    raise KeyError(f"runlog: {section} declares no table {name!r}")


# ---------------------------------------------------------------------------------- serves and names

def derive_serves(model) -> list:
    """The unit ids the run dispatched or closed, among those a spec in its build defines, lowest first.

    Dispatched: a `dispatch` row of the run's own record names it. Closed: its spec status reads CLOSED
    and one of the run's own commits names it. Any other id is outside the record, whatever named it.
    """
    m = derive_view(model)
    units = m.get("units") or []
    defined = {u["id"] for u in units if u.get("id")}
    named = {x for c in m.get("own_commits") or [] for x in c.get("units") or []}
    dispatched = {u["id"] for u in units if u.get("dispatches")}
    closed = {u["id"] for u in units if u.get("status") == "CLOSED" and u["id"] in named}
    return sorted((dispatched | closed) & defined, key=derive_unit_key)


def derive_unit_key(uid) -> tuple:
    m = UNIT_ID_RE.fullmatch(uid)
    return (m.group(1), m.group(2), int(m.group(3))) if m else (uid, "", 0)


def render_serves(ids) -> str:
    """Ids as check 21 reads them, a contiguous run of one family and slug written `N..M`."""
    out, run = [], []
    for uid in sorted(ids, key=derive_unit_key):
        key = derive_unit_key(uid)
        if run and key[:2] == run[-1][:2] and key[2] == run[-1][2] + 1:
            run.append(key)
            continue
        if run:
            out.append(render_id_run(run))
        run = [key]
    if run:
        out.append(render_id_run(run))
    return " ".join(out)


def render_id_run(run) -> str:
    fam, slug, lo = run[0]
    hi = run[-1][2]
    return f"{fam}-{slug}-{lo}" if lo == hi else f"{fam}-{slug}-{lo}..{hi}"


def derive_runkey(model) -> str:
    """The run's key, READ from the model, which took it from `derive_run_starts`: the first 8 hex of the
    commit that started the run. Never re-derived here, so a file name and its window cannot disagree."""
    m = derive_view(model)
    key, start = str(m.get("runkey") or ""), str(m.get("start_commit") or "")
    if not re.fullmatch(r"[0-9a-f]{8}", key) or not start.startswith(key):
        raise ValueError(f"runlog: the model's runkey {key[:40]!r} is not the first 8 hex of its start "
                         "commit, so no record name can be derived from it")
    return key


def derive_record_relpath(memory_root, slug, day, uid, key) -> str:
    """The repo-relative path the renderer writes a run's record to. ONE builder: `resolve_record_path`
    names a new record with it, and the schema leg asserts at run time that its glob admits what this
    returns, so a renamed record cannot drop out of the leg's population in silence."""
    return f"{memory_root}/builds/{slug}/build/{day}-build-{uid}-{RECORD_TAG}-{key}.md"


def resolve_record_path(root, model, serves, date=None, memory_root=None) -> tuple:
    """`(path, existed)`: the run's record under `<memory root>/builds/<slug>/build/`.

    A record already carrying this run's key is the answer, whatever its date, so a later render never
    makes a second file; two carrying it refuse. A new record is named for the render date and the
    LOWEST id it serves, which is what check 21's filename projection requires.
    """
    m = derive_view(model)
    root = pathlib.Path(root)
    mr = memory_root if memory_root is not None else rl.resolve_memory_root(root)
    key = derive_runkey(m)
    day = date or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    target = root / derive_record_relpath(mr, m["slug"], day, serves[0], key)
    folder = target.parent
    found = sorted(folder.glob(f"*-{RECORD_TAG}-{key}.md")) if folder.is_dir() else []
    if len(found) > 1:
        raise ValueError(f"runlog: {len(found)} records carry the runkey {key}, so which one this run "
                         f"owns is a guess: {', '.join(p.name for p in found)}")
    if found:
        nm = RECORD_NAME_RE.fullmatch(found[0].name)
        if nm is None or nm.group(1) not in serves:
            raise ValueError(f"runlog: the existing record {found[0].name} names an id this run no longer "
                             "serves, so re-rendering into it would break check 21's projection")
        return found[0], True
    if not DATE_RE.fullmatch(str(day)):
        raise ValueError(f"runlog: {str(day)[:40]!r} is not a YYYY-MM-DD render date")
    return target, False


# ---------------------------------------------------------------------------------- the rows

def derive_timeline_values(e) -> tuple:
    """One timeline event as the seven raw column values its kind declares; `render_cell` classes them."""
    kind = e.get("kind")
    head = (mdl.derive_iso(e.get("t")), e.get("source"), kind)
    if kind == "phase":
        return head + (derive_short_sha(e.get("witness")), e.get("phase"), None, None)
    if kind in ("commit", "merge"):
        return head + (derive_short_sha(e.get("sha")), None, None, " ".join(e.get("units") or []))
    if kind in ("dispatch", "brief"):
        return head + (e.get("unit"), None, None, None)
    return head + (None, None, None, None)


def build_timeline_rows(m, ctx) -> list:
    spec = derive_table("Timeline", "events")["rows"]
    rows = []
    for e in m.get("timeline") or []:
        kind = e.get("kind")
        # Owner turns are counts per position, never clock times (spec S4), and a RETIRED kind is
        # timed by a journal or a transcript, which no record commits (TOOL-dLoggedFlight-22 S1).
        # NEITHER is a value outside its class, so neither is counted in `values withheld`.
        if kind == "owner" or kind in RETIRED_EVENTS:
            continue
        classes = spec.get(kind)
        if classes is None:
            ctx["withheld"] += 1      # an event kind the schema does not declare is never rendered
            continue
        rows.append([render_cell(ctx, c, v) for c, v in zip(classes, derive_timeline_values(e))])
    return rows


def build_unit_rows(m, ctx) -> list:
    cols = derive_table("Units", "units")["cols"]
    by_unit = Counter(u for c in m.get("own_commits") or [] for u in c.get("units") or [])
    units = sorted(m.get("units") or [],
                   key=lambda u: (u.get("order") if isinstance(u.get("order"), int) else 10 ** 9,
                                  derive_unit_key(str(u.get("id")))))
    rows = []
    for pos, u in enumerate(units, 1):
        order = u.get("order") if isinstance(u.get("order"), int) and u["order"] >= 0 else pos
        raw = (order, u.get("id"), u.get("status"), by_unit.get(u.get("id"), 0),
               len(u.get("dispatches") or []), len(u.get("briefs") or []),
               derive_short_sha(u.get("build_commit")))
        rows.append([render_cell(ctx, c, derive_count(v)) for c, v in zip(cols, raw)])
    return rows


def build_entry_rows(m, ctx) -> list:
    cols = derive_table("Decisions", "entries")["cols"]
    rows = []
    for i, e in enumerate((m.get("ledger") or {}).get("entries") or [], 1):
        ref = e.get("ref")
        ref = derive_short_sha(ref) if isinstance(ref, str) and mdl.SHA_RE.fullmatch(ref) else ref
        verdict = e.get("verdict") if e.get("source") == "review" else None
        rows.append([render_cell(ctx, c, v) for c, v in zip(cols, (str(i), e.get("source"), ref, verdict))])
    return rows


def build_round_rows(m, ctx) -> list:
    cols = derive_table("Decisions", "rounds")["cols"]
    rows = []
    for row in m.get("record_rows") or []:
        if row.get("kind") != "review":
            continue
        reason = row.get("reason") or ""
        blockers = re.search(r"(?:^|· )blockers ([0-9]+)(?: ·|$)", reason)
        raw = (str(len(rows) + 1), mdl.derive_iso(row.get("t")), mdl.derive_review_verdict(reason),
               blockers.group(1) if blockers else None, mdl.derive_review_exit(reason))
        rows.append([render_cell(ctx, c, v) for c, v in zip(cols, raw)])
    return rows


def build_conformance_rows(m, ctx) -> list:
    cols = derive_table("Conformance", "items")["cols"]
    return [[render_cell(ctx, c, v) for c, v in zip(cols, (str(i), c_.get("item"), c_.get("unit"),
                                                           c_.get("state")))]
            for i, c_ in enumerate(m.get("conformance") or [], 1)]


def build_anomaly_rows(m, ctx) -> list:
    """The anomalies, each led by its ordinal. An anomaly's time is NOT read: it is the time of the
    journal or transcript event that triggered it (TOOL-dLoggedFlight-22 S2). The model keeps it."""
    cols = derive_table("Anomalies", "anomalies")["cols"]
    return [[render_cell(ctx, c, v) for c, v in zip(cols, (str(i), a.get("kind"), a.get("subclass")))]
            for i, a in enumerate(m.get("anomalies") or [], 1)]


def build_coverage_rows(m, ctx) -> list:
    """One row per source, each led by its ordinal. A source's `epoch` is NOT read: it is the time of
    its journal's first line (TOOL-dLoggedFlight-22 S2). The model keeps it."""
    cols = derive_table("Coverage", "sources")["cols"]
    cov = m.get("coverage") or {}
    rows = []
    for i, name in enumerate(mdl.SOURCE_NAMES, 1):
        row = cov.get(name) or {}
        raw = (str(i), name, row.get("state"), derive_count(row.get("lines")), derive_count(row.get("bad")))
        rows.append([render_cell(ctx, c, v) for c, v in zip(cols, raw)])
    return rows


def build_aggregate(rows, keys, order, cols, ctx) -> list:
    """Rows counted by the cells at `keys`, in the order `order` gives each key, then `-` last."""
    counts = Counter(tuple(r[k] for k in keys) for r in rows)
    ranked = sorted(counts, key=lambda key: tuple((order[j].index(v) if v in order[j] else len(order[j]))
                                                   for j, v in enumerate(key)) + key)
    return [[render_cell(ctx, c, v) for c, v in zip(cols, (str(i),) + key + (str(counts[key]),))]
            for i, key in enumerate(ranked, 1)]


def build_summary_facts(m, ctx, serves, commitment) -> list:
    """The summary, one fixed template per line, never elided. `values withheld` is added last, by the
    caller, once every other value has been through its class."""
    cov = m.get("coverage") or {}
    pos = (m.get("owner_positions") or {}).get("counts") or {}
    usage = m.get("usage") or {}
    att = m.get("attribution") or {}
    # THE RENDERED WINDOW IS THE GIT-ONLY ONE (spec S2 of TOOL-dLoggedFlight-24): `record_window`,
    # every bound of which is a commit's committer time, so the record states a window a fresh clone
    # derives and the schema leg grades the derivation it renders. The model's journal-bounded
    # `window` is not read here at all: BOTH provenance facts come from `record_window` too (spec S1
    # of TOOL-dLoggedFlight-25), so the rendered bounds and the names of what set them are one
    # derivation. A model without the field renders both facts `-`, as any other absent value.
    start, close = derive_window_bounds(m.get("record_window"))
    dur = f"{int(close - start)}s" if start is not None and close >= start else None
    present = sum(1 for s in mdl.SOURCE_NAMES if (cov.get(s) or {}).get("state") == "present")
    # AN UNKNOWN COUNT IS `-`, never the zero that reads clean (spec S4). The owner turns, the usage
    # lines and the attributed calls come from the transcripts, and the model counts zero of what it
    # never read. M6 of the closing review, round 1: with the transcripts `not-local` the record said
    # `in-window 0`, a run that never asked, which is what the runlog Skill reads to answer "what did
    # it decide without asking".
    known = (cov.get("transcripts") or {}).get("state") in COUNTED_STATES

    def derive_known(value):
        return derive_count(value) if known else None

    values = {
        "run-state": (m.get("record"),),
        "run": (derive_count(m.get("run")), derive_count(m.get("runs"))),
        "start": (m.get("start_commit"),),
        "phase": (m.get("phase") or None,),
        "terminal": (derive_yes_no(m.get("terminal")),),
        "window": (mdl.derive_iso(start), mdl.derive_iso(close)),
        "window opened by": ((m.get("record_window") or {}).get("start_from"),),
        "window closed by": (derive_window_closer(m.get("record_window"), m.get("terminal")),),
        "duration": (dur,),
        "own commits": (str(len(m.get("own_commits") or [])),),
        "last own commit": (m.get("last_own"),),
        "merged": (derive_yes_no(m.get("merged")),),
        "units served": (str(len(serves)),),
        "sources present": (str(present), str(len(mdl.SOURCE_NAMES))),
        "owner turns": tuple(derive_known(pos.get(p, 0)) for p in mdl.OWNER_POSITIONS),
        "attributed calls": (derive_known(att.get("attributed", 0)), derive_known(att.get("calls", 0))),
    }
    for split in ex.SOURCES:
        values[f"usage {split}"] = tuple(derive_known((usage.get(split) or {}).get(f, 0)) for f in USAGE_FIELDS)
    facts = []
    for label, templates in RECORD_SCHEMA["sections"]["Summary"]["facts"]:
        if label == "values withheld":
            continue
        if label == "commitment":
            if commitment:
                facts.append((label, render_fact(ctx, templates[1], (
                    commitment.get("sha256"), derive_count(commitment.get("lines"))))))
            else:
                facts.append((label, templates[0]))
            continue
        facts.append((label, render_fact(ctx, templates[0], values[label])))
    return facts


def build_record_parts(model, memory_root=None, commitment=None) -> dict:
    """Everything a render needs that does not depend on the bounds, computed ONCE, so a render that has
    to halve its bounds counts each withheld value once."""
    m = derive_view(model)
    serves = derive_serves(m)
    if not serves:
        raise ValueError(f"runlog: {m.get('slug')} run {m.get('run')}: no spec-defined unit was dispatched "
                         "or closed, so no tracked record is written; an unbound record would move a "
                         "shrink-only pin")
    mr = memory_root if memory_root is not None else "memory"
    own = [u["id"] for u in m.get("units") or [] if u.get("id")]
    ctx = {"match": build_matchers(str(m.get("slug") or ""), mr, own), "forbidden": build_forbidden(),
           "withheld": 0}
    rows = {"timeline": build_timeline_rows(m, ctx), "units": build_unit_rows(m, ctx),
            "entries": build_entry_rows(m, ctx), "rounds": build_round_rows(m, ctx),
            "conformance": build_conformance_rows(m, ctx), "anomalies": build_anomaly_rows(m, ctx),
            "coverage": build_coverage_rows(m, ctx)}
    summary = build_summary_facts(m, ctx, serves, commitment)
    summary.insert(len(summary) - 1, ("values withheld", str(ctx["withheld"])))
    return {"m": m, "ctx": ctx, "serves": serves, "rows": rows, "summary": summary}


def build_record_doc(parts, edge, bound) -> dict:
    """The record as `{section: {"facts": [(label, text)], "tables": [table]}}` at ONE pair of bounds."""
    m, ctx, rows = parts["m"], parts["ctx"], parts["rows"]
    doc = {"Summary": {"facts": list(parts["summary"]), "tables": []}}

    tl = rows["timeline"]
    header = derive_table("Timeline", "events")["header"]
    shown = tl if len(tl) <= 2 * edge else (tl[:edge] + tl[-edge:] if edge else [])
    facts = [("events", f"{len(tl)} · shown {len(shown)} · elided {len(tl) - len(shown)}")]
    tables = []
    if len(shown) == len(tl):
        if tl:
            tables.append({"name": "events", "header": header, "rows": tl})
    else:
        gap = tl[edge:len(tl) - edge]
        facts.append(("elided", f"{len(gap)} events from {gap[0][0]} to {gap[-1][0]}"))
        if edge:
            tables += [{"name": "events", "header": header, "rows": tl[:edge]},
                       {"name": "events", "header": header, "rows": tl[-edge:]}]
    doc["Timeline"] = {"facts": facts, "tables": tables}

    units = rows["units"]
    agg = len(units) > bound
    t_units = derive_table("Units", "by-status" if agg else "units")
    body = (build_aggregate(units, (2,), (UNIT_STATUSES,), t_units["cols"], ctx) if agg else units)
    doc["Units"] = {"facts": [("units", f"{len(units)} · shown {0 if agg else len(units)} · aggregated "
                                        f"{'yes' if agg else 'no'}")],
                    "tables": [{"name": t_units["name"], "header": t_units["header"], "rows": body}] if body
                    else []}

    ledger = m.get("ledger") or {}
    counts = ledger.get("counts") or {}
    marks = ledger.get("marks") or {}
    excluded = Counter()
    for k, n in (ledger.get("excluded") or {}).items():
        excluded[k.split(" ", 1)[0]] += n
    entries, rounds = rows["entries"], rows["rounds"]
    agg_e, agg_r = len(entries) > bound, len(rounds) > bound
    facts = [("entries", f"{len(entries)} · shown {0 if agg_e else len(entries)} · aggregated "
                         f"{'yes' if agg_e else 'no'}"),
             ("trailer near-misses", render_fact(ctx, "{int}", (derive_count(ledger.get("near_miss", 0)),))),
             ("decision-log rows the owner's", render_fact(ctx, "{int}", (derive_count(ledger.get("owner_rows",
                                                                                                0)),))),
             ("spec marks", render_fact(ctx, derive_fact_templates("Decisions", "spec marks")[0], tuple(
                 derive_count(marks.get(k, 0)) for k in ("owner-before", "owner-inside", "agent-before",
                                                        "agent-inside")))),
             ("excluded rows", render_fact(ctx, derive_fact_templates("Decisions", "excluded rows")[0],
                                           tuple(derive_count(excluded.get(k, 0)) for k in EXCLUDED_KINDS))),
             ("review rounds", f"{len(rounds)} · shown {0 if agg_r else len(rounds)} · aggregated "
                               f"{'yes' if agg_r else 'no'}")]
    t_src = derive_table("Decisions", "by-source")
    tables = [{"name": "by-source", "header": t_src["header"],
               "rows": [[str(i), s, derive_count(counts.get(s, 0))] for i, s in enumerate(mdl.LEDGER_SOURCES, 1)]}]
    if entries and not agg_e:
        tables.append({"name": "entries", "header": derive_table("Decisions", "entries")["header"],
                       "rows": entries})
    if rounds:
        t_r = derive_table("Decisions", "rounds-by-verdict" if agg_r else "rounds")
        tables.append({"name": t_r["name"], "header": t_r["header"], "rows": build_aggregate(
            rounds, (2, 4), (REVIEW_VERDICTS, mdl.REVIEW_EXITS), t_r["cols"], ctx) if agg_r else rounds})
    doc["Decisions"] = {"facts": facts, "tables": tables}

    for section, key, name, agg_name, keys, order in (
            ("Conformance", "conformance", "items", "by-state", (1, 3),
             (mdl.CONFORMANCE_ITEMS, mdl.CONFORMANCE_STATES)),
            ("Anomalies", "anomalies", "anomalies", "by-kind", (1, 2),
             (mdl.ANOMALY_KINDS, mdl.MERGED_SUBCLASSES))):
        body = rows[key]
        agg = len(body) > bound
        table = derive_table(section, agg_name if agg else name)
        shown_rows = build_aggregate(body, keys, order, table["cols"], ctx) if agg else body
        label = RECORD_SCHEMA["sections"][section]["facts"][0][0]
        doc[section] = {"facts": [(label, f"{len(body)} · shown {0 if agg else len(body)} · aggregated "
                                          f"{'yes' if agg else 'no'}")],
                        "tables": [{"name": table["name"], "header": table["header"], "rows": shown_rows}]
                        if shown_rows else []}

    cov = m.get("coverage") or {}
    starts = cov.get("journal_starts") or {}
    tr = cov.get("transcripts") or {}
    idle = cov.get("idle") or {}
    doc["Coverage"] = {
        "facts": [("journal starts", render_fact(ctx, derive_fact_templates("Coverage", "journal starts")[0],
                                                 (derive_count(starts.get("joined", 0)),
                                                  derive_count(starts.get("record-creating", 0))))),
                  ("unjoined starts", str(len(cov.get("unjoined_starts") or []))),
                  ("sessions", render_fact(ctx, derive_fact_templates("Coverage", "sessions")[0],
                                           (derive_count(tr.get("sessions", 0)),
                                            derive_count(tr.get("extracts", 0))))),
                  ("idle gaps", render_fact(ctx, derive_fact_templates("Coverage", "idle gaps")[0],
                                            (derive_yes_no(idle.get("judged")),
                                             derive_count(idle.get("near_owner")))))],
        "tables": [{"name": "sources", "header": derive_table("Coverage", "sources")["header"],
                    "rows": rows["coverage"]}]}
    return doc


# ---------------------------------------------------------------------------------- the two copies

def render_twin(doc) -> str:
    """The `Data` block's JSON: the document re-encoded, one table row per line so a re-render diffs by
    row. It parses as ordinary JSON."""
    def render_json(v):
        return json.dumps(v, ensure_ascii=False, separators=(",", ":"))

    secs = []
    for name, sec in doc.items():
        tables = []
        for tb in sec["tables"]:
            rows = ",\n".join(render_json(r) for r in tb["rows"])
            tables.append('{"name":%s,"header":%s,"rows":[\n%s]}' % (render_json(tb["name"]),
                                                                     render_json(list(tb["header"])), rows))
        secs.append('%s:{"facts":%s,"tables":[%s]}' % (render_json(name), render_json(dict(sec["facts"])),
                                                        ",\n".join(tables)))
    return '{"schema":%d,"sections":{\n%s}}' % (RECORD_SCHEMA["schema"], ",\n".join(secs))


def render_markdown(doc, serves) -> str:
    out = [TITLE, "", f"**Serves:** {SERVES_KIND} {render_serves(serves)}", "", INTRO, ""]
    for name in RECORD_SCHEMA["headings"]:
        out += [f"## {name}", ""]
        if name == "Data":
            out += [DATA_OPEN, render_twin(doc), DATA_CLOSE]
            continue
        sec = doc[name]
        if sec["facts"]:
            out += [f"- {label}: {text}" for label, text in sec["facts"]] + [""]
        for tb in sec["tables"]:
            out.append("| " + " | ".join(tb["header"]) + " |")
            out.append("|" + "---|" * len(tb["header"]))
            out += ["| " + " | ".join(r) + " |" for r in tb["rows"]]
            out.append("")
    return "\n".join(out) + "\n"


def render_record(model, memory_root=None, commitment=None, bounds=None) -> str:
    """The record's bytes, as text. A pure function of the model: no git call and no file read.

    Raises ValueError when the run served no spec-defined unit, or when even every section
    aggregated and no timeline row shown cannot fit the cap.
    """
    parts = build_record_parts(model, memory_root, commitment)
    edge, bound = bounds or (TIMELINE_EDGE, LIST_BOUND)
    turn = 0
    while True:
        text = render_markdown(build_record_doc(parts, edge, bound), parts["serves"])
        if len(text.encode("utf-8")) <= RECORD_CAP_BYTES:
            return text
        if edge == 0 and bound == 0:
            raise ValueError(f"runlog: the record is {len(text.encode('utf-8'))} bytes with every section "
                             f"aggregated and no timeline row shown, over the {RECORD_CAP_BYTES}-byte cap")
        # The timeline's rows halve first, then the lists' bound, in turn: halving one side to nothing
        # before the other moved would drop the whole timeline to spare a list one aggregation.
        if (turn % 2 == 0 and edge > 0) or bound == 0:
            edge //= 2
        else:
            bound //= 2
        turn += 1


def write_record(root, model, journal_root=None, memory_root=None, date=None):
    """Render the run's record and write it into its build folder, through a temp file and contained
    under that build. Returns the path, or None when the run served no spec-defined unit, in which case
    nothing is written. `journal_root` None means no journal is read and the commitment is `none`."""
    m = derive_view(model)
    serves = derive_serves(m)
    if not serves:
        return None
    root = pathlib.Path(root)
    mr = memory_root if memory_root is not None else rl.resolve_memory_root(root)
    commitment = measure_commitment(m, journal_root) if journal_root is not None else None
    text = render_record(m, mr, commitment)
    path, _existed = resolve_record_path(root, m, serves, date, mr)
    base = (root / mr / "builds" / m["slug"]).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    if not ex._check_inside(path, base):
        raise ValueError(f"runlog: the record would land outside its build folder: {path}")
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    tmp.write_bytes(text.encode("utf-8"))
    os.replace(tmp, path)
    return path


# ---------------------------------------------------------------------------------- the commitment

def measure_commitment(model, journal_root, count=None) -> dict | None:
    """The sha256 and count of the journal lines the model attributed to the run.

    Each line is hashed as `<producer> TAB <its raw bytes> LF`, in time order. With `count`, this is the
    verify form: only the FIRST `count` lines of that order are hashed. A line the run appends after the
    render sorts past them and changes nothing; an edit, a deletion, or a line of the run inserted among
    them changes the hash. NO TIME IS RETURNED and none is committed: the count is the whole anchor, so
    a line earlier than every hashed one shifts the prefix and is REPORTED rather than absorbed, which
    is the direction an integrity check wants (spec S4). None when there is no line to hash.
    """
    m = derive_view(model)
    refs = m.get("journal_lines") or {}
    picked = []
    for rank, producer in enumerate(mdl.JOURNALS):
        nums = refs.get(producer) or []
        if not nums or journal_root is None:
            continue
        raw = (pathlib.Path(journal_root) / rl.PRODUCER_FILES[producer]).read_bytes().split(b"\n")
        for n in nums:
            if not 1 <= n <= len(raw):
                continue
            line = raw[n - 1]
            try:
                t = float(rl.parse_line(line.decode("utf-8"), n).fields["t"])
            except (UnicodeDecodeError, ValueError):
                continue
            picked.append((t, rank, n, producer, line))
    picked.sort()
    if count is not None:
        picked = picked[:count]
    if not picked:
        return None
    digest = hashlib.sha256()
    for _t, _rank, _n, producer, line in picked:
        digest.update(producer.encode("ascii") + b"\t" + line + b"\n")
    return {"sha256": digest.hexdigest(), "lines": len(picked)}


def parse_record(text) -> dict:
    """The record's `Data` twin, parsed. Raises ValueError naming what is missing or malformed."""
    lines = text.split("\n")
    try:
        at = lines.index("## Data")
        start = lines.index(DATA_OPEN, at)
        end = lines.index(DATA_CLOSE, start + 1)
    except ValueError:
        raise ValueError("runlog: the record carries no `## Data` heading with a fenced json block") from None
    try:
        doc = json.loads("\n".join(lines[start + 1:end]))
    except ValueError as exc:
        raise ValueError(f"runlog: the record's Data block is not JSON: {exc}") from None
    if not isinstance(doc, dict) or not isinstance(doc.get("sections"), dict):
        raise ValueError("runlog: the record's Data block carries no sections")
    return doc


def check_commitment(root, record_path, journal_root, memory_root=None) -> tuple:
    """`(state, detail)` for one record: `none`, `match` or `mismatch`, recomputed from this machine's
    journals. Raises ValueError for a record this cannot grade: unreadable, with no Data block, whose two
    copies disagree, whose run this clone cannot find, or whose journals are not on this machine."""
    root = pathlib.Path(root)
    path = pathlib.Path(record_path)
    mr = memory_root if memory_root is not None else rl.resolve_memory_root(root)
    try:
        text = path.read_bytes().decode("utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        raise ValueError(f"runlog: the record could not be read: {exc}") from None
    summary = (parse_record(text).get("sections", {}).get("Summary") or {}).get("facts") or {}
    in_md = next((ln[len("- commitment: "):] for ln in text.split("\n") if ln.startswith("- commitment: ")),
                 None)
    committed = summary.get("commitment")
    if committed is None or committed != in_md:
        raise ValueError(f"runlog: the record's two copies of its commitment disagree ({in_md!r} in the "
                         f"markdown, {committed!r} in its Data block)")
    if committed == "none":
        return "none", "commitment=none, so there is nothing to verify"
    cm = COMMITMENT_RE.fullmatch(committed)
    if cm is None:
        raise ValueError(f"runlog: the commitment line is not the schema's shape: {committed[:120]!r}")
    try:
        rel = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        raise ValueError(f"runlog: the record is not inside this repository: {path}") from None
    pm = re.fullmatch(re.escape(mr) + r"/builds/([^/]+)/build/[^/]+-" + RECORD_TAG + r"-([0-9a-f]{8})\.md", rel)
    start = str(summary.get("start") or "")
    if pm is None or not start.startswith(pm.group(2)):
        raise ValueError(f"runlog: {rel} is not a run record whose name carries its start's key")
    slug, key = pm.group(1), pm.group(2)
    runs = mdl.derive_run_starts(root, mr, [slug]).get(slug, [])
    k = next((r["k"] for r in runs if r["runkey"] == key), None)
    if k is None:
        raise ValueError(f"runlog: no run of {slug} in this clone's history starts at {key}")
    if journal_root is None or not any((pathlib.Path(journal_root) / rl.PRODUCER_FILES[p]).is_file()
                                       for p in mdl.JOURNALS):
        raise ValueError("runlog: no journal of this run is on this machine, so its commitment cannot be "
                         "recomputed here; it is checkable only on the node that produced it")
    model = mdl.build_run_model(root, slug, run=k, journal_root=journal_root)
    want = {"sha256": cm.group(1), "lines": int(cm.group(2))}
    now = measure_commitment(model, journal_root, count=want["lines"]) or {}
    bad = [f for f in ("sha256", "lines") if now.get(f) != want[f]]
    if bad:
        return "mismatch", ("the journal changed after the render: " + "; ".join(
            f"{f} committed {want[f]} and recomputed {now.get(f, 'nothing')}" for f in bad))
    return "match", f"{want['lines']} journal line(s) hash as committed"


# ---------------------------------------------------------------------------------- the schema leg

# THE LEG'S RULES (TOOL-dLoggedFlight-10 S2), a closed list: every refusal of a record names one. The
# first eight are the spec's list; `line`, `name` and `unreadable` are what a closed grammar implies.
RECORD_RULES = ("headings", "first-cell", "cell", "absolute-path", "uuid", "data", "size", "serves", "line",
                "name", "unreadable")
# A build's runs are refused under these, and the leg's own liveness assertions under the last two.
RUN_RULES = ("run-start", "run-window")
LIVENESS_RULES = ("root", "glob")
# The tracked glob the leg reads, as path SEGMENTS under the memory root, each matched with
# `fnmatchcase`, so a `*` never crosses a `/`. `check_records` holds it to `derive_record_relpath`.
RECORD_GLOB = ("builds", "*", "build", "*-" + RECORD_TAG + "-*.md")
# What a table row may lead with: a time, a sha or an ordinal, so no row leads with an id.
FIRST_CELL_CLASSES = ("utc", "sha", "int")
# How many refusals are printed per record. The COUNT is never capped; only the list is.
RECORD_REFUSALS_SHOWN = 20


def check_record_glob(rel, memory_root) -> str | None:
    """The build slug when `rel` is a path the leg's glob admits under the memory root, else None."""
    prefix = memory_root + "/"
    if not rel.startswith(prefix):
        return None
    parts = rel[len(prefix):].split("/")
    if len(parts) != len(RECORD_GLOB) or not all(fnmatch.fnmatchcase(p, g) for p, g in zip(parts, RECORD_GLOB)):
        return None
    return parts[1] or None


def read_index_entries(root, memory_root) -> list:
    """Every INDEX entry under the declared root, as `{mode, obj, stage, path}`. ONE `ls-files`, and the
    index rather than the working tree, so a pre-commit run grades the bytes about to be committed."""
    raw = mdl.run_git(root, ["ls-files", "-s", "-z", "--", f":(literal){memory_root}"])
    out = []
    for item in raw.split(b"\0"):
        meta, tab, path = item.partition(b"\t")
        bits = meta.decode("ascii", "replace").split()
        if not tab or len(bits) != 3:
            continue
        out.append({"mode": bits[0], "obj": bits[1], "stage": int(bits[2]) if bits[2].isdigit() else -1,
                    "path": path.decode("utf-8", "replace")})
    return out


def build_record_checks(slug, memory_root, own_ids) -> dict:
    """Every class of `RECORD_SCHEMA` as `(regex source, predicate)`, bound to ONE build.

    Compiled HERE from the schema's data, deliberately not taken from the renderer's `build_matchers`:
    the leg is the second enforcement point, and one that called the renderer's code would only confirm
    it. The regex sources feed the fact templates; the predicates grade each value whole.
    """
    out = {}
    for name, pat in RECORD_SCHEMA["shaped"].items():
        src = pat.replace("<root>", re.escape(memory_root)).replace("<slug>", re.escape(slug))
        out[name] = (src, re.compile(src).fullmatch)
    for name, members in RECORD_SCHEMA["vocab"].items():
        src = "|".join(re.escape(v) for v in sorted(members, key=len, reverse=True))
        out[name] = (src, frozenset(members).__contains__)
    own = frozenset(own_ids)
    unit_src, unit_rx = out["unit"]
    out["unit"] = (unit_src, lambda text: bool(unit_rx(text)) and text in own)
    out["units"] = (out["units"][0], lambda text: bool(text) and all(
        bool(unit_rx(t)) and t in own for t in text.split(" ")))
    out["none"] = ("(?!)", lambda text: False)
    return out


def check_cell(checks, cls, text) -> bool:
    """A cell's text is `-`, which every class admits because the renderer writes it for an absent or
    withheld value, or a value of its class."""
    return isinstance(text, str) and (text == NONE or checks[cls][1](text))


def check_fact_value(checks, templates, text) -> bool:
    """A fact's value matches one of its label's templates, each `{class}` filled by `-` or that class."""
    if not isinstance(text, str):
        return False
    for template in templates:
        parts = PLACEHOLDER_RE.split(template)
        classes = parts[1::2]
        rx = "".join(re.escape(p) if i % 2 == 0 else f"({re.escape(NONE)}|{checks[p][0]})"
                     for i, p in enumerate(parts))
        m = re.fullmatch(rx, text)
        if m and all(check_cell(checks, c, v) for c, v in zip(classes, m.groups())):
            return True
    return False


def check_table_row(ln, cells, table, checks) -> list:
    """Every refusal ONE table row earns: its first cell's shape, then each cell against its column's
    class, the timeline's columns classed by the event kind its key column names."""
    header = table["header"]
    if len(cells) != len(header):
        return [(ln, "cell", f"{len(cells)} cells under the {len(header)}-column `{table['name']}` header")]
    out = []
    if not any(checks[c][1](cells[0]) for c in FIRST_CELL_CLASSES):
        out.append((ln, "first-cell", "the row leads with neither a timestamp, a sha nor an ordinal"))
    if "rows" in table:
        classes = table["rows"].get(cells[table["key"]])
        if classes is None:
            out.append((ln, "cell", f"column `{header[table['key']]}` names an event kind the schema does "
                                    "not declare"))
            return out
    else:
        classes = table["cols"]
    for col, (cls, cell) in enumerate(zip(classes, cells)):
        if not check_cell(checks, cls, cell):
            out.append((ln, "cell", f"column `{header[col]}` holds a value outside the `{cls}` class"))
    return out


def scan_forbidden(lines) -> list:
    """`(line, rule, why)` for every line carrying a forbidden shape, read from `RECORD_SCHEMA` and
    compiled here. The shape itself is never echoed, only where it sits."""
    rules = [(rule, re.compile(p)) for rule, p in RECORD_SCHEMA["forbidden"].items()]
    out = []
    for ln, line in enumerate(lines, 1):
        for rule, rx in rules:
            m = rx.search(line)
            if m:
                out.append((ln, rule, f"a forbidden shape at column {m.start() + 1}"))
    return out


def check_serves_line(ln, line, slug, own_ids) -> list:
    """The head's binding line: `**Serves:** journal <ids>`, every id one a spec of THIS build defines."""
    m = re.fullmatch(r"\*\*Serves:\*\* (\S+) (.+)", line or "")
    if m is None:
        return [(ln, "serves", "the head's third line is not `**Serves:** <kind> <ids>`")]
    out = []
    if m.group(1) != SERVES_KIND:
        out.append((ln, "serves", f"the binding kind is not `{SERVES_KIND}`"))
    for tok in m.group(2).split(" "):
        r = re.fullmatch(r"([A-Z]+)-([A-Za-z0-9]+)-([0-9]+)(?:\.\.([0-9]+))?", tok)
        if r is None:
            out.append((ln, "serves", "a token that is neither a unit id nor an id range"))
            continue
        fam, s, lo = r.group(1), r.group(2), int(r.group(3))
        hi = int(r.group(4)) if r.group(4) else lo
        if s != slug:
            out.append((ln, "serves", f"an id of the build `{s}`, outside the record's own build `{slug}`"))
            continue
        if hi < lo or hi - lo > len(own_ids):
            out.append((ln, "serves", "an id range that runs backwards or past every unit the build defines"))
            continue
        missing = [f"{fam}-{s}-{n}" for n in range(lo, hi + 1) if f"{fam}-{s}-{n}" not in own_ids]
        if missing:
            out.append((ln, "serves", f"{len(missing)} id(s) no spec of `{slug}` defines, the first "
                                      f"{missing[0]}"))
    return out


def parse_json_pairs(pairs):
    """A JSON object that REFUSES a repeated key: `json.loads` keeps the last value silently, so a
    hand-edited twin could carry text in a key the parser throws away and the bytes keep."""
    seen = {}
    for k, v in pairs:
        if k in seen:
            raise ValueError("an object repeats a key, and the parser would keep only its last value")
        seen[k] = v
    return seen


def check_record_data(json_lines, fence_ln, checks) -> list:
    """The `Data` block: JSON, with exactly the schema's keys at every level, each value in its class."""
    if any("\\" in text for _, text in json_lines):
        ln = next(n for n, text in json_lines if "\\" in text)
        return [(ln, "data", "a JSON escape, which no value the schema admits needs")]
    try:
        doc = json.loads("\n".join(t for _, t in json_lines), object_pairs_hook=parse_json_pairs)
    except ValueError as exc:
        n = getattr(exc, "lineno", None)
        ln = json_lines[n - 1][0] if n and 0 < n <= len(json_lines) else fence_ln
        return [(ln, "data", f"the Data block is not JSON the schema admits: {getattr(exc, 'msg', exc)}")]

    def resolve_line(needle) -> int:
        return next((n for n, text in json_lines if needle in text), fence_ln)

    if not isinstance(doc, dict) or list(doc) != ["schema", "sections"]:
        return [(fence_ln, "data", "the top level carries keys other than `schema` and `sections`, in order")]
    out = []
    if doc["schema"] != RECORD_SCHEMA["schema"]:
        out.append((resolve_line('"schema"'), "data", f"schema is not {RECORD_SCHEMA['schema']}"))
    secs = doc["sections"]
    want = [h for h in RECORD_SCHEMA["headings"] if h != "Data"]
    if not isinstance(secs, dict) or list(secs) != want:
        out.append((resolve_line('"sections"'), "data", "the sections are not the schema's set and order"))
    for name, sec in (secs.items() if isinstance(secs, dict) else ()):
        spec = RECORD_SCHEMA["sections"].get(name)
        if spec is None or name == "Data":
            continue
        at = resolve_line(json.dumps(name) + ":")
        if not isinstance(sec, dict) or list(sec) != ["facts", "tables"]:
            out.append((at, "data", f"section `{name}` carries keys other than `facts` and `tables`"))
            continue
        declared = dict(spec["facts"])
        facts = sec["facts"] if isinstance(sec["facts"], dict) else None
        if facts is None:
            out.append((at, "data", f"section `{name}`'s facts are not an object"))
        for label, value in (facts or {}).items():
            if label not in declared:
                out.append((at, "data", f"section `{name}` carries a fact key the schema does not declare"))
            elif not check_fact_value(checks, declared[label], value):
                out.append((at, "cell", f"the `{label}` fact's twin value matches none of its templates"))
        tables = sec["tables"] if isinstance(sec["tables"], list) else None
        if tables is None:
            out.append((at, "data", f"section `{name}`'s tables are not a list"))
        for tb in tables or ():
            decl = next((t for t in spec["tables"] if isinstance(tb, dict) and t["name"] == tb.get("name")), None)
            if not isinstance(tb, dict) or list(tb) != ["name", "header", "rows"] or decl is None:
                out.append((at, "data", f"a table in section `{name}` is not a declared name, header and rows"))
                continue
            if tb["header"] != list(decl["header"]):
                out.append((resolve_line(json.dumps(tb["name"])), "data", f"table `{decl['name']}`'s header is not "
                                                                    "the declared one"))
            if not isinstance(tb["rows"], list):
                out.append((at, "data", f"table `{decl['name']}`'s rows are not a list"))
                continue
            for row in tb["rows"]:
                if not isinstance(row, list) or not all(isinstance(c, str) for c in row):
                    out.append((at, "data", f"a row of table `{decl['name']}` is not a list of strings"))
                    continue
                out += check_table_row(resolve_line(json.dumps(row, ensure_ascii=False, separators=(",", ":"))),
                                       row, decl, checks)
    return out


def check_record_lines(lines, checks, slug, own_ids) -> list:
    """The record grammar, line by line: the fixed head, the declared headings in order, each section's
    declared facts before its declared tables, and one fenced JSON block under `## Data`."""
    out = [(ln, "line", "a CR byte; the renderer writes LF only") for ln, line in enumerate(lines, 1)
           if "\r" in line]
    lines = [line.replace("\r", "") for line in lines]
    for i, want in enumerate((TITLE, "", None, "", INTRO, "")):
        got = lines[i] if i < len(lines) else None
        if want is None:
            out += check_serves_line(i + 1, got, slug, own_ids)
        elif got != want:
            out.append((i + 1, "line", "the record's head is fixed text, and this line departs from it"))
    headings, sec, spec, labels, table, started = [], None, None, [], None, False
    data_state, fence_ln, json_lines = None, 0, []
    last = len(lines) - 1 if lines and lines[-1] == "" else len(lines)
    for idx in range(min(6, len(lines)), last):
        ln, line = idx + 1, lines[idx]
        if data_state == "open":
            if line == DATA_CLOSE:
                data_state = "closed"
            else:
                json_lines.append((ln, line))
            continue
        if line.startswith("## "):
            headings.append((ln, line[3:]))
            sec = line[3:] if line[3:] in RECORD_SCHEMA["sections"] else None
            spec = RECORD_SCHEMA["sections"].get(sec) if sec else None
            labels, table, started = [], None, False
            continue
        if line == "":
            table = None
            continue
        if sec is None:
            out.append((ln, "line", "a line under no declared heading"))
            continue
        if sec == "Data":
            if data_state is None and line == DATA_OPEN:
                data_state, fence_ln = "open", ln
            else:
                out.append((ln, "line", "a line under `## Data` outside its one fenced json block"))
            continue
        if line.startswith("|"):
            started = True
            if table is None:
                cells = line[2:-2].split(" | ") if line.startswith("| ") and line.endswith(" |") else None
                decl = next((t for t in spec["tables"] if cells is not None and tuple(cells) == tuple(t["header"])),
                            None)
                table = {"decl": decl, "sep": False}
                if decl is None:
                    out.append((ln, "cell", f"a table header section `{sec}` declares no table for"))
                continue
            if table["decl"] is None:
                out.append((ln, "cell", "a row of an undeclared table"))
                continue
            if not table["sep"]:
                table["sep"] = True
                if line != "|" + "---|" * len(table["decl"]["header"]):
                    out.append((ln, "line", "a table header is not followed by its separator row"))
                continue
            if not (line.startswith("| ") and line.endswith(" |")):
                out.append((ln, "line", "a table row not framed `| … |`"))
                continue
            out += check_table_row(ln, line[2:-2].split(" | "), table["decl"], checks)
            continue
        if line.startswith("- "):
            label, sep, value = line[2:].partition(": ")
            order = [name for name, _ in spec["facts"]]
            if not sep:
                out.append((ln, "line", "a list line that is not `- <label>: <value>`"))
            elif started:
                out.append((ln, "line", "a fact after a table; a section's facts come first"))
            elif label not in order:
                out.append((ln, "cell", f"a fact label section `{sec}` does not declare"))
            elif label in labels or (labels and order.index(label) < order.index(labels[-1])):
                out.append((ln, "cell", f"the `{label}` fact repeated or out of its declared order"))
            elif not check_fact_value(checks, dict(spec["facts"])[label], value):
                out.append((ln, "cell", f"the `{label}` fact's value matches none of its templates"))
            if sep and label in order:
                labels.append(label)
            continue
        out.append((ln, "line", "free text: neither a heading, a fact nor a table row"))
    names = [name for _, name in headings]
    want = list(RECORD_SCHEMA["headings"])
    if names != want:
        j = next((i for i, (a, b) in enumerate(zip(names, want)) if a != b), min(len(names), len(want)))
        ln = headings[j][0] if j < len(headings) else len(lines)
        wanted = f"`{want[j]}`" if j < len(want) else "the end of the record"
        out.append((ln, "headings", f"the headings depart from the schema's set and order at heading {j + 1}, "
                                    f"where {wanted} belongs"))
    if data_state is None:
        out.append((len(lines), "data", "no fenced json block under `## Data`"))
    elif data_state == "open":
        out.append((fence_ln, "data", "the Data block's fence is never closed"))
    else:
        out += check_record_data(json_lines, fence_ln, checks)
    return out


def check_record(rel, data, slug, own_ids, memory_root) -> list:
    """Every refusal ONE record's staged bytes earn, as sorted `(line, rule, why)`, graded against
    `RECORD_SCHEMA` alone. Line 0 is the record as a whole."""
    out = []
    name = rel.rsplit("/", 1)[-1]
    if RECORD_NAME_RE.fullmatch(name) is None:
        out.append((0, "name", "the glob admits this name, and the renderer would never write it"))
    cap = RECORD_SCHEMA["cap_bytes"]
    if len(data) > cap:
        out.append((data[:cap].count(b"\n") + 1, "size", f"{len(data)} bytes, over the {cap}-byte cap, "
                                                         "which this line crosses"))
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        out.append((data[:exc.start].count(b"\n") + 1, "unreadable", "the bytes are not UTF-8"))
        return sorted(out)
    lines = text.split("\n")
    out += scan_forbidden(lines)
    out += check_record_lines(lines, build_record_checks(slug, memory_root, own_ids), slug, own_ids)
    return sorted(set(out))


def check_run_states(root, memory_root, tracked, texts) -> dict:
    """S6: every tracked run's start and window, from git alone, as a fresh clone must derive them.

    `tracked` is the index's path set and `texts` each tracked run-state file's staged text. Three git
    calls whatever the number of builds: `derive_run_starts`'s one log over the population, one log
    over the run-state paths, and one batch read of the terminal runs' record writes. The window is the
    model's own derivation, read through `derive_record_commits` and `derive_window`, never a copy. It
    hands `derive_window` the record commits alone, so a non-terminal end here is at or before the
    model's, which also reads the run's own commits and journals (TOOL-dLoggedFlight-10 S6). Neither
    refusal reads that end: a non-terminal run is its build's last, since a preflight rotates only a
    terminal record.
    """
    runs_by = mdl.derive_run_starts(root, memory_root, None, tracked=tracked)
    live = {f"{memory_root}/builds/{slug}/RUN.md" for slug in runs_by}
    history = mdl.read_git_range(root, ["HEAD"], paths=[f"{memory_root}/builds/*/RUN.md"]) if runs_by else []
    by_path: dict = {}
    for c in history:
        for p in {p for _s, p in c["files"] if p in live}:
            by_path.setdefault(p, []).append(c)
    plan, requests = [], []
    for slug, runs in sorted(runs_by.items()):
        live_path = f"{memory_root}/builds/{slug}/RUN.md"
        for run, era in zip(runs, mdl.derive_run_eras(runs)):
            commits = mdl.derive_record_commits(by_path.get(live_path, []), era, live_path)
            terminal = mdl.derive_phase(texts.get(run["record"])) in mdl.PHASES_TERMINAL
            plan.append((slug, live_path, run, commits, terminal))
            if terminal:
                requests += [f"{c['sha']}:{live_path}" for c in commits]
    blobs = mdl.read_blobs(root, requests)
    windows: dict = {}
    for slug, live_path, run, commits, terminal in plan:
        phases = [(c, mdl.derive_phase(blobs.get(f"{c['sha']}:{live_path}")) if terminal else None)
                  for c in commits]
        windows.setdefault(slug, []).append((run, mdl.derive_window(float(run["t"]), "git", phases, terminal)))
    refusals, builds = [], []
    for slug, pairs in sorted(windows.items()):
        by_start: dict = {}
        for run, _w in pairs:
            by_start.setdefault(run["start"], []).append(run["k"])
        shared = {s: ks for s, ks in by_start.items() if len(ks) > 1}
        for s, ks in sorted(shared.items()):
            why = (f"runs {', '.join(map(str, ks))} share the start commit {s[:8]}, so their keys and windows "
                   "collapse into one")
            # The shape a squashed history or a moved memory root leaves, named so the refusal says
            # what it saw (L3 of the closing review, round 1); spec 8's S1 owns the shape.
            if any(run.get("joint_add") for run, _w in pairs if run["start"] == s):
                why += (f"; {s[:8]} added the live record and an archive together, the shape a squashed "
                        "history or a memory root or build folder moved in one commit leaves, and nothing "
                        "here follows a path back past it")
            refusals.append((slug, "run-start", why))
        backwards = [(run, w) for run, w in pairs if w["end"] < w["start"]]
        for run, w in backwards:
            refusals.append((slug, "run-window", f"run {run['k']}'s window ends at {mdl.derive_iso(w['end'])}, "
                                                 f"before it starts at {mdl.derive_iso(w['start'])}"))
        overlaps = [(a, b) for a, b in itertools.combinations(pairs, 2)
                    if a[1]["start"] < b[1]["end"] and b[1]["start"] < a[1]["end"]]
        for (ra, wa), (rb, wb) in overlaps:
            refusals.append((slug, "run-window", f"runs {ra['k']} and {rb['k']} overlap, "
                                                 f"[{mdl.derive_iso(wa['start'])}, {mdl.derive_iso(wa['end'])}) and "
                                                 f"[{mdl.derive_iso(wb['start'])}, {mdl.derive_iso(wb['end'])})"))
        builds.append({"slug": slug, "runs": [(run["k"], run["start"], w) for run, w in pairs],
                       "distinct": not shared, "ordered": not backwards, "disjoint": not overlaps})
    return {"builds": builds, "refusals": refusals, "runs": sum(len(p) for p in windows.values())}


def check_records(root, memory_root=None) -> dict:
    """The schema leg (TOOL-dLoggedFlight-10): every committed run record graded, and every run's start
    and window, over the INDEX, in five git calls whatever the population.

    The population is every tracked `<memory root>/builds/*/build/*-runlog-*.md`, read from the index,
    so a pre-commit run grades the bytes about to be committed. Two liveness assertions keep an empty
    population honest: the declared root must hold tracked files (`root`), and the glob must admit the
    path the renderer's own `derive_record_relpath` builds (`glob`). A record the index holds unmerged,
    or as anything but a regular file, is refused as `unreadable`, never skipped.

    WHAT THIS DOES NOT CHECK. Whether a record's values are TRUE: a count can be wrong and still be an
    integer, and a sha can name a commit the run never made. Whether the Data twin AGREES with the
    markdown: each copy is graded on its own. Whether a record's run exists, or its name's key is that
    run's start. Records in any other folder or under any other name, which the glob never reads. A run
    on a branch HEAD has not merged, since the starts are read from HEAD. A window's END against the
    commit graph: windows are compared in commit time, so a clock skew between two nodes that puts a
    predecessor's terminal write after its successor's start moves a window without redding it. A
    history that moved its memory root or a build folder: the starts are read under the current root
    with renames off, so the move ADDS every record it carries and a rotated build's runs all start at
    it. The `run-start` refusal names that shape and no waiver clears it; nothing follows the path back.

    Raises ValueError when the memory root refuses or git cannot be run, which the command makes exit 2.
    """
    t0 = time.perf_counter()
    calls0 = mdl.GIT_CALLS[0]
    root = pathlib.Path(root)
    mr = memory_root if memory_root is not None else rl.resolve_memory_root(root)
    out = {"root": mr, "glob": "/".join((mr,) + RECORD_GLOB), "records": [], "refusals": [], "liveness": [],
           "run_state": None, "pending": 0, "git_calls": 0, "wall_s": 0.0}
    probe = derive_record_relpath(mr, "xProbe", "2000-01-01", "X-xProbe-1", "0" * 8)
    if check_record_glob(probe, mr) is None:
        out["liveness"].append(("glob", f"the glob {out['glob']} does not admit {probe}, the path the "
                                        "renderer writes, so it would grade a population the renderer "
                                        "never produces"))
    entries = read_index_entries(root, mr)
    if not entries:
        out["liveness"].append(("root", f"the declared memory root {mr} holds no tracked file, so an empty "
                                        "population would be a wrong root rather than a clean one"))
    records, specs, run_files = {}, {}, {}
    for e in entries:
        slug = check_record_glob(e["path"], mr)
        rest = e["path"][len(mr) + 1:].split("/")
        if slug is not None:
            records.setdefault(e["path"], (slug, []))[1].append(e)
        elif len(rest) == 4 and rest[0] == "builds" and rest[2] == "spec" and rest[3].endswith(".md"):
            specs.setdefault(rest[1], []).append(e)
        elif len(rest) == 3 and rest[0] == "builds" and (rest[2] == "RUN.md" or mdl.ARCHIVE_RE.fullmatch(rest[2])):
            run_files[e["path"]] = e
    with_records = {slug for slug, _ in records.values()}
    wanted = [e["obj"] for _p, (_s, es) in records.items() for e in es if e["stage"] == 0]
    wanted += [e["obj"] for slug in with_records for e in specs.get(slug, []) if e["stage"] == 0]
    wanted += [e["obj"] for e in run_files.values() if e["stage"] == 0]
    blobs = mdl.read_blobs(root, wanted, decode=False)
    own = {}
    for slug in with_records:
        id_re = mdl.build_unit_id_re(slug)
        units = (mdl.derive_spec_unit((blobs.get(e["obj"]) or b"").decode("utf-8", "replace"), id_re)
                 for e in specs.get(slug, []))
        own[slug] = {u["id"] for u in units if u}
    for rel, (slug, es) in sorted(records.items()):
        out["records"].append(rel)
        e = es[0]
        if len(es) != 1 or e["stage"] != 0:
            found = [(0, "unreadable", "the index holds this record unmerged, so no one set of bytes is staged")]
        elif e["mode"] not in ("100644", "100755"):
            found = [(0, "unreadable", "the index holds this record as something other than a regular file")]
        elif blobs.get(e["obj"]) is None:
            found = [(0, "unreadable", "the staged blob could not be read")]
        else:
            found = check_record(rel, blobs[e["obj"]], slug, own.get(slug, set()), mr)
        out["refusals"] += [(rel, ln, rule, why) for ln, rule, why in found]
    if run_files:
        texts = {p: (blobs.get(e["obj"]) or b"").decode("utf-8", "replace") for p, e in run_files.items()}
        out["run_state"] = check_run_states(root, mr, set(run_files), texts)
        out["pending"] = len(run_files) - out["run_state"]["runs"]
    out["git_calls"] = mdl.GIT_CALLS[0] - calls0
    out["wall_s"] = round(time.perf_counter() - t0, 3)
    return out


def render_check_report(result) -> tuple:
    """`(lines, rc)`: what the leg prints, and 0 for a graded population with no refusal, else 1."""
    lines = []
    for rule, why in result["liveness"]:
        lines.append(f"runlog: check-records REFUSED — {rule} — {why}")
    n = len(result["records"])
    shown = Counter()
    refused = {rel for rel, *_ in result["refusals"]}
    for rel, ln, rule, why in result["refusals"]:
        shown[rel] += 1
        if shown[rel] <= RECORD_REFUSALS_SHOWN:
            lines.append(f"runlog: {rel}:{ln} refused — {rule} — {why}")
    for rel, count in sorted(shown.items()):
        if count > RECORD_REFUSALS_SHOWN:
            lines.append(f"runlog: {rel}: {count - RECORD_REFUSALS_SHOWN} more refusal(s) not listed")
    if n == 0:
        lines.append(f"runlog: check-records 0 records (none committed yet) under {result['glob']}")
    else:
        lines.append(f"runlog: check-records {n} record{'s' if n != 1 else ''} under {result['glob']} · "
                     f"{len(refused)} refused · {len(result['refusals'])} refusal(s)")
    rs = result["run_state"]
    run_refusals = rs["refusals"] if rs else []
    if rs:
        rotated = [b for b in rs["builds"] if len(b["runs"]) > 1]
        lines.append(f"runlog: check-records run-state {len(rs['builds'])} builds · {rs['runs']} runs · "
                     f"{len(rotated)} rotated · {result['pending']} run-state file(s) not yet committed")
        for b in rotated:
            starts = " ".join(s[:8] for _k, s, _w in b["runs"])
            spans = " ".join(f"[{mdl.derive_iso(w['start'])}, {mdl.derive_iso(w['end'])})" for _k, _s, w in b["runs"])
            lines.append(f"runlog: check-records run-state {b['slug']} · {len(b['runs'])} runs · starts {starts} · "
                         f"{'distinct' if b['distinct'] else 'SHARED'} · windows {spans} · "
                         f"{'each ends at or after its start' if b['ordered'] else 'one ends BEFORE its start'} · "
                         f"{'disjoint' if b['disjoint'] else 'OVERLAPPING'}")
        for slug, rule, why in run_refusals:
            lines.append(f"runlog: check-records run-state {slug} refused — {rule} — {why}")
    else:
        lines.append("runlog: check-records run-state 0 builds: no run-state file is tracked under the root")
    lines.append(f"runlog: check-records git_calls={result['git_calls']} wall={result['wall_s']}s "
                 "(report-only, grades nothing)")
    bad = bool(result["liveness"] or result["refusals"] or run_refusals)
    lines.append(f"runlog: check-records {'RED' if bad else 'GREEN'}")
    return lines, 1 if bad else 0
