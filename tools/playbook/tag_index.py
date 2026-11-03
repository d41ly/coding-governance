"""tag_index — the tag grammar, the namespace registry and the derived SQLite tag index (PLAY-dOrderedCharter-19).

THE GRAMMAR. A tag is `<ns>.<seg>(.<seg>)*`, each `seg` `[a-z0-9][a-z0-9-]*`, at most TAG_MAX_BYTES bytes;
`<ns>` is a word the registry, `namespaces.toml` beside this file, declares, never one typed here. A
document section is `doc.<name>#<seg>`, its `<seg>` the `##` heading folded by `derive_heading_seg`.

THE INDEX is `<git-common-dir>/gov/index.db`, one file per node that every worktree of the repository
shares, written by the extractors alone through `build_index`, never committed: deleting it costs one
rebuild. Its tables, keyed by blob or by path and blob so a later build can add its own beside them:

  tree_path(tree, path, blob)                               the paths a built tree holds
  blob_row(blob, extractor, tag, kind, line, end_line, text) what a blob holds, whatever path it sits at
  path_row(path, blob, extractor, tag, kind, line)          what a path names, a citation among them
  dirty_path(worktree, path, blob)                          a worktree's uncommitted edits to tracked files
  tree_built(tree, built_at)                                the freshness key

A blob row's tag `""` or `#<seg>` is relative to the name its path gives it (a document's `doc.<name>`),
so one blob at two paths is parsed once and named twice; every other tag is whole. A `parsed` row marks a
(blob, extractor) or (path, blob, extractor) pair read, so an extractor that found nothing is not re-run.

AN EXTRACTOR is `<module>:<function>`, called `fn(ctx, path, None)` to ask whether it reads `path` (the
path's name, `""` for none, or None when it does not read it) and `fn(ctx, path, text)` for the rows,
each `(tag, kind, line, end_line, text)`. A module other than this one is loaded from the registry's
directory. `extract_citations` runs over every path whatever the registry says.

THE OVERLAY. A worktree's uncommitted edits to tracked files are its own `dirty_path` rows, keyed by the
worktree's top-level path and served to that worktree alone; the freshness key exempts them.
"""
from __future__ import annotations

import fnmatch
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
CREATE TABLE IF NOT EXISTS blob_row(blob TEXT, extractor TEXT, tag TEXT, kind TEXT, line INTEGER,
                                    end_line INTEGER, text TEXT);
CREATE INDEX IF NOT EXISTS blob_row_key ON blob_row(blob, extractor);
CREATE TABLE IF NOT EXISTS path_row(path TEXT, blob TEXT, extractor TEXT, tag TEXT, kind TEXT, line INTEGER);
CREATE INDEX IF NOT EXISTS path_row_key ON path_row(path, blob);
CREATE INDEX IF NOT EXISTS path_row_tag ON path_row(tag);
CREATE TABLE IF NOT EXISTS dirty_path(worktree TEXT, path TEXT, blob TEXT, PRIMARY KEY(worktree, path));
CREATE TABLE IF NOT EXISTS tree_built(tree TEXT PRIMARY KEY, built_at REAL);
"""
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
    """The registry's `[[namespace]]` rows, each carrying every field of REGISTRY_FIELDS, or TagError."""
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
        if not SEG_RE.fullmatch(row["ns"]) or row["ns"] in seen:
            raise TagError(f"{path.as_posix()}: namespace '{row['ns']}' is malformed or registered twice")
        if row["role"] not in ("selects", "describes"):
            raise TagError(f"{path.as_posix()}: namespace '{row['ns']}' has role '{row['role']}', not selects or describes")
        if ":" not in row["extractor"]:
            raise TagError(f"{path.as_posix()}: namespace '{row['ns']}' extractor is not <module>:<function>")
        seen.add(row["ns"])
    return rows


def load_extractors(namespaces, registry_dir) -> dict:
    """{'<module>:<function>': callable} for every row's extractor, and extract_citations."""
    out = {"tag_index:extract_citations": extract_citations}
    for row in namespaces:
        name = row["extractor"]
        if name in out:
            continue
        mod_name, _, fn_name = name.partition(":")
        if mod_name == "tag_index":
            mod = sys.modules[__name__]
        else:
            src = pathlib.Path(registry_dir) / f"{mod_name}.py"
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


def scan_unfenced(text: str):
    """(line number, line) for every line of Markdown `text` outside a ``` or ~~~ fence."""
    fence = ""
    for n, line in enumerate(text.splitlines(), 1):
        s = line.lstrip()
        if fence:
            if s.startswith(fence):
                fence = ""
            continue
        if s.startswith("```") or s.startswith("~~~"):
            fence = s[:3]
            continue
        yield n, line


