"""tag_index — the tag grammar, the namespace registry and the derived SQLite tag index (PLAY-dOrderedCharter-19).

THE GRAMMAR. A tag is `<ns>.<seg>(.<seg>)*`, each `seg` `[a-z0-9][a-z0-9-]*`, at most TAG_MAX_BYTES bytes;
`<ns>` is a word the registry, `namespaces.toml` beside this file, declares, never one typed here. A
document section is `doc.<name>#<seg>`, its `<seg>` the `##` heading folded by `derive_heading_seg`.

THE INDEX is `<git-common-dir>/gov/index-s<INDEX_SCHEMA>.db`, `derive_index_path`'s, one file per node
that every worktree of the repository shares, written by the extractors alone through `build_index`, never committed: deleting it costs one
rebuild. Its tables, keyed by blob or by path and blob so a later build can add its own beside them:

  tree_path(tree, path, blob)                               the paths a built tree holds
  blob_row(blob, extractor, version, tag, kind, line, end_line, text)  what a blob holds, at any path
  path_row(path, blob, extractor, version, conf, tag, kind, line)  what a path names under one conf
  dirty_path(worktree, path, blob)                           a worktree's uncommitted edits to tracked files
  tree_built(tree, versions, built_at)                       the freshness key of a tree
  blob_parsed(blob, extractor, version)                      the freshness key of a blob (PLAY-dOrderedCharter-44)

A blob row's tag `""` or `#<seg>` is relative to the name its path gives it (a document's `doc.<name>`),
so one blob at two paths is parsed once and named twice; every other tag is whole. A `blob_parsed` row
marks a blob read by one extractor at one version, written when the run yields nothing too, so a build
runs each extractor over the blobs it has not read at its current version: a newly registered extractor
reads old blobs. A `parsed` path row marks a (path, blob, extractor, version) quadruple named. The file is
stamped `PRAGMA user_version = INDEX_SCHEMA`, and the schema is in its name, so two schemas never share one
file; a file of another stamp is rebuilt in place, its tables dropped and created again inside one
`BEGIN IMMEDIATE` transaction and the file never unlinked, so a reader holding it keeps it
(PLAY-dOrderedCharter-55 S16).

EACH VERSION'S ROWS STAND APART (PLAY-dOrderedCharter-51). Every worktree shares the file and two of them
can carry different extractor bytes, so a build never deletes a row of another version: the rows of two
versions of one extractor over one blob sit side by side. A worktree's `{extractor: version}` map is its
own, and every read is joined to it through the temp table `view_version`, so a worktree is served only
rows its own extractor bytes wrote. A tree is fresh under `tree_built(tree, versions)`, `versions` the
digest of that map and of the conf key (`derive_versions_digest`). `gov_tag.py --gc` collects the versions
and conf keys no live worktree derives; a plain build collects none.

THE CONF KEYS WHAT A PATH NAMES (PLAY-dOrderedCharter-70 S8). `MEMORY_ROOT` and `CHARTER` decide which
path is `doc.charter` and which are guides, so `derive_conf_key` folds both into `path_row`'s `conf`, into
the freshness digest, and into every read through the temp table `view_conf`: a conf edit, committed or
not, is served the names its own conf gives. `blob_row` is keyed by text alone and needs no key.

AN EXTRACTOR'S VERSION is derived, never typed: the first 12 hex of the SHA-256 over the bytes of the
module file defining it and of every module of its import closure, in path order, the closure from
memory-tree's `import_walk.derive_module_closure` over the module's own directory, then memory-tree's
(PLAY-dOrderedCharter-55 S15), so a helper's edit re-runs every extractor importing it. `--gc` reads
another worktree's modules through this worktree's memory-tree directory.

AN EXTRACTOR is `<module>:<function>`, called `fn(ctx, path, None)` to ask whether it reads `path` (the
path's name, `""` for none, or None when it does not read it) and `fn(ctx, path, text)` for the rows,
each `(tag, kind, line, end_line, text)`. A module other than this one is loaded from the registry's
directory. `extract_citations` runs over every path whatever the registry says.

THE OVERLAY. A worktree's uncommitted edits to tracked files are its own `dirty_path` rows, keyed by the
worktree's top-level path and served to that worktree alone; the freshness key exempts them.
"""
from __future__ import annotations

import collections
import fnmatch
import functools
import hashlib
import importlib.util
import os
import pathlib
import re
import sqlite3
import subprocess
import sys
import time
import tomllib

KIT_DIR = pathlib.Path(os.path.abspath(__file__)).parent
if str(KIT_DIR) not in sys.path:
    sys.path.insert(0, str(KIT_DIR))


# >>> resolve_prefix_token -- canonical copy: resolve_prefix_token.py in the gov lib dir (byte-identical; gated)
def resolve_prefix_token(spelled, troot):
    """<spelled> with its {prefix} token resolved against the tool root <troot>.

    An empty or "." root is a root install: the token drops with its slash, and a bare token
    becomes ".". Any other root replaces the token. Text with no token passes unchanged.
    """
    spelled = str(spelled)
    if not troot or troot == ".":
        return spelled.replace("{prefix}/", "").replace("{prefix}", ".")
    return spelled.replace("{prefix}", troot)
# <<< resolve_prefix_token


TAG_MAX_BYTES = 64
SEG = r"[a-z0-9][a-z0-9-]*"
TAG_RE = re.compile(rf"{SEG}(?:\.{SEG})+")
SEG_RE = re.compile(SEG)
#: a span that may be a citation (`<tag>` or `<tag>#<seg>`) or a bare reference (`<seg>(.<seg>)*`)
SPAN_RE = re.compile(rf"{SEG}(?:\.{SEG})*(?:#{SEG})?")
DEFINE_KINDS = ("doc", "section", "tag")
SCHEMA = """
CREATE TABLE IF NOT EXISTS tree_path(tree TEXT, path TEXT, blob TEXT, PRIMARY KEY(tree, path));
CREATE INDEX IF NOT EXISTS tree_path_blob ON tree_path(blob);
CREATE TABLE IF NOT EXISTS blob_row(blob TEXT, extractor TEXT, version TEXT NOT NULL, tag TEXT, kind TEXT,
                                    line INTEGER, end_line INTEGER, text TEXT);
CREATE INDEX IF NOT EXISTS blob_row_key ON blob_row(blob, extractor, version);
CREATE TABLE IF NOT EXISTS path_row(path TEXT, blob TEXT, extractor TEXT, version TEXT NOT NULL,
                                    conf TEXT NOT NULL, tag TEXT, kind TEXT, line INTEGER);
CREATE INDEX IF NOT EXISTS path_row_key ON path_row(path, blob);
CREATE INDEX IF NOT EXISTS path_row_tag ON path_row(tag);
CREATE TABLE IF NOT EXISTS dirty_path(worktree TEXT, path TEXT, blob TEXT, PRIMARY KEY(worktree, path));
CREATE TABLE IF NOT EXISTS tree_built(tree TEXT NOT NULL, versions TEXT NOT NULL, built_at TEXT NOT NULL,
                                      PRIMARY KEY(tree, versions));
CREATE TABLE IF NOT EXISTS blob_parsed(blob TEXT NOT NULL, extractor TEXT NOT NULL, version TEXT NOT NULL,
                                       PRIMARY KEY(blob, extractor, version));
"""
#: the index file's `PRAGMA user_version` and the number in its name; a file stamped otherwise is rebuilt in place
INDEX_SCHEMA = 3
#: SQLite's busy timeout, seconds: a second writer waits this long on the first, then the verb exits 2.
BUSY_TIMEOUT = 60


class TagError(RuntimeError):
    """A refusal: an unreadable registry, an extractor that does not load, a locked index, a git failure."""


def parse_tag(text: str, namespaces=None):
    """-> ((ns, [seg, ...]), None) for a tag, or (None, the rule it breaks). With `namespaces`, a set of
    registered words, a namespace outside it is a broken rule too."""
    if len(text.encode("utf-8")) > TAG_MAX_BYTES:
        return None, f"longer than {TAG_MAX_BYTES} bytes ({len(text.encode('utf-8'))})"
    parts = text.split(".")
    if len(parts) < 2:
        return None, "no namespace: a tag is <ns>.<seg>(.<seg>)*"
    for seg in parts:
        if not seg:
            return None, "an empty segment"
        if not SEG_RE.fullmatch(seg):
            return None, f"segment '{seg}' is outside [a-z0-9][a-z0-9-]*"
    if namespaces is not None and parts[0] not in namespaces:
        return None, f"namespace '{parts[0]}' is not registered"
    return (parts[0], parts[1:]), None


REGISTRY_FIELDS = ("ns", "owner", "layer", "source", "extractor", "role", "purpose-source", "join-armed-by")


