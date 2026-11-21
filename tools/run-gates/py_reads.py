#!/usr/bin/env python3
"""py_reads.py - what the bar otherwise never reads in a Python file (PLAY-dOrderedCharter-67).

    python <this kit>/py_reads.py                  # both arms: exit 0 green, 1 red, 2 refused
    python <this kit>/py_reads.py --names <file>   # the name arm over one file, `-` being stdin
    python <this kit>/py_reads.py --guards <leg>   # one leg's import closure and its gaps
    python <this kit>/py_reads.py --list-params    # the params arm's measured keys and counts, the seed
    python <this kit>/py_reads.py --selftest       # the plants, each arm's failing case included

THREE ARMS, one AST read each:

  guard  every leg of gate-legs.json with a non-empty `guard` whose argv runs a Python file: the
         entry's import closure, sibling kits reached through a literal `resolve_kit_dir` call
         included, reds a walked module its guard does not cover. A scoped bar skips such a leg, or
         reuses its green, after an edit to that module alone.
  name   every tracked `*.py` outside the memory root: reds a name loaded and bound nowhere in its
         module, which raises only when that line runs.
  params every tracked `*.py` outside the memory root: reds a parameter of a `def` that no name load
         in its body reads, nested bodies included, unless the shrink-only `unread-params` ledger keeps
         its `(path, function, parameter)` key, and reds a kept row no hit carries. `self`, `cls` and a
         parameter opening `_` are never hits (TOOL-dWitnessedBar-108 S7).

WHAT IT DOES NOT READ, printed on every run because a zero here reads as coverage to everyone who
did not write it. The guard arm: a leg whose head is not Python, a module reached through a
subprocess, a `python -c` body, a data file a suite reads, a kit named by a computed string, and a
`dynamic` row of the import walk. The name arm binds per MODULE, so a name bound in one function and
read in another passes, and so do a read before its binding, an attribute, a name in a string or an
`eval`, a Python script with no `.py` suffix, and every name of a file with a star import, which is
skipped and counted. The params arm: a lambda's parameter, and a parameter read only through
`locals()` or a string.

An unparsable file, an absent manifest, an empty population, and an absent `unread-params` home or
registration each exit 2 naming what could not be read, so a zero is never a reading of nothing. GOV-ONLY: this kit's descriptor withholds the file
from `govkit apply`, which is why it may import the memory-tree kit's walk and conf reader.
"""
import ast
import builtins
import contextlib
import io
import json
import os
import pathlib
import subprocess
import sys
import tempfile

HERE = pathlib.Path(os.path.abspath(__file__)).parent

# The sibling-kit resolver, INLINED byte-identically from the canonical copy named on its marker
# line and gated by the resolve-python self-test.
# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


GUARDS_NOT_READ = ("py-reads: guards, not read · a module reached through a subprocess, a python -c body, "
                   "a data file a suite reads, a kit named by a computed string, a dynamic import")
NAMES_NOT_READ = ("py-reads: names, not read · a name bound in one function and read in another, a read "
                  "before its binding, an attribute, a name in a string or an eval, a Python script with "
                  "no .py suffix")
NAMES_LINE = "py-reads: names · {} files read, {} star imports skipped"
PARAMS_NOT_READ = "py-reads: params, not read · a lambda, a parameter read only through locals() or a string"
PARAMS_LINE = "py-reads: params · {} hits, {} kept rows, {} unlisted, {} stale"
PARAMS_POPULATION = "unread-params"  # the ledger population that keeps the params arm's tolerated hits
UNUSED_SLOTS = ("self", "cls")  # never a hit, with any parameter opening `_`: the corpus's unused-slot spelling


class Refused(Exception):
    """A refusal: one line, exit 2."""


def load_readers():
    """The memory-tree kit's import walk and conf reader, found from this install."""
    mt = resolve_kit_dir("memory-tree", "import_walk.py", HERE)
    if str(mt) not in sys.path:
        sys.path.insert(0, str(mt))
    import id_grammar  # noqa: PLC0415
    import import_walk  # noqa: PLC0415
    return id_grammar, import_walk


