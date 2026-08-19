#!/usr/bin/env python3
"""profile_bar.py — measure a run-gates bar run as a RUN, and say which lever can move it.

    python <prefix>/run-gates/profile_bar.py                 # profile the full bar at the default width
    python <prefix>/run-gates/profile_bar.py --width 4       # pin the pool width
    python <prefix>/run-gates/profile_bar.py --report        # re-print the last record, run nothing

WHAT THIS DOES NOT CHECK. It does not verify a leg is correct, does not attribute a leg's cost to any
cause inside it, and does not prove the machine was quiet — it ASSERTS what it could verify and marks
the rest `unverified`. A wall clock measured on a busy machine is a real number about a busy machine.

WHY IT WRAPS RATHER THAN PATCHES. `run-gates.sh` already times every leg and already prints a
parseable verdict per leg. What it does not record is the RUN those numbers came from: the width, the
commit, the host, the wall clock, and whether guards were bypassed. Without that envelope two numbers
taken a month apart are not comparable, which is how `<git-dir>/gate-timings.tsv` — a dispatch hint,
last-write-wins, never evicting a renamed leg — became the thing people read as a profile.

THE ONE NUMBER THIS EXISTS FOR. A bounded-pool bar has two independent lower bounds on its wall clock:
the longest single leg (no width beats it) and the total work divided by the width (perfect packing).
Whichever is larger is the regime, and the regime decides which fix is the only one that can work.
Trimming small legs on a floor-bound bar buys nothing at all; adding workers to it buys nothing
either. That arithmetic is a property of any bounded-pool bar, not of this repo's legs, which is why
this verb ships with the kit.
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
# and a hardcoded "tools/run-gates/run-gates.sh" resolves to nothing at any other prefix. Same rule the
# runner applies to its own manifest.
# Forward-SLASHED before it is ever handed to bash. A POSIX-emulation shell on Windows mangles a
# backslash path (`bash C:\repo\x.sh` cannot be opened), and os.path.join gives backslashes on
# this platform. Measured: the runner exited 127 having run zero legs.
RUNNER = os.path.join(KITDIR, "run-gates.sh").replace("\\", "/")

# The runner's verdict grammar (its TAIL CONTRACT): "<verb>  <leg name>[  (<tail>)]", where the verb is
# GATE followed by ok / skip / FAIL. The name is separated from any parenthesised tail by TWO spaces,
# which is what makes splitting on a double space return the bare name even when the name has spaces in
# it — and most leg names do. Anchored, so a leg that PRINTS a line resembling a verdict cannot inject
# one: only the runner writes at column 0.
VERDICT = re.compile(r"^GATE (ok|skip|FAIL)\s\s+(.*)$")


def parse_verdicts(stdout):
    """Runner stdout -> [(name, verdict)], in the order reported (which is manifest order)."""
    out = []
    for line in stdout.splitlines():
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


def check_quiet():
    """Can we show the machine had no OTHER bar running? Returns (state, detail).

    LIVENESS, not decoration. This probe can FAIL TO RUN — there is no portable process table, and on
    Windows the MSYS `ps` sees only its own subtree. A probe that cannot look must say `unverified`;
    reporting `true` because it found nothing is exactly the reassuring zero this repo's charter
    forbids, and it would silently bless a contaminated measurement as a clean one.
    """
    ps = shutil.which("ps")
    if not ps:
        return "unverified", "no ps on PATH — cannot enumerate processes"
    try:
        out = subprocess.run([ps, "-W"], capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.SubprocessError) as exc:
        return "unverified", "ps failed: %s" % exc
    if out.returncode != 0:
        # `ps -W` is an MSYS extension; elsewhere it is an error. Fall back to a plain listing.
        try:
            out = subprocess.run([ps, "ax"], capture_output=True, text=True, timeout=20)
        except (OSError, subprocess.SubprocessError) as exc:
            return "unverified", "ps failed: %s" % exc
        if out.returncode != 0:
            return "unverified", "ps exited %d" % out.returncode
    hits = [ln for ln in out.stdout.splitlines() if "run-gates" in ln]
    # Our own child is not contamination; anything else with the runner's name is.
    if len(hits) > 1:
        return "false", "%d run-gates processes visible" % len(hits)
    return "true", "no other run-gates process visible to ps"


def resolve_bash(script):
    r"""Find a bash that can actually SEE `script`, by RUNNING each candidate. Never by PATH alone.

    On Windows, PATH order commonly puts C:\Windows\System32\bash.exe — the WSL launcher — ahead of
    Git-Bash. WSL bash cannot open a `C:/...` path at all (it wants /mnt/c/...), so it answers
    `No such file or directory` for a script that plainly exists, and the runner exits 127 having run
    zero legs. MEASURED here, not theorised. Being on PATH is not evidence a launcher is the right
    one; the same reasoning the sibling resolve_python applies to the MS-Store python3 stub.

    The probe is the property that matters: can this bash stat the script we are about to hand it?
    """
    cands = [os.environ.get("GOV_BASH", ""), shutil.which("bash") or "",
             "C:/Program Files/Git/bin/bash.exe", "C:/Program Files/Git/usr/bin/bash.exe", "bash"]
    tried = []
    for c in cands:
        if not c or c in tried:
            continue
        tried.append(c)
        try:
            r = subprocess.run([c, "-c", "test -f \"$1\"", "_", script],
                               capture_output=True, text=True, timeout=20)
        except (OSError, subprocess.SubprocessError):
            continue
        if r.returncode == 0:
            return c, tried
    return "", tried


def measure_orphans(manifest_path, timings_path):
    """Count timing-cache rows naming a leg the manifest no longer declares. Reports, never gates.

    The runner's carry-forward keeps any cached row this run did not measure, and that predicate is
    "did this run measure it", never "does the manifest still declare it". So a renamed or deleted leg
    keeps its row forever and the file grows with the rename history. Measured on node `a`: 3 orphans
    holding 965 s, which inflates a naive sum of the file by 12%.

    Returns (orphan_count, orphan_seconds, manifest_leg_count) or None when either file is unreadable —
    a probe that cannot look reports that it could not look.
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