def read_namespaces(path) -> list[dict]:
    """The registry's `[[namespace]]` rows, each carrying every field of REGISTRY_FIELDS, or TagError. A row
    whose `ns` is outside `seg` is returned: `derive_context` keeps it out of every pattern and the shape
    check reds it by name (PLAY-dOrderedCharter-10 S3)."""
    path = pathlib.Path(path)
    try:
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("namespace") or []
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise TagError(f"the namespace registry {path.as_posix()} is unreadable: {exc}") from None
    seen: set[str] = set()
    for i, row in enumerate(rows, 1):
        missing = [f for f in REGISTRY_FIELDS if not isinstance(row.get(f), str) or not row.get(f)]
        if missing:
            raise TagError(f"{path.as_posix()}: namespace row {i} lacks {', '.join(missing)}")
        if row["ns"] in seen:
            raise TagError(f"{path.as_posix()}: namespace '{row['ns']}' is registered twice")
        if row["role"] not in ("selects", "describes"):
            raise TagError(f"{path.as_posix()}: namespace '{row['ns']}' has role '{row['role']}', not selects or describes")
        if ":" not in row["extractor"]:
            raise TagError(f"{path.as_posix()}: namespace '{row['ns']}' extractor is not <module>:<function>")
        seen.add(row["ns"])
    return rows


CITATIONS = "tag_index:extract_citations"


def resolve_extractor_module(mod_name, registry_dir) -> pathlib.Path:
    """The file defining `<module>`: `<module>.py` beside the registry, or the one of this file's own kit
    directory, `tag_index` and `instruction_units` among them, for a module the registry's directory does
    not hold (a fixture's). `--gc` reads another worktree's map, so its modules are that worktree's copies."""
    own = pathlib.Path(registry_dir) / f"{mod_name}.py"
    kit = pathlib.Path(os.path.abspath(__file__)).parent / f"{mod_name}.py"
    if not own.is_file() and kit.is_file():
        return kit
    return own


def derive_extractor_versions(namespaces, registry_dir) -> dict:
    """{'<module>:<function>': version} for every row's extractor and extract_citations, each module file
    hashed once (PLAY-dOrderedCharter-44 S3) with its import closure (PLAY-dOrderedCharter-55 S15). An
    unreadable or unparsable module of a closure refuses, naming the row."""
    tree_lib, _ = load_memory_tree()
    import import_walk  # memory-tree's, on the path load_memory_tree put it on
    mt = str(pathlib.Path(tree_lib.__file__).parent)
    by_file: dict = {}
    out = {}
    for name, ns in [(CITATIONS, "")] + [(r["extractor"], r["ns"]) for r in namespaces]:
        src = resolve_extractor_module(name.partition(":")[0], registry_dir)
        if src not in by_file:
            try:
                digest = hashlib.sha256()
                for path in import_walk.derive_module_closure(str(src), [str(src.parent), mt]):
                    digest.update(pathlib.Path(path).read_bytes())
                by_file[src] = digest.hexdigest()[:12]
            except (OSError, SyntaxError, ValueError) as exc:
                raise TagError(f"namespace '{ns}' extractor {name}: its module {src.as_posix()} or a module it "
                               f"imports is unreadable: {getattr(exc, 'strerror', None) or exc}") from None
        out[name] = by_file[src]
    return out


def derive_conf_key(memory_root, charter) -> str:
    """The first 12 hex of the SHA-256 of the conf's MEMORY_ROOT and CHARTER: `path_row`'s `conf` key."""
    return hashlib.sha256(f"{memory_root}\n{charter}".encode("utf-8")).hexdigest()[:12]


def derive_versions_digest(versions, conf) -> str:
    """The first 12 hex of the SHA-256 of a map's `extractor=version` pairs, sorted and joined by newlines,
    then a `conf=<key>` line: the `versions` key of `tree_built` (PLAY-dOrderedCharter-51 S4, -70 S8)."""
    text = "\n".join(sorted(f"{e}={v}" for e, v in versions.items())) + f"\nconf={conf}"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def load_extractors(namespaces, registry_dir) -> dict:
    """{'<module>:<function>': callable} for every row's extractor, and extract_citations."""
    out = {CITATIONS: extract_citations}
    for row in namespaces:
        name = row["extractor"]
        if name in out:
            continue
        mod_name, _, fn_name = name.partition(":")
        if mod_name == "tag_index":
            mod = sys.modules[__name__]
        else:
            src = resolve_extractor_module(mod_name, registry_dir)
            spec = importlib.util.spec_from_file_location(f"tag_extractor_{mod_name}", src)
            if spec is None or not src.is_file():
                raise TagError(f"extractor {name}: no module {src.as_posix()}")
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
        fn = getattr(mod, fn_name, None)
        if not callable(fn):
            raise TagError(f"extractor {name}: no function {fn_name}")
        out[name] = fn
    return out


# ------------------------------------------------------------------------------------------ the extractors

def derive_heading_seg(text: str) -> str:
    """A heading's section `<seg>`: lower-cased, each run outside [a-z0-9] one hyphen, the ends trimmed."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def scan_unfenced(text: str, unclosed: list | None = None):
    """(line number, line) for every line of Markdown `text` outside a fence, through memory-tree's one fence
    reader; the line an unclosed fence opens at goes to `unclosed`, a caller that does not ask reading on.
    Joining `str.splitlines` keeps this walker's line numbers across a form feed or a CRLF."""
    tree_lib, _ = load_memory_tree()
    for n, line in tree_lib.unfenced_lines("\n".join(text.splitlines())):
        if line is not None:
            yield n, line
        elif unclosed is not None:
            unclosed.append(n)


def extract_doc(ctx, path, text=None):
    """The `doc` namespace: the charter (`doc.charter`), each `<MEMORY_ROOT>/guides/*.md`, `HYGIENE.md`
    and `TEMPLATE-SPEC.md` (`doc.<stem lower-cased>`); each `##` heading a section `#<seg>`. The document
    registry beside this one adds each row whose tag no file of those derives, a class of files or a
    Skill (PLAY-dOrderedCharter-3 S1). The reference declaration beside it adds each `[[reference]]` row's
    `registry` that opens `doc.reference.`, declared at that row (PLAY-dOrderedCharter-40 S4)."""
    if _read_kit_file(ctx, path, "references.toml"):
        if text is None:
            return ""
        return [r for r in derive_tag_rows(text, "reference") if r[0].startswith("doc.reference.")]
    if _read_kit_file(ctx, path, "documents.toml"):
        if text is None:
            return ""
        try:
            rows = tomllib.loads(text).get("document") or []
        except tomllib.TOMLDecodeError:
            return []
        derived = {r.get("tag") for r in rows if isinstance(r, dict) and r.get("tag") == extract_doc(
            ctx, str(r.get("path", "")).replace("{memory_root}", ctx["memory_root"]))}
        return [r for r in derive_tag_rows(text, "document") if r[0] not in derived]
    if text is None:
        mr = ctx["memory_root"]
        if path == ctx["charter"]:
            return "doc.charter"
        if not (fnmatch.fnmatchcase(path, f"{mr}/guides/*.md") and path.count("/") == mr.count("/") + 2
                or path in (f"{mr}/HYGIENE.md", f"{mr}/TEMPLATE-SPEC.md")):
            return None
        name = "doc." + pathlib.PurePosixPath(path).stem.lower()
        return name if parse_tag(name)[1] is None else None
    lines = text.splitlines()
    heads = [(n, line[3:].strip()) for n, line in scan_unfenced(text) if line.startswith("## ")]
    rows = [("", "doc", 1, len(lines), lines[0] if lines else "")]
    for i, (n, head) in enumerate(heads):
        end = heads[i + 1][0] - 1 if i + 1 < len(heads) else len(lines)
        seg = derive_heading_seg(head)
        if seg:
            rows.append((f"#{seg}", "section", n, end, "\n".join(lines[n - 1:end])))
    return rows


#: the extractors whose members are unit rows themselves, which a unit's `scope` never selects
UNIT_EXTRACTORS = ("instruction_units:extract_unit", "instruction_units:extract_repo")


#: the one table-to-key map both TOML row readers read: a table absent here keys its rows on `tag`
#: (PLAY-dOrderedCharter-40 S4, its section 8 F4)
ROW_TAG_KEYS = {"reference": "registry"}


def read_toml_tags(text, table):
    """(value, line, end_line) for each `[[table]]` row's string tag in TOML `text`, read under the table's
    ROW_TAG_KEYS key, else `tag`, unfiltered: the shape
    check, never the extractor, refuses a malformed value. The nth parsed row is the nth `[[table]]` header,
    `line` the first `tag =` key line inside its span and `end_line` the span's last non-blank line before the
    next `[` header (PLAY-dOrderedCharter-70 S3). Where the header count is not the row count, a header inside
    a multi-line string say, each row keeps line 1. A file that does not parse names nothing."""
    try:
        rows = tomllib.loads(text).get(table) or []
    except tomllib.TOMLDecodeError:
        return []
    lines = text.splitlines()
    key = ROW_TAG_KEYS.get(table, "tag")
    key_line = re.compile(rf"^\s*{re.escape(key)}\s*=")
    heads = [i for i, ln in enumerate(lines, 1) if ln.strip() == f"[[{table}]]"]
    cuts = [i for i, ln in enumerate(lines, 1) if ln.lstrip().startswith("[")] + [len(lines) + 1]
    out = []
    for k, row in enumerate(rows):
        val = row.get(key) if isinstance(row, dict) else None
        if not (isinstance(val, str) and val):
            continue
        if len(heads) != len(rows):
            out.append((val, 1, 1))
            continue
        span = range(heads[k] + 1, next(c for c in cuts if c > heads[k]))
        line = next((i for i in span if key_line.match(lines[i - 1])), heads[k])
        end = max((i for i in span if lines[i - 1].strip()), default=line)
        out.append((val, line, max(end, line)))
    return out


