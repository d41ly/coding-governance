#!/usr/bin/env python3
"""id_grammar.py — the id grammar, the conf layer it binds to and check 27's index names, in one module.

PLAY-dOrderedCharter-18. These names lived in the memory-recall kit, in its conf reader, its
extractor and its benchmark, and every memory-tree module that needed the grammar reached across kits for it, so
a tree with memory-tree alone could not resolve an id. They moved here, not copied: memory-recall's
three files keep their names and re-export every name below from this module, so the recall CLI
reads exactly what it read before, and there is one grammar.

IMPORTING THIS MODULE RESOLVES NO CONF. The default grammar binds on first use, to the repo this
file lives in (`repo_root()` anchors on THIS FILE), and is cached per process; a tree with no
`.memory-tree.conf` imports every memory-tree module and refuses only when something asks for an id.
Nothing outside the standard library is imported at module level: `extract_records` reaches its
sibling `tree_lib.parse_spec_h1` on first call.

The conf parser is a copy of the twenty lines in codebase-map's map_lib.load_conf, not an import of
it: kits are copied into adopters independently. The refusal text still names memory-recall, the
kit whose CLI prints it; its wording is unchanged so every reader of it reads the same bytes.

Four OPTIONAL `RECALL_*` keys carry facts that belong to the adopter's corpus (TOOL-aRepatriatedFork-12):
`RECALL_NODE_TAG_CLASS`, `RECALL_CITED_FAMILIES`, `RECALL_BUILD_QID_CUTOFF` and `RECALL_EXPORT_DIR`;
a malformed value is a ConfError naming the key. `RECALL_EXCLUDE` and `RECALL_EXTRA_SOURCES` change
which documents exist, so both enter `digest()`.
"""

from __future__ import annotations

import fnmatch
import hashlib
import pathlib
import re
import sqlite3
import subprocess
import sys
import types

# A module's bytecode lands next to its SOURCE, inside the adopter's worktree; the recall kit's
# "a query writes nothing in your tree" property holds only while every module it imports says this.
sys.dont_write_bytecode = True

# ---------------------------------------------------------------------------- the conf layer

CONF_NAME = ".memory-tree.conf"
# The DEFAULT: a-z, per the memory-tree hygiene gate's own `node [a-z]`. `RECALL_NODE_TAG_CLASS`
# narrows it for a corpus whose registry is narrower.
NODE_TAG_CLASS = "a-z"
_TAG_CLASS_RE = re.compile(r"^[a-z0-9-]+$")
_CUTOFF_RE = re.compile(r"^([a-z]):(\d+)$")


class ConfError(RuntimeError):
    """The project layer is missing or unusable. Always a refusal, never a default."""


