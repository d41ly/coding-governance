#!/usr/bin/env python3
"""The memory-recall kit's project layer: read `.memory-tree.conf`, declare nothing of its own.

gov:kit memory-recall@1.4

The kit indexes the memory tree the memory-tree kit already declares. Two of that conf's keys are
read and no third declaration is invented:

  MEMORY_ROOT   the corpus root passed to `git ls-files` and folded into extract.DURABLE
  FAMILIES      discipline:FAMILY pairs; the uppercase FAMILY tokens are the id allowlist

The conf is REQUIRED and its absence is a refusal, not a default -- matching adopt-memory-tree.sh
and adopt-codebase-map.sh, which refuse for the same reason. This kit does not OWN the conf, so it
must not create one: the refusal names the memory-tree kit and prints a two-key stub instead. There
is deliberately no --memory-root and no --families flag anywhere in the kit; a second way to declare
the same values is the hand-kept-second-copy defect the port exists to remove.

The node-tag character class is NOT a conf key. Upstream pins `[a-f]`; the memory-tree kit's own
hygiene gate admits `node [a-z]`, so the kit takes `a-z` and adds no key.

The conf PARSER below is a copy of the twenty lines in codebase-map's map_lib.load_conf, not an
import of it: kits are copied into adopters independently, and importing across kit directories
would make memory-recall un-adoptable without codebase-map. The drift is gated by asserting this
parser against BASH sourcing the same file (selftest `conf parser == bash`), never against a second
Python parser -- two operands from one generator assert nothing.
"""

from __future__ import annotations

import hashlib
import pathlib
import re
import subprocess
import sys

# The kit never leaves bytecode in the adopter's worktree — see query.py's note.
sys.dont_write_bytecode = True

KIT_MEMORY_RECALL_VERSION = "1.4"

CONF_NAME = ".memory-tree.conf"
# a-z, per tools/memory-tree/check-memory-hygiene.sh's own `node [a-z]` (spec Q1 option (b)).
NODE_TAG_CLASS = "a-z"


class ConfError(RuntimeError):
    """The project layer is missing or unusable. Always a refusal, never a default."""


