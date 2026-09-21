#!/usr/bin/env python3
"""transition_audit.py — hygiene check 25: the transition-merge audit.

A merge that joins a lineage still editing AUTHORED backlog shards to a lineage already rendering
them from build folders can lose a row change with nobody watching. The shards side's edit touches a
file the builds side no longer authors, so a clean three-way merge can take either side and neither
outcome is a conflict. This module finds every such merge in the history a tip carries, names the
rows whose change has no provenance record, and refuses.

    python transition_audit.py                              # audit HEAD, account against HEAD
    python transition_audit.py --at <sha>                   # audit <sha>, account against <sha>
    python transition_audit.py --at <sha> --expect-builds   # ... with the caller's own mode reading
    python transition_audit.py --report                     # list every transition; never red
    python transition_audit.py --pin                        # print the rows unpinned transitions owe
    python transition_audit.py --staged                     # audit the pending merge, tree the index

Exit 0 accounted or dormant, 1 unaccounted or duplicate, 2 DEAD PROBE.

WHAT THIS DOES NOT CHECK, stated because a structural check reads as a semantic one to everybody who
did not write it. It reads MERGES. A rebase, a squash or a cherry-pick that drops a row leaves no
merge commit behind and is invisible here; that hole is stated rather than closed. It keys rows by
the anchor grammar, which reads ONE physical line, so a text change on a continuation line of a
wrapped legacy row is not a version change to this module. It does not decide whether a RELOCATED
row's `why` is TRUE — only that exactly one row names the id and the commit. And it grades the
BACKLOG population alone: the decision log, its rotated archives, the retired ledger shards and the
frozen charter snapshots are outside the watched set on purpose, because rotating the decision log
is routine and every id anchored in a rotated log would otherwise read as a lost row.

EVERY GIT READ GOES THROUGH `run_git`, which pins the dereference: `--no-replace-objects` plus an
empty `GIT_GRAFT_FILE`. A `git replace` ref rewrites what a sha MEANS and a graft file rewrites the
commit GRAPH, and this module's whole answer is about what a sha means and whose ancestor it is.
The unattended kit's history leg holds the identical pin for the identical reason.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import subprocess
import sys

# CPython writes a module's bytecode beside its SOURCE, which is inside the tree a commit-msg hook
# is in the middle of committing. This module reads git objects and prints lines; the advisory cache
# under the git dir is the only thing it ever writes.
sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent

# The cache's generation. BUMP IT whenever the delta's SHAPE or the rule computing it changes: an
# entry written by an older rule is not a faster answer, it is a different one. The epoch is stored
# INSIDE each file rather than only in its path, so a foreign entry is DETECTED and reported instead
# of being quietly skipped by a path that never matched.
CACHE_EPOCH = 1

# ONE PREFIX ON EVERY LINE THIS CHECK PRINTS — the liveness line, the dormant announcement and each
# refusal. A consumer (remote CI's history-audit step, an operator's grep) then greps one string and
# cannot miss a class of line it did not know to look for.
SAY = "memory-hygiene: check 25 "

NEW, CHANGED, REMOVED = "new", "changed", "removed"
# The pseudo-rev for the staged tree. Carries a byte no sha can, so it cannot collide with one.
INDEX = "\x00index"


class Problem(Exception):
    """A named, user-facing failure. Printed as one line, never as a traceback."""


class DeadProbe(Problem):
    """The check cannot answer. Exit 2, and never a reassuring zero."""


# ------------------------------------------------------------------------------------ git, pinned
def build_git_env() -> dict:
    """The environment every git call in this module runs under.

    `GIT_GRAFT_FILE=/dev/null` is the spelling `tools/unattended/check-pass-order.sh` uses and it
    works under Git for Windows, whose MSYS layer maps the name. A graft file re-parents commits, so
    without this pin every ancestry answer below could be honest about a sha and wrong about what
    that sha means.
    """
    env = dict(os.environ)
    env["GIT_GRAFT_FILE"] = "/dev/null"
    return env


def run_git(root, *args, stdin: bytes | None = None, want_bytes: bool = False):
    """One git call, pinned. Raises `Problem` naming the argv on a non-zero status."""
    argv = ["git", "--no-replace-objects", "-C", str(root), *args]
    proc = subprocess.run(argv, input=stdin, capture_output=True, env=build_git_env())
    if proc.returncode != 0:
        detail = proc.stderr.decode("utf-8", "replace").strip()
        raise Problem(f"`git {' '.join(args)}` failed: {detail}")
    return proc.stdout if want_bytes else proc.stdout.decode("utf-8", "replace")


def resolve_root() -> pathlib.Path:
    """The nearest ancestor of THIS FILE holding `.memory-tree.conf`.

    Not `git rev-parse --show-toplevel`, for the reason `merge-rows.py` records: this module runs
    inside a commit-msg hook, where the shell is whatever git found, and a walk-up needs no process
    at all. It is also correct at both install prefixes — `tools/memory-tree/` here and
    `memory-tree/` in a repo that copy-installed the kit — with no env var and no second
    declaration. AN EMPTY DERIVATION REFUSES: a guessed root grades somebody else's corpus.
    """
    for parent in KIT.parents:
        if (parent / ".memory-tree.conf").is_file():
            return parent
    raise Problem(f"no .memory-tree.conf above {KIT.as_posix()}, so there is no tree to audit and "
                  f"no declaration to read the watched paths from")


def resolve_recall_kit(root: pathlib.Path) -> pathlib.Path:
    """The memory-recall kit directory, in either install layout.

    Tools-first, the order `merge-rows.py` and `check-wiring.sh` already use. THERE IS NO DEGRADED
    MODE: keying rows by anything but the declared anchor grammar grades a different population
    under a rule nobody configured, which is worse than refusing and harder to notice.
    """
    tried = [root / "tools" / "memory-recall", root / "memory-recall"]
    for cand in tried:
        if cand.is_dir() and (cand / "extract.py").is_file():
            return cand
    looked = " and ".join(c.as_posix() for c in tried)
    raise Problem(
        f"the `memory-recall` kit is not installed beside this one (looked in {looked}). Check 25 "
        f"keys every delta row through that kit's anchor grammar and there is no degraded mode: a "
        f"second row grammar spelled here would be two answers to one question. "
        f"Remedy: install the memory-recall kit")


def resolve_anchor(root: pathlib.Path):
    """`(anchor_at, grammar)` bound to THIS tree, imported lazily from the memory-recall kit.

    Lazy on purpose, and the same import `merge-rows.py` makes: at module scope an import failure
    would kill the commit-msg hook before it could name what is missing, and a hook that dies with a
    traceback reads as a broken repository rather than as a missing kit.
    """
    kit = resolve_recall_kit(root)
    # APPEND, never `insert(0, ...)`: prepending puts the kit dir ahead of the stdlib, so any module
    # name it ever gains shadows the real one.
    if str(kit) not in sys.path:
        sys.path.append(str(kit))
    import extract as EX   # noqa: PLC0415 — deliberately deferred; see above

    return EX.anchor_at, EX.grammar_for(str(root))


def add_kit_to_path() -> None:
    """This kit's own directory on `sys.path`, so the sibling modules import at any prefix."""
    if str(KIT) not in sys.path:
        sys.path.append(str(KIT))


