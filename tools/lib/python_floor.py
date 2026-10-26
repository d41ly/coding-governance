"""python_floor — the interpreter floor: its one declaration, the query for every statement of it,
the copies' check, and the floor step's down (TOOL-dSafePassage-11).

    python <prefix>/lib/python_floor.py check [--rev <sha>]    # every floor statement and copy finding
    python <prefix>/lib/python_floor.py down <prior> <target>  # the step's down: grade, then restore

THE DECLARATION is `python-floor.txt` beside this file, one `<major>.<minor>` line. Every other
spelling of the floor is one of two kinds. A GENERATED COPY is the resolver block's `_rp_floor`
literal, carried inline by every copy of the block because a copy-installed kit has no lib dir to
read; `check_floor_copies` holds each to the declaration, and the resolver self-test's parity rows
hold the copies to each other. A POINTER is prose naming `python-floor.txt` and spelling no version.

THE QUERY. `scan_floor_statements` runs FLOOR_STATEMENT_RX over the tracked files outside `memory/`,
so it finds a statement whatever version it names; on gov's tree after the raise it finds none.

THE DOWN. `check_down_floor` grades every tracked `.py` and `.toml` of a target under the floor it
restores: by a real interpreter at that floor where `resolve_floor_interpreter` finds one, mode
`interpreter <path>`; elsewhere, mode `static`, by `ast.parse` at that floor's feature version, the
four PEP 701 shapes over the tokens, the running `tomllib`, and the four TOML 1.1 deltas. WHAT THE
STATIC MODE DOES NOT SEE: every other grammar change after the restored floor that `feature_version`
does not model (deviation-31). The down executes no target code; a finding writes nothing.

A LATER RAISE copies this unit: `write_floor` the new value, a `lib/python-floor-<X.Y>` step row whose
down names the floor it replaces, and every statement the query finds rewritten as a pointer.
"""
import ast
import io
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tokenize

HERE = pathlib.Path(__file__).absolute().parent
DECLARATION = "python-floor.txt"
FLOOR_LITERAL = re.compile(r'^(\s*_rp_floor=")([^"]*)("\s*)$', re.M)
FLOOR_VALUE = re.compile(r"(\d+)\.(\d+)")
# PINNED on 2026-10-23 at a255d0de, where it finds the six statements of the raise and no other line.
FLOOR_STATEMENT_RX = re.compile(r"""(?ix)
  \b(?:c?python|py)\s*(?:>=|≥|=>)\s*\d+\.\d+
| \bc?python\s*\d+\.\d+\s*(?:\+|or\s+(?:newer|later|above))
| \bat\s+least\s+c?python\s*\d+\.\d+
| \bpython-version\s*:\s*["']?\d+\.\d+
| \brequires-python\b
""")
PARITY_GREP = ["grep", "-l", "^# >>> resolve_python", "--", "*.sh", "*.py", ".githooks/*",
               "WIRE-INTO-PROJECT.md"]
DEFINITION = re.compile(r"^\s*(?:function\s+)?resolve_python\s*\(\)")


def run_git(root, *args):
    """git's stdout in `root`, or "" where git exits non-zero (a grep with no hit among them)."""
    p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, encoding="utf-8",
                       errors="replace")
    return p.stdout if p.returncode == 0 else ""


def derive_lib_rel():
    """This file's directory as a path from its repository's top, `/`-separated: where the
    declaration sits in gov's source tree and in any clone of it."""
    top = next((d for d in (HERE, *HERE.parents) if (d / ".git").exists()), HERE)
    return HERE.relative_to(top).as_posix()


def read_floor(root):
    """The declaration under `root` as (major, minor). Any content but `<major>.<minor>` and one
    optional newline is a ValueError naming the file; a CRLF checkout reads as its one newline."""
    path = pathlib.Path(root) / derive_lib_rel() / DECLARATION
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"{path.as_posix()}: the floor declaration is unreadable: {exc}") from None
    m = FLOOR_VALUE.fullmatch(text.removesuffix("\n"))
    if not m:
        raise ValueError(f"{path.as_posix()}: the floor declaration must be one <major>.<minor> line, "
                         f"and it reads {text!r}")
    return int(m[1]), int(m[2])


def read_parity_population(root):
    """Every tracked file carrying the resolver block's marker, the canonical included, derived by
    the parity rows' own grep and never listed."""
    return [p for p in run_git(root, *PARITY_GREP).splitlines() if p]


