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
ASSERTION_FLOOR = 34
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
    seed_commit(repo, "tests/test_land.py", "def test_merge_survives():\n    pass\n", "test: landed")
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


ARMS = [arm_census, arm_patch, arm_landing, arm_records, arm_rotated, arm_noop, arm_lease,
        arm_content, arm_stash]


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
