#!/usr/bin/env python3
"""selftest.py — the branch-reconcile kit's self-test. Withheld from adopters (kit.toml).

    python <this kit>/selftest.py

Every fixture is a repository built under a fresh temporary directory, with the caller's git
environment held out: `GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE` are dropped, a private global
config replaces the user's, and `GIT_CEILING_DIRECTORIES` stops discovery at the fixture root. The
remote is named `upstream`, never `origin`, because one adopter node's is not.

Prints `branch-reconcile: <n> passed, <m> failed (<t> assertions, floor <f>)` and exits 1 on any
failure or when fewer assertions ran than the floor.
"""
from __future__ import annotations

import importlib.util
import io
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout

HERE = pathlib.Path(__file__).resolve().parent
CLI = HERE / "branch_reconcile.py"
ASSERTION_FLOOR = 14
PASS, FAIL = [], []
SCRATCH = []


def load_module():
    spec = importlib.util.spec_from_file_location("branch_reconcile", CLI)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


BR = load_module()


def check(name, got, want):
    if got == want:
        PASS.append(name)
    else:
        FAIL.append(name)
        print(f"FAIL {name}\n  got:  {got!r}\n  want: {want!r}")


def seed_env(base):
    """A git environment that reads nothing of the caller's."""
    env = {k: v for k, v in os.environ.items()
           if not k.startswith("GIT_") and k not in ("GOV_REMOTE", "GOV_DEFAULT_BRANCH")}
    cfg = pathlib.Path(base) / "gitconfig"
    cfg.write_text("[user]\n\tname = Fixture\n\temail = fixture@example.invalid\n"
                   "[init]\n\tdefaultBranch = main\n[core]\n\tautocrlf = false\n"
                   "[protocol \"file\"]\n\tallow = always\n[advice]\n\tdetachedHead = false\n",
                   encoding="utf-8")
    env.update({"GIT_CONFIG_GLOBAL": str(cfg), "GIT_CONFIG_NOSYSTEM": "1",
                "GIT_CEILING_DIRECTORIES": str(pathlib.Path(base).parent)})
    return env


ENV = {}


def run_git(cwd, *args, ok=True):
    p = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=ENV)
    if ok and p.returncode != 0:
        raise RuntimeError(f"fixture: git {' '.join(args)} in {cwd} failed: {p.stderr.strip()}")
    return p.stdout.strip()


def seed_commit(repo, rel, text, msg):
    p = pathlib.Path(repo) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")
    run_git(repo, "add", "--", rel)
    run_git(repo, "commit", "-q", "-m", msg)
    return run_git(repo, "rev-parse", "HEAD")


def build_dir():
    d = tempfile.mkdtemp(prefix="br-selftest-")
    SCRATCH.append(d)
    return pathlib.Path(d)


def seed_repo(base):
    """A clone at <base>/fx/repo with one commit on main and a bare remote named `upstream`."""
    repo = base / "fx" / "repo"
    repo.mkdir(parents=True)
    run_git(repo, "init", "-q", "-b", "main")
    seed_commit(repo, "a.txt", "a1\n", "seed: a")
    seed_commit(repo, "b.txt", "b1\n", "seed: b")
    run_git(base, "clone", "-q", "--bare", str(repo), str(base / "remote.git"))
    run_git(repo, "remote", "add", "upstream", str(base / "remote.git"))
    run_git(repo, "fetch", "-q", "upstream")
    run_git(repo, "remote", "set-head", "upstream", "main")
    return repo


def run_cli(root, *args, env=None):
    p = subprocess.run([sys.executable, str(CLI), "--root", str(root), *args], capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=env or ENV)
    return p.returncode, p.stdout, p.stderr


def read_rows(out):
    """-> {(kind, name): fields} from a report's row lines."""
    rows = {}
    for line in out.splitlines():
        f = line.split(" · ")
        if len(f) >= 8 and f[0] in BR.VERDICT_RANK:
            rows[(f[1], f[2])] = f[:7] + [" · ".join(f[7:])]
    return rows


