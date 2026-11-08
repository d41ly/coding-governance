#!/usr/bin/env python3
"""instruction_units.py — the instruction ladder, levels 0 to 7, and the one term for a place on it
(PLAY-dOrderedCharter-13); the statement grammar and the render provenance lock (PLAY-dOrderedCharter-12);
the instruction-unit registry, its one reader and documents rendered from units (PLAY-dOrderedCharter-9);
the unit schema, one fact in one unit, status from the change record, and the instruction-file population
the renderer-of-record table and the legacy list grade (PLAY-dOrderedCharter-20); the practice catalogue's
reader and its active set (PLAY-dOrderedCharter-1).

    python instruction_units.py ladder-terms             # the leg: no source names a ladder place by priority or rank
    python instruction_units.py grammar [--doc <path>]   # the leg: unit rows, unit-rendered documents, the lock
    python instruction_units.py lock --check             # the lock against the tree
    python instruction_units.py schema one-fact          # the leg: both verbs, each also run alone
    python instruction_units.py schema                   # every row's fields
    python instruction_units.py one-fact                 # no fact and no term held by two active units
    python instruction_units.py fixture [--plant <case>]  # the plants, each in a throwaway tree
    python instruction_units.py practices --list         # the shipped catalogue's tags, in render order
    python instruction_units.py practices --check [<path>]  # a catalogue, the shipped one by default
    python instruction_units.py practices --active [<tags>]  # the active set of a comma-joined value; none, the default

`LEVELS` is the one place an envelope, a unit row, a card or a map reads a level from: a tuple whose index is
the level, so `len(LEVELS)` is the ladder's height and `LEVELS[n]` a level's name. `PLATFORM` names the
harness's own instructions, which sit above the ladder and hold no level. `parse_level` reads a level and
raises `LevelError` on anything else. The `level` namespace's members are `level.<name>`, one per name, which
`tag_index.extract_level` reads from the tuple's literals.

LADDER-TERMS reds each line of a tracked instruction source, the closed pathspec list `LADDER_SOURCES`, that
names an instruction's place as a priority or a rank with a number, naming the path, the line and the remedy;
a pathspec list matching no tracked file is red, never green.

THE REGISTRY. Each kit's `instructions.toml` holds one `[[unit]]` table per unit. `parse_unit_rows` is
the one reader of a manifest's text, a working-tree file or a blob at any revision: a `Unit` per readable
row and a `UnitRowError` per row it cannot read. `derive_manifest_kind` names the population, `kit` for
`<prefix>/<dir>/instructions.toml` and `overlay` for `.governance/instructions.toml`; `read_units` reads
every kit manifest, `origin` the kit's descriptor `id`; `extract_unit` and `extract_repo` are the tag
index's extractors of the `unit` and `repo` namespaces, `extract_unit` also reading each change record, the
file `CHANGE_RECORD_RE` names, for the `retired` row of a tag it ended. `derive_unit_selection` picks a document's units
by selector, and `render_unit` gives the line each loads as, a derived unit's from its source.

THE STATEMENT GRAMMAR. Every loaded unit is one of `STATEMENT_TYPES`; `check_statement` grades a unit row
against its type and `check_document` a rendered document for the four shapes that load without giving
direction. GRAMMAR grades every unit row `read_units` returns, `unarmed` while the tree holds none, every
lock row whose `units` is non-empty through `check_document`, and the lock; `--doc` grades one document.

THE LOCK, `.governance/instructions.lock`, carries render provenance instead of the loaded text: one
`[[target]]` row per rendered target, `path`, `blob` (the git blob id of the rendered bytes), `units`
(`<tag>@<hash8>` each), `renderer` and `template`. `write_lock_row` is its one writer, the renderer its
caller, and `read_lock` its one reader. LOCK --CHECK reds an absent or empty lock, a row breaking those
fields, an untracked path, a blob the working tree no longer matches, and a rendered charter carrying a
version marker.

THE SCHEMA AND ONE FACT. SCHEMA grades each row's fields, naming the manifest, the tag and the field;
ONE-FACT reds two active units holding one key, a typed unit's type and pinned text or a derived unit's type
and source, and two active definitions of one term. A row carries no status: `derive_status` reads it from
the records naming the tag, and `read_change_records` is every tree read's one source of them.

THE POPULATION. `INSTRUCTION_PATHSPECS` is the instruction files, closed. `check_renderers` holds them against
`renderers.toml` both ways and `check_legacy` against `instructions-legacy.txt`; the render gate calls both.

THE PRACTICES. `read_practice_catalogue` reads `practices.toml`: its `foundation` tags and its `[[practice]]`
rows, each a tag, a line and a reach table, a row it refuses naming the row. `resolve_active_practices` turns
the value of `charter.practices` into the active rows, in catalogue order.

Exit 0 green, 1 red, 2 a usage refusal.
"""
from __future__ import annotations

import datetime
import functools
import os
import json
import pathlib
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import tomllib
from dataclasses import dataclass

sys.dont_write_bytecode = True

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

SAY = "instruction-units"

LEVELS = ("charter", "card", "loop", "methods", "runbooks", "role", "task", "records")
"""The ladder, R-G's order, the index the level:

| Level | `LEVELS[n]` | What sits there |
|---|---|---|
| 0 | `charter` | the charter |
| 1 | `card` | the build's card |
| 2 | `loop` | the loop and the policy values |
| 3 | `methods` | methods, protocols and templates, as rendered views, and reuse entries |
| 4 | `runbooks` | runbooks, Skills and path rules |
| 5 | `role` | the role's static instructions |
| 6 | `task` | the task |
| 7 | `records` | records and memory, evidence only |
"""

PLATFORM = "platform"
"""The harness's own instructions: above the ladder, holding no level."""

#: `{prefix}` is the tool root, resolved in run_ladder_terms against derive_kit_prefix (PLAY-dOrderedCharter-72)
LADDER_SOURCES = (
    "coding-governance-agents.template.md",
    "{prefix}/playbook/practices.toml",
    ":(glob){prefix}/*.template.md",
    ":(glob){prefix}/*/*.template.md",
    ":(glob){prefix}/roles/agents/*.agent.md",
    ":(glob)skills/*/SKILL.md",
    ":(glob){prefix}/workflows/*.template.js",
)
LADDER_TERM = re.compile(r"\b(priority|rank)[ -]?[0-7]\b", re.IGNORECASE)

STATEMENT_TYPES = ("directive", "constraint", "definition", "pointer", "policy-value", "fact")
"""S9's closed set (PLAY-dOrderedCharter-12): every loaded unit is one of these, and no other file types it."""
DIRECTIVE, CONSTRAINT, DEFINITION, POINTER, POLICY_VALUE, FACT = STATEMENT_TYPES

MODALS = ("MUST", "NEVER", "ALWAYS")
"""The modal a directive's text opens with."""

# ponytail: a pointer's trigger is its opening word from this closed list; a richer trigger grammar is unit 20's
TRIGGERS = ("When", "Before", "After", "If", "For", "On")
SPAN = re.compile(r"`([^`\n]+)`")
DEFINITION_RE = re.compile(r"^\S[^—]*? — \S")
VALUE_RE = re.compile(r"\d|`[^`\n]+`")
PROVENANCE = re.compile(r"rendered from|\bre-render\b|never edit the rendered", re.IGNORECASE)
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)]) ")
UNLOADED = ("the marker below", "the marker above", "the comment below", "the comment above")
NUMBERED_HEADING = re.compile(r"^#{1,6} +\d+[.)]? ")
HEADING = re.compile(r"^#{1,6} +(.*?)\s*$")
BOLD_KEY = re.compile(r"^\s*[-*] +\*\*([^*\n]+?)\*\*")

LOCK = ".governance/instructions.lock"
LOCK_FIELDS = ("path", "blob", "units", "renderer", "template")
LOCK_SHAPES = {
    "blob": re.compile(r"[0-9a-f]{40}"),
    "unit": re.compile(r"[a-z0-9][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+@[0-9a-f]{8}"),
    "renderer": re.compile(r"[a-z0-9][a-z0-9-]*@[0-9]+(?:\.[0-9]+)*"),
    "template": re.compile(r"[^\s@]+@v[0-9]+\.[0-9]+"),
}

MANIFEST = "instructions.toml"
OVERLAY = ".governance/instructions.toml"
UNIT_HEADER = "[[unit]]"
EVERY = "reader.every"
ENFORCED_NONE = "none — "
#: S1's string fields and list fields, in their row spelling; `level`, `enforced-by` and `class` read apart
UNIT_STRINGS = ("tag", "type", "trigger", "budget", "text", "source", "owner", "usage", "help")
UNIT_LISTS = ("scope", "required-by", "edges")
UNIT_KEYS = frozenset((*UNIT_STRINGS, *UNIT_LISTS, "level", "enforced-by", "class"))
#: the two keys a unit row derives and never carries: status from the change record, origin from the kit
DERIVED_UNIT_KEYS = ("origin", "status")
UNIT_REQUIRED = ("tag", "level", "type")
UNIT_CLASSES = ("fixed", "open")
BUDGET_BYTES = {"line": 200, "block": 600}
TYPED_TYPES = (DIRECTIVE, CONSTRAINT, DEFINITION, POINTER)
#: A change record's `Action` values that end a tag; every other leaves it active.
ENDING_ACTIONS = ("remove", "rename", "split")
ACTIVE = "active"
#: A change record's name under `<memory_root>/builds/*/build/`, and its one field shape, the factory's bullet.
CHANGE_RECORD_RE = re.compile(r"(?:^|/)builds/[^/]+/build/\d{4}-\d{2}-\d{2}-build-[A-Za-z]+-[A-Za-z0-9]+-\d+-change-\d+\.md$")
CHANGE_FIELD_RE = re.compile(r"^- \*\*([A-Z][a-z-]+(?: [a-z]+)?):\*\* (.+)$")

INSTRUCTION_PATHSPECS = (
    "{charter}",
    "CLAUDE.md",
    ".claude/agents/*.md",
    ".claude/rules/*.md",
    ".claude/skills/*/SKILL.md",
    "skills/*/SKILL.md",
    "{memory_root}/guides/*.md",
    "{memory_root}/TEMPLATE-SPEC.md",
    "{memory_root}/HYGIENE.md",
)
"""Every instruction file, closed; `{charter}` the conf's CHARTER and `{memory_root}` its MEMORY_ROOT."""
RENDERERS_TABLE = "renderers.toml"
LEGACY_LIST = "instructions-legacy.txt"
#: the closed set of commands a `cmd:` source may run (PLAY-dOrderedCharter-70 S1); a target's manifest cannot widen it
REGISTERED_COMMANDS = ("git rev-parse --abbrev-ref HEAD",)
#: seconds a registered command may run before its render is refused
CMD_TIMEOUT_S = 30
RENDERERS = ("playbook:charter", "playbook:entry-files", "kit-adopter", "hand")


class LockError(ValueError):
    """A lock that cannot be read."""


class LevelError(ValueError):
    """A value that is no level of the ladder."""


def parse_level(value) -> int:
    """`0` to `7`, an integer or a one-digit string, as the level; anything else, a boolean and the platform
    included, raises LevelError naming the value and the range."""
    if isinstance(value, int) and not isinstance(value, bool) and 0 <= value < len(LEVELS):
        return value
    if isinstance(value, str) and len(value) == 1 and "0" <= value <= str(len(LEVELS) - 1):
        return int(value)
    where = " sits above the ladder and" if value == PLATFORM else ""
    raise LevelError(f"level {value!r}{where} is no level: a level is 0 to {len(LEVELS) - 1}")


def run_git(root, *args) -> str:
    done = subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    if done.returncode:
        raise LevelError(f"git {' '.join(args[:2])} failed: {done.stderr.decode('utf-8', 'replace').strip()}")
    return done.stdout.decode("utf-8", "replace")


class UnitRowError(ValueError):
    """A unit row the reader cannot read, naming its manifest and its row; `read_units` raises one naming
    every fault of the tree, and a refused render raises one naming the unit and its source."""


@dataclass(frozen=True)
class Unit:
    """One `[[unit]]` row as S1 reads it: `origin` the kit's descriptor `id`, never a row field; `line` its
    header's line and `body` its text from that header to the next table header."""
    tag: str | None
    level: int | None
    type: str | None
    scope: tuple
    trigger: str | None
    budget: str | None
    text: str | None
    source: str | None
    origin: str | None
    owner: str | None
    usage: str | None
    help: str | None
    required_by: tuple
    enforced_by: tuple | str
    klass: str
    edges: tuple
    path: str
    index: int
    line: int
    body: str