def scan_floor_statements(root, rev=None):
    """[(path, line, text)] for every line of a tracked file outside `memory/` that
    FLOOR_STATEMENT_RX matches, read at `rev` through `git grep <rev>` when given. git narrows the
    population to lines holding `py`, which every alternative of the pattern spells."""
    args = ["grep", "-I", "-n", "-i", "--null", "-F", "-e", "py", *([rev] if rev else []),
            "--", ".", ":(exclude)memory/"]
    found = []
    for row in filter(None, run_git(root, *args).split("\n")):
        path, line, text = row.split("\0", 2)
        if rev and path.startswith(f"{rev}:"):
            path = path[len(rev) + 1:]
        if FLOOR_STATEMENT_RX.search(text):
            found.append((path, int(line), text.strip()))
    return found


def check_floor_copies(root):
    """[(path, line, text)]: each file of the parity population whose `_rp_floor` literal differs
    from the declaration, or that carries none, and each multi-line `resolve_python` definition in
    a tracked shell, Python or hook file that sits outside a marked block."""
    want = "%d.%d" % read_floor(root)
    root = pathlib.Path(root)
    found = []
    for rel in read_parity_population(root):
        text = (root / rel).read_text(encoding="utf-8", errors="replace")
        lits = [(text.count("\n", 0, m.start()) + 1, m[2]) for m in FLOOR_LITERAL.finditer(text)]
        if not lits:
            found.append((rel, 0, f"carries the resolver block and no _rp_floor literal; the floor is {want}"))
        for line, got in lits:
            if got != want:
                found.append((rel, line, f'_rp_floor="{got}" differs from the declaration {want}'))
    hits = run_git(root, "grep", "-l", "-E", r"^[[:space:]]*(function[[:space:]]+)?resolve_python[[:space:]]*\(\)",
                   "--", "*.sh", "*.py", ".githooks/*", "WIRE-INTO-PROJECT.md")
    for rel in filter(None, hits.splitlines()):
        inside = False
        lines = (root / rel).read_text(encoding="utf-8", errors="replace").splitlines()
        for n, ln in enumerate(lines, 1):
            if ln.startswith("# >>> resolve_python"):
                inside = True
            elif ln.startswith("# <<< resolve_python"):
                inside = False
            elif DEFINITION.match(ln) and not inside and "}" not in ln.partition("{")[2]:
                found.append((rel, n, "an unmarked multi-line definition of resolve_python, which no parity row grades"))
    return found


def resolve_floor_interpreter(version):
    """The executable of the first of `python<X.Y>`, `py -<X.Y>` and `uv python find <X.Y>` (the last
    only when uv runs) whose isolated probe reports exactly `version`, or None."""
    cands = []
    if shutil.which(f"python{version}"):
        cands.append([shutil.which(f"python{version}")])
    if shutil.which("py"):
        cands.append(["py", f"-{version}"])
    if shutil.which("uv"):
        try:
            p = subprocess.run(["uv", "python", "find", version], capture_output=True, text=True, timeout=60)
            if p.returncode == 0 and p.stdout.strip():
                cands.append([p.stdout.strip()])
        except (OSError, subprocess.TimeoutExpired):
            pass
    probe = "import sys; print('%d.%d' % sys.version_info[:2]); print(sys.executable)"
    for argv in cands:
        try:
            p = subprocess.run([*argv, "-I", "-c", probe], capture_output=True, text=True, timeout=60)
        except (OSError, subprocess.TimeoutExpired):
            continue
        out = p.stdout.split()
        if p.returncode == 0 and len(out) >= 2 and out[0] == version:
            return p.stdout.splitlines()[1].strip()
    return None


# The interpreter mode's one child, run -I at the restored floor over the paths on stdin.
CHILD = r"""
import json, re, sys
try:
    import tomllib
except ImportError:
    tomllib = None
for p in json.load(sys.stdin):
    try:
        with open(p, "rb") as f:
            data = f.read()
        if p.endswith(".py"):
            compile(data, p, "exec", dont_inherit=True)
        elif tomllib is not None:
            tomllib.loads(data.decode("utf-8"))
    except SyntaxError as e:
        print("%s:%s: %s" % (p, e.lineno or 0, e.msg))
    except Exception as e:
        m = re.search(r"line (\d+)", str(e))
        print("%s:%s: %s" % (p, m.group(1) if m else 0, str(e).splitlines()[0] if str(e) else type(e).__name__))
"""