def scan_unbound_names(source):
    """-> the sorted names `source` loads and binds nowhere, or None for a star import, whose names
    cannot be known. Raises what `ast.parse` raises."""
    tree = ast.parse(source)
    bound = set()
    for x in ast.walk(tree):
        if isinstance(x, ast.ImportFrom) and any(al.name == "*" for al in x.names):
            return None
        if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            bound.add(x.name)
        if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            a = x.args
            bound.update(y.arg for y in a.posonlyargs + a.args + a.kwonlyargs + [z for z in (a.vararg, a.kwarg) if z])
        if isinstance(x, ast.Name) and isinstance(x.ctx, (ast.Store, ast.Del)):
            bound.add(x.id)
        if isinstance(x, (ast.Import, ast.ImportFrom)):
            bound.update((al.asname or al.name).split(".")[0] for al in x.names)
        if isinstance(x, ast.ExceptHandler) and x.name:
            bound.add(x.name)
        if isinstance(x, (ast.Global, ast.Nonlocal)):
            bound.update(x.names)
        if isinstance(x, (ast.MatchAs, ast.MatchStar)) and x.name:
            bound.add(x.name)
        if isinstance(x, ast.MatchMapping) and x.rest:
            bound.add(x.rest)
    known = bound | set(dir(builtins)) | {"__file__", "__name__", "__doc__"}
    return sorted({x.id for x in ast.walk(tree) if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Load)} - known)


def scan_unread_params(source):
    """-> `(function name, parameter)` for each positional, keyword-only, `*` or `**` parameter of each
    `def` that no `ast.Name` load in the function's body reads, nested bodies included, in walk order.
    `self`, `cls` and a parameter opening `_` are never hits. Raises what `ast.parse` raises."""
    hits = []
    for node in ast.walk(ast.parse(source)):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        a = node.args
        params = [y.arg for y in a.posonlyargs + a.args + a.kwonlyargs + [z for z in (a.vararg, a.kwarg) if z]]
        loads = {x.id for stmt in node.body for x in ast.walk(stmt)
                 if isinstance(x, ast.Name) and isinstance(x.ctx, ast.Load)}
        hits += [(node.name, y) for y in params if y not in loads and y not in UNUSED_SLOTS and not y.startswith("_")]
    return hits


def scan_kit_homes(path):
    """-> every literal first argument of a `resolve_kit_dir` call in one parsed file."""
    tree = ast.parse(path.read_bytes().decode("utf-8"), filename=str(path))
    homes = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and node.args and isinstance(node.args[0], ast.Constant) \
                and isinstance(node.args[0].value, str):
            f = node.func
            if (f.id if isinstance(f, ast.Name) else getattr(f, "attr", "")) == "resolve_kit_dir":
                homes.add(node.args[0].value)
    return homes


def derive_closure(entry, tool_root, read):
    """-> the sorted files `entry` imports, itself included, by the search of one process: the
    importer's directory, then the entry's, then each kit a walked file resolves, since `sys.path`
    is one per process and a kit found late serves a file walked early. The walk repeats until no
    directory is added. `read` caches each file's scan across legs. A package directory is no
    `<name>.py`, so it is not walked either."""
    _, import_walk = load_readers()
    dirs = [entry.parent]
    while True:
        known, queue = len(dirs), [entry]
        seen = {entry}
        for path in queue:
            if path not in read:
                try:
                    rows = import_walk.scan_imports(str(path))
                    read[path] = ({n.split(".")[0] for n, _line, kind in rows if kind != "dynamic"},
                                  scan_kit_homes(path))
                except (OSError, UnicodeDecodeError, SyntaxError, ValueError) as e:
                    raise Refused(f"{path.as_posix()} does not parse, so its imports were not read: {e}") from e
            names, homes = read[path]
            dirs += [d for d in sorted(tool_root / h for h in homes) if d.is_dir() and d not in dirs]
            for name in names:
                hit = next((d / f"{name}.py" for d in (path.parent, *dirs) if (d / f"{name}.py").is_file()), None)
                if hit and hit not in seen:
                    seen.add(hit)
                    queue.append(hit)
        if len(dirs) == known:
            return sorted(seen)


