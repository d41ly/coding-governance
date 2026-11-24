#!/usr/bin/env python3
"""claims.py — a stored claim keyed over its sources, and trusted by its key and its weakest source (TOOL-dDeclaredLoop-8).

    python claims.py key <source>...              # one key over the sources
    python claims.py key --stdin                  # one key per input line, the line's sources TAB-separated
    python claims.py verdict --stored <k> --class <c> [--recomputed <k>] [--at <iso>] [--bound <s>]
    python claims.py card-keys                    # the orientation card's two keys over this working directory
    python claims.py --fixture --plant <case>     # one fixture case
    python claims.py --selftest                   # every case

A SOURCE is a string, `<name>=<value>` (`commit`, `tree`, `base`, `toplevel`, `branch`, `dirty`,
`runstate`) or a ref as `<ref>@<sha>`. `derive_claim_key` keys a claim over its sources: `k1:` and the
first sixteen hex digits of the SHA-1 of the sources sorted bytewise and joined by NUL. A source the
caller could not read is spelled `<name>=?` or `<ref>@?`, and a key over one opens `k1:?` before its
digits, which `derive_claim_verdict` never reads as equal to anything. The age is never hashed: the
derivation's UTC time is stored beside the key as `at`, and the `remote` class's bound reads it.

`CLAIM_CLASSES` is the `[trust]` table's five source classes as data, strongest first: `history`,
`view`, `remote`, `provenance` and `typed`. A claim over several sources takes its weakest class, so
`--class` takes one class or several joined by commas. `derive_claim_verdict` answers `evidence` for
a `typed` claim or one with no recomputed key, since no deriver exists; `fresh` when the two keys are
equal, neither carries `?`, and, for `remote`, the claim's age is at most the bound the caller passes;
`re-derived` otherwise, the caller re-deriving the claim. This module holds no age bound: the
unattended driver's `RESUME_STALE_BOUND` is its caller's.

`card-keys` runs git in its own working directory and nowhere else, and prints four lines: `view <k>`,
`remote <k>`, `at <iso>` and `remote-cells` with the cells `CARD_CELL_CLASSES` joins to the `remote`
key. The view key is over `commit=` HEAD, `base=` the default branch's remote-tracking sha, `toplevel=`,
`branch=` and `dirty=<n>`, the inputs the card's `tree —` cell reads; the remote key is over every ref
under `refs/remotes/<remote>/` and under `refs/gov/` as `<ref>@<sha>`. The remote and the default
branch are the inline ladder's below, so this module names no remote.

`--fixture --plant <case>` runs one case of `PLANTS`, printing one `claims: <case> · ...` line ending
`held` or `MISSED`, and exits 0 when it held, 1 when it missed. The worktree case builds a scratch
repository with a bare remote and one linked worktree under the system temp folder and removes it.
`--selftest` runs every case through `loop_lib.run_selftest_cases`. Exit 2 is a usage error.

WHAT THIS DOES NOT CHECK: the cells whose inputs sit outside the commit and the refs, the CLI version,
the worktree list, the drift history, the auto-memory index and the health log, so a `fresh` view key
says nothing about them; that a stored key was derived over the sources its caller names; who acts on
a claim. It reads git alone and imports only `loop_lib` beside it, so it takes no kit edge.
"""
import argparse
import datetime
import hashlib
import os
import pathlib
import shutil
import stat
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
KIT = pathlib.Path(__file__).absolute().parent
if str(KIT) not in sys.path:
    sys.path.insert(0, str(KIT))
from loop_lib import run_selftest_cases  # noqa: E402
import atexit
import contextlib
import time


# >>> remove_tree_py — canonical copy: owned_scratch.py in gov's lib dir (byte-identical; gated)
# A TREE REMOVAL THAT NEVER SWALLOWS A READ-ONLY FILE (TOOL-dQuietDisk-9 S1). git writes its objects
# read-only, and on Windows an unlink of one raises, so `rmtree(..., ignore_errors=True)` left every
# fixture repository's objects in the temp folder. The hook clears the bit on the failing path and
# retries it once; a removal that still fails raises nothing and answers False, as `ignore_errors` did.
def remove_tree(path) -> bool:
    """`path` removed, read-only files included; True when it is gone. Never raises."""
    def set_writable(func, failed, _exc):
        try:
            os.chmod(failed, 0o700)
            func(failed)
        except OSError:
            pass
    try:
        shutil.rmtree(path, onexc=set_writable)
    except OSError:
        pass
    return not os.path.lexists(path)


