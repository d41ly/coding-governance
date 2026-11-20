#!/usr/bin/env python3
"""verdict_backends.py — the verdict backends registered under the policy key `verdict` (TOOL-dWitnessedBar-6).

    python verdict_backends.py read [--backend <name>] --sha <sha>   # one line: verdict: <backend> · <state> · <sha8> · <why>
    python verdict_backends.py verify-peer [--remote <name>]          # run on a second fleet node
    python verdict_backends.py --fixture --plant <case>

THE REGISTRY. A `[[verdict_backend]]` row in a kit descriptor, `name`, `reader` (`<module>:<function>`
under its kit), `off_node` (boolean) and `owner`, read across every `<tool root>/*/kit.toml` by
`read_backends`; a name declared twice is refused naming both descriptors. The run-gates kit declares
`local-hook`, `peer-node` and `remote-ci`; an expansion registers a backend by declaring a row in its own
kit. The table is the precedent `[[drive]]` and `[[command]]` set: govkit's install does not read it.

THE VALUE. `read` with no `--backend` reads `verdict` at the landed revision through the policy kit's
`policy.py get`; a reader that refuses is passed on, exit 2 naming its line, and never read as
`local-hook`. Only a run-gates kit with no policy kit beside it reads the catalogue default, said on one
line. `check_backend` refuses a value no declared row names, naming it and the declared names, before
any read.

ONE READ for every backend, `read_verdict(backend, sha, tree)` -> `Verdict(state, witness, why)`, the
state one of GREEN, RED, NONE, HELD and DEAD PROBE. Only GREEN stands: NONE, HELD and DEAD PROBE are no
verdict and never green. `read` exits 0 on GREEN, 1 on any other state, 2 on a refusal.

`local-hook` reads the runner-written per-tree verdict `<common-dir>/gate-verdict/<tree hash>`, the full
slot only, never the `.scoped` one beside it. `peer-node` fetches `refs/gov/verdict/<sha>`, an annotated
tag a second node's `verify-peer` pushed, and stands only when it points at the SHA, its `tree` line is
the SHA's tree, its `verdict` line reads GREEN and its `node` line is not this node's `GOV_NODE`.
`remote-ci`'s reader is `remote_verdict.py`'s.

WHAT THIS DOES NOT CHECK: that the peer ran the bar it names, or that its tag is signed by a registered
node key (TOOL-dWitnessedBar-43); that `GOV_NODE` is unique across the fleet.
"""
import argparse
import collections
import importlib
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

sys.dont_write_bytecode = True
# ONE MODULE under both names, so a reader imported by name returns the Verdict this script checks.
sys.modules.setdefault("verdict_backends", sys.modules[__name__])
HERE = pathlib.Path(os.path.abspath(__file__)).parent
TOOL_ROOT = HERE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from leg_factory import resolve_kit_dir  # noqa: E402 - the kit's inline copy of the sibling resolver

SAY = "verdict-backends"
STATES = ("GREEN", "RED", "NONE", "HELD", "DEAD PROBE")
DEFAULT_BACKEND = "local-hook"  # the catalogue default of `verdict`, read only where no policy kit resolves
CANDIDATE_REF = "refs/gov/candidate/"
VERDICT_REF = "refs/gov/verdict/"
BOUND = 60  # seconds, every git call that reaches a remote and every policy read
NAME = re.compile(r"[a-z][a-z0-9-]*")
READER = re.compile(r"[A-Za-z_][A-Za-z0-9_]*:[A-Za-z_][A-Za-z0-9_]*")
SHA = re.compile(r"[0-9a-f]{40}|[0-9a-f]{64}")

Verdict = collections.namedtuple("Verdict", "state witness why")


class Refusal(Exception):
    """Exit 2, nothing read and nothing pushed."""


# >>> resolve_bash_py -- canonical copy: resolve_bash.py in the gov lib dir (byte-identical; gated)
BASH_NAMES = ("bash.exe", "bash")


def wrong_shell_at(path, wsl):
    """True when `path` is a Windows checkout under WSL: `wsl` set and `path` under a single-letter
    `/mnt/<drive>/`, WSL's mount of a Windows drive (TOOL-dWitnessedBar-27). The twin of the shell
    block `refuse_wrong_shell`'s `wrong_shell_at` in `refuse-wrong-shell.sh` in the gov lib dir; a
    WSL path on its own disk, and any path where no WSL marker is set, is green."""
    p = str(path)
    return bool(wsl) and len(p) > 6 and p.startswith("/mnt/") and "a" <= p[5] <= "z" and p[6] == "/"


