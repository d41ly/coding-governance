#!/usr/bin/env python3
"""precommit.py — the pre-commit hook's leg list, DERIVED from the manifest (TOOL-dWitnessedBar-10).

    bash <prefix>/run-gates/run-gates.sh --precommit            # the hook's one call
    python <prefix>/run-gates/precommit.py [--legs <path>]      # the same, under any python
    python <prefix>/run-gates/precommit.py --list               # each row's name, argv and trigger

THE LIST IS THE MANIFEST'S. Every row carrying `precommit`, an argv in the manifest's `{prefix}`
grammar, is a commit-time leg; a row without the key never runs here. The hook used to name each leg
by hand behind a trigger typed beside it, so a leg ran at commit time only if somebody edited the hook
(memory/gotchas/hand-named-gate-list-green-while-the-bar-reds.md).

THE TRIGGER IS THE ROW'S `guard`, read with the runner's semantics: a staged path trips a guard when it
equals it or sits under it as a directory, and a guard ending in `/` names a directory only. A row
with no guard runs at every commit. There is no second, commit-time trigger: that would be a second
declaration of what a leg reads beside the one the bar already uses (spec §8 F1).

THE MANIFEST is `--legs <path>`, else `GATE_LEGS`, else the one beside this kit dir, as the runner
reads it. `{prefix}` resolves against the manifest's own directory, the tool root. The staged set is
listed once, from the index this process sees: the hook runs this outside the index git handed it,
as the hand-named legs ran.

PER ROW, in manifest order, one line: `pre-commit: <name> not tripped`, `pre-commit: <name> ok`, or
`pre-commit: <name> FAILED (rc <n>)`. A row whose argv names a script absent from the tree prints the
hook's announced skip and is not a failure, as the hook's own miss is. `python`/`python3` runs under
this interpreter, and `bash` under the bash the `resolve_bash_py` block finds by running it. The leg's
own output passes through unfiltered.

EXIT 0 every run row passed or none ran · 1 a run row failed · 2 the manifest cannot be read.

WHAT IT DOES NOT CHECK. Whether a leg's commit-time argv grades what its bar argv grades: the two sit
side by side in one declaration, where a reviewer reads them. And the memory hygiene leg: its
commit-time form is a grade, a check-9 render and a regrade no one argv states, so the hook keeps it
hand-named and the leg declares no `precommit` (spec §8 F3).
"""
import argparse
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(os.path.abspath(__file__)).parent
SAY = "pre-commit"
# The argv words that name an interpreter this process resolves itself, never by PATH.
PYTHON_WORDS = ("python", "python3")
BASH_WORDS = ("bash",)
# The suffixes that mark an argv element as a script whose absence is the announced skip.
SCRIPT_SUFFIXES = (".sh", ".py", ".js")


# >>> resolve_prefix_token -- canonical copy: resolve_prefix_token.py in the gov lib dir (byte-identical; gated)
def resolve_prefix_token(spelled, troot):
    """<spelled> with its {prefix} token resolved against the tool root <troot>.

    An empty or "." root is a root install: the token drops with its slash, and a bare token
    becomes ".". Any other root replaces the token. Text with no token passes unchanged.
    """
    spelled = str(spelled)
    if not troot or troot == ".":
        return spelled.replace("{prefix}/", "").replace("{prefix}", ".")
    return spelled.replace("{prefix}", troot)
# <<< resolve_prefix_token


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


_BASH = []


def resolve_bash_launcher():
    """(the bash to run, "") or ("", the refusal): the `resolve_bash_py` block, asked once per run."""
    if not _BASH:
        found, _tried, refusal = scan_bash()
        _BASH.append((found, refusal))
    return _BASH[0]


def read_manifest(path):
    """The manifest's rows, or exit 2 naming the path: an unreadable manifest is never an empty list."""
    try:
        rows = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"{SAY}: cannot read the leg manifest {path}: {e}", file=sys.stderr)
        raise SystemExit(2)
    if not isinstance(rows, list):
        print(f"{SAY}: the leg manifest {path} is not a JSON list", file=sys.stderr)
        raise SystemExit(2)
    return [r for r in rows if isinstance(r, dict)]


