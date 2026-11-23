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
Nothing outside the standard library is imported at module level: every reach for the sibling
`tree_lib` goes through `load_sibling` on first call.

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
import importlib
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

    __slots__ = ("root", "path", "memory_root", "families", "node_tag_class",
                 "extra_sources", "cited_families", "build_qid_cutoff", "export_dir", "exclude")

    def __init__(self, root: pathlib.Path, memory_root: str, families: tuple[str, ...],
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
        # DECLARED extra corpus sources, repo-relative. Empty is the pre-widening corpus exactly.
        self.extra_sources = extra_sources
        # `RECALL_EXCLUDE`: repo-relative glob patterns the ONE corpus walk leaves out.
        self.exclude = exclude

    def digest(self) -> str:
        """A hash of the RESOLVED values, not of the conf file's bytes.

        Recall's row digest folds this (query.derive_recall_digest) and the transition audit's
        cache key folds it, so an id-grammar or corpus-root edit re-extracts every served pair. Hashing
        the file's bytes instead would force a full re-extraction for a comment edit.

        THE GRAMMAR'S EPOCH IS IN THE BLOB: the eras are the other half of the id grammar and live
        in this module's code, so a widening of an era reaches none of the project values. Measured
        when the session era widened: `records` went 53 documents to 91 and every already-built
        cache stayed warm and blind to the 38 new ones. `derive_grammar_epoch()` is this file's own bytes.
        The slug class is folded beside it (TOOL-dTotalRecall-5 S4): a README recording a new slug
        grammar widens the session era with no byte of this file moving.
        """
        # `extra_sources` and `exclude` change WHICH documents exist; `cited_families`,
        # `node_tag_class` and the slug class change which strings are ids.
        blob = "\0".join((self.memory_root, ",".join(sorted(self.families)), self.node_tag_class,
                          " ".join(self.extra_sources), derive_grammar_epoch(),
                          ",".join(sorted(self.cited_families)), " ".join(self.exclude),
                          derive_slug_grammar(self.root).slug_class))
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
    out = Conf(base, memory_root, families,
               tuple(conf.get("RECALL_EXTRA_SOURCES", "").split()), tag_class, cited, cutoff,
               export_dir, tuple(conf.get("RECALL_EXCLUDE", "").split()))
    if root is None:
        _cached = out
    return out


# ---------------------------------------------------------------------------- the slug grammar
#
# TOOL-dTotalRecall-5. One slug grammar, declared by the policy keys `builds.slug-words`,
# `builds.slug-style` and `builds.slug-date` and derived here once, is what every slug and id reader
# reads. A grammar's shape is `<node-letter><date><word>{lo,hi}`: a word is a capital and at least one
# lower-case letter, the date is empty unless `in-slug`, then eight digits or a hyphenated date after
# the node letter. `style` is the minting source and never a shape. A changed grammar binds new mints
# only: `mint_re` is the grammar in force, and `slug_class` the alternation of the frozen legacy shape,
# the grammar in force and every grammar a tracked build README records in `slug-grammar:`, so no
# reader refuses a slug minted under any of them. `slug_class` is spliced by Python readers and
# `slug_ere`, the same construction with capturing group openers, by shell, awk and JavaScript ones:
# ERE has no `(?:` (gawk and bash `=~` refuse it, §8 F7).

# The catalogue's three defaults, for a tree with no policy kit or a refused read. The build-index
# self-test holds them to the catalogue rows wherever the policy kit resolves.
SLUG_DEFAULTS = {"builds.slug-words": "1-3", "builds.slug-style": "humorous", "builds.slug-date": "none"}
_SLUG_STYLES = ("humorous", "descriptive")
_SLUG_DATES = ("none", "shown", "in-slug")
_SLUG_RECORD_RE = re.compile(r"^words=([0-9]+)-([0-9]+) style=(\S+) date=(\S+)$")
_SLUG_DATE_SHAPE = "[0-9]{8}|[0-9]{4}-[0-9]{2}-[0-9]{2}"

# The legacy shape, `[<node>][A-Za-z]{2,}`, a `%` template over the node class: frozen, and the
# answer of a kit that cannot reach this module, which carries this block inline.
# >>> slug_legacy_py — canonical copy: id_grammar.py in the memory-tree kit (byte-identical; gated)
SLUG_LEGACY = "[%s][A-Za-z]{2,}"
# <<< slug_legacy_py


class SlugGrammar(types.SimpleNamespace):
    """The slug grammar of one tree: `words` (lo, hi), `style`, `date`, `node`, `slug_class`,
    `slug_ere`, `BUILD_SLUG_RE`, `mint_re`, `record` and `fallback`, the reason the defaults apply or
    empty when the three keys read."""

    def render_label(self, slug: str, opened: str | None) -> str:
        """`<slug> (<opened>)` under `shown`, the bare slug otherwise: a date beside a slug, never in an id."""
        return f"{slug} ({opened})" if self.date == "shown" and opened else slug


def parse_slug_grammar(value: str, where: str | None = None) -> tuple[tuple[int, int], str, str]:
    """`words=<lo>-<hi> style=<style> date=<date>` -> ((lo, hi), style, date), the record's one reader.

    A value outside the grammar, `lo` below 1 or above `hi` among it, is a ConfError naming the README
    `where` that carried it, or with none the policy key, never a default."""
    m = _SLUG_RECORD_RE.match(str(value).strip())
    if not m:
        raise ConfError(f"refused: {where or 'the builds.slug-* keys'} {value!r} is not "
                        "`words=<lo>-<hi> style=<style> date=<date>`")
    lo, hi, style, date = int(m.group(1)), int(m.group(2)), m.group(3), m.group(4)
    if not 1 <= lo <= hi:
        raise ConfError(f"refused: {where or 'builds.slug-words'} words={lo}-{hi} is not a range "
                        "with 1 <= lo <= hi")
    if style not in _SLUG_STYLES:
        raise ConfError(f"refused: {where or 'builds.slug-style'} style={style} is not one of "
                        f"{', '.join(_SLUG_STYLES)}")
    if date not in _SLUG_DATES:
        raise ConfError(f"refused: {where or 'builds.slug-date'} date={date} is not one of "
                        f"{', '.join(_SLUG_DATES)}")
    return (lo, hi), style, date


def render_slug_shape(g, opener: str) -> str:
    """One grammar's shape. `opener` is the group opener: `(?:` renders the Python spelling, `(` the
    POSIX ERE one; the two differ in nothing else. `g` carries `node`, `words` and `date`."""
    date = opener + _SLUG_DATE_SHAPE + ")" if g.date == "in-slug" else ""
    return "[" + g.node + "]" + date + opener + "[A-Z][a-z]+){%d,%d}" % g.words


def render_slug_record(words: tuple[int, int], style: str, date: str) -> str:
    return "words=%d-%d style=%s date=%s" % (words[0], words[1], style, date)


def load_sibling(name: str):
    """The memory-tree module `name` beside this file, imported on first call, never at this module's
    import (TOOL-dTotalRecall-54 S5). The one path guard every sibling reach in this module goes through."""
    here = str(pathlib.Path(__file__).resolve().parent)
    if here not in sys.path:
        sys.path.append(here)  # APPEND, never insert(0, ...): a kit dir ahead of the stdlib could shadow a stdlib module.
    return importlib.import_module(name)


def read_slug_policy(root: pathlib.Path) -> tuple[str, str]:
    """-> (the record of the three keys, the fallback line). The first refused read ends the reads and
    `SLUG_DEFAULTS` applies to all three, as checks 6 and 7 treat their read: a LookupError is no
    policy kit, a ValueError the reader refusing, no landed revision among its causes."""
    tree_lib = load_sibling("tree_lib")

    vals = dict(SLUG_DEFAULTS)
    key = "builds.slug-words"
    try:
        vals[key] = tree_lib.read_policy_value("builds.slug-words", root)
        key = "builds.slug-style"
        vals[key] = tree_lib.read_policy_value("builds.slug-style", root)
        key = "builds.slug-date"
        vals[key] = tree_lib.read_policy_value("builds.slug-date", root)
    except LookupError:
        vals = dict(SLUG_DEFAULTS)
        why = "slug grammar: no policy kit, the defaults apply"
    except ValueError as exc:
        vals = dict(SLUG_DEFAULTS)
        said = str(exc).partition(" did not read: ")[2] or str(exc)
        why = f"slug grammar: the policy reader refused {key}, the defaults apply: {said}"
    else:
        why = ""
    record = "words=%s style=%s date=%s" % (vals["builds.slug-words"], vals["builds.slug-style"],
                                            vals["builds.slug-date"])
    return record, why


def read_recorded_grammars(root: pathlib.Path, memory_root: str) -> list[tuple[str, str]]:
    """[(record, README path)], each tracked `<memory_root>/builds/<slug>/README.md` recording one in
    its front matter's `slug-grammar:`, in path order. A README recording none is legacy."""
    try:
        out = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--", f"{memory_root}/builds"],
                             capture_output=True, check=True).stdout.decode("utf-8", "replace")
    except (OSError, subprocess.CalledProcessError):
        return []
    tree_lib = load_sibling("tree_lib")

    found = []
    for rel in sorted(p for p in out.split("\0") if p):
        parts = rel.split("/")
        if parts[-1] != "README.md" or len(parts) != len(memory_root.split("/")) + 3:
            continue
        try:
            fm = tree_lib.FM_RE.match(tree_lib.read_text(str(root / rel)))
        except (OSError, UnicodeDecodeError):
            continue
        for line in (fm.group(1).splitlines() if fm else ()):
            if line.startswith("slug-grammar:"):
                found.append((line.partition(":")[2].strip(), rel))
    return found