def _scan_pep701(data):
    """[(line, what)] for the four PEP 701 shapes in a .py file's tokens, each a replacement field
    the restored floor's tokenizer refuses: a string reusing an enclosing f-string's quote, a
    backslash, a `#`, and a line break in a single-quoted f-string's field."""
    starts = {tokenize.FSTRING_START, getattr(tokenize, "TSTRING_START", tokenize.FSTRING_START)}
    ends = {tokenize.FSTRING_END, getattr(tokenize, "TSTRING_END", tokenize.FSTRING_END)}
    stack, found = [], []  # each open f-string: [quote, brace depth, start row]

    def note(row, what):
        if (row, what) not in found:
            found.append((row, what))

    def quote_of(s):
        s = s.lstrip("rRbBfFtTuU")
        return s[:3] if s[:3] in ('"""', "'''") else s[:1]

    try:
        for tok in tokenize.tokenize(io.BytesIO(data).readline):
            # The f-strings whose replacement field holds this token: every enclosing one, and the
            # innermost only while its brace depth is open.
            fields = stack[:-1] + ([stack[-1]] if stack and stack[-1][1] > 0 else [])
            if fields:
                if tok.type in starts or tok.type == tokenize.STRING:
                    q = quote_of(tok.string)
                    if any(q[:1] == f[0][:1] and len(q) >= len(f[0]) for f in fields):
                        note(tok.start[0], "a string in a replacement field reuses the enclosing f-string's quote")
                if tok.type in (tokenize.STRING, tokenize.FSTRING_MIDDLE) and "\\" in tok.string:
                    note(tok.start[0], "a backslash in a replacement field")
                if tok.type == tokenize.COMMENT or (tok.type in (tokenize.STRING, tokenize.FSTRING_MIDDLE) and "#" in tok.string):
                    note(tok.start[0], "a # in a replacement field")
                if any(len(f[0]) == 1 and tok.end[0] > f[2] for f in fields):
                    note(tok.start[0], "a line break in a single-quoted f-string's replacement field")
            if tok.type in starts:
                stack.append([quote_of(tok.string), 0, tok.start[0]])
            elif tok.type in ends and stack:
                stack.pop()
            elif stack and tok.type == tokenize.OP and tok.string in "{}":
                stack[-1][1] += 1 if tok.string == "{" else -1
    except (tokenize.TokenError, SyntaxError):
        pass  # ast.parse names a file the tokenizer cannot read
    return found


def _scan_toml11(text):
    """[(line, what)] for the four TOML 1.1 deltas the running tomllib accepts and TOML 1.0 refuses:
    a line break or a trailing comma inside an inline table, a `\\e` or `\\xHH` escape in a basic
    string, and a time without seconds."""
    found, stack, code = [], [], {}
    i, n, line, bol, last = 0, len(text), 1, True, ""
    while i < n:
        c = text[i]
        if c == "\n":
            if stack and stack[-1] == "{":
                found.append((line, "a line break inside an inline table"))
            line, bol, i = line + 1, True, i + 1
            continue
        if c in " \t\r":
            i += 1
            continue
        if c == "#":
            while i < n and text[i] != "\n":
                i += 1
            continue
        if bol and not stack and c == "[":  # a table header
            while i < n and text[i] != "\n":
                i += 1
            continue
        bol = False
        if c in "\"'":
            q = c * 3 if text.startswith(c * 3, i) else c
            j = i + len(q)
            while j < n and not text.startswith(q, j):
                if text[j] == "\n":
                    line += 1
                if text[j] == "\\" and c == '"':
                    nxt = text[j + 1:j + 2]
                    if nxt in ("e", "x"):
                        found.append((line, f"a \\{nxt} escape"))
                    if nxt == "\n":
                        line += 1
                    j += 2
                    continue
                j += 1
            i, last = j + len(q), "v"
            continue
        if c in "[{":
            stack.append(c)
        elif c in "]}":
            if c == "}" and last == ",":
                found.append((line, "a trailing comma inside an inline table"))
            if stack:
                stack.pop()
        code.setdefault(line, []).append(c)
        last = c
        i += 1
    for ln, chars in code.items():
        if re.search(r"(?<![\d:+\-])\d{2}:\d{2}(?![:\d])", "".join(chars)):
            found.append((ln, "a time without seconds"))
    return sorted(found)