def repo_root() -> pathlib.Path:
    """The adopting repo's root, anchored on THIS FILE rather than on the cwd.

    The kit directory lives inside the adopting repo (`memory-recall/` at the root in an adopter,
    `tools/memory-recall/` in this one), so the anchor is exact from any cwd, and a throwaway-repo
    test that copies the kit in resolves to that repo rather than to wherever the runner stood.

    WALK UP FOR THE CONF RATHER THAN ASKING GIT (TOOL-aCollapsedScan-7), which is the choice
    `tools/codebase-map/map_lib.py`'s `resolve_root` already made for the same measured reason,
    and which `tools/govkit/govkit.py` reached for the same defect WITHOUT the boundary - its walk
    is still unbounded, which is `TOOL-aCollapsedScan-12`. `git -C <dir> rev-parse
    --show-toplevel` returns <dir> ITSELF when an absolute GIT_DIR is inherited and no
    GIT_WORK_TREE names a tree, because git then treats the current directory as the work tree.
    That is exactly what git exports to a merge driver inside a LINKED WORKTREE, and it is how the
    row-keyed merge driver was found inert here: this function answered `<root>/tools/memory-recall`,
    `resolve()` looked for the conf beside the kit, `extract.py`'s import-time CONF raised, and
    every `memory/DECISIONS.md` and `memory/backlog/*.md` merge got conflict markers instead of a
    merge. Measured with a control: in an ordinary clone git exports no GIT_DIR and the defect is
    ABSENT, so the precondition is the worktree and not the merge.

    THE ALTERNATIVE WAS AN ENVIRONMENT SCRUB and it lost on being a DENYLIST. `.githooks/pre-push`
    already pins eight names for that job under `TOOL-dScrubbedConduit-1`, with one deliberate
    exclusion; a second list here would be a ninth thing to keep current. The walk inherits nothing.

    THEY DO NOT ALWAYS COINCIDE, and an earlier revision of this docstring said they did. The
    nearest conf-holding ancestor is deliberately NOT the answer once a `.git` boundary intervenes -
    see the walk below, which is where that rule lives. Where no boundary intervenes the two agree,
    because `resolve()` refuses a root that does not hold `.memory-tree.conf`.
    """
    here = pathlib.Path(__file__).resolve()
    for parent in here.parents:
        # THE WALK STOPS AT THE REPOSITORY BOUNDARY, which `tools/codebase-map/map_lib.py`'s
        # `resolve_root` already pays two lines for and records the reason: worktrees are commonly
        # kept INSIDE the primary tree (this repo puts them under `.claude/worktrees/`), so an
        # UNBOUNDED walk out of a checkout reaches the PRIMARY tree's conf and answers with a
        # different repository. Reproduced during this unit's own closing review: with a conf at
        # `outer/` and a separate repo at `outer/inner/` holding the kit, an unbounded walk answered
        # `outer` and `resolve()` succeeded against a FOREIGN conf, where the pre-fix code refused.
        # `.git` is a directory in a primary tree and a FILE in a linked worktree, so one
        # `exists()` covers both.
        #
        # THE CONF IS TESTED FIRST, so an adopted root that holds both still wins on its own line.
        # Falling out of the loop hands the question to the git probe below, which is what raises
        # the not-a-git-repository refusal for a conf-bearing tree that is not a checkout at all.
        if (parent / CONF_NAME).is_file() and (parent / ".git").exists():
            return parent
        if (parent / ".git").exists():
            break
    # NO USABLE CONF ON THE WALK - none at all, or one only beyond the repository boundary. Keep
    # the old git answer, so `resolve()` raises ITS refusal - the one
    # carrying the copy-pasteable conf stub an adopter needs. This is NOT a fallback that
    # fabricates a passing value: the path it returns is by definition one with no conf on it, so
    # `resolve()` refuses on the very next line. It also cannot mask the defect above, because that
    # defect only reaches a tree where a conf DOES exist and the walk-up therefore wins first.
    here = here.parent
    try:
        out = subprocess.run(
            ["git", "-C", str(here), "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
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
        value = value.strip()
        if value[:1] in {'"', "'"} and value[-1:] == value[:1] and len(value) >= 2:
            value = value[1:-1]
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

# The default cache budget, MEASURED on this tree rather than inherited: one cache here is 2.4 MB,
# and upstream measured ~110 MB per LIVE worktree on a far larger corpus. 512 sits well above any
# plausible single-corpus cache, so the cap protects an adopter carrying many worktrees without ever
# firing on a normal one. Blank in the conf = uncapped; absent = this.
DEFAULT_CACHE_BUDGET_MB = 512.0


def _budget(raw: str | None) -> float | None:
    """`RECALL_CACHE_BUDGET_MB` -> megabytes, or None for uncapped.

    A BLANK value disables the cap, matching every other knob in this tree. An unparseable one also
    disables it rather than raising: this is a housekeeping limit, and refusing to answer a question
    because a size limit is misspelled would be a worse failure than not evicting.
    """
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


class Conf:
    """The RESOLVED values every other module in the kit reads."""

    __slots__ = ("root", "path", "memory_root", "families", "node_tag_class", "cache_budget_mb",
                 "extra_sources")

    def __init__(self, root: pathlib.Path, memory_root: str, families: tuple[str, ...],
                 cache_budget_mb: float | None = DEFAULT_CACHE_BUDGET_MB,
                 extra_sources: tuple[str, ...] = ()):
        self.root = root
        self.path = root / CONF_NAME
        self.memory_root = memory_root
        self.families = families
        self.node_tag_class = NODE_TAG_CLASS
        # None = uncapped, which is what a BLANK value means — the same convention as every other
        # measured knob in this tree. It is deliberately NOT part of digest(): a size limit is not a
        # corpus input, and folding it in would rebuild every cache whenever someone raised the cap.
        self.cache_budget_mb = cache_budget_mb
        # DECLARED extra corpus sources, repo-relative. Empty is the pre-widening corpus
        # exactly, which is what an adopter whose conf has no such key must keep getting.
        self.extra_sources = extra_sources

    def digest(self) -> str:
        """A hash of the RESOLVED values, not of the conf file's bytes.

        The manifest keys freshness on this (query.ensure_cache), so an id-grammar or corpus-root
        edit invalidates a warm cache the way an alias edit already does. Hashing the file's bytes
        instead would force a full rebuild for a comment edit, for no semantic change.

        THE KIT VERSION IS IN THE BLOB, and it is here because the sentence above was half false. The
        eras are the other half of the id grammar and they live in `extract.py`, so a widening of the
        session era reached none of the three project values below. Measured on the commit that
        widened it: `records` went 53 documents to 91 and every already-built cache stayed warm and
        stayed blind to the 38 new ones. `corpus_digest` cannot cover it either — that is mtime+size
        over the tree's `.md` files, and a regex edit moves no `.md` byte.

        The VERSION rather than the era tuple, on two grounds. It is already this kit's declared
        epoch for its own behaviour and `check-kit-versions.sh` plus the selftest's marker arm force
        it to move when the kit's behaviour does. And passing the resolved eras down would invert the
        layering: `extract` imports `recall_conf`, not the other way round. The cost is one rebuild
        per kit bump, which is the same order as the alias-edit rebuild already accepted above.
        """
        # `extra_sources` is in the blob for the same reason the kit version is: it changes WHICH
        # documents exist, so a widened or narrowed list must not read a cache built before it.
        # Measured: without it, editing the declaration left the index warm and the corpus stale,
        # so both arms proving the widening is opt-in were answered by a cached number.
        blob = "\0".join((self.memory_root, ",".join(sorted(self.families)), self.node_tag_class,
                          " ".join(self.extra_sources), KIT_MEMORY_RECALL_VERSION))
        return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:12]


_cached: Conf | None = None


def resolve(root: pathlib.Path | None = None) -> Conf:
    """The kit's project layer, or a ConfError carrying the printable refusal.

    Cached per process: every module in the kit calls this at import. It no longer costs a
    `git rev-parse` on any path where a conf exists - `repo_root()` walks for it - but the call
    frequency is what justified the cache and that has not changed.
    """
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
    out = Conf(base, memory_root, families, _budget(conf.get("RECALL_CACHE_BUDGET_MB")),
               tuple(conf.get("RECALL_EXTRA_SOURCES", "").split()))
    if root is None:
        _cached = out
    return out


def main() -> int:
    """Print the resolved project layer as KEY=VALUE, or the refusal on stderr.

    ONE home for the refusal text: adopt-memory-recall.sh shells out to this rather than restating
    it, so the CLI and the adopt script cannot drift on what a missing conf says (AC3).

    The KEY=VALUE lines are a MACHINE-READABLE protocol (adopt-memory-recall.sh parses them with
    `read`), so the newline is part of the contract. On Windows, text-mode stdout translated every
    \\n to \\r\\n and each value reached the shell carrying a trailing CR — which rendered into
    SKILL.md as `memory\\r/` and `(PLAY KICK TOOL DEPL\\r)`, breaking its YAML frontmatter outright.
    Pin LF so the protocol is byte-identical on every OS.
    """
    try:
        sys.stdout.reconfigure(newline="\n")
    except (AttributeError, ValueError):  # a replaced or non-TextIOWrapper stdout
        pass
    try:
        c = resolve()
    except ConfError as e:
        print(e, file=sys.stderr)
        return 2
    print(f"ROOT={c.root.as_posix()}")
    print(f"MEMORY_ROOT={c.memory_root}")
    print(f"FAMILIES={' '.join(c.families)}")
    print(f"NODE_TAG_CLASS={c.node_tag_class}")
    print(f"CONF_DIGEST={c.digest()}")
    print(f"KIT_VERSION={KIT_MEMORY_RECALL_VERSION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
