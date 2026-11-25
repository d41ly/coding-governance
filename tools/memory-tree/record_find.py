#!/usr/bin/env python3
"""record_find — `record find`, `record show` and the per-item read budget over the one tag index
(TOOL-dTotalRecall-9 S3, S5, S6, S7).

    python gov_record.py find [<question> --terms <words>] [--kind <k>] [--tag <t>] [--build <slug>] [--paths <glob>]
    python gov_record.py show <key>[#<tag>][@<blob>]
    python gov_record.py budget --role <role> <key>...
    python record_find.py --fixture --plant <case>

`find` lists records, never their content: at most FIND_CAP rows, one per record, `key · kind · build ·
bytes · path:line`, sorted by build then key, superseded records hidden; past the cap the last line reads
`<total> rows match; narrow with --kind, --build or --paths`. Filters read the `record` and `section` rows
of the served view (the playbook-render kit's `tag_index.load_view` and `VIEW_JOIN`), reached through the
inline `resolve_kit_dir` at call time; a question ranks by the fusion moved here from memory-recall's
`query.py` (`query_expr` through `run_fusion`, unchanged in ranking) over the FTS tables that kit's
`load_served_set` fills, then takes the same filters and cap. A filter-only `find` needs no recall kit:
its supersession map is the served one where that kit resolves, else `row_grammar`'s direct derivation.

`show` prints one record, or with `#<tag>` one section of it, sliced from its blob at the row's lines;
`@<blob>` reads that blob, its rows where the index holds them, else its bytes from git sectioned by the
`section` extractor. A blob not verified as the key's is refused: the key names no record of the served
view and the index holds no row of it at that blob, or no row the blob's text defines is the key's and
git's history never held the blob at the path whose file name the key is. `budget` sums each key's `show`
slice against the role's `memory.item-budget` (`measured` reads MEASURED_CAP until a role has 30 sliced
work orders measured, `96` or `128` that many KB, a KB 1,000 bytes) and answers as `memory.over-budget`
says; a key the served supersession map names superseded is refused or marked as
`memory.superseded-slices` says. It prints one `read <key> <bytes> B` line per key, ` superseded-by <id>`
after a marked one.

Exit: 0 an answer · 2 a refusal naming what refused: an unknown key, tag or blob, a blob that is no version
of the key, a policy read refused, an over-cap or superseded read refused, an unresolved kit named.
WHAT IT DOES NOT CHECK: a per-role `memory.item-budget` value, which the catalogue's values cannot spell;
and that a record's kind is current where its registry row changed after its blob was indexed.
"""
from __future__ import annotations

import collections
import fnmatch
import os
import pathlib
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(os.path.abspath(__file__)).parent
TOOL_ROOT_NAME = KIT.parent.name   # the tool root as this tree places it, so a fixture lays its kits out at the installed prefix
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))

import id_grammar  # noqa: E402  the record anchors, the supersession readers and the FTS term rules
import tree_lib  # noqa: E402  the one policy read and the one blob reader
from backlog import resolve_kit_dir  # noqa: E402  the kit's inline copy of the sibling resolver

SAY = "record-find"
#: S3: the rows one `find` prints before its total line (PINNED, TOOL-dTotalRecall-9 S3)
FIND_CAP = 40
#: how deep a question's fusion reads before the filters and the cap
QUESTION_DEPTH = 200
#: S6: `measured`'s cap until 30 sliced work orders per role are measured (PINNED, §8 F4, v2:1370)
MEASURED_CAP = 96_000
KB = 1000
OVER_VALUES = ("refuse", "report", "off")
SUPERSEDED_VALUES = ("refuse", "mark")
ADDRESS_RE = re.compile(r"(?P<key>[^#@\s]+)(?:#(?P<tag>[^@\s]+))?(?:@(?P<blob>[0-9a-f]{4,40}))?")

# ---------------------------------------------------------------------------------- the moved fusion
# Moved from memory-recall's `query.py` (TOOL-dTotalRecall-9 S3), which imports every name back.
# The document set a hit names -> the FTS5 table holding it.
RECALL_SETS = {"records": "fts_record", "chunks": "fts_chunk"}
# The join every read of recall's rows makes: this call's served pairs, at this call's digest. CROSS,
# so the FTS5 table is always the outer loop: it has no index on the UNINDEXED key columns, and a
# plan probing it once per served pair would scan it once per pair.
SERVED_JOIN = "CROSS JOIN recall_view v ON f.path = v.path AND f.blob = v.blob AND f.digest = v.digest"
SNIPPET_TOKENS = 64  # FTS5's documented maximum; a larger value is silently clamped
# How deep the chunk arm reads before it is rolled up to `k`. MIRRORS the `k * 8` literal inside
# `bench.run_rollup`, the instrument this serving path is aligned with -- named rather than
# re-derived, because the two must agree and `bench.py` is byte-pinned in `verbatim.json` so the
# literal there cannot move to meet this one. Collapsing several hits from one parent leaves fewer
# than `k` distinct parents from a `k`-deep read, which is why the arm reads deeper than it returns.
ROLLUP_DEPTH = 8