def derive_tag_rows(text, table):
    """Each row's tag, its `tag =` line through its span's end, and that text, as `extract_doc` serves a section."""
    lines = text.splitlines()
    return [(val, "tag", n, end, "\n".join(lines[n - 1:end]) if lines else "")
            for val, n, end in read_toml_tags(text, table)]


def _read_kit_file(ctx, path, name):
    return path == f"{ctx['kit']}/{name}"


def extract_reader(ctx, path, text=None):
    """The `reader` namespace: each `[[reader]]` row of `readers.toml` beside the registry."""
    if text is None:
        return "" if _read_kit_file(ctx, path, "readers.toml") else None
    return derive_tag_rows(text, "reader")


def extract_practice(ctx, path, text=None):
    """The `practice` namespace: each `[[practice]]` row of `practices.toml` (PLAY-dOrderedCharter-1)."""
    if text is None:
        return "" if _read_kit_file(ctx, path, "practices.toml") else None
    return derive_tag_rows(text, "practice")


def extract_layer(ctx, path, text=None):
    """The `layer` namespace: the `tag` of each `[[layer]]` row of `layers.toml`."""
    if text is None:
        return "" if _read_kit_file(ctx, path, "layers.toml") else None
    return derive_tag_rows(text, "layer")


def extract_principle(ctx, path, text=None):
    """The `principle` namespace: each `[[principle]]` row of `principles.toml` (PLAY-dOrderedCharter-7)."""
    if text is None:
        return "" if _read_kit_file(ctx, path, "principles.toml") else None
    return derive_tag_rows(text, "principle")


def extract_kind(ctx, path, text=None):
    """The `kind` namespace: each `[[kind]]` row of `kinds.toml` (PLAY-dOrderedCharter-7)."""
    if text is None:
        return "" if _read_kit_file(ctx, path, "kinds.toml") else None
    return derive_tag_rows(text, "kind")


def extract_level(ctx, path, text=None):
    """The `level` namespace: `level.<name>` for each name of the `LEVELS` tuple in `instruction_units.py`
    (PLAY-dOrderedCharter-13), at the tuple's line; a module that does not parse names nothing."""
    if text is None:
        return "" if _read_kit_file(ctx, path, "instruction_units.py") else None
    import ast
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return []
    lines = text.splitlines()
    for node in tree.body:
        if (isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "LEVELS" for t in node.targets)
                and isinstance(node.value, (ast.Tuple, ast.List))):
            n = node.lineno
            return [(f"level.{e.value}", "tag", n, n, lines[n - 1]) for e in node.value.elts
                    if isinstance(e, ast.Constant) and isinstance(e.value, str)]
    return []


def extract_kit(ctx, path, text=None):
    """The `kit` namespace: `kit.<id>` for the top-level `id` of each tracked `kit.toml` or `*.kit.toml`
    descriptor, at the `id` key's own line (§8 F5)."""
    if text is None:
        name = pathlib.PurePosixPath(path).name
        return "" if name == "kit.toml" or name.endswith(".kit.toml") else None
    try:
        kid = tomllib.loads(text).get("id")
    except tomllib.TOMLDecodeError:
        return []
    if not isinstance(kid, str) or not kid:
        return []
    lines = text.splitlines()
    n = next((i for i, ln in enumerate(lines, 1) if re.match(r"\s*id\s*=", ln)), 1)
    return [(f"kit.{kid}", "tag", n, n, lines[n - 1] if lines else "")]


CODE_SPAN_RE = re.compile(r"(`+)(.+?)(?<!`)\1(?!`)")
BRACKET_RE = re.compile(r"\[([^\[\]\n]+)\]")


def extract_citations(ctx, path, text=None):
    """Every whole backticked or bracketed span of tracked Markdown, outside fences, that SPAN_RE matches:
    kind `span`. Whether one is a citation, a bare reference or neither is decided at the read, against the
    registry, so the rows do not move when a namespace is registered. Nothing outside `.md` is read. A span
    row carries no text: its line is where `refs` points, and the index holds a few hundred thousand."""
    if text is None:
        return "" if path.endswith(".md") else None
    rows, unclosed = [], []
    for n, line in scan_unfenced(text, unclosed):
        rest = line
        for m in CODE_SPAN_RE.finditer(line):
            body = m.group(2)
            if len(m.group(1)) > 1 and body.startswith(" ") and body.endswith(" "):
                body = body[1:-1]
            if SPAN_RE.fullmatch(body):
                rows.append((body, "span", n, n, ""))
            rest = rest.replace(m.group(0), " " * len(m.group(0)), 1)
        for m in BRACKET_RE.finditer(rest):
            if SPAN_RE.fullmatch(m.group(1)):
                rows.append((m.group(1), "span", n, n, ""))
    return rows + [("", "unclosed", n, n, "") for n in unclosed]  # PLAY-dOrderedCharter-68: `check_unclosed` reads it


# ------------------------------------------------------------------------------------------ git and the db

def read_git_stdout(repo: pathlib.Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True,
        encoding="utf-8", errors="replace",
    ).stdout


git = read_git_stdout  # the name the inlined common_git_dir block calls


# >>> common_git_dir -- canonical copy: common_dir.py in the gov lib dir (byte-identical; gated)
def common_git_dir(repo: pathlib.Path) -> pathlib.Path:
    """The MAIN repository's git directory, shared by every worktree.

    ``--git-dir`` in a linked worktree is ``.git/worktrees/<name>``, which ``git worktree remove``
    deletes outright -- taking the query log with it. It is also RELATIVE (bare ``.git``) when run
    at the repo root and absolute elsewhere, so the raw value is not a usable path either way.
    """
    raw = git(repo, "rev-parse", "--git-common-dir").strip()
    p = pathlib.Path(raw)
    return p.resolve() if p.is_absolute() else (repo / raw).resolve()
# <<< common_git_dir


def read_git(root, *args) -> str:
    try:
        return read_git_stdout(pathlib.Path(root), *args)
    except (OSError, subprocess.CalledProcessError) as exc:
        detail = (getattr(exc, "stderr", "") or str(exc)).strip().splitlines()
        raise TagError(f"`git {' '.join(args)}` failed: {detail[0] if detail else exc}") from None


@functools.cache
def load_memory_tree():
    """memory-tree's `tree_lib` (the one `<rev>:<path>` reader) and `id_grammar` (its conf reader); this
    kit reaches them through its inline `resolve_kit_dir`, never a spelled sibling path. Cached: the fence
    walker calls it once per Markdown blob, and each call reads the install receipt."""
    from policy_value import resolve_kit_dir
    try:
        mt = resolve_kit_dir("memory-tree", "tree_lib.py", KIT_DIR)
    except LookupError as exc:
        raise TagError(f"the tag index reads blobs through memory-tree's tree_lib.py: {exc}") from None
    if str(mt) not in sys.path:
        sys.path.append(str(mt))
    import id_grammar
    import tree_lib
    return tree_lib, id_grammar


def derive_index_path(root) -> pathlib.Path:
    """The node's index file, `<git-common-dir>/gov/index-s<INDEX_SCHEMA>.db`, the one spelling every code
    reader uses: two schemas never share a file (PLAY-dOrderedCharter-55 S16)."""
    return common_git_dir(pathlib.Path(root)) / "gov" / f"index-s{INDEX_SCHEMA}.db"


