#!/usr/bin/env python3
"""model.py — one unattended run's sources joined into one account of it. gov:kit runlog@1.0

A run's evidence is spread across its run-state file, three journals, git, its build folder and, where
local, its session extracts. `build_run_model` joins them into ONE model of ONE run: a timeline, a
decision ledger, a conformance block, an anomaly set, the owner's turns by position, what it cost, and
a coverage block saying how much of each answer the sources support. Every later surface renders from
this model rather than re-deriving it, and `derive_run_starts` is the one owner of which commit
started which run. The rules, each with the measurement behind it, are the unit's spec
(TOOL-dLoggedFlight-8) and the kit README's model section; this docstring does not restate them.

EVERY SOURCE READER RETURNS WHAT IT READ AND A COVERAGE STATE, and the join never fails on a missing
source: it marks the state and continues, because most runs predate the journals and must still model
from their run-state files and git. A run log is evidence, never an input, so nothing here decides a
run's fate and no verb reads what this prints.

GIT COST IS CONSTANT. Every git process goes through `run_git`, and a model costs the same number of
them whatever the run's commit or record count: one log for the run starts, one ref listing, one log
over the run-state paths, one over the own-commit range, one `rev-list` for the push join and one
`cat-file --batch` for every blob. The self-test counts them independently of `GIT_CALLS`.

WHAT THIS DOES NOT DO. It judges no decision's quality and renders nothing for a tracked file. Every
answer that is inferred rather than read is named in the model's `method` field, so a reader knows
which is which. It reads every path it is handed or resolves from git and the memory-tree conf; it
names nothing outside this kit by literal.
"""
from __future__ import annotations

import calendar
import json
import os
import pathlib
import re
import subprocess
import sys
import time
from collections import Counter
from dataclasses import asdict, dataclass, field

HERE = pathlib.Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import extract as ex  # noqa: E402
import runlog_lib as rl  # noqa: E402

MODEL_SCHEMA = 1
# The CLOSED lists. The self-test drives a fixture for every member and holds every fixture's answer
# to membership, in both directions, so a member with no fixture and an answer outside the list both
# red.
ANOMALY_KINDS = ("nonterminal-merged", "no-progress", "out-of-band-edit", "refusal-loop", "killed-verb",
                 "push-outside-lander", "red-behind-zero", "destructive-git", "converged-on-blocked",
                 "idle-gap", "multi-run-session", "stalled")
# `refused-landing` first because it is decided from the journal, which the drift signal's table of
# tracked bytes cannot see; the other four ARE that table, cited in the spec and not restated there.
MERGED_SUBCLASSES = ("refused-landing", "retired-unit", "surfaced-park", "no-rows", "other")
CONFORMANCE_ITEMS = ("brief-before-build", "phases-walked", "green-at-close", "keepalive-reaped",
                     "review-exited")
CONFORMANCE_STATES = ("MET", "UNMET", "UNJUDGEABLE")
COVERAGE_STATES = ("present", "absent", "partial", "dead", "not-local")
OWNER_POSITIONS = ("launch", "pre-run", "in-window", "post-close")
SOURCE_NAMES = ("run-state", "driver", "gates", "pushes", "git", "transcripts", "build-folder")
LEDGER_SOURCES = ("decision", "abort", "override", "waiver", "rescope-retire", "rescope-supersede",
                  "review", "trailer", "spec-mark", "decision-log", "ledger")
# THE DRIVER'S OWN SETS, COPIED, because a kit reads no sibling kit at run time. A replicated policy
# value is held to the file that owns it: the withheld self-test extracts these from the driver's
# source where that file is present, compares both directions, and announces its skip where it is not.
PARK_KINDS = ("decision", "abort", "override", "waiver", "proposal", "rescope", "dispatch", "review",
              "brief")
PARK_KINDS_OWED = ("decision", "abort", "override", "waiver")
PARK_ACTS_OWED = ("retire", "supersede")
PHASES_TERMINAL = ("LANDED", "ABORTED")
# The phases at and past the close. An item whose evidence exists only once a run has closed is
# UNJUDGEABLE before it, rather than UNMET for a run that has not got there yet.
PHASES_CLOSED = ("LANDING",) + PHASES_TERMINAL
REVIEW_EXITS = ("CONVERGED", "NON-CONVERGENT", "CEILING")
# The verbs whose END carries a unit, which is what attribution reads. Every other verb leaves the unit
# where it was, so a heartbeat `--status` between a `--brief` and an event does not reset it.
UNIT_VERBS = ("--brief", "--dispatch", "--rescope", "--review")
IDLE_GAP_S = 900
# B1 (closing review, round 1): a stretch with an owner turn inside it, or within this many seconds of
# either end, is kept out of the idle gaps and counted. Dropping the turn from the gap sequence is not
# enough alone: the owner's reply lands seconds after the turn, so a gap that ends on the reply still
# places the turn to within that latency. One idle threshold, because a stretch that close is the
# owner's own episode rather than the run's idleness.
IDLE_OWNER_GUARD_S = IDLE_GAP_S
# F1, RESOLVED (agent, 2026-09-13, delegated): six heartbeats with no head or phase change, one hour
# at the declared ten-minute cadence. Both numbers are printed in the anomaly's evidence.
HEARTBEAT_CADENCE_S = 600
STALL_HEARTBEATS = 6
REFUSAL_LOOP_MIN = 3
JOURNALS = ("driver", "gates", "pushes")
MODELS_DIR = "models"
DECISION_LOG = "DECISIONS.md"
# The spellings that make a decision-log row the owner's (spec S4), and the near-miss the report-only
# arm prints beside them. A row is the owner's when ANY spelling hits; each is counted separately.
OWNER_SPELLINGS = (("(owner)", re.compile(r"\(owner\)")), ("(owner,", re.compile(r"\(owner,")),
                   ("(owner:", re.compile(r"\(owner:")),
                   ("owner ruling", re.compile(r"owner ruling", re.I)),
                   ("owner call", re.compile(r"owner call", re.I)))
OWNER_NEAR_MISS = re.compile(r"\(owner[A-Za-z]")
# What makes an acceptance line not met. Heuristic, and named so in `method`.
LEDGER_UNMET_RE = re.compile(r"\b(owed|not met|unmet)\b", re.I)
AC_LINE_RE = re.compile(r"- (AC[0-9]+) — ")

ISO_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
ROW_RE = re.compile(r"([0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z) ([a-z][a-z-]*) · item (.*)")
FACT_RE = re.compile(r"([a-z][a-z0-9-]*): ?(.*)")
ARCHIVE_RE = re.compile(r"RUN\.([A-Z]+)\.([0-9a-f]{8})\.md")
MARK_RE = re.compile(r"RESOLVED \((owner|agent), ([0-9]{4}-[0-9]{2}-[0-9]{2})(, delegated)?\)")
VERDICT_RE = re.compile(r"## Verdict: *(.*)")
SHA_RE = re.compile(r"[0-9a-f]{40}")

# Every inferred answer, named. A reader of the model learns here which answers are read and which
# are the join's own inference, so a heuristic never passes for a measurement.
METHOD = {
    "run-starts": "read: the commits that added each run-state path, with renames off",
    "journal-join": "read: a record-creating preflight START joins the first start commit at or "
                    "after its END, the latest such START winning a commit",
    "own-commits": "inferred: an era commit descending from the start commit whose subject names a "
                   "unit id of the build",
    "build-commit": "heuristic: a unit's first own non-merge commit touching a path outside the memory "
                    "root, so a spec commit that re-renders a generated index is not a build",
    "push-join": "inferred: a push from the run's worktree inside the window, or one inside it "
                 "pushing the default branch to a descendant of the run's last own commit",
    "gate-join": "read where a joined push pinned gate_run, inferred from the worktree otherwise",
    "close-head": "inferred: the first parent of the commit recording the LANDING write, else HEAD",
    "attribution": "inferred: the most recent END of the same session",
    "decision-log-owner": "heuristic: (owner followed by ), , or :, or owner ruling or owner call in "
                          "any case",
    "ledger-unmet": "heuristic: an acceptance line saying owed, not met or unmet",
    "stall-heads": "inferred: the run's own and record commits stand in for its worktree head",
    "idle": "inferred: a stretch of IDLE_GAP_S or more between two events that no event of any source "
            "covers, a tool call covering its span and an owner turn covering nothing; judged only "
            "where the transcripts read present, and kept out within IDLE_OWNER_GUARD_S of an owner "
            "turn",
    "sessions": "read from the run's START lines; heuristic when discovered by slug in the store",
}

GIT_CALLS = [0]


@dataclass
class RunModel:
    """One run, joined. Every field is JSON-shaped, so `asdict` is the model's serialisation."""
    slug: str
    run: int
    runs: int
    runkey: str
    record: str
    start_commit: str
    era: dict
    window: dict
    phase: str
    terminal: bool
    facts: dict
    repairs: list
    worktrees: list
    sessions: list
    own_commits: list
    last_own: str | None
    merged: bool | None
    close: dict
    timeline: list
    tools: list
    record_rows: list
    record_commits: list
    shared_sessions: list
    units: list
    ledger: dict
    conformance: list
    anomalies: list
    owner_positions: dict
    usage: dict
    attribution: dict
    coverage: dict
    # The line numbers, per producer file, of every journal line this model attributed to the run. The
    # committed record hashes those lines (TOOL-dLoggedFlight-9 S5), so this model is the ONE owner of
    # which lines are the run's, and the record never re-joins them.
    journal_lines: dict = field(default_factory=dict)
    method: dict = field(default_factory=lambda: dict(METHOD))
    cost: dict = field(default_factory=dict)
    schema: int = MODEL_SCHEMA