class FindError(Exception):
    """A refusal of find, show or budget, its message naming what refused."""


def load_recall_kit() -> pathlib.Path:
    """memory-recall's directory, on `sys.path` after the kit's own: the kit `load_served_set` and the
    instrument constant `RRF_K` live in. FindError naming the kit where it does not resolve."""
    try:
        kit = resolve_kit_dir("memory-recall", "query.py", KIT)
    except LookupError as exc:
        raise FindError(f"a question reads the memory-recall kit's FTS tables, and {exc}") from None
    if str(kit) not in sys.path:
        sys.path.append(str(kit))
    return kit


def query_expr(question: str, extra_terms: list[str] | None = None) -> str | None:
    """The FTS5 MATCH expression, or None when nothing searchable survives.

    ``bench.match_expr`` falls back to ``'"the"'`` on an empty term set, which turns "how do I do
    this?" into five arbitrary records presented as answers. The caller refuses instead.

    Ids are added as quoted PHRASES: the ``unicode61`` tokenizer splits ``ARCH-169`` into ``arch``
    and ``169``, so ``"arch 169"`` is how the pair is matched adjacently.
    """
    extra_terms = extra_terms or []
    parts: list[str] = []
    base_terms = id_grammar.terms(question)
    if base_terms:
        parts.append(id_grammar.match_expr(question))
    for t in extra_terms:
        cleaned = t.replace('"', " ").strip()
        if cleaned:
            parts.append(f'"{cleaned}"')
    for found in dict.fromkeys(id_grammar.grammar_for().ID_RE.findall(question + " " + " ".join(extra_terms))):
        parts.append('"' + found.replace("-", " ").lower() + '"')
    if not parts:
        return None
    return " OR ".join(parts)


def search(con, name: str, expr: str, k: int) -> list[dict]:
    """The top ``k`` of document set ``name`` (`RECALL_SETS`) for ``expr``, over the served rows only.

    The ranking is today's -- ``bm25`` with the alias column down-weighted -- over the FTS5 table,
    joined to `recall_view` so a row of another worktree's tree or another digest is never a hit.
    A MATCH the FTS5 grammar refuses is a miss, never a crash."""
    t = RECALL_SETS[name]  # MATCH, snippet() and bm25() take the table's hidden column, never the alias
    try:
        rows = con.execute(
            "SELECT f.rowid, f.id, f.path, f.line, "
            f"snippet({t}, 1, '', '', '…', {SNIPPET_TOKENS}), f.body "
            f"FROM {t} f {SERVED_JOIN} "
            f"WHERE {t} MATCH ? ORDER BY bm25({t}, 1.0, 1.0, {id_grammar.ALIAS_WEIGHT}) LIMIT ?",
            (expr, k),
        ).fetchall()
    except sqlite3.OperationalError:
        return []
    return [
        {
            "set": name,
            "rowid": r[0],
            "id": r[1],
            "path": r[2],
            "line": r[3],
            "snippet": r[4],
            "text": r[5],
        }
        for r in rows
    ]


def rrf(rankings: list[list[dict]]) -> list[dict]:
    """Reciprocal rank fusion at ``bench.RRF_K``, the instrument's own constant.

    Keyed on (path, line) rather than rowid: the same passage can surface from both sets, and two
    sets' rowids are unrelated integers.
    """
    load_recall_kit()
    import bench as B  # noqa: E402  memory-recall's instrument, on the path load_recall_kit put it on
    scored: dict[tuple, list] = {}
    for ranked in rankings:
        for rank, hit in enumerate(ranked, 1):
            key = (hit["path"], hit["line"], (hit.get("text") or "")[:60])
            slot = scored.setdefault(key, [0.0, hit])
            slot[0] += 1.0 / (B.RRF_K + rank)
            # Prefer the record-level view of the same passage: it carries the id.
            if hit["set"] == "records":
                slot[1] = hit
    return [h for _, (_, h) in sorted(scored.items(), key=lambda kv: -kv[1][0])]


def run_rollup(hits: list[dict], k: int) -> list[dict]:
    """Keep the best hit per PARENT, in rank order, capped at ``k``.

    ``bench.run_rollup`` does the same thing over its own in-memory ``docs`` list and a
    ``bench.build_fts_rows`` connection; this one serves the dictionaries ``search()`` returns, read
    from the index's own ``id`` column. The two cannot be one function -- different inputs,
    different connections -- so what is shared is the PARENT KEY, and the two spellings are NOT
    identical: ``bench.parent_of`` is ``rec or id or path`` while this is ``id or path``. They agree
    only because ``build_fts_rows`` folds the two into one column -- it writes ``id`` as
    ``d.get("id") or d.get("rec")`` -- so a chunk row arrives here with its parent record id
    already IN ``id``. That fold is the load-bearing step and it is named here because nothing
    else names it and no arm tests it: change that column and this rollup silently becomes a
    per-path cap for the anchored 0.6% as well.

    THE PARENT KEY IS THE PATH FOR ALMOST EVERYTHING, and calling this a per-record rollup would be
    wrong. ``extract_chunks`` sets a chunk's ``rec`` only when a HEADING LINE itself defines a record
    id, and the heading pattern requires ``#{2,6}``, so an H1, a bold-list anchor and a table anchor
    all leave it unset. Measured over the tracked corpus: 129 of 20056 chunk documents carry a
    ``rec`` -- 0.6%. For the other 99.4% this is a per-PATH cap, at most one hit per file, which is
    exactly what the duplicate-slot problem needs. The per-record behaviour is the rare case, and
    both branches carry a self-test arm because an arm on the 0.6% certifies nothing about the rest.
    """
    best: dict = {}
    for hit in hits:
        key = hit.get("id") or hit["path"]
        if key not in best:
            best[key] = hit
        if len(best) >= k:
            break
    return list(best.values())[:k]


