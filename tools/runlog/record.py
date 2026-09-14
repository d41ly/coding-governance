#!/usr/bin/env python3
"""record.py — one run's committed record: a closed-schema report and its JSON twin. gov:kit runlog@1.0

A run's model is machine-local, and most runs are made on some other node. This renders the model into
ONE tracked record in the build folder, under the declared memory root, that every node can read. The
repository is public, so the record is STRUCTURAL ONLY: every value in it is drawn from `RECORD_SCHEMA`,
a closed set of value classes. Some are shaped, such as a UTC timestamp, a verb token or a sha. The rest
are closed vocabularies, such as the coverage states. No free text, absolute path, session id, host id
or command can reach the file, because nothing reaches it except through a class. A model value outside
its field's class is written `-`, which also stands for an absent value, and the summary's `values
withheld` line counts every one, so a model that grew a value the schema does not admit says so.

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

THE COMMITMENT makes a later edit to the journal detectable on the node that holds it: the sha256, the
line count and the first and last times of the journal lines the MODEL attributed to the run, read from
its `journal_lines` and never re-joined here. `check_commitment` rebuilds the model and hashes the
committed number of lines from the committed first time on, so a line the run appends after the render
is not an edit.

WHAT THIS DOES NOT DO. It makes no git call: the model's calls are the whole cost, and rendering is a
pure function of the model. It does not judge whether a value is TRUE, only that it is in its class. It
does not choose when a record is rendered; the unattended Skill's step does. And it names nothing
outside this kit by literal: the memory root is resolved, and the build-index generator is found beside
this kit by its file name.
"""
from __future__ import annotations

import dataclasses
import datetime
import hashlib
import json
import os
import pathlib
import re
import sys
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

# THREE LISTS ANOTHER FILE OWNS, COPIED, because a kit reads no sibling at run time. The withheld
# self-test holds each to its owner in both directions where the owner is present: the spec status
# tokens to the spec template, the push decisions to the pre-push hook, whose three pre-loop refusals
# and seven END decisions they are, and the review verdicts to the hygiene doc's check 22. A value
# outside a copy is withheld like any other, never guessed at.
UNIT_STATUSES = ("OPEN", "SPECCED", "INPROGRESS", "BLOCKED", "DEFERRED", "CLOSED", "WONTDO")
PUSH_DECISIONS = ("refuse-default-branch", "skip-nondefault", "skip-delete", "refuse-manifest",
                  "refuse-raw", "refuse-head", "full", "scoped")
REVIEW_VERDICTS = ("CLEAN", "CLEAN WITH FIXES", "BLOCKED")
# The gate verdicts are the spec's own list (S4): the runner writes GREEN, RED and NONE, and REFUSED is
# declared for a refusal line; a verdict outside it is withheld and counted.
GATE_VERDICTS = ("GREEN", "RED", "REFUSED", "NONE")
# The timeline's event kinds. `owner` is deliberately absent: owner turns are counts per position and
# never clock times, so the renderer drops them from the timeline before a row is built.
TIMELINE_EVENTS = ("phase", "verb", "commit", "merge", "push", "push-refused", "gate", "dispatch",
                   "brief", "compact", "limit", "idle", "workflow")
EXCLUDED_KINDS = tuple(k for k in mdl.PARK_KINDS if k not in mdl.PARK_KINDS_OWED)
USAGE_FIELDS = ("requests", "in", "out", "cache_read", "cache_write")
DATE_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
RECORD_NAME_RE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}-build-([A-Z]+-[A-Za-z0-9]+-[0-9]+)-"
                            + RECORD_TAG + r"-([0-9a-f]{8})\.md")
UNIT_ID_RE = re.compile(r"([A-Z]+)-([A-Za-z0-9]+)-([0-9]+)")
PLACEHOLDER_RE = re.compile(r"\{([a-z-]+)\}")
COMMITMENT_RE = re.compile(r"sha256 ([0-9a-f]{64}) · lines ([0-9]+) · first (\S+) · last (\S+)")

