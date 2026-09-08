#!/usr/bin/env python3
"""census.py — one bounded read of the process table, or a refusal.

gov:kit process-monitor@0.1

Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-1.md

WHAT THIS MODULE DOES NOT DO, stated here because a structural reader looks like a semantic one to
everybody who did not write it. It reports what is running. It decides nothing: it does not know
which rows are yours (scope.py), which are dead weight (classify.py), or how to kill one (reap.py).

THE ROW CONTRACT, and every field is load-bearing:

    winpid     int         PRIMARY KEY. Every process has one. Never None.
    msys_pid   int|None    the MSYS id, present only for kind == 'msys'
    win_ppid   int|None    CIM's ParentProcessId. Defined for every row.
    msys_ppid  int|None    the MSYS parent. Present only for kind == 'msys'.
    kind       str         'msys' | 'native'
    age_s      float
    cpu_s      float|None  None means UNJOINED or unreported, NEVER zero
    command    str|None    the full command line. None for a process reporting none.
    backend    str         'windows-join' | 'posix-ps'

WHY TWO PARENT FIELDS. Measured on the machine this was built for: MSYS rows are 26 of 332, and the
gate runner dispatches its legs as NATIVE processes. A descendant walk over MSYS edges alone
structurally cannot see the children of a python leg, which is most of what this kit exists to
reap. `win_ppid` is defined for every row and carries no sentinel; `msys_ppid` is an overlay that is
absent for the native majority, and its absence is a statement about backend visibility, never
about a parent being dead.

WHY IT REFUSES. A backend that cannot answer raises. It never returns an empty list, because a
census reporting zero processes because its reader failed is indistinguishable from a machine with
nothing running on it, and every unit downstream would report a clean tree.
"""
import os
import re
import subprocess
import sys

# The bit MSYS sets on the PID it reports for a process it did not spawn. Measured: 306 of 332 rows
# carry it, and `msys_pid & ~BIT == winpid` for every one. A PID carrying it is a SYNTHETIC id that
# addresses nothing MSYS can signal, which is why it decides `kind` rather than being masked off and
# forgotten.
MSYS_SYNTHETIC_BIT = 0x400000

# Applied to the CHILD, never through a pipe: `subprocess.run(timeout=)` kills the child and raises.
# A bound wrapped around a pipeline bounds the verdict and not the clock.
BACKEND_TIMEOUT_S = 90

_PS_W_ROW = re.compile(r"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+")

_CIM_QUERY = (
    "Get-CimInstance Win32_Process | ForEach-Object { "
    "@($_.ProcessId, $_.ParentProcessId, "
    "(($_.KernelModeTime + $_.UserModeTime)/1e7), "
    "([int]((Get-Date) - $_.CreationDate).TotalSeconds), "
    "($_.CommandLine -replace '[\\r\\n]+',' ')) -join [char]1 }"
)
_CIM_SEP = ""


class CensusRefused(RuntimeError):
    """A backend could not answer. Never swallowed into an empty table."""


def run_bounded(argv, timeout=BACKEND_TIMEOUT_S):
    """Run argv, return its stdout decoded with errors='replace'.

    BYTES, not text=True. Measured: PowerShell writes the console codepage, and a single 0xe7 in
    some process's command line killed a text=True read with a UnicodeDecodeError raised on a
    READER THREAD — after which `.stdout` is None and the caller sees an AttributeError far from
    the cause.
    """
    try:
        done = subprocess.run(argv, capture_output=True, timeout=timeout)
    except FileNotFoundError as exc:
        raise CensusRefused("%s: not runnable (%s)" % (argv[0], exc))
    except subprocess.TimeoutExpired:
        raise CensusRefused("%s: did not answer within %ds" % (argv[0], timeout))
    return (done.stdout or b"").decode("utf-8", "replace")


