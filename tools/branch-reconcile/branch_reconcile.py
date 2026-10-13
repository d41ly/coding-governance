#!/usr/bin/env python3
"""branch_reconcile.py — every worktree, branch and stash entry, with one verdict each. gov:kit branch-reconcile@1.0

    python <this kit>/branch_reconcile.py [--root <path>] [--fresh-hours <n>] [--write [--remote]]

Read-only without `--write`. It prints one report: a header naming the remote, the default branch and its tip, a
`skipped — <predicate> · <why>` line for every predicate that could not run, and one row per
worktree, local branch, remote branch and stash entry:

    <VERDICT> · <kind> · <name> · <tip12> · <tip date> · age <n>d · <action> · <evidence>

The age is whole days from the tip's commit date to the default tip's, so the report reads no clock
and two runs over an unchanged repository print the same bytes. It fetches nothing: fetch first.

`--write` then writes a recovery manifest under the git common directory and removes the worktrees,
then the local branches, whose verdict is MERGED, EQUIVALENT or SUPERSEDED; `--remote` adds those
remote branches, deleted in one push. Nothing else is ever deleted, and the default branch is never
touched.

Exit 0 with the report printed and every write action done or busy; 1 when a write action failed.
Exit 2 on a refusal: no repository, a remote ladder that cannot choose, a default branch that
resolves nowhere, `--remote` without `--write`, or a manifest that could not be written. The
verdicts, the write mode and the removal rules are the kit README's (TOOL-dSweptBranches-1 to -4).
"""
from __future__ import annotations

import argparse
import collections
import datetime
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

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
# A tip, a lease or a worktree touched this recently is somebody's work in progress.
FRESH_HOURS = 24.0


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


def check_worktree_identity(root, path):
    """-> "" when <path> is provably a linked worktree of the repository at <root>, else why not.

    git's registry names a path, not what now sits there (TOOL-dSweptBranches-8): the directory may
    have been replaced by another repository, whose clean status would grade it on the registered
    HEAD and whose refusal to be removed as a worktree would hand it to `rm -rf`. Proof is a `.git`
    FILE whose common dir is this repository's.
    """
    dotgit = pathlib.Path(path) / ".git"
    if dotgit.is_dir():
        return "it holds a .git directory of its own, so it is another repository"
    if not dotgit.is_file():
        return "it has no .git file"
    mine = read_git(root, "rev-parse", "--path-format=absolute", "--git-common-dir")
    theirs = read_git(path, "rev-parse", "--path-format=absolute", "--git-common-dir")
    if not mine or not theirs or derive_key(mine) != derive_key(theirs):
        return "its git common dir is not this repository's"
    return ""


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
        w["foreign"] = ""
        if readable and w["kind"] != "worktree/primary":
            w["foreign"] = check_worktree_identity(root, w["path"])
            if w["foreign"]:
                w["flags"].append("foreign")
                readable = False
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
    # EVERY NAME THE DEFAULT GOES BY is kept (TOOL-dSweptBranches-12): the branch the ladder chose
    # and the remote's own HEAD branch, which differ when GOV_DEFAULT_BRANCH overrides the remote.
    observed = resolve_remote(root)[2]
    return {"root": str(root), "remote": remote, "branch": branch, "default_ref": ref,
            "default_names": sorted({branch, observed} - {""}),
            "default_tip": tip, "default_ct": read_commit_time(root, ref), "notes": notes,
            "primary": primary, "worktrees": worktrees, "refs": read_refs(root, remote),
            "stash": read_stash(root), "skips": {}, "fresh": FRESH_HOURS * 3600, "now": time.time()}


# ------------------------------------------------------------------------------- the default side
# Everything a predicate compares against is read once per repository or per merge base and cached
# in inv["cache"]: the default tree's blobs, the commits the default branch gained since a merge base,
# and each commit's patch lines and files.

def read_cached(inv, key, fn):
    cache = inv.setdefault("cache", {})
    if key not in cache:
        cache[key] = fn()
    return cache[key]


def read_memory_root(inv):
    """MEMORY_ROOT from `.memory-tree.conf` at the repository top, else `memory`."""
    def load():
        top = read_git(inv["root"], "rev-parse", "--show-toplevel")
        conf = pathlib.Path(top or inv["root"]) / ".memory-tree.conf"
        if conf.is_file():
            for line in conf.read_text(encoding="utf-8", errors="replace").splitlines():
                m = re.match(r'^\s*MEMORY_ROOT\s*=\s*"?([^"#\s]+)"?', line)
                if m:
                    return m.group(1).strip("/")
        return "memory"
    return read_cached(inv, "memory-root", load)