def load_kit_conf(root: pathlib.Path) -> dict:
    """This tree's `.memory-tree.conf`, through the kit's ONE parser and never a second one."""
    add_kit_to_path()
    import corpus_ids   # noqa: PLC0415 — sibling module, same kit directory

    conf: dict = {}
    corpus_ids.parse_conf((root / ".memory-tree.conf").read_text(encoding="utf-8"), conf)
    return conf


def read_mode(text: str) -> str:
    """The backlog mode a `.memory-tree.conf` BLOB declares — `builds` or `shards`.

    Routed through the kit's own parser and the parser module's own resolver, so "a blank key reads
    shards" is written in one place. An UNRECOGNISED value reads as shards here rather than raising:
    this is a HISTORICAL blob, not a live configuration, and a commit whose conf nobody can parse is
    certainly not a commit that had already switched.
    """
    add_kit_to_path()
    import backlog        # noqa: PLC0415 — sibling module, same kit directory
    import corpus_ids     # noqa: PLC0415 — sibling module, same kit directory

    conf: dict = {}
    try:
        corpus_ids.parse_conf(text, conf)
        return backlog.read_conf(conf).mode
    except Exception:
        return "shards"


def derive_watched(root: pathlib.Path, conf: dict) -> tuple:
    """`(memory_root, backlog_prefix, family_archive_re)` — the WATCHED PATHS, and nothing else.

    The backlog directory, plus the FAMILY-named rotated archives under `archive/` and NOT that
    directory as a whole. `archive/` also holds the rotated DECISION LOG, the retired ledger shards
    and the frozen charter snapshots. Rotating the decision log is a routine, sanctioned action
    under `ROTATION_MODE="cut"`, and every id anchored in a rotated log would then read as a NEW row
    on any straggler that rotated one — redding this check with decision ids whose only printed
    remedy is a RELOCATED row per decision. `row_grammar.derive_families` is the ONE derivation of
    the family set; this reads it rather than spelling a second alternation.
    """
    add_kit_to_path()
    import row_grammar    # noqa: PLC0415 — sibling module, same kit directory

    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    fams = row_grammar.derive_families(conf)
    alt = "|".join(re.escape(f) for f in sorted(fams))
    archive_re = re.compile(
        r"^" + re.escape(f"{memory_root}/archive/") + r"(?:" + alt + r")"
        r"\.[0-9]{4}-[0-9]{2}-[0-9]{2}[a-z0-9]*\.md$")
    return memory_root, f"{memory_root}/backlog/", archive_re


def check_watched(path: str, backlog_prefix: str, archive_re) -> bool:
    """Is this tracked path one of the WATCHED PATHS? One predicate, every caller."""
    if path.startswith(backlog_prefix):
        return True
    return bool(archive_re.match(path))


def derive_conf_rel(root: pathlib.Path) -> str:
    """`.memory-tree.conf`'s path relative to the GIT toplevel, which its tree may sit under.

    Git object paths are repo-relative and the memory-tree root is not required to BE the repo root.
    An empty prefix is the ordinary case and is not a failure.
    """
    prefix = run_git(root, "rev-parse", "--show-prefix").strip()
    return f"{prefix}.memory-tree.conf" if prefix else ".memory-tree.conf"


