"""fixture_target.py — the scratch repositories govkit's fixtures build (TOOL-dSafePassage-5 S12).

One factory per kind: `build_target`, the scratch adopter target a fixture installs into, and
`build_scratch_gov`, an empty synthetic gov repository a fixture fills (TOOL-dSafePassage-26 S19),
lifted from `selftest.py`'s `build_gov17`. Callers: `selftest.py`'s arms, `upgrade_walk.py`'s
release-0 tree, and the fixtures of `upgrade_steps.py` and `fixtures/retired_edits.py`. Beside them,
the deploy-tail factory `render_deploy_tail`, a scratch deploy file's stub answers, read by
`matrix.py`'s shapes 6 and 7 and the suite's recall closure (TOOL-dTotalRecall-21 S11). A local
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
# Git's own name for a hooks directory, under the planted hooksPath and template dir: named once,
# so the plant's paths are joined from names (TOOL-dSafePassage-82 S3).
GIT_HOOKS_DIR = "hooks"


def run_git(cwd: pathlib.Path, *args: str) -> None:
    """Every call is a step of the factory's contract, so a git exit other than 0 raises `OSError`
    naming the argv, the directory and git's stderr (TOOL-dSafePassage-67 S2): a target that
    returned with no `base` would leave every arm grading an empty history."""
    env = {k: v for k, v in os.environ.items() if k not in GIT_LOCATION_VARS}
    p = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", check=False, env=env)
    if p.returncode != 0:
        raise OSError(f"git {' '.join(args)} in {cwd.as_posix()} exited {p.returncode}: "
                      f"{p.stderr.strip()}")


def build_scratch_gov(g: pathlib.Path) -> pathlib.Path:
    """`g` made an empty repository on `main`, initialised with no template, with a commit
    identity and `core.autocrlf false`, `commit.gpgsign false` and `core.hooksPath .git/hooks`
    pinned in its own config, nothing committed: the synthetic gov a fixture writes its kits into.
    Returns `g`."""
    g.mkdir(parents=True, exist_ok=True)
    # PINNED, not inherited, in the repository's own config so every later git process there reads
    # them too, the callers' own commits included (TOOL-dSafePassage-67). `core.autocrlf`:
    # DEPL-dCarriedReceipt-7 S5 lands bytes through `checkout-index`, so the TARGET's own filters
    # decide its worktree — which is the whole point, and which makes every arm asserting worktree
    # bytes depend on the DEVELOPER's global `core.autocrlf` until it is pinned here. It is `true`
    # by default on a Windows git install, and measured: eight arms asserting `b"v3\n"` went red on
    # this machine for that reason alone. The filter is still exercised, deliberately and per
    # fixture, by the clones `-7`'s own arms build with `-c core.autocrlf=true`.
    # `commit.gpgsign` and `core.hooksPath`: a developer's global signing program and global hooks
    # would otherwise refuse, hang or run inside every fixture commit; `.git/hooks` is git's own
    # default, and `--template=` keeps a global `init.templateDir` from copying hooks into it.
    for a in (("init", "-q", "--template=", "-b", "main"), ("config", "user.email", "t@e"),
              ("config", "user.name", "t"), ("config", "core.autocrlf", "false"),
              ("config", "commit.gpgsign", "false"), ("config", "core.hooksPath", ".git/hooks")):
        run_git(g, *a)
    return g


def build_target(tmp: pathlib.Path, deploy: str | None, name: str = "target",
                 files: dict | None = None) -> pathlib.Path:
    """`tmp/<name>`, a repository holding `README.md`, the `deploy` text at
    `.governance/deploy.toml` where given, and `files` ({path: text or bytes}), committed once as
    `base`."""
    t = build_scratch_gov(tmp / name)
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


#: The five answers shapes 6 and 7 fix over the stubs (PLAY-dOrderedCharter-80 S7), one constant so the
#: default install and the aged one cannot drift apart. Moved here from `matrix.py` with the two
#: functions below at their second consumer, the deployer suite's recall closure (TOOL-dTotalRecall-21 S11).
INSTALL_ANSWERS = {"memory_root": "memory", "playbook_path": "docs/PARALLEL.md", "playbook_dir": "docs",
                   "manifest_path": "docs/SESSION-KICKOFF.md", "user_skills": "~/.claude/skills"}


def derive_bullet_placeholders() -> set[str]:
    """PLAY-dOrderedCharter-81 S2, PLAY-dOrderedCharter-82 S2. The lowercased keys whose token is a
    whole line inside a one-line region of gov's charter template, as the renderer's `--bullet-keys`
    prints them. A child process, so no import edge joins the renderer's closure to this one.
    `govkit` is imported here rather than at the module's head: `upgrade_steps.py`, a `build_target`
    caller, runs inside the engine (TOOL-dTotalRecall-21 S11)."""
    import sys  # noqa: PLC0415
    import govkit  # noqa: PLC0415
    here = pathlib.Path(__file__).resolve().parent
    kd = govkit.resolve_kit_dir("playbook", "render_playbook.py", here)
    p = subprocess.run([sys.executable, str(kd / "render_playbook.py"), "--bullet-keys"], capture_output=True,
                       text=True, encoding="utf-8", stdin=subprocess.DEVNULL)
    if p.returncode:
        raise RuntimeError(f"render_playbook.py --bullet-keys exited {p.returncode}: {p.stderr.strip()}")
    return set(p.stdout.split())


def render_deploy_tail(kits, fixed: dict) -> str:
    """A scratch deploy file's tail: the `kits` line, the `[answers]` header and one stub per
    placeholder the playbook entry declares, with `fixed` over the stubs. PLAY-dOrderedCharter-80 S7.

    The answers are DERIVED from the descriptor's own placeholder rows, never listed. Every key gets
    a stub, whatever its class: for a `derived` row the probe still wins when it can see, and the stub
    is only the override the engine already honours when it cannot. A hand list here would go stale
    the first time the charter grew a placeholder. A placeholder whose token is a whole line inside a
    one-line region the render grades (aDistilledCharter) takes a `- ` bullet stub: the template,
    not the row's default, decides the bullet shape. The descriptor is read from this module's own
    directory, the deployer kit's (TOOL-dTotalRecall-21 S11)."""
    import govkit  # noqa: PLC0415
    nl = chr(10)
    pdesc = govkit.load_toml(pathlib.Path(__file__).resolve().parent / "entries" / "playbook.kit.toml")
    bullets = derive_bullet_placeholders()
    ans = {r["key"].lower(): ("- stated" if r["key"].lower() in bullets else "stated")
           for r in pdesc.get("placeholder", [])}
    ans.update(fixed)
    return ("kits = [" + ", ".join('"%s"' % k for k in kits) + "]" + nl + "[answers]" + nl
            + nl.join('%s = "%s"' % (k, v) for k, v in sorted(ans.items())) + nl)


