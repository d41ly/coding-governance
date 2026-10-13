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

import contextlib
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
ASSERTION_FLOOR = 59
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


def seed_commit(repo, rel, text, msg, when=None):
    """Write <rel>, commit it, and return the sha. <when> backdates the commit (git date syntax)."""
    p = pathlib.Path(repo) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8", newline="\n")
    run_git(repo, "add", "--", rel)
    if when:
        p = subprocess.run(["git", "-C", str(repo), "commit", "-q", "-m", msg], capture_output=True,
                           text=True, env=dict(ENV, GIT_AUTHOR_DATE=when, GIT_COMMITTER_DATE=when))
        if p.returncode != 0:
            raise RuntimeError(f"fixture: backdated commit failed: {p.stderr.strip()}")
    else:
        run_git(repo, "commit", "-q", "-m", msg)
    return run_git(repo, "rev-parse", "HEAD")


def seed_publish(repo):
    """Push main to `upstream` and fetch, so upstream/main is the default tip the report grades."""
    run_git(repo, "push", "-q", "upstream", "main")
    run_git(repo, "fetch", "-q", "upstream")


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


def read_report(repo, *args):
    rc, out, err = run_cli(repo, *args)
    if rc != 0:
        raise RuntimeError(f"report exited {rc}: {err.strip()}")
    return read_rows(out)


def read_verdict(rows, kind, name):
    row = rows.get((kind, name))
    return (row[0], row[7]) if row else ("absent", "")


def seed_lines(n, tag=""):
    return "".join(f"line {i}{tag}\n" for i in range(n))


def arm_patch():
    """TOOL-dSweptBranches-2 AC1 — a rebased copy that drifted by one and two lines per patch."""
    repo = seed_repo(build_dir())
    run_git(repo, "checkout", "-q", "-b", "rebased")
    seed_commit(repo, "one.txt", seed_lines(6), "feat: one")
    seed_commit(repo, "two.txt", seed_lines(8), "feat: two")
    run_git(repo, "checkout", "-q", "main")
    seed_commit(repo, "other.txt", "o\n", "unrelated")
    seed_commit(repo, "one.txt", seed_lines(5) + "line 5 drifted\n", "feat: one")
    seed_commit(repo, "two.txt", seed_lines(6) + "line 6 drifted\nline 7 drifted\n", "feat: two")
    seed_publish(repo)
    cherry = run_git(repo, "cherry", "upstream/main", "rebased").split()
    check("patch: git cherry misses both rebased copies", cherry.count("+"), 2)
    verdict, ev = read_verdict(read_report(repo, "--fresh-hours", "0"), "local", "rebased")
    check("patch: AC1 the rebased copy reads SUPERSEDED by patch", (verdict, "patch 2" in ev),
          ("SUPERSEDED", True))


def arm_landing():
    """AC2 — a pre-fold variant whose later landing merge touched every file it did."""
    repo = seed_repo(build_dir())
    run_git(repo, "checkout", "-q", "-b", "prefold")
    (repo / "y.md").write_text("draft\n", encoding="utf-8", newline="\n")
    seed_commit(repo, "x.py", "x = 1\n", "build(dFoo): TOOL-dFoo-1 — the thing")
    run_git(repo, "add", "y.md")
    run_git(repo, "commit", "-q", "--amend", "--no-edit")
    run_git(repo, "checkout", "-q", "-b", "folded", "main")
    (repo / "y.md").write_text("folded\n", encoding="utf-8", newline="\n")
    seed_commit(repo, "x.py", "x = 2\n", "build(dFoo): TOOL-dFoo-1 — the thing, folded")
    run_git(repo, "add", "y.md")
    run_git(repo, "commit", "-q", "--amend", "--no-edit")
    seed_commit(repo, "z.txt", "z\n", "records(dFoo): ledger")
    run_git(repo, "checkout", "-q", "main")
    run_git(repo, "merge", "-q", "--no-ff", "-m", "merge: dFoo — land onto upstream/main", "folded")
    run_git(repo, "branch", "-q", "-D", "folded")
    seed_publish(repo)
    verdict, ev = read_verdict(read_report(repo, "--fresh-hours", "0"), "local", "prefold")
    check("landing: AC2 the pre-fold variant reads SUPERSEDED by its landing merge",
          (verdict, "landing 1" in ev, "no-op" in ev), ("SUPERSEDED", True, False))


def arm_records():
    """AC3 — a run-records-only commit for a build the default branch shows landed."""
    repo = seed_repo(build_dir())
    run_git(repo, "checkout", "-q", "-b", "records")
    seed_commit(repo, "memory/builds/dBar/RUN.md", "phase: VERIFYING\n", "records(dBar): verifying")
    run_git(repo, "checkout", "-q", "main")
    seed_commit(repo, "memory/builds/dBar/RUN.md", "phase: LANDED\n", "records(dBar): landed")
    seed_publish(repo)
    verdict, ev = read_verdict(read_report(repo, "--fresh-hours", "0"), "local", "records")
    check("records: AC3 a records-only commit for a landed build reads SUPERSEDED",
          (verdict, "records 1" in ev), ("SUPERSEDED", True))


