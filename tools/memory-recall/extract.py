#!/usr/bin/env python3
"""Build the retrieval document sets from the tracked corpus under ``$MEMORY_ROOT``.

Ported from adopter ic ``scripts/recall/extract.py`` at 5318064 (file last changed 958bd35c3; fd6274d
is that revision's tip and never touched this file). The fork is SEVEN constructs wide, so a future
re-pull is a three-way merge rather than archaeology: (1) ``FAMILIES``; (2) BOTH halves of the
session era inside ``ERAS`` -- the node-tag class, and the trailing ``[a-z]*`` that keys this
corpus's ratified correction-id form (``TOOL-aDrainedSluice-<n>b``), which upstream never mints and
so never had a reason to admit; (3) ``DURABLE``; (4) ``corpus_files()``; (5) the zero-record
diagnosis, now two branches; (6) ``sys.dont_write_bytecode`` above the ``recall_conf`` import plus
``CONF = recall_conf.resolve()`` -- upstream's blob has zero occurrences of either name. Count the
sixth: two of its three lines are load-bearing (without ``CONF``, ``FAMILIES = CONF.families`` is a
NameError, so a re-pull that drops them fails loudly), but ``dont_write_bytecode`` is the whole of
the kit's "writes nothing inside your worktree" property on this file and a re-pull can drop it in
silence -- the .pyc lands next to the source, inside the adopter's tree, and ``git status`` is
clean anyway because ``__pycache__/`` is a near-universal ignore rule; (7) the supersession
derivation, ``extract_supersessions`` and ``derive_supersession_map`` beside ``extract_records``
and the ``superseded`` report line (TOOL-aGraftedHelix-4). Everything else is upstream's, byte for
byte.

Rebuilt instrument for the upstream recall measurement. The original harness lived in a session
scratchpad and was lost with the session, which made every number it produced unfalsifiable. This
version is committed, stdlib-only, and runs anywhere git does.

Three document sets, because they fail differently and the measurement uses all of them:

  spine    one anchored record, definition homes only: DECISIONS.md, BACKLOG.md, an index named
           for an id FAMILY, anything under decisions/, and rotated archive/<INDEX>.<date>.md --
           under the root or one directory down, so both the flat and the nested layout match
  records  one anchored record, anywhere -- including builds/, journals and archives
  chunks   heading-bounded slices of the whole corpus, capped at CHUNK_MAX chars

Usage:  python extract.py <repo-root> <out-dir> [--rev REV] [--aliases <path|none>]

``<repo-root>`` is the repo whose corpus is read; the id grammar and the corpus root always come
from the conf beside THIS kit, so run it inside the repo you are extracting.

Writes ``spine.jsonl``, ``records.jsonl``, ``chunks.jsonl``, ``anchors.json`` and
``orphan-ids.txt``.
Reading at a git rev (rather than the worktree) keeps a measurement reproducible against a sha.

THE GRAMMAR IS THE MEMORY-TREE KIT'S since PLAY-dOrderedCharter-18: the eras, ``Grammar``,
``grammar_for``, ``anchor_at``, the corpus walk and the four record readers check 27 imports live
in that kit's ``id_grammar.py``, found through ``resolve_kit_dir`` (this kit ``requires``
memory-tree), and this file re-exports each name and re-binds its module constants from the
default grammar at import, so the CLI and ``query.py`` read exactly what they read before.
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import re
import subprocess
import sys
from collections import defaultdict

# ABOVE the sibling import, not below it: CPython writes a module's bytecode next to its SOURCE,
# which is inside the adopter's worktree. The kit's whole "a query writes nothing in your tree"
# property is one line, and it has to be this line (spec F5).
sys.dont_write_bytecode = True

import recall_conf  # noqa: E402

CONF = recall_conf.resolve()


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


# The id grammar, from the memory-tree kit's ONE module (PLAY-dOrderedCharter-18), APPENDED to the
# path rather than prepended so no module name that kit carries can shadow one of this kit's.
_GRAMMAR_KIT = str(resolve_kit_dir("memory-tree", "id_grammar.py", pathlib.Path(__file__).resolve().parent))
if _GRAMMAR_KIT not in sys.path:
    sys.path.append(_GRAMMAR_KIT)

import id_grammar  # noqa: E402
from id_grammar import (  # noqa: E402,F401 — re-exported: every reader of this module keeps its spelling
    _EXCLUDE_ANNOUNCED,
    SUPERSEDE_PARTIAL,
    Grammar,
    anchor_at,
    corpus_files,
    corpus_inputs,
    derive_supersession_map,
    extract_records,
    extract_supersessions,
    git,
    grammar_for,
    heading_level,
    resolve_declared_sources,
)

# The module constants, RE-BOUND from the default grammar: the memory-tree kit's binding to the repo
# this kit is installed in, built once per process. The family allowlist is the conf's FAMILIES plus
# its RECALL_CITED_FAMILIES, an id this corpus mentions and never homes, which never joins `_IDX`.
_G = grammar_for()
FAMILIES = _G.families
_NODE = CONF.node_tag_class
ERAS = _G.eras
ID = _G.ID
ID_RE = _G.ID_RE
# An anchor is a line that DEFINES a record, as opposed to one that merely cites it; four shapes.
A_HEADING, A_BOLD_LI, A_TABLE, A_DASH = _G.anchors
SUPERSEDE_P1, SUPERSEDE_P2, SUPERSEDE_P3 = id_grammar.build_supersede_patterns(_G)


# A record's DURABLE home. `archive/<INDEX>.<date>.md` is included: rotation MOVES an index, it does
# not retire its records, so a decision that lived in `DECISIONS.md` is still a decision after the
# file rotates (ARCH-aSmirkingBallast-4, owner 2026-07-28). Before this, the 2026-07-27 rotation
# dropped ids-with-a-durable-anchor 1778 -> 940 and left three fully-written PERF/ARCH records with
# no durable home at all.
#
# Blast radius, measured rather than assumed: DURABLE selects ONLY the `spine` document set
# (below). `anchors.json` is built from `records`, and `check_recall.py` grades `records`+`chunks`,
# so no gate and no merge-bar floor reads this. `bench.py --sets spine` moves; nothing else does.
_ROOT = re.escape(CONF.memory_root)  # FORKED: the corpus root is a conf value, not a literal
# FORKED: the directory segment below the root is OPTIONAL, and an index named for an id FAMILY is
# admitted beside DECISIONS/BACKLOG. Upstream's tree is nested -- `<root>/<dir>/DECISIONS.md` -- and
# every alternation required that segment, so on a FLAT root, which is the shape the memory-tree
# kit's own adopter writes, nothing matched and `spine` was silently empty. Measured here before
# wiring: 0 files matched the nested-only pattern against 1325 tracked, and the form below matches 9
# -- the decision log, the four backlog shards and the four rotated archives -- with zero
# near-misses among index-shaped basenames. Both layouts, one pattern; nothing that matched before
# stops matching.
#
# The family alternation is DERIVED from `CONF.families` and is never a literal list: this repo's
# four prefixes are not an adopter's, and a literal would ship them into every installed kit.
#
# The archive arm also admits one optional segment AFTER `archive/` (TOOL-aRepatriatedFork-12 S3):
# Adopter ic rotates to `<root>/archive/<discipline>/DECISIONS.<date>.md`. Measured over each tree's
# `git ls-files` with its own conf: gov 9 -> 9, nc 13 -> 13, ic 56 -> 71, the 71 being exactly
# the set adopter ic's own pattern selects. No key: a layout knob with one value is not a decision.
#
# The per-build ask file `builds/<slug>/BACKLOG.md` is the fourth arm (TOOL-dDerivedDocket-34 S9).
# Under `BACKLOG_MODE="builds"` an ask's ONE authored home is that file, TWO levels below the root,
# which the first arm's single optional segment cannot reach: without this arm every migrated ask
# loses its durable home the moment the shards become generated views, and the `records` floor
# cannot see it because `DURABLE` selects only the spine. Spelled as the exact basename under
# `builds/`, never a second optional segment, so no other file two levels down joins the spine.
_IDX = "(?:DECISIONS|BACKLOG|" + "|".join(re.escape(f) for f in CONF.families) + ")"
DURABLE = re.compile(
    rf"{_ROOT}/(?:[^/]+/)?{_IDX}\.md$"
    rf"|{_ROOT}/(?:[^/]+/)?decisions/[^/]+\.md$"
    rf"|{_ROOT}/(?:[^/]+/)?archive/(?:[^/]+/)?{_IDX}\.[^/]+\.md$"
    rf"|{_ROOT}/builds/[^/]+/BACKLOG\.md$"
)


def render_empty_spine_diagnosis(n_records: int, n_spine: int) -> str | None:
    """A non-empty ``records`` beside an empty ``spine``. ``None`` when there is nothing to say.

    Unlike zero records, this state has NO honest reading. Records exist, so the corpus root and the
    id grammar both work, and the only remaining cause is that ``DURABLE`` describes a layout this
    tree does not have -- which is exactly what shipped: the pattern required a directory segment
    the flat layout has none of, and the ``spine`` set was empty here, and in any adopter with a
    flat memory root, for a month with nothing saying so.

    A PRINT rather than a refusal, matching ``zero_record_diagnosis`` exactly. The defect was
    invisible because nothing SAID anything, not because nothing refused, and a refusal would block
    an adopter mid-migration whose repo was working a minute earlier.
    """
    if n_spine or not n_records:
        return None
    return (
        f"EMPTY SPINE — {n_records} records extracted but 0 durable homes matched.\n"
        f"  DURABLE resolved to: {DURABLE.pattern}\n"
        f"  MEMORY_ROOT resolved to: {CONF.memory_root}\n"
        f"  FAMILIES resolved to: {' '.join(CONF.families)}\n"
        "  Records exist, so the root and the id grammar both work. The pattern above is\n"
        "  describing index files this tree does not have. It looks for, under the root and\n"
        "  optionally one directory down: DECISIONS.md, BACKLOG.md, <FAMILY>.md, anything under\n"
        "  decisions/, and rotated archive/<INDEX>.<date>.md. `bench.py --sets spine` grades an\n"
        "  empty set until this is fixed; nothing else reads it."
    )

CHUNK_MAX = 2400

# --- the alias layer ------------------------------------------------------------------------------
# The alias MECHANISM ships; no alias DATA does. Upstream's aliases.json is 915 515 bytes of
# questions authored against adopter ic's corpus and joined by id, and no id in it exists anywhere
# else. An absent default is a legal alias-free corpus (see load_aliases), so an adopter runs with
# every alias cell empty until they author their own; drop an `aliases.json` in THIS directory and
# it is picked up with no config edit, and the cache rebuilds on the digest change.
#
# The join is by id, newline-joining each record's `questions` -- `bench.build_index` gives the
# `alias` key a separate, down-weighted FTS5 column, so bridge text is searchable without diluting
# the record's own vocabulary.
#
# Resolved beside THIS SCRIPT rather than under the repo root: script and data ship together, and
# both call sites (`main()` here and `query._docs`) hold a repo path that need not contain the kit
# directory at all -- a throwaway test repo does not.
ALIASES_DEFAULT = pathlib.Path(__file__).resolve().parent / "aliases.json"


class AliasError(RuntimeError):
    """An EXPLICITLY REQUESTED alias source that could not be read. An absent DEFAULT is not one."""


_DECL_RE = re.compile(r"^\s*(?:export\s+)?([A-Z][A-Z0-9_]*)\s*=(.*)$")


def extract_declarations(path: str, text: str) -> list[dict]:
    """One chunk per ``KEY=value`` assignment, carrying the comment block ABOVE it.

    The comment block is the whole point. This tree puts a constraint's justification in the lines
    above the number -- ``INDEX_CAP_BYTES`` carries its derivation and every movement of it -- and a
    chunk of just ``INDEX_CAP_BYTES="61440"`` would be reachable and worthless. The example this
    docstring used to give was ``READ_PATH_CEILING``, retired in memory-tree 2.42.

    These are CHUNKS, not records: a record is keyed by a corpus id in this tree's
    ``FAMILY-slug-seq`` grammar, and a declaration has a KEY. Admitting them to ``records`` would
    put un-id'd rows into the set ``anchors.json`` is built from.
    """
    lines = text.split("\n")
    out = []
    for i, line in enumerate(lines):
        m = _DECL_RE.match(line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        j = i - 1
        while j >= 0 and lines[j].lstrip().startswith("#"):
            j -= 1
        why = "\n".join(lines[j + 1:i]).strip()
        body = f"{key} = {value}"
        if why:
            body += "\n" + why
        out.append({
            "path": path, "line": i + 1, "heading": key,
            "text": body[:CHUNK_MAX], "kind": "declaration",
        })
    return out


def read(repo: pathlib.Path, path: str, rev: str | None) -> str:
    if rev:
        try:
            return git(repo, "show", f"{rev}:{path}")
        except subprocess.CalledProcessError:
            return ""
    try:
        return (repo / path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def load_aliases(
    source: str | None = None, repo: pathlib.Path | None = None, rev: str | None = None
) -> tuple[dict[str, str], str, str]:
    """``(id -> alias block, resolved source, content digest)`` for one alias source.

    ``source`` is a path, the literal ``none``, or ``None`` for the committed default.

    The refusal fires ONLY on an explicitly requested but unreadable source. An absent DEFAULT is a
    legal alias-free corpus -- the selftest's throwaway repo is one -- while a caller that NAMED a
    file and got nothing would otherwise be handed a silent empty join, which is indistinguishable
    from a working one until a recall floor reds minutes later. Malformed JSON always refuses: a
    parse failure is never a legal alias-free corpus.

    Under ``--rev`` the blob is read AT THAT REV, so a measurement pinned to a sha is pinned on both
    halves rather than mixing that rev's corpus with the working tree's alias text. A file OUTSIDE
    that repo has no blob at any rev, so it is read from the worktree and the source string says
    so -- see the branch below.
    """
    if source == "none":
        return {}, "none", ""
    explicit = source is not None
    path = pathlib.Path(source).resolve() if explicit else ALIASES_DEFAULT
    raw: str | None = None
    off_rev = False
    if rev and repo is not None:
        rel = None
        try:
            rel = path.relative_to(repo).as_posix()
        except ValueError:
            rel = None
        if rel:
            try:
                raw = git(repo, "show", f"{rev}:{rel}")
            except subprocess.CalledProcessError:
                raw = None
        else:
            # The file is OUTSIDE the repo under measurement, so it HAS no blob at that
            # rev -- and the DEFAULT resolves beside this script, so every cross-tree
            # `--rev` run lands here. Read the worktree copy and SAY SO. Leaving `raw`
            # unset dropped through to the `(absent)` return below, which is the legal
            # alias-free corpus: a `--rev` run, the one path whose whole purpose is a
            # reproducible measurement, then scored an alias-free corpus behind a
            # success-looking summary line (ARCH-aGrittedFlagstone-4, closing review F7).
            try:
                raw = path.read_text(encoding="utf-8")
                off_rev = True
            except OSError:
                raw = None
    else:
        try:
            raw = path.read_text(encoding="utf-8")
        except OSError:
            raw = None
    if raw is None:
        if explicit:
            raise AliasError(
                f"aliases: cannot read {path}" + (f" at rev {rev}" if rev else "")
                + " — it was requested explicitly, so this is a refusal, not an empty join."
            )
        return {}, f"{path} (absent)", ""
    try:
        payload = json.loads(raw)
    except ValueError as e:
        raise AliasError(f"aliases: {path} is not valid JSON: {e}") from e
    rows = payload["aliases"] if isinstance(payload, dict) else payload
    by_id: dict[str, str] = {}
    for a in rows:
        rid = (a.get("id") or "").strip()
        block = "\n".join(str(q) for q in (a.get("questions") or []) if str(q).strip())
        if rid and block:
            by_id[rid] = block
    src_label = f"{path} (worktree, not at rev)" if off_rev else str(path)
    return by_id, src_label, hashlib.sha1(raw.encode("utf-8")).hexdigest()[:12]


def join_aliases(records: list[dict], by_id: dict[str, str]) -> int:
    """Set ``alias`` on every record whose id carries one. Returns how many were augmented.

    Records only. `chunks` stay alias-free (the handed measurement holds them constant) and so does
    `spine` -- its rows are copied off `records` BEFORE this runs, because `main()` derives spine as
    a filter over the SAME dict objects and `dump()` writes every key.
    """
    n = 0
    for r in records:
        block = by_id.get(r.get("id", ""))
        if block:
            r["alias"] = block
            n += 1
    return n


def zero_record_diagnosis(
    n_records: int, n_chunks: int, rebuild_hint: str = "--rebuild"
) -> str | None:
    """The mis-declared-FAMILIES failure, named. ``None`` when there is nothing to say.

    THE defect this port exists to close. The chunk arm is family-blind and works with zero
    configuration; the record arm is the only consumer of the id grammar. Point the conf at a
    corpus whose ids it does not describe and upstream returns "index 0 records + N chunks" and
    reports success -- a healthy-looking run that silently answers from half the index. Zero
    records is ALSO the honest state of a tree that has not written a decision yet, so this is a
    loud printed diagnosis rather than a refusal: it names the key, the conf, the families it
    resolved, and the escape hatch for a cache built before the conf was repaired.

    TWO branches, because 0 records + 0 chunks has a DIFFERENT cause and a single guard reading
    ``n_records or not n_chunks`` excluded it from every diagnosis. The chunk arm needs no id
    grammar, so an empty chunk arm cannot be FAMILIES -- it is MEMORY_ROOT, which is one of the
    three keys the adopter hand-edits and where a one-character typo produces exactly this.
    """
    if n_records:
        return None
    resolved = (
        f"  FAMILIES in {CONF.path.as_posix()} resolved to: {' '.join(CONF.families)}\n"
        f"  MEMORY_ROOT resolved to: {CONF.memory_root}\n"
    )
    if not n_chunks:
        return (
            "EMPTY CORPUS — no records AND no chunks: nothing reached the index at all.\n"
            + resolved
            + "  MEMORY_ROOT is the prime suspect: the chunk arm needs no id grammar, so FAMILIES\n"
              "  cannot cause this. Check it names a directory that exists, and that the files in\n"
              "  it are TRACKED — the corpus is read from the git index, so anything nobody\n"
              "  `git add`ed reads as absent.\n"
            + f"  After fixing the conf, re-run with {rebuild_hint} if the cache predates the fix."
        )
    return (
        f"ZERO RECORDS — the corpus produced {n_chunks} chunks and not one anchored record.\n"
        + resolved
        + "  Either no decision has been written yet, or FAMILIES does not describe this corpus's\n"
          "  ids. The chunk arm works without the grammar, so this is the only signal you get.\n"
        + f"  After fixing the conf, re-run with {rebuild_hint} if the cache predates the fix."
    )


def extract_chunks(
    path: str, text: str, chunk_max: int = CHUNK_MAX, overlap: float = 0.0
) -> list[dict]:
    """Heading-bounded slices of the whole file, hard-capped at ``chunk_max`` chars.

    Each chunk also carries two structural fields, so alternative index shapes can be measured
    without re-extracting:

      ``crumb``  the heading ancestry above it (``H1 > H2 > H3``) -- context a bare slice loses
      ``rec``    the anchored record it sits inside, if any -- lets a hit roll up to its parent

    ``overlap`` (0..0.9) slides the window instead of tiling it, so an answer straddling a boundary
    is not split across two documents that each carry half of it.
    """
    lines = text.splitlines()
    bounds = [k for k, ln in enumerate(lines) if heading_level(ln) is not None] or [0]
    if bounds[0] != 0:
        bounds.insert(0, 0)
    bounds.append(len(lines))
    step = max(1, int(chunk_max * (1.0 - min(0.9, max(0.0, overlap)))))
    out: list[dict] = []
    stack: list[tuple[int, str]] = []
    cur_rec: str | None = None
    for a, b in zip(bounds, bounds[1:], strict=False):
        head_line = lines[a] if heading_level(lines[a]) is not None else ""
        lvl = heading_level(head_line) if head_line else None
        if lvl is not None:
            while stack and stack[-1][0] >= lvl:
                stack.pop()
            stack.append((lvl, re.sub(r"^#+\s*", "", head_line).strip()))
            found = anchor_at(head_line)
            if found:
                cur_rec = found
        crumb = " > ".join(t for _, t in stack)
        seg = "\n".join(lines[a:b]).strip()
        if not seg:
            continue
        base = {"path": path, "line": a + 1, "crumb": crumb}
        if cur_rec:
            base["rec"] = cur_rec
        # Long sections split into windows; each window re-carries the heading so a hit deep in a
        # section still names what it belongs to.
        if len(seg) <= chunk_max:
            out.append({**base, "text": seg})
        else:
            for off in range(0, len(seg), step):
                piece = seg[off : off + chunk_max]
                if not piece.strip():
                    continue
                out.append(
                    {
                        **base,
                        "text": piece if off == 0 or not head_line else head_line + "\n" + piece,
                    }
                )
                if off + chunk_max >= len(seg):
                    break
    return out


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    # A FLAG IS NOT A PATH, and the check above is ARITY alone. `extract.py <repo> --help` is a
    # well-formed three-argument call, so `--help` reached `outdir` and the `mkdir(parents=True)`
    # below CREATED A DIRECTORY named `--help`, exit 0. The lexicon kit's scaffolder shipped
    # the same defect and wrote a FILE by the same route; that one was committed and pushed to a
    # real adopter before anyone noticed it. A path whose name is a flag breaks every unquoted
    # glob in its directory from then on, and the directory is the worse half -- `rm -rf --help`
    # does not remove it either. `./--help` still reaches a genuine leading-dash path.
    for _slot, _val in (("REPO", sys.argv[1]), ("OUTDIR", sys.argv[2])):
        if _val.startswith("-"):
            sys.stderr.write(f"extract.py: {_val!r} is a flag, not a path, in the {_slot} "
                             f"slot -- this script takes two positional PATHS.\n")
            print(__doc__)
            return 2
    repo = pathlib.Path(sys.argv[1]).resolve()
    outdir = pathlib.Path(sys.argv[2])
    outdir.mkdir(parents=True, exist_ok=True)
    rev = None
    if "--rev" in sys.argv:
        rev = sys.argv[sys.argv.index("--rev") + 1]
    chunk_max = CHUNK_MAX
    if "--chunk-max" in sys.argv:
        chunk_max = int(sys.argv[sys.argv.index("--chunk-max") + 1])
    overlap = 0.0
    if "--overlap" in sys.argv:
        overlap = float(sys.argv[sys.argv.index("--overlap") + 1])
    asrc = None
    if "--aliases" in sys.argv:
        asrc = sys.argv[sys.argv.index("--aliases") + 1]

    # BEFORE the corpus scan: a refusal a caller waits 4.5 s for is one they will route around.
    try:
        by_id, alias_src, alias_digest = load_aliases(asrc, repo, rev)
    except AliasError as e:
        print(e, file=sys.stderr)
        return 1

    files = corpus_files(repo, rev)
    records, chunks = [], []
    anchors: dict[str, list[str]] = defaultdict(list)
    cited: set[str] = set()
    sup_edges: list[tuple[str, str, str, str]] = []

    for path in files:
        text = read(repo, path, rev)
        if not text:
            continue
        cited.update(ID_RE.findall(text))
        recs = extract_records(path, text)
        for d in recs:
            records.append(d)
            anchors[d["id"]].append(path)
        sup_edges += extract_supersessions(path, text, recs)
        chunks.extend(extract_chunks(path, text, chunk_max, overlap))

    # The DECLARED extra sources. Chunks only, and separate from the loop above because these are
    # not markdown: a conf swept as prose would put shell syntax and section banners into
    # retrieval, where the unit of value is the declaration plus its justification.
    for path in resolve_declared_sources(repo, rev):
        text = read(repo, path, rev)
        if not text:
            continue
        chunks.extend(extract_declarations(path, text))

    # COPIES, and BEFORE the join: spine is a filter over the same dict objects and `dump()` writes
    # every key, so a join applied first would silently alias 2 505 of spine's 2 959 documents --
    # a document set no published figure was ever measured on (`alias_bench.py` copies spine
    # byte-for-byte from the un-augmented dir, so every figure came from an alias-FREE spine).
    spine = [dict(d) for d in records if DURABLE.search(d["path"])]
    n_aliased = join_aliases(records, by_id)
    unresolved = sorted(i for i in by_id if i not in anchors)

    def dump(name: str, rows: list[dict]) -> int:
        p = outdir / f"{name}.jsonl"
        with p.open("w", encoding="utf-8", newline="\n") as fh:
            for k, r in enumerate(rows):
                fh.write(json.dumps({"doc": k, **r}, ensure_ascii=False) + "\n")
        return sum(len(r["text"]) for r in rows)

    sizes = {n: dump(n, r) for n, r in (("spine", spine), ("records", records), ("chunks", chunks))}

    (outdir / "anchors.json").write_text(
        json.dumps({k: sorted(set(v)) for k, v in anchors.items()}, indent=0, sort_keys=True),
        encoding="utf-8",
        newline="\n",
    )
    orphans = sorted(cited - set(anchors))
    (outdir / "orphan-ids.txt").write_text(
        "\n".join(orphans) + "\n", encoding="utf-8", newline="\n"
    )

    durable_ids = {d["id"] for d in spine}
    print(f"corpus      {len(files):>7} files, rev={rev or 'worktree'}")
    diag = zero_record_diagnosis(len(records), len(chunks))
    if diag:
        print(diag, file=sys.stderr)
    spine_diag = render_empty_spine_diagnosis(len(records), len(spine))
    if spine_diag:
        print(spine_diag, file=sys.stderr)
    for n, rows in (("spine", spine), ("records", records), ("chunks", chunks)):
        print(f"{n:<11} {len(rows):>7} docs, {sizes[n]:>10} indexed chars")
    print(f"ids cited   {len(cited):>7}")
    print(f"ids anchored{len(anchors):>7}  (durable home: {len(durable_ids)})")
    pct = 100 * len(orphans) / max(1, len(cited))
    print(f"orphan ids  {len(orphans):>7}  ({pct:.1f}% of cited)")
    # The source and its digest, so a recorded measurement names the blob it used. The two counts
    # are REPORTED here and pinned in `check_recall.py`: both move with corpus growth.
    print(f"aliases     {n_aliased:>7} records aliased  (ids {len(by_id)}, unresolved "
          f"{len(unresolved)}, digest {alias_digest or '-'}, source {alias_src})")
    # Always printed, a zero included: a map that derived nothing reads as zero out loud.
    _, sc = derive_supersession_map(sup_edges, set(anchors))
    pp = " ".join(f"{p} {v['whole'] + v['partial']} ({v['whole']} whole, {v['partial']} partial)"
                  for p, v in sc["patterns"].items())
    print(f"superseded  {sc['ids']:>7} ids  ({sc['whole']} whole, {sc['partial']} partial only; "
          f"edges {pp}; unresolved {len(sc['unresolved'])}"
          + (": " + " ".join(sc["unresolved"]) if sc["unresolved"] else "") + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