def check_inherited_config() -> int:
    """`--selftest` (TOOL-dSafePassage-67 S3): a global config planted through `GIT_CONFIG_GLOBAL`
    signs with a failing program, points `core.hooksPath` at a canary hook and copies a canary
    hook from `init.templateDir`. Its liveness is shown on a plain, unpinned control repository
    first, so a plant that stopped biting cannot read as a pass; then `build_target` under it must
    hold `base` with no canary and no copied hook, and `run_git` must raise on a refused commit.
    Prints one line per observation; returns 0 when all hold, else 1."""
    import shutil  # noqa: PLC0415
    import sys  # noqa: PLC0415
    import tempfile  # noqa: PLC0415
    results: list[tuple[bool, str]] = []

    def add_result(ok: bool, label: str, liveness: bool = False) -> None:
        results.append((ok, label))
        print(f"fixture-target: {'ok  ' if ok else ('LIVENESS miss' if liveness else 'MISS')} "
              f"{label}")

    with tempfile.TemporaryDirectory() as td:
        d = pathlib.Path(td)
        canary = d / "canary"
        for hook, mark in ((d / GIT_HOOKS_DIR / "pre-commit", "hooks-path"),
                           (d / "tpl" / GIT_HOOKS_DIR / "pre-commit", "template")):
            hook.parent.mkdir(parents=True)
            hook.write_text(f'#!/bin/sh\nmkdir -p "{canary.as_posix()}"\n'
                            f'echo hit > "{canary.as_posix()}/{mark}"\nexit 0\n',
                            encoding="utf-8", newline="\n")
            hook.chmod(0o755)
        (d / "global").write_text(
            f'[commit]\n\tgpgsign = true\n[gpg]\n\tprogram = false\n'
            f'[core]\n\thooksPath = "{(d / GIT_HOOKS_DIR).as_posix()}"\n'
            f'[init]\n\ttemplateDir = "{(d / "tpl").as_posix()}"\n', encoding="utf-8", newline="\n")
        os.environ["GIT_CONFIG_GLOBAL"] = str(d / "global")  # run_git copies os.environ
        env = {k: v for k, v in os.environ.items() if k not in GIT_LOCATION_VARS}

        def run_env_git(cwd: pathlib.Path, *args: str) -> subprocess.CompletedProcess:
            return subprocess.run(["git", "-C", str(cwd), "-c", "user.email=t@e", "-c", "user.name=t",
                                   *args], capture_output=True, text=True, encoding="utf-8",
                                  errors="replace", check=False, env=env)

        ctl = d / "control"
        ctl.mkdir()
        run_env_git(ctl, "init", "-q")
        add_result((ctl / ".git" / "hooks" / "pre-commit").is_file(),
             "liveness: the unpinned control's init copied the template's pre-commit", True)
        p = run_env_git(ctl, "commit", "--allow-empty", "-qm", "c")
        add_result(p.returncode != 0, "liveness: the unpinned control's commit was refused "
             f"(exit {p.returncode})", True)
        add_result((canary / "hooks-path").is_file(),
             "liveness: the unpinned control's commit wrote the hooks-path canary", True)
        p = run_env_git(ctl, "-c", "commit.gpgsign=false", "commit", "--allow-empty", "-qm", "c")
        add_result(p.returncode == 0, "liveness: the control's commit with commit.gpgsign=false exits 0 "
             f"(exit {p.returncode})", True)
        shutil.rmtree(canary, ignore_errors=True)

        try:
            t = build_target(d, None)
        except OSError as e:
            add_result(False, f"build_target holds base at HEAD: it raised {e}")
        else:
            subj = run_env_git(t, "show", "-s", "--format=%s", "HEAD^{commit}").stdout.strip()
            add_result(subj == "base", f"build_target holds base at HEAD (subject {subj!r})")
            left = sorted(q.name for q in canary.glob("*")) if canary.is_dir() else []
            add_result(not left, f"no canary written under the factory's target ({left})")
            add_result(not (t / ".git" / "hooks" / "pre-commit").exists(),
                 "no .git/hooks/pre-commit copied into the factory's target")
            try:
                run_git(t, "-c", "commit.gpgsign=true", "commit", "--allow-empty", "-qm", "signed")
            except OSError as e:
                add_result("commit" in str(e), f"run_git raised OSError on the refused signed commit: {e}")
            else:
                add_result(False, "run_git raised OSError on the refused signed commit: it returned")
    held = sum(ok for ok, _ in results)
    if held == len(results):
        print(f"fixture-target: PASS · {held} of {len(results)} observations hold")
        return 0
    print(f"fixture-target: FAIL · {len(results) - held} of {len(results)} observations missed: "
          + "; ".join(label for ok, label in results if not ok), file=sys.stderr)
    return 1


if __name__ == "__main__":
    import sys
    if sys.argv[1:] != ["--selftest"]:
        sys.exit(f"usage: python {pathlib.Path(__file__).name} --selftest")
    sys.exit(check_inherited_config())
