#!/usr/bin/env python3
"""profile_bar.py — measure a run-gates bar run as a RUN, and say which lever can move it.

    python <prefix>/run-gates/profile_bar.py                 # profile the full bar at the default width
    python <prefix>/run-gates/profile_bar.py --width 4       # pin the pool width
    python <prefix>/run-gates/profile_bar.py --report        # re-print the last record, run nothing

WHAT THIS DOES NOT CHECK. It does not verify a leg is correct, does not attribute a leg's cost to any
cause inside it, and does not prove the machine was quiet — it asserts what it could verify and marks
the rest `unverified`. A wall clock measured on a busy machine is a real number about a busy machine.

WHY IT WRAPS RATHER THAN PATCHES. `run-gates.sh` already times every leg and already prints a
parseable verdict per leg. What it does not record is the RUN those numbers came from: the width, the
commit, the host, the wall clock, and whether guards were bypassed. Without that envelope two numbers
taken a month apart are not comparable, which is how `<git-dir>/gate-ledger.tsv` — a dispatch hint,
last-write-wins, never evicting a renamed leg — became the thing people read as a profile.

THE ONE NUMBER THIS EXISTS FOR. A bounded-pool bar has two independent lower bounds on its wall clock:
the longest single leg (no width beats it) and the total work divided by the width (perfect packing).
Whichever is larger is the regime, and the regime decides which fix is the only one that can work.
Trimming small legs on a floor-bound bar buys nothing at all; adding workers to it buys nothing
either. That arithmetic is a property of any bounded-pool bar, not of this repo's legs, which is why
this verb ships with the kit.

WHY IT REFUSES SO READILY. Every refusal below exists because a wrong measurement is worse than no
measurement: this record is advertised as comparable across months, and a confident wrong number in
it gets believed. The refusals are a ledger that did not move, and a packing ratio below 1.0 —
arithmetically impossible for a real run, and therefore proof the durations came from another one.
"""
import argparse
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import time
from datetime import datetime, timezone

KITDIR = os.path.dirname(os.path.abspath(__file__))
# The runner is this file's SIBLING, derived and never spelled: this kit installs at <prefix>/run-gates/
# and a hardcoded "tools/run-gates/run-gates.sh" resolves to nothing at any other prefix.
# Forward-SLASHED before it is ever handed to bash. A POSIX-emulation shell on Windows mangles a
# backslash path, and os.path.join gives backslashes there. Measured: the runner exited 127 having
# run zero legs.
RUNNER = os.path.join(KITDIR, "run-gates.sh").replace("\\", "/")

# The runner's verdict grammar (its TAIL CONTRACT): "<verb>  <leg name>[  (<tail>)]", where the verb
# is GATE followed by ok / skip / FAIL. The name is separated from any parenthesised tail by TWO
# spaces, which is what makes splitting on a double space return the bare name even when the name has
# spaces in it, and most leg names do.
#
# The anchor holds ONLY because LF is the sole line break honoured below. It is NOT true that "only
# the runner writes at column 0": a failing leg's own output is echoed into this stream, indented by
# `sed` after LF and after LF alone, so a leg emitting \x1e, \v or \f could otherwise present a
# fabricated verdict at column 0 — and \x1e is the runner's own field separator, so that is reachable
# by accident rather than only by malice.
VERDICT = re.compile(r"^GATE (ok|skip|FAIL)\s\s+(.*)$")


def parse_verdicts(stdout):
    """Runner stdout -> [(name, verdict)], in the order reported, which is manifest order.

    Splits on LF ONLY. `str.splitlines()` also breaks on \\v \\f \\x1c \\x1d \\x1e, none of which the
    runner treats as a line break, so using it lets leg output inject a verdict row.
    """
    out = []
    for line in stdout.split("\n"):
        line = line.rstrip("\r")
        m = VERDICT.match(line)
        if not m:
            continue
        verdict, rest = m.group(1), m.group(2)
        name = rest.split("  ")[0].strip()   # the tail contract: two spaces before any tail
        if name:
            out.append((name, verdict))
    return out


def read_timings(path):
    """The runner's TSV -> {leg name: seconds}. A corrupt file is an EMPTY file, never a crash."""
    durs = {}
    if not path or not os.path.exists(path):
        return durs
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                parts = line.rstrip("\n").split("\t")
                if len(parts) >= 2:
                    try:
                        durs[parts[0]] = float(parts[1])
                    except ValueError:
                        pass
    except OSError:
        return {}
    return durs