def arm_rotated():
    """AC4 — a decision row the default branch keeps only in an archive."""
    repo = seed_repo(build_dir())
    seed_commit(repo, "memory/DECISIONS.md", "# decisions\n", "seed: decisions")
    seed_publish(repo)
    run_git(repo, "checkout", "-q", "-b", "rotated")
    seed_commit(repo, "memory/DECISIONS.md", "# decisions\n- TOOL-dBaz-3 · the rotated ruling\n",
                "records(dBaz): a decision row")
    run_git(repo, "checkout", "-q", "main")
    seed_commit(repo, "memory/archive/DECISIONS-2026-09.md", "- TOOL-dBaz-3 · the rotated ruling\n",
                "rotate: decisions")
    seed_publish(repo)
    # The negative, found on gov's own tree while this predicate was built: a spec rewrite whose
    # prose CITES ids the default branch holds is content of its own, never a rotated row.
    run_git(repo, "checkout", "-q", "-b", "cites", "main")
    seed_commit(repo, "memory/builds/dBaz/spec.md",
                "# spec\n\nThis rewrite cites TOOL-dBaz-3 and adds a design of its own.\n",
                "spec(dBaz): rev-2")
    run_git(repo, "checkout", "-q", "main")
    rows = read_report(repo, "--fresh-hours", "0")
    verdict, ev = read_verdict(rows, "local", "rotated")
    check("rotated: AC4 a row kept only in the archive reads SUPERSEDED",
          (verdict, "rotated 1" in ev), ("SUPERSEDED", True))
    check("rotated: AC4 prose citing an id the default holds is not a rotated row",
          read_verdict(rows, "local", "cites")[0], "UNMERGED-LIVE")


def arm_noop():
    """AC5 — a net-zero branch is proven by merge-tree; a conflicting one is never."""
    repo = seed_repo(build_dir())
    run_git(repo, "checkout", "-q", "-b", "netzero")
    seed_commit(repo, "a.txt", "a1\nextra\n", "try: a line")
    seed_commit(repo, "a.txt", "a1\n", "revert: the line")
    run_git(repo, "checkout", "-q", "-b", "clash", "main")
    seed_commit(repo, "b.txt", "mine\n", "clash: b")
    run_git(repo, "checkout", "-q", "main")
    seed_commit(repo, "b.txt", "theirs\n", "main: b")
    seed_publish(repo)
    rows = read_report(repo, "--fresh-hours", "0")
    verdict, ev = read_verdict(rows, "local", "netzero")
    check("noop: AC5 a net-zero branch reads SUPERSEDED by the merge-tree proof",
          (verdict, "no-op" in ev), ("SUPERSEDED", True))
    check("noop: AC5 a conflicting branch is never superseded by merge-tree",
          read_verdict(rows, "local", "clash")[0], "UNMERGED-LIVE")


