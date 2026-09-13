#!/usr/bin/env python3
"""runlog_lib.py — ONE line grammar every run-log producer writes, and ONE reader every consumer parses.

KIT_RUNLOG_VERSION below is the version constant a deployer greps; the README carries the same marker.

Three producers append one line per act to a machine-local journal: the unattended driver, the gate
runner and the pre-push hook. They are shell scripts, several consumers read what they write, and a
format that each side re-derives drifts on the first edit. So the grammar is stated once in this
kit's README, implemented once here, and graded by the self-test against a golden line copied from
every producer's data model.

THE GRAMMAR, in the order a reader applies it. One act is one line, ending in LF. Fields are
TAB-separated and every field is `key=value`, split on the FIRST `=`, so a value may carry `=`.
Field 1 is `v=<grammar version>`, and a version this reader does not know is refused rather than
guessed at. A key is `[a-z][a-z0-9_]*` with an optional `.` suffix of `[A-Za-z0-9_]+`; the suffix is
an INDEX when it is all digits. Values escape exactly four bytes — backslash, TAB, LF and CR — and
nothing else. `v`, `t`, `p` and `ev` are required. `ev` is `start`, `end` or `once`, and a `start` or
an `end` also requires `n`, the nonce the pair shares. A key a reader does not know is KEPT.

WHAT THIS DOES NOT CHECK, stated because a structural check reads as a semantic one:
  - whether a VALUE means anything. `rc=banana` parses. The grammar is syntax; each producer's own
    suite grades its values.
  - whether a line cut at a field boundary was cut. A writer killed after `ev=start\tn=1` and before
    the rest leaves a line that still parses. A torn line is caught only when the cut breaks the
    grammar — a missing required key, a broken escape, a missing LF at end of file — and is then
    COUNTED rather than dropped, which is the most a line-local reader can promise.
  - whether a journal is complete. A producer that never wrote leaves nothing to count.

Every path this module touches is passed in or resolved from git; it names nothing outside itself.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
from dataclasses import dataclass, field

KIT_RUNLOG_VERSION = "1.0"  # gov:kit runlog@1.0

# The grammar versions this reader knows. A set, so a v2 reader can keep reading v1 lines.
GRAMMAR_VERSIONS = frozenset({"1"})
# The byte cap on one line, NOT counting its terminating LF. Small enough that a producer's single
# `printf >>` stays one write, which is what keeps concurrent appends from interleaving in practice.
MAX_LINE_BYTES = 2048
EVENTS = frozenset({"start", "end", "once"})
PAIRED_EVENTS = frozenset({"start", "end"})
REQUIRED_KEYS = ("t", "p", "ev")
# The location contract (spec S2): one file per producer, under `runlog` in the git COMMON dir, so a
# linked worktree and the primary tree of one clone write and read the same three files.
JOURNAL_DIR = "runlog"
PRODUCER_FILES = {"driver": "driver.log", "gates": "gates.log", "pushes": "pushes.log"}
# The memory tree's declaration, owned by the memory-tree kit. Read here and never written.
CONF_NAME = ".memory-tree.conf"
MEMORY_ROOT_DEFAULT = "memory"
# The invocation states `build_invocations` assigns. A start with no end is NOT called "killed": a
# verb still running when the journal is read looks exactly the same, and the name says so.
INVOCATION_STATES = ("ended", "killed-or-running", "orphan-end")

# Compiled ONCE, at import. The parser calls only these objects' methods, so reading a journal of any
# length compiles nothing per line — the self-test counts that by patching `re.compile`.
_KEY_RE = re.compile(r"[a-z][a-z0-9_]*(?:\.[A-Za-z0-9_]+)?")
_TIME_RE = re.compile(r"[0-9]+(?:\.[0-9]{1,6})?")
# Keys already graded, so the regex runs once per DISTINCT key rather than once per field. Bounded,
# because the keys come from a file anybody can write and an unbounded cache is a memory leak with an
# attacker-chosen size.
_KEYS_OK: set[str] = set()
_KEYS_OK_CAP = 4096
_UNESCAPES = {"\\": "\\", "t": "\t", "n": "\n", "r": "\r"}
# The longest a line may be in CHARACTERS before its byte length can exceed the cap: UTF-8 spends at
# most four bytes on one character, so a shorter string cannot be over and is never encoded to check.
_CHARS_ALWAYS_UNDER = MAX_LINE_BYTES // 4


@dataclass(frozen=True, slots=True)
class JournalLine:
    """One parsed line. `fields` keeps the line's own key order, unknown keys included."""
    fields: dict
    lineno: int = 0


