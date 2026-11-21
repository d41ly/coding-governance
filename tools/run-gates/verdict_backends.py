#!/usr/bin/env python3
"""verdict_backends.py — the verdict backends registered under the policy key `verdict` (TOOL-dWitnessedBar-6).

    python verdict_backends.py read [--backend <name>] --sha <sha>   # one line: verdict: <backend> · <state> · <sha8> · <why>
    python verdict_backends.py off-node [--backend <name>]           # is the row off-node? exit 0 yes, 1 no, 2 refused
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

`off-node` (TOOL-dWitnessedBar-2 F5) reads the value as `read` does, finds its row by `check_backend`, and
prints one line, `verdict-backends: off-node · <name> · <true|false> · off-node backends: <names>`, the
names every declared row with `off_node = true`. It exits 0 when the row is off-node, 1 when it is not, 2
on a refusal. The lander and the pre-push hook ask it under `hooks.bypass = refused`, which stands only on
an off-node witness, because a hook on the bypassing node cannot refuse its own bypass.

`local-hook` reads the runner-written per-tree verdict `<common-dir>/gate-verdict/<tree hash>`, the full
slot only, never the `.scoped` one beside it, and stands on a GREEN one only where the pre-push hook's two
record predicates would adopt it (TOOL-dWitnessedBar-56 S7, S8, `check_local_record`): the reuse pair says
no leg came from the cache, and the selection's rows hash to its `selection` and the landed revision
derives them; NONE otherwise, DEAD PROBE where that revision or the check cannot be read. `peer-node` fetches `refs/gov/verdict/<sha>`, an annotated
tag a second node's `verify-peer` pushed, and stands only when it points at the SHA, its `tree` line is
the SHA's tree, its `node` line is not this node's `GOV_NODE`, and (TOOL-dWitnessedBar-43):
- SIGNED. `git verify-tag --raw` against `verdict.peer.signers`, the owner's allowed-signers lines read at
  the landed revision and written to a temp file under the common git dir, exits 0 and its `Good "git"
  signature for <principal>` line names the tag's `node` line. Unsigned, an unknown key, a bad signature
  (`Signature verification failed`, a message changed after signing) or another principal is NONE; no
  signer table is NONE; a verify that cannot run, an `ls-remote` or `fetch` that fails and a refused
  policy read are DEAD PROBE.
- GREEN, its `verdict` line.
- SOURCED. `remote_verdict.py`'s `check_pin_source`, the pin over `verdict.remote.pin-scope`'s files at
  the SHA, under `verdict.remote.trust`; the `workflow` scope, which pins only a workflow no peer runs,
  reads HELD naming the key outside `app-only`.
`verify-peer` signs its tag with `git -c gpg.format=ssh tag -s` under the operator's `user.signingkey`,
and refuses, exit 2, where that reads empty. `remote-ci`'s reader is `remote_verdict.py`'s.

WHAT THIS DOES NOT CHECK: that the peer ran the bar it names, beyond the pinned files it ran it from;
that `GOV_NODE` is unique across the fleet; that a registered key is still held only by its node.
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
import time
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
SIGNERS_KEY = "verdict.peer.signers"
GOOD_SIGNATURE = re.compile(r'Good "git" signature for (\S+) with ')
# Seconds a signer temp may stand before a peer read sweeps it as a killed read's.
# `TAIL_GRACE_S`, the run-gates kit's own constant for the runner's tail sweep (TOOL-dWitnessedBar-42),
# is not reused: its span is seven days, far past a peer read's life, and it is a bash constant of the
# runner, which this Python module cannot read (TOOL-dWitnessedBar-65 S21).
PEER_SIGNERS_GRACE_S = 86400

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
def run_git(repo, *args, bound=BOUND, data=None, both=False):
    """`git -C <repo> <args>` -> (exit, stdout stripped), and with `both` (exit, stdout, stderr) stripped;
    exit 124 where it outlived `bound` seconds. Bytes on both pipes, so `data` reaches git with LF line
    endings on every host."""
    try:
        p = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, timeout=bound,
                           input=None if data is None else data.encode("utf-8"))
    except subprocess.TimeoutExpired:
        return (124, "", f"git outlived its {bound} s bound") if both else (124, "")
    except OSError as e:
        return (127, "", str(e)) if both else (127, str(e))
    out = p.stdout.decode("utf-8", "replace").strip()
    return (p.returncode, out, p.stderr.decode("utf-8", "replace").strip()) if both else (p.returncode, out)


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


def read_policy_value(repo, key, every=False):
    """`key` at the landed revision, by the policy kit's `policy.py get` run in `repo` -> (value or None,
    the reader's refusal line or ''); (None, '') where no policy kit resolves beside this kit. With `every`
    the value is the list of every line it printed, a set's members one per line."""
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
    return (said if every else said[0]), ""


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
    if rec.get("verdict") == "RED":
        return Verdict("RED", "", f"the full bar, run {rec.get('run_id', '?')}, red on tree {tree[:8]}")
    if rec.get("verdict") != "GREEN":
        return Verdict("DEAD PROBE", "", f"gate-verdict/{tree[:8]} carries no GREEN or RED verdict line")
    refused = check_local_record(rec, common, repo)
    if refused is not None:
        return refused
    return Verdict("GREEN", "witnessed", f"the full bar, run {rec.get('run_id', '?')}, on tree {tree[:8]}")