# ------------------------------------------------------------------------------- the commit graph
def build_graph(root: pathlib.Path, tips: list) -> tuple:
    """`(parents, order, pos)` from ONE `rev-list --parents` over every tip.

    `order` is git's own newest-first ordering, a linear extension of the graph, which is what lets
    the change-commit scan walk backwards without a second sort; `pos` is its inverse so no caller
    pays a list scan per lookup. `parents` keeps parent order, so first-parent stays answerable.
    """
    out = run_git(root, "rev-list", "--parents", *tips)
    parents: dict = {}
    order: list = []
    for raw in out.split("\n"):
        line = raw.strip()
        if not line:
            continue
        bits = line.split()
        parents[bits[0]] = bits[1:]
        order.append(bits[0])
    return parents, order, {sha: i for i, sha in enumerate(order)}


def derive_ancestors(parents: dict, start: str) -> set:
    """Every commit reachable from `start`, `start` included. Iterative: histories are deep."""
    seen = {start}
    stack = [start]
    while stack:
        for par in parents.get(stack.pop(), ()):
            if par not in seen:
                seen.add(par)
                stack.append(par)
    return seen


def derive_bases(parents: dict, sets: list) -> list:
    """The MERGE BASES of the given ancestor sets — git's `merge-base --all`, in Python.

    The common ancestors are the intersection, which is downward closed; a base is a MAXIMAL member,
    and a member is maximal exactly when no CHILD of it is also common. That equivalence is what
    makes this one pass rather than a search: downward closure means any path from a non-maximal
    member up to a maximal one has its first step inside the set.

    Computed here rather than shelled out because the walk classifies every merge in the history,
    and a process per merge per parent is the cost this module exists not to pay.
    """
    common = set(sets[0])
    for other in sets[1:]:
        common &= other
    if not common:
        return []
    has_child: set = set()
    for sha in common:
        for par in parents.get(sha, ()):
            if par in common:
                has_child.add(par)
    return sorted(sha for sha in common if sha not in has_child)


def derive_lineage(parents: dict, tip: str, others: list, cache: dict) -> tuple:
    """`(lineage, bases)` for `tip` against `others` — `merge-base --all(tip, others)..tip`.

    The excluded set is the INTERSECTION of the others' ancestor sets, because that is what git's
    multi-argument `merge-base` answers. With one other parent — which is every merge this corpus
    has — it reduces to `other..tip`.
    """
    mine = cache.setdefault(tip, derive_ancestors(parents, tip))
    theirs = [cache.setdefault(o, derive_ancestors(parents, o)) for o in others]
    if not theirs:
        return set(mine), []
    excluded = set(theirs[0])
    for other in theirs[1:]:
        excluded &= other
    return mine - excluded, derive_bases(parents, [mine] + theirs)


def derive_boundaries(parents: dict, order: list, modes: dict) -> tuple:
    """`(boundaries, reaches)` — the mode boundaries, and which commits have one behind them.

    A MODE BOUNDARY is a builds-mode commit with a shards-mode parent: a linear flip commit is one,
    and so is every transition merge. `reaches` is computed in ONE oldest-first pass over `order`,
    which is a linear extension, so a per-merge ancestor walk is never paid just to ask whether a
    merge is a candidate at all.
    """
    boundaries = {sha for sha in order
                  if modes.get(sha) == "builds"
                  and any(modes.get(p) != "builds" for p in parents.get(sha, ()))}
    reaches: dict = {}
    for sha in reversed(order):
        hit = sha in boundaries
        if not hit:
            hit = any(reaches.get(p) for p in parents.get(sha, ()))
        reaches[sha] = hit
    return boundaries, reaches


# ------------------------------------------------------------------------------ blobs, in batches
def scan_touching(root: pathlib.Path, tips: list, memory_root: str,
                  backlog_prefix: str, archive_re) -> tuple:
    """`(touching, paths)` — the commits that touch a WATCHED PATH, and every path they touched.

    ONE `git log` over the two candidate directories. `--diff-merges=first-parent` makes a merge
    report the diff it introduced against its first parent, so a merge that brought rows in is named
    rather than reading as empty. The family filter runs HERE, in Python, because the archive half
    of the watched set is an alternation over declared families and not a pathspec.
    """
    out = run_git(root, "log", "--format=%x01%H", "--name-only", "--diff-merges=first-parent",
                  "--no-renames", *tips, "--",
                  backlog_prefix.rstrip("/"), f"{memory_root}/archive")
    touching: set = set()
    paths: set = set()
    cur = ""
    for raw in out.split("\n"):
        line = raw.rstrip("\r")
        if line.startswith("\x01"):
            cur = line[1:].strip()
            continue
        line = line.strip()
        if not line or not cur:
            continue
        if check_watched(line, backlog_prefix, archive_re):
            touching.add(cur)
            paths.add(line)
    return touching, paths