def scan_bash(script="", host=""):
    r"""`(found, tried, refusal)`: the bash to run, found by RUNNING each candidate, never by its name.

    GOV_BASH first, and when it is set nothing after it is tried; then Git's own `bin/bash.exe`, the
    third parent of `git --exec-path`; then each PATH directory's BASH_NAMES, a System32 or
    WindowsApps launcher reported and never run. A candidate passes when one run prints `uname -s` as
    its first line and exits 0, `test -f` on `script` included when one is given; on a `windows` host
    the answer must start MINGW or MSYS, so WSL's launcher, which answers `Linux` and drops `$1`, is
    refused under any name (gotcha subprocess-resolves-a-different-shell). Past GOV_BASH every
    candidate is run, `tried` holding one `<candidate>: <why>` for each and a repeat never twice;
    `found` is the first that passed, or "" with `refusal` naming every `tried` line, and the bare name
    `bash` is never returned. `host` is `windows` or `posix`, this host's when empty. No memo: an
    adapter keeps its own, so this stays a function a truth table can call twice. On a `posix` host
    the hosting file is judged first: WSL running it from a Windows checkout under `/mnt/` returns
    no `found`, an empty `tried` and the wrong-shell refusal, before any candidate is tried."""
    host = host or ("windows" if os.name == "nt" else "posix")
    if host == "posix":
        here = os.path.abspath(__file__)
        wsl = bool(os.environ.get("WSL_DISTRO_NAME")) or os.path.exists("/proc/sys/fs/binfmt_misc/WSLInterop")
        if wrong_shell_at(here, wsl):
            return "", [], ("WSL is running " + here + " from a Windows checkout under /mnt/; "
                            "run it with Git's bash (C:/Program Files/Git/bin/bash.exe)")
    tried, seen = [], set()

    def run_probe(cand):
        try:
            r = subprocess.run([cand, "-c", 'uname -s && { [ -z "$1" ] || test -f "$1"; }', "_", str(script)],
                               stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            return "did not run"
        u = r.stdout.decode("utf-8", "replace").replace("\x00", "").split("\n")[0].strip()
        if not u:
            return "did not run"
        if host == "windows" and not u.startswith(("MINGW", "MSYS")):
            return "answered " + u
        return "runs" if r.returncode == 0 else "cannot see " + str(script)

    def check_candidate(cand):
        key = cand.lower() if host == "windows" else cand
        if key in seen:
            return False
        seen.add(key)
        low = cand.lower()
        why = "a launcher" if "/system32/" in low or "/windowsapps/" in low else run_probe(cand)
        tried.append(cand + ": " + why)
        return why == "runs"

    gov = os.environ.get("GOV_BASH", "")
    if gov:
        why = run_probe(gov)
        tried.append(gov + ": " + why)
        if why == "runs":
            return gov, tried, ""
        return "", tried, ("GOV_BASH is set to '" + gov + "' and " + why + ", so nothing after it is tried: "
                           "an override that is set and unusable is refused, never a fall-through")
    try:
        r = subprocess.run(["git", "--exec-path"], stdin=subprocess.DEVNULL, capture_output=True, timeout=20)
        ex = r.stdout.decode("utf-8", "replace").strip().replace("\\", "/") if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        ex = ""
    found = ""
    if not ex:
        tried.append("git --exec-path: did not run")
    else:
        cand = "/".join(ex.rstrip("/").split("/")[:-3]) + "/bin/bash.exe"
        if not os.path.isfile(cand):
            tried.append(cand + ": absent")
        elif check_candidate(cand):
            found = cand
    for d in os.environ.get("PATH", "").split(os.pathsep):
        for name in BASH_NAMES:
            cand = (d.rstrip("/\\") + "/" + name).replace("\\", "/")
            if d and os.path.isfile(cand) and check_candidate(cand):
                found = found or cand
    if found:
        return found, tried, ""
    return "", tried, ("no bash runs" + (" that can see " + str(script) if script else "") + ": "
                       + "; ".join(tried) + "; set GOV_BASH to Git's bash")
# <<< resolve_bash_py


def resolve_bash(script):
    """The bash that can SEE `script`, or None: the one `resolve_bash_py` block above, run with it,
    its refusal read as None (TOOL-dWitnessedBar-26)."""
    return scan_bash(script)[0] or None


# ------------------------------------------------------------------------------------------ shared reads
def run_git(repo, *args, bound=BOUND, data=None):
    """`git -C <repo> <args>` -> (exit, stdout stripped); exit 124 where it outlived `bound` seconds. Bytes
    on both pipes, so `data` reaches git with LF line endings on every host."""
    try:
        p = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, timeout=bound,
                           input=None if data is None else data.encode("utf-8"))
    except subprocess.TimeoutExpired:
        return 124, ""
    except OSError as e:
        return 127, str(e)
    return p.returncode, p.stdout.decode("utf-8", "replace").strip()


def read_backends(tool_root):
    """Every `[[verdict_backend]]` row across `<tool_root>/*/kit.toml`, each a dict with its `kit` dir and
    `descriptor` added. A row missing a field, a malformed one, or a name declared twice is a Refusal."""
    tool_root = pathlib.Path(tool_root)
    rows, seen = [], {}
    for desc in sorted(tool_root.glob("*/kit.toml")):
        rel = desc.relative_to(tool_root.parent).as_posix()
        try:
            data = tomllib.loads(desc.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, tomllib.TOMLDecodeError) as e:
            raise Refusal(f"{rel} does not read, so no verdict backend is known: {e}") from None
        declared = data.get("verdict_backend") or []
        if not isinstance(declared, list):
            raise Refusal(f"{rel}: 'verdict_backend' is not an array of tables")
        for n, row in enumerate(declared, 1):
            bad = [f for f, ok in (("name", isinstance(row.get("name"), str) and NAME.fullmatch(row["name"])),
                                   ("reader", isinstance(row.get("reader"), str) and READER.fullmatch(row["reader"])),
                                   ("off_node", isinstance(row.get("off_node"), bool)),
                                   ("owner", isinstance(row.get("owner"), str) and row["owner"]))
                   if not ok] if isinstance(row, dict) else ["name", "reader", "off_node", "owner"]
            if bad:
                raise Refusal(f"{rel}: [[verdict_backend]] row {n} carries no valid {', '.join(bad)}")
            if row["name"] in seen:
                raise Refusal(f"verdict backend {row['name']} is declared twice: in {seen[row['name']]} and in {rel}")
            seen[row["name"]] = rel
            rows.append(dict(row, kit=desc.parent, descriptor=rel))
    return rows