@functools.lru_cache(maxsize=None)
def derive_kit_prefix() -> str:
    """The parent of this module's own kit directory inside its repository: `tools` in gov, empty at the top."""
    here = pathlib.PurePosixPath(run_git(KIT_DIR, "rev-parse", "--show-prefix").strip().rstrip("/"))
    return here.parent.as_posix().strip(".")


def derive_manifest_kind(path, prefix) -> str | None:
    """S2's one population predicate: `kit` for `<prefix>/<dir>/instructions.toml`, `overlay` for
    `.governance/instructions.toml`, else None."""
    if path == OVERLAY:
        return "overlay"
    head, parts = [s for s in str(prefix).split("/") if s not in ("", ".")], str(path).split("/")
    return "kit" if parts[-1] == MANIFEST and len(parts) == len(head) + 2 and parts[:len(head)] == head else None


def parse_unit_rows(text, path, origin=None) -> tuple[list, list]:
    """S2's text entry, the one parser of a manifest: `(units, faults)` of one manifest's text, a `Unit` per
    readable `[[unit]]` table in row order and a `UnitRowError` per row it cannot read, naming the file and
    the row's index or tag. Field rules beyond a field's TOML type are the schema check's."""
    heads, n, faults = [], 1, []
    for chunk in re.split(r"(?m)^(?=\[)", text):
        if chunk.startswith(UNIT_HEADER):
            heads.append((n, chunk))
        n += chunk.count("\n")

    def add_fault(i, tag, why):
        name = f" ({tag})" if isinstance(tag, str) and tag else ""
        at = f" at line {heads[i - 1][0]}" if 0 < i <= len(heads) else ""
        faults.append(UnitRowError(f"{path}: unit row {i}{name}{at} · {why}"))

    try:
        rows = tomllib.loads(text).get("unit")
    except tomllib.TOMLDecodeError as exc:
        for i in range(1, max(len(heads), 1) + 1):
            add_fault(i, None, f"the manifest is no TOML: {exc}")
        return [], faults
    rows = [] if rows is None else rows
    if not isinstance(rows, list):
        add_fault(1, None, "`unit` is no array of [[unit]] tables")
        return [], faults
    units = []
    for i, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            add_fault(i, None, "the row is no table")
            continue
        tag = row.get("tag")
        if len(rows) != len(heads):
            add_fault(i, tag, "the row sits under no [[unit]] header")
            continue
        bad, vals = [], {}
        for key in UNIT_STRINGS:
            vals[key] = row.get(key)
            if vals[key] is not None and not isinstance(vals[key], str):
                bad.append(f"`{key}` is no string")
        for key in UNIT_LISTS:
            v = row.get(key, [])
            vals[key] = tuple(v) if isinstance(v, list) else ()
            if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                bad.append(f"`{key}` is no list of strings")
        level = row.get("level")
        if level is not None:
            try:
                level = parse_level(level)
            except LevelError as exc:
                bad.append(f"`level` · {exc}")
        enforced = row.get("enforced-by", [])
        if isinstance(enforced, list) and all(isinstance(x, str) for x in enforced):
            enforced = tuple(enforced)
        elif not (isinstance(enforced, str) and enforced.startswith(ENFORCED_NONE)
                  and enforced[len(ENFORCED_NONE):].strip()):
            bad.append("`enforced-by` is no list of descriptions and no `none — <why>`")
        klass = row.get("class", "fixed")
        if not isinstance(klass, str):
            bad.append("`class` is no string")
        if bad:
            add_fault(i, tag, "; ".join(bad))
            continue
        line, body = heads[i - 1]
        units.append(Unit(tag=vals["tag"], level=level, type=vals["type"], scope=vals["scope"],
                          trigger=vals["trigger"], budget=vals["budget"], text=vals["text"],
                          source=vals["source"], origin=origin, owner=vals["owner"], usage=vals["usage"],
                          help=vals["help"], required_by=vals["required-by"], enforced_by=enforced,
                          klass=klass, edges=vals["edges"], path=path, index=i, line=line, body=body))
    return units, faults


def read_unit_rows(root) -> tuple[list, list]:
    """`(units, faults)` of every `kit` manifest git tracks under `root`, in path then row order, each
    `origin` its kit's descriptor `id`; `read_units` raises what this returns."""
    root, prefix = pathlib.Path(root), derive_kit_prefix()
    paths = sorted(p for p in run_git(root, "ls-files", "-z", "--", f"*{MANIFEST}").split("\0")
                   if p and derive_manifest_kind(p, prefix) == "kit")
    units, faults = [], []
    for rel in paths:
        try:
            kit = tomllib.loads((root / rel).parent.joinpath("kit.toml").read_text(encoding="utf-8")).get("id")
        except (OSError, tomllib.TOMLDecodeError):
            kit = None
        try:
            text = (root / rel).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            faults.append(UnitRowError(f"{rel}: the manifest is unreadable: {exc}"))
            continue
        got, bad = parse_unit_rows(text, rel, kit if isinstance(kit, str) else None)
        units += got
        faults += bad
    return units, faults


def read_units(root) -> list:
    """S2's tree entry: `read_unit_rows`' Units. Raises one UnitRowError naming every fault."""
    units, faults = read_unit_rows(root)
    if faults:
        raise UnitRowError("\n".join(str(f) for f in faults))
    return units


def read_change_fields(text) -> dict:
    """A change record's `- **<Field>:** <value>` bullets, a field given twice its first: the playbook side's read
    of the fields `build_records.py read` prints."""
    fields = {}
    for line in text.splitlines():
        m = CHANGE_FIELD_RE.match(line)
        if m:
            fields.setdefault(m.group(1), m.group(2).strip())
    return fields


def derive_retired_rows(text) -> list:
    """The `retired` row of a change record whose `Action` ends a tag: the record's `Unit`, at its `Unit` line, its
    text the `Successor` line with its bullet cut, where `show` reads the redirect back. A malformed record's
    fault is the status read's to red."""
    fields = read_change_fields(text)
    if fields.get("Action") not in ENDING_ACTIONS or not fields.get("Unit"):
        return []
    n = next(i for i, ln in enumerate(text.splitlines(), 1) if ln.startswith("- **Unit:**"))
    return [(fields["Unit"], "retired", n, n, f"**Successor:** {fields.get('Successor', 'none')}")]


def extract_unit(ctx, path, text=None):
    """The `unit` namespace: each readable row's `tag` of every kit manifest, and each `scope` value as a
    `selector` row; the overlay's rows are the `repo` namespace's. `text` is a blob at any revision, read
    through `parse_unit_rows`; a row's fault is the schema and edge checks' to red, never the index's. A
    change record under the memory root gives its `retired` row, `derive_retired_rows`."""
    record = str(path).startswith(ctx.get("memory_root", "memory") + "/") and CHANGE_RECORD_RE.search(path)
    if text is None:
        return "" if record or derive_manifest_kind(path, derive_kit_prefix()) == "kit" else None
    if record:
        return derive_retired_rows(text)
    lines, rows = text.splitlines(), []
    for u in parse_unit_rows(text, path)[0]:
        span = lines[u.line - 1:u.line - 1 + u.body.count("\n") + 1]
        for val, kind in [(u.tag, "tag")] * bool(u.tag) + [(v, "selector") for v in u.scope if v]:
            n = u.line + next((i for i, ln in enumerate(span) if f'"{val}"' in ln), 0)
            rows.append((val, kind, n, n, lines[n - 1] if lines else ""))
    return rows


def extract_repo(ctx, path, text=None):
    """The `repo` namespace: the units of `.governance/instructions.toml`, the repository's own (S14)."""
    if text is None:
        return "" if derive_manifest_kind(path, derive_kit_prefix()) == "overlay" else None
    return extract_unit(ctx, path, text)


def derive_unit_selection(units, selector) -> list:
    """S4: the units a document holds, those whose `scope` holds `selector` or `reader.every`, ordered by
    level, then manifest path, then row order."""
    wanted = {selector, EVERY}
    return sorted((u for u in units if wanted & set(u.scope)),
                  key=lambda u: (len(LEVELS) if u.level is None else u.level, u.path, u.index))


def render_unit(unit, policy_reader, root=None) -> str:
    """S4: the line a unit loads as: its `text` when typed; a `policy:<key>` source's value lines through
    `policy_reader(key)`, one member per line; a `cmd:<command>` source's one line of output, never typed
    text, the command one of REGISTERED_COMMANDS run in `root` with the caller's git variables aside. A
    refused read refuses the render, a UnitRowError naming the unit, the key and the reader's line."""
    from policy_value import PolicyRefused
    if unit.type not in (POLICY_VALUE, FACT):
        return unit.text or ""
    kind, _, arg = (unit.source or "").partition(":")
    where = f"{unit.path}: unit {unit.tag}"
    if kind == "policy":
        try:
            return "\n".join(policy_reader(arg)[0])
        except PolicyRefused as exc:
            raise UnitRowError(f"{where} · the render is refused: policy {exc.key}: {exc.line}") from None
    if kind == "cmd":
        if arg not in REGISTERED_COMMANDS:
            raise UnitRowError(f"{where} · the render is refused: `{arg}` is no registered command, one of "
                               f"{REGISTERED_COMMANDS}")
        load_memory_tree_path()
        from tree_lib import GIT_ENV_LEAKS
        try:
            done = subprocess.run(shlex.split(arg), capture_output=True, text=True, encoding="utf-8", errors="replace",
                                  stdin=subprocess.DEVNULL, cwd=root, timeout=CMD_TIMEOUT_S,
                                  env={k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS})
        except (OSError, ValueError, subprocess.TimeoutExpired) as exc:
            raise UnitRowError(f"{where} · the render is refused: `{arg}` did not run: {exc}") from None
        if done.returncode:
            raise UnitRowError(f"{where} · the render is refused: `{arg}` exited {done.returncode}")
        out = done.stdout.strip()
        if "\n" in out:
            raise UnitRowError(f"{where} · the render is refused: `{arg}` printed more than one line")
        return out
    # ponytail: no probe registry exists, so a `probe:<name>` source refuses; its runner lands with the registry
    raise UnitRowError(f"{where} · the render is refused: source {unit.source!r} names no policy key and "
                       f"no command")


def render_units(units, policy_reader, root=None) -> str:
    """S4: the units' rendered lines joined, one line per unit."""
    return "\n".join(render_unit(u, policy_reader, root) for u in units)


def read_practice_catalogue(path) -> dict:
    """S3: the catalogue at `path`, as TOML reads it: `foundation`, its default tags, and `practice`, its rows
    in render order. Raises one UnitRowError naming each row refused: a tag outside `practice.<seg>`, a tag
    twice, an empty `line`, no reach, a reach key outside the `seg` shape, a `foundation` entry naming no row.
    A line's length is the render's to grade."""
    import tag_index
    try:
        table = tomllib.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:     # ValueError: a TOML or a UTF-8 fault
        raise UnitRowError(f"{path}: the practice catalogue is unreadable: {exc}") from None
    rows, foundation = table.get("practice"), table.get("foundation", [])
    if not rows or not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
        raise UnitRowError(f"{path}: the practice catalogue holds no [[practice]] row")
    faults, seen = [], set()
    for i, row in enumerate(rows, 1):
        tag = str(row.get("tag"))
        where = f"{path}: practice row {i} ({tag})"
        name = tag.partition("practice.")[2]
        if not tag.startswith("practice.") or not tag_index.SEG_RE.fullmatch(name):
            faults.append(f"{where} · its tag is outside practice.<name>, a name of [a-z0-9][a-z0-9-]*")
        if tag in seen:
            faults.append(f"{where} · its tag is held by an earlier row")
        seen.add(tag)
        if not str(row.get("line") or "").strip():
            faults.append(f"{where} · its `line` is empty")
        reach = row.get("reach")
        if not reach or not isinstance(reach, dict):
            faults.append(f"{where} · it carries no reach.<step> key")
            continue
        faults += [f"{where} · reach key `{step}` is outside [a-z0-9][a-z0-9-]*" for step in reach
                   if not tag_index.SEG_RE.fullmatch(step)]
    faults += [f"{path}: `foundation` names {tag}, which no row holds" for tag in foundation if tag not in seen]
    if faults:
        raise UnitRowError("\n".join(faults))
    return {"foundation": foundation, "practice": rows}


