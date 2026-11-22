r"""history_store -- one store of immutable history verdicts and one `cat-file --batch` reader
(TOOL-dQuietDisk-1).

The canonical copy. `<prefix>/lib/` is gov-internal and ships nothing, so this module travels WHOLE,
byte-identical, as the unattended kit's and the memory-tree kit's `history_store.py`, the two kits whose
history legs grade through it, and `<prefix>/lib/resolve-python.test.sh`'s parity table reds a copy
whose `history_store_py` block drifts. Each file carries the sibling-kit resolver, through which the
switch's policy read finds the policy kit, and the `git_env_leaks_py` block, the names every git child
of this module drops, each under its own parity row. Its bash face is `<prefix>/lib/history-store.sh`.

THE STORE. One leg's verdicts live under `<git common dir>/history-verdicts/v1/<leg>/`, beside the
reuse cache's `gate-cache` and never inside it:

    items/<key[0:2]>/<key>     history-verdict v1 <key> <body length>\n<body bytes>
    tips/<scope>               sha\t<tip>\n
    pruned                     empty; its mtime is the last prune

    key   = sha256("history-verdict v1\n" + leg + "\n" + code digest + "\n" + "\n".join(fields))
    code  = sha256 over sorted "<path>\0<sha256 of its working bytes>\n" for each code path
    scope = sha256(absolute git dir)[:16]

An item is immutable per key. Its fields are the commit and blob ids the item reads, never HEAD, and
the code digest hashes the grading code's WORKING bytes, so an edit to the checker or to a library it
sources moves every key, committed or not. A code path given relative names itself relative to the
repository, so every worktree of one repository shares the items; the tip is per worktree. A missing,
unreadable, truncated or foreign-version item reads as a miss, never as a verdict, and a code path that
does not read disables the store for the run. Every write stages a sibling `mkstemp` temp in the item's
own directory and moves it with `os.replace`, as the reuse cache's writer does, so two bars writing at
once lose nothing and leave no temp. `remove_aged` unlinks items older than 30 days by mtime, at most
once a day per leg, by the mtime of the `pruned` stamp. The policy key `tests.history-verdicts` is the
switch: `stored`, the default, or `regraded`, under which every read misses and nothing is written.

THE READER. `BatchReader(repo)` holds one `git cat-file --batch` process, started on the first
question. A `missing` or `ambiguous` reply is None. An end of stream or a header that does not parse
is a dead process, never a missing object: the reader restarts it once, and after a second death
answers each question by a one-shot spawn, as it answers a name holding a newline, since the protocol
is line-framed.

    python history_store.py --leg <leg> --code <path>... tip
    python history_store.py --leg <leg> --code <path>... lookup  < <item id>TAB<field>... lines
    python history_store.py --leg <leg> --code <path>... store [--tip <sha>]  < <item id>TAB<field>...TAB<body> lines
    python history_store.py --leg <leg> --code <path>... resolve
    python history_store.py --selftest

The CLI runs in the repository its working directory sits in, and `--code` may repeat. `lookup` prints
`<item id>TAB<hit|miss>TAB<body>` per line and one stderr line, `history-store: <leg> <hits> hit(s),
<misses> miss(es)`; `store` writes each item, then the tip, then prunes. A body is escaped one way,
`\\`, `\t` and `\n`. Exit 0, or 2 on a refusal. WHAT THIS DOES NOT CHECK: that the verdict an item holds
is right for the ids its key names, which is the writer's claim; and a forged item, which needs write
access to the git dir already.

THE EXPORT. Each verb reads the switch and the git dirs, 8 git processes, so the bash face's `init_hs`
runs `resolve` once and exports the line it prints as `HS_RESOLVED`: `history-store-resolved v1`, the
key, the mode, the git dir, the common dir and the switch's escaped note, tab-separated. The key is
`os.path.normcase` of the absolute directory it was resolved in, and every other verb reads the export
only where its own working directory has that key, its tag and six fields read, and under `stored`
both dirs are directories; any other value is resolved afresh, so a wrong one costs a saving, never a
verdict. `resolve` never reads the export and prints nothing on stderr; each verb prints the note.
WHAT THIS DOES NOT CHECK: a repository re-created at the same path while one shell holds the export.
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time
import atexit
import contextlib


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


# CPython writes bytecode beside the SOURCE, inside the tree a hook may be committing.
sys.dont_write_bytecode = True


# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — a `.governance/install.json` row whose `path` exists inside this tree and whose
       `source` ends in <home>/<anchor>, or a `rendered` row whose `source`, its template, sits
       directly under <home>/ and whose `path` names a file <anchor>. The only record of a RENAMED
       kit dir: no probe finds a memory-recall kit an adopter homed at `scripts/recall/`.
    2. probe — <here>/<home>/<anchor>, then <here>/../<home>/<anchor>.
    3. refuse — LookupError naming the three places looked; never a guessed prefix.
    A receipt row whose path escapes the tree or does not exist is skipped, never followed.
    """
    import json
    import pathlib
    here = pathlib.Path(here).absolute()  # never resolve(): a junction must not move it
    root = next((d for d in (here, *here.parents) if (d / ".git").exists()), here)
    receipt = root / ".governance" / "install.json"
    try:
        rows = json.loads(receipt.read_text(encoding="utf-8")).get("files") or []
    except (OSError, ValueError, AttributeError):
        rows = []
    for row in rows:
        if not isinstance(row, dict) or not row.get("path"):
            continue
        src = str(row.get("source") or "").split("/")
        made = row.get("role") == "rendered" and str(row["path"]).split("/")[-1] == anchor
        if src[-2:] != [home, anchor] and not (made and src[-2:-1] == [home]):
            continue
        hit = (root / str(row["path"])).absolute()
        if hit.is_file() and root in hit.parents and ".." not in hit.parts:
            return hit.parent
    probes = (here / home, here.parent / home)
    for cand in probes:
        if (cand / anchor).is_file():
            return cand
    raise LookupError("no %s kit holding %s in this install: looked in %s, %s and %s" % (
        home, anchor, receipt.as_posix(), probes[0].as_posix(), probes[1].as_posix()))
