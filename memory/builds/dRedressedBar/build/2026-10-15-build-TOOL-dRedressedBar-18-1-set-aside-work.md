# Unit 18's set-aside work — dRedressedBar, the profiler as built before its divergence

**Serves:** journal TOOL-dRedressedBar-18

The builder of run wf_2e958a62-4b6 built this, then removed it from the tree when AC1 and AC2 failed on node d, and returned DIVERGENCE. It is kept here verbatim for the redispatch, which restores it rather than rewriting it. The builder's divergence, as returned:

~~~~text
DIVERGENCE: spec 18's Job Object mechanism (S3; §4 candidates row 1 and "Measured on node d"; §5 risks; AC1, AC2) fails its own test on node d, and §5 rules on that case: "a breakaway there parks the unit rather than shipping a census-only count". The cause is one the spec did not consider. The runner's resolve_python resolves PYBIN to `python3`, which on node d is a Microsoft Store App Execution Alias (C:\Users\d41ly\AppData\Local\Microsoft\WindowsApps\python3.exe, starting pythoncore-3.14-64). Everything started through that alias leaves a job created with no limit flags. Evidence: on serial.json every leg read procs_total 1 (the bash root only), so spawn six minus spawn none = 0, not 6 (AC1 fails), and memio read peak_job_mem_b 6950912 with write_bytes 0 against at least 200 MiB (AC2 fails). In a scratch manifest, a bash leg running only sleeps counted 7 (bash-forked processes DO stay in, so the escape §4 feared does not happen), a plain Python312 python.exe running spawn.py 2 1 counted 4, and the `python3` and `py` aliases counted 1 each. With no bash in the path, a plain python.exe kept its child in the job (2) while the alias kept only its stub (1). The spec has to choose how an alias launcher is handled, which is a design fork, not a build choice: (a) a preflight that runs PYBIN and each distinct launcher once in a test job and refuses with exit 2 naming the alias, remedy GOV_PYTHON set to a non-alias interpreter, which the runner honours too so the bar and the profile still run one python; (b) resolving the alias to its real interpreter for the legs, which drops the alias's own extra process from every reading so they are no longer the bar's; or (c) a per-leg escape check, the census tree compared against job membership, that marks the job totals unknown. AC1 and AC2 must also name the python they run under. Every path I changed is restored; the work is saved in the scratchpad's unit18-wip/ for the redispatch.

TOOL-dRedressedBar-18 was not committed. Spec 18's Job Object mechanism failed AC1 on node d, and spec §5 says that case parks the unit (see why).

