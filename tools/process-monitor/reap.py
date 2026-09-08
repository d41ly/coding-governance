#!/usr/bin/env python3
"""reap.py — kill a tree and PROVE each member died.

gov:kit process-monitor@0.1

Contract: memory/builds/aReapedSpinner/spec/2026-09-08-spec-TOOL-aReapedSpinner-4.md

THE ONLY IRREVERSIBLE THING THIS KIT DOES. Three measurements shape it and each killed an obvious
design:

  `kill -9 <top>`                left all four descendants of a three-deep tree ALIVE.
  `taskkill /PID <win> /T /F`    printed SUCCESS and killed ONE of four — `/T` walks the WINDOWS
                                 tree, and MSYS parent edges are a different graph.
  a leaves-first walk of the right graph, signalled per row, killed 5 of 5.

And one more that inverts the naive fix: a native process the MSYS shell did NOT spawn answers
`No such process` to both the bash builtin `kill` and `/usr/bin/kill`, and dies only to
`taskkill /PID`. The predicate is not "native" — it is "not an MSYS child", which is every orphan
worth reaping.

SO THE SIGNAL IS CHOSEN PER ROW, and the choice is OPERATIONAL rather than a label: whichever probe
answers decides. A row neither probe can see is reported UNSIGNALABLE and never claimed killed.

`/PID` AND `/F`, ONE SLASH. The `//PID` spelling in this build's records is an MSYS *shell* idiom —
the doubling tells bash not to path-mangle the argument. A list argv through `subprocess` does no
such mangling, and `taskkill //PID` from a non-shell exec returns rc 1 with an invalid-option error.
A bash-issued equivalent needs `//`; this one must not.
"""
import os
import shutil
import subprocess
import sys

SIGNAL_TIMEOUT_S = 20


class ReapRefused(RuntimeError):
    """The call may not proceed. Nothing was signalled."""


def resolve_signal_binaries():
    """The two signal paths, RESOLVED. An absent one is reported, never silently substituted."""
    return {"msys": shutil.which("kill"), "native": shutil.which("taskkill")}


def check_msys_addressable(row, binaries):
    """Can MSYS see this row? The probe ANSWERS the question; `kind` only predicts it."""
    if row.get("msys_pid") is None or not binaries.get("msys"):
        return False
    done = subprocess.run([binaries["msys"], "-0", str(row["msys_pid"])],
                          capture_output=True, timeout=SIGNAL_TIMEOUT_S)
    return done.returncode == 0


def build_walk(rows, target):
    """The descendant set of `target`, DEPTH-DESCENDING, target last.

    Leaves first, because killing a parent first is what CREATES the orphans this kit reaps —
    measured, and one test descendant reparented in front of the probe while it happened.

    Over the UNION of both parent graphs, with msys ids translated first, under a VISITED-SET: at
    least one cycle was measured in this union over 337 live rows, so termination is a guarantee
    this walk carries rather than an assumption.
    """
    import scope
    edges, _dropped, _unmapped = scope.build_edges(rows)
    children = {}
    for winpid, parents in edges.items():
        for p in parents:
            children.setdefault(p, set()).add(winpid)

    depth = {target: 0}
    frontier, visited = [target], set()
    while frontier:
        cur = frontier.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for kid in children.get(cur, ()):
            if kid not in depth:
                depth[kid] = depth[cur] + 1
                frontier.append(kid)
    return [w for w, _d in sorted(depth.items(), key=lambda kv: -kv[1])]