def read_default_tree(inv):
    """-> {path: blob sha} for every file at the default tip."""
    def load():
        out = read_git(inv["root"], "ls-tree", "-r", "-z", "--full-tree", inv["default_ref"])
        tree = {}
        for entry in out.split("\0"):
            meta, _, path = entry.partition("\t")
            parts = meta.split()
            if len(parts) == 3 and parts[1] == "blob":
                tree[path] = parts[2]
        return tree
    return read_cached(inv, "default-tree", load)


def read_side(inv, mb):
    """-> ({subject: [non-merge sha]}, [(merge sha, subject)]) for <mb>..<default>."""
    def load():
        by_subject, merges = {}, []
        out = read_git(inv["root"], "log", "--format=%H%x00%P%x00%s", f"{mb}..{inv['default_ref']}")
        for line in out.splitlines():
            sha, parents, subject = line.split("\0", 2)
            if len(parents.split()) > 1:
                merges.append((sha, subject))
            else:
                by_subject.setdefault(subject, []).append(sha)
        return by_subject, merges
    return read_cached(inv, ("side", mb), load)


def read_patch_lines(inv, sha):
    """-> Counter of a commit's `+` and `-` lines, headers dropped."""
    def load():
        out = run_git(inv["root"], "show", "--format=", "--no-color", "--no-ext-diff", "-U0",
                      "--no-renames", sha)[1]
        return collections.Counter(line for line in out.splitlines()
                                   if line[:1] in "+-" and not line.startswith(("+++", "---")))
    return read_cached(inv, ("lines", sha), load)


def read_files(inv, sha, merge=False):
    """-> the paths a commit touched; a merge's against its first parent."""
    def load():
        args = ["diff", "--name-only", "--no-renames", f"{sha}^1", sha] if merge else \
            ["show", "--format=", "--name-only", "--no-renames", sha]
        return frozenset(p for p in read_git(inv["root"], *args).splitlines() if p)
    return read_cached(inv, ("files", sha, merge), load)


def check_ancestor(inv, sha):
    return read_cached(inv, ("anc", sha), lambda: run_git(
        inv["root"], "merge-base", "--is-ancestor", sha, inv["default_ref"])[0] == 0)


def check_row_on_default(inv, row):
    """True when the row text <row>, stripped, is a whole line under the memory root at the default
    tip, archives included. The WHOLE text, not the id heading it (TOOL-dSweptBranches-11): a row
    edited in place keeps its id, and the old row still on the default would vouch for the new one."""
    mem = read_memory_root(inv)

    def load():
        rc, out = run_git(inv["root"], "grep", "-F", "-h", "-e", row, inv["default_ref"], "--", mem)
        return rc == 0 and any(line.strip() == row for line in out.splitlines())
    return read_cached(inv, ("row", row), load)


def derive_row_lines(lines):
    """-> the row lines a commit adds, stripped, or an empty set when any added line is not a row.

    The rotated predicate covers a commit that adds ROWS only. One added line of prose means the
    commit carries content of its own, which a row elsewhere cannot vouch for. A row is a line whose
    first token, after list or table markup, is a row id; a line that merely cites an id is not one.
    """
    rows = set()
    for line in lines:
        if not line.startswith("+") or not line[1:].strip():
            continue
        if not re.match(ROW_HEAD + ID_RE.pattern, line[1:]):
            return set()
        rows.add(line[1:].strip())
    return rows


ID_RE = re.compile(r"(?<![A-Za-z0-9-])[A-Z][A-Z0-9]{1,9}-[a-z][A-Za-z0-9]*-\d+(?![A-Za-z0-9])")
# A row's head: optional list or table markup, an optional link bracket, then the id.
ROW_HEAD = r"^[ \t]*([-*|][ \t]*)?\[?"
SCOPE_RE = re.compile(r"^[a-z][a-z-]*\(([A-Za-z0-9]+)\)")
DRIFT_LINES = 4


def derive_names(subject):
    """-> the unit ids and slugs a commit subject names: `FAMILY-slug-seq` ids and a `type(slug):` scope."""
    names = set(ID_RE.findall(subject))
    names |= {i.split("-")[1] for i in list(names)}
    m = SCOPE_RE.match(subject)
    if m:
        names.add(m.group(1))
    return names


def check_names(names, subject):
    return any(re.search(r"(?<![A-Za-z0-9-])" + re.escape(n) + r"(?![A-Za-z0-9])", subject)
               for n in names)


def read_run_fact(text, key):
    m = re.search(rf"^{re.escape(key)}:[ \t]*(\S.*?)\s*$", text or "", re.M)
    return m.group(1) if m else ""


def read_at(inv, rev, path):
    rc, out = run_git(inv["root"], "show", f"{rev}:{path}")
    return out if rc == 0 else None


