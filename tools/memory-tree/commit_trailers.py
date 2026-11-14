"""commit_trailers — the one reader of a commit's trailers, with both attribution views
(TOOL-dDeclaredLoop-23 S3).

This kit's copy. Each block below is INLINED byte-identically from the canonical copy its marker line
names, gov's lib dir, which ships nothing; `<prefix>/lib/resolve-python.test.sh`'s parity table reds a
copy that drifts. `routed_commits.py` and `deviation_join.py` import it, and the `commit` native class's pattern and resolver are read from it. The sibling-kit resolver rides beside the reader because the reader finds the
trailer key table through it, and the `git_env_leaks_py` block because the reader's runner drops those names.

Every git read through the default runner `run_git` is pinned (TOOL-dDeclaredLoop-39): the argv
carries `--no-replace-objects` and `-c log.showSignature=false`, the environment `GIT_GRAFT_FILE=/dev/null`
and no `GIT_ENV_LEAKS` name, so a replace ref, a graft or an inherited `GIT_DIR` cannot change what a
commit is attributed to. These are the pins of the readers it replaced: `routed_commits.run_git` and
the unattended kit's shell `GIT`.

A commit is a node of the `commit` native class, and every trailer key gov reads is one `[[trailer]]`
row of the playbook kit's `edges.toml`. `read_commits` reads a registered key and refuses any other, so
no consumer reads a trailer the table does not name. Where this install holds no playbook kit, or its
table holds no `[[trailer]]` row, the reader reads a closed floor of keys instead, `FLOOR_KEYS`, refuses
any other by name and says once on stderr that the check was skipped (TOOL-dDeclaredLoop-40). Two views
answer who a commit is attributed to, and each consumer names its own:

    union     the subject's ids plus the `Pass:` trailer's; `Pass: none` adds none and keeps the subject's
    replace   the `Pass:` trailer's ids alone, a `none` anywhere attributing nothing; the subject's
              ids where the commit carries no `Pass:` trailer

    python commit_trailers.py tokens <git-log revision arguments>   # one tokenised line per commit
    python commit_trailers.py message <file>                        # a message not yet committed
    python commit_trailers.py --print-commits                       # the commit class's members
    python commit_trailers.py --fixture                             # three planted commits, both views
"""
from __future__ import annotations

import os
import pathlib
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import tomllib

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


# >>> commit_trailers_py -- canonical copy: commit_trailers.py in the gov lib dir (byte-identical; gated)
#: A member of the `commit` native class: the full sha, which is what a `Decided:` edge's target spells.
SHA_RE = re.compile(r"[0-9a-f]{40}")
VIEWS = ("union", "replace")
SAY = "commit_trailers"
#: The one token rule: an id is a run of these characters, and every other character splits.
_SPLIT = re.compile(r"[^A-Za-z0-9-]")
_FIXTURE = (("TOOL-tFix-1: a subject id, no trailer", ""),
            ("TOOL-tFix-1: a subject id, trailer none", "Pass: none"),
            ("chore: no subject id, a trailer id", "Pass: TOOL-tFix-2"))
_FIXTURE_ID = re.compile(r"TOOL-tFix-[0-9]+")


