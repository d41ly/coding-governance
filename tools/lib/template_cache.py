r"""template_cache -- one suite template cache: each base repository built once, keyed by its inputs,
and cloned per case (TOOL-dQuietDisk-7).

THE PROTOCOL, stated here once and implemented by both faces: this module, the python face, and the
`template_cache_sh` block of `template-cache.sh` beside it, the bash face.

    <cache root>/<key>/repo           the template: a committed, non-bare repository
    <cache root>/<key>/config-pins    its local config, one key=value per line, less remote.*, branch.*
                                      and the seven keys git writes at init
    <cache root>/<key>/ready          empty; a template is complete when it exists
    <cache root>/.stage-<key>-<pid>   a build in flight

ROOT. `SELFTEST_TEMPLATE_ROOT` when it names a directory; else the nearest ancestor of the process's
temp dir named `gate-work.*` and holding an `owner` file, a bar's owned `$WORK`, with `templates`
appended; else the caller's own scratch, `$SELFTEST_ROOT/templates` for the bash face and the `root`
argument here. Each root dies with the directory that holds it, and with none of the three the
cache refuses rather than choose a root that would outlive the run.

KEY. The SHA-1, in git's blob form, of `template-cache v1`, the face, the builder's name, its
definition and the caller's declared inputs. The bash face reads the definition with `declare -f` and
each input file's blob id with one `git hash-object --no-filters --stdin-paths`; this face hashes the
caller's `inputs` mapping in-process, and its builder's definition is whatever the caller spells
into `builder_id` or `inputs`, since a python callable has no `declare -f`. The bash face's
`resolve_template` also folds the builder arguments a caller passes after the builder into the key
its directory is named by: one more `git hash-object` over `template-cache args v1`, the caller's
key and one `%q` line per argument, the key unchanged where no argument is passed
(TOOL-dQuietDisk-37 S4). This face takes no builder arguments, so a value its `build` callable binds,
a closure's or a `functools.partial`'s, belongs in `inputs`, or two such callables share a template.

BUILD. The builder runs in the stage's `repo`. Where it leaves no `.git`, the face runs
`git init -q --template=` there; then it stages and commits everything as `base` with
`core.autocrlf=false`, an empty `core.hooksPath`, `commit.gpgsign=false` and a pinned identity, all
`-c` options, a builder that committed its own tree committing nothing more. It records the config
pins, writes `ready` in the stage and renames the stage to `<key>`: `mv -T` in bash, `os.rename`
here, each of which fails onto the key directory because that directory is never empty. A rename
that fails where `<key>/ready` exists is another run having built it: the loser removes its stage
and uses the winner's template.

CLONE. `git -c core.autocrlf=false clone --shared --quiet --template= -c <pin>... <template> <dest>`,
then `git -C <dest> remote remove <CLONE_REMOTE>`: three git processes, objects never copied, the template's
config carried, no remote kept, and line endings pinned for the clone process alone.

THE SWITCH. The policy key `tests.fixture-templates`, read once per cache through `policy.py get`:
`shared`, the default, or `per-case`, under which a caller builds per case as it did before the
cache. An absent policy kit, an unreadable key or no usable python reads as the default. WHAT THIS
DOES NOT CHECK: that a builder is deterministic in its inputs, which the key assumes; and a template a
crashed run left without `ready`, which is rebuilt rather than read.
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
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

POLICY_KIT = "policy"  # the sibling kit the switch is read through, named once
POLICY_KEY = "tests.fixture-templates"
# The name the clone gives its one remote, set with `clone -o` and removed by that name, so neither the
# clone nor the removal depends on the caller's `clone.defaultRemoteName`.
CLONE_REMOTE = "template-source"
MODES = ("shared", "per-case")
INIT_KEYS = ("core.repositoryformatversion", "core.filemode", "core.bare", "core.logallrefupdates",
             "core.symlinks", "core.ignorecase", "core.precomposeunicode")
COMMIT_PINS = ("-c", "core.autocrlf=false", "-c", "core.hooksPath=", "-c", "commit.gpgsign=false",
               "-c", "user.name=t", "-c", "user.email=t@e")


def run_git(cwd: pathlib.Path, *args: str) -> str:
    """`git -C <cwd> <args>`'s stdout; OSError naming the argv and git's stderr on a non-zero exit."""
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS}
    p = subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", check=False, env=env, stdin=subprocess.DEVNULL)
    if p.returncode != 0:
        raise OSError(f"git {' '.join(args)} in {pathlib.Path(cwd).as_posix()} exited {p.returncode}: "
                      f"{p.stderr.strip()}")
    return p.stdout


class TemplateCache:
    """One cache root and the switch's value, both resolved once, at construction."""

    def __init__(self, root=None):
        named = os.environ.get("SELFTEST_TEMPLATE_ROOT") or ""
        found = pathlib.Path(named) if named and os.path.isdir(named) else None
        if found is None:
            owned = resolve_owned_work(tempfile.gettempdir())
            found = owned / "templates" if owned is not None else None
        if found is None and root is None:
            raise ValueError("template-cache: no root: no SELFTEST_TEMPLATE_ROOT, no owned gate-work, "
                             "and no root argument, so a cache would outlive the run")
        self.root = found if found is not None else pathlib.Path(root)
        self.mode = MODES[0]
        policy = pathlib.Path(__file__).absolute().parent.parent / POLICY_KIT / "policy.py"
        if policy.is_file():
            try:
                got = subprocess.run([sys.executable, str(policy), "get", POLICY_KEY], capture_output=True,
                                     text=True, encoding="utf-8", errors="replace", check=False,
                                     stdin=subprocess.DEVNULL,
                                     env={k: v for k, v in os.environ.items() if k not in GIT_ENV_LEAKS})
            except OSError:
                got = None
            said = got.stdout.split() if got is not None and got.returncode == 0 else []
            if len(said) == 1 and said[0] in MODES:
                self.mode = said[0]

    def derive_key(self, builder_id: str, inputs: dict) -> str:
        """The key, 40 hex: SHA-1 in git's blob form of the version, the face, `builder_id` and each
        input, sorted by name, its value a str, bytes or None, each length-framed so no two input sets
        share a text."""
        text = bytearray(b"template-cache v1\npython\n")
        text += b"%d:%s\n" % (len(builder_id.encode("utf-8")), builder_id.encode("utf-8"))
        for name in sorted(inputs):
            value = inputs[name]
            body = b"" if value is None else value if isinstance(value, bytes) else str(value).encode("utf-8")
            tag = b"n" if value is None else b"b" if isinstance(value, bytes) else b"s"
            raw = name.encode("utf-8")
            text += b"input %d:%s %s %d:%s\n" % (len(raw), raw, tag, len(body), body)
        return hashlib.sha1(b"blob %d\0" % len(text) + bytes(text)).hexdigest()

    def resolve_template(self, builder_id: str, inputs: dict, build) -> pathlib.Path:
        """`<root>/<key>/repo`, built once per root: `build(repo)` populates the stage's repo, then the
        face commits and records it as the protocol states. OSError where the build or its commit fails."""
        key = self.derive_key(builder_id, inputs)
        home = self.root / key
        if (home / "ready").is_file():
            return home / "repo"
        stage = self.root / f".stage-{key}-{os.getpid()}"
        remove_tree(stage)
        repo = stage / "repo"
        repo.mkdir(parents=True)
        try:
            build(repo)
            if not (repo / ".git").exists():
                run_git(repo, "init", "-q", "--template=")
            run_git(repo, *COMMIT_PINS, "add", "-A")
            try:
                run_git(repo, *COMMIT_PINS, "commit", "-q", "-m", "base")
            except OSError:
                run_git(repo, "rev-parse", "-q", "--verify", "HEAD^{commit}")
                run_git(repo, "diff", "--cached", "--quiet")
            pins = []
            for line in run_git(repo, "config", "--local", "--list").splitlines():
                name = line.split("=", 1)[0]
                if name and not name.startswith(("remote.", "branch.")) and name not in INIT_KEYS:
                    pins.append(line + "\n")
            (stage / "config-pins").write_text("".join(pins), encoding="utf-8", newline="\n")
            (stage / "ready").write_bytes(b"")
        except BaseException:
            remove_tree(stage)
            raise
        try:
            os.rename(stage, home)
        except OSError:
            remove_tree(stage)
            if not (home / "ready").is_file():
                raise
        return home / "repo"

    def build_clone(self, template: pathlib.Path, dest: pathlib.Path) -> pathlib.Path:
        """`dest`, a `--shared` clone of `template` carrying its config pins and no remote. Returns `dest`."""
        pins = []
        for line in (pathlib.Path(template).parent / "config-pins").read_text(encoding="utf-8").splitlines():
            if line:
                pins += ["-c", line]
        template, dest = pathlib.Path(template).absolute(), pathlib.Path(dest).absolute()
        run_git(template, "-c", "core.autocrlf=false", "clone", "--shared", "--quiet", "--template=",
                "-o", CLONE_REMOTE, *pins, str(template), str(dest))
        run_git(dest, "remote", "remove", CLONE_REMOTE)
        return dest