def derive_regime(durations, width):
    """The regime arithmetic. `durations` is the list of EXECUTED leg costs, in seconds."""
    if not durations or width < 1:
        return None
    floor = max(durations)
    throughput = sum(durations) / float(width)
    return {
        "floor": round(floor, 3),
        "throughput": round(throughput, 3),
        "bound": "floor" if floor >= throughput else "throughput",
        "ideal": round(max(floor, throughput), 3),
        "work": round(sum(durations), 3),
    }


def derive_width(explicit, env):
    """The width the CHILD will actually use. Returns (width, source).

    The runner reads `JOBS=${GATE_JOBS:-min(8,nproc)}`, so an INHERITED GATE_JOBS wins over any
    default this process would compute. Deriving the recorded width from `cpu_count` while the child
    obeys an exported GATE_JOBS records a divisor the run never used, and `throughput`, `bound`,
    `ideal` and `packing` are then all wrong together. `GATE_JOBS=1` is this repo's own documented
    serial rollback, so that environment is ordinary rather than exotic.

    The clamps MIRROR the runner's deliberately: bound by LENGTH before any numeric test, because a
    20-digit value overflows the comparison rather than failing it.
    """
    if explicit > 0:
        return explicit, "--width"
    raw = env.get("GATE_JOBS", "")
    if raw:
        if not raw.isdigit():
            return 1, "GATE_JOBS non-numeric, clamped"
        if len(raw) >= 5:
            return 64, "GATE_JOBS over-long, clamped"
        return max(1, int(raw)), "GATE_JOBS"
    try:
        cores = os.cpu_count() or 4
    except NotImplementedError:
        cores = 4
    return max(1, min(8, cores)), "default min of 8 and nproc"


def check_quiet(_runner=None):
    """Can we show the machine had no OTHER bar running? Returns (state, detail).

    LIVENESS FIRST. This probe reports `true` or `false` only after proving it can actually READ a
    command line. MSYS `ps` prints the executable path and never argv, so grepping its output for a
    script name matches nothing on any Windows node and returns a confident, permanent affirmative —
    the reassuring zero this repo's charter forbids, and the exact defect this function shipped with.

    The liveness assertion is that the query can read THIS process's own command line. If it cannot
    read the one command line we know exists, a zero from it is evidence of nothing.

    ONE query, filtered to `bash.exe` plus our own pid. An unfiltered enumeration of every process
    with its command line took long enough on a loaded node to dominate the profiler's own runtime,
    which matters because a probe nobody can afford to run is a probe that gets removed.

    `_runner` is the subprocess entry point, injected so the self-test can drive this function
    against a query that returns rows it cannot read. It is not a knob: no caller passes it.
    """
    runner = _runner or subprocess.run
    ps = shutil.which("powershell") or shutil.which("pwsh")
    if not ps:
        return "unverified", "no powershell on PATH, cannot read process command lines on this host"
    script = (
        "Get-CimInstance Win32_Process -Filter \"Name='bash.exe' or ProcessId=%d\" | "
        "ForEach-Object { \"$($_.ProcessId)|$($_.CommandLine)\" }" % os.getpid()
    )
    try:
        out = runner([ps, "-NoProfile", "-NonInteractive", "-Command", script],
                     capture_output=True, text=True, timeout=120,
                     encoding="utf-8", errors="replace")
    except Exception as exc:   # a PROBE reports that it could not look; it never raises
        return "unverified", "process query failed: %s" % exc
    if getattr(out, "returncode", 1) != 0:
        return "unverified", "process query exited %s" % getattr(out, "returncode", "?")
    rows = [l.strip() for l in (out.stdout or "").split("\n") if l.strip()]
    mypid = str(os.getpid())
    # THE LIVENESS ASSERTION: our own row must be present AND carry a non-empty command line.
    mine = [r for r in rows if r.split("|", 1)[0] == mypid]
    if not mine or not mine[0].split("|", 1)[-1].strip():
        return ("unverified",
                "process query returned %d row(s) but could not read this process's own command "
                "line, so a zero from it proves nothing" % len(rows))
    foreign = [r for r in rows if "run-gates.sh" in r and r.split("|", 1)[0] != mypid]
    if foreign:
        return "false", "%d foreign run-gates process(es) visible, read %d row(s)" % (
            len(foreign), len(rows))
    return "true", "read %d row(s) including this process, no foreign run-gates among them" % len(rows)


