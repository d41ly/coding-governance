#!/usr/bin/env python3
"""derive-ceilings.py — make a leg's ceiling arguable. TOOL-aQuenchedHarness-2.

Ninety-four ceilings sit in `tools/gate-legs.json` with no evidence beside them, so nobody can tell a
bound that was measured from one that was raised to make a leg stop complaining. This verb reads what
the runner already records and puts a number beside each one.

WHAT IT DOES NOT DO, first, because the obvious reading is wrong: it does NOT tighten ceilings. This
build measured the same leg varying 5.5x median and 47.1x worst across readings on one node, so the
current ~10x values sit between the p75 and the p90 of the observed load spread. A tighter bound
would red healthy legs, which `TOOL-dRetiredFork-40` records as strictly worse than a loose one. What
is missing is not tightness, it is EVIDENCE.

THE READING SOURCE IS `gate-run`, NOT THE LEDGER. `<git-dir>/gate-ledger.tsv` keeps exactly ONE row
per leg -- it is rebuilt and moved over on every run -- so it holds no history at all, and a rev of
this spec that derived a per-leg spread from it had an empty population by construction.
`<git-dir>/gate-run/<runid>/<i>.leg` keeps one file per leg PER RUN, several runs retained, which is
the history. Fields, from the runner: name, status, rc, seconds, started, ended, key.

THE GATE READS TRACKED FILES ONLY. Both `gate-run` and the ledger are untracked, per-worktree and
node-local -- measured, 46 rows in one worktree against 96 in the primary -- so a leg whose verdict
depended on them would give the same tree different answers on different machines. `--write` distils
them into `ceiling-evidence.txt`, which IS tracked, and `--check` compares that against
`gate-legs.json` and nothing else. Charter section 12's committed-artifact-plus-parity shape.
"""
import argparse
import glob
import json
import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
EVIDENCE = HERE / "ceiling-evidence.txt"
MARGIN_FILE = HERE / "ceiling-margin.txt"

# How far ABOVE its declared ceiling a failing reading may sit and still be admitted as evidence.
# 5 s of it is arithmetic: `run-gates.sh` wraps a bounded leg in `timeout -k 5s "$bound"`, so
# SIGKILL lands five seconds after SIGTERM and nothing the leg decides can put its death later.
# The other 30 s is a teardown allowance — `runleg` stamps its end time after `cat`-ing the leg's
# output, so a file read and a `date` spawn sit inside the measured seconds, all of it competing
# with the rest of a full bar.
#
# NO OVERSHOOT FIGURE IS WRITTEN HERE, deliberately. `run-gates.sh`'s rc=124 block owns that
# measurement and states it beside the code that produces it, and `run-gates.test.sh` arm 1c owns
# the reading it was taken from; a copy of the number in this comment would be a second answer to
# one question and the copy is what rots. Read it there. What this comment owns is the SIZING
# ARGUMENT over it: the overhead is a FIXED cost — arm 1c's own words are that it "does NOT shrink
# when the sleeper does" — so a teardown allowance has to clear the largest ABSOLUTE overshoot on
# record rather than the largest one relative to its ceiling. THE MAGNITUDE IS NOT PARAPHRASED HERE
# EITHER, and that is the same ban one level down: the first cut of this comment sized the worst
# reading in words instead of copying it, understated it, and stood beside the two sources it was
# understating. An adjective is the same second answer to one question that a numeral would be.
# Read the size at those sources. Widening this widens the inert-host band `read_runs` discloses;
# tightening it silently discards the readings this filter exists to admit.
#
# WRITTEN AS A SUM, so the two halves are stated once each and the total is derived. A literal 35
# beside a comment saying "5 plus 30" is two answers to one question, and the comment is the copy
# that rots.
CEILING_WINDOW_S = 5 + 30


