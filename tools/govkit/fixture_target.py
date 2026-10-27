"""fixture_target.py — the scratch adopter target govkit's fixtures install into (TOOL-dSafePassage-5 S12).

One factory, two callers: `selftest.py`'s arms and `upgrade_walk.py`'s release-0 tree. Moved here
unchanged from `selftest.py` at its second caller, as the charter's factory rule asks.
"""
from __future__ import annotations

import pathlib
import subprocess


def run_git(cwd: pathlib.Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, encoding="utf-8",
                   errors="replace", check=False)


def build_target(tmp: pathlib.Path, deploy: str | None) -> pathlib.Path:
    t = tmp / "target"
    t.mkdir(parents=True, exist_ok=True)
    run_git(t, "init", "-q", "-b", "main")
    run_git(t, "config", "user.email", "t@e")
    run_git(t, "config", "user.name", "t")
    # PINNED, not inherited. DEPL-dCarriedReceipt-7 S5 lands bytes through `checkout-index`, so the
    # TARGET's own filters decide its worktree — which is the whole point, and which makes every
    # arm asserting worktree bytes depend on the DEVELOPER's global `core.autocrlf` until it is
    # pinned here. It is `true` by default on a Windows git install, and measured: eight arms
    # asserting `b"v3\n"` went red on this machine for that reason alone. The filter is still
    # exercised, deliberately and per fixture, by the clones `-7`'s own arms build with
    # `-c core.autocrlf=true`.
    run_git(t, "config", "core.autocrlf", "false")
    (t / "README.md").write_text("target\n", encoding="utf-8")
    if deploy is not None:
        gov = t / ".governance"
        gov.mkdir(exist_ok=True)
        (gov / "deploy.toml").write_text(deploy, encoding="utf-8", newline="\n")
    run_git(t, "add", "-A")
    run_git(t, "commit", "-qm", "base")
    return t
