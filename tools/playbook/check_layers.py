"""check_layers — the layer register's contract and the check that the core never depends on an
expansion or an optional component (PLAY-dOrderedCharter-16).

    python check_layers.py                 # the leg: the contract, the edges and EX-1 over the tree
    python check_layers.py --list          # every row, every descriptor and every edge, allowed or not
    python check_layers.py --new <tag> --kind <kind> [--of <tag>] --definition <text>
    python check_layers.py --fixture [--plant <case>] [--list]

The register is `layers.toml` beside this file: one `[[layer]]` row per layer and a top-level `shared`
list of tool directories that hold inline-copied primitives and no layer. Each kit descriptor,
`<tool root>/*/kit.toml` and `<tool root>/govkit/entries/*.kit.toml`, declares `layer = "<tag>"`, and a
core kit declares `optional = [{ part, point, fallback }]` for each edge it is allowed to keep.

An EDGE runs from a file a core kit ships, one its descriptor does not withhold with
`role = "project-owned"`, to a non-core kit, and is found by kind: `import` (an `import` or `from`
name resolving to a `.py` file at a non-core home and not in the importer's own directory),
`dynamic` (a literal `__import__`, `importlib.import_module` or `spec_from_file_location` load),
`probe` (a `resolve_kit_dir` call whose home is a non-core home, or a path literal naming one),
`copy` (a `shutil.copy*`/`copytree` or a shell `cp` whose source names a non-core kit's file),
`shell` (a shell line running a path under a non-core home) and `requires-if` (a core descriptor's
`requires_if` row naming a non-core kit). An edge is allowed when the source kit's `optional` rows
name its file as `part`; every other edge is red. Exit 0 green, 1 red, 2 an unreadable register or
descriptor.

WHAT IT DOES NOT READ, printed every run: a path computed at run time, JavaScript, and a file no
descriptor claims. A Python docstring and a shell comment line are no edge.
"""
import ast
import fnmatch
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib


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

HERE = pathlib.Path(__file__).absolute().parent
sys.path.insert(0, str(resolve_kit_dir("memory-tree", "import_walk.py", HERE)))
import import_walk  # noqa: E402  the one AST walk, shared with the verdict-epoch gate

KINDS = ("import", "dynamic", "probe", "copy", "shell", "requires-if")
LAYER_KINDS = ("core", "optional", "expansion")
TAG = re.compile(r"^layer(\.[a-z][a-z0-9-]*)+$")
COPY_CALLS = ("copy", "copy2", "copyfile", "copytree")
NOT_READ = "layers: not read: a path computed at run time, JavaScript, and a file no descriptor claims"


class Unreadable(Exception):
    """A register or a descriptor that does not parse: exit 2, naming it."""


def read_layers(path):
    """-> the register as a dict; Unreadable naming the file when it is absent or not TOML."""
    try:
        with open(path, "rb") as fh:
            reg = tomllib.load(fh)
    except (OSError, tomllib.TOMLDecodeError) as e:
        raise Unreadable("the register %s does not read: %s" % (pathlib.Path(path).as_posix(), e))
    reg.setdefault("shared", [])
    reg.setdefault("layer", [])
    return reg


def derive_tracked(root):
    """-> every file under root, repo-relative and posix: git's index in a work tree, else a walk."""
    if (root / ".git").exists():
        out = subprocess.run(["git", "-C", str(root), "ls-files", "-z"], capture_output=True, check=True)
        return [p for p in out.stdout.decode("utf-8").split("\0") if p]
    return sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file())


