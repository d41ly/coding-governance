#!/usr/bin/env python3
"""Encoding-posture scan — tracked Python that does text IO without naming its encoding.

Project-agnostic. Run over any repo:

    python <this file> [registry-path] [root] [pathspec ...]   # exit 0 clean, 1 findings, 2 refusal
    python <this file> --stdout [registry-path] [root] [pathspec ...]   # the stdout arm, Python
    python <this file> --js [registry-path] [root] [pathspec ...]       # the JavaScript arm
    python <this file> --cleanup [registry-path] [root] [pathspec ...]  # the tree-removal arm, Python
    python <this file> [--stdout | --js | --cleanup] --measure [root] [pathspec ...]   # each key, its count
    python <this file> --selftest                               # prove every arm in BOTH directions

`--measure` grades nothing: it prints one `<path> TAB <arm> TAB <count>` line per measured key, the
rows a ledger seed writes, and exits 0, or 1 over an empty population.

THE STDOUT ARM, `--stdout` (TOOL-dWitnessedBar-24 S4). A tracked `*.py` holding a module-level
`if __name__ == "__main__":` block, that calls `print` or writes `sys.stdout`, and that holds neither
a `.reconfigure(...)` call naming `encoding` nor a reference to `sys.stdout.buffer`, is one site keyed
`<path>` `stdout`: its prints encode with the console's code page on a Windows node, and a non-ASCII
character raises `UnicodeEncodeError` there and nowhere else. WHAT IT DOES NOT CHECK: that the
reconfigure precedes the first print; a print reached through an imported module; which stream a
reconfigure names, so a reconfigure of stderr alone admits the file; and a print to stderr, which is
graded as a print.

THE JAVASCRIPT ARM, `--js` (TOOL-dWitnessedBar-24 S5). A call to `readFileSync`, `writeFileSync`,
`appendFileSync`, `spawnSync`, `execFileSync` or `execSync` whose argument list, read across lines
to its closing parenthesis, names neither `'utf8'`, `'utf-8'` nor an `encoding` key is one site keyed
`<path>` `js-io`. It reads TOKENS, not a syntax tree: strings and comments are masked so a name inside
either is no call, and an argument list's strings are read for the encoding. WHAT IT DOES NOT CHECK: a
call through an alias (`const r = fs.readFileSync; r(p)`), an encoding held in a variable, which is
graded as none, and a binary read that wants a Buffer, which is graded as a site and declared.

THE CLEANUP ARM, `--cleanup` (TOOL-dQuietDisk-9 S6). A call named `rmtree` with the keyword
`ignore_errors` set to a true constant, or `TemporaryDirectory` with `ignore_cleanup_errors` set to
one, read by AST and so across lines, is one site keyed `<path>` `cleanup`: git writes its objects
read-only, an unlink of one raises on Windows, and the swallowed error leaves the whole tree in the
temp folder. The remedy is the `remove_tree_py` block, `remove_tree` and `build_scratch_dir`, which
clear the bit and retry. WHAT IT DOES NOT CHECK: a keyword held in a variable or passed through
`**kwargs`, a call through an alias, and a plain `TemporaryDirectory()`, whose own cleanup already
resets permissions and retries; and whether a removal that is not swallowed is ever retried.

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

  * stdout encoding, in the default mode: the `--stdout` arm above grades it by shape, with its own
    limits, and neither mode knows the console a process will run under.
  * `p.open()` where `p` is a Path VARIABLE. Only a provably-Path receiver — `Path(x).open()` or
    `(a / b).open()` — is graded, because `Image.open` and `tokenize.open` reject an `encoding=`
    outright, and a fixer acting on a false report raises TypeError. A MISS, deliberately.
  * A mode held in a variable is graded as TEXT, the fail-closed direction: an unresolvable mode
    must not buy an exemption.
  * `io.open`, `codecs.open`, `subprocess` imported under another name, and a call through an alias
    (`run = subprocess.run`). Each is a MISS.

THE POPULATION is `git ls-files` under the root, restricted to `*.py` (`*.js` under `--js`) and to the optional pathspecs,
never a list somebody maintains: a scan that graded a hand-kept set goes quiet on the file that
arrives without being added to it. The clean line prints the graded file count, and an empty
population prints its zero and exits 1, because a green run over nothing reads as coverage.

THE REGISTRY is a shrink-only declaration of the sites that predate the gate, a ledger population
read through the factory (TOOL-dWitnessedBar-16): one row per
`<path>\t<arm>\t<count>\t<sha>\t<disposition>`, keyed on the ARM and never on a line number — a line-keyed
registry reds on unrelated edits, and a gate whose steady state is red gets bypassed. Set equality
in both directions: a measured site with no row fails, a row the scan no longer finds fails, and a
count may fall with its sites and may not rise. The argument is OPTIONAL: omitted, the run grades
against an empty declaration, which is the honest first reading of a tree nobody has graded; one
that was SUPPLIED and does not resolve is a typo and refuses.
"""
from __future__ import annotations

