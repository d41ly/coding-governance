#!/usr/bin/env python3
"""Ask the memory tree a question and get the records that answer it.

Ported from adopter ic ``scripts/recall/query.py`` at 5318064 (file last changed fd6274d).
Eight constructs are edited and the rest is upstream's byte for byte, so a re-pull is a three-way merge:
(1) ``corpus_files()`` and the id grammar derive from ``.memory-tree.conf`` via ``recall_conf``;
(2) ``sys.dont_write_bytecode`` above the ``sys.path`` insert; (3) every printed invocation derives
from ``__file__`` and launches ``python3``, and the ``--terms`` refusal's worked example is a
generic one rather than the source project's domain vocabulary; (4) ``--export`` writes beside the
log under the common git dir, or under the conf's ``RECALL_EXPORT_DIR``, and requires ``--tag``;
(5) the rows live in the playbook kit's one index file per node, keyed by path, blob and an
extraction digest folding ``conf_digest`` (TOOL-dTotalRecall-21), where upstream kept a cache per
worktree; (6) an empty record arm, an empty corpus, or an alias layer that joins to nothing is
diagnosed out loud, from counts over the served rows; (7) the served
chunk arm is ROLLED UP through ``run_rollup`` and the two fusion call sites are collapsed into one
``run_fusion()``, so no caller can serve a different shape;
(8) supersession (TOOL-aGraftedHelix-4): the map ``extract`` derives is read from the served rows,
``derive_supersession_order`` runs inside ``run_fusion``, ``render``, ``render_pointer`` and
``emit`` tag a superseded hit's header, and ``main`` prints ``EVIDENCE_BANNER`` once per answer.

Standard library only. Two FTS5 tables -- one row per anchored record, one per 600-char
heading-bounded chunk -- in the tag index under the COMMON git directory, every worktree sharing
them: a call extracts only the (path, blob) pairs it serves that the index lacks, so after one edit
it extracts that one file (``load_served_set``). The QUERY PATH writes nothing inside the worktree,
and neither does ``--export`` unless the conf's ``RECALL_EXPORT_DIR`` declares a repo-relative
destination: otherwise both write only under the common git dir.

Usage:
  {cli} "<question>" --terms "<8-14 coined words>" [--k 20] [--budget N]
  {cli} "<question>" --no-terms      # the un-rewritten baseline, logged
  {cli} "<question>" --rebuild       # re-extract every served file, ignoring the rows already held
  {cli} --opened <rank> [--qid N]    # record which hit you actually read
  {cli} --export --tag <letter>      # aggregate the log beside itself, outside the worktree
  {cli} --used                       # was each answer cited by its worktree's next commit? writes nothing

``--terms`` is REQUIRED. Rewriting is the measured half of the retrieval gain (records recall@20
0.71 -> 0.84, MRR 0.389 -> 0.530, for zero committed bytes) and the CLI cannot generate the terms
itself: that needs a model, and this instrument is stdlib-only and offline on six nodes. The caller
IS a model, so supplying them costs nothing. Supplied terms BYPASS ``bench.terms()`` and are quoted
straight into the MATCH expression -- ``terms()`` would delete ``db``, ``ui``, ``422``, ``c++`` and
every id, which is most of what a rewriter produces.

Why the ranking looks the way it does, in one place so it cannot drift from the instrument:

  * ``--k`` is the depth PER SOURCE, not the length of the merged list. ``union.py`` ranks k from
    ``records`` and k from ``chunks``, so the published ensemble recall at "k=20" is a merged pool
    of up to 40 documents. A CLI whose k meant "20 hits total" would score a different, smaller
    configuration than the one that was measured.
  * The two rankings are fused with RECIPROCAL RANK FUSION at 60, reusing ``bench.RRF_K``. Their
    ``bm25()`` scores are not comparable -- different corpora, different IDF, different document
    lengths -- and a raw concatenation gives a merged top-20 that is ~80% chunks, because that set
    is 22x larger.
  * The CHUNK arm is ROLLED UP: it reads ``k * ROLLUP_DEPTH`` deep and keeps the best hit per
    parent before fusion, so a top-k cannot be several slices of one document. It is what
    ``bench.run_rollup`` grades as the ``roll`` substrate, and with terms at the live chunk width
    that substrate is the only chunk configuration that beats grep. What it costs is the deeper
    read; what it buys is slot diversity, which is the same thing the duplicate-path rate measures.
    ``run_rollup``'s own docstring in ``bench.py`` advises against expecting an ensemble gain from
    this, and that advice was measured on the BARE question -- it is not evidence about the served
    shape, which carries terms. The records arm is untouched, where the rollup is a no-op.
  * An id in the question is matched as a PHRASE. ``bench.terms()`` drops tokens of two characters
    or fewer and anything not starting with a letter, so ``ARCH-169`` reaches FTS5 as ``arch`` and
    the governing record ranks 523rd.
  * Output is sized by a BYTE BUDGET, not a document count, because the documents are not the same
    size -- a ``records`` hit averages ~1 020 chars and a chunk is capped at 600, so a fixed hit
    count costs anywhere between 12 KB and 70 KB. The consumer is a model with a context window, so
    bytes are the quantity to bound. Measured: the same recall costs 70 387 B printing whole
    documents and 19 606 B printing snippets.
"""

from __future__ import annotations

import collections
import hashlib
import json
import os
import pathlib
import sqlite3
import statistics
import subprocess
import sys
import time
from datetime import UTC, datetime

# ABOVE the sys.path insert, not below it: importing the siblings makes CPython write their
# bytecode next to the SOURCE, which is inside the adopter's worktree -- so "a query writes nothing
# in your tree" was false by two .pyc files until this line existed (spec F5). Asserted by PATH in
# selftest.py, never by a clean `git status`: a status is also clean when the write was merely
# hidden by a .gitignore rule the adopter may not have.
sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import recall_conf  # noqa: E402

try:
    CONF = recall_conf.resolve()
except recall_conf.ConfError as _e:
    # At QUERY time, not just at adopt time: a later FAMILIES edit would otherwise reintroduce the
    # silent-zero failure with nothing to say about it.
    print(_e, file=sys.stderr)
    raise SystemExit(2) from None

import bench as B  # noqa: E402
import extract as E  # noqa: E402


def load_tag_index():
    """The playbook kit's `tag_index`, the one index file recall writes its rows into, reached through
    the inlined resolver `extract` carries (TOOL-dTotalRecall-21 S4): the kit `requires` playbook."""
    kit = str(E.resolve_kit_dir("playbook", "tag_index.py", pathlib.Path(__file__).resolve().parent))
    if kit not in sys.path:
        sys.path.append(kit)
    import tag_index
    return tag_index


T = load_tag_index()


def _self_path() -> str:
    """This script's path as the adopter spells it -- repo-relative when it can be."""
    me = pathlib.Path(__file__).resolve()
    try:
        return me.relative_to(CONF.root).as_posix()
    except ValueError:
        return me.as_posix()


# ONE expression, reused by the docstring usage block, the REFUSAL and the qid hand-back. Ported
# unedited from upstream, all three named a path that does not exist in an adopter repo -- so the
# instruction printed after every successful query told the caller to run a missing file (spec F7).
# `python3`, not bare `python`: a stock Debian/Ubuntu host without python-is-python3 has no such
# binary, so every instruction this CLI prints would be an exit-127 dead end there. The rendered
# Skill says python3 for the same reason -- these two surfaces must agree or one of them lies.
CLI = "python3 " + _self_path()
# The usage block above is a plain literal so it stays a real docstring; the substitution happens
# once, here, after CLI exists.
__doc__ = (__doc__ or "").replace("{cli}", CLI)