def derive_guard_gaps(legs, tool_root):
    """-> `[(leg, closure, gaps)]`, root-relative, for each row with a non-empty `guard`, a Python
    `argv[0]` and a `.py` word in its argv. A guard path is covered exactly, or under a guard ending
    `/`, with `{prefix}` expanded. An entry no file holds is a refusal, never a closure of nothing."""
    root, prefix = tool_root.parent, tool_root.name
    rows, read = [], {}
    for leg in legs:
        argv, guard = leg.get("argv") or [], [g.replace("{prefix}", prefix) for g in leg.get("guard") or []]
        word = next((w for w in argv if w.endswith(".py")), None)
        if not (guard and word and argv[0].startswith("python")):
            continue
        entry = root / word.replace("{prefix}", prefix)
        if not entry.is_file():
            raise Refused(f"leg {leg['name']!r} runs {entry.as_posix()}, which no file holds")
        closure = [p.relative_to(root).as_posix() for p in derive_closure(entry, tool_root, read)]
        gaps = [m for m in closure if not any(m == g or (g.endswith("/") and m.startswith(g)) for g in guard)]
        rows.append((leg["name"], closure, gaps))
    return rows


def read_tracked_sources(root, id_grammar):
    """-> `[(path, bytes)]` of the tracked `*.py` outside the memory root, sorted: the population the name
    arm and the params arm both read. An empty one is a refusal."""
    memory_root = id_grammar.load_conf(root).get("MEMORY_ROOT", "").strip().strip("/")
    if not memory_root:
        raise Refused(f"{id_grammar.CONF_NAME} declares no MEMORY_ROOT, so the population has no boundary")
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    p = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--", "*.py"], capture_output=True,
                       text=True, encoding="utf-8", env=env, stdin=subprocess.DEVNULL)
    if p.returncode:
        raise Refused(f"git ls-files exited {p.returncode}, so the population is unknown: {p.stderr.strip()}")
    sources = [(rel, (root / rel).read_bytes()) for rel in sorted(
        r for r in p.stdout.split("\0") if r and not r.startswith(memory_root + "/")) if (root / rel).is_file()]
    if not sources:
        raise Refused(f"no tracked *.py outside {memory_root}/ under {root.as_posix()}: an empty population is not a pass")
    return sources


def scan_tracked_names(root, id_grammar):
    """-> `(hits, files read, star imports)` over the tracked `*.py` outside the memory root."""
    hits, read, stars = [], 0, 0
    for rel, data in read_tracked_sources(root, id_grammar):
        missing = read_unbound_names(rel, data)
        read += 1
        stars += missing is None
        hits += [(rel, name) for name in missing or []]
    return hits, read, stars


def measure_unread_params(root, id_grammar):
    """-> `{(path, function, parameter): hits}` of `scan_unread_params` over the name arm's population."""
    measured = {}
    for rel, data in read_tracked_sources(root, id_grammar):
        try:
            found = scan_unread_params(data.decode("utf-8"))
        except (SyntaxError, UnicodeDecodeError, ValueError) as e:
            raise Refused(f"{rel} does not parse, so its parameters were not read: {e}") from e
        for function, param in found:
            measured[(rel, function, param)] = measured.get((rel, function, param), 0) + 1
    return measured