import ast
import pathlib
import re
import subprocess
import sys
import tempfile

# The baseline ledger factory, this kit's own inline copy (TOOL-dWitnessedBar-13 S9): the registry's
# rows are read by `read_rows` and graded by `compare_counts`, and the two adapters below keep this
# scanner's signatures, messages and four-field grammar.
from legacy_ledger import compare_counts, read_rows, render_malformed
from sh_hygiene import derive_default_registry  # the kit's one default-registry reader

ARMS = ("file-io", "subprocess")
STDOUT_ARMS = ("stdout",)
JS_ARMS = ("js-io",)
CLEANUP_ARMS = ("cleanup",)
# The removal calls that swallow their error, and the keyword that makes each swallow it.
CLEANUP_FLAGS = {"rmtree": "ignore_errors", "TemporaryDirectory": "ignore_cleanup_errors"}
# The JavaScript calls whose text decoding or encoding falls to a default when no encoding is named.
JS_IO_CALL = re.compile(r"\b(readFileSync|writeFileSync|appendFileSync|spawnSync|execFileSync|execSync)\s*\(")
JS_ENCODING = re.compile(r"""['"]utf-?8['"]|\bencoding\b""")
# method -> the positional slot its `encoding` argument occupies:
#   Path.read_text(encoding, errors) · Path.write_text(data, encoding, errors)
FILE_TEXT_METHODS = {"read_text": 0, "write_text": 1}
SUBPROCESS_FNS = {"run", "Popen", "call", "check_call", "check_output"}
TEXT_MODE_FLAGS = ("text", "universal_newlines")

#: The executed-assertion floor for `--selftest`, compared against the count it prints. Raise it
#: with the arms; it may never be lowered to fit a regression.
#: RAISED 26 -> 41 by TOOL-dWitnessedBar-24: seven stdout rows, six JavaScript rows and the two
#: per-mode arm-set rows, 15 executed, every one unconditional.
#: RAISED 41 -> 49 by TOOL-dQuietDisk-9: six cleanup rows, the cleanup arm set's registry row and the
#: fixture tree's row, 8 executed, every one unconditional.
#: RAISED 49 -> 50 on the merge with TOOL-aFlattenedSeed-3's default-home row.
#: RAISED 50 -> 51 on the merge with TOOL-aFlattenedSeed-4's row.
FLOOR_ASSERTIONS = 51


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


def check_main_guard(node: ast.stmt) -> bool:
    """True for a module-level `if __name__ == "__main__":`, either operand order."""
    if not (isinstance(node, ast.If) and isinstance(node.test, ast.Compare) and len(node.test.ops) == 1
            and isinstance(node.test.ops[0], ast.Eq)):
        return False
    sides = [node.test.left, node.test.comparators[0]]
    return (any(isinstance(s, ast.Name) and s.id == "__name__" for s in sides)
            and any(isinstance(s, ast.Constant) and s.value == "__main__" for s in sides))


def check_sys_stdout(node: ast.AST) -> bool:
    """True for the expression `sys.stdout`."""
    return (isinstance(node, ast.Attribute) and node.attr == "stdout" and isinstance(node.value, ast.Name)
            and node.value.id == "sys")