def derive_supersession_order(hits: list[dict], smap: dict) -> list[dict]:
    """Annotate every hit from the supersession map, and move a WHOLE-superseded hit under its
    successor when that successor is listed below it.

    ``supersession`` is ``whole``, ``partial`` or None; ``superseded_by`` lists the whole
    successors, or the partial ones when there is no whole edge. A whole-superseded hit moves to sit
    directly after the LOWEST-ranked of its listed successors; a partial hit, and one whose
    successor is absent or ranks above it, keeps its rank, and every other hit keeps its relative
    order. Not a score multiplier: spec §4 shows one sinks the label far from the successor it names.
    A hit only ever moves DOWN, and only past its own successor.
    """
    last: dict[str, int] = {}
    for i, h in enumerate(hits):
        edges = smap.get(h.get("id") or "", [])
        whole = [n for n, kind in edges if kind == "whole"]
        h["supersession"] = "whole" if whole else ("partial" if edges else None)
        h["superseded_by"] = whole or [n for n, _ in edges]
        if h.get("id"):
            last[h["id"]] = i
    after: dict[int, list[int]] = collections.defaultdict(list)
    for i, h in enumerate(hits):
        if h["supersession"] == "whole":
            j = max((last[n] for n in h["superseded_by"] if n in last), default=-1)
            if j > i:
                after[j].append(i)
    moved = {i for v in after.values() for i in v}
    out: list[dict] = []

    def add_hit(i: int) -> None:
        # Recursion terminates: a hit is only ever hung after a STRICTLY later one.
        out.append(hits[i])
        for d in after.get(i, ()):
            add_hit(d)

    for i in range(len(hits)):
        if i not in moved:
            add_hit(i)
    return out


def run_fusion(con, expr: str, k: int, smap: dict | None = None) -> list[dict]:
    """The served fusion: the records arm as-is, the chunk arm rolled up to one hit per parent.

    ONE call site, deliberately. This was two identical expressions -- the first attempt and the
    rebuild after a ``sqlite3.DatabaseError`` -- and a rollup applied to only one of them would make
    the served shape depend on whether the cache happened to be healthy, surfacing only on a
    corrupted cache in a live session. Every acceptance arm runs the healthy path, so the
    duplication was unobservable by construction; deleting it is smaller than gating it.

    The chunk arm pulls ``k * ROLLUP_DEPTH`` before rolling up, because collapsing several hits from
    one parent leaves fewer than ``k`` distinct parents from a ``k``-deep read. The records arm is
    untouched: ``bench.parent_of`` returns a record's own id there, so the rollup is a no-op and the
    extra depth would be paid for nothing.

    The supersession order step runs HERE for the same reason the rollup does: one call site, so
    no caller can serve a different order. ``smap`` is `derive_served_supersessions`'s map; an
    empty one annotates every hit as current and moves nothing. ``con`` is `load_served_set`'s.
    """
    return derive_supersession_order(rrf([
        search(con, "records", expr, k),
        run_rollup(search(con, "chunks", expr, k * ROLLUP_DEPTH), k),
    ]), smap or {})


# ---------------------------------------------------------------------------------- the index
def load_tag_index():
    """The playbook-render kit's `tag_index` and `record_extract`, reached at call time, never at import.
    FindError naming the kit where it does not resolve."""
    try:
        kit = resolve_kit_dir("playbook", "tag_index.py", KIT)
    except LookupError as exc:
        raise FindError(f"record find reads the playbook-render kit's tag index, and {exc}") from None
    if str(kit) not in sys.path:
        sys.path.append(str(kit))
    import record_extract  # noqa: E402
    import tag_index  # noqa: E402
    return tag_index, record_extract


def load_view(root):
    """`(con, ctx, tree, ti)`: the node's index brought up to date and this worktree's view served."""
    ti, _rx = load_tag_index()
    try:
        ctx = ti.derive_context(root, ti.KIT_DIR / "namespaces.toml")
        con = ti.load_index(root)
        view = ti.load_view(con, root, ctx)
    except ti.TagError as exc:
        raise FindError(str(exc)) from None
    return con, ctx, view["tree"], ti