def read_descriptors(root, tool_root, tracked):
    """-> one dict per kit descriptor: path, id, home (a directory, or None for a flat entry), layer,
    optional, requires_if and files, the tracked files it ships."""
    pats = (tool_root + "/*/kit.toml", tool_root + "/govkit/entries/*.kit.toml")
    tset = set(tracked)
    kits = []
    for dpath in sorted(p for p in tracked if any(fnmatch.fnmatchcase(p, pat) for pat in pats)):
        try:
            with open(root / dpath, "rb") as fh:
                d = tomllib.load(fh)
        except (OSError, tomllib.TOMLDecodeError) as e:
            raise Unreadable("the descriptor %s does not read: %s" % (dpath, e))
        rules = [r for r in d.get("files") or [] if isinstance(r, dict)]
        withheld = [r for r in rules if r.get("role") == "project-owned"]
        if dpath.startswith(tool_root + "/govkit/entries/"):
            home_d = None
            h = str(d.get("home", ".")).strip("/")  # no home at all: the includes are repo-relative
            base = h if "home" not in d or d.get("home_root_relative") else (tool_root if h in ("", ".") else tool_root + "/" + h)
            files = []
            for r in rules:
                if r in withheld:
                    continue
                inc = r.get("include")
                for s in (inc if isinstance(inc, list) else [inc] if inc else []):
                    s = s.replace("{prefix}", tool_root)
                    p = s if r.get("root_relative") else base + "/" + s
                    if p in tset:
                        files.append(p)
        else:
            home_d = tool_root + "/" + str(d.get("home") or dpath.split("/")[-2]).strip("/")
            pats_w = []
            for r in withheld:
                inc = r.get("include")
                pats_w += inc if isinstance(inc, list) else [inc] if inc else []
            files = [p for p in tracked if p.startswith(home_d + "/")
                     and not any(fnmatch.fnmatchcase(p[len(home_d) + 1:], w) for w in pats_w)]
        kits.append({"path": dpath, "id": d.get("id") or dpath, "home": home_d, "layer": d.get("layer"),
                     "optional": [o for o in d.get("optional") or [] if isinstance(o, dict)],
                     "requires_if": [e for e in d.get("requires_if") or [] if isinstance(e, dict)],
                     "files": sorted(set(files))})
    return kits


def derive_string_constants(tree):
    """-> [(value, line)] of every string constant but a docstring or a bare string statement."""
    bare = {id(n.value) for n in ast.walk(tree) if isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant)}
    return [(n.value, n.lineno) for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in bare]