# ---------------------------------------------------------------------------------- small readers

def derive_iso(t) -> str | None:
    return None if t is None else time.strftime(ISO_FORMAT, time.gmtime(float(t)))


def parse_iso(text) -> float | None:
    try:
        return float(calendar.timegm(time.strptime(text, ISO_FORMAT)))
    except (TypeError, ValueError):
        return None


def parse_float(value) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def derive_path_key(path) -> str:
    """A worktree path in one spelling, so the driver's and the runner's copies of one path compare
    equal: forward slashes, no trailing slash, and on Windows a lowercase drive, with the MSYS `/c/`
    form folded to `c:/`."""
    s = str(path or "").replace("\\", "/").rstrip("/")
    if os.name == "nt":
        m = re.match(r"/([A-Za-z])(/|$)", s)
        if m:
            s = f"{m.group(1)}:{s[2:]}"
        if re.match(r"[A-Za-z]:", s):
            s = s[0].lower() + s[1:]
    return s


def run_git(root, args, stdin=None) -> bytes:
    """ONE git process, counted. Raises ValueError naming the call when git refuses it."""
    GIT_CALLS[0] += 1
    try:
        proc = subprocess.run(["git", "-C", str(root), "-c", "core.quotepath=off", *args], input=stdin,
                              capture_output=True)
    except OSError as exc:
        raise ValueError(f"runlog: git could not be run: {exc}") from exc
    if proc.returncode != 0:
        why = proc.stderr.decode("utf-8", "replace").strip().splitlines()
        raise ValueError(f"runlog: git {args[0]} refused ({why[0] if why else proc.returncode})")
    return proc.stdout


def resolve_repo_root(start=None) -> pathlib.Path:
    """The work-tree top of the repository holding `start`. One git call."""
    out = run_git(start or ".", ["rev-parse", "--show-toplevel"]).decode("utf-8", "replace").strip()
    if not out:
        raise ValueError("runlog: not inside a git work tree")
    return pathlib.Path(out)


# ---------------------------------------------------------------------------------- the run starts

def derive_run_starts(root, memory_root=None, slugs=None, tracked=None) -> dict:
    """`{slug: [run, ...]}`, oldest first, keyed on the commit that STARTED each run.

    ONE git call for one build or the whole population: the commits that ADDED a run-state path, renames
    off. A rotation is a `git mv -f` plus a fresh `RUN.md` in the successor's preflight commit, so with
    renames off that commit ADDS the archive and only modifies `RUN.md`: each rotation commit is its
    successor's start, an archive takes the entry immediately before the commit that added it, and the
    live `RUN.md` takes the last. A path's own creation commit cannot tell an archive from its successor.
    A run's `k` is its 1-up position, and `runkey` the first 8 hex of its start.

    `tracked`, a set of repo-relative paths, answers which run-state files exist instead of the working
    tree, so a caller grading the INDEX (the schema leg, TOOL-dLoggedFlight-10) gets the index's runs.
    """
    root = pathlib.Path(root)
    mr = memory_root if memory_root is not None else rl.resolve_memory_root(root)

    def check_present(rel) -> bool:
        return rel in tracked if tracked is not None else (root / rel).is_file()

    names = ["*"] if slugs is None else list(slugs)
    if not names:
        return {}
    specs = []
    for s in names:
        specs += [f"{mr}/builds/{s}/RUN.md", f"{mr}/builds/{s}/RUN.*.md"]
    raw = run_git(root, ["log", "--no-renames", "--diff-filter=A", "--name-only",
                         "--format=%x1e%H %ct", "--", *specs]).decode("utf-8", "replace")
    prefix = f"{mr}/builds/"
    entries: dict = {}
    for chunk in raw.split("\x1e")[1:]:
        lines = [ln.strip() for ln in chunk.split("\n")]
        head = lines[0].split()
        if len(head) != 2 or SHA_RE.fullmatch(head[0]) is None:
            continue
        sha, ct = head[0], int(head[1])
        # Within one commit the live path sorts before an archive, so a squashed history that adds
        # both at once still gives the archive the earlier of the two entries.
        for path in sorted((p for p in lines[1:] if p.startswith(prefix)),
                           key=lambda p: (not p.endswith("/RUN.md"), p)):
            slug, _, name = path[len(prefix):].partition("/")
            if "/" in name or not (name == "RUN.md" or ARCHIVE_RE.fullmatch(name)):
                continue
            entries.setdefault(slug, []).append({"sha": sha, "t": ct, "path": path, "name": name})
    out = {}
    for slug, found in entries.items():
        found.reverse()
        runs = []
        for j, entry in enumerate(found):
            if entry["name"] != "RUN.md" and check_present(entry["path"]):
                start = found[j - 1] if j > 0 else entry
                runs.append({"record": entry["path"], "start": start["sha"], "t": start["t"]})
        live = f"{prefix}{slug}/RUN.md"
        if check_present(live):
            runs.append({"record": live, "start": found[-1]["sha"], "t": found[-1]["t"]})
        for k, run in enumerate(runs, 1):
            run.update(k=k, runkey=run["start"][:8])
        if runs:
            out[slug] = runs
    return out


def derive_run_eras(runs) -> list:
    """Run k's era: the commits from its start up to the next start of the same build, or to HEAD for
    the last run. Half-open in commit time, `[t0, t1)`, with `t1` None for the last."""
    eras = []
    for i, run in enumerate(runs):
        nxt = runs[i + 1] if i + 1 < len(runs) else None
        eras.append({"k": run["k"], "start": run["start"], "t0": run["t"],
                     "next": nxt["start"] if nxt else None, "t1": nxt["t"] if nxt else None})
    return eras


def check_in_era(t, era) -> bool:
    return t >= era["t0"] and (era["t1"] is None or t < era["t1"])


def derive_record_commits(history, era, live_path) -> list:
    """The run's own writes to its live run-state path, oldest first: the era's non-merge commits that
    added or modified it. Bounded to the era because rotation keeps the path, so the path's history
    also holds every predecessor's writes, its terminal one included. The model and the schema leg
    (TOOL-dLoggedFlight-10) both read this, so the two cannot bound a run's writes differently."""
    return sorted((c for c in history if check_in_era(c["t"], era) and len(c["parents"]) <= 1
                   and any(p == live_path and s in "AM" for s, p in c["files"])), key=lambda c: c["t"])


def derive_window(start, start_from, phases_at, terminal, term_end=None, last_line=None) -> dict:
    """A run's half-open window (spec S2 of TOOL-dLoggedFlight-8), from what the caller read.

    `phases_at` is `[(record commit, phase)]`, oldest first, over `derive_record_commits`. The window
    closes at the END that moved the phase into a terminal one, else, for a terminal run, at its first
    terminal write, else one second after the later of the last journal line and the last record
    commit, the resolution of a commit time, so the run's last event is inside its own window. A caller
    with no journal, such as a fresh clone, passes no `term_end` and no `last_line`, and gets the window
    git alone gives.
    """
    term_write = next((c for c, ph in phases_at if ph in PHASES_TERMINAL), None)
    if term_end is not None:
        end, end_from = term_end, "terminal-end"
    elif terminal and term_write is not None:
        end, end_from = float(term_write["t"]), "terminal-write"
    else:
        last_rec = phases_at[-1][0]["t"] if phases_at else None
        latest = max((v for v in (last_line, last_rec) if v is not None), default=start)
        end, end_from = float(latest) + 1.0, "last-activity"
    return {"start": start, "end": end, "start_from": start_from, "end_from": end_from}


# ---------------------------------------------------------------------------------- the run-state file

def read_run_state(text, path="") -> tuple:
    """`(record, state)`: the facts, the parked rows with their line numbers, and the labelled repairs.

    Rows are park()'s grammar, `<ts> <kind> · item <item>[ · step <step>] · reason <reason>`, read with
    the item ending at the FIRST ` · reason `, as the driver's own readers take it. A row of a kind the
    driver does not declare is counted, never guessed at.
    """
    if text is None:
        return {"path": path, "facts": {}, "rows": [], "repairs": [], "unknown_kinds": {}}, "absent"
    facts, rows, repairs, unknown = {}, [], [], {}
    section = None
    for lineno, line in enumerate(text.split("\n"), 1):
        line = line.rstrip("\r")
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        m = ROW_RE.fullmatch(line)
        if m:
            kind = m.group(2)
            if kind not in PARK_KINDS:
                unknown[kind] = unknown.get(kind, 0) + 1
                continue
            rest = m.group(3)
            j = rest.find(" · reason ")
            item, reason = (rest, "") if j < 0 else (rest[:j], rest[j + len(" · reason "):])
            step = None
            k = item.find(" · step ")
            if k >= 0:
                item, step = item[:k], item[k + len(" · step "):]
            rows.append({"t": parse_iso(m.group(1)), "kind": kind, "item": item, "step": step,
                         "reason": reason, "line": lineno})
            continue
        if section == "Run facts" and line and not line[0].isspace():
            f = FACT_RE.fullmatch(line)
            if f:
                facts.setdefault(f.group(1), f.group(2).strip())
                if f.group(1).endswith("-source"):
                    repairs.append(f.group(1))
    return {"path": path, "facts": facts, "rows": rows, "repairs": repairs,
            "unknown_kinds": unknown}, "present"