def load_served(root):
    """memory-recall's served set over the node's index: `(con, ctx, tree, ti, smap)`, `smap` the
    supersession map of the served pairs' `fts_supersession` edges (TOOL-dTotalRecall-21 S4)."""
    load_recall_kit()
    import query  # noqa: E402  memory-recall's, on the path load_recall_kit put it on
    ti, _rx = load_tag_index()
    try:
        served = query.load_served_set(pathlib.Path(root), untracked=False)
    except (ti.TagError, query.UnbornHeadError, sqlite3.DatabaseError) as exc:
        raise FindError(str(exc)) from None
    con = served["con"]
    smap = query.derive_served_supersessions(con, served["pairs"])[0]
    ctx = ti.derive_context(root, ti.KIT_DIR / "namespaces.toml")
    return con, ctx, served["tree"], ti, smap


def read_supersession_map(root) -> tuple:
    """`(con, ctx, tree, ti, smap)` for a filter-only find: the served map where the recall kit resolves,
    else `row_grammar.derive_relation_successors`' direct derivation over the corpus."""
    try:
        resolve_kit_dir("memory-recall", "query.py", KIT)
    except LookupError:
        import row_grammar  # noqa: E402  this kit's own map, read without the recall kit
        con, ctx, tree, ti = load_view(root)
        return con, ctx, tree, ti, row_grammar.derive_relation_successors(root)
    return load_served(root)


RECORD_ROWS = ("SELECT DISTINCT p.tag, p.path, p.line, p.blob, b.end_line, b.text FROM path_row p "
               "JOIN view_path v ON p.path=v.path AND p.blob=v.blob "
               "JOIN view_version w ON p.extractor=w.extractor AND p.version=w.version "
               "JOIN view_conf c ON p.conf=c.conf "
               "JOIN blob_row b ON b.blob=p.blob AND b.extractor=p.extractor AND b.version=p.version "
               "AND b.kind=p.kind AND b.line=p.line WHERE p.kind=?")


def scan_records(con, ctx, *, kind=None, tag=None, build=None, paths=None) -> list[dict]:
    """The served view's records, each `{key, kind, build, path, line, end_line, blob}`, that every given
    filter admits: `kind` the record's kind, `tag` its `record.<kind>` or a `section.<seg>` row inside
    it, `build` the slug of the build folder holding it, `paths` a glob over its path."""
    mr = ctx["memory_root"]
    build_re = re.compile(re.escape(mr) + r"/builds/([^/]+)/")
    sections = collections.defaultdict(list)
    if tag and tag.startswith("section."):
        for _t, path, line, _blob, end, _text in con.execute(RECORD_ROWS + " AND p.tag=?", ("section", tag)):
            sections[path].append(line)
    out = []
    for rtag, path, line, blob, end, key in con.execute(RECORD_ROWS, ("record",)):
        k = rtag[len("record."):] if rtag.startswith("record.") else ""
        m = build_re.match(path)
        b = m.group(1) if m else ""
        if kind is not None and k != kind or build is not None and b != build:
            continue
        if paths is not None and not fnmatch.fnmatchcase(path, paths):
            continue
        if tag and (not any(line <= s <= end for s in sections.get(path, ())) if tag.startswith("section.")
                    else rtag != tag):
            continue
        out.append({"key": key, "kind": k, "build": b, "path": path, "line": line, "end_line": end, "blob": blob})
    return out


def read_view_texts(root, con, tree, rows) -> dict:
    """`{(path, blob): text}` for `rows`: a HEAD-tree blob through `tree_lib.read_blobs_at`, a dirty one
    from the working file."""
    held = {}
    for r in rows:
        hit = con.execute("SELECT blob FROM tree_path WHERE tree=? AND path=?", (tree, r["path"])).fetchone()
        held[(r["path"], r["blob"])] = bool(hit and hit[0] == r["blob"])
    got = tree_lib.read_blobs_at(root, [(tree, p) for (p, _b), h in held.items() if h])
    out = {}
    for (path, blob), h in held.items():
        if h:
            out[(path, blob)] = got.get((tree, path)) or ""
        else:
            try:
                out[(path, blob)] = tree_lib.read_text(os.path.join(str(root), path))
            except (OSError, UnicodeDecodeError):
                out[(path, blob)] = ""
    return out


def derive_slice(text: str, line: int, end: int) -> str:
    """Lines `line` to `end` of `text`, 1-based and inclusive, joined by newlines."""
    return "\n".join(text.split("\n")[line - 1:end])


def check_superseded(key: str, smap: dict) -> list[str]:
    """The whole successors the supersession map names for `key`; [] for a current record."""
    return [n for n, kind in smap.get(key, []) if kind == "whole"]