def check_local_record(rec, common, repo="."):
    """None where a GREEN per-tree record `rec` is one the pre-push hook adopts on its own two record
    predicates, else the NONE or DEAD PROBE Verdict saying why not (TOOL-dWitnessedBar-56 S7, S8). A
    second copy of the hook's `check_tree_reuse` and `check_tree_selection`, since the hook ships
    verbatim and sources no kit; the hook suite's parity arm holds the two copies to one decision.
    - the reuse pair (TOOL-dWitnessedBar-40): neither `reused` nor `reused_cache` is NONE, a non-zero
      `reused_cache` is NONE, and a non-zero `reused` with no `reused_cache` is NONE;
    - the selection (TOOL-dWitnessedBar-41): no `selection` key is NONE and `none` passes; otherwise
      `held`, a TAB and each `selection.<n>` from 1 upward, each LF-terminated, must hash to it, else
      NONE, and `verdict_flow.py select --check --selection` over those rows at the landed revision R,
      the policy kit's `derive_landed_revision`, must exit 0: exit 1 is NONE, and an R that does not
      derive or a check that cannot run is DEAD PROBE."""
    reused, cache = rec.get("reused", ""), rec.get("reused_cache", "")
    if not reused and not cache:
        return Verdict("NONE", "", "the record carries neither reused nor reused_cache, so it cannot say whether "
                                   "its run reused a leg")
    if cache and cache != "0":
        return Verdict("NONE", "", f"the record says its run reused {cache} leg(s) from the cache, and a reused "
                                   f"verdict proves nothing whole")
    if not cache and reused != "0":
        return Verdict("NONE", "", f"the record says its run reused {reused} leg(s), and a reused verdict proves "
                                   f"nothing whole")
    sel = rec.get("selection", "")
    if not sel:
        return Verdict("NONE", "", "the record carries no selection, so it cannot say whether its bar held legs")
    if sel == "none":
        return None
    rows, n = [], 1
    while f"selection.{n}" in rec:
        rows.append(f"held\t{rec[f'selection.{n}']}\n")
        n += 1
    text = "".join(rows)
    rc, h = run_git(repo, "hash-object", "--stdin", data=text)
    if rc != 0 or not h:
        return Verdict("DEAD PROBE", "", f"git hash-object exited {rc}, so the record's selection rows cannot be hashed")
    if h != sel:
        return Verdict("NONE", "", f"the record's selection rows do not hash to {sel[:8]}, so a row was edited or lost")
    landed, why = read_landed_revision(repo)
    if not landed:
        return Verdict("DEAD PROBE", "", f"the landed revision does not derive, so the selection cannot be checked "
                                         f"at R: {why}")
    name = ""
    try:
        fd, name = tempfile.mkstemp(prefix="gov-selection-", dir=str(common))
        with os.fdopen(fd, "wb") as f:
            f.write(text.encode("utf-8"))
        p = subprocess.run([sys.executable, str(HERE / "verdict_flow.py"), "select", "--check", "--selection", name,
                            "--rev", landed], capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=BOUND, cwd=str(repo))
    except (OSError, subprocess.SubprocessError) as e:
        return Verdict("DEAD PROBE", "", f"select --check could not run at {landed[:8]}: {type(e).__name__}: {e}")
    finally:
        if name:
            try:
                os.unlink(name)
            except OSError:
                pass
    said = " ".join(ln.strip() for ln in (p.stdout + p.stderr).splitlines() if ln.strip())
    if p.returncode == 1:
        return Verdict("NONE", "", f"the record's selection is not what {landed[:8]} derives: {said}")
    if p.returncode != 0:
        return Verdict("DEAD PROBE", "", f"select --check at {landed[:8]} exited {p.returncode}: {said or 'nothing said'}")
    return None


def read_landed_revision(repo):
    """The landed revision R as the policy kit's `derive_landed_revision` reads it -> (sha, ''), or ('', why
    it does not derive)."""
    try:
        kit = resolve_kit_dir("policy", "policy.py", HERE)
    except LookupError as e:
        return "", f"no policy kit resolves beside this kit: {e}"
    if str(kit) not in sys.path:
        sys.path.append(str(kit))
    try:
        policy = importlib.import_module("policy")
    except ImportError as e:
        return "", f"the policy kit does not load: {e}"
    try:
        return policy.derive_landed_revision(str(repo))[0], ""
    except (policy.Refusal, OSError, subprocess.SubprocessError) as e:
        return "", str(e)


def read_node_tag():
    """This node's tag, `GOV_NODE`, or ''."""
    node = os.environ.get("GOV_NODE", "").strip()
    return node if re.fullmatch(r"[A-Za-z0-9._-]+", node) else ""