def check_backend(name, backends):
    """The row of `backends` named `name`; a Refusal naming the value and every declared name otherwise."""
    for row in backends:
        if row["name"] == name:
            return row
    names = ", ".join(r["name"] for r in backends) or "none"
    raise Refusal(f"verdict = {name} names no declared verdict backend; the descriptors declare {names}")


def read_policy_value(repo, key):
    """`key` at the landed revision, by the policy kit's `policy.py get` run in `repo` -> (value or None,
    the reader's refusal line or ''); (None, '') where no policy kit resolves beside this kit."""
    try:
        kit = resolve_kit_dir("policy", "policy.py", HERE)
    except LookupError:
        return None, ""
    try:
        p = subprocess.run([sys.executable, str(kit / "policy.py"), "get", key], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=BOUND, cwd=str(repo))
    except (OSError, subprocess.TimeoutExpired) as e:
        return None, f"policy.py get {key} did not answer: {type(e).__name__}"
    said = [ln.strip() for ln in p.stdout.splitlines() if ln.strip()]
    if p.returncode != 0 or not said:
        why = [ln.strip() for ln in (p.stderr + p.stdout).splitlines() if ln.strip()]
        return None, why[0] if why else f"policy.py get {key} exited {p.returncode} and printed nothing"
    return said[0], ""


def read_backend_name(repo):
    """The value of `verdict` at the landed revision; a Refusal passing the reader's own refusal on."""
    value, refused = read_policy_value(repo, "verdict")
    if refused:
        raise Refusal(refused)
    if value is None:
        print(f"{SAY}: verdict reads its catalogue default, {DEFAULT_BACKEND}: no policy kit resolves beside this kit")
        return DEFAULT_BACKEND
    return value


def read_common_dir(repo):
    """The absolute common git dir of `repo`, or None."""
    rc, out = run_git(repo, "rev-parse", "--path-format=absolute", "--git-common-dir")
    return pathlib.Path(out) if rc == 0 and out else None


def read_tree_of(repo, sha):
    """The tree id of the commit `sha` in `repo`, or '' where the clone lacks it."""
    if not SHA.fullmatch(sha or ""):
        return ""
    rc, out = run_git(repo, "rev-parse", "--verify", "-q", f"{sha}^{{tree}}")
    return out if rc == 0 else ""


def read_tag_lines(text):
    """The `<key>TAB<value>` lines of a verdict record or a tag message -> {key: value}, the last one winning."""
    out = {}
    for ln in text.splitlines():
        k, sep, v = ln.rstrip("\r").partition("\t")
        if sep:
            out[k] = v
    return out


# ------------------------------------------------------------------------------------------ the readers
def read_verdict(backend, sha, tree, repo="."):
    """`backend`'s verdict on `sha`, whose tree is `tree`, through the reader its row declares."""
    if not tree:
        return Verdict("DEAD PROBE", "", f"this clone lacks {sha[:8] or 'the sha'}, so its tree is unknown")
    mod, _, fn = backend["reader"].partition(":")
    kit = str(backend["kit"])
    if kit not in sys.path:
        sys.path.insert(0, kit)
    try:
        reader = getattr(importlib.import_module(mod), fn)
    except (ImportError, AttributeError) as e:
        return Verdict("DEAD PROBE", "", f"the reader {backend['reader']} does not load: {e}")
    v = reader(backend, sha, tree, repo=repo)
    if not isinstance(v, Verdict) or v.state not in STATES:
        return Verdict("DEAD PROBE", "", f"the reader {backend['reader']} answered no state: {v!r}")
    return v


def read_local_verdict(backend, sha, tree, repo="."):
    """`local-hook`: the runner-written FULL per-tree verdict for `tree`, never the `.scoped` slot."""
    common = read_common_dir(repo)
    if common is None:
        return Verdict("DEAD PROBE", "", "no git common dir resolves here")
    slot = common / "gate-verdict" / tree
    if not slot.is_file():
        return Verdict("NONE", "", f"no full per-tree verdict at gate-verdict/{tree[:8]}")
    try:
        rec = read_tag_lines(slot.read_text(encoding="utf-8", errors="replace"))
    except OSError as e:
        return Verdict("DEAD PROBE", "", f"gate-verdict/{tree[:8]} does not read: {e}")
    if rec.get("tree") != tree:
        return Verdict("DEAD PROBE", "", f"gate-verdict/{tree[:8]} names the tree {rec.get('tree', '')[:8] or 'none'}")
    if rec.get("verdict") == "GREEN":
        return Verdict("GREEN", "witnessed", f"the full bar, run {rec.get('run_id', '?')}, on tree {tree[:8]}")
    if rec.get("verdict") == "RED":
        return Verdict("RED", "", f"the full bar, run {rec.get('run_id', '?')}, red on tree {tree[:8]}")
    return Verdict("DEAD PROBE", "", f"gate-verdict/{tree[:8]} carries no GREEN or RED verdict line")