CHUNK_MAX = 600  # pinned by the parent spec: 2400 and 300 both measured worse
CACHE_VERSION = 5  # bump when extraction changes: it is in every row's digest, so old rows are never served
# 4 -> 5 at TOOL-aGraftedHelix-4: the manifest carries the `superseded` map, and a cache built
# without it would be served with no supersession label and no order step, saying nothing.
# 3 -> 4 at the backlog switch-over (TOOL-dDerivedDocket-34 S9): `DURABLE` gained the per-build
# `builds/<slug>/BACKLOG.md` arm and the backlog archives were deleted, so a warm cache would serve
# anchors from files that no longer exist and miss every migrated ask's new durable home.
# 1 -> 2 on 2026-08-02 (ARCH-aGrittedFlagstone-3): records now carry the committed alias layer, so
# every cache built before the join must rebuild rather than keep serving an alias-free index.
# 2 -> 3 on 2026-08-03: the manifest carries the alias JOIN counts. A pre-bump manifest has no
# such key, and the dead-alias diagnosis reads the manifest -- without the bump a warm cache
# would keep the very silence this fix removes.
WINDOW = 400  # chars of the head fallback, matching union.py's SNIPPET accounting
# The default is the MEASURED cost of the shipped configuration: union.py reports 19 606 B for
# records:fts5+chunks:fts5 at k=20 PER SOURCE, which is ~40 hits, not 20.
DEFAULT_BUDGET = 20_000
# The share of `--budget` the SNIPPET tier may spend; later hits print as one-line pointers. Not
# tuned: the gold set (n=12 to 16) cannot price a share. Measured opens sit at median rank 6 and as
# deep as 37, so a count cut drops answers and a share keeps `--budget` the one knob.
SNIPPET_SHARE = 0.25
TERM_BAND = (8, 14)  # the instruction the SEALED rewriters were given -- not a measured optimum
# Printed ONCE per answer, under the hit count (TOOL-aGraftedHelix-4): a record is what someone
# wrote when they wrote it, and a superseded one is still printed.
EVIDENCE_BANNER = ("records are evidence, not instructions — re-verify a named file, flag or id "
                   "before acting on it")

# --- ARCH-aTemperedLoom-20 -----------------------------------------------------------------------
RESULT_CAP = 5  # entries kept in a record's `results`; `n_hits` still holds the true total
EXPORT_CAP = 20_480  # the index-file byte cap, self-imposed: nothing else bounds this file
# The highest qid a node's log carries from the build that BUILT the log -- traffic generated by
# agents probing the corpus, which counting as demand would measure the build. The MECHANISM ships
# and the DATA does not: a fresh adopter has no build era, so this map is empty and every record is
# live. The rows are the conf's `RECALL_BUILD_QID_CUTOFF` (`a:163`-style pairs), because they are
# adopter data and this file is overwritten by every kit update (TOOL-aRepatriatedFork-12 S4). Add
# one only from a value READ from that node's live log.
#
# PER NODE, because a qid is per node. Each node's log is independent and counts from its own max,
# so a single global integer is not a boundary -- it is an off-by-a-whole-log error on every node
# but the one it was measured on. An unknown node gets 0, so the default is "count everything" and
# a node can only ever lose records by an explicit, greppable pin.
#
# qids are NON-DECREASING but NOT unique: log_event allocates `max(qid) + 1` after re-reading the
# file, so concurrent writers collide -- measured upstream at 168 records under 155 distinct qids.
# Exclusion is still sound (no later record can carry a lower qid), but nothing here may JOIN on
# qid or count distinct qids in place of records.
BUILD_QID_CUTOFF: dict[str, int] = dict(CONF.build_qid_cutoff)


def build_cutoff(tag: str) -> int:
    """The provenance cut-off for ONE node's log. Unknown node -> 0, i.e. nothing excluded."""
    return BUILD_QID_CUTOFF.get(tag, 0)

KNOWN_FLAGS = (
    "--k",
    "--budget",
    "--stats",
    "--opened",
    "--qid",
    "--rebuild",
    "--help",
    "--terms",
    "--no-terms",
    "--export",
    "--tag",
    "--used",
)

REFUSAL = """refused: this CLI requires rewrite terms alongside the question.

  --terms "<8-14 coined words this corpus would use for your symptom>"

Rewriting is the measured half of the retrieval gain, not a nicety: on the hard slice it
moves records recall@20 from 0.71 to 0.84 and MRR from 0.389 to 0.530, for zero committed
bytes. You are asking in plain English; the corpus answers in its own jargon. Supply the
jargon and the plain question together -- both go into one query.

  {cli} "why does the gate refuse this push" \\
      --terms "pre-push hook gate leg refusal exit-1 bypass no-verify merge bar \\
               single-head parity"

Terms are what THIS corpus calls your symptom -- one of its id families, a module name, an
error code, a flag key, a file name -- not synonyms of the words you just typed.

To run the un-rewritten baseline deliberately -- a measurement, or checking whether your own
record is findable without help -- pass --no-terms. It is logged as such.""".replace("{cli}", CLI)


def git(repo: pathlib.Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    ).stdout


# TOOL-aCollapsedScan-7 - a SECOND `repo_root()` lived here, shelling a bare `rev-parse` with no
# `-C` anchor at all, so it resolved from the cwd AND was identically fooled by an inherited
# GIT_DIR. One kit, one answer: `recall_conf.repo_root()` walks up for the conf and is the only
# resolver this kit has.


def read_worktree_head(repo: pathlib.Path) -> str | None:
    """The sha HEAD names in this worktree, or None on an unborn HEAD or any git failure.

    Logged on every query row so ``--used`` can find the next commit by ANCESTRY once
    ``git worktree remove`` has taken the reflog (TOOL-aMendedFleet-82). Not ``git()``: that
    helper raises, and an unborn HEAD must not cost the query its log row.
    """
    try:
        p = subprocess.run(["git", "-C", str(repo), "rev-parse", "--verify", "--quiet", "HEAD"],
                           capture_output=True, text=True, encoding="utf-8")
    except OSError:
        return None
    sha = p.stdout.strip()
    return sha if p.returncode == 0 and sha else None


# The query path's corpus walk lived HERE as a second enumerator and is gone: `E.corpus_inputs`
# serves both callers, with `include_untracked=True` the one thing this path asks for.


def log_path(repo: pathlib.Path) -> pathlib.Path:
    return T.common_git_dir(repo) / "recall" / "queries.jsonl"


# ---------------------------------------------------------------------------------- the rows
#
# TOOL-dTotalRecall-21. Recall's rows live in the ONE index file the playbook kit keeps per node,
# `tag_index.derive_index_path`'s, keyed by (path, blob) and the extraction digest: a commit
# re-extracts only the files it changed, and every worktree shares the rows. The tag index's HEAD
# tree and this worktree's dirty rows say which blob each corpus path holds; an untracked corpus
# file is hashed here and lives in no table but recall's own, so no other worktree is served it.

# The three plain tables; the two FTS5 tables are `build_fts_rows`'s own spelling, created on open.
RECALL_SCHEMA = """
CREATE TABLE IF NOT EXISTS fts_blob(path TEXT, blob TEXT, digest TEXT, PRIMARY KEY (path, blob, digest));
CREATE TABLE IF NOT EXISTS fts_supersession(path TEXT, blob TEXT, digest TEXT, old TEXT, new TEXT,
    kind TEXT, pattern TEXT);
CREATE TABLE IF NOT EXISTS fts_digest(worktree TEXT PRIMARY KEY, digest TEXT);
"""
# The fusion and its constants live in memory-tree's `record_find.py`, the record finder's own ranking
# (TOOL-dTotalRecall-9 S3), on the path `extract` put that kit on; imported here, never copied, so this
# CLI and a `query.<name>` caller rank through the one fusion `record find` runs.
from record_find import (  # noqa: E402,F401  re-exported: every reader of this module keeps its spelling
    RECALL_SETS,
    ROLLUP_DEPTH,
    SERVED_JOIN,
    SNIPPET_TOKENS,
    derive_supersession_order,
    query_expr,
    rrf,
    run_fusion,
    run_rollup,
    search,
)


def alias_digest() -> str:
    """Content digest of the committed alias layer, one input of `derive_recall_digest`.

    The corpus is `memory/` and the declared sources only, so an edit to `aliases.json` changes no
    served blob: without this a row extracted before the edit would keep serving un-joined text
    with no signal at all.
    """
    return E.load_aliases()[2]