def arm_lease():
    """AC6 — a live run lease is IN-PROGRESS; a stale lease on an old tip is not."""
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc)
    fresh = (now - datetime.timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%SZ")
    stale = (now - datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    old = (now - datetime.timedelta(days=10)).strftime("%Y-%m-%dT%H:%M:%S+0000")
    repo = seed_repo(build_dir())
    run_git(repo, "checkout", "-q", "-b", "leased")
    seed_commit(repo, "memory/builds/dQux/RUN.md", f"phase: BUILDING\nlease-utc: {fresh}\n",
                "records(dQux): preflight", when=old)
    run_git(repo, "checkout", "-q", "-b", "stale-lease", "main")
    seed_commit(repo, "memory/builds/dQuy/RUN.md", f"phase: BUILDING\nlease-utc: {stale}\n",
                "records(dQuy): preflight", when=old)
    run_git(repo, "checkout", "-q", "-b", "live-work", "main")
    seed_commit(repo, "feature.py", "print('unlanded')\n", "feat: the unlanded fix", when=old)
    run_git(repo, "checkout", "-q", "main")
    rows = read_report(repo)
    check("lease: AC6 a live run lease reads IN-PROGRESS", read_verdict(rows, "local", "leased")[0],
          "IN-PROGRESS")
    check("lease: AC6 a stale lease on an old tip is not IN-PROGRESS",
          read_verdict(rows, "local", "stale-lease")[0], "UNMERGED-LIVE")
    check("lease: AC6 the unlanded fix reads UNMERGED-LIVE",
          read_verdict(rows, "local", "live-work")[0], "UNMERGED-LIVE")
    check("lease: AC6 the unlanded fix's evidence names its uncovered commit",
          "uncovered" in read_verdict(rows, "local", "live-work")[1], True)


def arm_content():
    """AC7 — worktree content: a landed merge, a landed probe, an uncovered file, and freshness."""
    base = build_dir()
    repo = seed_repo(base)
    old_main = run_git(repo, "rev-parse", "main")
    run_git(repo, "checkout", "-q", "-b", "side")
    seed_commit(repo, "side.txt", "side\n", "feat: side")
    run_git(repo, "checkout", "-q", "main")
    seed_commit(repo, "tests/test_land.py",
                "import os\n\n\ndef test_merge_survives():\n    assert True\n", "test: landed")
    run_git(repo, "merge", "-q", "--no-ff", "-m", "merge: side", "side")
    seed_publish(repo)
    det = base / "fx" / "det"
    run_git(repo, "worktree", "add", "-q", "--detach", str(det), old_main)
    run_git(det, "merge", "-q", "--no-ff", "--no-commit", "side")
    probe = base / "fx" / "probe"
    run_git(repo, "worktree", "add", "-q", "-b", "probe-br", str(probe), "main")
    (probe / "tests").mkdir(exist_ok=True)
    (probe / "tests" / "test_probe.py").write_text("def test_merge_survives():\n    assert True\n",
                                                   encoding="utf-8", newline="\n")
    live = base / "fx" / "live"
    run_git(repo, "worktree", "add", "-q", "-b", "live-br", str(live), "main")
    (live / "notes.txt").write_text("only here\n", encoding="utf-8", newline="\n")
    nest = repo / ".claude" / "worktrees" / "nest"
    run_git(repo, "worktree", "add", "-q", "-b", "nest-br", str(nest), "main")
    tmp_wt = build_dir() / "wt"
    run_git(repo, "worktree", "add", "-q", "-b", "tmp-br", str(tmp_wt), "main")
    rows = read_report(repo, "--fresh-hours", "0")
    key = lambda p: str(p).replace("\\", "/")
    det_v, det_ev = read_verdict(rows, "worktree/sibling", key(det))
    check("content: AC7 the detached worktree's in-progress merge landed",
          (det_v, "the merge's other side" in det_ev), ("MERGED", True))
    probe_v, probe_ev = read_verdict(rows, "worktree/sibling", key(probe))
    check("content: AC7 the probe whose case landed as a test is covered",
          (probe_v, "its case landed as a test" in probe_ev), ("MERGED", True))
    check("content: AC7 an uncovered untracked file reads UNMERGED-LIVE",
          read_verdict(rows, "worktree/sibling", key(live))[0], "UNMERGED-LIVE")
    check("content: AC7 the nested harness worktree reads its HEAD's verdict",
          read_verdict(rows, "worktree/nested", ".claude/worktrees/nest")[0], "MERGED")
    check("content: AC7 the temp-dir worktree reads its HEAD's verdict",
          read_verdict(rows, "worktree/temp", key(tmp_wt))[0], "MERGED")
    fresh = read_report(repo)
    check("content: AC7 under the default bound a fresh worktree reads IN-PROGRESS",
          read_verdict(fresh, "worktree/nested", ".claude/worktrees/nest")[0], "IN-PROGRESS")


def arm_stash():
    """AC8 — a stash whose bytes landed is SUPERSEDED; one with new bytes is UNKNOWN."""
    repo = seed_repo(build_dir())
    (repo / "a.txt").write_text("a2\n", encoding="utf-8", newline="\n")
    run_git(repo, "stash", "push", "-q", "-m", "landed")
    seed_commit(repo, "a.txt", "a2\n", "feat: a2")
    seed_publish(repo)
    (repo / "a.txt").write_text("zzz\n", encoding="utf-8", newline="\n")
    run_git(repo, "stash", "push", "-q", "-m", "new bytes")
    rows = read_report(repo, "--fresh-hours", "0")
    check("stash: AC8 a stash whose bytes landed reads SUPERSEDED",
          read_verdict(rows, "stash", "stash@{1}")[0], "SUPERSEDED")
    check("stash: AC8 a stash with new bytes reads UNKNOWN",
          read_verdict(rows, "stash", "stash@{0}")[0], "UNKNOWN")


@contextlib.contextmanager
def seed_environ():
    """Run in-process calls of the CLI's functions under the fixture's git environment."""
    saved = dict(os.environ)
    os.environ.clear()
    os.environ.update(ENV)
    try:
        yield
    finally:
        os.environ.clear()
        os.environ.update(saved)


@contextlib.contextmanager
def seed_seam(name, value):
    """Replace one module attribute of the CLI for the length of a block."""
    saved = getattr(BR, name)
    setattr(BR, name, value)
    try:
        yield
    finally:
        setattr(BR, name, saved)


def arm_remover():
    """TOOL-dSweptBranches-4 AC1 to AC5 — the removal fallbacks, the skeleton rule and busy."""
    base = build_dir()
    repo = seed_repo(base)
    key = lambda p: str(p).replace("\\", "/")

    def seed_worktree(name):
        p = base / "fx" / name
        run_git(repo, "worktree", "add", "-q", "-b", name + "-br", str(p), "main")
        return p

    def run_failing_remove(root, path):
        return 1, "error: failed to delete 'node_modules/x': Result too large"

    real_remove = BR.run_worktree_remove
    linked = []

    def build_skeleton_remover(extra_file):
        def remove(root, path):
            rc = real_remove(root, path)
            d = pathlib.Path(path) / "node_modules" / ".pnpm" / "pkg@1" / "node_modules"
            d.mkdir(parents=True)
            try:
                os.symlink("/" + "c/nonexistent/pnpm/target", d / "pkg")
                linked.append(True)
            except OSError:
                linked.append(False)
            if extra_file:
                (pathlib.Path(path) / "node_modules" / "leftover.txt").write_text("x", encoding="utf-8")
            return rc
        return remove

    spawned = []
    real_run = subprocess.run

    def run_spied(argv, *a, **k):
        spawned.append(list(argv))
        return real_run(argv, *a, **k)

    with seed_environ():
        wt = seed_worktree("fallback")
        (wt / "deep").mkdir()
        (wt / "deep" / "f.txt").write_text("x", encoding="utf-8")
        with seed_seam("run_worktree_remove", run_failing_remove):
            got = BR.remove_worktree(repo, str(wt))
        listed = run_git(repo, "worktree", "list", "--porcelain")
        check("remover: AC1 a failed git removal falls back to rm -rf",
              (got[0], wt.exists(), key(wt) in listed), ("removed", False, False))

        wt = seed_worktree("skeleton")
        subprocess.run = run_spied
        try:
            with seed_seam("run_worktree_remove", build_skeleton_remover(False)):
                got = BR.remove_worktree(repo, str(wt))
        finally:
            subprocess.run = real_run
        check("remover: AC2 an empty skeleton of links is removed", (got[0], os.path.lexists(wt)),
              ("removed", False))
        check("remover: AC2 no readlink is spawned",
              [a for a in spawned if any("readlink" in str(x) for x in a)], [])
        if linked and not linked[-1]:
            print("remover: skipped — this node cannot create a symlink, so the skeleton held "
                  "empty directories only")

        wt = seed_worktree("holds")
        with seed_seam("run_worktree_remove", build_skeleton_remover(True)):
            got = BR.remove_worktree(repo, str(wt))
        check("remover: AC3 a skeleton holding a regular file is kept",
              (got[0], "regular file" in got[1], wt.exists()), ("kept", True, True))
        shutil.rmtree(wt, ignore_errors=True)

        wt = seed_worktree("busy")
        with seed_seam("run_worktree_remove", run_failing_remove), seed_seam(
                "run_rm", lambda rm, path: (1, f"rm: cannot remove '{path}': Device or resource busy")):
            got = BR.remove_worktree(repo, str(wt))
        check("remover: AC4 a busy directory is reported busy, not failed", got[0], "busy")

        wt = seed_worktree("norm")
        with seed_seam("run_worktree_remove", run_failing_remove), seed_seam("RM_NAME", "rm-absent-from-path"):
            got = BR.remove_worktree(repo, str(wt))
        check("remover: AC5 with no rm on PATH the row fails and names rm",
              (got[0], "rm-absent-from-path" in got[1], wt.exists()), ("failed", True, True))


def seed_write_fixture():
    """One row of each verdict, worktrees on two of them, and two branches published to upstream."""
    import datetime
    old = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=10)).strftime(
        "%Y-%m-%dT%H:%M:%S+0000")
    base = build_dir()
    repo = seed_repo(base)
    run_git(repo, "checkout", "-q", "-b", "merged-br")
    seed_commit(repo, "m.txt", "m\n", "feat: merged", when=old)
    run_git(repo, "checkout", "-q", "main")
    run_git(repo, "merge", "-q", "--ff-only", "merged-br")
    run_git(repo, "checkout", "-q", "-b", "equiv-br", "HEAD~1")
    seed_commit(repo, "e.txt", "e\n", "feat: equivalent", when=old)
    run_git(repo, "checkout", "-q", "main")
    run_git(repo, "cherry-pick", "equiv-br")
    run_git(repo, "checkout", "-q", "-b", "live-br", "main")
    seed_commit(repo, "l.txt", "unlanded\n", "feat: unlanded", when=old)
    run_git(repo, "checkout", "-q", "-b", "open-br", "main")
    seed_commit(repo, "memory/builds/dOpen/README.md", "**Build status:** INPROGRESS · 1 unit(s)\n",
                "spec(dOpen): open the build", when=old)
    run_git(repo, "checkout", "-q", "--orphan", "orphan-br")
    seed_commit(repo, "o.txt", "o\n", "orphan: unrelated history", when=old)
    run_git(repo, "checkout", "-q", "main")
    seed_publish(repo)
    run_git(repo, "push", "-q", "upstream", "merged-br", "live-br")
    run_git(repo, "fetch", "-q", "upstream")
    wt_gone = base / "fx" / "wt-merged"
    run_git(repo, "worktree", "add", "-q", str(wt_gone), "merged-br")
    wt_live = base / "fx" / "wt-live"
    run_git(repo, "worktree", "add", "-q", str(wt_live), "live-br")
    return repo, wt_gone, wt_live


