"""common_dir — the main repository's git directory, shared by every worktree (PLAY-dOrderedCharter-19 S10).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy
that drifts. The copies are the recall kit's `query.py`, whose query log lives there, and the playbook
kit's `tag_index.py`, whose `gov/index-s<INDEX_SCHEMA>.db` does. The block calls `git(repo, *args)`, a one-call stdout
reader each consumer binds beside it; this module binds its own.
"""
from __future__ import annotations

import pathlib
import subprocess


def read_git_stdout(repo: pathlib.Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", check=True
    ).stdout


git = read_git_stdout  # the name the block below calls


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
