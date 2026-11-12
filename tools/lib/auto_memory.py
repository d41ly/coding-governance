"""auto_memory — where the harness keeps a project's auto-memory (PLAY-dOrderedCharter-14 S1).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so every consumer carries the
block below INLINE, byte-identical, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy
that drifts. The copies are drift-audit's `drift_report.py`, whose dangling-pointer signal reads the
project layer's own declaration, and the playbook kit's `memory_index.py`, which passes
`AUTO_MEMORY_TEMPLATE`. The block needs `pathlib`, `re` and `subprocess` imported beside it, and the
`common_git_dir` block, `common_dir.py`'s, beside it with the `git` reader that block calls: the one common-dir
derivation, never a `rev-parse` of its own (PLAY-dOrderedCharter-49 S68).
"""
from __future__ import annotations

import pathlib
import re
import subprocess


def read_git_stdout(repo: pathlib.Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8", check=True
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


# >>> auto_memory -- canonical copy: auto_memory.py in the gov lib dir (byte-identical; gated)
#: the harness's location of a project's auto-memory; one constant, so a layout change is one edit
AUTO_MEMORY_TEMPLATE = "~/.claude/projects/{checkout}/memory"


def resolve_auto_memory_dir(root: pathlib.Path, declared: str) -> pathlib.Path | None:
    """Expand an AUTO_MEMORY_DIR declaration; None when it is blank (NOT ASKED).

    `~` is the user's home. `{checkout}` is the PRIMARY checkout's absolute path with every
    character outside `[A-Za-z0-9-]` turned into `-` — how Claude Code keys a project's
    auto-memory. The primary checkout is the parent of the common git dir, so every worktree of one
    clone reads the same directory. If git cannot answer, the token stays unexpanded and the path
    names no directory, which the signal reports as DEAD with the path it tried."""
    declared = (declared or "").strip()
    if not declared:
        return None
    if "{checkout}" in declared:
        try:   # the one common-dir derivation, the block beside this one (PLAY-dOrderedCharter-49 S68)
            common = common_git_dir(root)
        except (OSError, subprocess.CalledProcessError):
            common = None
        if common is not None:
            key = re.sub(r"[^A-Za-z0-9-]", "-", str(common.parent))
            declared = declared.replace("{checkout}", key)
    return root / pathlib.Path(declared).expanduser()
# <<< auto_memory