def derive_recall_digest() -> str:
    """The SHA-1 of the five inputs every row is extracted under (TOOL-dTotalRecall-21 S2).

    `CACHE_VERSION`, the kit's version, `CHUNK_MAX`, `CONF.digest()` and `alias_digest()`: a
    grammar, alias, chunking or extraction change re-extracts every served pair once, and a
    worktree whose conf differs keeps its own rows rather than overwriting another's.
    """
    blob = "\0".join((str(CACHE_VERSION), recall_conf.KIT_MEMORY_RECALL_VERSION, str(CHUNK_MAX),
                      CONF.digest(), alias_digest()))
    return hashlib.sha1(blob.encode("utf-8")).hexdigest()


def derive_served_pairs(repo: pathlib.Path, con, ctx: dict, tree: str, paths: list[str]
                        ) -> list[tuple[str, str]]:
    """``[(path, blob)]`` for each corpus path, in corpus order.

    This worktree's `dirty_path` blob for a tracked file with uncommitted edits (blob ``""``, a
    file gone from the working tree, is not served), else its `tree_path` blob in the HEAD tree,
    else, for an untracked file, the blob ONE `git hash-object` call prints over the untracked
    paths, read from stdin so the paths never meet a command-line length limit.
    """
    dirty = dict(con.execute("SELECT path, blob FROM dirty_path WHERE worktree=?", (ctx["worktree"],)))
    held = dict(con.execute("SELECT path, blob FROM tree_path WHERE tree=?", (tree,)))
    loose = [p for p in paths if p not in dirty and p not in held]
    hashed: dict[str, str] = {}
    if loose:
        out = subprocess.run(["git", "-C", str(repo), "hash-object", "--stdin-paths"],
                             input="\n".join(loose) + "\n", capture_output=True, text=True,
                             encoding="utf-8", errors="replace")
        if out.returncode != 0:
            raise T.TagError(f"`git hash-object` over {len(loose)} untracked corpus file(s) failed: "
                             f"{out.stderr.strip()}")
        hashed = dict(zip(loose, out.stdout.split()))
    pairs = []
    for p in dict.fromkeys(paths):
        blob = dirty[p] if p in dirty else held.get(p) or hashed.get(p, "")
        if blob:
            pairs.append((p, blob))
    return pairs


def remove_recall_pairs(con, keys) -> None:
    """Delete every row of recall's five-table set keyed by one of ``keys``' (path, blob, digest).

    Through a temp table and ONE scan per FTS5 table, by rowid: an FTS5 table has no index on an
    UNINDEXED column, so a delete per key would scan the table once per key."""
    con.execute("CREATE TEMP TABLE IF NOT EXISTS recall_drop(path TEXT, blob TEXT, digest TEXT, "
                "PRIMARY KEY (path, blob, digest))")
    con.execute("DELETE FROM recall_drop")
    con.executemany("INSERT OR IGNORE INTO recall_drop VALUES (?,?,?)", keys)
    for table in RECALL_SETS.values():
        con.execute(f"DELETE FROM {table} WHERE rowid IN (SELECT f.rowid FROM {table} f CROSS JOIN recall_drop k "
                    "ON f.path = k.path AND f.blob = k.blob AND f.digest = k.digest)")
    for table in ("fts_supersession", "fts_blob"):
        con.execute(f"DELETE FROM {table} WHERE EXISTS (SELECT 1 FROM recall_drop k WHERE k.path = "
                    f"{table}.path AND k.blob = {table}.blob AND k.digest = {table}.digest)")
    con.execute("DELETE FROM recall_drop")


def remove_unheld_recall_rows(con, repo: pathlib.Path) -> int:
    """Drop the rows of pairs no tree, dirty row or this call's served set holds, and of digests no
    live worktree's `fts_digest` row names; returns the pairs dropped.

    Run inside the transaction of a call that extracted. A worktree `git worktree list` no longer
    names loses its digest row first. Another live worktree's untracked pairs are held by nothing
    here, so they go too, and that worktree re-extracts them at its next query.
    """
    _trees, tops = T.read_worktree_trees(repo)
    for (wt,) in con.execute("SELECT worktree FROM fts_digest").fetchall():
        if wt not in tops:
            con.execute("DELETE FROM fts_digest WHERE worktree=?", (wt,))
    dead = con.execute(
        "SELECT path, blob, digest FROM fts_blob b WHERE b.digest NOT IN (SELECT digest FROM fts_digest) "
        "OR (NOT EXISTS (SELECT 1 FROM tree_path t WHERE t.blob = b.blob AND t.path = b.path) "
        "AND NOT EXISTS (SELECT 1 FROM dirty_path d WHERE d.blob = b.blob AND d.path = b.path) "
        "AND NOT EXISTS (SELECT 1 FROM recall_view v WHERE v.path = b.path AND v.blob = b.blob "
        "AND v.digest = b.digest))").fetchall()
    if dead:
        remove_recall_pairs(con, dead)
    return len(dead)


def write_recall_rows(con, repo: pathlib.Path, worktree: str, pairs: list[tuple[str, str]],
                      declared: list[str], digest: str, *, rebuild: bool = False) -> int:
    """Extract each served pair `fts_blob` lacks at ``digest`` (every pair under ``rebuild``), all
    inside ONE `BEGIN IMMEDIATE` transaction; returns the pairs extracted.

    Today's record, chunk, declaration and alias extraction, per path, reading the path's working
    bytes: a pair is a tracked blob only when those bytes are its blob. Records, their supersession
    edges and chunks for a corpus file; declaration chunks for a declared source. The worktree's
    `fts_digest` row is written on every call; any call that extracted then sweeps the rows nothing
    holds (`remove_unheld_recall_rows`).
    """
    declared_set = set(declared)
    try:
        with con:
            con.execute("BEGIN IMMEDIATE")
            con.execute("INSERT OR REPLACE INTO fts_digest VALUES (?,?)", (worktree, digest))
            held = set() if rebuild else set(
                con.execute("SELECT path, blob FROM fts_blob WHERE digest=?", (digest,)))
            todo = [pr for pr in pairs if pr not in held]
            if not todo:
                return 0
            if rebuild:
                remove_recall_pairs(con, [(p, b, digest) for p, b in todo])
            by_id, _src, _ = E.load_aliases()
            for path, blob in todo:
                try:
                    text = (repo / path).read_text(encoding="utf-8", errors="replace")
                except OSError:
                    text = ""
                records, chunks, edges = [], [], []
                if text and path not in declared_set:
                    records = E.extract_records(path, text)
                    edges = E.extract_supersessions(path, text, records)
                    chunks = E.extract_chunks(path, text, CHUNK_MAX)
                if path in declared_set:
                    chunks += E.extract_declarations(path, text)
                E.join_aliases(records, by_id)
                B.build_fts_rows(con, RECALL_SETS["records"], records, path=path, blob=blob, digest=digest)
                B.build_fts_rows(con, RECALL_SETS["chunks"], chunks, path=path, blob=blob, digest=digest)
                con.executemany("INSERT INTO fts_supersession VALUES (?,?,?,?,?,?,?)",
                                [(path, blob, digest, *e) for e in edges])
                con.execute("INSERT OR REPLACE INTO fts_blob VALUES (?,?,?)", (path, blob, digest))
            remove_unheld_recall_rows(con, repo)
    except sqlite3.OperationalError as exc:
        raise T.TagError(f"the tag index {T.derive_index_path(repo).as_posix()} is locked or "
                         f"unwritable: {exc}") from None
    return len(todo)


class UnbornHeadError(RuntimeError):
    """HEAD names no commit, so the served set has no tree (TOOL-dTotalRecall-21 S4): the remedy is a
    first commit, never the index file's removal."""