def derive_edges(root, kits, rows):
    """-> [(file, line, kind, source kit, target kit, allowed)], every edge from a core kit's shipped
    file to a non-core kit, sorted."""
    by_tag = {r.get("tag"): r for r in rows}
    core = lambda k: by_tag.get(k["layer"], {}).get("kind") == "core"  # noqa: E731
    homes = {}  # home basename -> (kit name, core?)
    for k in kits:
        if k["home"]:
            homes[k["home"].rsplit("/", 1)[-1]] = (k["id"], core(k))
    for r in rows:
        for h in r.get("homes") or []:
            homes[h] = (h, r.get("kind") == "core")
    far = {h: name for h, (name, is_core) in homes.items() if not is_core}
    near_dirs = {k["home"] for k in kits if k["home"] and core(k)}
    by_id = {k["id"]: k for k in kits}
    tool_root = next((k["home"].rsplit("/", 1)[0] for k in kits if k["home"]), "tools")
    modules = {}  # module file name -> the non-core homes holding it at their top level
    for h in far:
        d = root / tool_root / h
        for p in (d.iterdir() if d.is_dir() else []):
            if p.suffix in (".py", ".sh") and p.is_file():
                modules.setdefault(p.name, []).append(h)
    seg = re.compile(r"(?:^|[^\w.-])(%s)/" % "|".join(re.escape(h) for h in sorted(far, key=len, reverse=True))) if far else None
    # ponytail: precedence keeps one edge per file, line and target, the kind that names it most exactly
    precedence = ("requires-if", "import", "dynamic", "copy", "shell", "probe")
    rkd = re.compile(r"""resolve_kit_dir(?:\(\s*|\s+(?:"[^"]*"|\S+)\s+)["']?([\w.-]+)""")
    token = re.compile(r"[\w.-]+\.(?:py|sh)\b")
    runs = re.compile(r"""(?:^|[\s;&|(`])(?:bash|sh|exec|source|python3?|"?\$\{?\w*(?:py|PY)\w*\}?"?)\s+["'$\w./{-]""")
    cp = re.compile(r"(?:^|[\s;&|(])cp\s")
    alt = "|".join(re.escape(h) for h in sorted(far, key=len, reverse=True)) or "(?!)"
    bare = re.compile(r"""(?:^|[\s"'=(])(%s)(?=["'\s;)]|$)""" % alt)

    def derive_named_homes(text):
        return [m.group(1) for m in seg.finditer(text)] if seg else []

    def derive_module_homes(name, own_dir):
        if (root / own_dir / name).is_file() or any((root / d / name).is_file() for d in near_dirs):
            return []
        return modules.get(name, [])

    edges = {}

    def add_edge(f, line, kind, src, home):
        key = (f, line, far[home])
        if key not in edges or precedence.index(kind) < precedence.index(edges[key][0]):
            edges[key] = (kind, src)

    for k in kits:
        if not core(k):
            continue
        for e in k["requires_if"]:
            other = by_id.get(e.get("kit"))
            if other and not core(other):
                text = (root / k["path"]).read_text(encoding="utf-8").splitlines()
                line = next((i for i, t in enumerate(text, 1) if 'kit = "%s"' % e["kit"] in t), 1)
                key = (k["path"], line, other["id"])
                edges[key] = ("requires-if", k)
        for f in k["files"]:
            own = f.rsplit("/", 1)[0] if "/" in f else ""
            path = root / f
            if f.endswith(".py"):
                try:
                    rows_i = import_walk.scan_imports(str(path))
                    tree = ast.parse(path.read_text(encoding="utf-8"), filename=f)
                except (OSError, UnicodeDecodeError, SyntaxError, ValueError):
                    continue
                for name, line, kind in rows_i:
                    if kind == "dynamic" and ("/" in name or "\\" in name):
                        for h in derive_named_homes(name.replace("\\", "/")):
                            add_edge(f, line, "dynamic", k, h)
                        continue
                    for h in derive_module_homes(name.split(".")[0] + ".py", own):
                        add_edge(f, line, "dynamic" if kind == "dynamic" else "import", k, h)
                for node in ast.walk(tree):
                    if not isinstance(node, ast.Call):
                        continue
                    fn = node.func
                    called = fn.id if isinstance(fn, ast.Name) else (fn.attr if isinstance(fn, ast.Attribute) else "")
                    if called == "resolve_kit_dir" and node.args and isinstance(node.args[0], ast.Constant) \
                            and node.args[0].value in far:
                        add_edge(f, node.lineno, "probe", k, node.args[0].value)
                    elif called in COPY_CALLS and node.args:
                        for v, _l in derive_string_constants(node.args[0]):
                            for h in derive_named_homes(v) + derive_module_homes(v.rsplit("/", 1)[-1], own):
                                add_edge(f, node.lineno, "copy", k, h)
                for v, line in derive_string_constants(tree):
                    for h in derive_named_homes(v):
                        add_edge(f, line, "probe", k, h)
                for node in ast.walk(tree):  # a bare home name handed to a call or bound to a name
                    vals = node.args if isinstance(node, ast.Call) else [node.value] if isinstance(node, ast.Assign) else []
                    for v in vals:
                        if isinstance(v, ast.Constant) and v.value in far:
                            add_edge(f, v.lineno, "probe", k, v.value)
            elif f.endswith(".sh") or check_shell_file(path):
                try:
                    text = path.read_text(encoding="utf-8").splitlines()
                except (OSError, UnicodeDecodeError):
                    continue
                inline = False  # an inlined copy of a shared primitive is the shared directory's, no kit's
                for line, t in enumerate(text, 1):
                    if t.startswith("# >>> ") or t.startswith("# <<< "):
                        inline = t.startswith("# >>> ")
                    if inline or t.lstrip().startswith(("#", "echo ")):
                        continue
                    probed = [m.group(1) for m in rkd.finditer(t) if m.group(1) in far]
                    copied = cp.search(t)
                    kind = "probe" if probed else "copy" if copied else "shell" if runs.search(t) else "probe"
                    unquoted = re.sub(r""""[^"]*"|'[^']*'""", '""', t)
                    hits = derive_named_homes(t) + probed + [m.group(1) for m in bare.finditer(unquoted)]
                    if copied:
                        hits += [h for m in token.findall(t) for h in derive_module_homes(m.rsplit("/", 1)[-1], own)]
                    for h in hits:
                        add_edge(f, line, kind, k, h)
    out = []
    for (f, line, target), (kind, src) in sorted(edges.items()):
        parts = {o.get("part") for o in src["optional"]}
        rel = f[len(src["home"]) + 1:] if src["home"] and f.startswith(src["home"] + "/") else f
        out.append((f, line, kind, src["id"], target, f in parts or rel in parts))
    return out


