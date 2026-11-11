"""import_walk — every import a Python file makes, by kind (PLAY-dOrderedCharter-16 S5).

Lifted from `check-verdict-epoch.sh`'s inline import-closure walk at its second instance, the layer
check in the playbook kit, so a lexer bug in the walk moves both gates at once.

`scan_imports(path)` reads one file as UTF-8, parses it with `ast` and returns `[(name, line, kind)]`
in `ast.walk` order, nested imports included, since a lazy import in a function is reached the moment
that function runs. Kinds: `import` (each `import a.b` name), `from` (an absolute `from m import ...`;
a relative one is no other module's and is skipped), and `dynamic`: a literal `__import__("<n>")`, an
`importlib.import_module("<n>")`, or an `importlib.util.spec_from_file_location(_, "<path>")`, whose
name is the literal path. It raises what the read or the parse raises, so a caller can say the file's
imports were not read.

`derive_import_closure(kit, scan)` is the verdict-epoch gate's closure, its message strings verbatim:

    python import_walk.py --closure <kit-prefix> <scanned file>...

`derive_module_closure(path, dirs)` is one module's own closure, the tag index's extractor version
(PLAY-dOrderedCharter-55 S15): each static import's first name `<n>` resolves to the first `<dir>/<n>.py`
among `dirs`, as `sys.path` would, a dynamic one is skipped, and a module that does not parse raises.

WHAT IT DOES NOT SEE: a module loaded by a computed name or path, and a shell invocation.
"""
import ast
import os
import sys

DYNAMIC_CALLS = ("__import__", "import_module", "spec_from_file_location")


def scan_imports(path):
    """-> [(name, line, kind)] for one Python file; raises OSError, UnicodeDecodeError, SyntaxError
    or ValueError where the file cannot be read or parsed."""
    with open(path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), filename=path)
    rows = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            rows.extend((a.name, node.lineno, "import") for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            if not node.level and node.module:
                rows.append((node.module, node.lineno, "from"))
        elif isinstance(node, ast.Call):
            f = node.func
            called = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else "")
            if called not in DYNAMIC_CALLS:
                continue
            at = 1 if called == "spec_from_file_location" else 0
            if len(node.args) > at and isinstance(node.args[at], ast.Constant) \
                    and isinstance(node.args[at].value, str):
                rows.append((node.args[at].value, node.lineno, "dynamic"))
    return rows


def derive_module_closure(path, dirs):
    """-> the sorted paths of `path` and of every module its static imports reach, each walked the same
    way: an import's first name `<n>` is the first `<dir>/<n>.py` among `dirs`, and one no dir holds, the
    standard library's, is skipped. Raises what `scan_imports` raises on a module that does not parse."""
    start = os.path.normpath(path)
    seen, queue = {start}, [start]
    for mod in queue:
        for name, _line, kind in scan_imports(mod):
            if kind == "dynamic":
                continue
            first = name.split(".")[0] + ".py"
            hit = next((os.path.normpath(os.path.join(d, first)) for d in dirs
                        if os.path.isfile(os.path.join(d, first))), None)
            if hit and hit not in seen:
                seen.add(hit)
                queue.append(hit)
    return sorted(seen)


def derive_import_closure(kit, scan):
    """-> (lines, rc). The scan set's sibling closure: a first name `<n>` of a static import is a
    sibling when `<kit><n>.py` is a file, and each sibling reached is walked the same way. rc 2 when a
    reached sibling is not in the scan set or a scanned module does not parse, else 0."""
    queue = [p for p in scan if p.endswith(".py")]
    read, importer, missing, broken = set(queue), {}, [], []
    for path in queue:
        try:
            rows = scan_imports(path)
        except (OSError, UnicodeDecodeError, SyntaxError, ValueError) as e:
            broken.append((path, " ".join(("%s: %s" % (type(e).__name__, e)).split())))
            continue
        for name, _line, kind in rows:
            if kind == "dynamic":
                continue
            sib = kit + name.split(".")[0] + ".py"
            if sib in read or not os.path.isfile(sib):
                continue
            read.add(sib)
            queue.append(sib)
            importer[sib] = path
            missing.append(sib)
    dash, tick = chr(0x2014), chr(0x27)
    lines = []
    for sib in missing:
        lines.append("verdict-epoch: FAILED %s %s is imported by %s and is not in DELEGATES, so a change to it moves a verdict this gate never dates; add it to DELEGATES" % (dash, sib, importer[sib]))
    for path, why in broken:
        lines.append("verdict-epoch: FAILED %s %s does not parse, so its imports were not read and the import closure is unknown (%s)" % (dash, path, why))
    if missing or broken:
        return lines, 2
    sibs = sum(1 for p in read if p.startswith(kit) and "/" not in p[len(kit):])
    lines.append("verdict-epoch: the delegates%s import closure is %d sibling module(s) and %d other scanned file(s), every sibling in DELEGATES" % (tick, sibs, len(read) - sibs))
    return lines, 0


def main(argv):
    if len(argv) < 2 or argv[0] != "--closure":
        sys.stderr.write("usage: import_walk.py --closure <kit-prefix> <scanned file>...\n")
        return 2
    lines, rc = derive_import_closure(argv[1], argv[2:])
    for line in lines:
        sys.stdout.buffer.write((line + "\n").encode("utf-8"))
        sys.stdout.buffer.flush()
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