def load_served_set(repo: pathlib.Path, *, untracked: bool = True, rebuild: bool = False) -> dict:
    """Open the node's index, bring this worktree's view up to date, and fill `recall_view`.

    `tag_index.load_view` once, for the HEAD tree and this worktree's tracked edits; then each path
    `corpus_inputs(repo, include_untracked=untracked)` lists mapped to its blob
    (`derive_served_pairs`); then `write_recall_rows`. Recall's five tables are created when absent,
    so they come back at the first open after a tag-index reset. ``rebuild`` re-extracts every
    served pair at the digest, the `--rebuild` escape hatch.

    Returns ``{"con", "tree", "digest", "pairs", "extracted", "seconds"}``; the caller closes
    ``con``. Raises `tag_index.TagError` or `sqlite3.DatabaseError`, each naming the file, and
    `UnbornHeadError` BEFORE the index is opened when HEAD names no commit: `load_view` reads the
    HEAD tree, and a repository with no commit has none, which no removal of the file mends.
    """
    t0 = time.time()
    if read_worktree_head(repo) is None:  # `git rev-parse --verify -q HEAD`
        raise UnbornHeadError(f"{repo.as_posix()} has no commit, so there is no HEAD tree to serve; "
                              "make a first commit (`git commit`) and ask again")
    con = T.load_index(repo)
    try:
        con.executescript(RECALL_SCHEMA)
        for table in RECALL_SETS.values():
            B.build_fts_rows(con, table, [])
        ctx = T.derive_context(repo, T.KIT_DIR / "namespaces.toml")
        view = T.load_view(con, repo, ctx)
        files, declared = E.corpus_inputs(repo, include_untracked=untracked)
        pairs = derive_served_pairs(repo, con, ctx, view["tree"], files + declared)
        digest = derive_recall_digest()
        con.execute("CREATE TEMP TABLE IF NOT EXISTS recall_view(path TEXT, blob TEXT, digest TEXT, "
                    "PRIMARY KEY (path, blob, digest))")
        con.execute("DELETE FROM recall_view")
        con.executemany("INSERT OR IGNORE INTO recall_view VALUES (?,?,?)", [(p, b, digest) for p, b in pairs])
        extracted = write_recall_rows(con, repo, ctx["worktree"], pairs, declared, digest, rebuild=rebuild)
    except BaseException:
        con.close()
        raise
    return {"con": con, "tree": view["tree"], "digest": digest, "pairs": pairs,
            "extracted": extracted, "seconds": round(time.time() - t0, 2)}


def read_served_counts(con) -> dict:
    """``{"records", "chunks", "joined"}`` over the served rows, `joined` the records an alias
    reached: the figures the index line and both diagnoses read."""
    rec, joined = con.execute(f"SELECT COUNT(*), COALESCE(SUM(f.alias != ''), 0) FROM fts_record f "
                              f"{SERVED_JOIN}").fetchone()
    (chunks,) = con.execute(f"SELECT COUNT(*) FROM fts_chunk f {SERVED_JOIN}").fetchone()
    return {"records": rec, "chunks": chunks, "joined": joined}


def derive_served_supersessions(con, pairs: list[tuple[str, str]]) -> tuple[dict, dict]:
    """`extract.derive_supersession_map` over the served pairs' `fts_supersession` edges, in corpus
    order, with every served record id as defined: the map and counts the manifest carried."""
    order = {p: i for i, (p, _b) in enumerate(pairs)}
    rows = con.execute("SELECT f.path, f.old, f.new, f.kind, f.pattern FROM fts_supersession f "
                       f"{SERVED_JOIN} ORDER BY f.rowid").fetchall()
    rows.sort(key=lambda r: order.get(r[0], len(order)))
    defined = {i for (i,) in con.execute(f"SELECT f.id FROM fts_record f {SERVED_JOIN} WHERE f.id != ''")}
    return E.derive_supersession_map([r[1:] for r in rows], defined)


def dead_alias_diagnosis(aliases: dict) -> str | None:
    """An alias layer that loaded ids and joined to NOT ONE of them, named out loud.

    The zero-record class one layer in. The alias column is a down-weighted ranking aid, so an
    alias file authored against another id family is 100% dead with no symptom beyond slightly
    worse ranking -- a content hash says nothing about coverage. ``aliases`` is
    ``{"ids", "joined", "src"}``, `joined` counted from the SERVED rows, so this fires identically
    on a call that extracted and on one that extracted nothing. Silent on a partial join: some ids
    resolving is the normal state of an alias file written ahead of the records it names.
    """
    a = aliases or {}
    if not a.get("ids") or a.get("joined"):
        return None
    return (
        f"DEAD ALIAS LAYER — {a['ids']} alias ids loaded and not one joined to a record.\n"
        f"  alias source: {a.get('src', '?')}\n"
        f"  FAMILIES in {CONF.path.as_posix()} resolved to: {' '.join(CONF.families)}\n"
        "  Not one of those ids names a record in this corpus, so the alias column is empty and\n"
        "  the only symptom is slightly worse ranking. Check the ids are this corpus's own."
    )


# ---------------------------------------------------------------------------------- querying


def render_supersession_tag(hit: dict) -> str:
    """The header tag for a superseded hit, or "" — one spelling for both renderers."""
    if not hit.get("superseded_by"):
        return ""
    part = "partly " if hit.get("supersession") == "partial" else ""
    return f"  [{part}superseded by {', '.join(hit['superseded_by'])}]"


# ---------------------------------------------------------------------------------- emission


def render(hit: dict, question: str, extra_terms: list[str] | None = None) -> tuple[str, bool]:
    """One hit as text, plus whether it fell back to a head window.

    ``snippet(d, 1, …)`` returns the BODY's leading tokens rather than a query-biased window when
    the match landed only in the ``head`` or ``alias`` column -- measured, 5 of 3 680 fixture hits.
    Those are labelled rather than passed off as match windows.

    The header is ``id · path:line`` and carries NO heading. ``union.py`` charges 100 B per hit for
    "id + path + heading"; measured on this corpus, id + path:line is 61 B mean / 102 B p90 and
    fits, while adding the heading takes the mean to 646 B -- six times the accounting every byte
    figure in the parent spec rests on.
    """
    wanted = set(B.terms(question)) | {t.lower() for t in (extra_terms or [])}
    body = " ".join((hit["snippet"] or "").split())
    is_head = bool(wanted) and not any(w in body.lower() for w in wanted)
    if not body:
        body = " ".join(hit["text"].split())[:WINDOW]
        is_head = True
    head = f"{hit['id']} · " if hit["id"] else ""
    tag = "  [head window — matched on the title, not the body]" if is_head else ""
    sup = render_supersession_tag(hit)
    return f"{head}{hit['path']}:{hit['line']}{sup}{tag}\n    {body}", is_head


def render_pointer(hit: dict, n: int) -> str:
    """One hit as a single line, ``[n] id · path:line`` -- the header half of ``render``, so it
    carries the supersession tag too: a deep superseded hit printed untagged reads as current."""
    head = f"{hit['id']} · " if hit["id"] else ""
    return f"[{n}] {head}{hit['path']}:{hit['line']}{render_supersession_tag(hit)}"


def emit(
    hits: list[dict], question: str, budget: int, full: bool = False
) -> tuple[str, int, int, int, int]:
    """Render hits in rank order, in two tiers, until the NEXT one would exceed ``budget``.

    The SNIPPET tier renders whole hits while their bytes stay within ``SNIPPET_SHARE`` of the
    budget, and the first hit is always in it. Every later hit is a POINTER, one line, so a deep
    hit stays in the list at a fraction of a snippet's cost (TOOL-aMendedFleet-31).

    Returns ``(text, shown, bytes_spent, overflow, snippets)``; ``shown`` counts both tiers. The one
    exception to the bound is a budget too small for even the first hit: that hit is emitted alone
    and ``overflow`` says by how much, rather than printing an empty list that reads as "no such
    record". ``bytes_spent`` counts each hit's own bytes, not the newlines that separate them.

    ``full=True`` renders whole documents instead of snippets. It is not a CLI flag -- restoring
    whole-document output is the cost this item exists to remove -- it exists so the saving can be
    MEASURED against the same ranked pool rather than against a number written in a document.
    """
    snippet_parts: list[str] = []
    pointer_parts: list[str] = []
    spent = overflow = 0
    for n, h in enumerate(hits, 1):
        if not pointer_parts:
            if full:
                text = (f"{h['id'] + ' · ' if h['id'] else ''}{h['path']}:{h['line']}"
                        f"{render_supersession_tag(h)}\n    {h['text']}")
            else:
                text, _ = render(h, question)
            chunk = f"[{n}] {text}\n"
            cost = len(chunk.encode())
            if not snippet_parts and cost > budget:
                snippet_parts.append(chunk)
                spent, overflow = cost, cost - budget
                break
            if not snippet_parts or spent + cost <= budget * SNIPPET_SHARE:
                snippet_parts.append(chunk)
                spent += cost
                continue
        chunk = render_pointer(h, n) + "\n"
        cost = len(chunk.encode())
        if spent + cost > budget:
            break
        pointer_parts.append(chunk)
        spent += cost
    text = "\n".join(snippet_parts)
    if pointer_parts:
        text += "\n" + "".join(pointer_parts)
    return text, len(snippet_parts) + len(pointer_parts), spent, overflow, len(snippet_parts)