# <<< resolve_kit_dir


# >>> git_env_leaks_py -- canonical copy: git_env_leaks.py in the gov lib dir (byte-identical; gated)
# The eight location variables git EXPORTS to a hook, which reach any subprocess the hook starts and
# name another tree than the one a reader was pointed at; and the four pathspec-mode variables a
# caller can carry, which turn a `:(glob)` pathspec into a literal name that matches nothing.
GIT_ENV_LEAKS = (
    "GIT_DIR",
    "GIT_WORK_TREE",
    "GIT_INDEX_FILE",
    "GIT_OBJECT_DIRECTORY",
    "GIT_ALTERNATE_OBJECT_DIRECTORIES",
    "GIT_COMMON_DIR",
    "GIT_NAMESPACE",
    "GIT_PREFIX",
    "GIT_LITERAL_PATHSPECS",
    "GIT_GLOB_PATHSPECS",
    "GIT_NOGLOB_PATHSPECS",
    "GIT_ICASE_PATHSPECS",
)
# <<< git_env_leaks_py


# >>> history_store_py -- canonical copy: history_store.py in the gov lib dir (byte-identical; gated)
SAY = "history-store"
SCHEMA = "history-verdict v1"
#: The store's home under the git common dir. Its `v1` moves with SCHEMA, so an old store is never read.
HOME = ("history-verdicts", "v1")
LEG_RE = re.compile(r"[a-z0-9-]+")
TIP_RE = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")
POLICY_KEY = "tests.history-verdicts"
#: The switch's two values, its default first.
MODES = ("stored", "regraded")
AGE_LIMIT = 30 * 86400
PRUNE_EVERY = 86400
VERBS = ("tip", "lookup", "store", "resolve")
#: The first field of an `HS_RESOLVED` line; its `v1` moves with the line's shape.
RESOLVED_TAG = "history-store-resolved v1"
_UNESCAPES = {"\\": "\\", "t": "\t", "n": "\n"}
_ESCAPE_RE = re.compile(r"\\(.?)", re.S)


def derive_git_env() -> dict:
    """This process's environment less `GIT_ENV_LEAKS`, so `-C <repo>` names the tree every git child reads."""
    return {k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS}


def render_escaped(text: str) -> str:
    """A body as one line: a backslash, a tab and a newline escaped, and nothing else."""
    return text.replace("\\", "\\\\").replace("\t", "\\t").replace("\n", "\\n")


def parse_escaped(text: str) -> str:
    """The inverse of `render_escaped`. ValueError on a backslash it would not have written."""
    def read_escape(match):
        if match.group(1) not in _UNESCAPES:
            raise ValueError("a backslash before %r is no escape this store writes" % match.group(1))
        return _UNESCAPES[match.group(1)]
    return _ESCAPE_RE.sub(read_escape, text)


def parse_item(data: bytes, key: str) -> str | None:
    """The body an item file holds under `key`, or None where its header is not this schema's and this
    key's, or its body is not exactly the length the header names."""
    head, sep, body = data.partition(b"\n")
    want = ("%s %s " % (SCHEMA, key)).encode("ascii")
    if not sep or not head.startswith(want):
        return None
    size = head[len(want):]
    if not size.isdigit() or int(size) != len(body):
        return None
    try:
        return body.decode("utf-8")
    except UnicodeDecodeError:
        return None


def write_staged(path: pathlib.Path, data: bytes) -> bool:
    """Write `data` at `path` through a sibling `mkstemp` temp and `os.replace`; False where it did not
    land, the temp removed either way. A replace refused while another writer's rename of the same
    path holds it is retried briefly: on Windows a rename over a file being renamed is refused."""
    tmp = ""
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=str(path.parent), prefix=path.name + ".", suffix=".tmp")
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        for attempt in range(5):
            try:
                os.replace(tmp, str(path))
                tmp = ""
                return True
            except PermissionError:
                if attempt == 4:
                    raise
                time.sleep(0.02 * (attempt + 1))
    except OSError:
        return False
    finally:
        if tmp:
            try:
                os.remove(tmp)
            except OSError:
                pass
    return False


