#!/usr/bin/env python3
"""memory_index.py — the harness's auto-memory index, measured, its directives detected, one promoted
(PLAY-dOrderedCharter-14).

    python memory_index.py measure [--home <dir>]
    python memory_index.py directives [--home <dir>]
    python memory_index.py promote <name> --level <n> --tag <tag> [--home <dir>] [--build <slug> --unit <id> --mark <mark>]

THE INDEX. The harness writes `MEMORY.md` under `AUTO_MEMORY_TEMPLATE` and injects it into every session;
gov never writes, trims or renders it. `--home` stands for `~`, so a fixture or a card names its home.

`measure` prints one line of at most LINE_MAX bytes, the session card's `memory —` cell: the index's bytes
and lines against `memory.load-budget`, read through the policy reader at the repository the working
directory sits in, a `k` being 1,000 bytes, and the count of standing directives not yet promoted. Every
other outcome is one `memory — skipped:` line, and the verb exits 0 whenever it prints one.

`directives` prints each unpromoted directive, its name then its description, then a count line naming
the links it skipped. `promote` composes one instruction unit row from a directive and hands it to the
guarded write command beside this module, `instructions_edit.py add --manifest overlay`, printing that
command's answer verbatim; only on its exit 0 does the entry's front matter gain `promoted-to: <tag>`.
A refused input exits 2 and calls no command; any other exit of the command is this verb's.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))

from policy_value import PolicyRefused, read_policy_value  # noqa: E402

SAY = "memory-index"
CELL = "memory —"
LINE_MAX = 200
TEXT_MAX = 200
BUDGET_KEY = "memory.load-budget"
#: the levels a repository cannot write a unit at: the card, the task and the records (adopter-instructions item 3)
UNWRITABLE_LEVELS = (1, 6, 7)
LINK = re.compile(r"\[[^\]\n]*\]\(([^)\s]+\.md)\)")
BUDGET = re.compile(r"(\d+)(k?)")


# >>> auto_memory -- canonical copy: auto_memory.py in the gov lib dir (byte-identical; gated)
#: the harness's location of a project's auto-memory; one constant, so a layout change is one edit
AUTO_MEMORY_TEMPLATE = "~/.claude/projects/{checkout}/memory"


def resolve_auto_memory_dir(root: pathlib.Path, declared: str) -> pathlib.Path | None:
    """Expand an AUTO_MEMORY_DIR declaration; None when it is blank (NOT ASKED).

    `~` is the user's home. `{checkout}` is the PRIMARY checkout's absolute path with every
    character outside `[A-Za-z0-9-]` turned into `-` — how Claude Code keys a project's
    auto-memory. The primary checkout is the parent of the common git dir, so every worktree of one
    clone reads the same directory. If git cannot answer, the token stays unexpanded and the path
    names no directory, which the signal reports as DEAD with the path it tried."""
    declared = (declared or "").strip()
    if not declared:
        return None
    if "{checkout}" in declared:
        out = subprocess.run(["git", "-C", str(root), "rev-parse", "--path-format=absolute",
                              "--git-common-dir"], capture_output=True, text=True,
                             encoding="utf-8", errors="replace")
        common = out.stdout.strip()
        if out.returncode == 0 and common:
            key = re.sub(r"[^A-Za-z0-9-]", "-", str(pathlib.Path(common).parent))
            declared = declared.replace("{checkout}", key)
    return root / pathlib.Path(declared).expanduser()
# <<< auto_memory


def resolve_root() -> pathlib.Path:
    """The repository the working directory sits in, else the working directory."""
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                         encoding="utf-8", errors="replace")
    top = out.stdout.strip()
    return pathlib.Path(top) if out.returncode == 0 and top else pathlib.Path.cwd()


def derive_index_dir(root, home=None) -> pathlib.Path:
    """The auto-memory directory of `root`, `home` standing for `~` when given."""
    declared = AUTO_MEMORY_TEMPLATE
    if home is not None:
        declared = str(pathlib.Path(home)) + declared[1:]
    return resolve_auto_memory_dir(pathlib.Path(root), declared)


def derive_byte_cut(text: str, cap: int) -> str:
    """`text` cut to at most `cap` UTF-8 bytes, never inside a character."""
    return text.encode("utf-8")[:cap].decode("utf-8", errors="ignore")


def read_front_matter(path: pathlib.Path) -> dict:
    """The entry's `name`, `description`, whether it is a directive (`type: feedback`, at column 0 or
    indented under `metadata:`) and whether a `promoted-to:` line marks it promoted."""
    lines = path.read_text(encoding="utf-8").splitlines()
    got = {"name": path.stem, "description": "", "directive": False, "promoted": False}
    if not lines or lines[0].strip() != "---":
        return got
    under_metadata = False
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line[:1] not in (" ", "\t"):
            under_metadata = line.startswith("metadata:")
        key, _, value = line.strip().partition(":")
        value = value.strip()
        top = line[:1] not in (" ", "\t")
        if key == "promoted-to":
            got["promoted"] = True
        elif key == "type" and value == "feedback" and (top or under_metadata):
            got["directive"] = True
        elif top and key in ("name", "description") and value:
            if value[:1] == '"':
                try:
                    value = json.loads(value)
                except ValueError:
                    value = value.strip('"')
            elif value[:1] == "'" and value[-1:] == "'":
                value = value[1:-1].replace("''", "'")
            got[key] = value
    return got


def scan_directives(root, home=None) -> dict:
    """Each index entry whose file is a directive and carries no `promoted-to:` line.

    It walks the index's `[<title>](<file>.md)` links and opens a file under the memory directory only: a
    link resolving outside it is skipped and listed in `outside`, one naming no readable file in
    `unreadable`. WHAT IT DOES NOT READ: a directive written as prose inside a `project` or `reference`
    entry, and an index line carrying no link. -> {"dir", "directives", "entries", "outside", "unreadable"}."""
    d = derive_index_dir(root, home)
    text = (d / "MEMORY.md").read_text(encoding="utf-8")
    base = d.resolve()
    found = {"dir": d, "directives": [], "entries": 0, "outside": [], "unreadable": []}
    for target in LINK.findall(text):
        path = (base / target).resolve()
        if base not in path.parents:
            found["outside"].append(target)
            continue
        try:
            entry = read_front_matter(path)
        except (OSError, UnicodeDecodeError):
            found["unreadable"].append(target)
            continue
        found["entries"] += 1
        if entry["directive"] and not entry["promoted"]:
            found["directives"].append({**entry, "path": path})
    return found


def measure_index(root, home=None) -> dict:
    """The index's bytes and lines, its budget in bytes with the policy reader's source, and the
    unpromoted directives; `skipped` carries the reason instead where any of them cannot be read."""
    d = derive_index_dir(root, home)
    try:
        raw = (d / "MEMORY.md").read_bytes()
        found = scan_directives(root, home)
    except (OSError, UnicodeDecodeError) as exc:
        detail = "" if isinstance(exc, FileNotFoundError) else f" · {exc}"
        return {"skipped": f"no auto-memory index at {d}{detail}"}
    try:
        values, explain = read_policy_value("memory.load-budget", root)
    except PolicyRefused as exc:
        return {"skipped": f"{BUDGET_KEY} unread · {exc.line}"}
    hit = BUDGET.fullmatch(values[0].strip()) if values else None
    if hit is None:
        return {"skipped": f"{BUDGET_KEY} unread · {values!r} is no byte figure"}
    fields = [f.strip() for f in explain.split("·")]
    return {"bytes": len(raw), "lines": len(raw.splitlines()),
            "budget": int(hit.group(1)) * (1000 if hit.group(2) else 1),
            "source": fields[1] if len(fields) > 1 else "read", "directives": found["directives"]}


def render_memory_line(measured: dict) -> str:
    """The `memory —` cell's one line, cut to LINE_MAX bytes."""
    if "skipped" in measured:
        return derive_byte_cut(f"{CELL} skipped: {measured['skipped']}", LINE_MAX)
    side = "over" if measured["bytes"] > measured["budget"] else "within"
    return derive_byte_cut(f"{CELL} MEMORY.md {measured['bytes']} B {side} its {measured['budget']} B budget "
                     f"({BUDGET_KEY} {measured['source']}) · {measured['lines']} lines · "
                     f"{len(measured['directives'])} standing directives unpromoted · list: memory_index.py directives",
                     LINE_MAX)


