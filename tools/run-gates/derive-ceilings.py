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
# with the rest of a full bar. Sized against what this repo has recorded rather than against
# comfort: the worst overshoot on record is 0.481 s and the worst single process spawn measured on
# a degraded node is 1.297 s (TOOL-aMeteredTurnstile-6). Widening this buys margin nothing has
# needed and widens the inert-host band `read_runs` discloses; tightening it silently discards the
# readings this filter exists to admit.
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


def read_runs(gd: pathlib.Path, legs: dict) -> dict:
    """Every recorded reading per leg, from the per-run leg files. Returns {name: [seconds, ...]}.

    THE ADMISSION RULE. An `ok` row counts at any duration, because a completed run measured the
    work whatever bound was or was not in force around it. A NON-`ok` row counts only when its
    seconds land inside the CLOSED WINDOW `[ceiling, ceiling + CEILING_WINDOW_S]`, against the
    ceiling the leg manifest declares for that leg TODAY: that is a run the ceiling itself
    stopped, so its seconds are a LOWER BOUND on the work, which is the one property a monotone
    maximum needs and the property `ok` rows are admitted for. Every other failing row stays
    excluded — a leg that failed fast measures the failure and not the work, and a maximum that
    admits it holds a ceiling above a number nothing did. A leg with no integer ceiling admits
    `ok` rows only, because there is nothing for a failing row to have reached. `legs` is
    `read_legs`'s map and is REQUIRED rather than defaulted: a defaulted ceilings map is how one
    call site keeps the old `ok`-only behaviour while every other criterion still passes green.

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
    """
    per: dict[str, list[float]] = {}
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
                ceiling = (legs.get(p[0]) or {}).get("ceiling")
                if not isinstance(ceiling, int):
                    continue
                if not ceiling <= secs <= ceiling + CEILING_WINDOW_S:
                    continue
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
    runs = read_runs(gd, legs)
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
        if over is None:
            state = "no-ceiling"
        elif over < need:
            state = "UNDER"          # the ceiling does not clear the evidenced max by the headroom
        print(f"{name}\t{mx:.1f}\t{len(vals)}\t{ceiling}\t"
              f"{('%.0f' % over) if over is not None else '-'}\t{need:.0f}\t{state}")
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
    # THE CEILINGS ARE READ HERE TOO, and this call is the whole of a criterion. `read_runs`'s
    # admission rule compares against them, and this is the only path that produces the tracked
    # artifact — a write path still holding an `ok`-only filter is invisible to `--check`, which
    # reads no run file at all.
    runs = read_runs(gd, read_legs(root))
    if not runs:
        print("derive-ceilings: DEAD PROBE — no readings to write.", file=sys.stderr)
        return 2
    have = read_evidence()
    node = os.environ.get("GOV_NODE") or "a"
    date = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%cs"],
                          capture_output=True, text=True).stdout.strip() or "unknown"
    rows, raised, held = {}, 0, 0
    for name, vals in runs.items():
        mx = max(vals)
        prev = have.get(name)
        if prev and prev[0] >= mx and name not in (args.reset or []):
            rows[name] = prev
            held += 1
        else:
            rows[name] = (mx, len(vals), node, date)
            if prev:
                raised += 1
    for name, prev in have.items():                     # rows this run measured nothing for
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
          f"({raised} raised, {held} held at a previous maximum)")
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
                    help="with --write, allow this leg's row to LOWER")
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