def check_packing(wall, ideal):
    """Is this wall clock arithmetically possible for these durations? Returns (ok, packing, why).

    Wall clock cannot be below the longest single leg, and cannot be below total work over the width.
    So a packing ratio under 1.0 is not a bad result, it is PROOF the durations did not come from
    this run — whatever any mtime said. Separated from main() so the self-test can reach it: a
    refusal reachable only through a run that produces stale data is a refusal nobody ever arms.
    """
    if not ideal:
        return True, None, ""
    packing = round(wall / ideal, 3)
    if packing < 0.99:
        return False, packing, (
            "packing %.3f is below 1.0, which is arithmetically impossible for a real run — wall "
            "%.1fs cannot be under the %.1fs these durations imply, so they are not this run's"
            % (packing, wall, ideal))
    return True, packing, ""


def measure_orphans(manifest_path, timings_path):
    """Count timing-cache rows naming a leg the manifest no longer declares. Reports, never gates.

    The runner's carry-forward keeps any cached row this run did not measure, and that predicate is
    "did this run measure it", never "does the manifest still declare it". So a renamed or deleted leg
    keeps its row forever and the file grows with the rename history.

    Returns (count, seconds, manifest_leg_count), or None when either file is unreadable — a probe
    that cannot look reports that it could not look.
    """
    try:
        with open(manifest_path, encoding="utf-8") as fh:
            legs = {l["name"] for l in json.load(fh)}
    except (OSError, ValueError, KeyError, TypeError):
        return None
    durs = read_timings(timings_path)
    if not durs:
        return None
    orphans = [(k, v) for k, v in durs.items() if k not in legs]
    return len(orphans), round(sum(v for _, v in orphans), 1), len(legs)