def resolve_active_practices(catalogue, value) -> list:
    """S4: the active rows in catalogue order, `value` the set `charter.practices` holds or None for the
    `foundation` set. An empty set and a tag in no row raise UnitRowError naming it."""
    rows = catalogue["practice"]
    if value is None:
        value = catalogue["foundation"]
    elif not value:
        raise UnitRowError("charter.practices is the empty set: name a practice, or leave the key unset")
    unknown = sorted(set(value) - {r["tag"] for r in rows})
    if unknown:
        raise UnitRowError(f"charter.practices names {', '.join(unknown)}, which no practice row holds")
    return [r for r in rows if r["tag"] in value]


def run_practices(args) -> tuple[list, int]:
    """The `practices` verbs: `--list`, `--check [<path>]` and `--active [<tags>]`, a comma-joined value, an
    empty one the empty set."""
    shipped = KIT_DIR / "practices.toml"
    if args == ["--list"]:
        return [r["tag"] for r in read_practice_catalogue(shipped)["practice"]], 0
    if args[:1] == ["--check"] and len(args) <= 2:
        path = args[1] if len(args) == 2 else shipped
        rows = read_practice_catalogue(path)["practice"]
        return [f"{SAY}: practices · {path} · {len(rows)} row(s) · green"], 0
    if args[:1] == ["--active"] and len(args) <= 2:
        value = [t for t in args[1].split(",") if t] if len(args) == 2 else None
        return [r["tag"] for r in resolve_active_practices(read_practice_catalogue(shipped), value)], 0
    return [__doc__.split("\n\n")[1]], 2


def run_ladder_terms(root=".") -> tuple[list, int]:
    """S4: every tracked LADDER_SOURCES line naming a ladder place as a priority or a rank, red."""
    from tag_index import resolve_prefix_token
    specs = [resolve_prefix_token(s, derive_kit_prefix()) for s in LADDER_SOURCES]
    paths = [p for p in run_git(root, "ls-files", "-z", "--", *specs).split("\0") if p]
    if not paths:
        return [f"{SAY}: red · ladder-terms · LADDER_SOURCES matches no tracked file"], 1
    reds = []
    for rel in paths:
        text = (pathlib.Path(root) / rel).read_text(encoding="utf-8", errors="replace")
        for n, line in enumerate(text.splitlines(), 1):
            for m in LADDER_TERM.finditer(line):
                reds.append(f"{SAY}: red · {rel} line {n} · '{m.group(0)}' names a ladder place by "
                            f"{m.group(1).lower()} · remedy: name it 'level'")
    tail = f"{SAY}: ladder-terms · {len(paths)} source(s) · {len(reds)} red"
    return reds + [tail], 1 if reds else 0


def check_level_tags(text) -> list:
    """S3: `extract_level` over a module's text names `level.<name>` for each of LEVELS, in order, each a tag."""
    import tag_index
    rows = tag_index.extract_level({}, "instruction_units.py", text)
    tags = [r[0] for r in rows]
    want = [f"level.{name}" for name in LEVELS]
    reds = [f"tag {t} breaks the tag shape" for t in tags
            if not tag_index.TAG_RE.fullmatch(t) or not all(tag_index.SEG_RE.fullmatch(s) for s in t.split("."))]
    if tags != want:
        reds.append(f"extract_level names {tags}, not {want}")
    return reds


RESOLVERS = {}


def load_resolver(root=None):
    """Unit 19's resolver over `root`, the repository holding this module by default: a tag to its
    definition rows, each `{tag, path, line, end_line, kind, text}`. One index view per root."""
    import tag_index as ti
    root = pathlib.Path(root or run_git(KIT_DIR, "rev-parse", "--show-toplevel").strip())
    if root not in RESOLVERS:
        ctx = ti.derive_context(root, KIT_DIR / "namespaces.toml")
        con = ti.load_index(root)
        ti.load_view(con, root, ctx)
        aliases = ti.read_aliases(KIT_DIR / "aliases.toml")
        RESOLVERS[root] = lambda tag: ti.resolve_address(con, tag, "leaf", aliases)
    return RESOLVERS[root]


def check_pointer_target(text, resolve) -> tuple[str, str] | None:
    """A pointer's target, its first code span: a tag resolving to a unit or a slice, or a command.
    `(rule, remedy)` when it is neither, a whole document included; None when it holds."""
    import tag_index
    spans = SPAN.findall(text)
    if not spans:
        return "names no target", "name a unit or slice tag, or a command, in a code span"
    target = spans[0]
    if tag_index.SPAN_RE.fullmatch(target) and "." in target:
        rows = (resolve or load_resolver())(target)
        if not rows:
            return f"`{target}` resolves to no unit or slice", "point at a tag the resolver resolves"
        if all(r["kind"] == "doc" for r in rows):
            return f"`{target}` is a whole document", "point at the unit or the section that answers"
        return None
    if re.search(r"\s", target):
        return None
    return (f"`{target}` is no tag and no command",
            "point at a unit or slice tag, or a command; a file is a whole document")


def check_statement(row, resolve=None) -> list[str]:
    """S2: one unit row, in unit 9's field names, graded against its `type`. Each red names the tag, the
    rule and the remedy. `resolve`, a tag to its rows, is the repository's own resolver when omitted."""
    tag = row.get("tag") or "<no tag>"
    kind, text = row.get("type"), (row.get("text") or "").strip()
    found = []

    def add_red(rule, remedy):
        found.append(f"{SAY}: red · {tag} · {rule} · remedy: {remedy}")

    if kind not in STATEMENT_TYPES:
        add_red(f"type {kind!r} is no statement type", f"type it one of {', '.join(STATEMENT_TYPES)}")
        return found
    if kind in (POLICY_VALUE, FACT):
        source = row.get("source") or ""
        if text:
            add_red(f"a {kind} carries typed text {text!r}", "drop the text: its value comes from its source")
        if kind == POLICY_VALUE and not re.fullmatch(r"policy:\S+", source):
            add_red(f"a {kind} carries source {source!r}", "source it as policy:<key>")
        if kind == FACT and not source:
            add_red(f"a {kind} carries no source", "source it from a policy, probe or command, or delete it")
        if kind == FACT and source.startswith("cmd:") and source[4:] not in REGISTERED_COMMANDS:
            add_red(f"source {source!r} names no registered command",
                    f"source it as cmd:<one of {REGISTERED_COMMANDS}>, or from a policy")
        return found
    if not text:
        add_red(f"a {kind} carries no text", f"type the {kind}'s one line")
    elif kind == DIRECTIVE:
        if not re.match(rf"(?:{'|'.join(MODALS)})\b", text):
            add_red("a directive opens with no modal", f"open it with one of {', '.join(MODALS)}")
        if not row.get("trigger"):
            add_red("a directive carries no trigger", "state its condition in `trigger`")
    elif kind == CONSTRAINT:
        if not VALUE_RE.search(text):
            add_red("a constraint carries no value", "state the value it bounds")
        if not row.get("enforced-by"):
            add_red("a constraint names no enforcer", "name what refuses a bypass in `enforced-by`")
    elif kind == DEFINITION:
        if not DEFINITION_RE.match(text):
            add_red("a definition holds no `<term> — <meaning>`", "write the term, an em dash, and its meaning")
    elif kind == POINTER:
        if text.split(" ", 1)[0].rstrip(",") not in TRIGGERS:
            add_red("a pointer names no trigger", f"open it with one of {', '.join(TRIGGERS)}")
        fault = check_pointer_target(text, resolve)
        if fault:
            add_red(*fault)
    return found


def check_document(text, units=()) -> list[str]:
    """S3: a rendered document's lines graded for R-D's four shapes, outside code fences: a provenance
    paragraph or version marker, a numbered heading, a pointer to text never loaded, and a bold-key bullet
    under `Facts` no `units` entry (`<tag>@<hash8>`) attributes. Each red names the line, shape and remedy."""
    from tag_index import scan_unfenced
    from render_playbook import TEMPLATE_MARKER_RE
    found, para, section = [], [], None
    pins = {u.rsplit("@", 1)[-1] for u in units}

    def check_paragraph():
        if para and PROVENANCE.search(" ".join(ln for _n, ln in para)):
            found.append(f"{SAY}: red · lines {para[0][0]} to {para[-1][0]} · a provenance paragraph · "
                         f"remedy: render provenance lives in {LOCK}, never in loaded text")
        para.clear()

    last = 0
    for n, line in scan_unfenced(text):
        if not line.strip() or n != last + 1 or LIST_ITEM.match(line):
            check_paragraph()
        if line.strip():
            para.append((n, line))
        last = n
        if TEMPLATE_MARKER_RE.search(line):
            found.append(f"{SAY}: red · line {n} · a template version marker · remedy: the lock's `template` "
                         f"carries it")
        heading = HEADING.match(line)
        if heading:
            section = heading.group(1)
            if NUMBERED_HEADING.match(line):
                found.append(f"{SAY}: red · line {n} · the heading `{line.strip()}` names a number · "
                             f"remedy: name the heading, never number it")
        for phrase in UNLOADED:
            if phrase in line.lower():
                found.append(f"{SAY}: red · line {n} · `{phrase}` points at text never loaded · remedy: "
                             f"say the thing itself, or point at a tag")
        bullet = BOLD_KEY.match(line)
        if bullet and section == "Facts" and not (pins and derive_unit_pin(line.strip()) in pins):
            found.append(f"{SAY}: red · line {n} · the fact `**{bullet.group(1)}**` is typed · remedy: "
                         f"render it from a `fact` unit with a `source`")
    check_paragraph()
    return found


def load_memory_tree_path():
    """The memory-tree kit beside this one, put on `sys.path`, since a kit imports no sibling by name."""
    from policy_value import resolve_kit_dir
    mt = str(resolve_kit_dir("memory-tree", "design_lib.py", KIT_DIR))
    if mt not in sys.path:
        sys.path.append(mt)


def derive_unit_pin(text) -> str:
    """Unit 24's `derive_pin_hash` of `text`, read from the memory-tree kit beside this one."""
    load_memory_tree_path()
    import design_lib
    return design_lib.derive_pin_hash(text)


def read_change_records(root) -> list:
    """Every tree read's change records, `build_records.read_changes`' mappings, the ones `derive_status`
    reads, oldest first. Raises one UnitRowError naming each malformed record."""
    load_memory_tree_path()
    import build_records
    records = build_records.read_changes(root)
    bad = [f"{r['path']}: {key} {why}" for r in records for key, why in r["malformed"]]
    if bad:
        raise UnitRowError("\n".join(bad))
    return records


def derive_status(tag, records) -> str:
    """`active`, or `retired:<successors>` from the last record naming `tag`, `retired:none` for a removal;
    each record a mapping of the change record's `Unit`, `Action` and `Successor`."""
    last = next((r for r in reversed(list(records)) if r.get("Unit") == tag), None)
    if last is None or last.get("Action") not in ENDING_ACTIONS:
        return ACTIVE
    heirs = [s.strip() for s in str(last.get("Successor") or "none").split(",") if s.strip()]
    return "retired:" + ",".join(heirs or ["none"])


@functools.lru_cache(maxsize=None)
def read_namespace_words() -> frozenset:
    """The words the registry beside this module registers."""
    import tag_index
    return frozenset(r["ns"] for r in tag_index.read_namespaces(KIT_DIR / "namespaces.toml"))


def check_tag_entry(value) -> str | None:
    """Why `value` is no tag of a registered namespace, or None when it is one."""
    import tag_index
    if not tag_index.TAG_RE.fullmatch(value):
        return "breaks the tag grammar"
    word = value.split(".", 1)[0]
    return None if word in read_namespace_words() else f"opens with `{word}`, which no namespace registers"