def derive_code_digest(repo: pathlib.Path, paths) -> str:
    """sha256 over the sorted `<path>\\0<sha256 of its working bytes>\\n` rows of the grading code. A
    relative path is read under `repo` and named as given; an absolute one inside `repo` is named
    relative to it. OSError where a path does not read."""
    rows = []
    for given in paths:
        full = pathlib.Path(given)
        name = full.as_posix()
        if full.is_absolute():
            try:
                name = full.relative_to(repo).as_posix()
            except ValueError:
                pass
        else:
            full = repo / full
        rows.append("%s\0%s\n" % (name, hashlib.sha256(full.read_bytes()).hexdigest()))
    return hashlib.sha256("".join(sorted(rows)).encode("utf-8")).hexdigest()


def read_policy_mode(repo: pathlib.Path) -> tuple[str, str]:
    """`(mode, note)`: `tests.history-verdicts` at `repo`, through the policy kit's `policy.py get`, the
    kit found by `resolve_kit_dir` beside this file. Its default where no policy kit resolves or the key
    does not read, the second with the one stderr line that says so as its note, returned, not printed;
    the note is "" otherwise."""
    try:
        kit = resolve_kit_dir("policy", "policy.py", pathlib.Path(__file__).absolute().parent)
    except LookupError:
        return MODES[0], ""
    try:
        got = subprocess.run([sys.executable, str(kit / "policy.py"), "get", POLICY_KEY], cwd=str(repo),
                             capture_output=True, text=True, encoding="utf-8", errors="replace",
                             stdin=subprocess.DEVNULL, env=derive_git_env())
    except OSError as exc:
        return MODES[0], "%s: %s did not read, so %s holds: %s" % (SAY, POLICY_KEY, MODES[0], exc)
    said = got.stdout.split()
    if got.returncode == 0 and len(said) == 1 and said[0] in MODES:
        return said[0], ""
    why = (got.stderr or got.stdout).strip().splitlines()
    return MODES[0], "%s: %s did not read, so %s holds: %s" % (
        SAY, POLICY_KEY, MODES[0], why[-1] if why else "exit %d" % got.returncode)


def read_resolved(repo) -> tuple[str, str, str, str]:
    """`(mode, note, git dir, common dir)` at `repo`, the two reads `resolve_store` makes, made once:
    the switch as `read_policy_mode` reads it, its note held, then, under `stored` only, one `rev-parse`
    for the absolute git dir and the common dir, made absolute. A rev-parse that fails leaves both
    dirs "", as does `regraded`, under which no git runs."""
    repo = pathlib.Path(repo).absolute()
    mode, note = read_policy_mode(repo)
    if mode != MODES[0]:
        return mode, note, "", ""
    try:
        got = subprocess.run(["git", "-C", str(repo), "rev-parse", "--absolute-git-dir", "--git-common-dir"],
                             capture_output=True, text=True, encoding="utf-8", errors="replace",
                             stdin=subprocess.DEVNULL, env=derive_git_env())
        lines = got.stdout.splitlines() if got.returncode == 0 else []
    except OSError:
        lines = []
    if len(lines) != 2:
        return mode, note, "", ""
    common = pathlib.Path(lines[1])
    if not common.is_absolute():
        common = repo / common
    return mode, note, lines[0], str(common)


def render_resolved(repo, resolved) -> str:
    """`resolved`, as `read_resolved` answers it for `repo`, as the one `HS_RESOLVED` line: the tag, the
    key, the mode, the git dir, the common dir and the escaped note, tab-separated. The key is
    `os.path.normcase` of `repo`'s absolute path. "" where the key or a dir holds a tab or a newline."""
    key = os.path.normcase(str(pathlib.Path(repo).absolute()))
    mode, note, git_dir, common = resolved
    if any(c in text for text in (key, git_dir, common) for c in "\t\n"):
        return ""
    return "\t".join((RESOLVED_TAG, key, mode, git_dir, common, render_escaped(note)))


def parse_resolved(text, repo):
    """The `(mode, note, git dir, common dir)` a `render_resolved` line holds, where it was rendered for
    `repo`: its tag this one, six fields, its key `repo`'s, its mode one of MODES and, under `stored`,
    both dirs absolute and directories. None for any other text, which means resolve afresh. The key is
    compared by rendering the answer again for `repo`, so `render_resolved` alone spells it."""
    cells = (text or "").split("\t")
    if len(cells) != 6 or cells[0] != RESOLVED_TAG or cells[2] not in MODES:
        return None
    try:
        if cells[2] == MODES[0] and not all(
                pathlib.Path(d).is_absolute() and pathlib.Path(d).is_dir() for d in cells[3:5]):
            return None
        held = cells[2], parse_escaped(cells[5]), cells[3], cells[4]
    except (OSError, ValueError):
        return None
    if render_resolved(repo, held) != text:
        return None
    return held