def check_unread_params(root, measured):
    """-> `(findings, kept)`: `compare_counts` of `measured` against the `unread-params` ledger under its
    registration's direction, each finding `(finding, key, measured, kept)`, and the kept rows' counts by
    key. The registration is read through the ledger factory's `read_registrations` and the home through
    `read_ledger`; no registration, an absent home, a home whose first line is not its header and a
    malformed row are each a refusal."""
    import legacy_ledger  # noqa: PLC0415 - the ledger factory, on sys.path once load_readers ran
    try:
        regs = [r for r in legacy_ledger.read_registrations(root) if r.population == PARAMS_POPULATION]
    except ValueError as e:
        raise Refused(f"the [[ledger]] registrations do not read, so the params arm has no ledger: {e}") from e
    if len(regs) != 1:
        raise Refused(f"{len(regs)} [[ledger]] tables register {PARAMS_POPULATION}, not one, so the params arm has no ledger")
    reg = regs[0]
    if not (root / reg.home).is_file():
        raise Refused(f"{reg.home} is absent, so nothing is kept; seed it: python <memory-tree kit>/legacy_ledger.py "
                      f"seed --population {PARAMS_POPULATION}")
    bad = legacy_ledger.check_home_readable(root / reg.home, legacy_ledger.render_header(reg))
    if bad:
        raise Refused(f"{reg.home}: {bad}")
    rows, malformed = legacy_ledger.read_ledger(root, reg)
    if malformed:
        raise Refused(f"{reg.home}: {legacy_ledger.render_malformed(malformed[0])}")
    kept = {key: row[0] for key, row in rows.items()}
    return legacy_ledger.compare_counts(measured, kept, reg.direction), kept


def read_unbound_names(label, data):
    """`scan_unbound_names` over a file's bytes, a file it cannot read being a refusal."""
    try:
        return scan_unbound_names(data.decode("utf-8"))
    except (SyntaxError, UnicodeDecodeError, ValueError) as e:
        raise Refused(f"{label} does not parse, so its names were not read: {e}") from e


def read_legs(tool_root):
    """-> the manifest's rows; an absent or unreadable manifest is a refusal."""
    path = tool_root / "gate-legs.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise Refused(f"{path.as_posix()} could not be read: {e}") from e


def print_gaps(rows):
    for leg, _closure, gaps in rows:
        for module in gaps:
            print(f"py-reads: RED guard · {leg} · {module} is imported and outside its guard")


def print_name_hits(hits):
    for path, name in hits:
        print(f"py-reads: RED name · {path} · {name} is read and never bound")


def run_both(tool_root):
    """The three arms over this tree, the closing lines last; the params arm runs after the name arm."""
    id_grammar, _ = load_readers()
    legs = read_legs(tool_root)
    rows = derive_guard_gaps(legs, tool_root)
    if not rows:
        raise Refused("no guarded leg runs a Python file: an empty population is not a pass")
    hits, read, stars = scan_tracked_names(tool_root.parent, id_grammar)
    measured = measure_unread_params(tool_root.parent, id_grammar)
    findings, kept = check_unread_params(tool_root.parent, measured)
    print_gaps(rows)
    print_name_hits(hits)
    for finding, (path, function, param), have, want in findings:
        print(f"py-reads: RED params · {path} · {function} · {param} · {finding} ({have or 0} measured, {want or 0} kept)")
    print(GUARDS_NOT_READ)
    print(NAMES_NOT_READ)
    print(PARAMS_NOT_READ)
    unread = sum(1 for leg in legs if leg.get("guard")) - len(rows)
    print(f"py-reads: guards · {len(rows)} suites walked, {unread} guarded legs of another head not read")
    print(NAMES_LINE.format(read, stars))
    print(PARAMS_LINE.format(sum(measured.values()), len(kept), sum(f[0] == "undeclared site" for f in findings),
                             sum(f[0] == "unmeasured row" for f in findings)))
    return 1 if hits or findings or any(gaps for _leg, _closure, gaps in rows) else 0


def run_list_params(tool_root):
    """`--list-params`: each measured key's fields and its count, TAB-joined, the `unread-params` seed."""
    id_grammar, _ = load_readers()
    for (path, function, param), count in sorted(measure_unread_params(tool_root.parent, id_grammar).items()):
        print(f"{path}\t{function}\t{param}\t{count}")
    return 0


def run_names(target):
    """`--names`: the name arm over one file, `-` being stdin."""
    data = sys.stdin.buffer.read() if target == "-" else pathlib.Path(target).read_bytes()
    missing = read_unbound_names(target, data)
    print_name_hits((target, name) for name in missing or [])
    print(NAMES_NOT_READ)
    print(NAMES_LINE.format(1, int(missing is None)))
    return 1 if missing else 0