def derive_phase(text) -> str:
    for line in (text or "").split("\n"):
        if line.startswith("phase: "):
            return line[len("phase: "):].strip()
    return ""


def derive_fact(text, key) -> str:
    head = f"{key}: "
    for line in (text or "").split("\n"):
        if line.startswith(head):
            return line[len(head):].strip()
    return ""


def derive_review_exit(reason) -> str | None:
    parts = [p.strip() for p in reason.split(" · ")]
    for token in REVIEW_EXITS:
        if token in parts:
            return token
    return None


def derive_review_verdict(reason) -> str | None:
    m = re.match(r"verdict (.*?)(?: · |$)", reason)
    return m.group(1) if m else None


# ---------------------------------------------------------------------------------- git

def read_git_range(root, revs, paths=()) -> list:
    """Commits as dicts, newest first: sha, parents, time, subject, `Decided:` trailers, body and files.

    ONE git call. The trailers are git's own parse (`%(trailers:key=Decided,valueonly)`), so a line
    reads as a trailer exactly when git reads it as one; the body is kept so a caller can count the
    `Decided:` lines git did NOT parse. Merges carry no file list, which is git's default.
    """
    fmt = "%x1e%H%x1f%P%x1f%ct%x1f%s%x1f%(trailers:key=Decided,valueonly,separator=%x1d)%x1f%B%x1f"
    args = ["log", "--no-renames", "--name-status", f"--format={fmt}", *revs]
    if paths:
        args += ["--", *paths]
    raw = run_git(root, args).decode("utf-8", "replace")
    out = []
    for chunk in raw.split("\x1e")[1:]:
        parts = chunk.split("\x1f")
        if len(parts) < 7 or SHA_RE.fullmatch(parts[0]) is None:
            continue
        files = []
        for line in parts[6].split("\n"):
            bits = line.strip().split("\t")
            if len(bits) >= 2 and bits[0]:
                files.append((bits[0][0], bits[-1]))
        decided = [v.strip() for v in parts[4].split("\x1d") if v.strip()]
        out.append({"sha": parts[0], "parents": parts[1].split(), "t": int(parts[2]),
                    "subject": parts[3], "decided": decided, "body": parts[5], "files": files})
    return out


def read_refs(root) -> dict:
    """Every branch and remote-tracking ref with its sha, the checked-out branch, and origin/HEAD's
    target. ONE call; a detached HEAD costs one more."""
    # `for-each-ref` spells a hex byte `%1f`, not `log`'s `%x1f`; the log spelling passes through as
    # text and every line then fails to split, which reads as a clone with no refs at all.
    raw = run_git(root, ["for-each-ref", "--format=%(HEAD)%1f%(refname)%1f%(objectname)%1f%(symref)",
                         "refs/heads", "refs/remotes"]).decode("utf-8", "replace")
    refs, head, origin_head = {}, None, None
    for line in raw.split("\n"):
        bits = line.split("\x1f")
        if len(bits) != 4:
            continue
        mark, name, sha, symref = bits
        refs[name] = sha
        if mark.strip() == "*":
            head = sha
        if name == "refs/remotes/origin/HEAD" and symref:
            origin_head = symref
    if raw.strip() and not refs:
        raise ValueError("runlog: for-each-ref printed lines this reader could not split, so every ref "
                         "would read as absent")
    if head is None:
        head = run_git(root, ["rev-parse", "--verify", "-q", "HEAD"]).decode().strip() or None
    return {"refs": refs, "head": head, "origin_head": origin_head}


def resolve_default_ref(refs, default_ref=None) -> tuple:
    """`(refname, branch name)` of the default branch: a given ref, else origin/HEAD's target, else a
    local main, else a local master. `(None, None)` when none resolves."""
    table = refs["refs"]
    for cand in (default_ref, refs.get("origin_head"), "refs/heads/main", "refs/heads/master"):
        if cand and cand in table:
            name = re.sub(r"^refs/(heads|remotes/[^/]+)/", "", cand)
            return cand, name
    return None, None


def read_blobs(root, requests, decode=True) -> dict:
    """`{request: text or None}` for `<rev>:<path>` requests, or any object name, through ONE
    `cat-file --batch`. `decode=False` returns each blob's BYTES, for a caller grading bytes."""
    wanted = sorted(set(requests))
    if not wanted:
        return {}
    raw = run_git(root, ["cat-file", "--batch"], stdin=("\n".join(wanted) + "\n").encode("utf-8"))
    out, pos = {}, 0
    for req in wanted:
        nl = raw.find(b"\n", pos)
        if nl < 0:
            break
        header = raw[pos:nl].decode("utf-8", "replace").split()
        pos = nl + 1
        if len(header) == 3 and header[1] == "blob":
            size = int(header[2])
            body = raw[pos:pos + size]
            out[req] = body.decode("utf-8", "replace") if decode else body
            pos += size + 1
        elif len(header) == 3:
            pos += int(header[2]) + 1
            out[req] = None
        else:
            out[req] = None
    return out


# ---------------------------------------------------------------------------------- the journals

def read_journals(journal_root) -> dict:
    """Each producer file as a `Journal`, with its EPOCH: the time of its first good line."""
    out = {}
    for name in JOURNALS:
        if journal_root is None:
            j = rl.Journal(path="", state="absent")
        else:
            j = rl.read_journal(pathlib.Path(journal_root) / rl.PRODUCER_FILES[name])
        epoch = parse_float(j.lines[0].fields.get("t")) if j.lines else None
        out[name] = {"journal": j, "epoch": epoch}
    return out


def derive_invocation(inv) -> dict:
    s = inv.start.fields if inv.start else {}
    e = inv.end.fields if inv.end else {}
    t0 = parse_float(s.get("t"))
    t1 = parse_float(e.get("t"))
    checks = [c for c in (e.get("checks") or "").split(",") if c]
    sids = sorted({v for k, v in s.items() if k.startswith("sess.") and ex.SID_RE.fullmatch(v or "")})
    return {"t": t0 if t0 is not None else t1, "end": t1, "state": inv.state,
            "verb": s.get("verb") or e.get("verb") or "", "slug": s.get("slug") or e.get("slug") or "",
            "rc": e.get("rc"), "exit": e.get("exit"), "checks": checks,
            "phase_from": s.get("phase_from"), "phase_to": e.get("phase_to"),
            "unit": e.get("unit") or None, "oob": s.get("oob") == "1", "wt": s.get("wt"),
            "sids": sids,
            "lines": [ln.lineno for ln in (inv.start, inv.end) if ln is not None and ln.lineno]}


def check_record_creating(inv) -> bool:
    """A successful preflight that CREATED a record: its START saw no phase or a terminal one (a fresh
    build, or a rotation), and its END says it chose exit 0. A re-preflight of a live record resumes it
    and starts nothing."""
    return (inv["verb"] == "--preflight" and inv["state"] == "ended" and inv["rc"] == "0"
            and inv["exit"] == "clean" and (inv["phase_from"] or "") in ("",) + PHASES_TERMINAL)


def derive_journal_join(invs, runs) -> tuple:
    """`(joined, unjoined)`: which record-creating START belongs to which run, by a NAMED key.

    A START belongs to the start commit its own call made — the first start commit of its slug at or
    after its END — and when several STARTs name one commit, the latest wins, since the earlier ones'
    commits never reached this clone. `joined` maps a run's k to its START; `unjoined` lists the STARTs
    that start no run.
    """
    creating = [inv for inv in invs if check_record_creating(inv)]
    claims: dict = {}
    unjoined = []
    for inv in creating:
        target = None
        for run in runs:
            if run["t"] >= int(inv["end"]):
                target = run["k"]
                break
        if target is None:
            unjoined.append(inv)
            continue
        prev = claims.get(target)
        if prev is not None:
            unjoined.append(prev)
        claims[target] = inv
    return claims, sorted(unjoined, key=lambda i: i["t"])


# ---------------------------------------------------------------------------------- sessions

def resolve_run_sessions(sids, slug, store=None, projects=None) -> tuple:
    """`(extracts, state, note)`: each session's structural extract, from the store where one was
    written, else extracted in memory where its transcript is on this machine. With no session named
    by the journal, the store's extracts attributed to the slug stand in, heuristically."""
    extracts, note = {}, ""
    store_dir = pathlib.Path(store) if store else None
    discovered = False
    if store_dir is not None and not sids:
        sess_dir = store_dir / ex.SESSIONS_DIR
        for p in sorted(sess_dir.glob("*.json")) if sess_dir.is_dir() else []:
            try:
                data = json.loads(p.read_bytes())
            except (OSError, ValueError):
                continue
            if slug in (data.get("slugs") or []) and ex.SID_RE.fullmatch(str(data.get("sid", ""))):
                extracts[data["sid"]] = data
                discovered = True
    for sid in sids:
        data = None
        if store_dir is not None:
            p = store_dir / ex.SESSIONS_DIR / f"{sid}.json"
            if p.is_file():
                try:
                    data = json.loads(p.read_bytes())
                except (OSError, ValueError):
                    data = None
        if data is None and projects is not None:
            try:
                tree = ex.resolve_session_tree(sid, projects)
            except ValueError:
                tree = None
            if tree is not None and tree.main is not None:
                data = ex.extract_session(tree, "driver", [slug])
        if data is not None:
            extracts[sid] = data
    named = len(sids)
    found = sum(1 for s in sids if s in extracts)
    if discovered:
        state, note = "present", "sessions discovered by slug in the store, heuristically"
    elif named and found == named:
        state = "present"
    elif found:
        state, note = "partial", f"{named - found} of {named} sessions have no local transcript"
    else:
        state = "not-local"
        note = ("the run's journal names no session" if not named
                else "no named session has a transcript or an extract on this machine")
    return extracts, state, note