def repo_root() -> pathlib.Path:
    """The adopting repo's root, anchored on THIS FILE rather than on the cwd.

    WALK UP FOR THE CONF RATHER THAN ASKING GIT (TOOL-aCollapsedScan-7): `git rev-parse
    --show-toplevel` returns the current directory itself when an absolute GIT_DIR is inherited and
    no GIT_WORK_TREE names a tree, which is what git exports to a merge driver inside a LINKED
    WORKTREE. THE WALK STOPS AT THE REPOSITORY BOUNDARY: worktrees are commonly kept inside the
    primary tree, and an unbounded walk would answer with the primary tree's conf. `.git` is a
    directory in a primary tree and a FILE in a linked worktree, so one `exists()` covers both.
    """
    here = pathlib.Path(__file__).resolve()
    for parent in here.parents:
        if (parent / CONF_NAME).is_file() and (parent / ".git").exists():
            return parent
        if (parent / ".git").exists():
            break
    # No usable conf on the walk: the git answer, so `resolve()` raises ITS refusal on the next line.
    here = here.parent
    try:
        out = subprocess.run(
            ["git", "-C", str(here), "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True, encoding="utf-8",
            check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError) as e:
        raise ConfError(f"memory-recall: {here} is not inside a git repository") from e
    return pathlib.Path(out).resolve()


def load_conf(root: pathlib.Path) -> dict[str, str]:
    """Parse the restricted shell grammar `.memory-tree.conf` documents.

    Quoted values keep everything inside the quotes; an unquoted value ends at the first
    whitespace, so a trailing ` # comment` cannot leak in and diverge from bash.
    """
    path = root / CONF_NAME
    conf: dict[str, str] = {}
    if not path.is_file():
        return conf
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip().removeprefix("export ").strip()
        # TOOL-aRepatriatedFork-38 rev-3 (the closing review's C4): whitespace right after `=`
        # ends the assignment, so `K=   # note` is empty in bash, not the word `#`.
        if value[:1].isspace():
            conf[key] = ""
            continue
        value = value.strip()
        # TOOL-aRepatriatedFork-38: a quoted value ends at its MATCHING quote, whatever follows it.
        close = value.find(value[0], 1) if value[:1] in {'"', "'"} else -1
        if close >= 0:
            value = value[1:close]
        else:
            value = value.split()[0] if value.split() else ""
        conf[key] = value
    return conf


def refusal(root: pathlib.Path, why: str) -> str:
    return (
        f"refused: {why}\n\n"
        "memory-recall reads the memory-tree kit's project layer and declares no config of its\n"
        "own, so it will not create one. Adopt the memory-tree kit (adopt-memory-tree.sh), or\n"
        f"paste this into {(root / CONF_NAME).as_posix()} and fill in real values:\n\n"
        "  MEMORY_ROOT=memory\n"
        '  FAMILIES="<discipline>:<FAMILY> ..."\n\n'
        "There is no --memory-root and no --families: the conf is the single source."
    )


_FAMILY_RE = re.compile(r"^[A-Z][A-Z0-9]*$")

# The default cache budget, in MB. Blank in the conf = uncapped; absent = this.
DEFAULT_CACHE_BUDGET_MB = 512.0


def _budget(raw: str | None) -> float | None:
    """`RECALL_CACHE_BUDGET_MB` -> megabytes, or None for uncapped. Blank or unparseable is uncapped."""
    if raw is None:
        return DEFAULT_CACHE_BUDGET_MB
    raw = raw.strip()
    if not raw:
        return None
    try:
        val = float(raw)
    except ValueError:
        return None
    return val if val > 0 else None


def derive_grammar_epoch() -> str:
    """The SHA-1 of THIS FILE's bytes, CRLF folded to LF, cut to 12: the grammar's own epoch.

    `Conf.digest` folds it where it folded the recall kit's version (§8 F1 of PLAY-dOrderedCharter-18):
    the eras live here now, so the term that dates them is this file, and it moves exactly when the
    grammar's code does, with no typed constant and no recall constant read by memory-tree.
    """
    raw = pathlib.Path(__file__).read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha1(raw).hexdigest()[:12]


class Conf:
    """The RESOLVED values every grammar and recall reader reads."""

    __slots__ = ("root", "path", "memory_root", "families", "node_tag_class", "cache_budget_mb",
                 "extra_sources", "cited_families", "build_qid_cutoff", "export_dir", "exclude")

    def __init__(self, root: pathlib.Path, memory_root: str, families: tuple[str, ...],
                 cache_budget_mb: float | None = DEFAULT_CACHE_BUDGET_MB,
                 extra_sources: tuple[str, ...] = (), node_tag_class: str = NODE_TAG_CLASS,
                 cited_families: tuple[str, ...] = (),
                 build_qid_cutoff: dict[str, int] | None = None, export_dir: str | None = None,
                 exclude: tuple[str, ...] = ()):
        self.root = root
        self.path = root / CONF_NAME
        self.memory_root = memory_root
        self.families = families
        self.node_tag_class = node_tag_class
        # Ids, never homes: the grammar joins these to `ID` and recall keeps them out of `DURABLE`.
        self.cited_families = cited_families
        # Neither of these two changes which strings are ids, so neither is in digest().
        self.build_qid_cutoff = dict(build_qid_cutoff or {})
        self.export_dir = export_dir
        # None = uncapped. Not part of digest(): a size limit is not a corpus input.
        self.cache_budget_mb = cache_budget_mb
        # DECLARED extra corpus sources, repo-relative. Empty is the pre-widening corpus exactly.
        self.extra_sources = extra_sources
        # `RECALL_EXCLUDE`: repo-relative glob patterns the ONE corpus walk leaves out.
        self.exclude = exclude

    def digest(self) -> str:
        """A hash of the RESOLVED values, not of the conf file's bytes.

        The recall manifest keys freshness on this (query.ensure_cache) and the transition audit's
        cache key folds it, so an id-grammar or corpus-root edit invalidates a warm cache. Hashing
        the file's bytes instead would force a full rebuild for a comment edit.

        THE GRAMMAR'S EPOCH IS IN THE BLOB: the eras are the other half of the id grammar and live
        in this module's code, so a widening of an era reaches none of the project values. Measured
        when the session era widened: `records` went 53 documents to 91 and every already-built
        cache stayed warm and blind to the 38 new ones. `derive_grammar_epoch()` is this file's own bytes.
        """
        # `extra_sources` and `exclude` change WHICH documents exist; `cited_families` and
        # `node_tag_class` change which strings are ids.
        blob = "\0".join((self.memory_root, ",".join(sorted(self.families)), self.node_tag_class,
                          " ".join(self.extra_sources), derive_grammar_epoch(),
                          ",".join(sorted(self.cited_families)), " ".join(self.exclude)))
        return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:12]