def run_git(args, cwd=None):
    try:
        r = subprocess.run(["git"] + args, capture_output=True, text=True, cwd=cwd, timeout=30)
        return r.stdout.strip() if r.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def main():
    ap = argparse.ArgumentParser(description="Measure a run-gates bar run and derive_regime its regime.")
    ap.add_argument("--width", type=int, default=0, help="pool width (GATE_JOBS); 0 = the runner's default")
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
        print("profile-bar: no git dir — nowhere to write the record", file=sys.stderr)
        return 2
    record_path = args.out or os.path.join(gitdir, "gate-profile.jsonl")
    timings_path = os.path.join(gitdir, "gate-timings.tsv")
    # The manifest, derived the way the runner derives it: GATE_LEGS wins, else the kit dir's sibling.
    manifest_path = os.environ.get("GATE_LEGS") or os.path.join(os.path.dirname(KITDIR), "gate-legs.json")

    if args.report:
        return print_last(record_path)

    if not os.path.exists(RUNNER):
        print("profile-bar: runner not found beside this verb: %s" % RUNNER, file=sys.stderr)
        return 2

    env = dict(os.environ)
    if args.width > 0:
        env["GATE_JOBS"] = str(args.width)
    if not args.scoped:
        env["GATE_FULL"] = "1"

    BASH, bash_tried = resolve_bash(RUNNER)
    if not BASH:
        print("profile-bar: no bash could open the runner. Tried: %s" % ", ".join(bash_tried),
              file=sys.stderr)
        return 2

    quiet, quiet_detail = check_quiet()
    before_mtime = os.path.getmtime(timings_path) if os.path.exists(timings_path) else 0

    print("profile-bar: running the bar (%s, %s) — this takes as long as the bar takes" % (
        ("width %d" % args.width) if args.width > 0 else "default width",
        "scoped" if args.scoped else "GATE_FULL=1"))
    start = time.monotonic()
    proc = subprocess.run([BASH, RUNNER], cwd=root, env=env, capture_output=True, text=True)
    wall = time.monotonic() - start

    verdicts = parse_verdicts(proc.stdout)
    if not verdicts:
        print("profile-bar: the run produced NO parseable verdict lines — refusing to record a "
              "measurement of nothing. Runner exit was %d." % proc.returncode, file=sys.stderr)
        sys.stderr.write(proc.stdout[-2000:])
        sys.stderr.write(proc.stderr[-2000:])
        return 2

    after_mtime = os.path.getmtime(timings_path) if os.path.exists(timings_path) else 0
    durs = read_timings(timings_path)
    # Only legs this run EXECUTED carry a duration we may trust. A guard-skipped leg produces no fresh
    # measurement and the runner carries its stale row forward; a leg deleted or renamed since some
    # earlier run keeps its row forever. Both are in that file right now and neither is this run.
    legs, missing = [], []
    for name, verdict in verdicts:
        if verdict == "skip":
            legs.append({"name": name, "verdict": verdict, "sec": None})
            continue
        if name in durs:
            legs.append({"name": name, "verdict": verdict, "sec": durs[name]})
        else:
            legs.append({"name": name, "verdict": verdict, "sec": None})
            missing.append(name)

    executed = [l["sec"] for l in legs if l["verdict"] != "skip" and l["sec"] is not None]
    width = args.width if args.width > 0 else derive_width(len(executed))
    regime = derive_regime(executed, width)
    if regime is None:
        print("profile-bar: no executed leg carried a duration — the timing cache did not move "
              "(mtime %s -> %s). Refusing to derive_regime." % (before_mtime, after_mtime), file=sys.stderr)
        return 2

    rec = {
        "run": "%s-%s-w%d" % (run_git(["rev-parse", "--short=8", "HEAD"]) or "unknown",
                              datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"), width),
        "at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "sha": run_git(["rev-parse", "--short=8", "HEAD"]) or "unknown",
        "host": socket.gethostname(),
        "width": width,
        "full": not args.scoped,
        "wall": round(wall, 3),
        "exit": proc.returncode,
        "env": {
            "quiet": quiet,
            "quiet_detail": quiet_detail,
            "timings_moved": after_mtime > before_mtime,
            "legs_without_duration": missing,
            "timings_orphans": measure_orphans(manifest_path, timings_path),
        },
        "regime": regime,
        "legs": legs,
    }
    rec["regime"]["packing"] = round(rec["wall"] / regime["ideal"], 3) if regime["ideal"] else None

    with open(record_path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")

    print_summary(rec)
    print("\nprofile-bar: appended to %s" % record_path)
    return 0


def derive_width(_n):
    """The runner's own default: min(8, nproc), clamped at 1. Mirrored, not read — the runner does not
    print it. Pass --width to make this a fact instead of an inference."""
    try:
        cores = os.cpu_count() or 4
    except NotImplementedError:
        cores = 4
    return max(1, min(8, cores))


def print_summary(rec):
    r = rec["regime"]
    ran = [l for l in rec["legs"] if l["verdict"] != "skip"]
    skipped = [l for l in rec["legs"] if l["verdict"] == "skip"]
    print("")
    print("profile-bar %s  ·  %s  ·  width %d  ·  %s" % (
        rec["sha"], rec["host"], rec["width"], "FULL" if rec["full"] else "scoped"))
    print("  wall observed      %8.1fs" % rec["wall"])
    print("  total leg work     %8.1fs   across %d executed leg(s), %d skipped"
          % (r["work"], len(ran), len(skipped)))
    print("  floor  (longest)   %8.1fs   <- no width beats this" % r["floor"])
    print("  throughput (work/w)%8.1fs   <- perfect packing at width %d" % (r["throughput"], rec["width"]))
    print("  ideal              %8.1fs   packing %.2fx" % (r["ideal"], rec["regime"]["packing"] or 0))
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
    if rec["env"]["quiet"] != "true":
        print("")
        print("  CAVEAT: machine quiet = %s (%s)." % (rec["env"]["quiet"], rec["env"]["quiet_detail"]))
        print("  A wall clock measured under other load is a real number about a loaded machine.")
    orph = rec["env"].get("timings_orphans")
    if orph is None:
        print("")
        print("  timing-cache orphans: UNVERIFIED — manifest or cache unreadable.")
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
        print("profile-bar: no record at %s — run without --report first" % path, file=sys.stderr)
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