# ---------------------------------------------------------------------------------- the blocks

def measure_coverage(journals, window, lines, activity, transcripts, record_state="present",
                     build_state="present") -> dict:
    """Each source's state from `COVERAGE_STATES`, with each journal's epoch.

    A journal is `absent` when its file is, or when the window closes at or before its epoch; `partial`
    when the window holds the epoch; and, when the window opens at or after it, `present` if it holds
    lines for the run or nothing the run's own rows prove required one, else `dead`. `activity` names,
    per journal, the run's own proof that its producer should have written.
    """
    start, end = window["start"], window["end"]
    out = {"run-state": {"state": record_state}, "git": {"state": "present"},
           "build-folder": {"state": build_state}}
    for name in JOURNALS:
        info = journals[name]
        j, epoch = info["journal"], info["epoch"]
        n = lines.get(name, 0)
        row = {"epoch": epoch, "lines": n, "bad": j.bad}
        if j.state in ("absent", "empty", "unreadable") or epoch is None:
            row["state"] = "absent"
            if j.state == "unreadable":
                row["note"] = j.note
        elif end <= epoch:
            row["state"] = "absent"
        elif start < epoch:
            row["state"] = "partial"
        elif n:
            row["state"] = "present"
        elif activity.get(name):
            row["state"] = "dead"
            row["proof"] = activity[name]
        else:
            row["state"] = "present"
        out[name] = row
    out["transcripts"] = dict(transcripts)
    return out


def build_owner_positions(turns, start, close) -> dict:
    """Each owner turn classed by the run's boundaries: `launch` for a session's first turn when it
    precedes the start, `pre-run` for any other turn before it, `in-window` from the start to the close,
    and `post-close` from the close on. `turns` is `[(t, session)]`; `start` is the preflight START or,
    for a run with none, its start commit; `close` is the `--close` END, else the terminal END, else
    the window end."""
    first: dict = {}
    for t, sid in sorted(turns, key=lambda x: x[0]):
        first.setdefault(sid, t)
    counts = {p: 0 for p in OWNER_POSITIONS}
    classed = []
    for t, sid in sorted(turns, key=lambda x: x[0]):
        if t < start:
            pos = "launch" if first.get(sid) == t else "pre-run"
        elif t < close:
            pos = "in-window"
        else:
            pos = "post-close"
        counts[pos] += 1
        classed.append({"t": t, "position": pos})
    return {"counts": counts, "turns": classed}


def derive_idle_gaps(spans, owner_ts, start, end) -> tuple:
    """`(gaps, near_owner)`: the idle stretches of the half-open window `[start, end)` (spec S6).

    `spans` are `(t, t_end)` pairs, one per event of every source the run holds EXCEPT an owner turn,
    with `t_end` None for a point. A tool call is its whole span, so a long bar, or a stretch of
    workflow calls, covers what it ran through. Each span is clipped to the window and the covered
    stretches merged; a hole of `IDLE_GAP_S` or more BETWEEN two of them is a gap, and a hole reaching
    a window edge is not. A gap with an owner turn inside it, or within `IDLE_OWNER_GUARD_S` of either
    end, is not returned but counted in `near_owner`: its endpoints would place that turn, and the
    committed record keeps owner turns to counts with no clock time.
    """
    covered = []
    for t, t_end in spans:
        if not isinstance(t, (int, float)) or isinstance(t, bool):
            continue
        b = t_end if isinstance(t_end, (int, float)) and not isinstance(t_end, bool) and t_end > t else t
        if b < start or t >= end:
            continue
        covered.append((max(t, start), min(b, end)))
    owners = [o for o in owner_ts if isinstance(o, (int, float)) and not isinstance(o, bool)]
    gaps, near_owner, reach = [], 0, None
    for a, b in sorted(covered):
        if reach is not None and a - reach >= IDLE_GAP_S:
            if any(reach - IDLE_OWNER_GUARD_S <= o <= a + IDLE_OWNER_GUARD_S for o in owners):
                near_owner += 1
            else:
                gaps.append((reach, a))
        reach = b if reach is None else max(reach, b)
    return gaps, near_owner


def build_run_usage(extracts, start, end) -> dict:
    """Token totals inside the window, split three ways, through the extractor's own `build_usage`."""
    events = [ev for data in extracts.values() for ev in data.get("events", [])
              if ev.get("kind") == "usage" and start <= (ev.get("t") or 0) < end]
    return ex.build_usage(events)


def derive_attribution(invs, extracts) -> dict:
    """Which unit and phase each tool call ran under, within ONE session (spec S8).

    A call takes the unit of the most recent unit-bearing END of its own session and the phase of the
    most recent END's `phase_to`; a START with no END contributes its `phase_from` and no unit, and a
    verb carrying no unit leaves the unit where it was. A call before its session's first END is
    unattributed. Returns counts by unit and phase and the attributed share of calls and wall time.
    """
    points: dict = {}
    for inv in invs:
        for sid in inv["sids"]:
            if inv["state"] == "ended" and inv["end"] is not None:
                unit = inv["unit"] if inv["verb"] in UNIT_VERBS and inv["unit"] else None
                points.setdefault(sid, []).append((inv["end"], "end", inv["phase_to"] or "", unit))
            elif inv["state"] == "killed-or-running" and inv["t"] is not None:
                points.setdefault(sid, []).append((inv["t"], "start", inv["phase_from"] or "", None))
    for sid in points:
        points[sid].sort(key=lambda p: p[0])
    by_unit, by_phase = Counter(), Counter()
    calls = attributed = unit_calls = 0
    wall = attributed_wall = 0.0
    for sid, data in extracts.items():
        pts = points.get(sid, [])
        for ev in data.get("events", []):
            if ev.get("kind") != "tool":
                continue
            t = ev.get("t") or 0
            dur = ev.get("dur") or 0.0
            calls += 1
            wall += dur
            seen_end = False
            phase = unit = None
            for pt, kind, ph, un in pts:
                if pt > t:
                    break
                if kind == "end":
                    seen_end = True
                phase = ph
                if un:
                    unit = un
            if not seen_end:
                continue
            attributed += 1
            attributed_wall += dur
            by_phase[phase or ""] += 1
            if unit:
                unit_calls += 1
                by_unit[unit] += 1
    return {"calls": calls, "attributed": attributed, "unit_calls": unit_calls,
            "unattributed": calls - attributed, "by_unit": dict(sorted(by_unit.items())),
            "by_phase": dict(sorted(by_phase.items())), "wall_s": round(wall, 3),
            "attributed_wall_s": round(attributed_wall, 3),
            "share_calls": round(attributed / calls, 4) if calls else None,
            "share_wall": round(attributed_wall / wall, 4) if wall else None}


def scan_owner_spellings(text) -> dict:
    """Hits per owner spelling and the `(owner<letter>` near-misses, over a decision log's text. The
    report-only arm prints this over the tracked log; `scan_decisions` classifies rows with it."""
    counts = {name: len(rx.findall(text)) for name, rx in OWNER_SPELLINGS}
    counts["near-miss"] = len(OWNER_NEAR_MISS.findall(text))
    return counts


def check_owner_row(row) -> bool:
    return any(rx.search(row) for _, rx in OWNER_SPELLINGS)


def scan_decisions(ctx) -> dict:
    """The decision ledger (spec S4): every entry names its source and a file and line or a sha.

    `ctx` carries the run's `record` (from `read_run_state`), its `own_commits`, the spec `marks`
    already split into before and inside, the decision-log `rows` its commits added, the `reviews`
    and the unmet acceptance `ledgers`. Parked rows enter only when their kind is owed, or when they
    are a `rescope` whose act is; every other row is counted as excluded, by kind.
    """
    entries, excluded = [], Counter()
    record = ctx.get("record") or {"rows": [], "path": ""}
    for row in record["rows"]:
        kind = row["kind"]
        ref = f"{record['path']}:{row['line']}"
        if kind in PARK_KINDS_OWED:
            entries.append({"source": kind, "ref": ref, "t": row["t"], "item": row["item"]})
            continue
        if kind == "rescope":
            act = (row["item"].split() or [""])[0]
            if act in PARK_ACTS_OWED:
                entries.append({"source": f"rescope-{act}", "ref": ref, "t": row["t"],
                                "item": row["item"]})
                continue
            excluded[f"rescope {act or '(none)'}"] += 1
            continue
        excluded[kind] += 1
    for rv in ctx.get("reviews", []):
        entries.append({"source": "review", "ref": f"{rv['path']}:{rv['line']}" if rv["line"]
                        else rv["path"], "verdict": rv["verdict"]})
    near_miss = 0
    for c in ctx.get("own_commits", []):
        for value in c.get("decided", []):
            entries.append({"source": "trailer", "ref": c["sha"], "t": c["t"], "value": value})
        body_lines = sum(1 for ln in c.get("body", "").split("\n") if ln.startswith("Decided:"))
        near_miss += max(0, body_lines - len(c.get("decided", [])))
    for mark in ctx.get("marks", []):
        entries.append({"source": "spec-mark", "ref": mark["ref"], "resolver": mark["resolver"],
                        "when": mark["when"]})
    for row in ctx.get("decision_rows", []):
        entries.append({"source": "decision-log", "ref": row["sha"], "owner": row["owner"],
                        "id": row["id"]})
    for ln in ctx.get("ledgers", []):
        entries.append({"source": "ledger", "ref": ln["ref"], "ac": ln["ac"]})
    counts = {s: 0 for s in LEDGER_SOURCES}
    for e in entries:
        counts[e["source"]] += 1
    marks = Counter(f"{m['resolver']}-{m['when']}" for m in ctx.get("marks", []))
    return {"entries": entries, "counts": counts, "near_miss": near_miss,
            "excluded": dict(sorted(excluded.items())), "marks": dict(sorted(marks.items())),
            "owner_rows": sum(1 for r in ctx.get("decision_rows", []) if r["owner"])}