def resolve_bash(script):
    r"""Find a bash that can actually SEE `script`, by RUNNING each candidate. Never by PATH alone.

    On Windows, PATH order commonly puts C:\Windows\System32\bash.exe — the WSL launcher — ahead of
    Git-Bash. WSL bash cannot open a `C:/...` path at all, so it answers `No such file or directory`
    for a script that plainly exists and the runner exits 127 having run zero legs. MEASURED here,
    not theorised. The probe is the property that matters: can this bash stat the script?
    """
    cands = [os.environ.get("GOV_BASH", ""), shutil.which("bash") or "",
             "C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe", "bash"]
    tried = []
    for c in cands:
        if not c or c in tried:
            continue
        tried.append(c)
        try:
            r = subprocess.run([c, "-c", 'test -f "$1"', "_", script],
                               capture_output=True, text=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            continue
        if r.returncode == 0:
            return c, tried
    return "", tried


def run_git(args, cwd=None):
    try:
        r = subprocess.run(["git"] + args, capture_output=True, text=True, cwd=cwd, timeout=30)
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def main():
    ap = argparse.ArgumentParser(description="Measure a run-gates bar run and derive its regime.")
    ap.add_argument("--width", type=int, default=0, help="pool width (GATE_JOBS); 0 = resolve it")
    ap.add_argument("--scoped", action="store_true", help="honour leg guards (default profiles the FULL bar)")
    ap.add_argument("--out", default="", help="record path (default <git-dir>/gate-profile.jsonl)")
    ap.add_argument("--report", action="store_true", help="print the last record and exit; run nothing")
    args = ap.parse_args()

    root = run_git(["rev-parse", "--show-toplevel"])
    if not root:
        print("profile-bar: not a git repo", file=sys.stderr)
        return 2
    gitdir = run_git(["rev-parse", "--git-dir"])
    if not gitdir:
        print("profile-bar: no git dir, nowhere to write the record", file=sys.stderr)
        return 2
    record_path = args.out or os.path.join(gitdir, "gate-profile.jsonl")
    # THE LEDGER, not the retired `gate-timings.tsv`. The run-record unit replaced that cache
    # rather than writing both, so a profiler still pointed at the old path would find a file
    # nothing updates and take its did-not-move refusal on EVERY invocation — turning this tool
    # and its gate leg into a leg whose subject can no longer run. The parser below needs no
    # edit: the ledger keeps the duration in field 2 for exactly this reason.
    timings_path = os.path.join(gitdir, "gate-ledger.tsv")
    manifest_path = os.environ.get("GATE_LEGS") or os.path.join(os.path.dirname(KITDIR), "gate-legs.json")

    if args.report:
        return print_last(record_path)

    if not os.path.exists(RUNNER):
        print("profile-bar: runner not found beside this verb: %s" % RUNNER, file=sys.stderr)
        return 2

    bash, bash_tried = resolve_bash(RUNNER)
    if not bash:
        print("profile-bar: no bash could open the runner. Tried: %s" % ", ".join(bash_tried),
              file=sys.stderr)
        return 2

    # Resolve the width the CHILD will use, then PIN it into the child's environment. Recording a
    # width the run did not use is the whole defect this ordering removes: after this the record and
    # the run cannot diverge, whatever the caller exported.
    env = dict(os.environ)
    width, width_source = derive_width(args.width, env)
    env["GATE_JOBS"] = str(width)
    if args.scoped:
        # Only ever SETTING this left an inherited GATE_FULL in place, so --scoped printed "scoped"
        # over a run in which the child honoured no guard at all. `full` is the one field the envelope
        # can lie about, so the flag must name the run in both directions.
        env.pop("GATE_FULL", None)
    else:
        env["GATE_FULL"] = "1"

    quiet, quiet_detail = check_quiet()
    before_mtime = os.path.getmtime(timings_path) if os.path.exists(timings_path) else 0

    print("profile-bar: running the bar (width %d via %s, %s) — this takes as long as the bar takes"
          % (width, width_source, "scoped" if args.scoped else "GATE_FULL=1"))
    start = time.monotonic()
    proc = subprocess.run([bash, RUNNER], cwd=root, env=env, capture_output=True, text=True)
    wall = time.monotonic() - start

    verdicts = parse_verdicts(proc.stdout)
    if not verdicts:
        print("profile-bar: the run produced NO parseable verdict lines — refusing to record a "
              "measurement of nothing. Runner exit was %d." % proc.returncode, file=sys.stderr)
        sys.stderr.write(proc.stdout[-2000:])
        sys.stderr.write(proc.stderr[-2000:])
        return 2

    after_mtime = os.path.getmtime(timings_path) if os.path.exists(timings_path) else 0
    timings_moved = after_mtime > before_mtime
    durs = read_timings(timings_path)

    legs, missing = [], []
    for name, verdict in verdicts:
        if verdict == "skip":
            legs.append({"name": name, "verdict": verdict, "sec": None})
            continue
        legs.append({"name": name, "verdict": verdict, "sec": durs.get(name)})
        if name not in durs:
            missing.append(name)

    executed = [l["sec"] for l in legs if l["verdict"] != "skip" and l["sec"] is not None]

    # FRESHNESS, acted on rather than merely recorded. The runner writes the cache with
    # `cp ... || true`, an advisory write that fails silently on a locked or read-only gitdir while
    # the bar still exits 0, and then carries forward every row it did not measure. So a cache that
    # did not move means every duration available belongs to an earlier run. Publishing that as this
    # run's measurement is exactly the confident wrong number this tool exists not to produce.
    if executed and not timings_moved:
        print("profile-bar: the ledger did not move, so every duration available belongs to an "
              "EARLIER run. Refusing to publish it as this run's measurement. The bar itself ran: "
              "%d leg(s) reported, runner exit %d." % (len(verdicts), proc.returncode), file=sys.stderr)
        return 2

    regime = derive_regime(executed, width)
    if regime is None:
        print("profile-bar: no executed leg carried a duration, refusing to derive a regime.",
              file=sys.stderr)
        return 2

    ok, packing, why = check_packing(wall, regime["ideal"])
    if not ok:
        print("profile-bar: %s. Refusing." % why, file=sys.stderr)
        return 2
    regime["packing"] = packing

    failed = [l["name"] for l in legs if l["verdict"] == "FAIL"]
    rec = {
        "run": "%s-%s-w%d" % (run_git(["rev-parse", "--short=8", "HEAD"]) or "unknown",
                              datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"), width),
        "at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "sha": run_git(["rev-parse", "--short=8", "HEAD"]) or "unknown",
        "host": socket.gethostname(),
        "width": width,
        "width_source": width_source,
        "full": not args.scoped,
        "wall": round(wall, 3),
        "exit": proc.returncode,
        "failed_legs": failed,
        "env": {
            "quiet": quiet,
            "quiet_detail": quiet_detail,
            "timings_moved": timings_moved,
            "legs_without_duration": missing,
            "timings_orphans": measure_orphans(manifest_path, timings_path),
        },
        "regime": regime,
        "legs": legs,
    }

    with open(record_path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")

    print_summary(rec)
    print("\nprofile-bar: appended to %s" % record_path)
    return 0


def print_summary(rec):
    r = rec["regime"]
    ran = [l for l in rec["legs"] if l["verdict"] != "skip"]
    skipped = [l for l in rec["legs"] if l["verdict"] == "skip"]
    failed = rec.get("failed_legs", [])
    print("")
    print("profile-bar %s  ·  %s  ·  width %d (%s)  ·  %s  ·  runner exit %s" % (
        rec["sha"], rec["host"], rec["width"], rec.get("width_source", "?"),
        "FULL" if rec["full"] else "scoped", rec.get("exit", "?")))
    print("  wall observed      %8.1fs" % rec["wall"])
    print("  total leg work     %8.1fs   across %d executed leg(s), %d skipped, %d FAILED"
          % (r["work"], len(ran), len(skipped), len(failed)))
    print("  floor  (longest)   %8.1fs   <- no width beats this" % r["floor"])
    print("  throughput (work/w)%8.1fs   <- perfect packing at width %d" % (r["throughput"], rec["width"]))
    print("  ideal              %8.1fs   packing %.2fx" % (r["ideal"], r.get("packing") or 0))
    print("")
    if r["bound"] == "floor":
        top = max((l for l in ran if l["sec"] is not None), key=lambda l: l["sec"], default=None)
        print("  BOUND: floor. The bar cannot go below %.1fs at ANY width on ANY hardware." % r["floor"])
        if top:
            print("  The binding leg is: %s (%.1fs, %.0f%% of wall)"
                  % (top["name"], top["sec"], 100.0 * top["sec"] / rec["wall"]))
        print("  Widening the pool and trimming small legs both buy ZERO. Only making that leg")
        print("  cheaper, sharding it, or removing it from the critical path moves this number.")
    else:
        print("  BOUND: throughput. Total work (%.1fs) over width %d dominates the longest leg (%.1fs)."
              % (r["work"], rec["width"], r["floor"]))
        print("  More width or less total work both help. Guards that skip legs help most.")
    if rec.get("exit") not in (0, None):
        print("")
        print("  CAVEAT: the bar was RED (runner exit %s), %d leg(s) FAILED: %s"
              % (rec["exit"], len(failed), ", ".join(failed[:5]) or "not attributable"))
        print("  A failing leg records the duration it reached before failing, so this regime is")
        print("  derived from a run that did not complete. Fix the bar, then measure it.")
    if rec["env"]["quiet"] != "true":
        print("")
        print("  CAVEAT: machine quiet = %s (%s)." % (rec["env"]["quiet"], rec["env"]["quiet_detail"]))
        print("  A wall clock measured under other load is a real number about a loaded machine.")
    orph = rec["env"].get("timings_orphans")
    if orph is None:
        print("")
        print("  timing-cache orphans: UNVERIFIED, manifest or cache unreadable.")
    elif orph[0]:
        print("")
        print("  timing-cache orphans: %d row(s) holding %.1fs name a leg the %d-leg manifest no longer"
              % (orph[0], orph[1], orph[2]))
        print("  declares. The runner never evicts them, so any sum taken from that file is inflated.")
    if rec["env"]["legs_without_duration"]:
        print("")
        print("  %d executed leg(s) carried NO duration: %s"
              % (len(rec["env"]["legs_without_duration"]),
                 ", ".join(rec["env"]["legs_without_duration"][:5])))


def print_last(path):
    if not os.path.exists(path):
        print("profile-bar: no record at %s, run without --report first" % path, file=sys.stderr)
        return 2
    last = None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    last = json.loads(line)
                except ValueError:
                    continue
    if last is None:
        print("profile-bar: %s holds no parseable record" % path, file=sys.stderr)
        return 2
    print_summary(last)
    return 0


if __name__ == "__main__":
    sys.exit(main())
