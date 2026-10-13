#!/usr/bin/env python3
"""branch_reconcile.py — every worktree, branch and stash entry, with one verdict each. gov:kit branch-reconcile@1.0

    python <this kit>/branch_reconcile.py [--root <path>]

Read-only. It prints one report: a header naming the remote, the default branch and its tip, a
`skipped — <predicate> · <why>` line for every predicate that could not run, and one row per
worktree, local branch, remote branch and stash entry:

    <VERDICT> · <kind> · <name> · <tip12> · <tip date> · age <n>d · <action> · <evidence>

The age is whole days from the tip's commit date to the default tip's, so the report reads no clock
and two runs over an unchanged repository print the same bytes. It fetches nothing: fetch first.

Exit 0 with the report printed. Exit 2 on a refusal: no repository, a remote ladder that cannot
choose, or a default branch that resolves nowhere. The verdicts, the write mode and the removal
rules are the kit README's (TOOL-dSweptBranches-1 to -4).
"""
from __future__ import annotations

import argparse
import datetime
import os
import pathlib
import subprocess
import sys
import tempfile

KIT_BRANCH_RECONCILE_VERSION = "1.0"

MERGED = "MERGED"
EQUIVALENT = "EQUIVALENT"
SUPERSEDED = "SUPERSEDED"
IN_PROGRESS = "IN-PROGRESS"
UNMERGED_LIVE = "UNMERGED-LIVE"
UNKNOWN = "UNKNOWN"
# REPORT ORDER: the owner's decisions first, then what is kept, then what write mode removes.
VERDICT_RANK = [UNMERGED_LIVE, UNKNOWN, IN_PROGRESS, SUPERSEDED, EQUIVALENT, MERGED]
DELETABLE = frozenset([MERGED, EQUIVALENT, SUPERSEDED])
KIND_RANK = ["worktree/primary", "worktree/nested", "worktree/sibling", "worktree/temp",
             "worktree/elsewhere", "local", "remote", "stash"]
NESTED_DIR = ".claude/worktrees"


class Refusal(Exception):
    """A reason the report cannot be produced; `main` prints it and exits 2."""


def run_git(root, *args):
    """-> (returncode, stdout as text). No shell; NUL-separated output survives the decode."""
    try:
        p = subprocess.run(["git", "-C", str(root), *args], capture_output=True)
    except OSError as exc:
        return 127, str(exc)
    return p.returncode, p.stdout.decode("utf-8", errors="replace")


def read_git(root, *args):
    """-> stdout stripped, or "" when git exits non-zero."""
    rc, out = run_git(root, *args)
    return out.strip() if rc == 0 else ""


# The remote ladder (TOOL-dLadderedRemote-2), INLINED byte-identically from the canonical copy
# named on its marker line and gated by the resolve-python self-test.
# >>> remote_ladder_py -- canonical copy: resolve_remote.py in the gov lib dir (byte-identical; gated)
def resolve_remote(root):
    """-> (remote, branch, observed, refusal) for the repository at <root>. Fetches nothing.

    remote    GOV_REMOTE, else branch.<current>.remote unless it is ".", else the ONLY remote.
              Several remotes and none chosen, or a chosen name that is not a remote here, is a
              REFUSAL naming GOV_REMOTE. No remote at all is remote "" and NO refusal: the caller
              keeps its own no-remote fallback.
    observed  the branch refs/remotes/<remote>/HEAD names, or "". A caller whose GOV_DEFAULT_BRANCH
              only CROSS-CHECKS the observation reads this one.
    branch    GOV_DEFAULT_BRANCH, else observed, else "".
    A refusal empties the other three, so no caller can pick a remote the ladder refused.
    """
    import os
    import subprocess

    def read(*args):
        try:
            p = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
        except OSError:
            return ""
        return p.stdout.strip() if p.returncode == 0 else ""

    names = read("remote").split()
    listed = " ".join(names) or "none"
    # FULL refs, never `--short`: a tag or branch sharing the name makes the short form ambiguous
    # (`heads/x`, `remotes/r/x`), and the prefix is stripped exactly instead.
    cur = read("symbolic-ref", "--quiet", "HEAD")
    cur = cur[len("refs/heads/"):] if cur.startswith("refs/heads/") else ""
    remote, how = os.environ.get("GOV_REMOTE") or "", "GOV_REMOTE"
    if not remote and cur:
        remote, how = read("config", "branch." + cur + ".remote"), "branch." + cur + ".remote"
        if remote == ".":
            remote = ""
    if not remote and len(names) == 1:
        remote = names[0]
    if not remote and len(names) > 1:
        where = "branch " + cur if cur else "a detached HEAD"
        return "", "", "", ("cannot choose a remote: GOV_REMOTE is unset, %s has no configured remote, "
                            "and this repository has %d remotes (%s). Name it: export GOV_REMOTE=<remote>."
                            % (where, len(names), listed))
    if remote and remote not in names:
        return "", "", "", ("%s names %s, which is no remote of this repository (%s). Name one that is: "
                            "export GOV_REMOTE=<remote>." % (how, remote, listed))
    observed = ""
    if remote:
        pre = "refs/remotes/" + remote + "/"
        head = read("symbolic-ref", "--quiet", pre + "HEAD")
        if head.startswith(pre) and len(head) > len(pre):
            observed = head[len(pre):]
    return remote, os.environ.get("GOV_DEFAULT_BRANCH") or observed, observed, ""