def check_build_landed(inv, slug, merges):
    """The default branch shows <slug> landed: its run record says LANDED, or a merge names it."""
    mem = read_memory_root(inv)
    run = read_at(inv, inv["default_ref"], f"{mem}/builds/{slug}/RUN.md")
    if read_run_fact(run, "phase") == "LANDED":
        return True
    tree = read_default_tree(inv)
    if any(p.startswith(f"{mem}/builds/{slug}/RUN.LANDED.") for p in tree):
        return True
    return any(check_names({slug}, subject) for _sha, subject in merges)


def check_rebased_copy(inv, lines, files, cand):
    """True when <cand> is a rebased copy of a commit with these patch lines and files.

    TOOL-dSweptBranches-9: a shared subject proves nothing on its own. Two one-line edits of
    unrelated lines differ by exactly 4, which an absolute drift bound accepts, and a binary-only
    commit has no lines at all. So the copy must touch the same files, and the lines the two share
    must outnumber the lines that drifted, which also refuses an empty patch: none shared is never
    more than the drift.
    """
    other = read_patch_lines(inv, cand)
    if read_files(inv, cand) != files:
        return False
    drift = sum(((lines - other) + (other - lines)).values())
    return drift <= DRIFT_LINES and sum((lines & other).values()) > drift


def derive_coverage(inv, tip):
    """-> what covers each unique commit of <tip>, or why that could not be read. Cached by tip."""
    def load():
        root, dref = inv["root"], inv["default_ref"]
        mb = read_git(root, "merge-base", dref, tip)
        if not mb:
            return {"error": f"shares no history with {inv['branch']}"}
        rc, out = run_git(root, "rev-list", "--parents", f"{dref}..{tip}")
        if rc != 0:
            return {"error": "git rev-list failed"}
        commits = [line.split() for line in out.splitlines() if line.strip()]
        unique = {c[0] for c in commits}
        applied = {line[2:].strip() for line in read_git(root, "cherry", dref, tip).splitlines()
                   if line.startswith("- ")}
        by_subject, merges = read_side(inv, mb)
        mem = read_memory_root(inv)
        run_re = re.compile(rf"^{re.escape(mem)}/builds/([A-Za-z0-9]+)/RUN(\.[^/]*)?\.md$")
        counts, landings, uncovered, slugs = {}, set(), [], set()
        for c in commits:
            sha, parents = c[0], c[1:]
            subject = read_git(root, "log", "-1", "--format=%s", sha)
            slugs |= {n for n in derive_names(subject) if not ID_RE.fullmatch(n)}
            how = None
            if len(parents) > 1:
                if all(p in unique or check_ancestor(inv, p) for p in parents):
                    how = "merge"
            elif sha in applied:
                how = "patch-id"
            else:
                lines = read_patch_lines(inv, sha)
                files = read_files(inv, sha)
                for cand in by_subject.get(subject, []):
                    if check_rebased_copy(inv, lines, files, cand):
                        how = "patch"
                        break
                names = derive_names(subject)
                if how is None and names:
                    for msha, msubject in merges:
                        if check_names(names, msubject) and files <= read_files(inv, msha, True):
                            how = "landing"
                            landings.add(msha[:12])
                            break
                if how is None and files and all(run_re.match(f) for f in files):
                    if all(check_build_landed(inv, run_re.match(f).group(1), merges) for f in files):
                        how = "records"
                if how is None and files and all(f.startswith(mem + "/") for f in files):
                    rows = derive_row_lines(lines)
                    if rows and all(check_row_on_default(inv, r) for r in sorted(rows)):
                        how = "rotated"
            if how is None:
                uncovered.append((sha, subject))
            else:
                counts[how] = counts.get(how, 0) + 1
        return {"error": "", "unique": len(commits), "counts": counts, "landings": sorted(landings),
                "uncovered": uncovered, "slugs": sorted(slugs)}
    return read_cached(inv, ("coverage", tip), load)


def check_noop(inv, tip):
    """The merge-tree proof: merging <tip> into the default branch yields the default's own tree.

    Only ever a POSITIVE proof. Its conflict count is never read: a stale branch whose every commit
    landed conflicts heavily, so the count separates nothing.
    """
    def load():
        tree = read_git(inv["root"], "rev-parse", inv["default_ref"] + "^{tree}")
        # THE CAPABILITY IS PROBED ONCE, on the default merged with itself, because a per-tip
        # failure is also what unrelated histories produce, and that is no statement about git.
        able = read_cached(inv, "merge-tree", lambda: run_git(
            inv["root"], "merge-tree", "--write-tree", inv["default_ref"], inv["default_ref"])[0] == 0)
        if not able:
            inv["skips"]["merge-tree no-op proof"] = "this git has no `merge-tree --write-tree`"
            return False
        rc, out = run_git(inv["root"], "merge-tree", "--write-tree", inv["default_ref"], tip)
        return rc == 0 and out.split("\n", 1)[0].strip() == tree
    return read_cached(inv, ("noop", tip), load)