def remove_stale_signer_temps(common, now=None):
    """Unlink every `gov-signers-` file directly under the common git dir `common` whose mtime is older
    than `PEER_SIGNERS_GRACE_S`, the file a killed peer read left (TOOL-dWitnessedBar-63 S20, §8 F5). A
    younger one may be a concurrent read's live file and is kept; one that cannot be read or unlinked is
    left for the next read. Only a regular file is touched, never a link or a directory; an unlink that
    finds the file gone is silent, and any other failure names the file on one stderr line, the read
    going on either way (TOOL-dWitnessedBar-65 S11). -> the names removed."""
    now = time.time() if now is None else now
    gone = []
    try:
        found = sorted(pathlib.Path(common).glob("gov-signers-*"))
    except OSError:
        return gone
    for p in found:
        try:
            if not (p.is_file(follow_symlinks=False) and now - p.stat().st_mtime > PEER_SIGNERS_GRACE_S):
                continue
        except OSError:
            continue
        try:
            os.unlink(p)
        except FileNotFoundError:
            continue
        except OSError as e:
            print(f"verdict_backends: the aged signer temp {p} could not be removed, left for the next read: {e}",
                  file=sys.stderr)
            continue
        gone.append(p.name)
    return gone


def read_signer_principal(repo, ref, members):
    """`ref` verified by `git verify-tag --raw` against the allowed-signers lines `members`, written to a temp
    file under the common git dir and removed after -> (the principal its `Good "git" signature` line names,
    None), or ('', the NONE or DEAD PROBE Verdict saying why none stands). Git writes that line to standard
    error, so both streams are read. The file is created, written, read and unlinked inside ONE
    `try`/`finally`, so a normal exit, an exception, a subprocess timeout or a `KeyboardInterrupt` after
    `mkstemp` leaves nothing behind (TOOL-dWitnessedBar-62 S39). A process kill runs no `finally` and can
    leave the file, so each read first runs `remove_stale_signer_temps`, which sweeps any such file older
    than `PEER_SIGNERS_GRACE_S` (TOOL-dWitnessedBar-63 S20)."""
    common = read_common_dir(repo)
    if common is None:
        return "", Verdict("DEAD PROBE", "", "no git common dir resolves here, so no signer file can be written")
    remove_stale_signer_temps(common)
    name = None
    try:
        fd, name = tempfile.mkstemp(prefix="gov-signers-", dir=str(common))
        try:
            with os.fdopen(fd, "wb") as f:
                f.write("".join(m + "\n" for m in members).encode("utf-8"))
        except OSError as e:
            return "", Verdict("DEAD PROBE", "", f"the signer file under the common git dir does not write: {e}")
        rc, _out, err = run_git(repo, "-c", "gpg.ssh.allowedSignersFile=" + pathlib.Path(name).as_posix(),
                                "verify-tag", "--raw", ref, both=True)
    except OSError as e:
        return "", Verdict("DEAD PROBE", "", f"the signer file under the common git dir does not write: {e}")
    finally:
        if name is not None:
            try:
                os.unlink(name)
            except OSError:
                pass
    good = GOOD_SIGNATURE.search(err)
    if rc == 0 and good:
        return good.group(1), None
    if "no signature found" in err:
        return "", Verdict("NONE", "", f"{ref} is unsigned, so no registered node key witnesses it")
    if "No principal matched" in err:
        return "", Verdict("NONE", "", f"{ref} is signed by an unknown key, one no {SIGNERS_KEY} line names")
    if "Signature verification failed" in err:  # TOOL-dWitnessedBar-56 S15: the tag changed after it was signed
        return "", Verdict("NONE", "", f"{ref} carries a bad signature, its message changed after it was signed")
    said = next((ln.strip() for ln in err.splitlines() if ln.strip()), "nothing on standard error")
    return "", Verdict("DEAD PROBE", "", f"git verify-tag --raw {ref} exited {rc}: {said}")


def read_peer_verdict(backend, sha, tree, repo="."):
    """`peer-node`: `refs/gov/verdict/<sha>` fetched from the remote, standing only when it is an annotated
    tag on `sha` whose `tree` is `tree`, whose `node` is not this node's, signed by the key
    `verdict.peer.signers` registers for that node, whose `verdict` is GREEN, and whose pinned files at
    `sha` derive the pin (TOOL-dWitnessedBar-43)."""
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
    # SIGNED: the owner's list at the landed revision, never the working tree or the candidate.
    rvm = read_remote_module()
    members, refused = read_policy_value(repo, SIGNERS_KEY, every=True)
    if refused and rvm.DERIVED_REFUSAL not in refused:
        return Verdict("DEAD PROBE", "", f"{SIGNERS_KEY} does not read: {refused}")
    if not members:
        return Verdict("NONE", "", f"no signer table: {SIGNERS_KEY} registers no node key; the owner sets it with "
                                   f"policy_edit.py set {SIGNERS_KEY}")
    principal, refusal = read_signer_principal(repo, ref, members)
    if refusal is not None:
        return refusal
    if principal != peer:
        return Verdict("NONE", "", f"signer {principal} is not node {peer}: the tag's node line names another node")
    if principal == node:
        return Verdict("NONE", "", f"signer {principal} is this node, so the verdict is its own")
    if rec.get("verdict") == "RED":
        return Verdict("RED", "", f"node {peer}'s full bar, run {rec.get('run_id', '?')}, red on tree {tree[:8]}")
    if rec.get("verdict") != "GREEN":
        return Verdict("DEAD PROBE", "", f"node {peer}'s tag carries no GREEN or RED verdict line")
    # SOURCED: the one source rule remote-ci applies, through its own function.
    try:
        keys = rvm.read_remote_keys(repo)
        trust, scope, _pin = keys
        if trust != "app-only" and scope == "workflow":
            return Verdict("HELD", "", "verdict.remote.pin-scope = workflow pins only the remote workflow, which no "
                                       "peer runs; the owner sets verdict.remote.pin-scope = dispatch-closure and pins "
                                       "under it")
        v = rvm.check_pin_source(backend, sha, keys, repo)
    except rvm.DeadProbe as e:
        return Verdict("DEAD PROBE", "", str(e))
    if v.state != "GREEN":
        return v
    return v._replace(why=f"node {peer}'s full bar, run {rec.get('run_id', '?')}, on tree {tree[:8]}, signed by "
                          f"its registered key, {v.why}")