def check_unit_row(unit, row, ns="unit") -> list[str]:
    """S1: one row's fields, `row` the table as TOML reads it; each red names the manifest, the tag and the
    field. A row with no `budget` is held to `line`, the smaller; `ns` is its manifest's namespace."""
    found = []

    def add_red(field, why, remedy):
        found.append(f"{SAY}: red · {unit.path} · {unit.tag or f'row {unit.index}'} · `{field}` {why} · remedy: {remedy}")

    for key in UNIT_REQUIRED:
        if row.get(key) is None:
            add_red(key, "is missing", f"give the row its `{key}`")
    for key in sorted(set(row) - UNIT_KEYS):
        add_red(key, "is no field of a unit row", "delete it: status derives from the change record, origin "
                                                  "from the kit" if key in DERIVED_UNIT_KEYS else "delete it")
    if unit.tag is not None:
        import tag_index
        if not unit.tag.startswith(f"{ns}.") or not tag_index.TAG_RE.fullmatch(unit.tag):
            add_red("tag", f"{unit.tag!r} is no tag of the `{ns}` namespace", f"spell it {ns}.<name>")
    if unit.type is not None and unit.type not in STATEMENT_TYPES:
        add_red("type", f"{unit.type!r} is no statement type", f"type it one of {', '.join(STATEMENT_TYPES)}")
    if unit.budget is not None and unit.budget not in BUDGET_BYTES:
        add_red("budget", f"{unit.budget!r} is no budget class", f"use one of {', '.join(BUDGET_BYTES)}")
    limit = BUDGET_BYTES.get(unit.budget or "line")
    if limit is not None and len((unit.text or "").encode("utf-8")) > limit:
        add_red("text", f"is over its budget's {limit} bytes", "shorten it, or point at what holds the rest")
    if unit.type in TYPED_TYPES and not unit.text:
        add_red("text", f"a {unit.type} carries no text", f"type the {unit.type}'s line")
    if unit.type in (POLICY_VALUE, FACT) and not unit.source:
        add_red("source", f"a {unit.type} carries no source", "source it from a policy key or a command")
    if unit.klass not in UNIT_CLASSES:
        add_red("class", f"{unit.klass!r} is no class", f"use one of {', '.join(UNIT_CLASSES)}")
    for key, values in (("scope", unit.scope), ("required-by", unit.required_by)):
        for value in values:
            fault = check_tag_entry(value)
            if fault:
                add_red(key, f"entry {value!r} {fault}", "name a tag of a registered namespace")
    if isinstance(unit.enforced_by, tuple) and not all(d.strip() for d in unit.enforced_by):
        add_red("enforced-by", "holds an empty description", f"describe the enforcer, or write `{ENFORCED_NONE}<why>`")
    return found


def run_schema(root=".") -> tuple[list, int]:
    """S1 over every row `read_units` reads, `unarmed` with none; a row the reader cannot read reds as its
    fault names it."""
    root = pathlib.Path(root)
    units, faults = read_unit_rows(root)
    reds = [f"{SAY}: red · {f}" for f in faults]
    tables = {}
    for u in units:
        if u.path not in tables:
            tables[u.path] = tomllib.loads((root / u.path).read_text(encoding="utf-8"))["unit"]
        reds += check_unit_row(u, tables[u.path][u.index - 1])
    if not units and not reds:
        return [f"{SAY}: schema · unarmed: the tree holds no unit row (PLAY-dOrderedCharter-40 writes the first)"], 0
    return reds + [f"{SAY}: schema · {len(units)} row(s) · {len(reds)} red"], 1 if reds else 0


def check_one_fact(units, records) -> list[str]:
    """S2: two active units holding one key, and two active definitions of one term, each red."""
    held = {}
    for u in units:
        if derive_status(u.tag, records) != ACTIVE:
            continue
        if u.type in TYPED_TYPES and u.text:
            held.setdefault(("the fact", u.type, derive_unit_pin(u.text)), []).append(u)
        elif u.type in (POLICY_VALUE, FACT) and u.source:
            held.setdefault(("the fact", u.type, u.source), []).append(u)
        if u.type == DEFINITION and u.text:
            held.setdefault(("the term", DEFINITION, u.text.split(" — ", 1)[0].strip()), []).append(u)
    return [f"{SAY}: red · {what} {key!r} ({kind}) is held by {', '.join(f'{u.tag} in {u.path}' for u in us)} · "
            f"remedy: keep one unit and point at it"
            for (what, kind, key), us in held.items() if len(us) > 1]


def run_one_fact(root=".") -> tuple[list, int]:
    """S2 over the tree: every row `read_units` reads, statuses from `read_change_records`."""
    root = pathlib.Path(root)
    units, records = read_units(root), read_change_records(root)
    if not units:
        return [f"{SAY}: one-fact · unarmed: the tree holds no unit row"], 0
    reds = check_one_fact(units, records)
    return reds + [f"{SAY}: one-fact · {len(units)} row(s) · {len(reds)} red"], 1 if reds else 0


def derive_kit_file(root, name) -> pathlib.Path:
    """`name` of this kit in the tree under check, the tree's own table rather than this module's."""
    return pathlib.Path(root) / derive_kit_prefix() / KIT_DIR.name / name


def derive_instruction_tokens(root) -> dict:
    """The two tokens of `INSTRUCTION_PATHSPECS` and `renderers.toml`, read from the tree's conf."""
    from render_playbook import derive_memory_root, read_conf
    root = pathlib.Path(root)
    return {"charter": read_conf(root, ".memory-tree.conf", "CHARTER") or "AGENTS.md",
            "memory_root": derive_memory_root(root, {})}


def derive_instruction_files(root) -> list:
    """S4: the tracked files `INSTRUCTION_PATHSPECS` names, sorted."""
    tokens = derive_instruction_tokens(root)
    specs = [":(glob)" + p.format(**tokens) for p in INSTRUCTION_PATHSPECS]
    return sorted(p for p in run_git(root, "ls-files", "-z", "--", *specs).split("\0") if p)


def read_renderers(root) -> list[dict]:
    """`renderers.toml`'s `[[target]]` rows, their tokens filled; raises UnitRowError on one it cannot read."""
    path = derive_kit_file(root, RENDERERS_TABLE)
    try:
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("target") or []
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise UnitRowError(f"{path.as_posix()} is unreadable: {exc}") from None
    tokens = derive_instruction_tokens(root)
    for i, row in enumerate(rows, 1):
        paths, renderer = row.get("paths"), row.get("renderer")
        if not isinstance(paths, list) or not paths or not isinstance(renderer, str):
            raise UnitRowError(f"{path.as_posix()}: target row {i} carries no `paths` list and `renderer`")
    return [{"paths": [p.format(**tokens) for p in r["paths"]], "renderer": r["renderer"]} for r in rows]


def check_path_match(path, pattern) -> bool:
    """A table glob against a tracked path, `*` holding within one segment as the pathspec's does."""
    return pathlib.PurePosixPath(path).full_match(pattern)


def check_renderers(root) -> list[str]:
    """S4, both ways: each instruction file claimed by exactly one row, each row's path claiming a file, and
    each renderer one the table knows. An empty population is red, never green."""
    say = "render-playbook: red · renderers"
    rows, files = read_renderers(root), derive_instruction_files(root)
    reds = [] if files else [f"{say} · INSTRUCTION_PATHSPECS matches no tracked file"]
    for row in rows:
        if row["renderer"] not in RENDERERS:
            reds.append(f"{say} · {row['renderer']!r} is no renderer · remedy: use one of {', '.join(RENDERERS)}")
        for pattern in row["paths"]:
            if not any(check_path_match(f, pattern) for f in files):
                reds.append(f"{say} · {pattern} claims no instruction file · remedy: drop the path from "
                            f"{RENDERERS_TABLE}")
    for path in files:
        owners = [r["renderer"] for r in rows if any(check_path_match(path, p) for p in r["paths"])]
        if not owners:
            reds.append(f"{say} · {path} has no renderer of record · remedy: claim it in {RENDERERS_TABLE}")
        elif len(owners) > 1:
            reds.append(f"{say} · {path} has {len(owners)} renderers of record, {', '.join(owners)} · remedy: leave "
                        f"it on one row of {RENDERERS_TABLE}")
    return reds


def read_legacy(root) -> list:
    """`instructions-legacy.txt`'s paths; absent, none."""
    path = derive_kit_file(root, LEGACY_LIST)
    if not path.is_file():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    return [ln.strip() for ln in lines if ln.strip() and not ln.startswith("#")]


def check_legacy(root, value) -> list[str]:
    """S8 under `instructions.legacy`: an instruction file neither rendered from units nor listed is red under
    either value and a listed path no instruction file holds is stale; `shrink-only` reds a listed file now
    rendered from units as stale, and `refuse` reds every listed file."""
    say = "render-playbook: red · legacy"
    listed, files = read_legacy(root), set(derive_instruction_files(root))
    rendered = {r.get("path") for r in read_lock(root) if r.get("units")}
    reds = [f"{say} · {f} is neither rendered from units nor on {LEGACY_LIST} · remedy: render it from units"
            for f in sorted(files - rendered - set(listed))]
    for path in listed:
        if path not in files:
            reds.append(f"{say} · {path} is stale: it is no instruction file · remedy: drop it from {LEGACY_LIST}")
        elif value == "refuse":
            reds.append(f"{say} · {path} is listed and instructions.legacy is refuse · remedy: render it from units")
        elif path in rendered:
            reds.append(f"{say} · {path} is stale: its lock row lists units · remedy: drop it from {LEGACY_LIST}")
    return reds


def read_lock(root=".") -> list[dict]:
    """S4's one reader: the lock's `[[target]]` rows, `[]` for an absent lock. Raises LockError on a lock
    that does not parse and on a `target` entry that is no table, naming the entry."""
    path = pathlib.Path(root) / LOCK
    if not path.is_file():
        return []
    try:
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("target") or []
    except tomllib.TOMLDecodeError as exc:
        raise LockError(f"{LOCK} does not parse: {exc}") from None
    if not isinstance(rows, list):
        raise LockError(f"{LOCK}: `target` is {rows!r}, no array of [[target]] tables")
    for i, r in enumerate(rows, 1):
        if not isinstance(r, dict):
            raise LockError(f"{LOCK}: target entry {i}, {r!r}, is no table")
    return rows


def write_lock_row(root, path, renderer, template, units=()) -> dict:
    """S4's one writer: `path`'s row, `blob` the git blob id of the bytes on disk and `units` each
    `(tag, text)` pinned `<tag>@<hash8>`, written beside the other rows, sorted by path, the lock whole."""
    row = {"path": path, "blob": run_git(root, "hash-object", "--", path).strip(),
           "units": [f"{tag}@{derive_unit_pin(text)}" for tag, text in units],
           "renderer": renderer, "template": template}
    rows = sorted([r for r in read_lock(root) if r.get("path") != path] + [row], key=lambda r: r["path"])
    out = ["# instructions.lock — render provenance, one row per rendered target. Written by the renderer\n"
           "# through instruction_units.write_lock_row; never by hand.\n"]
    for r in rows:
        out.append("\n[[target]]\n" + "".join(
            f"{k} = {json.dumps(r.get(k), ensure_ascii=False)}\n" for k in LOCK_FIELDS))
    lock = pathlib.Path(root) / LOCK
    lock.parent.mkdir(parents=True, exist_ok=True)
    lock.write_text("".join(out), encoding="utf-8", newline="\n")
    return row


def check_lock(root=".") -> tuple[list, int]:
    """S6: red a lock that is absent or empty, a row breaking S4's fields, a path git does not track, a
    `blob` differing from the working tree's bytes, and a rendered charter carrying a version marker."""
    from render_playbook import TEMPLATE_MARKER_RE
    root = pathlib.Path(root)
    rows = read_lock(root)
    if not rows:
        return [f"{SAY}: red · {LOCK} holds no row · remedy: render the charter, which writes it"], 1
    tracked = set(run_git(root, "ls-files", "-z").split("\0"))
    found = []
    for r in rows:
        path = r.get("path")
        bad = [k for k in LOCK_FIELDS if k not in r] + [k for k in r if k not in LOCK_FIELDS]
        bad += [k for k in ("blob", "renderer", "template") if not isinstance(r.get(k), str)
                or (r[k] or k != "template") and not LOCK_SHAPES[k].fullmatch(r[k])]
        units = r.get("units")
        if not isinstance(units, list) or not all(isinstance(u, str) and LOCK_SHAPES["unit"].fullmatch(u)
                                                  for u in units):
            bad.append("units")
        if not isinstance(path, str) or bad:
            found.append(f"{SAY}: red · {path!r} · the row breaks {', '.join(sorted(set(bad))) or 'path'} · "
                         f"remedy: re-render; the renderer writes the lock")
            continue
        if path not in tracked:
            found.append(f"{SAY}: red · {path} · the target is not tracked · remedy: commit it or drop its row")
            continue
        if run_git(root, "hash-object", "--", path).strip() != r["blob"]:
            found.append(f"{SAY}: red · {path} · differs from the bytes the renderer wrote · remedy: "
                         f"re-render; never edit the rendered text")
        if r["template"] and TEMPLATE_MARKER_RE.search((root / path).read_text(encoding="utf-8")):
            found.append(f"{SAY}: red · {path} · the rendered charter carries a version marker · remedy: "
                         f"the lock's `template` carries it; re-render")
    return found + [f"{SAY}: lock · {len(rows)} row(s) · {len(found)} red"], 1 if found else 0


