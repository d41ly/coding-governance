#!/usr/bin/env python3
"""instruction_units.py — the instruction ladder, levels 0 to 7, and the one term for a place on it
(PLAY-dOrderedCharter-13); the statement grammar and the render provenance lock (PLAY-dOrderedCharter-12).

    python instruction_units.py ladder-terms             # the leg: no source names a ladder place by priority or rank
    python instruction_units.py grammar [--doc <path>]   # the leg: unit rows, unit-rendered documents, the lock
    python instruction_units.py lock --check             # the lock against the tree
    python instruction_units.py fixture [--plant <case>]  # the plants, each in a throwaway tree

`LEVELS` is the one place an envelope, a unit row, a card or a map reads a level from: a tuple whose index is
the level, so `len(LEVELS)` is the ladder's height and `LEVELS[n]` a level's name. `PLATFORM` names the
harness's own instructions, which sit above the ladder and hold no level. `parse_level` reads a level and
raises `LevelError` on anything else. The `level` namespace's members are `level.<name>`, one per name, which
`tag_index.extract_level` reads from the tuple's literals.

LADDER-TERMS reds each line of a tracked instruction source, the closed pathspec list `LADDER_SOURCES`, that
names an instruction's place as a priority or a rank with a number, naming the path, the line and the remedy;
a pathspec list matching no tracked file is red, never green.

THE STATEMENT GRAMMAR. Every loaded unit is one of `STATEMENT_TYPES`; `check_statement` grades a unit row
against its type and `check_document` a rendered document for the four shapes that load without giving
direction. GRAMMAR grades every unit row through unit 9's reader, `unarmed` until it lands, every lock row
whose `units` is non-empty through `check_document`, and the lock; `--doc` grades one document on demand.

THE LOCK, `.governance/instructions.lock`, carries render provenance instead of the loaded text: one
`[[target]]` row per rendered target, `path`, `blob` (the git blob id of the rendered bytes), `units`
(`<tag>@<hash8>` each), `renderer` and `template`. `write_lock_row` is its one writer, the renderer its
caller, and `read_lock` its one reader. LOCK --CHECK reds an absent or empty lock, a row breaking those
fields, an untracked path, a blob the working tree no longer matches, and a rendered charter carrying a
version marker.

Exit 0 green, 1 red, 2 a usage refusal.
"""
from __future__ import annotations

import os
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

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