@dataclass(frozen=True, slots=True)
class Invocation:
    """A `start` and its `end`, paired on (`p`, `n`). Either half may be absent; `state` says which."""
    key: tuple
    state: str
    start: JournalLine | None
    end: JournalLine | None


@dataclass(frozen=True)
class Journal:
    """What `read_journal` found. `state` is `absent`, `empty`, `read` or `unreadable`.

    `bad` is `len(refusals)`, set once by the builder so the count and the reasons cannot disagree.
    """
    path: str
    state: str
    lines: list = field(default_factory=list)
    refusals: list = field(default_factory=list)
    bad: int = 0
    note: str = ""


def _build_journal(path: str, state: str, lines: list, refusals: list, note: str = "") -> Journal:
    return Journal(path=path, state=state, lines=lines, refusals=refusals, bad=len(refusals),
                   note=note)


# ---------------------------------------------------------------------------------- one value

def _parse_value(raw: str) -> str:
    """Undo the four escapes. Any other byte after a backslash, or a lone trailing one, is refused."""
    if "\\" not in raw:
        return raw
    out = []
    i, size = 0, len(raw)
    while i < size:
        j = raw.find("\\", i)
        if j < 0:
            out.append(raw[i:])
            break
        out.append(raw[i:j])
        if j + 1 >= size:
            raise ValueError("a value ends in a lone backslash, which escapes nothing")
        ch = _UNESCAPES.get(raw[j + 1])
        if ch is None:
            raise ValueError(f"a value carries the unknown escape \\{raw[j + 1]}; only \\\\ \\t \\n "
                             "\\r exist")
        out.append(ch)
        i = j + 2
    return "".join(out)


def _render_value(value: str) -> str:
    """Escape the four bytes the grammar escapes. The backslash goes FIRST, or it re-escapes the rest."""
    if "\\" in value:
        value = value.replace("\\", "\\\\")
    return value.replace("\t", "\\t").replace("\n", "\\n").replace("\r", "\\r")


def _check_key(key: str) -> bool:
    if key in _KEYS_OK:
        return True
    if _KEY_RE.fullmatch(key) is None:
        return False
    if len(_KEYS_OK) < _KEYS_OK_CAP:
        _KEYS_OK.add(key)
    return True


# ---------------------------------------------------------------------------------- one line

def parse_line(raw: str, lineno: int = 0) -> JournalLine:
    """Parse one line, given WITHOUT its LF. Raises ValueError naming the rule the line breaks."""
    if "\r" in raw:
        raise ValueError("an unescaped CR, which the grammar writes as \\r")
    if "\n" in raw:
        raise ValueError("an unescaped LF, so this is two lines or a torn one")
    if len(raw) > _CHARS_ALWAYS_UNDER and len(raw.encode("utf-8")) > MAX_LINE_BYTES:
        raise ValueError(f"over the {MAX_LINE_BYTES}-byte line cap")
    parts = raw.split("\t")
    head = parts[0]
    if not head.startswith("v="):
        raise ValueError("field 1 is not v=<grammar version>")
    if head[2:] not in GRAMMAR_VERSIONS:
        raise ValueError(f"an unknown grammar version {head!r}; this reader knows "
                         f"{sorted(GRAMMAR_VERSIONS)}")
    fields: dict[str, str] = {}
    for part in parts:
        key, sep, value = part.partition("=")
        if not sep:
            raise ValueError(f"a field with no '=' ({part[:40]!r}), so the line is torn or not "
                             "this grammar")
        if not _check_key(key):
            raise ValueError(f"a key outside the key grammar: {key[:40]!r}")
        if key in fields:
            raise ValueError(f"the key {key!r} twice, which is two lines run together")
        fields[key] = _parse_value(value)
    for key in REQUIRED_KEYS:
        if not fields.get(key):
            raise ValueError(f"the required key {key!r} is missing or empty")
    if _TIME_RE.fullmatch(fields["t"]) is None:
        raise ValueError(f"t={fields['t'][:40]!r} is not epoch seconds with a '.' radix and at "
                         "most six fraction digits")
    ev = fields["ev"]
    if ev not in EVENTS:
        raise ValueError(f"an unknown event ev={ev[:40]!r}; the events are {sorted(EVENTS)}")
    if ev in PAIRED_EVENTS and not fields.get("n"):
        raise ValueError(f"an ev={ev} line with no nonce n, so it can pair with nothing")
    return JournalLine(fields=fields, lineno=lineno)