# ------------------------------------------------------------------------------- the verdict seam
# One function per predicate, each returning (verdict, evidence) or None for "not decided". The
# ladder reads them in order and falls to UNKNOWN (TOOL-dSweptBranches-2).

TEST_CASE_RES = [re.compile(r"^\s*def (test_\w+)\s*\(", re.M),
                 re.compile(r"\b(?:it|test)\(\s*[\"']([^\"']+)[\"']"),
                 re.compile(r"^\s*arm\s+\"([^\"]+)\"", re.M)]


def scan_test_cases(text):
    """-> the sorted names of every test case <text> declares."""
    return sorted({m for rx in TEST_CASE_RES for m in rx.findall(text)})


def check_probe_landed(inv, path):
    """True when the untracked file at <path> declares test cases and every non-blank line of it,
    stripped, exists in a default-branch file naming one of those cases: its case and its body landed.

    TOOL-dSweptBranches-10. A name alone proves nothing — `it("works")` is in half the suites ever
    written, and `test_parse` is a prefix of `test_parse_args`. The body check needs no separate
    declaration anchor: the line declaring each case is itself one of the probe's lines, so it must
    exist, whole, in a file the name led to. The name only narrows which files are read.
    """
    try:
        text = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    names = scan_test_cases(text)
    if not names:
        return False
    files = set()
    for name in names:
        out = read_git(inv["root"], "grep", "-F", "-l", "-e", name, inv["default_ref"], "--")
        files.update(line.split(":", 1)[1] for line in out.splitlines() if ":" in line)
    landed = set()
    for f in sorted(files):
        landed |= {line.strip() for line in (read_at(inv, inv["default_ref"], f) or "").splitlines()}
    return all(line.strip() in landed for line in text.splitlines() if line.strip())


def read_newest_activity(inv, w):
    """-> the newest of the worktree's HEAD commit time, its index's mtime and each dirty path's mtime."""
    stamps = [w["ct"]]
    st = w["dirt"]
    if st is not None:
        index = read_git_path(w["path"], "index")
        paths = [index] if index is not None else []
        paths += [pathlib.Path(w["path"]) / p for p in st["changed"] + st["untracked"]]
        for p in paths:
            try:
                stamps.append(int(os.stat(p).st_mtime))
            except OSError:
                pass
    return max(stamps)


def check_worktree(inv, item):
    """A worktree's activity and content, decided before its HEAD's ref ladder.

    It is IN-PROGRESS when it is the tree the report was run from, or when anything in it moved inside
    the freshness bound. Otherwise each piece of its content must already exist on the default branch;
    covered content is recorded on the item and the HEAD's verdict decides the row.
    """
    w = item.get("worktree")
    if w is None:
        return None
    if w["invoking"]:
        return IN_PROGRESS, "the worktree this report was run from"
    if w.get("foreign"):
        return UNKNOWN, f"not provably this repository's worktree: {w['foreign']}"
    if inv["now"] - read_newest_activity(inv, w) < inv["fresh"]:
        return IN_PROGRESS, f"activity inside the {inv['fresh'] / 3600:g}h freshness bound"
    st = w["dirt"]
    if st is None:
        # UNDECIDED IS NEVER "NO OBJECTION" (TOOL-dSweptBranches-7). A directory whose status could
        # not be read holds content nobody graded; only a worktree whose path is gone falls through
        # to its HEAD's verdict, to be pruned.
        if os.path.lexists(w["path"]) and "bare" not in w["flags"]:
            return UNKNOWN, "worktree status could not be read; its content is ungraded"
        return None
    covered, uncovered, unknown = [], [], []
    if st["merge"]:
        if check_ancestor(inv, st["merge"]):
            covered.append(f"the merge's other side {st['merge'][:12]} landed")
        else:
            uncovered.append(f"a merge of {st['merge'][:12]} in progress")
    if st["rebase"]:
        unknown.append("a rebase in progress")
    if st["drift"]:
        unknown.append(f"submodule pointer drift {st['drift']}")
    tree = read_default_tree(inv)
    files = [p for p in sorted(set(st["changed"])) if (pathlib.Path(w["path"]) / p).is_file()]
    probes = [p for p in st["untracked"] if not p.endswith("/")]
    unknown += [f"untracked directory {p}" for p in st["untracked"] if p.endswith("/")]
    blobs = read_git(w["path"], "hash-object", "--", *(files + probes)).split() \
        if files + probes else []
    if len(blobs) != len(files + probes):
        return UNKNOWN, "git hash-object failed over the worktree's content"
    have = dict(zip(files + probes, blobs))
    for p in sorted(set(st["changed"])):
        if have.get(p) == tree.get(p) or (p not in have and p not in tree
                                           and not (pathlib.Path(w["path"]) / p).exists()):
            covered.append(f"{p} matches {inv['branch']}")
        elif not st["drift"] or (pathlib.Path(w["path"]) / p).is_file():
            uncovered.append(f"changed {p}")
    default_blobs = set(tree.values())
    for p in probes:
        if have[p] in default_blobs:
            covered.append(f"untracked {p} exists on {inv['branch']}")
        elif check_probe_landed(inv, pathlib.Path(w["path"]) / p):
            covered.append(f"probe {p}: its case landed as a test")
        else:
            uncovered.append(f"untracked {p}")
    if unknown:
        return UNKNOWN, "content undecidable: " + ", ".join(unknown)
    if uncovered:
        more = f" (+{len(uncovered) - 3} more)" if len(uncovered) > 3 else ""
        return UNMERGED_LIVE, "uncovered content: " + ", ".join(uncovered[:3]) + more
    if covered:
        item["content"] = "content covered: " + ", ".join(covered)
    return None