def read_node_tag():
    """This node's tag, `GOV_NODE`, or ''."""
    node = os.environ.get("GOV_NODE", "").strip()
    return node if re.fullmatch(r"[A-Za-z0-9._-]+", node) else ""


def read_peer_verdict(backend, sha, tree, repo="."):
    """`peer-node`: `refs/gov/verdict/<sha>` fetched from the remote, standing only when it is an annotated
    tag on `sha` whose `tree` is `tree`, whose `verdict` is GREEN and whose `node` is not this node's."""
    node = read_node_tag()
    if not node:
        return Verdict("DEAD PROBE", "", "GOV_NODE names no node tag here, so no peer verdict can be told off-node")
    remote = os.environ.get("GOV_REMOTE") or "origin"
    ref = VERDICT_REF + sha
    rc, out = run_git(repo, "ls-remote", remote, ref)
    if rc != 0:
        return Verdict("DEAD PROBE", "", f"git ls-remote {remote} {ref} exited {rc}")
    if not out:
        return Verdict("NONE", "", f"no peer verdict published at {remote} {VERDICT_REF}{sha[:8]}")
    rc, _ = run_git(repo, "fetch", "-q", "--no-tags", remote, f"+{ref}:{ref}")
    if rc != 0:
        return Verdict("DEAD PROBE", "", f"git fetch {remote} {ref} exited {rc}")
    rc, body = run_git(repo, "cat-file", "tag", ref)
    if rc != 0:
        return Verdict("NONE", "", f"{VERDICT_REF}{sha[:8]} is no annotated tag")
    head, _, message = body.partition("\n\n")
    obj = next((ln[7:] for ln in head.splitlines() if ln.startswith("object ")), "")
    rec = read_tag_lines(message)
    peer = rec.get("node", "")
    if obj != sha:
        return Verdict("NONE", "", f"{VERDICT_REF}{sha[:8]} points at {obj[:8] or 'nothing'}, not the sha")
    if rec.get("tree") != tree:
        return Verdict("NONE", "", f"node {peer or '?'}'s verdict names the tree {rec.get('tree', '')[:8] or 'none'}, "
                                   f"not {tree[:8]}")
    if not peer or peer == node:
        return Verdict("NONE", "", f"the verdict is node {peer or '(unnamed)'}'s, this node's own, so it is not off-node")
    if rec.get("verdict") == "GREEN":
        return Verdict("GREEN", "witnessed", f"node {peer}'s full bar, run {rec.get('run_id', '?')}, on tree {tree[:8]}")
    if rec.get("verdict") == "RED":
        return Verdict("RED", "", f"node {peer}'s full bar, run {rec.get('run_id', '?')}, red on tree {tree[:8]}")
    return Verdict("DEAD PROBE", "", f"node {peer}'s tag carries no GREEN or RED verdict line")


# ------------------------------------------------------------------------------------------ the peer verb
def write_peer_tag(repo, sha, rec, node, remote):
    """An annotated tag on `sha` whose message is `rec`'s verdict, tree and run_id lines and `node`'s, pushed
    as `refs/gov/verdict/<sha>` -> '' pushed, else why not."""
    rc, ident = run_git(repo, "var", "GIT_COMMITTER_IDENT")
    if rc != 0 or not ident:
        return "no committer identity resolves for the tag"
    message = "".join(f"{k}\t{rec.get(k, '')}\n" for k in ("verdict", "tree", "run_id")) + f"node\t{node}\n"
    body = f"object {sha}\ntype commit\ntag verdict-{sha}\ntagger {ident}\n\n{message}"
    rc, tag = run_git(repo, "mktag", data=body)
    if rc != 0 or not tag:
        return f"git mktag exited {rc}"
    rc, _ = run_git(repo, "push", "-q", "--force", remote, f"{tag}:{VERDICT_REF}{sha}")
    return "" if rc == 0 else f"git push {remote} {VERDICT_REF}{sha[:8]} exited {rc}"