def extract_doc(ctx, path, text=None):
    """The `doc` namespace: the charter (`doc.charter`), each `<MEMORY_ROOT>/guides/*.md`, `HYGIENE.md`
    and `TEMPLATE-SPEC.md` (`doc.<stem lower-cased>`); each `##` heading a section `#<seg>`."""
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


def extract_unit(ctx, path, text=None):
    """The `unit` namespace: the `tag` of each `[[unit]]` row of every `instructions.toml`, a kit's and
    `.governance/`'s. Empty until a build lands rows; a file that does not parse names nothing."""
    if text is None:
        return "" if pathlib.PurePosixPath(path).name == "instructions.toml" else None
    try:
        units = tomllib.loads(text).get("unit") or []
    except tomllib.TOMLDecodeError:
        return []
    lines = text.splitlines()
    rows = []
    for unit in units:
        tag = unit.get("tag") if isinstance(unit, dict) else None
        if isinstance(tag, str) and parse_tag(tag)[1] is None:
            n = next((i for i, ln in enumerate(lines, 1) if f'"{tag}"' in ln), 1)
            rows.append((tag, "tag", n, n, lines[n - 1] if lines else ""))
    return rows


CODE_SPAN_RE = re.compile(r"(`+)(.+?)(?<!`)\1(?!`)")
BRACKET_RE = re.compile(r"\[([^\[\]\n]+)\]")


def extract_citations(ctx, path, text=None):
    """Every whole backticked or bracketed span of tracked Markdown, outside fences, that SPAN_RE matches:
    kind `span`. Whether one is a citation, a bare reference or neither is decided at the read, against the
    registry, so the rows do not move when a namespace is registered. Nothing outside `.md` is read. A span
    row carries no text: its line is where `refs` points, and the index holds a few hundred thousand."""
    if text is None:
        return "" if path.endswith(".md") else None
    rows = []
    for n, line in scan_unfenced(text):
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
    return rows


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


def load_memory_tree():
    """memory-tree's `tree_lib` (the one `<rev>:<path>` reader) and `id_grammar` (its conf reader); this
    kit reaches them through its inline `resolve_kit_dir`, never a spelled sibling path."""
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


def load_index(root) -> sqlite3.Connection:
    """The node's index, `<git-common-dir>/gov/index.db`, created on first use. WAL off: every worktree
    opens the one file, and SQLite's lock serialises the writers."""
    db = common_git_dir(pathlib.Path(root)) / "gov" / "index.db"
    db.parent.mkdir(parents=True, exist_ok=True)
    try:
        con = sqlite3.connect(str(db), timeout=BUSY_TIMEOUT)
        con.execute("PRAGMA journal_mode=DELETE")
        con.executescript(SCHEMA)
    except sqlite3.Error as exc:
        raise TagError(f"the tag index {db.as_posix()} cannot be opened: {exc}") from None
    return con


def derive_context(root, registry) -> dict:
    """What every extractor and check reads: the conf's MEMORY_ROOT and CHARTER, the registry and its
    extractors, and the worktree's own top-level path."""
    _tree_lib, id_grammar = load_memory_tree()
    conf = id_grammar.load_conf(pathlib.Path(root))
    namespaces = read_namespaces(registry)
    return {
        "root": pathlib.Path(root),
        "memory_root": (conf.get("MEMORY_ROOT") or "memory").strip("/"),
        "charter": conf.get("CHARTER") or "AGENTS.md",
        "namespaces": namespaces,
        "extractors": load_extractors(namespaces, pathlib.Path(registry).parent),
        "worktree": read_git(root, "rev-parse", "--show-toplevel").strip(),
    }


def _write_parsed(con, ctx, blobs: dict, read_text) -> int:
    """Parse every (blob, extractor) no `parsed` row holds; `blobs` maps blob -> [(path, extractor)].
    Returns the number of blobs parsed."""
    held = {(b, e) for b, e in con.execute("SELECT blob, extractor FROM blob_row WHERE kind = 'parsed'")}
    todo = {b: [(p, e) for p, e in pe if (b, e) not in held] for b, pe in blobs.items()}
    todo = {b: pe for b, pe in todo.items() if pe}
    if not todo:
        return 0
    texts = read_text({b: pe[0][0] for b, pe in todo.items()})
    for blob, pe in todo.items():
        text = texts.get(blob)
        done: set[str] = set()
        for path, ex in pe:
            if ex in done:
                continue
            done.add(ex)
            rows = ctx["extractors"][ex](ctx, path, text) if text is not None else []
            con.executemany("INSERT INTO blob_row VALUES (?,?,?,?,?,?,?)",
                            [(blob, ex, *r) for r in rows] + [(blob, ex, "", "parsed", 0, 0, "")])
    return len(todo)