_cached: Conf | None = None


def resolve(root: pathlib.Path | None = None) -> Conf:
    """The project layer, or a ConfError carrying the printable refusal. Cached per process for root=None."""
    global _cached
    if root is None and _cached is not None:
        return _cached
    base = root if root is not None else repo_root()
    path = base / CONF_NAME
    if not path.is_file():
        raise ConfError(refusal(base, f"no {CONF_NAME} at {path.as_posix()}"))
    conf = load_conf(base)
    memory_root = conf.get("MEMORY_ROOT", "").strip().strip("/")
    if not memory_root:
        raise ConfError(refusal(base, f"{CONF_NAME} declares no MEMORY_ROOT"))
    families = tuple(
        dict.fromkeys(
            fam
            for pair in conf.get("FAMILIES", "").split()
            if _FAMILY_RE.match(fam := pair.rpartition(":")[2].strip())
        )
    )
    if not families:
        raise ConfError(
            refusal(base, f"{CONF_NAME} declares no usable FAMILIES (want `discipline:FAMILY ...`)")
        )
    # Each malformed value is refused as `<KEY>=<value> is not <shape>`, one string shape for all four.
    refused = "refused: " + CONF_NAME + " {}={!r} is not {}"
    tag_class = conf.get("RECALL_NODE_TAG_CLASS", "").strip() or NODE_TAG_CLASS
    if not _TAG_CLASS_RE.match(tag_class):
        raise ConfError(refused.format("RECALL_NODE_TAG_CLASS", tag_class,
                                       "a character-class body over [a-z0-9-], e.g. a-f"))
    try:
        re.compile(f"[{tag_class}]")
    except re.error as e:  # a reversed range such as `f-a` passes the shape and fails here
        raise ConfError(refused.format("RECALL_NODE_TAG_CLASS", tag_class,
                                       f"a valid character class ({e})")) from e
    cited = tuple(dict.fromkeys(conf.get("RECALL_CITED_FAMILIES", "").split()))
    for fam in cited:
        if not _FAMILY_RE.match(fam):
            raise ConfError(refused.format("RECALL_CITED_FAMILIES", fam, "an uppercase family token"))
        if fam in families:
            raise ConfError(refused.format("RECALL_CITED_FAMILIES", fam,
                                           "a family FAMILIES does not already declare"))
    cutoff: dict[str, int] = {}
    for pair in conf.get("RECALL_BUILD_QID_CUTOFF", "").split():
        m = _CUTOFF_RE.match(pair)
        if not m:
            raise ConfError(refused.format("RECALL_BUILD_QID_CUTOFF", pair,
                                           "a `<tag>:<qid>` pair, e.g. a:163"))
        cutoff[m.group(1)] = int(m.group(2))
    # Only the TRAILING slash goes: a leading one is an absolute path and must reach the refusal.
    export_dir = conf.get("RECALL_EXPORT_DIR", "").strip().rstrip("/") or None
    if export_dir is not None:
        # A WRITE destination: refused here, before any caller can open a file under it.
        dest = (base / export_dir).resolve()
        if pathlib.PurePath(export_dir).is_absolute() or not dest.is_relative_to(base.resolve()):
            raise ConfError(refused.format("RECALL_EXPORT_DIR", export_dir,
                                           "a repo-relative directory inside the root"))
    out = Conf(base, memory_root, families, _budget(conf.get("RECALL_CACHE_BUDGET_MB")),
               tuple(conf.get("RECALL_EXTRA_SOURCES", "").split()), tag_class, cited, cutoff,
               export_dir, tuple(conf.get("RECALL_EXCLUDE", "").split()))
    if root is None:
        _cached = out
    return out