def run_verify_peer(remote, repo="."):
    """Each `refs/gov/candidate/<sha>` the remote lists with no `refs/gov/verdict/<sha>` beside it: fetched,
    barred under GATE_FULL=1 in a detached worktree of this clone, and its full slot published as a tag."""
    node = read_node_tag()
    if not node:
        print(f"{SAY}: verify-peer refused · GOV_NODE names no node tag here, so no verdict could name its node")
        return 2
    rc, out = run_git(repo, "ls-remote", remote, CANDIDATE_REF + "*", VERDICT_REF + "*")
    if rc != 0:
        print(f"{SAY}: verify-peer · DEAD PROBE · git ls-remote {remote} exited {rc}")
        return 2
    refs = {ln.split("\t", 1)[1] for ln in out.splitlines() if "\t" in ln}
    todo = sorted(r[len(CANDIDATE_REF):] for r in refs
                  if r.startswith(CANDIDATE_REF) and VERDICT_REF + r[len(CANDIDATE_REF):] not in refs)
    rc, prefix = run_git(HERE, "rev-parse", "--show-prefix")
    common = read_common_dir(repo)
    print(f"{SAY}: verify-peer · {len(todo)} candidate(s) without a verdict on {remote}")
    failed = 0
    for sha in todo:
        why = ""
        scratch = pathlib.Path(tempfile.mkdtemp(prefix="gov-peer-")) / "tree"
        try:
            if not SHA.fullmatch(sha):
                why = "the ref names no sha"
            elif run_git(repo, "fetch", "-q", "--no-tags", remote, CANDIDATE_REF + sha)[0] != 0:
                why = "the candidate does not fetch"
            elif run_git(repo, "worktree", "add", "-q", "--detach", str(scratch), sha)[0] != 0:
                why = "no detached worktree could be added"
            else:
                bar = scratch / prefix / "run-gates.sh"
                bash = resolve_bash(bar)
                if bash is None:
                    raise OSError("no bash runs that can see " + bar.as_posix())
                p = subprocess.run([bash, str(bar)], cwd=str(scratch), env=dict(os.environ, GATE_FULL="1"))
                tree = read_tree_of(repo, sha)
                slot = common / "gate-verdict" / tree if common and tree else None
                if slot is None or not slot.is_file():
                    why = f"the bar exited {p.returncode} and wrote no full slot for tree {tree[:8]}"
                else:
                    why = write_peer_tag(repo, sha, read_tag_lines(slot.read_text(encoding="utf-8", errors="replace")),
                                         node, remote)
        finally:
            run_git(repo, "worktree", "remove", "--force", str(scratch))
            shutil.rmtree(scratch.parent, ignore_errors=True)
        failed += bool(why)
        print(f"{SAY}: verify-peer · {sha[:8]} · " + (f"not published: {why}" if why else
                                                      f"published {VERDICT_REF}{sha[:8]} as node {node}"))
    return 1 if failed else 0


# ------------------------------------------------------------------------------------------ the fixture
PLANTS = {
    "registry": "the three declared rows, then a second descriptor declaring local-hook again",
    "unregistered": "verdict = ci-cloud in the policy's only revision: read and the lander refuse, no push",
    "undeclared": "verdict = remote-ci over descriptors declaring no remote-ci row: read and the lander refuse, no push",
    "local-green": "a full per-tree verdict GREEN, then RED, then none, then a scoped-only GREEN",
    "peer": "a tag from node b read on node a, the same tag from node a, and one naming another tree",
    "lander-peer": "the lander under verdict = peer-node with no peer verdict: a candidate published, nothing landed",
    "remote-green": "a push run of the declared workflow, its bar step success, the pinned file deriving the pin",
    "swapped-workflow": "the same run over a workflow differing from the pin, under pinned-workflow then app-only",
    "other-path": "a run whose path is another workflow file",
    "step-skipped": "the bar step concluded skipped",
    "api-404": "the runs listing answers 404",
    "held": "a scheduled run of two held jobs, one failure",
}
FIX_ENV = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@e", "GIT_COMMITTER_NAME": "t",
           "GIT_COMMITTER_EMAIL": "t@e", "GIT_CONFIG_COUNT": "1", "GIT_CONFIG_KEY_0": "core.autocrlf",
           "GIT_CONFIG_VALUE_0": "false", "GOV_DEFAULT_BRANCH": "main"}
FIX_ROWS = (("local-hook", "verdict_backends:read_local_verdict", "false"),
            ("peer-node", "verdict_backends:read_peer_verdict", "true"),
            ("remote-ci", "remote_verdict:read_remote_verdict", "true"))
FIX_KIT_FILES = ("verdict_backends.py", "remote_verdict.py", "leg_factory.py", "regen.py")
FIX_WORKFLOW = ".github/workflows/remote-ci.yml"


def run_fixture_git(top, *args):
    """git in the scratch repository `top`, a failure raised."""
    p = subprocess.run(["git", "-C", str(top), *args], capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=BOUND, env=dict(os.environ, **FIX_ENV))
    if p.returncode != 0:
        raise OSError(f"git {' '.join(args)} exited {p.returncode}: {p.stderr.strip()}")
    return p.stdout.strip()


def render_rows(names):
    """The `[[verdict_backend]]` rows of FIX_ROWS named in `names`, as the run-gates descriptor spells them."""
    return "".join(f'[[verdict_backend]]\nname = "{n}"\nreader = "{r}"\noff_node = {o}\nowner = "tFix"\n\n'
                   for n, r, o in FIX_ROWS if n in names)


def write_fixture_tree(top, files, remote=True, kits=True):
    """A repository at `top/work` committed on `main`: `files`, and with `kits` the lander, the policy kit and
    this kit's readers under `tools/`; with `remote` pushed to the bare `top/remote.git`, origin/HEAD set."""
    work = pathlib.Path(top, "work")
    work.mkdir(parents=True)
    run_fixture_git(work, "init", "-q", "--template=", "-b", "main")
    put = dict(files)
    if kits:
        policy = resolve_kit_dir("policy", "policy.py", HERE)
        put["tools/push-main.sh"] = (TOOL_ROOT / "push-main.sh").read_text(encoding="utf-8")
        for name in ("policy.py", "budgets.py", "caps.toml", "catalogue.toml"):
            put["tools/policy/" + name] = (policy / name).read_text(encoding="utf-8")
        for name in FIX_KIT_FILES:
            put["tools/run-gates/" + name] = (HERE / name).read_text(encoding="utf-8")
        put.setdefault("tools/run-gates/kit.toml", render_rows([n for n, _r, _o in FIX_ROWS]))
    for rel, text in put.items():
        path = work / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.replace("\r\n", "\n").encode("utf-8"))
    run_fixture_git(work, "add", "-A")
    run_fixture_git(work, "commit", "-q", "--no-verify", "-m", "fixture")
    if remote:
        run_fixture_git(top, "init", "-q", "--bare", "--template=", "remote.git")
        run_fixture_git(work, "remote", "add", "origin", str(pathlib.Path(top, "remote.git")))
        run_fixture_git(work, "push", "-q", "--no-verify", "origin", "main")
        run_fixture_git(work, "remote", "set-head", "origin", "main")
    return work