def read_blobs(root: pathlib.Path, specs: list) -> dict:
    """`{spec: text or None}` for every `<rev>:<path>` in `specs`, in ONE `cat-file --batch`.

    A missing path yields None rather than an exception: an absent backlog shard is a real state of
    a tree, and it is exactly the version an id is REMOVED to.
    """
    if not specs:
        return {}
    stdin = ("\n".join(specs) + "\n").encode("utf-8")
    raw = run_git(root, "cat-file", "--batch", stdin=stdin, want_bytes=True)
    out: dict = {}
    pos = 0
    for spec in specs:
        nl = raw.find(b"\n", pos)
        if nl < 0:
            out[spec] = None
            continue
        header = raw[pos:nl].decode("utf-8", "replace")
        pos = nl + 1
        bits = header.split()
        if len(bits) != 3 or not bits[2].isdigit():
            out[spec] = None
            continue
        size = int(bits[2])
        out[spec] = raw[pos:pos + size].decode("utf-8", "replace")
        pos += size + 1   # git writes a trailing newline after every body
    return out


def read_modes(root: pathlib.Path, commits: list, conf_rel: str) -> dict:
    """`{sha: 'builds'|'shards'}` for every commit, in two processes for the whole history.

    One `cat-file --batch-check` resolves each commit's conf BLOB ID, then one `cat-file --batch`
    reads the DISTINCT blobs. A history re-uses one conf blob for hundreds of commits at a time, so
    the second process reads a handful of objects however long the history is.
    """
    if not commits:
        return {}
    stdin = ("\n".join(f"{sha}:{conf_rel}" for sha in commits) + "\n").encode("utf-8")
    check = run_git(root, "cat-file", "--batch-check", stdin=stdin).split("\n")
    blob_of: dict = {}
    for sha, line in zip(commits, check):
        bits = line.split()
        blob_of[sha] = bits[0] if len(bits) == 3 and bits[1] == "blob" else None
    texts = read_blobs(root, sorted({b for b in blob_of.values() if b}))
    return {sha: (read_mode(texts.get(blob) or "") if blob else "shards")
            for sha, blob in blob_of.items()}


def read_versions(root: pathlib.Path, revs: list, paths: list, anchor, grammar) -> dict:
    """`{rev: {id: row text}}` — every keyed row of the watched files, at every rev.

    ONE `cat-file --batch` over the whole `revs x paths` cross product. A rev whose tree lacks a
    path contributes nothing for it, which is how a REMOVED row is recognised at all. An id anchored
    on several lines of one rev keeps all of them, joined, so a duplicated row that moves is a
    version change rather than a coin toss.
    """
    specs = [f"{rev}:{path}" for rev in revs for path in paths]
    texts = read_blobs(root, specs)
    out: dict = {}
    for rev in revs:
        rows: dict = {}
        for path in paths:
            body = texts.get(f"{rev}:{path}")
            if body is None:
                continue
            for raw in body.split("\n"):
                line = raw.rstrip("\r")
                key = anchor(line, grammar)
                if key:
                    rows.setdefault(key, []).append(line.strip())
        out[rev] = {k: "\n".join(v) for k, v in rows.items()}
    return out


def read_index_files(root: pathlib.Path, memory_root: str) -> dict:
    """`{path: text}` for every `<M>/builds/*/BACKLOG.md` in the INDEX.

    Read through `ls-files -s` and `cat-file`, never `write-tree`: the commit-msg hook must write
    nothing, and a tree object written by a hook that is about to refuse is an object nobody wanted.
    """
    listing = run_git(root, "ls-files", "-s", "--", f"{memory_root}/builds")
    wanted: list = []
    for raw in listing.split("\n"):
        line = raw.rstrip("\r")
        if not line or "\t" not in line:
            continue
        meta, path = line.split("\t", 1)
        if path.endswith("/BACKLOG.md"):
            wanted.append((path, meta.split()[1]))
    texts = read_blobs(root, [blob for _p, blob in wanted])
    return {path: (texts.get(blob) or "") for path, blob in wanted}


def read_backlog_files(root: pathlib.Path, tip: str, memory_root: str) -> dict:
    """`{path: text}` for every `<M>/builds/*/BACKLOG.md` at `tip` — or in the index, for `INDEX`."""
    if tip == INDEX:
        return read_index_files(root, memory_root)
    listing = run_git(root, "ls-tree", "-r", "--name-only", tip, "--", f"{memory_root}/builds")
    wanted = [p.strip() for p in listing.split("\n") if p.strip().endswith("/BACKLOG.md")]
    texts = read_blobs(root, [f"{tip}:{p}" for p in wanted])
    return {p: (texts.get(f"{tip}:{p}") or "") for p in wanted}


# --------------------------------------------------------------------------------------- the walk
class Walk:
    """Everything one audit resolved once: the graph, the modes, the watched set, the grammar.

    Passed around instead of eleven parameters, and built in exactly one place, so the per-merge
    delta and the public `delta()` cannot end up reading two different watched sets.
    """

    def __init__(self, root: pathlib.Path, tips: list):
        self.root = root
        self.conf = load_kit_conf(root)
        self.memory_root, self.prefix, self.archive_re = derive_watched(root, self.conf)
        self.conf_rel = derive_conf_rel(root)
        self.parents, self.order, self.pos = build_graph(root, tips)
        self.modes = read_modes(root, self.order, self.conf_rel)
        touching, paths = scan_touching(root, tips, self.memory_root, self.prefix, self.archive_re)
        self.touching = touching
        self.paths = sorted(paths)
        self.anc: dict = {}
        self._anchor = None

    def resolve_grammar(self):
        """The anchor grammar, resolved on FIRST USE so a dormant tree never needs the recall kit."""
        if self._anchor is None:
            self._anchor = resolve_anchor(self.root)
        return self._anchor

    def set_grammar(self, pair) -> None:
        """Adopt a grammar the caller already resolved, so the prerequisite is asserted ONCE.

        Full mode resolves it eagerly, before any merge is classified, and hands it here. Doing it
        lazily was a measured defect: a warm delta cache answers every merge without ever keying a
        row, so a tree whose memory-recall kit had been deleted reported a clean audit — the
        refusal S15 owes never fired because nothing asked for the grammar.
        """
        self._anchor = pair