class BatchReader:
    """One `git -C <repo> cat-file --batch` process for a leg run, started on the first question (S2)."""

    def __init__(self, repo):
        self.repo = str(repo)
        self.proc = None
        self.deaths = 0

    def read(self, name: str) -> bytes | None:
        """The bytes of the object `name` names, or None where git answers `missing` or `ambiguous`."""
        got = self.read_reply(name, False)
        return None if got is None else got[1]

    def read_info(self, name: str) -> tuple[str, str, int] | None:
        """`(oid, type, size)` of the object `name` names, or None where git answers `missing` or `ambiguous`."""
        got = self.read_reply(name, True)
        return None if got is None else got[0]

    def read_reply(self, name: str, want_oid: bool):
        """`((oid, type, size), bytes)` or None, from the process while it has died fewer than twice."""
        if "\n" in name or "\r" in name:
            return self.run_oneshot(name, want_oid)
        while self.deaths < 2:
            reply = self.read_batch(name)
            if reply is not False:
                return reply
            self.remove()
            self.deaths += 1
        return self.run_oneshot(name, want_oid)

    def read_batch(self, name: str):
        """One question to the process: the reply, None on `missing` or `ambiguous`, False on a dead one."""
        try:
            if self.proc is None:
                self.proc = subprocess.Popen(["git", "-C", self.repo, "cat-file", "--batch"],
                                             stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                             stderr=subprocess.DEVNULL, env=derive_git_env())
            self.proc.stdin.write(name.encode("utf-8") + b"\n")
            self.proc.stdin.flush()
            head = self.proc.stdout.readline()
            if not head.endswith(b"\n"):
                return False
            if head.endswith((b" missing\n", b" ambiguous\n")):
                return None
            parts = head.split()
            if len(parts) != 3 or not parts[2].isdigit():
                return False
            size = int(parts[2])
            body = self.proc.stdout.read(size + 1)
            if len(body) != size + 1 or body[-1:] != b"\n":
                return False
            return (parts[0].decode("ascii"), parts[1].decode("ascii"), size), body[:-1]
        except (OSError, ValueError):
            return False

    def run_oneshot(self, name: str, want_oid: bool):
        """The safe fallback, not a second reader: `git cat-file -t`, then `git cat-file <type>`, and
        `git rev-parse --verify` where the oid is asked."""
        def run_git(*args):
            return subprocess.run(["git", "-C", self.repo, *args], capture_output=True,
                                  stdin=subprocess.DEVNULL, env=derive_git_env())
        kind = run_git("cat-file", "-t", name)
        if kind.returncode != 0:
            return None
        typ = kind.stdout.decode("ascii", "replace").strip()
        body = run_git("cat-file", typ, name)
        if body.returncode != 0:
            return None
        oid = ""
        if want_oid:
            got = run_git("rev-parse", "--verify", "--quiet", name)
            if got.returncode != 0:
                return None
            oid = got.stdout.decode("ascii", "replace").strip()
        return (oid, typ, len(body.stdout)), body.stdout

    def remove(self) -> None:
        """End the process, if one runs; the next question starts another."""
        proc, self.proc = self.proc, None
        if proc is None:
            return
        for stream in (proc.stdin, proc.stdout):
            try:
                stream.close()
            except OSError:
                pass
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()