def check_conformance(model) -> list:
    """The conformance block (spec S5): each item MET, UNMET or UNJUDGEABLE, each naming its evidence."""
    out = []
    phase = model.get("phase") or ""
    closed = phase in PHASES_CLOSED
    # brief-before-build, per unit the run built.
    built = [u for u in model.get("units", []) if u.get("build_commit")]
    for u in built:
        bt = u["build_t"]
        briefs = [t for t in u.get("briefs", []) if t is not None and t < bt]
        dispatches = [t for t in u.get("dispatches", []) if t is not None and t < bt]
        state = "MET" if briefs and dispatches else "UNMET"
        ev = (f"build commit {u['build_commit'][:8]} at {derive_iso(bt)}; brief rows "
              f"{[derive_iso(t) for t in u.get('briefs', [])] or 'none'}; dispatch rows "
              f"{[derive_iso(t) for t in u.get('dispatches', [])] or 'none'}")
        out.append({"item": "brief-before-build", "unit": u["id"], "state": state, "evidence": ev})
    if not built:
        out.append({"item": "brief-before-build", "unit": None, "state": "UNJUDGEABLE",
                    "evidence": "no unit has a build commit in this run"})
    # phases-walked
    seq = sorted([(e["t"], e["phase"]) for e in model.get("timeline", []) if e["kind"] == "phase"]
                 + [(e["end"], e["phase_to"]) for e in model.get("timeline", [])
                    if e["kind"] == "verb" and e.get("phase_to") and e.get("end") is not None])
    phases = [p for _, p in seq]
    if "ABORTED" in phases or phase == "ABORTED":
        out.append({"item": "phases-walked", "state": "MET", "evidence": "the run aborted"})
    else:
        idx = next((i for i, p in enumerate(phases) if p in ("LANDING", "LANDED")), None)
        if idx is None:
            out.append({"item": "phases-walked", "state": "UNJUDGEABLE",
                        "evidence": f"the run has not reached LANDING; phases seen {sorted(set(phases))}"})
        elif "BUILDING" in phases[:idx]:
            out.append({"item": "phases-walked", "state": "MET",
                        "evidence": f"BUILDING before {phases[idx]} at {derive_iso(seq[idx][0])}"})
        else:
            out.append({"item": "phases-walked", "state": "UNMET",
                        "evidence": f"{phases[idx]} at {derive_iso(seq[idx][0])} with no BUILDING "
                                    "before it"})
    # green-at-close
    close = model.get("close") or {}
    gates = [e for e in model.get("timeline", []) if e["kind"] == "gate"]
    if close.get("t") is None:
        out.append({"item": "green-at-close", "state": "UNJUDGEABLE",
                    "evidence": "no successful --close END in the run's journal"})
    elif not gates:
        out.append({"item": "green-at-close", "state": "UNJUDGEABLE",
                    "evidence": f"no gate line in the window; --close ended {derive_iso(close['t'])}"})
    else:
        hit = [g for g in gates if g.get("verdict") == "GREEN" and g.get("head") == close.get("head")
               and g["t"] < close["t"]]
        if hit:
            out.append({"item": "green-at-close", "state": "MET",
                        "evidence": f"GREEN at {(close.get('head') or '')[:8]} at {derive_iso(hit[-1]['t'])}, "
                                    f"before --close ended {derive_iso(close['t'])}"})
        else:
            out.append({"item": "green-at-close", "state": "UNMET",
                        "evidence": f"{len(gates)} gate line(s) in the window, none GREEN at "
                                    f"{(close.get('head') or 'an unknown head')[:8]} before --close "
                                    f"ended {derive_iso(close['t'])}"})
    # keepalive-reaped
    value = (model.get("facts") or {}).get("keepalive-reaped", "")
    if re.match(r"(yes|true)\b", value):
        out.append({"item": "keepalive-reaped", "state": "MET", "evidence": f"keepalive-reaped: {value}"})
    elif closed:
        out.append({"item": "keepalive-reaped", "state": "UNMET",
                    "evidence": f"phase {phase} and the fact reads {value or 'absent'}"})
    else:
        out.append({"item": "keepalive-reaped", "state": "UNJUDGEABLE",
                    "evidence": f"phase {phase or 'none'}: the run has not reached LANDING"})
    # review-exited
    last: dict = {}
    for row in (model.get("record_rows") or []):
        if row["kind"] == "review":
            last[row["item"]] = row
    if not last:
        out.append({"item": "review-exited", "state": "UNJUDGEABLE", "evidence": "no review rows"})
    else:
        open_ = sorted(s for s, row in last.items() if derive_review_exit(row["reason"]) is None)
        if not open_:
            out.append({"item": "review-exited", "state": "MET",
                        "evidence": f"{len(last)} subject(s), each last row carrying an exit"})
        elif closed:
            out.append({"item": "review-exited", "state": "UNMET",
                        "evidence": f"{len(open_)} of {len(last)} subject(s) with no exit on their "
                                    f"last row, at lines {[last[s]['line'] for s in open_]}"})
        else:
            out.append({"item": "review-exited", "state": "UNJUDGEABLE",
                        "evidence": f"{len(open_)} subject(s) still open and the run has not reached "
                                    "LANDING"})
    return out


def derive_merged_subclass(model) -> tuple:
    """The sub-class of a `nonterminal-merged` run and the evidence for it. A refused `--landed` in the
    window comes first, because the table of tracked bytes cannot see refusals; otherwise the record's
    own last parked row, by the drift signal's table."""
    w = model["window"]
    for e in model.get("timeline", []):
        if (e["kind"] == "verb" and e["verb"] == "--landed" and e.get("rc") not in (None, "0")
                and e.get("exit") == "clean" and w["start"] <= e["t"] < w["end"]):
            return "refused-landing", f"--landed refused at {derive_iso(e['t'])} on checks {e['checks']}"
    rows = model.get("record_rows") or []
    if not rows:
        return "no-rows", "no parked row at all"
    last = rows[-1]
    act = (last["item"].split() or [""])[0]
    if last["kind"] == "rescope" and act in PARK_ACTS_OWED:
        return "retired-unit", f"last row is a rescope {act} at line {last['line']}"
    if last["kind"] in PARK_KINDS_OWED:
        return "surfaced-park", f"last row is a {last['kind']} at line {last['line']}"
    return "other", f"last row is a {last['kind']} at line {last['line']}"