def build_entry(merge: str, row_id: str, kind: str, change: str, bases: dict, ours: str) -> dict:
    """One delta entry, as a plain dict so the cache can hold it verbatim."""
    return {"merge": merge, "id": row_id, "kind": kind, "change": change,
            "bases": bases, "ours": ours}


def derive_change_commit(row_id: str, here, mine: list, versions: dict, ours: str) -> str:
    """The NEWEST lineage commit that MADE this version — the one a RELOCATED row must name.

    `mine` is newest-first. Walking back while the version is unchanged and stopping at the first
    commit that held something else lands on the commit that INTRODUCED the surviving version, which
    is the honest answer when a row is set, changed away and set back: the newest introduction wins
    and the older one is history.
    """
    found = ours
    for sha in mine:
        if versions.get(sha, {}).get(row_id) == here:
            found = sha
            continue
        break
    return found


def derive_entries(walk: Walk, ours: str, others: list, merge: str = "") -> list:
    """S4's delta for the side `ours` against `others`, keyed by row id.

    An id is reported when its row version at `ours` differs from its version at EVERY merge base,
    which is the criss-cross clause: a version equal to one base's is a version somebody already
    merged, whatever the other base says.

    AND NEVER WHEN THE OTHER SIDE ALREADY HELD IT. A straggler that merged a shards-mode default
    commit carries that commit's rows forward, and reporting them as the straggler's own change
    demands a provenance row nobody can honestly write — the author of that change is on the other
    side. The clause tests the VERSION rather than the id, so a row the straggler then edited itself
    is still its own.
    """
    anchor, grammar = walk.resolve_grammar()
    lineage, bases = derive_lineage(walk.parents, ours, others, walk.anc)
    other_lineage: set = set()
    for side in others:
        rest = [o for o in others if o != side] + [ours]
        side_lineage, _b = derive_lineage(walk.parents, side, rest, walk.anc)
        other_lineage |= side_lineage

    mine = sorted(lineage & walk.touching, key=lambda s: walk.pos.get(s, 0))
    theirs_shards = sorted({s for s in other_lineage & walk.touching
                            if walk.modes.get(s) != "builds"},
                           key=lambda s: walk.pos.get(s, 0))

    revs = sorted({ours, *bases, *mine, *theirs_shards})
    versions = read_versions(walk.root, revs, walk.paths, anchor, grammar)
    at_ours = versions.get(ours, {})
    base_maps = [versions.get(b, {}) for b in bases]

    ids = set(at_ours)
    for bmap in base_maps:
        ids |= set(bmap)

    entries: list = []
    for row_id in sorted(ids):
        here = at_ours.get(row_id)
        if base_maps and all(bmap.get(row_id) == here for bmap in base_maps):
            continue
        if not base_maps and here is None:
            continue
        # A6 — the version came across from the other side, so it is not this side's change.
        if any(versions.get(sha, {}).get(row_id) == here for sha in theirs_shards):
            continue
        if here is None:
            kind = REMOVED
        elif not base_maps or all(bmap.get(row_id) is None for bmap in base_maps):
            kind = NEW
        else:
            kind = CHANGED
        entries.append(build_entry(
            merge, row_id, kind, derive_change_commit(row_id, here, mine, versions, ours),
            {b: base_maps[i].get(row_id) for i, b in enumerate(bases)}, here))
    return entries


def derive_transition(walk: Walk, merge: str) -> tuple | None:
    """S3's predicate for one merge: `(shards_side, other_parents)`, or None.

    BY LINEAGE AND NEVER BY TIP. Classifying on a parent's own conf blob is refuted by the straggler
    that pulled the new conf early: its tip reads `builds` while everything it edited is a shard.
    The second conjunct — a builds-mode commit in another parent's lineage — is what keeps an
    ordinary pre-flip merge of two shards-mode branches out of the population.
    """
    kin = walk.parents.get(merge, [])
    if len(kin) < 2:
        return None
    for side in kin:
        others = [k for k in kin if k != side]
        lineage, _bases = derive_lineage(walk.parents, side, others, walk.anc)
        if not any(walk.modes.get(sha) != "builds" for sha in lineage & walk.touching):
            continue
        for other in others:
            rest = [k for k in kin if k != other]
            olin, _ob = derive_lineage(walk.parents, other, rest, walk.anc)
            if any(walk.modes.get(sha) == "builds" for sha in olin):
                return side, others
    return None


# ------------------------------------------------------------------------------------- the public
def delta(ours: str, theirs, root=None) -> list:
    """S13 — the delta of `ours` against `theirs`, with no merge commit between them.

    THE ONE TRANSITION RULE, as a callable. The per-merge delta is this same function applied to a
    merge's shards-side parent against its other parents, so the relocation tools, the hooks and
    check 25 reach one rule rather than three spellings of it. `theirs` is one rev or several.
    """
    base = pathlib.Path(root) if root else resolve_root()
    sides = [theirs] if isinstance(theirs, str) else list(theirs)
    walk = Walk(base, [ours, *sides])
    return derive_entries(walk, ours, sides)