# ---------------------------------------------------------------------------------- the log


def log_event(repo: pathlib.Path, event: dict) -> int | None:
    """Append one JSONL record. Never fatal: a query that answered is worth more than its log."""
    p = log_path(repo)
    try:
        p.parent.mkdir(parents=True, exist_ok=True)
        qid = 0
        if p.exists():
            with p.open(encoding="utf-8") as fh:
                for line in fh:
                    try:
                        qid = max(qid, json.loads(line).get("qid", 0))
                    except ValueError:
                        continue
        qid += 1
        event = {"qid": qid, "at": datetime.now(UTC).isoformat(timespec="seconds"), **event}
        with p.open("a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(event, ensure_ascii=False) + "\n")
        return qid
    except OSError as e:
        print(f"warning: query log not written ({e})", file=sys.stderr)
        return None


def last_qid(repo: pathlib.Path) -> int | None:
    p = log_path(repo)
    if not p.exists():
        return None
    qid = None
    with p.open(encoding="utf-8") as fh:
        for line in fh:
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if row.get("type") != "opened":
                qid = row.get("qid", qid)
    return qid


def qid_exists(repo: pathlib.Path, qid: int) -> bool:
    """Is there a non-``opened`` row carrying this qid?

    A typo'd ``--qid`` would otherwise write a dangling outcome record into the one
    instrument this feature has, and nothing downstream could tell it from a real one.
    """
    p = log_path(repo)
    if not p.exists():
        return False
    with p.open(encoding="utf-8") as fh:
        for line in fh:
            try:
                row = json.loads(line)
            except ValueError:
                continue
            if row.get("qid") == qid and row.get("type") != "opened":
                return True
    return False


# ------------------------------------------------------- the export (ARCH-aTemperedLoom-20)


# FORKED: upstream resolved the node tag by parsing its own CLAUDE.md node registry, a document no
# adopter has. `--tag` is required for `--export` instead; a project-specific lookup is exactly the
# hand-kept second copy this port exists to remove.


def read_log(repo: pathlib.Path) -> list[dict]:
    p = log_path(repo)
    if not p.exists():
        return []
    rows = []
    with p.open(encoding="utf-8") as fh:
        for line in fh:
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    return rows


def _table(header: list[str], body: list[list[str]]) -> list[str]:
    return [
        "| " + " | ".join(header) + " |",
        "|" + "|".join("---" for _ in header) + "|",
        *["| " + " | ".join(r) + " |" for r in body],
    ]


def export_text(rows: list[dict], tag: str, cutoff: int | None = None,
                export_dir: str | None = None) -> str:
    """The aggregate, as markdown. Pure: same rows in, byte-identical text out.

    NO wall clock and NO unordered iteration anywhere -- a ``generated <now>`` line is the natural
    thing to write and it would churn a tracked file on every session close, which is the one thing
    ``--export`` promises not to do. Every table sorts on a stated key.

    NO raw query text. Not for secrecy -- a dev question is not sensitive -- but because raw text
    is what makes the artifact big, churn-prone and unmergeable, and no question the log exists to
    answer needs it.
    """
    # Resolved from the TAG, so the boundary is the one belonging to the log being read. A caller
    # may override for a test, but never inherits another node's number by default.
    if cutoff is None:
        cutoff = build_cutoff(tag)
    # LABEL, do not EXCLUDE (owner 2026-07-28). The perishable asset is the BOUNDARY, not the
    # exclusion: node `a`'s build-era records are separable by qid and only approximately by date,
    # because a genuine query landed the same day. So both segments are REPORTED and neither is
    # hidden -- a mechanism that can silently drop a record is a poor guardian for a risk that
    # shrinks on its own, and this one had already misfired once by eating a foreign node's log.
    build_era = [r for r in rows if r.get("qid", 0) <= cutoff]
    kept = [r for r in rows if r.get("qid", 0) > cutoff]
    queries = [r for r in kept if r.get("type") == "query"]

    def _seg(rs: list[dict]) -> list[str]:
        qs = [r for r in rs if r.get("type") == "query"]
        return [
            str(len(rs)),
            str(len(qs)),
            str(sum(1 for r in rs if r.get("type") == "refused")),
            str(sum(1 for r in qs if not r.get("rewritten"))),
        ]

    out = [
        f"# Recall traffic — node `{tag}`",
        "",
        f"Generated by `{CLI} --export --tag {tag}`. One file per node so it never conflicts, and",
        # RENDERED from the destination, never asserted: under `RECALL_EXPORT_DIR` the file IS in
        # the worktree, and a header saying otherwise would be false in every copy of it.
        *(
            [
                f"it is written to `{export_dir}/`, inside the worktree, where `RECALL_EXPORT_DIR`",
                "declares it. It carries counts only, so no free-text question reaches that file.",
                "Aggregate only — no raw query text.",
            ]
            if export_dir
            else [
                "it is written beside the raw JSONL under the common git dir -- OUTSIDE the worktree, so no",
                "free-text question ever reaches a tracked file. Aggregate only — no raw query text.",
            ]
        ),
        "Re-running `--export` on an unchanged log rewrites this file byte-identically.",
        "",
        "## Provenance",
        "",
        *(
            [
                f"`build-era` is every record at or below the pinned boundary `qid <= {cutoff}` —",
                "traffic generated by the build that built this log, probing the corpus. It is",
                "LABELLED, never hidden: counting it as demand would measure that build, but",
                "dropping it would destroy a boundary nothing can reconstruct later (these",
                "records are separable by `qid` and only approximately by date, because a genuine",
                "query landed the same day). Every table after this section covers `live` only,",
                "and this one shows you exactly what that leaves out.",
            ]
            if cutoff
            else [
                "No boundary is pinned for this node, so everything is `live`. The boundary is PER",
                "NODE — a `qid` is per node — and only a node whose log opens with known build",
                "traffic carries one. See `RECALL_BUILD_QID_CUTOFF` in `.memory-tree.conf`.",
            ]
        ),
        "",
        *_table(
            ["segment", "records", "queries", "refused", "--no-terms"],
            [["build-era", *_seg(build_era)], ["live", *_seg(kept)]],
        ),
        "",
        "## Per day",
        "",
        "`live` records only — see Provenance above for what sits below the boundary.",
        "",
    ]

    by_day: dict[str, list[dict]] = collections.defaultdict(list)
    for r in kept:
        by_day[r.get("at", "")[:10] or "(undated)"].append(r)
    body = []
    for day in sorted(by_day):
        rs = by_day[day]
        qs = [r for r in rs if r.get("type") == "query"]
        terms = [len(r.get("terms") or []) for r in qs]
        hits = [r.get("n_hits", 0) for r in qs]
        emitted = [r.get("bytes_emitted", 0) for r in qs]
        body.append([
            day,
            str(len(qs)),
            str(sum(1 for r in qs if r.get("rewritten"))),
            str(sum(1 for r in qs if not r.get("rewritten"))),
            str(sum(1 for r in rs if r.get("type") == "refused")),
            str(sum(1 for r in rs if r.get("type") == "opened")),
            f"{statistics.fmean(hits):.1f}" if hits else "—",
            f"{statistics.fmean(emitted):,.0f}" if emitted else "—",
            f"{statistics.median(terms):.0f}" if terms else "—",
        ])
    out += _table(
        ["day", "queries", "rewritten", "--no-terms", "refused", "opened",
         "mean hits", "mean B out", "median terms"],
        body or [["(none)"] + ["—"] * 8],
    )

    out += ["", "## Supplied-term count", "", "`0` is `--no-terms`, the deliberate baseline.", ""]
    hist = collections.Counter(len(r.get("terms") or []) for r in queries)
    out += _table(
        ["terms", "queries"], [[str(n), str(hist[n])] for n in sorted(hist)] or [["—", "—"]]
    )

    out += [
        "",
        "## Opened rank",
        "",
        "The rank the caller said they actually read. This is the only signal answering *what was",
        "right* rather than *what was asked*; everything else here measures demand.",
        "",
    ]
    oh = collections.Counter(r.get("rank") for r in kept if r.get("type") == "opened")
    out += _table(
        ["rank", "times"],
        [[str(n), str(oh[n])] for n in sorted(oh, key=lambda x: (x is None, x))] or [["—", "—"]],
    )

    out += [
        "",
        "## Top target paths",
        "",
        f"By hit count across retained queries. Records written after `RESULT_CAP={RESULT_CAP}`",
        "carry only their top few hits, so this ranks what callers were SHOWN, not the full pool.",
        "",
    ]
    paths = collections.Counter(
        h.get("path", "") for r in queries for h in (r.get("results") or []) if h.get("path")
    )
    # Count DESC then path ASC, so ties never reorder between runs.
    top = sorted(paths.items(), key=lambda kv: (-kv[1], kv[0]))[:20]
    out += _table(["hits", "path"], [[str(n), f"`{p}`"] for p, n in top] or [["—", "—"]])

    out += [
        "",
        "## By worktree",
        "",
        "A burst from one tree is the shape the cut-off above excluded once already; averaged",
        "into a total it is invisible. `(unrecorded)` is counted rather than dropped — the field",
        "is absent from older query records and from every `refused`/`opened` row, so a table",
        "without it would silently under-report.",
        "",
    ]
    wt = collections.Counter(r.get("worktree") or "(unrecorded)" for r in queries)
    out += _table(
        ["queries", "worktree"],
        [[str(n), w if w == "(unrecorded)" else f"`{w}`"]
         for w, n in sorted(wt.items(), key=lambda kv: (-kv[1], kv[0]))] or [["—", "—"]],
    )
    return "\n".join(out) + "\n"


def read_export_cap(repo: pathlib.Path) -> tuple:
    """`(value, mode, rule)` of the census cap `recall-export` (TOOL-dGroundRules-9): the policy kit's
    `budgets.resolve_caps`, handed EXPORT_CAP as its default, so a `budgets.recall-export` in the
    policy file takes its place; the kit found by the inlined resolver extract.py carries. No kit, or
    any refusal of the reader, keeps EXPORT_CAP under `refuse`, as before, the rule saying why."""
    try:
        kit = str(E.resolve_kit_dir("policy", "budgets.py", pathlib.Path(__file__).resolve().parent))
        if kit not in sys.path:
            sys.path.insert(0, kit)
        import budgets  # the policy kit's caps module, found above
        try:
            a = budgets.resolve_caps([f"recall-export=default:{EXPORT_CAP}"], str(repo))["recall-export"]
            return a.value, a.mode, a.rule
        except budgets.policy.Refusal as exc:
            why = f"the policy reader refused: {exc}"
    except (LookupError, ImportError) as exc:
        why = f"no policy kit answered: {exc}"
    return EXPORT_CAP, "refuse", f"{why}; an export over the cap refuses as before"


def export(repo: pathlib.Path, tag: str) -> int:
    rows = read_log(repo)
    if not rows:
        print(f"no query log at {log_path(repo)} — nothing to export", file=sys.stderr)
        return 1
    text = export_text(rows, tag, export_dir=CONF.export_dir)
    size = len(text.encode())
    cap, mode, rule = read_export_cap(repo)
    # FORKED: beside the log under the common git dir, not `<root>/memory/project/` inside the
    # worktree. That was the kit's ONE tracked write and the only path that could carry a
    # free-text question into version control; moving it keeps the reader and closes the path.
    # An adopter that WANTS the aggregate tracked declares `RECALL_EXPORT_DIR`, which
    # `recall_conf.resolve()` has already refused if it escapes the root (TOOL-aRepatriatedFork-12).
    dest = (repo / CONF.export_dir if CONF.export_dir else T.common_git_dir(repo) / "recall") \
        / f"recall-traffic-{tag}.md"
    if cap and size > cap and mode == "warn":
        # THE SWITCH (TOOL-dGroundRules-9): under `warn` the export writes, and says it is over.
        print(f"BUDGET WARN — recall-export · {dest.as_posix()} · {size} bytes over {cap} · {rule}",
              file=sys.stderr)
        # The runner's `gate-warn` marker on the next line of the same stream (TOOL-dWitnessedBar-29 S2, §8 F4, F5),
        # the policy kit's module already loaded by `read_export_cap`, whose `warn` only it answers.
        import budgets
        print(budgets.render_warn_marker(dest.as_posix(), f"recall-export · {size} bytes over {cap}"),
              file=sys.stderr)
    elif cap and size > cap:
        # A bound nobody can trip is not a bound. Refuse BEFORE writing, so the oversized file
        # never exists.
        print(
            f"refused: the export is {size:,} B, over the {cap:,} B cap ({rule}).\n"
            f"  mv {dest.as_posix()} {dest.as_posix()}.<date>\n"
            "  then re-run --export to start a fresh file.",
            file=sys.stderr,
        )
        return 1
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {dest.as_posix()} ({size:,} B, unchecked)" if not cap else
          f"wrote {dest.as_posix()} ({size:,} B of {cap:,} B)")
    return 0