def scan_question(con, rows, question, terms, smap) -> list[dict]:
    """`rows` ranked by the fusion over the FTS tables for `question`, one per record, superseded hits
    out: a hit joins the record its id keys, else the record file at its path, else the anchored record
    holding its line."""
    expr = query_expr(question, terms)
    if expr is None:
        raise FindError("the question holds no searchable term; add words or --terms")
    by_key = {r["key"]: r for r in rows}
    by_path = collections.defaultdict(list)
    for r in rows:
        by_path[r["path"]].append(r)
    out, seen = [], set()
    for hit in run_fusion(con, expr, QUESTION_DEPTH, smap):
        if hit.get("supersession") == "whole":
            continue
        r = by_key.get(hit.get("id") or "")
        if r is None:
            held = [x for x in by_path.get(hit["path"], ()) if x["line"] <= (hit["line"] or 1) <= x["end_line"]]
            r = min(held, key=lambda x: x["end_line"] - x["line"]) if held else None
        if r is not None and (r["path"], r["line"]) not in seen:
            seen.add((r["path"], r["line"]))
            out.append(r)
    return out


def run_find(root, question=None, terms=None, **filters) -> list[str]:
    """S3's lines: at most FIND_CAP record rows, then the total line where more match."""
    if question:
        con, ctx, tree, _ti, smap = load_served(root)
    else:
        con, ctx, tree, _ti, smap = read_supersession_map(root)
    try:
        rows = scan_records(con, ctx, **filters)
        if question:
            rows = scan_question(con, rows, question, terms, smap)
        else:
            rows = sorted((r for r in rows if not check_superseded(r["key"], smap)),
                          key=lambda r: (r["build"], r["key"], r["path"], r["line"]))
        shown = rows[:FIND_CAP]
        texts = read_view_texts(root, con, tree, shown)
    finally:
        con.close()
    lines = []
    for r in shown:
        size = len(derive_slice(texts[(r["path"], r["blob"])], r["line"], r["end_line"]).encode("utf-8"))
        lines.append(f"{r['key']} · {r['kind'] or '-'} · {r['build'] or '-'} · {size} · {r['path']}:{r['line']}")
    if len(rows) > FIND_CAP:
        lines.append(f"{len(rows)} rows match; narrow with --kind, --build or --paths")
    return lines