class HistoryStore:
    """One leg's store as `resolve_store` resolved it for this run. Not `stored`, every read misses and
    nothing is written: the switch at `regraded`, or a store that could not resolve."""

    def __init__(self, root, leg: str, code: str, scope: str, stored: bool):
        self.root = pathlib.Path(root) if root else None
        self.leg, self.code, self.scope, self.stored = leg, code, scope, stored

    def derive_key(self, fields) -> str:
        """The item key of `fields`. ValueError on a field holding a newline, which would join two field
        lists to one key text."""
        fields = [str(f) for f in fields]
        if any("\n" in f for f in fields):
            raise ValueError("a field holding a newline would join two field lists to one key text")
        text = SCHEMA + "\n" + self.leg + "\n" + self.code + "\n" + "\n".join(fields)
        return hashlib.sha256(text.encode("utf-8")).hexdigest()

    def derive_item_path(self, key: str) -> pathlib.Path:
        return self.root / "items" / key[:2] / key

    def read(self, fields) -> str | None:
        """The body stored under `fields`, or None: a miss, a torn or foreign item, or the store off."""
        key = self.derive_key(fields)
        if not self.stored:
            return None
        try:
            data = self.derive_item_path(key).read_bytes()
        except OSError:
            return None
        return parse_item(data, key)

    def write(self, fields, body: str) -> bool:
        """Store `body` under `fields`; True where the item holds it after. An item already holding it is
        left as it is, so a warm run writes nothing."""
        key = self.derive_key(fields)
        if not self.stored:
            return False
        if self.read(fields) == body:
            return True
        data = body.encode("utf-8")
        head = ("%s %s %d\n" % (SCHEMA, key, len(data))).encode("ascii")
        return write_staged(self.derive_item_path(key), head + data)

    def read_tip(self) -> str | None:
        """This worktree's last graded tip for the leg, or None."""
        if not self.stored:
            return None
        try:
            text = (self.root / "tips" / self.scope).read_bytes().decode("utf-8")
        except (OSError, UnicodeDecodeError):
            return None
        if not text.startswith("sha\t") or not text.endswith("\n") or not TIP_RE.fullmatch(text[4:-1]):
            return None
        return text[4:-1]

    def write_tip(self, sha: str) -> bool:
        """Record `sha` as this worktree's last graded tip. ValueError on a value that is no full sha."""
        if not TIP_RE.fullmatch(sha or ""):
            raise ValueError("a tip is a full sha, not %r" % (sha,))
        if not self.stored:
            return False
        return write_staged(self.root / "tips" / self.scope, ("sha\t%s\n" % sha).encode("ascii"))

    def remove_aged(self) -> int:
        """Unlink each item older than AGE_LIMIT by mtime, at most once per PRUNE_EVERY, as the `pruned`
        stamp's mtime records; the count removed."""
        if not self.stored:
            return 0
        stamp = self.root / "pruned"
        now = time.time()
        try:
            if now - stamp.stat().st_mtime < PRUNE_EVERY:
                return 0
        except OSError:
            pass
        try:
            self.root.mkdir(parents=True, exist_ok=True)
            stamp.touch()
        except OSError:
            return 0
        cut, removed = now - AGE_LIMIT, 0
        items = self.root / "items"
        try:
            subs = [e.path for e in os.scandir(items) if e.is_dir() and len(e.name) == 2]
        except OSError:
            return 0
        for sub in subs:
            try:
                entries = list(os.scandir(sub))
            except OSError:
                continue
            for entry in entries:
                try:
                    if entry.is_file() and entry.stat().st_mtime < cut:
                        os.remove(entry.path)
                        removed += 1
                except OSError:
                    continue
        return removed


def resolve_store(repo, leg: str, code_paths, resolved=None) -> HistoryStore:
    """The store for one run of `leg` in the repository at `repo`, keyed by the working bytes of
    `code_paths`. ValueError on a leg that is not `[a-z0-9-]+` or no code path. The switch and the git
    dirs are `resolved`, as `read_resolved` answers them, which starts no git process, or else read
    once now; a repository git cannot name or a code path that does not read gives a store that is
    off, the reason on one stderr line, after the switch's note where it did not read."""
    if not isinstance(leg, str) or not LEG_RE.fullmatch(leg):
        raise ValueError("a leg is [a-z0-9-]+, not %r" % (leg,))
    paths = [str(p) for p in code_paths]
    if not paths:
        raise ValueError("a store needs the grading code's paths, so an edit to them moves every key")
    repo = pathlib.Path(repo).absolute()
    off = HistoryStore(None, leg, "", "", False)
    mode, note, git_dir, common = read_resolved(repo) if resolved is None else resolved
    if note:
        print(note, file=sys.stderr)
    if mode != MODES[0]:
        return off
    if not git_dir or not common:
        print("%s: %s: git names no git dir at %s, so this run regrades" % (SAY, leg, repo.as_posix()),
              file=sys.stderr)
        return off
    common = pathlib.Path(common)
    try:
        code = derive_code_digest(repo, paths)
    except OSError as exc:
        print("%s: %s: a code path does not read, so this run regrades: %s" % (SAY, leg, exc), file=sys.stderr)
        return off
    scope = hashlib.sha256(git_dir.encode("utf-8")).hexdigest()[:16]
    return HistoryStore(common.joinpath(*HOME, leg), leg, code, scope, True)


def run_git(repo, *args, data=None) -> bytes:
    """git in `repo`, its stdout; CalledProcessError on a failure. The self-test's one git runner."""
    return subprocess.run(["git", "-C", str(repo), *args], input=data, capture_output=True, check=True,
                          env=derive_git_env()).stdout


def build_scratch_repo(repo: pathlib.Path) -> pathlib.Path:
    """A repository on `main` holding twenty committed files and the code path `src/check.sh`."""
    repo.mkdir(parents=True)
    run_git(repo, "init", "-q", "-b", "main", ".")
    for key, value in (("core.autocrlf", "false"), ("user.name", "fx"), ("user.email", "fx@example.invalid"),
                       ("commit.gpgsign", "false")):
        run_git(repo, "config", key, value)
    (repo / "src").mkdir()
    (repo / "src" / "check.sh").write_bytes(b"echo graded\n")
    for i in range(20):
        (repo / ("f%02d.txt" % i)).write_bytes(("file %d\n" % i).encode("ascii") * (i + 1))
    run_git(repo, "add", "-A")
    run_git(repo, "commit", "-q", "--no-verify", "-m", "fixture")
    return repo


