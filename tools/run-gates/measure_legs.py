#!/usr/bin/env python3
"""measure_legs.py — every manifest leg run clean and unbounded, each one profiled down to its processes.

    python <prefix>/run-gates/measure_legs.py --serial                      # one leg at a time
    python <prefix>/run-gates/measure_legs.py --concurrent                  # admitted under a live load cap
    python <prefix>/run-gates/measure_legs.py --serial --legs <path> --out <root>
    python <prefix>/run-gates/measure_legs.py --selftest                    # its arms, over its own fixtures

TOOL-dRedressedBar-18. The bar's profile had to be rebuilt from scratch files the runner erases. It
came from a run with a knob in its environment, saw nothing inside a leg, and called the bar
spawn-bound from a ten-second CPU average. This verb runs every leg the manifest beside this kit
declares, read at run time so a leg added later is profiled with no edit here: guarded legs,
kit-subject legs and `selftests` legs included, with no guard, hold, reuse, docs mode, ceiling,
whole-run wall, retry or reap. Every record lands under `<git-dir>/gate-profile/<run id>/`.

WHAT EACH READING COMES FROM.
  * Per-leg totals: a Windows Job Object made for the leg before any of its processes exist. Its
    kernel accounting counts every process the leg spawned, user and kernel time, peak commit and
    I/O exactly, short-lived processes included.
  * Per-process rows: the process-monitor census, polled every `--census-every` seconds and walked
    from the leg's root. A process that starts and ends between two scans is invisible to it, and
    the job's exact count minus the census rows is recorded as `unseen`.
  * The cost of one spawn: the runner's own `measure_spawn_cost`, run from its source every census
    tick. The host's CPU and memory load: `GetSystemTimes` and `GlobalMemoryStatusEx` every second,
    neither of which spawns.
  * Foreign gate work beside a leg: the runner's census predicate, ported and held to the runner's
    awk by a selftest arm. The host turnstile: its slot beacons and queue, read and never written.

AN ALIAS LAUNCHER RUNS AS THE INTERPRETER IT STARTS (F3, resolved b). Every process a Microsoft Store
App Execution Alias starts leaves the leg's job, so a PYBIN that is one would read one process per
leg. Before the first leg the launchers are probed: one whose file carries the alias reparse tag runs,
in every leg, as the interpreter that alias reports as `sys.executable`, and the legs' `GOV_PYTHON`
names it. The interpreter the legs will run must keep its child inside a test job, or the run refuses.
The envelope's `substitutions` names each one, because a substituted reading lacks the alias's own
process per launch and is therefore not the bar's.

WHAT IT DOES NOT CHECK, said here because a profile reads as a verdict to everybody who did not
write it. It grades no leg: `ok` and `fail` are the leg's exit status, recorded. It sees no work
done for a leg by another process, a WMI host answering a query or a scanner opening an image, and
no bar on another turnstile key. A leg sleeping, or waiting in the host queue, longer than the stall
window reads STALLED, and the record names the waiting tickets so a queue wait reads as one. It
runs on Windows only and refuses anywhere else. It never signals a process that has run: a leg that
never ends keeps the run open, by the owner's design. The one terminate is a leg's root that could
not join its job or be resumed, still suspended and having executed nothing (TOOL-dRedressedBar-19
S35); that leg records `fail`, rc 1 and a `launch_error`, and the run goes on.

A DEAD RUN'S RAW CAPTURES ARE SWEPT. Each run writes `owner.json` into its scratch dir, and at start
redacts and deletes the raw captures of every sibling scratch dir whose owner is proved dead by pid
and creation time, naming each in the envelope's `raw_recovered` (TOOL-dRedressedBar-19 S38).

NO KNOB. Every setting is a flag. Every `GATE_*` name, every name `git rev-parse --local-env-vars`
prints and every name the push hook's `unset GIT_…` line names is scrubbed from each leg's
environment. The set is DERIVED at run time and printed, and the values are never recorded. The one
variable this tool sets in a leg's environment beyond the runner's `TMPDIR` is the existing
`GOV_PYTHON`, and only when an alias was resolved.

EXIT 0 every leg ended and every record was written, whatever the legs' verdicts · 1 a record write
failed, named on stderr · 2 a refusal before the first leg · 130 an interrupt, which writes the
envelope, names each running leg's kept capture, and leaves the legs running.
"""
import argparse
import ast
import contextlib
import ctypes
import fnmatch
import hashlib
import io
import json
import os
import posixpath
import re
import shutil
import socket
import stat
import statistics
import subprocess
import sys
import tempfile
import threading
import time
from datetime import datetime, timezone
from types import SimpleNamespace

KITDIR = os.path.dirname(os.path.abspath(__file__))
# The runner is this file's SIBLING and is never spelled: forward-slashed before bash sees it, for the
# reason profile_bar.py records beside its own RUNNER.
RUNNER = os.path.join(KITDIR, "run-gates.sh").replace("\\", "/")
FIXTURES = os.path.join(KITDIR, "fixtures", "measure-legs")
sys.path.insert(0, KITDIR)
import held_halves  # noqa: E402  the sibling: load_manifest, the one leg-manifest reader (S19)
import profile_bar  # noqa: E402  the sibling: resolve_bash, run_git, check_quiet, derive_regime

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

# >>> resolve_kit_dir — canonical copy: resolve_kit_dir.py in gov's lib dir (byte-identical; gated)
def resolve_kit_dir(home, anchor, here):
    """The directory holding <anchor> of the kit gov homes at <tool root>/<home>, in THIS install.

    1. receipt — the `.governance/install.json` row whose `source` ends in <home>/<anchor> and
       whose `path` exists inside this tree. The only record of a RENAMED kit dir: no probe finds
       a memory-recall kit an adopter homed at `scripts/recall/`.
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
        if str(row.get("source") or "").split("/")[-2:] != [home, anchor]:
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

# ---- declared constants. W and C below are declared bounds, not measurements.
HOST_EVERY_S = 1                  # the main loop's host-load tick
CPU_CAP_PCT = 80                  # --concurrent admits only at or under this host CPU load
MEM_CAP_PCT = 90                  # ... and at or under this memory load (the owner's caps)
CENSUS_EVERY_DEFAULT_S = 5.0      # --census-every, bounded 1 to 3600
STALL_WINDOW_DEFAULT_S = 300.0    # --stall-window W, bounded 2 x the census period to 86400
STALL_CPU_DEFAULT_S = 1.0         # --stall-cpu C, bounded above 0 and to 3600
FLAG_MAX_CHARS = 4096             # any flag value longer than this refuses at parse
HOLD_BEACON_WAIT_S = 120          # the selftest's wait for its holder's slot beacon, the bound its budget row prices
# The runner functions this tool runs from the runner's own source text. A name the runner lacks is
# a refusal before the first leg, never a profile that quietly records no spawn cost (AC2).
RUNNER_FUNCTIONS = ("resolve_python", "measure_spawn_cost", "read_spawn_floor")
EPOCH_AS_FILETIME = 116444736000000000   # 1970-01-01 in 100 ns ticks since 1601

# ---- the Windows API surface. Values from the Windows SDK headers.
CREATE_SUSPENDED = 0x00000004
PROCESS_TERMINATE = 0x0001        # AssignProcessToJobObject requires it; the one terminate is S35's
PROCESS_SET_QUOTA = 0x0100
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
SYNCHRONIZE = 0x00100000
THREAD_SUSPEND_RESUME = 0x0002
TH32CS_SNAPTHREAD = 0x00000004
JOB_BASIC_AND_IO_ACCOUNTING = 8   # JobObjectBasicAndIoAccountingInformation
JOB_EXTENDED_LIMIT = 9            # JobObjectExtendedLimitInformation
WAIT_OBJECT_0 = 0
MAX_WAIT_HANDLES = 64
RESUME_FAILED = 0xFFFFFFFF
STILL_ACTIVE = 259                # GetExitCodeProcess of a process that has not exited
ERROR_INVALID_PARAMETER = 87      # OpenProcess of a pid no process carries

WRITE_FAILURES = []               # every record write that failed this run; exit 1 names them


class ProfileRefused(RuntimeError):
    """A precondition the profile cannot run without. Exit 2, before the first leg."""


class LaunchFailed(OSError):
    """A leg's root could not join its job or be resumed, and was terminated still suspended (S35).
    Its one argument is the record's `launch_error`: `launch: <call> <winerror>`."""


