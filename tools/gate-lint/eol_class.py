#!/usr/bin/env python3
"""Line-ending class scan — every tracked execution-sensitive file is LF by its attribute, not by luck.

Project-agnostic. Run over any repo:

    python <this file> [root]        # exit 0 every member pinned LF, 1 on any finding, 2 a refusal
    python <this file> --selftest    # prove each predicate in BOTH directions, in scratch repositories

THE CLASS (practice.portable.line-endings, TOOL-dWitnessedBar-24). A tracked file whose extension is
`sh`, `py`, `js`, `json` or `toml`, or an extensionless tracked file whose first line, read from the
index, is a `#!` line. A CR in any of them is read by an interpreter or a parser: a shebang names
`bash\\r`, a TAB-split value ends in `\\r`, a byte compare reads every line as changed.

THE PREDICATE. For each member, `git check-attr eol` must resolve `lf` and the index column of
`git ls-files --eol` must not read `crlf`; either failing is one finding naming the path. Both reads
take `-z`, and git resolves its own patterns, so no glob is re-implemented here.

WHY ATTRIBUTES AND THE INDEX, NEVER THE WORKTREE. A checkout under `core.autocrlf=true` writes CRLF
into the worktree of every file the attribute does not pin, and an LF worktree on the node that ran
the check says nothing about the next node. The attribute is what every checkout obeys, and the index
is what every clone receives, so the two together are the class; worktree bytes are one node's luck.

THE POPULATION is `git ls-files` under the root, never a list: an empty one prints its zero and exits
1, because a green run over nothing reads as coverage. The clean line prints the graded count.

WHAT THIS DOES NOT CHECK: a member's worktree bytes (deliberately, above); a file outside the class
that an interpreter still reads, such as a `.txt` table parsed with a TAB split, which its own pin
carries; an index column of `mixed`, which is neither `lf` nor `crlf` and is not graded; and a
shebang file with an extension outside the class. Nor an existing worktree's checkout: a clone made
before the pin keeps its CRLF copies until those files are checked out again
(`git checkout -- <paths>`), which `git add --renormalize .` does not do, since it rewrites the index
and an LF blob is already what the index holds.
"""
from __future__ import annotations

import os
import pathlib
import subprocess
import sys
import tempfile

CLASS_EXTENSIONS = ("sh", "py", "js", "json", "toml")

#: The executed-assertion floor for `--selftest`, compared against the count it prints. Raise it with
#: the arms; it may never be lowered to fit a regression.
FLOOR_ASSERTIONS = 9


def run_git(root: pathlib.Path, args: list[str], stdin: bytes | None = None) -> bytes:
    """git's stdout as bytes under `root`, the inherited-location variables dropped; OSError on a failure."""
    env = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE")}
    p = subprocess.run(["git", "-C", str(root), *args], input=stdin, capture_output=True, env=env)
    if p.returncode != 0:
        raise OSError(f"git {' '.join(args)} exited {p.returncode}: "
                      + p.stderr.decode("utf-8", "replace").strip())
    return p.stdout


def read_index_eol(root: pathlib.Path) -> dict[str, str]:
    """`{path: index eol}` for every tracked path, from `git ls-files --eol -z`."""
    out: dict[str, str] = {}
    for rec in run_git(root, ["ls-files", "--eol", "-z"]).split(b"\0"):
        if not rec:
            continue
        info, _tab, path = rec.partition(b"\t")
        out[path.decode("utf-8", "surrogateescape")] = info.split()[0].decode("ascii", "replace")[2:]
    return out


def read_shebang_members(root: pathlib.Path, paths: list[str]) -> list[str]:
    """The extensionless `paths` whose INDEX blob opens with `#!`, read through one `cat-file --batch`.
    A gitlink (mode 160000, a submodule) names a commit of another repository, which this object store
    need not hold, so it is no file and never a member (TOOL-aFlattenedSeed-1 S2)."""
    if not paths:
        return []
    stage = run_git(root, ["ls-files", "-s", "-z", "--", *paths])
    blobs = {}
    for rec in stage.split(b"\0"):
        if rec:
            meta, _tab, path = rec.partition(b"\t")
            mode, sha = meta.split()[:2]
            if mode != b"160000":
                blobs[path.decode("utf-8", "surrogateescape")] = sha.decode("ascii")
    if not blobs:
        return []
    order = sorted(blobs)
    data = run_git(root, ["cat-file", "--batch"], ("\n".join(blobs[p] for p in order) + "\n").encode("ascii"))
    members, at = [], 0
    for path in order:
        nl = data.index(b"\n", at)
        size = int(data[at:nl].split()[2])
        body = data[nl + 1:nl + 1 + size]
        at = nl + 1 + size + 1
        if body.startswith(b"#!"):
            members.append(path)
    return members


def read_class_population(root: pathlib.Path) -> tuple[list[str], dict[str, str]]:
    """(the class members in path order, every tracked path's index eol)."""
    index = read_index_eol(root)
    members, bare = [], []
    for path in sorted(index):
        name = path.rsplit("/", 1)[-1]
        ext = name.rsplit(".", 1)[-1] if "." in name.lstrip(".") else ""
        if ext in CLASS_EXTENSIONS:
            members.append(path)
        elif not ext and not name.startswith("."):
            bare.append(path)
    members += read_shebang_members(root, bare)
    return sorted(members), index