def load_index(root, reset=False) -> sqlite3.Connection:
    """The node's index at `derive_index_path`, created on first use. WAL off: every worktree opens the one
    file, and SQLite's lock serialises the writers. A file holding tables under a `user_version` other than
    INDEX_SCHEMA, or any file under `reset`, has every table dropped and created again in place inside one
    `BEGIN IMMEDIATE` transaction, never unlinked, so a reader holding the file keeps it (S16); a stale
    stamp prints one line saying so."""
    db = derive_index_path(root)
    db.parent.mkdir(parents=True, exist_ok=True)
    try:
        con = sqlite3.connect(str(db), timeout=BUSY_TIMEOUT)
        con.execute("PRAGMA journal_mode=DELETE")
        old = con.execute("PRAGMA user_version").fetchone()[0]
        if (reset or old != INDEX_SCHEMA) and con.execute("SELECT 1 FROM sqlite_master LIMIT 1").fetchone():
            con.execute("BEGIN IMMEDIATE")
            try:
                old = con.execute("PRAGMA user_version").fetchone()[0]  # read again under the write lock
                if reset or old != INDEX_SCHEMA:
                    for (name,) in con.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall():
                        con.execute(f'DROP TABLE "{name}"')
                    for statement in SCHEMA.split(";"):
                        if statement.strip():
                            con.execute(statement)
                    con.execute(f"PRAGMA user_version = {INDEX_SCHEMA}")
                con.commit()
            except BaseException:
                con.rollback()
                raise
            if old != INDEX_SCHEMA:
                print(f"tag-index — rebuilt: schema {old} to {INDEX_SCHEMA}", file=sys.stderr)
        con.executescript(SCHEMA)
        con.execute(f"PRAGMA user_version = {INDEX_SCHEMA}")
    except (sqlite3.Error, OSError) as exc:
        raise TagError(f"the tag index {db.as_posix()} cannot be opened: {exc}") from None
    return con


def derive_context(root, registry) -> dict:
    """What every extractor and check reads: the conf's MEMORY_ROOT and CHARTER, the registry and its
    extractors, and the worktree's own top-level path."""
    _tree_lib, id_grammar = load_memory_tree()
    conf = id_grammar.load_conf(pathlib.Path(root))
    rows = read_namespaces(registry)
    # validate before splice: a word outside `seg` reaches no LIKE pattern and no word set, only a red
    namespaces = [r for r in rows if SEG_RE.fullmatch(r["ns"])]
    versions = derive_extractor_versions(namespaces, pathlib.Path(registry).parent)
    memory_root, charter = (conf.get("MEMORY_ROOT") or "memory").strip("/"), conf.get("CHARTER") or "AGENTS.md"
    key = derive_conf_key(memory_root, charter)
    return {
        "root": pathlib.Path(root),
        "memory_root": memory_root,
        "charter": charter,
        "conf": key,
        "kit": pathlib.Path(os.path.relpath(pathlib.Path(registry).parent, root)).as_posix(),
        "registry": pathlib.Path(os.path.relpath(registry, root)).as_posix(),
        "malformed": [r["ns"] for r in rows if not SEG_RE.fullmatch(r["ns"])],
        "namespaces": namespaces,
        "versions": versions,
        "digest": derive_versions_digest(versions, key),
        "extractors": load_extractors(namespaces, pathlib.Path(registry).parent),
        "worktree": derive_worktree_key(read_git(root, "rev-parse", "--show-toplevel").strip()),
    }


def derive_worktree_key(path) -> str:
    """A worktree's key in `dirty_path`: its top-level path with the slashes forward and a drive letter
    lower-cased, so the spelling `--show-toplevel` prints and the one `git worktree list` prints compare
    equal (PLAY-dOrderedCharter-55 S21)."""
    key = str(path).replace("\\", "/")
    return key[0].lower() + key[1:] if key[1:2] == ":" else key


def _write_parsed(con, ctx, blobs: dict, read_text, stats) -> None:
    """Run each extractor over each blob `blob_parsed` holds no row for at the extractor's current version;
    `blobs` maps blob -> [(path, extractor)]. A row of another version is never deleted: another worktree
    may derive it (PLAY-dOrderedCharter-51 S2). Counts into `stats`, load_view's."""
    versions = ctx["versions"]
    held = set(con.execute("SELECT blob, extractor, version FROM blob_parsed"))
    todo: dict = {}
    for blob, pe in blobs.items():
        done: set[str] = set()
        for path, ex in pe:
            if ex in done:
                continue
            done.add(ex)
            if (blob, ex, versions[ex]) in held:
                stats["skipped"][ex] += 1
            else:
                todo.setdefault(blob, []).append((path, ex))
    if not todo:
        return
    texts = read_text({b: pe[0][0] for b, pe in todo.items()})
    for blob, pe in todo.items():
        text = texts.get(blob)
        for path, ex in pe:
            rows = ctx["extractors"][ex](ctx, path, text) if text is not None else []
            con.executemany("INSERT INTO blob_row VALUES (?,?,?,?,?,?,?,?)",
                            [(blob, ex, versions[ex], *r) for r in rows])
            con.execute("INSERT OR REPLACE INTO blob_parsed VALUES (?,?,?)", (blob, ex, versions[ex]))
            stats["runs"][ex] += 1
    stats["parsed"] += len(todo)


def _write_path_rows(con, pairs, versions, conf) -> None:
    """Name every (path, blob, extractor, name) no `parsed` path row of the extractor's version in
    `versions` and of the conf key `conf` holds, from its blob's rows of that version."""
    for path, blob, ex, name in pairs:
        v = versions[ex]
        if con.execute("SELECT 1 FROM path_row WHERE path=? AND blob=? AND extractor=? AND version=? AND conf=? "
                       "AND kind='parsed'", (path, blob, ex, v, conf)).fetchone():
            continue
        rows = con.execute("SELECT tag, kind, line FROM blob_row WHERE blob=? AND extractor=? AND version=?",
                           (blob, ex, v)).fetchall()
        con.executemany("INSERT INTO path_row VALUES (?,?,?,?,?,?,?,?)",
                        [(path, blob, ex, v, conf, name + tag if (tag == "" or tag.startswith("#")) else tag, kind,
                          line) for tag, kind, line in rows] + [(path, blob, ex, v, conf, "", "parsed", 0)])


def _derive_applicable(ctx, entries):
    """[(path, blob, extractor, name)] for every extractor that reads a path of `entries`."""
    out = []
    for path, blob in entries:
        for ex, fn in ctx["extractors"].items():
            name = fn(ctx, path, None)
            if name is not None:
                out.append((path, blob, ex, name))
    return out


def build_index(root, tree, ctx, con, stats) -> None:
    """Index `tree` (a tree id) of the repository at `root`, unless `tree_built` already holds it under this
    worktree's `versions` digest (PLAY-dOrderedCharter-51 S4): one
    `git ls-tree -r`, then each extractor over each blob it has not read at its current version
    (`_write_parsed`), read through memory-tree's `read_blobs_at`, in one transaction. Then rows no tree
    or worktree holds are removed. Counts into `stats`, nothing for a tree already built."""
    if con.execute("SELECT 1 FROM tree_built WHERE tree=? AND versions=?", (tree, ctx["digest"])).fetchone():
        return
    tree_lib, _ = load_memory_tree()
    entries = []
    for rec in read_git(root, "ls-tree", "-r", "-z", "--full-tree", tree).split("\0"):
        meta, _, path = rec.partition("\t")
        fields = meta.split()
        if path and len(fields) == 3 and fields[1] == "blob":
            entries.append((path, fields[2]))
    pairs = _derive_applicable(ctx, entries)
    blobs: dict = {}
    for path, blob, ex, _name in pairs:
        blobs.setdefault(blob, []).append((path, ex))

    def read_text(want):
        try:
            got = tree_lib.read_blobs_at(root, [(tree, p) for p in want.values()])
        except OSError as exc:
            raise TagError(f"the blobs of tree {tree[:12]} cannot be read: {exc}") from None
        return {b: got.get((tree, p)) for b, p in want.items()}

    try:
        with con:
            con.execute("DELETE FROM tree_path WHERE tree=?", (tree,))
            con.executemany("INSERT INTO tree_path VALUES (?,?,?)", [(tree, p, b) for p, b in entries])
            _write_parsed(con, ctx, blobs, read_text, stats)
            _write_path_rows(con, pairs, ctx["versions"], ctx["conf"])
            con.execute("INSERT OR REPLACE INTO tree_built VALUES (?,?,?)", (tree, ctx["digest"], time.time()))
            remove_unheld_rows(con, root, keep={tree})
    except sqlite3.OperationalError as exc:
        raise TagError(f"the tag index is locked or unwritable: {exc}") from None


def read_worktree_trees(root) -> tuple[set, set]:
    """(the tree each worktree's HEAD names, the worktrees' top-level paths, each `derive_worktree_key`'s)."""
    trees, tops = set(), set()
    for block in read_git(root, "worktree", "list", "--porcelain").split("\n\n"):
        fields = dict(ln.split(" ", 1) for ln in block.splitlines() if " " in ln)
        if "worktree" in fields:
            tops.add(derive_worktree_key(fields["worktree"]))
        if fields.get("HEAD"):
            try:
                trees.add(read_git(root, "rev-parse", fields["HEAD"] + "^{tree}").strip())
            except TagError:
                pass
    return trees, tops