# ---------------------------------------------------------------------------- the id grammar


def _eras(node: str) -> tuple[str, ...]:
    """The three id eras, from ONE construction. A second copy is the catalogue-drift class.

    flat `ARCH-001` · node-scoped `ABL-d119` · session `ABL-bSiftedArchive-3`, and its `-3b`
    correction. Spelled out rather than approximated: a loose `[A-Za-z0-9]+` tail also swallows
    `ARCH-codebase` and bare session slugs, measured upstream at +348 phantom ids. The session era's
    `[a-z]*` tail is the narrowest widening that admits the ratified correction id.
    """
    return (
        r"\d{3}",  # flat            ARCH-001
        rf"[{node}]\d{{2,3}}",  # node-scoped     ABL-d119
        rf"[{node}][A-Za-z]{{2,}}-\d+[a-z]*",  # session  ABL-bSiftedArchive-3, and its -3b
    )


class Grammar(types.SimpleNamespace):
    """The id + anchor grammar bound to ONE resolved conf."""


def build_grammar(conf: Conf) -> Grammar:
    """The grammar of one resolved conf. Built by concatenation: `.format()` reads `{2,6}` as a field."""
    families = conf.families + conf.cited_families
    eras = _eras(conf.node_tag_class)
    ident = r"(?:" + "|".join(families) + r")-(?:" + "|".join(eras) + r")"
    # An anchor is a line that DEFINES a record, as opposed to one that merely cites it: a heading,
    # a bold list item, a pipe-table row's first cell and a charter-form dash row. H1 is NOT one of
    # the four: a spec's H1 would own its whole file; `extract_records` anchors a spec's defining H1
    # by PATH as well as line, through `parse_spec_h1`.
    return Grammar(
        ID=ident,
        ID_RE=re.compile(r"\b" + ident + r"\b"),
        anchors=(
            re.compile(r"^#{2,6}\s+[`*]*(" + ident + r")\b"),
            re.compile(r"^\s*[-*]\s+[`*]*(" + ident + r")\b[`*]*\s*[-—:·]"),
            re.compile(r"^\|\s*[`*]*(" + ident + r")\b[^|]*\|"),
            re.compile(r"^\s*[-*]\s+[`*]*(" + ident + r")\b[`*]*\s*[·|]"),
        ),
        families=families,
        eras=eras,
        memory_root=conf.memory_root,
    )


_default: Grammar | None = None


def grammar_for(root=None) -> Grammar:
    """The grammar bound to an EXPLICIT repo root, or with none the default one, built on first call.

    The default binds to the repo THIS FILE lives in, so no `chdir` can move it. That is right for
    the recall CLI and wrong for a caller classifying a DIFFERENT tree — the id alternation would
    come from the wrong repo and every id in the target would fail to match, silently. Measured:
    `corpus_ids.py`'s first selftest run reported a CLEAN scratch corpus while using this repo's
    family list. One accessor, no second grammar.
    """
    global _default
    if root is not None:
        return build_grammar(resolve(pathlib.Path(root)))
    if _default is None:
        _default = build_grammar(resolve())
    return _default


def anchor_at(line: str, g=None) -> str | None:
    """Return the record id this line DEFINES, or None if it merely cites one.

    `g` is a grammar bundle from `grammar_for(root)`; omitted, it is the default grammar.
    """
    if g is None:
        g = grammar_for()
    for pat in g.anchors:
        m = pat.match(line)
        if m:
            found = g.ID_RE.search(m.group(0))
            if found:
                return found.group(0)
    return None