def run_kill(target, rows, scope_set, dry_run=False):
    """Kill `target` and its descendants. Returns a report dict; NEVER a bare success.

    The membership test is against the set the fence computed ONCE over the whole census. There is
    no per-member re-derivation here: rev-2 had one, with an inheritance clause that admitted every
    member unconditionally, so the refusal it retained had no reachable failing case.
    """
    by_win = {r["winpid"]: r for r in rows}
    if target not in by_win:
        raise ReapRefused("winpid %s is not in this census — wrong namespace? `run_kill` is keyed "
                          "on winpid, and an MSYS id here resolves to nothing." % target)
    if target not in scope_set:
        raise ReapRefused("winpid %s is not in scope. The walk ROOT is graded before anything is "
                          "walked, so an out-of-scope root refuses the whole call." % target)

    binaries = resolve_signal_binaries()
    walked = build_walk(rows, target)
    dropped = [w for w in walked if w not in scope_set]
    kill_set = [w for w in walked if w in scope_set]

    signalled, unsignalable, errors, already_gone = [], [], [], []
    if not dry_run:
        for winpid in kill_set:
            row = by_win[winpid]
            if check_msys_addressable(row, binaries):
                argv = [binaries["msys"], "-9", str(row["msys_pid"])]
            elif binaries.get("native"):
                # SINGLE-PID, never /T. One slash: a list argv is not shell-mangled.
                argv = [binaries["native"], "/PID", str(winpid), "/F"]
            else:
                unsignalable.append(winpid)
                continue
            done = subprocess.run(argv, capture_output=True, timeout=SIGNAL_TIMEOUT_S)
            if done.returncode != 0:
                # CLASSIFIED, not collapsed. invalid-argument, access-denied and no-such-process
                # are three outcomes and reporting all three the same way is how a wrong-namespace
                # signal hides among ordinary noise.
                #
                # NO-SUCH-PROCESS IS NOT AN ERROR HERE, and measuring the reaper against a real
                # tree is what showed it: killing leaves-first still cascades, so by the time the
                # walk reaches an ancestor its remaining descendants are already gone. A clean
                # 8-of-8 kill reported four "signal errors" until this branch existed, which would
                # have trained an operator to ignore the field that matters.
                blob = (done.stderr or done.stdout or b"").decode("utf-8", "replace").strip()
                if "not found" in blob.lower() or "no such process" in blob.lower():
                    already_gone.append(winpid)
                else:
                    errors.append((winpid, done.returncode, blob[:120]))
            signalled.append(winpid)

    return {
        "target": target,
        "walked": walked,
        "kill_set": kill_set,
        "dropped": dropped,
        "signalled": signalled,
        "unsignalable": unsignalable,
        "errors": errors,
        "already_gone": already_gone,
        "dry_run": dry_run,
    }


def check_survivors(report, rescan):
    """VERIFICATION, from a SECOND census. Never from a signal command's exit status.

    `kill -9` returns success for a signal DELIVERED, and `taskkill /T` printed SUCCESS over one
    death of four. The only honest answer to "did it die" is to look again.
    """
    still = {r["winpid"] for r in rescan}
    report["survivors"] = [w for w in report["kill_set"] if w in still]
    report["killed"] = [w for w in report["kill_set"] if w not in still]
    return report


def render_kill(report):
    out = ["reap: %s target %d · walked %d · in scope %d · dropped %d"
           % ("DRY RUN" if report["dry_run"] else "kill", report["target"],
              len(report["walked"]), len(report["kill_set"]), len(report["dropped"]))]
    if "killed" in report:
        out.append("reap: killed %d · survivors %d · already gone %d · unsignalable %d "
                   "· signal errors %d"
                   % (len(report["killed"]), len(report["survivors"]),
                      len(report.get("already_gone", ())), len(report["unsignalable"]),
                      len(report["errors"])))
    for winpid, rc, msg in report["errors"]:
        out.append("reap:   signal error on %d (rc %d): %s" % (winpid, rc, msg))
    for winpid in report["unsignalable"]:
        out.append("reap:   UNSIGNALABLE %d — neither probe can address it; not claimed killed"
                   % winpid)
    return "\n".join(out)