def check_line(raw: str) -> str | None:
    """The verdict on one line: None when it conforms, else the reason `parse_line` would raise."""
    try:
        parse_line(raw)
    except ValueError as exc:
        return str(exc)
    return None


def render_line(fields: dict) -> str:
    """The kit's REFERENCE writer: escape every value and fit the line under the cap. No LF appended.

    The truncation order is the grammar's, and it is the half a producer is most likely to get wrong:
    drop WHOLE indexed fields, highest index first, counting each family's drops into
    `<base>_more` (added to any count the producer already wrote), and only when no indexed field is
    left, cut the longest non-required value from its end. A cut never ends inside an escape. A cut
    value carries no marker; no producer's data model reaches that step, and the README says so.
    """
    items = [[str(k), _render_value(str(v))] for k, v in fields.items()]
    if not items or items[0][0] != "v":
        raise ValueError("field 1 must be v")
    for key, _ in items:
        if not _check_key(key):
            raise ValueError(f"a key outside the key grammar: {key[:40]!r}")

    def measure_bytes() -> int:
        return len("\t".join(f"{k}={v}" for k, v in items).encode("utf-8"))

    size = measure_bytes()
    while size > MAX_LINE_BYTES:
        # The highest index across every family; on a tie the LATER field, so the drop is the one a
        # reader would least miss. A non-digit suffix (`sess.<NAME>`) is a name, never an index.
        best, top = -1, -1
        for i, (key, _) in enumerate(items):
            _, dot, suffix = key.partition(".")
            if dot and suffix.isdigit() and int(suffix) >= top:
                best, top = i, int(suffix)
        if best < 0:
            break
        base = items[best][0].partition(".")[0]
        del items[best]
        more = f"{base}_more"
        for pair in items:
            if pair[0] == more:
                try:
                    pair[1] = str(int(pair[1]) + 1)
                except ValueError:
                    raise ValueError(f"{more}={pair[1]!r} is not a count, so a drop cannot be "
                                     "added to it") from None
                break
        else:
            items.append([more, "1"])
        size = measure_bytes()
    protected = set(("v", "n") + REQUIRED_KEYS)
    while size > MAX_LINE_BYTES:
        cands = [i for i, (k, v) in enumerate(items)
                 if k not in protected and not k.endswith("_more") and v]
        if not cands:
            raise ValueError("the required fields alone are over the line cap")
        idx = max(cands, key=lambda i: len(items[i][1].encode("utf-8")))
        raw = items[idx][1].encode("utf-8")
        cut = raw[:max(0, len(raw) - (size - MAX_LINE_BYTES))].decode("utf-8", "ignore")
        while cut.endswith("\\") and (len(cut) - len(cut.rstrip("\\"))) % 2 == 1:
            cut = cut[:-1]
        items[idx][1] = cut
        size = measure_bytes()
    return "\t".join(f"{k}={v}" for k, v in items)


# ---------------------------------------------------------------------------------- a journal

def read_journal(path) -> Journal:
    """Read one producer file. Never raises: every outcome is a named `state` or a counted refusal.

    Read as BYTES and split on LF alone, so a lone CR stays inside the line that carries it and is
    refused there, and a torn multi-byte character fails one line's decode instead of the file's.
    """
    p = pathlib.Path(path)
    shown = p.as_posix()
    try:
        data = p.read_bytes()
    except FileNotFoundError:
        return _build_journal(shown, "absent", [], [])
    except OSError as exc:
        return _build_journal(shown, "unreadable", [], [], f"{type(exc).__name__}: {exc}")
    if not data:
        return _build_journal(shown, "empty", [], [])
    chunks = data.split(b"\n")
    tail = chunks.pop()
    lines: list[JournalLine] = []
    refusals: list[tuple[int, str]] = []
    for lineno, chunk in enumerate(chunks, 1):
        # No byte-cap test here: `parse_line` owns the cap, and a second copy of it in this loop was
        # a branch no arm could turn red, because the first one always caught the line anyway.
        try:
            text = chunk.decode("utf-8")
        except UnicodeDecodeError:
            refusals.append((lineno, "not UTF-8, which a torn multi-byte write leaves behind"))
            continue
        try:
            lines.append(parse_line(text, lineno))
        except ValueError as exc:
            refusals.append((lineno, str(exc)))
    if tail:
        refusals.append((len(chunks) + 1, "torn: the final line has no terminating LF"))
    return _build_journal(shown, "read", lines, refusals)