def run_fixture_command(cwd, argv, **put):
    """A process in `cwd`, FIX_ENV and `put` in its environment -> (exit, its stdout and stderr)."""
    env = dict(os.environ, **FIX_ENV, **put)
    env.pop("GIT_DIR", None)
    env.pop("GIT_WORK_TREE", None)
    try:
        p = subprocess.run(argv, cwd=str(cwd), capture_output=True, text=True, encoding="utf-8", errors="replace",
                           env=env, timeout=300)
    except subprocess.TimeoutExpired:
        return 124, "the command outlived its 300 s bound\n"
    sys.stdout.write(p.stdout + p.stderr)
    return p.returncode, p.stdout + p.stderr


def run_plant(case, top):
    """The scenarios of `case` over the scratch at `top`: [(scenario, exit, owed exit, [needles], output)]."""
    out = []
    me = [sys.executable, str(HERE / "verdict_backends.py")]
    rv = [sys.executable, str(HERE / "remote_verdict.py")]

    def run_scenario(name, cwd, argv, owed, needles, **put):
        rc, said = run_fixture_command(cwd, argv, **put)
        out.append((name, rc, owed, needles, said))
        return said

    if case == "registry":
        rows = read_backends(TOOL_ROOT)
        said = "".join(f"{r['name']} off_node={str(r['off_node']).lower()} · {r['descriptor']}\n" for r in rows) + "\n"
        sys.stdout.write(said)
        out.append(("the declared rows", 0, 0, ["local-hook off_node=false", "peer-node off_node=true",
                                                 "remote-ci off_node=true"], said))
        root = pathlib.Path(top, "tools")
        for kit, text in (("run-gates", render_rows([n for n, _r, _o in FIX_ROWS])), ("other", render_rows(["local-hook"]))):
            (root / kit).mkdir(parents=True)
            (root / kit / "kit.toml").write_text(text, encoding="utf-8")
        try:
            read_backends(root)
            said, rc = "read_backends admitted a duplicate row\n", 0
        except Refusal as e:
            said, rc = f"{SAY}: refused · {e}\n", 2
        sys.stdout.write(said)
        out.append(("local-hook declared twice", rc, 2, ["tools/other/kit.toml", "tools/run-gates/kit.toml"], said))
    elif case in ("unregistered", "undeclared", "lander-peer"):
        value = {"unregistered": "ci-cloud", "undeclared": "remote-ci", "lander-peer": "peer-node"}[case]
        names = ["local-hook", "peer-node"] if case == "undeclared" else [n for n, _r, _o in FIX_ROWS]
        work = write_fixture_tree(top, {".governance/policy.toml": f'verdict = "{value}"\n',
                                        "tools/run-gates/kit.toml": render_rows(names)})
        (work / "unit.txt").write_text("a unit to land\n", encoding="utf-8")
        run_fixture_git(work, "add", "-A")
        run_fixture_git(work, "commit", "-q", "--no-verify", "-m", "a unit to land")
        sha = run_fixture_git(work, "rev-parse", "HEAD")
        remote = pathlib.Path(top, "remote.git")
        before = run_fixture_git(remote, "for-each-ref")
        reader = ["tools/run-gates/verdict_backends.py", "read", "--sha", sha]
        bash = resolve_bash(work / "tools/push-main.sh")
        if bash is None:
            raise OSError("no bash runs that can see the fixture lander")
        lander = [bash, "tools/push-main.sh"]
        if case == "unregistered":
            needles = ["ci-cloud", "local-hook", "peer-node", "remote-ci"]
            run_scenario("read", work, [sys.executable, *reader], 2, needles)
            run_scenario("the lander", work, lander, 1, needles, GOV_NODE="a")
        elif case == "undeclared":
            needles = ["verdict = remote-ci names no declared verdict backend", "local-hook, peer-node"]
            run_scenario("read", work, [sys.executable, *reader], 2, needles)
            run_scenario("the lander", work, lander, 1, needles, GOV_NODE="a")
        else:
            run_scenario("the lander", work, lander, 1,
                         ["verdict: peer-node · NONE · " + sha[:8], "reads NONE"], GOV_NODE="a")
        after = run_fixture_git(remote, "for-each-ref")
        main_kept = run_fixture_git(remote, "rev-parse", "refs/heads/main") != sha
        if case == "lander-peer":
            cand = run_fixture_git(remote, "for-each-ref", "--format=%(objectname)", CANDIDATE_REF + sha)
            said = f"candidate published: {cand == sha} · main moved: {not main_kept}\n"
            out.append(("a candidate published, main unmoved", 0 if cand == sha and main_kept else 1, 0,
                        ["candidate published: True"], said))
        else:
            said = f"remote refs unchanged: {before == after}\n"
            out.append(("no push made", 0 if before == after else 1, 0, ["remote refs unchanged: True"], said))
        sys.stdout.write(said)
    elif case == "local-green":
        work = write_fixture_tree(top, {"a.txt": "a\n"}, remote=False, kits=False)
        sha = run_fixture_git(work, "rev-parse", "HEAD")
        tree = read_tree_of(work, sha)
        slot = read_common_dir(work) / "gate-verdict"
        slot.mkdir()
        argv = [*me, "read", "--backend", "local-hook", "--sha", sha]
        for name, files, owed, state in (("a full GREEN", {tree: "GREEN"}, 0, "GREEN"),
                                         ("a full RED", {tree: "RED"}, 1, "RED"),
                                         ("no file", {}, 1, "NONE"),
                                         ("a scoped-only GREEN", {tree + ".scoped": "GREEN"}, 1, "NONE")):
            for f in slot.iterdir():
                f.unlink()
            for f, v in files.items():
                (slot / f).write_text(f"tree\t{tree}\nsha\t{sha}\nverdict\t{v}\nkind\tfull\nrun_id\tr1\n", encoding="utf-8")
            run_scenario(name, work, argv, owed, [f"verdict: local-hook · {state} · {sha[:8]}"])
    elif case == "peer":
        work = write_fixture_tree(top, {"a.txt": "a\n"}, kits=False)
        sha = run_fixture_git(work, "rev-parse", "HEAD")
        tree = read_tree_of(work, sha)
        argv = [*me, "read", "--backend", "peer-node", "--sha", sha]
        for name, node, rec_tree, state in (("node b's tag read on node a", "b", tree, "GREEN"),
                                            ("node a's own tag", "a", tree, "NONE"),
                                            ("a tag naming another tree", "b", "0" * len(tree), "NONE")):
            why = write_peer_tag(work, sha, {"verdict": "GREEN", "tree": rec_tree, "run_id": "r1"}, node, "origin")
            if why:
                raise OSError(why)
            run_scenario(name, work, argv, 0 if state == "GREEN" else 1, [f"verdict: peer-node · {state} · {sha[:8]}"],
                         GOV_NODE="a", GOV_REMOTE="origin")
    elif case == "held":
        resp = pathlib.Path(top, "responses")
        resp.mkdir()
        sha = "a" * 40
        rvm = read_remote_module()
        write_responses(rvm, resp, {
            "/repos/o/r/actions/workflows/remote-ci.yml/runs?event=schedule&status=completed&per_page=1":
                {"workflow_runs": [{"id": 77, "head_sha": sha}]},
            "/repos/o/r/actions/runs/77/jobs?per_page=100&page=1":
                {"total_count": 3, "jobs": [{"name": "held one", "conclusion": "success"},
                                            {"name": "held two", "conclusion": "failure"},
                                            {"name": "held-plan", "conclusion": "success"}]}})
        said = run_scenario("two held jobs, one failure", top, [*rv, "held", "--responses", str(resp),
                                                                "https://github.com/o/r", "remote-ci.yml"], 0,
                            ["held reader: run 77 at aaaaaaaa · 2 held job(s) read · 1 red"])
        rows = [ln for ln in said.splitlines() if ln.startswith("held\t")]
        out.append(("two held rows", 0 if len(rows) == 2 else 1, 0, ["held\ttwo\t" + sha + "\t77\tfailure"], said))
    else:
        out.extend(run_remote_plant(case, top, rv))
    return out