def check_stash(inv, item):
    """A stash entry is SUPERSEDED when every path it changed already holds its bytes on the default."""
    if item["kind"] != "stash":
        return None
    root, w = inv["root"], item["tip"]
    if check_ref(root, f"{w}^3"):
        return UNKNOWN, "it carries untracked files"
    paths = [p for p in read_git(root, "diff", "--name-only", "--no-renames", f"{w}^1", w).splitlines()
             if p]
    tree = read_default_tree(inv)
    differ = [p for p in paths if (read_git(root, "rev-parse", "--verify", "--quiet", f"{w}:{p}")
                                   or None) != tree.get(p)]
    if paths and not differ:
        return SUPERSEDED, f"every path it changed ({len(paths)}) holds its bytes on {inv['branch']}"
    return UNKNOWN, f"{len(differ)} of {len(paths)} path(s) hold bytes {inv['branch']} does not"


def check_merged(inv, item):
    if item["tip"] and check_ancestor(inv, item["tip"]):
        return MERGED, f"an ancestor of {inv['branch']}"
    return None


def check_equivalent(inv, item):
    if not item["tip"]:
        return None
    lines = [line for line in read_git(inv["root"], "cherry", inv["default_ref"], item["tip"])
             .splitlines() if line.strip()]
    if lines and all(line.startswith("- ") for line in lines):
        return EQUIVALENT, f"git cherry: all {len(lines)} commit(s) already applied"
    return None


def check_superseded(inv, item):
    if not item["tip"]:
        return None
    if check_noop(inv, item["tip"]):
        return SUPERSEDED, f"merge-tree no-op: merging it into {inv['branch']} yields {inv['branch']}'s tree"
    cov = derive_coverage(inv, item["tip"])
    if cov["error"] or cov["uncovered"] or not cov["unique"]:
        return None
    parts = [f"{k} {cov['counts'][k]}" for k in ("patch-id", "patch", "landing", "records",
                                                  "rotated", "merge") if k in cov["counts"]]
    landed = f" (landing {' '.join(cov['landings'])})" if cov["landings"] else ""
    return SUPERSEDED, f"covered: {', '.join(parts)}{landed}"


def check_in_progress(inv, item):
    """A run record with a live lease, a build not yet closed, or a tip inside the freshness bound."""
    if not item["tip"]:
        return None
    cov = derive_coverage(inv, item["tip"])
    mem = read_memory_root(inv)
    hours = f"{inv['fresh'] / 3600:g}h"
    for slug in cov.get("slugs", []):
        run = read_at(inv, item["tip"], f"{mem}/builds/{slug}/RUN.md")
        phase, lease = read_run_fact(run, "phase"), read_run_fact(run, "lease-utc")
        if phase and phase not in ("LANDED", "ABORTED") and lease:
            try:
                at = datetime.datetime.strptime(lease, "%Y-%m-%dT%H:%M:%SZ").replace(
                    tzinfo=datetime.timezone.utc).timestamp()
            except ValueError:
                at = 0
            if inv["now"] - at < inv["fresh"]:
                return IN_PROGRESS, f"run {slug} at {phase}, its lease inside the {hours} bound"
        readme = read_at(inv, item["tip"], f"{mem}/builds/{slug}/README.md")
        m = re.search(r"\*\*Build status:\*\* ([A-Z]+)", readme or "")
        if m and m.group(1) not in ("CLOSED", "WONTDO"):
            there = re.search(r"\*\*Build status:\*\* ([A-Z]+)",
                              read_at(inv, inv["default_ref"], f"{mem}/builds/{slug}/README.md") or "")
            if not there or there.group(1) not in ("CLOSED", "WONTDO"):
                return IN_PROGRESS, f"build {slug} is {m.group(1)}"
    if item["ct"] and inv["now"] - item["ct"] < inv["fresh"]:
        return IN_PROGRESS, f"tip committed inside the {hours} freshness bound"
    return None