def read_slug_node(root: pathlib.Path) -> tuple[str, str]:
    """-> (the node-tag class, the memory root) of `root`'s conf, as `resolve` validates the class."""
    conf = load_conf(root)
    node = conf.get("RECALL_NODE_TAG_CLASS", "").strip() or NODE_TAG_CLASS
    if not _TAG_CLASS_RE.match(node):
        raise ConfError(f"refused: {CONF_NAME} RECALL_NODE_TAG_CLASS={node!r} is not a character-class "
                        "body over [a-z0-9-], e.g. a-f")
    return node, conf.get("MEMORY_ROOT", "").strip().strip("/") or "memory"


_slug_cache: dict[str, SlugGrammar] = {}


def derive_slug_grammar(root=None) -> SlugGrammar:
    """The slug grammar of `root`, or with none the repo this file lives in, cached per process and root."""
    base = pathlib.Path(root) if root is not None else repo_root()
    key = str(base.resolve())
    if key in _slug_cache:
        return _slug_cache[key]
    node, memory_root = read_slug_node(base)
    record, fallback = read_slug_policy(base)
    words, style, date = parse_slug_grammar(record)
    g = SlugGrammar(words=words, style=style, date=date, node=node, fallback=fallback,
                    record=render_slug_record(words, style, date))
    recorded = []
    for value, rel in read_recorded_grammars(base, memory_root):
        rw, rs, rd = parse_slug_grammar(value, rel)
        recorded.append(types.SimpleNamespace(words=rw, style=rs, date=rd, node=node,
                                              record=render_slug_record(rw, rs, rd)))
    g.recorded = list(dict.fromkeys(r.record for r in recorded))
    legacy = SLUG_LEGACY % node
    g.slug_class = "|".join(dict.fromkeys([legacy, render_slug_shape(g, "(?:"),
                                           *(render_slug_shape(r, "(?:") for r in recorded)]))
    g.slug_ere = "|".join(dict.fromkeys([legacy, render_slug_shape(g, "("),
                                         *(render_slug_shape(r, "(") for r in recorded)]))
    g.BUILD_SLUG_RE = re.compile(r"^(?:" + g.slug_class + r")$")
    g.mint_re = re.compile(r"^" + render_slug_shape(g, "(?:") + r"$")
    _slug_cache[key] = g
    return g