def accounted(entries: list, tip: str = "HEAD", root=None) -> dict:
    """S5 — `{entry index: verdict}` over `tip`'s tree, a verdict being `ok`, `none` or a file list.

    EXACTLY ONE provenance row, in some `<M>/builds/*/BACKLOG.md`, naming the id and carrying a sha
    that is a prefix of the change commit. Zero is unaccounted. Two or more is a DUPLICATE verdict
    naming both files, because two records of one relocation are two claims about what happened.

    Bound to `tip` and never to HEAD, which is the whole reason it takes the argument: the pre-push
    caller grades a tip it is about to publish while its own checkout sits somewhere else.
    """
    base = pathlib.Path(root) if root else resolve_root()
    conf = load_kit_conf(base)
    memory_root = (conf.get("MEMORY_ROOT") or "memory").strip().strip("/")
    add_kit_to_path()
    import backlog        # noqa: PLC0415 — sibling module, same kit directory
    import row_grammar    # noqa: PLC0415 — sibling module, same kit directory

    grammar = backlog.build_grammar(row_grammar.derive_families(conf))
    rows: dict = {}
    for path, text in sorted(read_backlog_files(base, tip, memory_root).items()):
        for raw in text.split("\n"):
            row = backlog.extract_row(raw.rstrip("\r"), grammar)
            if row is not None and row.cls == "provenance":
                rows.setdefault(row.target, []).append((path, row.value))
    out: dict = {}
    for idx, entry in enumerate(entries):
        hits = sorted(path for path, sha in rows.get(entry["id"], [])
                      if sha and entry["change"].startswith(sha))
        out[idx] = "ok" if len(hits) == 1 else ("none" if not hits else hits)
    return out


# -------------------------------------------------------------------------------------- the cache
def resolve_cache_dir(root: pathlib.Path) -> pathlib.Path:
    """The per-merge delta cache, under the git COMMON dir so every worktree shares one."""
    common = pathlib.Path(run_git(root, "rev-parse", "--git-common-dir").strip())
    if not common.is_absolute():
        common = root / common
    return common / "transition-audit-cache"


def read_cache(cache_dir: pathlib.Path, merge: str) -> tuple:
    """`(entries, reason)` — the cached delta, or `(None, 'unreadable'|'foreign epoch')`.

    ONLY THE DELTA IS CACHED, because only the delta is immutable: it is a fact about two lineages
    that cannot change while the merge exists. The VERDICT is not — a RELOCATED row written today
    accounts for a delta computed last week — so caching it would pin an answer to the tree that
    happened to be checked out when the cache was warmed.
    """
    path = cache_dir / f"{merge}.json"
    if not path.is_file():
        return None, ""
    try:
        blob = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None, "unreadable"
    if not isinstance(blob, dict):
        return None, "unreadable"
    if blob.get("epoch") != CACHE_EPOCH:
        return None, "foreign epoch"
    entries = blob.get("entries")
    if not isinstance(entries, list):
        return None, "unreadable"
    return entries, ""


def write_cache(cache_dir: pathlib.Path, merge: str, entries: list) -> None:
    """Best effort. The cache is ADVISORY: an unwritable git dir costs wall clock and nothing else."""
    try:
        cache_dir.mkdir(parents=True, exist_ok=True)
        (cache_dir / f"{merge}.json").write_text(
            json.dumps({"epoch": CACHE_EPOCH, "entries": entries}), encoding="utf-8")
    except OSError:
        pass


# ----------------------------------------------------------------------------------- the registry
def resolve_registry(root: pathlib.Path, memory_root: str) -> pathlib.Path:
    return root / memory_root / "project" / "transition-audit.txt"


def read_registry(path: pathlib.Path) -> list:
    """`[(sha, verdict)]` from the pinned registry; comments and blank lines dropped."""
    if not path.is_file():
        return []
    rows = []
    for raw in path.read_text(encoding="utf-8").split("\n"):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        bits = line.split()
        rows.append((bits[0], bits[1] if len(bits) > 1 else ""))
    return rows