Built, then removed: tools/run-gates/measure_legs.py (the full profiler and its --selftest), 12 fixtures under tools/run-gates/fixtures/measure-legs/, and the process-monitor changes (census.py CIM query and parse_cim carrying peak_mem_b and mem_b, selftest.py's CIM fixtures moved to seven fields, the row-contract arm admitting the two keys, the AC3 arm test_cim_memory_fields_are_bytes, and every 0.18 marker moved to 0.19). The process-monitor files were restored with git checkout. measure_legs.py, the fixtures dir and the __pycache__ dirs my compile created were deleted. The tree matches HEAD 26beaa6fe apart from the dispatcher's pre-existing INPROGRESS header on spec 18, which I did not touch. The planner will keep naming this unit until that header is reset or the spec is revised.

Saved for the redispatch: C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/unit18-wip/ (measure_legs.py, fixtures/measure-legs/ with 12 files, process-monitor.diff of 255 lines). Never written: the gate-legs.json row, kit.toml, selftest-budgets.txt, windows-only-legs.txt, the runner version bump, the two READMEs, the help page, the map claim.

Checks that ran. Each is a probe of this unit's code, and the merge bar did not run.
- Pure probe, standing in for the process-monitor census selftest and the measure-legs selftest arms. AC3: peak_mem_b 307200, mem_b 409600, command intact, POSIX rows None, FIELDS unchanged; the red staging, reading index 4, gives '300'. AC5: [False, True, False, False, True]. AC12: refused, naming 'linux' and the Job Object API. The scrub derivation and the extraction refusal also held.
- AC8 parity probe: the runner's own measure_foreign with ps shimmed and the port both gave 2 roots, {200:lib9/runner.sh, 300:probe/two/selftest.py}. The port without the selftest.py rule gives 1.
- CLI run over serial.json with the AC9 knobs set. AC9: GATE_JOBS, GATE_REUSE and GATE_TURNSTILE_HOLDER scrubbed by the GATE_ prefix and GIT_NAMESPACE by the pre-push unset line, none in the leg's log. AC10: every record on disk, each .leg row 8 fields. AC11: the log carries ://***:***@, no s3cret in the run dir or raw/, raw/ empty, raw_kept empty. AC1 and AC2 FAILED, which is the divergence.
- escape.json probe and a direct alias-in-job probe, which isolated the cause.
- CIM unit probe: PeakWorkingSetSize is KiB (78232 beside Get-Process 76533760 bytes); WorkingSetSize is already bytes.
- The naming lexicon (--suggest) answered OK for every added name.

Skipped or owed:
- AC4, AC6, AC7: the concurrent and stall runs were skipped once AC1 failed.
- AC13, AC14: the declarations were never written.
- AC15 and the RED-first observation of both New arm lines run the real runner, so they are owed at the close.
- gotchas.py --for-diff was not run, because there is no commit.

For the spec writer:
1. Unit 19's S11 path conversion is needed in unit 18 already. Native Python cannot open bash's /tmp/... scratch path; the saved code uses cygpath -m for the scratch dir and the turnstile key.
2. The pre-commit kickoff-manifest ratchet refuses a commit that stages tools/gate-legs.json or run-gates.sh unless it carries a last-audit re-stamp of memory/guides/SESSION-KICKOFF.md, as unit 17's commit did. Unit 18's Files touched should list that file, while unit 19 S1 keeps the reviewed second commit.
3. test_row_contract_is_complete compares exact key sets, so it goes red when census rows gain keys unless it changes in the same commit.
~~~~

## Files

### measure_legs.py

~~~~text
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

WHAT IT DOES NOT CHECK, said here because a profile reads as a verdict to everybody who did not
write it. It grades no leg: `ok` and `fail` are the leg's exit status, recorded. It sees no work
done for a leg by another process, a WMI host answering a query or a scanner opening an image, and
no bar on another turnstile key. A leg sleeping, or waiting in the host queue, longer than the stall
window reads STALLED, and the record names the waiting tickets so a queue wait reads as one. It
runs on Windows only and refuses anywhere else. It never signals a process: a leg that never ends
keeps the run open, by the owner's design.

NO KNOB. Every setting is a flag. Every `GATE_*` name, every name `git rev-parse --local-env-vars`
prints and every name the push hook's `unset GIT_…` line names is scrubbed from each leg's
environment. The set is DERIVED at run time and printed, and the values are never recorded.

EXIT 0 every leg ended and every record was written, whatever the legs' verdicts · 1 a record write
failed, named on stderr · 2 a refusal before the first leg · 130 an interrupt, which writes the
envelope, names each running leg's kept capture, and leaves the legs running.
"""
import argparse
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
# The runner functions this tool runs from the runner's own source text. A name the runner lacks is
# a refusal before the first leg, never a profile that quietly records no spawn cost (AC2).
RUNNER_FUNCTIONS = ("resolve_python", "measure_spawn_cost", "read_spawn_floor")
EPOCH_AS_FILETIME = 116444736000000000   # 1970-01-01 in 100 ns ticks since 1601

# ---- the Windows API surface. Values from the Windows SDK headers.
CREATE_SUSPENDED = 0x00000004
PROCESS_TERMINATE = 0x0001        # AssignProcessToJobObject requires it; nothing here terminates
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

WRITE_FAILURES = []               # every record write that failed this run; exit 1 names them


class ProfileRefused(RuntimeError):
    """A precondition the profile cannot run without. Exit 2, before the first leg."""


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
    if rc != 0 or len(lines) < 2 or not os.path.isdir(lines[1]):
        raise ProfileRefused("the legs' scratch dir could not be made in %s (exit %d): %s"
                             % (bash, rc, (err or out).strip()[-400:]))
    return lines[0], lines[1]


TURNSTILE_SCRIPT = r'''d=${GATE_TURNSTILE_DIR:-$HOME/.gov/gate-turnstile}
if [ -d "$d" ]; then d=$(cd "$d" 2>/dev/null && pwd) || exit 3; fi
printf '%s\n' "$d"
cygpath -m "$d" 2>/dev/null || printf '%s\n' "$d"
'''


def resolve_turnstile_dir(bash, env):
    """The host turnstile key the legs' bars resolve, by the runner's own expression in the resolved
    bash under the legs' environment: (bash spelling, the spelling this process opens). Resolved
    once. Nothing is created: an absent key reads as an empty one. ("", "") when it did not resolve,
    which every tick then reads as a refused read."""
    rc, out, _err = run_bash(bash, TURNSTILE_SCRIPT, env=env)
    lines = [ln for ln in out.split("\n") if ln]
    if rc != 0 or len(lines) < 2:
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


TOOLS_SCRIPT = r'''for w in "$@"; do printf 'launcher\t%s\t%s\n' "$w" "$(command -v -- "$w" 2>/dev/null)"; done
'''


def read_tool_versions(bash, env, pybin, launchers, top):
    """The tools a leg's verdict can depend on: each launcher's resolved path in the legs' bash,
    `bash --version`'s first line, PYBIN and its version, `git version`, and the two eol settings."""
    _rc, out, _err = run_bash(bash, TOOLS_SCRIPT, list(launchers), env=env, cwd=top)
    resolved = {}
    for line in out.split("\n"):
        parts = line.split("\t")
        if len(parts) == 3 and parts[0] == "launcher":
            resolved[parts[1]] = parts[2] or None
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

def read_legs(path):
    """The manifest's rows, every one of them. Refuses an empty list, a row with no name or no argv
    list, and a duplicate name: a profile of a malformed manifest is a profile of nothing in particular."""
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError) as exc:
        raise ProfileRefused("cannot read the leg manifest %s: %s" % (path, exc))
    if not isinstance(data, list) or not data:
        raise ProfileRefused("the leg manifest %s holds no leg, so there is nothing to profile" % path)
    seen = set()
    for k, row in enumerate(data):
        name = row.get("name") if isinstance(row, dict) else None
        if not isinstance(name, str) or not name:
            raise ProfileRefused("row %d of %s carries no name" % (k, path))
        argv = row.get("argv")
        if not isinstance(argv, list) or not argv or not all(isinstance(a, str) for a in argv):
            raise ProfileRefused("leg '%s' in %s carries no argv list" % (name, path))
        if name in seen:
            raise ProfileRefused("leg '%s' appears twice in %s" % (name, path))
        seen.add(name)
    return data