def check_shell_file(path):
    """-> True for a file with no `.sh` suffix whose first line is a shell's `#!`, such as a git hook."""
    try:
        with open(path, "rb") as fh:
            first = fh.readline(200)
    except OSError:
        return False
    return first.startswith(b"#!") and b"sh" in first and b"python" not in first and b"node" not in first


def check_rows(rows):
    """-> the contract's reds over the register's rows alone: shape, kind, parent, definition, the
    points used and declared, and EX-1."""
    reds = []
    by_tag = {}
    for r in rows:
        tag = r.get("tag")
        if not isinstance(tag, str) or not TAG.match(tag):
            reds.append("row %r: its tag is not layer.<seg>(.<seg>)*" % (tag,))
        if tag in by_tag:
            reds.append("row '%s': registered twice" % tag)
        by_tag.setdefault(tag, r)
        if r.get("kind") not in LAYER_KINDS:
            reds.append("row '%s': kind %r is not one of %s" % (tag, r.get("kind"), ", ".join(LAYER_KINDS)))
        if r.get("kind") == "optional" and not any(o.get("tag") == r.get("of") and o.get("kind") == "core" for o in rows):
            reds.append("row '%s': an optional row's `of` must name a core row, and names %r" % (tag, r.get("of")))
        if not str(r.get("definition") or "").strip():
            reds.append("row '%s': its definition is empty" % tag)
    declared = {}
    for r in rows:
        for p in r.get("declares") or []:
            declared.setdefault(p, []).append(r)
            if r.get("kind") != "core":
                reds.append("row '%s' (%s) declares %s: only a core row declares a point (EX-1)" % (r.get("tag"), r.get("kind"), p))
    for r in rows:
        for p in r.get("uses") or []:
            reds += check_point(p, "row '%s' uses" % r.get("tag"), declared)
    return reds


def check_point(point, who, declared):
    """-> the reds for one point a row uses or a descriptor's `optional` row names."""
    owners = declared.get(point, [])
    far = [o for o in owners if o.get("kind") != "core"]
    near = [o for o in owners if o.get("kind") == "core"]
    if far:
        return ["%s %s, which '%s' declares, a non-core row: an expansion meets the core only at a core point (EX-1)"
                % (who, point, "', '".join(o.get("tag") for o in far))]
    if len(near) != 1:
        return ["%s %s, which %d core row(s) declare: exactly one must" % (who, point, len(near))]
    return []


