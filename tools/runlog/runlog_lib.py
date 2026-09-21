#!/usr/bin/env python3
"""runlog_lib.py — ONE line grammar every run-log producer writes, and ONE reader every consumer parses.

KIT_RUNLOG_VERSION below is the version constant a deployer greps; the README carries the same marker.

Three producers append one line per act to a machine-local journal: the unattended driver, the gate
runner and the pre-push hook. They are shell scripts, several consumers read what they write, and a
format that each side re-derives drifts on the first edit. So the grammar is implemented once HERE
and stated once in this kit's README, which is also where the reader's limits are listed. Neither is
restated in this docstring: a second prose copy of a grammar is the copy that rots. The self-test
grades this implementation against a golden line copied from every producer's data model.

The same module carries the kit's ONE redaction table reader, for the consumers that print or classify
free text a transcript holds. The rules are DATA in the table beside this file, whose header states
its columns; the README states what the table does not catch.

Every path this module touches is passed in, resolved from git, or is the table beside this file; it
names nothing outside itself.
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
# THE SLUG GRAMMAR, the unattended driver's own: its `check_slug_shape`, and hygiene check 4's default
# beside it, admit a letter, then letters, digits or dashes. One constant, so no reader in this kit
# refuses a build folder the driver accepts; the extractor kept a copy that refused dashed and
# single-letter slugs (L4 of the closing review, round 1). Read it with `fullmatch`. The withheld
# self-test holds it to that function, run by bash from the driver's source.
SLUG_RE = re.compile(r"[A-Za-z][A-Za-z0-9-]*")

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

    The truncation order it implements is the README's, stated there and nowhere else, because it is
    the half of the grammar a shell producer is most likely to get wrong and one statement of it is
    what that producer is graded against.
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

    A COPY of the memory-tree engine's own line reader, `parse_conf_line`, in its order, not an import
    of it: kits are copied into adopters independently. The withheld self-test holds this copy to that
    reader, and both to bash sourcing the same file, over a table of spellings (TOOL-dLoggedFlight-1
    AC10). The rules that change a value: an `export` prefix, a QUOTED value being the text up to its
    matching quote whatever follows it, an unquoted value ending at a `#` that begins a word, and the
    LAST assignment winning. The first cut told quoted from unquoted by whether the value's first and
    last characters matched, so `KEY="v"  # note` failed that test and kept its quotes (M7 of the
    closing review, round 1). The one deliberate departure from the engine and from bash is the leading
    BOM strip: a BOM-led conf is a real Windows artifact, and bash reads that first line as a command.
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
        k = k.strip()
        if k.startswith(("export ", "export\t")):
            k = k[len("export"):].strip()
        if k != key:
            continue
        v = v.strip()
        if v[:1] in ("'", '"'):
            close = v.find(v[0], 1)
            if close >= 0:
                found = v[1:close]
                continue
        # Unquoted, or a quote never closed, which bash itself refuses: a `#` that begins a word,
        # position 0 included, starts a comment, and a `#` inside a word is data.
        cut = next((i for i, ch in enumerate(v) if ch == "#" and (i == 0 or v[i - 1].isspace())), None)
        if cut is not None:
            v = v[:cut].strip()
        found = v.strip('"').strip("'")
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


# ---------------------------------------------------------------------------------- redaction

# The CLOSED list of secret classes (TOOL-dLoggedFlight-5 S2). The table beside this file holds one
# row per id, and the self-test asserts the two against each other in BOTH directions, so a class
# cannot go missing from the table and a row cannot arrive without being declared here first.
CLASS_IDS = ("url-userinfo", "auth-header", "bearer-token", "github-token", "sk-key", "aws-key",
             "aws-sts-key", "pem-block", "env-assign", "env-table", "jwt", "cookie", "json-secret",
             "conn-password", "azure-key", "vendor-key", "flag-secret", "lower-assign", "named-token")
TABLE_NAME = "redaction.tsv"
TABLE_COLUMNS = ("id", "hint", "pattern", "positive", "negative")
# What a redacted value becomes is `<redacted:<id>>`. A value that already starts with this head is
# never matched again, which is what keeps a rendered text clean under a second scan.
PLACEHOLDER_HEAD = "<redacted:"
_RULE_ID_RE = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*")
# The kit's own table, compiled once on first use and never at import: a consumer that never redacts
# pays nothing, and the parse arm's zero-compile count is not disturbed by a table it does not read.
_DEFAULT_RULES: tuple | None = None


@dataclass(frozen=True, slots=True)
class Rule:
    """One row of the redaction table, compiled.

    `pattern` is the compiled regex, and the only method called on it is `finditer`. That is the seam
    a caller counting regex searches wraps; nothing else about the object is assumed.
    """
    id: str
    hints: tuple
    pattern: object
    positive: str
    negative: str
    lineno: int = 0


def load_rules(path=None) -> tuple:
    """Read and compile a redaction table: the kit's own by default. Raises ValueError naming the line.

    Read as BYTES and split on LF. A CR ending a line is dropped, so a CRLF checkout reads the same
    table; a CR anywhere else is refused. Every malformed row is refused by name rather than skipped,
    because a skipped row is a secret class that silently stopped being redacted.
    """
    p = pathlib.Path(path) if path is not None else pathlib.Path(__file__).resolve().parent / TABLE_NAME
    where = p.name
    try:
        raw = p.read_bytes()
    except OSError as exc:
        raise ValueError(f"runlog: the redaction table {where} could not be read: {exc}") from exc
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"runlog: the redaction table {where} is not UTF-8: {exc}") from exc
    rules: list[Rule] = []
    seen: set[str] = set()
    header = False
    for lineno, line in enumerate(text.split("\n"), 1):
        if line.endswith("\r"):
            line = line[:-1]
        if "\r" in line:
            raise ValueError(f"runlog: {where}:{lineno} carries a lone CR inside a row")
        if not line or line.startswith("#"):
            continue
        cells = line.split("\t")
        if not header:
            if tuple(cells) != TABLE_COLUMNS:
                raise ValueError(f"runlog: {where}:{lineno} is not the header row "
                                 f"{' TAB '.join(TABLE_COLUMNS)}")
            header = True
            continue
        if len(cells) != len(TABLE_COLUMNS):
            raise ValueError(f"runlog: {where}:{lineno} has {len(cells)} columns, not "
                             f"{len(TABLE_COLUMNS)}")
        for name, cell in zip(TABLE_COLUMNS, cells):
            if not cell.strip():
                raise ValueError(f"runlog: {where}:{lineno} has an empty {name} cell")
        rid, hint, source, positive, negative = cells
        if _RULE_ID_RE.fullmatch(rid) is None:
            raise ValueError(f"runlog: {where}:{lineno} has the id {rid[:40]!r}, outside the id "
                             "grammar of lowercase words joined by '-'")
        if rid in seen:
            raise ValueError(f"runlog: {where}:{lineno} carries the id {rid!r} twice")
        hints = tuple(hint.split("|"))
        if any(not h or h != h.lower() for h in hints):
            raise ValueError(f"runlog: {where}:{lineno} ({rid}) has a hint that is empty or not "
                             "lowercase, and a hint is matched against lowercased text")
        try:
            compiled = re.compile(source)
        except re.error as exc:
            raise ValueError(f"runlog: {where}:{lineno} ({rid}) has a pattern that does not "
                             f"compile: {exc}") from exc
        if "v" not in compiled.groupindex:
            raise ValueError(f"runlog: {where}:{lineno} ({rid}) has a pattern with no named group "
                             "v, so it names no value to redact")
        rules.append(Rule(id=rid, hints=hints, pattern=compiled, positive=positive,
                          negative=negative, lineno=lineno))
        seen.add(rid)
    if not header:
        raise ValueError(f"runlog: the redaction table {where} has no header row")
    if not rules:
        raise ValueError(f"runlog: the redaction table {where} has no rule row")
    return tuple(rules)


def _load_default_rules() -> tuple:
    global _DEFAULT_RULES
    if _DEFAULT_RULES is None:
        _DEFAULT_RULES = load_rules()
    return _DEFAULT_RULES


def scan_secrets(text, rules=None) -> list:
    """Every secret VALUE in `text`, as sorted `(start, end, rule_id)` spans. Values never leave it.

    Rules run in table order. A rule's regex runs only when the lowercased text holds one of its
    hints, and once per such rule, which is the count a wrapped pattern observes. A span overlapping
    one an earlier rule took is dropped, and so is a value that already reads as a placeholder.
    """
    if not isinstance(text, str):
        raise TypeError(f"scan_secrets reads a str, not {type(text).__name__}; decode it first")
    if not text:
        return []
    table = _load_default_rules() if rules is None else rules
    low = text.lower()
    taken: list[tuple[int, int, str]] = []
    for rule in table:
        for hint in rule.hints:
            if hint in low:
                break
        else:
            continue
        for match in rule.pattern.finditer(text):
            start, end = match.span("v")
            if start >= end or text.startswith(PLACEHOLDER_HEAD, start):
                continue
            if any(start < t_end and t_start < end for t_start, t_end, _ in taken):
                continue
            taken.append((start, end, rule.id))
    taken.sort()
    return taken


def render_redacted(text, rules=None) -> str:
    """`text` with every value `scan_secrets` finds replaced by `<redacted:<id>>`, keys kept."""
    spans = scan_secrets(text, rules)
    if not spans:
        return text
    out = []
    pos = 0
    for start, end, rid in spans:
        out.append(text[pos:start])
        out.append(f"{PLACEHOLDER_HEAD}{rid}>")
        pos = end
    out.append(text[pos:])
    return "".join(out)