def scan_stdout(tree: ast.AST) -> list[tuple[int, int, str, str]]:
    """The one `stdout` site of an entry point that prints with no UTF-8 stdout, or nothing (S4)."""
    if not any(check_main_guard(node) for node in getattr(tree, "body", [])):
        return []
    first = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr == "buffer" and check_sys_stdout(node.value):
            return []
        if not isinstance(node, ast.Call):
            continue
        if isinstance(node.func, ast.Attribute) and node.func.attr == "reconfigure" \
                and read_kwarg(node, "encoding") is not None:
            return []
        prints = isinstance(node.func, ast.Name) and node.func.id == "print"
        writes = (isinstance(node.func, ast.Attribute) and node.func.attr in ("write", "writelines")
                  and check_sys_stdout(node.func.value))
        if (prints or writes) and (first is None or (node.lineno, node.col_offset) < first[:2]):
            first = (node.lineno, node.col_offset, "print(...)" if prints else "sys.stdout.write(...)")
    if first is None:
        return []
    return [(first[0], first[1], "stdout", f"{first[2]} in an entry point")]


JS_CODE, JS_STRING, JS_COMMENT = 0, 1, 2


def read_js_regions(text: str) -> list[int]:
    """One region per character of JavaScript source: JS_CODE, JS_STRING (a string or a template) or
    JS_COMMENT. A regex literal is read as code, so one holding a quote can mis-read what follows it."""
    regions = [JS_CODE] * len(text)
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if text.startswith("//", i):
            end, kind = text.find("\n", i), JS_COMMENT
            end = n if end < 0 else end
        elif text.startswith("/*", i):
            end, kind = text.find("*/", i + 2), JS_COMMENT
            end = n if end < 0 else end + 2
        elif c in "'\"`":
            end, kind = i + 1, JS_STRING
            while end < n and text[end] != c and (c == "`" or text[end] != "\n"):
                end += 2 if text[end] == "\\" else 1
            end = min(end + 1, n)
        else:
            i += 1
            continue
        regions[i:end] = [kind] * (end - i)
        i = end
    return regions


def scan_js_io(text: str) -> list[tuple[int, int, str, str]]:
    """(line, col, `js-io`, description) for every JavaScript text IO call naming no encoding (S5)."""
    regions = read_js_regions(text)
    found = []
    for m in JS_IO_CALL.finditer(text):
        if regions[m.start()] != JS_CODE:
            continue
        depth, k = 0, m.end() - 1
        while k < len(text):
            if regions[k] == JS_CODE:
                depth += {"(": 1, ")": -1}.get(text[k], 0)
                if depth == 0:
                    break
            k += 1
        args = "".join(ch for ch, kind in zip(text[m.end():k], regions[m.end():k]) if kind != JS_COMMENT)
        if not JS_ENCODING.search(args):
            line = text.count("\n", 0, m.start()) + 1
            col = m.start() - (text.rfind("\n", 0, m.start()) + 1)
            found.append((line, col, "js-io", f"{m.group(1)}(...)"))
    return found


def scan_python_text_io(text: str) -> list[tuple[int, int, str, str]]:
    return scan_text_io(ast.parse(text))


def scan_python_stdout(text: str) -> list[tuple[int, int, str, str]]:
    return scan_stdout(ast.parse(text))


def scan_python_cleanup(text: str) -> list[tuple[int, int, str, str]]:
    """(line, col, `cleanup`, description) for every tree removal that swallows its error (S6)."""
    found = []
    for node in ast.walk(ast.parse(text)):
        if not isinstance(node, ast.Call):
            continue
        func = node.func
        name = func.attr if isinstance(func, ast.Attribute) else func.id if isinstance(func, ast.Name) else ""
        flag = CLEANUP_FLAGS.get(name)
        value = read_kwarg(node, flag) if flag else None
        if isinstance(value, ast.Constant) and bool(value.value):
            found.append((node.lineno, node.col_offset, "cleanup", f"{name}(..., {flag}=True)"))
    return found


# Each mode: (the population's suffix, the per-file scan over its text, the registry's closed arm set).
#: Each mode's ledger home under `<MEMORY_ROOT>/project/`, read when no registry argument is given.
DEFAULT_HOMES = {"": "encoding-posture-sites.txt", "--stdout": "encoding-stdout-sites.txt",
                 "--js": "encoding-js-sites.txt", "--cleanup": "cleanup-sites.txt"}
MODES = {
    "": (".py", scan_python_text_io, ARMS),
    "--stdout": (".py", scan_python_stdout, STDOUT_ARMS),
    "--js": (".js", scan_js_io, JS_ARMS),
    "--cleanup": (".py", scan_python_cleanup, CLEANUP_ARMS),
}