def test_reader(repo, check_arm) -> None:
    reader = BatchReader(repo)
    names = ["HEAD:f%02d.txt" % i for i in range(20)]
    want = {n: run_git(repo, "show", n) for n in names}
    got = {n: reader.read(n) for n in names}
    first = reader.proc
    check_arm("reader: twenty blobs read through one process each equal git show",
              got == want and first is not None and reader.proc is first and reader.deaths == 0,
              "deaths %d, %d of 20 equal" % (reader.deaths, sum(got[n] == want[n] for n in names)))
    check_arm("reader: a missing name is None and is no death",
              reader.read_info("HEAD:absent") is None and reader.read("HEAD:absent") is None
              and reader.proc is first and reader.deaths == 0, "deaths %d" % reader.deaths)
    oid = run_git(repo, "rev-parse", names[0]).decode("ascii").strip()
    info = reader.read_info(names[0])
    check_arm("reader: read_info answers the oid, the type and the size",
              info == (oid, "blob", len(want[names[0]])), "answered %r" % (info,))
    reader.proc.kill()
    reader.proc.wait()
    after = reader.read(names[1])
    check_arm("reader: an end of stream restarts the process once and still answers",
              after == want[names[1]] and reader.deaths == 1 and reader.proc is not None,
              "deaths %d, answered %r" % (reader.deaths, after))
    reader.proc.kill()
    reader.proc.wait()
    again = reader.read(names[2])
    info = reader.read_info(names[3])
    check_arm("reader: after a second death each question is a one-shot spawn",
              again == want[names[2]] and reader.deaths == 2 and reader.proc is None
              and info is not None and info[1:] == ("blob", len(want[names[3]])),
              "deaths %d, answered %r and %r" % (reader.deaths, again, info))
    other = BatchReader(repo)
    check_arm("reader: a name holding a newline is asked by a one-shot spawn",
              other.read("HEAD:f00.txt\nHEAD:f01.txt") is None and other.proc is None, "a process started")
    reader.remove()
    other.remove()


def test_store(repo, check_arm) -> None:
    code = ["src/check.sh"]
    store = resolve_store(repo, "selftest-leg", code)
    fields = ["commit", "0" * 40, "blob", "1" * 40]
    body = "rc 0\tone\nwith a back\\slash"
    check_arm("store: a written item reads back", store.write(fields, body) and store.read(fields) == body,
              "read %r" % (store.read(fields),))
    path = store.derive_item_path(store.derive_key(fields))
    data = path.read_bytes()
    path.write_bytes(data[:-1])
    short = store.read(fields)
    path.write_bytes(data.replace(b"history-verdict v1 ", b"history-verdict v2 ", 1))
    foreign = store.read(fields)
    path.write_bytes(data)
    check_arm("store: an item cut one byte short, or of another version, is a miss",
              short is None and foreign is None and store.read(fields) == body,
              "short %r, foreign %r" % (short, foreign))
    check_path = repo / "src" / "check.sh"
    kept = check_path.read_bytes()
    check_path.write_bytes(kept + b"# an uncommitted edit\n")
    edited = resolve_store(repo, "selftest-leg", code)
    check_path.write_bytes(kept)
    check_arm("store: an uncommitted edit to a code path moves every key",
              edited.stored and edited.code != store.code and edited.read(fields) is None,
              "the digest did not move")
    gone = resolve_store(repo, "selftest-leg", ["src/absent.sh"])
    check_arm("store: a code path that does not read turns the store off",
              not gone.stored and gone.read(fields) is None and not gone.write(fields, body), "it stayed on")
    try:
        store.read(["a\nb"])
        refused = False
    except ValueError:
        refused = True
    temps = list((store.root / "items").rglob("*.tmp"))
    check_arm("store: a field holding a newline is refused and no temp is left", refused and not temps,
              "refused %s, temps %s" % (refused, temps))


def test_worktree_tips(repo, scratch, check_arm) -> None:
    code = ["src/check.sh"]
    tree = scratch / "wt"
    run_git(repo, "worktree", "add", "-q", "--detach", str(tree))
    one, two = resolve_store(repo, "selftest-tip", code), resolve_store(tree, "selftest-tip", code)
    head = run_git(repo, "rev-parse", "HEAD").decode("ascii").strip()
    one.write_tip(head)
    two.write_tip("f" * 40)
    check_arm("tip: each worktree reads back its own tip", one.read_tip() == head and two.read_tip() == "f" * 40,
              "read %r and %r" % (one.read_tip(), two.read_tip()))
    one.write(["shared"], "one")
    check_arm("items: an item written from one worktree is a hit in the other", two.read(["shared"]) == "one",
              "read %r" % (two.read(["shared"]),))


def test_prune(repo, check_arm) -> None:
    store = resolve_store(repo, "selftest-prune", ["src/check.sh"])
    now = time.time()
    paths = {}
    for name, days in (("old", 31), ("young", 29)):
        store.write([name], name)
        paths[name] = store.derive_item_path(store.derive_key([name]))
        os.utime(paths[name], (now - days * 86400, now - days * 86400))
    store.remove_aged()
    check_arm("prune: an item 31 days old goes and one 29 days old stays",
              not paths["old"].exists() and paths["young"].exists(), "old %s, young %s" % (
                  paths["old"].exists(), paths["young"].exists()))
    store.write(["later"], "later")
    later = store.derive_item_path(store.derive_key(["later"]))
    os.utime(later, (now - 31 * 86400, now - 31 * 86400))
    store.remove_aged()
    check_arm("prune: a second prune within the day removes nothing", later.exists(), "it pruned again")