# <<< remote_ladder_py


def check_ref(root, ref):
    return run_git(root, "rev-parse", "--verify", "--quiet", ref + "^{commit}")[0] == 0


def resolve_default(root):
    """-> (remote, branch, ref, notes). The ladder, then `main`, then `master`.

    The ref is the remote-tracking branch whenever it resolves, else the local branch, ANNOUNCED in
    the notes: a report graded against a local branch must say so.
    """
    remote, branch, _observed, refusal = resolve_remote(root)
    if refusal:
        raise Refusal(refusal)
    notes = []
    if not branch:
        for cand in ("main", "master"):
            if (remote and check_ref(root, f"refs/remotes/{remote}/{cand}")) \
                    or check_ref(root, f"refs/heads/{cand}"):
                branch = cand
                break
    if not branch:
        raise Refusal("cannot resolve a default branch: set GOV_DEFAULT_BRANCH, or run "
                      f"`git remote set-head {remote or '<remote>'} -a`")
    if remote and check_ref(root, f"refs/remotes/{remote}/{branch}"):
        return remote, branch, f"refs/remotes/{remote}/{branch}", notes
    if check_ref(root, f"refs/heads/{branch}"):
        why = f"{remote} has no {branch} ref here" if remote else "this clone has no remote"
        notes.append(f"note — {why}, so the default branch is local {branch}")
        return remote, branch, f"refs/heads/{branch}", notes
    raise Refusal(f"the default branch {branch} resolves neither as a remote-tracking ref nor locally")


def derive_key(path):
    """A path as this platform compares paths: absolute, normalised, case-folded on Windows."""
    return os.path.normcase(os.path.normpath(os.path.abspath(str(path))))


def check_under(path, parent):
    p, q = derive_key(path), derive_key(parent)
    return p != q and p.startswith(q.rstrip(os.sep) + os.sep)


def derive_location(path, primary):
    """One location kind per worktree. Sibling is tested before temp: a primary may itself sit there."""
    if derive_key(path) == derive_key(primary):
        return "worktree/primary"
    if check_under(path, pathlib.Path(primary) / NESTED_DIR):
        return "worktree/nested"
    if derive_key(pathlib.Path(path).parent) == derive_key(pathlib.Path(primary).parent):
        return "worktree/sibling"
    if check_under(os.path.realpath(path), os.path.realpath(tempfile.gettempdir())):
        return "worktree/temp"
    return "worktree/elsewhere"


def parse_worktrees(text):
    """`git worktree list --porcelain -z` -> one dict per worktree, in git's order."""
    out, cur = [], None
    for field in text.split("\0"):
        if not field:
            if cur is not None:
                out.append(cur)
                cur = None
            continue
        key, _, val = field.partition(" ")
        if key == "worktree":
            if cur is not None:
                out.append(cur)
            cur = {"path": val, "head": "", "branch": "", "flags": []}
        elif cur is None:
            continue
        elif key == "HEAD":
            cur["head"] = val
        elif key == "branch":
            cur["branch"] = val[len("refs/heads/"):] if val.startswith("refs/heads/") else val
        elif key in ("detached", "bare", "locked", "prunable"):
            cur["flags"].append(key)
    if cur is not None:
        out.append(cur)
    return out


def parse_status(text):
    """`git status --porcelain=v2 -z --untracked-files=all` -> counts and the paths behind them."""
    st = {"staged": 0, "unstaged": 0, "unmerged": 0, "untracked": [], "drift": 0, "changed": []}
    fields = text.split("\0")
    i = 0
    while i < len(fields):
        f = fields[i]
        i += 1
        if not f:
            continue
        kind = f[0]
        if kind in "12":
            parts = f.split(" ", 8 if kind == "1" else 9)
            xy, sub = parts[1], parts[2]
            if xy[0] != ".":
                st["staged"] += 1
            if xy[1] != ".":
                st["unstaged"] += 1
            if sub.startswith("S") and sub[1] == "C":
                st["drift"] += 1
            st["changed"].append(parts[-1])
            if kind == "2":
                i += 1  # a rename's original path rides the next NUL-separated field
        elif kind == "u":
            st["unmerged"] += 1
            st["changed"].append(f.split(" ", 10)[-1])
        elif kind == "?":
            st["untracked"].append(f[2:])
    return st