class IoCounters(ctypes.Structure):
    _fields_ = [(n, ctypes.c_uint64) for n in (
        "ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
        "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]


class BasicAccounting(ctypes.Structure):
    _fields_ = [("TotalUserTime", ctypes.c_int64), ("TotalKernelTime", ctypes.c_int64),
                ("ThisPeriodTotalUserTime", ctypes.c_int64), ("ThisPeriodTotalKernelTime", ctypes.c_int64),
                ("TotalPageFaultCount", ctypes.c_uint32), ("TotalProcesses", ctypes.c_uint32),
                ("ActiveProcesses", ctypes.c_uint32), ("TotalTerminatedProcesses", ctypes.c_uint32)]


class BasicAndIoAccounting(ctypes.Structure):
    _fields_ = [("BasicInfo", BasicAccounting), ("IoInfo", IoCounters)]


class BasicLimit(ctypes.Structure):
    _fields_ = [("PerProcessUserTimeLimit", ctypes.c_int64), ("PerJobUserTimeLimit", ctypes.c_int64),
                ("LimitFlags", ctypes.c_uint32), ("MinimumWorkingSetSize", ctypes.c_size_t),
                ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", ctypes.c_uint32),
                ("Affinity", ctypes.c_size_t), ("PriorityClass", ctypes.c_uint32),
                ("SchedulingClass", ctypes.c_uint32)]


class ExtendedLimit(ctypes.Structure):
    _fields_ = [("BasicLimitInformation", BasicLimit), ("IoInfo", IoCounters),
                ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t),
                ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]


class MemoryStatus(ctypes.Structure):
    _fields_ = [("dwLength", ctypes.c_uint32), ("dwMemoryLoad", ctypes.c_uint32)] + [
        (n, ctypes.c_uint64) for n in ("ullTotalPhys", "ullAvailPhys", "ullTotalPageFile",
                                       "ullAvailPageFile", "ullTotalVirtual", "ullAvailVirtual",
                                       "ullAvailExtendedVirtual")]


class ThreadEntry(ctypes.Structure):
    _fields_ = [("dwSize", ctypes.c_uint32), ("cntUsage", ctypes.c_uint32),
                ("th32ThreadID", ctypes.c_uint32), ("th32OwnerProcessID", ctypes.c_uint32),
                ("tpBasePri", ctypes.c_int32), ("tpDeltaPri", ctypes.c_int32),
                ("dwFlags", ctypes.c_uint32)]


# ================================================================== the runner, read as text

def read_runner_text(path=RUNNER):
    """The runner's source, LF only, or a refusal: every runner function this tool runs comes from it."""
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read().replace("\r\n", "\n")
    except OSError as exc:
        raise ProfileRefused("cannot read the runner beside this tool, %s: %s" % (path, exc))


def extract_runner_function(runner_text, name):
    """The text of the runner's `<name>() {` definition, through its closing `}` at column 0.

    The extraction seam the turnstile suite uses (`sed -n '/^name() {/,/^}/p'`), read in Python. A
    one-line definition, `redact() { …; }`, is returned as its line. A name the runner does not
    define REFUSES: a profile that silently ran no spawn measurement would record a zero cost.
    """
    head = name + "() {"
    lines = runner_text.split("\n")
    for k, line in enumerate(lines):
        if not line.startswith(head):
            continue
        rest = line[len(head):].rstrip()
        if rest.endswith("}") and not rest.lstrip().startswith("#"):
            return line
        for j in range(k + 1, len(lines)):
            if lines[j].startswith("}"):
                return "\n".join(lines[k:j + 1])
        break
    raise ProfileRefused("the runner %s defines no function `%s` this tool can run from its source. "
                         "Refusing before the first leg rather than profiling without it." % (RUNNER, name))


def read_digest_classes(runner_text):
    """The verdict-relevant environment classes, read from the runner's `# digest-env-names` line."""
    m = re.search(r"^\s*([^)\s]+)\)\s.*#\s*digest-env-names\s*$", runner_text, re.M)
    if not m:
        raise ProfileRefused("the runner carries no `# digest-env-names` line, so the verdict-relevant "
                             "environment classes cannot be read from it")
    return m.group(1).split("|")


def read_kit_version(runner_text):
    """`KIT_RUN_GATES_VERSION` as the runner states it, or `unknown`."""
    m = re.search(r"^KIT_RUN_GATES_VERSION=([0-9][0-9.]*)", runner_text, re.M)
    return m.group(1) if m else "unknown"


def run_bash(bash, script, args=(), env=None, cwd=None, timeout=120):
    """One `bash -c <script> measure-legs <args…>` run: (rc, stdout, stderr), decoded, CR-free."""
    try:
        done = subprocess.run([bash, "-c", script, "measure-legs"] + [str(a) for a in args],
                              env=env, cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True,
                              timeout=timeout)
    except (OSError, subprocess.SubprocessError) as exc:
        return 127, "", str(exc)
    return (done.returncode, done.stdout.decode("utf-8", "replace").replace("\r", ""),
            done.stderr.decode("utf-8", "replace").replace("\r", ""))


def resolve_leg_python(bash, env, fn_text):
    """PYBIN: what the runner's own `resolve_python`, run from its source, prints under `env`."""
    rc, out, err = run_bash(bash, fn_text + "\nresolve_python\n", env=env)
    first = out.split("\n", 1)[0].strip()
    if rc != 0 or not first:
        raise ProfileRefused("the runner's resolve_python found no usable python under the legs' "
                             "environment (exit %d): %s" % (rc, err.strip()[-400:]))
    return first


def measure_spawn_us(bash, env, fn_text):
    """One sample of the cost of a spawn, in microseconds: the runner's `measure_spawn_cost 3`. None
    when it measured nothing, which it never rounds to a figure."""
    rc, out, _err = run_bash(bash, "SPAWN_CMD=\n" + fn_text + '\nmeasure_spawn_cost 3\nprintf "%s" "$SPAWN_US"\n',
                             env=env, timeout=60)
    out = out.strip()
    return int(out) if rc == 0 and out.isdigit() and int(out) > 0 else None


def read_spawn_floor_us(bash, env, fn_text, path):
    """(microseconds or None, state) from the runner's own `read_spawn_floor` over its floor file."""
    rc, out, _err = run_bash(bash, fn_text + '\nread_spawn_floor "$1"\n'
                             'printf "%s\\t%s" "$SPAWN_FLOOR_US" "$SPAWN_FLOOR_STATE"\n',
                             [path], env=env, timeout=60)
    us, _sep, state = out.partition("\t")
    return (int(us) if rc == 0 and us.isdigit() else None), (state.strip() or "unread")


SCRATCH_SCRIPT = r'''d=$(mktemp -d "${TMPDIR:-/tmp}/gate-profile.XXXXXXXX") || exit 3
mkdir "$d/tmp" "$d/raw" || exit 4
printf '%s\n' "$d"
cygpath -m "$d" 2>/dev/null || printf '%s\n' "$d"
'''


def build_scratch(bash, env):
    """The legs' scratch dir, made ONCE in the resolved bash as the runner makes its own: (bash
    spelling, the spelling this process opens). Its `tmp/` is every leg's TMPDIR and its `raw/`
    holds each leg's capture until the redacted copy exists. Never under the git dir, where git
    discovery answers differently and would move a leg's verdict."""
    rc, out, err = run_bash(bash, SCRATCH_SCRIPT, env=env)
    lines = [ln for ln in out.split("\n") if ln]
    if rc != 0 or len(lines) < 2:
        raise ProfileRefused("the legs' scratch dir could not be made in %s (exit %d): %s"
                             % (bash, rc, (err or out).strip()[-400:]))
    if not os.path.isdir(lines[1]):
        # S15: native Python resolves an MSYS spelling against the drive root, where no such dir is.
        raise ProfileRefused("the legs' scratch dir %s, spelled %s for this process, is no directory it "
                             "can open: this tool opens only its `cygpath -m` spelling" % (lines[0], lines[1]))
    return lines[0], lines[1]


# No fallback after `cygpath -m` (TOOL-dRedressedBar-19 S11): the bash spelling handed to native
# Python resolves against the drive root, where no key is, so every tick would read as an EMPTY host.
TURNSTILE_SCRIPT = r'''d=${GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile}
if [ -d "$d" ]; then d=$(cd "$d" 2>/dev/null && pwd) || exit 3; fi
printf '%s\n' "$d"
cygpath -m "$d" 2>/dev/null
'''
DRIVE_SPELLING = re.compile(r"^[A-Za-z]:/")


def resolve_turnstile_dir(bash, env):
    """The host turnstile key the legs' bars resolve, by the runner's own expression in the resolved
    bash under the legs' environment: (bash spelling, the spelling this process opens). Resolved
    once. Nothing is created: an absent key reads as an empty one. ("", "") when it did not resolve,
    or when its conversion failed or printed no drive-letter spelling, which every tick then reads
    as a refused read, never as an empty one."""
    rc, out, _err = run_bash(bash, TURNSTILE_SCRIPT, env=env)
    lines = [ln for ln in out.split("\n") if ln]
    if rc != 0 or len(lines) < 2 or not DRIVE_SPELLING.match(lines[1]):
        return "", ""
    return lines[0], lines[1]


# ================================================================== the environment a leg gets

def read_local_env_vars(top):
    """`git rev-parse --local-env-vars`, or None when git refused: that half of the scrub is unarmed."""
    names = profile_bar.run_git(["rev-parse", "--local-env-vars"], cwd=top).split()
    return names or None


def read_hook_unsets(top):
    """The names on the push hook's `unset GIT_…` line, or None when the hook is absent or unreadable."""
    try:
        with open(os.path.join(top, ".githooks", "pre-push"), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
    except OSError:
        return None
    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("unset GIT_"):
            return [w for w in line.split()[1:] if re.fullmatch(r"[A-Z_][A-Z0-9_]*", w)]
    return []


def derive_scrub_set(env_names, git_names, hook_names):
    """[(name, rule)] for every name in `env_names` a leg must not inherit, first matching rule named.

    No `GATE_` name is exempt, the turnstile's two nesting names included: the profile holds no
    turnstile, so an inherited holder nonce would nest a leg's bar under some other bar.
    """
    out = []
    for name in sorted(env_names):
        if name.startswith("GATE_"):
            rule = "GATE_ prefix"
        elif git_names and name in git_names:
            rule = "git rev-parse --local-env-vars"
        elif hook_names and name in hook_names:
            rule = "pre-push unset line"
        else:
            continue
        out.append((name, rule))
    return out


def derive_env_digest(env, classes):
    """{name: first 12 hex of the SHA-256 of its value} for every verdict-relevant name, and PATH."""
    out = {}
    for name in sorted(env):
        if name == "PATH" or any(fnmatch.fnmatchcase(name, c) for c in classes):
            out[name] = hashlib.sha256(env[name].encode("utf-8", "surrogatepass")).hexdigest()[:12]
    return out


# Each launcher as the legs' bash resolves it, and beside it the `cygpath -m` spelling this process
# opens (S15): the bash spelling omits the `.exe` and reads `/c/...`, which native Python resolves
# against the drive root. An empty conversion is printed empty, never replaced by the bash spelling.
# A `command -v` answer with no slash is a builtin or a function, which is no file and is not converted.
TOOLS_SCRIPT = r'''for w in "$@"; do
  p=$(command -v -- "$w" 2>/dev/null); m=
  case $p in */*) m=$(cygpath -m -- "$p" 2>/dev/null) ;; esac
  printf 'launcher\t%s\t%s\t%s\n' "$w" "$p" "$m"
done
'''


def read_tool_versions(bash, env, pybin, launchers, top):
    """The tools a leg's verdict can depend on: each launcher's resolved path in the legs' bash with
    its `cygpath -m` spelling (None when `command -v` finds none), `bash --version`'s first line,
    PYBIN and its version, `git version`, and the two eol settings."""
    _rc, out, _err = run_bash(bash, TOOLS_SCRIPT, list(launchers), env=env, cwd=top)
    resolved = {}
    for line in out.split("\n"):
        parts = line.split("\t")
        if len(parts) == 4 and parts[0] == "launcher":
            resolved[parts[1]] = {"posix": parts[2], "path": parts[3]} if parts[2] else None
    try:
        bv = subprocess.run([bash, "--version"], capture_output=True, timeout=60, env=env)
        bash_version = bv.stdout.decode("utf-8", "replace").split("\n", 1)[0].strip()
    except (OSError, subprocess.SubprocessError):
        bash_version = ""
    _rc, pv, _err = run_bash(bash, '"$1" --version 2>&1', [pybin], env=env, cwd=top)
    return {
        "launchers": resolved,
        "bash": bash,
        "bash_version": bash_version,
        "pybin": pybin,
        "pybin_version": pv.strip().split("\n", 1)[0],
        "git_version": profile_bar.run_git(["version"], cwd=top),
        "core.autocrlf": profile_bar.run_git(["config", "--get", "core.autocrlf"], cwd=top) or None,
        "core.eol": profile_bar.run_git(["config", "--get", "core.eol"], cwd=top) or None,
    }


# ================================================================== the manifest

def read_profile_legs(path):
    """The manifest's rows, every one of them, read by the runner kit's one manifest reader,
    `held_halves.load_manifest`, whose refusals this tool raises as its own (S19). Then refuses an
    empty list, a name that is no string or holds a tab, CR or LF, an argv that is not a non-empty
    list of strings, a duplicate name, and an argv token still carrying `{` once `{prefix}` is
    resolved: a profile of a malformed manifest is a profile of nothing in particular. Every row
    refusal names the row's index (S37)."""
    # load_manifest's `refuse` must not return; a lambda cannot `raise`, so it throws into a generator.
    data = held_halves.load_manifest(path, refuse=lambda msg: (_ for _ in ()).throw(ProfileRefused(msg)))
    if not data:
        raise ProfileRefused("the leg manifest %s holds no leg, so there is nothing to profile" % path)
    seen = set()
    for k, row in enumerate(data):
        name = row["name"]
        if not isinstance(name, str) or any(c in name for c in "\t\r\n"):
            raise ProfileRefused("row %d of %s: its name %r is not one line of text, which every record "
                                 "here keys a leg by" % (k, path, name))
        argv = row.get("argv")
        if not isinstance(argv, list) or not argv or not all(isinstance(a, str) for a in argv):
            raise ProfileRefused("row %d of %s: leg '%s' carries no argv list of strings" % (k, path, name))
        if name in seen:
            raise ProfileRefused("row %d of %s: leg '%s' appears a second time" % (k, path, name))
        seen.add(name)
        unresolved = [a for a in argv if "{" in resolve_prefix_token(a, ".")]
        if unresolved:
            raise ProfileRefused("row %d of %s: leg '%s' carries %s, a token this tool cannot resolve"
                                 % (k, path, name, ", ".join(repr(a) for a in unresolved)))
    return data


def derive_leg_argv(row, troot, pybin, aliases=None):
    """The argv the runner would run: `{prefix}` resolved, a first word `python`/`python3` -> PYBIN.
    Then a first word an alias substitution resolved -> the interpreter that alias starts (S14)."""
    argv = [resolve_prefix_token(a, troot) for a in row["argv"]]
    if argv[0] in ("python", "python3"):
        argv[0] = pybin
    if aliases and argv[0] in aliases:
        argv[0] = aliases[argv[0]]
    return argv


def derive_census_tokens(kitrel, argvs):
    """The runner's foreign-census tokens: its own two runner paths and every argv word carrying a
    `/` and ending `.sh`, `.py` or `.js`, a word with whitespace in it excepted."""
    out = [kitrel + "/" + os.path.basename(RUNNER), kitrel + "/run-selftests.sh"]
    for argv in argvs:
        for w in argv:
            if any(c.isspace() for c in w) or "/" not in w or not w.endswith((".sh", ".py", ".js")):
                continue
            if w not in out:
                out.append(w)
    return out


REDACT_BYTES = re.compile(rb"://[^/@ \t\n\v\f\r]+:[^/@ \t\n\v\f\r]+@")
REDACT_TEXT = re.compile(r"://[^/@ \t\n\v\f\r]+:[^/@ \t\n\v\f\r]+@")


def derive_redacted(data):
    """URL userinfo masked as the runner's `redact` masks it: `://***:***@`. Bytes in, bytes out."""
    if isinstance(data, bytes):
        return REDACT_BYTES.sub(b"://***:***@", data)
    return REDACT_TEXT.sub("://***:***@", data)


# ================================================================== the foreign census

def measure_foreign(rows, tokens, own):
    """(count, [(winpid, token)]): foreign gate-work trees, by the runner's predicate over census rows.

    A row is gate work when its command carries a token, or a word ending `.test.sh` or
    `selftest.py`. Rows in `own`, this profiler's ancestors and descendants, are never foreign. A
    tree counts once, at its topmost matching process: a match whose parent also matched is not a
    root. Parents are the census's union graph, msys parents translated through the census's own
    join, which over single-parent rows is exactly the runner's `ps -ef` graph.
    """
    by_msys = {r["msys_pid"]: r["winpid"] for r in rows if r.get("msys_pid") is not None}
    par, hit = {}, {}
    for r in rows:
        ps = set()
        if r.get("win_ppid") is not None:
            ps.add(r["win_ppid"])
        if r.get("msys_ppid") is not None and r["msys_ppid"] in by_msys:
            ps.add(by_msys[r["msys_ppid"]])
        ps.discard(r["winpid"])
        par[r["winpid"]] = ps
        cmd = r.get("command") or ""
        tok = next((t for t in tokens if t in cmd), None)
        if tok is None:
            tok = next((w for w in cmd.split() if w.endswith(".test.sh") or w.endswith("selftest.py")), None)
        if tok is not None:
            hit[r["winpid"]] = tok
    cand = {p for p in hit if p not in own}
    roots = sorted((p, hit[p]) for p in cand if not (par.get(p, set()) & cand))
    return len(roots), roots


# ================================================================== the host turnstile, read only

def read_ticket_stamp(name):
    """The epoch second a ticket's `<UTC stamp>-<pid>-<random>` name was stamped at, or None."""
    try:
        return datetime.strptime(name.split("-", 1)[0], "%Y%m%dT%H%M%S").replace(
            tzinfo=timezone.utc).timestamp()
    except ValueError:
        return None


def read_turnstile(ts_dir):
    """{"holders": [(slot, msys pid)], "tickets": [(name, msys pid, stamp)]}: one listing and one small
    read per slot beacon, no spawn and no write. An absent key or queue reads empty, because the
    runner creates both on first use. A key that exists and cannot be read raises OSError."""
    if not ts_dir:
        raise OSError("the turnstile key did not resolve")
    holders, tickets = [], []
    try:
        names = os.listdir(ts_dir)
    except FileNotFoundError:
        return {"holders": holders, "tickets": tickets}
    for slot in sorted(names):
        if slot != "gate-bar-beacon" and not slot.startswith("gate-bar-beacon."):
            continue
        try:
            with open(os.path.join(ts_dir, slot, "pid"), encoding="utf-8", errors="replace") as fh:
                pid = fh.readline().strip()
        except FileNotFoundError:
            continue
        if pid.isdigit():
            holders.append((slot, int(pid)))
    try:
        queue = os.listdir(os.path.join(ts_dir, "gate-bar-queue"))
    except FileNotFoundError:
        queue = []
    for name in sorted(queue):
        parts = name.split("-")
        if len(parts) >= 3 and parts[1].isdigit():
            tickets.append((name, int(parts[1]), read_ticket_stamp(name)))
    return {"holders": holders, "tickets": tickets}


def derive_leg_turnstile(rows, trees, ts):
    """Attribute one tick's turnstile read by the census of the same tick.

    `trees` maps a leg index to the winpids of its tree. A holder or ticket pid (an MSYS pid) in a
    leg's tree belongs to that leg; one in any other row is `foreign`; one no row carries is not
    judged at this tick and reads None.
    """
    by_msys = {r["msys_pid"]: r["winpid"] for r in rows if r.get("msys_pid") is not None}
    owner_of = {}
    for i, tree in trees.items():
        for w in tree:
            owner_of[w] = i

    def resolve_owner(pid):
        w = by_msys.get(pid)
        return None if w is None else owner_of.get(w, "foreign")

    return {"holders": [(pid, resolve_owner(pid)) for _slot, pid in ts["holders"]],
            "tickets": [(name, resolve_owner(pid)) for name, pid, _stamp in ts["tickets"]]}


def derive_turnstile_wait(sightings, tick_t, stamps, lo, hi):
    """(ts_queued, ts_wait_s, waiting ticket names) for one leg.

    A ticket is the leg's bar WAITING only when it was seen at two consecutive census ticks: an
    uncontended acquire holds its ticket for one attempt's few processes. The wait is the length of
    the union of the waiting tickets' intervals, each from its name's stamp to its last sighting,
    clipped to the leg's [lo, hi].
    """
    spans, waiting = [], []
    for name, ks in sightings.items():
        ks = sorted(set(ks))
        if not any(b == a + 1 for a, b in zip(ks, ks[1:])):
            continue
        waiting.append(name)
        a = stamps.get(name)
        a = tick_t[ks[0]] if a is None else a
        a, b = max(a, lo), min(tick_t[ks[-1]], hi)
        if b > a:
            spans.append((a, b))
    total, cur = 0.0, None
    for a, b in sorted(spans):
        if cur is None or a > cur[1]:
            if cur is not None:
                total += cur[1] - cur[0]
            cur = [a, b]
        else:
            cur[1] = max(cur[1], b)
    if cur is not None:
        total += cur[1] - cur[0]
    return len(waiting), round(total, 3), sorted(waiting)


# ================================================================== admission and stalls

def check_admit(cpu, mem, running, fresh, cpu_cap=CPU_CAP_PCT, mem_cap=MEM_CAP_PCT):
    """May --concurrent admit one more leg? Yes when no leg of the run is running — the `drained`
    release of the runner's memory pause, so foreign load can delay a profile and never deadlock it.
    Otherwise only on a FRESH sample, taken after the previous admission, at or under both caps."""
    if running == 0:
        return True
    return bool(fresh) and cpu is not None and mem is not None and cpu <= cpu_cap and mem <= mem_cap


def check_stalled(tree_delta, job_delta, log_same, cpu_cap):
    """True when, over one window, the tree's census CPU delta AND the job's exact CPU delta are both
    under `cpu_cap` and the log did not grow; None when the tick cannot be judged. The job veto is
    what keeps a silent leg working through children shorter than a scan from reading STALLED."""
    if tree_delta is None or job_delta is None:
        return None
    return tree_delta < cpu_cap and job_delta < cpu_cap and bool(log_same)


# ================================================================== the job API

def resolve_job_backend(platform=None):
    """The kernel32 surface every per-leg total is read from, or a refusal naming the platform.

    Windows only, by design: every registered node is Windows and so is every CI job, so a POSIX
    backend would be untested scaffolding. A platform without the Job Object API refuses rather
    than profiling less.
    """
    platform = sys.platform if platform is None else platform
    if not str(platform).startswith("win"):
        raise ProfileRefused(
            "platform %r has no Windows Job Object API (CreateJobObjectW, QueryInformationJobObject), "
            "which every per-leg total here is read from, and no POSIX backend is built" % platform)
    k32 = ctypes.WinDLL("kernel32", use_last_error=True)
    h, b, d, p = ctypes.c_void_p, ctypes.c_int, ctypes.c_uint32, ctypes.c_void_p
    sigs = {
        "CreateJobObjectW": (h, [p, ctypes.c_wchar_p]),
        "AssignProcessToJobObject": (b, [h, h]),
        "QueryInformationJobObject": (b, [h, ctypes.c_int, p, d, p]),
        "OpenProcess": (h, [d, b, d]),
        "OpenThread": (h, [d, b, d]),
        "ResumeThread": (d, [h]),
        "CloseHandle": (b, [h]),
        "CreateToolhelp32Snapshot": (h, [d, d]),
        "Thread32First": (b, [h, p]),
        "Thread32Next": (b, [h, p]),
        "GetProcessTimes": (b, [h, p, p, p, p]),
        "GetExitCodeProcess": (b, [h, p]),
        "WaitForSingleObject": (d, [h, d]),
        "WaitForMultipleObjects": (d, [d, p, b, d]),
        "GetSystemTimes": (b, [p, p, p]),
        "GlobalMemoryStatusEx": (b, [p]),
    }
    api = {}
    for name, (restype, argtypes) in sigs.items():
        fn = getattr(k32, name)
        fn.restype, fn.argtypes = restype, argtypes
        api[name] = fn
    return SimpleNamespace(**api)


def build_job(api):
    """A fresh job with NO limit flags: no breakaway, no silent breakaway, no kill-on-close."""
    job = api.CreateJobObjectW(None, None)
    if not job:
        raise OSError(ctypes.get_last_error(), "CreateJobObjectW failed")
    return job


def read_job_accounting(api, job):
    """The job's exact totals: processes, user and kernel seconds, I/O, and its two memory peaks."""
    acct, ext = BasicAndIoAccounting(), ExtendedLimit()
    if not api.QueryInformationJobObject(job, JOB_BASIC_AND_IO_ACCOUNTING, ctypes.byref(acct),
                                         ctypes.sizeof(acct), None) \
            or not api.QueryInformationJobObject(job, JOB_EXTENDED_LIMIT, ctypes.byref(ext),
                                                 ctypes.sizeof(ext), None):
        raise OSError(ctypes.get_last_error(), "QueryInformationJobObject failed")
    b, o = acct.BasicInfo, acct.IoInfo
    return {
        "user_s": round(b.TotalUserTime / 1e7, 4),
        "kernel_s": round(b.TotalKernelTime / 1e7, 4),
        "procs_total": b.TotalProcesses,
        "active": b.ActiveProcesses,
        "io": {"read_ops": o.ReadOperationCount, "write_ops": o.WriteOperationCount,
               "other_ops": o.OtherOperationCount, "read_bytes": o.ReadTransferCount,
               "write_bytes": o.WriteTransferCount, "other_bytes": o.OtherTransferCount},
        "peak_job_mem_b": ext.PeakJobMemoryUsed,
        "peak_proc_mem_b": ext.PeakProcessMemoryUsed,
    }


def read_host_load(api, prev):
    """(cpu %, memory %, times): CPU busy over the interval since `prev`, None on the first call.
    busy = 100 x (kernel + user - idle) / (kernel + user); memory is `dwMemoryLoad`. No spawn."""
    idle, kern, user = ctypes.c_uint64(), ctypes.c_uint64(), ctypes.c_uint64()
    cpu = None
    cur = None
    if api.GetSystemTimes(ctypes.byref(idle), ctypes.byref(kern), ctypes.byref(user)):
        cur = (idle.value, kern.value, user.value)
        if prev is not None:
            di, dk, du = (c - q for c, q in zip(cur, prev))
            if dk + du > 0:
                cpu = round(100.0 * (dk + du - di) / (dk + du), 1)
    ms = MemoryStatus()
    ms.dwLength = ctypes.sizeof(ms)
    mem = ms.dwMemoryLoad if api.GlobalMemoryStatusEx(ctypes.byref(ms)) else None
    return cpu, mem, cur


def run_leg(api, bash, argv, env, cwd, capture):
    """Launch one leg SUSPENDED, put its root in a fresh job, then resume its one thread.

    The root is `<bash> -c 'exec "$@"' measure-legs <argv…>`, the runner's own worker shape, so the
    leg resolves `bash`, `node` and PYBIN through MSYS `PATH` as it would under the bar. Its stdin is
    the null device and its stdout and stderr go to one capture FILE: a pipe's read end closing
    would SIGPIPE an orphan still writing. No descendant exists before the job does, so the job
    counts every process the leg ever starts. The start stamp is taken at the resume.

    THE ONE TERMINATE (S35). When `OpenProcess`, the job assign, the thread snapshot or the resume
    fails, the root is still suspended and has executed nothing: it is terminated through the
    handle `CreateProcess` returned, `Popen.terminate`'s `TerminateProcess(hProcess, 1)`, and
    `LaunchFailed` names the call. Left alone it would stay suspended for ever, holding the capture.
    The job is left to close with this process, as every leg's job is.
    """
    job = build_job(api)
    with open(capture, "wb") as fh:
        proc = subprocess.Popen([bash, "-c", 'exec "$@"', "measure-legs"] + list(argv), cwd=cwd, env=env,
                                stdin=subprocess.DEVNULL, stdout=fh, stderr=subprocess.STDOUT,
                                creationflags=CREATE_SUSPENDED)
    hq = api.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION | SYNCHRONIZE, False, proc.pid)
    failed = None if hq else ("OpenProcess", ctypes.get_last_error())
    ha = None
    if failed is None:
        ha = api.OpenProcess(PROCESS_SET_QUOTA | PROCESS_TERMINATE, False, proc.pid)
        failed = None if ha else ("OpenProcess", ctypes.get_last_error())
    if failed is None and not api.AssignProcessToJobObject(job, ha):
        failed = ("AssignProcessToJobObject", ctypes.get_last_error())
    if ha:
        api.CloseHandle(ha)
    resumed = 0
    if failed is None:
        snap = api.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0)
        if not snap or snap == ctypes.c_void_p(-1).value:
            failed = ("CreateToolhelp32Snapshot", ctypes.get_last_error())
        else:
            te = ThreadEntry()
            te.dwSize = ctypes.sizeof(te)
            ok = api.Thread32First(snap, ctypes.byref(te))
            while ok and failed is None:
                if te.th32OwnerProcessID == proc.pid:
                    ht = api.OpenThread(THREAD_SUSPEND_RESUME, False, te.th32ThreadID)
                    if not ht:
                        failed = ("OpenThread", ctypes.get_last_error())
                    else:
                        if api.ResumeThread(ht) == RESUME_FAILED:
                            failed = ("ResumeThread", ctypes.get_last_error())
                        else:
                            resumed += 1
                        api.CloseHandle(ht)
                ok = api.Thread32Next(snap, ctypes.byref(te))
            api.CloseHandle(snap)
            if failed is None and not resumed:
                failed = ("ResumeThread", ctypes.get_last_error())
    if failed is not None:
        proc.terminate()
        try:
            proc.wait(timeout=30)
        except subprocess.TimeoutExpired:
            pass
        if hq:
            api.CloseHandle(hq)
        raise LaunchFailed("launch: %s %d" % failed)
    return {"proc": proc, "pid": proc.pid, "job": job, "hq": hq, "started_ns": time.time_ns()}


