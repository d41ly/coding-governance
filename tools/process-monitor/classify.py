#!/usr/bin/env python3
"""classify.py — age DECIDES, the CPU rate LABELS.

gov:kit process-monitor@0.1

Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-3.md

A single CPU sample cannot separate a spin loop from honest work; a declared deadline can separate
either from abandonment. So a row is FLAGGED on age alone, and the rate only describes it.

THE VOCABULARY IS CLOSED, five members, and every one has a producing condition:

    OK       under the ceiling. Nothing else about the row matters.
    UNKNOWN  flagged, but `cpu_s` is None — the backend could not describe it.
    ORPHAN   flagged, and `win_ppid` names no row in this census.
    SPIN     flagged, and cpu_s/age_s >= the declared rate.
    IDLE     flagged, and none of the above.

PARENTLESS IS A LABEL AND NEVER A LICENCE. Measured on the machine this was built for: 24 of 337
rows are parentless and 18 are older than an hour — csrss, wininit, winlogon, explorer, Spotify,
msedge. On Windows a parent exiting neither reparents its children nor clears the field, so
parentless is the ORDINARY state of a long-lived desktop process and no age ceiling separates it
from an abandoned one. The only thing between `reap-orphans` and `explorer.exe` is the SCOPE FENCE,
which is why this module grades only rows the fence admitted and why that ordering is a safety
requirement rather than tidiness.

`msys_ppid` PARTICIPATES IN NEITHER PREDICATE. It is absent for the native majority — 318 of 337
rows here — and reading that absence as a dead parent would grade every native process ORPHAN, or
(the mirror defect) every native process UNKNOWN and the default mode inert over the whole
population this kit exists to reap. The parent question is `win_ppid`'s, which has no sentinel.
"""
import os
import sys

VERDICTS = ("OK", "UNKNOWN", "ORPHAN", "SPIN", "IDLE")


def derive_verdict(row, ceiling, spin_rate, live_winpids):
    """One row -> one member of VERDICTS."""
    age = row.get("age_s") or 0.0
    if age <= ceiling:
        return "OK"
    cpu = row.get("cpu_s")
    if cpu is None:
        return "UNKNOWN"
    parent = row.get("win_ppid")
    if parent is None or parent not in live_winpids:
        return "ORPHAN"
    return "SPIN" if age > 0 and (cpu / age) >= spin_rate else "IDLE"


def scan_verdicts(rows, scope, ceiling, spin_rate):
    """Grade every row the fence admitted. Returns (graded, counts).

    `graded` is a list of (row, verdict), flagged rows only, oldest first.
    """
    live = {r["winpid"] for r in rows}
    graded = []
    for r in rows:
        if r["winpid"] not in scope:
            continue
        verdict = derive_verdict(r, ceiling, spin_rate, live)
        if verdict != "OK":
            graded.append((r, verdict))
    graded.sort(key=lambda pair: -(pair[0].get("age_s") or 0))
    counts = {"census": len(rows), "scoped": len(scope), "flagged": len(graded)}
    for v in VERDICTS:
        counts[v.lower()] = sum(1 for _r, x in graded if x == v)
    return graded, counts


def render_report(graded, counts):
    out = []
    for r, verdict in graded:
        rate = "" if r.get("cpu_s") is None or not r.get("age_s") \
            else "%.2f" % (r["cpu_s"] / r["age_s"])
        out.append("%-8s winpid %-7d age %7.2fh cpu %9.1fs rate %-5s %s"
                   % (verdict, r["winpid"], (r["age_s"] or 0) / 3600.0, r.get("cpu_s") or 0.0,
                      rate or "?", (r.get("command") or "")[:70]))
    out.append("classify: %(flagged)d flagged of %(scoped)d scoped of %(census)d in the census "
               "· %(orphan)d orphan · %(spin)d spin · %(idle)d idle · %(unknown)d unknown"
               % counts)
    return "\n".join(out)


def main(argv):
    import census
    import scope as scope_mod
    root_dir = os.environ.get("PROCMON_ROOT", os.getcwd())
    conf_path = os.path.join(root_dir, ".process-monitor.conf")
    ceiling, spin_rate = 14400.0, 0.5
    try:
        with open(conf_path, "r", encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("PROCMON_AGE_CEILING="):
                ceiling = float(line.split("=", 1)[1].strip().strip("\"'"))
            elif line.startswith("PROCMON_SPIN_RATE="):
                spin_rate = float(line.split("=", 1)[1].strip().strip("\"'"))
        roots = scope_mod.read_roots(text)
        rows, _c = census.scan_processes(os.environ.get("PROCMON_BACKEND", ""))
        chain = scope_mod.build_self_chain(rows, os.getpid())
        scope, _sc = scope_mod.derive_scope(rows, roots, chain)
    except (OSError, ValueError, scope_mod.ScopeRefused, census.CensusRefused) as exc:
        # A read failure is NOT a clean report. Printing "0 flagged" here would be
        # indistinguishable from a healthy machine, which is the class this kit exists to refuse.
        sys.stderr.write("classify: REFUSED — %s\n" % exc)
        return 1
    graded, counts = scan_verdicts(rows, scope, ceiling, spin_rate)
    if "--report" in argv:
        print(render_report(graded, counts))
    return 0


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(sys.argv[1:]))