def remove_unheld_rows(con, root, keep=()) -> None:
    """Drop the trees no worktree's HEAD names (bar `keep`), the dirty rows of worktrees that are gone,
    and every path, blob and `blob_parsed` row no remaining tree or dirty row holds. A tree with `tree_path`
    rows and no `tree_built` row is read here too."""
    trees, tops = read_worktree_trees(root)
    trees |= set(keep)
    for (tree,) in con.execute("SELECT tree FROM tree_built UNION SELECT DISTINCT tree FROM tree_path").fetchall():
        if tree not in trees:
            con.execute("DELETE FROM tree_path WHERE tree=?", (tree,))
            con.execute("DELETE FROM tree_built WHERE tree=?", (tree,))
    for (wt,) in con.execute("SELECT DISTINCT worktree FROM dirty_path").fetchall():
        if wt not in tops:
            con.execute("DELETE FROM dirty_path WHERE worktree=?", (wt,))
    con.execute("DELETE FROM path_row WHERE NOT EXISTS (SELECT 1 FROM tree_path t WHERE t.path=path_row.path "
                "AND t.blob=path_row.blob) AND NOT EXISTS (SELECT 1 FROM dirty_path d WHERE d.path=path_row.path "
                "AND d.blob=path_row.blob)")
    for table in ("blob_row", "blob_parsed"):
        con.execute(f"DELETE FROM {table} WHERE NOT EXISTS (SELECT 1 FROM tree_path t WHERE t.blob={table}.blob) "
                    f"AND NOT EXISTS (SELECT 1 FROM dirty_path d WHERE d.blob={table}.blob)")


def build_overlay(root, ctx, con, stats) -> None:
    """Record this worktree's uncommitted edits to tracked files as its own `dirty_path` rows, a deleted
    file as blob "", replacing the rows it held. Counts into `stats`."""
    wt = ctx["worktree"]
    # --no-renames: a staged rename is its old path deleted and its new one added (PLAY-dOrderedCharter-70 S7)
    changed = [p for p in read_git(root, "diff", "--name-only", "--no-renames", "-z", "HEAD").split("\0") if p]
    entries = []
    for path in changed:
        f = pathlib.Path(root) / path
        blob = read_git(root, "hash-object", "--", path).strip() if f.is_file() else ""
        entries.append((path, blob))
    live = [(p, b) for p, b in entries if b]
    pairs = _derive_applicable(ctx, live)
    blobs: dict = {}
    for path, blob, ex, _name in pairs:
        blobs.setdefault(blob, []).append((path, ex))

    def read_text(want):
        out = {}
        for blob, path in want.items():
            try:
                out[blob] = (pathlib.Path(root) / path).read_bytes().decode("utf-8").replace("\r\n", "\n")
            except (OSError, UnicodeDecodeError):
                out[blob] = None
        return out

    try:
        with con:
            con.execute("DELETE FROM dirty_path WHERE worktree=?", (wt,))
            con.executemany("INSERT INTO dirty_path VALUES (?,?,?)", [(wt, p, b) for p, b in entries])
            _write_parsed(con, ctx, blobs, read_text, stats)
            _write_path_rows(con, pairs, ctx["versions"], ctx["conf"])
    except sqlite3.OperationalError as exc:
        raise TagError(f"the tag index is locked or unwritable: {exc}") from None


def read_live_versions(root, kit_rel) -> tuple[set, set, set]:
    """(every (extractor, version) pair, every `versions` digest, every conf key) a live worktree derives:
    each worktree `git worktree list` names, its map from its own registry and module files under `kit_rel`
    and its key from its own conf. A worktree whose registry or a module cannot be read refuses, naming it,
    rather than having its versions collected (PLAY-dOrderedCharter-51 S5)."""
    _tree_lib, id_grammar = load_memory_tree()
    pairs, digests, keys = set(), set(), set()
    for top in sorted(read_worktree_trees(root)[1]):
        registry = pathlib.Path(top) / kit_rel / "namespaces.toml"
        try:
            rows = [r for r in read_namespaces(registry) if SEG_RE.fullmatch(r["ns"])]
            versions = derive_extractor_versions(rows, registry.parent)
        except TagError as exc:
            raise TagError(f"--gc: worktree {top} cannot be read, so nothing is collected: {exc}") from None
        conf = id_grammar.load_conf(pathlib.Path(top))
        key = derive_conf_key((conf.get("MEMORY_ROOT") or "memory").strip("/"), conf.get("CHARTER") or "AGENTS.md")
        pairs |= set(versions.items())
        digests.add(derive_versions_digest(versions, key))
        keys.add(key)
    return pairs, digests, keys


def remove_dead_versions(con, root, kit_rel) -> tuple[int, int]:
    """`--gc` (PLAY-dOrderedCharter-51 S5): delete the blob, path and `blob_parsed` rows of every (extractor,
    version) pair no live worktree derives and the `tree_built` rows of every digest none does, then the
    rows no live tree or worktree holds, as a build's sweep does. -> (rows, versions) collected."""
    live, digests, keys = read_live_versions(root, kit_rel)
    rows = 0
    try:
        with con:
            dead = set(con.execute("SELECT extractor, version FROM blob_parsed UNION SELECT extractor, version "
                                   "FROM blob_row UNION SELECT extractor, version FROM path_row")) - live
            for ex, ver in dead:
                for table in ("blob_row", "path_row", "blob_parsed"):
                    rows += con.execute(f"DELETE FROM {table} WHERE extractor=? AND version=?", (ex, ver)).rowcount
            for (key,) in con.execute("SELECT DISTINCT conf FROM path_row").fetchall():
                if key not in keys:
                    rows += con.execute("DELETE FROM path_row WHERE conf=?", (key,)).rowcount
            for (d,) in con.execute("SELECT DISTINCT versions FROM tree_built").fetchall():
                if d not in digests:
                    rows += con.execute("DELETE FROM tree_built WHERE versions=?", (d,)).rowcount
            remove_unheld_rows(con, root)
    except sqlite3.OperationalError as exc:
        raise TagError(f"the tag index is locked or unwritable: {exc}") from None
    return rows, len(dead)


def load_view(con, root, ctx, tree=None, overlay=True) -> dict:
    """Bring the index up to date for this worktree and fill the temp table `view_path` with the paths it
    is served: its HEAD tree (or `tree`) and, with `overlay`, its own dirty rows. Returns the tree and the
    counts: blobs `parsed`, and per extractor its `runs` and its blobs `skipped` as fresh."""
    tree = tree or read_git(root, "rev-parse", "HEAD^{tree}").strip()
    stats = {"parsed": 0, "runs": collections.Counter(), "skipped": collections.Counter()}
    build_index(root, tree, ctx, con, stats)
    if overlay:
        build_overlay(root, ctx, con, stats)
    con.execute("CREATE TEMP TABLE IF NOT EXISTS view_version(extractor TEXT PRIMARY KEY, version TEXT)")
    con.execute("DELETE FROM view_version")
    con.executemany("INSERT INTO view_version VALUES (?,?)", ctx["versions"].items())
    con.execute("CREATE TEMP TABLE IF NOT EXISTS view_conf(conf TEXT PRIMARY KEY)")
    con.execute("DELETE FROM view_conf")
    con.execute("INSERT INTO view_conf VALUES (?)", (ctx["conf"],))
    con.execute("CREATE TEMP TABLE IF NOT EXISTS view_path(path TEXT PRIMARY KEY, blob TEXT)")
    con.execute("DELETE FROM view_path")
    con.execute("INSERT INTO view_path SELECT path, blob FROM tree_path WHERE tree=?", (tree,))
    if overlay:
        for path, blob in con.execute("SELECT path, blob FROM dirty_path WHERE worktree=?",
                                      (ctx["worktree"],)).fetchall():
            if blob:
                con.execute("INSERT OR REPLACE INTO view_path VALUES (?,?)", (path, blob))
            else:
                con.execute("DELETE FROM view_path WHERE path=?", (path,))
    return {"tree": tree, **stats}


#: the path rows a worktree is served: its view's paths, at its own extractor versions (PLAY-dOrderedCharter-51 S3)
#: and under its own conf key (PLAY-dOrderedCharter-70 S8)
VIEW_JOIN = ("FROM path_row p JOIN view_path v ON p.path=v.path AND p.blob=v.blob "
             "JOIN view_version w ON p.extractor=w.extractor AND p.version=w.version "
             "JOIN view_conf c ON p.conf=c.conf")
VIEW_ROWS = "SELECT p.tag, p.path, p.line, p.kind, p.blob, p.extractor " + VIEW_JOIN


def read_rows(con, kinds, tag=None, like=None):
    """The served view's path rows of `kinds`, optionally of one tag or a LIKE pattern."""
    q = VIEW_ROWS + f" WHERE p.kind IN ({','.join('?' * len(kinds))})"
    args = list(kinds)
    if tag is not None:
        q += " AND p.tag=?"
        args.append(tag)
    if like is not None:
        q += " AND p.tag LIKE ?"
        args.append(like)
    return con.execute(q + " ORDER BY p.tag, p.path, p.line", args).fetchall()


def read_text_of(con, blob, extractor, kind, line):
    hit = con.execute("SELECT b.end_line, b.text FROM blob_row b JOIN view_version w ON b.extractor=w.extractor "
                      "AND b.version=w.version WHERE b.blob=? AND b.extractor=? AND b.kind=? AND b.line=?",
                      (blob, extractor, kind, line)).fetchone()
    return hit or (line, "")