def derive_leg_argv(row, troot, pybin):
    """The argv the runner would run: `{prefix}` resolved, a first word `python`/`python3` -> PYBIN."""
    argv = [resolve_prefix_token(a, troot) for a in row["argv"]]
    if argv[0] in ("python", "python3"):
        argv[0] = pybin
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

    def owner(pid):
        w = by_msys.get(pid)
        return None if w is None else owner_of.get(w, "foreign")

    return {"holders": [(pid, owner(pid)) for _slot, pid in ts["holders"]],
            "tickets": [(name, owner(pid)) for name, pid, _stamp in ts["tickets"]]}


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
    """
    job = build_job(api)
    with open(capture, "wb") as fh:
        proc = subprocess.Popen([bash, "-c", 'exec "$@"', "measure-legs"] + list(argv), cwd=cwd, env=env,
                                stdin=subprocess.DEVNULL, stdout=fh, stderr=subprocess.STDOUT,
                                creationflags=CREATE_SUSPENDED)
    hq = api.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION | SYNCHRONIZE, False, proc.pid)
    ha = api.OpenProcess(PROCESS_SET_QUOTA | PROCESS_TERMINATE, False, proc.pid)
    try:
        if not hq or not ha or not api.AssignProcessToJobObject(job, ha):
            raise OSError(ctypes.get_last_error(), "the leg's root %d could not join its job" % proc.pid)
    finally:
        if ha:
            api.CloseHandle(ha)
    resumed = 0
    snap = api.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, 0)
    if snap and snap != ctypes.c_void_p(-1).value:
        te = ThreadEntry()
        te.dwSize = ctypes.sizeof(te)
        ok = api.Thread32First(snap, ctypes.byref(te))
        while ok:
            if te.th32OwnerProcessID == proc.pid:
                ht = api.OpenThread(THREAD_SUSPEND_RESUME, False, te.th32ThreadID)
                if ht:
                    if api.ResumeThread(ht) != RESUME_FAILED:
                        resumed += 1
                    api.CloseHandle(ht)
            ok = api.Thread32Next(snap, ctypes.byref(te))
        api.CloseHandle(snap)
    if not resumed:
        raise OSError(ctypes.get_last_error(), "the leg's root %d could not be resumed" % proc.pid)
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
        rows = read_legs(legs_path)
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
        scratch_posix, scratch = build_scratch(bash, base_env)
        leg_env = dict(base_env)
        leg_env["TMPDIR"] = scratch_posix + "/tmp"
        run_id = time.strftime("%Y%m%dT%H%M%SZ", time.gmtime()) + "-" + str(os.getpid())
        out_root = os.path.abspath(opts.out) if opts.out else os.path.join(gitdir, "gate-profile")
        run_dir = os.path.join(out_root, run_id)
        try:
            os.makedirs(run_dir, mode=0o700)
        except OSError as exc:
            raise ProfileRefused("the record dir %s could not be made: %s" % (run_dir, exc))
    except ProfileRefused as exc:
        print("measure-legs: REFUSED — %s" % exc, file=sys.stderr, flush=True)
        return 2

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
        "tools": read_tool_versions(bash, leg_env, pybin, sorted({a[0] for a in argvs}), top),
        "pybin": pybin, "scratch": scratch, "scratch_bash": scratch_posix,
        "turnstile_dir": ts_dir, "turnstile_dir_bash": ts_posix, "raw_kept": [],
        "manifest": {"path": legs_path, "blob": profile_bar.run_git(["hash-object", legs_path], cwd=top) or None},
        "legs": len(rows), "census_backend": None, "spawn_floor_us": floor_us,
        "spawn_floor_state": floor_state, "kit_version": read_kit_version(runner_text),
        "process_monitor": pm.dir, "regimes": None,
    }
    write_envelope(run_dir, envelope)
    print("measure-legs: run %s · %s · %d leg(s) from %s" % (run_id, opts.mode, len(rows), legs_path), flush=True)
    print("measure-legs: record %s" % run_dir, flush=True)
    print("measure-legs: scrubbed %s" % (", ".join("%s (%s)" % s for s in scrubbed) or "none"), flush=True)
    if not git_names:
        print("measure-legs: NOTE - git rev-parse --local-env-vars refused, so that half of the scrub is UNARMED",
              flush=True)
    print("measure-legs: turnstile key %s (read, never written)" % (ts_dir or "UNRESOLVED, every read refused"),
          flush=True)
    print("measure-legs: scratch %s (every leg's TMPDIR is its tmp/; nothing sweeps it)" % scratch, flush=True)
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

    def admit(event_rows):
        i = pending.pop(0)
        lg = legs[i]
        now = time.monotonic()
        lg["queued_s"] = round(now - state["eligible_m"], 3)
        launched = run_leg(api, bash, lg["argv"], leg_env, top, lg["capture"])
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
        return i

    def end_leg(i, ended_ns, rc):
        lg = running.pop(i)
        lg["ended_ns"], lg["rc"], lg["end_m"] = ended_ns, rc, time.monotonic()
        try:
            lg["acct"] = read_job_accounting(api, lg["job"])
            lg["left_running"] = lg["acct"]["active"]
        except OSError:
            lg["acct"], lg["left_running"] = None, None
        if lg["episode"] is not None:
            lg["episode"]["closed"], lg["episode"]["how"] = round(ended_ns / 1e9, 3), "ended"
            lg["episode"] = None
        lg["raw_pending"] = write_leg_capture(lg, final=False)
        lg["proc"].poll()
        state["last_end_m"] = lg["end_m"]
        if opts.mode == "serial":
            state["eligible_m"] = lg["end_m"]
        write_record_line(os.path.join(run_dir, "host.tsv"),
                          render_host_row(time.time_ns(), state["cpu"], state["mem"], len(running), "end %d" % i))
        ending[i] = lg

    def finalize(lg):
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
                    admit(events)
                write_record_line(os.path.join(run_dir, "host.tsv"),
                                  render_host_row(time.time_ns(), cpu, mem, n_before, ",".join(events)))
                next_tick += HOST_EVERY_S
                if next_tick <= now:
                    next_tick = now + HOST_EVERY_S
            if pending and not running:
                events = []
                admit(events)
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
                    finalize(ending.pop(i))
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
                    end_leg(i, *ex)
    except KeyboardInterrupt:
        for lg in running.values():
            raw_kept.append({"leg": lg["name"], "path": lg["capture"], "reason": "interrupted"})
        for i in sorted(ending):
            finalize(ending.pop(i))
        envelope["exit"] = 130
        envelope["failed_legs"] = [lg["name"] for lg in legs if lg.get("record") and lg["record"]["verdict"] != "ok"]
        write_envelope(run_dir, envelope)
        print("measure-legs: INTERRUPTED — %d leg(s) left running, their captures kept; record %s"
              % (len(running), run_dir), file=sys.stderr, flush=True)
        return 130

    # ---- run end: each job re-read, each kept capture retried, each profile rewritten
    for lg in legs:
        rec = lg["record"]
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
          " · scratch %d B · record %s" % (
              len(recs), sum(1 for r in recs if r["verdict"] == "ok"), len(envelope["failed_legs"]),
              envelope["wall"], est, leg_wall, 100.0 * est / leg_wall if leg_wall else 0.0,
              measure_scratch_bytes(scratch), run_dir), flush=True)
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
    """AC1 AC2 AC9 AC10 AC11, over one --serial run of serial.json with four knobs exported."""
    knobs = {"GATE_JOBS": "3", "GATE_REUSE": "1", "GATE_TURNSTILE_HOLDER": "probe", "GIT_NAMESPACE": "probe"}
    with set_environ(knobs):
        rc, _out, run_dir, recs = run_fixture(tmp, "serial.json")
        top = profile_bar.run_git(["rev-parse", "--show-toplevel"])
        scrub = derive_scrub_set(list(os.environ), read_local_env_vars(top), read_hook_unsets(top))
        env = {k: v for k, v in os.environ.items() if k not in {n for n, _r in scrub}}
        bash, _tried = profile_bar.resolve_bash(RUNNER)
        want_py = resolve_leg_python(bash, env, extract_runner_function(read_runner_text(), "resolve_python"))
    if rc != 0 or not run_dir or len(recs) != 4:
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
        log = fh.read().decode("utf-8", "replace")
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
        "%d.%s" % (i, ext) for i in range(4) for ext in ("leg", "log", "json")}
    rows_ok = True
    for i in range(4):
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
    check_arm("AC6 the blocked leg reads STALLED",
              len(stall["stalls"]) == 1 and any("sleep" in (p.get("command") or "") for p in stall["stalls"][0]["tree"])
              and re.search(r"^measure-legs: STALLED  stall  ", out, re.M) is not None, repr(stall["stalls"])[:300])
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
        scrub = derive_scrub_set(list(os.environ), read_local_env_vars(top), read_hook_unsets(top))
        env = {k: v for k, v in os.environ.items() if k not in {n for n, _r in scrub}}
        log = open(os.path.join(tmp, "holder.out"), "wb")
        holder = subprocess.Popen([bash, RUNNER, "--hold", "--", "sleep", "20"], cwd=top, env=env,
                                  stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT)
        log.close()
        beacon = os.path.join(home, ".gov", "gate-turnstile", "gate-bar-beacon", "pid")
        deadline = time.monotonic() + 120
        while not os.path.exists(beacon) and holder.poll() is None and time.monotonic() < deadline:
            time.sleep(0.2)
        if not os.path.exists(beacon):
            check_arm("test_turnstile_run", False, "the holder's slot beacon never appeared")
            holder.wait()
            return
        rc, _out, run_dir, recs = run_fixture(tmp, "turnstile.json")
    holder.wait()
    if rc != 0 or len(recs) != 2:
        check_arm("test_turnstile_run", False, "exit %s, %d record(s)" % (rc, len(recs)))
        return
    steady, queued = recs["steady"], recs["queued"]
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


def cmd_selftest():
    del ARM_PASSED[:], ARM_FAILED[:]
    tmp = tempfile.mkdtemp(prefix="measure-legs-selftest.")
    print("measure-legs selftest: arms", flush=True)
    try:
        for arm in (test_platform_refusal, test_check_admit, test_scrub_derivation, test_extract_refuses,
                    test_foreign_parity, test_serial_run, test_concurrent_run, test_stall_run,
                    test_turnstile_run):
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
~~~~

### process-monitor.diff

~~~~text
diff --git a/tools/process-monitor/README.md b/tools/process-monitor/README.md
index 20fccc3c3..1b7dd8478 100644
--- a/tools/process-monitor/README.md
+++ b/tools/process-monitor/README.md
@@ -1,6 +1,6 @@
 # process-monitor — find, report and kill the processes an agent session forgot
 
-<!-- gov:kit process-monitor@0.18 -->
+<!-- gov:kit process-monitor@0.19 -->
 
 Every deadline a repo like this owns bounds a command a CHECKER launched. Nothing bounds a process
 an AGENT launched — a `Bash run_in_background` job, a `Monitor` pipeline, a suite invoked by hand —
diff --git a/tools/process-monitor/adopt-process-monitor.sh b/tools/process-monitor/adopt-process-monitor.sh
index f36f37a85..9b9c5d8e1 100644
--- a/tools/process-monitor/adopt-process-monitor.sh
+++ b/tools/process-monitor/adopt-process-monitor.sh
@@ -1,7 +1,7 @@
 #!/usr/bin/env bash
 # adopt-process-monitor.sh — wire the process-monitor kit into a project.
 #
-# gov:kit process-monitor@0.18
+# gov:kit process-monitor@0.19
 #
 # Run from anywhere INSIDE the target repo AFTER copying this kit dir in as `<prefix>/process-monitor/`.
 # The kit dir's NAME is load-bearing; the one-segment prefix is free and every path below is DERIVED
@@ -24,7 +24,7 @@
 #   Exit 0 = adopted / wired · 1 = unwired or refused · 2 = wrong invocation or not a repo.
 set -u
 
-KIT_PROCESS_MONITOR_VERSION="0.18"   # gov:kit process-monitor@0.18 — the deployer's read (kit.toml version_from)
+KIT_PROCESS_MONITOR_VERSION="0.19"   # gov:kit process-monitor@0.19 — the deployer's read (kit.toml version_from)
 
 # >>> resolve_python — canonical copy: resolve-python.sh in gov's lib dir (byte-identical; gated)
 resolve_python() {
diff --git a/tools/process-monitor/census.py b/tools/process-monitor/census.py
index b392b1ad0..36ef1e81b 100644
--- a/tools/process-monitor/census.py
+++ b/tools/process-monitor/census.py
@@ -1,7 +1,7 @@
 #!/usr/bin/env python3
 """census.py — one bounded read of the process table, or a refusal.
 