# ------------------------------------------------------------------------------------------ the peer verb
def write_peer_tag(repo, sha, rec, node, remote):
    """An annotated tag on `sha` whose message is `rec`'s verdict, tree and run_id lines and `node`'s, signed
    by `git -c gpg.format=ssh tag -s` under the operator's own `user.signingkey` and pushed as
    `refs/gov/verdict/<sha>`, its local name deleted -> '' pushed, else why not."""
    message = "".join(f"{k}\t{rec.get(k, '')}\n" for k in ("verdict", "tree", "run_id")) + f"node\t{node}\n"
    name = f"verdict-{sha}"
    rc, _out, err = run_git(repo, "-c", "gpg.format=ssh", "tag", "-s", "-f", "--cleanup=verbatim", "-F", "-", name,
                            sha, data=message, both=True)
    rc_tag, tag = run_git(repo, "rev-parse", "--verify", "-q", f"refs/tags/{name}") if rc == 0 else (rc, "")
    run_git(repo, "tag", "-d", name)
    if rc != 0:
        said = next((ln.strip() for ln in err.splitlines() if ln.strip()), "nothing on standard error")
        return f"git tag -s exited {rc}: {said}"
    if rc_tag != 0 or not tag:
        return f"the signed tag {name} does not resolve"
    rc, _ = run_git(repo, "push", "-q", "--force", remote, f"{tag}:{VERDICT_REF}{sha}")
    return "" if rc == 0 else f"git push {remote} {VERDICT_REF}{sha[:8]} exited {rc}"