def run_main(*argv):
    """-> (exit, stdout) of the CLI's main, in-process, so a seam can stage a failure."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        rc = BR.main(list(argv))
    return rc, buf.getvalue()


def arm_write():
    """TOOL-dSweptBranches-3 AC1 to AC4 — the manifest first, the three verdicts only, one push."""
    repo, wt_gone, wt_live = seed_write_fixture()
    key = lambda p: str(p).replace("\\", "/")
    with seed_environ():
        before = read_rows(run_cli(repo, "--fresh-hours", "0")[1])
        check("write: the fixture holds one row of each verdict", sorted({v[0] for v in before.values()}),
              sorted(["MERGED", "EQUIVALENT", "UNMERGED-LIVE", "IN-PROGRESS", "UNKNOWN"]))
        rc, _out, err = run_cli(repo, "--remote")
        check("write: --remote without --write refuses", (rc, "--write" in err), (2, True))
        BR.WRITE_TRACE.clear()
        rc, out = run_main("--root", str(repo), "--fresh-hours", "0", "--write")
        check("write: the run exits 0", rc, 0)
        trace = [t[0] for t in BR.WRITE_TRACE]
        check("write: AC1 the manifest precedes the first deletion",
              (trace[:1], len(trace) > 1), (["manifest"], True))
        manifest = pathlib.Path(BR.WRITE_TRACE[0][1]).read_text(encoding="utf-8")
        common = run_git(repo, "rev-parse", "--path-format=absolute", "--git-common-dir")
        check("write: AC1 the manifest sits under the git common dir",
              key(BR.WRITE_TRACE[0][1]).startswith(key(common)), True)
        check("write: AC1 the manifest lists every branch tip and worktree HEAD",
              all(f"branch {b} " in manifest for b in ("main", "merged-br", "equiv-br", "live-br",
                                                       "open-br", "orphan-br"))
              and f"worktree {key(wt_gone)} " in manifest.replace("\\", "/")
              and f"worktree {key(wt_live)} " in manifest.replace("\\", "/"), True)
        branches = set(run_git(repo, "for-each-ref", "--format=%(refname:short)", "refs/heads").split())
        check("write: AC2 only the landed worktree and branches are gone",
              (wt_gone.exists(), wt_live.exists(), sorted(branches)),
              (False, True, sorted(["main", "live-br", "open-br", "orphan-br"])))
        remote_before = run_git(repo, "ls-remote", "upstream")
        check("write: AC2 no remote branch is touched without --remote",
              "refs/heads/merged-br" in remote_before, True)
        main_tip = run_git(repo, "rev-parse", "upstream/main")

        BR.WRITE_TRACE.clear()
        rc, out = run_main("--root", str(repo), "--fresh-hours", "0", "--write", "--remote")
        pushes = [t for t in BR.WRITE_TRACE if t[0] == "push-delete"]
        remote_after = run_git(repo, "ls-remote", "upstream")
        check("write: AC3 one push deletes exactly the landed remote branch, and exits 0",
              (rc, [p[1] for p in pushes], "refs/heads/merged-br" in remote_after,
               "refs/heads/live-br" in remote_after), (0, [("merged-br",)], False, True))
        check("write: AC3 the default branch's tip on the remote is unchanged",
              run_git(str(pathlib.Path(repo).parent.parent / "remote.git"), "rev-parse", "main"),
              main_tip)

    repo, wt_gone, wt_live = seed_write_fixture()
    with seed_environ():
        run_git(repo, "branch", "merged-two", "merged-br")
        wt_two = pathlib.Path(repo).parent / "wt-two"
        run_git(repo, "worktree", "add", "-q", str(wt_two), "merged-two")
        real = BR.remove_worktree
        def remove_one_failing(root, path):
            if key(path) == key(wt_gone):
                return "failed", "staged failure"
            return real(root, path)
        with seed_seam("remove_worktree", remove_one_failing):
            rc, out = run_main("--root", str(repo), "--fresh-hours", "0", "--write")
        check("write: AC4 one failed removal reports, the rest proceed, and the exit is 1",
              (rc, "failed — worktree" in out, wt_two.exists()), (1, True, False))
        repo2, wt_b, _wt_l = seed_write_fixture()
        def remove_busy(root, path):
            return "busy", "busy: held as a working directory"
        with seed_seam("remove_worktree", remove_busy):
            rc, out = run_main("--root", str(repo2), "--fresh-hours", "0", "--write")
        check("write: AC4 a busy worktree is reported and the exit stays 0",
              (rc, "busy — worktree" in out), (0, True))


def arm_keeps():
    """Closing review round 1, B1 and B2 — every keep is the DECIDING keep in some fixture.

    B1: a deletable linked worktree holding a kept worktree inside it is kept. B2: run from a linked
    worktree, with the primary on another branch, the primary worktree and local `main` survive only
    through their own keeps, and their rows say so.
    """
    base = build_dir()
    repo = seed_repo(base)
    key = lambda p: str(p).replace("\\", "/")
    with seed_environ():
        run_git(repo, "branch", "x-br", "main")
        outer = base / "fx" / "outer"
        run_git(repo, "worktree", "add", "-q", str(outer), "x-br")
        inner = outer / ".claude" / "worktrees" / "inner"
        run_git(repo, "worktree", "add", "-q", "-b", "y-br", str(inner), "main")
        (inner / "precious.txt").write_text("unlanded\n", encoding="utf-8")
        run_git(repo, "checkout", "-q", "-b", "side")
        here = base / "fx" / "here"
        run_git(repo, "worktree", "add", "-q", "-b", "here-br", str(here), "main")
        rows = read_rows(run_cli(here, "--fresh-hours", "0")[1])
        outer_row = rows.get(("worktree/sibling", key(outer)))
        check("keeps: B1 a worktree holding a kept worktree reads keep (contains kept worktree ...)",
              bool(outer_row) and outer_row[6].startswith("keep (contains kept worktree"), True)
        check("keeps: B2 the primary worktree reads keep (the primary worktree)",
              rows.get(("worktree/primary", key(repo)), [""] * 8)[6], "keep (the primary worktree)")
        check("keeps: B2 local main reads keep (the default branch)",
              rows.get(("local", "main"), [""] * 8)[6], "keep (the default branch)")
        check("keeps: B2 upstream/main reads keep (the default branch)",
              rows.get(("remote", "upstream/main"), [""] * 8)[6], "keep (the default branch)")
        inv = BR.read_inventory(here)
        inv["fresh"] = 0
        check("keeps: no action carries the row separator, so the report parses",
              [r["action"] for r in BR.build_rows(inv) if " · " in r["action"]], [])
        rc, out = run_main("--root", str(here), "--fresh-hours", "0", "--write")
        branches = set(run_git(repo, "for-each-ref", "--format=%(refname:short)", "refs/heads").split())
        check("keeps: B1 --write spares the container and the live worktree inside it",
              (rc, outer.exists(), (inner / "precious.txt").exists(), "x-br" in branches),
              (0, True, True, True))
        check("keeps: B2 --write spares the primary and local main",
              (repo.exists(), (repo / ".git").exists(), "main" in branches), (True, True, True))


def arm_unread():
    """TOOL-dSweptBranches-7 — a worktree whose status was never read is kept, its files untouched."""
    base = build_dir()
    repo = seed_repo(base)
    key = lambda p: str(p).replace("\\", "/")
    with seed_environ():
        wt = base / "fx" / "lost"
        run_git(repo, "worktree", "add", "-q", "-b", "lost-br", str(wt), "main")
        (wt / ".git").unlink()
        (wt / "notes.txt").write_text("never committed\n", encoding="utf-8")
        rows = read_rows(run_cli(repo, "--fresh-hours", "0")[1])
        check("unread: AC1 a worktree whose status was not read reads UNKNOWN",
              read_verdict(rows, "worktree/sibling", key(wt))[0], "UNKNOWN")
        rc, _out = run_main("--root", str(repo), "--fresh-hours", "0", "--write")
        check("unread: AC1 --write leaves its untracked file", (wt / "notes.txt").exists(), True)


def arm_foreign():
    """TOOL-dSweptBranches-8 — another repository at a registered worktree path survives --write."""
    base = build_dir()
    repo = seed_repo(base)
    key = lambda p: str(p).replace("\\", "/")
    with seed_environ():
        wt = base / "fx" / "taken"
        run_git(repo, "worktree", "add", "-q", "-b", "taken-br", str(wt), "main")
        shutil.rmtree(wt)
        wt.mkdir()
        run_git(wt, "init", "-q", "-b", "main")
        seed_commit(wt, "own.txt", "its own history\n", "foreign: unpushed work")
        gone = base / "fx" / "gone"
        run_git(repo, "worktree", "add", "-q", "-b", "gone-br", str(gone), "main")
        shutil.rmtree(gone)
        rows = read_rows(run_cli(repo, "--fresh-hours", "0")[1])
        check("foreign: AC1 a foreign repository at a worktree path reads UNKNOWN",
              read_verdict(rows, "worktree/sibling", key(wt))[0], "UNKNOWN")
        rc, out = run_main("--root", str(repo), "--fresh-hours", "0", "--write")
        check("foreign: AC1 --write leaves the foreign repository and its commit",
              ((wt / ".git").is_dir(), (wt / "own.txt").exists()), (True, True))
        listed = run_git(repo, "worktree", "list", "--porcelain")
        check("foreign: AC1 a worktree whose path is gone is pruned, and the run exits 0",
              (rc, key(gone) in listed), (0, False))
        with seed_seam("run_worktree_remove", lambda root, path: (1, "fatal: '.git' is not a .git file")):
            got = BR.remove_worktree(repo, str(wt))
        check("foreign: AC1 the rm -rf fallback refuses a path that is not this repository's worktree",
              (got[0], (wt / "own.txt").exists()), ("failed", True))


def arm_patch_negative():
    """TOOL-dSweptBranches-9 — a same subject is not a rebased copy unless the patches share lines."""
    repo = seed_repo(build_dir())
    seed_commit(repo, "x.txt", seed_lines(10), "seed: x")
    seed_publish(repo)
    run_git(repo, "checkout", "-q", "-b", "other-file")
    seed_commit(repo, "b.txt", "b2\n", "fix: typo")
    run_git(repo, "checkout", "-q", "-b", "disjoint", "main")
    seed_commit(repo, "x.txt", seed_lines(10).replace("line 1\n", "line 1 edited\n"), "fix: spacing")
    run_git(repo, "checkout", "-q", "-b", "same-lines", "main")
    seed_commit(repo, "c1.txt", seed_lines(5, " shared"), "feat: the table")
    run_git(repo, "checkout", "-q", "main")
    seed_commit(repo, "a.txt", "a2\n", "fix: typo")
    seed_commit(repo, "x.txt", seed_lines(10).replace("line 8\n", "line 8 edited\n"), "fix: spacing")
    seed_commit(repo, "c2.txt", seed_lines(5, " shared"), "feat: the table")
    seed_publish(repo)
    rows = read_report(repo, "--fresh-hours", "0")
    check("patch-negative: AC1 a same-subject commit on another file is not a copy",
          read_verdict(rows, "local", "other-file")[0], "UNMERGED-LIVE")
    check("patch-negative: AC1 a same-subject edit of disjoint lines is not a copy",
          read_verdict(rows, "local", "disjoint")[0], "UNMERGED-LIVE")
    check("patch-negative: AC1 the same lines added to a different file are not a copy",
          read_verdict(rows, "local", "same-lines")[0], "UNMERGED-LIVE")


def arm_probe_negative():
    """TOOL-dSweptBranches-10 — a probe's case NAME on the default branch does not cover its body."""
    base = build_dir()
    repo = seed_repo(base)
    seed_commit(repo, "tests/test_land.py", "def test_merge_survives_twice():\n    assert True\n",
                "test: a longer name")
    seed_commit(repo, "docs/notes.md", "We still owe test_mentioned a real fixture.\n", "docs: prose")
    seed_commit(repo, "tests/test_other.py", "def test_parse():\n    return 1\n", "test: parse")
    seed_publish(repo)
    key = lambda p: str(p).replace("\\", "/")
    probes = {"prefix": "def test_merge_survives():\n    assert True\n",
              "prose": "def test_mentioned():\n    assert False\n",
              "body": "def test_parse():\n    return 2\n"}
    for name, text in probes.items():
        wt = base / "fx" / name
        run_git(repo, "worktree", "add", "-q", "-b", name + "-br", str(wt), "main")
        (wt / "test_probe.py").write_text(text, encoding="utf-8", newline="\n")
    rows = read_report(repo, "--fresh-hours", "0")
    for name, why in (("prefix", "only a longer name shares its prefix"),
                      ("prose", "its name appears only in prose"),
                      ("body", "its name is declared under another body")):
        check(f"probe-negative: AC1 a probe is uncovered when {why}",
              read_verdict(rows, "worktree/sibling", key(base / "fx" / name))[0], "UNMERGED-LIVE")