def scan_anomalies(model) -> list:
    """The anomaly set (spec S6): each kind of `ANOMALY_KINDS` with its trigger's evidence, and `t`, the
    time of the event that triggered it: the last own commit for `nonterminal-merged`, and None for
    `no-progress` and `multi-run-session`, which are decided over the run as a whole."""
    out = []
    w = model["window"]
    tl = model.get("timeline", [])
    terminal = model.get("terminal")
    own = model.get("own_commits") or []
    if not terminal and own and model.get("merged"):
        sub, why = derive_merged_subclass(model)
        out.append({"kind": "nonterminal-merged", "subclass": sub, "t": float(own[-1]["t"]),
                    "evidence": f"phase {model['phase']}; last own commit {model['last_own'][:8]} is on "
                                f"the default branch; {why}"})
    if not terminal and not own:
        out.append({"kind": "no-progress", "t": None,
                    "evidence": f"no own commit after start {model['start_commit'][:8]}; window ends "
                                f"{derive_iso(w['end'])}"})
    verbs = [e for e in tl if e["kind"] == "verb"]
    for e in verbs:
        if e.get("oob"):
            out.append({"kind": "out-of-band-edit", "t": e["t"],
                        "evidence": f"{e['verb']} START at {derive_iso(e['t'])} carried oob=1"})
    loops, first = Counter(), {}
    for e in verbs:
        if e.get("rc") not in (None, "0") and e.get("exit") == "clean":
            for c in e["checks"]:
                loops[(e["verb"], c)] += 1
                first.setdefault((e["verb"], c), e["t"])
    for (verb, check), n in sorted(loops.items()):
        if n >= REFUSAL_LOOP_MIN:
            out.append({"kind": "refusal-loop", "t": first[(verb, check)],
                        "evidence": f"{verb} refused {n} times on check {check}"})
    for e in verbs:
        if e["state"] == "killed-or-running":
            out.append({"kind": "killed-verb", "t": e["t"],
                        "evidence": f"{e['verb']} START at {derive_iso(e['t'])} has no END"})
        elif e.get("exit") == "unclean":
            out.append({"kind": "killed-verb", "t": e["end"],
                        "evidence": f"{e['verb']} END at {derive_iso(e['end'])} reads exit=unclean"})
    default_name = model.get("coverage", {}).get("default_branch")
    for e in tl:
        if e["kind"] == "push" and e.get("lander") == "0" and default_name and any(
                (r.split() + ["", "", ""])[2] == f"refs/heads/{default_name}" for r in e.get("refs", [])):
            out.append({"kind": "push-outside-lander", "t": e["t"],
                        "evidence": f"a push at {derive_iso(e['t'])} to refs/heads/{default_name} with "
                                    "lander=0"})
    gates = [e for e in tl if e["kind"] == "gate"]
    for call in model.get("tools", []):
        if call.get("cls") == "bar" and call.get("bg") and call.get("rc") == 0 and call.get("end"):
            red = [g for g in gates if g.get("verdict") == "RED" and call["t"] <= g["t"] <= call["end"]]
            if red:
                out.append({"kind": "red-behind-zero", "t": call["t"],
                            "evidence": f"a background bar at {derive_iso(call['t'])} notified rc 0 "
                                        f"and its gate line at {derive_iso(red[0]['t'])} reads RED"})
        if "destructive" in (call.get("flags") or []):
            out.append({"kind": "destructive-git", "t": call["t"],
                        "evidence": f"a {call.get('cls')} call at {derive_iso(call['t'])} flagged "
                                    "destructive"})
    for row in model.get("record_rows") or []:
        if (row["kind"] == "review" and derive_review_verdict(row["reason"]) == "BLOCKED"
                and derive_review_exit(row["reason"]) == "CONVERGED"):
            out.append({"kind": "converged-on-blocked", "t": row["t"],
                        "evidence": f"review of {row['item']} at line {row['line']}: BLOCKED and "
                                    "CONVERGED"})
    for e in tl:
        if e["kind"] == "idle":
            out.append({"kind": "idle-gap", "t": e["t"], "evidence": f"{int(e['dur'])} s with no event of "
                                                        f"any source from {derive_iso(e['t'])}"})
    for other in model.get("shared_sessions", []):
        out.append({"kind": "multi-run-session", "t": None,
                    "evidence": f"a session of this run also started {other['starts']} verb(s) of "
                                f"{other['slug']}"})
    heads = sorted([c["t"] for c in own] + [c["t"] for c in model.get("record_commits", [])])
    for streak in scan_heartbeat_streaks(verbs, heads):
        if len(streak) >= STALL_HEARTBEATS:
            out.append({"kind": "stalled", "t": streak[0]["t"],
                        "evidence": f"{len(streak)} --status calls in a row from "
                                    f"{derive_iso(streak[0]['t'])} to {derive_iso(streak[-1]['end'])} "
                                    f"with phase {streak[0]['phase_to']} and no commit; the rule is "
                                    f"{STALL_HEARTBEATS} heartbeats, one hour at the declared "
                                    f"{HEARTBEAT_CADENCE_S} s cadence"})
    return out


def scan_heartbeat_streaks(verbs, heads) -> list:
    """Maximal runs of consecutive ended `--status` calls sharing one `phase_to` with no commit of the
    run between their first START and their last END. Any other verb breaks a run."""
    streaks, cur = [], []
    for e in verbs:
        beat = e["verb"] == "--status" and e["state"] == "ended" and e.get("end") is not None
        if not beat:
            streaks.append(cur)
            cur = []
            continue
        if cur and (e["phase_to"] != cur[0]["phase_to"]
                    or any(cur[0]["t"] <= h <= e["end"] for h in heads)):
            streaks.append(cur)
            cur = []
        cur.append(e)
    streaks.append(cur)
    return [s for s in streaks if s]


# ---------------------------------------------------------------------------------- the join

def scan_spec_marks(section_text) -> list:
    squeezed = " ".join((section_text or "").split())
    return [(m.group(1), m.group(2), bool(m.group(3))) for m in MARK_RE.finditer(squeezed)]


def extract_open_questions(text) -> str:
    """The body of a spec's section 8, which is where the fork marks live."""
    out, inside = [], False
    for line in (text or "").split("\n"):
        if line.startswith("## "):
            inside = line.startswith("## 8.")
            continue
        if inside:
            out.append(line)
    return "\n".join(out)


def build_unit_id_re(slug) -> re.Pattern:
    """A unit id of ONE build, as a word: `<FAMILY>-<slug>-<n>`."""
    return re.compile(r"\b[A-Z]+-" + re.escape(slug) + r"-[0-9]+\b")


def derive_spec_unit(text, id_re) -> dict | None:
    """The unit a spec's text defines: the first of the build's ids on its `# ` title line, with the
    status and order its status header carries. None when the text defines no unit. `read_units` reads
    the working tree through this and the schema leg (TOOL-dLoggedFlight-10) reads staged bytes through
    it, so the two cannot disagree about which unit a spec defines."""
    first = (text or "").split("\n", 1)[0]
    m = id_re.search(first)
    if not first.startswith("# ") or not m:
        return None
    status = order = None
    for line in text.split("\n")[:12]:
        if line.startswith("**Status:**"):
            status = line[len("**Status:**"):].split("·")[0].strip()
            om = re.search(r"·\s*order\s+([0-9]+)", line)
            order = int(om.group(1)) if om else None
    return {"id": m.group(0), "status": status, "order": order}


def read_units(root, build, id_re) -> list:
    """The build's units from its specs' status headers: id, status, order and path. A build with no
    specs has an empty unit table."""
    units = []
    spec_dir = root / build / "spec"
    for p in sorted(spec_dir.glob("*.md")) if spec_dir.is_dir() else []:
        try:
            text = p.read_bytes().decode("utf-8", "replace")
        except OSError:
            continue
        unit = derive_spec_unit(text, id_re)
        if unit is not None:
            units.append(dict(unit, spec=p.relative_to(root).as_posix()))
    return units


def read_ledger_lines(root, paths) -> list:
    """Acceptance lines not met, from the ledger files the run's commits touched."""
    out = []
    for rel in sorted(set(paths)):
        p = root / rel
        try:
            lines = p.read_bytes().decode("utf-8", "replace").split("\n")
        except OSError:
            continue
        i = 0
        while i < len(lines):
            m = AC_LINE_RE.match(lines[i])
            if not m:
                i += 1
                continue
            text, j = lines[i], i + 1
            while j < len(lines) and lines[j].startswith("  ") and not AC_LINE_RE.match(lines[j]):
                text += " " + lines[j].strip()
                j += 1
            if LEDGER_UNMET_RE.search(text):
                out.append({"ref": f"{rel}:{i + 1}", "ac": m.group(1)})
            i = j
    return out


def read_review_records(root, paths) -> list:
    out = []
    for rel in sorted(set(paths)):
        try:
            lines = (root / rel).read_bytes().decode("utf-8", "replace").split("\n")
        except OSError:
            continue
        verdict, line = None, None
        for n, text in enumerate(lines, 1):
            m = VERDICT_RE.match(text.rstrip("\r"))
            if m:
                verdict, line = m.group(1).strip(), n
                break
        out.append({"path": rel, "line": line, "verdict": verdict})
    return out