# ---------------------------------------------------------------------------- the record readers


def git(repo: pathlib.Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", check=True
    ).stdout


_EXCLUDE_ANNOUNCED: set[str] = set()


def corpus_files(repo: pathlib.Path, rev: str | None = None,
                 include_untracked: bool = False) -> list[str]:
    """The ONE corpus walk. Markdown under ``$MEMORY_ROOT``, for both callers.

    The MEASUREMENT path stays pinnable to a ``rev``; the QUERY path also takes untracked-not-ignored
    files, because a note written this session and not yet committed is what a session needs to
    find. ``rev`` and ``include_untracked`` are mutually exclusive and passing both is REFUSED.
    """
    if rev and include_untracked:
        raise ValueError(
            "corpus_files: rev and include_untracked are mutually exclusive — a revision has no "
            "untracked files, and silently preferring one would make the corpus depend on which")
    conf = resolve()
    root = conf.memory_root + "/"
    if rev:
        names = git(repo, "ls-tree", "-r", "--name-only", rev, root).splitlines()
    else:
        names = git(repo, "ls-files", root).splitlines()
        if include_untracked:
            names += git(repo, "ls-files", "--others", "--exclude-standard", root).splitlines()
    md = {p for p in names if p.endswith(".md")}
    # `RECALL_EXCLUDE` (TOOL-aMendedFleet-27): shell-style patterns over the repo-relative path, so
    # `*` spans a slash; case-SENSITIVE on every OS. A pattern matching nothing is announced once per
    # process: a mistyped exclusion would otherwise look exactly like one with nothing to exclude.
    for pat in conf.exclude:
        hit = {p for p in md if fnmatch.fnmatchcase(p, pat)}
        if not hit and pat not in _EXCLUDE_ANNOUNCED:
            _EXCLUDE_ANNOUNCED.add(pat)
            print(f"recall: RECALL_EXCLUDE pattern matches no corpus path: {pat}", file=sys.stderr)
        md -= hit
    return sorted(md)


def corpus_inputs(repo: pathlib.Path, rev: str | None = None,
                  include_untracked: bool = False) -> tuple[list[str], list[str]]:
    """Both halves of the corpus in ONE call: markdown, and the DECLARED extra sources.

    Enumerated together so a caller cannot take one and forget the other: three call sites each had
    to be taught about declared sources, and the digest pair was taught on only one side.
    """
    return (corpus_files(repo, rev, include_untracked), resolve_declared_sources(repo, rev))


def resolve_declared_sources(repo: pathlib.Path, rev: str | None = None) -> list[str]:
    """The DECLARED extra sources, from ``RECALL_EXTRA_SOURCES``. Declared, never globbed.

    A declared file that is absent is SKIPPED and reported; a glob matching nothing says nothing,
    which is the vacuous-selector shape.
    """
    out = []
    for rel in resolve().extra_sources:
        if rev:
            try:
                git(repo, "cat-file", "-e", f"{rev}:{rel}")
            except subprocess.CalledProcessError:
                print(f"recall: declared source absent at {rev}, skipped: {rel}", file=sys.stderr)
                continue
        elif not (repo / rel).is_file():
            print(f"recall: declared source absent, skipped: {rel}", file=sys.stderr)
            continue
        out.append(rel)
    return sorted(out)


def heading_level(line: str) -> int | None:
    m = re.match(r"^(#{1,6})\s", line)
    return len(m.group(1)) if m else None


def _parse_spec_h1(path: str, text: str):
    """`tree_lib.parse_spec_h1` over the default conf: the sibling, imported on first call."""
    here = str(pathlib.Path(__file__).resolve().parent)
    if here not in sys.path:
        # APPEND, never insert(0, ...): a kit dir ahead of the stdlib could shadow a stdlib module.
        sys.path.append(here)
    from tree_lib import parse_spec_h1  # noqa: PLC0415 — the sibling, deliberately not at import

    conf = resolve()
    return parse_spec_h1(path, text, conf.memory_root, conf.families)