def run_grammar(root=".", doc=None) -> tuple[list, int]:
    """S7: `--doc` grades one document through S3; bare, every unit row `read_units` returns through
    `check_statement`, `unarmed` with none, the lock's rows whose `units` is non-empty through S3, and
    the lock through S6."""
    root = pathlib.Path(root)
    if doc is not None:
        found = check_document((root / doc).read_text(encoding="utf-8"))
        return found + [f"{SAY}: grammar · {doc} · {len(found)} red"], 1 if found else 0
    try:
        units, reds = read_units(root), []
    except UnitRowError as exc:
        units, reds = [], [f"{SAY}: red · {ln}" for ln in str(exc).splitlines()]
    for u in units:
        reds += check_statement({"tag": u.tag, "type": u.type, "text": u.text, "source": u.source,
                                 "trigger": u.trigger, "enforced-by": u.enforced_by},
                                lambda tag: load_resolver(root)(tag))
    if not units and not reds:
        lines = [f"{SAY}: grammar · units · unarmed: the tree holds no unit row (PLAY-dOrderedCharter-40 "
                 f"writes the first)"]
    else:
        lines = [f"{SAY}: grammar · units · {len(units)} row(s) · {len(reds)} red"] + reds
    found = []
    graded = [r for r in read_lock(root) if r.get("units")]
    for r in graded:
        found += check_document((root / r["path"]).read_text(encoding="utf-8"), r["units"])
    lines += found + [f"{SAY}: grammar · {len(graded)} unit-rendered document(s) · {len(found)} red"]
    lock_lines, rc = check_lock(root)
    return lines + lock_lines, 1 if reds or found or rc else 0


class Case:
    def __init__(self, top, out):
        self.top, self.out, self.failed = top, out, 0

    def check(self, label, ok, detail=""):
        self.out.append(f"{SAY}:   {'ok' if ok else 'FAILED'} · {label}{' · ' + detail if detail and not ok else ''}")
        self.failed += not ok

    def write_file(self, rel, text):
        path = self.top / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8", newline="")
        run_git(self.top, "add", "--", rel)


def arm_parse(c):
    for good in [*range(len(LEVELS)), *(str(n) for n in range(len(LEVELS)))]:
        c.check(f"parse_level({good!r}) is {int(good)}", parse_level(good) == int(good))
    for bad in (8, -1, PLATFORM, True, "01"):
        try:
            parse_level(bad)
            c.check(f"parse_level({bad!r}) raises LevelError", False, "it parsed")
        except LevelError as exc:
            c.check(f"parse_level({bad!r}) raises LevelError", repr(bad) in str(exc), str(exc))


def arm_tags(c):
    import tag_index
    shipped = pathlib.Path(os.path.abspath(__file__)).read_text(encoding="utf-8")
    c.out.append(f"{SAY}:   extract_level · {' '.join(r[0] for r in tag_index.extract_level({}, '', shipped))}")
    reds = check_level_tags(shipped)
    c.check("the shipped module names level.charter to level.records in LEVELS order", not reds, "; ".join(reds))
    planted = re.sub(r"^LEVELS = .*$", 'LEVELS = tuple(name for name in ("charter", "card"))', shipped,
                     count=1, flags=re.M)
    c.write_file(derive_kit_rel("instruction_units.py"), planted)
    reds = check_level_tags(planted)
    c.check("a computed LEVELS names no tag and reds", bool(reds), "it passed")


def arm_priority(c):
    lines, rc = run_ladder_terms(c.top)
    c.check("a tree with no tracked source reds", rc == 1 and "matches no tracked file" in lines[0],
             " | ".join(lines))
    c.write_file("skills/demo/SKILL.md", "[AGENTS.md · Priority 1 · …]\n")
    demo = derive_tool_rel("demo.template.md")
    c.write_file(demo, "this sits at rank 3\n")
    lines, rc = run_ladder_terms(c.top)
    both = all(any(p in ln and "'level'" in ln for ln in lines)
               for p in ("skills/demo/SKILL.md", demo))
    c.check("ladder-terms exits 1 naming both", rc == 1 and both, " | ".join(lines))
    c.write_file("skills/demo/SKILL.md", "[AGENTS.md · Level 1 · …]\n")
    c.write_file(demo, "this sits at Level 3\n")
    lines, rc = run_ladder_terms(c.top)
    c.check("ladder-terms exits 0 once each reads Level", rc == 0, " | ".join(lines))


STATEMENT_ROWS = (
    # (row, None for a well-formed row, else the rule its red names)
    ({"tag": "fx.directive", "type": DIRECTIVE, "text": "MUST land through the lander.", "trigger": "always"},
     None),
    ({"tag": "fx.constraint", "type": CONSTRAINT, "text": "A guide is at most 30720 bytes.",
      "enforced-by": ["the guide size leg"]}, None),
    ({"tag": "fx.definition", "type": DEFINITION, "text": "pass — one unit built and committed"}, None),
    ({"tag": "fx.pointer", "type": POINTER, "text": "When a level is named, read `level.charter`."}, None),
    ({"tag": "fx.command", "type": POINTER, "text": "Before a push, run `bash {prefix}/push-main.sh`."}, None),
    ({"tag": "fx.policy", "type": POLICY_VALUE, "source": "policy:tags.slice"}, None),
    ({"tag": "fx.fact", "type": FACT, "source": "cmd:git rev-parse --abbrev-ref HEAD"}, None),
    ({"tag": "fx.unregistered", "type": FACT, "source": "cmd:git worktree list"}, "names no registered command"),
    ({"tag": "fx.no-modal", "type": DIRECTIVE, "text": "Land through the lander.", "trigger": "always"},
     "opens with no modal"),
    ({"tag": "fx.no-enforcer", "type": CONSTRAINT, "text": "A guide is at most 30720 bytes."},
     "names no enforcer"),
    ({"tag": "fx.typed-fact", "type": FACT, "text": "Worktrees: none yet"}, "carries no source"),
    ({"tag": "fx.nosuch", "type": POINTER, "text": "When a document is needed, read `doc.nosuch`."},
     "resolves to no unit or slice"),
    ({"tag": "fx.whole", "type": POINTER, "text": "When governing, read `doc.charter`."}, "is a whole document"),
    ({"tag": "fx.typed-policy", "type": POLICY_VALUE, "text": "leaf", "source": "policy:tags.slice"},
     "carries typed text"),
    ({"tag": "fx.prose", "type": "prose", "text": "Some prose."}, "is no statement type"),
)

TODAY_SHAPES = """# fixture — agent charter

*Rendered from the fixture template, whose version is the marker below. Change a source and
re-render; never edit the rendered text.*

<!-- governance-template: v4.4 -->

## 1. Governing practices

- MUST land through the lander.

## Facts

- **Worktrees:** none yet
"""
REFOUNDED = """# fixture — agent charter

## Governing practices

- MUST land through the lander.

```bash
# 1. a shell comment, fenced, never a heading
```

## Facts

- Run `git worktree list` for the worktrees.
"""
FACT_LINE = "- **Worktrees:** three"
FX_TEMPLATE = "<!-- governance-template: v4.4 -->\n\n# fixture — agent charter\n\n- MUST land through the lander.\n"


def arm_statements(c):
    resolve = load_resolver()
    for row, rule in STATEMENT_ROWS:
        reds = check_statement(row, resolve)
        if rule is None:
            c.check(f"a well-formed {row['type']} ({row['tag']}) passes", not reds, " | ".join(reds))
        else:
            c.check(f"{row['tag']} reds naming its tag and '{rule}'",
                    any(row["tag"] in r and rule in r and "remedy:" in r for r in reds), " | ".join(reds) or "passed")


def arm_document(c):
    c.write_file("today.md", TODAY_SHAPES)
    c.write_file("refounded.md", REFOUNDED)
    lines, rc = run_grammar(c.top, "today.md")
    said = "\n".join(lines)
    for label, want in (("the provenance paragraph", "lines 3 to 4 · a provenance paragraph"),
                        ("the version marker", "line 6 · a template version marker"),
                        ("the numbered heading", "`## 1. Governing practices` names a number"),
                        ("the unloaded pointer", "`the marker below` points at text never loaded"),
                        ("the typed fact", "the fact `**Worktrees:**` is typed")):
        c.check(f"grammar --doc exits 1 naming {label}", rc == 1 and want in said, said)
    lines, rc = run_grammar(c.top, "refounded.md")
    c.check("grammar --doc exits 0 on the re-founded charter", rc == 0, " | ".join(lines))
    faced = REFOUNDED + FACT_LINE + "\n"
    pin = f"fx.worktrees@{derive_unit_pin(FACT_LINE)}"
    c.check("a bold-key fact no unit attributes reds", len(check_document(faced)) == 1)
    c.check("the same fact a lock `units` entry attributes passes", not check_document(faced, [pin]),
            " | ".join(check_document(faced, [pin])))


def arm_lock(c):
    import contextlib
    import io
    import render_playbook
    c.write_file(".governance/deploy.toml", 'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "TPL.md"\n')
    c.write_file("TPL.md", FX_TEMPLATE)
    lock = c.top / LOCK
    seen = []
    for _ in range(2):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = render_playbook.main(["--target", str(c.top)])
        seen.append(lock.read_bytes() if lock.is_file() else b"")
        c.check("the render exits 0 and writes the lock", rc == 0 and bool(seen[-1]), out.getvalue())
    c.check("two renders write identical lock bytes", seen[0] == seen[1])
    rows = read_lock(c.top)
    row = rows[0] if len(rows) == 1 else {}
    blob = run_git(c.top, "hash-object", "--", "AGENTS.md").strip()
    c.check("the row's blob is git hash-object of the rendered file", row.get("blob") == blob, f"{row} vs {blob}")
    c.check("the row's renderer and template carry the provenance",
            row.get("renderer") == f"playbook-render@{render_playbook.KIT_PLAYBOOK_RENDER_VERSION}"
            and row.get("template") == "TPL.md@v4.4" and row.get("units") == [], str(row))
    charter = (c.top / "AGENTS.md").read_text(encoding="utf-8")
    c.check("the rendered charter carries no version marker", "governance-template" not in charter, charter)
    run_git(c.top, "add", "--", "AGENTS.md", LOCK)
    lines, rc = check_lock(c.top)
    c.check("lock --check is green over the render", rc == 0, " | ".join(lines))
    c.write_file("AGENTS.md", charter + "a hand edit\n")
    lines, rc = check_lock(c.top)
    c.check("a hand edit reds lock --check naming the path",
            rc == 1 and any("AGENTS.md · differs" in ln for ln in lines), " | ".join(lines))
    c.write_file("AGENTS.md", "<!-- governance-template: v4.4 -->\n" + charter)
    lines, rc = check_lock(c.top)
    c.check("a rendered charter carrying a version marker reds",
            rc == 1 and any("carries a version marker" in ln for ln in lines), " | ".join(lines))
    c.write_file(LOCK, 'target = ["AGENTS.md"]\n')
    try:
        said = f"it read {read_lock(c.top)}"
    except LockError as exc:
        said = str(exc)
    c.check("a target entry that is no table refuses naming the entry", "target entry 1, 'AGENTS.md'" in said, said)
    lock.unlink()
    lines, rc = check_lock(c.top)
    c.check("an absent lock reds", rc == 1 and "holds no row" in lines[0], " | ".join(lines))


#: S6's manifests: every S1 field on one row, the second declaring no class and a forged `origin`
FULL_ROW = '''[[unit]]
tag = "unit.full"
level = 3
type = "directive"
scope = ["reader.every"]
trigger = "always"
budget = "line"
text = "MUST probe the map, then recall."
source = "policy:tags.slice"
owner = "dFixture"
usage = "fixture usage"
help = "the fixture's rationale"
required-by = ["step.build"]
enforced-by = ["spec tokens"]
class = "open"
edges = ["part-of=layer.instruction"]

[[unit]]
tag = "unit.bare"
origin = "forged"
'''
EDGED = '[[unit]]\ntag = "{}"\nscope = ["reader.every"]\nedges = ["part-of=layer.instruction"]\n'
FX_KITS = {"tools/alpha/kit.toml": 'id = "alpha-kit"\n', "tools/beta/kit.toml": 'id = "beta-kit"\n'}
UNREADABLE = {
    "tools/alpha/instructions.toml": '[[unit]]\ntag = "unit.broken"\nlevel = = 3\n',
    "tools/beta/instructions.toml": '[[unit]]\ntag = "unit.nine"\nlevel = "nine"\n\n'
                                    '[[unit]]\ntag = "unit.flat"\nscope = "reader.every"\n',
}
NO_PAIR = '[[unit]]\ntag = "unit.pairless"\nedges = ["part-of"]\n'
NONE_WHY = ('[[unit]]\ntag = "unit.hooked"\nenforced-by = "none — a hook outside this tree"\n\n'
            '[[unit]]\ntag = "unit.gated"\nenforced-by = ["the guide size leg"]\n')