def test_cli(repo, check_arm) -> None:
    head = run_git(repo, "rev-parse", "HEAD").decode("ascii").strip()
    body = "a\tb\nc\\d"
    argv = [sys.executable, str(pathlib.Path(__file__).absolute()), "--leg", "selftest-cli", "--code", "src/check.sh"]

    def run_cli(verb, data):
        return subprocess.run([*argv, *verb], cwd=str(repo), input=data.encode("utf-8"), capture_output=True,
                              env=derive_git_env())
    stored = run_cli(["store", "--tip", head], "i1\tc1\tb1\t%s\n" % render_escaped(body))
    looked = run_cli(["lookup"], "i1\tc1\tb1\ni2\tc9\n")
    tip = run_cli(["tip"], "")
    want = ("i1\thit\t%s\ni2\tmiss\t\n" % render_escaped(body)).encode("utf-8")
    check_arm("cli: store then lookup answers hit and miss, the body escaped, and tip the tip",
              stored.returncode == 0 and looked.stdout == want and tip.stdout.strip() == head.encode("ascii")
              and b"selftest-cli 1 hit(s), 1 miss(es)" in looked.stderr,
              "store rc %d, lookup %r, tip %r" % (stored.returncode, looked.stdout, tip.stdout))
    check_arm("cli: the escape reverses", parse_escaped(render_escaped(body)) == body
              and parse_escaped(looked.stdout.decode("utf-8").split("\t")[2].split("\n")[0]) == body, "it did not")
    refused = run_cli(["store"], "i1\tc1\tbad \\x escape\n")
    check_arm("cli: a body escaped another way is refused", refused.returncode == 2, "rc %d" % refused.returncode)


def test_resolved(repo, scratch, check_arm) -> None:
    code = ["src/check.sh"]
    held = read_resolved(repo)
    line = render_resolved(repo, held)
    cells = line.split("\t")
    bad = [render_resolved(scratch, held), line.replace(RESOLVED_TAG, "history-store-resolved v2", 1),
           "\t".join(cells[:5]), "\t".join(cells[:2] + ["kept"] + cells[3:]),
           "\t".join(cells[:3] + [str(repo / "absent")] + cells[4:])]
    check_arm("resolved: a held line keyed to another directory, or malformed, is not read",
              len(cells) == 6 and parse_resolved(line, repo) == held
              and all(parse_resolved(text, repo) is None for text in bad),
              "read %r" % ([parse_resolved(text, repo) for text in bad],))
    argv = [sys.executable, str(pathlib.Path(__file__).absolute()), "--leg", "selftest-held", "--code", *code]
    env = {k: v for k, v in derive_git_env().items() if k != "HS_RESOLVED"}
    fresh = subprocess.run([*argv, "resolve"], cwd=str(repo), capture_output=True, env=env)
    lied = subprocess.run([*argv, "resolve"], cwd=str(repo), capture_output=True,
                          env=dict(env, HS_RESOLVED="\t".join(cells[:2] + ["regraded", "", ""] + cells[5:])))
    text = fresh.stdout.decode("utf-8").rstrip("\n")
    real_run, spawned = subprocess.run, []

    def measure_run(*args, **kwargs):
        spawned.append(args)
        return real_run(*args, **kwargs)
    subprocess.run = measure_run
    try:
        again = resolve_store(repo, "selftest-held", code, parse_resolved(text, repo))
        quiet = len(spawned)
        want = resolve_store(repo, "selftest-held", code)
    finally:
        subprocess.run = real_run
    same = (again.stored, again.root, again.scope, again.code) == (want.stored, want.root, want.scope, want.code)
    check_arm("resolved: a resolve line read back in its own directory resolves the same store, no git run",
              fresh.returncode == 0 and not fresh.stderr and lied.stdout == fresh.stdout and same
              and quiet == 0 and len(spawned) > 0,
              "rc %d, stderr %r, spawned %d then %d, read %r" % (
                  fresh.returncode, fresh.stderr, quiet, len(spawned), text))