def resolve_repo_root() -> pathlib.Path:
    out = subprocess.run(["git", "-C", str(HERE), "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit("derive-ceilings: not a git work tree")
    return pathlib.Path(out.stdout.strip())


def resolve_git_dir(root: pathlib.Path) -> pathlib.Path:
    out = subprocess.run(["git", "-C", str(root), "rev-parse", "--git-dir"],
                         capture_output=True, text=True)
    return pathlib.Path(out.stdout.strip()) if out.returncode == 0 else root / ".git"


def read_legs(root: pathlib.Path) -> dict:
    p = root / "tools" / "gate-legs.json"
    return {l["name"]: l for l in json.loads(p.read_text(encoding="utf-8"))}


def read_margin() -> tuple[int, float, str]:
    """The declared headroom: a FLOOR in seconds and a FRACTION of the evidenced maximum.

    Required headroom is `max(floor, fraction * max)`. BOTH halves are needed and running the first
    cut proved it: a flat floor alone forces every ceiling above the floor, so a 2.2 s leg with a
    300 s ceiling -- 136x headroom -- read UNDER against a 1800 s margin. A fraction alone gives a
    2.2 s leg 2.2 s of headroom, which any scheduling hiccup crosses.

    This is NOT the multiplier `TOOL-dRetiredFork-40` rejected. That row rejected predicting a
    LOADED reading from a QUIET one by multiplying, because the relationship is not a multiplier --
    it measured 443 s under load against 583 s quiet, the wrong way round. Here the input is already
    the worst OBSERVED reading, and the fraction only sizes headroom above it.

    A MISSING file is a refusal, never a default. Headroom nobody wrote is headroom nobody decided.
    """
    if not MARGIN_FILE.is_file():
        sys.exit(f"derive-ceilings: no margin declared at {MARGIN_FILE.name} — a bound with an "
                 f"undeclared margin is a number nobody chose. Refusing rather than defaulting.")
    for line in MARGIN_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        f = [x.strip() for x in s.split("\t")]
        if len(f) >= 2 and f[0].isdigit():
            try:
                return int(f[0]), float(f[1]), s
            except ValueError:
                continue
    sys.exit(f"derive-ceilings: {MARGIN_FILE.name} declares no "
             f"<floor seconds>, tab, <fraction> row")


def read_runs(gd: pathlib.Path, legs: dict, reset) -> dict:
    """Every recorded reading per leg, from the per-run leg files. Returns {name: [seconds, ...]}.

    THE ADMISSION RULE. An `ok` row counts at any duration, because a completed run measured the
    work whatever bound was or was not in force around it. A NON-`ok` row counts only when its
    seconds land inside the CLOSED WINDOW `[ceiling, ceiling + CEILING_WINDOW_S]`, against the
    ceiling the leg manifest declares for that leg TODAY: that is a run the ceiling itself
    stopped, so the CEILING is a LOWER BOUND on the work, which is the one property a monotone
    maximum needs and the property `ok` rows are admitted for. Every other failing row stays
    excluded — a leg that failed fast measures the failure and not the work, and a maximum that
    admits it holds a ceiling above a number nothing did. A leg with no integer ceiling admits
    `ok` rows only, because there is nothing for a failing row to have reached. `legs` is
    `read_legs`'s map and is REQUIRED rather than defaulted: a defaulted ceilings map is how one
    call site keeps the old `ok`-only behaviour while every other criterion still passes green.

    AN ADMITTED FAILING ROW ENTERS AT ITS CEILING, NOT AT ITS ELAPSED SECONDS. Only the ceiling is
    provable: the leg was killed there, and `run-gates.sh`'s own rc=124 block states that the
    elapsed value on that path is the ceiling PLUS kill-path overhead. Storing the raw elapsed
    number asserts that the work took it, which nothing measured, and this file is MONOTONE, so
    that assertion never comes back down and permanently inflates the headroom `--check` demands.
    `min(secs, ceiling)` stores exactly the property the paragraph above claims and drops the
    teardown noise, without touching which rows are admitted.

    THE WINDOW IS CLOSED AT BOTH ENDS, and the upper edge carries as much of the rule as the lower.
    `seconds >= ceiling` proves the bound expired only where the ceiling WAS the bound, and two
    states break that. A host whose `CEILINGS_LIVE` probe fails runs every leg UNBOUNDED, and the
    `.leg` row carries no bound field, so a leg that ran far past its ceiling and failed on its own
    would enter a MONOTONE file as though a bound had stopped it. A ceiling edited after a row was
    recorded breaks it the same way, since the comparison uses today's manifest against a
    historical run. A reading materially above its ceiling is itself evidence that no such bound
    produced it. What survives is a residual band the width of the window on such a host.

    WHAT THIS CANNOT TELL APART, because the record holds one signature for all three: a leg that
    is merely slow, a leg that was contended by its neighbours on a wide bar, and a leg that hung.
    The runner records nothing that would separate them — no pool width, no neighbour count, no
    bound. The evidence file is MONOTONE, so a contended or hung reading admitted once holds a
    floor under that ceiling until somebody lowers it, and lowering one is `--write --reset <leg>`,
    which exists for exactly this and records that somebody chose it.

    `reset` IS THAT ESCAPE, AND IT ACTS HERE RATHER THAN ON THE MONOTONE HOLD ALONE. A named leg
    admits its `ok` readings ONLY, so the reset re-derives from the runs where the leg finished and
    the killed reading stops counting. Bypassing the hold and nothing else made `--reset` INERT for
    the whole `GATE_RUN_KEEP` window — `max(vals)` was re-derived from the same retained rows and
    the identical value went straight back — which is precisely the window an operator reaches for
    it in, since the offending run is what put the row there. A named leg with no `ok` reading at
    all yields nothing here and `cmd_write` then DROPS its row rather than carrying the old one
    forward: an escape that silently restored the value it was asked to clear would be worse than
    one that does nothing, because it looks like it worked. `reset` is REQUIRED rather than
    defaulted, for the reason `legs` is.
    """
    per: dict[str, list[float]] = {}
    reset = set(reset or ())
    for f in glob.glob(str(gd / "gate-run" / "*" / "*.leg")):
        try:
            txt = pathlib.Path(f).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line in txt.splitlines():
            p = line.split("\t")
            if len(p) < 4:
                continue
            try:
                secs = float(p[3])
            except ValueError:
                continue
            if p[1] != "ok":
                if p[0] in reset:
                    continue
                ceiling = (legs.get(p[0]) or {}).get("ceiling")
                if not isinstance(ceiling, int):
                    continue
                if not ceiling <= secs <= ceiling + CEILING_WINDOW_S:
                    continue
                secs = min(secs, float(ceiling))
            per.setdefault(p[0], []).append(secs)
    return per


def read_evidence() -> dict:
    """The tracked artifact: {name: (max_seconds, readings, node, date)}."""
    out: dict[str, tuple[float, int, str, str]] = {}
    if not EVIDENCE.is_file():
        return out
    for line in EVIDENCE.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        f = line.split("\t")
        if len(f) < 5:
            continue
        try:
            out[f[0]] = (float(f[1]), int(f[2]), f[3], f[4])
        except ValueError:
            continue
    return out


def cmd_report(root, gd, args) -> int:
    legs = read_legs(root)
    runs = read_runs(gd, legs, args.reset)
    floor, frac, mline = read_margin()
    if not runs:
        print(f"derive-ceilings: DEAD PROBE — no readings under {gd}/gate-run/. Nothing was "
              f"measured, so nothing below would be evidence. Run a bar first; a report over an "
              f"empty population is not a small report, it is a false one.", file=sys.stderr)
        return 2
    print(f"# headroom max({floor}s, {frac} x max) — {mline}")
    print(f"# {len(runs)} leg(s) with a reading, over {len(set(os.path.dirname(f) for f in glob.glob(str(gd / 'gate-run' / '*' / '*.leg'))))} retained run(s)")
    print("# leg\tmax_s\treadings\tceiling\thave\tneed\tstate")
    unbacked = []
    for name in sorted(legs):
        ceiling = legs[name].get("ceiling")
        vals = runs.get(name) or []
        if not vals:
            unbacked.append(name)
            continue
        mx = max(vals)
        need = max(floor, frac * mx)
        over = (ceiling - mx) if isinstance(ceiling, int) else None
        state = "ok"
        # THE REACHED BRANCH IS `cmd_check`'s, ON THE SAME CONDITION AND FROM THE SAME TWO VALUES.
        # This is the table an operator actually sizes a ceiling FROM, so it is the reader that
        # most needs to be told a reading is a LOWER BOUND on the work rather than its duration —
        # and it was the one left saying `UNDER` with a `need` target beside it, which is the
        # invitation the sibling reader was amended to withdraw. `have` and `need` print as `-`
        # here for the same reason: there is no headroom to state above a number the work merely
        # got to, and an arithmetic target offered against one is a sizing instruction.
        if over is None:
            state = "no-ceiling"
        elif mx >= ceiling:
            state = "REACHED"
        elif over < need:
            state = "UNDER"          # the ceiling does not clear the evidenced max by the headroom
        cells = ("-", "-") if state == "REACHED" else (
            ("%.0f" % over) if over is not None else "-", "%.0f" % need)
        print(f"{name}\t{mx:.1f}\t{len(vals)}\t{ceiling}\t{cells[0]}\t{cells[1]}\t{state}")
    # REPORTED, never silent: a leg with no reading is a leg whose ceiling nothing supports, and it
    # is a different state from a leg whose ceiling is wrong.
    if unbacked:
        print(f"# {len(unbacked)} leg(s) UNBACKED — declared a ceiling, measured nothing: "
              f"{', '.join(sorted(unbacked)[:6])}{' …' if len(unbacked) > 6 else ''}",
              file=sys.stderr)
    return 0


def cmd_write(root, gd, args) -> int:
    """Refresh the tracked evidence. MONOTONE: a row only ever rises.

    `gate-run` retains a handful of runs, so a pruned or quiet window would otherwise LOWER an
    evidenced maximum and, with it, the floor the gate holds every ceiling above. Lowering takes
    `--reset <leg>`, which records that somebody chose it.
    """
    reset = set(args.reset or ())
    # THE CEILINGS ARE READ HERE TOO, and this call is the whole of a criterion. `read_runs`'s
    # admission rule compares against them, and this is the only path that produces the tracked
    # artifact — a write path still holding an `ok`-only filter is invisible to `--check`, which
    # reads no run file at all. `reset` goes the same way and for the same reason: bypassing the
    # monotone hold below cannot lower anything while the run that produced the reading is still
    # retained, because `max(vals)` is re-derived from it.
    runs = read_runs(gd, read_legs(root), reset)
    if not runs:
        print("derive-ceilings: DEAD PROBE — no readings to write.", file=sys.stderr)
        return 2
    have = read_evidence()
    node = os.environ.get("GOV_NODE") or "a"
    date = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%cs"],
                          capture_output=True, text=True).stdout.strip() or "unknown"
    rows, raised, held, lowered = {}, 0, 0, 0
    for name, vals in runs.items():
        mx = max(vals)
        prev = have.get(name)
        if prev and prev[0] >= mx and name not in reset:
            rows[name] = prev
            held += 1
        else:
            rows[name] = (mx, len(vals), node, date)
            if prev and mx < prev[0]:
                lowered += 1
            elif prev:
                raised += 1
    dropped = 0
    for name, prev in have.items():                     # rows this run measured nothing for
        # A RESET LEG IS NOT CARRIED FORWARD. Reaching here with one means every reading it had was
        # the killed one the reset was asked to discard, so restoring the old row would hand back
        # exactly the value the operator was clearing while printing that the reset ran. The row
        # goes, the leg reads UNBACKED — which `--check` reports and does not fail on — and the
        # next ordinary `--write` re-derives it once the window holds a finished run.
        if name in reset:
            if name not in rows:                        # COUNTED ONLY WHEN A ROW ACTUALLY WENT:
                dropped += 1                            # a reset leg that kept `ok` readings was
            continue                                    # re-derived, not dropped
        rows.setdefault(name, prev)
    lines = [
        "# ceiling-evidence.txt — the recorded maximum per gate leg, TRACKED so a gate can read it.",
        "#",
        "# GENERATED by `python tools/run-gates/derive-ceilings.py --write` from",
        "# `<git-dir>/gate-run/*/*.leg`, which keeps one file per leg per run. Do not hand-edit: a",
        "# row here is a claim about a measurement, and one typed by hand is a claim about nothing.",
        "#",
        "# MONOTONE. A row only ever rises. `gate-run` retains a handful of runs, so a quiet window",
        "# would otherwise lower the evidenced maximum and with it the floor every ceiling is held",
        "# above. `--reset <leg>` lowers one, and that is a decision somebody made.",
        "#",
        "# <leg>\t<max seconds>\t<readings>\t<node>\t<date>",
    ]
    for name in sorted(rows):
        mx, n, nd, dt = rows[name]
        lines.append(f"{name}\t{mx:.1f}\t{n}\t{nd}\t{dt}")
    EVIDENCE.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"derive-ceilings: wrote {len(rows)} row(s) to {EVIDENCE.name} "
          f"({raised} raised, {lowered} lowered by --reset, {dropped} dropped by --reset, "
          f"{held} held at a previous maximum)")
    return 0