# --------------------------------------------------------------------------------- the whole audit
def scan_history(root: pathlib.Path, tips: list, expect_builds: bool, account_tip: str) -> dict:
    """The audit over the history `tips` carry. Returns a report dict; raises `DeadProbe`.

    THE ORDER OF THE REFUSALS IS THE ORDER OF THE QUESTIONS. Dormancy is asked first: a shards-mode
    tree with no independent claim otherwise has nothing to audit, must not pay for the walk, and
    must not red on a shallow clone it has no use for.
    """
    conf = load_kit_conf(root)
    conf_rel = derive_conf_rel(root)
    # The module's OWN reading of the tip's mode, from the committed conf blob. The SHELL's reading
    # arrives as `expect_builds`. Two readers of one key by two different expressions is the whole
    # of the first refusal: a guard sharing a variable with the thing it guards is not a guard.
    spec = f"{tips[0]}:{conf_rel}"
    tip_mode = read_mode(read_blobs(root, [spec]).get(spec) or "")
    if tip_mode != "builds" and not expect_builds:
        return {"dormant": True, "mode": tip_mode, "conf": conf}

    if run_git(root, "rev-parse", "--is-shallow-repository").strip() == "true":
        raise DeadProbe("DEAD PROBE — this is a SHALLOW repository, so the history a transition "
                        "would live in is truncated and an examined count of zero would be a fact "
                        "about the clone and not about the tree")

    # THE PREREQUISITE, ASSERTED BEFORE ANYTHING IS GRADED. Every delta row is keyed through the
    # memory-recall kit's anchor grammar and there is no degraded mode, so a builds-mode tree
    # without that kit is refused by name here rather than wherever the first row happens to be
    # keyed — which, with a warm cache, is nowhere at all.
    grammar = resolve_anchor(root)

    walk = Walk(root, tips)
    walk.set_grammar(grammar)
    any_builds = any(m == "builds" for m in walk.modes.values())
    any_shards = any(m != "builds" for m in walk.modes.values())
    if not any_builds:
        raise DeadProbe("DEAD PROBE — the caller reads this tree as `builds` and the walk finds no "
                        "builds-mode commit anywhere in its history, so the two conf readers "
                        "disagree and one of them is broken")
    _boundaries, reaches = derive_boundaries(walk.parents, walk.order, walk.modes)
    if any_shards and not any(reaches.values()):
        raise DeadProbe("DEAD PROBE — the history holds both shards-mode and builds-mode commits "
                        "and yields no mode boundary between them, which no real flip can produce; "
                        "the boundary detector is not answering")

    cache_dir = resolve_cache_dir(root)
    report = {"dormant": False, "merges": 0, "transitions": [], "entries": [], "hits": 0,
              "recomputed": {}, "conf": conf}
    for merge in walk.order:
        if len(walk.parents.get(merge, ())) < 2:
            continue
        report["merges"] += 1
        if not reaches.get(merge):
            continue
        found = derive_transition(walk, merge)
        if found is None:
            continue
        report["transitions"].append(merge)
        cached, reason = read_cache(cache_dir, merge)
        if cached is None:
            if reason:
                report["recomputed"][reason] = report["recomputed"].get(reason, 0) + 1
            entries = derive_entries(walk, found[0], found[1], merge)
            write_cache(cache_dir, merge, entries)
        else:
            report["hits"] += 1
            entries = cached
        report["entries"].extend(entries)

    report["verdicts"] = accounted(report["entries"], account_tip, root)
    report["registry"] = read_registry(
        resolve_registry(root, walk.memory_root))
    report["known"] = set(walk.order)
    return report


# --------------------------------------------------------------------------------------- printing
def render_liveness(report: dict, expect_builds: bool) -> str:
    """The one line every full run prints, whatever its verdict. Every count is DERIVED here."""
    pinned = {sha for sha, _v in report["registry"]}
    unpinned = [m for m in report["transitions"] if not any(m.startswith(p) for p in pinned)]
    line = (f"{SAY}transitions examined {len(report['transitions'])} · "
            f"merges walked {report['merges']} · pinned {len(pinned)} · "
            f"unpinned {len(unpinned)} · cache hits {report['hits']}")
    if not expect_builds:
        line += " · reader cross-check not run"
    return line


def print_dormant(report: dict) -> int:
    print(f"{SAY}is DORMANT — this tree's audited tip declares BACKLOG_MODE=`{report['mode']}`, so "
          f"no commit here has switched and there is no transition merge to audit. It arms itself "
          f"the day the flip lands.")
    return 0


def print_recomputed(report: dict) -> None:
    for reason, count in sorted(report["recomputed"].items()):
        print(f"{SAY}cache recomputed {count} ({reason})")


def print_entries(report: dict) -> int:
    """Every unaccounted and duplicate entry, with its remedy. Returns the status they earn."""
    status = 0
    for idx, entry in enumerate(report["entries"]):
        verdict = report["verdicts"].get(idx)
        if verdict == "ok":
            continue
        status = 1
        if verdict == "none":
            print(f"{SAY}UNACCOUNTED — merge {entry['merge']} carries a lost row: {entry['id']} "
                  f"({entry['kind']}), changed by {entry['change']}. Remedy: repair it forward with "
                  f"`--repair {entry['merge']}`, which writes the RELOCATED row this check reads.")
        else:
            print(f"{SAY}DUPLICATE — merge {entry['merge']}: {entry['id']} carries more than one "
                  f"RELOCATED row naming {entry['change']}, in {' and '.join(verdict)}. Two records "
                  f"of one relocation are two claims; keep the one that is true.")
    return status


def print_registry(report: dict) -> int:
    """The pinned registry, graded against this history. Returns the status the rows earn."""
    status = 0
    live = set(report["transitions"])
    for sha, verdict in report["registry"]:
        if not any(k.startswith(sha) for k in report["known"]):
            status = 1
            print(f"{SAY}STALE PIN — the registry lists {sha}, which this history does not hold.")
            continue
        if not any(m.startswith(sha) for m in live):
            status = 1
            print(f"{SAY}STALE PIN — the registry lists {sha}, which no longer classifies as a "
                  f"transition merge. A transition in history is permanent, so a row that stopped "
                  f"classifying is a classifier regression and never a row to delete.")
            continue
        if verdict != "accounted":
            status = 1
            print(f"{SAY}STALE PIN — the registry row for {sha} reads "
                  f"`{verdict or '(nothing)'}`, and the only verdict a pinned row may carry is "
                  f"`accounted`.")
    return status