def check_layers(root, tool_root, register, listing=False):
    """-> (lines, rc) for the contract, the edges and EX-1 over the tree at root."""
    try:
        reg = read_layers(register)
        tracked = derive_tracked(root)
        kits = read_descriptors(root, tool_root, tracked)
    except Unreadable as e:
        return ["layers: UNREADABLE %s" % e], 2
    rows = [r for r in reg["layer"] if isinstance(r, dict)]
    reds = check_rows(rows)
    by_tag = {r.get("tag"): r for r in rows}
    declared = {}
    for r in rows:
        for p in r.get("declares") or []:
            declared.setdefault(p, []).append(r)
    for k in kits:
        if not k["layer"]:
            reds.append("descriptor %s declares no layer" % k["path"])
        elif k["layer"] not in by_tag:
            reds.append("descriptor %s names layer '%s', which no row holds" % (k["path"], k["layer"]))
        for o in k["optional"]:
            reds += check_point(o.get("point"), "descriptor %s's optional row for %r names" % (k["path"], o.get("part")), declared)
    for r in rows:
        if r.get("kind") == "core" and not any(k["layer"] == r.get("tag") for k in kits):
            reds.append("row '%s': a core layer with no kit" % r.get("tag"))
    covered = {k["home"] for k in kits if k["home"]}
    covered |= {tool_root + "/" + h for r in rows for h in r.get("homes") or []}
    covered |= {tool_root + "/" + s for s in reg["shared"]}
    dirs = {tool_root + "/" + p[len(tool_root) + 1:].split("/", 1)[0]
            for p in tracked if p.startswith(tool_root + "/") and "/" in p[len(tool_root) + 1:]}
    for d in sorted(dirs):
        if d not in covered:
            reds.append("tool directory %s is no descriptor's home, no row's homes entry and no shared entry" % d)
    edges = derive_edges(root, kits, rows)
    lines = []
    if listing:
        for r in rows:
            lines.append("layers: row %s · %s · kits: %s" % (r.get("tag"), r.get("kind"),
                         " ".join(k["id"] for k in kits if k["layer"] == r.get("tag")) or "none"))
        for k in kits:
            lines.append("layers: kit %s · %s · %s" % (k["id"], k["path"], k["layer"] or "NO LAYER"))
        for f, line, kind, src, target, ok in edges:
            lines.append("layers: edge %s:%d · %s · %s -> %s · %s" % (f, line, kind, src, target, "allowed" if ok else "red"))
    for red in reds:
        lines.append("layers: RED %s" % red)
    for f, line, kind, src, target, ok in edges:
        if not ok:
            lines.append("layers: RED %s:%d · %s · core kit %s depends on non-core kit %s, and no optional row of its descriptor names the file as part"
                         % (f, line, kind, src, target))
    n_red = sum(1 for e in edges if not e[5])
    counts = " · ".join("%s %d" % (kd, sum(1 for e in edges if e[2] == kd)) for kd in KINDS)
    lines.append(NOT_READ)
    lines.append("layers: %d layer row(s), %d kit descriptor(s); edges by kind: %s; %d allowed, %d red; %d contract red(s)"
                 % (len(rows), len(kits), counts, len(edges) - n_red, n_red, len(reds)))
    return lines, (1 if reds or n_red else 0)