def run_guards(leg, tool_root):
    """`--guards`: one leg's closure and its gaps; a leg the arm does not walk is a refusal."""
    rows = derive_guard_gaps([r for r in read_legs(tool_root) if r.get("name") == leg], tool_root)
    if not rows:
        raise Refused(f"{leg!r} is no guarded leg running a Python file, so nothing was walked")
    for module in rows[0][1]:
        print(f"py-reads: closure · {leg} · {module}")
    print_gaps(rows)
    return 1 if rows[0][2] else 0


def run_selftest():
    """The plants, each in a scratch tool root: every arm's failing case beside its passing one."""
    failed, ran = [], []

    def check(label, got, want):
        ran.append(label)
        if got != want:
            failed.append(f"{label}: got {got!r}, want {want!r}")

    def run_quietly(*argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            return main(list(argv)), out.getvalue()

    check("an undefined name reds", scan_unbound_names("print(planted)\n"), ["planted"])
    check("the same name defined is green", scan_unbound_names("planted = 1\nprint(planted)\n"), [])
    check("an unread parameter is a hit", scan_unread_params("def f(planted):\n    return 1\n"), [("f", "planted")])
    check("the same parameter read is none", scan_unread_params("def f(planted):\n    return planted\n"), [])
    check("a parameter opening _ is none", scan_unread_params("def f(_planted):\n    return 1\n"), [])
    check("a parameter read only in a nested function is none",
          scan_unread_params("def f(planted):\n    def g():\n        return planted\n    return g\n"), [])
    with tempfile.TemporaryDirectory() as tmp:
        tools = pathlib.Path(tmp) / HERE.parent.name  # the scratch tool root carries this install's name
        for rel, text in (("kit-a/suite.py", "import helper\n"), ("kit-a/helper.py", "x = 1\n"),
                          ("kit-a/reach.py", 'resolve_kit_dir("kit-b", "mod.py", ".")\nimport mod\n'),
                          ("kit-b/mod.py", "x = 1\n"), ("star.py", "from helper import *\nprint(planted)\n"),
                          ("broken.py", "def (\n")):
            (tools / rel).parent.mkdir(parents=True, exist_ok=True)
            (tools / rel).write_text(text, encoding="utf-8")

        def derive_gaps(entry, *guard):
            leg = {"name": "fx", "argv": ["python", "{prefix}/" + entry], "guard": list(guard)}
            return derive_guard_gaps([leg], tools)[0][2]

        rc, out = run_quietly("--names", str(tools / "star.py"))
        check("a star import reds nothing", rc, 0)
        check("a star import counts", "1 star imports skipped" in out, True)
        check("a suite import outside its guard reds", derive_gaps("kit-a/suite.py", "{prefix}/kit-a/suite.py"),
              [f"{HERE.parent.name}/kit-a/helper.py"])
        check("the same path in its guard is green",
              derive_gaps("kit-a/suite.py", "{prefix}/kit-a/suite.py", "{prefix}/kit-a/helper.py"), [])
        check("a sibling kit reached by a literal resolve reds", derive_gaps("kit-a/reach.py", "{prefix}/kit-a/"),
              [f"{HERE.parent.name}/kit-b/mod.py"])
        check("a file that does not parse refuses", run_quietly("--names", str(tools / "broken.py"))[0], 2)
    for line in failed:
        print(f"py-reads: selftest FAILED · {line}")
    print(f"py-reads: selftest · {len(ran) - len(failed)} of {len(ran)} plants held")
    return 1 if failed else 0


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")  # a `·` through a pipe on a cp125x node
    tool_root = HERE.parent
    try:
        if argv == ["--selftest"]:
            return run_selftest()
        if len(argv) == 2 and argv[0] == "--names":
            return run_names(argv[1])
        if len(argv) == 2 and argv[0] == "--guards":
            return run_guards(argv[1], tool_root)
        if argv == ["--list-params"]:
            return run_list_params(tool_root)
        if argv:
            raise Refused("usage: py_reads.py [--names <file>|--guards <leg>|--list-params|--selftest]")
        return run_both(tool_root)
    except (Refused, OSError) as e:
        print(f"py-reads: REFUSED · {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
