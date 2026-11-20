"""python_floor — the interpreter floor: its one declaration, the query for every statement of it,
the copies' check, and the floor step's down (TOOL-dSafePassage-11).

    python <prefix>/lib/python_floor.py check [--rev <sha>]    # every floor statement and copy finding
    python <prefix>/lib/python_floor.py down <prior> <target> [<to>, required outside gov]  # the step's down: grade, then restore
    python <prefix>/lib/python_floor.py census       # the tree compiled by a real interpreter at the floor, and its feature census

THE CENSUS (TOOL-dWitnessedBar-24 S10, practice.portable.interpreter-floor) finds an interpreter at
exactly the declared floor through `resolve_floor_interpreter`, compiles every tracked `*.py` under it
through `CHILD` in one process, and counts each feature of FLOOR_FEATURES by an AST scan: red on a
file that does not compile at the floor, on a feature added after the floor and on one removed at or
before it, one line per feature with its count. No interpreter at the floor is red, naming the floor
and the install command, never a skip: a floor tested nowhere is the gap this verb closes. WHAT IT
DOES NOT CHECK: a feature outside the declared table; a use reached through an alias or `getattr`;
and an attribute read through a name bound by `from <module> import <name>` rather than the module.

THE DECLARATION is `python-floor.txt` beside this file, one `<major>.<minor>` line. Every other
spelling of the floor is one of two kinds. A GENERATED COPY is the resolver block's `_rp_floor`
literal, carried inline by every copy of the block because a copy-installed kit has no lib dir to
read; `check_floor_copies` holds each to the declaration, and the resolver self-test's parity rows
hold the copies to each other. A POINTER is prose naming `python-floor.txt` and spelling no version.

THE QUERY. `scan_floor_statements` runs FLOOR_STATEMENT_RX over the tracked files outside `memory/`,
so it finds a statement whatever version it names; on gov's tree after the raise it finds none.

THE DOWN. `check_down_floor` grades the files the rollback restores, read at its `--to` commit
`<to>`, under the floor it restores (TOOL-dSafePassage-26 S10, S11): in an adopter, each receipt row
gov shipped ending `.py` or `.toml`, its source read from gov at `<to>`, and every `.governance/*.toml`
of the target, never the adopter's other files; on gov's own tree, gov's tracked set at `<to>`. By a
real interpreter at that floor where `resolve_floor_interpreter` finds one, mode
`interpreter <path>`; elsewhere, mode `static`, by `ast.parse` at that floor's feature version, the
four PEP 701 shapes over the tokens below 3.12, the running `tomllib`, and the four TOML 1.1 deltas.
WHAT THE STATIC MODE DOES NOT SEE: every other grammar change after the restored floor that
`feature_version` does not model (deviation-31), and no PEP 701 shape at a restored floor of 3.12 or
newer, where they are legal (TOOL-dSafePassage-69). The down executes no target code; a finding
writes nothing. It reports on stderr, one stream, its count line naming the first finding, since a
step's `tail` is stderr and the walk keeps only its last line (TOOL-dSafePassage-69 S3).

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
# PINNED on 2026-10-23 at a255d0de, where it finds the six statements of the raise and no other line;
# the last alternative, TOOL-dSafePassage-26 S49, adds the lexicon selftest's seventh at 3708a705.
FLOOR_STATEMENT_RX = re.compile(r"""(?ix)
  \b(?:c?python|py)\s*(?:>=|≥|=>)\s*\d+\.\d+