def run_directives(root, home=None) -> tuple[list, int]:
    try:
        found = scan_directives(root, home)
    except (OSError, UnicodeDecodeError) as exc:
        return [f"{SAY}: no auto-memory index at {derive_index_dir(root, home)} · {exc}"], 1
    lines = [f"{e['name']} — {e['description']}" for e in found["directives"]]
    tail = f"{SAY}: {len(found['directives'])} unpromoted of {found['entries']} entries read · " \
           f"{len(found['outside'])} links outside the memory directory skipped"
    if found["outside"]:
        tail += ": " + ", ".join(found["outside"])
    if found["unreadable"]:
        tail += f" · {len(found['unreadable'])} unreadable: " + ", ".join(found["unreadable"])
    return [*lines, tail], 0


def write_promoted_to(path: pathlib.Path, tag: str) -> None:
    """One `promoted-to: <tag>` line before the front matter's closing `---`, every other byte kept."""
    raw = path.read_bytes().decode("utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(nl)
    end = next(i for i, ln in enumerate(lines[1:], 1) if ln.strip() == "---")
    lines.insert(end, f"promoted-to: {tag}")
    path.write_bytes(nl.join(lines).encode("utf-8"))


def run_promote(root, name, level, tag, home=None, record=(), command=None) -> tuple[list, int]:
    """S4: refuse what the command must never see, compose the row, hand it to the guarded command and
    print its answer, then mark the entry on the command's exit 0 alone. `record` is the `--build`,
    `--unit` and `--mark` pairs given; `command` the guarded command's file, the one beside this module."""
    import instruction_units as iu
    import tag_index
    try:
        found = scan_directives(root, home)
    except (OSError, UnicodeDecodeError) as exc:
        return [f"{SAY}: refused · no auto-memory index at {derive_index_dir(root, home)} · {exc}"], 2
    entry = next((e for e in found["directives"] if e["name"] == name), None)
    if entry is None:
        return [f"{SAY}: refused · no unpromoted directive is named {name!r} · remedy: `directives` lists them"], 2
    if not str(level).isdigit() or int(level) >= len(iu.LEVELS):
        return [f"{SAY}: refused · --level {level} is outside the levels 0 to {len(iu.LEVELS) - 1}"], 2
    if int(level) in UNWRITABLE_LEVELS:
        return [f"{SAY}: refused · --level {level} ({iu.LEVELS[int(level)]}) is a level the repository cannot "
                f"write · remedy: a level of 0 or 2 to 5"], 2
    words = {r["ns"] for r in tag_index.read_namespaces(KIT_DIR / "namespaces.toml")}
    fault = tag_index.derive_tag_fault(tag, words)
    if fault:
        return [f"{SAY}: refused · --tag {tag} · {fault}"], 2
    row = {"tag": tag, "level": int(level), "type": "directive", "text": derive_byte_cut(entry["description"], TEXT_MAX)}
    composed = [f"{SAY}: composed · [[unit]] from auto-memory {name}",
                *(f"{k} = {json.dumps(v, ensure_ascii=False)}" for k, v in row.items())]
    argv = [sys.executable, str(command or KIT_DIR / "instructions_edit.py"), "add", "--manifest", "overlay",
            "--tag", tag, "--level", str(row["level"]), "--type", "directive", "--text", row["text"],
            "--promoted-from", f"auto-memory {name}", *[a for pair in record for a in pair]]
    # stderr stays this process's own: the command reads a terminal on it as the owner's proof
    said = subprocess.run(argv, cwd=str(root), stdout=subprocess.PIPE, stdin=subprocess.DEVNULL,
                          text=True, encoding="utf-8", errors="replace")
    lines = [*composed, *said.stdout.splitlines()]
    if said.returncode != 0:
        return lines, said.returncode
    write_promoted_to(entry["path"], tag)
    return [*lines, f"{SAY}: promoted · {entry['path'].name} carries promoted-to: {tag}"], 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="memory_index.py", description=__doc__.split("\n\n")[0], allow_abbrev=False)
    sub = ap.add_subparsers(dest="verb", required=True)
    for verb in ("measure", "directives", "promote"):
        p = sub.add_parser(verb, allow_abbrev=False)
        p.add_argument("--home")
        if verb == "promote":
            p.add_argument("name")
            p.add_argument("--level", required=True)
            p.add_argument("--tag", required=True)
            for flag in ("--build", "--unit", "--mark"):
                p.add_argument(flag)
    return ap


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    args = build_parser().parse_args(sys.argv[1:] if argv is None else argv)
    root = resolve_root()
    if args.verb == "measure":
        lines, rc = [render_memory_line(measure_index(root, args.home))], 0
    elif args.verb == "directives":
        lines, rc = run_directives(root, args.home)
    else:
        record = [(f"--{k}", getattr(args, k)) for k in ("build", "unit", "mark") if getattr(args, k)]
        lines, rc = run_promote(root, args.name, args.level, args.tag, args.home, record)
    print("\n".join(lines))
    return rc


if __name__ == "__main__":
    sys.exit(main())