def run_verify_peer(remote, repo="."):
    """Each `refs/gov/candidate/<sha>` the remote lists with no `refs/gov/verdict/<sha>` beside it: fetched,
    barred under GATE_FULL=1 in a detached worktree of this clone, and its full slot published as a tag."""
    node = read_node_tag()
    if not node:
        print(f"{SAY}: verify-peer refused · GOV_NODE names no node tag here, so no verdict could name its node")
        return 2
    if not run_git(repo, "config", "user.signingkey")[1]:
        print(f"{SAY}: verify-peer refused · user.signingkey reads empty, so no tag could be signed with this node's "
              f"key; set it to the key the owner registered under {SIGNERS_KEY}")
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
    "reused-cache": "a full GREEN whose reused_cache reads 1",
    "reused-alone": "a full GREEN carrying reused 2 and no reused_cache",
    "no-pair": "a full GREEN carrying neither reused nor reused_cache",
    "no-selection": "a full GREEN carrying no selection key",
    "edited-selection": "a full GREEN whose selection.1 was edited after its hash was taken",
    "underived-selection": "a full GREEN holding a quarantine row the landed revision does not derive",
    "clean": "a full GREEN with the reuse pair at 0 under selection none, then holding the row R derives",
    "key-no-tab": "a full GREEN whose reuse key is a bare reused line with no TAB, read as an absent key",
    "peer-tip-missing": "a peer ref the remote advertises whose tag names a commit the remote lacks, so the fetch fails",
    "peer-no-ssh-keygen": "node b's signed GREEN read on node a with gpg.ssh.program at an absent path, beside an aged "
                          "and a young signer temp",
    "peer-bad-signature": "a tag node b signed whose message was edited after signing, read on node a",
    "peer": "over the signed, pinned setup: a tag node b signed read on node a, one node a signed of its own, and one "
            "naming another tree",
    "peer-signed": "a GREEN node b signed with its registered key, the pinned files equal, read on node a",
    "peer-unsigned": "an unsigned tag from node b read on node a, then verify-peer with user.signingkey empty",
    "peer-self-tag": "a tag whose node line reads b, signed by node a's key, read on node a",
    "peer-swapped-manifest": "a GREEN node b signed over a candidate emptying the leg manifest, under dispatch-closure, "
                             "then workflow pinning the workflow alone, then app-only",
    "lander-peer": "the lander under verdict = peer-node with no peer verdict: a candidate published, nothing landed",
    "lander-refused": "off-node asked of local-hook, then the lander under hooks.bypass = refused and verdict = local-hook: "
                      "both name the off-node backends, no push",
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
FIX_TOOLS = TOOL_ROOT.name  # the fixture tree mirrors this tool root's name
FIX_KIT = f"{FIX_TOOLS}/{HERE.name}"  # this kit, as the fixture tree spells it


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
        put[f"{FIX_TOOLS}/push-main.sh"] = (TOOL_ROOT / "push-main.sh").read_text(encoding="utf-8")
        for name in ("policy.py", "budgets.py", "caps.toml", "catalogue.toml"):
            put[f"{FIX_TOOLS}/{policy.name}/" + name] = (policy / name).read_text(encoding="utf-8")
        for name in FIX_KIT_FILES:
            put[f"{FIX_KIT}/" + name] = (HERE / name).read_text(encoding="utf-8")
        put.setdefault(f"{FIX_KIT}/kit.toml", render_rows([n for n, _r, _o in FIX_ROWS]))
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
        out.append(("local-hook declared twice", rc, 2, [f"{FIX_TOOLS}/other/kit.toml", f"{FIX_KIT}/kit.toml"], said))
    elif case in ("unregistered", "undeclared", "lander-peer", "lander-refused"):
        value = {"unregistered": "ci-cloud", "undeclared": "remote-ci", "lander-peer": "peer-node",
                 "lander-refused": "local-hook"}[case]
        names = ["local-hook", "peer-node"] if case == "undeclared" else [n for n, _r, _o in FIX_ROWS]
        bypass = '\n[hooks]\nbypass = "refused"\n' if case == "lander-refused" else ""
        work = write_fixture_tree(top, {".governance/policy.toml": f'verdict = "{value}"\n{bypass}',
                                        f"{FIX_KIT}/kit.toml": render_rows(names)})
        (work / "unit.txt").write_text("a unit to land\n", encoding="utf-8")
        run_fixture_git(work, "add", "-A")
        run_fixture_git(work, "commit", "-q", "--no-verify", "-m", "a unit to land")
        sha = run_fixture_git(work, "rev-parse", "HEAD")
        remote = pathlib.Path(top, "remote.git")
        before = run_fixture_git(remote, "for-each-ref")
        reader = [f"{FIX_KIT}/verdict_backends.py", "read", "--sha", sha]
        bash = resolve_bash(work / FIX_TOOLS / "push-main.sh")
        if bash is None:
            raise OSError("no bash runs that can see the fixture lander")
        lander = [bash, f"{FIX_TOOLS}/push-main.sh"]
        if case == "unregistered":
            needles = ["ci-cloud", "local-hook", "peer-node", "remote-ci"]
            run_scenario("read", work, [sys.executable, *reader], 2, needles)
            run_scenario("the lander", work, lander, 1, needles, GOV_NODE="a")
        elif case == "undeclared":
            needles = ["verdict = remote-ci names no declared verdict backend", "local-hook, peer-node"]
            run_scenario("read", work, [sys.executable, *reader], 2, needles)
            run_scenario("the lander", work, lander, 1, needles, GOV_NODE="a")
        elif case == "lander-refused":
            run_scenario("off-node", work, [sys.executable, f"{FIX_KIT}/verdict_backends.py", "off-node", "--backend",
                                            "local-hook"], 1,
                         ["off-node · local-hook · false · off-node backends: peer-node, remote-ci"])
            run_scenario("the lander", work, lander, 1,
                         ["hooks.bypass is refused and verdict local-hook is no off-node backend", "peer-node, remote-ci"],
                         GOV_NODE="a")
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
                (slot / f).write_text(f"tree\t{tree}\nsha\t{sha}\nverdict\t{v}\nkind\tfull\nrun_id\tr1\nreused\t0\n"
                                      f"reused_cache\t0\nselection\tnone\n", encoding="utf-8")
            run_scenario(name, work, argv, owed, [f"verdict: local-hook · {state} · {sha[:8]}"])
    elif case in LOCAL_PLANTS:
        run_local_plant(case, top, run_scenario)
    elif case.startswith("peer"):
        run_peer_plant(case, top, run_scenario)
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


LOCAL_PLANTS = ("reused-cache", "reused-alone", "no-pair", "no-selection", "edited-selection", "underived-selection",
                "clean", "key-no-tab")
LOCAL_POLICY = '[tests]\nlanding-levels = ["unit", "integration"]\nwithout-cadence = "report-unrun"\n'


