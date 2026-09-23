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

A READING TAKEN OUTSIDE THE RUNNER IS ADMISSIBLE, AND HAS TO BE (TOOL-cMendedVintage-17). The
mechanism above raises a row from the evidence of a COMPLETED run, and a leg killed at its ceiling
never completes one: the retained record holds the kill row, that row enters at the ceiling, and the
ceiling therefore holds a floor under itself. The mechanism cannot reach exactly the legs that most
need it. It was broken by hand twice -- two healthy legs measured quiet, two ceilings edited from
numbers nothing in the tree recorded -- and a hand-edit is what `--observed` replaces.

  GOV_NODE=<tag> ... --write --observed '<leg>=<seconds>' --how '<how it was taken>'

A FLAG, not a second tracked file and not a forged run row. A run row would make the reading
indistinguishable from one the runner saw, which is the exact failure the margin file's header
names; a second tracked file would be a new artifact to keep in step with this one, plus its own
registry row, to hold what one command already writes. The flag leaves the claim in the same
tracked artifact, in a commit, beside the rows it has to be told apart from.

WHICH IT IS, IN THE ARTIFACT: a sixth column carrying the SOURCE. An in-band row spells the literal
`runner`; an out-of-band row spells the operator's own `--how` text, so the provenance travels with
the number rather than beside it. `--check` names those legs separately for the same reason. The
node is REFUSED rather than defaulted here, because a reading whose stated node is wrong is worse
evidence than no reading.

`--report` is untouched and still reads the retained runs alone, so a leg raised by `--observed`
shows there whatever its RUN record says -- REACHED where the kill row is still retained, UNBACKED
where nothing is. That is the truth about the run record and it stays that. The number the gate
consumes is the tracked one, and `--check` is the reader that reports it.
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

# The SOURCE column's value for a row this tool derived from the runner's own record. Anything else
# in that column is the `--how` text of a reading taken outside it, which is what makes the two
# tellable apart by a reader with no access to the run record. A row written before the column
# existed reads as this value, because every one of them was runner-derived.
RUNNER_SOURCE = "runner"