def test_switch(scratch, check_arm) -> None:
    try:
        resolve_kit_dir("policy", "policy.py", pathlib.Path(__file__).absolute().parent)
    except LookupError as exc:
        print("skip switch: no policy kit resolves beside this module, so the switch reads its default: %s" % exc)
        return
    repo = build_scratch_repo(scratch / "switch")
    code = ["src/check.sh"]
    resolve_store(repo, "selftest-switch", code).write(["item"], "verdict")
    (repo / ".governance").mkdir()
    (repo / ".governance" / "policy.toml").write_bytes(b'tests.history-verdicts = "regraded"\n')
    run_git(repo, "add", "-A")
    run_git(repo, "commit", "-q", "--no-verify", "-m", "regraded")
    off = resolve_store(repo, "selftest-switch", code)
    wrote = off.write(["other"], "x")
    tipped = off.write_tip("a" * 40)
    check_arm("switch: under regraded a stored item misses and nothing is written",
              not off.stored and off.read(["item"]) is None and not wrote and not tipped and off.read_tip() is None,
              "stored %s" % off.stored)
    run_git(repo, "rm", "-q", ".governance/policy.toml")
    run_git(repo, "commit", "-q", "--no-verify", "-m", "stored")
    back = resolve_store(repo, "selftest-switch", code)
    check_arm("switch: with the key gone the item is a hit again, and the off run wrote nothing",
              back.read(["item"]) == "verdict" and back.read(["other"]) is None and back.read_tip() is None,
              "read %r" % (back.read(["item"]),))


def run_selftest() -> int:
    """`--selftest`: the module's arms in a scratch repository of its own, one line per arm, then a count."""
    results = []

    def check_arm(name, ok, detail=""):
        results.append(bool(ok))
        print("%s %s%s" % ("ok  " if ok else "FAIL", name, "" if ok else " -- %s" % detail))
    init_owned_tempdir()
    scratch = pathlib.Path(tempfile.mkdtemp(prefix="history-store-"))
    try:
        repo = build_scratch_repo(scratch / "repo")
        test_reader(repo, check_arm)
        test_store(repo, check_arm)
        test_worktree_tips(repo, scratch, check_arm)
        test_prune(repo, check_arm)
        test_cli(repo, check_arm)
        test_resolved(repo, scratch, check_arm)
        test_switch(scratch, check_arm)
    finally:
        remove_tree(str(scratch))
    failed = results.count(False)
    print("%s selftest: %d arm(s), %d failed" % (SAY, len(results), failed))
    return 1 if failed or not results else 0


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--selftest"]:
        return run_selftest()
    leg, code, verb, tip, bad, i = "", [], "", None, "", 0
    while i < len(args):
        arg = args[i]
        if arg in ("--leg", "--tip") and i + 1 < len(args):
            leg, tip = (args[i + 1], tip) if arg == "--leg" else (leg, args[i + 1])
            i += 2
        elif arg == "--code":
            i += 1
            while i < len(args) and args[i] not in VERBS and not args[i].startswith("--"):
                code.append(args[i])
                i += 1
        elif arg in VERBS and not verb:
            verb, i = arg, i + 1
        else:
            bad = arg
            break
    if bad or not leg or not code or not verb or (tip is not None and verb != "store"):
        print("%s: usage: --leg <leg> --code <path>... (tip | lookup | store [--tip <sha>] | resolve)"
              " | --selftest%s" % (SAY, "; %r is no argument here" % bad if bad else ""), file=sys.stderr)
        return 2
    if tip is not None and not TIP_RE.fullmatch(tip):
        print("%s: --tip takes a full sha, not %r" % (SAY, tip), file=sys.stderr)
        return 2
    if verb == "resolve":
        line = render_resolved(os.getcwd(), read_resolved(os.getcwd()))
        sys.stdout.buffer.write(("%s\n" % line).encode("utf-8") if line else b"")
        return 0
    try:
        held = parse_resolved(os.environ.get("HS_RESOLVED", ""), os.getcwd())
        store = resolve_store(os.getcwd(), leg, code, held)
    except ValueError as exc:
        print("%s: %s" % (SAY, exc), file=sys.stderr)
        return 2
    if verb == "tip":
        sys.stdout.buffer.write(("%s\n" % store.read_tip()).encode("ascii") if store.read_tip() else b"")
        return 0
    try:
        lines = [line for line in sys.stdin.buffer.read().decode("utf-8").split("\n") if line]
        rows = []
        for n, line in enumerate(lines, 1):
            cells = line.split("\t")
            if verb == "store" and len(cells) < 2:
                raise ValueError("line %d holds no body" % n)
            fields = cells[1:-1] if verb == "store" else cells[1:]
            rows.append((cells[0], fields, parse_escaped(cells[-1]) if verb == "store" else None))
    except ValueError as exc:
        print("%s: %s: nothing written" % (SAY, exc), file=sys.stderr)
        return 2
    if verb == "store":
        for _item, fields, body in rows:
            store.write(fields, body)
        if tip:
            store.write_tip(tip)
        store.remove_aged()
        return 0
    out, hits = [], 0
    for item, fields, _body in rows:
        body = store.read(fields)
        hits += body is not None
        out.append("%s\t%s\t%s\n" % (item, "miss" if body is None else "hit", render_escaped(body or "")))
    sys.stdout.buffer.write("".join(out).encode("utf-8"))
    print("%s: %s %d hit(s), %d miss(es)" % (SAY, leg, hits, len(rows) - hits), file=sys.stderr)
    return 0
# <<< history_store_py


if __name__ == "__main__":
    sys.exit(main())