def run_local_plant(case, top, run_scenario):
    """The local-hook plants of TOOL-dWitnessedBar-56 S7 and S8 over one fixture pushed to its bare remote, so
    the landed revision R is its `main`: a manifest giving leg x level e2e and a policy landing `unit
    integration`, so R derives one `level` row, which `verdict_flow.py select` writes and the plant reads
    rather than spells. Each plant writes the full per-tree verdict of R's tree and reads it on `local-hook`."""
    me = [sys.executable, str(HERE / "verdict_backends.py")]
    work = write_fixture_tree(top, {"gate-legs.json": '[{"name": "x", "argv": ["bash", "a.sh"], "level": "e2e"}]\n',
                                    ".governance/policy.toml": LOCAL_POLICY}, kits=False)
    sha = run_fixture_git(work, "rev-parse", "HEAD")
    tree = read_tree_of(work, sha)
    slot = read_common_dir(work) / "gate-verdict"
    slot.mkdir()
    out = pathlib.Path(top, "derived")
    rc, said = run_fixture_command(work, [sys.executable, str(HERE / "verdict_flow.py"), "select", "--rev", sha,
                                          "--out", str(out)])
    derived = [ln[len("held\t"):] for ln in (out.read_text(encoding="utf-8").splitlines() if out.is_file() else [])
               if ln.startswith("held\t")]
    if rc != 0 or len(derived) != 1:
        raise OSError(f"select --rev at the fixture's R derived {len(derived)} row(s), exit {rc}, not the one level "
                      f"row the plant needs: {said.strip()}")

    def write_record(pair=("reused\t0\n", "reused_cache\t0\n"), selection=("none", []), head=None):
        """`head` replaces the sha and verdict lines, written with its bytes as given."""
        hashed, rows = selection
        lead = f"sha\t{sha}\nverdict\tGREEN\n" if head is None else head
        text = f"tree\t{tree}\n{lead}kind\tfull\nrun_id\tr1\n" + "".join(pair)
        if hashed is not None:
            text += f"selection\t{hashed}\n" + "".join(f"selection.{n}\t{r}\n" for n, r in enumerate(rows, 1))
        (slot / tree).write_text(text, encoding="utf-8", newline=None if head is None else "")

    def derive_rows_hash(rows):
        rc, h = run_git(work, "hash-object", "--stdin", data="".join(f"held\t{r}\n" for r in rows))
        if rc != 0 or not h:
            raise OSError("git hash-object did not answer for the planted rows")
        return h

    def read_local(name, state, needles):
        run_scenario(name, work, [*me, "read", "--backend", "local-hook", "--sha", sha], 0 if state == "GREEN" else 1,
                     [f"verdict: local-hook · {state} · {sha[:8]}", *needles])

    underived = "x\tquarantine\tTOOL-x-7 · 3/10"
    if case == "reused-cache":
        write_record(pair=("reused\t1\n", "reused_cache\t1\n"))
        read_local("reused_cache 1", "NONE", ["reused 1 leg(s) from the cache"])
    elif case == "reused-alone":
        write_record(pair=("reused\t2\n",))
        read_local("reused 2 with no reused_cache", "NONE", ["reused 2 leg(s), and"])
    elif case == "no-pair":
        write_record(pair=())
        read_local("neither reuse key", "NONE", ["neither reused nor reused_cache"])
    elif case == "key-no-tab":
        # TOOL-dWitnessedBar-63 AC11 (S19): `read_tag_lines` skips a line with no TAB, so a bare `reused`
        # reads as no key at all; a reader taking the key as its value reads `reused reused leg(s)`.
        # TOOL-dWitnessedBar-65 AC12 (S15): the record also holds `verdict<TAB>GREEN<CR>` and two `sha`
        # lines, the second R's, so the pair line is reached only where the verdict reads GREEN with its
        # CR stripped; the hook's `read_green_file` reads the same lines in the gov suite.
        write_record(pair=("reused\n",), head=f"sha\t{'a' * 40}\nsha\t{sha}\nverdict\tGREEN\r\n")
        read_local("a bare reused line, no TAB", "NONE", ["neither reused nor reused_cache"])
    elif case == "no-selection":
        write_record(selection=(None, []))
        read_local("no selection key", "NONE", ["carries no selection"])
    elif case == "edited-selection":
        write_record(selection=(derive_rows_hash(derived), [derived[0] + " edited"]))
        read_local("selection.1 edited after its hash", "NONE", ["do not hash to"])
    elif case == "underived-selection":
        write_record(selection=(derive_rows_hash([underived]), [underived]))
        read_local("a row R does not derive", "NONE", [f"is not what {sha[:8]} derives", "TOOL-x-7"])
    else:
        write_record()
        read_local("the pair at 0, selection none", "GREEN", ["witness witnessed"])
        write_record(selection=(derive_rows_hash(derived), derived))
        read_local("the pair at 0, the row R derives", "GREEN", ["witness witnessed"])


def write_unsigned_tag(repo, sha, rec, node, remote):
    """The tag `write_peer_tag` writes, built by `git mktag` with no signature, the fixture's forger -> '' pushed,
    else why not."""
    rc, ident = run_git(repo, "var", "GIT_COMMITTER_IDENT")
    if rc != 0 or not ident:
        return "no committer identity resolves for the tag"
    message = "".join(f"{k}\t{rec.get(k, '')}\n" for k in ("verdict", "tree", "run_id")) + f"node\t{node}\n"
    rc, tag = run_git(repo, "mktag", data=f"object {sha}\ntype commit\ntag verdict-{sha}\ntagger {ident}\n\n{message}")
    if rc != 0 or not tag:
        return f"git mktag exited {rc}"
    rc, _ = run_git(repo, "push", "-q", "--force", remote, f"{tag}:{VERDICT_REF}{sha}")
    return "" if rc == 0 else f"git push {remote} {VERDICT_REF}{sha[:8]} exited {rc}"