class SlugPattern:
    """A compiled pattern bound from the slug grammar at FIRST USE, never at import: importing a reader
    resolves no conf and runs no policy read. `build` takes the grammar and returns the pattern text;
    every attribute of the compiled pattern (`match`, `fullmatch`, `pattern`, ...) reads through."""

    def __init__(self, build, flags: int = 0, root=None):
        self._build, self._flags, self._root, self._re = build, flags, root, None

    def __getattr__(self, name):
        if self._re is None:
            self._re = re.compile(self._build(derive_slug_grammar(self._root)), self._flags)
        return getattr(self._re, name)


# ---------------------------------------------------------------------------- the id grammar


def _eras(node: str, slug_class: str) -> tuple[str, ...]:
    """The three id eras, from ONE construction. A second copy is the catalogue-drift class.

    flat `ARCH-001` · node-scoped `ABL-d119` · session `ABL-bSiftedArchive-3`, and its `-3b`
    correction. Spelled out rather than approximated: a loose `[A-Za-z0-9]+` tail also swallows
    `ARCH-codebase` and bare session slugs, measured upstream at +348 phantom ids. The session era's
    `[a-z]*` tail is the narrowest widening that admits the ratified correction id.

    The session era's slug is `slug_class`, the slug grammar's (TOOL-dTotalRecall-5 S4), so an id
    whose slug carries an `in-slug` date parses; the legacy shape is the first arm of that class.
    """
    session = r"(?:" + slug_class + r")"
    return (
        r"\d{3}",  # flat            ARCH-001
        rf"[{node}]\d{{2,3}}",  # node-scoped     ABL-d119
        session + r"-\d+[a-z]*",  # session  ABL-bSiftedArchive-3, and its -3b
    )