RENDER_ROWS = {
    "tools/alpha/instructions.toml": '[[unit]]\ntag = "unit.land"\nlevel = 3\ntype = "directive"\n'
    'scope = ["reader.driver"]\ntrigger = "always"\ntext = "MUST land through the lander."\n\n'
    '[[unit]]\ntag = "unit.slice"\nlevel = 2\ntype = "policy-value"\nscope = ["reader.every"]\n'
    'source = "policy:tags.slice"\ntext = "typed, never rendered"\n',
    "tools/beta/instructions.toml": '[[unit]]\ntag = "unit.branch"\nlevel = 1\ntype = "fact"\n'
    'scope = ["reader.driver"]\nsource = "cmd:git rev-parse --abbrev-ref HEAD"\n\n'
    '[[unit]]\ntag = "unit.other"\nlevel = 0\ntype = "directive"\nscope = ["reader.subagent"]\n'
    'trigger = "always"\ntext = "MUST stay out of the driver\'s document."\n',
}
UNKNOWN = ('[[unit]]\ntag = "unit.unknown"\nlevel = 2\ntype = "policy-value"\nscope = ["reader.driver"]\n'
           'source = "policy:zz.unknown"\n')


def write_kits(c, alpha, beta=None):
    for rel, text in FX_KITS.items():
        c.write_file(rel, text)
    c.write_file("tools/alpha/instructions.toml", alpha)
    if beta is not None:
        c.write_file("tools/beta/instructions.toml", beta)


def run_commit(top, msg):
    run_git(top, "-c", "user.name=f", "-c", "user.email=f@f", "-c", "commit.gpgsign=false", "commit", "-q", "-m", msg)


def arm_row(c):
    write_kits(c, FULL_ROW)
    units = read_units(c.top)
    full, bare = (units + [None, None])[:2]
    for key, val in tomllib.loads(FULL_ROW)["unit"][0].items():
        got = getattr(full, {"class": "klass"}.get(key, key.replace("-", "_")), None)
        c.check(f"`{key}` reads back", got == (tuple(val) if isinstance(val, list) else val), repr(got))
    c.check("origin is the kit's id, never the row's",
            (getattr(full, "origin", None), getattr(bare, "origin", None)) == ("alpha-kit", "alpha-kit"), str(units))
    c.check("a row declaring no class reads fixed", getattr(bare, "klass", None) == "fixed", str(bare))


def arm_two_kits(c):
    from edge_grammar import read_tree_edges
    c.write_file(".memory-tree.conf", "MEMORY_ROOT=memory\n")
    write_kits(c, EDGED.format("unit.a1") + "\n" + EDGED.format("unit.a2"), EDGED.format("unit.b1"))
    for rel in (OVERLAY, "tools/alpha/sub/instructions.toml", "docs/instructions.toml"):
        c.write_file(rel, EDGED.format("repo.x" if rel == OVERLAY else "unit.decoy"))
    kits = {"tools/alpha/instructions.toml", "tools/beta/instructions.toml"}
    tags = [u.tag for u in read_units(c.top)]
    c.check("read_units reads both kits in path then row order", tags == ["unit.a1", "unit.a2", "unit.b1"], str(tags))
    tracked = [p for p in run_git(c.top, "ls-files", "-z").split("\0") if p]
    claimed = {p for p in tracked if extract_unit({}, p) is not None}
    c.check("extract_unit claims the two kit manifests alone", claimed == kits, str(sorted(claimed)))
    repo = {p for p in tracked if extract_repo({}, p) is not None}
    c.check("extract_repo claims the overlay alone", repo == {OVERLAY}, str(sorted(repo)))
    edges, bad = read_tree_edges(c.top, None)
    sites = {e["path"] for e in edges if e["site"] == "unit"}
    c.check("read_tree_edges reads the two kits and the overlay alone", sites == kits | {OVERLAY} and not bad,
            f"{sorted(sites)} {bad}")


def arm_unreadable(c):
    from edge_grammar import EdgeRefusal, read_unit_edges
    write_kits(c, *UNREADABLE.values())
    for rel, text in UNREADABLE.items():
        faults = parse_unit_rows(text, rel)[1]
        c.check(f"each fault of {rel} names the file and the row",
                bool(faults) and all(f"{rel}: unit row " in str(f) for f in faults), str(faults))
    try:
        said = f"it read {read_units(c.top)}"
    except UnitRowError as exc:
        said = str(exc)
    for want in ("tools/alpha/instructions.toml: unit row 1 at line 1 · the manifest is no TOML",
                 "unit row 1 (unit.nine) at line 1 · `level`", "unit row 2 (unit.flat) at line 5 · `scope`"):
        c.check(f"read_units raises one UnitRowError naming `{want}`", want in said, said)
    units = parse_unit_rows(NO_PAIR, "tools/x/instructions.toml")[0]
    c.check("an edges entry with no `=` reads back as its string",
            [u.edges for u in units] == [("part-of",)], str(units))
    try:
        said = f"it read {read_unit_edges(NO_PAIR, 'tools/x/instructions.toml')}"
    except EdgeRefusal as exc:
        said = str(exc)
    c.check("read_unit_edges refuses it naming the file, the row's line and the entry",
            "tools/x/instructions.toml:{}: unit unit.pairless edges entry 'part-of'".format(1) in said, said)
    enforces = [e["source"] for e in read_unit_edges(NONE_WHY, "tools/x/instructions.toml") if e["type"] == "enforces"]
    c.check("a `none — <why>` enforced-by yields no enforces edge, a list one",
            enforces == ["the guide size leg"], str(enforces))


def arm_arms(c):
    import gov_tag
    import tag_index as ti
    from edge_grammar import read_tree_edges
    root = gov_tag.build_tags_fixture(c.top, "none")
    reg = root / gov_tag.FIXTURE_KIT / "namespaces.toml"
    gov_tag.write_commit(root, {f"{gov_tag.FIXTURE_KIT}/namespaces.toml": reg.read_text(encoding="utf-8")
                                + gov_tag.FIXTURE_UNIT_ROW}, "the unit namespace")
    for files in ({}, {"tools/corekit/instructions.toml": NONE_WHY}):
        if files:
            gov_tag.write_commit(root, files, "unit rows")
        grammar = run_grammar(root)[0][0]
        ctx = ti.derive_context(root, reg)
        con = ti.load_index(root)
        try:
            ti.load_view(con, root, ctx)
            joins = "\n".join(ti.check_namespace_joins(con, ctx)[1])
            members = sorted(r[0] for r in ti.read_rows(con, ("tag",)) if r[5] in ti.UNIT_EXTRACTORS)
        finally:
            con.close()
        edges = [e for e in read_tree_edges(root, None)[0] if e["site"] == "unit"]
        c.out.append(f"{SAY}:   {grammar} · unit members {members} · {len(edges)} unit edge(s)")
        if files:
            c.check("the grammar half grades the fixture's rows", "units · 2 row(s)" in grammar, grammar)
            c.check("the unit namespace holds the fixture's rows", members == ["unit.gated", "unit.hooked"]
                    and "join unit · unarmed" not in joins, f"{members} {joins}")
            c.check("the unit edge site reads the fixture's rows", len(edges) == 1, str(edges))
        else:
            c.check("the grammar half prints unarmed with no row", "units · unarmed" in grammar, grammar)
            c.check("the unit namespace prints unarmed with no row", "join unit · unarmed" in joins, joins)
            c.check("the unit edge site reads no edge with no row", not edges, str(edges))


def arm_render(c):
    from policy_value import read_policy_value, resolve_kit_dir
    write_kits(c, *RENDER_ROWS.values())
    run_git(c.top, "checkout", "-q", "-b", "main")
    run_commit(c.top, "the fixture's rows")

    def read_fixture_policy(key):
        return read_policy_value(key, c.top)

    chosen = derive_unit_selection(read_units(c.top), "reader.driver")
    c.check("the selector holds its own units and reader.every's, in level order",
            [u.tag for u in chosen] == ["unit.branch", "unit.slice", "unit.land"], str([u.tag for u in chosen]))
    said = render_units(chosen, read_fixture_policy).split("\n")
    policy = resolve_kit_dir("policy", "policy.py", KIT_DIR) / "policy.py"
    value = subprocess.run([sys.executable, str(policy), "get", "tags.slice"], cwd=c.top, capture_output=True,
                           text=True, encoding="utf-8", stdin=subprocess.DEVNULL).stdout.rstrip("\n")
    branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True, encoding="utf-8",
                            stdin=subprocess.DEVNULL).stdout.strip()
    c.out.append(f"{SAY}:   rendered · {' | '.join(said)}")
    c.check("one line per unit: the command's output, the key's value as policy.py prints it, the typed text",
            said == [branch, value, "MUST land through the lander."], f"{said} vs {[branch, value]}")
    try:
        said = "it rendered " + render_units(chosen + parse_unit_rows(UNKNOWN, "tools/beta/instructions.toml")[0],
                                             read_fixture_policy)
    except UnitRowError as exc:
        said = str(exc)
    c.check("a refused policy read refuses the render naming the key", "policy zz.unknown" in said, said)


def arm_extractor(c):
    import tag_index as ti
    rel = "tools/alpha/instructions.toml"
    write_kits(c, EDGED.format("unit.blob"))
    run_commit(c.top, "base")
    (c.top / rel).unlink()
    rows = [r[:2] for r in extract_unit({}, rel, run_git(c.top, "show", f"HEAD:{rel}"))]
    c.check("extract_unit reads the base blob's tag and selector rows, absent from the working tree",
            rows == [("unit.blob", "tag"), (EVERY, "selector")], str(rows))
    kit = c.top / derive_tool_rel(KIT_DIR.name)
    kit.mkdir(parents=True)
    for name in ("namespaces.toml", "instruction_units.py"):
        shutil.copyfile(KIT_DIR / name, kit / name)
    names = ("instruction_units:extract_unit", "instruction_units:extract_repo")
    before = ti.derive_extractor_versions(ti.read_namespaces(kit / "namespaces.toml"), kit)
    c.check("the registry names both unit extractors in instruction_units", all(n in before for n in names),
            str(sorted(before)))
    src = (kit / "instruction_units.py").read_text(encoding="utf-8")
    (kit / "instruction_units.py").write_text(src.replace("def parse_unit_rows(", "def parse_unit_rows( ", 1),
                                              encoding="utf-8", newline="")
    after = ti.derive_extractor_versions(ti.read_namespaces(kit / "namespaces.toml"), kit)
    c.check("a byte in the copy's parse_unit_rows changes both versions",
            all(before.get(n) != after.get(n) for n in names), f"{before} {after}")


GOOD_ROW = ('[[unit]]\ntag = "unit.good"\nlevel = 3\ntype = "directive"\nscope = ["reader.every"]\n'
            'trigger = "always"\nbudget = "line"\ntext = "MUST probe the map."\nenforced-by = ["the schema leg"]\n')
SCHEMA_ROWS = (
    # (a malformed row's fields, the field its red names)
    ('tag = "unit.levelless"\ntype = "directive"\ntext = "MUST hold."\n', "level"),
    ('tag = "unit.prose"\nlevel = 3\ntype = "prose"\ntext = "Some prose."\n', "type"),
    (f'tag = "unit.long"\nlevel = 3\ntype = "directive"\nbudget = "line"\ntext = "{"x" * 201}"\n', "text"),
    ('tag = "unit.sourceless"\nlevel = 3\ntype = "fact"\ntext = "Worktrees: none yet"\n', "source"),
    ('tag = "unit.keyed"\nlevel = 3\ntype = "directive"\ntext = "MUST hold."\nprio = 1\n', "prio"),
    ('tag = "unit.unenforced"\nlevel = 3\ntype = "directive"\ntext = "MUST hold."\nenforced-by = ""\n', "enforced-by"),
    ('tag = "repo.elsewhere"\nlevel = 3\ntype = "directive"\ntext = "MUST hold."\n', "tag"),
    ('tag = "unit.classed"\nlevel = 3\ntype = "directive"\ntext = "MUST hold."\nclass = "loose"\n', "class"),
    ('tag = "unit.scoped"\nlevel = 3\ntype = "directive"\ntext = "MUST hold."\nscope = ["nosuch.reader"]\n', "scope"),
    ('tag = "unit.budgeted"\nlevel = 3\ntype = "directive"\ntext = "MUST hold."\nbudget = "page"\n', "budget"),
)
ONE_FACT_ROWS = ('[[unit]]\ntag = "unit.a"\nlevel = 3\ntype = "directive"\ntext = "MUST land  through it."\n\n'
                 '[[unit]]\ntag = "unit.b"\nlevel = 3\ntype = "directive"\ntext = "MUST land through it."\n')