def build_run_model(root, slug, run=None, journal_root=None, store=None, projects=None,
                    default_ref=None) -> RunModel:
    """Join every source of ONE run of `slug` into a `RunModel`. `run` is the 1-up run number and
    defaults to the last. `journal_root`, `store` and `projects` default to nothing, so a caller that
    wants the machine's own journals and extracts resolves and passes them; a missing one is a coverage
    state, never an error. Raises ValueError when the build has no committed run-state file or the run
    number names no run."""
    wall0 = time.perf_counter()
    calls0 = GIT_CALLS[0]
    root = pathlib.Path(root)
    mr = rl.resolve_memory_root(root)
    build = f"{mr}/builds/{slug}"
    id_re = build_unit_id_re(slug)
    slug_re = re.compile(r"\b" + re.escape(slug) + r"\b")

    runs = derive_run_starts(root, mr, [slug]).get(slug, [])                          # git 1
    if not runs:
        raise ValueError(f"runlog: {slug} has no run-state file that was ever committed, so no run "
                         "has a start commit")
    k = len(runs) if run is None else int(run)
    if not 1 <= k <= len(runs):
        raise ValueError(f"runlog: {slug} has {len(runs)} run(s); there is no run {k}")
    pick = runs[k - 1]
    era = derive_run_eras(runs)[k - 1]
    try:
        text = (root / pick["record"]).read_bytes().decode("utf-8", "replace")
    except OSError:
        text = None
    record, record_state = read_run_state(text, pick["record"])
    facts = record["facts"]
    phase = derive_phase(text)
    terminal = phase in PHASES_TERMINAL

    refs = read_refs(root)                                                              # git 2
    default_refname, default_name = resolve_default_ref(refs, default_ref)
    tips = []
    branch_ref = facts.get("branch-ref") or ""
    if branch_ref in refs["refs"]:
        tips.append(branch_ref)
    if default_refname and default_refname not in tips:
        tips.append(default_refname)
    if refs["head"] and not tips:
        tips.append(refs["head"])

    # The run-state history, over HEAD and the run's own branch where it resolves.
    hist_tips = [t for t in ([refs["head"]] if refs["head"] else []) + tips]
    history = read_git_range(root, list(dict.fromkeys(hist_tips)),                      # git 3
                             paths=[f"{build}/RUN.md", f"{build}/RUN.*.md"])
    live_path = f"{build}/RUN.md"
    record_commits = derive_record_commits(history, era, live_path)
    # The own-commit range: descendants of the start commit, on the run's branch and the default one.
    span = read_git_range(root, ["--ancestry-path", f"^{pick['start']}", *tips]) if tips else []  # git 4
    era_commits = sorted((c for c in span if check_in_era(c["t"], era)), key=lambda c: c["t"])
    own = [c for c in era_commits if id_re.search(c["subject"])]
    own_shas = {c["sha"] for c in own}
    last_own = own[-1]["sha"] if own else None
    merged = None
    descendants: set = set()
    if last_own:
        raw = run_git(root, ["rev-list", "--ancestry-path", f"^{last_own}", "--branches",   # git 5
                             "--remotes"]).decode("utf-8", "replace")
        descendants = set(raw.split())
        tip_sha = refs["refs"].get(default_refname) if default_refname else None
        merged = bool(tip_sha) and (tip_sha == last_own or tip_sha in descendants)

    # Every blob, through ONE cat-file.
    era_end_rev = (refs["head"] or "HEAD") if era["next"] is None else f"{era['next']}^"
    units = read_units(root, build, id_re)
    requests = [f"{c['sha']}:{live_path}" for c in record_commits]
    for u in units:
        requests += [f"{pick['start']}^:{u['spec']}", f"{era_end_rev}:{u['spec']}"]
    log_path = f"{mr}/{DECISION_LOG}"
    log_commits = [c for c in own if len(c["parents"]) == 1 and any(p == log_path for _, p in c["files"])]
    for c in log_commits:
        requests += [f"{c['sha']}^:{log_path}", f"{c['sha']}:{log_path}"]
    blobs = read_blobs(root, requests) if requests else {}                              # git 6

    # ---- journals
    journals = read_journals(journal_root)
    dj = journals["driver"]["journal"]
    all_invs = [derive_invocation(inv) for inv in rl.build_invocations(dj.lines)]
    invs = sorted((i for i in all_invs if i["slug"] == slug and i["t"] is not None), key=lambda i: i["t"])
    joined, unjoined = derive_journal_join(invs, runs)
    seg_starts = []
    for r in runs:
        st = joined.get(r["k"])
        seg_starts.append(st["t"] if st else float(r["t"]))
    seg_start = seg_starts[k - 1]
    seg_end = seg_starts[k] if k < len(runs) else None
    for u in unjoined:
        if u["t"] > seg_start and (seg_end is None or u["t"] < seg_end):
            seg_end = u["t"]
            break
    seg = [i for i in invs if i["t"] >= seg_start and (seg_end is None or i["t"] < seg_end)]

    # ---- the window (spec S2)
    start_st = joined.get(k)
    w_start = start_st["t"] if start_st else float(pick["t"])
    w_from = "driver" if start_st else "git"
    # The terminal END is the verb that MOVED the phase into a terminal one: its START read a phase
    # that was not terminal. A `--status` after landing reads LANDED on both lines and ends nothing.
    term_end = next((i["end"] for i in seg if i["state"] == "ended" and i["end"] is not None
                     and (i["phase_to"] or "") in PHASES_TERMINAL
                     and (i["phase_from"] or "") not in PHASES_TERMINAL), None)
    phases_at = [(c, derive_phase(blobs.get(f"{c['sha']}:{live_path}"))) for c in record_commits]
    window = derive_window(w_start, w_from, phases_at, terminal, term_end,
                           max((i["end"] or i["t"] for i in seg), default=None))
    w_end = window["end"]

    def check_in_window(t) -> bool:
        return t is not None and w_start <= t < w_end

    worktrees = sorted({derive_path_key(i["wt"]) for i in seg if i["wt"]})
    sids = sorted({s for i in seg for s in i["sids"]})

    # ---- timeline
    timeline = []
    prev = None
    for c, ph in phases_at:
        if ph and ph != prev:
            timeline.append({"t": float(c["t"]), "source": "run-state", "kind": "phase", "phase": ph,
                             "witness": derive_fact(blobs.get(f"{c['sha']}:{live_path}"), "witness"),
                             "sha": c["sha"]})
        prev = ph or prev
    for i in seg:
        timeline.append({"t": i["t"], "source": "driver", "kind": "verb", "verb": i["verb"],
                         "end": i["end"], "state": i["state"], "rc": i["rc"], "exit": i["exit"],
                         "checks": i["checks"], "phase_from": i["phase_from"],
                         "phase_to": i["phase_to"], "unit": i["unit"], "oob": i["oob"]})
    for c in era_commits:
        is_merge = len(c["parents"]) > 1
        if c["sha"] in own_shas or (is_merge and slug_re.search(c["subject"])):
            timeline.append({"t": float(c["t"]), "source": "git", "kind": "merge" if is_merge else "commit",
                             "sha": c["sha"], "units": sorted(set(id_re.findall(c["subject"]))),
                             "own": c["sha"] in own_shas})
    pushes = journals["pushes"]["journal"]
    push_invs = rl.build_invocations(pushes.lines)
    pinned = set()
    push_nums, gate_nums = set(), set()
    for inv in push_invs:
        s = inv.start.fields if inv.start else {}
        e = inv.end.fields if inv.end else {}
        t = parse_float(s.get("t"))
        if not check_in_window(t):
            continue
        refs_pushed = [v for key, v in s.items() if key.startswith("ref.")]
        via = None
        if derive_path_key(s.get("wt")) in worktrees:
            via = "worktree"
        elif last_own and default_name:
            for r in refs_pushed:
                bits = r.split()
                if (len(bits) == 4 and bits[2] == f"refs/heads/{default_name}"
                        and (bits[1] == last_own or bits[1] in descendants)):
                    via = "pushed-sha"
        if via is None:
            continue
        push_nums.update(ln.lineno for ln in (inv.start, inv.end) if ln is not None and ln.lineno)
        if e.get("gate_run"):
            pinned.add(e["gate_run"])
        timeline.append({"t": t, "source": "pushes", "kind": "push", "via": via,
                         "lander": s.get("lander"), "refs": refs_pushed, "end": parse_float(e.get("t")),
                         "decision": e.get("decision"), "rc": e.get("rc"), "exit": e.get("exit"),
                         "gate_run": e.get("gate_run")})
    for line in pushes.lines:
        f = line.fields
        t = parse_float(f.get("t"))
        if f.get("ev") == "once" and check_in_window(t) and derive_path_key(f.get("wt")) in worktrees:
            push_nums.add(line.lineno)
            timeline.append({"t": t, "source": "pushes", "kind": "push-refused",
                             "decision": f.get("decision"), "lander": f.get("lander")})
    for line in journals["gates"]["journal"].lines:
        f = line.fields
        t = parse_float(f.get("t"))
        via = None
        if f.get("run") and f["run"] in pinned:
            via = "gate_run"
        elif check_in_window(t) and derive_path_key(f.get("wt")) in worktrees:
            via = "worktree"
        if via:
            gate_nums.add(line.lineno)
            timeline.append({"t": t, "source": "gates", "kind": "gate", "via": via, "run": f.get("run"),
                             "verdict": f.get("verdict"), "head": f.get("head"), "rc": f.get("rc"),
                             "failed": f.get("failed")})
    for row in record["rows"]:
        if row["kind"] in ("dispatch", "brief") and check_in_window(row["t"]):
            unit = (id_re.findall(row["item"]) or [None])[-1]
            timeline.append({"t": row["t"], "source": "run-state", "kind": row["kind"], "unit": unit,
                             "line": row["line"]})

    # ---- sessions, from the extractor where local
    extracts, tr_state, tr_note = resolve_run_sessions(sids, slug, store, projects)
    tools, turns = [], []
    for sid, data in sorted(extracts.items()):
        events = data.get("events", [])
        ends = {ev.get("call"): ev for ev in events if ev.get("kind") == "tool_end"}
        for ev in events:
            kind, t = ev.get("kind"), ev.get("t")
            if kind == "owner":
                turns.append((t, sid))
            if kind in ("owner", "compact", "limit") and check_in_window(t):
                timeline.append({"t": t, "source": "transcripts", "kind": kind,
                                 **({"via": ev.get("via")} if kind == "owner" else {})})
            # A workflow run with its label: the extractor keeps a label only token-shaped and clean
            # under the redaction table, and the committed record admits it only in its own class.
            if kind == "workflow" and check_in_window(t):
                timeline.append({"t": t, "source": "transcripts", "kind": "workflow",
                                 "label": ev.get("label")})
            if kind == "tool" and check_in_window(t):
                note = ends.get(ev.get("call")) if ev.get("bg") else None
                tools.append({"t": t, "end": ev.get("end"), "cls": ev.get("cls"), "bg": ev.get("bg"),
                              "rc": note.get("rc") if note else ev.get("rc"),
                              "flags": ev.get("flags") or []})
    timeline.sort(key=lambda e: (e["t"], e["source"], e["kind"]))
    # ---- idle gaps (spec S6, rev-6), over EVERY source with a tool call covering its span, and never
    # with an owner turn as an event. Rev-5 read the timeline alone, which holds no tool call, so every
    # busy stretch read idle (H1), and an in-window owner turn became a gap's start or end, which the
    # record renders (B1). Judged only where every named session's transcript is local, since only
    # then is every call seen and every owner turn the guard needs known.
    idle = {"judged": tr_state == "present", "gaps": None, "near_owner": None}
    if idle["judged"]:
        spans = [(e["t"], e.get("end") if e["kind"] in ("verb", "push") else None)
                 for e in timeline if e["kind"] != "owner"]
        spans += [(ev.get("t"), ev.get("end") if ev.get("kind") == "tool" else None)
                  for data in extracts.values() for ev in data.get("events", []) if ev.get("kind") != "owner"]
        gaps, near = derive_idle_gaps(spans, [t for t, _sid in turns], w_start, w_end)
        for a, b in gaps:
            timeline.append({"t": a, "source": "model", "kind": "idle", "dur": b - a})
        idle.update(gaps=len(gaps), near_owner=near)
    else:
        idle["note"] = ("idleness is judged only where every named session's transcript is local, and "
                        f"the transcripts read {tr_state}")
    timeline.sort(key=lambda e: (e["t"], e["source"], e["kind"]))

    # ---- the close, and the head it ran at
    closes = [i for i in seg if i["verb"] == "--close" and i["state"] == "ended" and i["rc"] == "0"]
    close = {"t": None, "head": None}
    if closes:
        close["t"] = closes[-1]["end"]
        landing = next((c for c, ph in phases_at if ph in PHASES_CLOSED), None)
        close["head"] = (landing["parents"][0] if landing and landing["parents"] else refs["head"])

    # ---- units
    rows = record["rows"]
    for u in units:
        uid = u["id"]
        u["briefs"] = [r["t"] for r in rows if r["kind"] == "brief" and r["item"].strip() == uid]
        u["dispatches"] = [r["t"] for r in rows if r["kind"] == "dispatch" and uid in r["item"].split()]
        bc = next((c for c in own if len(c["parents"]) == 1 and uid in id_re.findall(c["subject"])
                   and any(not p.startswith(mr + "/") for _, p in c["files"])), None)
        u["build_commit"] = bc["sha"] if bc else None
        u["build_t"] = float(bc["t"]) if bc else None

    # ---- ledger inputs
    marks = []
    for u in units:
        before = Counter(scan_spec_marks(extract_open_questions(blobs.get(f"{pick['start']}^:{u['spec']}"))))
        at_end = Counter(scan_spec_marks(extract_open_questions(blobs.get(f"{era_end_rev}:{u['spec']}"))))
        for mark, n in sorted(at_end.items()):
            kept = min(n, before.get(mark, 0))
            for when, count in (("before", kept), ("inside", n - kept)):
                for _ in range(count):
                    marks.append({"resolver": mark[0], "when": when, "ref": u["spec"]})
    decision_rows = []
    for c in log_commits:
        old = Counter(ln for ln in (blobs.get(f"{c['sha']}^:{log_path}") or "").split("\n")
                      if ln.startswith("- "))
        new = Counter(ln for ln in (blobs.get(f"{c['sha']}:{log_path}") or "").split("\n")
                      if ln.startswith("- "))
        for ln, n in (new - old).items():
            for _ in range(n):
                head = ln[2:].split(" ", 1)[0]
                decision_rows.append({"sha": c["sha"], "owner": check_owner_row(ln),
                                      "id": head if re.fullmatch(r"[A-Z]+-[A-Za-z0-9]+-[0-9]+", head) else None})
    ledger_paths = {p for c in own for s, p in c["files"]
                    if s in "AM" and p.startswith(f"{build}/build/") and "acceptance-ledger" in p}
    review_paths = {p for c in era_commits for s, p in c["files"]
                    if s == "A" and p.startswith(f"{build}/reviews/") and p.endswith(".md")}
    ledger = scan_decisions({"record": record, "own_commits": own, "marks": marks,
                             "decision_rows": decision_rows, "reviews": read_review_records(root, review_paths),
                             "ledgers": read_ledger_lines(root, ledger_paths)})

    # ---- other slugs' starts sharing a session with this run
    shared = Counter()
    for i in all_invs:
        if i["slug"] and i["slug"] != slug and set(i["sids"]) & set(sids):
            shared[i["slug"]] += 1
    shared_sessions = [{"slug": s, "starts": n} for s, n in sorted(shared.items())]

    # ---- coverage
    lines = {"driver": sum((i["state"] != "orphan-end") + (i["end"] is not None) for i in seg),
             "gates": sum(1 for e in timeline if e["kind"] == "gate"),
             "pushes": sum(1 for e in timeline if e["kind"] in ("push", "push-refused"))}
    moves = [e for e in timeline if e["kind"] == "phase" and check_in_window(e["t"])]
    moves += [{"phase": e["phase_to"]} for e in timeline
              if e["kind"] == "verb" and e.get("phase_to") and check_in_window(e.get("end"))]
    in_rows = [r for r in rows if check_in_window(r["t"])]
    activity = {"driver": f"{len(in_rows)} parked row(s) in the window" if in_rows else None,
                "gates": ("a LANDING write in the window, which --close makes only after its bar"
                          if any(m["phase"] in PHASES_CLOSED for m in moves) else None),
                "pushes": ("a LANDED write in the window, which --landed makes only after the push"
                           if any(m["phase"] == "LANDED" for m in moves) else None)}
    transcripts = {"state": tr_state, "sessions": len(sids), "extracts": len(extracts)}
    if tr_note:
        transcripts["note"] = tr_note
    coverage = measure_coverage(journals, window, lines, activity, transcripts, record_state,
                                "present" if (root / build).is_dir() else "absent")
    attribution = derive_attribution(seg, extracts)
    coverage["attribution"] = {k2: attribution[k2] for k2 in ("calls", "attributed", "share_calls",
                                                               "wall_s", "attributed_wall_s",
                                                               "share_wall")}
    coverage["idle"] = idle
    coverage["unjoined_starts"] = [{"t": u["t"], "slug": u["slug"]} for u in unjoined]
    coverage["default_branch"] = default_name
    coverage["journal_starts"] = {"joined": len(joined), "record-creating": len(joined) + len(unjoined)}

    start_t = w_start
    close_t = close["t"] if close["t"] is not None else (term_end if term_end is not None else w_end)
    owner_positions = build_owner_positions(turns, start_t, close_t)
    usage = build_run_usage(extracts, w_start, w_end)

    model = RunModel(
        slug=slug, run=k, runs=len(runs), runkey=pick["runkey"], record=pick["record"],
        start_commit=pick["start"], era=era, window=window, phase=phase, terminal=terminal,
        facts=facts, repairs=record["repairs"], worktrees=worktrees, sessions=sids,
        own_commits=[{"sha": c["sha"], "t": c["t"], "units": sorted(set(id_re.findall(c["subject"]))),
                      "merge": len(c["parents"]) > 1, "subject": c["subject"]} for c in own],
        last_own=last_own, merged=merged, close=close, timeline=timeline, tools=tools,
        record_rows=rows, record_commits=[{"sha": c["sha"], "t": c["t"]} for c in record_commits],
        shared_sessions=shared_sessions, units=units, ledger=ledger, conformance=[], anomalies=[],
        owner_positions=owner_positions, usage=usage, attribution=attribution, coverage=coverage,
        journal_lines={"driver": sorted({n for i in seg for n in i["lines"]}),
                       "gates": sorted(gate_nums), "pushes": sorted(push_nums)})
    view = asdict(model)
    model.conformance = check_conformance(view)
    model.anomalies = scan_anomalies(view)
    model.cost = {"git_calls": GIT_CALLS[0] - calls0, "wall_s": round(time.perf_counter() - wall0, 3)}
    return model