def arm_row_edit():
    """TOOL-dSweptBranches-11 — a row edited in place is not a rotated row, though its id heads one."""
    repo = seed_repo(build_dir())
    seed_commit(repo, "memory/backlog/TOOL.md", "| TOOL-aSlug-1 | fix x | open |\n", "seed: backlog")
    seed_publish(repo)
    run_git(repo, "checkout", "-q", "-b", "row-edit")
    seed_commit(repo, "memory/backlog/TOOL.md", "| TOOL-aSlug-1 | fix x, and y | RESOLVED |\n",
                "records(aSlug): resolve the row")
    run_git(repo, "checkout", "-q", "main")
    rows = read_report(repo, "--fresh-hours", "0")
    check("row-edit: AC1 a row edited in place reads UNMERGED-LIVE",
          read_verdict(rows, "local", "row-edit")[0], "UNMERGED-LIVE")


def arm_default_names():
    """TOOL-dSweptBranches-12 — the remote's own HEAD branch is kept when an override names another."""
    repo = seed_repo(build_dir())
    with seed_environ():
        run_git(repo, "checkout", "-q", "-b", "develop")
        seed_commit(repo, "d.txt", "develop\n", "feat: develop")
        run_git(repo, "push", "-q", "upstream", "develop")
        run_git(repo, "fetch", "-q", "upstream")
        os.environ["GOV_DEFAULT_BRANCH"] = "develop"
        rows = read_rows(run_cli(repo, "--fresh-hours", "0", env=dict(ENV, GOV_DEFAULT_BRANCH="develop"))[1])
        check("default-names: AC1 local main reads keep (the default branch)",
              rows.get(("local", "main"), [""] * 8)[6], "keep (the default branch)")
        check("default-names: AC1 upstream/main reads keep (the default branch)",
              rows.get(("remote", "upstream/main"), [""] * 8)[6], "keep (the default branch)")
        rc, _out = run_main("--root", str(repo), "--fresh-hours", "0", "--write", "--remote")
        remote = run_git(repo, "ls-remote", "upstream")
        branches = set(run_git(repo, "for-each-ref", "--format=%(refname:short)", "refs/heads").split())
        check("default-names: AC1 --write --remote keeps local and remote main",
              ("main" in branches, "refs/heads/main" in remote), (True, True))