def read_aliases(path) -> dict:
    """{ref: target} from the aliases file's `[[alias]]` rows; a missing file is none."""
    try:
        rows = tomllib.loads(pathlib.Path(path).read_text(encoding="utf-8")).get("alias") or []
    except FileNotFoundError:
        return {}
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise TagError(f"the aliases file {pathlib.Path(path).as_posix()} is unreadable: {exc}") from None
    return {r["ref"]: r["target"] for r in rows if isinstance(r.get("ref"), str) and isinstance(r.get("target"), str)}


def resolve_address(con, address, slice_="leaf", aliases=None) -> list[dict]:
    """The definition rows of `address`, an alias resolved first: the tag alone under `leaf`, and every tag
    with it as a dot-prefix too under `subtree`."""
    tag = (aliases or {}).get(address, address)
    rows = read_rows(con, DEFINE_KINDS, tag=tag)
    if slice_ == "subtree":
        rows += read_rows(con, DEFINE_KINDS, like=tag + ".%")
    out = []
    for t, path, line, kind, blob, ex in rows:
        end, text = read_text_of(con, blob, ex, kind, line)
        out.append({"tag": t, "path": path, "line": line, "end_line": end, "kind": kind, "text": text})
    return out


# ------------------------------------------------------------------------------------------ the checks

def read_population(con, ctx, namespaces=(), words=()) -> tuple[list, list]:
    """(graded, records): the view's span rows whose text opens with a namespace of `namespaces` or
    equals a word of `words`, outside `<MEMORY_ROOT>/builds/` and under it. SQL selects them, so the
    few hundred thousand spans of a tree are never fetched to find the few that matter."""
    con.execute("CREATE TEMP TABLE IF NOT EXISTS want_tag(tag TEXT PRIMARY KEY)")
    con.execute("DELETE FROM want_tag")
    con.executemany("INSERT OR IGNORE INTO want_tag VALUES (?)", [(w,) for w in words])
    conds = " OR ".join(["p.tag IN (SELECT tag FROM want_tag)"] + ["p.tag LIKE ?"] * len(namespaces))
    rows = con.execute(VIEW_ROWS + f" WHERE p.kind='span' AND ({conds}) ORDER BY p.tag, p.path, p.line",
                       [f"{ns}.%" for ns in namespaces]).fetchall()
    builds = ctx["memory_root"] + "/builds/"
    graded, records = [], []
    for row in rows:
        (records if row[1].startswith(builds) else graded).append(row)
    return graded, records


def derive_namespace_state(con, ctx) -> dict:
    """{ns: number of tags defined in the view}; 0 is `unarmed`."""
    counts = {row["ns"]: 0 for row in ctx["namespaces"]}
    for (tag,) in con.execute(f"SELECT p.tag {VIEW_JOIN} WHERE p.kind IN ({','.join('?' * len(DEFINE_KINDS))})", DEFINE_KINDS):
        ns = tag.split("#")[0].split(".")[0]
        if ns in counts:
            counts[ns] += 1
    return counts


def _derive_span_ns(text):
    head = text.split("#")[0]
    return head.split(".")[0] if "." in head else None


def read_view_file_names(con) -> set:
    """The base name of every path the view serves: a span equal to one, naming no row, is a file name."""
    return {p.rsplit("/", 1)[-1] for (p,) in con.execute("SELECT path FROM view_path")}


def read_defined(con) -> set:
    return {t for (t,) in con.execute(f"SELECT DISTINCT p.tag {VIEW_JOIN} "
                                      "WHERE p.kind IN ('doc','section','tag','retired')")}


def check_unclosed(con, ctx) -> tuple[list, list]:
    """The view's `unclosed` rows: red outside `<MEMORY_ROOT>/builds/`, printed under it (PLAY-dOrderedCharter-68)."""
    frozen, reds, lines = f"{ctx['memory_root']}/builds/", [], []
    for _tag, path, line, *_ in read_rows(con, ("unclosed",)):
        if path.startswith(frozen):
            lines.append(f"tags: unclosed fence, frozen record, printed · {path}:{line}")
        else:
            reds.append(f"tags: {path}:{line} · unclosed fence · it opens here and never closes, so every "
                        f"later line goes unread")
    return reds, lines


def check_resolves(con, ctx, bare_mode, armed, file_names=None) -> tuple[list, dict]:
    """S7 `resolves`: a graded citation into an armed namespace that resolves to no row is red; one into
    an unarmed namespace, or under `<MEMORY_ROOT>/builds/`, is counted and never graded. A retired tag
    resolves here: whether citing it is red is the `retired` arm's question. A span naming no row that is
    the base name of a served path is a file name, counted and never red (PLAY-dOrderedCharter-10 §8 F3).
    Bare references read as `bare_mode` says (`charter-only`, `unique`, `never`)."""
    defined = read_defined(con)
    if file_names is None:
        file_names = read_view_file_names(con)
    tails = {t.split(".", 1)[1] for t in defined if "#" not in t and "." in t}
    graded, records = read_population(con, ctx, namespaces=list(armed), words=tails)
    counts = {"graded": 0, "unresolved": 0, "bare": 0, "records": 0, "file_names": 0, "unarmed": {}}
    counts["records"] = sum(1 for r in records if _derive_span_ns(r[0]) in armed)
    reds, notes = [], []
    for text, path, line, *_ in graded:
        ns = _derive_span_ns(text)
        if ns in armed:
            if not armed[ns]:
                counts["unarmed"][ns] = counts["unarmed"].get(ns, 0) + 1
                continue
            if text not in defined and text in file_names:
                counts["file_names"] += 1
                continue
            counts["graded"] += 1
            if text not in defined:
                counts["unresolved"] += 1
                reds.append(f"tags: {path}:{line} · unresolved · `{text}` names no row")
            continue
        if "#" in text:
            continue
        matches = sorted(f"{n}.{text}" for n in armed if f"{n}.{text}" in defined)
        if bare_mode == "charter-only":
            matches = [m for m in matches if m.startswith("practice.")]
        if not matches:
            continue
        counts["bare"] += 1
        if bare_mode == "charter-only":
            notes.append(f"tags: {path}:{line} · bare `{text}` -> {matches[0]}")
        elif bare_mode == "unique" and len(matches) > 1:
            reds.append(f"tags: {path}:{line} · bare `{text}` is ambiguous: {' and '.join(matches)}")
        elif bare_mode == "never" and path != ctx["charter"]:
            reds.append(f"tags: {path}:{line} · bare `{text}` outside the charter: write {' or '.join(matches)}")
    counts["notes"] = notes
    return reds, counts


def check_retired(con, ctx, mode, base_spans, armed, base_sections=None, aliases=None) -> tuple[list, list, int]:
    """S7 `retired`: a retired name minted again is red under every value; a graded citation of a retired
    tag that `base_spans` (the base tree's (path, tag) citations, None for no base) lacks is new text, red
    under `refuse-new`, a WARN line under `warn`, silent under `allow`. -> (reds, warns, cited).
    PLAY-dOrderedCharter-29 S8, over sections: a `doc.<name>#<seg>` of `base_sections` (the compare base's
    section rows, None for no base) gone at the tip with no `[[alias]]` row is red, and a section an alias
    row retires minted again at the tip is red, under every value."""
    retired = {}
    for tag, path, line, *_ in read_rows(con, ("retired",)):
        retired.setdefault(tag, (path, line))
    reds, warns, cited = [], [], 0
    aliases = aliases or {}
    tip = {}
    for tag, path, line, *_ in read_rows(con, ("section",)):
        tip.setdefault(tag, (path, line))
    for tag in sorted(set(base_sections or ()) - set(tip) - set(aliases)):
        reds.append(f"tags: retired section · {tag} is at the compare base and gone at the tip with no [[alias]] "
                    "row: add one in aliases.toml naming where it went")
    for ref in sorted(r for r in aliases if r in tip):
        reds.append(f"tags: {tip[ref][0]}:{tip[ref][1]} · retired section minted again · {ref} (an [[alias]] row "
                    f"retires it to {aliases[ref]})")
    if not retired:
        return reds, warns, cited
    for tag, path, line, *_ in read_rows(con, DEFINE_KINDS):
        if tag in retired:
            reds.append(f"tags: {path}:{line} · retired name minted again · {tag} "
                        f"(retired at {retired[tag][0]}:{retired[tag][1]})")
    graded, _records = read_population(con, ctx, words=retired)
    for text, path, line, *_ in graded:
        if text not in retired or _derive_span_ns(text) not in armed:
            continue
        cited += 1
        if base_spans is not None and (path, text) in base_spans:
            continue
        msg = f"{path}:{line} · new text cites retired {text}"
        if mode == "refuse-new":
            reds.append(f"tags: {msg}")
        elif mode == "warn":
            warns.append(f"tags: WARN {msg}")
    return reds, warns, cited