def _write_path_rows(con, pairs) -> None:
    """Name every (path, blob, extractor, name) no `parsed` path row holds, from its blob's rows."""
    for path, blob, ex, name in pairs:
        if con.execute("SELECT 1 FROM path_row WHERE path=? AND blob=? AND extractor=? AND kind='parsed'",
                       (path, blob, ex)).fetchone():
            continue
        rows = con.execute("SELECT tag, kind, line FROM blob_row WHERE blob=? AND extractor=? AND kind != 'parsed'",
                           (blob, ex)).fetchall()
        con.executemany("INSERT INTO path_row VALUES (?,?,?,?,?,?)",
                        [(path, blob, ex, name + tag if (tag == "" or tag.startswith("#")) else tag, kind, line)
                         for tag, kind, line in rows] + [(path, blob, ex, "", "parsed", 0)])


def _derive_applicable(ctx, entries):
    """[(path, blob, extractor, name)] for every extractor that reads a path of `entries`."""
    out = []
    for path, blob in entries:
        for ex, fn in ctx["extractors"].items():
            name = fn(ctx, path, None)
            if name is not None:
                out.append((path, blob, ex, name))
    return out


def build_index(root, tree, ctx, con) -> int:
    """Index `tree` (a tree id) of the repository at `root`, unless `tree_built` already holds it: one
    `git ls-tree -r`, then a parse of each blob no blob row holds, read through memory-tree's
    `read_blobs_at`, in one transaction. Then rows no tree or worktree holds are removed. Returns the
    number of blobs parsed, 0 for a tree already built."""
    if con.execute("SELECT 1 FROM tree_built WHERE tree=?", (tree,)).fetchone():
        return 0
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
            parsed = _write_parsed(con, ctx, blobs, read_text)
            _write_path_rows(con, pairs)
            con.execute("INSERT OR REPLACE INTO tree_built VALUES (?,?)", (tree, time.time()))
            remove_unheld_rows(con, root, keep={tree})
    except sqlite3.OperationalError as exc:
        raise TagError(f"the tag index is locked or unwritable: {exc}") from None
    return parsed


def read_worktree_trees(root) -> tuple[set, set]:
    """(the tree each worktree's HEAD names, the worktrees' top-level paths)."""
    trees, tops = set(), set()
    for block in read_git(root, "worktree", "list", "--porcelain").split("\n\n"):
        fields = dict(ln.split(" ", 1) for ln in block.splitlines() if " " in ln)
        if "worktree" in fields:
            tops.add(fields["worktree"])
        if fields.get("HEAD"):
            try:
                trees.add(read_git(root, "rev-parse", fields["HEAD"] + "^{tree}").strip())
            except TagError:
                pass
    return trees, tops


def remove_unheld_rows(con, root, keep=()) -> None:
    """Drop the trees no worktree's HEAD names (bar `keep`), the dirty rows of worktrees that are gone,
    and every path and blob row no remaining tree or dirty row holds."""
    trees, tops = read_worktree_trees(root)
    trees |= set(keep)
    for (tree,) in con.execute("SELECT tree FROM tree_built").fetchall():
        if tree not in trees:
            con.execute("DELETE FROM tree_path WHERE tree=?", (tree,))
            con.execute("DELETE FROM tree_built WHERE tree=?", (tree,))
    for (wt,) in con.execute("SELECT DISTINCT worktree FROM dirty_path").fetchall():
        if wt not in tops:
            con.execute("DELETE FROM dirty_path WHERE worktree=?", (wt,))
    con.execute("DELETE FROM path_row WHERE NOT EXISTS (SELECT 1 FROM tree_path t WHERE t.path=path_row.path "
                "AND t.blob=path_row.blob) AND NOT EXISTS (SELECT 1 FROM dirty_path d WHERE d.path=path_row.path "
                "AND d.blob=path_row.blob)")
    con.execute("DELETE FROM blob_row WHERE NOT EXISTS (SELECT 1 FROM tree_path t WHERE t.blob=blob_row.blob) "
                "AND NOT EXISTS (SELECT 1 FROM dirty_path d WHERE d.blob=blob_row.blob)")


