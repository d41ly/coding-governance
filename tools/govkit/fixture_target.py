"""fixture_target.py — the scratch repositories govkit's fixtures build (TOOL-dSafePassage-5 S12).

One factory per kind: `build_target`, the scratch adopter target a fixture installs into, and
`build_scratch_gov`, an empty synthetic gov repository a fixture fills (TOOL-dSafePassage-26 S19),
lifted from `selftest.py`'s `build_gov17`. Callers: `selftest.py`'s arms, `upgrade_walk.py`'s
release-0 tree, and the fixtures of `upgrade_steps.py` and `fixtures/retired_edits.py`. A local
helper that calls a factory takes a name of its own, since a local binding of the factory's name
calling it calls itself.
"""
from __future__ import annotations

import os
import pathlib
import subprocess

# A calling hook's location variables would point every fixture git call at another repository.
GIT_LOCATION_VARS = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_OBJECT_DIRECTORY",
                     "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_COMMON_DIR", "GIT_NAMESPACE", "GIT_PREFIX")


def run_git(cwd: pathlib.Path, *args: str) -> None:
    env = {k: v for k, v in os.environ.items() if k not in GIT_LOCATION_VARS}
    subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, encoding="utf-8",
                   errors="replace", check=False, env=env)


def build_scratch_gov(g: pathlib.Path) -> pathlib.Path:
    """`g` made an empty repository on `main` with a commit identity and `core.autocrlf` pinned
    false, nothing committed: the synthetic gov a fixture writes its kits into. Returns `g`."""
    g.mkdir(parents=True, exist_ok=True)
    for a in (("init", "-q", "-b", "main"), ("config", "user.email", "t@e"),
              ("config", "user.name", "t"), ("config", "core.autocrlf", "false")):
        run_git(g, *a)
    return g


def build_target(tmp: pathlib.Path, deploy: str | None, name: str = "target",
                 files: dict | None = None) -> pathlib.Path:
    """`tmp/<name>`, a repository holding `README.md`, the `deploy` text at
    `.governance/deploy.toml` where given, and `files` ({path: text or bytes}), committed once as
    `base`."""
    t = build_scratch_gov(tmp / name)
    # PINNED, not inherited (the factory's `core.autocrlf` above). DEPL-dCarriedReceipt-7 S5 lands
    # bytes through `checkout-index`, so the TARGET's own filters decide its worktree — which is the
    # whole point, and which makes every arm asserting worktree bytes depend on the DEVELOPER's
    # global `core.autocrlf` until it is pinned here. It is `true` by default on a Windows git
    # install, and measured: eight arms asserting `b"v3\n"` went red on this machine for that
    # reason alone. The filter is still exercised, deliberately and per fixture, by the clones
    # `-7`'s own arms build with `-c core.autocrlf=true`.
    (t / "README.md").write_text("target\n", encoding="utf-8")
    if deploy is not None:
        gov = t / ".governance"
        gov.mkdir(exist_ok=True)
        (gov / "deploy.toml").write_text(deploy, encoding="utf-8", newline="\n")
    for rel, body in (files or {}).items():
        (t / rel).parent.mkdir(parents=True, exist_ok=True)
        (t / rel).write_bytes(body if isinstance(body, bytes) else body.encode("utf-8"))
    run_git(t, "add", "-A")
    run_git(t, "commit", "-qm", "base")
    return t