def run_sweep(root_dir, mode, dry_run, backend=""):
    """The whole chain: census -> fence -> classify -> kill per mode. This unit owns it."""
    import census
    import classify
    import scope as scope_mod

    with open(os.path.join(root_dir, ".process-monitor.conf"), "r",
              encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    ceiling, rate = 14400.0, 0.5
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("PROCMON_AGE_CEILING="):
            ceiling = float(line.split("=", 1)[1].strip().strip("\"'"))
        elif line.startswith("PROCMON_SPIN_RATE="):
            rate = float(line.split("=", 1)[1].strip().strip("\"'"))

    rows, _c = census.scan_processes(backend)
    chain = scope_mod.build_self_chain(rows, os.getpid())
    scope, scope_counts = scope_mod.derive_scope(rows, scope_mod.read_roots(text), chain)
    graded, verdict_counts = classify.scan_verdicts(rows, scope, ceiling, rate)

    wanted = {"report": (), "reap-orphans": ("ORPHAN",),
              "reap-all": ("ORPHAN", "SPIN", "IDLE", "UNKNOWN")}[mode]
    # A self-chain row is in scope and is NOT a kill target.
    targets = [r["winpid"] for r, v in graded
               if v in wanted and scope.get(r["winpid"], {}).get("killable")]

    reports = []
    for winpid in targets:
        try:
            rep = run_kill(winpid, rows, set(scope), dry_run=dry_run)
        except ReapRefused as exc:
            reports.append({"target": winpid, "refused": str(exc)})
            continue
        if not dry_run:
            fresh, _ = census.scan_processes(backend)
            rep = check_survivors(rep, fresh)
        else:
            rep["survivors"] = list(rep["kill_set"])
            rep["killed"] = []
        reports.append(rep)

    counts = {
        "census": len(rows), "scoped": len(scope), "flagged": len(graded),
        "targets": len(targets),
        "killed": sum(len(r.get("killed", ())) for r in reports),
        "survivors": sum(len(r.get("survivors", ())) for r in reports),
        "mode": mode, "dry_run": dry_run,
        "unattributable": scope_counts["unattributable"],
    }
    return graded, reports, counts


def render_sweep(graded, reports, counts):
    out = [classify.render_report(graded, {
        "census": counts["census"], "scoped": counts["scoped"], "flagged": counts["flagged"],
        "orphan": sum(1 for _r, v in graded if v == "ORPHAN"),
        "spin": sum(1 for _r, v in graded if v == "SPIN"),
        "idle": sum(1 for _r, v in graded if v == "IDLE"),
        "unknown": sum(1 for _r, v in graded if v == "UNKNOWN"),
        "ok": 0,
    })]
    for rep in reports:
        out.append(rep["refused"] if "refused" in rep else render_kill(rep))
    out.append("reap: mode %(mode)s%(dry)s · %(targets)d target(s) · %(killed)d killed · "
               "%(survivors)d survivor(s) · %(unattributable)d unattributable row(s) this kit "
               "cannot see" % dict(counts, dry=" (DRY RUN)" if counts["dry_run"] else ""))
    return "\n".join(out)


def main(argv):
    import census
    import classify as _classify  # noqa: F401  (render_sweep uses the module-level import)
    global classify
    classify = _classify
    root_dir = os.environ.get("PROCMON_ROOT", os.getcwd())
    backend = os.environ.get("PROCMON_BACKEND", "")
    dry_run = "--dry-run" in argv
    mode = os.environ.get("PROCMON_REAP_MODE", "")
    if not mode:
        try:
            with open(os.path.join(root_dir, ".process-monitor.conf"), "r",
                      encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    if line.strip().startswith("PROCMON_REAP_MODE="):
                        mode = line.split("=", 1)[1].strip().strip("\"'")
        except OSError as exc:
            sys.stderr.write("reap: REFUSED — %s\n" % exc)
            return 1
    if mode not in ("report", "reap-orphans", "reap-all"):
        sys.stderr.write("reap: REFUSED — PROCMON_REAP_MODE=%r is outside the closed set\n" % mode)
        return 1

    try:
        if "--kill" in argv:
            target = int(argv[argv.index("--kill") + 1])
            rows, _c = census.scan_processes(backend)
            import scope as scope_mod
            with open(os.path.join(root_dir, ".process-monitor.conf"), "r",
                      encoding="utf-8", errors="replace") as fh:
                text = fh.read()
            chain = scope_mod.build_self_chain(rows, os.getpid())
            scope, _sc = scope_mod.derive_scope(rows, scope_mod.read_roots(text), chain)
            # The explicit path bypasses the MODE, never the FENCE.
            rep = run_kill(target, rows, set(scope), dry_run=dry_run)
            if not dry_run:
                fresh, _ = census.scan_processes(backend)
                rep = check_survivors(rep, fresh)
            print(render_kill(rep))
            return 1 if rep.get("survivors") else 0
        graded, reports, counts = run_sweep(root_dir, mode, dry_run, backend)
    except (ReapRefused, OSError, ValueError) as exc:
        sys.stderr.write("reap: REFUSED — %s\n" % exc)
        return 1
    except Exception as exc:  # a census or scope refusal
        sys.stderr.write("reap: REFUSED — %s\n" % exc)
        return 1
    print(render_sweep(graded, reports, counts))
    # A survivor is precisely the state a human must see, and the state this build was opened over.
    return 1 if counts["survivors"] else 0


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(sys.argv[1:]))