def write_layer_row(register, tag, kind, of, definition):
    """-> (lines, rc). Append one row the contract admits, or refuse naming why."""
    try:
        reg = read_layers(register)
    except Unreadable as e:
        return ["layers: UNREADABLE %s" % e], 2
    rows = [r for r in reg["layer"] if isinstance(r, dict)]
    if any(r.get("tag") == tag for r in rows):
        return ["layers: REFUSED '%s' is already registered" % tag], 1
    row = {"tag": tag, "kind": kind, "definition": definition, "declares": [], "uses": []}
    if of:
        row["of"] = of
    reds = check_rows(rows + [row])
    reds = [r for r in reds if r not in check_rows(rows)]
    if reds:
        return ["layers: REFUSED %s" % r for r in reds], 1
    text = "\n[[layer]]\ntag = %s\nkind = %s\n" % (json.dumps(tag), json.dumps(kind))
    if of:
        text += "of = %s\n" % json.dumps(of)
    text += "definition = %s\ndeclares = []\nuses = []\n" % json.dumps(definition, ensure_ascii=False)
    with open(register, "a", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return ["layers: registered %s (%s) in %s" % (tag, kind, pathlib.Path(register).as_posix()),
            "layers: a kit joins it with the descriptor key: layer = %s" % json.dumps(tag)], 0


PLANTS = ("import", "dynamic", "probe", "copy", "shell", "requires-if", "unslotted", "slotted",
          "ex1-pair", "no-layer", "unknown-layer", "undeclared-point")


def build_layers_fixture(top, plant):
    """Write a scratch tree of three kits under a three-row register at `top`, with `plant` staged.
    -> the register's path."""
    rows = [
        ("layer.core", "core", None, ["point.core.slot"], []),
        ("layer.core.map", "optional", "layer.core", [], []),
        ("layer.exp", "expansion", None, [], ["point.core.missing" if plant == "undeclared-point" else
                                              "point.exp.hook" if plant == "ex1-pair" else "point.core.slot"]),
    ]
    if plant == "ex1-pair":
        rows.append(("layer.exp2", "expansion", None, ["point.exp.hook"], []))
    reg = "shared = []\n"
    for tag, kind, of, dec, use in rows:
        reg += "\n[[layer]]\ntag = %s\nkind = %s\n%sdefinition = \"fixture\"\ndeclares = %s\nuses = %s\n" % (
            json.dumps(tag), json.dumps(kind), "of = %s\n" % json.dumps(of) if of else "", json.dumps(dec), json.dumps(use))
    (top / "layers.toml").write_text(reg, encoding="utf-8")
    core_desc = 'id = "corekit"\nhome = "corekit"\nlayer = "layer.core"\n'
    if plant == "slotted":
        core_desc += 'optional = [{ part = "core.py", point = "point.core.slot", fallback = "renders not-installed" }]\n'
    if plant == "requires-if":
        core_desc += 'requires_if = [{ kit = "expkit", why = "fixture" }]\n'
    map_layer = {"no-layer": "", "unknown-layer": 'layer = "layer.nowhere"\n'}.get(plant, 'layer = "layer.core.map"\n')
    core_py = "import os\n\n\ndef read():\n    return os.sep\n"
    core_py += {
        "import": "\n\ndef late():\n    import reader\n    return reader\n",
        "dynamic": "\n\ndef late():\n    import importlib\n    a = __import__(\"reader\")\n    return a, importlib.import_module(\"reader\")\n",
        "probe": "\n\ndef late(here):\n    return resolve_kit_dir(\"mapkit\", \"reader.py\", here)\n",
        "copy": "\n\ndef late(kit, dst):\n    import shutil\n    shutil.copyfile(os.path.join(kit, \"reader.py\"), dst)\n",
        "unslotted": "\nfrom reader import read as read_map\n",
        "slotted": "\nfrom reader import read as read_map\n",
    }.get(plant, "")
    core_sh = "#!/usr/bin/env bash\n# bash tools/expkit/go.sh in a comment is no edge\necho core\n"
    if plant == "shell":
        core_sh += 'bash "$ROOT/tools/expkit/go.sh"\n'
    files = {
        "tools/corekit/kit.toml": core_desc,
        "tools/corekit/core.py": core_py,
        "tools/corekit/run.sh": core_sh,
        "tools/mapkit/kit.toml": 'id = "mapkit"\nhome = "mapkit"\n' + map_layer,
        "tools/mapkit/reader.py": "def read():\n    return 1\n",
        "tools/expkit/kit.toml": 'id = "expkit"\nhome = "expkit"\nlayer = "layer.exp"\n',
        "tools/expkit/go.sh": "#!/usr/bin/env bash\necho go\n",
    }
    for rel, text in files.items():
        p = top / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    return top / "layers.toml"


def main(argv):
    args = list(argv)

    def read_flag(flag):
        if flag not in args:
            return None
        i = args.index(flag)
        if i + 1 >= len(args):
            raise SystemExit("layers: %s takes a value" % flag)
        val = args[i + 1]
        del args[i:i + 2]
        return val

    listing = "--list" in args
    tool_root_abs = HERE.parent
    if "--new" in args:
        tag, kind, of, definition = read_flag("--new"), read_flag("--kind"), read_flag("--of"), read_flag("--definition")
        if not tag or not kind or definition is None:
            sys.stderr.write("usage: check_layers.py --new <tag> --kind <kind> [--of <tag>] --definition <text>\n")
            return 2
        lines, rc = write_layer_row(HERE / "layers.toml", tag, kind, of, definition)
    elif "--fixture" in args:
        plant = read_flag("--plant")
        if plant is not None and plant not in PLANTS:
            sys.stderr.write("layers: no plant %r; the plants are %s\n" % (plant, ", ".join(PLANTS)))
            return 2
        top = pathlib.Path(tempfile.mkdtemp(prefix="layers-fixture-"))
        try:
            register = build_layers_fixture(top, plant)
            lines, rc = check_layers(top, "tools", register, listing)
            lines.insert(0, "layers: fixture, plant %s" % (plant or "none (the control)"))
        finally:
            shutil.rmtree(top, ignore_errors=True)
    else:
        root = next((d for d in (tool_root_abs, *tool_root_abs.parents) if (d / ".git").exists()), None)
        if root is None:
            sys.stderr.write("layers: no work tree above %s\n" % tool_root_abs.as_posix())
            return 2
        lines, rc = check_layers(root, tool_root_abs.relative_to(root).as_posix(), HERE / "layers.toml", listing)
    for line in lines:
        sys.stdout.buffer.write((line + "\n").encode("utf-8"))
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