def check_unmerged_live(inv, item):
    if not item["tip"]:
        return None
    cov = derive_coverage(inv, item["tip"])
    if cov["error"]:
        return UNKNOWN, cov["error"]
    if cov["uncovered"]:
        sha, subject = cov["uncovered"][0]
        return UNMERGED_LIVE, (f"{len(cov['uncovered'])} of {cov['unique']} unique commit(s) uncovered, "
                               f"first {sha[:12]} {subject}")
    return None


PREDICATES = [check_worktree, check_stash, check_merged, check_equivalent, check_superseded,
              check_in_progress, check_unmerged_live]


def derive_verdict(inv, item):
    """The first predicate that decides, with any covered worktree content prefixed to its evidence."""
    for pred in PREDICATES:
        try:
            got = pred(inv, item)
        except (OSError, ValueError, KeyError, IndexError) as exc:
            inv["skips"][pred.__name__] = f"raised {type(exc).__name__} on at least one row"
            return UNKNOWN, f"{pred.__name__} could not run"
        if got is not None:
            verdict, evidence = got
            if item.get("content"):
                evidence = f"{item['content']} · {evidence}"
            return verdict, evidence
    return UNKNOWN, "no predicate decided"


def derive_action(inv, row, kept_branches):
    """-> what write mode does with a row: `remove worktree`, `delete branch`,
    `delete remote branch (--remote)`, or `keep` with its reason. The default branch is excluded by
    NAME before the verdict is read (TOOL-dSweptBranches-3)."""
    kind, name, verdict = row["kind"], row["name"], row["verdict"]
    if kind == "stash":
        return "keep (a stash entry is never deleted)"
    if (kind == "local" and name in inv["default_names"]) or \
            (kind == "remote" and name in [f"{inv['remote']}/{n}" for n in inv["default_names"]]):
        return "keep (the default branch)"
    if kind == "worktree/primary":
        return "keep (the primary worktree)"
    if verdict not in DELETABLE:
        return "keep"
    if kind.startswith("worktree/"):
        return "remove worktree"
    if kind == "local":
        return "keep (checked out in a kept worktree)" if name in kept_branches else "delete branch"
    return "delete remote branch (--remote)"


# ------------------------------------------------------------------------------- the remover
# TOOL-dSweptBranches-4. Every trap below was measured on adopter ic's node on 2026-10-13: git's removal
# fails with "Result too large" on deep node_modules; a clean removal often leaves an empty skeleton
# of pnpm links made under MSYS whose targets are POSIX paths; .NET Directory.Delete and
# `cmd rmdir /s /q` both refuse those links; GNU `rm -rf`, which never follows a link, removes them.

RM_NAME = "rm"
FILE_ATTRIBUTE_REPARSE_POINT = 0x400
BUSY_MARKERS = ("Device or resource busy", "EBUSY")


def run_worktree_remove(root, path):
    """-> (returncode, stderr) of `git worktree remove --force --force <path>`."""
    try:
        p = subprocess.run(["git", "-C", str(root), "worktree", "remove", "--force", "--force",
                            str(path)], capture_output=True)
    except OSError as exc:
        return 127, str(exc)
    return p.returncode, p.stderr.decode("utf-8", errors="replace").strip()


def run_rm(rm, path):
    """-> (returncode, stderr) of GNU `rm -rf -- <path>`."""
    try:
        p = subprocess.run([rm, "-rf", "--", str(path)], capture_output=True)
    except OSError as exc:
        return 127, str(exc)
    return p.returncode, p.stderr.decode("utf-8", errors="replace").strip()


def check_holds_file(path):
    """True when a regular file sits anywhere under <path>. Follows no link and no junction: a
    reparse point is neither descended nor counted, and no link is ever resolved. An entry that
    cannot be read counts as a file, so doubt keeps the directory. Stops at the first file."""
    stack = [str(path)]
    while stack:
        try:
            entries = list(os.scandir(stack.pop()))
        except OSError:
            return True
        for e in entries:
            try:
                st = e.stat(follow_symlinks=False)
            except OSError:
                return True
            if getattr(st, "st_file_attributes", 0) & FILE_ATTRIBUTE_REPARSE_POINT or e.is_symlink():
                continue
            if e.is_dir(follow_symlinks=False):
                stack.append(e.path)
            elif e.is_file(follow_symlinks=False):
                return True
    return False


def derive_rm_failure(err):
    line = (err.splitlines() or ["rm failed"])[-1]
    if any(m in err for m in BUSY_MARKERS):
        return "busy", f"busy: a process holds it, likely as its working directory ({line})"
    return "failed", line