def run_peer_plant(case, top, run_scenario):
    """The peer plants over ONE signed, pinned setup (TOOL-dWitnessedBar-43): throwaway keys for nodes a and b,
    made by `ssh-keygen -N ""` under `top`, both registered in `verdict.peer.signers`, and the files
    `dispatch-closure` names pinned, committed on `main` and pushed so the landed revision carries them. Each
    tag is signed by `write_peer_tag` under the key its scenario names, and read on node a."""
    me = [sys.executable, str(HERE / "verdict_backends.py")]
    rvm = read_remote_module()
    members = []
    for n in ("a", "b"):
        key = pathlib.Path(top, f"key-{n}")
        try:
            p = subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-C", n, "-f", str(key)],
                               capture_output=True, text=True, encoding="utf-8", timeout=BOUND, stdin=subprocess.DEVNULL)
        except (OSError, subprocess.SubprocessError) as e:
            raise OSError(f"no ssh-keygen runs, so no throwaway node key is made: {e}") from None
        if p.returncode != 0:
            raise OSError(f"ssh-keygen exited {p.returncode}: {p.stderr.strip()}")
        kind, body = pathlib.Path(top, f"key-{n}.pub").read_text(encoding="utf-8").split()[:2]
        members.append(f"{n} {kind} {body}")
    paths = rvm.read_scope_paths({}, "dispatch-closure")
    manifest = next(p for p in paths if p.endswith("gate-legs.json"))
    work = write_fixture_tree(top, {p: f"{p}\n" for p in paths}, kits=False)
    for k, v in (("user.name", "t"), ("user.email", "t@e")):
        run_fixture_git(work, "config", k, v)
    base = run_fixture_git(work, "rev-parse", "HEAD")
    pins = {scope: rvm.derive_pin(work, base, rvm.read_scope_paths({}, scope))[1] for scope in rvm.SCOPES}

    def write_policy(scope="dispatch-closure", trust=""):
        signers = ", ".join(f'"{m}"' for m in members)
        pathlib.Path(work, ".governance").mkdir(exist_ok=True)
        pathlib.Path(work, ".governance/policy.toml").write_text(
            f'[verdict.remote]\n{trust}pin-scope = "{scope}"\npin = "{pins[scope]}"\n\n'
            f'[verdict.peer]\nsigners = [{signers}]\n', encoding="utf-8")
        run_fixture_git(work, "add", "-A")
        run_fixture_git(work, "commit", "-q", "--no-verify", "-m", f"the policy, {scope} {trust.strip()}")
        run_fixture_git(work, "push", "-q", "--no-verify", "origin", "main")

    def write_tag(sha, node_line, signer, tree, signed=True):
        rec = {"verdict": "GREEN", "tree": tree, "run_id": "r1"}
        if signed:
            run_fixture_git(work, "config", "user.signingkey", pathlib.Path(top, f"key-{signer}").as_posix())
        why = (write_peer_tag if signed else write_unsigned_tag)(work, sha, rec, node_line, "origin")
        if why:
            raise OSError(why)

    def run_node_read(name, sha, owed, needles):
        run_scenario(name, work, [*me, "read", "--backend", "peer-node", "--sha", sha], owed, needles,
                     GOV_NODE="a", GOV_REMOTE="origin")

    write_policy()
    sha = run_fixture_git(work, "rev-parse", "HEAD")
    tree = read_tree_of(work, sha)
    said = f"verdict: peer-node · %s · {sha[:8]}"
    if case == "peer":
        for name, node_line, signer, rec_tree, state in (("node b's tag read on node a", "b", "b", tree, "GREEN"),
                                                         ("node a's own tag", "a", "a", tree, "NONE"),
                                                         ("a tag naming another tree", "b", "b", "0" * len(tree), "NONE")):
            write_tag(sha, node_line, signer, rec_tree)
            run_node_read(name, sha, 0 if state == "GREEN" else 1, [said % state])
    elif case == "peer-signed":
        write_tag(sha, "b", "b", tree)
        run_node_read("node b's signed GREEN, the pin derived", sha, 0, [said % "GREEN" + " · witness witnessed"])
    elif case == "peer-self-tag":
        write_tag(sha, "b", "a", tree)
        run_node_read("node line b, node a's key", sha, 1, [said % "NONE", "signer a is not node b"])
    elif case == "peer-unsigned":
        write_tag(sha, "b", "b", tree, signed=False)
        run_node_read("an unsigned tag from node b", sha, 1, [said % "NONE", "unsigned"])
        run_fixture_git(work, "config", "user.signingkey", "")
        run_scenario("verify-peer with user.signingkey empty", work, [*me, "verify-peer"], 2,
                     ["verify-peer refused · user.signingkey"], GOV_NODE="b", GOV_REMOTE="origin")
    elif case == "peer-tip-missing":
        # A tag object naming a commit nobody has, written loose into the remote, so the ref is advertised
        # and the fetch, which must bring the commit in too, fails (TOOL-dWitnessedBar-56 S15).
        remote = pathlib.Path(top, "remote.git")
        body = (f"object {'1' * len(sha)}\ntype commit\ntag verdict-{sha}\n"
                f"tagger {run_fixture_git(work, 'var', 'GIT_COMMITTER_IDENT')}\n\nverdict\tGREEN\ntree\t{tree}\nnode\tb\n")
        rc, tag = run_git(remote, "hash-object", "-t", "tag", "-w", "--literally", "--stdin", data=body)
        if rc != 0 or not tag:
            raise OSError(f"git hash-object --literally exited {rc}, so no broken tag is planted")
        run_fixture_git(remote, "update-ref", VERDICT_REF + sha, tag)
        run_node_read("an advertised tip the fetch cannot bring in", sha, 1,
                      [said % "DEAD PROBE", f"git fetch origin {VERDICT_REF}{sha}"])
    elif case == "peer-no-ssh-keygen":
        write_tag(sha, "b", "b", tree)
        run_fixture_git(work, "config", "gpg.ssh.program", pathlib.Path(top, "absent", "ssh-keygen").as_posix())
        # TOOL-dWitnessedBar-63 AC12 (S20): a killed read's signer temp, aged past the grace, and a younger
        # one a concurrent read may still hold, both planted before the read.
        common = read_common_dir(work)
        aged, young = common / "gov-signers-aged", common / "gov-signers-young"
        for p in (aged, young):
            p.write_bytes(b"")
        old = time.time() - 2 * PEER_SIGNERS_GRACE_S
        os.utime(aged, (old, old))
        run_node_read("gpg.ssh.program at an absent path", sha, 1, [said % "DEAD PROBE", "verify-tag --raw"])
        # TOOL-dWitnessedBar-62 AC26: the failed read leaves no allowed-signers temp of its own in the common
        # git dir, listed by a process of its own as `ls <git-dir>` would; the aged temp is swept and the
        # young one kept, so the young one alone is left, else exit 1.
        run_scenario("no signer temp of the read left, the aged one swept, the young one kept", work,
                     [sys.executable, "-c", "import pathlib, sys; left = sorted(p.name for p in "
                      "pathlib.Path(sys.argv[1]).glob('gov-signers-*')); "
                      "print('signer temps left:', len(left), *left); sys.exit(0 if left == ['gov-signers-young'] else 1)",
                      str(common)], 0, ["signer temps left: 1 gov-signers-young"])
        young.unlink(missing_ok=True)
    elif case == "peer-bad-signature":
        write_tag(sha, "b", "b", tree)
        ref = VERDICT_REF + sha
        signed = run_fixture_git(work, "ls-remote", "origin", ref).split("\t")[0]
        body = run_fixture_git(work, "cat-file", "tag", signed) + "\n"
        if "run_id\tr1\n" not in body:
            raise OSError("the signed tag carries no run_id line to edit")
        rc, edited = run_git(work, "hash-object", "-t", "tag", "-w", "--stdin", data=body.replace("run_id\tr1\n", "run_id\tr2\n"))
        if rc != 0 or not edited:
            raise OSError(f"git hash-object exited {rc}, so no edited tag is written")
        run_fixture_git(work, "push", "-q", "--force", "--no-verify", "origin", f"{edited}:{ref}")
        run_node_read("a tag edited after node b signed it", sha, 1, [said % "NONE", "bad signature"])
    else:
        run_fixture_git(work, "checkout", "-q", "-b", "candidate")
        pathlib.Path(work, manifest).write_text("", encoding="utf-8")
        run_fixture_git(work, "commit", "-q", "--no-verify", "-am", "the leg manifest emptied")
        cand = run_fixture_git(work, "rev-parse", "HEAD")
        run_fixture_git(work, "checkout", "-q", "main")
        write_tag(cand, "b", "b", read_tree_of(work, cand))
        said = f"verdict: peer-node · %s · {cand[:8]}"
        run_node_read("under dispatch-closure", cand, 1, [said % "HELD", manifest])
        write_policy("workflow")
        run_node_read("under workflow, the workflow alone pinned", cand, 1,
                 [said % "HELD", "verdict.remote.pin-scope = workflow pins only"])
        write_policy("dispatch-closure", 'trust = "app-only"\n')
        run_node_read("under app-only", cand, 0, [said % "GREEN" + " · witness claimed"])


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