def read_git_path(path, name):
    p = read_git(path, "rev-parse", "--git-path", name)
    if not p:
        return None
    q = pathlib.Path(p)
    return q if q.is_absolute() else pathlib.Path(path) / q


def read_dirt(path, others):
    """The worktree's dirty state, with untracked paths that ARE other worktrees left out.

    A nested harness worktree is a directory its primary's status lists as untracked; counting it
    would make every primary read dirty (gotcha a-gate-that-walks-the-repo-root-reads-other-worktrees).
    """
    rc, out = run_git(path, "status", "--porcelain=v2", "-z", "--untracked-files=all",
                      "--ignore-submodules=none")
    if rc != 0:
        return None
    st = parse_status(out)
    keep = []
    for rel in st["untracked"]:
        full = pathlib.Path(path) / rel.rstrip("/")
        if any(derive_key(full) == derive_key(o) or check_under(o, full) for o in others):
            continue
        keep.append(rel)
    st["untracked"] = sorted(keep)
    st["merge"] = ""
    merge_head = read_git_path(path, "MERGE_HEAD")
    if merge_head is not None and merge_head.is_file():
        words = merge_head.read_text(encoding="utf-8", errors="replace").split()
        st["merge"] = words[0] if words else ""
    st["rebase"] = False
    for d in ("rebase-merge", "rebase-apply"):
        p = read_git_path(path, d)
        st["rebase"] = st["rebase"] or (p is not None and p.is_dir())
    return st


def render_dirt(st):
    """-> the dirty-state evidence, or "" for a clean worktree."""
    if st is None:
        return ""
    bits = [f"{key} {st[key]}" for key in ("staged", "unstaged", "unmerged") if st[key]]
    if st["untracked"]:
        bits.append(f"untracked {len(st['untracked'])}")
    if st["merge"]:
        bits.append(f"merging {st['merge'][:12]}")
    if st["rebase"]:
        bits.append("rebasing")
    if st["drift"]:
        bits.append(f"submodule drift {st['drift']}")
    return " · ".join(bits)


def read_commit_time(root, rev):
    """-> the committer epoch of <rev>, or 0."""
    out = read_git(root, "log", "-1", "--format=%ct", rev, "--")
    return int(out) if out.isdigit() else 0


def read_worktrees(root):
    rc, out = run_git(root, "worktree", "list", "--porcelain", "-z")
    if rc != 0:
        raise Refusal("git worktree list failed, so no worktree could be read")
    worktrees = parse_worktrees(out)
    primary = worktrees[0]["path"] if worktrees else str(root)
    paths = [w["path"] for w in worktrees]
    here = read_git(root, "rev-parse", "--show-toplevel")
    for w in worktrees:
        w["kind"] = derive_location(w["path"], primary)
        w["invoking"] = bool(here) and derive_key(here) == derive_key(w["path"])
        readable = "prunable" not in w["flags"] and "bare" not in w["flags"] \
            and os.path.isdir(w["path"])
        others = [p for p in paths if derive_key(p) != derive_key(w["path"])]
        w["dirt"] = read_dirt(w["path"], others) if readable else None
        w["ct"] = read_commit_time(root, w["head"]) if w["head"] else 0
    return primary, worktrees


def read_refs(root, remote):
    refs = []
    scopes = ["refs/heads"] + ([f"refs/remotes/{remote}"] if remote else [])
    out = read_git(root, "for-each-ref",
                   "--format=%(refname)%00%(objectname)%00%(committerdate:unix)", *scopes)
    for line in out.splitlines():
        name, sha, ct = line.split("\0")
        if name == f"refs/remotes/{remote}/HEAD":
            continue
        local = name.startswith("refs/heads/")
        short = name[len("refs/heads/"):] if local else name[len("refs/remotes/"):]
        refs.append({"kind": "local" if local else "remote", "name": short, "ref": name, "tip": sha,
                     "ct": int(ct or 0)})
    return refs


def read_stash(root):
    stash = []
    for line in read_git(root, "stash", "list", "--format=%gd%x00%H%x00%ct").splitlines():
        name, sha, ct = line.split("\0")
        stash.append({"kind": "stash", "name": name, "ref": sha, "tip": sha, "ct": int(ct or 0)})
    return stash