def read_root_exit(api, hq):
    """(ended epoch ns, exit code) once the root has exited, else None. The end is the root's
    `ExitTime` on a handle held since launch, so the loop's poll latency never enters a wall time."""
    if api.WaitForSingleObject(hq, 0) != WAIT_OBJECT_0:
        return None
    code = ctypes.c_uint32()
    api.GetExitCodeProcess(hq, ctypes.byref(code))
    created, exited, kern, user = (ctypes.c_uint64() for _ in range(4))
    api.GetProcessTimes(hq, ctypes.byref(created), ctypes.byref(exited), ctypes.byref(kern),
                        ctypes.byref(user))
    return (exited.value - EPOCH_AS_FILETIME) * 100, code.value


def scan_root_exits(api, handles, timeout_s):
    """Block until one of `handles` exits or `timeout_s` passes. Never signals anything."""
    ms = max(0, int(timeout_s * 1000))
    if not handles:
        time.sleep(ms / 1000.0)
        return
    first = handles[:MAX_WAIT_HANDLES]
    arr = (ctypes.c_void_p * len(first))(*first)
    api.WaitForMultipleObjects(len(first), arr, False, ms)


# ================================================================== alias launchers (S14, F3 resolved b)
#
# A Microsoft Store App Execution Alias is a reparse point Windows answers by activating a packaged
# app, and every process it starts leaves the leg's job: on node d, 2026-10-15, PYBIN was the
# `python3` alias and every leg read one process. The owner chose to run the interpreter the alias
# starts (F3 b), so a substituted reading lacks the alias's own process per launch, and says so.

# The child-starting program the interpreter probe runs, and the job wait that bounds each launch.
JOB_CHILD_PROGRAM = "import subprocess, sys; sys.exit(subprocess.call([sys.executable, '-I', '-c', 'pass']))"
JOB_PROBE_WAIT_S = 120            # a probe launch not ended by then refuses; nothing is signalled


def check_app_alias(path):
    """True when <path> is an App Execution Alias: `os.lstat` reads the file system's own reparse
    tag, `IO_REPARSE_TAG_APPEXECLINK`. `os.path.islink` reads False for one (measured on node d,
    2026-10-15), so a link test would let every alias through. False for any other file, for a path
    that does not exist, and on a platform whose `stat` carries no such tag."""
    tag = getattr(stat, "IO_REPARSE_TAG_APPEXECLINK", None)
    try:
        st = os.lstat(path)
    except (OSError, ValueError):
        return False
    return tag is not None and getattr(st, "st_reparse_tag", 0) == tag


def resolve_alias_interpreter(bash, env, top, launcher, alias):
    """The interpreter the alias <launcher> starts, forward-slashed: its own `sys.executable`, printed
    by running it once in the legs' bash as PYBIN spells it. Refuses unless that is a file and no
    alias itself, naming the alias and what it printed."""
    rc, out, err = run_bash(bash, '"$1" -I -c \'import sys; print(sys.executable)\'', [launcher],
                            env=env, cwd=top)
    printed = out.split("\n", 1)[0].strip()
    resolved = printed.replace("\\", "/")
    if rc != 0 or not resolved or not os.path.isfile(resolved) or check_app_alias(resolved):
        raise ProfileRefused("PYBIN %s is the App Execution Alias %s, and what it printed as its "
                             "interpreter (exit %d) is no plain file to run in its place: %r%s"
                             % (launcher, alias, rc, printed, ("; " + err.strip()[-300:]) if err.strip() else ""))
    return resolved


def measure_job_children(api, bash, env, top, interp):
    """(TotalProcesses with one child, without one): <interp> launched twice as a leg is launched,
    its output sent to the null device. One run starts `sys.executable -I -c pass` and waits for it;
    its twin runs `-I -c pass`. The twin cancels the wrapper and the interpreter, so the difference
    is 1 exactly when the child stayed in the job. Nothing is signalled: a launch that has not ended
    within `JOB_PROBE_WAIT_S` refuses."""
    counts = []
    for program in (JOB_CHILD_PROGRAM, "pass"):
        try:
            launched = run_leg(api, bash, [interp, "-I", "-c", program], env, top, os.devnull)
        except OSError as exc:
            raise ProfileRefused("the interpreter probe could not launch %s in a job: %s" % (interp, exc))
        try:
            if api.WaitForSingleObject(launched["hq"], JOB_PROBE_WAIT_S * 1000) != WAIT_OBJECT_0:
                raise ProfileRefused("the interpreter probe of %s did not end within %d s"
                                     % (interp, JOB_PROBE_WAIT_S))
            counts.append(read_job_accounting(api, launched["job"])["procs_total"])
        except OSError as exc:
            raise ProfileRefused("the interpreter probe of %s read no job accounting: %s" % (interp, exc))
        finally:
            launched["proc"].poll()
            api.CloseHandle(launched["hq"])
            api.CloseHandle(launched["job"])
    return counts[0], counts[1]


def resolve_launcher_aliases(api, bash, env, top, pybin, argvs, launchers):
    """Steps 1 to 4 of the alias rule, once, before the first leg: ([substitution…], interpreter probe).

    1. The probed set: PYBIN, and each distinct first word of `argvs`, which are already PYBIN-mapped,
       each as `launchers` holds it: `command -v` in the legs' bash and its `cygpath -m` spelling. One
       `command -v` did not find is unresolved and probed no further, and its leg fails as it would
       under the bar. A builtin or a function is no file and runs in the legs' bash, inside the job.
    2. Detection: `check_app_alias` over the converted spelling. A found launcher whose file
       `os.lstat` cannot read REFUSES, because nothing then proves it is no alias.
    3. Resolution: PYBIN's alias by `resolve_alias_interpreter`. A leg launcher that is an alias and
       is not PYBIN REFUSES, because no rule here resolves one.
    4. Verification: `measure_job_children` over the interpreter the legs will run, the resolved one
       or PYBIN itself, on EVERY run. Totals that do not differ by exactly 1 REFUSE, naming it: no job
       reading of a leg it runs would be true.
    A substitution is {launcher, alias, resolved, applied}, `applied` naming `argv0` when a leg runs
    it first and `GOV_PYTHON` always. A probe program that rebinds this function to return
    ([], None) disables detection and verification together: AC1's resolution red half.
    """
    substitutions = []
    for word in dict.fromkeys([pybin] + [a[0] for a in argvs]):
        found = launchers.get(word)
        if not found or "/" not in found["posix"]:
            continue
        path = found["path"]
        if path and not os.path.isabs(path):
            path = os.path.join(top, path).replace("\\", "/")
        try:
            os.lstat(path)
        except (OSError, ValueError) as exc:
            raise ProfileRefused("the launcher %s resolves to %s, spelled %r here, which os.lstat cannot "
                                 "read (%s), so nothing proves it is no App Execution Alias"
                                 % (word, found["posix"], path, exc))
        if not check_app_alias(path):
            continue
        if word != pybin:
            raise ProfileRefused("the leg launcher %s is the App Execution Alias %s, and no rule here "
                                 "resolves an alias that is not PYBIN (%s)" % (word, path, pybin))
        substitutions.append({"launcher": word, "alias": path,
                              "resolved": resolve_alias_interpreter(bash, env, top, word, path),
                              "applied": (["argv0"] if any(a[0] == word for a in argvs) else [])
                              + ["GOV_PYTHON"]})
    interp = substitutions[0]["resolved"] if substitutions else pybin
    with_child, without_child = measure_job_children(api, bash, env, top, interp)
    if with_child - without_child != 1:
        raise ProfileRefused("the interpreter %s keeps no child inside a job: launched as a leg is, with "
                             "one child it read %d processes and without one %d, a difference of %d "
                             "where 1 is the child. No job reading of a leg it runs would be true."
                             % (interp, with_child, without_child, with_child - without_child))
    return substitutions, {"interpreter": interp, "with_child": with_child, "without_child": without_child}


# ================================================================== the census side

def load_process_monitor():
    """The process-monitor kit's census, reap and scope modules, from the sibling kit dir."""
    try:
        pm_dir = resolve_kit_dir("process-monitor", "census.py", KITDIR)
    except LookupError as exc:
        raise ProfileRefused("the process-monitor kit is not resolvable beside this kit: %s" % exc)
    if str(pm_dir) not in sys.path:
        sys.path.insert(0, str(pm_dir))
    import census
    import reap
    import scope
    return SimpleNamespace(census=census, reap=reap, scope=scope, dir=str(pm_dir))


def scan_leg_trees(pm, rows, roots):
    """{leg index: [winpid…]}: each leg's process tree in this scan, walked from its root."""
    present = {r["winpid"] for r in rows}
    return {i: [w for w in pm.reap.build_walk(rows, root) if w in present] for i, root in roots.items()}


def scan_census_tick(pm, bash, env, spawn_fn, ts_dir):
    """One census tick, run on the worker thread: the scan, one spawn-cost sample, the turnstile read.
    A refusal of any of the three is recorded on the tick, never raised."""
    tick = {"t": time.time(), "m0": time.monotonic(), "rows": None, "refused": "",
            "spawn_us": None, "ts": None, "ts_refused": ""}
    try:
        tick["rows"], counts = pm.census.scan_processes()
        tick["backend"] = counts.get("backend")
    except pm.census.CensusRefused as exc:
        tick["refused"] = str(exc)
    tick["scan_s"] = round(time.monotonic() - tick["m0"], 3)
    tick["spawn_us"] = measure_spawn_us(bash, env, spawn_fn)
    try:
        tick["ts"] = read_turnstile(ts_dir)
    except OSError as exc:
        tick["ts_refused"] = str(exc) or "refused"
    tick["m1"] = time.monotonic()
    return tick


def run_census_worker(box, *args):
    """The worker thread's body: one tick into `box`, whatever it raised recorded as a refusal."""
    try:
        box["tick"] = scan_census_tick(*args)
    except Exception as exc:  # a worker that died must read as a refused tick, never as no tick
        box["tick"] = {"t": time.time(), "m0": time.monotonic(), "m1": time.monotonic(), "rows": None,
                       "refused": "census worker raised %r" % exc, "spawn_us": None, "ts": None,
                       "ts_refused": "census worker raised", "scan_s": 0.0}


# ================================================================== records

def write_atomic(path, data):
    """`data` (bytes) into `path`, owner-only, through a temp file and a rename. A failure is named
    and remembered, never raised: the run goes on, and exits 1."""
    tmp = path + ".tmp"
    try:
        fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | getattr(os, "O_BINARY", 0), 0o600)
        with os.fdopen(fd, "wb") as fh:
            fh.write(data)
        os.replace(tmp, path)
        return True
    except OSError as exc:
        WRITE_FAILURES.append("%s: %s" % (path, exc))
        print("measure-legs: RECORD WRITE FAILED — %s: %s" % (path, exc), file=sys.stderr, flush=True)
        return False


def write_record_line(path, line):
    """One LF-terminated line appended to `path`, owner-only; a failure is named and remembered."""
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND | getattr(os, "O_BINARY", 0), 0o600)
        with os.fdopen(fd, "wb") as fh:
            fh.write((line + "\n").encode("utf-8"))
        return True
    except OSError as exc:
        WRITE_FAILURES.append("%s: %s" % (path, exc))
        print("measure-legs: RECORD WRITE FAILED — %s: %s" % (path, exc), file=sys.stderr, flush=True)
        return False


def write_envelope(run_dir, envelope):
    """`envelope.json`, rewritten whole through a temp file and a rename."""
    return write_atomic(os.path.join(run_dir, "envelope.json"),
                        (json.dumps(envelope, indent=1) + "\n").encode("utf-8"))


def render_leg_row(rec):
    """The runner's eight-field `.leg` row. The eighth field is `foreign + ts_holders + ts_queued`,
    or `unknown` when the census or the turnstile read was refused at any tick of the window, so
    `derive-ceilings.py`'s `read_runs` sets a contended reading aside by the rule it already applies."""
    parts = (rec.get("foreign"), rec.get("ts_holders"), rec.get("ts_queued"))
    if rec.get("census_refused") or any(not isinstance(v, int) or isinstance(v, bool) for v in parts):
        eighth = "unknown"
    else:
        eighth = str(sum(parts))
    return "\t".join([rec["name"], rec["verdict"], str(rec["rc"]), "%.3f" % rec["wall_s"],
                      str(rec["started_ns"]), str(rec["ended_ns"]), "-", eighth])


def write_leg_record(run_dir, rec):
    """`<i>.json`, the full profile of one leg."""
    return write_atomic(os.path.join(run_dir, "%d.json" % rec["i"]),
                        (json.dumps(rec, indent=1) + "\n").encode("utf-8"))