class Grammar(types.SimpleNamespace):
    """The id + anchor grammar bound to ONE resolved conf."""


def build_grammar(conf: Conf) -> Grammar:
    """The grammar of one resolved conf. Built by concatenation: `.format()` reads `{2,6}` as a field."""
    families = conf.families + conf.cited_families
    eras = _eras(conf.node_tag_class, derive_slug_grammar(conf.root).slug_class)
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


# The session era's correction tail, `[a-z]*` after the final digits (`_eras`): `-9b` parses as `-9`.
SUFFIX_RE = re.compile(r"(?<=\d)[a-z]+$")


def parse_id_parts(ident: str, root, *, alt: str | None = None) -> tuple:
    """-> (family, slug, seq) of one session-era id, `seq` an int (TOOL-dTotalRecall-54 S1 to S3).

    Matched whole by `tree_lib.build_id_token_re(alt, root)`, the one named-group id token, never
    by the grammar's own id regex, whose groups are unnamed. `alt` is the family alternation, by default `grammar_for(root).families`, the declared
    and cited families together; the slug class always comes from `root`, None the tree this file
    lives in. One trailing correction suffix is stripped first. A flat or node-scoped id, an
    undeclared family, a malformed id and a pinned `@rev-N` id raise ValueError naming it."""
    if alt is None:
        alt = "|".join(grammar_for(root).families)
    token_re = load_sibling("tree_lib").build_id_token_re(alt, root)
    m = token_re.fullmatch(SUFFIX_RE.sub("", ident))
    if m is None or m.group("rev") is not None:
        raise ValueError(f"not an id under this tree's grammar: {ident}")
    return m.group("fam"), m.group("slug"), int(m.group("seq"))


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
    tree_lib = load_sibling("tree_lib")

    conf = resolve()
    return tree_lib.parse_spec_h1(path, text, conf.memory_root, conf.families)


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