def read_eol_attributes(root: pathlib.Path, paths: list[str]) -> dict[str, str]:
    """`{path: eol attribute value}` from one `git check-attr --stdin -z eol`."""
    if not paths:
        return {}
    out = run_git(root, ["check-attr", "--stdin", "-z", "eol"],
                  ("\0".join(paths) + "\0").encode("utf-8", "surrogateescape")).split(b"\0")
    return {out[i].decode("utf-8", "surrogateescape"): out[i + 2].decode("utf-8", "replace")
            for i in range(0, len(out) - 2, 3)}


def check_eol(root: pathlib.Path) -> tuple[list[str], int]:
    """(one finding per member not pinned LF or held CRLF in the index, the graded member count)."""
    members, index = read_class_population(root)
    attrs = read_eol_attributes(root, members)
    found = []
    for path in members:
        if attrs.get(path) != "lf":
            found.append(f"{path}: eol attribute is {attrs.get(path, 'unread')!r}, not lf — add a class line "
                         f"to .gitattributes")
        if index.get(path) == "crlf":
            found.append(f"{path}: the index holds CRLF — renormalize it (`git add --renormalize`)")
    return found, len(members)


def run_selftest() -> int:
    """Stage each break in a scratch repository, confirm RED, then its fix, confirm GREEN."""
    ok, n = True, 0

    def check(claim: str, got: object, want: object) -> None:
        nonlocal ok, n
        n += 1
        if got != want:
            print(f"SELFTEST FAIL: {claim} — got {got!r}, wanted {want!r}")
            ok = False

    with tempfile.TemporaryDirectory() as scratch:
        repo = pathlib.Path(scratch)
        run_git(repo, ["init", "-q"])
        run_git(repo, ["config", "core.autocrlf", "false"])
        (repo / ".gitattributes").write_text("* text=auto\n", encoding="utf-8", newline="\n")
        (repo / "a.py").write_text("print(1)\n", encoding="utf-8", newline="\n")
        (repo / "notes.md").write_text("x\n", encoding="utf-8", newline="\n")
        (repo / "hook").write_bytes(b"#!/bin/sh\nexit 0\n")
        (repo / "data").write_bytes(b"plain\n")
        run_git(repo, ["add", "-A"])
        found, graded = check_eol(repo)
        check("an LF worktree a.py with no pin is still red: the attribute is read, not the bytes",
              any(f.startswith("a.py:") for f in found), True)
        check("an extensionless shebang file is a member and red unpinned", any(f.startswith("hook:") for f in found), True)
        check("a .md and an extensionless non-shebang file are outside the class", graded, 2)
        (repo / ".gitattributes").write_text("* text=auto\n*.py text eol=lf\nhook text eol=lf\n",
                                             encoding="utf-8", newline="\n")
        check("each member pinned reads green", check_eol(repo), ([], 2))
        # The CRLF blob lands under `-text`, so git stores its bytes as given; the pin arrives after it.
        (repo / "b.json").write_bytes(b"{}\r\n")
        (repo / ".gitattributes").write_text("* -text\n*.py text eol=lf\nhook text eol=lf\n",
                                             encoding="utf-8", newline="\n")
        run_git(repo, ["add", "b.json"])
        (repo / ".gitattributes").write_text("* text=auto\n*.py text eol=lf\nhook text eol=lf\n*.json eol=lf\n",
                                             encoding="utf-8", newline="\n")
        found, graded = check_eol(repo)
        check("a CRLF blob in the index is red although its attribute reads lf",
              [f.split(":")[0] for f in found], ["b.json"])
        check("the index finding names the renormalize remedy", "renormalize" in (found or [""])[0], True)
        run_git(repo, ["update-index", "--add", "--cacheinfo", "160000," + "1" * 40 + ",vendor"])
        check("a gitlink whose commit this store lacks is no member, and the scan does not crash",
              check_eol(repo)[1], graded)
        empty =pathlib.Path(scratch, "empty")
        empty.mkdir()
        run_git(empty, ["init", "-q"])
        check("an empty population grades zero members", check_eol(empty), ([], 0))
        check("main exits 1 over an empty population", main(["eol_class.py", str(empty)]), 1)
    if n < FLOOR_ASSERTIONS:
        print(f"SELFTEST FAIL: {n} assertion(s) executed, under the floor of {FLOOR_ASSERTIONS}")
        ok = False
    print(f"PASS ({n} assertions)" if ok else f"eol-class selftest: RED ({n} assertions)")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return run_selftest()
    root = pathlib.Path(argv[1] if len(argv) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"eol-class: not a directory: {root}", file=sys.stderr)
        return 2
    try:
        found, graded = check_eol(root)
    except (OSError, ValueError, IndexError) as exc:
        print(f"eol-class: {exc}", file=sys.stderr)
        return 2
    if graded == 0:
        print("eol-class: 0 tracked execution-sensitive files graded — a run over an empty population "
              "is not a pass", file=sys.stderr)
        return 1
    if not found:
        print(f"eol-class: OK — {graded} tracked execution-sensitive file(s) graded, each pinned LF "
              f"by attribute and LF in the index")
        return 0
    print(f"eol-class: {len(found)} finding(s) over {graded} tracked execution-sensitive file(s). A file "
          f"the attribute does not pin is checked out CRLF under core.autocrlf=true.")
    for line in found:
        print(f"  {line}")
    return 1


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")
    raise SystemExit(main(sys.argv))