def arm_census():
    """TOOL-dSweptBranches-1 AC1 to AC5."""
    base = build_dir()
    repo = seed_repo(base)
    sub_src = base / "subsrc"
    sub_src.mkdir()
    run_git(sub_src, "init", "-q", "-b", "main")
    seed_commit(sub_src, "s.txt", "s\n", "sub: seed")
    run_git(repo, "submodule", "-q", "add", str(sub_src), "sub")
    run_git(repo, "commit", "-q", "-m", "seed: submodule")
    run_git(repo, "push", "-q", "upstream", "main")
    run_git(repo, "fetch", "-q", "upstream")
    seed_commit(repo, "d.txt", "d\n", "feature a")
    run_git(repo, "branch", "feature-a")
    seed_commit(repo, "c.txt", "c\n", "local only")
    run_git(repo, "branch", "feature-b")
    run_git(repo, "reset", "-q", "--hard", "upstream/main")
    run_git(repo, "push", "-q", "upstream", "feature-a")
    run_git(repo, "fetch", "-q", "upstream")
    run_git(repo, "worktree", "add", "-q", "-b", "nest-br", str(repo / ".claude" / "worktrees" / "nest"),
        "main")
    sib = base / "fx" / "sib"
    run_git(repo, "worktree", "add", "-q", "-b", "sib-br", str(sib), "main")
    tmp_wt = build_dir() / "wt"
    run_git(repo, "worktree", "add", "-q", "-b", "tmp-br", str(tmp_wt), "main")
    det = base / "fx" / "det"
    run_git(repo, "worktree", "add", "-q", "--detach", str(det), "main")
    gone = base / "fx" / "gone"
    run_git(repo, "worktree", "add", "-q", "-b", "gone-br", str(gone), "main")
    shutil.rmtree(gone)
    # dirt: staged, unstaged and untracked in the sibling; a merge in progress in the detached one
    (sib / "a.txt").write_text("a2\n", encoding="utf-8", newline="\n")
    run_git(sib, "add", "a.txt")
    (sib / "b.txt").write_text("b2\n", encoding="utf-8", newline="\n")
    (sib / "new.txt").write_text("n\n", encoding="utf-8", newline="\n")
    run_git(det, "merge", "-q", "--no-ff", "--no-commit", "feature-a")
    # a stash entry, then submodule-pointer drift in the primary
    (repo / "a.txt").write_text("stashed\n", encoding="utf-8", newline="\n")
    run_git(repo, "stash", "push", "-q", "-m", "fixture stash")
    run_git(repo / "sub", "commit", "-q", "--allow-empty", "-m", "sub: drift")

    rc, out, err = run_cli(repo)
    check("census: the report exits 0", (rc, err), (0, ""))
    rows = read_rows(out)
    kinds = sorted((k, n) for (k, n) in rows if k.startswith("worktree/"))
    check("census: one row per worktree, each with its location kind", kinds, sorted([
        ("worktree/primary", str(repo).replace("\\", "/")),
        ("worktree/nested", ".claude/worktrees/nest"),
        ("worktree/sibling", str(sib).replace("\\", "/")),
        ("worktree/sibling", str(det).replace("\\", "/")),
        ("worktree/sibling", str(gone).replace("\\", "/")),
        ("worktree/temp", str(tmp_wt).replace("\\", "/"))]))
    check("census: the detached worktree is flagged and its merge is read",
          ["detached" in rows[("worktree/sibling", str(det).replace("\\", "/"))][7],
           "merging " in rows[("worktree/sibling", str(det).replace("\\", "/"))][7]], [True, True])
    check("census: the prunable worktree is flagged and its status is not read",
          rows[("worktree/sibling", str(gone).replace("\\", "/"))][7].startswith(
              "prunable · status not read"), True)
    sib_ev = rows[("worktree/sibling", str(sib).replace("\\", "/"))][7]
    check("census: the sibling's staged, unstaged and untracked counts",
          ["staged 1" in sib_ev, "unstaged 1" in sib_ev, "untracked 1" in sib_ev], [True] * 3)
    prim_ev = rows[("worktree/primary", str(repo).replace("\\", "/"))][7]
    check("census: the primary's submodule-pointer drift", "submodule drift 1" in prim_ev, True)
    check("census: AC4 the nested worktree is not the primary's untracked content",
          "untracked" in prim_ev, False)
    refs = sorted((k, n) for (k, n) in rows if k in ("local", "remote", "stash"))
    check("census: every local, upstream and stash ref", refs, sorted([
        ("local", "main"), ("local", "feature-a"), ("local", "feature-b"), ("local", "nest-br"),
        ("local", "sib-br"), ("local", "tmp-br"), ("local", "gone-br"), ("remote", "upstream/main"),
        ("remote", "upstream/feature-a"), ("stash", "stash@{0}")]))
    check("census: the header names upstream/main and the counts",
          out.splitlines()[0].split(" at ")[0] + " · " + out.splitlines()[0].split(" · ", 1)[1],
          "branch-reconcile — upstream/main · 6 worktree(s) · 7 local · 2 remote · 1 stash")

    # AC2 — byte-stable
    rc2, out2, _ = run_cli(repo)
    check("census: AC2 two runs over the unchanged fixture print the same bytes", out2, out)

    # AC3 — the ladder
    env = dict(ENV, GOV_REMOTE="nope")
    rc, _out, err = run_cli(repo, env=env)
    check("census: AC3 GOV_REMOTE naming no remote refuses with exit 2", (rc, "GOV_REMOTE" in err),
          (2, True))
    run_git(repo, "remote", "add", "other", str(base / "remote.git"))
    rc, _out, err = run_cli(repo)
    check("census: AC3 two remotes and none chosen refuses with exit 2",
          (rc, "GOV_REMOTE" in err), (2, True))
    run_git(repo, "remote", "remove", "other")

    # AC5 — the seam: with no predicate, every row is UNKNOWN
    saved = BR.PREDICATES[:]
    BR.PREDICATES[:] = []
    try:
        inv = BR.read_inventory(repo)
        verdicts = {r["verdict"] for r in BR.build_rows(inv)}
        evidence = all("no predicate decided" in r["evidence"] for r in BR.build_rows(inv))
    finally:
        BR.PREDICATES[:] = saved
    check("census: AC5 with no predicate every row reads UNKNOWN", (verdicts, evidence),
          ({BR.UNKNOWN}, True))

    # a directory that is no repository refuses
    rc, _out, err = run_cli(build_dir(), env=ENV)
    check("census: a directory that is no repository refuses with exit 2", rc, 2)


ARMS = [arm_census]


def main():
    global ENV
    root = build_dir()
    ENV = seed_env(root)
    try:
        for arm in ARMS:
            try:
                arm()
            except Exception as exc:  # an arm that raised is one failure, named, and the rest run
                FAIL.append(f"{arm.__name__} raised")
                print(f"FAIL {arm.__name__} raised {type(exc).__name__}: {exc}")
    finally:
        for d in SCRATCH:
            shutil.rmtree(d, ignore_errors=True)
    total = len(PASS) + len(FAIL)
    print(f"branch-reconcile: {len(PASS)} passed, {len(FAIL)} failed "
          f"({total} assertions, floor {ASSERTION_FLOOR})")
    if total < ASSERTION_FLOOR:
        print(f"branch-reconcile: FAIL the suite executed {total} assertions, under its floor of "
              f"{ASSERTION_FLOOR} — an arm went missing", file=sys.stderr)
        return 1
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())