HOST_HEADER = "epoch_ns\tcpu_pct\tmem_pct\trunning\tevent"
CENSUS_HEADER = "epoch\tforeign\troots\tscan_s\tspawn_us\tholders\ttickets"
LEGS_COLUMNS = ("i", "name", "verdict", "rc", "wall_s", "work_s", "ts_wait_s", "user_s", "kernel_s",
                "procs_total", "active_peak", "left_running", "unseen", "peak_job_mem_b",
                "peak_proc_mem_b", "avg_ws_b", "io.read_ops", "io.write_ops", "io.other_ops",
                "io.read_bytes", "io.write_bytes", "io.other_bytes", "spawn_us.min",
                "spawn_us.median", "spawn_us.max", "spawn_s_est", "spawn_share", "foreign",
                "ts_holders", "ts_queued", "host_cpu.mean", "host_cpu.max", "host_mem.mean",
                "host_mem.max", "queued_s", "concurrency.at_admit", "concurrency.max", "ceiling",
                "share", "over_ceiling", "log_bytes", "started_ns", "ended_ns")


def render_host_row(ns, cpu, mem, running, event):
    return "%d\t%s\t%s\t%d\t%s" % (ns, "-" if cpu is None else cpu, "-" if mem is None else mem,
                                   running, event or "-")


def render_census_row(tick):
    return "\t".join([str(int(tick["t"])), "unknown" if tick.get("foreign") is None else str(tick["foreign"]),
                      " ".join("%d:%s" % rt for rt in tick.get("roots", [])), "%.3f" % tick.get("scan_s", 0.0),
                      "-" if tick.get("spawn_us") is None else str(tick["spawn_us"]),
                      " ".join(tick.get("holder_cells", [])), " ".join(tick.get("ticket_cells", []))])


def render_legs_row(rec):
    """One `legs.tsv` row: the profile less `procs`, `stalls` and the run-end fields."""
    cells = []
    for col in LEGS_COLUMNS:
        v = rec
        for part in col.split("."):
            v = v.get(part) if isinstance(v, dict) else None
        cells.append("-" if v is None else str(v).replace("\t", " ").replace("\n", " "))
    return "\t".join(cells)


def measure_scratch_bytes(path):
    """The bytes under the legs' scratch dir, which nothing sweeps."""
    total = 0
    for base, _dirs, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(base, f))
            except OSError:
                pass
    return total


def derive_regimes(durations, cores, mode):
    """`derive_regime` at every power of two up to the logical core count: the width profile, read
    off unbounded durations, labelled with the mode they were taken in."""
    out, w = {}, 1
    while w <= max(1, cores):
        out[str(w)] = profile_bar.derive_regime(durations, w)
        w *= 2
    return {"mode": mode, "by_width": out}


def derive_mean_max(values):
    vals = [v for v in values if v is not None]
    return {"mean": round(sum(vals) / len(vals), 1), "max": max(vals)} if vals else None


def derive_leg_profile(leg, ticks, ctx):
    """The full per-leg record, from the leg's own state and the census ticks in its window.

    The window for the foreign count, the spawn samples and the refusal test is the runner's: ticks
    from three census periods before the leg started to its end, so a leg shorter than one period
    still has a sample. Holders and tickets count only at ticks the leg was running.
    """
    period = ctx["census_every"]
    s_s, e_s = leg["started_ns"] / 1e9, leg["ended_ns"] / 1e9
    win = [t for t in ticks if s_s - 3 * period <= t["t"] <= e_s]
    census_unknown = not win or any(t.get("foreign") is None for t in win)
    foreign = "unknown" if census_unknown else max(t["foreign"] for t in win)
    refused = census_unknown or any(t.get("ts_refused") for t in win)
    acct = leg.get("acct") or {}
    wall_s = round((leg["ended_ns"] - leg["started_ns"]) / 1e9, 3)
    tick_t = {t["k"]: t["t"] for t in ticks}
    ts_queued, ts_wait_s, waiting = derive_turnstile_wait(leg["ts_sightings"], tick_t, leg["ts_stamps"],
                                                          s_s, e_s)
    spawn = sorted(t["spawn_us"] for t in win if t.get("spawn_us"))
    spawn_us = {"min": spawn[0], "median": statistics.median(spawn), "max": spawn[-1],
                "samples": len(spawn)} if spawn else None
    procs_total = acct.get("procs_total")
    spawn_s_est = (round(procs_total * spawn_us["median"] / 1e6, 6)
                   if spawn_us and procs_total is not None else None)
    mem = sorted(leg["mem"])
    avg_ws_b = None
    if mem:
        weights = [(mem[k + 1][0] if k + 1 < len(mem) else e_s) - mem[k][0] for k in range(len(mem))]
        wsum = sum(w for w in weights if w > 0)
        avg_ws_b = (int(sum(m[1] * w for m, w in zip(mem, weights) if w > 0) / wsum) if wsum > 0
                    else int(sum(m[1] for m in mem) / len(mem)))
    procs = sorted(leg["procs"].values(), key=lambda p: (p["first_seen"], p["winpid"]))
    ceiling = leg["ceiling"]
    rec = {
        "i": leg["i"], "name": leg["name"], "argv": leg["argv"],
        "verdict": "ok" if leg["rc"] == 0 else "fail", "rc": leg["rc"],
        "wall_s": wall_s, "started_ns": leg["started_ns"], "ended_ns": leg["ended_ns"],
        "user_s": acct.get("user_s"), "kernel_s": acct.get("kernel_s"),
        "procs_total": procs_total, "active_peak": leg["active_peak"],
        "left_running": leg.get("left_running"),
        "peak_job_mem_b": acct.get("peak_job_mem_b"), "peak_proc_mem_b": acct.get("peak_proc_mem_b"),
        "avg_ws_b": avg_ws_b, "io": acct.get("io"),
        "spawn_us": spawn_us, "spawn_s_est": spawn_s_est,
        "spawn_share": round(spawn_s_est / wall_s, 4) if spawn_s_est is not None and wall_s > 0 else None,
        "procs": procs,
        "unseen": (procs_total - len(procs)) if procs_total is not None else None,
        "foreign": foreign,
        "ts_holders": len(leg["ts_holder_pids"]), "ts_queued": ts_queued,
        "ts_wait_s": ts_wait_s, "work_s": round(wall_s - ts_wait_s, 3),
        "ts_waiting_tickets": waiting, "census_refused": refused,
        "host_cpu": derive_mean_max(c for c, _m in leg["host"]),
        "host_mem": derive_mean_max(m for _c, m in leg["host"]),
        "queued_s": leg["queued_s"],
        "concurrency": {"at_admit": leg["conc_at_admit"], "max": leg["conc_max"]},
        "ceiling": ceiling,
        "share": round(wall_s / ceiling, 4) if ceiling else None,
        "over_ceiling": (wall_s > ceiling) if ceiling else None,
        "stalls": leg["stalls"], "stall_windows": leg["stall_windows"],
        "log_bytes": leg.get("log_bytes"), "job_final": None,
        "launch_error": leg.get("launch_error"),
    }
    return rec


# ================================================================== the run

def derive_tick_readings(tick, legs, ctx):
    """Fold one finished census tick into every leg it overlapped, and write its `census.tsv` row.

    Per overlapping leg: its tree, its per-process rows, its summed working set, the turnstile's
    holders and its own waiting tickets. Per leg still running: one stall window. The foreign
    census is the runner's predicate over this scan, this profiler's own ancestors and descendants
    excluded; a scan that cannot see this process reads `unknown`, as the runner's does.
    """
    pm, opts = ctx["pm"], ctx["opts"]
    tick["k"] = len(ctx["ticks"])
    ctx["ticks"].append(tick)
    t0, rows = tick["t"], tick["rows"]
    overlap = [lg for lg in legs if lg.get("admit_m") is not None and lg["admit_m"] <= tick["m1"]
               and (lg.get("end_m") is None or lg["end_m"] >= tick["m0"])]
    tick["foreign"], tick["roots"] = None, []
    if rows is None:
        write_record_line(os.path.join(ctx["run_dir"], "census.tsv"), render_census_row(tick))
        return
    by_win = {r["winpid"]: r for r in rows}
    trees = scan_leg_trees(pm, rows, {lg["i"]: lg["pid"] for lg in overlap})
    for lg in overlap:
        tree = trees[lg["i"]]
        mem_known = False
        mem_sum = 0
        for w in tree:
            r = by_win[w]
            p = lg["procs"].get(w)
            if p is None:
                p = lg["procs"][w] = {
                    "winpid": w, "msys_pid": r.get("msys_pid"), "ppid": r.get("win_ppid"),
                    "command": derive_redacted(r["command"]) if r.get("command") else None,
                    "first_seen": round(t0, 3), "start": round(t0 - r["age_s"], 3), "peak_mem_b": None}
            p["last_seen"] = round(t0, 3)
            p["cpu_s"] = r.get("cpu_s")
            p["mem_b"] = r.get("mem_b")
            if r.get("peak_mem_b") is not None:
                p["peak_mem_b"] = max(p["peak_mem_b"] or 0, r["peak_mem_b"])
            if r.get("mem_b") is not None:
                mem_known = True
                mem_sum += r["mem_b"]
        if mem_known:
            lg["mem"].append((t0, mem_sum))
    try:
        own = set(pm.scope.build_self_chain(rows, os.getpid())) | set(pm.reap.build_walk(rows, os.getpid()))
        tick["foreign"], tick["roots"] = measure_foreign(rows, ctx["tokens"], own)
    except pm.scope.ScopeRefused:
        pass
    if tick["ts"] is not None:
        att = derive_leg_turnstile(rows, {i: set(t) for i, t in trees.items()}, tick["ts"])
        stamps = {name: stamp for name, _pid, stamp in tick["ts"]["tickets"]}
        tick["holder_cells"] = ["%d:%s" % (pid, "unseen" if o is None else o) for pid, o in att["holders"]]
        tick["ticket_cells"] = ["%s:%s" % (name, "unseen" if o is None else o) for name, o in att["tickets"]]
        for pid, o in att["holders"]:
            if o == "foreign":
                for lg in overlap:
                    lg["ts_holder_pids"].add(pid)
        for name, o in att["tickets"]:
            if isinstance(o, int) and not isinstance(o, bool):
                legs[o]["ts_sightings"].setdefault(name, []).append(tick["k"])
                legs[o]["ts_stamps"][name] = stamps.get(name)
    for lg in overlap:
        if lg.get("end_m") is None:
            derive_stall_window(lg, tick, trees[lg["i"]], by_win, ctx)
    write_record_line(os.path.join(ctx["run_dir"], "census.tsv"), render_census_row(tick))


def derive_stall_window(lg, tick, tree, by_win, ctx):
    """One stall window for a running leg, ending at this tick: its tree's census CPU delta, its job's
    exact CPU delta and its log's growth against the newest earlier tick at least W seconds back.
    Opens an episode on the first STALLED window and closes it on the first that is not."""
    opts, api = ctx["opts"], ctx["api"]
    t0 = tick["t"]
    try:
        acct = read_job_accounting(api, lg["job"])
        job_cpu, procs_total = acct["user_s"] + acct["kernel_s"], acct["procs_total"]
    except OSError:
        job_cpu, procs_total = None, None
    try:
        log = os.path.getsize(lg["capture"])
    except OSError:
        log = None
    cpu = {w: by_win[w].get("cpu_s") for w in tree}
    if any(v is None for v in cpu.values()):
        cpu = None
    sample = {"k": tick["k"], "t": t0, "cpu": cpu, "job_cpu": job_cpu, "log": log, "procs_total": procs_total}
    lg["census"].append(sample)
    j = next((s for s in reversed(lg["census"][:-1]) if s["t"] <= t0 - opts.stall_window), None)
    if j is None:
        return
    tree_delta = job_delta = None
    deltas = {}
    if cpu is not None and j["cpu"] is not None:
        for w, c in cpu.items():
            d = c - j["cpu"].get(w, 0.0)
            deltas[w] = c if d < 0 else d
        tree_delta = round(sum(deltas.values()), 3)
    if job_cpu is not None and j["job_cpu"] is not None:
        job_delta = round(job_cpu - j["job_cpu"], 3)
    log_same = log is not None and log == j["log"]
    churn = (procs_total - j["procs_total"]) if procs_total is not None and j["procs_total"] is not None else None
    lg["stall_windows"].append({"t": round(t0, 3), "from": round(j["t"], 3), "tree_delta": tree_delta,
                                "job_delta": job_delta,
                                "log_delta": (log - j["log"]) if log is not None and j["log"] is not None else None,
                                "churn": churn})
    stalled = check_stalled(tree_delta, job_delta, log_same, opts.stall_cpu)
    ep = lg["episode"]
    if stalled and ep is None:
        waiting = sorted(n for n, ks in lg["ts_sightings"].items() if any(j["k"] <= k <= tick["k"] for k in ks))
        ep = lg["episode"] = {
            "opened": round(t0, 3), "closed": None, "how": None, "window_s": opts.stall_window,
            "job_delta": job_delta, "tree_delta": tree_delta, "log_bytes": log, "churn": churn,
            "waiting_tickets": waiting,
            "tree": [{"winpid": w, "msys_pid": by_win[w].get("msys_pid"), "ppid": by_win[w].get("win_ppid"),
                      "age_s": by_win[w].get("age_s"), "cpu_s": by_win[w].get("cpu_s"),
                      "cpu_delta": round(deltas.get(w, 0.0), 3), "mem_b": by_win[w].get("mem_b"),
                      "command": derive_redacted(by_win[w]["command"]) if by_win[w].get("command") else None}
                     for w in tree]}
        lg["stalls"].append(ep)
        print("measure-legs: STALLED  %s  (%gs: job +%ss, tree +%ss, log %s B unchanged)"
              % (lg["name"], opts.stall_window, job_delta, tree_delta, log), flush=True)
    elif stalled is False and ep is not None:
        ep["closed"], ep["how"] = round(t0, 3), "resumed"
        lg["episode"] = None
        print("measure-legs: RESUMED  %s  (after %.0fs stalled)" % (lg["name"], t0 - ep["opened"]), flush=True)


# ================================================================== a dead run's raw captures (S38)
#
# A run killed, crashed or powered off between a leg's end and its log's redaction leaves the leg's
# raw capture, unredacted, in its scratch dir. Each run therefore writes `owner.json` beside its own
# captures, and at start sweeps the siblings whose owner is PROVED dead: a pid alone is not proof,
# because pids are reused, and a profile running at the same moment must never lose a live capture.

def read_process_created(api, pid):
    """(state, creation FILETIME) of process <pid>. ("live", t) while it runs; ("dead", None) when
    `OpenProcess` reads ERROR_INVALID_PARAMETER, no such pid, or the process has exited; ("unknown",
    None) for any other failure, access denied included, which cannot prove an owner dead."""
    h = api.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    if not h:
        return ("dead" if ctypes.get_last_error() == ERROR_INVALID_PARAMETER else "unknown"), None
    try:
        code = ctypes.c_uint32()
        if not api.GetExitCodeProcess(h, ctypes.byref(code)):
            return "unknown", None
        if code.value != STILL_ACTIVE:
            return "dead", None
        created, exited, kern, user = (ctypes.c_uint64() for _ in range(4))
        if not api.GetProcessTimes(h, ctypes.byref(created), ctypes.byref(exited), ctypes.byref(kern),
                                   ctypes.byref(user)):
            return "unknown", None
        return "live", created.value
    finally:
        api.CloseHandle(h)


def derive_abandoned_scratch(api, scratch):
    """[(scratch dir, its owner's record dir)] for every `gate-profile.*` sibling of <scratch> whose
    `owner.json` reads and whose owner is dead: no live process carries that pid with that creation
    time. A scratch with no readable `owner.json`, or whose owner cannot be opened for a reason other
    than absence, is left alone, and so is this run's own."""
    parent, own = os.path.split(os.path.normpath(scratch))
    try:
        names = sorted(os.listdir(parent))
    except OSError:
        return []
    out = []
    for name in names:
        if not name.startswith("gate-profile.") or name == own:
            continue
        d = os.path.join(parent, name)
        try:
            with open(os.path.join(d, "owner.json"), encoding="utf-8") as fh:
                owner = json.load(fh)
            pid, created = owner["pid"], owner["created"]
        except (OSError, ValueError, TypeError, KeyError):
            continue
        if any(not isinstance(v, int) or isinstance(v, bool) for v in (pid, created)) or pid <= 0:
            continue
        state, now = read_process_created(api, pid)
        if state == "dead" or (state == "live" and now != created):
            out.append((d, owner.get("record")))
    return out


def write_recovered_logs(abandoned, run_dir):
    """Each abandoned scratch's `raw/<i>.out`, redacted by `derive_redacted` into `<record>/<i>.log.recovered`,
    or into `recovered/<scratch name>/` under this run's record when that record dir is gone; then the
    raw file deleted. Returns the envelope's `raw_recovered` entries, one per capture, naming the raw
    file, the recovered log and, where the raw file could not go, why it was kept."""
    out = []
    for d, record in abandoned:
        try:
            names = sorted(os.listdir(os.path.join(d, "raw")))
        except OSError:
            continue
        for f in names:
            stem = f[:-len(".out")] if f.endswith(".out") else ""
            if not stem.isdigit():
                continue
            raw = os.path.join(d, "raw", f)
            entry = {"raw": raw.replace("\\", "/"), "log": None}
            out.append(entry)
            dest_dir = (record if isinstance(record, str) and record and os.path.isdir(record)
                        else os.path.join(run_dir, "recovered", os.path.basename(d)))
            try:
                with open(raw, "rb") as fh:
                    data = fh.read()
                os.makedirs(dest_dir, mode=0o700, exist_ok=True)
            except OSError as exc:
                entry["kept"] = str(exc)
                continue
            dest = os.path.join(dest_dir, stem + ".log.recovered")
            if not write_atomic(dest, derive_redacted(data)):
                entry["kept"] = "its redacted copy could not be written"
                continue
            entry["log"] = dest.replace("\\", "/")
            try:
                os.remove(raw)
            except OSError as exc:
                entry["kept"] = str(exc)
    return out