def remove_worktree(root, path):
    """-> (result, detail), result one of removed, busy, kept or failed.

    git's removal first. On its failure, `rm -rf` and `git worktree prune`. A directory that survives
    a clean removal is a skeleton candidate, removed only when it holds no regular file.
    """
    # A registered worktree whose directory is gone needs no special case: git's own removal drops
    # it, measured. PROVED BEFORE git's removal runs, because a removal that fails part-way may already have
    # taken the .git file the proof reads (TOOL-dSweptBranches-8).
    foreign = check_worktree_identity(root, path)
    rc, err = run_worktree_remove(root, path)
    rm = shutil.which(RM_NAME)
    how = "git worktree remove"
    if rc != 0:
        first = (err.splitlines() or ["no message"])[-1]
        if foreign:
            return "failed", (f"git worktree remove failed ({first}) and the path is not provably "
                              f"this repository's worktree ({foreign}), so no rm -rf ran")
        if not rm:
            return "failed", (f"skipped — git worktree remove failed ({first}) and `{RM_NAME}` is "
                              "not on PATH, so no fallback ran")
        rc, err = run_rm(rm, path)
        run_git(root, "worktree", "prune")
        if rc != 0:
            return derive_rm_failure(err)
        how = f"rm -rf after git refused ({first})"
    if os.path.lexists(path):
        if check_holds_file(path):
            return "kept", "kept · it still holds a regular file, so it is no empty skeleton"
        if not rm:
            return "failed", f"skipped — an empty skeleton survived and `{RM_NAME}` is not on PATH"
        rc, err = run_rm(rm, path)
        if rc != 0:
            return derive_rm_failure(err)
        how += ", then its empty skeleton with rm -rf"
    return "removed", how


# ------------------------------------------------------------------------------- write mode
# TOOL-dSweptBranches-3. Deletes only, of the three landed verdicts, after a recovery manifest is on
# disk. It never merges, commits, checks out or pushes the default branch; its one push is a delete.

WRITE_TRACE = []  # every mutation in order, the manifest first: the self-test reads the order


def write_manifest(inv):
    """Write every tip and worktree HEAD under the git common dir, flushed, before any deletion."""
    common = read_git(inv["root"], "rev-parse", "--git-common-dir")
    if not common:
        raise Refusal("cannot resolve the git common directory, so no recovery manifest can be written")
    base = pathlib.Path(common)
    base = (base if base.is_absolute() else pathlib.Path(inv["root"]) / base) / "branch-reconcile"
    base.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path, n = base / f"recovery-{stamp}.txt", 1
    while path.exists():
        n += 1
        path = base / f"recovery-{stamp}-{n}.txt"
    lines = [f"# branch-reconcile recovery manifest · {stamp} · {inv['remote'] or 'no remote'}/"
             f"{inv['branch']} at {inv['default_tip']}",
             "# restore a branch: git branch <name> <sha> · a worktree: git worktree add <path> <sha>"]
    lines += [f"branch {r['name']} {r['tip']}" for r in inv["refs"] if r["kind"] == "local"]
    lines += [f"remote {r['name']} {r['tip']}" for r in inv["refs"] if r["kind"] == "remote"]
    lines += [f"stash {s['name']} {s['tip']}" for s in inv["stash"]]
    lines += [f"worktree {w['path']} {w['head'] or 'none'}" for w in inv["worktrees"]]
    try:
        with open(path, "x", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(lines) + "\n")
            f.flush()
            os.fsync(f.fileno())
    except OSError as exc:
        raise Refusal(f"the recovery manifest could not be written, so nothing was deleted: {exc}")
    WRITE_TRACE.append(("manifest", str(path)))
    return path