def parse_cim(text):
    """CIM lines -> {winpid: (win_ppid, cpu_s, age_s, command)} plus the rejected-row count."""
    rows, rejected = {}, 0
    # THE PRODUCER'S TERMINATOR, not Python's. `str.splitlines()` also breaks on \v, \f, \x1c,
    # \x1d, \x1e, \x85, U+2028 and U+2029, while the CIM query strips only [\r\n]. A process whose
    # own command line embeds any of those splits across rows, and the well-formed fragment
    # OVERWRITES the row for whatever winpid it names -- a forged census row, with rejected=0.
    for line in text.replace("\r", "").split("\n"):
        if not line.strip():
            continue
        parts = line.split(_CIM_SEP)
        # The ROW GUARD. Adopted by citation from the gate runner's own scan_descendants, which
        # records the hazard: a command line containing a newline splits one process across rows
        # "whose field 2 and 3 are attacker-or-accident-chosen text", and without an anchored
        # numeric test "this walk feeds arbitrary text to kill -9". Counted, never dropped silently.
        if len(parts) < 4 or not parts[0].isdigit() or not parts[1].isdigit():
            rejected += 1
            continue
        try:
            cpu = float(parts[2])
            age = float(parts[3])
        except ValueError:
            rejected += 1
            continue
        command = parts[4].strip() if len(parts) > 4 else ""
        rows[int(parts[0])] = (int(parts[1]), cpu, age, command or None)
    return rows, rejected


def parse_ps_w(text):
    """`ps -W` lines -> {winpid: (msys_pid, msys_ppid)} plus the rejected-row count.

    Only the four id columns are read. `STIME` is a clock for today and a `Mon DD` for anything
    older, so it cannot give an age; `COMMAND` is the EXECUTABLE PATH with no arguments, which is
    why scope attribution reads CIM's CommandLine instead — an earlier probe scoped on this column
    and matched ZERO of 315 rows in a tree full of agent processes.
    """
    rows, rejected = {}, 0
    for line in text.replace("\r", "").split("\n")[1:]:
        if not line.strip():
            continue
        hit = _PS_W_ROW.match(line)
        if not hit:
            rejected += 1
            continue
        msys_pid, msys_ppid, _pgid, winpid = (int(g) for g in hit.groups())
        rows[winpid] = (msys_pid, msys_ppid)
    return rows, rejected


def build_windows_rows(cim_rows, psw_rows):
    """Join the two reads into the row contract."""
    out = []
    for winpid, (win_ppid, cpu, age, command) in cim_rows.items():
        overlay = psw_rows.get(winpid)
        msys_pid = msys_ppid = None
        kind = "native"
        if overlay is not None:
            cand_pid, cand_ppid = overlay
            # THE DISCRIMINATOR. A PID carrying the synthetic bit is MSYS's stand-in for a process
            # it did not spawn; it is not an id MSYS can signal. Without this test every row would
            # be labelled `msys` -- `ps -W` reports a PID for all of them -- and the whole native
            # population would be handed to a signal that cannot reach it.
            if not cand_pid & MSYS_SYNTHETIC_BIT:
                kind = "msys"
                msys_pid, msys_ppid = cand_pid, cand_ppid
        out.append({
            "winpid": winpid,
            "msys_pid": msys_pid,
            "win_ppid": win_ppid,
            "msys_ppid": msys_ppid,
            "kind": kind,
            "age_s": age,
            "cpu_s": cpu,
            "command": command,
            "backend": "windows-join",
        })
    return out


def parse_posix(text):
    """`ps -eo pid,ppid,etimes,times,args` -> rows, rejected.

    UNEXERCISED on the machine this was built on: MSYS `ps` rejects `-o` outright
    (`ps: unknown option -- o`), so this path is graded by a captured fixture and its arm says so
    rather than implying coverage. On POSIX both namespaces collapse to one, which is exactly what
    the row contract records.
    """
    rows, rejected = [], 0
    for line in text.replace("\r", "").split("\n")[1:]:
        parts = line.split(None, 4)
        if len(parts) < 4 or not parts[0].isdigit() or not parts[1].isdigit() \
                or not parts[2].isdigit():
            rejected += 1
            continue
        pid, ppid, etimes = int(parts[0]), int(parts[1]), float(parts[2])
        cpu = parse_cpu_clock(parts[3])
        if cpu is None:
            rejected += 1
            continue
        rows.append({
            "winpid": pid,
            "msys_pid": pid,
            "win_ppid": ppid,
            "msys_ppid": ppid,
            "kind": "msys",
            "age_s": etimes,
            "cpu_s": cpu,
            "command": (parts[4].strip() if len(parts) > 4 else "") or None,
            "backend": "posix-ps",
        })
    return rows, rejected