-gov:kit process-monitor@0.18
+gov:kit process-monitor@0.19
 
 Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-1.md
 
@@ -20,6 +20,15 @@ THE ROW CONTRACT, and every field is load-bearing:
     cpu_s      float|None  None means UNJOINED or unreported, NEVER zero
     command    str|None    the full command line. None for a process reporting none.
     backend    str         'windows-join' | 'posix-ps'
+    peak_mem_b int|None    the process's peak working set in BYTES (CIM PeakWorkingSetSize, which
+                           is KiB, times 1024). None when unreported, NEVER zero for unreported.
+    mem_b      int|None    its working set in BYTES (CIM WorkingSetSize). None as above.
+
+THE TWO MEMORY KEYS ARE NOT IN `FIELDS` (TOOL-dRedressedBar-18 S4). They are extra keys on every
+row, POSIX rows carrying None, so `render_rows` and every line the reap and classify verbs print keep
+their bytes. Their reader is the gate profiler beside the run-gates kit. The KiB unit was confirmed
+on node d, 2026-10-15, against one live row: CIM read 78232 beside Get-Process PeakWorkingSet64 of
+76533760 bytes taken a moment before, and WorkingSetSize read 79138816, already bytes.
 
 WHY TWO PARENT FIELDS. Measured on the machine this was built for: MSYS rows are 26 of 332, and the
 gate runner dispatches its legs as NATIVE processes. A descendant walk over MSYS edges alone