def extract_records(path: str, text: str) -> list[dict]:
    """One document per anchored record.

    A heading anchor owns its section, down to the next heading of the same or higher level. A row
    anchor (list entry or table row) owns its own line plus indented continuations. A spec's
    DEFINING H1 -- `parse_spec_h1` -- anchors too, and owns what a row anchor owns: its own line and
    the non-blank lines under it, which is the spec's title (TOOL-aRepatriatedFork-40).
    """
    lines = text.splitlines()
    h1 = _parse_spec_h1(path, text)
    h1_at = None
    if h1:
        # The predicate numbers `split("\n")` lines and this loop walks `splitlines()`, which also
        # breaks on form feeds and U+2028; re-find the line by content when the two disagree.
        want = text.split("\n")[h1[0] - 1].rstrip("\r")
        h1_at = h1[0] - 1
        if h1_at >= len(lines) or lines[h1_at] != want:
            h1_at = next((k for k, ln in enumerate(lines) if ln == want), None)
    docs, i = [], 0
    while i < len(lines):
        rid = anchor_at(lines[i])
        lvl = heading_level(lines[i])
        if not rid and i == h1_at:
            # A ROW, not a section: the H1 line and the non-blank lines under it, i.e. the title.
            rid, lvl = h1[1], None
        if not rid:
            i += 1
            continue
        start, j = i, i + 1
        if lvl is not None:
            while j < len(lines):
                nl = heading_level(lines[j])
                if nl is not None and nl <= lvl:
                    break
                j += 1
        else:
            while j < len(lines) and lines[j].strip() and not anchor_at(lines[j]):
                j += 1
        body = "\n".join(lines[start:j]).strip()
        if body:
            docs.append({"id": rid, "path": path, "line": start + 1, "text": body})
        i = max(j, i + 1)
    return docs


# --- supersession (TOOL-aGraftedHelix-4) ----------------------------------------------------------
# Three spellings. P1 and P2 read a record's TEXT; P3 reads a spec's STATUS LINE. An edge is PARTIAL
# when the id is followed at once by a possessive or by `for` -- "SUPERSEDES <id>'s PREMISE" retires
# a clause, not a record.
_SUP_W = r"[`*\[]*"  # optional wrapping before an id
SUPERSEDE_PARTIAL = re.compile(r"^[`*\]]*(?:['’]s\b|\s+for\b)", re.I)


def build_supersede_patterns(g=None) -> tuple:
    """`(P1, P2, P3)` over grammar `g`, the default grammar when omitted; cached on the grammar."""
    if g is None:
        g = grammar_for()
    pats = getattr(g, "supersede", None)
    if pats is None:
        ident = g.ID
        pats = g.supersede = (
            re.compile(r"\bsupersed(?:e|es|ing)\s+" + _SUP_W + "(" + ident + r")\b", re.I),
            re.compile(r"\bsuperseded\s+by\s+" + _SUP_W + "(" + ident + r")\b", re.I),
            re.compile(r"\bsuperseded[ -]by\s+((?:" + _SUP_W + ident + r"\b[`*\]]*[\s,]*)+)", re.I),
        )
    return pats


def extract_supersessions(path: str, text: str, records: list[dict]) -> list[tuple[str, str, str, str]]:
    """Candidate edges ``(old, new, kind, pattern)`` from one file; ``kind`` is whole or partial.

    ``records`` is what ``extract_records`` returned for this file. P1 (``supersedes <id>``) makes
    the cited id old and the record new; P2 (``superseded by <id>``) the reverse; P3 is a
    ``superseded by``/``superseded-by`` list on the ``**Status:** `` line in a spec's first five
    lines, old being the id its H1 defines. A self-edge is skipped. Nothing here checks that an id
    exists: ``derive_supersession_map`` does, over the whole walk.
    """
    p1, p2, p3 = build_supersede_patterns()
    edges: list[tuple[str, str, str, str]] = []

    def add(old: str, new: str, after: str, pattern: str) -> None:
        if old != new:
            kind = "partial" if SUPERSEDE_PARTIAL.match(after) else "whole"
            edges.append((old, new, kind, pattern))

    for r in records:
        t = r["text"]
        for m in p1.finditer(t):
            add(m.group(1), r["id"], t[m.end(1):], "P1")
        for m in p2.finditer(t):
            add(r["id"], m.group(1), t[m.end(1):], "P2")
    h1 = _parse_spec_h1(path, text)
    if h1:
        id_re = grammar_for().ID_RE
        for line in text.split("\n")[:5]:
            if not line.startswith("**Status:** "):
                continue
            for m in p3.finditer(line):
                for i in id_re.finditer(m.group(1)):
                    add(h1[1], i.group(0), line[m.start(1) + i.end():], "P3")
    return edges