def read_staged(root):
    """The staged paths: added, copied, modified or renamed, NUL-separated so no name is C-quoted."""
    out = subprocess.run(["git", "-C", str(root), "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z"],
                         capture_output=True)
    return [p for p in out.stdout.decode("utf-8", "replace").split("\0") if p]


def check_guard_trips(path, guard):
    """The runner's guard match: the exact path, or anything under it as a directory; a guard ending in
    `/` names a directory, so it never matches a file of that exact name."""
    g = guard.rstrip("/")
    return (path == g and not guard.endswith("/")) or path.startswith(g + "/")


def derive_trigger(row, troot):
    """The row's resolved guard list; empty means every commit."""
    return [resolve_prefix_token(g, troot) for g in (row.get("guard") or [])]


def resolve_argv(row, troot):
    """The row's `precommit` argv with `{prefix}` resolved against the tool root."""
    return [resolve_prefix_token(a, troot) for a in row["precommit"]]


def derive_missing_script(argv, root):
    """The first argv element naming a script absent from the tree, or ""."""
    for a in argv[1:]:
        if a.endswith(SCRIPT_SUFFIXES) and not a.startswith("-") and not (pathlib.Path(root) / a).is_file():
            return a
    return ""


def run_precommit(rows, root, troot, staged):
    """Run every tripped row's argv; the count of failed runs."""
    failed = 0
    for row in rows:
        nm = row.get("name")
        guards = derive_trigger(row, troot)
        if guards and not any(check_guard_trips(p, g) for p in staged for g in guards):
            print(f"{SAY}: {nm} not tripped", flush=True)
            continue
        argv = resolve_argv(row, troot)
        miss = derive_missing_script(argv, root)
        if miss:
            print(f"{SAY}: {nm} leg SKIPPED — no kit root: {miss} is absent from this tree.", flush=True)
            continue
        if argv[0] in PYTHON_WORDS:
            argv[0] = sys.executable
        elif argv[0] in BASH_WORDS:
            bash, refusal = resolve_bash_launcher()
            if not bash:
                print(f"{SAY}: {nm} FAILED — {refusal}", flush=True)
                failed += 1
                continue
            argv[0] = bash
        try:
            rc = subprocess.run(argv, cwd=str(root), stdin=subprocess.DEVNULL).returncode
        except OSError as e:
            print(f"{SAY}: {nm} FAILED — {argv[0]} did not start: {e}", flush=True)
            failed += 1
            continue
        if rc == 0:
            print(f"{SAY}: {nm} ok", flush=True)
        else:
            print(f"{SAY}: {nm} FAILED (rc {rc})", flush=True)
            failed += 1
    return failed


def main(argv=None):
    ap = argparse.ArgumentParser(prog="precommit.py", description="Run every manifest row's `precommit` argv its guard trips.")
    ap.add_argument("--legs", default="", help="a leg manifest (default: GATE_LEGS, else the manifest beside this kit dir)")
    ap.add_argument("--list", action="store_true", help="print each row's name, argv and trigger, and run nothing")
    a = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    top = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, encoding="utf-8")
    if top.returncode != 0:
        print(f"{SAY}: not a git work tree", file=sys.stderr)
        return 2
    root = pathlib.Path(top.stdout.strip())
    legs = pathlib.Path(a.legs or os.environ.get("GATE_LEGS") or HERE.parent / "gate-legs.json")
    legs = legs if legs.is_absolute() else pathlib.Path.cwd() / legs
    try:
        troot = pathlib.Path(os.path.abspath(legs)).parent.relative_to(os.path.abspath(root)).as_posix()
    except ValueError:
        troot = "."
    rows = [r for r in read_manifest(legs) if isinstance(r.get("precommit"), list) and r["precommit"]]
    if not rows:
        print(f"{SAY}: no row of {legs.name} carries `precommit`, so nothing ran")
        return 0
    if a.list:
        for r in rows:
            guards = derive_trigger(r, troot)
            print(f"{r.get('name')}\t{' '.join(resolve_argv(r, troot))}\t"
                  f"{'guard ' + ','.join(guards) if guards else 'every commit'}")
        return 0
    return 1 if run_precommit(rows, root, troot, read_staged(root)) else 0


if __name__ == "__main__":
    sys.exit(main())