# ------------------------------------------------------- answer used (TOOL-aMendedFleet-34)
# `--opened` is recorded by hand almost never, so the outcome signal is thin. This joins each logged
# query's result ids to the ids its worktree's NEXT commit cites. Offline and read-only: no index,
# no log row, no file anywhere. A removed worktree's reflog is gone with it, so its rows are counted
# UNATTRIBUTED rather than guessed at; a time window over `git log --all` would credit a query with
# a concurrent session's citation. A row that logged its `head` is the exception (TOOL-aMendedFleet-82):
# its next commit is the ONE child of that sha committed at or after the query, and two such
# children are AMBIGUOUS, never a pick.


def resolve_worktree_reflog(common: pathlib.Path, worktree: str) -> pathlib.Path | None:
    """The HEAD reflog of the tree a query row names, or None when there is none to read.

    A linked worktree's admin dir under ``<common>/worktrees/`` holds a ``gitdir`` file naming
    ``<worktree>/.git``; the primary tree's reflog is the common dir's own. Both sides go through
    ``normcase(abspath())`` because the log spells Windows paths with either separator.
    """
    want = os.path.normcase(os.path.abspath(worktree))
    if want == os.path.normcase(os.path.abspath(common.parent)):
        log = common / "logs" / "HEAD"
        return log if log.is_file() else None
    admin = common / "worktrees"
    if not admin.is_dir():
        return None
    for d in admin.iterdir():
        try:
            named = (d / "gitdir").read_text(encoding="utf-8").strip()
        except OSError:
            continue
        if os.path.normcase(os.path.abspath(os.path.dirname(named))) == want:
            log = d / "logs" / "HEAD"
            return log if log.is_file() else None
    return None


def read_cited_ids(repo: pathlib.Path, shas: list[str]) -> dict[str, tuple[str, set[str]]]:
    """``sha -> (subject, ids cited in its message or added lines)``, from ONE ``git log`` spawn.

    One call, not one per commit: a spawn costs most of a second on some nodes. A sha the object
    store no longer holds is skipped by ``--ignore-missing`` and reads as citing nothing.
    """
    if not shas:
        return {}
    out = subprocess.run(
        ["git", "-C", str(repo), "log", "--no-walk=unsorted", "--stdin", "--ignore-missing",
         "-p", "-U0", "--no-color", "--format=%x1e%H%n%B"],
        input="\n".join(shas) + "\n", capture_output=True, text=True, encoding="utf-8",
        errors="replace", check=True,
    ).stdout
    cited: dict[str, tuple[str, set[str]]] = {}
    for block in out.split("\x1e")[1:]:
        sha, _, rest = block.partition("\n")
        msg, sep, patch = rest.partition("\ndiff --git ")
        ids = set(E.ID_RE.findall(msg))
        if sep:
            added = "\n".join(ln[1:] for ln in patch.splitlines()
                              if ln.startswith("+") and not ln.startswith("+++"))
            ids.update(E.ID_RE.findall(added))
        cited[sha.strip()] = (msg.lstrip("\n").split("\n", 1)[0], ids)
    return cited