def scan_tree(root: pathlib.Path, pathspecs: list[str], mode: str = ""
              ) -> tuple[list[tuple[str, int, int, str, str]], int]:
    """Every tracked file of `mode`'s suffix under `root` and the pathspecs, scanned by the mode's scan.
    Returns (hits, files scanned).

    Raises OSError on a dead probe or an unparseable file: both are refusals, never a zero.
    """
    suffix, scan, _arms = MODES[mode]
    listing = subprocess.run(
        ["git", "ls-files", "-z", "--", *(pathspecs or ["."])],
        cwd=str(root), capture_output=True, text=True, encoding="utf-8")
    if listing.returncode != 0:
        # A DEAD PROBE must not be spelled the way an empty tree is: both yield zero files.
        raise OSError("git ls-files failed, so the population could not be derived at all: "
                      + (listing.stderr or "").strip())
    hits: list[tuple[str, int, int, str, str]] = []
    scanned = 0
    for rel in sorted(p for p in listing.stdout.split("\0") if p.endswith(suffix)):
        full = root / rel
        if not full.is_file():
            continue
        try:
            found = scan(full.read_bytes().decode("utf-8"))
        except (SyntaxError, UnicodeDecodeError, ValueError) as exc:
            raise OSError(f"{rel}: cannot be parsed, so it cannot be graded: {exc}") from exc
        scanned += 1
        hits.extend((rel, line, col, arm, what) for line, col, arm, what in found)
    return hits, scanned


def build_measured(hits: list[tuple[str, int, int, str, str]]) -> dict[tuple[str, str], int]:
    """The hits as `{(path, arm): count}` — the registry's own key."""
    measured: dict[tuple[str, str], int] = {}
    for rel, _line, _col, arm, _what in hits:
        measured[(rel, arm)] = measured.get((rel, arm), 0) + 1
    return measured


def resolve_declaration(arg: str | None, arms: tuple = ARMS) -> tuple[dict[tuple[str, str], int], list[str]]:
    """The declared sites for the OPTIONAL registry argument, plus every malformed row; a supplied path
    that does not resolve raises.

    THE REGISTRY IS A LEDGER POPULATION (TOOL-dWitnessedBar-16 S4), read through the factory's
    `read_rows`: `path TAB arm TAB count TAB sha TAB disposition`, a row's reason the conversion
    record's or its widen record's. The factory's line-number refusal is skipped on both key fields,
    because the closed arm set is the stricter test here and the one whose words this registry has
    always printed; each line the factory read or refused is graded in line order, the arm first.
    """
    if arg is None:
        return {}, []
    path = pathlib.Path(arg)
    if not path.is_file():
        raise OSError(f"no registry at {path} — the argument was SUPPLIED and does not resolve to a "
                      f"file, which is a typo and not a posture; OMIT it to grade against an empty "
                      f"declaration")
    rows, refused = read_rows(path, 2, verbatim=(0, 1))
    graded = sorted([(number, None, row) for _count, _tail, number, row in rows.values()] + refused)
    declared: dict[tuple[str, str], int] = {}
    malformed: list[str] = []
    for number, kind, row in graded:
        if kind == "fields":
            malformed.append(f"line {number}: not <path> TAB <arm> TAB <count> TAB <sha> TAB <disposition>: {row}")
            continue
        fields = row.split("\t")
        rel, arm = fields[0].strip(), fields[1].strip()
        if arm not in arms:
            malformed.append(f"line {number}: {arm!r} is not an arm ({', '.join(arms)}) — the key is "
                             f"the ARM, never a line number, because a line number moves on an "
                             f"unrelated edit: {row}")
        elif kind == "duplicate":
            malformed.append(f"line {number}: ({rel}, {arm}) is declared twice: {row}")
        elif kind is not None:
            malformed.append(render_malformed((number, kind, row)))
        else:
            declared[(rel, arm)] = rows[(rel, arm)][0]
    return declared, malformed