def read_git_blob(root, blob: str) -> tuple[str, str]:
    """`(full sha, text)` of the blob `blob` names; FindError naming it where git holds no such blob."""
    p = subprocess.run(["git", "rev-parse", "--verify", "-q", f"{blob}^{{blob}}"], cwd=str(root),
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    sha = p.stdout.strip()
    if p.returncode != 0 or not sha:
        raise FindError(f"blob {blob} is no blob of this repository")
    q = subprocess.run(["git", "cat-file", "blob", sha], cwd=str(root), capture_output=True)
    try:
        return sha, q.stdout.decode("utf-8").replace("\r\n", "\n")
    except UnicodeDecodeError:
        raise FindError(f"blob {blob} is not UTF-8 text") from None


def check_blob_path(root, sha: str, path: str) -> bool:
    """Whether some commit this clone holds, an amended one included, held the blob `sha` at `path`;
    FindError naming git where it refuses."""
    p = subprocess.run(["git", "--literal-pathspecs", "log", "--all", "--reflog", "-m", "-1", "--format=%H",
                        f"--find-object={sha}", "--", path], cwd=str(root), capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if p.returncode != 0:
        raise FindError(f"git log --find-object={sha} refused: {p.stderr.strip()}")
    return bool(p.stdout.strip())


def read_section(root, address: str) -> dict:
    """S5: `{key, tag, path, line, end_line, blob, text}` of `<key>[#<tag>][@<blob>]`: the record, or its
    section of that tag, sliced from its blob, a section counting only inside the record's own extent
    (TOOL-dTotalRecall-121 S5). FindError naming an unknown key, tag or blob."""
    m = ADDRESS_RE.fullmatch(address.strip())
    if not m:
        raise FindError(f"{address} is no <key>[#<tag>][@<blob>] address")
    key, tag, blob = m.group("key"), m.group("tag"), m.group("blob")
    con, ctx, tree, ti = load_view(root)
    try:
        # an id cited as an anchor in several files: its spec's defining H1 first, then by path
        spec_re = re.compile(re.escape(ctx["memory_root"]) + r"/builds/[^/]+/spec/")
        rows = sorted((r for r in scan_records(con, ctx) if r["key"] == key),
                      key=lambda r: (not spec_re.match(r["path"]), r["path"], r["line"]))
        if blob is None:
            if not rows:
                raise FindError(f"key {key} names no record of the served view")
            rec, secs = rows[0], []
            for cand in rows:
                held = [(t, line, end) for t, _p, line, _b, end, _x in con.execute(
                    RECORD_ROWS + " AND p.path=? AND p.blob=?", ("section", cand["path"], cand["blob"]))]
                if not tag or any(s[0] == tag and cand["line"] <= s[1] <= cand["end_line"] for s in held):
                    rec, secs = cand, held
                    break
            text = read_view_texts(root, con, tree, [rec])[(rec["path"], rec["blob"])]
        else:
            sha, text = read_git_blob(root, blob)
            path = next((r["path"] for r in rows if r["blob"] == sha), "")   # where the served view holds it
            held = con.execute("SELECT b.line, b.end_line FROM blob_row b JOIN view_version w ON "
                               "b.extractor=w.extractor AND b.version=w.version WHERE b.blob=? AND b.kind='record' "
                               "AND b.text=?", (sha, key)).fetchone()
            secs = [tuple(x) for x in con.execute(
                "SELECT b.tag, b.line, b.end_line FROM blob_row b JOIN view_version w ON b.extractor=w.extractor "
                "AND b.version=w.version WHERE b.blob=? AND b.kind='section'", (sha,))]
            if held is not None and not path:   # a blob another tree of this node holds
                got = [p for (p,) in con.execute(
                    "SELECT DISTINCT path FROM path_row WHERE blob=? AND kind='record'", (sha,))]
                if not got:
                    raise FindError(f"blob {sha} stands at no path the index holds")
                path = min(got, key=lambda p: (pathlib.PurePosixPath(p).stem != key, p))
            if held is None and not rows:
                raise FindError(f"key {key} names no record of the served view, and blob {sha} holds no indexed "
                                "row of it")
            if held is None:   # a blob no live tree holds under this key has lost its rows: verify its bytes here
                _ti, rx = load_tag_index()
                for cand in dict.fromkeys(r["path"] for r in rows):
                    found = [(r[2], r[3]) for r in rx.extract_record(ctx, cand, text)
                             if r[1] == "record" and r[4] == key]
                    # a stem's row comes from the path alone, so only git's history tells whose text it is
                    stem = pathlib.PurePosixPath(cand).stem == key
                    if found and (not stem or check_blob_path(root, sha, cand)):
                        held, path = found[0], cand
                        secs = [(r[0], r[2], r[3]) for r in rx.extract_section(ctx, cand, text)]
                        break
                if held is None:
                    raise FindError(f"blob {sha} is no version of {key}")
            rec = {"key": key, "path": path, "line": held[0], "end_line": held[1], "blob": sha}
    finally:
        con.close()
    line, end = rec["line"], rec["end_line"]
    if tag:
        inside = [s for s in secs if s[0] == tag and line <= s[1] <= end]
        if not inside:
            raise FindError(f"tag {tag} names no section of {key}")
        _t, line, end = inside[0]
    return {"key": key, "tag": tag, "path": rec["path"], "line": line, "end_line": end, "blob": rec["blob"],
            "text": derive_slice(text, line, end)}


def read_policy(key: str, root, values=None) -> str:
    """One policy key at `root`'s landed revision; FindError naming it where the read refuses or answers
    outside `values`."""
    try:
        value = tree_lib.read_policy_value(key, root)
    except (LookupError, ValueError) as exc:
        raise FindError(f"{key} did not read: {exc}") from None
    if values is not None and value not in values:
        raise FindError(f"{key} reads {value!r}, outside {' | '.join(values)}")
    return value


def read_item_cap(root) -> int:
    """S6: the role's `memory.item-budget` in bytes: MEASURED_CAP under `measured`, else KB times its value."""
    value = read_policy("memory.item-budget", root)
    if value == "measured":
        return MEASURED_CAP
    if not value.isdigit():
        raise FindError(f"memory.item-budget reads {value!r}, which is no KB figure")
    return int(value) * KB


def check_read_set(root, role: str, keys: list[str]) -> tuple[int, list[str]]:
    """S6, S7: `(exit, lines)` of one read set: a `read <key> <bytes> B` line per key, a superseded key
    refused or marked, and the sum over the role's cap answered as `memory.over-budget` says."""
    if not keys:
        raise FindError("budget takes at least one key")
    cap = read_item_cap(root)
    over = read_policy("memory.over-budget", root, OVER_VALUES)
    mode = read_policy("memory.superseded-slices", root, SUPERSEDED_VALUES)
    con, _ctx, _tree, _ti, smap = load_served(root)
    con.close()
    lines, total = [], 0
    for key in keys:
        sec = read_section(root, key)
        size = len(sec["text"].encode("utf-8"))
        total += size
        successors = check_superseded(sec["key"], smap)
        if successors and mode == "refuse":
            return 2, [f"refused budget: {key} is superseded by {', '.join(successors)}"]
        mark = f" superseded-by {', '.join(successors)}" if successors else ""
        lines.append(f"read {key} {size} B{mark}")
    if total > cap and over != "off":
        said = f"memory over budget: {role} {total} B > {cap} B"
        if over == "refuse":
            return 2, [f"refused budget: {said}"]
        lines.append(said)
    return 0, lines


# ---------------------------------------------------------------------------------- the fixture
PLANTS = ("cap", "archive", "superseded", "over-report", "over-refuse", "over-off", "superseded-refuse",
          "superseded-mark", "unheld-blob", "blob-unknown-key", "blob-foreign-text", "blob-foreign-record",
          "missing-section", "section-outside")
FIXTURE_BUILD = "bFix"
#: the kits a fixture copy-installs under its own `tools/`, each found as this kit finds a sibling
FIXTURE_KITS = (("memory-tree", "tree_lib.py"), ("playbook", "tag_index.py"), ("memory-recall", "query.py"),
                ("policy", "policy.py"))
BIG_BYTES = 130_000


def write_fixture_file(root: pathlib.Path, rel: str, text: str) -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(text.encode("utf-8"))


def run_fixture_git(root, *args) -> str:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t.test", GIT_COMMITTER_NAME="t",
               GIT_COMMITTER_EMAIL="t@t.test")
    return subprocess.run(["git", *args], cwd=str(root), env=env, check=True, capture_output=True, text=True,
                          encoding="utf-8", errors="replace").stdout


def build_fixture(top: pathlib.Path, plant: str) -> pathlib.Path:
    """A throwaway repository at `top/repo`, the four kits copy-installed under `tools/`, a memory tree of
    one build, `plant` applied, committed on `main`."""
    root = top / "repo"
    root.mkdir(parents=True)
    run_fixture_git(root, "init", "-q", "-b", "main")
    run_fixture_git(root, "config", "core.autocrlf", "false")
    for home, anchor in FIXTURE_KITS:
        src = KIT if home == KIT.name else resolve_kit_dir(home, anchor, KIT)
        shutil.copytree(src, root / TOOL_ROOT_NAME / home, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    write_fixture_file(root, ".memory-tree.conf",
                       'MEMORY_ROOT="memory"\nDISCIPLINES="tooling decisions"\nFAMILIES="tooling:TOOL decisions:DEC"\n')
    write_fixture_file(root, "memory/README.md", "# memory\n")
    folder = f"memory/builds/{FIXTURE_BUILD}"
    write_fixture_file(root, f"{folder}/README.md", f"---\nslug: {FIXTURE_BUILD}\nids: TOOL-{FIXTURE_BUILD}-1\n---\n# {FIXTURE_BUILD}\n")
    write_fixture_file(root, f"{folder}/build/2026-01-01-build-TOOL-{FIXTURE_BUILD}-1-deviation-1.md",
                       f"# deviation\n\n**Serves:** deviation TOOL-{FIXTURE_BUILD}-1\n\n## Findings\n\nthe first\n\n"  # census: kept cause-writer fixture: a record head its fixture plants
                       "## Findings\n\nthe second\n")
    policy = []
    if plant == "blob-foreign-record":
        write_fixture_file(root, f"{folder}/build/2026-01-01-build-TOOL-{FIXTURE_BUILD}-1-deviation-2.md",
                           f"# deviation 2\n\n**Serves:** deviation TOOL-{FIXTURE_BUILD}-1\n")  # census: kept cause-writer fixture: a record head its fixture plants
    if plant == "cap":
        for i in range(2, FIND_CAP + 2):
            write_fixture_file(root, f"{folder}/build/2026-01-01-build-TOOL-{FIXTURE_BUILD}-1-deviation-{i}.md",
                               f"# deviation {i}\n\n**Serves:** deviation TOOL-{FIXTURE_BUILD}-1\n")  # census: kept cause-writer fixture: a record head its fixture plants
    if plant in ("archive", "superseded", "superseded-refuse", "superseded-mark"):
        write_fixture_file(root, "memory/archive/2025-01-01-decisions.md",
                           "# Archived decisions\n\n## DEC-tFix-1 — the boojum colour is mauve\n\n"
                           "The snark hunters paint the boojum mauve.\n")
    if plant in ("superseded", "superseded-refuse", "superseded-mark"):
        write_fixture_file(root, "memory/DECISIONS.md",
                           "# Decisions\n\n## DEC-tFix-2 — the boojum colour is teal\n\n"
                           "Supersedes DEC-tFix-1: the snark hunters paint the boojum teal.\n")
    if plant in ("over-report", "over-refuse", "over-off"):
        head = f"# big\n\n**Serves:** deviation TOOL-{FIXTURE_BUILD}-1\n\n"  # census: kept cause-writer fixture: a record head its fixture plants
        n, rest = divmod(BIG_BYTES - len(head), 100)   # the slice is the text less its last newline
        write_fixture_file(root, f"{folder}/build/2026-01-01-build-TOOL-{FIXTURE_BUILD}-1-deviation-big.md",
                           head + ("x" * 99 + "\n") * n + "y" * rest + "\n")
        policy.append(f'over-budget = "{plant[5:]}"')
    if plant == "superseded-mark":
        policy.append('superseded-slices = "mark"')
    if plant == "section-outside":   # TOOL-dTotalRecall-121 S5: two ids, the one `section.findings` under the second
        write_fixture_file(root, f"{folder}/build/2026-01-01-build-TOOL-{FIXTURE_BUILD}-1-notes.md",
                           f"# notes\n\n**Serves:** research TOOL-{FIXTURE_BUILD}-1\n\n"  # census: kept cause-writer fixture: a record head its fixture plants
                           f"## TOOL-{FIXTURE_BUILD}-11 — the first\n\nno section of its own\n\n"
                           f"## TOOL-{FIXTURE_BUILD}-12 — the second\n\n### Outcome\n\nthe second's outcome\n")
    if plant == "missing-section":
        template = pathlib.Path(KIT.parent.parent, "memory", "TEMPLATE-SPEC.md")
        text = template.read_bytes().decode("utf-8").replace("\r\n", "\n") if template.is_file() else ""
        write_fixture_file(root, "memory/TEMPLATE-SPEC.md", text.replace("## 6. Acceptance criteria\n", ""))
    if policy:
        write_fixture_file(root, ".governance/policy.toml", "[memory]\n" + "\n".join(policy) + "\n")
    run_fixture_git(root, "add", "-A")
    run_fixture_git(root, "commit", "-q", "-m", "fixture")
    return root


def run_fixture_cli(root, argv) -> tuple[int, list[str]]:
    """The fixture's own copy of the door run in it, as an operator runs it."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    p = subprocess.run([sys.executable, str(root / TOOL_ROOT_NAME / KIT.name / "gov_record.py"), *argv], cwd=str(root),
                       env=env, capture_output=True, text=True, encoding="utf-8", errors="replace",
                       stdin=subprocess.DEVNULL)
    return p.returncode, [ln for ln in (p.stdout + p.stderr).splitlines() if ln.strip()]


def run_fixture(plant: str) -> tuple[int, list[str]]:
    """`--fixture --plant <case>`: the fixture built under the system temp directory and the plant's verb
    run there; every line it printed, then `record-find: fixture <plant> · exit <n>`."""
    if plant not in PLANTS:
        return 2, [f"{SAY}: refused · no plant {plant!r}: the plants are {', '.join(PLANTS)}"]
    top = pathlib.Path(tempfile.mkdtemp(prefix="rf-"))
    try:
        root = build_fixture(top, plant)
        stem = f"2026-01-01-build-TOOL-{FIXTURE_BUILD}-1-deviation-1"
        question = ["find", "what colour do the snark hunters paint the boojum", "--terms", "boojum colour mauve teal"]
        argv = {"cap": ["find", "--build", FIXTURE_BUILD],
                "archive": question, "superseded": question,
                "superseded-refuse": ["budget", "--role", "gov-builder", "DEC-tFix-1"],
                "superseded-mark": ["budget", "--role", "gov-builder", "DEC-tFix-1"],
                "section-outside": ["show", f"TOOL-{FIXTURE_BUILD}-11#section.outcome"],
                "missing-section": ["new", "spec", f"TOOL-{FIXTURE_BUILD}-2", "--tier", "2"]}.get(
            plant, ["budget", "--role", "gov-builder", f"2026-01-01-build-TOOL-{FIXTURE_BUILD}-1-deviation-big"])
        if plant == "unheld-blob":   # the record edited and the commit amended, so no tree holds its old blob
            rel = f"memory/builds/{FIXTURE_BUILD}/build/{stem}.md"
            old = run_fixture_git(root, "rev-parse", f"HEAD:{rel}").strip()
            run_fixture_cli(root, ["show", f"{stem}#section.findings-2"])   # the old blob indexed first
            write_fixture_file(root, rel, (root / rel).read_text(encoding="utf-8").replace("the second", "the third"))
            run_fixture_git(root, "commit", "-q", "-a", "--amend", "-m", "fixture")
            argv = ["show", f"{stem}#section.findings-2@{old}"]
        if plant.startswith("blob-"):   # an address whose blob is not the key's
            key, rel = {"blob-unknown-key": ("NO-SUCH-KEY", f"memory/builds/{FIXTURE_BUILD}/build/{stem}.md"),
                        "blob-foreign-text": (stem, "memory/README.md"),
                        "blob-foreign-record": (stem, f"memory/builds/{FIXTURE_BUILD}/build/{stem[:-1]}2.md")}[plant]
            argv = ["show", f"{key}@{run_fixture_git(root, 'rev-parse', f'HEAD:{rel}').strip()}"]
        rc, lines = run_fixture_cli(root, argv)
        if plant == "section-outside":   # the file's stem reaches the section, the first id does not
            stem_rc, shown = run_fixture_cli(root, ["show", f"2026-01-01-build-TOOL-{FIXTURE_BUILD}-1-notes#section.outcome"])
            lines += shown + [f"{SAY}: fixture section-outside · file stem · exit {stem_rc}"]
        if plant == "missing-section":
            lines.append(f"{SAY}: fixture missing-section · spec files "
                         f"{len(list((root / 'memory/builds' / FIXTURE_BUILD).glob('spec/*.md')))}")
        return rc, lines + [f"{SAY}: fixture {plant} · exit {rc}"]
    finally:
        from deviation_join import remove_tree   # noqa: E402  the kit's fixture helper
        remove_tree(top)


def main(argv) -> int:
    for s in (sys.stdout, sys.stderr):
        s.reconfigure(encoding="utf-8", errors="replace")
    if argv[:1] == ["--fixture"] and len(argv) == 3 and argv[1] == "--plant":
        rc, lines = run_fixture(argv[2])
        print("\n".join(lines))
        return rc
    print(__doc__.split("\n\n")[1], file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