def build_overlay(root, ctx, con) -> int:
    """Record this worktree's uncommitted edits to tracked files as its own `dirty_path` rows, a deleted
    file as blob "", replacing the rows it held. Returns the number of blobs parsed."""
    wt = ctx["worktree"]
    changed = [p for p in read_git(root, "diff", "--name-only", "-z", "HEAD").split("\0") if p]
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
            parsed = _write_parsed(con, ctx, blobs, read_text)
            _write_path_rows(con, pairs)
    except sqlite3.OperationalError as exc:
        raise TagError(f"the tag index is locked or unwritable: {exc}") from None
    return parsed


def load_view(con, root, ctx, tree=None, overlay=True) -> dict:
    """Bring the index up to date for this worktree and fill the temp table `view_path` with the paths it
    is served: its HEAD tree (or `tree`) and, with `overlay`, its own dirty rows. Returns the counts."""
    tree = tree or read_git(root, "rev-parse", "HEAD^{tree}").strip()
    parsed = build_index(root, tree, ctx, con)
    if overlay:
        parsed += build_overlay(root, ctx, con)
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
    return {"tree": tree, "parsed": parsed}


VIEW_ROWS = ("SELECT p.tag, p.path, p.line, p.kind, p.blob, p.extractor FROM path_row p JOIN view_path v "
             "ON p.path=v.path AND p.blob=v.blob")


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
    hit = con.execute("SELECT end_line, text FROM blob_row WHERE blob=? AND extractor=? AND kind=? AND line=?",
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
    for (tag,) in con.execute("SELECT p.tag FROM path_row p JOIN view_path v ON p.path=v.path AND p.blob=v.blob "
                              f"WHERE p.kind IN ({','.join('?' * len(DEFINE_KINDS))})", DEFINE_KINDS):
        ns = tag.split("#")[0].split(".")[0]
        if ns in counts:
            counts[ns] += 1
    return counts


def _derive_span_ns(text):
    head = text.split("#")[0]
    return head.split(".")[0] if "." in head else None


def check_resolves(con, ctx, bare_mode, armed) -> tuple[list, dict]:
    """S7 `resolves`: a graded citation into an armed namespace that resolves to no row is red; one into
    an unarmed namespace, or under `<MEMORY_ROOT>/builds/`, is counted and never graded. A retired tag
    resolves here: whether citing it is red is the `retired` arm's question. Bare references
    read as `bare_mode` says (`charter-only`, `unique`, `never`)."""
    defined = {t for (t,) in con.execute("SELECT DISTINCT p.tag FROM path_row p JOIN view_path v ON p.path=v.path "
                                         "AND p.blob=v.blob WHERE p.kind IN ('doc','section','tag','retired')")}
    tails = {t.split(".", 1)[1] for t in defined if "#" not in t and "." in t}
    graded, records = read_population(con, ctx, namespaces=list(armed), words=tails)
    counts = {"graded": 0, "unresolved": 0, "bare": 0, "records": 0, "unarmed": {}}
    counts["records"] = sum(1 for r in records if _derive_span_ns(r[0]) in armed)
    reds, notes = [], []
    for text, path, line, *_ in graded:
        ns = _derive_span_ns(text)
        if ns in armed:
            if not armed[ns]:
                counts["unarmed"][ns] = counts["unarmed"].get(ns, 0) + 1
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


def check_retired(con, ctx, mode, base_spans, armed) -> tuple[list, list, int]:
    """S7 `retired`: a retired name minted again is red under every value; a graded citation of a retired
    tag that `base_spans` (the base tree's (path, tag) citations, None for no base) lacks is new text, red
    under `refuse-new`, a WARN line under `warn`, silent under `allow`. -> (reds, warns, cited)."""
    retired = {}
    for tag, path, line, *_ in read_rows(con, ("retired",)):
        retired.setdefault(tag, (path, line))
    reds, warns, cited = [], [], 0
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


def read_index_rows(con) -> list[str]:
    """Every row of the index, sorted, `built_at` aside: what a rebuild from nothing must reproduce."""
    out = []
    for table, cols in (("tree_path", "tree, path, blob"),
                        ("blob_row", "blob, extractor, tag, kind, line, end_line, text"),
                        ("path_row", "path, blob, extractor, tag, kind, line"),
                        ("dirty_path", "worktree, path, blob"), ("tree_built", "tree")):
        out += [f"{table}\t" + "\t".join(map(str, r)) for r in con.execute(f"SELECT {cols} FROM {table}")]
    return sorted(out)