def check_registry(measured: dict[tuple[str, str], int],
                   declared: dict[tuple[str, str], int]) -> list[str]:
    """Set equality in both directions, with the counts. Returns one line per violation.

    A thin adapter over the factory's `compare_counts` (TOOL-dWitnessedBar-13 S9); `shrink-only`
    reports a count that fell as well as one that rose, so the equality is unchanged.
    """
    problems = []
    for finding, key, have, want in compare_counts(measured, declared, "shrink-only"):
        rel, arm = key
        if finding == "undeclared site" and arm == "cleanup":
            problems.append(f"{rel}: {have} tree removal(s) that swallow their error [{arm}] and no registry "
                            f"row declares them — call remove_tree, the remove_tree_py block")
        elif finding == "undeclared site":
            fix = "make stdout UTF-8 before the first print" if arm == "stdout" else "pass encoding=\"utf-8\""
            problems.append(f"{rel}: {have} unencoded [{arm}] call(s) and no registry row declares "
                            f"them — {fix}")
        elif finding == "unmeasured row":
            problems.append(f"{rel}: the registry declares [{arm}] and the scan no longer finds it — "
                            f"delete the row, or a drained site leaves a widened exemption behind")
        else:
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

    # THE STDOUT ARM (S4): the planted entry point, and each of its two admissions.
    def scan_stdout_arms(source: str) -> list[str]:
        return [arm for _l, _c, arm, _w in scan_stdout(ast.parse(source))]

    entry = 'if __name__ == "__main__":\n    print("\\u00e9")\n'
    check("stdout: an entry point that prints with no reconfigure is named", scan_stdout_arms(entry), ["stdout"])
    check("stdout: a reconfigure naming encoding before the print clears",
          scan_stdout_arms('import sys\nsys.stdout.reconfigure(encoding="utf-8")\n' + entry), [])
    check("stdout: a write to sys.stdout.buffer clears",
          scan_stdout_arms('import sys\nif __name__ == "__main__":\n    sys.stdout.buffer.write(b"x")\n'), [])
    check("stdout: a reconfigure with no encoding does not clear",
          scan_stdout_arms('import sys\nsys.stdout.reconfigure(newline="\\n")\n' + entry), ["stdout"])
    check("stdout: sys.stdout.write in an entry point is named",
          scan_stdout_arms('import sys\nif __name__ == "__main__":\n    sys.stdout.write("x")\n'), ["stdout"])
    check("stdout: a module with no entry point is not one", scan_stdout_arms('print("x")\n'), [])
    check("stdout: a file is one site however many prints it holds",
          scan_stdout_arms(entry + 'print(1)\nprint(2)\n'), ["stdout"])

    # THE JAVASCRIPT ARM (S5): read across lines to the closing parenthesis, strings and comments masked.
    def scan_js_arms(source: str) -> list[str]:
        return [arm for _l, _c, arm, _w in scan_js_io(source)]

    check("js: a read split across two lines is named", scan_js_arms("fs.readFileSync(\n  p)\n"), ["js-io"])
    check("js: the same split read with 'utf8' clears", scan_js_arms("fs.readFileSync(\n  p, 'utf8')\n"), [])
    check("js: an encoding key clears", scan_js_arms("spawnSync(c, a, { encoding: 'utf-8' })\n"), [])
    check("js: a nested call's parentheses do not end the argument list",
          scan_js_arms("execSync(cmd(a), {\n  stdio: 'pipe' })\n"), ["js-io"])
    check("js: a call named inside a string or a comment is no call",
          scan_js_arms("const s = 'readFileSync(p)';\n// writeFileSync(p, d)\n"), [])
    check("js: 'utf8' in a comment inside the call does not clear it",
          scan_js_arms("writeFileSync(p, d /* 'utf8' */)\n"), ["js-io"])

    # THE CLEANUP ARM (TOOL-dQuietDisk-9 S6): each swallowing form, read across lines, and its twin.
    def scan_cleanup_arms(source: str) -> list[str]:
        return [arm for _l, _c, arm, _w in scan_python_cleanup(source)]

    check("cleanup: a swallowing rmtree split over two lines is named",
          scan_cleanup_arms("shutil.rmtree(p,\n              ignore_errors=True)\n"), ["cleanup"])
    check("cleanup: an rmtree that raises its error clears", scan_cleanup_arms("shutil.rmtree(p)\n"), [])
    check("cleanup: ignore_errors=False clears", scan_cleanup_arms("shutil.rmtree(p, ignore_errors=False)\n"), [])
    check("cleanup: a bare rmtree name is named", scan_cleanup_arms("rmtree(p, ignore_errors=True)\n"), ["cleanup"])
    check("cleanup: TemporaryDirectory with ignore_cleanup_errors is named",
          scan_cleanup_arms("tempfile.TemporaryDirectory(\n    prefix='x', ignore_cleanup_errors=True)\n"), ["cleanup"])
    check("cleanup: a plain TemporaryDirectory clears", scan_cleanup_arms("tempfile.TemporaryDirectory()\n"), [])

    measured = {("a.py", "file-io"): 1}
    check("an undeclared measured site fails", len(check_registry(measured, {})), 1)
    check("a declared measured site passes", check_registry(measured, {("a.py", "file-io"): 1}), [])
    check("a stale row fails", len(check_registry({}, {("a.py", "subprocess"): 1})), 1)
    check("a count that no longer matches fails", len(check_registry(measured, {("a.py", "file-io"): 2})), 1)
    with tempfile.TemporaryDirectory() as scratch:
        reg = pathlib.Path(scratch) / "reg.txt"
        reg.write_text("# a comment\na.py\tfile-io\t1\tabcdef12\tseeded\n", encoding="utf-8")
        check("a well-formed row parses", resolve_declaration(str(reg)), ({("a.py", "file-io"): 1}, []))
        reg.write_text("a.py\t153\t1\tabcdef12\tseeded\n", encoding="utf-8")
        check("a line-numbered key is refused as malformed", len(resolve_declaration(str(reg))[1]), 1)
        reg.write_text("a.py\tfile-io\t1\n", encoding="utf-8")
        check("a row with no sha and disposition is refused as malformed", len(resolve_declaration(str(reg))[1]), 1)
        check("an absent argument resolves to an empty declaration", resolve_declaration(None), ({}, []))
        try:
            resolve_declaration(str(pathlib.Path(scratch) / "nosuch.txt"))
            refusal = "resolved"
        except OSError as exc:
            refusal = "named" if "nosuch.txt" in str(exc) else f"refused without naming it: {exc}"
        check("a supplied argument that does not resolve refuses, naming the path", refusal, "named")
        reg.write_text("a.py\tstdout\t1\tabcdef12\tseeded\n", encoding="utf-8")
        check("a mode's own arm set grades its registry", resolve_declaration(str(reg), STDOUT_ARMS),
              ({("a.py", "stdout"): 1}, []))
        check("another mode's arm is malformed there", len(resolve_declaration(str(reg))[1]), 1)
        reg.write_text("a.py\tcleanup\t1\tabcdef12\twidened:2026-01-01-build-TOOL-dFix-1-widen-1\n", encoding="utf-8")
        check("the cleanup arm set grades its registry", resolve_declaration(str(reg), CLEANUP_ARMS),
              ({("a.py", "cleanup"): 1}, []))
        # The two planted forms staged in a fixture tree, through the mode's own population walk.
        tree = pathlib.Path(scratch) / "cleanup-tree"
        tree.mkdir()
        (tree / "a.py").write_text("import shutil, tempfile\nshutil.rmtree(p,\n              ignore_errors=True)\n"
                                   "tempfile.TemporaryDirectory(ignore_cleanup_errors=True)\n", encoding="utf-8")
        (tree / "b.py").write_text("import shutil\nshutil.rmtree(p)\n", encoding="utf-8")
        staged = subprocess.run(["git", "init", "-q", str(tree)], capture_output=True, check=False).returncode == 0 \
            and subprocess.run(["git", "-C", str(tree), "add", "a.py", "b.py"], capture_output=True,
                               check=False).returncode == 0
        got = build_measured(scan_tree(tree, [], "--cleanup")[0]) if staged else "the fixture tree did not stage"
        check("cleanup: the fixture tree's two planted removals are measured, the raising one is not",
              got, {("a.py", "cleanup"): 2})
        # TOOL-aFlattenedSeed-3: an adopter's row names no registry, so the run reads the mode's home under
        # <MEMORY_ROOT>/project/ and a seeded site is declared there, not undeclared.
        import os  # noqa: PLC0415  the one arm that runs from a planted root
        tree = pathlib.Path(scratch) / "tree"
        (tree / "records" / "project").mkdir(parents=True)
        (tree / "a.py").write_text('open("x")\n', encoding="utf-8")
        (tree / ".memory-tree.conf").write_text("MEMORY_ROOT=records\n", encoding="utf-8")
        (tree / "records" / "project" / "encoding-posture-sites.txt").write_text(
            "a.py\tfile-io\t1\tabcdef12\tseeded\n", encoding="utf-8")
        for argv in (["git", "init", "-q", "."], ["git", "add", "-A"]):
            subprocess.run(argv, cwd=str(tree), capture_output=True, check=True)
        here = os.getcwd()
        os.chdir(tree)
        try:
            check("no registry argument reads <MEMORY_ROOT>/project/encoding-posture-sites.txt",
                  main(["encoding_posture.py"]), 0)
            (tree / "records" / "b.py").write_text('open("y")\n', encoding="utf-8")  # a frozen record's site
            subprocess.run(["git", "add", "-A"], cwd=str(tree), capture_output=True, check=True)
            # TOOL-aFlattenedSeed-4: an empty registry argument is the home too, so an adopter's row can
            # pass a population after it; the memory root's own site sits outside that population.
            check("an empty registry argument reads the home over the pathspecs after it",
                  main(["encoding_posture.py", "", ".", ":!records"]), 0)
        finally:
            os.chdir(here)

    if n < FLOOR_ASSERTIONS:
        print(f"SELFTEST FAIL: {n} assertion(s) executed, under the floor of {FLOOR_ASSERTIONS}")
        ok = False
    print(f"PASS ({n} assertions)" if ok else f"encoding-posture selftest: RED ({n} assertions)")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        return run_selftest()
    mode = next((flag for flag in MODES if flag and flag in argv), "")
    measure = "--measure" in argv
    # The default mode's flag is "", so an empty registry argument is never taken for it (TOOL-aFlattenedSeed-4).
    args = [arg for arg in argv[1:] if arg != "--measure" and (not mode or arg != mode)]
    if measure:
        args = [None, *args]  # `--measure` reads no registry: its positionals open at the root
    suffix, _scan, arms = MODES[mode]
    root = pathlib.Path(args[1] if len(args) > 1 else ".").resolve()
    if not root.is_dir():
        print(f"encoding-posture: not a directory: {root}", file=sys.stderr)
        return 2
    try:
        # TOOL-aFlattenedSeed-3: no registry argument reads the population's home, as an adopter's row names none.
        # TOOL-aFlattenedSeed-4: an empty one too, so a row can name the population after it.
        default = None if measure or (args and args[0]) else derive_default_registry(root, DEFAULT_HOMES[mode])
        declared, malformed = resolve_declaration(args[0] if args and args[0] else default, arms)
        hits, scanned = scan_tree(root, args[2:], mode)
    except OSError as exc:
        print(f"encoding-posture: {exc}", file=sys.stderr)
        return 2
    if scanned == 0:
        print(f"encoding-posture: 0 tracked *{suffix} graded under the root and pathspecs — a run over an "
              "empty population is not a pass", file=sys.stderr)
        return 1
    measured = build_measured(hits)
    if measure:
        for (rel, arm), count in sorted(measured.items()):
            print(f"{rel}\t{arm}\t{count}")
        return 0
    problems = malformed + check_registry(measured, declared)
    if not problems:
        print(f"encoding-posture: OK — {scanned} tracked *{suffix} graded, {sum(declared.values())} "
              f"declared site(s) in {len(declared)} row(s), no undeclared {'/'.join(arms)} site")
        return 0
    if mode == "--cleanup":
        print(f"encoding-posture: {len(problems)} finding(s) over {scanned} tracked *{suffix}. A tree removal "
              f"that swallows its error leaves git's read-only objects in the temp folder on Windows: call "
              f"remove_tree, the remove_tree_py block, which clears the bit and retries.")
    else:
        remedy = ("call sys.stdout.reconfigure(encoding=\"utf-8\") before the first print" if mode == "--stdout"
                  else "name the encoding")
        print(f"encoding-posture: {len(problems)} finding(s) over {scanned} tracked *{suffix}. Text IO with no "
              f"named encoding uses the platform default, which is cp1251/cp1252 on a Windows node: {remedy}.")
    for problem in problems:
        print(f"  {problem}")
    for rel, line, col, arm, what in hits:
        if (rel, arm) not in declared:
            print(f"  - [{arm}] {rel}:{line}:{col + 1} — {what} "
                  f"{'swallows its error' if arm == 'cleanup' else 'names no encoding'}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