def arm_graded_sha():
    """TOOL-dSweptBranches-13 — a ref that moved after it was graded is not deleted."""
    base = build_dir()
    repo = seed_repo(base)
    with seed_environ():
        run_git(repo, "branch", "landed-a", "main")
        run_git(repo, "branch", "landed-b", "main")
        run_git(repo, "push", "-q", "upstream", "landed-a", "landed-b")
        run_git(repo, "fetch", "-q", "upstream")
        other = base / "other"
        run_git(base, "clone", "-q", "-o", "upstream", str(base / "remote.git"), str(other))
        run_git(other, "checkout", "-q", "landed-b")
        seed_commit(other, "late.txt", "pushed after the grading fetch\n", "feat: late work")
        run_git(other, "push", "-q", "upstream", "landed-b")
        rc, out = run_main("--root", str(repo), "--fresh-hours", "0", "--write", "--remote")
        remote = run_git(repo, "ls-remote", "upstream")
        check("graded-sha: AC1 a remote branch that moved after the fetch survives, named as failed",
              ("refs/heads/landed-b" in remote, "landed-b" in out and "failed" in out, rc),
              (True, True, 1))
        check("graded-sha: AC1 the other deletable remote branch still goes",
              "refs/heads/landed-a" in remote, False)

    base = build_dir()
    repo = seed_repo(base)
    with seed_environ():
        run_git(repo, "branch", "moving", "main")
        run_git(repo, "checkout", "-q", "-b", "elsewhere")
        later = seed_commit(repo, "later.txt", "x\n", "feat: later")
        run_git(repo, "checkout", "-q", "main")
        wt = base / "fx" / "wt"
        run_git(repo, "worktree", "add", "-q", "-b", "wt-br", str(wt), "main")
        real = BR.remove_worktree

        def remove_then_move(root, path):
            got = real(root, path)
            run_git(repo, "branch", "-f", "moving", later)
            return got
        with seed_seam("remove_worktree", remove_then_move):
            rc, out = run_main("--root", str(repo), "--fresh-hours", "0", "--write")
        branches = set(run_git(repo, "for-each-ref", "--format=%(refname:short)", "refs/heads").split())
        check("graded-sha: AC2 a local branch that moved after grading is kept and reported",
              ("moving" in branches, "moving" in out and "moved" in out), (True, True))