| \bc?python\s*\d+\.\d+\s*(?:\+|or\s+(?:newer|later|above))
| \bat\s+least\s+c?python\s*\d+\.\d+
| \bpython-version\s*:\s*["']?\d+\.\d+
| \brequires-python\b
| \bno\s+declared\s+python\s+floor\b
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
            p = subprocess.run(["uv", "python", "find", version], capture_output=True, text=True, encoding="utf-8", timeout=60)
            if p.returncode == 0 and p.stdout.strip():
                cands.append([p.stdout.strip()])
        except (OSError, subprocess.TimeoutExpired):
            pass
    probe = "import sys; print('%d.%d' % sys.version_info[:2]); print(sys.executable)"
    for argv in cands:
        try:
            p = subprocess.run([*argv, "-I", "-c", probe], capture_output=True, text=True, encoding="utf-8", timeout=60)
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


# The census's declared table: a module, or a `(module, attribute)` pair, and the version that bounds
# it, from the feature census of PLAY-dClosedLoop-1's night-pass instruments. An `added` feature is red
# above the floor; a `removed` one, or one whose `removal` is announced, is red at or below it.
_PEP594 = ("aifc audioop cgi cgitb chunk crypt imghdr mailcap msilib nis nntplib ossaudiodev pipes sndhdr "
           "spwd sunau telnetlib uu xdrlib").split()
FLOOR_FEATURES = {
    "tomllib": "added 3.11", "zoneinfo": "added 3.9", "graphlib": "added 3.9", "annotationlib": "added 3.14",
    "compression": "added 3.14", "concurrent.interpreters": "added 3.14",
    "distutils": "removed 3.12", "imp": "removed 3.12", "asynchat": "removed 3.12", "asyncore": "removed 3.12",
    "smtpd": "removed 3.12", "lib2to3": "removed 3.13", **{m: "removed 3.13" for m in _PEP594},
    ("datetime", "UTC"): "added 3.11", ("enum", "StrEnum"): "added 3.11", ("asyncio", "TaskGroup"): "added 3.11",
    ("asyncio", "timeout"): "added 3.11", ("hashlib", "file_digest"): "added 3.11",
    ("contextlib", "chdir"): "added 3.11", ("typing", "Self"): "added 3.11",
    ("typing", "LiteralString"): "added 3.11", ("typing", "Never"): "added 3.11",
    ("typing", "NotRequired"): "added 3.11", ("typing", "Required"): "added 3.11",
    ("typing", "assert_never"): "added 3.11", ("typing", "override"): "added 3.12",
    ("typing", "TypeAliasType"): "added 3.12", ("typing", "TypeIs"): "added 3.13",
    ("typing", "ReadOnly"): "added 3.13", ("warnings", "deprecated"): "added 3.13",
    ("copy", "replace"): "added 3.13", ("glob", "translate"): "added 3.13", ("itertools", "batched"): "added 3.12",
    ("itertools", "pairwise"): "added 3.10", ("concurrent.futures", "InterpreterPoolExecutor"): "added 3.14",
    ("sys", "_is_gil_enabled"): "added 3.13", ("locale", "getdefaultlocale"): "removal 3.15",
    ("ast", "Num"): "removed 3.14", ("ast", "Str"): "removed 3.14", ("ast", "Bytes"): "removed 3.14",
    ("ast", "NameConstant"): "removed 3.14", ("ast", "Ellipsis"): "removed 3.14",
    ("pkgutil", "find_loader"): "removed 3.14", ("pkgutil", "get_loader"): "removed 3.14",
    ("unittest", "makeSuite"): "removed 3.13", ("unittest", "findTestCases"): "removed 3.13",
}


def check_feature_red(label, floor):
    """True where the feature's bound breaks the floor: added after it, or removed at or before it."""
    kind, version = label.split()
    bound = tuple(int(x) for x in version.split("."))
    return bound > floor if kind == "added" else bound <= floor


def read_feature_census(root, paths):
    """`{feature: count}` over `paths` under `root`, every FLOOR_FEATURES key, by an AST scan run on
    this interpreter; a file that does not parse here is skipped, since `CHILD` grades its compile."""
    counts = dict.fromkeys(FLOOR_FEATURES, 0)
    attrs = {key[1] for key in FLOOR_FEATURES if isinstance(key, tuple)}

    def add(key):
        if key in counts:
            counts[key] += 1
    for rel in paths:
        try:
            tree = ast.parse((pathlib.Path(root) / rel).read_bytes(), filename=rel)
        except (SyntaxError, ValueError, OSError):
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    parts = alias.name.split(".")
                    for k in range(1, len(parts) + 1):
                        add(".".join(parts[:k]))
            elif isinstance(node, ast.ImportFrom) and node.module and not node.level:
                add(node.module)
                for alias in node.names:
                    add((node.module, alias.name))
                    add(f"{node.module}.{alias.name}")
            elif isinstance(node, ast.Attribute) and node.attr in attrs:
                add((ast.unparse(node.value), node.attr))
    return counts


def run_census(root):
    """The census verb: (exit status, lines). 1 where no interpreter at the floor resolves, a file does
    not compile under it, or a feature breaks the floor; 0 otherwise."""
    major, minor = read_floor(root)
    version = f"{major}.{minor}"
    interp = resolve_floor_interpreter(version)
    if interp is None:
        return 1, [f"python-floor census: no interpreter at the floor {version} resolves here, so nothing "
                   f"was compiled at it; install one: uv python install {version}"]
    paths = [p for p in run_git(root, "ls-files", "-z", "--", "*.py").split("\0") if p]
    if not paths:
        return 1, ["python-floor census: no tracked *.py, so nothing was graded — an empty population is no pass"]
    p = subprocess.run([interp, "-I", "-c", CHILD], input=json.dumps(paths), cwd=str(root),
                       capture_output=True, encoding="utf-8", errors="replace", timeout=600)
    if p.returncode != 0:
        return 1, [f"python-floor census: the child at {version} exited {p.returncode}: {p.stderr.strip()[:400]}"]
    lines = [f"python-floor census: {f} does not compile at the floor {version}" for f in p.stdout.splitlines() if f]
    red = len(lines)
    for key, count in read_feature_census(root, paths).items():
        label = FLOOR_FEATURES[key]
        name = key if isinstance(key, str) else ".".join(key)
        breaks = count and check_feature_red(label, (major, minor))
        red += bool(breaks)
        lines.append(f"python-floor census: {name} · {label} · {count}" + (f" · RED at the floor {version}" if breaks else ""))
    lines.append(f"python-floor census: {len(paths)} tracked *.py compiled by {interp} at {version}, "
                 f"{len(FLOOR_FEATURES)} features counted, {red} finding(s)")
    return (1 if red else 0), lines


def _scan_pep701(data):
    """[(line, what)] for the four PEP 701 shapes in a .py file's tokens, each a replacement field
    the restored floor's tokenizer refuses: a string reusing an enclosing f-string's quote, a
    backslash, a `#`, and a line break in a single-quoted f-string's field."""
    starts = {tokenize.FSTRING_START, getattr(tokenize, "TSTRING_START", tokenize.FSTRING_START)}
    ends = {tokenize.FSTRING_END, getattr(tokenize, "TSTRING_END", tokenize.FSTRING_END)}
    stack, found = [], []  # each open f-string: [quote, brace depth, start row]

    def add_note(row, what):
        if (row, what) not in found:
            found.append((row, what))

    def extract_quote(s):
        s = s.lstrip("rRbBfFtTuU")
        return s[:3] if s[:3] in ('"""', "'''") else s[:1]

    try:
        for tok in tokenize.tokenize(io.BytesIO(data).readline):
            # The f-strings whose replacement field holds this token: every enclosing one, and the
            # innermost only while its brace depth is open.
            fields = stack[:-1] + ([stack[-1]] if stack and stack[-1][1] > 0 else [])
            if fields:
                if tok.type in starts or tok.type == tokenize.STRING:
                    q = extract_quote(tok.string)
                    if any(q[:1] == f[0][:1] and len(q) >= len(f[0]) for f in fields):
                        add_note(tok.start[0], "a string in a replacement field reuses the enclosing f-string's quote")
                if tok.type in (tokenize.STRING, tokenize.FSTRING_MIDDLE) and "\\" in tok.string:
                    add_note(tok.start[0], "a backslash in a replacement field")
                if tok.type == tokenize.COMMENT or (tok.type in (tokenize.STRING, tokenize.FSTRING_MIDDLE) and "#" in tok.string):
                    add_note(tok.start[0], "a # in a replacement field")
                if any(len(f[0]) == 1 and tok.end[0] > f[2] for f in fields):
                    add_note(tok.start[0], "a line break in a single-quoted f-string's replacement field")
            if tok.type in starts:
                stack.append([extract_quote(tok.string), 0, tok.start[0]])
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


def derive_gov_root():
    """Gov's root, resolved: the nearest directory at or above this file holding a `.git`, or this
    file's own directory where none does (TOOL-dSafePassage-76 S5)."""
    return next((d for d in (HERE, *HERE.parents) if (d / ".git").exists()), HERE).resolve()


def read_down_population(target, to_commit):
    """{label: bytes} the down grades (S11): on gov's own tree, every tracked `.py` and `.toml` of
    gov at `to_commit`; in an adopter, each receipt row gov shipped (any role but `adopter-owned`)
    whose `path` ends `.py` or `.toml`, its `source` read from gov at `to_commit` and labelled by its
    `path`, a source absent there skipped since the rollback removes it, plus every
    `.governance/*.toml` of the target as it stands. Gov is the repository holding this file."""
    target, gov = pathlib.Path(target).resolve(), derive_gov_root()
    if not run_git(gov, "rev-parse", "--verify", "--quiet", f"{to_commit}^{{commit}}").strip():
        raise ValueError(f"<to> {to_commit!r} names no commit in {gov.as_posix()}")

    def read_blob(rel):
        out = subprocess.run(["git", "-C", str(gov), "show", f"{to_commit}:{rel}"], capture_output=True)
        return out.stdout if out.returncode == 0 else None

    if target == gov:
        rels = run_git(gov, "ls-tree", "-r", "--name-only", "-z", to_commit).split("\0")
        return {r: read_blob(r) for r in rels if r.endswith((".py", ".toml"))}
    try:
        rows = json.loads((target / ".governance" / "install.json").read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    out = {}
    for row in rows:
        if (isinstance(row, dict) and str(row.get("path", "")).endswith((".py", ".toml"))
                and row.get("role") != "adopter-owned" and isinstance(row.get("source"), str)):
            data = read_blob(row["source"])
            if data is not None:
                out[row["path"]] = data
    for f in sorted((target / ".governance").glob("*.toml")):
        out[f".governance/{f.name}"] = f.read_bytes()
    return out


def check_down_floor(target, prior, to_commit):
    """(mode, findings) for the down to the floor `prior`, "<major>.<minor>": `read_down_population`
    at `to_commit` graded by a real interpreter at that floor where one resolves, mode
    `interpreter <path>`, else statically, mode `static`. Each finding is `path:line: what`."""
    m = FLOOR_VALUE.fullmatch(prior)
    if not m:
        raise ValueError(f"the prior floor must be <major>.<minor>, not {prior!r}")
    population = read_down_population(target, to_commit)
    interp = resolve_floor_interpreter(prior)
    if interp:
        import tempfile
        with tempfile.TemporaryDirectory(prefix="gk-floor-") as td:
            for rel, data in population.items():
                (pathlib.Path(td) / rel).parent.mkdir(parents=True, exist_ok=True)
                (pathlib.Path(td) / rel).write_bytes(data or b"")
            p = subprocess.run([interp, "-I", "-c", CHILD], input=json.dumps(sorted(population)),
                               capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=td)
        found = [ln for ln in p.stdout.splitlines() if ln.strip()]
        if p.returncode != 0:
            found.append(f"(interpreter {interp} exited {p.returncode}: {p.stderr.strip()[-300:]})")
        return f"interpreter {interp}", found
    feature = (int(m[1]), int(m[2]))
    found = []
    for rel, data in sorted(population.items()):
        if data is None:
            found.append(f"{rel}:0: unreadable at the rollback's --to commit")
            continue
        if rel.endswith(".py"):
            try:
                ast.parse(data, rel, feature_version=feature)
            except SyntaxError as e:
                found.append(f"{rel}:{e.lineno or 0}: {e.msg}")
                continue
            if feature < (3, 12):  # PEP 701 made these four shapes legal in 3.12 (TOOL-dSafePassage-69)
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
    if argv == ["census"]:
        root = run_git(".", "rev-parse", "--show-toplevel").strip() or "."
        try:
            rc, lines = run_census(root)
        except ValueError as exc:
            print(f"python-floor census: {exc}", file=sys.stderr)
            return 2
        print("\n".join(lines))
        return rc
    if argv[:1] == ["down"] and len(argv) in (3, 4):
        prior, target = argv[1], pathlib.Path(argv[2])
        # TOOL-dSafePassage-35 S22: <to> defaults to the target's HEAD, so the down always grades
        # bytes at a commit, never the working tree; TOOL-dSafePassage-76 S5: only on gov's own tree,
        # since an adopter's HEAD is a commit gov's repository never holds.
        if len(argv) == 3 and target.resolve() != derive_gov_root():
            print("python-floor down: <to> is required outside gov's own tree: the target's HEAD is a "
                  "commit gov's repository never holds", file=sys.stderr)
            return 2
        to = argv[3] if len(argv) == 4 else (run_git(target, "rev-parse", "--verify", "--quiet", "HEAD").strip()
                                             or "HEAD")
        try:
            mode, found = check_down_floor(target, prior, to)
        except ValueError as exc:
            print(f"python-floor down: {exc}", file=sys.stderr)
            return 2
        why = "" if mode != "static" else f", because no interpreter at {prior} resolves here"
        print(f"python-floor down: mode {mode}{why}", file=sys.stderr)
        if found:
            for f in found:
                print(f, file=sys.stderr)
            print(f"python-floor down: {len(found)} finding(s) under the floor {prior}, the first {found[0]}; "
                  "nothing was written", file=sys.stderr)
            return 1
        if not (target / derive_lib_rel() / DECLARATION).is_file():
            print("python-floor down: no finding; the target carries no floor declaration, so nothing is restored here",
                  file=sys.stderr)
            return 0
        written = write_floor(target, prior)
        print(f"python-floor down: no finding; the floor {prior} restored in {len(written)} file(s)", file=sys.stderr)
        return 0
    print(__doc__.split("\n\n")[0] + "\n\n" + __doc__.split("\n\n")[1], file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