def check_down_floor(target, prior):
    """(mode, findings) for the down to the floor `prior`, "<major>.<minor>": every tracked `.py`
    and `.toml` of `target` graded by a real interpreter at that floor where one resolves, mode
    `interpreter <path>`, else statically, mode `static`. Each finding is `path:line: what`."""
    m = FLOOR_VALUE.fullmatch(prior)
    if not m:
        raise ValueError(f"the prior floor must be <major>.<minor>, not {prior!r}")
    target = pathlib.Path(target)
    files = [p for p in run_git(target, "ls-files", "-z").split("\0") if p.endswith((".py", ".toml"))]
    interp = resolve_floor_interpreter(prior)
    if interp:
        p = subprocess.run([interp, "-I", "-c", CHILD], input=json.dumps(files), capture_output=True,
                           text=True, encoding="utf-8", errors="replace", cwd=target)
        found = [ln for ln in p.stdout.splitlines() if ln.strip()]
        if p.returncode != 0:
            found.append(f"(interpreter {interp} exited {p.returncode}: {p.stderr.strip()[-300:]})")
        return f"interpreter {interp}", found
    feature = (int(m[1]), int(m[2]))
    found = []
    for rel in files:
        try:
            data = (target / rel).read_bytes()
        except OSError as exc:
            found.append(f"{rel}:0: unreadable: {exc}")
            continue
        if rel.endswith(".py"):
            try:
                ast.parse(data, rel, feature_version=feature)
            except SyntaxError as e:
                found.append(f"{rel}:{e.lineno or 0}: {e.msg}")
                continue
            found += [f"{rel}:{ln}: {what}" for ln, what in _scan_pep701(data)]
        else:
            import tomllib
            try:
                text = data.decode("utf-8")
                tomllib.loads(text)
            except (UnicodeDecodeError, tomllib.TOMLDecodeError) as e:
                lm = re.search(r"line (\d+)", str(e))
                found.append(f"{rel}:{lm[1] if lm else 0}: {str(e).splitlines()[0] if str(e) else type(e).__name__}")
                continue
            found += [f"{rel}:{ln}: {what}" for ln, what in _scan_toml11(text)]
    return "static", found


def write_floor(root, value):
    """Write `value`, "<major>.<minor>", into the declaration under `root` and into the `_rp_floor`
    literal line of every file of the parity population; -> the paths written."""
    if not FLOOR_VALUE.fullmatch(value):
        raise ValueError(f"a floor is <major>.<minor>, not {value!r}")
    root = pathlib.Path(root)
    decl = root / derive_lib_rel() / DECLARATION
    decl.write_bytes(f"{value}\n".encode())
    written = [decl.relative_to(root).as_posix()]
    for rel in read_parity_population(root):
        raw = (root / rel).read_bytes().decode("utf-8")
        new = FLOOR_LITERAL.sub(lambda m: f"{m[1]}{value}{m[3]}", raw)
        if new != raw:
            (root / rel).write_bytes(new.encode("utf-8"))
            written.append(rel)
    return written


def main(argv):
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", newline="\n")
    if argv[:1] == ["check"] and (argv[1:] == [] or (len(argv) == 3 and argv[1] == "--rev")):
        root = run_git(".", "rev-parse", "--show-toplevel").strip() or "."
        rev = argv[2] if len(argv) == 3 else None
        try:
            found = scan_floor_statements(root, rev) + ([] if rev else check_floor_copies(root))
        except ValueError as exc:
            print(f"python-floor: {exc}", file=sys.stderr)
            return 2
        for path, line, text in found:
            print(f"{path}:{line}: {text}")
        return 1 if found else 0
    if argv[:1] == ["down"] and len(argv) == 3:
        prior, target = argv[1], pathlib.Path(argv[2])
        try:
            mode, found = check_down_floor(target, prior)
        except ValueError as exc:
            print(f"python-floor down: {exc}", file=sys.stderr)
            return 2
        why = "" if mode != "static" else f", because no interpreter at {prior} resolves here"
        print(f"python-floor down: mode {mode}{why}")
        if found:
            for f in found:
                print(f)
            print(f"python-floor down: {len(found)} finding(s) under the floor {prior}; nothing was written")
            return 1
        if not (target / derive_lib_rel() / DECLARATION).is_file():
            print("python-floor down: no finding; the target carries no floor declaration, so nothing is restored here")
            return 0
        written = write_floor(target, prior)
        print(f"python-floor down: no finding; the floor {prior} restored in {len(written)} file(s)")
        return 0
    print(__doc__.split("\n\n")[0] + "\n\n" + __doc__.split("\n\n")[1], file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