def print_report(report: dict, expect_builds: bool) -> int:
    """Full mode: the liveness line, every refusal it owes, and the status they earn."""
    if report.get("dormant"):
        return print_dormant(report)
    print_recomputed(report)
    print(render_liveness(report, expect_builds))
    return max(print_entries(report), print_registry(report))


def print_pin_rows(report: dict) -> int:
    """`--pin`: the registry rows the unpinned transitions owe. Prints; writes nothing."""
    if report.get("dormant"):
        print(f"{SAY}is DORMANT — nothing to pin.")
        return 0
    pinned = {sha for sha, _v in report["registry"]}
    for merge in report["transitions"]:
        if not any(merge.startswith(p) for p in pinned):
            print(f"{merge} accounted")
    return 0


def print_detail(report: dict, expect_builds: bool) -> int:
    """`--report`: every transition and every entry, and never a red verdict."""
    if report.get("dormant"):
        return print_dormant(report)
    print_recomputed(report)
    print(render_liveness(report, expect_builds))
    for merge in report["transitions"]:
        print(f"transition {merge}")
    for idx, entry in enumerate(report["entries"]):
        print(f"entry {entry['merge']} · {entry['id']} · {entry['kind']} · {entry['change']} · "
              f"{report['verdicts'].get(idx)}")
    return 0


# ----------------------------------------------------------------------------------------- the CLI
def read_merge_heads(root: pathlib.Path) -> list:
    """Every `MERGE_HEAD` line of the merge being concluded, or []."""
    git_dir = pathlib.Path(run_git(root, "rev-parse", "--git-dir").strip())
    if not git_dir.is_absolute():
        git_dir = root / git_dir
    path = git_dir / "MERGE_HEAD"
    if not path.is_file():
        return []
    return [ln.strip() for ln in path.read_text(encoding="utf-8").split("\n") if ln.strip()]


def cmd_staged(root: pathlib.Path) -> int:
    """S9 — audit the merge being CONCLUDED: parents HEAD and every MERGE_HEAD, tree the index.

    `commit-msg` is the one hook that sees every concluded merge: a clean `git merge` fires
    `pre-merge-commit` with no `MERGE_HEAD` and then `commit-msg` with one, and a conflicted merge
    finished by `git commit` fires `pre-commit` and `commit-msg`, both with `MERGE_HEAD` present.
    With no `MERGE_HEAD` there is no merge, so this exits 0 and prints nothing.

    No dormancy question is asked here and none is needed: S3's predicate IS the question, and a
    pending merge with no shards-side lineage and no builds-mode other side yields no entries.
    """
    heads = read_merge_heads(root)
    if not heads:
        return 0
    kin = [run_git(root, "rev-parse", "HEAD").strip(), *heads]
    walk = Walk(root, kin)
    entries: list = []
    for side in kin:
        others = [k for k in kin if k != side]
        lineage, _b = derive_lineage(walk.parents, side, others, walk.anc)
        if not any(walk.modes.get(sha) != "builds" for sha in lineage & walk.touching):
            continue
        if not any(walk.modes.get(sha) == "builds"
                   for other in others
                   for sha in derive_lineage(walk.parents, other,
                                             [k for k in kin if k != other], walk.anc)[0]):
            continue
        entries.extend(derive_entries(walk, side, others, "the pending merge"))
    if not entries:
        return 0
    verdicts = accounted(entries, INDEX, root)
    status = 0
    for idx, entry in enumerate(entries):
        if verdicts.get(idx) == "ok":
            continue
        status = 1
        print(f"{SAY}refuses this merge — {entry['id']} ({entry['kind']}), changed by "
              f"{entry['change']}, crosses a mode boundary with no RELOCATED row in the index. "
              f"Write the row and conclude the merge, or `--repair` it afterwards.")
    return status


def main(argv: list) -> int:
    mode, at_rev, expect_builds = "check", "HEAD", False
    args = list(argv)
    while args:
        arg = args.pop(0)
        if arg in ("--staged", "--report", "--pin"):
            mode = arg[2:]
        elif arg == "--expect-builds":
            expect_builds = True
        elif arg == "--at":
            if not args:
                print(f"{SAY}--at needs a sha", file=sys.stderr)
                return 2
            at_rev = args.pop(0)
        else:
            print(f"{SAY}unknown argument `{arg}`; the verbs are --at, --expect-builds, --report, "
                  f"--pin and --staged", file=sys.stderr)
            return 2
    try:
        root = resolve_root()
        if mode == "staged":
            return cmd_staged(root)
        tip = run_git(root, "rev-parse", at_rev).strip()
        report = scan_history(root, [tip], expect_builds, tip)
        if mode == "pin":
            return print_pin_rows(report)
        if mode == "report":
            return print_detail(report, expect_builds)
        return print_report(report, expect_builds)
    except DeadProbe as exc:
        print(f"{SAY}{exc}")
        return 2
    except Problem as exc:
        print(f"{SAY}cannot run: {exc}")
        return 1
    except Exception as exc:   # noqa: BLE001 — a gate leg prints a line, never a traceback
        print(f"{SAY}cannot run: {type(exc).__name__}: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