_PATH_SEG = r"[A-Za-z0-9][A-Za-z0-9._-]*"
_PATH = r"<root>/builds/<slug>/(?:" + _PATH_SEG + r"/)*" + _PATH_SEG + r"\.md"
_UNIT = r"[A-Z]+-<slug>-[0-9]+"
_WINDOW_USAGE = "requests {int} · in {int} · out {int} · cache-read {int} · cache-write {int}"

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
        "verb": r"--[a-z-]{2,20}",
        "phase": r"[A-Z]{3,12}",
        "checks": r"[0-9]{1,3}(?:,[0-9]{1,3})*",
        "label": r"[a-z0-9-]{1,40}",
        "unit": _UNIT,
        "units": _UNIT + r"(?: " + _UNIT + r")*",
        "path": _PATH,
        "ref": r"(?:" + _PATH + r"(?::[0-9]{1,7})?|[0-9a-f]{7,40})",
    },
    "vocab": {
        "yes-no": ("yes", "no"),
        "opened-by": ("driver", "git"),
        "closed-by": ("terminal-end", "terminal-write", "last-activity"),
        "event": TIMELINE_EVENTS,
        "source": mdl.SOURCE_NAMES,
        "coverage-state": mdl.COVERAGE_STATES,
        "ledger-source": mdl.LEDGER_SOURCES,
        "owner-position": mdl.OWNER_POSITIONS,
        "gate-verdict": GATE_VERDICTS,
        "push-decision": PUSH_DECISIONS,
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
                ("commitment", ("none", "sha256 {digest} · lines {int} · first {utc} · last {utc}")),
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
                     "verb": ("utc", "source", "event", "verb", "phase", "int", "checks"),
                     "commit": ("utc", "source", "event", "sha", "none", "none", "units"),
                     "merge": ("utc", "source", "event", "sha", "none", "none", "units"),
                     "push": ("utc", "source", "event", "push-decision", "none", "int", "yes-no"),
                     "push-refused": ("utc", "source", "event", "push-decision", "none", "none", "yes-no"),
                     "gate": ("utc", "source", "event", "gate-verdict", "none", "int", "sha"),
                     "dispatch": ("utc", "source", "event", "unit", "none", "none", "none"),
                     "brief": ("utc", "source", "event", "unit", "none", "none", "none"),
                     "compact": ("utc", "source", "event", "none", "none", "none", "none"),
                     "limit": ("utc", "source", "event", "none", "none", "none", "none"),
                     "idle": ("utc", "none", "event", "duration", "none", "none", "none"),
                     "workflow": ("utc", "source", "event", "label", "none", "none", "none"),
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
                {"name": "anomalies", "header": ("#", "UTC", "kind", "subclass"),
                 "cols": ("int", "utc", "anomaly-kind", "merged-subclass")},
                {"name": "by-kind", "header": ("#", "kind", "subclass", "count"),
                 "cols": ("int", "anomaly-kind", "merged-subclass", "int")},
            ),
        },
        "Coverage": {
            "facts": (
                ("journal starts", ("{int} joined of {int} record-creating",)),
                ("unjoined starts", ("{int}",)),
                ("sessions", ("{int} named · {int} extracted",)),
            ),
            "tables": (
                {"name": "sources", "header": ("#", "source", "state", "lines", "bad", "epoch"),
                 "cols": ("int", "source", "coverage-state", "int", "int", "utc")},
            ),
        },
        "Data": {"facts": (), "tables": ()},
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


def render_cell(ctx, cls, value) -> str:
    """ONE value through its class: itself when it belongs, `-` when it is absent or does not, and a
    value that does not belong is counted as withheld."""
    if cls == "none" or value is None or value == "" or value == [] or value == NONE:
        return NONE
    text = str(value)
    if ctx["match"][cls](text):
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
    folder = root / mr / "builds" / m["slug"] / "build"
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
    day = date or datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    if not DATE_RE.fullmatch(str(day)):
        raise ValueError(f"runlog: {str(day)[:40]!r} is not a YYYY-MM-DD render date")
    return folder / f"{day}-build-{serves[0]}-{RECORD_TAG}-{key}.md", False


# ---------------------------------------------------------------------------------- the rows

def derive_timeline_values(e) -> tuple:
    """One timeline event as the seven raw column values its kind declares; `render_cell` classes them."""
    kind = e.get("kind")
    head = (mdl.derive_iso(e.get("t")), e.get("source"), kind)
    if kind == "phase":
        return head + (derive_short_sha(e.get("witness")), e.get("phase"), None, None)
    if kind == "verb":
        # The phase the verb left, or, for a verb with no END, the phase it found.
        return head + (e.get("verb"), e.get("phase_to") or e.get("phase_from"), e.get("rc"),
                       ",".join(e.get("checks") or []))
    if kind in ("commit", "merge"):
        return head + (derive_short_sha(e.get("sha")), None, None, " ".join(e.get("units") or []))
    if kind == "push":
        return head + (e.get("decision"), None, e.get("rc"), derive_yes_no(e.get("lander")))
    if kind == "push-refused":
        return head + (e.get("decision"), None, None, derive_yes_no(e.get("lander")))
    if kind == "gate":
        return head + (e.get("verdict"), None, e.get("rc"), derive_short_sha(e.get("head")))
    if kind in ("dispatch", "brief"):
        return head + (e.get("unit"), None, None, None)
    if kind == "idle":
        dur = e.get("dur")
        return head + (f"{int(dur)}s" if isinstance(dur, (int, float)) and dur >= 0 else dur, None, None,
                       None)
    if kind == "workflow":
        return head + (e.get("label"), None, None, None)
    return head + (None, None, None, None)


def build_timeline_rows(m, ctx) -> list:
    spec = derive_table("Timeline", "events")["rows"]
    rows = []
    for e in m.get("timeline") or []:
        kind = e.get("kind")
        if kind == "owner":
            continue      # owner turns are counts per position, never clock times (spec S4)
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
    cols = derive_table("Anomalies", "anomalies")["cols"]
    return [[render_cell(ctx, c, v) for c, v in zip(cols, (str(i), mdl.derive_iso(a.get("t")), a.get("kind"),
                                                           a.get("subclass")))]
            for i, a in enumerate(m.get("anomalies") or [], 1)]