def read_layer_kinds(path) -> dict:
    try:
        rows = tomllib.loads(pathlib.Path(path).read_text(encoding="utf-8")).get("layer") or []
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise TagError(f"the layer register {pathlib.Path(path).as_posix()} is unreadable: {exc}") from None
    return {r.get("tag"): r.get("kind") for r in rows if isinstance(r, dict)}


def check_owned(con, ctx, layers_path) -> list:
    """S14 `owned`: a tag minted in a namespace whose row's layer is a core layer, by a source sitting in
    a kit whose descriptor's layer is an `optional` or `expansion` row, is red."""
    kinds = read_layer_kinds(layers_path)
    core_ns = {r["ns"] for r in ctx["namespaces"] if kinds.get(r["layer"]) == "core"}
    kit_of: dict = {}

    def read_kit_layer(path):
        for parent in pathlib.PurePosixPath(path).parents:
            key = parent.as_posix()
            if key == ".":
                break
            if key not in kit_of:
                desc = ctx["root"] / key / "kit.toml"
                try:
                    data = tomllib.loads(desc.read_text(encoding="utf-8")) if desc.is_file() else None
                except (OSError, tomllib.TOMLDecodeError):
                    data = None
                kit_of[key] = (data.get("id") or key, data.get("layer")) if data else None
            if kit_of[key]:
                return kit_of[key]
        return None

    reds = []
    for tag, path, line, *_ in read_rows(con, DEFINE_KINDS):
        ns = tag.split("#")[0].split(".")[0]
        if ns not in core_ns:
            continue
        hit = read_kit_layer(path)
        if hit and kinds.get(hit[1]) in ("optional", "expansion"):
            reds.append(f"tags: {path}:{line} · owned · kit {hit[0]} ({hit[1]}) mints {tag} in core namespace {ns}")
    return reds


def derive_tag_fault(head: str, words) -> str | None:
    """S3's rule for one tag `head`, no `#<seg>`, against the registry's namespace `words`: the rule it
    breaks, or None. The shape check and the memory index's promotion both grade through it."""
    ns, _, rest = head.partition(".")
    segs = rest.split(".") if rest else []
    bad = next((s for s in segs if not SEG_RE.fullmatch(s)), None)
    if ns not in words:
        return f"namespace '{ns}' is not registered"
    if not segs or bad is not None:
        return f"segment '{bad or ''}' is outside {SEG}"
    if len(head.encode("utf-8")) > TAG_MAX_BYTES:
        return f"over {TAG_MAX_BYTES} bytes ({len(head.encode('utf-8'))})"
    if segs[0] in words:
        return f"first segment '{segs[0]}' is a namespace word"
    return None


def check_tag_shape(con, ctx) -> tuple[list, list]:
    """S3, the shape check, over every defining row and every unit row's selector value: each graded
    before any `#<seg>`, against the registry's words, a word outside `seg` a red naming its row and
    never a word. -> (reds, the tags graded)."""
    words = {r["ns"] for r in ctx["namespaces"]}
    reds = [f"tags: {ctx['registry']} · shape · namespace row '{ns}' is outside seg, so no tag is graded "
            f"against it" for ns in ctx["malformed"]]
    graded = []
    for tag, path, line, *_ in read_rows(con, DEFINE_KINDS + ("selector",)):
        head = tag.split("#")[0]
        reason = derive_tag_fault(head, words)
        if reason:
            reds.append(f"tags: {path}:{line} · shape · {head} · {reason}")
        graded.append(head)
    return reds, graded


def check_namespace_joins(con, ctx, file_names=None) -> tuple[list, list]:
    """S4, each namespace joined both ways through `compute_coverage`: every graded citation into it is a
    member (a retired one included, the `retired` arm's question), file names aside; and, for a `selects`
    namespace whose members are not units, every member selects a unit, graded once some unit's `scope`
    names a tag of the namespace (PLAY-dOrderedCharter-75). An empty population prints `unarmed` and
    grades nothing; a descriptor's unused members are printed, never red. -> (reds, lines)."""
    load_memory_tree()
    from coverage_join import compute_coverage
    if file_names is None:
        file_names = read_view_file_names(con)
    members, declared = {}, {}
    for tag, path, line, kind, *_ in read_rows(con, DEFINE_KINDS + ("retired",)):
        ns = tag.split("#")[0].split(".")[0]
        members.setdefault(ns, set()).add(tag)
        if kind != "retired" and "#" not in tag:
            declared.setdefault(ns, {}).setdefault(tag, (path, line))
    units = [r for r in read_rows(con, ("tag",)) if r[5] in UNIT_EXTRACTORS]
    selected: dict = {}
    for tag, path, line, *_ in read_rows(con, ("selector",)):
        selected.setdefault(tag.split(".")[0], {}).setdefault(tag, (path, line))
    graded, _records = read_population(con, ctx, namespaces=[r["ns"] for r in ctx["namespaces"]])
    cited: dict = {}
    for text, path, line, *_ in graded:
        if text not in file_names:
            cited.setdefault(_derive_span_ns(text), {}).setdefault(text, (path, line))
    reds, lines, armed = [], [], []
    for row in ctx["namespaces"]:
        ns = row["ns"]
        if not members.get(ns):
            lines.append(f"tags: join {ns} · unarmed: its source declares nothing, so neither direction is graded")
            continue
        armed.append(ns)
        cov = compute_coverage({ns: sorted(members[ns])}, {"cited": {ns: tuple(cited.get(ns, ()))}}, {ns: ()})
        for key in cov.stale_claims.get(ns, []):
            tag = key.split(": ", 1)[1]
            path, line = cited[ns][tag]
            reds.append(f"tags: {path}:{line} · join · `{tag}` is cited and undeclared in {ns}")
        if row["extractor"] in UNIT_EXTRACTORS:
            continue
        sel = selected.get(ns, {})
        if row["role"] == "selects":
            if not sel:
                lines.append(f"tags: join {ns} · selects · unarmed: no unit's scope names a {ns} tag, "
                             "so no member is graded as selecting")
                continue
            dec = declared.get(ns, {})
            cov = compute_coverage({ns: sorted(dec)}, {"units": {ns: tuple(sel)}}, {ns: ()})
            for tag in cov.unclaimed.get(ns, []):
                reds.append(f"tags: {dec[tag][0]}:{dec[tag][1]} · join · `{tag}` is declared and selects no unit")
            for key in cov.stale_claims.get(ns, []):
                tag = key.split(": ", 1)[1]
                reds.append(f"tags: {sel[tag][0]}:{sel[tag][1]} · join · a unit selects `{tag}`, which {ns} does not declare")
        elif units:
            unused = sorted(set(declared.get(ns, {})) - set(sel))
            if unused:
                lines.append(f"tags: join {ns} · {len(unused)} unused, a descriptor (not red): {' '.join(unused)}")
    lines.insert(0, f"tags: joins · {len(armed)} armed ({' '.join(armed) or 'none'}), "
                    f"{len(ctx['namespaces']) - len(armed)} unarmed, {len(units)} unit rows")
    return reds, lines


#: the chain registry, under MEMORY_ROOT: one `[[build]]` row per chain build, `slug` and `purpose`
CHAIN_REGISTRY = "project/chain.toml"


def read_chain_registry(path) -> list[dict]:
    """The chain registry's `[[build]]` rows (PLAY-dOrderedCharter-22 S3); a missing file holds no row,
    so every namespace `owner` is unarmed against it (PLAY-dOrderedCharter-78 S3). A row with no `slug`, or a slug twice, is a TagError."""
    path = pathlib.Path(path)
    try:
        rows = tomllib.loads(path.read_text(encoding="utf-8")).get("build") or []
    except FileNotFoundError:
        return []
    except (OSError, tomllib.TOMLDecodeError) as exc:
        raise TagError(f"the chain registry {path.as_posix()} is unreadable: {exc}") from None
    seen: set[str] = set()
    for i, row in enumerate(rows, 1):
        slug = row.get("slug") if isinstance(row, dict) else None
        if not isinstance(slug, str) or not slug:
            raise TagError(f"{path.as_posix()}: build row {i} lacks slug")
        if slug in seen:
            raise TagError(f"{path.as_posix()}: build '{slug}' is registered twice")
        seen.add(slug)
    return rows


def read_toml_field(text, tag, field):
    """The non-empty string `field` of the TOML array-of-tables row whose tag is `tag`, keyed as ROW_TAG_KEYS
    keys its table, else None."""
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError:
        return None
    for table, rows in data.items():
        for row in rows if isinstance(rows, list) else ():
            if isinstance(row, dict) and row.get(ROW_TAG_KEYS.get(table, "tag")) == tag:
                val = row.get(field)
                return val if isinstance(val, str) and val.strip() else None
    return None


def read_py_assigns(text) -> set:
    """The names a Python module assigns at its top level; a module that does not parse assigns none."""
    import ast
    try:
        body = ast.parse(text).body
    except SyntaxError:
        return set()
    targets = [t for n in body if isinstance(n, ast.Assign) for t in n.targets]
    targets += [n.target for n in body if isinstance(n, ast.AnnAssign)]
    return {t.id for t in targets if isinstance(t, ast.Name)}


