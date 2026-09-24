#!/usr/bin/env python3
"""Encoding-posture scan — tracked Python that does text IO without naming its encoding.

Project-agnostic. Run over any repo:

    python <this file> [registry-path] [root] [pathspec ...]   # exit 0 clean, 1 findings, 2 refusal
    python <this file> --selftest                               # prove both arms in BOTH directions

THE CLASS. A text-mode read or subprocess with no `encoding=` decodes with the platform default:
cp1251 or cp1252 on a Windows node, UTF-8 in CI. An unencoded read of a UTF-8 file therefore raises
`UnicodeDecodeError` on one machine and passes on the other, and the population that crashes is the
one no gate runner reaches — a session running a script by hand, a hook calling one directly. Setting
`PYTHONUTF8=1` in a runner fixes the runner and nothing else, which is why the fix is the keyword.

Ported from an adopter's AST scanner, whose predicate is kept whole. Two arms, both by AST, because
a line grep cannot see a call split across continuation lines:

  * `file-io`    — `open` / `.open` / `.read_text` / `.write_text` in TEXT mode with no `encoding=`
    in either its keyword or its positional slot
  * `subprocess` — `subprocess.*` with `text=True` / `universal_newlines=True` and no `encoding=`

WHAT THIS DOES NOT CHECK, said here because a structural check reads as a semantic one to everyone
who did not write it:

  * stdout encoding. A static check of a print-encoding failure needs runtime context, and a weak
    one is vacuous, so it is not attempted.
  * `p.open()` where `p` is a Path VARIABLE. Only a provably-Path receiver — `Path(x).open()` or
    `(a / b).open()` — is graded, because `Image.open` and `tokenize.open` reject an `encoding=`
    outright, and a fixer acting on a false report raises TypeError. A MISS, deliberately.
  * A mode held in a variable is graded as TEXT, the fail-closed direction: an unresolvable mode
    must not buy an exemption.
  * `io.open`, `codecs.open`, `subprocess` imported under another name, and a call through an alias
    (`run = subprocess.run`). Each is a MISS.

THE POPULATION is `git ls-files` under the root, restricted to `*.py` and to the optional pathspecs,
never a list somebody maintains: a scan that graded a hand-kept set goes quiet on the file that
arrives without being added to it. The clean line prints the graded file count, and an empty
population prints its zero and exits 1, because a green run over nothing reads as coverage.

THE REGISTRY is a shrink-only declaration of the sites that predate the gate, one row per
`<path>\t<arm>\t<count>\t<reason>`, keyed on the ARM and never on a line number — a line-keyed
registry reds on unrelated edits, and a gate whose steady state is red gets bypassed. Set equality
in both directions: a measured site with no row fails, a row the scan no longer finds fails, and a
count may fall with its sites and may not rise. The argument is OPTIONAL: omitted, the run grades
against an empty declaration, which is the honest first reading of a tree nobody has graded; one
that was SUPPLIED and does not resolve is a typo and refuses.
"""
from __future__ import annotations

import ast
import pathlib
import subprocess
import sys
import tempfile

ARMS = ("file-io", "subprocess")
# method -> the positional slot its `encoding` argument occupies:
#   Path.read_text(encoding, errors) · Path.write_text(data, encoding, errors)
FILE_TEXT_METHODS = {"read_text": 0, "write_text": 1}
SUBPROCESS_FNS = {"run", "Popen", "call", "check_call", "check_output"}
TEXT_MODE_FLAGS = ("text", "universal_newlines")

#: The executed-assertion floor for `--selftest`, compared against the count it prints. Raise it
#: with the arms; it may never be lowered to fit a regression.
FLOOR_ASSERTIONS = 26


def read_kwarg(call: ast.Call, name: str) -> ast.expr | None:
    for kw in call.keywords:
        if kw.arg == name:
            return kw.value
    return None


def check_encoding(call: ast.Call, positional_index: int | None) -> bool:
    """True when `encoding` is supplied as a keyword OR in its positional slot.

    `Path.read_text("utf-8")` is already correct, and a gate that cannot see that reports it and
    tempts a fixer into passing the argument twice, which is a TypeError at runtime.
    """
    if read_kwarg(call, "encoding") is not None:
        return True
    return positional_index is not None and len(call.args) > positional_index