def write_deletions(inv, rows, remote_too):
    """Act on the rows' actions: worktrees, then local branches, then ONE remote push. -> exit code."""
    root, failed = inv["root"], False
    print(f"manifest — {write_manifest(inv)}")
    for r in rows:
        if r["action"] != "remove worktree":
            continue
        WRITE_TRACE.append(("remove-worktree", r["name"]))  # recorded BEFORE the act it orders
        result, detail = remove_worktree(root, r["item"]["worktree"]["path"])
        failed = failed or result == "failed"
        print(f"{result} — worktree {r['name']} · {detail}")
    run_git(root, "worktree", "prune")
    out = run_git(root, "worktree", "list", "--porcelain", "-z")[1]
    still = {w["branch"] for w in parse_worktrees(out) if w["branch"]}
    for r in rows:
        if r["action"] != "delete branch":
            continue
        if r["name"] in still or r["name"] in inv["default_names"]:
            print(f"kept — branch {r['name']} · still checked out in a worktree")
            continue
        # COMPARE BEFORE DELETE (TOOL-dSweptBranches-13): the verdict was graded on r["tip"], and a
        # branch that moved since holds work nobody graded.
        now = read_git(root, "rev-parse", "--verify", "--quiet", "refs/heads/" + r["name"])
        if now != r["tip"]:
            print(f"kept — branch {r['name']} · moved since it was graded "
                  f"({r['tip'][:12]} -> {now[:12] or 'gone'})")
            continue
        WRITE_TRACE.append(("delete-branch", r["name"]))
        rc, _out = run_git(root, "branch", "-D", "--", r["name"])
        failed = failed or rc != 0
        print(f"{'deleted' if rc == 0 else 'failed'} — branch {r['name']} · was {r['tip'][:12]}")
    graded = {r["name"][len(inv["remote"]) + 1:]: r["tip"] for r in rows
              if r["action"] == "delete remote branch (--remote)"}
    names = [n for n in graded if n not in inv["default_names"]]
    if remote_too and names:
        WRITE_TRACE.append(("push-delete", tuple(names)))
        # ONE push, EACH REF UNDER ITS OWN LEASE on the tip it was graded at (TOOL-dSweptBranches-13):
        # the tracking ref may be stale, and a delete must never take a tip nobody graded. Not
        # --atomic, so a refused ref keeps only itself.
        leases = [f"--force-with-lease=refs/heads/{n}:{graded[n]}" for n in names]
        try:
            p = subprocess.run(["git", "-C", str(root), "push", "--porcelain", *leases, inv["remote"],
                                *[f":refs/heads/{n}" for n in names]], capture_output=True)
            out = p.stdout.decode("utf-8", errors="replace")
        except OSError as exc:
            out = ""
            print(f"failed — the push could not run: {exc}")
        done = {line.split("\t")[1].split(":refs/heads/", 1)[-1]: line[0] for line in out.splitlines()
                if line[:1] in "-!*=" and "\t:refs/heads/" in line}
        for n in names:
            ok = done.get(n) == "-"
            failed = failed or not ok
            print(f"{'deleted' if ok else 'failed'} — remote branch {inv['remote']}/{n} · was "
                  f"{graded[n][:12]}" + ("" if ok else " · refused: it moved since it was graded, or "
                                         "the push failed"))
        print(f"push — one push carried {len(names)} remote branch deletion(s) to {inv['remote']}")
    elif names:
        print(f"kept — {len(names)} deletable remote branch(es): --remote deletes them in one push")
    return 1 if failed else 0


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
                     "ct": w["ct"], "evidence": " · ".join(p for p in pieces if p), "item": item})
    for r in inv["refs"] + inv["stash"]:
        item = dict(r)
        verdict, evidence = derive_verdict(inv, item)
        rows.append({"verdict": verdict, "kind": r["kind"], "name": r["name"], "tip": r["tip"],
                     "ct": r["ct"], "evidence": evidence, "item": item})
    # A branch stays while any worktree that keeps it checked out stays: git refuses to delete it.
    wt_rows = [r for r in rows if "worktree" in r["item"]]
    for r in wt_rows:
        r["action"] = derive_action(inv, r, set())
    # A WORKTREE THAT CONTAINS A KEPT WORKTREE IS KEPT (closing review round 1, B1). read_dirt hides
    # a nested worktree from its container's untracked content, so removing the container would take
    # the kept one with it. Containment is transitive, so one pass over the kept set suffices.
    held = [r["item"]["worktree"]["path"] for r in wt_rows if r["action"] != "remove worktree"]
    for r in wt_rows:
        if r["action"] == "remove worktree":
            inner = sorted(p for p in held if check_under(p, r["item"]["worktree"]["path"]))
            if inner:
                r["action"] = f"keep (contains kept worktree {inner[0].replace(chr(92), '/')})"
    kept = {r["item"]["worktree"]["branch"] for r in wt_rows
            if r["action"] != "remove worktree" and r["item"]["worktree"]["branch"]}
    for r in rows:
        if "worktree" not in r["item"]:
            r["action"] = derive_action(inv, r, kept)
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
    ap.add_argument("--fresh-hours", type=float, default=FRESH_HOURS,
                    help=f"activity this recent reads IN-PROGRESS (default: {FRESH_HOURS:g})")
    ap.add_argument("--write", action="store_true",
                    help="remove the MERGED, EQUIVALENT and SUPERSEDED worktrees and local branches")
    ap.add_argument("--remote", action="store_true",
                    help="with --write, also delete those remote branches, in one push")
    args = ap.parse_args(argv)
    if args.remote and not args.write:
        print("branch-reconcile: --remote deletes only under --write", file=sys.stderr)
        return 2
    try:
        inv = read_inventory(pathlib.Path(args.root))
        inv["fresh"] = args.fresh_hours * 3600
        rows = build_rows(inv)
        lines = render_report(inv, rows)
        print("\n".join(lines))
        if args.write:
            return write_deletions(inv, rows, args.remote)
    except Refusal as exc:
        print(f"branch-reconcile: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8", errors="backslashreplace")
    sys.exit(main())