@@ -54,6 +63,7 @@ _CIM_QUERY = (
     "@($_.ProcessId, $_.ParentProcessId, "
     "(($_.KernelModeTime + $_.UserModeTime)/1e7), "
     "([int]((Get-Date) - $_.CreationDate).TotalSeconds), "
+    "$_.PeakWorkingSetSize, $_.WorkingSetSize, "
     "($_.CommandLine -replace '[\\r\\n]+',' ')) -join [char]1 }"
 )
 _CIM_SEP = ""
@@ -80,8 +90,18 @@ def run_bounded(argv, timeout=BACKEND_TIMEOUT_S):
     return (done.stdout or b"").decode("utf-8", "replace")
 
 
+def parse_cim_bytes(text, scale):
+    """One CIM memory field -> bytes, or None for a blank or non-integer field. Never a zero for absent."""
+    text = text.strip()
+    return int(text) * scale if text.isdigit() else None
+
+
 def parse_cim(text):
-    """CIM lines -> {winpid: (win_ppid, cpu_s, age_s, command)} plus the rejected-row count."""
+    """CIM lines -> {winpid: (win_ppid, cpu_s, age_s, peak_mem_b, mem_b, command)} plus the rejected-row count.
+
+    Seven fields a line: the four numbers, the two memory fields, then the command LAST, so free text
+    stays the final field.
+    """
     rows, rejected = {}, 0
     # THE PRODUCER'S TERMINATOR, not Python's. `str.splitlines()` also breaks on \v, \f, \x1c,
     # \x1d, \x1e, \x85, U+2028 and U+2029, while the CIM query strips only [\r\n]. A process whose