TWO_TERMS = ('[[unit]]\ntag = "unit.c"\nlevel = 3\ntype = "definition"\ntext = "level — a place on the ladder"\n\n'
             '[[unit]]\ntag = "unit.d"\nlevel = 3\ntype = "definition"\ntext = "level — a height of a document"\n')
GATE_TABLE = ('[[target]]\npaths = ["{charter}"]\nrenderer = "playbook:charter"\n\n'
              '[[target]]\npaths = ["CLAUDE.md"]\nrenderer = "playbook:entry-files"\n\n'
              '[[target]]\npaths = [".claude/agents/*.md"]\nrenderer = "kit-adopter"\n\n'
              '[[target]]\npaths = ["memory/guides/KEPT.md"]\nrenderer = "hand"\n')
GATE_FILES = {".memory-tree.conf": 'MEMORY_ROOT=memory\nCHARTER="AGENTS.md"\n', "AGENTS.md": "# fixture charter\n",
              "CLAUDE.md": "@AGENTS.md\n", ".claude/agents/a.md": "an agent\n", "memory/guides/KEPT.md": "a guide\n"}
GATE_LEGACY = "AGENTS.md\nCLAUDE.md\n.claude/agents/a.md\nmemory/guides/KEPT.md\n"
SLOT_ROWS = ('[[unit]]\ntag = "unit.sub"\nlevel = 3\ntype = "directive"\nscope = ["reader.subagent"]\n'
             'trigger = "always"\ntext = "MUST answer the subagent."\n\n'
             '[[unit]]\ntag = "unit.driver"\nlevel = 3\ntype = "directive"\nscope = ["reader.driver"]\n'
             'trigger = "always"\ntext = "MUST stay out of a subagent\'s slot."\n')
SLOT_DEPLOY = 'kits = ["lexicon"]\n\n[answers]\nplaybook_path = "TPL.md"\n'
SLOT_TEMPLATE = "<!-- governance-template: v4.4 -->\n\n# fixture — agent charter\n\n<!-- units: {} -->\n"
SLOT_CHARTER = ("<!-- gov:playbook -->\n# fixture — agent charter\n\nMUST answer the subagent.\n"
                "<!-- /gov:playbook -->\n")
#: The handoff a kit renders over the case's build, pinned from `render_handoff` before the template held it.
ORDER_ROLE = ("---\nname: gov-fixture\ndescription: A fixture role.\nworkflow: fixture\nreads: {}\nrules: {}\n---\n\n"
              "You are the fixture role of {{{{MEMORY_ROOT}}}}.\n")
ORDER_CHARTER = ("## 1. Governing practices\n\n- [alpha] The first rule.\n- [beta] The second rule.\n\n"
                 "## Protocols\n\n- A protocol line.\n\n## Facts\n\n- A fact line.\n")
ORDER_HEAD = ("**Serves:** journal PLAY-fixture-1\n\n# gov-fixture handoff — PLAY-fixture-1\n\n"
              "<!-- gov:handoff role=gov-fixture build=fixture unit=PLAY-fixture-1 path=memory/builds/fixture/prompts/"
              "{date}-prompt-PLAY-fixture-1-1-fixture.md role-sha=e883c92f6c96 task-sha=TASK -->\n\n"
              "## Role\n\nYou are the fixture role of memory.\n\n## Task\n\n"
              "This handoff is for build `fixture`, unit `PLAY-fixture-1`.\nNot supplied, optional: `input:spec`.\n")
ORDER_CASES = (
    # (case, reads, rules, charter, --input, the bytes it pins)
    ("every slot", "input:question, input:spec?", "alpha", ORDER_CHARTER, ["--input", "question=why"],
     ORDER_HEAD.replace("TASK", "9465cdbea5bd") + "\n### input:question\n\nwhy\n\n### Charter rules\n\n"
     "- [alpha] The first rule.\n\n### Protocols\n\n- A protocol line.\n\n### Facts\n\n- A fact line.\n"),
    ("two slots with nothing to fill", "input:spec?", "", "## §1 — Practices\n\n- A pre-tag rule.\n", [],
     ORDER_HEAD.replace("TASK", "64d22ea8580c")),
)


def run_tool(argv, cwd) -> tuple[int, str]:
    """`argv` in `cwd`, no inherited `GIT_*` variable reaching it: `(exit, stdout and stderr)`."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    done = subprocess.run(argv, cwd=cwd, env=env, capture_output=True, stdin=subprocess.DEVNULL)
    return done.returncode, (done.stdout + done.stderr).decode("utf-8", "replace")


def run_render(top, *args) -> tuple[int, str]:
    """`render_playbook.main` over the fixture: `(exit, what it printed)`."""
    import contextlib
    import io
    import render_playbook
    out = io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
        rc = render_playbook.main(["--target", str(top), *args])
    return rc, out.getvalue()


def derive_tool_rel(*parts) -> str:
    """`parts` under the tool root, tree-relative; a root install's empty prefix adds no segment
    (PLAY-dOrderedCharter-70 S5)."""
    return "/".join(p for p in (derive_kit_prefix(), *parts) if p)


def derive_kit_rel(name) -> str:
    """`name` of this kit, tree-relative: the render gate's two tables as a fixture tree holds them."""
    return derive_tool_rel(KIT_DIR.name, name)


def write_gate_tree(c, legacy=GATE_LEGACY, **files):
    """The tree the render gate grades green, `GATE_FILES` with `files` over them, one commit on main."""
    run_git(c.top, "checkout", "-q", "-b", "main")
    c.write_file(derive_kit_rel(RENDERERS_TABLE), GATE_TABLE)
    c.write_file(derive_kit_rel(LEGACY_LIST), legacy)
    c.write_file(derive_tool_rel("check-playbook-parity.sh"), "exit 0\n")
    for rel, text in {**GATE_FILES, **{k.replace("__", "/"): v for k, v in files.items()}}.items():
        c.write_file(rel, text)
    run_commit(c.top, "the gate's tree")


def arm_schema(c):
    write_kits(c, GOOD_ROW)
    lines, rc = run_schema(c.top)
    c.check("a well-formed row passes", rc == 0 and "1 row(s) · 0 red" in lines[-1], " | ".join(lines))
    for row, field in SCHEMA_ROWS:
        write_kits(c, GOOD_ROW + "\n[[unit]]\n" + row)
        lines, rc = run_schema(c.top)
        tag = row.split('"')[1]
        c.check(f"{tag} reds naming the manifest, the tag and `{field}`",
                rc == 1 and any(f"`{field}`" in ln and tag in ln and "tools/alpha/instructions.toml" in ln for ln in lines),
                " | ".join(lines))


def arm_one_fact(c):
    for rows, tags, what in ((ONE_FACT_ROWS, ("unit.a", "unit.b"), "two directives of one normalised text"),
                             (TWO_TERMS, ("unit.c", "unit.d"), "two definitions of one term")):
        write_kits(c, rows)
        lines, rc = run_one_fact(c.top)
        c.check(f"{what} red one-fact naming both", rc == 1 and any(all(t in ln for t in tags) for ln in lines),
                " | ".join(lines))
        units = parse_unit_rows(rows, "tools/alpha/instructions.toml")[0]
        reds = check_one_fact(units, [{"Unit": tags[1], "Action": "remove", "Successor": "none"}])
        c.check(f"{what}, one retired, pass", not reds, " | ".join(reds))


def arm_status(c):
    load_memory_tree_path()
    import build_records
    for records, want in (([], ACTIVE), ([{"Unit": "unit.a", "Action": "edit", "Successor": ""}], ACTIVE),
                          ([{"Unit": "unit.a", "Action": "rename", "Successor": "unit.b"}], "retired:unit.b"),
                          ([{"Unit": "unit.a", "Action": "split", "Successor": "unit.b, unit.c"}], "retired:unit.b,unit.c"),
                          ([{"Unit": "unit.a", "Action": "remove", "Successor": "none"}], "retired:none")):
        got = derive_status("unit.a", records)
        c.check(f"derive_status is {want} over {records}", got == want, got)
    write_gate_tree(c, GATE_LEGACY.replace("AGENTS.md\n", "", 1), **{
        ".governance__deploy.toml": SLOT_DEPLOY, "TPL.md": SLOT_TEMPLATE.format("reader.subagent")})
    write_kits(c, SLOT_ROWS +'\n[[unit]]\ntag = "unit.typed"\nlevel = 3\ntype = "directive"\ntext = "MUST x."\n'
               'status = "active"\n')
    lines, rc = run_schema(c.top)
    c.check("a row typing `status` reds schema", rc == 1 and any("`status`" in ln for ln in lines), " | ".join(lines))
    write_kits(c, SLOT_ROWS)
    rc, said = run_render(c.top)
    c.check("the slot renders while its units are active", rc == 0, said)
    run_git(c.top, "add", "--", "AGENTS.md", LOCK)
    run_commit(c.top, "the rendered charter")
    c.check("read_change_records over a tree with no record returns none", read_change_records(c.top) == [])
    rc, said = run_render(c.top, "--check-render")
    c.check("the gate is green and prints no status line", rc == 0
            and not any(ln.startswith("render-playbook: status") for ln in said.splitlines()), said)
    (c.top / "memory/builds/fx").mkdir(parents=True)
    rel = build_records.write_change(c.top, "fx", "ARCH-fx-1", "unit.sub", "remove", "semantic",
                                     f"unit.sub@{derive_unit_pin('MUST answer the subagent.')}", "none",
                                     build_records.DOOR_PROOF, "none")
    run_git(c.top, "add", "--", rel)
    run_commit(c.top, "a committed record")
    c.check("the committed record reads back", [r["Unit"] for r in read_change_records(c.top)] == ["unit.sub"])
    rc, said = run_render(c.top)
    c.check("a committed record retires its unit at render", rc == 1 and "retired:none" in said, said)
    text = (c.top / rel).read_text(encoding="utf-8")
    c.write_file(rel, text.replace("- **Mark:** semantic\n", ""))
    try:
        raised = f"it read {read_change_records(c.top)}"
    except UnitRowError as exc:
        raised = str(exc)
    c.check("a malformed record raises naming it", rel in raised and "Mark is missing" in raised, raised)
    rc, said = run_render(c.top, "--check-render")
    c.check("a malformed record reds the gate", rc == 1 and rel in said, said)


def arm_renderers(c):
    write_gate_tree(c)
    rc, said = run_render(c.top, "--check-render")
    c.check("a table claiming each file once is green", rc == 0, said)
    c.write_file("memory/guides/NEW.md", "a guide no row claims\n")
    c.write_file(derive_kit_rel(RENDERERS_TABLE), GATE_TABLE + '\n[[target]]\npaths = [".claude/agents/a.md"]\n'
                 'renderer = "hand"\n')
    rc, said = run_render(c.top, "--check-render")
    c.check("--check-render exits 1 naming the unclaimed guide",
            rc == 1 and "memory/guides/NEW.md has no renderer of record" in said, said)
    c.check("--check-render exits 1 naming the agent file two rows claim",
            rc == 1 and ".claude/agents/a.md has 2 renderers of record" in said, said)
    c.write_file(derive_kit_rel(RENDERERS_TABLE), GATE_TABLE + '\n[[target]]\npaths = ["memory/guides/GONE.md"]\n'
                 'renderer = "hand"\n')
    rc, said = run_render(c.top, "--check-render")
    c.check("a row claiming no file reds", rc == 1 and "memory/guides/GONE.md claims no instruction file" in said, said)


def arm_slots(c):
    run_git(c.top, "checkout", "-q", "-b", "main")
    write_kits(c, SLOT_ROWS)
    c.write_file(".governance/deploy.toml", SLOT_DEPLOY)
    c.write_file("TPL.md", SLOT_TEMPLATE.format("reader.subagent"))
    rc, said = run_render(c.top)
    charter = (c.top / "AGENTS.md").read_text(encoding="utf-8")
    c.check("the slot expands to the selected unit's line and nothing of its own",
            rc == 0 and charter == SLOT_CHARTER, f"{said} {charter!r}")
    rows = read_lock(c.top)
    c.check("the lock's row lists the unit the slot rendered",
            [r.get("units") for r in rows] == [[f"unit.sub@{derive_unit_pin('MUST answer the subagent.')}"]], str(rows))
    c.write_file("TPL.md", SLOT_TEMPLATE.format("nosuch.reader"))
    rc, said = run_render(c.top)
    c.check("a selector no namespace registers refuses the render", rc == 1 and "no namespace registers" in said, said)