def measure_answer_used(repo: pathlib.Path) -> int:
    """Print how many attributable query rows' answers the worktree's next commit cites."""
    log = log_path(repo)
    if not log.exists():
        print(f"no query log at {log.as_posix()} — answer-used not measured", file=sys.stderr)
        return 2
    common = T.common_git_dir(repo)
    rows = [r for r in read_log(repo) if r.get("type") == "query"]
    reflogs: dict[str, list[tuple[int, str]] | None] = {}  # worktree -> commit entries, None = no reflog
    no_id = unattributed = no_commit = by_head = ambiguous = 0
    pending: list[tuple[dict, list[str], str]] = []  # (row, record ids in rank order, next sha)
    orphans: list[tuple[dict, list[str], str, float]] = []  # reflog gone, `head` logged: ancestry
    for row in rows:
        ranked = [res.get("id") or "" for res in row.get("results") or []]
        if not any(E.ID_RE.fullmatch(i) for i in ranked):
            no_id += 1
            continue
        wt = str(row.get("worktree") or "")
        try:
            at = datetime.fromisoformat(row["at"]).timestamp()
        except (KeyError, TypeError, ValueError):
            at = None
        if wt and wt not in reflogs:
            path = resolve_worktree_reflog(common, wt)
            entries = None
            if path is not None:
                # (timestamp, new sha, is a commit) per line; the FIRST line dates the tree itself.
                entries = []
                for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
                    head, _, msg = line.partition("\t")
                    parts = head.split(" ")
                    try:
                        entries.append((int(parts[-2]), parts[1], msg.startswith("commit")))
                    except (IndexError, ValueError):
                        continue
            reflogs[wt] = entries
        entries = reflogs.get(wt) if wt else None
        # A row older than the reflog's first entry ran in an earlier tree at this path, or its
        # entries expired: the join key outlived its subject, so the row is not attributed.
        if not entries or at is None or entries[0][0] > at:
            # TOOL-aMendedFleet-82: the reflog is gone (or is a later tree's), but a row that
            # logged its `head` still names the commit its next commit is a child of.
            if at is not None and row.get("head"):
                orphans.append((row, ranked, str(row["head"]), at))
            else:
                unattributed += 1
            continue
        nxt = next((sha for ts, sha, is_commit in entries if is_commit and ts >= at), None)
        if nxt is None:
            no_commit += 1
            continue
        pending.append((row, ranked, nxt))

    if orphans:
        # ONE spawn for the whole parent map, made only when a row needs it: sha, committer time,
        # parents. A commit no ref reaches is not here, and reads as "no commit after the query".
        children: dict[str, list[tuple[str, int]]] = collections.defaultdict(list)
        out = subprocess.run(["git", "-C", str(repo), "log", "--all", "--format=%H %ct %P"],
                             capture_output=True, text=True, encoding="utf-8", check=True).stdout
        for line in out.splitlines():
            sha, ct, *parents = line.split()
            for par in parents:
                children[par].append((sha, int(ct)))
        for row, ranked, head, at in orphans:
            kids = {sha for sha, ct in children.get(head, []) if ct >= at}
            if len(kids) == 1:
                by_head += 1
                pending.append((row, ranked, kids.pop()))
            elif kids:
                # Two worktrees started from one tip would credit each other's citations.
                ambiguous += 1
                unattributed += 1
            else:
                no_commit += 1
    head_line = f"  attributed by head ancestry: {by_head} · ambiguous head: {ambiguous}"

    if not pending:
        print(f"answer-used: not measured — none of {len(rows)} query row(s) is attributable "
              f"({unattributed} unattributed, {no_commit} no commit after the query, "
              f"{no_id} no record id in results); a removed worktree's reflog is gone",
              file=sys.stderr)
        print(head_line, file=sys.stderr)
        return 2
    cited = read_cited_ids(repo, sorted({sha for _, _, sha in pending}))
    used = 0
    hist = collections.Counter()
    for row, ranked, sha in pending:
        subject, ids = cited.get(sha, ("", set()))
        # The caller already held an id its own question or terms spell, or one from the build its
        # commit's subject names, so citing it says nothing about the answer. WHOLE tokens, never
        # substrings: `TOOL-aFoo-1` is not held by a row spelling `TOOL-aFoo-12`.
        held = set(E.ID_RE.findall(" ".join([str(row.get("query") or ""),
                                              *map(str, row.get("terms") or [])])))
        words = set("".join(c if c.isalpha() else " " for c in subject).split())
        for rank, rid in enumerate(ranked, 1):
            try:  # the one id parser, through extract's import (TOOL-dTotalRecall-38 S3)
                slug = E.id_grammar.parse_id_parts(rid, None)[1]
            except ValueError:
                slug = None
            if rid in ids and rid not in held and slug not in words:
                used += 1
                hist[rank] += 1
                break
    print(f"answer-used: {used} of {len(pending)} attributable query row(s) cite a shown record id "
          "in the worktree's next commit")
    print(f"  of {len(rows)} query rows: {unattributed} unattributed (reflog gone) · {no_commit} "
          f"no commit after the query · {no_id} no record id in results")
    print("  used at rank: " + " ".join(f"{r}:{hist[r]}" for r in range(1, RESULT_CAP + 1))
          + " — a deeper rank is not logged")
    print(head_line)
    return 0


# ---------------------------------------------------------------------------------- main


VALUE_FLAGS = ("--k", "--budget", "--opened", "--qid", "--terms", "--tag")
BARE_FLAGS = ("--stats", "--rebuild", "--help", "--no-terms", "--export", "--used")