def check_namespace_purpose(con, ctx, chain_rows) -> tuple[list, dict]:
    """S1 and S2 of PLAY-dOrderedCharter-22: every row's `owner` is a build of the chain registry, and its
    `purpose-source` grades its members, the `#`-free defining rows its own extractor serves for it. A
    source is `<path>` (tracked, printed path-only), `<path>#<field>` (each member at a `.toml` path
    carries the field on its row, a `.py` path assigns it; any other suffix is red), or `#<field>` (each
    member's own file carries it: its TOML row's key, or `h1`, a Markdown file's first `# ` line outside a
    fence). A `{prefix}/` in the source resolves first against the registry's tool root, the parent of
    its directory (PLAY-dOrderedCharter-72 S7). A source not in the view, a path not served or a
    `#<field>` with no member, is `pending`: printed as spelled and never graded. An `owner` the registry
    does not hold is `unarmed`, never red, its row's source graded as before (PLAY-dOrderedCharter-78 S3).
    -> (reds, {"graded": {ns: members}, "path_only": [ns], "pending": [(ns, source)],
    "unarmed": {owner: [ns]}})."""
    slugs = {r["slug"] for r in chain_rows}
    served = {p for (p,) in con.execute("SELECT path FROM view_path")}
    defined = read_rows(con, DEFINE_KINDS)
    texts: dict = {}

    def read_served(path):
        # ponytail: the working tree stands in for the served blob, as the view is HEAD plus this worktree's edits
        if path not in texts:
            try:
                texts[path] = (ctx["root"] / path).read_bytes().decode("utf-8", "replace").replace("\r\n", "\n")
            except OSError:
                texts[path] = ""
        return texts[path]

    reds: list = []
    state: dict = {"graded": {}, "path_only": [], "pending": [], "unarmed": {}}
    troot = pathlib.PurePosixPath(ctx["kit"]).parent.as_posix()  # PLAY-dOrderedCharter-72 S7: the registry's tool root
    for row in ctx["namespaces"]:
        ns, src = row["ns"], row["purpose-source"]
        at = f"tags: {ctx['registry']} · purpose · namespace '{ns}'"
        if row["owner"] not in slugs:
            state["unarmed"].setdefault(row["owner"], []).append(ns)
        members = [(t, p) for t, p, _n, _k, _b, ex in defined
                   if ex == row["extractor"] and "#" not in t and t.split(".")[0] == ns]
        path, hashed, field = resolve_prefix_token(src, troot).partition("#")
        if hashed and not field:
            reds.append(f"{at} · purpose-source '{src}' names no field after its #")
            continue
        if (path and path not in served) or (not path and not members):
            state["pending"].append((ns, src))
            continue
        if not hashed:
            state["path_only"].append(ns)
            continue
        if path:
            suffix = pathlib.PurePosixPath(path).suffix
            if suffix not in (".toml", ".py"):
                reds.append(f"{at} · purpose-source '{src}' reads a field in a {suffix or 'suffixless'} file, "
                            "which the arm reads no field in")
                continue
            held = [m for m in members if m[1] == path]
            if members and not held:
                reds.append(f"{at} · purpose-source '{src}' holds none of its {len(members)} members")
                continue
            members = held
        state["graded"][ns] = len(members)
        for tag, mpath in members:
            text, suffix = read_served(mpath), pathlib.PurePosixPath(mpath).suffix
            if suffix == ".toml":
                ok = read_toml_field(text, tag, field) is not None
            elif suffix == ".py" and path:
                ok = field in read_py_assigns(text)
            elif suffix == ".md" and field == "h1":
                ok = any(ln[2:].strip() for _n, ln in scan_unfenced(text) if ln.startswith("# "))
            else:
                reds.append(f"{at} · member {tag} sits in {mpath}, a file the arm reads no {field} in")
                continue
            if not ok:
                reds.append(f"{at} · member {tag} ({mpath}) lacks {field}")
    return reds, state


def check_chain_registry(root, conf, chain_rows, chain_rel) -> tuple[list, dict | None]:
    """S3 and S4 of PLAY-dOrderedCharter-22: the registry's slugs joined both ways with the design view's
    builds, and a row with no `purpose` legal only for a build of v2's `[chain]` at the design baseline,
    printed as awaiting PM-5's review. `conf`'s DESIGN_* keys all blank is no chain to read, (reds, None);
    a half-declared design is a TagError. -> (reds, {"rows", "builds", "awaiting": [slug]})."""
    load_memory_tree()
    import design_lib
    try:
        values = design_lib.read_design_keys(root, conf)
        if values is None:
            return [], None
        view = values["DESIGN_VIEW"]
        builds = {b for b, *_ in design_lib.read_design_view(view, root)}
        record, pin = values["DESIGN_RECORD"], values["DESIGN_BASELINE"]
        shown = design_lib.run_git(root, "show", f"{pin}:{record}")
        if shown.returncode:
            raise design_lib.DesignRefusal(f"DESIGN_RECORD {record} is absent at DESIGN_BASELINE {pin[:9]}")
        baseline = {b for b, *_ in design_lib.read_chain_clauses(shown.stdout.decode("utf-8", "replace"),
                                                                  f"{record} at {pin[:9]}")}
    except design_lib.DesignRefusal as exc:
        raise TagError(f"the chain registry's join cannot read the design: {exc}") from None
    slugs = [r["slug"] for r in chain_rows]
    reds = [f"tags: {chain_rel} · purpose · registry row '{s}' names no build of the design view {view}"
            for s in slugs if s not in builds]
    reds += [f"tags: {chain_rel} · purpose · chain build '{b}' of the design view has no registry row"
             for b in sorted(builds - set(slugs))]
    awaiting = []
    for row in chain_rows:
        purpose = row.get("purpose")
        if isinstance(purpose, str) and purpose.strip():
            continue
        if row["slug"] in baseline:
            awaiting.append(row["slug"])
        else:
            reds.append(f"tags: {chain_rel} · purpose · registry row '{row['slug']}' carries no purpose, and no "
                        "baseline [chain] row names it")
    return reds, {"rows": len(chain_rows), "builds": len(builds), "awaiting": awaiting}


def read_index_rows(con, ctx, tree) -> list[str]:
    """Every row of the index the worktree of `ctx` reads at `tree`, sorted, `built_at` aside: what a build
    from nothing at its own extractor versions must reproduce (the `--dump` the plants compare). A row of
    another version is left out, and so is one only another live worktree's HEAD tree or dirty edits hold
    (PLAY-dOrderedCharter-51 S3), and so is a path row of another conf key and a blob row only such a path row
    reaches (PLAY-dOrderedCharter-70 S8); a row no worktree holds stays in, so a sweep that missed it shows."""
    trees, tops = read_worktree_trees(ctx["root"])
    trees.discard(tree)
    tops.discard(ctx["worktree"])

    def read(q, *args):
        return con.execute(q, args).fetchall()
    own = set(read("SELECT path, blob FROM tree_path WHERE tree=?", tree))
    own |= set(read("SELECT path, blob FROM dirty_path WHERE worktree=?", ctx["worktree"]))
    other = {(p, b) for t, p, b in read("SELECT tree, path, blob FROM tree_path") if t in trees}
    other |= {(p, b) for w, p, b in read("SELECT worktree, path, blob FROM dirty_path") if w in tops}
    foreign = other - own
    foreign_blobs = {b for _p, b in foreign} - {b for _p, b in own}
    mine = set(ctx["versions"].items())
    reach = read("SELECT DISTINCT blob, extractor, conf = ? FROM path_row", ctx["conf"])
    elsewhere = {(b, ex) for b, ex, here in reach if not here} - {(b, ex) for b, ex, here in reach if here}
    rows = {
        "tree_path": [r for r in read("SELECT tree, path, blob FROM tree_path") if r[0] not in trees],
        "blob_row": [r for r in read("SELECT blob, extractor, version, tag, kind, line, end_line, text FROM blob_row")
                     if (r[1], r[2]) in mine and r[0] not in foreign_blobs and (r[0], r[1]) not in elsewhere],
        "path_row": [r for r in read("SELECT path, blob, extractor, version, conf, tag, kind, line FROM path_row")
                     if (r[2], r[3]) in mine and r[4] == ctx["conf"] and (r[0], r[1]) not in foreign],
        "dirty_path": [r for r in read("SELECT worktree, path, blob FROM dirty_path") if r[0] not in tops],
        "tree_built": [r for r in read("SELECT tree, versions FROM tree_built")
                       if r[1] == ctx["digest"] and r[0] not in trees],
        "blob_parsed": [r for r in read("SELECT blob, extractor, version FROM blob_parsed")
                        if (r[1], r[2]) in mine and r[0] not in foreign_blobs and (r[0], r[1]) not in elsewhere],
    }
    return sorted(f"{table}\t" + "\t".join(map(str, r)) for table, got in rows.items() for r in got)