@@ -104,8 +124,10 @@ def parse_cim(text):
         except ValueError:
             rejected += 1
             continue
-        command = parts[4].strip() if len(parts) > 4 else ""
-        rows[int(parts[0])] = (int(parts[1]), cpu, age, command or None)
+        peak = parse_cim_bytes(parts[4], 1024) if len(parts) > 4 else None
+        mem = parse_cim_bytes(parts[5], 1) if len(parts) > 5 else None
+        command = parts[6].strip() if len(parts) > 6 else ""
+        rows[int(parts[0])] = (int(parts[1]), cpu, age, peak, mem, command or None)
     return rows, rejected
 
 
@@ -133,7 +155,7 @@ def parse_ps_w(text):
 def build_windows_rows(cim_rows, psw_rows):
     """Join the two reads into the row contract."""
     out = []
-    for winpid, (win_ppid, cpu, age, command) in cim_rows.items():
+    for winpid, (win_ppid, cpu, age, peak, mem, command) in cim_rows.items():
         overlay = psw_rows.get(winpid)
         msys_pid = msys_ppid = None
         kind = "native"
@@ -156,6 +178,8 @@ def build_windows_rows(cim_rows, psw_rows):
             "cpu_s": cpu,
             "command": command,
             "backend": "windows-join",
+            "peak_mem_b": peak,
+            "mem_b": mem,
         })
     return out
 
@@ -190,6 +214,8 @@ def parse_posix(text):
             "cpu_s": cpu,
             "command": (parts[4].strip() if len(parts) > 4 else "") or None,
             "backend": "posix-ps",
+            "peak_mem_b": None,
+            "mem_b": None,
         })
     return rows, rejected
 
diff --git a/tools/process-monitor/classify.py b/tools/process-monitor/classify.py
index 264954da3..ee6f1b2d9 100644
--- a/tools/process-monitor/classify.py
+++ b/tools/process-monitor/classify.py
@@ -1,7 +1,7 @@
 #!/usr/bin/env python3
 """classify.py — age DECIDES, the CPU rate LABELS.
 
-gov:kit process-monitor@0.18
+gov:kit process-monitor@0.19
 
 Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-3.md
 
diff --git a/tools/process-monitor/procmon-hook.js b/tools/process-monitor/procmon-hook.js
index 13195398a..f4aa5153b 100644
--- a/tools/process-monitor/procmon-hook.js
+++ b/tools/process-monitor/procmon-hook.js
@@ -2,7 +2,7 @@
 /**
  * procmon-hook — put the process monitor's verdict where a session actually reads it.
  *
- * gov:kit process-monitor@0.18
+ * gov:kit process-monitor@0.19
  *
  * Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-5.md
  *
diff --git a/tools/process-monitor/reap.py b/tools/process-monitor/reap.py
index be3beb728..8c640aebf 100644
--- a/tools/process-monitor/reap.py
+++ b/tools/process-monitor/reap.py
@@ -1,7 +1,7 @@
 #!/usr/bin/env python3
 """reap.py — kill a tree and PROVE each member died.
 
-gov:kit process-monitor@0.18
+gov:kit process-monitor@0.19
 
 Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-4.md
 
diff --git a/tools/process-monitor/scope.py b/tools/process-monitor/scope.py
index c501e4669..02aafc15e 100644
--- a/tools/process-monitor/scope.py
+++ b/tools/process-monitor/scope.py
@@ -1,7 +1,7 @@
 #!/usr/bin/env python3
 """scope.py — which census rows are OURS. The safety property the whole kit rests on.
 
-gov:kit process-monitor@0.18
+gov:kit process-monitor@0.19
 
 Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-2.md
 
diff --git a/tools/process-monitor/selftest.py b/tools/process-monitor/selftest.py
index 11fb8f4e7..d8313c4c1 100644
--- a/tools/process-monitor/selftest.py
+++ b/tools/process-monitor/selftest.py
@@ -1,7 +1,7 @@
 #!/usr/bin/env python3
 """selftest.py — the process-monitor engine's arms.
 
-gov:kit process-monitor@0.18
+gov:kit process-monitor@0.19
 
 Two kinds of arm and the split is deliberate. PARSING arms run over captured fixtures, so they grade
 column contracts without a live table. LIVENESS arms run over a live read, because a property like