def build_invocations(lines) -> list[Invocation]:
    """Pair `start` and `end` lines on (`p`, `n`), in the order the starts and orphan ends appear.

    A `once` line is an act, never an invocation, and is skipped. An `end` pairs with the most recent
    unmatched `start` carrying its key; a second `end` for the same key is an orphan.
    """
    out: list[Invocation] = []
    waiting: dict[tuple, int] = {}
    for line in lines:
        f = line.fields
        ev = f.get("ev")
        if ev not in PAIRED_EVENTS:
            continue
        key = (f.get("p", ""), f.get("n", ""))
        if ev == "start":
            out.append(Invocation(key=key, state="killed-or-running", start=line, end=None))
            waiting[key] = len(out) - 1
            continue
        idx = waiting.pop(key, None)
        if idx is None:
            out.append(Invocation(key=key, state="orphan-end", start=None, end=line))
        else:
            out[idx] = Invocation(key=key, state="ended", start=out[idx].start, end=line)
    return out


# ---------------------------------------------------------------------------------- locations

def resolve_journal_root(start=None) -> pathlib.Path:
    """`<git common dir>/runlog` for the clone holding `start` (default: the cwd). ONE git call.

    `--path-format=absolute` is load-bearing: the bare `--git-common-dir` prints a RELATIVE `.git` in
    the primary tree, and `--git-dir` in a linked worktree names `.git/worktrees/<name>`, which would
    split one clone's journal in two.
    """
    cwd = None if start is None else str(start)
    try:
        out = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                             cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                             errors="replace")
    except OSError as exc:
        raise ValueError(f"runlog: git could not be run, so no journal root resolves: {exc}") from exc
    common = out.stdout.strip()
    if out.returncode != 0 or not common:
        raise ValueError(f"runlog: not inside a git work tree, so no journal root resolves: "
                         f"{cwd or '(the current directory)'}")
    return pathlib.Path(common) / JOURNAL_DIR


def _read_conf_key(path: pathlib.Path, key: str) -> str | None:
    """One key of a sourced `KEY=VALUE` conf, read the way bash sourcing reads it. None when absent.

    A narrow COPY of the grammar the memory-tree conf documents, not an import of another kit's
    reader: kits are copied into adopters independently. The rules kept are the ones that change a
    value — an `export ` prefix, a leading BOM, quotes keeping their contents, an unquoted value ending
    at whitespace so an inline comment cannot leak in, and the LAST assignment winning.
    """
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        return None
    except OSError as exc:
        raise ValueError(f"runlog: {path.name} could not be read: {exc}") from exc
    found = None
    for line in raw.decode("utf-8", "replace").split("\n"):
        line = line.lstrip("\ufeff").strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        if k.strip().removeprefix("export ").strip() != key:
            continue
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        else:
            v = v.split()[0] if v.split() else ""
        found = v
    return found


def resolve_memory_root(root) -> str:
    """The memory tree's repo-relative root, from `MEMORY_ROOT` in `.memory-tree.conf` at `root`.

    Slashes are stripped at both ends. An absent key — or an absent conf — is the kit default. A key
    naming no directory refuses, and so does one that would leave the repository, because a later
    unit WRITES under this root and a root of `..` would put that write in somebody else's tree.
    """
    value = _read_conf_key(pathlib.Path(root) / CONF_NAME, "MEMORY_ROOT")
    if value is None:
        return MEMORY_ROOT_DEFAULT
    stripped = value.strip("/")
    if not stripped:
        raise ValueError(f"runlog: MEMORY_ROOT in {CONF_NAME} names no directory ({value!r}), and "
                         "an empty root would put the memory tree at the repository root")
    if "\\" in stripped or ":" in stripped or ".." in stripped.split("/"):
        raise ValueError(f"runlog: MEMORY_ROOT in {CONF_NAME} leaves the repository ({value!r}); a "
                         "root is a repo-relative path with no '..' segment, drive or backslash")
    return stripped