def read_remote_module():
    """The kit's `remote_verdict` module."""
    return importlib.import_module("remote_verdict")


def write_responses(rvm, resp, answers):
    """Each `{request path: JSON body}` written under `resp` as `read_api --responses` names it."""
    import json
    for path, body in answers.items():
        (resp / rvm.derive_response_name(path)).write_text(json.dumps(body), encoding="utf-8")


def run_remote_plant(case, top, rv):
    """`remote_verdict.py read --responses` over one fixture repository: the workflow committed, the pin set
    at the landed revision, and the canned answers of one push run of it."""
    rvm = read_remote_module()
    out = []
    work = write_fixture_tree(top, {FIX_WORKFLOW: "name: remote-ci\n"}, remote=False, kits=False)
    first = run_fixture_git(work, "rev-parse", "HEAD")
    _lines, pin = rvm.derive_pin(work, first, [FIX_WORKFLOW])
    pathlib.Path(work, ".governance").mkdir()
    pathlib.Path(work, ".governance/policy.toml").write_text(f'[verdict.remote]\npin = "{pin}"\n', encoding="utf-8")
    run_fixture_git(work, "add", "-A")
    run_fixture_git(work, "commit", "-q", "--no-verify", "-m", "the pin")
    landed = run_fixture_git(work, "rev-parse", "HEAD")
    sha = landed
    if case == "swapped-workflow":
        pathlib.Path(work, FIX_WORKFLOW).write_text("name: remote-ci\non: push\n", encoding="utf-8")
        run_fixture_git(work, "commit", "-q", "--no-verify", "-am", "the workflow swapped")
        sha = run_fixture_git(work, "rev-parse", "HEAD")
    run_fixture_git(work, "remote", "add", "origin", "https://github.com/o/r.git")
    run_fixture_git(work, "update-ref", "refs/remotes/origin/main", landed)
    run_fixture_git(work, "symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
    resp = pathlib.Path(top, "responses")
    resp.mkdir()
    path = FIX_WORKFLOW if case != "other-path" else ".github/workflows/other.yml"
    step = "skipped" if case == "step-skipped" else "success"
    answers = {
        f"/repos/o/r/actions/workflows/remote-ci.yml/runs?head_sha={sha}&event=push&per_page=10":
            {"workflow_runs": [{"id": 5, "head_sha": sha, "event": "push", "path": path, "status": "completed",
                                "check_suite_id": 9}]},
        "/repos/o/r/actions/runs/5/jobs?per_page=100":
            {"total_count": 1, "jobs": [{"name": "bar", "steps": [
                {"name": "the merge bar, every leg guard ignored, walled inside the job limit", "conclusion": step}]}]},
        "/repos/o/r/check-suites/9": {"app": {"slug": "github-actions"}},
    }
    if case != "api-404":
        write_responses(rvm, resp, answers)
    argv = [*rv, "read", "--responses", str(resp), "--sha", sha]
    state = {"remote-green": "GREEN", "swapped-workflow": "HELD", "other-path": "NONE", "step-skipped": "NONE",
             "api-404": "DEAD PROBE"}[case]
    needles = [f"verdict: remote-ci · {state} · {sha[:8]}"] + ([FIX_WORKFLOW] if state == "HELD" else [])
    rc, said = run_fixture_command(work, argv)
    out.append((case, rc, 0 if state == "GREEN" else 1, needles, said))
    if case == "swapped-workflow":
        pathlib.Path(work, ".governance/policy.toml").write_text(
            f'[verdict.remote]\ntrust = "app-only"\npin = "{pin}"\n', encoding="utf-8")
        run_fixture_git(work, "commit", "-q", "--no-verify", "-am", "trust app-only")
        run_fixture_git(work, "update-ref", "refs/remotes/origin/main", run_fixture_git(work, "rev-parse", "HEAD"))
        rc, said = run_fixture_command(work, argv)
        out.append(("under app-only", rc, 0, [f"verdict: remote-ci · GREEN · {sha[:8]} · witness claimed"], said))
    return out


def run_fixture(case):
    """`case`'s scenarios over one scratch directory, each held or missed: the last owed exit when all held,
    else 3. A git variable the caller inherited, a hook's GIT_DIR say, is dropped first, so no git call
    the plant makes, its own or a child's, is retargeted at the caller's repository."""
    for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR", "GIT_OBJECT_DIRECTORY",
              "GIT_ALTERNATE_OBJECT_DIRECTORIES", "GIT_NAMESPACE", "GIT_PREFIX"):
        os.environ.pop(k, None)
    top = pathlib.Path(tempfile.mkdtemp(prefix="verdict-backends-")).absolute()
    try:
        print(f"{SAY}: fixture · plant {case} · {PLANTS[case]}")
        try:
            out = run_plant(case, top)
        except (LookupError, OSError, Refusal, subprocess.SubprocessError) as e:
            print(f"{SAY}: fixture · plant {case} · not run: {e}")
            return 2
        held = 0
        for name, rc, owed, needles, said in out:
            ok = rc == owed and all(n in said for n in needles)
            held += ok
            print(f"{SAY}: fixture · {name} · exit {rc} · owed {owed} naming {needles!r} · {'held' if ok else 'MISSED'}")
        whole = bool(out) and held == len(out)
        print(f"{SAY}: fixture · plant {case} · {held} of {len(out)} scenario(s) held{' · all held' if whole else ''}")
        return out[-1][2] if whole else 3
    finally:
        shutil.rmtree(top, ignore_errors=True)