_FTS_TABLE_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def build_fts_rows(
    db: sqlite3.Connection, table: str, docs: list[dict], *, path: str = "", blob: str = "",
    digest: str = "", crumb: bool = False,
) -> sqlite3.Connection:
    """Write ``docs`` into the FTS5 table ``table`` on ``db``, creating it when absent; returns ``db``.

    Three indexed columns, ``head``, ``body`` and ``alias``, then ``path``, ``blob``, ``digest``,
    ``id`` and ``line`` UNINDEXED, so a row carries the (path, blob) pair and the extraction digest it
    was written under (TOOL-dTotalRecall-21 S1): memory-recall's rows in the shared tag index are
    joined to a worktree's served pairs by them, and a benchmark caller hands a
    ``sqlite3.connect(":memory:")`` and the table ``d``. ``path`` defaults to each doc's own.

    Rowids continue from the table's highest, so a fresh table numbers ``docs`` from 0 in order --
    the index every benchmark substrate reads a hit back by.

    ``crumb=True`` folds each chunk's heading ancestry into the searchable head. ``alias`` is its OWN
    column rather than text concatenated onto the body, because BM25 divides by document length:
    appending alias text to a record cost it roughly a third of the weight of its own terms.
    """
    if not _FTS_TABLE_RE.match(table):
        raise ValueError(f"build_fts_rows: {table!r} is not a table name")
    db.execute(f"CREATE VIRTUAL TABLE IF NOT EXISTS {table} USING fts5(head, body, alias, "
               "path UNINDEXED, blob UNINDEXED, digest UNINDEXED, id UNINDEXED, line UNINDEXED, "
               "tokenize='unicode61')")
    if not docs:
        return db
    top = db.execute(f"SELECT rowid FROM {table} ORDER BY rowid DESC LIMIT 1").fetchone()
    base = top[0] + 1 if top else 0
    db.executemany(
        f"INSERT INTO {table}(rowid, head, body, alias, path, blob, digest, id, line) "
        "VALUES (?,?,?,?,?,?,?,?,?)",
        [
            (
                base + i,
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
                path or r["path"],
                blob,
                digest,
                r.get("id") or r.get("rec") or "",
                r.get("line", 0),
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


# ---------------------------------------------------------------------------- the slug grammar's CLI

# The reader search (TOOL-dTotalRecall-5 §4 "The readers"): a slug class followed by a hyphen and a
# digit class, at most a group's closing and opening parenthesis between them, its repeat a `*`, a `+`
# or a brace interval, single or an f-string's doubled; or a name holding `slug` bound to a regex literal.
_READER_ID_SHAPE = re.compile(r"\[[^\]\n]*a-z[^\]\n]*\](?:[*+]|\{\{?[0-9]*,?[0-9]*\}\}?)?\)?-\(?(?:\?:|\?P<\w+>)?"
                              r"(?:\\d|\[0-9\]|\[1-9\])")
_READER_SLUG_SHAPE = re.compile(r"\w*(?:SLUG|[Ss]lug)\w*\s*=\s*(?:re\.compile\(\s*)?\(?\s*"
                                r"(?:[rRbBfF]{0,2}(['\"])[^'\"\n]*\[|/[^/\n]*\[)")
_READER_BLOCK = re.compile(r"^(?:# |// )(>>>|<<<) slug_legacy_")
# The split shapes (TOOL-dTotalRecall-38 S2, keyed on the shape by TOOL-dTotalRecall-44): Python's
# `.split("-")` with no maxsplit, blanks inside its parentheses allowed, unless it is indexed `[0]` at
# once, since the family before the first hyphen is the one segment a hyphen in a slug cannot move; a
# shell `${name%-*}`, `${name%%-*}`, `${name#*-}` or `${name##*-}`, `cut -d-`, `cut -d '-'`,
# `cut -d "-"` or `IFS=-`. No value's NAME is read, so a reader of an id named `i` or `a` is listed;
# `.rsplit("-", 1)`, which reads the sequence after the last hyphen, and `.partition` are outside it.
_READER_SPLIT_SHAPE = re.compile(
    r"\.split\(\s*([\"'])-\1\s*\)(?!\[0\])"
    r"|\bcut\s+-d\s*(?:-|'-'|\"-\")(?=\s|$)|\bIFS=-(?=\s|;|$)"
    r"|\$\{[A-Za-z_]+(?:%%?-\*|##?\*-)\}")


def scan_readers(root) -> list[str]:
    """`path:line:text` for every line of a tracked `*.py`, `*.sh` or `*.js` file under `tools/` and
    `skills/`, and of every tracked file under `.githooks/`, that spells a slug or id shape or splits
    a value on a hyphen in a shape that reads past the family (`_READER_SPLIT_SHAPE`), outside the
    grammar's own entry points: this module and every `slug_legacy_*` block."""
    root = pathlib.Path(root)
    tool_root = pathlib.Path(__file__).resolve().parent.parent
    try:  # the tool root as this tree places it, so an adopter's install prefix is the one scanned
        tool_rel = tool_root.relative_to(repo_root().resolve()).as_posix()
    except (ValueError, ConfError):
        tool_rel = tool_root.name
    out = subprocess.run(["git", "-C", str(root), "ls-files", "-z", "--", tool_rel, "skills", ".githooks"],
                         capture_output=True, check=True).stdout.decode("utf-8", "replace")
    own = pathlib.Path(__file__).resolve()
    try:  # this module's own path in ITS tree, so a scanned clone's copy of it is excluded too
        own_rel = own.relative_to(repo_root().resolve()).as_posix()
    except (ValueError, ConfError):
        own_rel = None
    hits = []
    for rel in sorted(p for p in out.split("\0") if p):
        if not (rel.startswith(".githooks/") or rel.endswith((".py", ".sh", ".js"))):
            continue
        path = root / rel
        if not path.is_file() or path.resolve() == own or rel == own_rel:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeDecodeError):
            continue
        inside = False
        for n, line in enumerate(lines, 1):
            mark = _READER_BLOCK.match(line)
            if mark:
                inside = mark.group(1) == ">>>"
                continue
            if not inside and (_READER_ID_SHAPE.search(line) or _READER_SLUG_SHAPE.search(line)
                               or _READER_SPLIT_SHAPE.search(line)):
                hits.append(f"{rel}:{n}:{line}")
    return hits


# The six flips of §4 "The flips": (name, key, value, the new slug planted).
_FLIPS = (
    ("slug-words 1", "builds.slug-words", "1-1", "dLoop"),
    ("slug-words 3", "builds.slug-words", "3-3", "dClosedLoopTwo"),
    ("slug-style descriptive", "builds.slug-style", "descriptive", "dClosedLoop"),
    ("slug-date shown", "builds.slug-date", "shown", "dClosedLoop"),
    ("slug-date in-slug digit", "builds.slug-date", "in-slug", "d20261026ClosedLoop"),
    ("slug-date in-slug hyphenated", "builds.slug-date", "in-slug", "d2026-10-26ClosedLoop"),
)


def run_flip_probe(clone) -> int:
    """Each flip of `_FLIPS`, committed to `main` of the scratch clone `clone`, whose remote is removed
    so the policy reader's landed revision is that `main`: the new slug passes `mint_re`; a legacy
    two-word slug the flip does not admit fails it and passes `BUILD_SLUG_RE`, or the shape is stated
    unchanged; every tracked folder passes `BUILD_SLUG_RE`; `ID_RE` matches `TOOL-<slug>-3` whole;
    `parse_id_parts` returns the new slug and 3 for it; and the clone's census lists no split hit, by
    path and line text, that the census over this probe's own tree does not (TOOL-dTotalRecall-38 S4).
    One `flip <name>: ok` line or the failed checks each; 1 on any failure, 2 on an unusable clone."""
    global _default, _cached
    clone = pathlib.Path(clone).resolve()
    # The copy `tree_lib` imports, whose slug cache the parser's token regex reads: a second module
    # when this one runs as `__main__`, so both caches are cleared at each flip.
    twin = load_sibling("id_grammar")

    def run(*args: str) -> str:
        return subprocess.run(["git", "-C", str(clone), "-c", "user.name=flip-probe",
                               "-c", "user.email=flip-probe@invalid", "-c", "core.autocrlf=false", *args],
                              capture_output=True, text=True, encoding="utf-8", check=True).stdout

    try:
        if run("remote").strip():
            print(f"flip-probe: refused: {clone.as_posix()} has a remote, so its landed revision is not "
                  "its main; remove it in the scratch clone", file=sys.stderr)
            return 2
        if clone == repo_root().resolve():
            print("flip-probe: refused: the clone is this tree; make a scratch clone", file=sys.stderr)
            return 2
        run("checkout", "-q", "main")
        start = run("rev-parse", "HEAD").strip()
    except (OSError, subprocess.CalledProcessError) as exc:
        print(f"flip-probe: refused: {clone.as_posix()} is no git clone with a main: {exc}", file=sys.stderr)
        return 2
    policy = clone / ".governance" / "policy.toml"
    node, memory_root = read_slug_node(clone)
    depth = len(memory_root.split("/"))
    _slug_cache.clear()
    twin._slug_cache.clear()
    base_mint = derive_slug_grammar(clone).mint_re.pattern
    own_splits = {tuple(h.split(":", 2)[::2]) for h in scan_readers(repo_root())
                  if _READER_SPLIT_SHAPE.search(h.split(":", 2)[2])}
    failed = 0
    try:
        for name, key, value, slug in _FLIPS:
            run("reset", "-q", "--hard", start)
            vals = dict(SLUG_DEFAULTS, **{key: value})
            record = "words=%s style=%s date=%s" % (vals["builds.slug-words"], vals["builds.slug-style"],
                                                    vals["builds.slug-date"])
            text = policy.read_text(encoding="utf-8") if policy.is_file() else ""
            policy.parent.mkdir(parents=True, exist_ok=True)
            policy.write_text(text.rstrip("\n") + f'\n\n[builds]\n{key.partition(".")[2]} = "{value}"\n',
                              encoding="utf-8", newline="\n")
            readme = clone / memory_root / "builds" / slug / "README.md"
            readme.parent.mkdir(parents=True, exist_ok=True)
            readme.write_text(f"---\nslug: {slug}\nslug-grammar: {record}\nopened: 2026-10-26\n---\n\n"
                              f"# {slug}\n", encoding="utf-8", newline="\n")
            run("add", "--", policy.relative_to(clone).as_posix(), readme.relative_to(clone).as_posix())
            run("commit", "-q", "--no-verify", "-m", f"flip-probe: {name}")
            _slug_cache.clear()
            twin._slug_cache.clear()
            _default = _cached = None
            g = derive_slug_grammar(clone)
            why = []
            same = g.mint_re.pattern == base_mint
            if g.record != record:
                why.append(f"the grammar in force reads {g.record}, not {record} ({g.fallback or 'no fallback'})")
            if not g.mint_re.match(slug):
                why.append(f"mint_re refuses the new slug {slug}")
            if same and key == "builds.slug-words" or same and value == "in-slug":
                why.append("the shape did not change")
            elif not same and (g.mint_re.match("dTotalRecall") or not g.BUILD_SLUG_RE.match("dTotalRecall")):
                why.append("the legacy two-word slug dTotalRecall does not fail mint_re and pass BUILD_SLUG_RE")
            folders = sorted({p.split("/")[depth + 1] for p in run("ls-files", "--", f"{memory_root}/builds").splitlines()
                              if len(p.split("/")) > depth + 2})
            bad = [f for f in folders if not g.BUILD_SLUG_RE.match(f)]
            if bad or not folders:
                why.append(f"BUILD_SLUG_RE refuses the tracked folder(s) {' '.join(bad[:5]) or '(none tracked)'}")
            ident = f"TOOL-{slug}-3"
            m = grammar_for(clone).ID_RE.search(f"see {ident} here")
            if not m or m.group(0) != ident or not m.group(0).endswith("-3"):
                why.append(f"ID_RE does not match {ident} whole: {m.group(0) if m else 'no match'}")
            try:
                parts = parse_id_parts(ident, clone)
            except ValueError as exc:
                parts = str(exc)
            if parts != ("TOOL", slug, 3):
                why.append(f"parse_id_parts does not return {slug} and 3 for {ident}: {parts}")
            stray = [h for h in scan_readers(clone) if _READER_SPLIT_SHAPE.search(h.split(":", 2)[2])
                     and tuple(h.split(":", 2)[::2]) not in own_splits]
            if stray:
                why.append("the clone's census lists split hit(s) this tree's does not: " + " | ".join(stray[:5]))
            if value == "shown" and g.render_label("dClosedLoop", "2026-10-26") != "dClosedLoop (2026-10-26)":
                why.append("render_label does not render dClosedLoop (2026-10-26)")
            if why:
                print(f"flip {name}: " + "; ".join(why))
            else:
                print(f"flip {name}: ok" + (f" (the shape does not change under {value})" if same else ""))
            failed += bool(why)
    finally:
        run("reset", "-q", "--hard", start)
        _slug_cache.clear()
        twin._slug_cache.clear()
        _default = _cached = None
    return 1 if failed else 0


_USAGE = ("usage: id_grammar.py --print slug-re|slug-class|slug-grammar [<root>]\n"
          "       id_grammar.py --readers [<root>]\n"
          "       id_grammar.py --flip-probe <scratch clone>")


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", newline="\n")
    if args[:1] == ["--print"] and len(args) in (2, 3) and args[1] in ("slug-re", "slug-class", "slug-grammar"):
        try:
            g = derive_slug_grammar(args[2] if len(args) == 3 else None)
        except ConfError as exc:
            print(f"id_grammar: {exc}", file=sys.stderr)
            return 2
        if g.fallback:
            print(g.fallback, file=sys.stderr)
        if args[1] == "slug-re":
            print("^(" + g.slug_ere + ")$")
        elif args[1] == "slug-class":
            print(g.slug_ere)
        else:
            print(g.record)
            for record in g.recorded:
                print(f"recorded {record}")
        return 0
    if args[:1] == ["--readers"] and len(args) <= 2:
        hits = scan_readers(args[1] if len(args) == 2 else repo_root())
        for hit in hits:
            print(hit)
        print(f"readers: {len(hits)} line(s) in {len({h.split(':', 1)[0] for h in hits})} file(s)",
              file=sys.stderr)
        return 0
    if args[:1] == ["--flip-probe"] and len(args) == 2:
        return run_flip_probe(args[1])
    print(_USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