@contextlib.contextmanager
def build_scratch_dir(prefix=None):
    """A fresh `tempfile.mkdtemp` directory for the `with` block, removed by `remove_tree` on exit."""
    made = tempfile.mkdtemp(prefix=prefix)
    try:
        yield made
    finally:
        remove_tree(made)
# <<< remove_tree_py

# >>> owned_work_py — canonical copy: owned_scratch.py in gov's lib dir (byte-identical; gated)
# THE OWNED ROOT A PROCESS SITS IN: the nearest of `path` and its parents named `gate-work.*` and
# holding an `owner` file, a bar's `$WORK` or a suite's own root (TOOL-dQuietDisk-9 S2).
def resolve_owned_work(path):
    """The owned `gate-work.*` directory at or above `path`, a pathlib.Path, or None."""
    here = pathlib.Path(path).absolute()
    for d in (here, *here.parents):
        if d.name.startswith("gate-work.") and (d / "owner").is_file():
            return d
    return None
# <<< owned_work_py

# >>> owned_tempdir_py — canonical copy: owned_scratch.py in gov's lib dir (byte-identical; gated)
# A PYTHON SUITE'S OWNED ROOT (TOOL-dQuietDisk-9 S2, S9). Nested in an owned root, a bar's or another
# suite's, it takes that temp dir and makes nothing. Otherwise it sweeps each dead `py:` owner's root
# of this repository, or of a common dir that names no directory, makes `gate-work.*` with an owner
# line and `tmp`, points `tempfile` and the `TMPDIR`, `TEMP` and `TMP` its children read there, and
# removes the whole root at exit. A kill leaves the root with its owner, for the next suite to sweep.
def read_pid_alive(pid) -> bool:
    """False only when `pid` is provably gone; any error reads as alive, so a sweep can only keep."""
    if os.name == "nt":
        # Never `os.kill` here: signal 0 on Windows is CTRL_C_EVENT, sent to the pid's console group.
        try:
            import ctypes
            k32 = ctypes.WinDLL("kernel32", use_last_error=True)
            k32.OpenProcess.restype = ctypes.c_void_p
            handle = k32.OpenProcess(0x1000, False, int(pid))  # PROCESS_QUERY_LIMITED_INFORMATION
            if not handle:
                return ctypes.get_last_error() != 87  # ERROR_INVALID_PARAMETER: no such process
            try:
                code = ctypes.c_ulong()
                if not k32.GetExitCodeProcess(ctypes.c_void_p(handle), ctypes.byref(code)):
                    return True
                return code.value == 259  # STILL_ACTIVE
            finally:
                k32.CloseHandle(ctypes.c_void_p(handle))
        except (OSError, AttributeError, ValueError):
            return True
    try:
        os.kill(int(pid), 0)
    except ProcessLookupError:
        return False
    except (OSError, ValueError):
        return True
    return True


def scan_dead_scratch(ambient, common) -> list:
    """Removes each `gate-work.*` directly under `ambient` whose owner names a dead `py:` pid and
    `common`, or an absolute common dir that names no directory; an empty `common` removes nothing.
    Returns the roots removed, and says one stderr line per root it sweeps."""
    removed = []
    if not common:
        return removed
    try:
        names = sorted(os.listdir(ambient))
    except OSError:
        return removed
    for name in names:
        root = os.path.join(ambient, name)
        if not name.startswith("gate-work.") or not os.path.isdir(root):
            continue
        try:
            with open(os.path.join(root, "owner"), encoding="utf-8") as fh:
                fields = fh.readline().rstrip("\r\n").split("\t")
        except (OSError, UnicodeDecodeError):
            continue
        pid = fields[0][3:] if fields[0].startswith("py:") else ""
        if len(fields) < 2 or not (pid.isascii() and pid.isdigit()):
            continue
        if fields[1] != common and (not os.path.isabs(fields[1]) or os.path.isdir(fields[1])):
            continue
        if read_pid_alive(int(pid)):
            continue
        print(f"owned-scratch: sweeping the scratch of a dead suite (pid {pid}): {root}", file=sys.stderr)
        if remove_tree(root):
            removed.append(root)
    return removed