def check_binary_mode(call: ast.Call, positional_index: int) -> bool:
    """True when the call's mode argument is a literal containing 'b'. A variable mode is TEXT."""
    mode = read_kwarg(call, "mode")
    if mode is None and len(call.args) > positional_index:
        mode = call.args[positional_index]
    return isinstance(mode, ast.Constant) and isinstance(mode.value, str) and "b" in mode.value


def scan_text_io(tree: ast.AST) -> list[tuple[int, int, str, str]]:
    """(line, col, arm, description) for every unencoded text-IO call in one module."""
    found: list[tuple[int, int, str, str]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        # `open(file, mode, buffering, encoding, ...)`
        if isinstance(node.func, ast.Name) and node.func.id == "open":
            if not check_binary_mode(node, 1) and not check_encoding(node, 3):
                found.append((node.lineno, node.col_offset, "file-io", "open(...)"))
            continue
        if not isinstance(node.func, ast.Attribute):
            continue
        attr, receiver = node.func.attr, node.func.value
        if attr == "open":
            # ONLY a provably-Path receiver; the header says why a Path VARIABLE is a MISS.
            path_call = isinstance(receiver, ast.Call) and (
                (isinstance(receiver.func, ast.Name) and receiver.func.id == "Path")
                or (isinstance(receiver.func, ast.Attribute) and receiver.func.attr == "Path"))
            joined = isinstance(receiver, ast.BinOp) and isinstance(receiver.op, ast.Div)
            if (path_call or joined) and not check_binary_mode(node, 0) and not check_encoding(node, 2):
                found.append((node.lineno, node.col_offset, "file-io", ".open(...)"))
            continue
        if attr in FILE_TEXT_METHODS:
            if not check_encoding(node, FILE_TEXT_METHODS[attr]):
                found.append((node.lineno, node.col_offset, "file-io", f".{attr}(...)"))
            continue
        if attr in SUBPROCESS_FNS and isinstance(receiver, ast.Name) and receiver.id == "subprocess":
            text_mode = any(
                isinstance(v, ast.Constant) and bool(v.value)
                for v in (read_kwarg(node, f) for f in TEXT_MODE_FLAGS))
            if text_mode and read_kwarg(node, "encoding") is None:
                found.append((node.lineno, node.col_offset, "subprocess", f"subprocess.{attr}(...)"))
    return found


def scan_tree(root: pathlib.Path, pathspecs: list[str]) -> tuple[list[tuple[str, int, int, str, str]], int]:
    """Every tracked `*.py` under `root` and the pathspecs, scanned. Returns (hits, files scanned).

    Raises OSError on a dead probe or an unparseable file: both are refusals, never a zero.
    """
    listing = subprocess.run(
        ["git", "ls-files", "-z", "--", *(pathspecs or ["."])],
        cwd=str(root), capture_output=True, text=True, encoding="utf-8")
    if listing.returncode != 0:
        # A DEAD PROBE must not be spelled the way an empty tree is: both yield zero files.
        raise OSError("git ls-files failed, so the population could not be derived at all: "
                      + (listing.stderr or "").strip())
    hits: list[tuple[str, int, int, str, str]] = []
    scanned = 0
    for rel in sorted(p for p in listing.stdout.split("\0") if p.endswith(".py")):
        full = root / rel
        if not full.is_file():
            continue
        try:
            tree = ast.parse(full.read_bytes().decode("utf-8"), filename=rel)
        except (SyntaxError, UnicodeDecodeError, ValueError) as exc:
            raise OSError(f"{rel}: cannot be parsed, so it cannot be graded: {exc}") from exc
        scanned += 1
        hits.extend((rel, line, col, arm, what) for line, col, arm, what in scan_text_io(tree))
    return hits, scanned


def build_measured(hits: list[tuple[str, int, int, str, str]]) -> dict[tuple[str, str], int]:
    """The hits as `{(path, arm): count}` — the registry's own key."""
    measured: dict[tuple[str, str], int] = {}
    for rel, _line, _col, arm, _what in hits:
        measured[(rel, arm)] = measured.get((rel, arm), 0) + 1
    return measured


def read_registry(path: pathlib.Path) -> tuple[dict[tuple[str, str], int], list[str]]:
    """The declared sites, plus every malformed row. A row is `path TAB arm TAB count TAB reason`."""
    declared: dict[tuple[str, str], int] = {}
    malformed: list[str] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        row = raw.rstrip("\r")
        if not row.strip() or row.lstrip().startswith("#"):
            continue
        fields = row.split("\t")
        if len(fields) < 4 or not fields[3].strip():
            malformed.append(f"line {number}: not <path> TAB <arm> TAB <count> TAB <reason>: {row}")
            continue
        rel, arm, count = fields[0].strip(), fields[1].strip(), fields[2].strip()
        if arm not in ARMS:
            malformed.append(f"line {number}: {arm!r} is not an arm ({', '.join(ARMS)}) — the key is "
                             f"the ARM, never a line number, because a line number moves on an "
                             f"unrelated edit: {row}")
            continue
        if not count.isdigit() or int(count) < 1:
            malformed.append(f"line {number}: count {count!r} is not a positive integer: {row}")
            continue
        if (rel, arm) in declared:
            malformed.append(f"line {number}: ({rel}, {arm}) is declared twice: {row}")
            continue
        declared[(rel, arm)] = int(count)
    return declared, malformed


def resolve_declaration(arg: str | None) -> tuple[dict[tuple[str, str], int], list[str]]:
    """The declared sites for the OPTIONAL registry argument; a supplied path that does not resolve raises."""
    if arg is None:
        return {}, []
    path = pathlib.Path(arg)
    if not path.is_file():
        raise OSError(f"no registry at {path} — the argument was SUPPLIED and does not resolve to a "
                      f"file, which is a typo and not a posture; OMIT it to grade against an empty "
                      f"declaration")
    return read_registry(path)


def check_registry(measured: dict[tuple[str, str], int],
                   declared: dict[tuple[str, str], int]) -> list[str]:
    """Set equality in both directions, with the counts. Returns one line per violation."""
    problems = []
    for key in sorted(set(measured) | set(declared)):
        rel, arm = key
        have, want = measured.get(key), declared.get(key)
        if want is None:
            problems.append(f"{rel}: {have} unencoded [{arm}] call(s) and no registry row declares "
                            f"them — pass encoding=\"utf-8\"")
        elif have is None:
            problems.append(f"{rel}: the registry declares [{arm}] and the scan no longer finds it — "
                            f"delete the row, or a drained site leaves a widened exemption behind")
        elif have != want:
            problems.append(f"{rel}: the registry declares {want} [{arm}] site(s) and the scan "
                            f"measures {have} — the count may fall with the sites and may not rise")
    return problems


def run_selftest() -> int:
    """Stage the break, confirm RED. A gate whose failing case has never been observed is not one."""
    ok = True
    n = 0

    def check(claim: str, got: object, want: object) -> None:
        nonlocal ok, n
        n += 1
        if got != want:
            print(f"SELFTEST FAIL: {claim} — got {got!r}, wanted {want!r}")
            ok = False

    def scan_arms(source: str) -> list[str]:
        return [arm for _l, _c, arm, _w in scan_text_io(ast.parse(source))]

    # Each arm: the offending form and its nearest innocent twin, so an arm cannot pass by grading
    # nothing — the same run must name one and not the other.
    check("file-io: a bare open() is named", scan_arms("open(p)\n"), ["file-io"])
    check("file-io: open() with encoding= clears", scan_arms("open(p, encoding='utf-8')\n"), [])
    check("file-io: open() in binary mode clears", scan_arms("open(p, 'rb')\n"), [])
    check("file-io: a variable mode is TEXT", scan_arms("open(p, m)\n"), ["file-io"])
    check("file-io: encoding in open()'s positional slot clears", scan_arms("open(p, 'r', -1, 'utf-8')\n"), [])
    check("file-io: .read_text() is named", scan_arms("p.read_text()\n"), ["file-io"])
    check("file-io: .read_text('utf-8') clears", scan_arms("p.read_text('utf-8')\n"), [])
    check("file-io: .write_text(data) is named", scan_arms("p.write_text(s)\n"), ["file-io"])
    check("file-io: .write_text(data, 'utf-8') clears", scan_arms("p.write_text(s, 'utf-8')\n"), [])
    check("file-io: Path(x).open() is named", scan_arms("Path(x).open()\n"), ["file-io"])
    check("file-io: (a / b).open('rb') clears", scan_arms("(a / b).open('rb')\n"), [])
    check("file-io: a Path VARIABLE's .open() is a documented miss", scan_arms("p.open()\n"), [])
    check("subprocess: text=True with no encoding is named",
          scan_arms("subprocess.run(a, text=True)\n"), ["subprocess"])
    check("subprocess: the same call with encoding= clears",
          scan_arms("subprocess.run(a, text=True, encoding='utf-8')\n"), [])
    check("subprocess: universal_newlines=True is named",
          scan_arms("subprocess.check_output(a, universal_newlines=True)\n"), ["subprocess"])
    check("subprocess: a bytes-mode call clears", scan_arms("subprocess.run(a, capture_output=True)\n"), [])
    check("subprocess: a call split across lines is still named",
          scan_arms("subprocess.run(\n    a,\n    text=True,\n)\n"), ["subprocess"])

    measured = {("a.py", "file-io"): 1}
    check("an undeclared measured site fails", len(check_registry(measured, {})), 1)
    check("a declared measured site passes", check_registry(measured, {("a.py", "file-io"): 1}), [])
    check("a stale row fails", len(check_registry({}, {("a.py", "subprocess"): 1})), 1)
    check("a count that no longer matches fails", len(check_registry(measured, {("a.py", "file-io"): 2})), 1)
    with tempfile.TemporaryDirectory() as scratch:
        reg = pathlib.Path(scratch) / "reg.txt"
        reg.write_text("# a comment\na.py\tfile-io\t1\tpredates the gate\n", encoding="utf-8")
        check("a well-formed row parses", read_registry(reg), ({("a.py", "file-io"): 1}, []))
        reg.write_text("a.py\t153\t1\tkeyed on a line number\n", encoding="utf-8")
        check("a line-numbered key is refused as malformed", len(read_registry(reg)[1]), 1)
        reg.write_text("a.py\tfile-io\t1\n", encoding="utf-8")
        check("a row with no reason is refused as malformed", len(read_registry(reg)[1]), 1)
        check("an absent argument resolves to an empty declaration", resolve_declaration(None), ({}, []))
        try:
            resolve_declaration(str(pathlib.Path(scratch) / "nosuch.txt"))
            refusal = "resolved"
        except OSError as exc:
            refusal = "named" if "nosuch.txt" in str(exc) else f"refused without naming it: {exc}"
        check("a supplied argument that does not resolve refuses, naming the path", refusal, "named")

    if n < FLOOR_ASSERTIONS:
        print(f"SELFTEST FAIL: {n} assertion(s) executed, under the floor of {FLOOR_ASSERTIONS}")
        ok = False
    print(f"PASS ({n} assertions)" if ok else f"encoding-posture selftest: RED ({n} assertions)")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return run_selftest()
    args = argv[1:]
    root = pathlib.Path(args[1] if len(args) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"encoding-posture: not a directory: {root}", file=sys.stderr)
        return 2
    try:
        declared, malformed = resolve_declaration(args[0] if args else None)
        hits, scanned = scan_tree(root, args[2:])
    except OSError as exc:
        print(f"encoding-posture: {exc}", file=sys.stderr)
        return 2
    if scanned == 0:
        print("encoding-posture: 0 tracked *.py graded under the root and pathspecs — a run over an "
              "empty population is not a pass", file=sys.stderr)
        return 1
    problems = malformed + check_registry(build_measured(hits), declared)
    if not problems:
        print(f"encoding-posture: OK — {scanned} tracked *.py graded, {sum(declared.values())} "
              f"declared site(s) in {len(declared)} row(s), no undeclared unencoded text-IO call")
        return 0
    print(f"encoding-posture: {len(problems)} finding(s) over {scanned} tracked *.py. Text IO with no "
          f"encoding= decodes with the platform default, which is cp1251/cp1252 on a Windows node.")
    for problem in problems:
        print(f"  {problem}")
    for rel, line, col, arm, what in hits:
        if (rel, arm) not in declared:
            print(f"  - [{arm}] {rel}:{line}:{col + 1} — {what} has no `encoding=`")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