# ------------------------------------------------------------------------------------------ the verbs
def run_read(backend_name, sha, repo="."):
    """The `read` verb -> its exit: 0 GREEN, 1 any other state, 2 refused."""
    try:
        backends = read_backends(TOOL_ROOT)
        name = backend_name or read_backend_name(repo)
        backend = check_backend(name, backends)
    except Refusal as e:
        print(f"{SAY}: refused · {e}")
        return 2
    full = sha
    if SHA.fullmatch(sha or "") is None:
        rc, full = run_git(repo, "rev-parse", "--verify", "-q", f"{sha}^{{commit}}")
        full = full if rc == 0 else ""
    v = read_verdict(backend, full, read_tree_of(repo, full), repo=repo)
    why = f"witness {v.witness}: {v.why}" if v.witness else v.why
    print(f"verdict: {backend['name']} · {v.state} · {(full or sha)[:8]} · {why}")
    return 0 if v.state == "GREEN" else 1


def main(argv):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace", newline="\n")
    ap = argparse.ArgumentParser(prog="verdict_backends.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("verb", nargs="?", choices=["read", "verify-peer"])
    ap.add_argument("--backend", help="read this backend rather than the value `verdict` holds")
    ap.add_argument("--sha", help="the commit read")
    ap.add_argument("--remote", default=None, help="verify-peer's remote, origin by default")
    ap.add_argument("--fixture", action="store_true", help="run one plant's scenarios in a scratch directory")
    ap.add_argument("--plant", choices=list(PLANTS))
    args = ap.parse_args(argv)
    if args.fixture != bool(args.plant) or (args.fixture == bool(args.verb)):
        ap.error("one of read --sha <sha>, verify-peer or --fixture --plant <case>")
    if args.fixture:
        return run_fixture(args.plant)
    if args.verb == "read":
        if not args.sha:
            ap.error("read takes --sha <sha>")
        return run_read(args.backend, args.sha)
    return run_verify_peer(args.remote or os.environ.get("GOV_REMOTE") or "origin")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