def arm_evil_merge():
    """TOOL-dSweptBranches-14 — a merge that adds content of its own is never covered."""
    repo = seed_repo(build_dir())
    run_git(repo, "checkout", "-q", "-b", "z")
    seed_commit(repo, "f.txt", "f\n", "build(dFoo): TOOL-dFoo-1 — f")
    run_git(repo, "checkout", "-q", "main")
    seed_commit(repo, "m.txt", "m\n", "feat: main moves on")
    run_git(repo, "checkout", "-q", "z")
    run_git(repo, "merge", "-q", "--no-ff", "--no-commit", "main")
    (repo / "evil.txt").write_text("only in the merge\n", encoding="utf-8", newline="\n")
    run_git(repo, "add", "evil.txt")
    run_git(repo, "commit", "-q", "-m", "merge main into z")
    run_git(repo, "checkout", "-q", "main")
    run_git(repo, "cherry-pick", run_git(repo, "rev-parse", "z^1"))
    seed_publish(repo)
    verdict, ev = read_verdict(read_report(repo, "--fresh-hours", "0"), "local", "z")
    check("evil-merge: AC1 a branch whose merge adds its own content reads UNMERGED-LIVE",
          verdict, "UNMERGED-LIVE")


ARMS = [arm_census, arm_patch, arm_landing, arm_records, arm_rotated, arm_noop, arm_lease,
        arm_content, arm_stash, arm_remover, arm_write, arm_keeps, arm_unread, arm_foreign,
        arm_patch_negative, arm_probe_negative, arm_row_edit, arm_default_names, arm_graded_sha,
        arm_evil_merge]


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