@@ -68,10 +68,10 @@ def build_cim_fixture():
     """
     s = census._CIM_SEP
     return "\n".join([
-        s.join(["4242", "1000", "12.5", "3600", "C:/x/bash.exe -c sleep"]),
-        s.join(["4243", "4242", "0.0", "60", ""]),
+        s.join(["4242", "1000", "12.5", "3600", "2048", "1048576", "C:/x/bash.exe -c sleep"]),
+        s.join(["4243", "4242", "0.0", "60", "", "", ""]),
         "  && export TEMP='C:/tmp' && echo hi",          # continuation: no numeric head
-        s.join(["notanumber", "4242", "1.0", "10", "x"]),  # non-numeric id
+        s.join(["notanumber", "4242", "1.0", "10", "1", "1", "x"]),  # non-numeric id
     ])
 
 
@@ -105,8 +105,9 @@ def test_row_contract_is_complete():
     cim, _ = census.parse_cim(build_cim_fixture())
     psw, _ = census.parse_ps_w(build_ps_w_fixture())
     rows = census.build_windows_rows(cim, psw)
+    # FIELDS plus the two memory keys every row carries beside them (TOOL-dRedressedBar-18 S4).
     check("test_row_contract_is_complete",
-          all(sorted(r) == sorted(census.FIELDS) for r in rows) and
+          all(sorted(r) == sorted(census.FIELDS + ("peak_mem_b", "mem_b")) for r in rows) and
           all(r["winpid"] is not None for r in rows) and
           all(r["win_ppid"] is not None for r in rows),
           True)
@@ -205,11 +206,33 @@ def test_non_utf8_backend_output_survives():
     """
     raw = (b"4242" + census._CIM_SEP.encode() + b"1000" + census._CIM_SEP.encode()
            + b"1.0" + census._CIM_SEP.encode() + b"60" + census._CIM_SEP.encode()
+           + b"64" + census._CIM_SEP.encode() + b"65536" + census._CIM_SEP.encode()
            + b"caf\xe7 /x/y")
     cim, rejected = census.parse_cim(raw.decode("utf-8", "replace"))
     check("test_non_utf8_backend_output_survives", (len(cim), rejected), (1, 0))
 
 
+def test_cim_memory_fields_are_bytes():
+    """TOOL-dRedressedBar-18 AC3: the seven-field CIM line carries both memory keys as BYTES and the
+    command intact, a POSIX row carries both as None, and `FIELDS` keeps its bytes.
+
+    Red when `parse_cim` reads the command from index 4 as it did before the two fields: the command
+    then reads as the peak-memory number.
+    """
+    s = census._CIM_SEP
+    cim, rejected = census.parse_cim(
+        s.join(["5151", "1000", "2.0", "30", "300", "409600", "C:/x/python.exe -I -c pass"]))
+    row = census.build_windows_rows(cim, {})[0]
+    prow, _ = census.parse_posix("  PID  PPID ELAPSED     TIME COMMAND\n"
+                                 " 4242  1000    3600 00:00:12 /bin/bash -c sleep")
+    check("test_cim_memory_fields_are_bytes",
+          (rejected, row["peak_mem_b"], row["mem_b"], row["command"],
+           prow[0]["peak_mem_b"], prow[0]["mem_b"], census.FIELDS),
+          (0, 300 * 1024, 409600, "C:/x/python.exe -I -c pass", None, None,
+           ("winpid", "msys_pid", "win_ppid", "msys_ppid", "kind", "age_s", "cpu_s", "command",
+            "backend")))
+
+
 def test_summary_counts_are_derived():
     cim, rej = census.parse_cim(build_cim_fixture())
     psw, _ = census.parse_ps_w(build_ps_w_fixture())
~~~~

### fixtures/measure-legs/churn.py

~~~~text
"""churn.py <s> — a measure-legs fixture leg: silent, spawning `-c pass` children back to back for s seconds.

TOOL-dRedressedBar-18, AC7. Each child lives far shorter than one census scan, so the census walk of
this tree sees little CPU, while the job's exact accounting sees every child's. The job veto is what
keeps this leg from reading STALLED.
"""
import subprocess
import sys
import time

exe = getattr(sys, "_base_executable", None) or sys.executable
end = time.monotonic() + float(sys.argv[1])
while time.monotonic() < end:
    subprocess.run([exe, "-I", "-c", "pass"], check=False)
sys.exit(0)
~~~~

### fixtures/measure-legs/concurrent.json

~~~~text
[
  {
    "name": "hog",
    "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/hog.py", "10"]
  },
  {
    "name": "steady",
    "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/steady.py", "2"]
  }
]
~~~~

### fixtures/measure-legs/hog.py

~~~~text
"""hog.py <s> — a measure-legs fixture leg: one busy child per logical core for s seconds. TOOL-dRedressedBar-18.

It holds host CPU above the concurrent mode's 80% cap, so the next leg must wait for a sample at
or under it (AC4). On a host where it cannot, the arm's liveness half fails rather than passing.
"""
import os
import subprocess
import sys

s = float(sys.argv[1])
exe = getattr(sys, "_base_executable", None) or sys.executable
code = "import time\nend = time.monotonic() + %r\nwhile time.monotonic() < end:\n    pass\n" % s
kids = [subprocess.Popen([exe, "-I", "-c", code]) for _ in range(os.cpu_count() or 1)]
sys.exit(max(k.wait() for k in kids))
~~~~

### fixtures/measure-legs/memio.py

~~~~text
"""memio.py <mb> — a measure-legs fixture leg: commit and touch <mb> MiB, then write <mb> MiB. TOOL-dRedressedBar-18.

The job's peak commit must read at least <mb> MiB and its write counters at least <mb> MiB (AC2).
The file goes under TMPDIR, the scratch the profiler gives every leg, and is removed before exit.
"""
import os
import sys
import tempfile