def arm_legacy(c):
    write_gate_tree(c)
    rc, said = run_render(c.top, "--check-render")
    c.check("every instruction file listed reads green", rc == 0, said)
    c.write_file(".claude/agents/b.md", "an agent on no list\n")
    write_lock_row(c.top, ".claude/agents/a.md", "playbook-render@1.0", "", [("unit.x", "MUST x.")])
    rc, said = run_render(c.top, "--check-render")
    c.check("shrink-only reds a file neither rendered from units nor listed",
            rc == 1 and ".claude/agents/b.md is neither rendered from units nor on" in said, said)
    c.check("shrink-only reds a listed file whose lock row lists units as stale",
            rc == 1 and ".claude/agents/a.md is stale" in said, said)
    c.write_file(derive_kit_rel(LEGACY_LIST), GATE_LEGACY + "memory/guides/GONE.md\n.claude/agents/b.md\n")
    rc, said = run_render(c.top, "--check-render")
    c.check("a listed path no instruction file holds is stale", rc == 1 and "memory/guides/GONE.md is stale" in said, said)
    c.write_file(derive_kit_rel(LEGACY_LIST), GATE_LEGACY)
    c.write_file(".governance/policy.toml", 'instructions.legacy = "refuse"\n')
    run_commit(c.top, "refuse the list")
    rc, said = run_render(c.top, "--check-render")
    c.check("refuse reds every listed file", rc == 1 and all(
        f"{p} is listed and instructions.legacy is refuse" in said for p in ("AGENTS.md", "CLAUDE.md", "memory/guides/KEPT.md")),
        said)
    loose = Case(c.top / "loose", c.out)
    loose.top.mkdir()
    run_git(loose.top, "init", "-q")
    write_gate_tree(loose, **{".governance__policy.toml": 'instructions.legacy = "loose"\n'})
    rc, said = run_render(loose.top, "--check-render")
    c.check("a refused read reds the gate naming instructions.legacy, under no default",
            rc == 1 and "red · instructions.legacy" in said and "legacy · " not in said.replace("red · instructions.legacy", ""),
            said)
    c.failed += loose.failed


def arm_work_order(c):
    from policy_value import resolve_kit_dir
    try:
        kit = resolve_kit_dir("roles", "handoff.py", KIT_DIR)
    except LookupError as exc:
        c.check("the roles kit is present: this case needs it", False, str(exc))
        return
    home = c.top / derive_kit_prefix() / kit.name
    shutil.copytree(kit, home, ignore=shutil.ignore_patterns("__pycache__"))
    c.write_file(".memory-tree.conf", 'MEMORY_ROOT=memory\nCHARTER="AGENTS.md"\n')
    (c.top / "memory" / "builds" / "fixture" / "prompts").mkdir(parents=True)
    argv = [sys.executable, str(home / "handoff.py"), "render", "--role", "gov-fixture", "--build", "fixture",
            "--unit", "PLAY-fixture-1", "--stdout"]

    def read_order(reads, rules, charter, inputs) -> str:
        c.write_file("AGENTS.md", charter)
        (home / "agents" / "gov-fixture.agent.md").write_text(ORDER_ROLE.format(reads, rules), encoding="utf-8", newline="")
        rc, said = run_tool(argv + inputs, c.top)
        return said.split("handoff: ")[0].replace(datetime.date.today().isoformat(), "{date}") if rc == 0 else said

    c.check("the tree holds no playbook kit", not (home.parent / KIT_DIR.name).exists())
    for case, reads, rules, charter, inputs, pinned in ORDER_CASES:
        got = read_order(reads, rules, charter, inputs)
        c.check(f"{case}: handoff.py prints the bytes it printed before the template", got == pinned, repr(got))
    template = home / "templates" / "work-order.template.md"
    text = template.read_text(encoding="utf-8")
    template.write_text(text.replace("slot: reads", "slot: swap").replace("slot: charter-blocks", "slot: reads")
                        .replace("slot: swap", "slot: charter-blocks"), encoding="utf-8", newline="")
    case, reads, rules, charter, inputs, pinned = ORDER_CASES[0]
    c.check("a template moving a slot moves the bytes", read_order(reads, rules, charter, inputs) != pinned)


def arm_no_renderer(c):
    from policy_value import resolve_kit_dir
    from render_playbook import resolve_bash
    name = "adopt-agent-instructions.sh"
    try:
        kit = resolve_kit_dir("agent-instructions", name, KIT_DIR)
    except LookupError as exc:
        c.check("the agent-instructions kit is present: this case needs it", False, str(exc))
        return
    script = c.top / derive_kit_prefix() / kit.name / name
    script.parent.mkdir(parents=True)
    shutil.copyfile(kit / name, script)
    c.write_file("src.md", "# Rules\n")
    bash = resolve_bash(script)
    c.check("a bash sees the adopter", bash is not None)
    rc, said = run_tool([bash or "bash", script.as_posix(), "--source", "src.md"], c.top)
    c.check("the adopter exits 2 naming playbook-render", rc == 2 and "playbook-render" in said, said)
    written = [p for p in ("AGENTS.md", "CLAUDE.md", ".gemini", LOCK) if (c.top / p).exists()]
    c.check("it writes no target", not written, str(written))


def arm_git_env(c):
    """PLAY-dOrderedCharter-69 S4: the `statements` plant run as a child under an exported `GIT_DIR` naming a
    linked worktree of this scratch repository acts on its own scratch, never on the repository it names."""
    from deviation_join import set_env_aside
    c.write_file("a.txt", "a\n")
    run_commit(c.top, "base")
    linked = c.top / "linked"
    run_git(c.top, "worktree", "add", "-q", str(linked))
    index, sentinel = c.top / ".git" / "gov" / "index.db", b"sentinel, not a database"
    index.parent.mkdir(parents=True, exist_ok=True)
    index.write_bytes(sentinel)
    git_dir = run_git(linked, "rev-parse", "--absolute-git-dir").strip()
    with set_env_aside(GIT_DIR=git_dir):
        done = subprocess.run([sys.executable, str(pathlib.Path(__file__).resolve()), "fixture", "--plant", "statements"],
                              cwd=linked, capture_output=True, stdin=subprocess.DEVNULL)
    c.check("the child `statements` fixture exits 0", done.returncode == 0,
            f"exit {done.returncode}: {(done.stdout + done.stderr).decode('utf-8', 'replace').strip()}")
    bare = run_git(c.top, "config", "core.bare").strip()
    c.check("core.bare reads false", bare == "false", bare)
    c.check("the outer index is unchanged", index.read_bytes() == sentinel)


def arm_cmd_source(c):
    """PLAY-dOrderedCharter-70 S1: a `cmd:` source runs only a registered command, in the target, on one line."""
    global REGISTERED_COMMANDS, CMD_TIMEOUT_S
    py = shlex.quote(pathlib.Path(sys.executable).as_posix())
    sentinel = c.top / "sentinel.txt"

    def derive_unit(arg):
        row = f'[[unit]]\ntag = "unit.cmd"\nlevel = 3\ntype = "{FACT}"\nsource = {json.dumps("cmd:" + arg)}\n'
        return parse_unit_rows(row, "tools/alpha/instructions.toml")[0][0]

    def read_render(arg, root=None):
        try:
            return render_unit(derive_unit(arg), None, root)
        except UnitRowError as exc:
            return f"refused: {exc}"
    planted = f'{py} -c "open(\'{sentinel.as_posix()}\', \'w\').write(\'x\')"'
    reds = check_statement({"tag": "fx.cmd", "type": FACT, "source": "cmd:" + planted})
    c.check("an unregistered command reds naming the source and the registry",
            any(repr("cmd:" + planted) in r and "names no registered command" in r and REGISTERED_COMMANDS[0] in r for r in reds),
            " | ".join(reds))
    said = read_render(planted)
    c.check("an unregistered render refuses before any spawn", said.startswith("refused:")
            and "no registered command" in said and not sentinel.exists(), said)
    c.write_file("a.txt", "a\n")
    run_commit(c.top, "base")
    run_git(c.top, "checkout", "-q", "-b", "cmd-root")
    other = c.top / "caller"
    other.mkdir()
    run_git(other, "init", "-q")
    run_git(other, "checkout", "-q", "-b", "caller")
    run_git(other, "-c", "user.name=f", "-c", "user.email=f@f", "commit", "-q", "--allow-empty", "-m", "caller")
    here = os.getcwd()
    try:
        os.chdir(other)
        said = read_render(REGISTERED_COMMANDS[0], c.top)
    finally:
        os.chdir(here)
    c.check("the registered command answers from the target, not the caller's cwd", said == "cmd-root", said)
    kept = REGISTERED_COMMANDS, CMD_TIMEOUT_S
    two, slow = f'{py} -c "print(1); print(2)"', f'{py} -c "import time; time.sleep(5)"'
    try:
        REGISTERED_COMMANDS, CMD_TIMEOUT_S = (two, slow), 1
        said = read_render(two, c.top)
        c.check("a command printing two lines is refused", "more than one line" in said, said)
        said = read_render(slow, c.top)
        c.check("a command outliving the timeout is refused", said.startswith("refused:") and "did not run" in said,
                said)
    finally:
        REGISTERED_COMMANDS, CMD_TIMEOUT_S = kept


PLANTS = {"parse": arm_parse, "tags": arm_tags, "priority": arm_priority, "statements": arm_statements,
          "document": arm_document, "lock": arm_lock, "row": arm_row, "two-kits": arm_two_kits,
          "unreadable": arm_unreadable, "arms": arm_arms, "render": arm_render, "extractor": arm_extractor,
          "schema": arm_schema, "one-fact": arm_one_fact, "status": arm_status, "renderers": arm_renderers,
          "work-order": arm_work_order, "slots": arm_slots, "legacy": arm_legacy, "no-renderer": arm_no_renderer,
          "git-env": arm_git_env, "cmd-source": arm_cmd_source}


def run_fixture(plant=None) -> tuple[list, int]:
    """Each plant in a throwaway repository, the caller's git variables aside (PLAY-dOrderedCharter-69 S1)."""
    load_memory_tree_path()
    from deviation_join import set_env_aside
    from tree_lib import GIT_ENV_LEAKS
    out, failed = [], 0
    for name in [plant] if plant else list(PLANTS):
        top = pathlib.Path(tempfile.mkdtemp(prefix="ladder-fx-"))
        try:
            with set_env_aside(GIT_ENV_LEAKS):
                run_git(top, "init", "-q")
                case = Case(top, out)
                out.append(f"{SAY}: fixture · plant {name}")
                PLANTS[name](case)
                failed += case.failed
        finally:
            shutil.rmtree(top, ignore_errors=True)
    out.append(f"{SAY}: fixture · {'FAILED' if failed else 'green'} · {failed} expectation(s) failed")
    return out, 1 if failed else 0


def main(argv) -> int:
    try:
        root = pathlib.Path(run_git(KIT_DIR, "rev-parse", "--show-toplevel").strip()) if argv[:1] in (
            ["grammar"], ["lock"], ["schema"], ["one-fact"]) else None
        if argv == ["ladder-terms"]:
            lines, rc = run_ladder_terms()
        elif argv == ["schema"]:
            lines, rc = run_schema(root)
        elif argv == ["one-fact"]:
            lines, rc = run_one_fact(root)
        elif argv == ["schema", "one-fact"]:     # the leg: one argv, both verbs, every row's fields first
            lines, rc = run_schema(root)
            if rc == 0:
                more, rc = run_one_fact(root)
                lines += more
        elif argv == ["grammar"] or (len(argv) == 3 and argv[:2] == ["grammar", "--doc"]):
            lines, rc = run_grammar(root, argv[2] if len(argv) == 3 else None)
        elif argv == ["lock", "--check"]:
            lines, rc = check_lock(root)
        elif argv[:1] == ["practices"]:
            lines, rc = run_practices(argv[1:])
        elif argv[:1] == ["fixture"] and (len(argv) == 1 or (len(argv) == 3 and argv[1] == "--plant")):
            plant = argv[2] if len(argv) == 3 else None
            if plant is not None and plant not in PLANTS:
                lines, rc = [f"{SAY}: no plant {plant!r}; the plants are {', '.join(PLANTS)}"], 2
            else:
                lines, rc = run_fixture(plant)
        else:
            lines, rc = [__doc__.split("\n\n")[1]], 2
    except (LevelError, LockError, UnitRowError, OSError, RuntimeError) as exc:  # RuntimeError: the tag index's TagError
        lines, rc = [f"{SAY}: red · {exc}"], 1
    for line in lines:
        sys.stdout.buffer.write((line + "\n").encode("utf-8"))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
