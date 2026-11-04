#!/usr/bin/env python3
"""instruction_units.py — the instruction ladder, levels 0 to 7, and the one term for a place on it
(PLAY-dOrderedCharter-13).

    python instruction_units.py ladder-terms             # the leg: no source names a ladder place by priority or rank
    python instruction_units.py fixture [--plant <case>]  # the plants, each in a throwaway tree

`LEVELS` is the one place an envelope, a unit row, a card or a map reads a level from: a tuple whose index is
the level, so `len(LEVELS)` is the ladder's height and `LEVELS[n]` a level's name. `PLATFORM` names the
harness's own instructions, which sit above the ladder and hold no level. `parse_level` reads a level and
raises `LevelError` on anything else. The `level` namespace's members are `level.<name>`, one per name, which
`tag_index.extract_level` reads from the tuple's literals.

LADDER-TERMS reds each line of a tracked instruction source, the closed pathspec list `LADDER_SOURCES`, that
names an instruction's place as a priority or a rank with a number, naming the path, the line and the remedy;
a pathspec list matching no tracked file is red, never green.

Exit 0 green, 1 red, 2 a usage refusal.
"""
from __future__ import annotations

import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

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


PLANTS = {"parse": arm_parse, "tags": arm_tags, "priority": arm_priority}


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
        if argv == ["ladder-terms"]:
            lines, rc = run_ladder_terms()
        elif argv[:1] == ["fixture"] and (len(argv) == 1 or (len(argv) == 3 and argv[1] == "--plant")):
            plant = argv[2] if len(argv) == 3 else None
            if plant is not None and plant not in PLANTS:
                lines, rc = [f"{SAY}: no plant {plant!r}; the plants are {', '.join(PLANTS)}"], 2
            else:
                lines, rc = run_fixture(plant)
        else:
            lines, rc = [__doc__.split("\n\n")[1]], 2
    except LevelError as exc:
        lines, rc = [f"{SAY}: red · {exc}"], 1
    for line in lines:
        sys.stdout.buffer.write((line + "\n").encode("utf-8"))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
