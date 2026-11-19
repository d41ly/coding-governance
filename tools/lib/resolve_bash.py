"""resolve_bash -- the one bash a gov Python file runs, found by RUNNING each candidate (TOOL-dWitnessedBar-26).

The canonical `resolve_bash_py` block; its JavaScript twin is the `resolve_bash_js` block of
`resolve_bash.js` beside it. `<prefix>/lib/` is gov-internal and ships nothing, so a consumer carries
the block below INLINE, byte-identical, and keeps its own name and failure contract as a thin adapter
over the `(found, tried, refusal)` the block returns. `<prefix>/lib/resolve-python.test.sh`'s parity
table reds a copy that drifts, and its section 2j holds the two canonicals to one truth table.

    python <prefix>/lib/resolve_bash.py [--script <path>] [--host windows|posix]

prints one `tried: <candidate>: <why>` line per candidate, then `bash: <path>` and exit 0, or the
refusal line and exit 2.
"""
import argparse
import os
import subprocess
import sys


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


def main(argv=None):
    ap = argparse.ArgumentParser(prog="resolve_bash.py", description="The bash a gov tool runs, and every candidate tried.")
    ap.add_argument("--script", default="", help="a file the bash must be able to `test -f`")
    ap.add_argument("--host", choices=("windows", "posix"), default="", help="the host rule, this host's by default")
    opts = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    found, tried, refusal = scan_bash(opts.script, opts.host)
    for line in tried:
        print("tried: " + line)
    if found:
        print("bash: " + found)
        return 0
    print("refused: " + refusal)
    return 2


if __name__ == "__main__":
    sys.exit(main())