def write_leg_capture(lg, final):
    """`<i>.log` from the raw capture, redacted; then the raw capture deleted when no leg process can
    still write it. Returns None once deleted, else the reason it is kept."""
    try:
        with open(lg["capture"], "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        return "unreadable: %s" % exc
    lg["log_bytes"] = len(raw)
    if not write_atomic(lg["log"], derive_redacted(raw)):
        return "its redacted copy could not be written"
    if not final and lg.get("left_running"):
        return "%d process(es) still running at the root's exit" % lg["left_running"]
    try:
        os.remove(lg["capture"])
    except OSError as exc:
        return "held by a process still running: %s" % exc
    return None


def parse_flags(argv):
    """The flags, bounded at parse: an over-long value, a non-number or one out of its bounds exits 2."""
    for a in argv:
        if len(a) > FLAG_MAX_CHARS:
            raise ProfileRefused("a flag value longer than %d characters" % FLAG_MAX_CHARS)
    ap = argparse.ArgumentParser(prog="measure_legs.py",
                                 description="Run every manifest leg clean and unbounded, profiled to its processes.")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--serial", action="store_true", help="one leg at a time")
    mode.add_argument("--concurrent", action="store_true",
                      help="admit the next leg only at or under %d%% CPU and %d%% memory" % (CPU_CAP_PCT, MEM_CAP_PCT))
    mode.add_argument("--selftest", action="store_true", help="run this tool's arms over its own fixtures")
    ap.add_argument("--legs", default="", help="a leg manifest (default: the manifest beside this kit dir)")
    ap.add_argument("--out", default="", help="the record root (default: <git-dir>/gate-profile)")
    ap.add_argument("--census-every", type=float, default=CENSUS_EVERY_DEFAULT_S, help="seconds, 1 to 3600")
    ap.add_argument("--stall-window", type=float, default=STALL_WINDOW_DEFAULT_S,
                    help="W seconds, 2 x the census period to 86400")
    ap.add_argument("--stall-cpu", type=float, default=STALL_CPU_DEFAULT_S, help="C CPU seconds, above 0 to 3600")
    try:
        opts = ap.parse_args(argv)
    except SystemExit as exc:
        raise ProfileRefused("the flags did not parse (argparse exit %s)" % exc.code)
    if not 1 <= opts.census_every <= 3600:
        raise ProfileRefused("--census-every %g is outside 1 to 3600" % opts.census_every)
    if not 2 * opts.census_every <= opts.stall_window <= 86400:
        raise ProfileRefused("--stall-window %g is outside %g to 86400" % (opts.stall_window, 2 * opts.census_every))
    if not 0 < opts.stall_cpu <= 3600:
        raise ProfileRefused("--stall-cpu %g is outside (0, 3600]" % opts.stall_cpu)
    opts.mode = "serial" if opts.serial else "concurrent" if opts.concurrent else "selftest"
    return opts


def run_profile(opts):
    """The profile itself. Returns the exit status: 0, 1 on a failed record write, 2 on a refusal
    before the first leg, 130 on an interrupt."""
    del WRITE_FAILURES[:]
    try:
        api = resolve_job_backend()
        pm = load_process_monitor()
        top = profile_bar.run_git(["rev-parse", "--show-toplevel"])
        if not top:
            raise ProfileRefused("not inside a git work tree, so there is no top level to run legs from")
        top = os.path.normpath(top)
        gitdir = profile_bar.run_git(["rev-parse", "--absolute-git-dir"], cwd=top)
        common = profile_bar.run_git(["rev-parse", "--git-common-dir"], cwd=top)
        if not gitdir or not common:
            raise ProfileRefused("git answered no git dir for %s" % top)
        common = os.path.normpath(os.path.join(top, common))
        runner_text = read_runner_text()
        fns = {name: extract_runner_function(runner_text, name) for name in RUNNER_FUNCTIONS}
        classes = read_digest_classes(runner_text)
        bash, tried = profile_bar.resolve_bash(RUNNER)
        if not bash:
            raise ProfileRefused("no bash could open the runner. Tried: %s" % ", ".join(tried))
        legs_path = os.path.abspath(opts.legs or os.path.join(os.path.dirname(KITDIR), "gate-legs.json"))
        rows = read_profile_legs(legs_path)
        git_names = read_local_env_vars(top)
        hook_names = read_hook_unsets(top)
        scrubbed = derive_scrub_set(list(os.environ), git_names, hook_names)
        gone = {name for name, _rule in scrubbed}
        base_env = {k: v for k, v in os.environ.items() if k not in gone}
        pybin = resolve_leg_python(bash, base_env, fns["resolve_python"])
        kitrel = os.path.relpath(KITDIR, top).replace("\\", "/")
        if kitrel.startswith(".."):
            kitrel = KITDIR.replace("\\", "/")
        troot = posixpath.dirname(kitrel) or "."
        argvs = [derive_leg_argv(r, troot, pybin) for r in rows]
        # S14, before anything is made: a refusal here leaves no scratch dir and no record behind.
        tools = read_tool_versions(bash, base_env, pybin, list(dict.fromkeys([pybin] + [a[0] for a in argvs])),
                                   top)
        substitutions, interpreter_probe = resolve_launcher_aliases(api, bash, base_env, top, pybin, argvs,
                                                                    tools["launchers"])
        aliases = {s["launcher"]: s["resolved"] for s in substitutions}
        argvs = [derive_leg_argv(r, troot, pybin, aliases) for r in rows]
        run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + "-" + str(os.getpid())
        out_root = os.path.abspath(opts.out) if opts.out else os.path.join(gitdir, "gate-profile")
        run_dir = os.path.join(out_root, run_id)
        scratch_posix, scratch = build_scratch(bash, base_env)
        # S38: this run's owner, written before any capture exists. With no creation time to record
        # none is written, and the scratch is then one no later run sweeps.
        _state, created = read_process_created(api, os.getpid())
        if created is not None:
            write_atomic(os.path.join(scratch, "owner.json"), (json.dumps(
                {"pid": os.getpid(), "created": created, "record": run_dir.replace("\\", "/")}) + "\n").encode("utf-8"))
        leg_env = dict(base_env)
        leg_env["TMPDIR"] = scratch_posix + "/tmp"
        if pybin in aliases:
            # Every `resolve_python` a leg's own scripts run picks GOV_PYTHON before `python3`, and an
            # operator's GOV_PYTHON naming the alias is overridden the same way. Set before the digest.
            leg_env["GOV_PYTHON"] = aliases[pybin]
        try:
            os.makedirs(run_dir, mode=0o700)
        except OSError as exc:
            raise ProfileRefused("the record dir %s could not be made: %s" % (run_dir, exc))
    except ProfileRefused as exc:
        print("measure-legs: REFUSED — %s" % exc, file=sys.stderr, flush=True)
        return 2

    raw_recovered = write_recovered_logs(derive_abandoned_scratch(api, scratch), run_dir)
    ts_posix, ts_dir = resolve_turnstile_dir(bash, leg_env)
    tokens = derive_census_tokens(kitrel, argvs)
    floor_us, floor_state = read_spawn_floor_us(bash, leg_env, fns["read_spawn_floor"],
                                                common.replace("\\", "/") + "/gate-spawn-floor")
    quiet, quiet_detail = profile_bar.check_quiet()
    envelope = {
        "run": run_id, "at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "sha": profile_bar.run_git(["rev-parse", "--short=8", "HEAD"], cwd=top) or "unknown",
        "host": socket.gethostname(), "width": None, "width_source": None, "full": True,
        "wall": None, "exit": None, "failed_legs": [],
        "env": {"quiet": quiet, "quiet_detail": quiet_detail}, "regime": None,
        "mode": opts.mode, "caps": {"cpu_pct": CPU_CAP_PCT, "mem_pct": MEM_CAP_PCT},
        "periods": {"host_every_s": HOST_EVERY_S, "census_every_s": opts.census_every},
        "stall": {"window_s": opts.stall_window, "cpu_s": opts.stall_cpu},
        "scrubbed": [{"name": n, "rule": r} for n, r in scrubbed],
        "scrub_rules": {"GATE_ prefix": "armed",
                        "git rev-parse --local-env-vars": git_names if git_names else "UNARMED: git refused",
                        "pre-push unset line": hook_names if hook_names is not None else "absent: no hook here"},
        "env_digest": derive_env_digest(leg_env, classes),
        "tools": tools,
        "pybin": pybin, "scratch": scratch, "scratch_posix": scratch_posix,
        "turnstile_dir": ts_dir, "turnstile_dir_posix": ts_posix,
        "substitutions": substitutions, "interpreter_probe": interpreter_probe, "raw_kept": [],
        "raw_recovered": raw_recovered,
        "manifest": {"path": legs_path, "blob": profile_bar.run_git(["hash-object", legs_path], cwd=top) or None},
        "legs": len(rows), "census_backend": None, "spawn_floor_us": floor_us,
        "spawn_floor_state": floor_state, "kit_version": read_kit_version(runner_text),
        "process_monitor": pm.dir, "regimes": None,
    }
    write_envelope(run_dir, envelope)
    print("measure-legs: run %s · %s · %d leg(s) from %s" % (run_id, opts.mode, len(rows), legs_path), flush=True)
    print("measure-legs: record %s" % run_dir, flush=True)
    print("measure-legs: scrubbed %s" % (", ".join("%s (%s)" % s for s in scrubbed) or "none"), flush=True)
    for s in substitutions:
        print("measure-legs: SUBSTITUTED %s %s -> %s" % (s["launcher"], s["alias"], s["resolved"]), flush=True)
    if not git_names:
        print("measure-legs: NOTE - git rev-parse --local-env-vars refused, so that half of the scrub is UNARMED",
              flush=True)
    print("measure-legs: turnstile key %s (read, never written)" % (ts_dir or "UNRESOLVED, every read refused"),
          flush=True)
    print("measure-legs: scratch %s (every leg's TMPDIR is its tmp/; nothing sweeps it)" % scratch, flush=True)
    for k in raw_recovered:
        print("measure-legs: dead run's raw capture %s -> %s%s" % (
            k["raw"], k["log"] or "not recovered", "; KEPT: %s" % k["kept"] if k.get("kept") else ""), flush=True)
    write_record_line(os.path.join(run_dir, "host.tsv"), HOST_HEADER)
    write_record_line(os.path.join(run_dir, "census.tsv"), CENSUS_HEADER)
    write_record_line(os.path.join(run_dir, "legs.tsv"), "\t".join(LEGS_COLUMNS))

    legs = [{"i": i, "name": r["name"], "argv": argvs[i],
             "ceiling": r["ceiling"] if isinstance(r.get("ceiling"), int) and not isinstance(r.get("ceiling"), bool)
             and r["ceiling"] > 0 else None,
             "capture": os.path.join(scratch, "raw", "%d.out" % i), "log": os.path.join(run_dir, "%d.log" % i),
             "host": [], "census": [], "procs": {}, "mem": [], "stall_windows": [], "stalls": [],
             "episode": None, "ts_holder_pids": set(), "ts_sightings": {}, "ts_stamps": {},
             "active_peak": 0, "conc_max": 0, "admit_m": None, "end_m": None}
            for i, r in enumerate(rows)]
    ctx = {"api": api, "pm": pm, "opts": opts, "run_dir": run_dir, "ticks": [], "tokens": tokens,
           "census_every": opts.census_every}
    pending = list(range(len(legs)))
    running, ending = {}, {}
    state = {"prev": None, "cpu": None, "mem": None, "sample_m": -1.0, "admit_m": -1.0, "peak": 0,
             "first_admit_m": None, "last_end_m": None, "eligible_m": time.monotonic()}

    def run_admission(event_rows):
        i = pending.pop(0)
        lg = legs[i]
        now = time.monotonic()
        lg["queued_s"] = round(now - state["eligible_m"], 3)
        try:
            launched = run_leg(api, bash, lg["argv"], leg_env, top, lg["capture"])
        except LaunchFailed as exc:
            # S35: its root was terminated still suspended. A failed leg with no job and no handle,
            # ended at its admission, and the run goes on.
            launched = {"proc": None, "pid": None, "job": None, "hq": None, "started_ns": time.time_ns(),
                        "launch_error": str(exc)}
        lg.update(launched)
        lg["admit_m"] = time.monotonic()
        running[i] = lg
        lg["conc_at_admit"] = len(running)
        for other in running.values():
            other["conc_max"] = max(other["conc_max"], len(running))
        state["peak"] = max(state["peak"], len(running))
        state["admit_m"] = lg["admit_m"]
        state["first_admit_m"] = state["first_admit_m"] or lg["admit_m"]
        if opts.mode == "concurrent":
            state["eligible_m"] = lg["admit_m"]
        event_rows.append("admit %d" % i)
        if lg.get("launch_error"):
            write_leg_end(i, lg["started_ns"], 1)
        return i

    def write_leg_end(i, ended_ns, rc):
        lg = running.pop(i)
        lg["ended_ns"], lg["rc"], lg["end_m"] = ended_ns, rc, time.monotonic()
        lg["acct"], lg["left_running"] = None, None
        if lg["job"] is not None:
            try:
                lg["acct"] = read_job_accounting(api, lg["job"])
                lg["left_running"] = lg["acct"]["active"]
            except OSError:
                lg["acct"], lg["left_running"] = None, None
        if lg["episode"] is not None:
            lg["episode"]["closed"], lg["episode"]["how"] = round(ended_ns / 1e9, 3), "ended"
            lg["episode"] = None
        lg["raw_pending"] = write_leg_capture(lg, final=False)
        if lg["proc"] is not None:
            lg["proc"].poll()
        state["last_end_m"] = lg["end_m"]
        if opts.mode == "serial":
            state["eligible_m"] = lg["end_m"]
        write_record_line(os.path.join(run_dir, "host.tsv"),
                          render_host_row(time.time_ns(), state["cpu"], state["mem"], len(running), "end %d" % i))
        ending[i] = lg

    def write_leg_profile(lg):
        rec = derive_leg_profile(lg, ctx["ticks"], ctx)
        lg["record"] = rec
        write_atomic(os.path.join(run_dir, "%d.leg" % lg["i"]), (render_leg_row(rec) + "\n").encode("utf-8"))
        write_leg_record(run_dir, rec)
        write_record_line(os.path.join(run_dir, "legs.tsv"), render_legs_row(rec))
        tail = ["%.1fs" % rec["wall_s"], "%s process(es)" % rec["procs_total"]]
        if rec["ts_wait_s"]:
            tail.append("ts_wait_s %.1f" % rec["ts_wait_s"])
        if rec["ts_holders"]:
            tail.append("ts_holders %d" % rec["ts_holders"])
        if rec["stalls"]:
            tail.append("%d stall episode(s)" % len(rec["stalls"]))
        if rec["launch_error"]:
            tail.append(rec["launch_error"])
        print("measure-legs: %-4s  %s  (%s)" % (rec["verdict"], rec["name"], ", ".join(tail)), flush=True)

    box, worker = {}, None
    raw_kept = envelope["raw_kept"]
    try:
        first = scan_census_tick(pm, bash, leg_env, fns["measure_spawn_cost"], ts_dir)
        envelope["census_backend"] = first.get("backend")
        derive_tick_readings(first, legs, ctx)
        next_census = time.monotonic() + opts.census_every
        next_tick = state["eligible_m"] = time.monotonic()
        while pending or running or ending or worker is not None:
            now = time.monotonic()
            if now >= next_tick:
                cpu, mem, state["prev"] = read_host_load(api, state["prev"])
                state["cpu"], state["mem"], state["sample_m"] = cpu, mem, now
                for lg in running.values():
                    try:
                        acct = read_job_accounting(api, lg["job"])
                        lg["active_peak"] = max(lg["active_peak"], acct["active"])
                    except OSError:
                        pass
                    lg["host"].append((cpu, mem))
                events, n_before = [], len(running)
                if opts.mode == "concurrent" and pending and running \
                        and check_admit(cpu, mem, len(running), state["sample_m"] > state["admit_m"]):
                    run_admission(events)
                write_record_line(os.path.join(run_dir, "host.tsv"),
                                  render_host_row(time.time_ns(), cpu, mem, n_before, ",".join(events)))
                next_tick += HOST_EVERY_S
                if next_tick <= now:
                    next_tick = now + HOST_EVERY_S
            if pending and not running:
                events = []
                run_admission(events)
                write_record_line(os.path.join(run_dir, "host.tsv"),
                                  render_host_row(time.time_ns(), state["cpu"], state["mem"], 0, ",".join(events)))
            if worker is not None and not worker.is_alive():
                worker = None
                derive_tick_readings(box.pop("tick"), legs, ctx)
            if worker is None and (pending or running) and now >= next_census:
                worker = threading.Thread(target=run_census_worker, daemon=True,
                                          args=(box, pm, bash, leg_env, fns["measure_spawn_cost"], ts_dir))
                worker.start()
                state["worker_m0"] = time.monotonic()
                next_census = state["worker_m0"] + opts.census_every
            for i in sorted(ending):
                if worker is None or state["worker_m0"] > ending[i]["end_m"]:
                    write_leg_profile(ending.pop(i))
            wake = next_tick
            if worker is None and (pending or running):
                wake = min(wake, next_census)
            timeout = max(0.0, wake - time.monotonic())
            if running:
                scan_root_exits(api, [lg["hq"] for lg in running.values()], timeout)
            elif worker is not None:
                worker.join(min(timeout, HOST_EVERY_S))
            elif not pending and not ending:
                break
            for i in sorted(running):
                ex = read_root_exit(api, running[i]["hq"])
                if ex is not None:
                    write_leg_end(i, *ex)
    except KeyboardInterrupt:
        for lg in running.values():
            raw_kept.append({"leg": lg["name"], "path": lg["capture"], "reason": "interrupted"})
        for i in sorted(ending):
            write_leg_profile(ending.pop(i))
        envelope["exit"] = 130
        envelope["failed_legs"] = [lg["name"] for lg in legs if lg.get("record") and lg["record"]["verdict"] != "ok"]
        write_envelope(run_dir, envelope)
        print("measure-legs: INTERRUPTED — %d leg(s) left running, their captures kept; record %s"
              % (len(running), run_dir), file=sys.stderr, flush=True)
        return 130

    # ---- run end: each job re-read, each kept capture retried, each profile rewritten
    for lg in legs:
        rec = lg["record"]
        if lg["job"] is not None:  # a leg whose launch failed (S35) holds no job and no handle
            try:
                rec["job_final"] = read_job_accounting(api, lg["job"])
            except OSError as exc:
                rec["job_final"] = {"unread": str(exc)}
        if lg.get("raw_pending"):
            why = write_leg_capture(lg, final=True)
            rec["log_bytes"] = lg.get("log_bytes")
            if why:
                raw_kept.append({"leg": lg["name"], "path": lg["capture"], "reason": why})
        write_leg_record(run_dir, rec)
        if lg["hq"]:
            api.CloseHandle(lg["hq"])
    recs = [lg["record"] for lg in legs]
    width = 1 if opts.mode == "serial" else max(1, state["peak"])
    durs = [r["wall_s"] for r in recs]
    envelope.update({
        "width": width, "width_source": "--serial" if opts.mode == "serial" else "peak concurrency",
        "wall": round((state["last_end_m"] or 0) - (state["first_admit_m"] or 0), 3),
        "exit": 1 if WRITE_FAILURES else 0,
        "failed_legs": [r["name"] for r in recs if r["verdict"] != "ok"],
        "regime": profile_bar.derive_regime(durs, width),
        "regimes": derive_regimes(durs, os.cpu_count() or 1, opts.mode),
        "write_failures": list(WRITE_FAILURES),
    })
    write_envelope(run_dir, envelope)
    est = sum(r["spawn_s_est"] or 0.0 for r in recs)
    leg_wall = sum(durs)
    print("measure-legs: %d leg(s), %d ok, %d fail · run wall %.1fs · spawn est %.1fs of %.1fs leg time (%.0f%%)"
          " · %d substitution(s) · scratch %d B · record %s" % (
              len(recs), sum(1 for r in recs if r["verdict"] == "ok"), len(envelope["failed_legs"]),
              envelope["wall"], est, leg_wall, 100.0 * est / leg_wall if leg_wall else 0.0,
              len(envelope["substitutions"]), measure_scratch_bytes(scratch), run_dir), flush=True)
    for k in raw_kept:
        print("measure-legs: raw capture KEPT — %s: %s (%s)" % (k["leg"], k["path"], k["reason"]), flush=True)
    if WRITE_FAILURES:
        print("measure-legs: %d record write(s) FAILED: %s" % (len(WRITE_FAILURES), "; ".join(WRITE_FAILURES)),
              file=sys.stderr, flush=True)
        return 1
    return 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    try:
        opts = parse_flags(argv)
    except ProfileRefused as exc:
        print("measure-legs: REFUSED — %s" % exc, file=sys.stderr, flush=True)
        return 2
    if opts.mode == "selftest":
        return cmd_selftest()
    return run_profile(opts)


# ================================================================== the selftest
#
# Every arm runs the tool IN-PROCESS over the fixture manifests beside it, at --census-every 1
# --stall-window 8 --stall-cpu 0.5, writing to a temp --out. Each prints one line, and the run ends
# `PASS (<n> assertions)` or `FAIL (<n> assertions)`. Every fixture ends by itself.
#
# THE ALIAS HALVES — AC1 and AC2's resolution red half, and AC16's alias half — need a host whose
# PYBIN is an App Execution Alias. Anywhere else each prints `unexercised: no alias on this host` and
# adds no assertion, so a PASS there says nothing about an alias. The interpreter verification of S14
# and the path arm of AC17 run on every host.

ARM_PASSED, ARM_FAILED = [], []
SELFTEST_FLAGS = ["--census-every", "1", "--stall-window", "8", "--stall-cpu", "0.5"]


def check_arm(name, ok, detail=""):
    (ARM_PASSED if ok else ARM_FAILED).append(name)
    print("  %s %s%s" % ("ok  " if ok else "FAIL", name, "" if ok else "  (%s)" % detail), flush=True)


@contextlib.contextmanager
def set_environ(values):
    """`values` set in this process's environment for the block, the previous state restored after."""
    saved = {k: os.environ.get(k) for k in values}
    os.environ.update(values)
    try:
        yield
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def run_fixture(tmp, manifest, mode="--serial"):
    """One in-process profile over a fixture manifest: (exit, captured stdout, run dir, records)."""
    out_root = tempfile.mkdtemp(prefix="out.", dir=tmp)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = main([mode, "--legs", os.path.join(FIXTURES, manifest), "--out", out_root] + SELFTEST_FLAGS)
    sys.stdout.write(buf.getvalue())
    runs = os.listdir(out_root)
    run_dir = os.path.join(out_root, runs[0]) if len(runs) == 1 else ""
    recs = {}
    if run_dir:
        for f in os.listdir(run_dir):
            if f.endswith(".json") and f[:-5].isdigit():
                with open(os.path.join(run_dir, f), encoding="utf-8") as fh:
                    rec = json.load(fh)
                recs[rec["name"]] = rec
    return rc, buf.getvalue(), run_dir, recs


def read_envelope(run_dir):
    with open(os.path.join(run_dir, "envelope.json"), encoding="utf-8") as fh:
        return json.load(fh)


def remove_scratch(run_dir):
    """The selftest's own scratch dirs go once read; the tool itself never sweeps one."""
    try:
        shutil.rmtree(read_envelope(run_dir)["scratch"], ignore_errors=True)
    except (OSError, ValueError, KeyError):
        pass


def build_holder_env(env):
    """<env> scrubbed as a leg's environment is, then `GATE_REGEN_CHECK=0`, as `queued.sh` sets it
    (S12): the selftest's holder is a bar, and without it that bar runs the regen preflight first."""
    top = profile_bar.run_git(["rev-parse", "--show-toplevel"])
    gone = {n for n, _r in derive_scrub_set(list(env), read_local_env_vars(top), read_hook_unsets(top))}
    out = {k: v for k, v in env.items() if k not in gone}
    out["GATE_REGEN_CHECK"] = "0"
    return out


def read_hold_beacon(key, holder, bound_s):
    """The `pid` file of any slot beacon under the turnstile key <key>, polled every 0.2 s, once one
    exists. None when the process <holder> exits first or <bound_s> seconds pass: the beacon is the
    holder's only proof of holding, and a holder that never takes the slot must end the arm, not
    stall it (S12)."""
    deadline = time.monotonic() + bound_s
    while True:
        try:
            names = sorted(os.listdir(key))
        except OSError:
            names = []
        for slot in names:
            if slot == "gate-bar-beacon" or slot.startswith("gate-bar-beacon."):
                pid = os.path.join(key, slot, "pid")
                if os.path.exists(pid):
                    return pid
        if holder.poll() is not None or time.monotonic() >= deadline:
            return None
        time.sleep(0.2)


def render_holder_failure(holder_out):
    """The turnstile arm's failure line when no beacon appeared, with the holder's captured output."""
    try:
        with open(holder_out, "rb") as fh:
            said = fh.read().decode("utf-8", "replace").strip()
    except OSError as exc:
        said = "its output is unreadable: %s" % exc
    return "the holder's slot beacon never appeared; the holder printed: %s" % (said[-600:] or "nothing")


def resolve_msys_dir(path):
    """<path> as the resolved bash spells it (`cygpath -u`), forward-slashed as written when that fails."""
    bash, _tried = profile_bar.resolve_bash(RUNNER)
    rc, out, _err = run_bash(bash, 'cygpath -u -- "$1"', [path]) if bash else (1, "", "")
    out = out.strip()
    return out if rc == 0 and out.startswith("/") else path.replace("\\", "/")


def write_temp_manifest(tmp, name, rows):
    """A leg manifest of <rows> at <tmp>/<name>, for an arm that profiles legs no fixture manifest holds."""
    path = os.path.join(tmp, name)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(rows, fh)
    return path


def read_pybin_alias():
    """(PYBIN, its `cygpath -m` spelling or "", whether that file is an App Execution Alias) on this
    host, PYBIN being what the runner's `resolve_python` prints under the legs' scrubbed environment.

    The witness the alias halves switch on. It reads the reparse tag ITSELF rather than through
    `check_app_alias`, the function those halves grade, so a detector that misses the alias cannot
    also switch its own arm off.
    """
    top = profile_bar.run_git(["rev-parse", "--show-toplevel"])
    scrub = derive_scrub_set(list(os.environ), read_local_env_vars(top), read_hook_unsets(top))
    env = {k: v for k, v in os.environ.items() if k not in {n for n, _r in scrub}}
    bash, _tried = profile_bar.resolve_bash(RUNNER)
    pybin = resolve_leg_python(bash, env, extract_runner_function(read_runner_text(), "resolve_python"))
    found = read_tool_versions(bash, env, pybin, [pybin], top)["launchers"].get(pybin) or {}
    path = found.get("path") or ""
    try:
        tag = getattr(os.lstat(path), "st_reparse_tag", 0)
    except (OSError, ValueError):
        tag = 0
    return pybin, path, tag != 0 and tag == getattr(stat, "IO_REPARSE_TAG_APPEXECLINK", None)


def test_platform_refusal(_tmp):
    """AC12: a platform without the job API refuses, naming it. Red when it returns a backend."""
    try:
        resolve_job_backend("linux")
        check_arm("test_platform_refusal", False, "linux returned a backend")
    except ProfileRefused as exc:
        check_arm("test_platform_refusal", "linux" in str(exc) and "Job Object" in str(exc), str(exc))


def test_check_admit(_tmp):
    """AC5: hold, admit, hold, hold, admit. Red when the drained clause is missing."""
    got = [check_admit(81, 50, 1, True), check_admit(80, 90, 1, True), check_admit(50, 91, 1, True),
           check_admit(50, 50, 1, False), check_admit(99, 99, 0, False)]
    check_arm("test_check_admit", got == [False, True, False, False, True], repr(got))


def test_scrub_derivation(_tmp):
    """The scrub: every GATE_ name, the git list, the hook line; PATH and GIT_EXEC_PATH stay."""
    got = derive_scrub_set(["GATE_JOBS", "GATE_TURNSTILE_HOLDER", "GIT_DIR", "GIT_NAMESPACE", "PATH",
                            "GIT_EXEC_PATH"], ["GIT_DIR"], ["GIT_DIR", "GIT_NAMESPACE"])
    want = [("GATE_JOBS", "GATE_ prefix"), ("GATE_TURNSTILE_HOLDER", "GATE_ prefix"),
            ("GIT_DIR", "git rev-parse --local-env-vars"), ("GIT_NAMESPACE", "pre-push unset line")]
    check_arm("test_scrub_derivation", got == want, repr(got))


def test_extract_refuses(_tmp):
    """AC2's refusal: a runner function the runner lacks refuses, rather than measuring nothing."""
    try:
        extract_runner_function(read_runner_text(), "no_such_runner_function")
        check_arm("test_extract_refuses", False, "a missing function was extracted")
    except ProfileRefused:
        check_arm("test_extract_refuses", True)


def test_app_alias(tmp):
    """AC16's probe half: `check_app_alias` reads False for this interpreter and for a path that does
    not exist and, on a host whose PYBIN is an alias, True for PYBIN's file. Red when it tests
    `os.path.islink`, which reads False for an alias (measured on node d, 2026-10-15)."""
    missing = os.path.join(tmp, "no-such-launcher.exe")
    got = (check_app_alias(sys.executable), check_app_alias(missing))
    check_arm("AC16 check_app_alias reads False off an alias", got == (False, False), repr(got))
    pybin, path, alias = read_pybin_alias()
    if not alias:
        print("  unexercised: no alias on this host (AC16's alias half; PYBIN %s is %s)"
              % (pybin, path or "unresolved"), flush=True)
        return
    check_arm("AC16 check_app_alias reads True for the alias", check_app_alias(path) is True, path)


FOREIGN_SNAPSHOT = (
    "     UID     PID    PPID  TTY        STIME COMMAND\n"
    "    user       1       0 ?        10:00:00 /usr/bin/bash --login\n"
    "    user    @ME@       1 ?        10:00:01 /usr/bin/bash -c bash lib9/runner.sh\n"
    "    user     100    @ME@ ?        10:00:02 python3 probe/one/selftest.py\n"
    "    user     200       1 ?        10:00:03 bash lib9/runner.sh\n"
    "    user     201     200 ?        10:00:04 bash suite/x.test.sh\n"
    "    user     300       1 ?        10:00:05 python3 probe/two/selftest.py\n")


def build_snapshot_rows(snapshot):
    """Census-shaped rows from a `ps -ef` snapshot: one parent each, equal ages, so the census graph
    is exactly the snapshot's."""
    rows = []
    for line in snapshot.split("\n")[1:]:
        parts = line.split(None, 5)
        if len(parts) == 6 and parts[1].isdigit() and parts[2].isdigit():
            rows.append({"winpid": int(parts[1]), "win_ppid": int(parts[2]), "msys_pid": None,
                         "msys_ppid": None, "kind": "native", "age_s": 0.0, "cpu_s": 0.0,
                         "command": parts[5], "backend": "fixture"})
    return rows


def test_foreign_parity(tmp):
    """AC8: the runner's own `measure_foreign`, `ps` shimmed to print one six-row snapshot, against
    the port over the same rows: the same count and the same roots. Red when the port drops the
    `selftest.py` word rule."""
    pm = load_process_monitor()
    snap = os.path.join(tmp, "snapshot.txt")
    toks = os.path.join(tmp, "tokens.txt")
    with open(snap, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(FOREIGN_SNAPSHOT)
    with open(toks, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("lib9/runner.sh\n")
    fn = extract_runner_function(read_runner_text(), "measure_foreign")
    script = ('SNAPFILE=$1; CENSUS_TOKENS=$2\n'
              'ps() { while IFS= read -r l; do printf "%s\\n" "${l//@ME@/$$}"; done < "$SNAPFILE"; }\n'
              + fn + '\nprintf "%s\\n" "$$"\nmeasure_foreign\n')
    bash, _tried = profile_bar.resolve_bash(RUNNER)
    rc, out, err = run_bash(bash, script, [snap.replace("\\", "/"), toks.replace("\\", "/")])
    lines = out.split("\n")
    if rc != 0 or len(lines) < 2 or not lines[0].strip().isdigit():
        check_arm("test_foreign_parity", False, "the runner's measure_foreign did not run: %s" % err[-300:])
        return
    me = int(lines[0])
    fields = lines[1].split("\t")
    awk_count = fields[1] if len(fields) > 1 else "?"
    awk_roots = sorted(fields[2].split()) if len(fields) > 2 else []
    rows = build_snapshot_rows(FOREIGN_SNAPSHOT.replace("@ME@", str(me)))
    own = set(pm.scope.build_self_chain(rows, me)) | set(pm.reap.build_walk(rows, me))
    count, roots = measure_foreign(rows, ["lib9/runner.sh"], own)
    port_roots = sorted("%d:%s" % rt for rt in roots)
    check_arm("test_foreign_parity", (str(count), port_roots) == (awk_count, awk_roots) and count == 2,
              "awk %s %s, port %d %s" % (awk_count, awk_roots, count, port_roots))


def test_serial_run(tmp):
    """AC1 AC2 AC9 AC10 AC11 AC16 AC17, over one --serial run of serial.json's six legs with four knobs
    exported, and TOOL-dRedressedBar-19's AC39 over its printenv log. S14's interpreter verification
    is read on every host; AC1 and AC16's alias halves only where PYBIN is an alias, and
    `substitutions` must read [] anywhere else."""
    pybin_alias = read_pybin_alias()
    knobs = {"GATE_JOBS": "3", "GATE_REUSE": "1", "GATE_TURNSTILE_HOLDER": "probe", "GIT_NAMESPACE": "probe"}
    with set_environ(knobs):
        rc, out, run_dir, recs = run_fixture(tmp, "serial.json")
        top = profile_bar.run_git(["rev-parse", "--show-toplevel"])
        scrub = derive_scrub_set(list(os.environ), read_local_env_vars(top), read_hook_unsets(top))
        env = {k: v for k, v in os.environ.items() if k not in {n for n, _r in scrub}}
        bash, _tried = profile_bar.resolve_bash(RUNNER)
        want_py = resolve_leg_python(bash, env, extract_runner_function(read_runner_text(), "resolve_python"))
    if rc != 0 or not run_dir or len(recs) != 6:
        check_arm("test_serial_run", False, "exit %s, run dir %r, %d record(s)" % (rc, run_dir, len(recs)))
        return
    env_rec = read_envelope(run_dir)
    six, none, memio, penv = recs["spawn six"], recs["spawn none"], recs["memio"], recs["printenv"]
    kids = [p for p in six["procs"] if "-I -c" in (p.get("command") or "")]
    check_arm("AC1 spawn count", six["procs_total"] - none["procs_total"] == 6,
              "%s - %s" % (six["procs_total"], none["procs_total"]))
    check_arm("AC1 per-process rows", len(kids) == 6 and all(
        p.get(k) is not None for p in kids for k in ("ppid", "start", "first_seen", "last_seen", "cpu_s",
                                                    "peak_mem_b")), repr(kids)[:300])
    mib = 200 * 1024 * 1024
    check_arm("AC2 memio", memio["peak_job_mem_b"] >= mib and memio["io"]["write_bytes"] >= mib
              and memio["user_s"] + memio["kernel_s"] > 0, repr((memio["peak_job_mem_b"], memio["io"])))
    check_arm("AC2 spawn cost", all(
        r["spawn_us"] and r["spawn_us"]["median"] > 0
        and abs(r["spawn_s_est"] - r["procs_total"] * r["spawn_us"]["median"] / 1e6) < 1e-5
        for r in recs.values()), repr([(r["name"], r["spawn_us"], r["spawn_s_est"]) for r in recs.values()]))
    with open(os.path.join(run_dir, "%d.log" % penv["i"]), "rb") as fh:
        log_bytes = fh.read()
    log = log_bytes.decode("utf-8", "replace")
    check_arm("AC39 the log keeps every byte but the two credentials",
              b"\xe7" in log_bytes and b"\r" in log_bytes and log_bytes.count(b"://***:***@") == 2
              and b"s3cret" not in log_bytes, repr(log_bytes[-160:]))
    names = set(log.split())
    git_names = set(read_local_env_vars(top) or ())
    scrubbed = {s["name"]: s["rule"] for s in env_rec["scrubbed"]}
    check_arm("AC9 nothing scrubbed reaches the leg",
              not any(n.startswith("GATE_") for n in names) and not (names & git_names)
              and "GIT_NAMESPACE" not in names, sorted(n for n in names if n.startswith(("GATE_", "GIT_"))))
    check_arm("AC9 the scrubbed set is recorded with its rules",
              all(k in scrubbed for k in knobs) and scrubbed.get("GIT_NAMESPACE") == "pre-push unset line",
              repr(scrubbed))
    check_arm("AC9 PYBIN is the runner's", env_rec["pybin"] == want_py, "%r vs %r" % (env_rec["pybin"], want_py))
    listing = set(os.listdir(run_dir))
    want = {"envelope.json", "host.tsv", "census.tsv", "legs.tsv"} | {
        "%d.%s" % (i, ext) for i in range(6) for ext in ("leg", "log", "json")}
    rows_ok = True
    for i in range(6):
        with open(os.path.join(run_dir, "%d.leg" % i), encoding="utf-8") as fh:
            f = fh.read().rstrip("\n").split("\t")
        rows_ok = rows_ok and len(f) == 8 and re.fullmatch(r"[0-9]+\.[0-9]{3}", f[3]) is not None
    check_arm("AC10 every record is on disk", want <= listing and rows_ok and os.path.isdir(env_rec["scratch"]),
              repr(sorted(want - listing)))
    leaked = []
    for base in (run_dir, os.path.join(env_rec["scratch"], "raw")):
        for d, _dirs, files in os.walk(base):
            for f in files:
                with open(os.path.join(d, f), "rb") as fh:
                    if b"s3cret" in fh.read():
                        leaked.append(f)
    check_arm("AC11 the log is redacted and the raw capture gone",
              "://***:***@" in log and not leaked and not os.listdir(os.path.join(env_rec["scratch"], "raw"))
              and env_rec["raw_kept"] == [], repr((leaked, env_rec["raw_kept"])))
    probe = env_rec.get("interpreter_probe") or {}
    check_arm("S14 the legs' interpreter keeps its child in a job",
              all(isinstance(probe.get(k), int) for k in ("with_child", "without_child"))
              and probe["with_child"] - probe["without_child"] == 1, repr(probe))
    drive = re.compile(r"^[A-Za-z]:/")
    spelled = {k: env_rec.get(k) or "" for k in ("scratch", "turnstile_dir", "scratch_posix", "turnstile_dir_posix")}
    check_arm("AC17 the scratch dir and the turnstile key are opened as converted",
              drive.match(spelled["scratch"]) is not None and drive.match(spelled["turnstile_dir"]) is not None
              and os.path.isdir(spelled["scratch"]) and spelled["scratch_posix"].startswith("/")
              and spelled["turnstile_dir_posix"].startswith("/"), repr(spelled))
    pybin, alias_path, alias = pybin_alias
    subs = env_rec.get("substitutions")
    if not alias:
        check_arm("AC16 nothing is substituted where PYBIN is no alias", subs == [], repr(subs))
        print("  unexercised: no alias on this host (AC1 and AC16's alias halves; PYBIN %s)" % pybin, flush=True)
    else:
        sub = subs[0] if isinstance(subs, list) and len(subs) == 1 else {}
        resolved = sub.get("resolved") or ""
        check_arm("AC1 both spawn legs ran the interpreter the alias starts",
                  bool(resolved) and six["argv"][0] == none["argv"][0] == resolved,
                  repr((subs, six["argv"][0], none["argv"][0])))
        check_arm("AC16 the substitution is printed and recorded",
                  sub.get("launcher") == pybin and sub.get("alias") == alias_path and os.path.isfile(resolved)
                  and check_app_alias(resolved) is False and {"argv0", "GOV_PYTHON"} <= set(sub.get("applied") or ())
                  and re.search(r"^measure-legs: SUBSTITUTED %s " % re.escape(pybin), out, re.M) is not None
                  and "GOV_PYTHON" in names, repr((subs, "GOV_PYTHON" in names)))
    remove_scratch(run_dir)


def test_resolution_disabled(tmp):
    """AC1 and AC2's resolution red half, on a host whose PYBIN is an alias. `resolve_launcher_aliases`
    is rebound to resolve nothing and verify nothing, so both spawn legs run the alias: their process
    totals differ by 0, and the memio leg reads under 200 MiB with nothing written, as the first build
    read it on node d, 2026-10-15. Elsewhere it prints `unexercised` and asserts nothing."""
    pybin, _path, alias = read_pybin_alias()
    if not alias:
        print("  unexercised: no alias on this host (AC1 and AC2's resolution red half; PYBIN %s)" % pybin,
              flush=True)
        return
    real = globals()["resolve_launcher_aliases"]
    globals()["resolve_launcher_aliases"] = lambda *_a, **_k: ([], None)
    try:
        rc, _out, run_dir, recs = run_fixture(tmp, "serial.json")
    finally:
        globals()["resolve_launcher_aliases"] = real
    if rc != 0 or not run_dir or len(recs) != 6:
        check_arm("test_resolution_disabled", False, "exit %s, run dir %r, %d record(s)" % (rc, run_dir, len(recs)))
        return
    six, none, memio = recs["spawn six"], recs["spawn none"], recs["memio"]
    check_arm("AC1 red half: unresolved, the spawn difference reads 0",
              six["procs_total"] - none["procs_total"] == 0, "%s - %s" % (six["procs_total"], none["procs_total"]))
    check_arm("AC2 red half: unresolved, memio's work is outside its job",
              memio["peak_job_mem_b"] < 200 * 1024 * 1024 and memio["io"]["write_bytes"] == 0,
              repr((memio["peak_job_mem_b"], memio["io"])))
    remove_scratch(run_dir)


def test_concurrent_run(tmp):
    """AC4: no admission on a sample above 80% while a leg runs, and at least one sample above 80%
    between the hog's admission and the steady leg's. Red when the caps are disabled. The liveness
    half fails, never passes, on a host where the hog cannot raise CPU above 80%."""
    rc, _out, run_dir, _recs = run_fixture(tmp, "concurrent.json", mode="--concurrent")
    if rc != 0 or not run_dir:
        check_arm("test_concurrent_run", False, "exit %s" % rc)
        return
    with open(os.path.join(run_dir, "host.tsv"), encoding="utf-8") as fh:
        rows = [ln.split("\t") for ln in fh.read().split("\n")[1:] if ln]
    bad = [r for r in rows if r[4].startswith("admit") and int(r[3]) > 0 and r[1] != "-" and float(r[1]) > CPU_CAP_PCT]
    admits = [k for k, r in enumerate(rows) if "admit" in r[4]]
    hot = len(admits) == 2 and any(r[1] != "-" and float(r[1]) > CPU_CAP_PCT for r in rows[admits[0]:admits[1]])
    check_arm("AC4 no admission over the cap", not bad, repr(bad))
    check_arm("AC4 the cap was exercised", hot, "no sample above %d%% between the two admissions" % CPU_CAP_PCT)
    remove_scratch(run_dir)


def test_stall_run(tmp):
    """AC6 AC7: the FIFO-blocked leg reads STALLED with `sleep` in its tree, the steady leg does not,
    and the churning leg holds no episode with at least one window the job veto decided."""
    rc, out, run_dir, recs = run_fixture(tmp, "stall.json")
    if rc != 0 or len(recs) != 3:
        check_arm("test_stall_run", False, "exit %s, %d record(s)" % (rc, len(recs)))
        return
    stall, steady, churn = recs["stall"], recs["steady"], recs["churn"]
    # TOOL-dRedressedBar-19 S42: read line by line, so a STALLED line naming a sibling reds here.
    lines = [ln for ln in out.split("\n") if ln.startswith("measure-legs: STALLED  ")]
    check_arm("AC6 the blocked leg reads STALLED",
              len(stall["stalls"]) == 1 and any("sleep" in (p.get("command") or "") for p in stall["stalls"][0]["tree"])
              and len(lines) == 1 and lines[0].startswith("measure-legs: STALLED  stall  ")
              and not any(ln.startswith("measure-legs: STALLED  %s  " % n) for ln in lines for n in ("steady", "churn")),
              repr((lines, stall["stalls"]))[:300])
    check_arm("AC6 the steady leg does not", not steady["stalls"] and all(r["rc"] == 0 for r in recs.values()),
              repr((steady["stalls"], [r["rc"] for r in recs.values()])))
    vetoed = [w for w in churn["stall_windows"] if w["tree_delta"] is not None and w["tree_delta"] < 0.5
              and w["job_delta"] is not None and w["job_delta"] > 0.5]
    if not any(w["tree_delta"] is not None and w["tree_delta"] < 0.5 for w in churn["stall_windows"]):
        check_arm("AC7 the job veto", False, "veto UNEXERCISED: no churn window read a tree delta under 0.5s")
    else:
        check_arm("AC7 the job veto", not churn["stalls"] and bool(vetoed), repr(churn["stall_windows"])[:300])
    remove_scratch(run_dir)


def test_turnstile_run(tmp):
    """AC15: a real hold outside any leg counts as a foreign holder; a leg's own queued bar waits, and
    its wait is kept apart from its work; `read_runs` sets both readings aside and admits the zeroed
    third. Red when `derive_leg_turnstile` ignores tickets: the wait then reads 0."""
    home = tempfile.mkdtemp(prefix="home.", dir=tmp)
    top = profile_bar.run_git(["rev-parse", "--show-toplevel"])
    bash, _tried = profile_bar.resolve_bash(RUNNER)
    with set_environ({"HOME": home}):
        env = build_holder_env(dict(os.environ))
        holder_out = os.path.join(tmp, "holder.out")
        log = open(holder_out, "wb")
        holder = subprocess.Popen([bash, RUNNER, "--hold", "--", "sleep", "20"], cwd=top, env=env,
                                  stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT)
        log.close()
        if read_hold_beacon(os.path.join(home, ".gov", "gate-turnstile"), holder, HOLD_BEACON_WAIT_S) is None:
            check_arm("test_turnstile_run", False, render_holder_failure(holder_out))
            try:
                holder.wait(timeout=60)
            except subprocess.TimeoutExpired:
                pass
            return
        rc, _out, run_dir, recs = run_fixture(tmp, "turnstile.json")
    holder.wait()
    if rc != 0 or len(recs) != 2:
        check_arm("test_turnstile_run", False, "exit %s, %d record(s)" % (rc, len(recs)))
        return
    steady, queued = recs["steady"], recs["queued"]
    ts_dir = read_envelope(run_dir).get("turnstile_dir") or ""
    check_arm("AC17 the existing turnstile key opens as converted", os.path.isdir(ts_dir), repr(ts_dir))
    print("  (turnstile arm: queued.sh waited %.1fs)" % queued["ts_wait_s"])
    check_arm("AC15 a foreign holder", steady["ts_holders"] == 1 and steady["ts_queued"] == 0,
              repr((steady["ts_holders"], steady["ts_queued"])))
    check_arm("AC15 the leg's own bar waited", queued["ts_queued"] == 1 and queued["ts_wait_s"] >= 5
              and abs(queued["work_s"] - (queued["wall_s"] - queued["ts_wait_s"])) < 1e-6,
              repr((queued["ts_queued"], queued["ts_wait_s"], queued["work_s"], queued["wall_s"])))
    rows = []
    for rec in (steady, queued):
        with open(os.path.join(run_dir, "%d.leg" % rec["i"]), encoding="utf-8") as fh:
            rows.append(fh.read().rstrip("\n"))
    zeroed = dict(steady, foreign=0, ts_holders=0, ts_queued=0)
    rows.append(render_leg_row(zeroed))
    eighth = [r.split("\t")[7] for r in rows[:2]]
    gd = tempfile.mkdtemp(prefix="gd.", dir=tmp)
    for k, row in enumerate(rows):
        os.makedirs(os.path.join(gd, "gate-run", "r%d" % k))
        with open(os.path.join(gd, "gate-run", "r%d" % k, "0.leg"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(row + "\n")
    import importlib.util
    import pathlib
    spec = importlib.util.spec_from_file_location("derive_ceilings", os.path.join(KITDIR, "derive-ceilings.py"))
    dc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(dc)
    per, aside = dc.read_runs(pathlib.Path(gd), {}, ())
    check_arm("AC15 read_runs sets the contended readings aside",
              all(e.isdigit() and int(e) > 0 for e in eighth)
              and aside.get("steady", {}).get("contended") == 1 and aside.get("queued", {}).get("contended") == 1
              and per.get("steady") == [steady["wall_s"]], repr((eighth, per, aside)))
    remove_scratch(run_dir)


# ---- TOOL-dRedressedBar-19's arms

def test_turnstile_key(tmp):
    """AC11 and AC36. A key whose `cygpath -m` conversion fails resolves to ("", ""), which
    `read_turnstile` refuses; under this process's PATH it converts to a drive-letter spelling. A
    beacon with no `pid` file, one whose `pid` is no number and a ticket with no pid field are not
    judged, and a queue that cannot be listed is the one refused read. Red when the conversion keeps
    its bash-spelling fallback, or when a pid-less beacon reads as refused."""
    bash, _tried = profile_bar.resolve_bash(RUNNER)
    got = resolve_turnstile_dir(bash, dict(os.environ, PATH="/nonexistent"))
    try:
        read_turnstile(got[1])
        refused = False
    except OSError:
        refused = True
    check_arm("AC11 a key that does not convert is a refused read, never an empty one",
              got == ("", "") and refused, repr(got))
    own = resolve_turnstile_dir(bash, dict(os.environ))
    check_arm("AC11 ...and under this PATH the key converts to a drive-letter spelling",
              DRIVE_SPELLING.match(own[1]) is not None, repr(own))
    key = tempfile.mkdtemp(prefix="key.", dir=tmp)
    os.makedirs(os.path.join(key, "gate-bar-beacon"))
    os.makedirs(os.path.join(key, "gate-bar-beacon.1"))
    os.makedirs(os.path.join(key, "gate-bar-queue"))
    with open(os.path.join(key, "gate-bar-beacon.1", "pid"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("x\n")
    with open(os.path.join(key, "gate-bar-queue", "20261015T000000-nopid-x"), "w", encoding="utf-8") as fh:
        fh.write("")
    try:
        ts = read_turnstile(key)
    except OSError as exc:
        ts = "refused: %s" % exc
    check_arm("AC36 a half-written beacon and a pid-less ticket are not judged",
              ts == {"holders": [], "tickets": []}, repr(ts))
    # LIVENESS: the same reader over a key holding one whole beacon and one whole ticket lists both,
    # so the empty reading above is the per-entry rule and not a reader that reads nothing.
    live = tempfile.mkdtemp(prefix="key.", dir=tmp)
    os.makedirs(os.path.join(live, "gate-bar-beacon.2"))
    os.makedirs(os.path.join(live, "gate-bar-queue"))
    with open(os.path.join(live, "gate-bar-beacon.2", "pid"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("4242\n")
    with open(os.path.join(live, "gate-bar-queue", "20261015T000000-4243-x"), "w", encoding="utf-8") as fh:
        fh.write("")
    try:
        ts = read_turnstile(live)
    except OSError as exc:
        ts = "refused: %s" % exc
    check_arm("AC36 LIVENESS a whole beacon and a whole ticket are read",
              isinstance(ts, dict) and ts["holders"] == [("gate-bar-beacon.2", 4242)]
              and [t[:2] for t in ts["tickets"]] == [("20261015T000000-4243-x", 4243)], repr(ts))
    bad = tempfile.mkdtemp(prefix="key.", dir=tmp)
    with open(os.path.join(bad, "gate-bar-queue"), "w", encoding="utf-8") as fh:
        fh.write("")
    try:
        read_turnstile(bad)
        refused = False
    except OSError:
        refused = True
    check_arm("AC36 a queue that cannot be listed is a refused read", refused)


def test_hold_beacon(tmp):
    """AC12. The holder's environment is the legs' scrub with `GATE_REGEN_CHECK=0` set after it, and
    the beacon wait ends on its bound with the holder still running, and at once on the holder's
    exit, whose output the failure line carries. Red when `build_holder_env` sets nothing."""
    env = build_holder_env({"GATE_REGEN_CHECK": "1", "GATE_JOBS": "3"})
    check_arm("AC12 the holder runs under GATE_REGEN_CHECK=0, every other GATE_ name scrubbed",
              env.get("GATE_REGEN_CHECK") == "0" and "GATE_JOBS" not in env, repr(env))
    key = tempfile.mkdtemp(prefix="key.", dir=tmp)
    waiter = subprocess.Popen([sys.executable, "-I", "-c", "import sys; sys.stdin.read()"],
                              stdin=subprocess.PIPE, stdout=subprocess.DEVNULL)
    try:
        t0 = time.monotonic()
        got = read_hold_beacon(key, waiter, 2)
        took, alive = time.monotonic() - t0, waiter.poll() is None
    finally:
        waiter.stdin.close()
        waiter.wait(timeout=60)
    check_arm("AC12 the wait ends on its bound, the holder still running",
              got is None and took < 4 and alive, repr((got, round(took, 2), alive)))
    said = os.path.join(tmp, "said.out")
    with open(said, "wb") as fh:
        quitter = subprocess.Popen([sys.executable, "-I", "-c", "print('holder-said')"],
                                   stdout=fh, stderr=subprocess.STDOUT)
    quitter.wait(timeout=60)
    t0 = time.monotonic()
    got = read_hold_beacon(key, quitter, HOLD_BEACON_WAIT_S)
    took = time.monotonic() - t0
    line = render_holder_failure(said)
    check_arm("AC12 ...and at once on the holder's exit, its output in the failure line",
              got is None and took < 1 and "holder-said" in line, repr((got, round(took, 2), line)))


# S20's eight shapes, LF only: the runner's `sed` drops the CR of a CRLF under MSYS, so no shape holds one.
REDACT_SHAPES = (b"plain https://u:p@h/x\n"
                 b"two https://u:p@h/x and https://a:b@c/y\n"
                 b"ssh git+ssh://git:tok@host/repo\n"
                 b"colon https://u:p:q@h/x\n"
                 b"no colon https://user@h/x\n"
                 b"slash https://u/v:p@h/x\n"
                 b"tab https://u\tv:p@h/x\n"
                 b"byte caf\xe7 https://u:p@h/\xe7\n")


def test_redact_parity(_tmp):
    """AC20: the runner's own `redact`, run from its source in the resolved bash over S20's eight
    shapes on stdin, against `derive_redacted` over the same bytes, byte for byte. Red when the port
    drops `\\s` from its classes: the tab shape then differs. A liveness half requires the runner to
    have masked something, so a `redact` that printed nothing cannot pass."""
    bash, _tried = profile_bar.resolve_bash(RUNNER)
    fn = extract_runner_function(read_runner_text(), "redact")
    try:
        done = subprocess.run([bash, "-c", fn + "\nredact\n"], input=REDACT_SHAPES, capture_output=True,
                              timeout=60)
        got = done.stdout
    except (OSError, subprocess.SubprocessError) as exc:
        got = ("not run: %r" % exc).encode("utf-8")
    port = derive_redacted(REDACT_SHAPES)
    check_arm("AC20 the port masks every shape as the runner's redact does",
              got == port and got.count(b"://***:***@") >= 5, repr((got, port))[:600])


def test_no_bare_bash_argv(tmp):
    """AC34. An `ast` scan of this file finds no subprocess call whose argv opens with the literal
    'bash', so every bash this tool starts is the one `resolve_bash` found; and an empty resolve
    refuses with exit 2 before any leg, naming each candidate. Red when one call spells `["bash", …]`."""
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    calls, bare = 0, []
    for n in ast.walk(tree):
        f = n.func if isinstance(n, ast.Call) else None
        if not (isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id == "subprocess"
                and n.args):
            continue
        calls += 1
        a0 = n.args[0]
        while isinstance(a0, ast.BinOp):
            a0 = a0.left
        if isinstance(a0, (ast.List, ast.Tuple)) and a0.elts and isinstance(a0.elts[0], ast.Constant) \
                and a0.elts[0].value == "bash":
            bare.append(n.lineno)
    check_arm("AC34 no subprocess argv opens with a bare 'bash'", calls >= 3 and not bare,
              "%d subprocess call(s) read, bare at %s" % (calls, bare))
    out = tempfile.mkdtemp(prefix="out.", dir=tmp)
    real = profile_bar.resolve_bash
    profile_bar.resolve_bash = lambda *_a, **_k: ("", ["cand-a", "cand-b"])
    err = io.StringIO()
    try:
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(io.StringIO()):
            rc = main(["--serial", "--legs", os.path.join(FIXTURES, "serial.json"), "--out", out])
    finally:
        profile_bar.resolve_bash = real
    check_arm("AC34 an empty bash resolve refuses before any leg, naming every candidate",
              rc == 2 and not os.listdir(out) and "cand-a" in err.getvalue() and "cand-b" in err.getvalue(),
              repr((rc, os.listdir(out), err.getvalue()[-300:])))


def test_fork_count(tmp):
    """AC32: serial.json's `forks.sh 5` against its zero-count twin, alone. Each subshell and each
    command substitution is at least one process, so the job totals differ by at least 10. Red when
    the job lets a child break away: the difference then reads 0."""
    with open(os.path.join(FIXTURES, "serial.json"), encoding="utf-8") as fh:
        rows = [r for r in json.load(fh) if any(a.endswith("/forks.sh") for a in r["argv"])]
    rc, _out, run_dir, recs = run_fixture(tmp, write_temp_manifest(tmp, "forks.json", rows))
    five, none = recs.get("forks five") or {}, recs.get("forks none") or {}
    diff = (five.get("procs_total") or 0) - (none.get("procs_total") or 0)
    check_arm("AC32 the forked processes are counted", rc == 0 and len(rows) == 2 and diff >= 10,
              "exit %s, %d row(s), %s - %s" % (rc, len(rows), five.get("procs_total"), none.get("procs_total")))
    if run_dir:
        remove_scratch(run_dir)


# AC37's eight malformed manifests: (class, text, whether the refusal names a row).
MANIFEST_CLASSES = (
    ("unparseable JSON", '[{"name": ', False),
    ("a top-level object", '{"name": "a", "argv": ["true"]}', False),
    ("a non-object row", '[1]', True),
    ("an empty list", '[]', False),
    ("a duplicate name", '[{"name": "a", "argv": ["true"]}, {"name": "a", "argv": ["true"]}]', True),
    ("an argv holding a number", '[{"name": "a", "argv": ["true", 1]}]', True),
    ("a name holding a tab", '[{"name": "a\\tb", "argv": ["true"]}]', True),
    ("an unresolved token", '[{"name": "a", "argv": ["{nope}/x"]}]', True),
)


def test_manifest_refusals(tmp):
    """AC37: each malformed manifest class exits 2 before any leg with one `measure-legs: REFUSED — `
    line on stderr and no traceback, and each row class's line names the row. Red when a class is let
    through: the tab-named leg then runs."""
    bad = []
    for k, (what, text, row) in enumerate(MANIFEST_CLASSES):
        path = os.path.join(tmp, "malformed-%d.json" % k)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        out = tempfile.mkdtemp(prefix="out.", dir=tmp)
        err, std = io.StringIO(), io.StringIO()
        try:
            with contextlib.redirect_stderr(err), contextlib.redirect_stdout(std):
                rc = main(["--serial", "--legs", path, "--out", out])
        except Exception as exc:  # a crash is the failure this arm exists for, named, never raised
            rc = "raised %r" % exc
        lines = [ln for ln in err.getvalue().split("\n") if ln.startswith("measure-legs: REFUSED — ")]
        if rc != 2 or len(lines) != 1 or "Traceback" in err.getvalue() + std.getvalue() or os.listdir(out) \
                or (row and "row " not in lines[0]):
            bad.append((what, rc, lines))
    check_arm("AC37 every malformed manifest class refuses with exit 2, by row where it is one",
              not bad, repr(bad)[:600])


def test_launch_failure(tmp):
    """AC35. `build_job` hands the leg, after the interpreter probe's two real jobs, a job handle
    already closed, so the assign fails: the run returns 0, the leg reads `fail` with rc 1 and a
    `launch_error` naming the call, and no process carrying the leg's argv is left. Red when the
    terminate is taken out: the suspended root is then still in the census."""
    marker = "launch-probe-%d-%d" % (os.getpid(), time.time_ns())
    manifest = write_temp_manifest(tmp, "launch.json", [
        {"name": "launch", "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/spawn.py", "0", "1",
                                    marker]}])
    real, made = globals()["build_job"], []

    def build_closed_job(api):
        job = real(api)
        made.append(job)
        if len(made) > 2:
            api.CloseHandle(job)
        return job

    globals()["build_job"] = build_closed_job
    t0 = time.monotonic()
    try:
        rc, _out, run_dir, recs = run_fixture(tmp, manifest)
    finally:
        globals()["build_job"] = real
    took = time.monotonic() - t0
    rec = recs.get("launch") or {}
    check_arm("AC35 a failed launch is a failed leg, and the run goes on",
              rc == 0 and took < 60 and rec.get("verdict") == "fail" and rec.get("rc") == 1
              and str(rec.get("launch_error") or "").startswith("launch: AssignProcessToJobObject"),
              repr((rc, round(took, 1), rec.get("verdict"), rec.get("rc"), rec.get("launch_error"))))
    try:
        rows = load_process_monitor().census.scan_processes()[0]
        left = [r["winpid"] for r in rows if marker in (r.get("command") or "")]
        # LIVENESS: the census reads command lines at all, so `left` empty is the root gone and not
        # a census that sees no argv. This process's own row must carry its own command line.
        if not any(r["winpid"] == os.getpid() and r.get("command") for r in rows):
            left.append("the census read no command line for this process, so it cannot show the root gone")
    except Exception as exc:  # a census that cannot answer cannot show the root gone
        left = ["census refused: %s" % exc]
    check_arm("AC35 ...and its suspended root is terminated", not left, repr(left))
    if run_dir:
        remove_scratch(run_dir)


def test_scratch_sweep(tmp):
    """AC38, under a TMPDIR of this arm's own. Two sibling scratch dirs: a dead owner's, an exited child
    named with its own creation time and a record dir that exists, whose raw capture carries a
    credential; and a live one's, this process. The run redacts the dead capture into that record
    dir, deletes it and names it in `raw_recovered`, and leaves the live capture alone. Red when the
    owner test reads the pid alone: the exited child, its handle still held, then reads live."""
    api = resolve_job_backend()
    sweep = tempfile.mkdtemp(prefix="sweep.", dir=tmp)
    out = tempfile.mkdtemp(prefix="out.", dir=tmp)
    record = os.path.join(out, "dead-record")
    os.makedirs(record)
    child = subprocess.Popen([sys.executable, "-I", "-c", "import sys; sys.stdin.read()"], stdin=subprocess.PIPE)
    _state, child_created = read_process_created(api, child.pid)
    child.stdin.close()
    child.wait(timeout=60)
    _state, own_created = read_process_created(api, os.getpid())
    planted = {}
    for name, pid, created, raw in (("dead", child.pid, child_created, b"https://u:s3cret@example.invalid/\n"),
                                    ("live", os.getpid(), own_created, b"live-bytes")):
        d = os.path.join(sweep, "gate-profile.%s0000" % name)
        os.makedirs(os.path.join(d, "raw"))
        with open(os.path.join(d, "owner.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"pid": pid, "created": created, "record": record.replace("\\", "/")}, fh)
        planted[name] = os.path.join(d, "raw", "0.out")
        with open(planted[name], "wb") as fh:
            fh.write(raw)
    manifest = write_temp_manifest(tmp, "sweep.json", [
        {"name": "sweep", "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/spawn.py", "0", "1"]}])
    buf = io.StringIO()
    with set_environ({"TMPDIR": resolve_msys_dir(sweep)}), contextlib.redirect_stdout(buf):
        rc = main(["--serial", "--legs", manifest, "--out", out] + SELFTEST_FLAGS)
    sys.stdout.write(buf.getvalue())
    runs = [os.path.join(out, r) for r in os.listdir(out) if r != "dead-record"]
    recovered = (read_envelope(runs[0]).get("raw_recovered") if len(runs) == 1 else None) or []
    leaked = []
    for base in (out, os.path.dirname(os.path.dirname(planted["dead"]))):
        for d, _dirs, files in os.walk(base):
            for f in files:
                with open(os.path.join(d, f), "rb") as fh:
                    if b"s3cret" in fh.read():
                        leaked.append(f)
    try:
        with open(os.path.join(record, "0.log.recovered"), "rb") as fh:
            masked = b"://***:***@" in fh.read()
    except OSError:
        masked = False
    try:
        with open(planted["live"], "rb") as fh:
            live = fh.read()
    except OSError as exc:
        live = repr(exc).encode("utf-8")
    named = [os.path.normcase(os.path.normpath(str(k.get("raw")))) for k in recovered]
    check_arm("AC38 a dead run's raw capture is redacted, recorded and deleted",
              rc == 0 and child_created is not None and not os.path.exists(planted["dead"]) and masked
              and not leaked and named == [os.path.normcase(os.path.normpath(planted["dead"]))],
              repr((rc, child_created, os.path.exists(planted["dead"]), masked, leaked, recovered))[:600])
    check_arm("AC38 ...and a live run's is left alone", live == b"live-bytes", repr(live[:80]))
    if len(runs) == 1:
        remove_scratch(runs[0])


def test_fixtures_withheld(_tmp):
    """AC29: the run-gates descriptor's `project-owned` list names every file under the fixture
    directory, and only those, read off the filesystem and never off the list, and no `project-owned`
    element carries a glob, which a list include drops. Red when one fixture name is taken out of the
    list, or the list is respelled as one `fixtures/measure-legs/**` element."""
    import tomllib
    with open(os.path.join(KITDIR, "kit.toml"), "rb") as fh:
        desc = tomllib.load(fh)
    owned = [e for rule in desc.get("files", []) if rule.get("role") == "project-owned"
             and isinstance(rule.get("include"), list) for e in rule["include"]]
    listed = {e for e in owned if str(e).startswith("fixtures/measure-legs/")}
    on_disk = set()
    for base, dirs, files in os.walk(FIXTURES):
        dirs[:] = [d for d in dirs if d != "__pycache__"]  # bytecode is never tracked, so never shipped
        on_disk.update(os.path.relpath(os.path.join(base, f), KITDIR).replace("\\", "/") for f in files)
    check_arm("AC29 the fixture population is non-empty, so the comparison below can fail",
              bool(on_disk), FIXTURES)
    check_arm("AC29 every fixture, and only fixtures, is named project-owned",
              listed == on_disk, repr(sorted(listed ^ on_disk)))
    check_arm("AC29 no project-owned element carries a glob, which a list include would drop",
              not any(c in str(e) for e in owned for c in "*?["), repr(sorted(map(str, owned))))


def cmd_selftest():
    del ARM_PASSED[:], ARM_FAILED[:]
    tmp = tempfile.mkdtemp(prefix="measure-legs-selftest.")
    print("measure-legs selftest: arms", flush=True)
    try:
        # S38: every profile this selftest starts makes its scratch dir, and sweeps that dir's
        # siblings, under the selftest's own temp dir, never the operator's real TMPDIR. Spelled as
        # the resolved bash spells it, so `scratch_posix` still reads as the legs see it.
        with set_environ({"TMPDIR": resolve_msys_dir(tmp)}):
            for arm in (test_platform_refusal, test_check_admit, test_scrub_derivation, test_extract_refuses,
                        test_app_alias, test_foreign_parity, test_serial_run, test_resolution_disabled,
                        test_concurrent_run, test_stall_run, test_turnstile_run, test_turnstile_key,
                        test_hold_beacon, test_redact_parity, test_no_bare_bash_argv, test_fork_count,
                        test_manifest_refusals, test_launch_failure, test_scratch_sweep,
                        test_fixtures_withheld):
                try:
                    arm(tmp)
                except Exception as exc:  # an arm that raised is a failed arm, named, never a crash
                    check_arm(arm.__name__, False, "raised %r" % exc)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    n = len(ARM_PASSED) + len(ARM_FAILED)
    print("%s (%d assertions)" % ("FAIL" if ARM_FAILED else "PASS", n), flush=True)
    return 1 if ARM_FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