LADDER_SOURCES = (
    "coding-governance-agents.template.md",
    ":(glob)tools/*.template.md",
    ":(glob)tools/*/*.template.md",
    ":(glob)tools/roles/agents/*.agent.md",
    ":(glob)skills/*/SKILL.md",
    ":(glob)tools/workflows/*.template.js",
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


def run_ladder_terms(root=".") -> tuple[list, int]:
    """S4: every tracked LADDER_SOURCES line naming a ladder place as a priority or a rank, red."""
    paths = [p for p in run_git(root, "ls-files", "-z", "--", *LADDER_SOURCES).split("\0") if p]
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


def derive_unit_pin(text) -> str:
    """Unit 24's `derive_pin_hash` of `text`, read from the memory-tree kit beside this one."""
    from policy_value import resolve_kit_dir
    mt = str(resolve_kit_dir("memory-tree", "design_lib.py", KIT_DIR))
    if mt not in sys.path:
        sys.path.append(mt)
    import design_lib
    return design_lib.derive_pin_hash(text)


def read_lock(root=".") -> list[dict]:
    """S4's one reader: the lock's `[[target]]` rows, `[]` for an absent lock. Raises LockError on a lock
    that does not parse."""
    path = pathlib.Path(root) / LOCK
    if not path.is_file():
        return []
    try:
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("target") or []
    except tomllib.TOMLDecodeError as exc:
        raise LockError(f"{LOCK} does not parse: {exc}") from None
    return [r for r in rows if isinstance(r, dict)]


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
    """S7: `--doc` grades one document through S3; bare, the unit rows through unit 9's reader, the lock's
    rows whose `units` is non-empty through S3, and the lock through S6."""
    root = pathlib.Path(root)
    if doc is not None:
        found = check_document((root / doc).read_text(encoding="utf-8"))
        return found + [f"{SAY}: grammar · {doc} · {len(found)} red"], 1 if found else 0
    lines = [f"{SAY}: grammar · units · unarmed: no unit reader (PLAY-dOrderedCharter-9)"]
    found = []
    graded = [r for r in read_lock(root) if r.get("units")]
    for r in graded:
        found += check_document((root / r["path"]).read_text(encoding="utf-8"), r["units"])
    lines += found + [f"{SAY}: grammar · {len(graded)} unit-rendered document(s) · {len(found)} red"]
    lock_lines, rc = check_lock(root)
    return lines + lock_lines, 1 if found or rc else 0


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
    c.write_file("tools/playbook/instruction_units.py", planted)
    reds = check_level_tags(planted)
    c.check("a computed LEVELS names no tag and reds", bool(reds), "it passed")


def arm_priority(c):
    lines, rc = run_ladder_terms(c.top)
    c.check("a tree with no tracked source reds", rc == 1 and "matches no tracked file" in lines[0],
             " | ".join(lines))
    c.write_file("skills/demo/SKILL.md", "[AGENTS.md · Priority 1 · …]\n")
    c.write_file("tools/demo.template.md", "this sits at rank 3\n")
    lines, rc = run_ladder_terms(c.top)
    both = all(any(p in ln and "'level'" in ln for ln in lines)
               for p in ("skills/demo/SKILL.md", "tools/demo.template.md"))
    c.check("ladder-terms exits 1 naming both", rc == 1 and both, " | ".join(lines))
    c.write_file("skills/demo/SKILL.md", "[AGENTS.md · Level 1 · …]\n")
    c.write_file("tools/demo.template.md", "this sits at Level 3\n")
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
    ({"tag": "fx.command", "type": POINTER, "text": "Before a push, run `bash tools/push-main.sh`."}, None),
    ({"tag": "fx.policy", "type": POLICY_VALUE, "source": "policy:tags.slice"}, None),
    ({"tag": "fx.fact", "type": FACT, "source": "cmd:git worktree list"}, None),
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
    lock.unlink()
    lines, rc = check_lock(c.top)
    c.check("an absent lock reds", rc == 1 and "holds no row" in lines[0], " | ".join(lines))


PLANTS = {"parse": arm_parse, "tags": arm_tags, "priority": arm_priority, "statements": arm_statements,
          "document": arm_document, "lock": arm_lock}


def run_fixture(plant=None) -> tuple[list, int]:
    out, failed = [], 0
    for name in [plant] if plant else list(PLANTS):
        top = pathlib.Path(tempfile.mkdtemp(prefix="ladder-fx-"))
        try:
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
            ["grammar"], ["lock"]) else None
        if argv == ["ladder-terms"]:
            lines, rc = run_ladder_terms()
        elif argv == ["grammar"] or (len(argv) == 3 and argv[:2] == ["grammar", "--doc"]):
            lines, rc = run_grammar(root, argv[2] if len(argv) == 3 else None)
        elif argv == ["lock", "--check"]:
            lines, rc = check_lock(root)
        elif argv[:1] == ["fixture"] and (len(argv) == 1 or (len(argv) == 3 and argv[1] == "--plant")):
            plant = argv[2] if len(argv) == 3 else None
            if plant is not None and plant not in PLANTS:
                lines, rc = [f"{SAY}: no plant {plant!r}; the plants are {', '.join(PLANTS)}"], 2
            else:
                lines, rc = run_fixture(plant)
        else:
            lines, rc = [__doc__.split("\n\n")[1]], 2
    except (LevelError, LockError, OSError, RuntimeError) as exc:  # RuntimeError: the tag index's TagError
        lines, rc = [f"{SAY}: red · {exc}"], 1
    for line in lines:
        sys.stdout.buffer.write((line + "\n").encode("utf-8"))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