def resolve_repo_root() -> pathlib.Path:
    out = subprocess.run(["git", "-C", str(HERE), "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True, encoding="utf-8")
    if out.returncode != 0:
        sys.exit("derive-ceilings: not a git work tree")
    return pathlib.Path(out.stdout.strip())


def resolve_git_dir(root: pathlib.Path) -> pathlib.Path:
    out = subprocess.run(["git", "-C", str(root), "rev-parse", "--git-dir"],
                         capture_output=True, text=True, encoding="utf-8")
    return pathlib.Path(out.stdout.strip()) if out.returncode == 0 else root / ".git"


def read_legs(root: pathlib.Path) -> dict:
    # The manifest is this kit dir's SIBLING and GATE_LEGS outranks it, as in run-gates.sh (S1).
    beside = pathlib.Path(__file__).resolve().parent.parent / "gate-legs.json"
    p = pathlib.Path(os.environ.get("GATE_LEGS") or beside)
    p = p if p.is_absolute() else root / p
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

    `reset` IS THAT ESCAPE, AND WHAT IT DOES HERE IS THE PREVIEW OF IT, NOT THE DISCARD. A named
    leg admits its `ok` readings ONLY, so the reset re-derives from the runs where the leg finished
    and the killed reading stops counting. THAT FILTER LASTS ONE INVOCATION, which is the whole of
    what `--report --reset` needs and is NOT enough on the write path. Two revisions of this escape
    were inert in two different ways: bypassing the monotone hold alone re-derived the identical
    value from the same retained rows, and adding this filter beside it moved the inertness one
    step later rather than removing it — the next plain `--write` re-admitted those same rows,
    `max(vals)` handed the cleared value straight back, and the summary line called it `1 raised`.
    Measured on a fixture: 100.0 -> 20.0 -> 100.0. So `cmd_write` takes those rows OUT of the
    retained run files as well (`remove_reset_rows`), and the discard outlives the process that
    chose it — which is the only version of this escape an operator can reach for inside the
    `GATE_RUN_KEEP` window, and that window is the only one they ever reach for it in, since the
    offending run is what put the row there. A named leg with no `ok` reading at all yields nothing
    here and `cmd_write` then DROPS its row rather than carrying the old one forward: an escape
    that silently restored the value it was asked to clear would be worse than one that does
    nothing, because it looks like it worked. `reset` is REQUIRED rather than defaulted, for the
    reason `legs` is.
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


def remove_reset_rows(gd: pathlib.Path, reset) -> int:
    """Take the reset legs' non-`ok` rows OUT of the retained run files. Returns rows removed.

    THIS IS WHAT MAKES `--reset` STICK, and without it the escape is inert one `--write` later.
    `read_runs`'s filter is per-invocation; the `.leg` file holding the killed reading stays in the
    `GATE_RUN_KEEP` window, so the very next ordinary `--write` re-admits it and the monotone
    maximum restores the floor the operator just cleared. Deleting the row is what "somebody chose
    it" has to mean: these files are UNTRACKED, per-worktree, node-local scratch — the same
    property the module docstring gives as the reason a gate may not read them — and a discard that
    expires with the process is not a discard.

    ROWS, NOT FILES, and only the ones the reset names: `run-gates.sh` writes one row per file, but
    a file may carry several (a fixture does), and a reset leg's `ok` readings are exactly what the
    escape re-derives from. A file left with nothing is removed, since an empty `.leg` is a row
    nobody wrote. Every retained run but one is read by nothing except this module.

    THE ONE IT DOES NOT EXEMPT IS THE RUN IN FLIGHT, and that is a choice rather than an oversight.
    `run-gates.sh` re-reads its OWN `<RUNDIR>/<i>.leg` at ledger time, so a reset racing a live bar
    can take a row out from under it and leave that leg recorded as `ok` with no reuse key. The
    obvious guard — skip the directory `gate-run/current` names — is worse than the race: `current`
    survives the run that wrote it, so the exemption would fall on the most RECENTLY finished run,
    which is precisely the run whose killed reading an operator is resetting, and the escape would
    be inert again for the only case it exists for. The race needs two deliberate concurrent
    gestures on one worktree; the exemption would break the single one.

    A row that cannot be rewritten is NOT counted. The count is the operator's only evidence that
    the scratch record actually moved, and one that included a failed `unlink` would be the same
    could-not-fail shape as the summary line this fold is repairing.
    """
    reset = set(reset or ())
    if not reset:
        return 0
    gone = 0
    for f in glob.glob(str(gd / "gate-run" / "*" / "*.leg")):
        p = pathlib.Path(f)
        try:
            lines = p.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        # THE SAME PARSE `read_runs` USES, deliberately: a row this module would not read is a row
        # it has no business deleting, so a short or malformed line survives a reset untouched.
        keep = [ln for ln in lines
                if not (len(ln.split("\t")) >= 4
                        and ln.split("\t")[0] in reset and ln.split("\t")[1] != "ok")]
        if len(keep) == len(lines):
            continue
        try:
            if keep:
                p.write_text("\n".join(keep) + "\n", encoding="utf-8", newline="\n")
            else:
                p.unlink()
        except OSError:
            continue
        gone += len(lines) - len(keep)
    return gone


def read_evidence() -> dict:
    """The tracked artifact: {name: (max_seconds, readings, node, date, source)}.

    A FIVE-FIELD ROW READS AS `runner`, which is a fact about the corpus rather than a default
    chosen for convenience: the source column arrives with `--observed` and every row written
    before it was derived from the run record. Refusing a short row instead would empty the
    artifact on the upgrade commit and red the gate for a reason that is not a ceiling's.
    """
    out: dict[str, tuple[float, int, str, str, str]] = {}
    if not EVIDENCE.is_file():
        return out
    for line in EVIDENCE.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        f = line.split("\t")
        if len(f) < 5:
            continue
        try:
            out[f[0]] = (float(f[1]), int(f[2]), f[3], f[4],
                         f[5] if len(f) >= 6 and f[5].strip() else RUNNER_SOURCE)
        except ValueError:
            continue
    return out


def parse_observed(spec: str, how: str, legs: dict) -> tuple[str, float]:
    """`<leg>=<seconds>` plus the conditions it was taken under. Every refusal here is a REFUSAL.

    Nothing below defaults. A reading admitted with a leg name nobody checked, a duration that is
    not one, or an empty account of how it was taken is a number in a tracked file with no claim
    attached, which is the hand-edit this verb exists to replace wearing a command's clothes.

    THE TAB AND THE NEWLINE ARE STRUCTURE, not taste: the artifact is tab-separated and the `--how`
    text is the last field on its row, so either byte inside it forges a column or a row.
    """
    name, sep, raw = spec.partition("=")
    name = name.strip()
    if not sep or not name:
        sys.exit(f"derive-ceilings: --observed wants '<leg>=<seconds>', got {spec!r}")
    try:
        secs = float(raw.strip())
    except ValueError:
        sys.exit(f"derive-ceilings: --observed seconds {raw.strip()!r} is not a number")
    if secs <= 0:
        sys.exit(f"derive-ceilings: --observed seconds {secs} is not a duration")
    if name not in legs:
        sys.exit(f"derive-ceilings: --observed names '{name}', which the leg manifest does not "
                 f"carry — a reading for a leg that does not exist backs nothing")
    if not how or not how.strip():
        sys.exit("derive-ceilings: --observed needs --how '<how the reading was taken>' — a "
                 "reading with no stated conditions is the hand-edit this flag replaces")
    if "\t" in how or "\n" in how:
        sys.exit("derive-ceilings: --how may not carry a tab or a newline — the artifact is "
                 "tab-separated and this text is a field in it")
    return name, secs


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
    `--reset <leg>`, which records that somebody chose it — and, here, MAKES it stick by removing
    the discarded readings from the retained run files rather than filtering them for one process.
    """
    reset = set(args.reset or ())
    legs = read_legs(root)
    # THE LIVENESS QUESTION IS ASKED WITHOUT THE RESET FILTER, and the two are different questions.
    # "Is there any reading at all" is what DEAD PROBE answers; "what survives the reset" is what
    # the write consumes. Asking the second and printing the first misdiagnosed the one state this
    # verb exists for: a reset naming the only leg with a reading emptied the map, and the early
    # return fired forty lines above the drop path documented below, so the run exited 2 saying
    # nothing was measured — of readings it had just excluded itself — and the stale row survived.
    live = read_runs(gd, legs, ())
    # AN `--observed` READING IS ITSELF A READING, so it satisfies liveness on its own. The state
    # this flag exists for is a run record holding nothing admissible for the leg being raised — a
    # leg killed at its ceiling contributes only that ceiling back — and on a fresh worktree it
    # holds nothing at all. A DEAD PROBE return above the flag would refuse the one case it was
    # built for, which is the shape `read_runs`'s own liveness split was already repaired once for.
    if not live and not args.observed:
        print("derive-ceilings: DEAD PROBE — no readings to write.", file=sys.stderr)
        return 2
    # THE DISCARD IS PERSISTED BEFORE THE READ, so nothing downstream can re-admit it. `read_runs`
    # is still passed `reset` below: it is the belt for a row this call could not rewrite, and it
    # is what `--report --reset` previews with.
    removed = remove_reset_rows(gd, reset)
    # THE CEILINGS ARE READ HERE TOO, and this call is the whole of a criterion. `read_runs`'s
    # admission rule compares against them, and this is the only path that produces the tracked
    # artifact — a write path still holding an `ok`-only filter is invisible to `--check`, which
    # reads no run file at all.
    runs = read_runs(gd, legs, reset) if reset else live
    have = read_evidence()
    node = os.environ.get("GOV_NODE") or "a"
    date = subprocess.run(["git", "-C", str(root), "log", "-1", "--format=%cs"],
                          capture_output=True, text=True, encoding="utf-8").stdout.strip() or "unknown"
    rows, raised, held, lowered = {}, 0, 0, 0
    for name, vals in runs.items():
        mx = max(vals)
        prev = have.get(name)
        if prev and prev[0] >= mx and name not in reset:
            rows[name] = prev
            held += 1
        else:
            rows[name] = (mx, len(vals), node, date, RUNNER_SOURCE)
            # TALLIED ON MOVEMENT, never on which branch got here. A reset leg whose re-derived
            # maximum EQUALS the stored one lands in this branch because `name not in reset` forced
            # it out of the hold, and the old `elif prev` then reported `1 raised` for a row that
            # did not move — work nobody did, printed in the only line `--write` gives an operator,
            # and printed in answer to the gesture they make when the first reset appeared not to
            # stick. Equal is `held`: the value is the previous maximum, whatever the row's other
            # fields were refreshed to.
            if prev and mx < prev[0]:
                lowered += 1
            elif prev and mx > prev[0]:
                raised += 1
            elif prev:
                held += 1
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
    observed = 0
    if args.observed:
        # THE NODE IS REFUSED RATHER THAN DEFAULTED, and only here. A runner-derived row's node is
        # a statement about the machine that just ran the bar, and `GOV_NODE or "a"` is wrong there
        # at worst by a tag. An out-of-band row's node is half of what makes the number evidence —
        # the reading was taken somewhere, under conditions that machine had — so a defaulted tag
        # is a false claim about provenance, which is worse than having no row.
        obs_node = os.environ.get("GOV_NODE")
        if not obs_node:
            print("derive-ceilings: --observed needs GOV_NODE set to the node the reading was "
                  "taken on. The node is evidence here and is not defaulted.", file=sys.stderr)
            return 1
        obs_name, obs_secs = parse_observed(args.observed, args.how or "", legs)
        prev = rows.get(obs_name)
        # MONOTONE STILL, and the refusal is the point of saying so. A reading at or under the
        # stored maximum moves nothing, so admitting it quietly would answer the operator's gesture
        # with a fresh row and an unchanged number — the silent no-op this artifact is arranged
        # against. NOTHING IS WRITTEN on this path, because what was asked for did not happen.
        if prev and prev[0] >= obs_secs:
            print(f"derive-ceilings: --observed {obs_secs:.1f}s for '{obs_name}' does not raise "
                  f"its recorded maximum {prev[0]:.1f}s (source: {prev[4]}), and this file is "
                  f"MONOTONE. Nothing was written. Lowering one is "
                  f"`--write --reset {obs_name}`.", file=sys.stderr)
            return 1
        rows[obs_name] = (obs_secs, 1, obs_node, date, args.how.strip())
        observed = 1
    # The header names THIS install's own path, derived, so an adopter's committed evidence file
    # carries a command that exists in their tree (TOOL-aRepatriatedFork-2 S5).
    own = os.path.relpath(pathlib.Path(__file__).resolve(), root.resolve()).replace(os.sep, "/")
    lines = [
        "# ceiling-evidence.txt — the recorded maximum per gate leg, TRACKED so a gate can read it.",
        "#",
        f"# GENERATED by `python {own} --write` from",
        "# `<git-dir>/gate-run/*/*.leg`, which keeps one file per leg per run. Do not hand-edit: a",
        "# row here is a claim about a measurement, and one typed by hand is a claim about nothing.",
        "#",
        "# MONOTONE. A row only ever rises. `gate-run` retains a handful of runs, so a quiet window",
        "# would otherwise lower the evidenced maximum and with it the floor every ceiling is held",
        "# above. `--write --reset <leg>` lowers one by DELETING that leg's killed readings from the",
        "# untracked run record, so no later write can hand the value back — which is what a",
        "# decision somebody made has to mean here.",
        "#",
        "# THE SOURCE COLUMN tells a reading this tool derived from the run record apart from one",
        "# taken outside the runner and fed in with `--write --observed '<leg>=<seconds>' --how",
        f"# '<how>'`. In-band rows spell `{RUNNER_SOURCE}`; an out-of-band row spells the operator's",
        "# own account of how the number was taken, beside the node it was taken on. A leg killed",
        "# at its ceiling can produce no in-band reading above that ceiling, which is why the",
        "# out-of-band path exists — and why it is never allowed to look like the in-band one.",
        "#",
        "# <leg>\t<max seconds>\t<readings>\t<node>\t<date>\t<source>",
    ]
    for name in sorted(rows):
        mx, n, nd, dt, src = rows[name]
        lines.append(f"{name}\t{mx:.1f}\t{n}\t{nd}\t{dt}\t{src}")
    EVIDENCE.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    # `removed` IS THE LIVENESS HALF OF THIS LINE. `lowered` and `dropped` say the artifact moved;
    # only this says the scratch reading that would have restored it is gone, which is the property
    # the escape is actually asked for. A reset printing `1 lowered` over a run record it failed to
    # touch is the one report this fold exists to make impossible.
    print(f"derive-ceilings: wrote {len(rows)} row(s) to {EVIDENCE.name} "
          f"({raised} raised, {lowered} lowered by --reset, {dropped} dropped by --reset, "
          f"{removed} killed reading(s) removed by --reset, "
          f"{observed} raised by --observed, "
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
        #
        # IT IS A CLAIM ABOUT PROVENANCE, so it holds only for a runner-derived row, and finding
        # that out cost an arm (TOOL-cMendedVintage-17). "REACHED in a recorded run", "a LOWER
        # BOUND on the work", "do not size a new ceiling from it" are all true of a reading this
        # tool watched `timeout` stop, and all three are FALSE of one an operator measured to
        # completion elsewhere and typed in. Said over an out-of-band row the sentence withdraws
        # the invitation in the one case the flag was built to extend it: raising a bound from a
        # quiet measurement is the whole gesture. An out-of-band row falls to the headroom branch
        # below instead, which already prints the floor such a ceiling has to clear.
        if row[0] >= ceiling and row[4] == RUNNER_SOURCE:
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
    # THREE STATES, THREE SENTENCES, and this line is the third (TOOL-cMendedVintage-17). UNBACKED
    # stays reported-and-not-a-failure: a leg that has never run still has nothing to be measured
    # against, and a way to type a reading in does not change that. What DID need changing is the
    # word "backed", which now covers two different claims — a duration this tool watched the
    # runner produce, and one an operator measured elsewhere and typed. Naming the second kind with
    # its own stated conditions is what stops a scanner reading them as the same evidence. Derived
    # from the source column at check time, so there is no second thing to keep fresh.
    oob = sorted(n for n, r in ev.items() if n in legs and r[4] != RUNNER_SOURCE)
    if oob:
        print(f"derive-ceilings: {len(oob)} ceiling(s) backed by a reading taken OUTSIDE the "
              f"runner — a number an operator measured and typed, not one this tool watched: "
              + "; ".join(f"{n} {ev[n][0]:.1f}s on node {ev[n][2]}, {ev[n][4]}" for n in oob),
              file=sys.stderr)
    if bad:
        for b in bad:
            print(f"CEILING-EVIDENCE FAILED — {b}", file=sys.stderr)
        return 1
    print(f"ceiling-evidence: {len(legs) - len(unbacked)} of {len(legs)} leg(s) backed "
          f"({len(oob)} of them out-of-band), every one clearing its evidenced maximum by "
          f"max({floor}s, {frac} x max)")
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
                         "monotone hold, DELETES those killed readings from the untracked run "
                         "record so a later write cannot restore them, and drops the row entirely "
                         "when no `ok` reading remains")
    ap.add_argument("--observed", metavar="LEG=SECONDS",
                    help="with --write: admit a reading taken OUTSIDE the runner, so a leg killed "
                         "at its own ceiling can be raised from evidence instead of by hand. "
                         "Needs --how and GOV_NODE; the row is marked with its source and is "
                         "monotone like any other")
    ap.add_argument("--how", metavar="TEXT",
                    help="the conditions an --observed reading was taken under; recorded verbatim "
                         "as that row's source")
    args = ap.parse_args()
    # REFUSED RATHER THAN IGNORED on the read-only verbs. An operator who typed a measurement onto
    # a `--check` or `--report` line and got the ordinary output back would read it as accepted,
    # and the reading would exist nowhere. `--how` alone is the same gesture half-made.
    if (args.observed or args.how) and not args.write:
        sys.exit("derive-ceilings: --observed/--how are writes and belong to --write; "
                 "--report and --check read the tracked files and admit nothing")
    if args.how and not args.observed:
        sys.exit("derive-ceilings: --how describes an --observed reading and there is none")
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