def derive_supersession_map(edges, defined) -> tuple[dict, dict]:
    """``({old: [[new, kind], …]}, counts)`` over the edges whose two ends ``defined`` holds.

    An edge naming an id no record anchors is dropped and its id counted UNRESOLVED -- never kept,
    never minted. ``counts`` carries the map size, how many ids hold a whole edge and how many only
    partial ones, the kept edges per pattern and kind, and the unresolved ids.
    """
    smap: dict[str, set] = {}
    per = {p: {"whole": 0, "partial": 0} for p in ("P1", "P2", "P3")}
    unresolved: set[str] = set()
    for old, new, kind, pattern in edges:
        missing = {i for i in (old, new) if i not in defined}
        if missing:
            unresolved |= missing
            continue
        if (new, kind) not in smap.setdefault(old, set()):
            smap[old].add((new, kind))
            per[pattern][kind] += 1
    out = {old: [list(e) for e in sorted(smap[old])] for old in sorted(smap)}
    whole = sum(1 for v in out.values() if any(k == "whole" for _, k in v))
    return out, {"ids": len(out), "whole": whole, "partial": len(out) - whole,
                 "patterns": per, "unresolved": sorted(unresolved)}


# ---------------------------------------------------------------------------- check 27's index names

STOP = set(
    """a an and are as at be but by for from has have how in into is it its of on or that the
    this to was were what when where which who why will with does do did can could should would
    my our your their there here if then than so not no yes get got make made use used using i
    you we they he she them us me about after before between during over under again more most
    some any all each other same such only own too very just now new old also been being had"""
    .split()
)

TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9_]{1,}")


def terms(text: str) -> list[str]:
    return [t.lower() for t in TOKEN.findall(text) if t.lower() not in STOP and len(t) > 2]


# Swept on the 99-query hard slice with 262 records aliased. 1.0 costs r@10 a point against the
# un-aliased baseline; 0.25-0.5 recovers it and lifts r@20 to 0.74 against 0.71. Weights >=4 are
# actively harmful (16.0 drops r@10 to 0.55). The alias text is a bridge, not evidence -- it should
# break ties, not win them.
ALIAS_WEIGHT = 0.4


def build_index(
    docs: list[dict], crumb: bool = False, db_path: str = ":memory:"
) -> sqlite3.Connection:
    """FTS5 index over three columns: ``head``, ``body`` and ``alias``.

    ``crumb=True`` folds each chunk's heading ancestry into the searchable head. ``alias`` is its OWN
    column rather than text concatenated onto the body, because BM25 divides by document length:
    appending alias text to a record cost it roughly a third of the weight of its own terms.
    ``db_path`` defaults to ``":memory:"``; ``query.py`` passes a file so the CLI's cache is built by
    the SAME builder the measurement uses.
    """
    db = sqlite3.connect(db_path)
    db.execute("CREATE VIRTUAL TABLE d USING fts5(head, body, alias, tokenize='unicode61')")
    db.executemany(
        "INSERT INTO d(rowid, head, body, alias) VALUES (?,?,?,?)",
        [
            (
                i,
                " ".join(
                    x
                    for x in (
                        r.get("id", ""),
                        r["path"],
                        r["text"].split("\n", 1)[0],
                        r.get("crumb", "") if crumb else "",
                    )
                    if x
                ),
                r["text"],
                r.get("alias", ""),
            )
            for i, r in enumerate(docs)
        ],
    )
    return db


def match_expr(query: str) -> str:
    ts = terms(query)
    if not ts:
        return '"the"'
    # OR the terms. FTS5's query language treats most punctuation as syntax, so every term is
    # double-quoted -- an unquoted `use client` or `c++` is a syntax error, not a miss.
    return " OR ".join('"' + t.replace('"', "") + '"' for t in dict.fromkeys(ts))