mb = int(sys.argv[1])
block = bytearray(mb * 1024 * 1024)
for off in range(0, len(block), 4096):
    block[off] = 1
fd, path = tempfile.mkstemp(prefix="memio.")
try:
    with os.fdopen(fd, "wb") as fh:
        step = 1024 * 1024
        for off in range(0, len(block), step):
            fh.write(block[off:off + step])
        fh.flush()
        os.fsync(fh.fileno())
finally:
    os.remove(path)
sys.exit(0)
~~~~

### fixtures/measure-legs/printenv.py

~~~~text
"""printenv.py — a measure-legs fixture leg: every environment NAME it sees, then one planted credential.

TOOL-dRedressedBar-18, AC9 and AC11. Names only, never values: the log is a durable record. The last
line is a URL whose userinfo the profiler's redaction must mask before the log is kept.
"""
import os

for name in sorted(os.environ):
    print(name)
print("https://u:s3cret@example.invalid/x")
~~~~

### fixtures/measure-legs/queued.sh

~~~~text
#!/usr/bin/env bash
# queued.sh — a measure-legs fixture leg whose own bar QUEUES on the host turnstile. TOOL-dRedressedBar-18, AC15.
#
# It runs the real runner's hold verb over `true` from the top level, the leg's working directory.
# The profile holds no turnstile, so this bar takes a ticket and waits behind whatever holds the
# host, and the profiler must read that wait from the queue. GATE_REGEN_CHECK=0 is set HERE, inside
# the leg, so the bar's generated-output preflight does not run before it queues.
set -u
here=${0%/*}
GATE_REGEN_CHECK=0 exec bash "$here/../../run-gates.sh" --hold -- true
~~~~

### fixtures/measure-legs/serial.json

~~~~text
[
  {
    "name": "spawn six",
    "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/spawn.py", "6", "3"]
  },
  {
    "name": "spawn none",
    "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/spawn.py", "0", "3"]
  },
  {
    "name": "memio",
    "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/memio.py", "200"]
  },
  {
    "name": "printenv",
    "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/printenv.py"]
  }
]
~~~~

### fixtures/measure-legs/spawn.py

~~~~text
"""spawn.py <n> <hold_s> — a measure-legs fixture leg: n children, each sleeping hold_s. TOOL-dRedressedBar-18.

Each child is the BASE interpreter run with `-I -c`, so a launcher shim or a venv redirector adds no
process of its own and the profiler's per-process rows can be told apart by that argv. With n = 0
this process sleeps hold_s itself: it is the zero-child twin whose process count cancels the wrapper
and the interpreter, so the difference of the two counts is n by construction (AC1).
"""
import subprocess
import sys
import time

n, hold = int(sys.argv[1]), float(sys.argv[2])
exe = getattr(sys, "_base_executable", None) or sys.executable
kids = [subprocess.Popen([exe, "-I", "-c", "import time; time.sleep(%r)" % hold]) for _ in range(n)]
if not kids:
    time.sleep(hold)
sys.exit(max([k.wait() for k in kids] or [0]))
~~~~

### fixtures/measure-legs/stall.json

~~~~text
[
  {
    "name": "stall",
    "argv": ["bash", "{prefix}/run-gates/fixtures/measure-legs/stall.sh", "20"]
  },
  {
    "name": "steady",
    "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/steady.py", "20"]
  },
  {
    "name": "churn",
    "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/churn.py", "20"]
  }
]
~~~~

### fixtures/measure-legs/stall.sh

~~~~text
#!/usr/bin/env bash
# stall.sh <s> — a measure-legs fixture leg that HANGS and still spawns. TOOL-dRedressedBar-18, AC6.
#
# The shape of this build's hung canary: blocked reading a FIFO while a loop beside it keeps spawning
# `sleep`, so process churn alone would call it alive. It prints nothing while blocked, its tree's
# CPU stays near zero, and a delayed writer frees the FIFO after <s> seconds, so it ends by itself.
set -u
s=${1:-20}
d=$(mktemp -d "${TMPDIR:-/tmp}/stall.XXXXXXXX") || exit 1
mkfifo "$d/fifo" || exit 1
( while :; do sleep 1; done ) &
spinner=$!
( sleep "$s"; printf 'go\n' > "$d/fifo" ) &
IFS= read -r _line < "$d/fifo"
kill "$spinner" 2>/dev/null
wait "$spinner" 2>/dev/null
rm -rf "$d"
exit 0
~~~~

### fixtures/measure-legs/steady.py

~~~~text
"""steady.py <s> — a measure-legs fixture leg: silent and busy for s seconds. TOOL-dRedressedBar-18.

Its log never grows and its one process burns CPU the whole time, so the stall test's CPU half must
keep it from reading STALLED however long the window (AC6), and it is the leg a held host turnstile
runs beside (AC15).
"""
import sys
import time

end = time.monotonic() + float(sys.argv[1])
n = 0
while time.monotonic() < end:
    n += 1
sys.exit(0)
~~~~

### fixtures/measure-legs/turnstile.json

~~~~text
[
  {
    "name": "steady",
    "argv": ["python3", "{prefix}/run-gates/fixtures/measure-legs/steady.py", "3"]
  },
  {
    "name": "queued",
    "argv": ["bash", "{prefix}/run-gates/fixtures/measure-legs/queued.sh"]
  }
]
~~~~