def run_git(repo, argv, stdin=None):
    """The reader's own runner, pinned: `git --no-replace-objects -c log.showSignature=false -C <repo>
    <argv>` under the caller's environment with `GIT_GRAFT_FILE=/dev/null` and no `GIT_ENV_LEAKS` name,
    so neither a replace ref, a graft nor an inherited `GIT_DIR` changes what it reads. Its stdout as
    bytes, or OSError carrying git's stderr."""
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS}
    env["GIT_GRAFT_FILE"] = "/dev/null"
    proc = subprocess.run(["git", "--no-replace-objects", "-c", "log.showSignature=false", "-C", str(repo), *argv],
                          input=stdin, capture_output=True, env=env)
    if proc.returncode:
        raise OSError(f"`git {' '.join(argv)}` exited {proc.returncode}: "
                      + proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout


#: The keys read where no trailer key table is installed, or the one installed holds no `[[trailer]]`
#: row (TOOL-dDeclaredLoop-40): a closed list, each a row of the playbook kit's table, never joined to it.
FLOOR_KEYS = ("Pass", "Decided", "Gov-Transition", "Gov-Policy", "Red-fix")
_floor_noted = False


def read_key_table() -> tuple:
    """`(keys, path)`: every key a `[[trailer]]` row of the playbook kit's `edges.toml` registers, typed
    or not, and the table's path. The kit is the one the sibling-kit resolver finds from this file's
    directory. Where this install holds none, or its table holds no row, `(FLOOR_KEYS, None)`, and one
    stderr line per process says the check was skipped."""
    global _floor_noted
    try:
        path = resolve_kit_dir("playbook", "edges.toml", pathlib.Path(__file__).parent) / "edges.toml"
        with open(path, "rb") as fh:
            rows = tomllib.load(fh).get("trailer") or []
        keys = {row.get("key") for row in rows if isinstance(row, dict)}
    except LookupError:
        keys = set()
    if keys:
        return keys, path
    if not _floor_noted:
        _floor_noted = True
        print(f"{SAY}: unregistered-key check skipped: no edges.toml", file=sys.stderr)
    return set(FLOOR_KEYS), None


def read_commits(repo, revs, keys, files=False, run=None) -> list:
    """Every commit `git log <revs>` names, in its order, from ONE log call: `sha`, `parents`, `date`
    (committer, ISO), `subject` (the first paragraph joined) and `trailers`, each requested key mapped
    to the list of its values, by git's own trailer parse. `files` adds `paths`, renames read as a
    deletion plus an addition. `run(repo, argv)` is the consumer's git runner, returning stdout bytes.

    ValueError names a requested key the table does not register, or outside the floor where no table
    registers one, and a stream that ends mid-record."""
    registered, table = read_key_table()
    for key in keys:
        if key not in registered:
            where = table.as_posix() if table else "the floor keys, no trailer key table registering any"
            raise ValueError(f"the trailer key '{key}' is not registered in {where}, so no commit is read for it")
    fmt = "%x1e%H%x1f%P%x1f%cI%x1f%s" + "".join(
        f"%x1f%(trailers:key={k},valueonly,unfold,separator=%x1d)" for k in keys) + "%x1f"
    argv = ["log", *(("-z", "--root", "--no-renames", "--name-only") if files else ()), "--no-color",
            f"--format={fmt}", *revs, "--"]
    raw = (run or run_git)(repo, argv).decode("utf-8", "replace")
    commits = []
    for rec in raw.split("\x1e")[1:]:
        fields = rec.split("\x1f", 4 + len(keys))
        if len(fields) != 5 + len(keys):
            raise ValueError("the log stream ends inside a commit record; a truncated stream is not a clean one")
        commit = {"sha": fields[0], "parents": fields[1].split(), "date": fields[2], "subject": fields[3],
                  "trailers": {k: [v.strip() for v in fields[4 + i].split("\x1d")] if fields[4 + i] else []
                               for i, k in enumerate(keys)}}
        if files:
            commit["paths"] = [p for p in re.split(r"[\0\n]", fields[-1]) if p]
        commits.append(commit)
    return commits


def derive_tokens(text) -> list:
    """The tokens of `text` by the one rule, in order."""
    return _SPLIT.sub(" ", text).split()


def derive_attribution(commit, view, id_re=None) -> list:
    """The ids `commit` is attributed to under `view`, in token order, once each: the whole tokens
    `id_re` matches when given, else every token. A commit is trailered when a `Pass` value holds a
    non-blank character; `none` is never an id."""
    if view not in VIEWS:
        raise ValueError(f"no attribution view '{view}'; the views are {', '.join(VIEWS)}")
    subject = derive_tokens(commit["subject"])
    trailer = derive_tokens(" ".join(commit["trailers"].get("Pass") or []))
    if view == "union":
        tokens = subject + [t for t in trailer if t != "none"]
    elif any(commit["trailers"].get("Pass") or []):
        tokens = [] if "none" in trailer else trailer
    else:
        tokens = subject
    return list(dict.fromkeys(t for t in tokens if id_re is None or id_re.fullmatch(t)))


def read_message_ids(text) -> str:
    """The line the `message` verb prints for a commit message not yet committed: `PASSTRAILER <ids>`
    where its `Pass:` values hold a token, a `none` among them leaving no id, else its subject's
    tokens. The trailers are git's own parse of the message as written; the subject is the first
    paragraph, comment lines and CRs dropped, which is what `%s` reads once the commit exists."""
    raw = text if isinstance(text, bytes) else text.encode("utf-8", "surrogateescape")
    proc = subprocess.run(["git", "interpret-trailers", "--parse"], input=raw, capture_output=True)
    values = [m.group(1) for m in re.finditer(r"(?im)^pass: *(.*)$", proc.stdout.decode("utf-8", "replace"))]
    trailer = derive_tokens(" ".join(values))
    if trailer:
        return " ".join(["PASSTRAILER", *([] if "none" in trailer else dict.fromkeys(trailer))])
    subject = []
    for line in raw.decode("utf-8", "replace").split("\n"):
        line = line.removesuffix("\r")
        if line.startswith("#"):
            continue
        if not line.strip():
            if subject:
                break
            continue
        subject.append(line)
    return " ".join(derive_tokens(" ".join(subject)))


def build_fixture(top) -> pathlib.Path:
    """The three planted commits, oldest first, in a fresh repository under `top`: a subject id with no
    trailer, a subject id with `Pass: none`, and no subject id with a trailer id. The caller's git
    variables are set aside, so a fixture built under a hook lands in `top` and nowhere else."""
    repo = pathlib.Path(top) / "repo"
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    steps = [["init", "-q", "--template=", str(repo)]] + [
        ["-C", str(repo), "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid", "-c",
         "commit.gpgsign=false", "commit", "-q", "--no-verify", "--allow-empty", "-m", subject, *(("-m", body) if body else ())]
        for subject, body in _FIXTURE]
    for step in steps:
        proc = subprocess.run(["git", *step], capture_output=True, env=env)
        if proc.returncode:
            raise OSError(f"the fixture's `git {step[0]}` failed: " + proc.stderr.decode("utf-8", "replace").strip())
    return repo


def main(argv=None) -> int:
    # LF only, every verb: a shell loop reading this through `< <(...)` keeps a CR on its last token.
    sys.stdout.reconfigure(newline="\n")
    args = list(sys.argv[1:] if argv is None else argv)
    try:
        if args[:1] == ["tokens"]:
            # A range git cannot read prints nothing and exits 0, as the shell reader this verb replaced did.
            try:
                commits = read_commits(os.getcwd(), args[1:], ("Pass",))
            except OSError:
                return 0
            for c in commits:
                text = " ".join(c["trailers"]["Pass"])
                line = f"{c['sha']} {c['subject']}" if not text.strip() else (
                    f"{c['sha']} PASSTRAILER " + ("" if "none" in derive_tokens(text) else text))
                # byte by byte, as `tr -c` reads: a multi-byte character is as many spaces as it has bytes
                print(re.sub(rb"[^A-Za-z0-9-]", b" ", line.encode("utf-8")).decode("ascii"))
            return 0
        if args[:1] == ["message"] and len(args) == 2:
            print(read_message_ids(pathlib.Path(args[1]).read_bytes()))
            return 0
        if args == ["--print-commits"]:
            try:
                out = run_git(os.getcwd(), ["rev-list", "HEAD"])
            except OSError:
                return 3    # HEAD names no commit: the class is not armed here
            sys.stdout.write(out.decode("ascii", "replace"))
            return 0
        if args == ["--fixture"]:
            top = tempfile.mkdtemp(prefix="commit-trailers-")
            try:
                for c in read_commits(build_fixture(top), ["--reverse", "HEAD"], ("Pass",)):
                    print(f"{SAY}: fixture · {c['subject']} · " + " · ".join(
                        f"{view} {' '.join(derive_attribution(c, view, _FIXTURE_ID)) or '(nothing)'}" for view in VIEWS))
            finally:
                def remove_readonly(fn, path, _exc):
                    os.chmod(path, stat.S_IWRITE)
                    fn(path)
                shutil.rmtree(top, onexc=remove_readonly)
            return 0
    except (LookupError, ValueError, OSError) as exc:
        print(f"{SAY}: refused · {exc}", file=sys.stderr)
        return 2
    print(f"{SAY}: usage: tokens <git-log revision arguments> | message <file> | --print-commits | --fixture",
          file=sys.stderr)
    return 2
# <<< commit_trailers_py


if __name__ == "__main__":
    sys.exit(main())