def init_owned_tempdir() -> str:
    """The temp dir this process's scratch lands in, owned and removed at exit; see the block's head."""
    ambient = tempfile.gettempdir()
    if resolve_owned_work(ambient) is not None:
        tempfile.tempdir = ambient
        return ambient
    try:
        got = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                             capture_output=True, text=True, encoding="utf-8", errors="replace",
                             check=False, stdin=subprocess.DEVNULL)
        common = got.stdout.strip() if got.returncode == 0 else ""
    except OSError:
        common = ""
    scan_dead_scratch(ambient, common)
    root = tempfile.mkdtemp(prefix="gate-work.", dir=ambient)
    atexit.register(remove_tree, root)
    staged = os.path.join(root, f"owner.{os.getpid()}.tmp")
    with open(staged, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(f"py:{os.getpid()}\t{common}\t{int(time.time())}\n")
    os.replace(staged, os.path.join(root, "owner"))
    tmp = os.path.join(root, "tmp")
    os.mkdir(tmp)
    tempfile.tempdir = tmp
    for name in ("TMPDIR", "TEMP", "TMP"):
        os.environ[name] = tmp
    return tmp
# <<< owned_tempdir_py


SAY = "claims"
KEY_FORM = "k1:"
UNREAD = "?"
#: The `[trust]` table's five source classes, strongest first: (class, its members, how it is trusted).
CLAIM_CLASSES = (
    ("history", "a commit and its trailers, a verdict keyed by tree, BASE", "trusted for that commit or tree"),
    ("view", "the card's cells, LIVE.md, the plan view, generated regions", "trusted while the key matches"),
    ("remote", "leases, mailbox entries, run claims",
     "trusted while the key matches and its age is inside the caller's bound"),
    ("provenance", "the owner's verbatim words, a ratification through the guarded command, the policy file",
     "authoritative for intent"),
    ("typed", "status words an agent typed, README status, READY text, session logs, a compaction summary, "
              "auto-memory", "evidence only"),
)
#: Each card cell joined to one key by its class; `*` is every cell not named.
CARD_CELL_CLASSES = {"overlaps": "remote", "claims": "remote", "*": "view"}
#: `--plant`'s cases and what each owes.
PLANTS = {"key-stable": "the same sources keyed twice, in two orders: equal keys",
          "key-moves": "the base sha changed: different keys",
          "key-unread": "one source spelled ?: a k1:? key, and its verdict re-derived",
          "typed-evidence": "a typed claim with equal keys: evidence",
          "remote-aged": "a remote claim with equal keys, inside then past its bound: fresh, then re-derived",
          "card-keys-worktree": "a worktree whose HEAD differs from its primary's: the worktree's own view key"}
#: The sources the key cases share, the inputs a card's view key reads.
PLANT_SOURCES = ("commit=4f1c2b9d0e8a7f6c5b4a39281706f5e4d3c2b1a0", "base=0a1b2c3d4e5f60718293a4b5c6d7e8f901234567",
                 "toplevel=/scratch/tree", "branch=main", "dirty=0")


def derive_claim_key(sources):
    """`k1:` and sixteen hex digits over the sources sorted bytewise and joined by NUL; `k1:?` before the
    digits where a source is spelled `<name>=?` or `<ref>@?`."""
    raw = sorted(s.encode("utf-8") for s in sources)
    unread = any(s.endswith(("=" + UNREAD, "@" + UNREAD)) for s in sources)
    return KEY_FORM + (UNREAD if unread else "") + hashlib.sha1(b"\0".join(raw)).hexdigest()[:16]


def derive_weakest_class(claim_class):
    """The weakest of the comma-joined classes in `claim_class`; ValueError naming a class outside
    `CLAIM_CLASSES`."""
    order = [row[0] for row in CLAIM_CLASSES]
    names = [c.strip() for c in str(claim_class).split(",") if c.strip()]
    bad = [c for c in names if c not in order] or ([] if names else ["(none)"])
    if bad:
        raise ValueError("class %s is not one of %s" % (bad[0], ", ".join(order)))
    return max(names, key=order.index)


def derive_claim_verdict(stored, recomputed, claim_class, at, now, bound):
    """`evidence`, `fresh` or `re-derived` for a stored key against a recomputed one. `at` and `now` are
    datetimes and `bound` seconds, read for a `remote` claim alone; a `remote` claim missing any of the
    three cannot read `fresh`."""
    weakest = derive_weakest_class(claim_class)
    if weakest == "typed" or recomputed is None:
        return "evidence"
    if stored != recomputed or UNREAD in stored or UNREAD in recomputed:
        return "re-derived"
    if weakest == "remote" and (at is None or now is None or bound is None
                                or (now - at).total_seconds() > float(bound)):
        return "re-derived"
    return "fresh"


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


def derive_card_keys(where="."):
    """`{"view": k, "remote": k, "at": iso}` over the repository git finds from `where`: git runs there and
    nowhere else. An unreadable source is spelled `?`, and a refused remote ladder spells `remote=?`."""
    def read_git(*args):
        try:
            p = subprocess.run(["git", *args], cwd=where, capture_output=True, text=True,
                               encoding="utf-8", errors="replace")
        except OSError:
            return None
        return p.stdout.strip() if p.returncode == 0 else None

    at = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    remote, branch, _observed, refusal = resolve_remote(where)
    base = None
    if remote and branch:
        base = read_git("rev-parse", "-q", "--verify", "refs/remotes/%s/%s^{commit}" % (remote, branch))
    status = read_git("status", "--porcelain")
    view = ["commit=%s" % (read_git("rev-parse", "-q", "--verify", "HEAD^{commit}") or UNREAD),
            "base=%s" % (base or UNREAD),
            "toplevel=%s" % (read_git("rev-parse", "--show-toplevel") or UNREAD),
            "branch=%s" % (read_git("rev-parse", "--abbrev-ref", "HEAD") or UNREAD),
            "dirty=%s" % (UNREAD if status is None else len(status.splitlines()))]
    spaces = ["refs/gov/"] + (["refs/remotes/%s/" % remote] if remote else [])
    refs = None if refusal else read_git("for-each-ref", "--format=%(refname)@%(objectname)", *spaces)
    return {"view": derive_claim_key(view),
            "remote": derive_claim_key(refs.splitlines() if refs is not None else ["remote=" + UNREAD]),
            "at": at}


def run_worktree_plant():
    """The `card-keys-worktree` case: (observations, held). A primary tree with a bare remote and its
    default branch fetched, and one linked worktree carrying a commit the primary lacks; `card-keys` run
    in each, by this file's own CLI, must print two view keys over a read base that differ."""
    scratch = tempfile.mkdtemp(prefix="ck")
    env = {k: v for k, v in os.environ.items()
           if k not in ("GOV_REMOTE", "GOV_DEFAULT_BRANCH", "GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE")}
    env.update(GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@test", GIT_COMMITTER_NAME="t",
               GIT_COMMITTER_EMAIL="t@test")
    up, prim, wt, name = (os.path.join(scratch, "up.git"), os.path.join(scratch, "p"),
                          os.path.join(scratch, "w"), "up")

    def run_git(cwd, *args):
        subprocess.run(["git", "-c", "commit.gpgsign=false", *args], cwd=cwd, env=env, check=True,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")

    def read_view(tree):
        p = subprocess.run([sys.executable, str(pathlib.Path(__file__).absolute()), "card-keys"], cwd=tree,
                           env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
        return next((ln.split()[1] for ln in p.stdout.splitlines() if ln.startswith("view ")), "none")

    try:
        run_git(scratch, "init", "-q", "--bare", up)
        run_git(scratch, "init", "-q", "-b", "main", prim)
        run_git(prim, "commit", "-q", "--allow-empty", "--no-verify", "-m", "one")
        run_git(prim, "remote", "add", name, up)
        run_git(prim, "push", "-q", name, "main")
        run_git(prim, "fetch", "-q", name)
        run_git(prim, "symbolic-ref", "refs/remotes/%s/HEAD" % name, "refs/remotes/%s/main" % name)
        run_git(prim, "worktree", "add", "-q", "-b", "side", wt)
        run_git(wt, "commit", "-q", "--allow-empty", "--no-verify", "-m", "two")
        primary, worktree = read_view(prim), read_view(wt)
    except (OSError, subprocess.CalledProcessError) as e:
        return ["the scratch repository did not build: %s" % e], False
    finally:
        remove_tree(scratch)
    held = (primary.startswith(KEY_FORM) and worktree.startswith(KEY_FORM) and UNREAD not in primary + worktree
            and primary != worktree)
    return ["primary %s" % primary, "worktree %s" % worktree, "differ" if primary != worktree else "equal"], held


def run_claims_plant(case):
    """One case of `PLANTS`: its `claims: <case> · ...` line, and 0 when it held, 1 when it missed."""
    now = datetime.datetime.now(datetime.timezone.utc)
    key = derive_claim_key(PLANT_SOURCES)
    if case == "key-stable":
        again = derive_claim_key(tuple(reversed(PLANT_SOURCES)))
        seen, held = [key, again, "equal" if key == again else "different"], key == again
    elif case == "key-moves":
        moved = derive_claim_key(PLANT_SOURCES[:1] + ("base=1a1b2c3d4e5f60718293a4b5c6d7e8f901234567",)
                                 + PLANT_SOURCES[2:])
        seen, held = [key, moved, "equal" if key == moved else "different"], key != moved
    elif case == "key-unread":
        unread = derive_claim_key(PLANT_SOURCES[:1] + ("base=" + UNREAD,) + PLANT_SOURCES[2:])
        word = derive_claim_verdict(unread, unread, "view", None, None, None)
        seen, held = [unread, "verdict " + word], unread.startswith(KEY_FORM + UNREAD) and word == "re-derived"
    elif case == "typed-evidence":
        word = derive_claim_verdict(key, key, "view,typed", None, None, None)
        seen, held = [key, "verdict " + word], word == "evidence"
    elif case == "remote-aged":
        inside = derive_claim_verdict(key, key, "remote", now - datetime.timedelta(seconds=30), now, 60)
        past = derive_claim_verdict(key, key, "remote", now - datetime.timedelta(seconds=90), now, 60)
        seen, held = ["inside its bound %s" % inside, "past its bound %s" % past], (inside, past) == (
            "fresh", "re-derived")
    else:
        seen, held = run_worktree_plant()
    print("%s: %s · %s · %s" % (SAY, case, " · ".join(seen), "held" if held else "MISSED"))
    return 0 if held else 1


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(prog="claims.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--fixture", action="store_true", help="run one fixture case")
    ap.add_argument("--plant", choices=list(PLANTS))
    ap.add_argument("--selftest", action="store_true", help="run every fixture case")
    sub = ap.add_subparsers(dest="verb")
    key = sub.add_parser("key", help="print one key over the sources")
    key.add_argument("sources", nargs="*")
    key.add_argument("--stdin", action="store_true", help="one key per input line, its sources TAB-separated")
    ver = sub.add_parser("verdict", help="print evidence, fresh or re-derived")
    ver.add_argument("--stored", required=True)
    ver.add_argument("--class", dest="claim_class", required=True)
    ver.add_argument("--recomputed")
    ver.add_argument("--at")
    ver.add_argument("--bound", type=float)
    sub.add_parser("card-keys", help="print the card's view and remote keys over this working directory")
    args = ap.parse_args(argv)
    if args.selftest or args.fixture:
        init_owned_tempdir()
    if args.selftest:
        if args.fixture or args.plant or args.verb:
            ap.error("--selftest takes no verb and no plant")
        cases = [(p, ["--fixture", "--plant", p], 0, "%s: %s · " % (SAY, p), "· held") for p in PLANTS]
        return run_selftest_cases(main, cases, "%s: selftest" % SAY)
    if args.fixture != bool(args.plant) or (args.fixture and args.verb):
        ap.error("--fixture takes --plant <case> and no verb")
    if args.fixture:
        return run_claims_plant(args.plant)
    if args.verb == "key":
        if args.stdin == bool(args.sources):
            ap.error("key takes sources or --stdin, one of the two")
        if not args.stdin:
            print(derive_claim_key(args.sources))
            return 0
        for line in sys.stdin.buffer.read().decode("utf-8", errors="replace").splitlines():
            print(derive_claim_key([s for s in line.rstrip("\r").split("\t") if s]))
        return 0
    if args.verb == "verdict":
        try:
            at = datetime.datetime.fromisoformat(args.at) if args.at else None
            if at is not None and at.tzinfo is None:
                at = at.replace(tzinfo=datetime.timezone.utc)
            print(derive_claim_verdict(args.stored, args.recomputed, args.claim_class, at,
                                       datetime.datetime.now(datetime.timezone.utc), args.bound))
        except ValueError as e:
            print("%s: refused · %s" % (SAY, e))
            return 2
        return 0
    if args.verb == "card-keys":
        keys = derive_card_keys(os.getcwd())
        print("view %s\nremote %s\nat %s" % (keys["view"], keys["remote"], keys["at"]))
        print("remote-cells " + " ".join(c for c, k in CARD_CELL_CLASSES.items() if k == "remote"))
        return 0
    ap.error("a verb, key, verdict or card-keys, or --fixture --plant <case>, or --selftest")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