def read_inventory(root):
    """Every worktree, local branch, remote branch and stash entry, plus the default tip."""
    if run_git(root, "rev-parse", "--git-dir")[0] != 0:
        raise Refusal(f"{root} is not inside a git repository")
    remote, branch, ref, notes = resolve_default(root)
    tip = read_git(root, "rev-parse", ref)
    primary, worktrees = read_worktrees(root)
    return {"root": str(root), "remote": remote, "branch": branch, "default_ref": ref,
            "default_tip": tip, "default_ct": read_commit_time(root, ref), "notes": notes,
            "primary": primary, "worktrees": worktrees, "refs": read_refs(root, remote),
            "stash": read_stash(root), "skips": {}}


# ------------------------------------------------------------------------------- the verdict seam
# One function per predicate, each returning (verdict, evidence) or None for "not decided". The
# ladder reads them in order and falls to UNKNOWN. TOOL-dSweptBranches-2 replaces the stubs.

def check_merged(inv, item):
    return None


def check_equivalent(inv, item):
    return None


def check_superseded(inv, item):
    return None


def check_in_progress(inv, item):
    return None


def check_unmerged_live(inv, item):
    return None


PREDICATES = [check_merged, check_equivalent, check_superseded, check_in_progress,
              check_unmerged_live]


def derive_verdict(inv, item):
    for pred in PREDICATES:
        got = pred(inv, item)
        if got is not None:
            return got
    return UNKNOWN, "no predicate decided"


def derive_action(inv, item, verdict):
    return "keep"


def build_rows(inv):
    """-> one row per worktree, ref and stash entry, its verdict and action included, in report order."""
    rows = []
    for w in inv["worktrees"]:
        name = w["path"].replace("\\", "/")
        if check_under(w["path"], inv["primary"]):
            name = os.path.relpath(w["path"], inv["primary"]).replace("\\", "/")
        flags = list(w["flags"]) + (["invoking"] if w["invoking"] else [])
        if w["dirt"] is None and "bare" not in w["flags"]:
            flags.append("status not read")
        item = {"kind": w["kind"], "name": name, "tip": w["head"], "ct": w["ct"], "worktree": w}
        verdict, evidence = derive_verdict(inv, item)
        pieces = [" · ".join(flags), w["branch"] and f"branch {w['branch']}", render_dirt(w["dirt"]),
                  evidence]
        rows.append({"verdict": verdict, "kind": w["kind"], "name": name, "tip": w["head"],
                     "ct": w["ct"], "action": derive_action(inv, item, verdict),
                     "evidence": " · ".join(p for p in pieces if p), "item": item})
    for r in inv["refs"] + inv["stash"]:
        item = dict(r)
        verdict, evidence = derive_verdict(inv, item)
        rows.append({"verdict": verdict, "kind": r["kind"], "name": r["name"], "tip": r["tip"],
                     "ct": r["ct"], "action": derive_action(inv, item, verdict),
                     "evidence": evidence, "item": item})
    rows.sort(key=lambda r: (VERDICT_RANK.index(r["verdict"]), KIND_RANK.index(r["kind"]), r["name"]))
    return rows


def render_date(ct):
    if not ct:
        return "----------"
    return datetime.datetime.fromtimestamp(ct, datetime.timezone.utc).strftime("%Y-%m-%d")


def render_report(inv, rows):
    where = f"{inv['remote']}/{inv['branch']}" if inv["default_ref"].startswith("refs/remotes/") \
        else f"local {inv['branch']}"
    locals_ = sum(1 for r in inv["refs"] if r["kind"] == "local")
    lines = [f"branch-reconcile — {where} at {inv['default_tip'][:12]} · "
             f"{len(inv['worktrees'])} worktree(s) · {locals_} local · "
             f"{len(inv['refs']) - locals_} remote · {len(inv['stash'])} stash"]
    lines += inv["notes"]
    lines += [f"skipped — {pred} · {why}" for pred, why in sorted(inv["skips"].items())]
    for r in rows:
        age = (inv["default_ct"] - r["ct"]) // 86400 if r["ct"] else 0
        lines.append(" · ".join([r["verdict"], r["kind"], r["name"], (r["tip"] or "-")[:12],
                                 render_date(r["ct"]), f"age {age}d", r["action"],
                                 r["evidence"] or "-"]))
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(prog="branch_reconcile.py")
    ap.add_argument("--root", default=".", help="any path inside the repository (default: .)")
    args = ap.parse_args(argv)
    try:
        inv = read_inventory(pathlib.Path(args.root))
        lines = render_report(inv, build_rows(inv))
    except Refusal as exc:
        print(f"branch-reconcile: {exc}", file=sys.stderr)
        return 2
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())