def render_model_json(model) -> str:
    return json.dumps(asdict(model), indent=1, sort_keys=True, ensure_ascii=True)


def write_model_copy(model, store) -> pathlib.Path:
    """The model's local copy, beside the extracts: `<store>/models/<slug>-<runkey>.json`, contained."""
    store = pathlib.Path(store)
    target = store / MODELS_DIR / f"{model.slug}-{model.runkey}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    if not ex._check_inside(target, store.resolve()):
        raise ValueError(f"runlog: the model copy would land outside its store: {target}")
    tmp = target.with_name(f".{target.name}.{os.getpid()}.tmp")
    tmp.write_bytes((render_model_json(model) + "\n").encode("ascii"))
    os.replace(tmp, target)
    return target


def render_model_summary(model) -> str:
    """A few lines a person reads; `--json` prints the whole model."""
    cov = model.coverage
    lines = [f"runlog: model {model.slug} run {model.run} of {model.runs} · start {model.runkey} · "
             f"phase {model.phase or 'none'} · window {derive_iso(model.window['start'])} to "
             f"{derive_iso(model.window['end'])} ({model.window['end_from']})",
             "runlog: coverage " + " ".join(f"{s}={cov[s]['state']}" for s in SOURCE_NAMES),
             f"runlog: timeline {len(model.timeline)} · own commits {len(model.own_commits)} · ledger "
             + " ".join(f"{s}={n}" for s, n in model.ledger["counts"].items() if n),
             "runlog: conformance " + " ".join(f"{c['item']}={c['state']}" for c in model.conformance),
             "runlog: anomalies " + (" ".join(sorted(a["kind"] for a in model.anomalies)) or "none")]
    return "\n".join(lines)