def build_coverage_rows(m, ctx) -> list:
    cols = derive_table("Coverage", "sources")["cols"]
    cov = m.get("coverage") or {}
    rows = []
    for i, name in enumerate(mdl.SOURCE_NAMES, 1):
        row = cov.get(name) or {}
        raw = (str(i), name, row.get("state"), derive_count(row.get("lines")), derive_count(row.get("bad")),
               mdl.derive_iso(row.get("epoch")))
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
    w = m.get("window") or {}
    cov = m.get("coverage") or {}
    pos = (m.get("owner_positions") or {}).get("counts") or {}
    usage = m.get("usage") or {}
    att = m.get("attribution") or {}
    start, end = w.get("start"), w.get("end")
    dur = f"{int(end - start)}s" if isinstance(start, (int, float)) and isinstance(end, (int, float)) \
        and end >= start else None
    present = sum(1 for s in mdl.SOURCE_NAMES if (cov.get(s) or {}).get("state") == "present")
    values = {
        "run-state": (m.get("record"),),
        "run": (derive_count(m.get("run")), derive_count(m.get("runs"))),
        "start": (m.get("start_commit"),),
        "phase": (m.get("phase") or None,),
        "terminal": (derive_yes_no(m.get("terminal")),),
        "window": (mdl.derive_iso(start), mdl.derive_iso(end)),
        "window opened by": (w.get("start_from"),),
        "window closed by": (w.get("end_from"),),
        "duration": (dur,),
        "own commits": (str(len(m.get("own_commits") or [])),),
        "last own commit": (m.get("last_own"),),
        "merged": (derive_yes_no(m.get("merged")),),
        "units served": (str(len(serves)),),
        "sources present": (str(present), str(len(mdl.SOURCE_NAMES))),
        "owner turns": tuple(derive_count(pos.get(p, 0)) for p in mdl.OWNER_POSITIONS),
        "attributed calls": (derive_count(att.get("attributed", 0)), derive_count(att.get("calls", 0))),
    }
    for split in ex.SOURCES:
        values[f"usage {split}"] = tuple(derive_count((usage.get(split) or {}).get(f, 0)) for f in USAGE_FIELDS)
    facts = []
    for label, templates in RECORD_SCHEMA["sections"]["Summary"]["facts"]:
        if label == "values withheld":
            continue
        if label == "commitment":
            if commitment:
                facts.append((label, render_fact(ctx, templates[1], (
                    commitment.get("sha256"), derive_count(commitment.get("lines")), commitment.get("first"),
                    commitment.get("last")))))
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
    ctx = {"match": build_matchers(str(m.get("slug") or ""), mr, own), "withheld": 0}
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
            ("Anomalies", "anomalies", "anomalies", "by-kind", (2, 3),
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
    doc["Coverage"] = {
        "facts": [("journal starts", render_fact(ctx, derive_fact_templates("Coverage", "journal starts")[0],
                                                 (derive_count(starts.get("joined", 0)),
                                                  derive_count(starts.get("record-creating", 0))))),
                  ("unjoined starts", str(len(cov.get("unjoined_starts") or []))),
                  ("sessions", render_fact(ctx, derive_fact_templates("Coverage", "sessions")[0],
                                           (derive_count(tr.get("sessions", 0)),
                                            derive_count(tr.get("extracts", 0)))))],
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

    Raises ValueError when the run served no spec-defined unit, or when even every section aggregated
    and no timeline row shown cannot fit the cap.
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

def measure_commitment(model, journal_root, first=None, count=None) -> dict | None:
    """The sha256, count and first and last times of the journal lines the model attributed to the run.

    Each line is hashed as `<producer> TAB <its raw bytes> LF`, in time order. With `first` and `count`,
    this is the verify form: only lines at or after `first` count, and only the first `count` of them,
    so a line appended after the render changes nothing and an edit or a deletion changes the hash.
    None when there is no line to hash.
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
    if first is not None:
        floor = mdl.parse_iso(first)
        picked = [p for p in picked if floor is not None and p[0] >= floor]
        picked = picked[:count] if count is not None else picked
    if not picked:
        return None
    digest = hashlib.sha256()
    for _t, _rank, _n, producer, line in picked:
        digest.update(producer.encode("ascii") + b"\t" + line + b"\n")
    return {"sha256": digest.hexdigest(), "lines": len(picked), "first": mdl.derive_iso(picked[0][0]),
            "last": mdl.derive_iso(picked[-1][0])}


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
    want = {"sha256": cm.group(1), "lines": int(cm.group(2)), "first": cm.group(3), "last": cm.group(4)}
    now = measure_commitment(model, journal_root, first=want["first"], count=want["lines"]) or {}
    bad = [f for f in ("sha256", "lines", "first", "last") if now.get(f) != want[f]]
    if bad:
        return "mismatch", ("the journal changed after the render: " + "; ".join(
            f"{f} committed {want[f]} and recomputed {now.get(f, 'nothing')}" for f in bad))
    return "match", f"{want['lines']} journal line(s) hash as committed"