def parse(argv: list[str]) -> tuple[dict[str, str], list[str], str | None]:
    """One left-to-right scan. Returns ``(flags, positionals, error)``.

    The scan replaces a first-non-dash guess plus a repair loop, which got the question wrong for
    any ordering the repair did not anticipate: ``query.py --terms "a b" --budget 400 "question"``
    picked up ``400`` and queried it, printing "33 hits for: 400". A parser that has to be repaired
    per flag ordering is a parser that is wrong for the next ordering.
    """
    flags: dict[str, str] = {}
    pos: list[str] = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a.startswith("--"):
            name, _, inline = a.partition("=")
            if name in VALUE_FLAGS:
                if inline:
                    flags[name] = inline
                elif i + 1 < len(argv) and not argv[i + 1].startswith("--"):
                    flags[name] = argv[i + 1]
                    i += 1
                else:
                    return flags, pos, f"{name} needs a value"
            elif name in BARE_FLAGS:
                flags[name] = ""
            else:
                return flags, pos, f"unknown flag {name!r}; known: {' '.join(sorted(KNOWN_FLAGS))}"
        else:
            pos.append(a)
        i += 1
    return flags, pos, None


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    flags, pos, err = parse(argv)
    if err:
        print(err, file=sys.stderr)
        return 2
    if "--help" in flags or not argv:
        print(__doc__)  # the usage block already carries the resolved CLI path
        return 0 if "--help" in flags else 2

    def num(flag: str, default: int) -> int | None:
        raw = flags.get(flag)
        if raw is None:
            return default
        try:
            v = int(raw)
        except ValueError:
            print(f"{flag} takes an integer, got {raw!r}", file=sys.stderr)
            return None
        if v <= 0:
            print(f"{flag} must be positive, got {v}", file=sys.stderr)
            return None
        return v

    repo = recall_conf.repo_root()

    if "--export" in flags:
        tag = (flags.get("--tag") or "").strip().lower()
        if not tag:
            print("refused: --export needs --tag <letter>; the log is per node and so is its "
                  "aggregate.", file=sys.stderr)
            return 2
        if len(tag) != 1 or not tag.isalpha():
            print(f"--tag takes one letter from the node registry, got {tag!r}", file=sys.stderr)
            return 2
        return export(repo, tag)

    if "--used" in flags:
        return measure_answer_used(repo)

    if "--opened" in flags:
        rank = num("--opened", 0)
        if rank is None:
            return 2
        # WITHOUT --qid this attaches to the repo-wide LAST logged query: the log lives in
        # the COMMON git dir and `last_qid` carries no session or worktree predicate. The
        # fix is a KEY, not a filter -- measured over the live log, the race that actually
        # happens is INTRA-worktree (49 of 54 consecutive gaps from this checkout under
        # 60 s, concurrent agents in ONE tree), which no worktree predicate can see, while
        # the cross-worktree race a filter would close has 0 observed instances in 120
        # worktree-bearing rows (closing review F17). So the query path prints its qid and
        # the caller hands it back.
        if "--qid" in flags:
            qid = num("--qid", 0)
            if qid is None:
                return 2
            if not qid_exists(repo, qid):
                print(f"no query with qid {qid} in the log; the query path prints the qid "
                      "it logged", file=sys.stderr)
                return 2
        else:
            qid = last_qid(repo)
            if qid is None:
                print("no query to attach an --opened record to", file=sys.stderr)
                return 1
        log_event(repo, {"type": "opened", "of_qid": qid, "rank": rank})
        print(f"recorded: opened rank {rank} of query {qid}")
        return 0

    question = pos[0] if pos else ""
    if not question:
        print('no question given; usage: query.py "<question>"', file=sys.stderr)
        return 2

    k = num("--k", 20)
    budget = num("--budget", DEFAULT_BUDGET)
    if k is None or budget is None:
        return 2

    # An EMPTY --terms is not rewriting. It bypassed the refusal and logged identically to
    # --no-terms, which would have made the whole item opt-out by accident.
    terms = [t for t in (flags.get("--terms") or "").split() if t]
    has_terms = bool(terms)
    no_terms = "--no-terms" in flags
    if "--terms" in flags and not terms:
        print("--terms was given with no terms; pass real terms or --no-terms", file=sys.stderr)
        return 2
    if has_terms and no_terms:
        print("--terms and --no-terms contradict; pass one", file=sys.stderr)
        return 2
    if not has_terms and not no_terms:
        log_event(repo, {"type": "refused", "reason": "no-rewrite-terms", "query": question})
        print(REFUSAL, file=sys.stderr)
        return 2
    if has_terms and len(terms) < TERM_BAND[0]:
        # Warn, never refuse: a caller who supplied six real terms should get an answer. The band
        # describes the population the 0.84 was measured on; it is not a tuned threshold.
        print(
            f"note: {len(terms)} rewrite terms; the measured arm used "
            f"{TERM_BAND[0]}-{TERM_BAND[1]}",
            file=sys.stderr,
        )

    expr = query_expr(question, terms)
    if expr is None:
        log_event(repo, {"type": "refused", "reason": "no-searchable-term", "query": question})
        print(
            "refused: that question carries no distinctive term (every word is a stop word or "
            "shorter than three characters). Add the coined vocabulary you are looking for.",
            file=sys.stderr,
        )
        return 2

    # The index file is SHARED by every worktree of this node, so a failure to open or read it is a
    # refusal naming the file and never a delete (TOOL-dTotalRecall-21 S4): another worktree, or the
    # tag verbs, may be holding it.
    served = None
    try:
        served = load_served_set(repo, rebuild="--rebuild" in flags)
        con = served["con"]
        counts = read_served_counts(con)
        smap, sc = derive_served_supersessions(con, served["pairs"])
        hits = run_fusion(con, expr, k, smap)
    except UnbornHeadError as exc:
        print(f"refused: {exc}", file=sys.stderr)
        return 2
    except (T.TagError, sqlite3.DatabaseError) as exc:
        print(f"refused: {exc}\n  the index file is {T.derive_index_path(repo).as_posix()}; removing it "
              "costs one rebuild of the tag index and of recall's rows. Nothing was deleted.",
              file=sys.stderr)
        return 2
    finally:
        if served is not None:
            served["con"].close()
    by_id, alias_src, _ = E.load_aliases()
    aliases = {"ids": len(by_id), "joined": counts["joined"], "src": alias_src}

    if "--stats" in flags:
        print(json.dumps({"tree": served["tree"], "digest": served["digest"],
                          "counts": {"records": counts["records"], "chunks": counts["chunks"]},
                          "aliases": aliases, "superseded": sc}, indent=1))
    print(
        f"index {counts['records']} records + {counts['chunks']} chunks "
        f"· superseded {sc['ids']} ({sc['whole']} whole, {sc['partial']} partial) "
        f"(tree {served['tree'][:8]}, extracted {served['extracted']} blob(s) in {served['seconds']}s)"
    )
    # AFTER the index line and on EVERY path that can produce it -- the counts come from the served
    # rows, so this fires identically on a call that extracted and one that extracted nothing.
    # Upstream printed the line above and stopped, so a corpus whose ids the grammar does not
    # describe returned chunks, zero records, and exit 0 (spec S7).
    diag = E.zero_record_diagnosis(
        counts["records"], counts["chunks"], rebuild_hint=f"`{CLI} --rebuild`"
    )
    if diag:
        print(diag, file=sys.stderr)
    dead = dead_alias_diagnosis(aliases)
    if dead:
        print(dead, file=sys.stderr)
    print(f"{len(hits)} hits for: {question}\n{EVIDENCE_BANNER}\n")

    out, shown, spent, overflow, snippets = emit(hits, question + " " + " ".join(terms), budget)
    print(out)
    if shown > snippets:
        print(
            f"snippets for ranks 1-{snippets} · pointers for {snippets + 1}-{shown} "
            f"of {len(hits)} hits · raise --budget for more snippets"
        )
    if shown < len(hits):
        print(
            f"shown {shown} of {len(hits)} within {budget:,} B "
            f"(used {spent:,} B) — raise --budget"
        )
    if overflow:
        print(f"note: the first hit alone exceeded the budget by {overflow:,} B")
    qid = log_event(
        repo,
        {
            "type": "query",
            "query": question,
            "terms": terms,
            "rewritten": bool(terms),
            "k": k,
            "budget": budget,
            "bytes_emitted": spent,
            "worktree": str(repo),
            "head": read_worktree_head(repo),  # survives the worktree; `--used` reads it
            "n_hits": len(hits),
            "n_shown": shown,  # both tiers: a pointer line shows the path, so it maps to a rank
            "n_snippets": snippets,
            # Top RESULT_CAP only. Embedding every fused hit cost 12 987 B per record (mean 131.8
            # results) -- a month of six-node traffic in hundreds of MB. `n_hits` above keeps the
            # TRUE total, so the cap shrinks the log without clamping the count. What is lost: the
            # log can no longer answer "was the right record at rank 40". `opened` records the rank
            # the caller actually read, the byte budget truncates the emitted list anyway, and a
            # deep-rank question re-runs the fixture -- which is what the fixture is for.
            "results": [
                {"set": h["set"], "id": h["id"], "path": h["path"], "line": h["line"]}
                for h in hits[:RESULT_CAP]
            ],
            # The ordered paths the caller was actually SHOWN, one per emitted hit, duplicates and
            # order preserved -- `shown_paths.index(p) + 1` IS the rank. This exists for the opened
            # -rank INFERENCE hook (spec-20 §8 Q1 pick (c), owner 2026-07-27): the hook cannot map a
            # path to a rank the log never recorded, and RESULT_CAP=5 alone would silently cap every
            # inferred rank at 5 -- reporting "the answer is always in the top 5" by construction.
            # Paths only: strings cost a fraction of the {set,id,path,line} objects the cap removed.
            "shown_paths": [h["path"] for h in hits[:shown]],
        },
    )
    # The qid, printed WITH the hits. Without it the caller cannot name the query they
    # meant, and `--opened` can only guess at the last row in a repo-wide log.
    if qid is not None:
        print(f"\nlogged as qid {qid} — record which hit answered it:\n"
              f"  {CLI} --opened <rank> --qid {qid}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