def run_off_node(backend_name, repo="."):
    """The `off-node` verb -> its exit: 0 when the row `verdict` names is off-node, 1 when it is not, 2 refused."""
    try:
        backends = read_backends(TOOL_ROOT)
        name = backend_name or read_backend_name(repo)
        backend = check_backend(name, backends)
    except Refusal as e:
        print(f"{SAY}: refused · {e}")
        return 2
    names = ", ".join(r["name"] for r in backends if r["off_node"]) or "none"
    print(f"{SAY}: off-node · {backend['name']} · {str(backend['off_node']).lower()} · off-node backends: {names}")
    return 0 if backend["off_node"] else 1


def main(argv):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace", newline="\n")
    ap = argparse.ArgumentParser(prog="verdict_backends.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("verb", nargs="?", choices=["read", "off-node", "verify-peer"])
    ap.add_argument("--backend", help="read this backend rather than the value `verdict` holds")
    ap.add_argument("--sha", help="the commit read")
    ap.add_argument("--remote", default=None, help="verify-peer's remote, origin by default")
    ap.add_argument("--fixture", action="store_true", help="run one plant's scenarios in a scratch directory")
    ap.add_argument("--plant", choices=list(PLANTS))
    args = ap.parse_args(argv)
    if args.fixture != bool(args.plant) or (args.fixture == bool(args.verb)):
        ap.error("one of read --sha <sha>, off-node, verify-peer or --fixture --plant <case>")
    if args.fixture:
        return run_fixture(args.plant)
    if args.verb == "off-node":
        return run_off_node(args.backend)
    if args.verb == "read":
        if not args.sha:
            ap.error("read takes --sha <sha>")
        return run_read(args.backend, args.sha)
    return run_verify_peer(args.remote or os.environ.get("GOV_REMOTE") or "origin")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