def cmd_check(root, gd, args) -> int:
    """The gate. TWO TRACKED FILES and nothing else, so the verdict is a property of the tree."""
    legs = read_legs(root)
    ev = read_evidence()
    floor, frac, _ = read_margin()
    if not ev:
        print(f"derive-ceilings: UNMEASURED — {EVIDENCE.name} is absent or empty, so no ceiling "
              f"here is backed by anything. This is not a clean run: run `--write` on a tree that "
              f"has executed a bar.", file=sys.stderr)
        return 1
    bad, unbacked, stale = [], [], []
    for name, leg in legs.items():
        ceiling = leg.get("ceiling")
        row = ev.get(name)
        if row is None:
            unbacked.append(name)
            continue
        if not isinstance(ceiling, int):
            bad.append(f"{name}: no ceiling declared, but {row[0]:.1f}s is recorded")
            continue
        need = max(floor, frac * row[0])
        # A REACHED ceiling is a strict sub-case of the headroom failure below — required headroom
        # never drops under the floor — so this branch changes no verdict, only the sentence. It
        # exists because the headroom arithmetic reads as an invitation to size a new ceiling from
        # the evidenced maximum, and a reading AT a ceiling is a lower bound on the work rather
        # than its cost. Derived at check time from the two tracked files, so there is no stored
        # flag to keep fresh and no way for the message to disagree with the row.
        if row[0] >= ceiling:
            bad.append(f"{name}: ceiling {ceiling}s was REACHED in a recorded run at "
                       f"{row[0]:.1f}s — that reading is a LOWER BOUND on the work and not its "
                       f"duration, so do not size a new ceiling from it")
        elif ceiling < row[0] + need:
            bad.append(f"{name}: ceiling {ceiling}s does not clear its evidenced maximum "
                       f"{row[0]:.1f}s by the required max({floor}s, {frac}x) = {need:.0f}s "
                       f"(short by {row[0] + need - ceiling:.0f}s)")
    for name in ev:
        if name not in legs:
            stale.append(name)
    # A STALE ROW IS REPORTED AND DOES NOT FAIL. It cannot make a bound wrong; what it can do is
    # quietly widen a file written to narrow something, which is why it is named.
    for s in stale:
        print(f"derive-ceilings: evidence row '{s}' names a leg the manifest no longer carries",
              file=sys.stderr)
    if unbacked:
        print(f"derive-ceilings: {len(unbacked)} of {len(legs)} leg(s) have no evidence row — their "
              f"ceilings are unbacked, which is REPORTED and not a failure: a leg that has never "
              f"run has nothing to be measured against.", file=sys.stderr)
    if bad:
        for b in bad:
            print(f"CEILING-EVIDENCE FAILED — {b}", file=sys.stderr)
        return 1
    print(f"ceiling-evidence: {len(legs) - len(unbacked)} of {len(legs)} leg(s) backed, every one "
          f"clearing its evidenced maximum by max({floor}s, {frac} x max)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--report", action="store_true", help="print the ceiling-vs-recorded table")
    g.add_argument("--write", action="store_true", help="refresh the tracked evidence file")
    g.add_argument("--check", action="store_true", help="the gate: tracked files only")
    ap.add_argument("--reset", action="append", metavar="LEG",
                    help="re-derive this leg from its `ok` readings alone, so a killed reading "
                         "stops holding a floor under its ceiling; with --write it also lifts the "
                         "monotone hold, and drops the row entirely when no `ok` reading remains")
    args = ap.parse_args()
    root = resolve_repo_root()
    gd = resolve_git_dir(root)
    if not gd.is_absolute():
        gd = root / gd
    if args.report:
        return cmd_report(root, gd, args)
    if args.write:
        return cmd_write(root, gd, args)
    return cmd_check(root, gd, args)


if __name__ == "__main__":
    raise SystemExit(main())