def parse_cpu_clock(token):
    """`ps` TIME, as `[[DD-]HH:]MM:SS`, to seconds. None when it is not that shape."""
    days = 0
    if "-" in token:
        head, token = token.split("-", 1)
        if not head.isdigit():
            return None
        days = int(head)
    bits = token.split(":")
    if not bits or len(bits) > 3 or not all(b.isdigit() for b in bits):
        return None
    total = 0.0
    for b in bits:
        total = total * 60 + int(b)
    return total + days * 86400


def resolve_backend(forced=""):
    """Which backend to use. A forced name outside the set REFUSES, never falls through."""
    known = ("windows-join", "posix-ps")
    if forced:
        if forced not in known:
            raise CensusRefused(
                "PROCMON_BACKEND=%r names no known backend; known are %s. Refusing rather than "
                "defaulting: a census that silently picks a reader is one whose output nobody can "
                "attribute." % (forced, ", ".join(known)))
        return forced
    return "windows-join" if sys.platform.startswith("win") or os.name == "nt" else "posix-ps"


def scan_processes(forced_backend="", timeout=BACKEND_TIMEOUT_S):
    """The census. Returns (rows, counts). Raises CensusRefused; never returns an empty table."""
    backend = resolve_backend(forced_backend)
    if backend == "windows-join":
        cim_rows, cim_rejected = parse_cim(
            run_bounded(["powershell", "-NoProfile", "-Command", _CIM_QUERY], timeout))
        if not cim_rows:
            raise CensusRefused(
                "the CIM read returned no usable rows, so the process table was not read. "
                "Refusing rather than reporting an empty table.")
        psw_rows, psw_rejected = parse_ps_w(run_bounded(["ps", "-W"], timeout))
        rows = build_windows_rows(cim_rows, psw_rows)
        rejected = cim_rejected + psw_rejected
    else:
        rows, rejected = parse_posix(run_bounded(
            ["ps", "-eo", "pid,ppid,etimes,times,args"], timeout))
        if not rows:
            raise CensusRefused(
                "the ps read returned no usable rows. Refusing rather than reporting an empty "
                "table.")
    counts = measure_rows(rows, rejected, backend)
    return rows, counts


def measure_rows(rows, rejected, backend):
    """Every figure this module reports, DERIVED. No count of this population is ever authored."""
    return {
        "backend": backend,
        "total": len(rows),
        "rejected": rejected,
        "msys": sum(1 for r in rows if r["kind"] == "msys"),
        "native": sum(1 for r in rows if r["kind"] == "native"),
        "no_command": sum(1 for r in rows if r["command"] is None),
        "no_cpu": sum(1 for r in rows if r["cpu_s"] is None),
    }


FIELDS = ("winpid", "msys_pid", "win_ppid", "msys_ppid", "kind", "age_s", "cpu_s", "command",
          "backend")


def render_rows(rows, counts):
    """TSV, header first, then one line per row, then the derived summary."""
    out = ["\t".join(FIELDS)]
    for r in sorted(rows, key=lambda r: -r["age_s"]):
        out.append("\t".join(
            "" if r[f] is None else
            ("%.1f" % r[f] if f in ("age_s", "cpu_s") else str(r[f]).replace("\t", " "))
            for f in FIELDS))
    out.append(
        "# census: %(total)d row(s) via %(backend)s · %(msys)d msys · %(native)d native · "
        "%(rejected)d rejected · %(no_command)d with no command · %(no_cpu)d with no cpu" % counts)
    return "\n".join(out)


def main(argv):
    if "--print" not in argv:
        sys.stderr.write("usage: census.py --print\n")
        return 2
    try:
        rows, counts = scan_processes(os.environ.get("PROCMON_BACKEND", ""))
    except CensusRefused as exc:
        sys.stderr.write("census: REFUSED — %s\n" % exc)
        return 1
    sys.stdout.write(render_rows(rows, counts) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
