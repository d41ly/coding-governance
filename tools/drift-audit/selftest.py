#!/usr/bin/env python3
"""selftest.py — the drift-audit kit's own falsifiability test.

gov:kit drift-audit@1.25

    python <kit>/selftest.py

The kit's central claim is that a metric which cannot move is worse than no metric. That claim
obliges the kit to prove its OWN signals can move, so every gateable signal is exercised twice: once
against a fixture where it must be silent, and once against a minimal violating fixture where it must
fire. A signal that passes only the first arm is exactly the DEAD PROBE the report is built to refuse.

Also asserts the conf parser against BASH sourcing the same file — never against a second Python
parser, because two operands from one generator assert nothing.

Everything runs in a throwaway git repo under tempfile. Nothing is written into the adopter's tree.
"""

from __future__ import annotations

import os
import io
import pathlib
import shutil
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
# TOOL-aRepatriatedFork-46: this kit is named by the NAME its directory has in this install, and a
# SIBLING kit is reached through the resolver, which reads the install receipt first.
KIT_NAME = KIT.name
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
# The report's path INSIDE the scratch repos this file builds, which install the kit at the ROOT
# prefix on purpose — that is the dual-spelling support gov keeps for its not-retrofitted adopters,
# and a selftest that could not build one could not test it. Written ONCE here rather than twelve
# times below: a literal repeated twelve times is twelve chances for eleven of them to be updated.
ROOT_PFX = ""   # a root install's prefix is empty, and the scratch repos are built through it
REPORT_REL = f"{ROOT_PFX}{KIT_NAME}/drift_report.py"
FAILS: list[str] = []


def resolve_recall_name() -> str:
    """The memory-recall kit's directory NAME in this install, or "" where none is installed: a
    fixture built from this install cannot carry a kit this install does not have."""
    try:
        return resolve_kit_dir("memory-recall", "extract.py", KIT).name
    except LookupError:
        return ""


SKIPS: list[str] = []
EXECUTED: list[str] = []
# TOOL-dLoggedFlight-13. The suite printed "all checks passed" with no count behind it, so an arm
# stranded behind an early `return` passed by not running. This is the executed-check count measured
# on a run where no arm skipped; it rises by hand when arms land and never falls to absorb a missing
# one. A run with a SKIP does not compare it, and says so, because a skipped arm's checks are absent
# for a reason the floor cannot see.
CHECK_FLOOR = 478
# 474 -> 478, TOOL-dLadderedRemote-2: the four remote-ladder checks in `test_base_is_remote_tracking`,
# COUNTED off the arm rather than measured, because the unit pass runs no suite.
# 414 + 346 -> 474, the merge of origin/main into aMendedFleet: base 277, plus 137 from this
# branch (277 -> 414) and 69 from origin/main (277 -> 346), is 483, less the nine checks of
# `test_fleet_over_budget` that both sides counted for ONE arm: TOOL-aMendedFleet-92 ported
# TOOL-dUnstuckLanding-17's arm verbatim, and the merge keeps one copy, the one carrying M10.
# 411 -> 414, TOOL-aMendedFleet-110: the MOVE, EMPTY and CONTROL checks in `test_baselines`, COUNTED
# off the arms rather than measured, because the unit pass runs no suite.
# 402 -> 411, TOOL-aMendedFleet-92: the nine checks of `test_fleet_over_budget`, COUNTED off the arm
# rather than measured, because the unit pass runs no suite; the close's run re-reads it.
# 397 -> 402, TOOL-aMendedFleet-91: the five records-only checks of signal 6.
# 383 -> 397, TOOL-aMendedFleet-90: the fourteen checks of `test_dead_streaks`.
# 377 -> 383, TOOL-aMendedFleet-59: the six every-git-dir checks in `test_legs_retried_after_timeout`.
# 365 -> 377, TOOL-aMendedFleet-57: the twelve checks of `test_shrink_low_water`.
# 357 -> 365, TOOL-aMendedFleet-56: the eight checks of `test_baselines`.
# 352 -> 357, TOOL-aMendedFleet-55: the five `open_asks_cited_by_product_source` checks.
# 345 -> 352, TOOL-aMendedFleet-54: the seven checks of `test_live_builds_without_activity`.
# 330 -> 339, TOOL-aMendedFleet-52: the nine checks of `test_handkept_name_sets`.
# 339 -> 345, TOOL-aMendedFleet-53: the six checks of `test_auto_memory_pointers`.
# 327 -> 330, TOOL-aMendedFleet-51: the readme-drift all-CLOSED arm and the two pinless checks.
# 318 -> 327, TOOL-aMendedFleet-50: the nine checks of `test_escape_ratio`.
# 309 -> 318, TOOL-aMendedFleet-49: the nine checks of `test_drift_delta`.
# 302 -> 309, TOOL-aMendedFleet-48: the seven checks of `test_drift_history`.
# 295 -> 302, TOOL-aMendedFleet-47: the run-records arm's derived-LANDED checks — three derived
# fixtures left unlisted, their count, the summary line, and the LANDING call-count size's two.
# 289 -> 295, TOOL-aMendedFleet-37: the six checks of `test_stale_dossiers`.
# 284 -> 289, TOOL-aMendedFleet-21: the five checks of `test_cutoff_keys_armed`.
# 277 -> 284, TOOL-aMendedFleet-8: the seven checks of `test_remote_ci_red_streak`.
# 261 -> 267, TOOL-dDerivedDocket-26: the six checks of `test_legs_retried_after_timeout`.
# 267 -> 277, TOOL-dDerivedDocket-34: the five checks of the retired dGV-13 signal leave, one
# retirement check and the fourteen of `test_backlog_ask_signals` arrive.
# 277 -> 324, TOOL-dUnstuckLanding-15: the thirty-four checks of `test_aborted_work_landed` and the
# thirteen of `test_work_landed_matches_the_driver`.
# 324 -> 333, TOOL-dUnstuckLanding-17: the nine checks of `test_fleet_over_budget`, COUNTED off the arm
# rather than measured, because the unit pass runs no suite; the close's run re-reads it.
# 333 -> 344, implementation review round 1, fold pass A, COUNTED the same way: L3's tautological
# parity control leaves (-1); three fixture records add three `_AWL_WANT` readings and three parity
# rows (+6); AC4's merge-revert row (+1); L6's two-reader arm, two checks and one per fact (+4); and
# M10's unjudged fleet line (+1), net +11. L6 reaches its four only where the library's bash runs,
# as the parity arm already does, and a run without it skips and does not compare the floor.
# 344 -> 346, implementation review round 2, L5, COUNTED the same way: the off-ref tip arm's two
# checks, one per grader.


def check(label: str, cond: bool, detail: str = "") -> None:
    EXECUTED.append(label)
    if cond:
        print(f"  ok   {label}")
    else:
        print(f"  FAIL {label}{(' — ' + detail) if detail else ''}")
        FAILS.append(label)


def skip(label: str, why: str) -> None:
    """A skipped arm is announced and TALLIED, never printed as ok. An arm that quietly passes
    because it did not run is the green-by-absence class this whole kit is aimed at."""
    print(f"  SKIP {label} — {why}")
    SKIPS.append(label)


def resolve_posix_shell(probe_dir: pathlib.Path) -> str | None:
    """Find a POSIX shell that can actually read files at `probe_dir`.

    On Windows a bare `bash` resolves to the WSL shim ahead of MSYS on PATH, and WSL cannot source a
    Windows temp path the same way — so the probe returns empty and the comparison silently fails on
    an interpreter mismatch rather than on real parser drift. RESOLVE the interpreter; do not merely
    detect that it is wrong. Verified on Windows: `bash` -> GNU/Linux, `sh` -> Msys.
    """
    marker = probe_dir / ".shellprobe"
    marker.write_text("PROBE=works\n", encoding="utf-8", newline="\n")
    try:
        for cand in ("sh", "bash", "/usr/bin/bash", "/bin/sh"):
            try:
                out = subprocess.run(
                    [cand, "-c", 'set -a; . ./.shellprobe; printf "%s" "$PROBE"'],
                    cwd=str(probe_dir), capture_output=True, text=True,
                    encoding="utf-8", errors="replace",
                )
            except (OSError, FileNotFoundError):
                continue
            if out.returncode == 0 and out.stdout.strip() == "works":
                return cand
        return None
    finally:
        marker.unlink(missing_ok=True)


def run(cmd: list[str], cwd: pathlib.Path, env: dict | None = None) -> subprocess.CompletedProcess:
    # GOV_DEFAULT_BRANCH is declared for every fixture: these repos have no remote, and the report's
    # default-branch ladder now REFUSES to guess rather than falling back to a literal `main` that
    # may not exist. That refusal is the point of the change, so the fixtures state their default the
    # way an adopter without a remote has to. The arm that proves the refusal passes NO env.
    e = dict(os.environ)
    e.setdefault("GOV_DEFAULT_BRANCH", "main")
    if env is not None:
        e.update(env)
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True,
                          encoding="utf-8", errors="replace", env=e)


# ---------------------------------------------------------------------------------------------
# 1 — conf parser == bash sourcing
# ---------------------------------------------------------------------------------------------


def test_conf_parser_matches_bash(tmp: pathlib.Path) -> None:
    print("conf parser vs bash")
    # TOOL-aScouredKit-5 — the last two spellings are the ones this arm did NOT cover, and their
    # absence is why a gate written to catch parser divergence had never observed one. Both are
    # legal bash and both diverged: an `export ` prefix left the key spelled `export EXPORTED`, and
    # an unquoted value with a trailing comment swallowed the comment into the value. The arm below
    # was seen RED against the unfixed parser before the parser was touched.
    body = (
        '# a comment with an = sign\n'
        'MEMORY_ROOT=memory\n'
        'DISCIPLINES="one two three"\n'
        "QUOTED_SINGLE='x y'\n"
        '\n'
        'TRAILING=spaced   \n'
        'export EXPORTED=exported\n'
        'INLINE=value   # a trailing comment bash does not put in the value\n'
        'QUOTED_NOTE="noted"  # a note after a quoted value\n'
        "SINGLE_NOTE='single' # a note after a single-quoted value\n"
        # TOOL-aRepatriatedFork-38 rev-3 (C4): whitespace after `=` ends the assignment, so this is
        # empty, never the word `#`; a `#` opening the word is data.
        'BLANKED=   # blank on purpose\n'
        'HASHED=#x\n'
    )
    p = tmp / ".memory-tree.conf"
    p.write_text(body, encoding="utf-8", newline="\n")

    sys.path.insert(0, str(KIT))
    import drift_report as dr

    got = dr.load_conf(tmp)
    sh = resolve_posix_shell(tmp)
    if sh is None:
        skip("conf parser vs shell", "no POSIX shell here can source a file at this path")
        return
    # TOOL-dLoggedFlight-13 R2-L5 — QUOTED_NOTE and SINGLE_NOTE: a quoted value followed by a comment
    # kept its quotes, because the parser told quoted from unquoted by the value's last character.
    for key in ("MEMORY_ROOT", "DISCIPLINES", "QUOTED_SINGLE", "TRAILING",
                "EXPORTED", "INLINE", "QUOTED_NOTE", "SINGLE_NOTE", "BLANKED", "HASHED"):
        res = run([sh, "-c", f'set -a; . ./.memory-tree.conf; printf "%s" "${key}"'], tmp)
        if res.returncode != 0:
            check(f"{sh} could source the conf for {key}", False, res.stderr.strip()[:120])
            continue
        check(f"{key} parses identically to {sh}", got.get(key) == res.stdout,
              f"python={got.get(key)!r} shell={res.stdout!r}")


# ---------------------------------------------------------------------------------------------
# fixture: a throwaway repo shaped like a governance adopter
# ---------------------------------------------------------------------------------------------


# The build-spec path the fixture creates, expressed the way drift_report.py globs for it. Both
# sides read MEMORY_ROOT from the same conf, so changing the conf moves BOTH — which the arm at the
# bottom of this file proves rather than assumes.
FIXTURE_MEMORY_ROOT = "memory"
SPEC_DIR_FOR_FIXTURE = f"{FIXTURE_MEMORY_ROOT}/builds/2026-01-01-TOOL-x/spec"


def _side_branch_commit(r: pathlib.Path) -> str:
    """A commit that EXISTS but is not an ancestor of the default branch.

    The clean ledger fixture needs one: every commit reachable from `main` is an ancestor of `main`,
    so a row citing any of them is a row the probe must flag. Only a side branch gives "this sha is
    real, and this work has genuinely not landed" — which is what a correct open row looks like.
    """
    run(["git", "checkout", "-q", "-b", "sidework"], r)
    (r / "src" / "side.txt").write_text("side\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-qm", "side work, not merged", "--no-verify"], r)
    sha = run(["git", "rev-parse", "--short", "HEAD"], r).stdout.strip()
    run(["git", "checkout", "-q", "main"], r)
    return sha


def make_repo(tmp: pathlib.Path, name: str = "repo") -> pathlib.Path:
    # `name` exists so a second arm can build a SECOND fixture rather than thread itself through
    # `test_signals_can_move`'s eight mutations — that sequence ends by unlinking the project layer,
    # so anything appended to it would run against a repo that refuses to report at all.
    r = tmp / name
    # DERIVED from the conf this fixture is about to write, never a literal layout. The previous
    # line spelled `memory/tooling/builds/<x>/spec` — the pre-flatten shape — so an arm named
    # "violated: spec signal fires" was green while the dogfood's own signal printed DEAD PROBE. A
    # fixture that encodes a layout is a fixture that certifies the layout it encodes.
    (r / SPEC_DIR_FOR_FIXTURE).mkdir(parents=True)
    (r / "memory" / "project" / "in-flight").mkdir(parents=True)
    (r / "src").mkdir(parents=True)
    (r / "conf").mkdir(parents=True)
    (r / KIT_NAME).mkdir(parents=True)

    (r / ".memory-tree.conf").write_text("MEMORY_ROOT=memory\n", encoding="utf-8", newline="\n")
    (r / "AGENTS.md").write_text("# charter\n\n| Tag | Machine | Tree |\n|---|---|---|\n",
                                 encoding="utf-8", newline="\n")
    (r / "src" / "app.py").write_text("# nothing cited here\n", encoding="utf-8", newline="\n")
    (r / "shrinkme.txt").write_text("# header\nentry-one\nentry-two\n", encoding="utf-8", newline="\n")

    # A CLEAN ledger row must be JUDGEABLE and clean — not merely unjudgeable. The previous fixture
    # named only a BASE sha, so the probe had nothing of its own to judge; once `live` became the
    # judgeable population rather than the row count, that fixture made the signal correctly DEAD and
    # the "clean" arm was asserting over a probe that could not answer. A row that cites its own work
    # on a side branch is the real clean case: built, genuinely not merged.
    # The sha is filled in AFTER `git init`, below — a side branch cannot be cut before the repo
    # exists, and a fixture that silently wrote an empty sha would leave the probe unjudgeable again,
    # which is the state this fixture was changed to escape.
    (r / "memory" / "project" / "in-flight" / "a.md").write_text(
        "| slug | branch | status |\n|---|---|---|\n"
        "| `aThing` | `feature/x` off `BASESHA` | in-flight — NOT merged, work at `PENDING` |\n",
        encoding="utf-8", newline="\n")

    # a CLEAN spec: non-terminal, and its id appears nowhere in product source
    (r / SPEC_DIR_FOR_FIXTURE / "2026-01-01-spec-aThing-1.md").write_text(
        "# TOOL-aThing-1 — a thing\n\n**Status:** SPECCED · rev-1 · 2026-01-01 · node a · Tier-2 · base 0000000\n",
        encoding="utf-8", newline="\n")

    # --- signal 6's population, three specs, all DISTINCT from aThing ------------------------
    # aThing is mutated by the arms in test_signals_can_move (SPECCED -> CLOSED and back), so
    # building signal 6's fixture on it would couple two independent oracles' arms to one file.
    #
    # CLOSED after the cutoff and CERTIFIED: `commit the traced work` below names its slug and
    # touches src/, which is this fixture's TRACE_GLOBS. Signal 6 must be silent on it.
    (r / SPEC_DIR_FOR_FIXTURE / "2026-02-02-spec-aTraced-1.md").write_text(
        "# TOOL-aTraced-1 — a traced thing\n\n"
        "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
        encoding="utf-8", newline="\n")
    # The UNCERTIFIED spec is NOT written here. The base fixture must be CLEAN for every signal, or
    # the `--check` pin-semantics arms below inherit a second over-pin signal and stop asserting what
    # their names say. The violating spec is created by the arm that needs it, and removed after.
    #
    # Its FILENAME date is before the cutoff and its HEADER date is after it. Only a header-date key
    # judges this spec, so it is the one shape that can tell the two keys apart -- and the whole
    # header-date-versus-filename-date subsection of the spec rests on it.
    (r / SPEC_DIR_FOR_FIXTURE / "2025-12-20-spec-aLate-1.md").write_text(
        "# TOOL-aLate-1 — filename before the cutoff, closed after it\n\n"
        "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
        encoding="utf-8", newline="\n")
    # A CLOSED spec whose H1 carries no id at all: the probe must COUNT it as unjudgeable, never
    # guess at it and never let it fall into `value`.
    (r / SPEC_DIR_FOR_FIXTURE / "2026-02-02-spec-aNoId-1.md").write_text(
        "# a heading with no unit id in it\n\n"
        "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
        encoding="utf-8", newline="\n")
    # CLOSED BEFORE the cutoff and uncertified: grandfathered, so it must land in `unjudgeable`
    # rather than in `value`. Without it the cutoff is asserted only by its own absence.
    (r / SPEC_DIR_FOR_FIXTURE / "2025-12-31-spec-aElder-1.md").write_text(
        "# TOOL-aElder-1 — a thing that closed before the convention\n\n"
        "**Status:** CLOSED · rev-1 · 2025-12-31 · node a · Tier-2 · base 0000000\n",
        encoding="utf-8", newline="\n")

    for f in ("drift_report.py", "drift_signals.template.py"):
        (r / KIT_NAME / f).write_bytes((KIT / f).read_bytes())
    (r / KIT_NAME / "drift_signals.py").write_text(
        # PRODUCT_GLOBS is deliberately WIDER than TRACE_GLOBS here. The narrowing is the whole
        # point of TRACE_GLOBS -- in the shipping repo it drops `.claude/` and the kickoff
        # manifest so a records commit cannot certify the record -- and with the two equal, an
        # engine that ignored TRACE_GLOBS entirely would pass every arm below.
        "PRODUCT_GLOBS = ['src', 'conf']\n"
        # Signal 6's declarations. TRACE_CUTOFF must be SET here: unset, the engine returns
        # gateable:False and the arms below would assert over a signal that never ran — the
        # fixture-passes-by-finding-nothing class. The cutoff sits between aElder (2025-12-31) and
        # the two 2026-02-02 specs, so one spec is grandfathered and two are judged.
        "TRACE_CUTOFF = '2026-01-15'\n"
        "TRACE_GLOBS = ['src']\n"
        # Signal 2's own population, and NARROWER than PRODUCT_GLOBS on purpose:
        # `conf/` stays outside it, so an engine that read PRODUCT_GLOBS here would
        # be caught rather than passing by coincidence.
        "EVIDENCE_GLOBS = ['src', ':(exclude)*.test.sh']\n"
        "SHRINK_ONLY = {'shrinkme.txt': 'a list that promises to shrink'}\n"
        "HANDKEPT = []\n"
        # PINS stays EMPTY and is spelled exactly `PINS = {}`: the pin-semantics arm below rewrites
        # this literal, and seeding a pin here would silently turn that arm into a no-op.
        "PINS = {}\n"
        # HANDKEPT is empty here, as it is in the shipped template — so the signal it feeds is empty
        # BY DECLARATION, not blind, and must be named as such or `--check` reds this fixture for
        # modelling the adopter default faithfully. SHRINK_ONLY is populated above, so it is NOT
        # declared: leaving it in this set after populating it is how an exemption becomes a hole.
        "DECLARED_EMPTY = {'handkept_inventories_disagreeing_with_source'}\n",
        encoding="utf-8", newline="\n")

    run(["git", "init", "-q", "-b", "main"], r)
    run(["git", "config", "user.email", "selftest@example.com"], r)
    run(["git", "config", "user.name", "selftest"], r)
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "seed"], r)

    # Now the side-branch sha exists, so the clean row can cite work that is REAL and genuinely not
    # merged. Asserted, not assumed: an empty sha here puts the probe back in the unjudgeable state.
    side = _side_branch_commit(r)
    assert len(side) >= 7, f"side-branch sha not produced: {side!r}"
    led = r / "memory" / "project" / "in-flight" / "a.md"
    led.write_text(led.read_text(encoding="utf-8").replace("`PENDING`", "`" + side + "`"),
                   encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "clean ledger row cites unmerged side work"], r)

    # Signal 6's CERTIFYING commit: its subject names aTraced's slug AND it touches src/, which is
    # this fixture's TRACE_GLOBS. Written as a real commit rather than folded into the seed because
    # the seed's subject ("seed") names nothing — a certified spec has to be certified by something.
    (r / "src" / "traced.py").write_text("# the traced work\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "feat(aTraced): the work TOOL-aTraced-1 specified", "--no-verify"], r)

    # aLate is certified normally, from src/. conf/ gets a file so the directory is tracked; the
    # TRACE_GLOBS arm below adds the commit that names a spec from inside it.
    (r / "conf" / "settings.ini").write_text("k=v\n", encoding="utf-8", newline="\n")
    (r / "src" / "late.py").write_text("# late\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "feat(aLate): the work", "--no-verify"], r)
    return r


def report(r: pathlib.Path, *extra: str) -> dict:
    import json

    out = run([sys.executable, REPORT_REL, "--json", *extra], r)
    if out.returncode != 0 or not out.stdout.strip():
        raise AssertionError(f"report failed rc={out.returncode}: {out.stderr.strip()[:300]}")
    return {s["signal"]: s for s in json.loads(out.stdout)}


# ---------------------------------------------------------------------------------------------
# 2 — every gateable signal is silent on a clean fixture AND fires on a violating one
# ---------------------------------------------------------------------------------------------


def test_signals_can_move(tmp: pathlib.Path) -> None:
    print("signal falsifiability (each must be silent when clean AND fire when violated)")
    r = make_repo(tmp)

    base = report(r)
    check("clean fixture: ledger signal silent", base["ledger_rows_contradicting_git"]["value"] == 0)
    check("clean fixture: spec signal silent",
          base["non_terminal_specs_cited_by_product_source"]["value"] == 0)
    check("clean fixture: ledger probe is LIVE (population non-empty)",
          base["ledger_rows_contradicting_git"]["live"] is True)
    check("clean fixture: spec probe is LIVE (population non-empty)",
          base["non_terminal_specs_cited_by_product_source"]["live"] is True)

    # --- violate signal 1: a row claiming in-flight while naming a LANDED work sha ---------
    sha = run(["git", "rev-parse", "--short", "HEAD"], r).stdout.strip()
    led = r / "memory" / "project" / "in-flight" / "a.md"
    clean_row = led.read_text(encoding="utf-8")   # restored after the base-sha arm, which unjudges the row
    # Swap the side-branch sha for one that IS an ancestor of the default branch. Same row, same
    # claim, one fact changed — so the arm isolates the oracle rather than the row's wording.
    import re as _re
    led.write_text(_re.sub(r"work at `[0-9a-f]+`", f"work at `{sha}`",
                           led.read_text(encoding="utf-8")),
                   encoding="utf-8", newline="\n")
    v1 = report(r)
    check("violated: ledger signal fires on a landed work sha",
          v1["ledger_rows_contradicting_git"]["value"] == 1,
          f"got {v1['ledger_rows_contradicting_git']['value']}")

    # --- the BASE-sha exclusion must hold, or every row is a false positive ----------------
    led.write_text(led.read_text(encoding="utf-8").replace(
        f"NOT merged, work at `{sha}`", "NOT merged, nothing of its own").replace(
        "`BASESHA`", f"`{sha}`"), encoding="utf-8", newline="\n")
    v1b = report(r)
    check("base sha alone does NOT fire the ledger signal",
          v1b["ledger_rows_contradicting_git"]["value"] == 0,
          f"got {v1b['ledger_rows_contradicting_git']['value']} — base-sha exclusion is broken")
    # ...and it reports UNJUDGEABLE rather than a clean 0. This is the sharper half: "the base sha was
    # excluded" and "there was nothing left to judge" produce the same value, and only the second is
    # true here. Before `live` became the judgeable population, this arm could not tell them apart.
    check("...and says so: the row is unjudgeable, not clean",
          v1b["ledger_rows_contradicting_git"]["live"] is False
          and v1b["ledger_rows_contradicting_git"].get("unjudgeable") == 1,
          f"live={v1b['ledger_rows_contradicting_git']['live']} "
          f"unjudgeable={v1b['ledger_rows_contradicting_git'].get('unjudgeable')}")
    # Restore the judgeable clean row: every arm below judges a repo whose ledger can be judged, and
    # leaving it unjudgeable would make them assert over a DEAD probe.
    led.write_text(clean_row, encoding="utf-8", newline="\n")

    # --- violate signal 2: the spec's own id now appears in product source -----------------
    (r / "src" / "app.py").write_text("# implements TOOL-aThing-1\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "cite the id in product source"], r)
    v2 = report(r)
    check("violated: spec signal fires when the id reaches product source",
          v2["non_terminal_specs_cited_by_product_source"]["value"] == 1,
          f"got {v2['non_terminal_specs_cited_by_product_source']['value']}")

    # --- the PREFIX arm: a SIBLING's id must not certify this spec --------------------------
    # `-F` alone matches a PREFIX, so `TOOL-aThing-1` hit inside `TOOL-aThing-11`. Measured live on
    # this repo at TOOL-aBoundedVerdict-30: id `-1` carried three citations and all three were
    # `-11`'s. Without this arm the `-w` that fixes it is an unproven character.
    (r / "src" / "app.py").write_text("# implements TOOL-aThing-11\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "cite only the SIBLING id"], r)
    v2p = report(r)
    check("a sibling id sharing this id's prefix does not fire it",
          v2p["non_terminal_specs_cited_by_product_source"]["value"] == 0,
          f"got {v2p['non_terminal_specs_cited_by_product_source']['value']} "
          f"detail={v2p['non_terminal_specs_cited_by_product_source']['detail']}")
    # Without this the arm above is satisfied by a probe that judged nothing.
    check("...and the probe is still live, so that 0 is a measurement",
          v2p["non_terminal_specs_cited_by_product_source"]["live"] is True)
    # Restore the real citation: the arms below judge a repo where the id IS cited.
    (r / "src" / "app.py").write_text("# implements TOOL-aThing-1\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "restore the real citation"], r)

    # --- a TERMINAL status must not fire, or the signal is just counting specs -------------
    spec = r / SPEC_DIR_FOR_FIXTURE / "2026-01-01-spec-aThing-1.md"
    spec.write_text(spec.read_text(encoding="utf-8").replace("SPECCED", "CLOSED"),
                    encoding="utf-8", newline="\n")
    v2b = report(r)
    check("a CLOSED spec does not fire even when cited",
          v2b["non_terminal_specs_cited_by_product_source"]["value"] == 0)
    check("a population of zero reports DEAD PROBE, not a clean 0",
          v2b["non_terminal_specs_cited_by_product_source"]["live"] is False)
    spec.write_text(spec.read_text(encoding="utf-8").replace("CLOSED", "SPECCED"),
                    encoding="utf-8", newline="\n")

    # --- signal 3 is report-only but must still be able to observe a shrink ----------------
    s3 = report(r)["shrink_only_lists_not_shrinking"]
    check("shrink-only signal sees a list that has not shrunk", s3["value"] == 1, str(s3["detail"]))
    (r / "shrinkme.txt").write_text("# header\nentry-one\n", encoding="utf-8", newline="\n")
    s3b = report(r)["shrink_only_lists_not_shrinking"]
    check("shrink-only signal goes quiet once the list actually shrinks", s3b["value"] == 0,
          str(s3b["detail"]))

    # --- DEPL-dGaugedVintage-13's signal RETIRED at the backlog switch-over (TOOL-dDerivedDocket-34
    # --- S10). Its arms went with it; this one keeps the retirement from being undone by a merge.
    check("[dDD-34] the retired backlog_rows_outliving_closed_specs is absent from the report",
          "backlog_rows_outliving_closed_specs" not in report(r))

    # --- signal 6: a CLOSED spec must be backed by a commit that names it AND changed product ---
    print("closed-spec traceability (signal 6)")
    ghost = r / SPEC_DIR_FOR_FIXTURE / "2026-02-02-spec-aGhost-1.md"
    base6 = report(r)["closed_specs_with_no_product_commit"]
    check("clean fixture: the traceability signal is silent", base6["value"] == 0,
          f"got {base6['value']} detail={base6['detail']}")

    check("clean fixture: ...and LIVE, over a judged population", base6["live"] is True
          and base6["of"] >= 1, f"live={base6['live']} of={base6['of']}")
    # THE GRANDFATHER ARM. aElder is CLOSED before the cutoff with nothing naming it anywhere, so if
    # the cutoff were ignored it would be counted. Asserting it sits in `unjudgeable` — and not
    # merely that `value` is 0 — is what separates "grandfathered" from "not looked at at all".
    check("clean fixture: the pre-cutoff CLOSED spec is unjudgeable, not clean",
          base6["unjudgeable"] >= 1, f"unjudgeable={base6['unjudgeable']}")

    ghost.write_text("# TOOL-aGhost-1 — a thing with no commit behind it\n\n"
                     "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
                     encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "records: close it with nothing built", "--no-verify"], r)
    v6 = report(r)["closed_specs_with_no_product_commit"]
    check("violated: an uncertified CLOSED spec fires the traceability signal", v6["value"] == 1,
          f"got {v6['value']} detail={v6['detail']}")

    # THE `TERMINAL` FILTER, armed. Found unarmed by mutation: replacing the status test with a bare
    # "did the header parse" produced ZERO failures, because the only non-terminal spec in the base
    # fixture is dated before the cutoff and was unjudgeable either way. A signal that judged every
    # status would call every OPEN spec untraceable, which is the opposite of what it is for.
    live_spec = r / SPEC_DIR_FOR_FIXTURE / "2026-02-02-spec-aOpen-1.md"
    live_spec.write_text("# TOOL-aOpen-1 — specced, not built, and correctly so\n\n"
                         "**Status:** SPECCED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
                         encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "records: a post-cutoff spec that is not built yet",
         "--no-verify"], r)
    v6t = report(r)["closed_specs_with_no_product_commit"]
    check("a NON-TERMINAL post-cutoff spec with no commit does not fire", v6t["value"] == 1,
          f"got {v6t['value']} — a non-CLOSED status is being judged: {v6t['detail']}")
    live_spec.unlink()

    # THE SLUG FALLBACK, armed. Also found unarmed: the certifying subject named the slug AND the id,
    # so deleting the slug branch changed nothing. This spec is certified by its SLUG only.
    slugonly = r / SPEC_DIR_FOR_FIXTURE / "2026-02-02-spec-aSlugOnly-1.md"
    slugonly.write_text("# TOOL-aSlugOnly-1 — certified by its slug and never by its id\n\n"
                        "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
                        encoding="utf-8", newline="\n")
    (r / "src" / "slugonly.py").write_text("# work\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "fix(aSlugOnly): the work, subject naming no unit id",
         "--no-verify"], r)
    v6s = report(r)["closed_specs_with_no_product_commit"]
    check("a CLOSED spec certified by its SLUG alone does not fire", v6s["value"] == 1,
          f"got {v6s['value']} — the slug fallback is gone: {v6s['detail']}")
    slugonly.unlink()
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "records: drop the slug-only fixture", "--no-verify"], r)

    # A MERGE naming the slug must NOT certify it. Reconcile merges name the branch merged INTO, so
    # counting them let a build with no product commit of its own ride another build's merge — which
    # is exactly how this signal's pin read 0 instead of 1 on the repo that ships it.
    #
    # THE MERGE HAS TO BE NON-TREESAME OR THIS ARM PROVES NOTHING. A path-restricted `git log`
    # applies default history simplification, so a merge whose result for `src/` equals one parent's
    # is dropped from the walk before `--no-merges` is ever consulted. Measured: with a fast
    # side-branch merge this arm stayed green when `--no-merges` was deleted from the engine — it was
    # asserting that a commit git had already hidden was not being counted. Both sides therefore
    # touch the SAME file and the merge resolves to a third content, so the merge commit differs from
    # both parents and survives simplification. Verified by deleting `--no-merges` and watching this
    # arm go red.
    shared = r / "src" / "shared.py"
    shared.write_text("base\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "seed the shared file", "--no-verify"], r)
    run(["git", "checkout", "-q", "-b", "ghostwork"], r)
    shared.write_text("branch side\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "unrelated work on the branch", "--no-verify"], r)
    run(["git", "checkout", "-q", "main"], r)
    shared.write_text("main side\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "unrelated work on main", "--no-verify"], r)
    run(["git", "merge", "--no-ff", "-q", "--no-commit", "ghostwork"], r)   # conflicts, by design
    shared.write_text("resolved\n", encoding="utf-8", newline="\n")         # a third content
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "merge: aGhost — reconcile ghostwork", "--no-verify"], r)
    merge_seen = run(["git", "log", "main", "--format=%s", "--", "src"], r).stdout
    check("the merge fixture is VISIBLE to a path-restricted walk (else the arm below is vacuous)",
          "merge: aGhost" in merge_seen,
          "history simplification dropped it; the arm would pass without the guard")
    v6m = report(r)["closed_specs_with_no_product_commit"]
    check("a MERGE subject naming the slug does not certify it", v6m["value"] == 1,
          f"got {v6m['value']} — merge subjects are being counted as evidence")

    # Restore: every arm below judges a fixture whose only over-pin signal is the one it names.
    ghost.unlink()
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "reopen it", "--no-verify"], r)
    check("...and goes quiet once the uncertified spec is gone",
          report(r)["closed_specs_with_no_product_commit"]["value"] == 0)

    # TRACE_GLOBS NARROWS PRODUCT_GLOBS, and that narrowing needs its own arm: with the pathspec
    # dropped from the walk entirely, every other signal-6 arm here stays green. This spec is named
    # ONLY by a commit touching conf/ -- product by PRODUCT_GLOBS, not evidence by TRACE_GLOBS -- so
    # the house bookkeeping cannot certify the house.
    outside = r / SPEC_DIR_FOR_FIXTURE / "2026-02-02-spec-aOutside-1.md"
    outside.write_text("# TOOL-aOutside-1 — named only by a commit that changed no product\n\n"
                       "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
                       encoding="utf-8", newline="\n")
    (r / "conf" / "settings.ini").write_text("k=v2\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "chore(aOutside): bookkeeping only, no product", "--no-verify"], r)
    v6g = report(r)["closed_specs_with_no_product_commit"]
    check("a commit inside PRODUCT_GLOBS but outside TRACE_GLOBS does not certify",
          [d["id"] for d in v6g["detail"]] == ["TOOL-aOutside-1"],
          f"got {v6g['detail']} -- the evidence pathspec is not being applied")
    outside.unlink()
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "records: drop the outside fixture", "--no-verify"], r)

    # THE HEADER-DATE KEY, which a whole subsection of the spec rests on. This spec's FILENAME date
    # is before the cutoff and its HEADER date is after it, and nothing certifies it. Under the
    # shipped header-date key it is JUDGED and fires; under a filename-date key it is grandfathered
    # and silent. That divergence is the only shape that can tell the two keys apart, and swapping
    # the comparison to `p.name` leaves every other arm in this file green.
    late = r / SPEC_DIR_FOR_FIXTURE / "2025-12-20-spec-aStale-1.md"
    late.write_text("# TOOL-aStale-1 — filename before the cutoff, closed long after it\n\n"
                    "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
                    encoding="utf-8", newline="\n")
    run(["git", "add", SPEC_DIR_FOR_FIXTURE + "/2025-12-20-spec-aStale-1.md"], r)
    run(["git", "commit", "-q", "-m", "records: a spec whose two dates straddle the cutoff",
         "--no-verify"], r)
    v6h = report(r)["closed_specs_with_no_product_commit"]
    check("the cutoff is judged on the HEADER date, not the filename date",
          [d["id"] for d in v6h["detail"]] == ["TOOL-aStale-1"],
          f"got {v6h['detail']} -- a filename-date key would grandfather this spec")
    late.unlink()
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "records: drop the straddling fixture", "--no-verify"], r)

    # THE WAIVER, both directions over one fixture. `aWaived` is CLOSED, post-cutoff and certified by
    # nothing, so it FIRES on its own — that is the precondition, asserted first, because a waiver arm
    # over a spec that was already silent would pass without the waiver doing anything.
    waiver = r / "memory" / "project" / "trace-waiver.txt"
    wspec_rel = SPEC_DIR_FOR_FIXTURE + "/2026-02-02-spec-aWaived-1.md"
    wspec = r / wspec_rel
    wspec.write_text("# TOOL-aWaived-1 — a unit no product subject can name\n\n"
                     "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
                     encoding="utf-8", newline="\n")
    run(["git", "add", wspec_rel], r)
    run(["git", "commit", "-q", "-m", "records: a unit nothing certifies", "--no-verify"], r)
    v6w0 = report(r)["closed_specs_with_no_product_commit"]
    check("the waiver fixture fires BEFORE it is waived",
          [d["id"] for d in v6w0["detail"]] == ["TOOL-aWaived-1"],
          f"got {v6w0['detail']} -- the arm below would pass vacuously")

    waiver.write_text("# fixture\n" + wspec_rel + "\tTOOL-aWaived-1\tno subject can name it\n",
                      encoding="utf-8", newline="\n")
    v6w1 = report(r)["closed_specs_with_no_product_commit"]
    check("a waived spec is silent", v6w1["value"] == 0,
          f"got {v6w1['detail']} -- the waiver is not being read")

    # THE REGISTRY'S PATH IS DECLARABLE (TOOL-dMuffledSentinel-2), over the same fixture. Moved out of
    # `memory/project/` with no key, the spec FIRES again: that is the precondition, because an arm
    # over a spec a stray file already silenced would pass without the key doing anything. Then the
    # key names the new home and it is silent; then a declared path that is not there, and one outside
    # the tree, each come back as a finding of their own rather than as an empty waiver set.
    sigp = r / KIT_NAME / "drift_signals.py"
    sig_base = sigp.read_text(encoding="utf-8")
    moved = r / "waivers" / "trace.txt"
    moved.parent.mkdir(parents=True, exist_ok=True)
    moved.write_text(waiver.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
    waiver.unlink()
    v6m0 = report(r)["closed_specs_with_no_product_commit"]
    check("a relocated registry with no TRACE_WAIVER waives nothing",
          [d["id"] for d in v6m0["detail"]] == ["TOOL-aWaived-1"],
          f"got {v6m0['detail']} -- the TRACE_WAIVER arm below would pass vacuously")
    for decl, want, why in (
        ("waivers/trace.txt", [], "TRACE_WAIVER reads the registry where it is declared"),
        ("waivers/missing.txt", ["(declared TRACE_WAIVER)", "TOOL-aWaived-1"],
         "a declared TRACE_WAIVER that is not there is a finding, not an empty waiver set"),
        ("../trace.txt", ["(declared TRACE_WAIVER)", "TOOL-aWaived-1"],
         "a declared TRACE_WAIVER outside the tree is a finding, not an empty waiver set"),
    ):
        sigp.write_text(sig_base + f'\nTRACE_WAIVER = "{decl}"\n', encoding="utf-8", newline="\n")
        got = report(r)["closed_specs_with_no_product_commit"]
        check(why, sorted(d["id"] for d in got["detail"]) == want, f"got {got['detail']}")
    sigp.write_text(sig_base, encoding="utf-8", newline="\n")
    waiver.write_text(moved.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
    moved.unlink()
    moved.parent.rmdir()

    # A row must not outlive its subject. Deleting the spec leaves the row behind, which is the shape
    # that silently widens the exemption, so it has to come back as a finding rather than as silence.
    wspec.unlink()
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "records: drop the waived fixture", "--no-verify"], r)
    v6w2 = report(r)["closed_specs_with_no_product_commit"]
    check("a waiver row whose spec is gone becomes a finding of its own",
          [d["id"] for d in v6w2["detail"]] == ["(stale waiver)"],
          f"got {v6w2['detail']} -- a stale waiver is being swallowed")
    waiver.unlink()

    # THE RECORDS-ONLY VERB (TOOL-aMendedFleet-91). One fixture, CLOSED and certified by nothing, so
    # it FIRES bare: asserted first, or the exemption arm passes without the verb doing anything.
    ro_rel = SPEC_DIR_FOR_FIXTURE + "/2026-02-02-spec-aRecords-1.md"
    ro = r / ro_rel
    ro_h1 = "# TOOL-aRecords-1 — a census, records and nothing else\n\n"
    ro_status = "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-1 · base 0000000"

    # (status tail, body, waiver row, label, detail ids wanted, records_only wanted). The body arm
    # spells the token between `·` separators, so a read of the whole text rather than the status
    # line alone reds it.
    for tail, body, row, why, want, listed in (
        ("", "", "", "the records-only fixture fires BEFORE it declares the verb",
         ["TOOL-aRecords-1"], []),
        (" · records-only · order 7", "", "", "a CLOSED spec declaring records-only is silent and listed",
         [], [ro_rel]),
        (" · records-only", "", ro_rel + "\tTOOL-aRecords-1\tdeclared twice\n",
         "the verb beside a waiver row reports the row stale, naming the declaration",
         ["(stale waiver)"], [ro_rel]),
        (" · records-only-ish", "", "", "a lookalike tail token exempts nothing",
         ["TOOL-aRecords-1"], []),
        ("", "\n## 1. Goal\n\nIts tail would read · records-only · were it declared.\n", "",
         "records-only in body prose exempts nothing", ["TOOL-aRecords-1"], []),
    ):
        ro.write_text(ro_h1 + ro_status + tail + "\n" + body, encoding="utf-8", newline="\n")
        if row:
            waiver.write_text(row, encoding="utf-8", newline="\n")
        got = report(r)["closed_specs_with_no_product_commit"]
        if row:
            waiver.unlink()
        named = not row or bool(got["detail"]) and "records-only" in got["detail"][0].get("note", "")
        check(why, [d["id"] for d in got["detail"]] == want and got["records_only"] == listed
              and named, f"got {got['detail']} records_only={got.get('records_only')}")
    ro.unlink()

    # --- 3 — --check honours the pin in BOTH directions -------------------------------------
    print("--check pin semantics")
    sig = r / KIT_NAME / "drift_signals.py"
    over = run([sys.executable, REPORT_REL, "--check"], r)
    check("--check reds while a gateable signal is over its (default 0) pin", over.returncode == 1,
          f"rc={over.returncode}")
    # --- 3a — --offenders, the SIGNATURE the merge bar grades this leg with (TOOL-dDerivedDocket-23
    # S3). The bar's red attribution compares two trees' offender SETS, so the mode is graded on what
    # a set needs: its exit is --check's, every line is one TAB-separated key naming a signal --check
    # reds on, and no key carries a line locator, which an unrelated edit above a finding would move.
    offs = run([sys.executable, REPORT_REL, "--offenders"], r)
    olines = offs.stdout.splitlines()
    red_now = {k for k, v in report(r).items()
               if v["gateable"] and v["live"] and v["value"] > v["pin"]}
    check("--offenders exits as --check does over the same tree", offs.returncode == over.returncode,
          f"--offenders {offs.returncode}, --check {over.returncode}")
    check("--offenders prints one TAB-separated key per finding, each naming a signal --check reds on",
          bool(olines) and all(ln.count("\t") == 1 and ln.split("\t")[0] in red_now | {"ratchet"}
                               for ln in olines),
          f"lines={olines[:5]} red={sorted(red_now)}")
    check("--offenders carries no line locator in any key",
          not any(re.search(r":\d+(:|$)", ln) or '"line"' in ln for ln in olines), f"{olines[:5]}")
    sig.write_text(sig.read_text(encoding="utf-8").replace(
        "PINS = {}", "PINS = {'non_terminal_specs_cited_by_product_source': 1}"),
        encoding="utf-8", newline="\n")
    at = run([sys.executable, REPORT_REL, "--check"], r)
    check("--check greens once the pin is seeded at the measured value", at.returncode == 0,
          f"rc={at.returncode} stderr={at.stderr.strip()[:200]}")

    # THE UNION OF BOTH TIPS. The spec population is read from the working tree, so the evidence
    # must be too: a unit that flips its own spec to CLOSED on its branch has its certifying commits
    # on that branch and nowhere else. Walking base_ref alone reds correct work, which is the defect
    # this arm exists for -- and it had none until the closing review mutation-tested it.
    run(["git", "checkout", "-q", "-b", "unitwork"], r)
    (r / SPEC_DIR_FOR_FIXTURE / "2026-02-02-spec-aBranch-1.md").write_text(
        "# TOOL-aBranch-1 — closed on its own branch, before any merge\n\n"
        "**Status:** CLOSED · rev-1 · 2026-02-02 · node a · Tier-2 · base 0000000\n",
        encoding="utf-8", newline="\n")
    (r / "src" / "branch.py").write_text("# branch work\n", encoding="utf-8", newline="\n")
    # NAMED PATHS, never `git add -A`: the project layer is edited-but-uncommitted at this point in
    # the run, and sweeping it onto this branch means `git checkout main` below reverts it. That cost
    # two later arms their seeded pin and reported as a failure three arms away from its cause.
    run(["git", "add", SPEC_DIR_FOR_FIXTURE + "/2026-02-02-spec-aBranch-1.md", "src/branch.py"], r)
    run(["git", "commit", "-q", "-m", "feat(aBranch): the work, on the branch", "--no-verify"], r)
    # ASSERTED, not assumed: the certifying commit must be absent from the default branch, or this
    # arm passes whether or not HEAD is in the walk.
    onmain = run(["git", "log", "main", "--format=%s", "--", "src"], r).stdout
    check("the branch fixture is INVISIBLE from the default branch (else the arm is vacuous)",
          "feat(aBranch)" not in onmain, "the commit is already on main")
    v6b = report(r)["closed_specs_with_no_product_commit"]
    check("a spec CLOSED on its own branch is certified by that branch: both tips are walked",
          all(d["id"] != "TOOL-aBranch-1" for d in v6b["detail"]),
          f"base-only walk would red correct work: {v6b['detail']}")
    run(["git", "checkout", "-q", "main"], r)

    # A CLOSED spec whose H1 names no id is COUNTED, never guessed at.
    unj = v6b["unjudgeable"]
    check("a CLOSED spec with no parseable id lands in unjudgeable", unj >= 2, f"unjudgeable={unj}")

    # --- an UNSET TRACE_CUTOFF is "not asked", not "dead" ------------------------------------
    # Every existing adopter has a project layer with no TRACE_CUTOFF in it. If the engine returned
    # gateable:True there, `--check`'s dead-probe rule would red them on the first pull of this kit
    # for doing nothing at all — and DECLARED_EMPTY could not save them, because that set lives in
    # the file they have not edited. So the engine, not the declaration, has to answer this.
    keep = sig.read_text(encoding="utf-8")
    sig.write_text(keep.replace("TRACE_CUTOFF = '2026-01-15'", "TRACE_CUTOFF = ''"),
                   encoding="utf-8", newline="\n")
    unset = report(r)["closed_specs_with_no_product_commit"]
    check("unset cutoff: the signal is not gateable", unset["gateable"] is False,
          f"gateable={unset['gateable']}")
    quiet6 = run([sys.executable, REPORT_REL, "--check"], r)
    check("unset cutoff: --check stays green rather than reding a dead gateable probe",
          quiet6.returncode == 0, f"rc={quiet6.returncode} stderr={quiet6.stderr.strip()[:200]}")
    sig.write_text(keep, encoding="utf-8", newline="\n")

    # --- a missing project layer is a REFUSAL, never a default ------------------------------
    sig.unlink()
    gone = run([sys.executable, REPORT_REL], r)
    check("a missing project layer refuses with rc 2", gone.returncode == 2, f"rc={gone.returncode}")


# ---------------------------------------------------------------------------------------------
# 3b — the two LEXICON signals: NOT ASKED without the kit, and falsifiable with it
# ---------------------------------------------------------------------------------------------


def test_no_signal_hardcodes_live(tmp: pathlib.Path) -> None:
    """No signal may return a LITERAL `live: True`.

    `live` is the field that makes DEAD PROBE possible — the kit's central claim is that a metric
    which cannot move is worse than none, and `live` is how a probe admits it cannot. A literal True
    asserts the opposite by construction: it says "this probe can move" without consulting anything,
    which is the armed-but-unreachable-rule class landing on the very field that exists to refuse it.
    One signal shipped that way and reported a permanent, reassuring, GATEABLE zero.

    Grep-able and shrink-only, deliberately. It cannot tell a well-derived `live` from a badly
    derived one — only that SOMETHING was consulted — which is a smaller claim than it looks and is
    stated here rather than implied.
    """
    print("no signal hardcodes live:True")
    src = (KIT / "drift_report.py").read_text(encoding="utf-8")
    hits = [f"{i}: {l.strip()}" for i, l in enumerate(src.splitlines(), 1)
            if '"live": True' in l and not l.lstrip().startswith("#")]
    check("no signal returns a literal live:True", not hits, "; ".join(hits))


def test_lexicon_signals(tmp: pathlib.Path) -> None:
    """These are the only two signals in this shipped engine that name an OPTIONAL kit, so the
    absent-conf case is the load-bearing arm: an adopter who never took the lexicon must inherit
    `gateable: False` — not a clean 0, which would read as "asked and fine", and not a red."""
    print("lexicon signals (not-asked without the kit; falsifiable with it)")
    r = make_repo(tmp / "lexsig")

    base = report(r)
    for name in ("lexicon_verbs_declared_but_unused", "lexicon_ratified_older_than_language_surface"):
        s = base[name]
        check(f"no .lexicon.conf: {name} is NOT ASKED, not a clean zero",
              s["gateable"] is False and s["value"] == 0, f"{s}")
        check(f"no .lexicon.conf: {name} says why", "not adopted" in str(s["detail"]),
              f"{s['detail']}")

    # Adopt the kit INTO the fixture: the engine reaches it by `sys.path`, so the reader has to be
    # present exactly where an installed kit puts it -- BESIDE the drift-audit kit, which this fixture
    # installs at the root prefix, because the engine resolves its sibling through `resolve_kit_dir`
    # (TOOL-aRepatriatedFork-2 S3), not at the graded root's `<prefix>/`.
    kit_src = resolve_kit_dir("lexicon", "lexicon.py", KIT)
    shutil.copytree(kit_src, r / kit_src.name,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    src = r / "src" / "thing.py"
    src.write_text("def build_thing():\n    pass\n", encoding="utf-8", newline="\n")
    conf = r / ".lexicon.conf"
    conf.write_text(
        'BANNED_SUFFIXES="Manager"\nLANGS="py:python-ast:parser"\n'
        'VERB_OFFENDER_PIN="99"\nSUFFIX_OFFENDER_PIN="0"\n'
        'ratified="2999-01-01 node t"\n\nVERBS:\n  build  make a thing\n',
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "adopt the lexicon", "--no-verify"], r)

    clean = report(r)["lexicon_verbs_declared_but_unused"]
    check("clean fixture: every declared verb is used, so the signal is silent",
          clean["value"] == 0 and clean["gateable"] is True, f"{clean}")
    check("clean fixture: ...and LIVE over a non-empty population", clean["live"] is True, f"{clean}")

    # VIOLATE: declare a verb nothing is called. This is the OUTLIVING direction — the half no other
    # mechanism here can see.
    conf.write_text(conf.read_text(encoding="utf-8").replace(
        "VERBS:\n  build  make a thing\n", "VERBS:\n  build  make a thing\n  vanish  used by nothing\n"),
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "declare an unused verb", "--no-verify"], r)
    fired = report(r)["lexicon_verbs_declared_but_unused"]
    check("violated: a declared-but-unused verb fires the signal", fired["value"] == 1, f"{fired}")
    check("violated: it names the verb", "vanish" in str(fired["detail"]), f"{fired['detail']}")

    # THE LANGS LOOKUP, ARMED DIRECTLY. The first version of this arm rolled the stamp back AND
    # widened LANGS in ONE commit, so it fired off the stamp alone and would have stayed green with
    # the widening deleted — which is exactly how a `-S` pickaxe shipped here. `-S` counts
    # OCCURRENCES of the string, and `LANGS=` appears once before and once after an in-place
    # widening, so the lookup froze at the adoption commit forever while reporting a confident 0.
    # Asserting the COMMIT the lookup found is what makes the two implementations distinguishable;
    # a DATE cannot, because a same-day fixture gives both the same answer.
    before = report(r)["lexicon_ratified_older_than_language_surface"].get("langs_commit")
    conf.write_text(conf.read_text(encoding="utf-8").replace(
        'LANGS="py:python-ast:parser"', 'LANGS="py:python-ast:parser js:js-regex:probe"'),
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "widen the language surface IN PLACE", "--no-verify"], r)
    after = report(r)["lexicon_ratified_older_than_language_surface"].get("langs_commit")
    check("the LANGS lookup SEES an in-place widening (a -S pickaxe cannot)",
          bool(after) and after != before, f"before={before} after={after}")

    # ...and only THEN the end-to-end arm, on a stamp that predates it.
    conf.write_text(conf.read_text(encoding="utf-8").replace('ratified="2999-01-01 node t"',
                                                             'ratified="1999-01-01 node t"'),
                    encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "roll the stamp back", "--no-verify"], r)
    stale = report(r)["lexicon_ratified_older_than_language_surface"]
    check("violated: a language surface widened after ratification fires the staleness signal",
          stale["value"] == 1, f"{stale}")
    check("...and the signal is LIVE by derivation, not a hardcoded True",
          stale["live"] is True, f"{stale}")

    # THE PATTERNS RESOLUTION, ARMED, and nothing armed it before. Both lexicon signals read
    # `lex.PATTERN_SETS` — the SHIPPED constant — and skipped any extension whose pattern set was not
    # in it, so a language armed only through a `PATTERNS:` row was passed over file by file while
    # the signal reported a confident number with `live` still true off the Python half. That is
    # green-by-absence on a gateable signal. Reverting `_resolve_lexicon_sets` back to the constant
    # left this whole suite green, which is the defect this arm exists to make impossible.
    #
    # `vanish` is declared above and used by nothing. Its ONLY definition site now lives in a
    # language reachable only through the declaration, so the signal falls to 0 exactly when the
    # resolution is read and stays at 1 when it is not.
    (r / "web").mkdir()
    (r / "web" / "widget.ts").write_text("export function vanishThing() {}\n",
                                         encoding="utf-8", newline="\n")
    conf.write_text(
        conf.read_text(encoding="utf-8").replace(
            'LANGS="py:python-ast:parser js:js-regex:probe"',
            'LANGS="py:python-ast:parser js:js-regex:probe ts:ts-regex:probe"')
        + "\nPATTERNS:\n"
        + r"  ts-regex.functions  ^\s*(?:export\s+)?function\s+([A-Za-z_$][\w$]*)" + "\n",
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "arm a language through PATTERNS alone", "--no-verify"], r)
    armed = report(r)["lexicon_verbs_declared_but_unused"]
    check("a language armed ONLY by a PATTERNS row is read: the verb it defines stops being unused",
          armed["value"] == 0, f"{armed}")
    check("...and the signal stays LIVE over that widened population", armed["live"] is True,
          f"{armed}")

    # H1 OF THE CLOSING REVIEW — AN UNSHIPPED `parser` ID MUST NOT TAKE THE WHOLE REPORT DOWN.
    #
    # `_build_armed_exts` dropped `dark` rows and unknown-`probe` rows and KEPT a `parser` row whose
    # pattern-set id the kit does not ship, so `extract_text` reached `PARSERS[pset]` and raised
    # `KeyError`. Neither `except` tuple downstream covered it and `main()` evaluates every signal
    # unguarded, so ONE legal-looking `LANGS` row cost all eight signals and printed a traceback —
    # on a leg that carries no guard and runs on every bar. The engine's own `scan_corpus` refuses
    # the same row by name, so the two readers of one declaration disagreed; `_load_lexicon`'s
    # docstring promises "never a raise and never a red" for exactly this class.
    #
    # A TYPO IS THE WHOLE POPULATION. Nothing validates the id upstream — `langs()` checks the MODE
    # token, `check_declaration` checks the CELLS/PINS cross-references — so an adopter is one
    # mistyped set id away from a dead report.
    conf.write_text(conf.read_text(encoding="utf-8")
                    .replace("py:python-ast:parser", "py:bogus-parser:parser"),
                    encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "a parser id the kit does not ship", "--no-verify"], r)
    _raw = run([sys.executable, REPORT_REL, "--json"], r)
    check("H1: an unshipped `parser` pattern-set id does not raise out of the report",
          "Traceback" not in _raw.stderr and "KeyError" not in _raw.stderr,
          _raw.stderr.strip()[-400:])
    check("H1: ...and the report still returns every signal rather than none",
          _raw.returncode == 0 and _raw.stdout.strip().startswith("["),
          f"rc={_raw.returncode} {_raw.stdout.strip()[:200]}")


def test_lexicon_marginal_rate(tmp: pathlib.Path) -> None:
    """The marginal-offense-rate signal: four states, and each one must be distinguishable.

    THE ARM THAT MATTERS IS THE EMPTY WINDOW. A stretch in which nobody added a definition is a real
    and common state — a records-only week — and reporting it as a rate of 0 is byte-identical to
    reporting a clean one. Only the NOT ASKED arm separates them, and a version that returned 0 there
    would pass every other check here.

    THE SHALLOW ARM IS THE ONE THIS SIGNAL'S SPEC GOT WRONG. rev-2 asserted a `--depth 1` clone makes
    the derived base unresolvable; measured, `git log --diff-filter=A` there returns the SHALLOW ROOT
    as the adding commit and it resolves fine, so a resolves-check is armed against a case it cannot
    see and the signal would report a rate over a one-commit window. The assertion that fires asks
    whether the repository is truncated at all.
    """
    print("lexicon marginal-offense-rate (four states, each distinguishable)")
    r = make_repo(tmp / "lexrate")
    name = "lexicon_marginal_offense_rate"

    absent = report(r)[name]
    check("no .lexicon.conf: the rate is NOT ASKED, not a clean zero",
          absent["gateable"] is False and absent["value"] == 0, f"{absent}")
    check("no .lexicon.conf: it says why", "not adopted" in str(absent["detail"]), f"{absent['detail']}")

    kit_src = resolve_kit_dir("lexicon", "lexicon.py", KIT)
    shutil.copytree(kit_src, r / kit_src.name,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (r / ".lexicon.conf").write_text(
        'BANNED_SUFFIXES="Manager"\nLANGS="py:python-ast:parser"\n'
        'VERB_OFFENDER_PIN="99"\nSUFFIX_OFFENDER_PIN="0"\n'
        'ratified="2999-01-01 node t"\n\nVERBS:\n  build  make a thing\n',
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "adopt the lexicon", "--no-verify"], r)

    # The adoption commit IS the derived base, so HEAD == base and the window is empty BY
    # CONSTRUCTION. This is the state a rate of 0 would misreport as clean.
    empty = report(r)[name]
    # ASSERTS `not_asked`, not `value == 0`. A rate of 0 ALSO has value 0 and gateable False, so the
    # obvious spelling of this arm stays green under exactly the break it exists to catch -- observed
    # 2026-08-25 by staging that break and watching this line pass. `not_asked` is the field the
    # renderer branches on to keep the three states three, so it is the field the arm must read.
    check("empty window: NOT ASKED rather than a rate of 0",
          empty.get("not_asked") is True, f"{empty}")
    check("empty window: it names the reason, so 0 is never mistaken for clean",
          "no definition was added" in str(empty["detail"]), f"{empty['detail']}")

    # Two definitions added, exactly one of them off-table.
    (r / "src" / "later.py").write_text(
        "def build_ok():\n    pass\n\n\ndef frobnicate_bad():\n    pass\n",
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "add two definitions, one off-table", "--no-verify"], r)
    fired = report(r)[name]
    check("a window with definitions added reports offenders over that population",
          fired["value"] == 1 and fired["of"] == 2, f"{fired}")
    check("...and is LIVE by derivation over a non-empty population",
          fired["live"] is True, f"{fired}")
    check("...and carries the fresh-versus-pre-existing split the kill-rule reads",
          any("FRESH" in str(d.get("note", "")) for d in fired["detail"]), f"{fired['detail']}")

    # UNGRADEABLE NAMES ARE IN NEITHER OPERAND. `leading_verb` returns "" for an identifier with no
    # word characters, and the kit's own reuse note says plainly that a caller must treat that as
    # ungradeable rather than as a violation. The signal did neither: "" is not in the declared
    # table, so such a name counted as an offender AND stayed in the denominator, inflating the rate
    # at both ends. Asserting BOTH operands is the point -- an arm reading only `value` would stay
    # green against a version that merely stopped counting it as an offender while leaving it in
    # `of`, which is the same rate wrong in the other direction. Closing review L4.
    before = report(r)[name]
    # A GRADEABLE CONTROL LANDS IN THE SAME COMMIT. Round 1 asserted `before["of"] > 0` as its
    # non-vacuity guard, which is a property of the PREVIOUS window and says nothing about whether
    # this commit reached the signal at all -- the round-2 review patched the extractor to skip
    # word-character-free names entirely, an ordinary upstream change, and watched all three arms
    # report ok. The control makes one assertion do both jobs: `of` must rise by exactly one, which
    # proves the commit was seen, AND `value` must not move, which proves the ungradeable name left
    # both operands. Neither can pass by finding nothing.
    (r / "src" / "ungradeable.py").write_text(
        "def __():" + chr(10) + "    pass" + chr(10) + chr(10) + chr(10)
        + "def build_control():" + chr(10) + "    pass" + chr(10),
        encoding="utf-8", newline=chr(10))
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "one ungradeable name and one gradeable control", "--no-verify"], r)
    after = report(r)[name]
    check("an ungradeable name is not counted as an offender",
          after["value"] == before["value"], f"before={before['value']} after={after['value']}")
    check("...and the population grew by the CONTROL alone, so the ungradeable name left both operands",
          after["of"] == before["of"] + 1, f"before={before['of']} after={after['of']}")

    # THE SECOND RESOLUTION SITE. It was ungated until a re-verification pass reverted it ALONE and
    # watched both suites stay green. `build_lexicon_marginal_offense_rate` reads the resolved pattern
    # sets in three places -- the armed-extension set and both per-sha reads -- and the arm covering
    # the OTHER lexicon signal reaches none of them. Two call sites and one arm between them is the
    # same green-by-absence shape that sibling arm exists to abolish, one signal over.
    #
    # THE POPULATION IS THE OPERAND THAT MOVES. A language armed only through a `PATTERNS:` row is
    # invisible to the shipped constant, so its definitions never enter `of`. One gradeable definition
    # in that language must raise `of` by exactly one; with the resolution dropped it raises it by
    # nothing and the signal reports a confident rate over the Python half alone. Asserting `value`
    # holds STILL is the other half: a population that grew while the rate moved would mean the added
    # name was graded off-table, which would make this arm pass for the wrong reason.
    (r / "web").mkdir()
    (r / "web" / "panel.ts").write_text(
        "export function buildPanel() {}" + chr(10), encoding="utf-8", newline=chr(10))
    ts_regex = r"  ts-regex.functions  ^\s*(?:export\s+)?function\s+([A-Za-z_$][\w$]*)"
    conf_p = r / ".lexicon.conf"
    conf_p.write_text(
        conf_p.read_text(encoding="utf-8").replace(
            'LANGS="py:python-ast:parser"', 'LANGS="py:python-ast:parser ts:ts-regex:probe"')
        + chr(10) + "PATTERNS:" + chr(10) + ts_regex + chr(10),
        encoding="utf-8", newline=chr(10))
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "arm a second language through PATTERNS alone", "--no-verify"], r)
    widened = report(r)[name]
    check("the marginal rate READS a language armed only by a PATTERNS row: its population grows",
          widened["of"] == after["of"] + 1,
          f"of before={after['of']} after={widened['of']} -- a population that did not grow means "
          "build_lexicon_marginal_offense_rate never resolved the declared pattern sets")
    check("...and the rate itself did not move, so the population grew by an ON-TABLE name",
          widened["value"] == after["value"],
          f"value before={after['value']} after={widened['value']}")


    # ...and a window in which EVERY added definition is ungradeable must say so rather than read as
    # a clean measured window. The round-1 L4 fix pointed every operand at `gradeable` and left the
    # emptiness guard reading `added`, so that window returned value 0, of 0, live True and no
    # `not_asked` -- and `0 > 0` is false, so it printed a plain `ok`. Found by the round-2 review.
    #
    # IT NEEDS ITS OWN REPO. The window runs from the declaration's adoption commit to HEAD and is
    # cumulative, so appending an ungradeable file to the fixture above leaves the earlier gradeable
    # definitions in it and the window is not all-ungradeable at all. The first spelling of this arm
    # carried an `or of > 0` escape to paper over that, which made it satisfiable by the very
    # population it was supposed to exclude -- observed staying green with the guard reverted.
    b = make_repo(tmp, "lexblind")
    shutil.copytree(kit_src, b / kit_src.name,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (b / ".lexicon.conf").write_text(
        'BANNED_SUFFIXES="Manager"' + chr(10) + 'LANGS="py:python-ast:parser"' + chr(10)
        + 'VERB_OFFENDER_PIN="99"' + chr(10) + 'SUFFIX_OFFENDER_PIN="0"' + chr(10)
        + 'ratified="2999-01-01 node t"' + chr(10) + chr(10)
        + "VERBS:" + chr(10) + "  build  make a thing" + chr(10),
        encoding="utf-8", newline=chr(10))
    run(["git", "add", "-A"], b)
    run(["git", "commit", "-q", "-m", "adopt the lexicon", "--no-verify"], b)
    (b / "src" / "onlyblind.py").write_text(
        "def __():" + chr(10) + "    pass" + chr(10), encoding="utf-8", newline=chr(10))
    run(["git", "add", "-A"], b)
    run(["git", "commit", "-q", "-m", "add only an ungradeable name", "--no-verify"], b)
    _blind = report(b)[name]
    check("an all-ungradeable window is NOT ASKED, never a clean zero",
          _blind.get("not_asked") is True, f"{_blind}")
    check("...and it says WHY, so the zero is never mistaken for a clean window",
          "no word characters" in str(_blind["detail"]), f"{_blind['detail']}")

    # ADMITTING the verb must move the rate. Without this the offender test could be reading a
    # frozen table and nothing here would notice.
    conf = r / ".lexicon.conf"
    conf.write_text(conf.read_text(encoding="utf-8").replace(
        "VERBS:\n  build  make a thing\n", "VERBS:\n  build  make a thing\n  frobnicate  do the thing\n"),
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "admit the verb", "--no-verify"], r)
    admitted = report(r)[name]
    check("admitting a verb lowers the rate, so the table is read at HEAD and not frozen",
          admitted["value"] == 0 and admitted["of"] >= 2, f"{admitted}")

    # THE SHALLOW ARM. A `--depth 1` clone still DERIVES a base — the shallow root — and it resolves,
    # so only a truncation check can refuse it.
    shallow = tmp / "lexrate-shallow"
    run(["git", "clone", "-q", "--depth", "1", "file://" + str(r).replace("\\", "/"), str(shallow)], tmp)
    if (shallow / ".git").exists():
        deep = run(["git", "rev-parse", "--is-shallow-repository"], shallow).stdout.strip()
        check("the fixture clone really is shallow (or this arm proves nothing)", deep == "true", deep)
        got = report(shallow)[name]
        check("shallow clone: DEAD PROBE rather than a rate over a one-commit window",
              got["live"] is False and "shallow" in str(got["detail"]).lower(), f"{got}")
    else:
        skip("shallow-clone arm", "the fixture clone did not materialise on this platform")


# ---------------------------------------------------------------------------------------------
# 5 - backlog_stragglers: the fleet-wide half of the shards-to-builds transition
# ---------------------------------------------------------------------------------------------


def test_backlog_stragglers(tmp: pathlib.Path) -> None:
    """The straggler inventory, in the three states it can report.

    THE REMOTE-TRACKING HALF IS THE LOAD-BEARING ARM. The hooks beside `.githooks/` reach a
    straggler only on the node that owns it, and `check-wiring.sh` names the LOCAL ones. A signal
    that walked `refs/heads` alone would read a pushed straggler from another node as none, which is
    the reassuring zero this kit exists to refuse - so the fixture plants one that exists ONLY as a
    remote-tracking ref and the arm names it.
    """
    print("backlog stragglers (not asked without the relocation engine; falsifiable with it)")
    r = make_repo(tmp, name="stragglers")

    s = report(r)["backlog_stragglers"]
    check("no memory-tree kit: backlog_stragglers is NOT ASKED, not a clean zero",
          s.get("not_asked") is True and s["value"] == 0, f"{s}")
    check("no memory-tree kit: and it says why",
          "memory-tree" in str(s["detail"]), f"{s['detail']}")

    kit_root = KIT.parent
    missing = [n for n in ("memory-tree", "memory-recall", "lib") if not (kit_root / n).is_dir()]
    if missing:
        skip("backlog_stragglers: the live arms",
             f"the sibling kits are not installed beside this one: {', '.join(missing)}")
        return
    for name in ("memory-tree", "memory-recall", "lib"):
        shutil.copytree(kit_root / name, r / name,
                        ignore=shutil.ignore_patterns("__pycache__"))
    (r / ".memory-tree.conf").write_text(
        "MEMORY_ROOT=memory\nDISCIPLINES=\"tooling\"\nFAMILIES=\"tooling:TOOL\"\n"
        "ROTATION_MODE=\"cut\"\nBACKLOG_MODE=\"shards\"\n",
        encoding="utf-8", newline="\n")
    (r / ".gitignore").write_text("__pycache__/\n", encoding="utf-8", newline="\n")
    bl = r / "memory" / "backlog"
    bl.mkdir(parents=True, exist_ok=True)
    (bl / "TOOL.md").write_text("# TOOL backlog\n\n- TOOL-aSeed-1 - the first ask\n",
                                encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "a shards-mode backlog and the kits", "--no-verify"], r)

    # One LOCAL straggler, and one that exists only as a REMOTE-TRACKING ref - the branch another
    # node pushed. `update-ref` rather than a real remote on purpose: a remote would make
    # `origin/HEAD` observable and change which branch the inventory keys on, which is a different
    # question from the one this arm asks.
    for branch, text in (("strag", "REWORDED by the local straggler"),
                         ("elsewhere", "REWORDED by another node")):
        run(["git", "checkout", "-q", "-b", branch, "main"], r)
        (bl / "TOOL.md").write_text(f"# TOOL backlog\n\n- TOOL-aSeed-1 - {text}\n",
                                    encoding="utf-8", newline="\n")
        run(["git", "commit", "-q", "-am", f"the {branch} straggler edits a row", "--no-verify"], r)
    far = run(["git", "rev-parse", "HEAD"], r).stdout.strip()
    run(["git", "checkout", "-q", "main"], r)
    run(["git", "branch", "-q", "-D", "elsewhere"], r)
    run(["git", "update-ref", "refs/remotes/origin/elsewhere", far], r)

    (r / ".memory-tree.conf").write_text(
        "MEMORY_ROOT=memory\nDISCIPLINES=\"tooling\"\nFAMILIES=\"tooling:TOOL\"\n"
        "ROTATION_MODE=\"cut\"\nBACKLOG_MODE=\"builds\"\n",
        encoding="utf-8", newline="\n")
    flip = r / "memory" / "builds" / "aFlip"
    flip.mkdir(parents=True, exist_ok=True)
    (flip / "BACKLOG.md").write_text("# aFlip\n\n## Asks\n\n## Dispositions\n",
                                     encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "flip to builds", "--no-verify"], r)

    s = report(r)["backlog_stragglers"]
    check("two stragglers: the signal counts both", s["value"] == 2, f"{s}")
    check("two stragglers: and reports how many refs it examined", s["of"] >= 3, f"of={s['of']}")
    check("two stragglers: the probe is live", s["live"] is True, f"{s}")
    check("two stragglers: and it is never gateable", s["gateable"] is False, f"{s}")
    refs = [d.get("ref", "") for d in s["detail"]]
    check("two stragglers: the LOCAL one is named", any("refs/heads/strag" in x for x in refs), f"{refs}")
    check("two stragglers: the REMOTE-TRACKING one is named too",
          any("refs/remotes/origin/elsewhere" in x for x in refs), f"{refs}")

    # Nothing to examine: the inventory refuses rather than reporting a clean zero, and the signal
    # carries that through as NOT LIVE. A ref walk that examined nothing is a fact about the clone.
    tip = run(["git", "rev-parse", "HEAD"], r).stdout.strip()
    run(["git", "checkout", "-q", "--detach"], r)
    for branch in ("main", "strag", "sidework"):
        run(["git", "branch", "-q", "-D", branch], r)
    run(["git", "update-ref", "-d", "refs/remotes/origin/elsewhere"], r)
    s = report(r, "--base-ref", tip)["backlog_stragglers"]
    check("no ref to examine: the signal reports NOT LIVE, never a clean zero",
          s["live"] is False and s["value"] == 0, f"{s}")
    check("no ref to examine: and it carries the reason",
          "DEAD PROBE" in str(s["detail"]), f"{s['detail']}")


# ---------------------------------------------------------------------------------------------
# 4 — DECLARED_EMPTY relabels a drained probe WITHOUT muzzling it (three directions)
# ---------------------------------------------------------------------------------------------


def test_live_backlog_rows(tmp: pathlib.Path) -> None:
    """TOOL-aRelaxedShard-4: the live-row signal, in every direction it can be wrong."""
    print("live backlog rows per shard")
    r = make_repo(tmp, name="liverows")
    bl = r / "memory" / "backlog"
    bl.mkdir(parents=True, exist_ok=True)

    # Three live rows and two terminal ones. The terminal pair is the load-bearing half: a signal that
    # counted ENTRIES rather than LIVE entries would pass every other arm in this function.
    rows = [
        "# ARCH backlog",
        "- ARCH-tLive-1 · OPEN · one",
        "- ARCH-tLive-2 · SPECCED · two",
        "- ARCH-tLive-3 · INPROGRESS · three",
        "- ARCH-tLive-4 · CLOSED · four",
        "- ARCH-tLive-5 · WONTDO · five",
    ]
    (bl / "ARCH.md").write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
    # A second, EMPTY shard: it must contribute 0 and must NOT make the probe dead.
    (bl / "DES.md").write_text("# DES backlog\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "shards", "--no-verify"], r)

    got = report(r)["live_backlog_rows_per_shard"]
    check("counts LIVE rows, not entries: 3 of 5", got["value"] == 3, f"got {got['value']}")
    check("reports every shard, so a total cannot hide one", got["of"] == 2, f"got {got['of']}")
    check("probe is LIVE with shards present", got["live"] is True)
    # --- PINLESS BY DESIGN (TOOL-aMendedFleet-51 S1, S3): a None tolerance serialises as null, the
    # --- pin resolves to null with no PINS entry, and the table says so instead of `over pin 0`.
    check("pinless: the record serialises a null tolerance and a null pin",
          got["tolerance"] is None and got["pin"] is None,
          f"tolerance={got['tolerance']!r} pin={got['pin']!r}")
    _row = next((ln for ln in run([sys.executable, REPORT_REL], r).stdout.splitlines()
                 if "live_backlog_rows_per_shard" in ln), "")
    check("pinless: its printed row reads 'report only, no pin' and nothing about being over",
          "report only, no pin" in _row and "over" not in _row, f"row={_row.strip()!r}")
    per = {d["shard"]: d for d in got["detail"]}
    check("the empty shard reports 0 rather than being skipped",
          per.get("memory/backlog/DES.md", {}).get("live") == 0,
          f"got {per.get('memory/backlog/DES.md')}")
    check("the busy shard reports its total beside its live count",
          per.get("memory/backlog/ARCH.md", {}).get("total") == 5,
          f"got {per.get('memory/backlog/ARCH.md')}")

    # --- it MOVES when a row is closed. That is the whole point of the signal. ----------------
    closed = (bl / "ARCH.md").read_text(encoding="utf-8").replace(
        "- ARCH-tLive-1 · OPEN · one", "- ARCH-tLive-1 · CLOSED · one")
    (bl / "ARCH.md").write_text(closed, encoding="utf-8", newline="\n")
    check("closing a row lowers the count", report(r)["live_backlog_rows_per_shard"]["value"] == 2,
          "the signal does not track the variable it exists for")

    # --- REPORT-ONLY, and F2 decided that deliberately: `drift-audit records` is an unguarded
    # --- merge-bar leg, so a gateable version turns a growing backlog into a scheduled refusal.
    check("the signal is not gateable", report(r)["live_backlog_rows_per_shard"]["gateable"] is False)

    # --- DEAD, not a reassuring 0, where there are no shards at all --------------------------
    r2 = make_repo(tmp, name="noshards")
    for f in sorted((r2 / "memory" / "backlog").glob("*.md")):
        run(["git", "rm", "-q", str(f.relative_to(r2))], r2)
    run(["git", "commit", "-q", "-m", "drop shards", "--no-verify"], r2)
    dead = report(r2)["live_backlog_rows_per_shard"]
    check("no shards at all reports DEAD rather than 0",
          dead["live"] is False, f"live={dead['live']} value={dead['value']}")


# The stub generator the builds-mode arms install as a sibling `memory-tree` kit. It prints the ask
# projection a fixture file holds, so an arm can take ONE field away and watch its signal go DEAD.
_STUB_GENERATOR = """import json, pathlib, sys
rows = json.loads(pathlib.Path('projection.json').read_text(encoding='utf-8'))
if '--all' not in sys.argv:
    rows = [r for r in rows if r.get('status') not in ('CLOSED', 'WONTDO')]
print(json.dumps({'mode': 'builds', 'examined': 1, 'asks': rows}))
"""
_ASK_SIGNALS = ("backlog_asks_contested", "backlog_evidence_sha", "backlog_asks_unlabelled")


def test_backlog_ask_signals(tmp: pathlib.Path) -> None:
    """TOOL-dDerivedDocket-34 AC21: the builds-mode backlog signals, NOT ASKED, live, and DEAD.

    THREE STATES, EACH STAGED. Under `shards` the three report NOT ASKED and the live-row count
    still reads the shards; under `builds` with no `BACKLOG.md` tracked they are NOT ASKED too, the
    state right after an adopter sets the mode; and with a projection that lacks the field a signal
    reads, that signal alone prints DEAD PROBE — a projection that stopped emitting it is a probe
    that cannot move, and a clean zero there is the reassurance this kit refuses.
    """
    import json

    print("builds-mode backlog signals (TOOL-dDerivedDocket-34)")
    r = make_repo(tmp, name="asksignals")
    bl = r / "memory" / "backlog"
    bl.mkdir(parents=True, exist_ok=True)
    (bl / "ARCH.md").write_text("# ARCH backlog\n- ARCH-tLive-1 · OPEN · one\n",
                                encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "one shard", "--no-verify"], r)
    got = report(r)
    for name in _ASK_SIGNALS:
        check(f"[dDD-34] shards mode: {name} is NOT ASKED, never DEAD",
              got[name].get("not_asked") is True and got[name]["value"] == 0, f"{got[name]}")
    check("[dDD-34] shards mode: the live-row count still reads the shards",
          got["live_backlog_rows_per_shard"]["value"] == 1
          and got["live_backlog_rows_per_shard"]["live"] is True,
          f"{got['live_backlog_rows_per_shard']}")

    conf = (r / ".memory-tree.conf").read_text(encoding="utf-8")
    (r / ".memory-tree.conf").write_text(conf + 'BACKLOG_MODE="builds"\n',
                                         encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "builds mode, no ask file yet", "--no-verify"], r)
    got = report(r)
    for name in _ASK_SIGNALS:
        check(f"[dDD-34] builds mode, no BACKLOG.md: {name} is NOT ASKED, never DEAD",
              got[name].get("not_asked") is True, f"{got[name]}")

    _mt = resolve_kit_dir("memory-tree", "gen_build_index.py", KIT).name  # found, never typed
    (r / _mt).mkdir()
    (r / _mt / "gen_build_index.py").write_text(_STUB_GENERATOR, encoding="utf-8",
                                                          newline="\n")
    home = r / "memory" / "builds" / "aFoo"
    home.mkdir(parents=True, exist_ok=True)
    (home / "BACKLOG.md").write_text("# aFoo\n\n## Asks\n", encoding="utf-8", newline="\n")
    full = [{"id": "ARCH-aFoo-1", "status": "CLOSED", "closing": ["deadbeefdeadbeef"],
             "declining": ["aBar"], "live_specs": [], "sev": "unlabelled"},
            {"id": "ARCH-aFoo-2", "status": "OPEN", "closing": [], "declining": [],
             "live_specs": [], "sev": "unlabelled"}]
    (r / "projection.json").write_text(json.dumps(full), encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "an ask file and a stub projection", "--no-verify"], r)
    got = report(r)
    check("[dDD-34] contested: closing AND declining evidence on one ask is counted",
          got["backlog_asks_contested"]["value"] == 1 and got["backlog_asks_contested"]["live"],
          f"{got['backlog_asks_contested']}")
    check("[dDD-34] evidence sha: a `by` sha the object database cannot resolve is counted",
          got["backlog_evidence_sha"]["value"] == 1 and got["backlog_evidence_sha"]["live"],
          f"{got['backlog_evidence_sha']}")
    check("[dDD-34] unlabelled: a LIVE ask with no severity is counted, the terminal one not",
          got["backlog_asks_unlabelled"]["value"] == 1 and got["backlog_asks_unlabelled"]["live"],
          f"{got['backlog_asks_unlabelled']}")
    check("[dDD-34] builds mode: the live-row count is the LIVE projection's length",
          got["live_backlog_rows_per_shard"]["value"] == 1, f"{got['live_backlog_rows_per_shard']}")
    for name, field in (("backlog_asks_contested", "declining"), ("backlog_evidence_sha", "closing"),
                        ("backlog_asks_unlabelled", "sev")):
        rows = [{k: v for k, v in row.items() if k != field} for row in full]
        (r / "projection.json").write_text(json.dumps(rows), encoding="utf-8", newline="\n")
        dead = report(r)[name]
        check(f"[dDD-34] a projection lacking `{field}` makes {name} a DEAD PROBE, not a 0",
              dead["live"] is False and not dead.get("not_asked"), f"{dead}")

    # TOOL-aMendedFleet-55: live asks cited by product source, over the same stub projection. The
    # fixture's EVIDENCE_GLOBS is `src` minus `*.test.sh`; `-4` appears only inside `-41`.
    name = "open_asks_cited_by_product_source"
    asks = [{"id": f"ARCH-aFoo-{n}", "status": "OPEN"} for n in (2, 3, 4)]
    (r / "projection.json").write_text(json.dumps(asks), encoding="utf-8", newline="\n")
    (r / "src").mkdir(exist_ok=True)
    (r / "src" / "cites.py").write_text("# fixes ARCH-aFoo-2\n# and ARCH-aFoo-41, a longer sibling\n",
                                        encoding="utf-8", newline="\n")
    (r / "src" / "only.test.sh").write_text("# ARCH-aFoo-3\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "asks cited from source and from a test", "--no-verify"], r)
    got = report(r)[name]
    ids = [d["id"] for d in got.get("detail", [])]
    check("[aMF-55] cited asks: 1 of 3 live, report-only and pinless",
          (got["value"], got["of"], got["live"], got["gateable"], got["tolerance"])
          == (1, 3, True, False, None), f"{got}")
    check("[aMF-55] an ask cited from product source counts, with its status and path",
          {"id": "ARCH-aFoo-2", "status": "OPEN", "cited_in": ["src/cites.py"]} in got["detail"],
          f"{got['detail']}")
    check("[aMF-55] an ask cited only from a *.test.sh file does not count",
          "ARCH-aFoo-3" not in ids, f"{ids}")
    check("[aMF-55] a sibling id one digit longer does not count for the shorter id",
          "ARCH-aFoo-4" not in ids, f"{ids}")
    (r / "projection.json").write_text("not json", encoding="utf-8", newline="\n")
    dead = report(r)[name]
    check("[aMF-55] an unreadable projection reads not live, never not asked",
          dead["live"] is False and not dead.get("not_asked"), f"{dead}")


NL_ = chr(10)


def test_readme_mechanism_drift(tmp: pathlib.Path) -> None:
    """TOOL-dScriptedRepeat-14: a build README asserting a mechanism its own spec set has revised.

    Every arm here fixes the CLOCKS, because the predicate is entirely about which of two records
    spoke last. `GIT_AUTHOR_DATE` on the README commit sets the blame side; the revision log's own
    dates set the spec side. A fixture that let either float would be asserting over today's date."""
    print("readme mechanism drift")
    r = make_repo(tmp, name="rmdrift")
    bdir = (r / SPEC_DIR_FOR_FIXTURE).parent

    # THE README. Four authored claims and one generated one, chosen so each arm below has both
    # directions present in the SAME fixture — a corpus that only carries violations cannot tell a
    # working predicate from one that matches everything.
    readme = [
        "---",
        "slug: x",
        "---",
        "",
        "# a build",
        "",
        "The unit ships `--counts`, which takes the recorded FACTS.",
        "It also ships `--stable`, and nothing has moved it since.",
        "The run reaches `LANDED` at the end, which is a status and not a mechanism.",
        "Its entry point is `drift_report.py`, which is a file and not a mechanism.",
        "",
        "<!-- gen:build-units -->",
        "Rendered below this marker: `--generated-only` is not authored prose.",
        "<!-- /gen:build-units -->",
        "",
    ]
    (bdir / "README.md").write_text(NL_.join(readme) + NL_, encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "readme", "--no-verify"], r,
        env={"GIT_AUTHOR_DATE": "2026-01-02T00:00:00 +0000",
             "GIT_COMMITTER_DATE": "2026-01-02T00:00:00 +0000"})

    # THE SPEC SET. One revision AFTER the README line's date and three that are not, so the
    # `rd > d` comparison has a failing input as well as a passing one.
    spec = [
        "# TOOL-aDrift-1 - a drifting thing",
        "",
        "**Status:** INPROGRESS - rev-2 - 2026-01-05 - node a - Tier-2 - base 0000000",
        "",
        "## 9. Revision log",
        "",
        "- rev-2 - 2026-01-05 - `--counts` now takes a pinned BASE sha and re-parses the blob,",
        "  which is not what it did.",
        "- rev-1 - 2025-12-01 - `--stable` introduced, and `LANDED` and `drift_report.py` named here",
        "  so the shape filters below have an input rather than an absence to pass over.",
        "- rev-3 - 2026-01-09 - `--counts-format` is a DIFFERENT flag that merely STARTS WITH one the",
        "  README names. It is the latest entry here, so a bare-substring match would make it the",
        "  revision this row cites - and the row must cite rev-2 instead. This wording deliberately",
        "  never spells the shorter flag, because a fixture that mentions it grades its own prose.",
        "",
    ]
    (r / SPEC_DIR_FOR_FIXTURE / "2026-01-01-spec-aDrift-1.md").write_text(
        NL_.join(spec) + NL_, encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "spec", "--no-verify"], r)

    got = report(r)["readme_mechanism_drift"]
    toks = sorted(d["mechanism"] for d in got["detail"])
    check("AC1: the README claim its own spec later revised is reported",
          toks == ["--counts"], f"got {toks}")
    check("AC1: the row names both records",
          bool(got["detail"]) and got["detail"][0]["spec"].endswith("2026-01-01-spec-aDrift-1.md")
          and got["detail"][0]["readme"].endswith(":7"), f"got {got['detail'][:1]}")
    check("a revision EARLIER than the README line is not a hit", "--stable" not in toks)
    check("a status word is not a mechanism, so LANDED is not a hit", "LANDED" not in toks)
    check("a filename is not a mechanism, so drift_report.py is not a hit",
          "drift_report.py" not in toks)
    check("the generated region is not authored prose", "--generated-only" not in toks)
    # `--counts-format` is dated LATEST, so a bare-substring match would name rev-3 as the revision.
    # The row must still cite rev-2, which is the only entry that names `--counts` itself.
    check("a longer flag that merely starts with the token is not a match",
          bool(got["detail"]) and got["detail"][0]["revised"] == "2026-01-05",
          f"got {got['detail'][:1]}")
    check("the probe is LIVE with tokens and revisions present", got["live"] is True)
    # REPORT ONLY, for the reason F2 settled: `drift-audit records` is an unguarded merge-bar leg and
    # this predicate reports a POINTER, not a proven contradiction.
    check("the signal is not gateable", got["gateable"] is False)

    # --- TOOL-aMendedFleet-51 S4: a build whose every spec is CLOSED is a frozen record and is not
    # --- graded. EVERY spec of the build is flipped, `make_repo`'s SPECCED one included, because a
    # --- single live spec keeps the whole build graded. The arm above read one row from this tree.
    for _sp in sorted((r / SPEC_DIR_FOR_FIXTURE).glob("*.md")):
        _txt = _sp.read_text(encoding="utf-8")
        _sp.write_text(re.sub(r"^\*\*Status:\*\*\s*[A-Za-z]+", "**Status:** CLOSED", _txt, flags=re.M),
                       encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "close every spec", "--no-verify"], r)
    shut = report(r)["readme_mechanism_drift"]
    check("S4: a build whose every spec is CLOSED is not graded, so it reads zero rows",
          shut["value"] == 0 and shut["detail"] == [] and shut["of"] == 0,
          f"got value={shut['value']} of={shut['of']} rows={shut['detail'][:1]}")

    # --- AC2: a README and spec set that AGREE are silent, and the probe stays live -----------
    r2 = make_repo(tmp, name="rmagree")
    b2 = (r2 / SPEC_DIR_FOR_FIXTURE).parent
    (b2 / "README.md").write_text(
        "# a build" + NL_ + NL_ + "The unit ships `--counts`." + NL_,
        encoding="utf-8", newline="\n")
    (r2 / SPEC_DIR_FOR_FIXTURE / "2026-01-01-spec-aAgree-1.md").write_text(
        NL_.join([
            "# TOOL-aAgree-1 - a thing",
            "",
            "## 9. Revision log",
            "",
            "- rev-1 - 2025-12-01 - `--counts` introduced.",
            "",
        ]), encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r2)
    run(["git", "commit", "-q", "-m", "agree", "--no-verify"], r2,
        env={"GIT_AUTHOR_DATE": "2026-01-02T00:00:00 +0000",
             "GIT_COMMITTER_DATE": "2026-01-02T00:00:00 +0000"})
    ok = report(r2)["readme_mechanism_drift"]
    check("AC2: an agreeing pair reports nothing", ok["value"] == 0, f"got {ok['value']}")
    check("AC2: and the probe is still LIVE, so silence is a verdict rather than a blind spot",
          ok["live"] is True)

    # --- ROUND 7, MEDIUM 1: the two sides are dated on DIFFERENT CLOCKS unless the blame side
    # --- honours `author-tz`. The spec side is a hand-typed LOCAL date; reading `author-time` as UTC
    # --- backdates every README line written between 00:00 and 03:00 at +0300 and fires on a spec
    # --- revision made the same local day. On this repo that was 11 of 31 rows, and the shipped pin
    # --- was seeded through the skew. This arm is the one the existing fixtures could not be: every
    # --- other GIT_AUTHOR_DATE here is +0000, which is exactly the timezone that cannot show it.
    r4 = make_repo(tmp, name="rmtz")
    b4 = (r4 / SPEC_DIR_FOR_FIXTURE).parent
    (b4 / "README.md").write_text(
        "# a build" + NL_ + NL_ + "The unit ships `--counts`." + NL_,
        encoding="utf-8", newline="\n")
    (r4 / SPEC_DIR_FOR_FIXTURE / "2026-01-01-spec-aTz-1.md").write_text(
        NL_.join([
            "# TOOL-aTz-1 - a thing",
            "",
            "## 9. Revision log",
            "",
            "- rev-2 - 2026-01-02 - `--counts` revised on the same LOCAL day the README line was",
            "  written, which is only a hit if the two sides are read on different clocks.",
            "",
        ]), encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r4)
    # 01:00 at +0300 is 2026-01-01T22:00Z the day BEFORE. A UTC reader dates this line 2026-01-01 and
    # the rev-2 entry then compares as later; an author-tz reader dates it 2026-01-02 and it does not.
    run(["git", "commit", "-q", "-m", "tz", "--no-verify"], r4,
        env={"GIT_AUTHOR_DATE": "2026-01-02T01:00:00 +0300",
             "GIT_COMMITTER_DATE": "2026-01-02T01:00:00 +0300"})
    tz = report(r4)["readme_mechanism_drift"]
    check("MEDIUM 1: a README line and a spec revision on the same LOCAL day are not a hit",
          tz["value"] == 0, f"got {tz['value']} rows: {tz['detail'][:1]}")
    check("MEDIUM 1: and the probe is LIVE, so the zero is a verdict", tz["live"] is True)

    # --- ROUND 7, LOW 1: one row per README CLAIM, never one per backtick occurrence. `value` is
    # --- what the shipped pin ratchets against, and its comment says each row is one sentence to
    # --- re-read - which is false the moment a sentence naming a token twice counts twice.
    r5 = make_repo(tmp, name="rmdup")
    b5 = (r5 / SPEC_DIR_FOR_FIXTURE).parent
    (b5 / "README.md").write_text(
        "# a build" + NL_ + NL_
        + "It ships `--counts`, and `--counts` is the one that matters." + NL_,
        encoding="utf-8", newline="\n")
    (r5 / SPEC_DIR_FOR_FIXTURE / "2026-01-01-spec-aDup-1.md").write_text(
        NL_.join([
            "# TOOL-aDup-1 - a thing",
            "",
            "## 9. Revision log",
            "",
            "- rev-2 - 2026-01-05 - `--counts` now takes a pinned BASE sha.",
            "",
        ]), encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r5)
    run(["git", "commit", "-q", "-m", "dup", "--no-verify"], r5,
        env={"GIT_AUTHOR_DATE": "2026-01-02T00:00:00 +0000",
             "GIT_COMMITTER_DATE": "2026-01-02T00:00:00 +0000"})
    dup = report(r5)["readme_mechanism_drift"]
    check("LOW 1: a line naming one mechanism twice is ONE row",
          dup["value"] == 1, f"got {dup['value']}")

    # --- ROUND 7, LOW 3: the build slug comes from the DECLARED root. `MEMORY_ROOT` is not
    # --- constrained to one path segment and this repo's own manifest records `docs/mem` as a real
    # --- adopter value; an index-based split lands on the literal `builds` for every path and grades
    # --- every README against every build's revision log. One arm covers every future signal that
    # --- reaches for an index.
    r6 = make_repo(tmp, name="rmnested")
    (r6 / ".memory-tree.conf").write_text("MEMORY_ROOT=docs/mem" + NL_, encoding="utf-8", newline="\n")
    for _b in ("one", "two"):
        _d = r6 / "docs" / "mem" / "builds" / _b / "spec"
        _d.mkdir(parents=True, exist_ok=True)
        # THE TOKENS CROSS. Round 8's low 6: with each README naming its OWN build's token, a
        # slug collapse merges the spec sets and still yields the same row count as the correct
        # per-build grouping, so the count assertion passed with the fix reverted and only the
        # slug assertion discriminated. Build `one`'s README names `--two-flag`, which ONLY
        # build two's spec revises: a collapse produces rows here, correct grouping produces none.
        # Build `one` names BOTH tokens, build `two` names only its own. Correct grouping: one
        # row per build, two in total. A slug collapse grades every README against the merged
        # spec set and yields THREE, because one's `--two-flag` line then matches too. Both
        # assertions below discriminate; with each README naming only its own token neither did.
        _extra = (NL_ + "It also mentions `--two-flag`." + NL_) if _b == "one" else NL_
        (_d.parent / "README.md").write_text(
            "# build " + _b + NL_ + NL_ + "It ships `--" + _b + "-flag`." + _extra,
            encoding="utf-8", newline="\n")
        (_d / ("2026-01-01-spec-a" + _b + "-1.md")).write_text(
            NL_.join([
                "# TOOL-a" + _b + "-1 - a thing",
                "",
                # LIVE, so the build is graded at all (TOOL-aMendedFleet-51 S4).
                "**Status:** INPROGRESS - rev-2 - 2026-01-05 - node a - Tier-2 - base 0000000",
                "",
                "## 9. Revision log",
                "",
                "- rev-2 - 2026-01-05 - `--" + _b + "-flag` was revised here.",
                "",
            ]), encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r6)
    run(["git", "commit", "-q", "-m", "nested", "--no-verify"], r6,
        env={"GIT_AUTHOR_DATE": "2026-01-02T00:00:00 +0000",
             "GIT_COMMITTER_DATE": "2026-01-02T00:00:00 +0000"})
    nest = report(r6)["readme_mechanism_drift"]
    slugs = sorted({d["build"] for d in nest["detail"]})
    check("LOW 3: a two-segment MEMORY_ROOT still names the BUILD, not the literal `builds`",
          slugs == ["one", "two"], f"got {slugs}")
    check("LOW 3: and each README grades against its OWN spec set only",
          nest["value"] == 2, f"got {nest['value']} rows: {nest['detail'][:3]}")

    # --- AC4: LIVENESS over the population that CAN empty. Not "did I find a build" - the tree
    # --- always has builds - but "did I find a mechanism token to compare against a revision".
    r3 = make_repo(tmp, name="rmdead")
    b3 = (r3 / SPEC_DIR_FOR_FIXTURE).parent
    (b3 / "README.md").write_text(
        "# a build" + NL_ + NL_ + "Prose with no backticked mechanism in it." + NL_,
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r3)
    run(["git", "commit", "-q", "-m", "no tokens", "--no-verify"], r3)
    dead = report(r3)["readme_mechanism_drift"]
    check("AC4: a corpus with no mechanism token reports DEAD rather than a reassuring 0",
          dead["live"] is False, f"live={dead['live']} value={dead['value']}")


def test_declared_empty(tmp: pathlib.Path) -> None:
    """A declaration must stay LIFTABLE, or it is the DEAD PROBE defect wearing a nicer label.

    Direction one on its own — drain the population, declare it, watch `--check` go quiet — is
    indistinguishable from a probe that has simply gone blind, because that is exactly what a blind
    probe looks like too. Putting one row back and watching the same signal score again separates
    "empty on purpose" from "cannot see". All three directions run over ONE fixture, so the ledger
    row and the declaration are the only variables between them.

    WHY THREE DIRECTIONS AND NOT TWO. The earlier pair restored the row and STRIPPED the declaration
    in the same step, so the arm carrying the words "the declaration was not a muzzle" ran against a
    tree that no longer held the declaration — it asserted that the PROBE works, which nobody
    doubted, and said nothing about what the declaration does while it is in place. Measured: adding
    `and s["signal"] not in declared` to the over-pin filter in `drift_report.py`, i.e. turning
    DECLARED_EMPTY into an unconditional silencer, left that pair green, `check-arms.py` green,
    `--check` green and the codebase-map leg green. So direction two now restores the row with the
    declaration KEPT and demands `--check` red anyway: DECLARED_EMPTY excuses an EMPTY population
    from the dead-probe rule and NOTHING else. Direction three lifts the declaration as the control,
    proving that red is unchanged by the declaration rather than caused by it.
    """
    print("DECLARED_EMPTY (a drained probe reports declared, never muzzles a live one, and LIFTS)")
    r = make_repo(tmp, name="declared")
    sig = r / KIT_NAME / "drift_signals.py"
    ledger_dir = r / "memory" / "project" / "in-flight"

    # --- direction one: the population is drained and the emptiness is declared ----------------
    for f in sorted(ledger_dir.glob("*.md")):
        f.unlink()
    ledger_dir.rmdir()
    sig.write_text(sig.read_text(encoding="utf-8").replace(
        "DECLARED_EMPTY = {'handkept_inventories_disagreeing_with_source'}",
        "DECLARED_EMPTY = {'handkept_inventories_disagreeing_with_source',"
        " 'ledger_rows_contradicting_git'}"),
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "retire the ledger", "--no-verify"], r)

    drained = report(r)["ledger_rows_contradicting_git"]
    check("drained: the ledger probe is no longer live", drained["live"] is False,
          f"live={drained['live']}")
    check("drained: it reports 0 rather than a stale count", drained["value"] == 0,
          f"got {drained['value']}")
    quiet = run([sys.executable, REPORT_REL, "--check"], r)
    check("drained + declared: --check stays green", quiet.returncode == 0,
          f"rc={quiet.returncode} stderr={quiet.stderr.strip()[:200]}")

    # THE DISCRIMINATING ASSERTION of direction one. The three above hold just as well for a signal
    # `--check` is merely ignoring; only the PRINTED status tells a reader "empty on purpose" from
    # "blind", and that line is the one a human acts on.
    human = run([sys.executable, REPORT_REL], r)
    row = next((ln for ln in human.stdout.splitlines()
                if "ledger_rows_contradicting_git" in ln), "")
    check("drained + declared: the printed row reads 'empty by declaration'",
          "empty by declaration" in row, f"row={row.strip()!r}")
    check("drained + declared: and NOT 'DEAD PROBE'",
          bool(row) and "DEAD PROBE" not in row, f"row={row.strip()!r}")

    # --- direction two: one row returns and the declaration STAYS — the muzzle arm --------------
    # The declaration is deliberately NOT touched here. This is the only configuration in which the
    # words "the declaration was not a muzzle" mean anything: population non-empty, signal over its
    # pin, declaration in force. Every arm below must hold with `ledger_rows_contradicting_git`
    # still listed in DECLARED_EMPTY.
    sha = run(["git", "rev-parse", "--short", "HEAD"], r).stdout.strip()
    assert len(sha) >= 7, f"fixture HEAD sha not produced: {sha!r}"
    ledger_dir.mkdir(parents=True)
    # The row shape `make_repo` already writes. `BASESHA` is deliberately NOT hex, so `_SHA` finds
    # exactly one sha in the line and the arm isolates the oracle rather than the row's wording.
    (ledger_dir / "a.md").write_text(
        "| slug | branch | status |\n|---|---|---|\n"
        f"| `aThing` | `feature/x` off `BASESHA` | in-flight — NOT merged, work at `{sha}` |\n",
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "a ledger row returns, still declared", "--no-verify"], r)
    # ASSERTED, not assumed. If a future edit moves the strip above this point, these arms silently
    # become direction three all over again — which is precisely the defect being repaired here.
    assert "'ledger_rows_contradicting_git'" in sig.read_text(encoding="utf-8"), \
        "direction two must run with the declaration STILL in place"

    still = report(r)["ledger_rows_contradicting_git"]
    check("still declared, a row returns: the probe is LIVE again",
          still["live"] is True, f"live={still['live']}")
    check("still declared, a row returns: and it scores the contradiction", still["value"] == 1,
          f"got {still['value']}")
    # THE DISCRIMINATING ARM. A declaration that survived into the over-pin filter would green this.
    muzzle = run([sys.executable, REPORT_REL, "--check"], r)
    check("still declared, a row returns: --check REDS — the declaration was not a muzzle",
          muzzle.returncode == 1, f"rc={muzzle.returncode} stderr={muzzle.stderr.strip()[:200]}")
    check("still declared, a row returns: ...and names the signal on stderr",
          "ledger_rows_contradicting_git" in muzzle.stderr,
          f"stderr={muzzle.stderr.strip()[:200]}")
    # ...and the human-facing print must stop excusing it too. The status ladder reads the same
    # declaration set, so a muzzle can hide there just as easily as in the gate.
    printed = run([sys.executable, REPORT_REL], r)
    prow = next((ln for ln in printed.stdout.splitlines()
                 if "ledger_rows_contradicting_git" in ln), "")
    check("still declared, a row returns: the printed row reads OVER PIN, not 'empty by declaration'",
          "OVER PIN" in prow and "empty by declaration" not in prow, f"row={prow.strip()!r}")

    # --- direction three: lift the declaration — the CONTROL for direction two ------------------
    # One variable changes and nothing else: the same tree, the same row, no declaration. If
    # direction two's red had come from some other signal, this arm would be indistinguishable from
    # it; instead it pins the verdict as UNCHANGED by the declaration, which is what "not a muzzle"
    # asserts.
    sig.write_text(sig.read_text(encoding="utf-8").replace(
        ", 'ledger_rows_contradicting_git'", ""), encoding="utf-8", newline="\n")
    assert "'ledger_rows_contradicting_git'" not in sig.read_text(encoding="utf-8"), \
        "the declaration was not actually lifted — direction three would restate direction two"
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "lift the declaration", "--no-verify"], r)

    back = report(r)["ledger_rows_contradicting_git"]
    check("declaration lifted: the probe is still LIVE", back["live"] is True, f"live={back['live']}")
    check("declaration lifted: and still scores the contradiction", back["value"] == 1,
          f"got {back['value']}")
    fires = run([sys.executable, REPORT_REL, "--check"], r)
    check("declaration lifted: --check reds identically", fires.returncode == 1,
          f"rc={fires.returncode}")
    check("declaration lifted: ...and names the signal on stderr",
          "ledger_rows_contradicting_git" in fires.stderr,
          f"stderr={fires.stderr.strip()[:200]}")


def test_handkept_name_sets(tmp: pathlib.Path) -> None:
    """A HANDKEPT probe returning two SETS scores their symmetric difference and names both halves
    (TOOL-aMendedFleet-52). The fixture row's actual half is `ctx.signal_names`, so the arm also
    proves `main` hands the hand-kept signal the names every other signal reported."""
    import json

    print("HANDKEPT name sets (equal reads 0 and live; a missing and a stale name each count one)")
    r = make_repo(tmp, name="namesets")
    names = sorted(report(r))
    claims = r / "names.txt"
    sig = r / KIT_NAME / "drift_signals.py"
    text = sig.read_text(encoding="utf-8")
    assert text.count("HANDKEPT = []\n") == 1, "fixture HANDKEPT literal moved; this arm would test nothing"
    sig.write_text(text.replace("HANDKEPT = []\n", (
        "def read_fixture_names(ctx):\n"
        "    import pathlib\n"
        "    got = (pathlib.Path(ctx.root) / 'names.txt').read_text(encoding='utf-8').split()\n"
        "    return set(got), set(ctx.signal_names)\n"
        "HANDKEPT = [{'record': 'names.txt', 'source': 'the engine', 'probe': read_fixture_names}]\n")),
        encoding="utf-8", newline="\n")

    def read_row(claimed: list[str]) -> tuple[dict, dict]:
        claims.write_text("\n".join(claimed) + "\n", encoding="utf-8", newline="\n")
        rec = report(r)["handkept_inventories_disagreeing_with_source"]
        return rec, (rec["detail"][0] if rec["detail"] else {})

    rec, row = read_row(names)
    check("name sets: equal sets read 0 and live", rec["value"] == 0 and rec["live"] is True,
          f"value={rec['value']} live={rec['live']} row={json.dumps(row)[:200]}")
    check("name sets: the population is every reported name", rec["of"] == len(names),
          f"of={rec['of']} names={len(names)}")
    check("name sets: claims and actual are serialised as counts",
          row.get("claims") == len(names) and row.get("actual") == len(names), json.dumps(row)[:200])

    dropped = "closed_specs_with_no_product_commit"
    assert dropped in names, f"{dropped} is not a reported signal; this arm would drop nothing"
    rec, row = read_row([n for n in names if n != dropped])
    check("name sets: a name missing from the claims counts one", rec["value"] == 1,
          f"value={rec['value']}")
    check("name sets: ...and is named under missing", row.get("missing") == [dropped],
          json.dumps(row)[:200])
    check("name sets: ...and nothing under extra", row.get("extra") == [], json.dumps(row)[:200])

    rec, row = read_row(names + ["no_such_signal"])
    check("name sets: a stale extra name counts one", rec["value"] == 1, f"value={rec['value']}")
    check("name sets: ...and is named under extra", row.get("extra") == ["no_such_signal"],
          json.dumps(row)[:200])
    check("name sets: ...and the population is the union", rec["of"] == len(names) + 1,
          f"of={rec['of']}")


def test_ratchet_guard(tmp: pathlib.Path) -> None:
    """A pin RAISE and a population DRAIN look identical to `value > pin` — TOOL-aNumeralWarden-3.

    Three directions over ONE fixture, so the justification comment is the only variable between the
    two that matter. Direction one moves a declared scalar in its WEAKENING direction with nothing
    beside it and demands red. Direction two makes the IDENTICAL move with a justification naming
    both numbers and demands green — without it, direction one would pass just as well against a
    guard that refused every edit to the file, which is a different and useless check. Direction
    three moves the same scalar the TIGHTENING way, unjustified, and demands green: a ratchet that
    also refuses improvement is a ratchet nobody will turn.
    """
    print("RATCHET guard (a weakening move needs a reason; a tightening one never does)")
    r = make_repo(tmp, name="ratchet")
    conf = r / ".memory-tree.conf"
    sig = r / KIT_NAME / "drift_signals.py"

    # The pin must be COMMITTED before the arm moves it: the guard compares the working copy against
    # `git show <base>:<file>`, so a pin that exists only in the working tree has no prior value and
    # is correctly ignored. Seeding it in the working tree alone would make every direction below
    # pass by finding nothing.
    conf.write_text(conf.read_text(encoding="utf-8") + 'ORPHAN_ID_PIN="5"\n',
                    encoding="utf-8", newline="\n")
    # `make_repo` writes its own MINIMAL signals module, so there is no RATCHETS list to edit —
    # appending one is the only thing that arms this fixture. A `.replace()` against a string this
    # file does not contain is a no-op, and every direction below then grades an empty declaration
    # and passes by finding nothing. That is exactly what the first cut of this arm did.
    sig.write_text(
        sig.read_text(encoding="utf-8")
        + 'RATCHETS = [{"file": ".memory-tree.conf", "key": "ORPHAN_ID_PIN", "weakens": "up"}]\n',
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    seeded = run(["git", "commit", "-q", "-m", "seed the ratchet", "--no-verify"], r)
    check("the ratchet fixture committed its seed", seeded.returncode == 0,
          (seeded.stdout + seeded.stderr)[-200:])
    # The base value has to be READABLE, or every direction is a skip wearing a pass.
    at_base = run(["git", "show", "main:.memory-tree.conf"], r)
    check("the pin is readable at the fixture's base",
          at_base.returncode == 0 and 'ORPHAN_ID_PIN="5"' in at_base.stdout,
          at_base.stdout[-200:])
    committed = conf.read_text(encoding="utf-8")

    def _check() -> subprocess.CompletedProcess:
        return run([sys.executable, str(r / KIT_NAME / "drift_report.py"), "--check"], r)

    base_ok = _check()
    check("the fixture is clean before the arm", base_ok.returncode == 0,
          (base_ok.stdout + base_ok.stderr)[-400:])

    # --- direction one: weakened, unjustified -------------------------------------------------
    conf.write_text(committed.replace('ORPHAN_ID_PIN="5"', 'ORPHAN_ID_PIN="9"'),
                    encoding="utf-8", newline="\n")
    out = _check()
    check("an unjustified RAISE is refused",
          out.returncode != 0 and "RATCHET WEAKENED" in out.stderr,
          (out.stdout + out.stderr)[-400:])

    # --- direction two: the SAME raise, justified in place ------------------------------------
    justified = "# RAISED 5 -> 9 because the fixture says so.\n" + 'ORPHAN_ID_PIN="9"'
    conf.write_text(committed.replace('ORPHAN_ID_PIN="5"', justified),
                    encoding="utf-8", newline="\n")
    out = _check()
    check("the same RAISE with a justification naming both values is allowed",
          out.returncode == 0 and "RATCHET WEAKENED" not in out.stderr,
          (out.stdout + out.stderr)[-400:])

    # --- direction three: TIGHTENED, unjustified ----------------------------------------------
    # A ratchet that also refuses improvement is a ratchet nobody turns, so this direction must be
    # free. Without it, direction one would pass equally against a guard that refused any edit.
    conf.write_text(committed.replace('ORPHAN_ID_PIN="5"', 'ORPHAN_ID_PIN="1"'),
                    encoding="utf-8", newline="\n")
    out = _check()
    check("a tightening move needs no justification",
          out.returncode == 0 and "RATCHET WEAKENED" not in out.stderr,
          (out.stdout + out.stderr)[-400:])



def test_baselines(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-56 — a gateable signal bounded by WHICH offenders it holds, not how many.

    One fixture, signal 2 baselined at one listed id. Each arm moves one thing from the committed
    state and demands red, and the clean state and the equal-seed arm demand green, so a guard that
    refused every edit fails here as surely as one that refused none.
    """
    print("BASELINES (an equal-count swap, a drain and a growth each red)")
    r = make_repo(tmp, name="baselines")
    sig = r / KIT_NAME / "drift_signals.py"
    app = r / "src" / "app.py"
    name = "non_terminal_specs_cited_by_product_source"
    # A second SPECCED spec, so the swap has an id to swap in at an equal count.
    (r / SPEC_DIR_FOR_FIXTURE / "2026-01-01-spec-aOther-1.md").write_text(
        "# TOOL-aOther-1 — another thing\n\n"
        "**Status:** SPECCED · rev-1 · 2026-01-01 · node a · Tier-2 · base 0000000\n",
        encoding="utf-8", newline="\n")
    app.write_text("# implements TOOL-aThing-1\n", encoding="utf-8", newline="\n")
    # The layer sits INSIDE the evidence globs, as it does in this repo, so the drain arm also proves
    # that a list spelling an id is not a citation of it (S10).
    layer = sig.read_text(encoding="utf-8").replace(
        "EVIDENCE_GLOBS = ['src', ", "EVIDENCE_GLOBS = ['src', '" + KIT_NAME + "', ")
    seeded = layer + "BASELINES = {'" + name + "': ['TOOL-aThing-1']}\n"
    sig.write_text(seeded, encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "seed the baseline", "--no-verify"], r)

    def run_check() -> subprocess.CompletedProcess:
        return run([sys.executable, REPORT_REL, "--check"], r)

    clean = run_check()
    rec = report(r)[name]
    check("baselines: the seeded fixture is green, with the fields and nothing new or stale",
          clean.returncode == 0 and rec.get("baseline") == 1 and rec.get("new") == []
          and rec.get("stale") == [], f"rc={clean.returncode} {clean.stderr.strip()[-300:]} rec={rec}")

    # --- an equal-count SWAP: the defect a count could not see ----------------------------------
    app.write_text("# implements TOOL-aOther-1\n", encoding="utf-8", newline="\n")
    swap = run_check()
    offs = run([sys.executable, REPORT_REL, "--offenders"], r).stdout.splitlines()
    check("baselines: the swap leaves the count at the listed size", report(r)[name]["value"] == 1)
    check("baselines: an equal-count swap reds, keying the new row and the stale id",
          swap.returncode == 1 and any("TOOL-aOther-1" in ln for ln in offs)
          and f'{name}\t{{"stale": "TOOL-aThing-1"}}' in offs, f"rc={swap.returncode} {offs}")

    # --- a DRAIN: a listed id no row carries reds until its line goes --------------------------
    app.write_text("# nothing cited here\n", encoding="utf-8", newline="\n")
    drain = run_check()
    check("baselines: a drained listed id reds as stale though the layer still spells it",
          drain.returncode == 1 and "stale TOOL-aThing-1" in drain.stderr,
          f"rc={drain.returncode} {drain.stderr.strip()[-300:]}")

    # --- GROWTH against a committed base that lists the signal ---------------------------------
    app.write_text("# implements TOOL-aThing-1 and TOOL-aOther-1\n", encoding="utf-8", newline="\n")
    sig.write_text(seeded.replace("['TOOL-aThing-1']", "['TOOL-aThing-1', 'TOOL-aOther-1']"),
                   encoding="utf-8", newline="\n")
    grown = run_check()
    check("baselines: a set gaining an id against its base reds as a weakened ratchet",
          grown.returncode == 1 and "RATCHET WEAKENED" in grown.stderr
          and "gained TOOL-aOther-1" in grown.stderr, f"rc={grown.returncode} {grown.stderr.strip()[-300:]}")

    # --- the FIRST seed is bounded by the pin the base held ------------------------------------
    pinned = layer.replace("PINS = {}", "PINS = {'" + name + "': 1}")
    sig.write_text(pinned, encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "a pin at the base", "--no-verify"], r)
    sig.write_text(layer + "BASELINES = {'" + name + "': ['TOOL-aThing-1', 'TOOL-aOther-1']}\n",
                   encoding="utf-8", newline="\n")
    over = run_check()
    check("baselines: a first seed above the base's pin reds",
          over.returncode == 1 and "seeded with 2 ids where the base pins it at 1" in over.stderr,
          f"rc={over.returncode} {over.stderr.strip()[-300:]}")
    app.write_text("# implements TOOL-aThing-1\n", encoding="utf-8", newline="\n")
    sig.write_text(seeded, encoding="utf-8", newline="\n")
    equal = run_check()
    check("baselines: a first seed at the base's pin is green", equal.returncode == 0,
          f"rc={equal.returncode} {equal.stderr.strip()[-300:]}")

    # --- ONE bound per signal -------------------------------------------------------------------
    sig.write_text(seeded.replace("PINS = {}", "PINS = {'" + name + "': 1}"),
                   encoding="utf-8", newline="\n")
    both = run([sys.executable, REPORT_REL, "--check"], r)
    check("baselines: a signal in both PINS and BASELINES is refused with exit 2 before any line",
          both.returncode == 2 and not both.stdout.strip() and "PINS and BASELINES" in both.stderr,
          f"rc={both.returncode} out={both.stdout[:120]!r} {both.stderr.strip()[-200:]}")
    sig.write_text(seeded, encoding="utf-8", newline="\n")

    # --- TOOL-aMendedFleet-110: a MOVE out of BASELINES into PINS is graded against the base ----
    # The seeded set becomes the base first: the arms above end on a base that pins the signal.
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "the seeded set is the base", "--no-verify"], r)
    sys.path.insert(0, str(KIT))
    import drift_report as dr
    moved = dr.build_baseline_findings(
        dr.Git(r, "HEAD"), f"{ROOT_PFX}{KIT_NAME}/drift_signals.py",
        {"closed_specs_with_no_product_commit": []}, {name: 2})
    check("baselines: a set moved to PINS above the base's size is one finding naming it",
          len(moved) == 1 and f"{name!r} moved" in moved[0] and "WEAKENS" in moved[0], repr(moved))
    sig.write_text(layer.replace("PINS = {}", "PINS = {'" + name + "': 2}"),
                   encoding="utf-8", newline="\n")
    emptied = run_check()
    check("baselines: no BASELINES and the signal pinned above the base's size reds",
          emptied.returncode == 1 and "RATCHET WEAKENED" in emptied.stderr
          and f"{name!r} moved" in emptied.stderr,
          f"rc={emptied.returncode} {emptied.stderr.strip()[-300:]}")
    sig.write_text(layer.replace("PINS = {}", "PINS = {'" + name + "': 1}"),
                   encoding="utf-8", newline="\n")
    at_size = run_check()
    check("baselines: a move pinned at the base set's size is green", at_size.returncode == 0,
          f"rc={at_size.returncode} {at_size.stderr.strip()[-300:]}")
    sig.write_text(seeded, encoding="utf-8", newline="\n")


def test_shrink_low_water(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-57: a shrink-only list is graded against the lowest count its first-parent
    history reached, so one that drained and grew back is `regrown` while still under its seed."""
    import types
    print("shrink-only low-water (truth table + a list committed at 3, 1, 2)")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    # The truth table over the predicate: (seed, low_water, entries) -> reason.
    for args, want in (((3, 1, 2), "regrown"), ((0, 0, 4), "regrown"), ((2, 2, 2), "never drained"),
                       ((2, 1, 1), None), ((0, 0, 0), None), ((4, 0, 0), None), ((2, 2, -1), None)):
        check(f"check_shrink_row{args} reads {want!r}", dr.check_shrink_row(*args) == want,
              repr(dr.check_shrink_row(*args)))

    r = tmp / "low-water"
    r.mkdir()
    run(["git", "init", "-q", "-b", "main"], r)
    run(["git", "config", "user.email", "selftest@example.com"], r)
    run(["git", "config", "user.name", "selftest"], r)
    lst = r / "list.txt"
    for n in (3, 1, 2):
        lst.write_text("# header\n\n" + "".join(f"row-{i}\n" for i in range(n)),
                       encoding="utf-8", newline="\n")
        run(["git", "add", "-A"], r)
        run(["git", "commit", "-q", "-m", f"list at {n}", "--no-verify"], r)
    ctx = types.SimpleNamespace(root=r, git=dr.Git(r, "main"),
                                shrink_only={"list.txt": "a list", "never.txt": "never committed"})
    got = dr.derive_low_waters(ctx.git, list(ctx.shrink_only))
    check("the replay reads the list's low-water as 1", got.get("list.txt") == 1, repr(got))
    check("a path with no history has no low-water", got.get("never.txt") is None, repr(got))
    sig = dr.signal_shrink_only(ctx)
    row = next(x for x in sig["detail"] if x["file"] == "list.txt")
    check("the seed reading calls the list shrinking (shrunk_by 1)", row["shrunk_by"] == 1, repr(row))
    check("...and the low-water reading names it regrown", row["reason"] == "regrown", repr(row))
    check("the regrown list is the one offender, the historyless one unjudgeable",
          sig["value"] == 1 and sig["unjudgeable"] == 1, repr(sig))


def test_base_is_remote_tracking(tmp: pathlib.Path) -> None:
    """The comparison base is the REMOTE-TRACKING ref — TOOL-dDerivedDocket-21 S1 and S2, AC1 and AC2.

    A pin raise that already LANDED on origin is the whole shape of the defect. Against the bare
    branch name the report read the node's LOCAL main, so one commit graded a WEAKENED RATCHET on a
    node whose local main was behind the raise and graded clean on every other node. Three states of
    local main over ONE fixture — behind the raise, equal to origin, ahead by an unrelated commit —
    must report the same signal values and the same verdict.

    THE CONTROL IS WHAT MAKES THE THREE GREENS MEAN SOMETHING. The same behind state measured with
    `--base-ref refs/heads/main`, the base the report used to take, must red: without it the three
    agreeing states would pass just as well over a fixture whose raise never reached the ratchet.
    """
    import json

    print("BASE is remote-tracking (local main behind, equal and ahead of origin: one answer)")
    r = make_repo(tmp, name="remotebase")
    conf = r / ".memory-tree.conf"
    sig = r / KIT_NAME / "drift_signals.py"
    conf.write_text(conf.read_text(encoding="utf-8") + 'ORPHAN_ID_PIN="5"\n',
                    encoding="utf-8", newline="\n")
    sig.write_text(
        sig.read_text(encoding="utf-8")
        + 'RATCHETS = [{"file": ".memory-tree.conf", "key": "ORPHAN_ID_PIN", "weakens": "up"}]\n',
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "seed the ratchet", "--no-verify"], r)
    before = run(["git", "rev-parse", "HEAD"], r).stdout.strip()

    bare = tmp / "remotebase.git"
    run(["git", "init", "-q", "--bare", str(bare)], tmp)
    run(["git", "remote", "add", "origin", str(bare)], r)
    # THE RAISE, UNJUSTIFIED, pushed — what a raise another node already landed looks like from here.
    conf.write_text(conf.read_text(encoding="utf-8").replace('ORPHAN_ID_PIN="5"', 'ORPHAN_ID_PIN="9"'),
                    encoding="utf-8", newline="\n")
    run(["git", "commit", "-q", "-am", "raise the pin on origin", "--no-verify"], r)
    tip = run(["git", "rev-parse", "HEAD"], r).stdout.strip()
    pushed = run(["git", "push", "-q", "origin", "main"], r)
    tracked = run(["git", "rev-parse", "--verify", "--quiet", "refs/remotes/origin/main"], r)
    check("the fixture's origin carries the raise, and the tracking ref names it",
          pushed.returncode == 0 and tracked.stdout.strip() == tip,
          (pushed.stdout + pushed.stderr)[-300:])
    # HEAD stays AT the raise throughout; only local main moves. Detached, so `branch -f` may move it.
    run(["git", "checkout", "-q", "--detach", tip], r)

    def read_signal_values(*extra: str) -> tuple:
        out = run([sys.executable, REPORT_REL, "--json", "--check", *extra], r)
        try:
            vals = {s["signal"]: (s["value"], s["live"]) for s in json.loads(out.stdout)}
        except ValueError:
            vals = {}
        return vals, out

    run(["git", "branch", "-f", "main", before], r)
    behind, behind_out = read_signal_values()
    run(["git", "branch", "-f", "main", tip], r)
    equal, equal_out = read_signal_values()
    run(["git", "checkout", "-q", "main"], r)
    (r / "src" / "unrelated.txt").write_text("local only\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "an unrelated local commit", "--no-verify"], r)
    run(["git", "checkout", "-q", "--detach", tip], r)
    ahead, ahead_out = read_signal_values()

    check("AC1: the report produced signals in all three states",
          bool(behind) and bool(equal) and bool(ahead),
          (behind_out.stderr + equal_out.stderr + ahead_out.stderr)[-400:])
    check("AC1: local main BEHIND the raise reports the same signal values as EQUAL",
          behind == equal, f"{behind} vs {equal}")
    check("AC1: local main AHEAD by an unrelated commit reports the same signal values as EQUAL",
          ahead == equal, f"{ahead} vs {equal}")
    for label, out in (("behind", behind_out), ("equal", equal_out), ("ahead", ahead_out)):
        check(f"AC1: {label}: the landed raise is NOT a weakened ratchet",
              out.returncode == 0 and "RATCHET WEAKENED" not in out.stderr,
              (out.stdout[-200:] + out.stderr)[-400:])

    # THE CONTROL: the base the report used to take, over the behind state.
    run(["git", "branch", "-f", "main", before], r)
    _vals, stale = read_signal_values("--base-ref", "refs/heads/main")
    check("control: against the stale LOCAL main the same raise reds as a weakened ratchet",
          stale.returncode != 0 and "RATCHET WEAKENED" in stale.stderr,
          (stale.stdout[-200:] + stale.stderr)[-400:])
    run(["git", "branch", "-f", "main", tip], r)

    # AC2 — the header carries the base ref AND an eight-hex sha.
    head = run([sys.executable, REPORT_REL], r)
    first = head.stdout.splitlines()[0] if head.stdout.strip() else ""
    check("AC2: the header names refs/remotes/origin/main and the sha it resolved to",
          re.search(r"\(base refs/remotes/origin/main @ [0-9a-f]{8}\)", first) is not None,
          first or head.stderr[-300:])

    # AC2 — `origin` configured, no tracking ref: a refusal naming the fetch, never a silent fallback.
    run(["git", "update-ref", "-d", "refs/remotes/origin/main"], r)
    unf = run([sys.executable, REPORT_REL, "--json"], r)
    check("AC2: origin with no tracking ref REFUSES with exit 2",
          unf.returncode == 2 and not unf.stdout.strip(), f"rc={unf.returncode} {unf.stdout[-200:]}")
    check("AC2: ...and the refusal names `git fetch origin main`",
          "git fetch origin main" in unf.stderr, unf.stderr[-400:])

    # AC2 — no `origin` at all: the local branch IS the record, and the report says so.
    run(["git", "remote", "remove", "origin"], r)
    loc = run([sys.executable, REPORT_REL, "--json", "--check"], r)
    check("AC2: a clone with no remote at all names the LOCAL base on stderr",
          re.search(r"no remote, so the base is local main @ [0-9a-f]{8}", loc.stderr)
          is not None, loc.stderr[-400:])
    check("AC2: ...and exits as the signals decide, here clean",
          loc.returncode == 0, (loc.stdout[-200:] + loc.stderr)[-400:])
    txt = run([sys.executable, REPORT_REL], r)
    first = txt.stdout.splitlines()[0] if txt.stdout.strip() else ""
    check("AC2: ...and its header reads refs/heads/main with an eight-hex sha",
          re.search(r"\(base refs/heads/main @ [0-9a-f]{8}\)", first) is not None,
          first or txt.stderr[-300:])

    # TOOL-dLadderedRemote-2 — the remote is the LADDER'S, not one called `origin`. Every env value
    # is cleared, so the answer is the repository's own and an ambient export cannot pass an arm.
    clear = {"GOV_DEFAULT_BRANCH": "", "GOV_REMOTE": ""}
    run(["git", "remote", "add", "upstream", str(bare)], r)
    run(["git", "update-ref", "refs/remotes/upstream/main", tip], r)
    run(["git", "symbolic-ref", "refs/remotes/upstream/HEAD", "refs/remotes/upstream/main"], r)
    one = run([sys.executable, REPORT_REL], r, env=clear)
    first = one.stdout.splitlines()[0] if one.stdout.strip() else ""
    check("AC1 (dLadderedRemote): the ONLY remote named upstream resolves refs/remotes/upstream/main",
          re.search(r"\(base refs/remotes/upstream/main @ [0-9a-f]{8}\)", first) is not None,
          first or one.stderr[-300:])
    run(["git", "remote", "add", "origin", str(bare)], r)
    two = run([sys.executable, REPORT_REL, "--json"], r, env=clear)
    check("AC2 (dLadderedRemote): two remotes and none chosen REFUSES with exit 2",
          two.returncode == 2 and not two.stdout.strip(), f"rc={two.returncode} {two.stdout[-200:]}")
    check("AC2 (dLadderedRemote): ...and the refusal names GOV_REMOTE",
          "export GOV_REMOTE=<remote>" in two.stderr, two.stderr[-400:])
    chosen = run([sys.executable, REPORT_REL], r, env={**clear, "GOV_REMOTE": "upstream"})
    first = chosen.stdout.splitlines()[0] if chosen.stdout.strip() else ""
    check("AC3 (dLadderedRemote): GOV_REMOTE=upstream beside origin resolves refs/remotes/upstream/main",
          re.search(r"\(base refs/remotes/upstream/main @ [0-9a-f]{8}\)", first) is not None,
          first or chosen.stderr[-300:])


def test_ratchet_lookback(tmp: pathlib.Path) -> None:
    """The justification WINDOW is a project-layer declaration — TOOL-aDeclaredBound-3.

    Both directions over ONE fixture: the same pin, the same justification, the same distance, and
    only the declared window moving. A one-directional arm would pass under any window wide enough,
    which is the failure mode a tunable threshold invites. The shipped default is asserted against
    the module constant rather than a retyped 14, so an arm cannot agree with itself.
    """
    print("RATCHET_LOOKBACK (a declared window, both directions over one fixture)")
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from drift_report import _justified, _read_lookback, DEFAULT_RATCHET_LOOKBACK, DriftError

    lines = ["# filler"] * 21
    lines[10] = "# RAISED 5 -> 8 because the measurement said so"
    text = "\n".join(lines)

    check("a justification ten lines up is INSIDE the shipped window",
          _justified(text, 20, 5, 8, DEFAULT_RATCHET_LOOKBACK))
    check("...and OUTSIDE a declared window of five",
          not _justified(text, 20, 5, 8, 5))
    check("...and inside a declared eleven, so the boundary moves with the number",
          _justified(text, 20, 5, 8, 11))

    class _Bare:
        pass
    check("a layer declaring nothing takes the shipped default",
          _read_lookback(_Bare()) == DEFAULT_RATCHET_LOOKBACK)

    class _Declared:
        RATCHET_LOOKBACK = 6
    check("a layer declaring six gets six", _read_lookback(_Declared()) == 6)

    for bad in (0, -3, "14", 2.5, True):
        cls = type("_Bad", (), {"RATCHET_LOOKBACK": bad})
        named = False
        try:
            _read_lookback(cls())
        except DriftError as exc:
            named = "RATCHET_LOOKBACK" in str(exc)
        check(f"an unusable declaration ({bad!r}) is a refusal that NAMES the key", named)

    # THE RAISE IS NOT THE CHANNEL. Every arm above calls the function and catches the exception,
    # which is exactly what let the real defect through: the raise worked and nothing carried it to
    # the caller, because the only call site sat OUTSIDE main's try. That shipped as a raw traceback
    # and rc=1 -- the leg's "a signal is over its pin" exit -- so a config error read as drift.
    # This arm drives main() and asserts the REFUSAL CHANNEL: rc 2, and the `drift-report: ` prefix
    # a reader greps for. The repo's own idiom, asserted on the message and the code, never the raise.
    import drift_report as _dr
    import drift_signals as _ds

    _saved = getattr(_ds, "RATCHET_LOOKBACK", None)
    _err = io.StringIO()
    try:
        _ds.RATCHET_LOOKBACK = 0
        _stderr, sys.stderr = sys.stderr, _err
        try:
            rc = _dr.main(["--check"])
        finally:
            sys.stderr = _stderr
    finally:
        if _saved is None:
            delattr(_ds, "RATCHET_LOOKBACK")
        else:
            _ds.RATCHET_LOOKBACK = _saved

    check("an unusable RATCHET_LOOKBACK refuses through main with rc=2, not a traceback", rc == 2)
    check("...and on the prefixed channel a reader greps for",
          _err.getvalue().startswith("drift-report: ") and "RATCHET_LOOKBACK" in _err.getvalue())


def test_ratchet_message_states_its_window(tmp: pathlib.Path) -> None:
    """The finding says how far it looked, using the DECLARED number.

    Stated differentially on purpose: the message already interpolated the constant before this
    unit, so an arm asserting it names fourteen would have been green before a line was written.
    """
    print("RATCHET message (states the window it actually searched)")
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import drift_report as dr

    class _Git:
        base_ref = "BASE"
        def run(self, *a):
            return type("R", (), {"returncode": 0, "stdout": 'PIN="5"\n'})()

    root = tmp / "lookbackmsg"
    root.mkdir(parents=True, exist_ok=True)
    (root / "p.conf").write_text('PIN="9"\n', encoding="utf-8", newline="\n")
    spec = [{"file": "p.conf", "key": "PIN", "weakens": "up"}]

    out6 = dr.ratchet_findings(_Git(), root, spec, 6)
    check("a declared six is what the message reports",
          bool(out6) and "within 6 lines" in out6[0], str(out6))
    out_def = dr.ratchet_findings(_Git(), root, spec)
    check("...and the shipped default when the caller passes none",
          bool(out_def) and f"within {dr.DEFAULT_RATCHET_LOOKBACK} lines" in out_def[0], str(out_def))


def test_lang_mode_ratchet(tmp: pathlib.Path) -> None:
    """The LANGS mode ratchet: a weakening move needs its reason beside it.

    THE ARM THAT MATTERS IS THE JUSTIFIED ONE. A ratchet that only ever fires is a ratchet nobody can
    satisfy, and it would be indistinguishable from one that fires unconditionally -- which is the
    same could-not-fail shape one level up. Both directions are asserted over one fixture.

    THE EXTENSION IS REQUIRED IN THE MARKER, and that has its own arm. One LANGS line carries every
    extension, so a bare `parser -> dark` beside it would justify a move for whichever extension the
    reader guessed.
    """
    print("LANGS mode ratchet (a weakening move needs its reason)")
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    import drift_report as dr

    class _Git:
        base_ref = "BASE"
        def run(self, *a):
            return type("R", (), {"returncode": 0,
                                  "stdout": 'LANGS="py:python-ast:parser js:js-regex:probe"\n'})()

    root = tmp / "langmode"
    root.mkdir(parents=True, exist_ok=True)
    conf = root / ".lexicon.conf"

    # UNJUSTIFIED: py falls parser -> dark with nothing beside it.
    conf.write_text('LANGS="py:python-ast:dark js:js-regex:probe"\n', encoding="utf-8", newline="\n")
    out = dr.build_lang_mode_findings(_Git(), root)
    check("mode ratchet: an unjustified parser -> dark is a finding", bool(out), str(out))
    check("mode ratchet: it names the extension and both modes",
          bool(out) and ".py" in out[0] and "parser -> dark" in out[0], str(out))

    # JUSTIFIED: the same move, with the marker above the LANGS line.
    conf.write_text('# py: parser -> dark, because the extractor moved to another kit.\n'
                    'LANGS="py:python-ast:dark js:js-regex:probe"\n',
                    encoding="utf-8", newline="\n")
    check("mode ratchet: the SAME move with its reason beside it is silent",
          dr.build_lang_mode_findings(_Git(), root) == [], str(dr.build_lang_mode_findings(_Git(), root)))

    # The marker must name the EXTENSION, not just the two modes.
    conf.write_text('# parser -> dark, and this comment names no extension.\n'
                    'LANGS="py:python-ast:dark js:js-regex:probe"\n',
                    encoding="utf-8", newline="\n")
    check("mode ratchet: a marker naming no extension does NOT justify the move",
          bool(dr.build_lang_mode_findings(_Git(), root)),
          str(dr.build_lang_mode_findings(_Git(), root)))

    # AN EXTENSION WHOSE NAME IS NOT A WORD. `<none>` is what this repo declares for a dotless
    # basename, and the marker was anchored with a word boundary on both sides of the extension --
    # which sits before `<` and after `>` and can NEVER match there. So the one extension whose name
    # is not a word had a justification clause nobody could satisfy: every weakening move on it would
    # red forever with a correct marker sitting right above it. Gated as a CLASS rather than for
    # `<none>` alone, because the next such name will not be spelled that way. Closing review M2.
    class _GitNone:
        base_ref = "BASE"
        def run(self, *a):
            return type("R", (), {"returncode": 0,
                                  "stdout": 'LANGS="<none>::parser py:python-ast:parser"\n'})()

    conf.write_text('LANGS="<none>::dark py:python-ast:parser"\n', encoding="utf-8", newline="\n")
    _un = dr.build_lang_mode_findings(_GitNone(), root)
    check("mode ratchet: an unjustified move on a non-word extension is still a finding",
          any("<none>" in f for f in _un), str(_un))
    conf.write_text('# <none>: parser -> dark, because nothing extracts dotless files.\n'
                    'LANGS="<none>::dark py:python-ast:parser"\n',
                    encoding="utf-8", newline="\n")
    _j = dr.build_lang_mode_findings(_GitNone(), root)
    check("mode ratchet: a non-word extension CAN be justified (the marker must be satisfiable)",
          _j == [], str(_j))

    # THE MARKER GRAMMAR IS A SUPERSET OF THE ONE IT REPLACED, and that is asserted rather than
    # assumed. The round-1 M2 fix required whitespace-or-start before the extension, which fixed
    # `<none>` and silently NARROWED every other shape: `#py:` with no space, a parenthesised marker,
    # and `# js,py:` -- the natural way to justify one move for two extensions -- all stopped
    # matching. That reintroduced M2's own symptom (a permanent red under a correct-looking marker)
    # for the shapes that used to work, which is why the rows below are spellings and not one
    # spelling. `pyx` is the negative: a longer name must never be justified by a shorter one's row.
    for _marker, _want_ok in (
            ("# py: parser -> dark", True),
            ("#py: parser -> dark", True),
            ("# (py: parser -> dark)", True),
            ("# js,py: parser -> dark", True),
            ("# ext=py: parser -> dark", True),
            ("# pyx: parser -> dark", False),
            ("# parser -> dark", False),
    ):
        conf.write_text(_marker + chr(10) + 'LANGS="py:python-ast:dark js:js-regex:probe"' + chr(10),
                        encoding="utf-8", newline=chr(10))
        _silent = dr.build_lang_mode_findings(_Git(), root) == []
        check(f"mode ratchet: {'justifies' if _want_ok else 'refuses'} {_marker!r}",
              _silent is _want_ok, f"silent={_silent} want_ok={_want_ok}")

    # A STRENGTHENING move is free, and an extension that never moved is silent.
    conf.write_text('LANGS="py:python-ast:parser js:js-regex:parser"\n',
                    encoding="utf-8", newline="\n")
    check("mode ratchet: a tightening move needs no justification",
          dr.build_lang_mode_findings(_Git(), root) == [],
          str(dr.build_lang_mode_findings(_Git(), root)))

    # An extension DROPPED from LANGS entirely is the strongest weakening: rank falls to absent.
    conf.write_text('LANGS="js:js-regex:probe"\n', encoding="utf-8", newline="\n")
    gone = dr.build_lang_mode_findings(_Git(), root)
    check("mode ratchet: an extension DELETED from LANGS is a weakening, not an absence",
          bool(gone) and "absent" in gone[0], str(gone))

    # NOT ADOPTED: no declaration at all is silence, never a finding.
    conf.unlink()
    check("mode ratchet: a repo without the kit reports nothing",
          dr.build_lang_mode_findings(_Git(), root) == [], "expected []")


def test_harness_liveness_note_is_derived(tmp: pathlib.Path) -> None:
    """TOOL-dRetiredFork-6 S4 — the derived note, one arm per counter state.

    The harnesses are Workflow-runtime scripts: top-level `await`, globals this process does not
    have, so they cannot be imported. The two helpers are EXTRACTED and run in node, which grades
    the SHIPPED bytes rather than a paraphrase of them.

    WHY THREE ARMS AND NOT ONE. The ternary this replaced had three outcomes and conflated two of
    them: "nothing moved" and "the probe could not run" both rendered the bare word `complete`. An
    arm that only checked the dead state would pass against the ternary too, because the ternary
    also produced *a* string. What distinguishes them is that the three states are now DISTINCT
    sentences, so the arms assert distinctness, not just presence.
    """
    import json
    import subprocess

    LF = chr(10)

    for harness in ("drift-audit-code.js", "drift-audit-state.js"):
        src = (resolve_kit_dir("workflows", harness, KIT) / harness).read_text(encoding="utf-8")
        if "function deriveLiveness" not in src:
            check(f"{harness}: carries the derived note", False,
                  "deriveLiveness is absent — the hand-written ternary is back")
            continue

        def extract_fn(name: str) -> str:
            i = src.index("function " + name + "(")
            depth = 0
            started = False
            for j in range(i, len(src)):
                if src[j] == "{":
                    depth += 1
                    started = True
                elif src[j] == "}":
                    depth -= 1
                    if started and depth == 0:
                        return src[i:j + 1]
            raise AssertionError("unterminated " + name)

        driver = (
            extract_fn("deriveLiveness") + LF + extract_fn("renderLivenessNote") + LF +
            "const states = {" + LF +
            "  clean: { synth: true, lensesRun: 3, lensesDead: 0, skepticsDead: 0, unverified: 0 }," + LF +
            "  partial: { synth: true, lensesRun: 3, lensesDead: 1, skepticsDead: 0, unverified: 2 }," + LF +
            "  dead: { synth: false, lensesRun: 0, lensesDead: 3, skepticsDead: 0, unverified: 0 }," + LF +
            "};" + LF +
            "const out = {};" + LF +
            "for (const k of Object.keys(states)) {" + LF +
            "  out[k] = [deriveLiveness(states[k]), renderLivenessNote(deriveLiveness(states[k]), states[k])];" + LF +
            "}" + LF +
            "console.log(JSON.stringify(out));" + LF
        )
        d = tmp / (harness + ".driver.js")
        d.write_text(driver, encoding="utf-8")
        proc = subprocess.run(["node", str(d)], capture_output=True, text=True, encoding="utf-8")
        check(f"{harness}: the extracted helpers run", proc.returncode == 0, proc.stderr[:160])
        if proc.returncode != 0:
            continue
        got = json.loads(proc.stdout)

        # AC1 / AC2 — moved and did-not-move are DIFFERENT sentences, and a consumer re-deriving
        # either byte-matches, because both come from the same two functions.
        check(f"{harness}: a moved counter renders PARTIAL", got["partial"][0] == "partial"
              and got["partial"][1].startswith("PARTIAL:"), str(got["partial"]))
        check(f"{harness}: nothing-moved renders CLEAN, not the bare word complete",
              got["clean"][0] == "clean" and got["clean"][1].startswith("CLEAN:")
              and got["clean"][1] != "complete", str(got["clean"]))

        # AC3 — the state the ternary could not express. Observed RED against the ternary first:
        # with `!synth` it produced an UNVERIFIED string and with lensesRun 0 alone it produced the
        # bare `complete`, so a dead probe reported as a clean run.
        check(f"{harness}: a probe that could not run says DEAD PROBE",
              got["dead"][0] == "dead" and "DEAD PROBE" in got["dead"][1], str(got["dead"]))

        # ANTI-VACUITY: three states, three DISTINCT sentences. The defect was that two of them were
        # the same string, so an arm that never compared them would have passed against the ternary.
        check(f"{harness}: the three states are three distinct sentences",
              len({got["clean"][1], got["partial"][1], got["dead"][1]}) == 3)



# ---------------------------------------------------------------------------------------------
# The shipped-evidence oracle: one grammar, its own population, and a liveness half that can see
# that population collapse. Five arms, one per criterion that observes a change this unit makes.
# ---------------------------------------------------------------------------------------------


def test_evidence_oracle(tmp: pathlib.Path) -> None:
    r = make_repo(tmp, name="evidence")
    proj = r / KIT_NAME / "drift_signals.py"
    conf = r / ".memory-tree.conf"
    spec_dir = r / SPEC_DIR_FOR_FIXTURE

    def add(rel: str, body: str, msg: str) -> None:
        p = r / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8", newline="\n")
        run(["git", "add", "-A"], r)
        run(["git", "commit", "-q", "-m", msg, "--no-verify"], r)

    def read_signal(*extra: str) -> dict:
        return report(r, *extra)["non_terminal_specs_cited_by_product_source"]

    # ---- ARM 1: the correction-form id. Its seq carries a trailing lowercase letter, which the
    # hand-typed digits-then-boundary pattern could not match at all -- so the spec scored UNKEYED
    # and the probe declined to judge it, silently. Observed RED against that pattern: the spec was
    # absent from the judgeable population entirely.
    before = read_signal()["of"]
    add(str(pathlib.Path(SPEC_DIR_FOR_FIXTURE) / "2026-01-02-spec-aFixed-1b.md").replace("\\", "/"),
        "# TOOL-aFixed-1b \u2014 a ratified correction\n\n"
        "**Status:** SPECCED \u00b7 rev-1 \u00b7 2026-01-02 \u00b7 node a \u00b7 Tier-2 \u00b7 base 0000000\n",
        "spec(aFixed): a correction-form id")
    check("evidence: a correction-form id is JUDGED, not silently unkeyed",
          read_signal()["of"] == before + 1,
          f"population {before} -> {read_signal()['of']}, wanted +1")

    # ---- ARM 2: a citation from a TEST file is the house's own bookkeeping certifying the
    # bookkeeping, so it must not count as evidence a unit shipped. The same id cited from a
    # PRODUCT file must count. Both halves, because only the pair discriminates.
    add("src/thing.test.sh", "# cites TOOL-aThing-1 from a test file\n",
        "test: cite a spec id from a test file")
    check("evidence: a test-file citation is not evidence a unit shipped",
          all(row["id"] != "TOOL-aThing-1" for row in read_signal()["detail"]),
          f"detail: {[row['id'] for row in read_signal()['detail']]}")
    add("src/thing.py", "# cites TOOL-aThing-1 from product source\n",
        "feat: cite the same id from product source")
    check("evidence: a product-file citation IS evidence a unit shipped",
          any(row["id"] == "TOOL-aThing-1" for row in read_signal()["detail"]),
          f"detail: {[row['id'] for row in read_signal()['detail']]}")

    # ---- ARM 3: the drain. Remove every remaining product citation and the VALUE reaches zero,
    # while the judgeable population does NOT -- they are different fields, and an arm asserting on
    # the population would be green whatever the citations did.
    (r / "src" / "thing.py").unlink()
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "chore: drop the product citation", "--no-verify"], r)
    drained = read_signal()
    check("evidence: the value drains to zero when the product citations go",
          drained["value"] == 0, f"value {drained['value']}")
    check("evidence: the judgeable population does NOT drain with it",
          drained["of"] > 0, f"of {drained['of']}")

    # ---- ARM 4: the second liveness half. Empty the declaration and the signal must report itself
    # DEAD rather than a clean zero. Observed RED against the pre-change engine, whose only liveness
    # half counts specs and is computed before any glob is read -- it stayed True at full size.
    proj.write_text(proj.read_text(encoding="utf-8").replace(
        "EVIDENCE_GLOBS = ['src', ':(exclude)*.test.sh']", "EVIDENCE_GLOBS = ['no-such-directory']"),
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "chore: empty the evidence declaration", "--no-verify"], r)
    dead = read_signal()
    check("evidence: a declaration resolving to no file reports DEAD, not a clean zero",
          dead["live"] is False and dead["evidence_files"] == 0,
          f"live={dead['live']} evidence_files={dead['evidence_files']}")
    proj.write_text(proj.read_text(encoding="utf-8").replace(
        "EVIDENCE_GLOBS = ['no-such-directory']", "EVIDENCE_GLOBS = ['src', ':(exclude)*.test.sh']"),
        encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "chore: restore the evidence declaration", "--no-verify"], r)

    # ---- ARM 5: the grammar is bound to the TREE, not to the repo this kit lives in. A family this
    # repo does not declare must still be classified in a tree that declares it. Observed RED
    # against a module-constant binding, which reads the installing repo's family list and reports a
    # confident zero over a corpus full of ids it cannot see.
    conf.write_text("MEMORY_ROOT=memory\nFAMILIES=\"widget:WDGT\"\n",
                    encoding="utf-8", newline="\n")
    add(str(pathlib.Path(SPEC_DIR_FOR_FIXTURE) / "2026-01-03-spec-aWidget-1.md").replace("\\", "/"),
        "# WDGT-aWidget-1 \u2014 a foreign family\n\n"
        "**Status:** SPECCED \u00b7 rev-1 \u00b7 2026-01-03 \u00b7 node a \u00b7 Tier-2 \u00b7 base 0000000\n",
        "spec(aWidget): an id in a family this kit's own repo does not declare")
    add("src/widget.py", "# cites WDGT-aWidget-1 from product source\n",
        "feat: cite the foreign-family id")
    check("evidence: the grammar is bound to the tree, so a foreign family is classified",
          any(row["id"] == "WDGT-aWidget-1" for row in read_signal()["detail"]),
          f"detail: {[row['id'] for row in read_signal()['detail']]}")


def test_local_grammar_matches_the_extractor(tmp: pathlib.Path) -> None:
    """The local fallback is not a second grammar, and this is what keeps it honest.

    The report falls back to a local copy of the id alternation when the recall extractor is not
    importable, which is the only way a copy-installed kit can run in a tree without it. A copy
    nobody compares is a second grammar with extra steps, so compare it -- here, where this repo
    HAS the extractor, against what the extractor itself produces for this same tree.
    """
    import importlib.util

    try:
        extractor = resolve_kit_dir("memory-recall", "extract.py", KIT) / "extract.py"
    except LookupError:
        extractor = None
    if extractor is None or not extractor.exists():
        skip("local grammar equals the extractor's", "no memory-recall kit beside this one")
        return
    spec = importlib.util.spec_from_file_location("_drift_report_probe", KIT / "drift_report.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    root = next((p for p in KIT.parents if (p / ".git").exists()), KIT.parent.parent)
    families = mod._read_families(mod.load_conf(root))
    # AGAINST THE EXTRACTOR ITSELF, not against the accessor. The accessor falls back to the local
    # copy on ANY import failure, so comparing the two compared the copy to itself and passed for
    # free -- reproduced by forcing the import to raise. The arm now imports the extractor by path
    # and lets an import failure FAIL rather than quietly satisfy it.
    espec = importlib.util.spec_from_file_location("_recall_extract_probe", extractor)
    emod = importlib.util.module_from_spec(espec)
    sys.path.insert(0, str(extractor.parent))
    try:
        espec.loader.exec_module(emod)
        shipped = emod.grammar_for(root).ID
    finally:
        try:
            sys.path.remove(str(extractor.parent))
        except ValueError:
            pass
    check("local grammar equals the extractor's for this tree",
          mod._build_local_ident(families) == shipped,
          "the local fallback has diverged from the shipped alternation")


# ---------------------------------------------------------------------------------------------
# The source-citation signal: slug-resolvability as the discriminator, and two liveness halves.
# ---------------------------------------------------------------------------------------------


def test_source_cited_ids(tmp: pathlib.Path) -> None:
    NL = chr(10)
    r = make_repo(tmp, name="citations")
    conf = r / ".memory-tree.conf"
    proj = r / KIT_NAME / "drift_signals.py"

    def run_commit(msg: str) -> None:
        run(["git", "add", "-A"], r)
        run(["git", "commit", "-q", "-m", msg, "--no-verify"], r)

    def read_signal(*extra: str) -> dict:
        return report(r, *extra)["source_cited_ids_resolving_to_no_record"]

    base = read_signal()
    check("citations: the signal is live on a fixture with records and source",
          base["live"] and base["known_slugs"] > 0 and base["scanned_source_files"] > 0,
          f"slugs={base['known_slugs']} files={base['scanned_source_files']}")

    # ---- THE DISCRIMINATOR, both directions. A fabricated id under a slug that ANCHORS a record is
    # a real dangling citation; the same shape under a slug no record anchors is a fixture. Only the
    # pair proves the discriminator discriminates -- one half alone passes for a signal that counts
    # everything, and the other for a signal that counts nothing.
    before = read_signal()["value"]
    (r / "src" / "resolving.py").write_text(
        "# cites TOOL-aThing-999, whose slug anchors a record\n", encoding="utf-8", newline="\n")
    run_commit("chore: cite a fabricated id under a RESOLVING slug")
    check("citations: a dangling id under a known slug is a finding",
          read_signal()["value"] == before + 1, f"value {before} -> {read_signal()['value']}, wanted +1")

    mid = read_signal()["value"]
    (r / "src" / "fixture.py").write_text(
        "# cites TOOL-zNoSuchSlug-1, whose slug anchors nothing\n", encoding="utf-8", newline="\n")
    run_commit("chore: cite a fabricated id under a slug no record anchors")
    check("citations: a dangling id under an UNKNOWN slug is a fixture, not a finding",
          read_signal()["value"] == mid, f"value {mid} -> {read_signal()['value']}, wanted no movement")

    # ---- LIVENESS HALF ONE: no records, so no slugs. The signal must say it is dead rather than
    # report a clean zero over a corpus it cannot see.
    keep = {}
    for p in sorted((r / FIXTURE_MEMORY_ROOT).rglob("*.md")):
        keep[p] = p.read_text(encoding="utf-8")
        p.unlink()
    run_commit("chore: empty the memory root")
    dead = read_signal()
    check("citations: an empty memory root reports DEAD, not zero findings",
          dead["live"] is False and dead["known_slugs"] == 0,
          f"live={dead['live']} slugs={dead['known_slugs']}")
    for p, text in keep.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")
    run_commit("chore: restore the memory root")

    # ---- LIVENESS HALF TWO, and it is NOT the scanned-file count. That count can never reach zero
    # in a tree with this kit installed, because the report is itself a tracked non-memory file --
    # measured, by writing the arm the obvious way and watching it fail to go dead. What CAN collapse
    # is the CITED set: bind the grammar to a family nothing uses and every file is still scanned
    # while nothing matches, which is a confident zero over a corpus full of ids the signal cannot
    # see. That is the hazard, and this is the arm for it.
    conf.write_text("MEMORY_ROOT=memory" + NL + 'FAMILIES="nothing:ZZZZ"' + NL,
                    encoding="utf-8", newline=NL)
    run_commit("chore: bind the grammar to a family nothing uses")
    blind = read_signal()
    check("citations: a grammar matching nothing reports DEAD, not a clean zero",
          blind["live"] is False and blind["of"] == 0 and blind["scanned_source_files"] > 0,
          f"live={blind['live']} of={blind['of']} files={blind['scanned_source_files']}")

    # ---- THE FAMILY ENUM IS READ, NOT SPELLED, and the arm runs in the NARROWING direction. With no
    # FAMILIES declared the engine falls back to a permissive family pattern, so declaring an enum
    # can only narrow -- an arm that declared a family and expected the count to RISE would pass on
    # an engine that ignored the conf entirely, which is how it was first written.
    (r / "src" / "foreign.py").write_text(
        "# cites WDGT-aThing-7, in a family the conf may or may not declare" + NL,
        encoding="utf-8", newline=NL)
    run_commit("chore: cite an id in a foreign family")
    conf.write_text("MEMORY_ROOT=memory" + NL + 'FAMILIES="tooling:TOOL"' + NL,
                    encoding="utf-8", newline=NL)
    run_commit("chore: declare TOOL only")
    narrow = read_signal()["value"]
    conf.write_text("MEMORY_ROOT=memory" + NL + 'FAMILIES="widget:WDGT tooling:TOOL"' + NL,
                    encoding="utf-8", newline=NL)
    run_commit("chore: declare the foreign family too")
    check("citations: the family enum is READ from the conf, not spelled in the engine",
          read_signal()["value"] == narrow + 1,
          f"value {narrow} -> {read_signal()['value']}, wanted +1 once the family was declared")

    # ---- THE WHOLE REPORT SURVIVES A TREE WITH NO RECALL KIT. This fixture has never had one, so
    # the assertion is that the run RETURNS at all rather than raising and taking the other signals
    # with it -- the failure mode is a dead leg for that adopter, not a missing signal.
    check("citations: the report returns in a tree with drift-audit and no recall kit",
          not (resolve_recall_name() and (r / resolve_recall_name()).exists()) and read_signal()["signal"],
          "the fixture unexpectedly has a recall kit beside it")


# ---------------------------------------------------------------------------------------------
# The two closing-review repairs, each with the arm it landed without.
# ---------------------------------------------------------------------------------------------


def test_report_only_signal_is_judged_against_its_pin(tmp: pathlib.Path) -> None:
    """A report-only signal at exactly its pinned value prints a CALM status, not an over one.

    The display branch for a non-gateable signal compared against the bare `tolerance` while both
    gateable branches compared against the resolved `pin`, so a report-only signal WITH a pin
    announced itself over at the very value its pin ratifies. A signal whose only product is its
    status line cannot afford that: it trains a reader to ignore the column.
    """
    r = make_repo(tmp, name="pinned")
    proj = r / KIT_NAME / "drift_signals.py"
    NL = chr(10)

    def read_human_table() -> str:
        out = run([sys.executable, REPORT_REL], r)
        assert out.returncode == 0, out.stderr[:300]
        return out.stdout

    # A REPORT-ONLY SIGNAL WITH A NON-ZERO VALUE, built rather than assumed. The first version of
    # this arm reached for a signal the fixture leaves at 0, so pinning it at its value pinned it at
    # zero and the two checks below passed over nothing -- the fixture-passes-by-finding-nothing
    # class, in the arm written to catch a reporting defect. The premise is asserted first now.
    (r / "src" / "dangling.py").write_text(
        "# cites TOOL-aThing-404, whose slug anchors a record but whose seq does not" + NL,
        encoding="utf-8", newline=NL)
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "chore: plant a dangling citation", "--no-verify"], r)

    name = "source_cited_ids_resolving_to_no_record"
    value = report(r)[name]["value"]
    check("report-only: the fixture's report-only signal has a value to pin",
          value > 0, f"value {value} -- the arm below would pin at zero and prove nothing")

    proj.write_text(proj.read_text(encoding="utf-8").replace(
        "PINS = {}", "PINS = {'" + name + "': " + str(value) + "}"),
        encoding="utf-8", newline=NL)
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "chore: pin the report-only signal at its value", "--no-verify"], r)

    line = [ln for ln in read_human_table().splitlines() if name in ln]
    check("report-only: a signal AT its pin does not report itself over",
          bool(line) and "over" not in line[0],
          f"status line: {line[0].strip() if line else '(absent)'}")
    check("report-only: and it NAMES the pin rather than printing a bare ok",
          bool(line) and ("pin " + str(value)) in line[0],
          f"status line: {line[0].strip() if line else '(absent)'}")


def test_evidence_globs_exclude_test_templates(tmp: pathlib.Path) -> None:
    """A `.test-template` file is a test that is neither `.test.sh` nor named `fixture`.

    The exclusion list was collapsed to a single fixture predicate and silently lost this shape,
    re-admitting a template to the evidence population under a comment claiming total coverage.
    """
    r = make_repo(tmp, name="templates")
    proj = r / KIT_NAME / "drift_signals.py"
    proj.write_text(proj.read_text(encoding="utf-8").replace(
        "EVIDENCE_GLOBS = ['src', ':(exclude)*.test.sh']",
        "EVIDENCE_GLOBS = ['src', ':(exclude)*.test.sh', ':(exclude)*fixture*', "
        "':(exclude)*.test-template.*']"),
        encoding="utf-8", newline="\n")
    (r / "src" / "thing.test-template.py").write_text(
        "# cites TOOL-aThing-1 from a test TEMPLATE\n", encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "chore: cite a spec id from a test template", "--no-verify"], r)

    sig = report(r)["non_terminal_specs_cited_by_product_source"]
    check("evidence: a `.test-template` citation is not evidence a unit shipped",
          all(row["id"] != "TOOL-aThing-1" for row in sig["detail"]),
          f"detail: {[row['id'] for row in sig['detail']]}")

    # AND THE SHIPPED DECLARATION CARRIES IT. The arm above writes its own glob list into the
    # fixture's project layer, so it proves the PATHSPEC works and guards nothing about what this
    # repo actually declares -- measured, by deleting the shipped line and watching the arm stay
    # green. This half reads the shipped list directly, which is the only thing that reds when the
    # exclusion is dropped from it.
    shipped = KIT / "drift_signals.py"
    globs = [ln.strip().strip(",").strip('"').strip("'")
             for ln in shipped.read_text(encoding="utf-8").splitlines()]
    check("evidence: the SHIPPED declaration excludes the test-template shape",
          ":(exclude)*.test-template.*" in globs,
          "the shipped EVIDENCE_GLOBS lost the exclusion the arm above only proves is honoured")

def test_asks_disposed_overrides(tmp: pathlib.Path) -> None:
    """TOOL-dDerivedDocket-17: the count that makes owner ruling D12-b's override BOUNDED.

    The ruling allows `--close --override asks-disposed` with a recorded reason on the condition
    that the overrides are counted. Each one is a legitimate row in one record; the population is
    the thing nobody can see, and this is the reader of it.
    """
    print("asks-disposed overrides per run-state record")
    sep = chr(0xB7)
    r = make_repo(tmp, name="askoverrides")
    builds = r / "memory" / "builds"
    for slug, body in (
        ("aOne",
         f"2026-09-01T00:00:00Z override {sep} item asks-disposed {sep} reason the owner took the call\n"
         f"2026-09-02T00:00:00Z override {sep} item gates-green {sep} reason the bar was run by hand\n"),
        ("aTwo",
         f"2026-09-03T00:00:00Z override {sep} item asks-disposed {sep} reason a second, also recorded\n"
         f"2026-09-04T00:00:00Z decision {sep} item asks-disposed came up {sep} reason parked, never bought\n"),
    ):
        (builds / slug).mkdir(parents=True, exist_ok=True)
        (builds / slug / "RUN.md").write_text(
            f"# {slug} - run state\n\n## Run facts\nphase: LANDED\n\n## Parked\n{body}",
            encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "run-state records", "--no-verify"], r)

    got = report(r)["asks_disposed_overrides"]
    # THE OTHER TWO ROWS ARE THE LOAD-BEARING HALF of this fixture. A count over every `override`
    # row reads 4, and a count over every row naming the item reads 4 as well — so a fixture with
    # only this item's overrides in it would pass under either mistake.
    check("counts THIS item's overrides and nobody else's: 2", got["value"] == 2, f"got {got['value']}")
    check("reports every tracked record, so a total cannot hide one growing inside another",
          got["of"] == 2, f"got {got['of']}")
    check("the probe is LIVE where run-state records exist", got["live"] is True)
    check("report-only: an unguarded merge-bar leg must not turn a recorded ruling into a refusal",
          got["gateable"] is False)
    per = {d["record"]: d["overrides"] for d in got["detail"]}
    check("each record carries its own count",
          per == {"memory/builds/aOne/RUN.md": 1, "memory/builds/aTwo/RUN.md": 1}, f"got {per}")

    # --- it MOVES when another run buys the item. That is the whole point of the signal. --------
    p = builds / "aTwo" / "RUN.md"
    p.write_text(p.read_text(encoding="utf-8")
                 + f"2026-09-05T00:00:00Z override {sep} item asks-disposed {sep} reason a third\n",
                 encoding="utf-8", newline="\n")
    check("a further override raises the count",
          report(r)["asks_disposed_overrides"]["value"] == 3,
          "the signal does not track the variable it exists for")

    # --- DEAD, not a reassuring 0, where no run-state record exists at all ----------------------
    r2 = make_repo(tmp, name="norunstate")
    dead = report(r2)["asks_disposed_overrides"]
    check("no run-state record at all reports DEAD rather than 0",
          dead["live"] is False, f"live={dead['live']} value={dead['value']}")


# ---------------------------------------------------------------------------------------------
# TOOL-dDerivedDocket-26 — legs the merge bar retried after a timeout
# ---------------------------------------------------------------------------------------------


def _write_gate_verdict(r: pathlib.Path, run: str, body: str, git_dir: str = ".git",
                        retries: tuple = ()) -> None:
    """One run record's verdict file under a fixture git dir, where the gate runner writes it, with
    one `<i>.retry.leg` row per `(leg, status)` in `retries`."""
    d = r / git_dir / "gate-run" / run
    d.mkdir(parents=True, exist_ok=True)
    (d / "verdict").write_text(body, encoding="utf-8", newline="\n")
    for i, (leg, status) in enumerate(retries):
        (d / f"{i}.retry.leg").write_text(f"{leg}\t{status}\t0\t3\t1\t2\tabc\n",
                                          encoding="utf-8", newline="\n")


def test_legs_retried_after_timeout(tmp: pathlib.Path) -> None:
    """The sum of `retried` over the run records a git dir holds, and DEAD where none can move it.

    The runner retries a leg whose own ceiling fired and counts a pass on that retry green, which is
    right for one bar and invisible across many. This signal is the reader across them.
    """
    print("legs retried after a timeout, over the run records")
    r = make_repo(tmp, name="retried")
    _write_gate_verdict(r, "r1", "verdict\tGREEN\nretried\t1\n")
    _write_gate_verdict(r, "r2", "verdict\tRED\nretried\t1\n")
    got = report(r)["legs_retried_after_timeout"]
    check("two records with retried 1 report 2", got["value"] == 2, f"got {got['value']}")
    check("the probe is LIVE where a record carries the key", got["live"] is True)
    check("report-only: a retried leg is not a refusal", got["gateable"] is False)
    # --- a record from a runner that predates the retry is read but moves nothing ------------------
    _write_gate_verdict(r, "r0", "verdict\tGREEN\nran\t4\n")
    got = report(r)["legs_retried_after_timeout"]
    check("a record without the key is counted in `of` and adds nothing",
          got["value"] == 2 and got["of"] == 3, f"value {got['value']} of {got['of']}")
    # --- it MOVES when another bar retries ---------------------------------------------------------
    _write_gate_verdict(r, "r3", "verdict\tGREEN\nretried\t3\n")
    check("a further record raises the sum",
          report(r)["legs_retried_after_timeout"]["value"] == 5, "the signal does not track its variable")
    # --- DEAD, not a reassuring 0, over a git dir holding no run record -------------------------------
    dead = report(make_repo(tmp, name="noruns"))["legs_retried_after_timeout"]
    check("a git dir with no run record reports DEAD rather than 0",
          dead["live"] is False, f"live={dead['live']} value={dead['value']}")
    # --- TOOL-aMendedFleet-59: every git dir of the clone, grouped by leg ---------------------------
    # Red against a reader of the current git dir alone: the linked worktree's record goes unread.
    w = make_repo(tmp, name="retriedwt")
    _write_gate_verdict(w, "r1", "verdict\tGREEN\nretried\t1\n", retries=(("leg a", "ok"),))
    _write_gate_verdict(w, "r1", "verdict\tRED\nretried\t2\n", git_dir=".git/worktrees/w1",
                        retries=(("leg a", "ok"), ("leg b", "fail")))
    got = report(w)["legs_retried_after_timeout"]
    check("a linked worktree's run record is summed beside the common dir's",
          got["value"] == 3 and got["of"] == 2, f"value {got['value']} of {got['of']}")
    check("`git_dirs` counts the git dirs holding a record", got["git_dirs"] == 2, f"got {got['git_dirs']}")
    check("every counted retry names its leg", got["unattributed"] == 0, f"got {got['unattributed']}")
    legs = {d["leg"]: d for d in got["detail"]}
    check("a leg retried in two git dirs reads 2 retries over 2 git dirs",
          legs.get("leg a", {}).get("retried") == 2 and legs["leg a"]["git_dirs"] == 2, f"got {legs}")
    check("a leg that failed on its retry reads `failed_after_retry` 1",
          legs.get("leg b", {}).get("failed_after_retry") == 1
          and legs.get("leg a", {}).get("failed_after_retry") == 0, f"got {legs}")
    check("the detail orders legs by retries descending",
          [d["leg"] for d in got["detail"]] == ["leg a", "leg b"], f"got {got['detail']}")


def test_cutoff_keys_armed(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-21: armed `_CUTOFF` keys in TRACKED root confs, pinned only where declared.

    Two root confs carry an armed, a blank, an exported and a commented cutoff line, and an untracked
    conf carries one more; only the armed and exported ones in tracked confs are `value`.
    """
    print("armed cutoff keys across the tracked root confs")
    name = "cutoff_keys_armed"
    r = make_repo(tmp, name="cutoffs")
    NL = chr(10)
    dead = report(r).get(name, {})
    check("cutoffs: no _CUTOFF assignment anywhere reads DEAD, not 0",
          dead.get("live") is False, f"row {dead}")
    (r / ".memory-tree.conf").write_text(
        "MEMORY_ROOT=memory" + NL + 'A_CUTOFF="2026-01-01"' + NL + 'B_CUTOFF=""' + NL
        + '# C_CUTOFF="2026-01-01"' + NL, encoding="utf-8", newline=NL)
    (r / ".other.conf").write_text(
        "export D_CUTOFF=2026-02-02" + NL + "E_CUTOFF=   # blank on purpose" + NL,
        encoding="utf-8", newline=NL)
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "chore: two root confs with cutoff keys", "--no-verify"], r)
    (r / ".untracked.conf").write_text('F_CUTOFF="2026-03-03"' + NL, encoding="utf-8", newline=NL)
    got = report(r).get(name, {})
    check("cutoffs: armed and exported count, blank, commented and untracked do not",
          (got.get("value"), got.get("of"), got.get("live")) == (2, 4, True), f"row {got}")
    check("cutoffs: with no PINS entry the row is report-only and says no budget is declared",
          got.get("gateable") is False and "no budget" in str((got.get("detail") or [{}])[0]),
          f"row {got}")
    proj = r / KIT_NAME / "drift_signals.py"
    proj.write_text(proj.read_text(encoding="utf-8").replace(
        "PINS = {}", "PINS = {'" + name + "': 2}"), encoding="utf-8", newline=NL)
    check("cutoffs: a PINS entry makes it gateable", report(r).get(name, {}).get("gateable") is True)
    with (r / ".other.conf").open("a", encoding="utf-8", newline=NL) as fh:
        fh.write('G_CUTOFF="2026-04-04"' + NL)
    out = run([sys.executable, REPORT_REL, "--check"], r)
    check("cutoffs: arming a third key over a pin of 2 reds --check naming the signal",
          out.returncode == 1 and f"{name} = 3 (pin 2)" in out.stderr, out.stderr.strip()[-300:])


def _build_ci_rows(*conclusions) -> list:
    """Completed `push` runs, newest first, one per conclusion, as `gh run list --json` returns them."""
    return [{"databaseId": i, "status": "completed", "conclusion": c, "event": "push"}
            for i, c in enumerate(conclusions)]


def test_remote_ci_red_streak(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-8: the streak rules over canned rows, and the three non-live states.

    The reader is pointed at a host no remote matches, so `gh` refuses (or is absent): either way the
    signal must say DEAD PROBE, never a calm 0. No network answer is asserted here."""
    import types
    print("remote CI red streak (streak rules over canned rows; not asked, dead)")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    m = dr.measure_red_streak(_build_ci_rows("failure", "cancelled", "failure", "success"))
    check("a cancelled run neither ends nor extends the streak",
          m["streak"] == 2 and len(m["passed_over"]) == 1, f"got {m['streak']}")
    m = dr.measure_red_streak(_build_ci_rows("success", "failure"))
    check("a newest green reads 0", m["streak"] == 0 and not m["capped"], f"got {m}")
    m = dr.measure_red_streak(_build_ci_rows("failure", "timed_out", "startup_failure"))
    check("an all-red window reports its length, capped", m["streak"] == 3 and m["capped"], f"got {m}")
    m = dr.measure_red_streak(_build_ci_rows("cancelled", "skipped") + [{"databaseId": 9, "status": "in_progress"}])
    check("no verdict-bearing run reports no streak", m["streak"] is None, f"got {m}")

    r = make_repo(tmp, name="remoteci")
    ctx = types.SimpleNamespace(root=r, git=dr.Git(r, "refs/remotes/origin/main"), pins={},
                                remote_ci_workflow="", offline=False)
    check("no declared workflow is NOT ASKED",
          dr.build_remote_ci_red_streak(ctx).get("not_asked") is True)
    ctx.remote_ci_workflow, ctx.offline = "ci.yml", True
    check("--check / --offenders is NOT ASKED and spawns nothing",
          dr.build_remote_ci_red_streak(ctx).get("not_asked") is True)
    ctx.offline = False
    old = os.environ.get("GH_HOST")
    os.environ["GH_HOST"] = "nonexistent.invalid"
    try:
        got = dr.build_remote_ci_red_streak(ctx)
    finally:
        if old is None:
            os.environ.pop("GH_HOST", None)
        else:
            os.environ["GH_HOST"] = old
    check("an unreachable remote is DEAD PROBE, not a calm 0",
          got["live"] is False and not got.get("not_asked")
          and got["detail"][0]["note"].startswith("DEAD PROBE"), f"got {got}")


def test_auto_memory_pointers(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-53: `dangling_pointers_in_own_ledger` judges the backticked repo paths in a
    declared auto-memory directory against `git ls-files`, and its two non-live states."""
    import types
    print("auto-memory pointers (tracked vs untracked; not asked; dead)")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    r = tmp / "automem-repo"
    (r / "src").mkdir(parents=True)
    (r / "src" / "a.py").write_text("x = 1\n", encoding="utf-8", newline="\n")
    run(["git", "init", "-q", "-b", "main"], r)
    run(["git", "add", "-A"], r)
    run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", "seed",
         "--no-verify"], r)
    notes = tmp / "automem-notes"
    notes.mkdir()
    # One tracked path (with a line suffix), one untracked path under a tracked top-level directory,
    # and spans the probe must not judge: an untracked top level, a placeholder and a bare word.
    (notes / "n.md").write_text("See `src/a.py:3` and `src/gone.py`; not `elsewhere/x.py`, "
                                "`src/<name>.py` or `word`.\n", encoding="utf-8", newline="\n")
    ctx = types.SimpleNamespace(root=r, git=dr.Git(r, "main"), pins={}, auto_memory_dir=str(notes))
    got = dr.signal_dangling_pointers(ctx)
    check("auto-memory: one tracked and one untracked path read 1 of 2",
          got["value"] == 1 and got["of"] == 2 and got["live"] is True, f"got {got}")
    check("auto-memory: the detail row names the note and the untracked path",
          got["detail"] == [{"note_file": "n.md", "path": "src/gone.py"}], f"got {got['detail']}")
    check("auto-memory: report-only and pinless",
          got["gateable"] is False and got["tolerance"] is None, f"got {got}")
    ctx.auto_memory_dir = ""
    check("auto-memory: a blank declaration is NOT ASKED",
          dr.signal_dangling_pointers(ctx).get("not_asked") is True)
    ctx.auto_memory_dir = str(tmp / "no-such-dir")
    got = dr.signal_dangling_pointers(ctx)
    check("auto-memory: a missing directory is DEAD PROBE naming the resolved path",
          got["live"] is False and not got.get("not_asked")
          and "no-such-dir" in got["detail"][0]["note"], f"got {got}")
    key = dr.resolve_auto_memory_dir(r, "{checkout}").name
    check("auto-memory: {checkout} expands to a [A-Za-z0-9-] key",
          re.fullmatch(r"[A-Za-z0-9-]+", key) is not None, f"got {key}")


def test_stale_dossiers(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-37: the three states of `dossiers_older_than_their_paths` over canned
    `map_diff.py --stale-dossiers --json` output — the rule is the map kit's, so the arm grades only
    how this report reads its answer. The reader is swapped on the module and always restored."""
    import json
    import types
    print("dossiers older than their paths (canned map_diff output; not asked, dead, value)")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    name = "dossiers_older_than_their_paths"
    ctx = types.SimpleNamespace(root=tmp, pins={name: 2})
    rows = [{"feature": "b", "stale": True, "behind": 3}, {"feature": "a", "stale": True, "behind": 1},
            {"feature": "c", "stale": False, "behind": 0}]
    canned = {
        "value": (0, json.dumps({"of": 3, "stale": 2, "live": True, "note": "", "dossiers": rows}), ""),
        "dead": (0, json.dumps({"of": 0, "stale": 0, "live": False, "note": "the clone is shallow",
                                "dossiers": []}), ""),
        "garbled": (0, "{ not json", ""),
        "refused": (2, "", "map-diff refused: no .codebase-map.conf at the resolved repo root\nmore"),
        "absent": None,
    }
    real, got = dr.read_stale_dossiers, {}
    try:
        for state, answer in canned.items():
            dr.read_stale_dossiers = lambda _ctx, answer=answer: answer
            got[state] = dr.build_stale_dossiers(ctx)
    finally:
        dr.read_stale_dossiers = real
    v = got["value"]
    check("stale dossiers: a live answer reads the map's count, report-only, against its pin",
          (v["value"], v["of"], v["live"], v["gateable"], v["tolerance"]) == (2, 3, True, False, 2), f"got {v}")
    check("stale dossiers: the detail is the stale rows only, most-behind first as the map orders them",
          [r["feature"] for r in v["detail"]] == ["b", "a"], f"got {v['detail']}")
    d = got["dead"]
    check("stale dossiers: live false is DEAD PROBE quoting the map's note, never a calm 0",
          d["live"] is False and not d.get("not_asked")
          and d["detail"][0]["note"] == "DEAD PROBE — the clone is shallow", f"got {d}")
    g = got["garbled"]
    check("stale dossiers: unparseable output is DEAD PROBE",
          g["live"] is False and not g.get("not_asked") and g["detail"][0]["note"].startswith("DEAD PROBE"),
          f"got {g}")
    r = got["refused"]
    check("stale dossiers: an unadopted map (exit 2) is NOT ASKED, quoting the refusal",
          r.get("not_asked") is True and "no .codebase-map.conf" in r["detail"][0]["note"], f"got {r}")
    check("stale dossiers: no map kit beside this one is NOT ASKED",
          got["absent"].get("not_asked") is True, f"got {got['absent']}")


def test_live_builds_without_activity(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-54: `live_builds_without_activity` counts the `dormant` cells of the
    rendered LIVE.md table by header name, and its not-asked and dead states."""
    import types
    print("live builds without activity (fixture LIVE.md tables)")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    r = tmp / "live-activity"
    (r / "mem").mkdir(parents=True)
    ctx = types.SimpleNamespace(root=r, memory_root="mem")

    def read(*rows, head="| Build | Status | Last record | Activity |"):
        body = "\n".join([head, "|" + "---|" * (head.count("|") - 1)] + list(rows))
        (r / "mem" / "LIVE.md").write_text(f"# LIVE\n\nprose\n\n{body}\n\ntrailer\n",
                                           encoding="utf-8", newline="\n")
        return dr.build_live_builds_without_activity(ctx)

    three = ("| [bOne](builds/bOne/README.md) | SPECCED | 2026-08-01 | dormant |",
             "| [bTwo](builds/bTwo/README.md) | INPROGRESS | 2026-10-01 | active |",
             "| [bSix](builds/bSix/README.md) | SPECCED | 2026-07-02 | dormant |")
    got = read(*three)
    check("live activity: two dormant rows of three read 2 of 3, live, report-only and pinless",
          (got["value"], got["of"], got["live"], got["gateable"], got["tolerance"], got["unjudgeable"])
          == (2, 3, True, False, None, 0), f"got {got}")
    check("live activity: the detail names each dormant build and its last record",
          got["detail"] == [{"build": "bOne", "last_record": "2026-08-01"},
                            {"build": "bSix", "last_record": "2026-07-02"}], f"got {got['detail']}")
    later = read(*(row + " 4 |" for row in three),
                 head="| Build | Status | Last record | Activity | Landed-unclosed |")
    check("live activity: a column placed after Activity moves nothing",
          (later["value"], later["of"], later["detail"]) == (got["value"], got["of"], got["detail"]),
          f"got {later}")
    odd = read(three[0], three[1], three[2].replace("| dormant |", "| sleepy |"))
    check("live activity: an unknown cell is unjudgeable, never active",
          (odd["value"], odd["of"], odd["unjudgeable"]) == (1, 2, 1), f"got {odd}")
    bare = read(*(row.rsplit("|", 2)[0] + "|" for row in three),
                head="| Build | Status | Last record |")
    check("live activity: a table without the Activity header is NOT ASKED naming the column",
          bare.get("not_asked") is True and "Activity" in bare["detail"][0]["note"], f"got {bare}")
    empty = read()
    check("live activity: the column with no row is DEAD, not asked is not claimed",
          empty["live"] is False and not empty.get("not_asked") and empty["value"] == 0, f"got {empty}")
    (r / "mem" / "LIVE.md").unlink()
    check("live activity: no LIVE.md is NOT ASKED",
          dr.build_live_builds_without_activity(ctx).get("not_asked") is True)


_FLEET_SIG = "fleet_over_budget"


def _write_fleet_out(r: pathlib.Path, run: str, line: str) -> pathlib.Path:
    """One leg's stdout in a run record under the fixture's git dir, where the gate runner writes it."""
    d = r / ".git" / "gate-run" / run
    d.mkdir(parents=True, exist_ok=True)
    out = d / "0.out"
    out.write_text("unattended: some other line\n" + line + "\n", encoding="utf-8", newline="\n")
    return out


def test_fleet_over_budget(tmp: pathlib.Path) -> None:
    """TOOL-dUnstuckLanding-17 S10: the builds over budget, read from the newest bar run's fleet line.

    NOT ASKED without the unattended kit's conf, DEAD where the conf is present and no run record
    carries the line, and it MOVES with the line: one build over budget reads 1, `over none` reads 0
    while staying live, and deleting the record returns it to DEAD rather than a reassuring 0.
    """
    print("builds over their undeclared-write budget, over the check 23 fleet line")
    r = make_repo(tmp, name="fleet")
    got = report(r)[_FLEET_SIG]
    check("no .unattended.conf: the signal is NOT ASKED", got.get("not_asked") is True, f"got {got}")
    (r / ".unattended.conf").write_text("MEMORY_ROOT=memory\n", encoding="utf-8", newline="\n")
    got = report(r)[_FLEET_SIG]
    check("a conf and no run record: DEAD, not a clean 0",
          got["live"] is False and not got.get("not_asked"), f"got {got}")
    head8 = run(["git", "rev-parse", "HEAD"], r).stdout.strip()[:8]
    out = _write_fleet_out(r, "fx", "unattended: check 23 fleet — 3 undeclared write(s) over 9 graded pass(es) "
                                    "in 4 record(s) · budget 0 per build · over aFixture=2 · range whole (x) · at 0badc0de")
    got = report(r)[_FLEET_SIG]
    check("one build over budget reads value 1", got["value"] == 1, f"got {got['value']}")
    check("`of` is the record count the line states", got["of"] == 4, f"got {got['of']}")
    check("report-only: the fleet total is never a refusal", got["gateable"] is False)
    check("the detail names the build and its count", any("aFixture 2" in str(d) for d in got["detail"]),
          f"detail {got['detail']}")
    check("the detail notes that HEAD moved past the line's `at`",
          any("moved to " + head8 in str(d) for d in got["detail"]), f"detail {got['detail']}")
    out.write_text("unattended: check 23 fleet — 0 undeclared write(s) over 9 graded pass(es) in 4 record(s) "
                   "· budget 0 per build · over none · range whole (x) · at " + head8 + "\n",
                   encoding="utf-8", newline="\n")
    got = report(r)[_FLEET_SIG]
    check("`over none` reads 0 and stays LIVE", got["value"] == 0 and got["live"] is True, f"got {got}")
    # Implementation review round 1, M10: check 23 prints `over unjudged` when no budget is declared,
    # and that is a fleet nobody judged, never zero builds over it.
    out.write_text("unattended: check 23 fleet — 3 undeclared write(s) over 9 graded pass(es) in 4 record(s) "
                   "· budget undeclared per build · over unjudged · range whole (x) · at " + head8 + "\n",
                   encoding="utf-8", newline="\n")
    got = report(r)[_FLEET_SIG]
    check("`over unjudged` reads DEAD, never a live 0 (M10)",
          got["live"] is False and not got.get("not_asked") and "over unjudged" in str(got["detail"]),
          f"got {got}")
    out.unlink()
    got = report(r)[_FLEET_SIG]
    check("deleting the record returns it to DEAD, not a live 0",
          got["live"] is False, f"live={got['live']} value={got['value']}")


# ---------------------------------------------------------------------------------------------
# TOOL-dLoggedFlight-13 — run records left non-terminal after their build merged
# ---------------------------------------------------------------------------------------------

_RUN_SIG = "run_records_nonterminal_but_merged"


def _write_run_record(r: pathlib.Path, rel: str, facts: dict, rows=()) -> str:
    """A run-state file in the layout the driver leaves: its scaffold's header and generated region,
    `## Run facts` with one `<key>: <value>` line per fact, then `## Parked` with every row on its own
    line after a blank one, which is how `park` appends. A fact passed as None is absent, the way a
    record reads when no verb ever wrote it. Returns `rel`, the repo-relative path."""
    NL = chr(10)
    p = r / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    body = [f"# {p.parent.name} - run state", "", "<!-- run:generated -->", "<!-- /run:generated -->",
            "", "## Run facts"]
    body += [f"{k}: {v}" for k, v in facts.items() if v is not None]
    body += ["", "## Parked"]
    for row in rows:
        body += ["", row]
    p.write_text(NL.join(body) + NL, encoding="utf-8", newline=NL)
    return rel


def _build_park_row(kind: str, item: str) -> str:
    """One parked row, in the byte shape of the driver's `park`."""
    return f"2026-01-01T00:00:00Z {kind} \u00b7 item {item} \u00b7 reason a fixture row"


def _build_run_ctx(dr, r: pathlib.Path, base_ref: str = "main"):
    """The four attributes the signal reads, over a fixture repo, and nothing the full `Ctx` would
    derive from a charter or a family grammar this signal never consults."""
    import types
    return types.SimpleNamespace(root=r, memory_root=FIXTURE_MEMORY_ROOT, git=dr.Git(r, base_ref),
                                 pins={})


def _measure_git_calls(dr, r: pathlib.Path, subject=None) -> int:
    """How many git processes ONE call of the signal starts. Counted at the report module's own
    `subprocess` binding, which both `Git.run` and the held-open batch resolve at call time, so no
    other code in this process is touched and the binding is restored whatever happens. `subject` is
    the function called over a fresh context, the non-terminal signal where none is named."""
    import types
    real = dr.subprocess
    calls: list = []

    def run_counted(cmd, *a, **k):
        if cmd and cmd[0] == "git":
            calls.append(cmd)
        return real.run(cmd, *a, **k)

    def run_piped_counted(cmd, *a, **k):
        if cmd and cmd[0] == "git":
            calls.append(cmd)
        return real.Popen(cmd, *a, **k)

    proxy = types.SimpleNamespace(**{k: getattr(real, k) for k in dir(real) if not k.startswith("__")})
    proxy.run, proxy.Popen = run_counted, run_piped_counted
    dr.subprocess = proxy
    try:
        (subject or dr.build_nonterminal_merged_runs)(_build_run_ctx(dr, r))
    finally:
        dr.subprocess = real
    return len(calls)


def test_nonterminal_merged_runs(tmp: pathlib.Path) -> None:
    """TOOL-dLoggedFlight-13 AC1 AC2 AC3 AC4: every row of the S3 table and every alternative in it,
    the witness-to-base test in both stale directions, each other unjudgeable reason, the read at HEAD
    and never the working tree, the report-only property, and the call count.

    The value is asserted against THIS fixture and never against the tree the kit lives in, whose
    count moves with every landing. Witnesses are real commits on and off `main`, so ancestry is
    git's answer rather than a double of it.
    """
    print("run records left non-terminal after their build merged")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    NL = chr(10)
    B = f"{FIXTURE_MEMORY_ROOT}/builds"
    P = _build_park_row
    r = make_repo(tmp, name="runrecords")

    def run_commit(msg: str) -> None:
        run(["git", "add", "-A"], r)
        run(["git", "commit", "-q", "-m", msg, "--no-verify"], r)

    def read_signal(base_ref: str = "main") -> dict:
        return dr.build_nonterminal_merged_runs(_build_run_ctx(dr, r, base_ref))

    # ---- S4, the two empty states. Nothing adopted is NOT ASKED; the kit's conf with no record is a
    # population that may have gone blind, so it is DEAD. Neither may read as a clean zero.
    empty = read_signal()
    check("run records: none tracked and no .unattended.conf reads NOT ASKED, not a clean zero",
          empty.get("not_asked") is True and empty["live"] is False, f"{empty}")
    (r / ".unattended.conf").write_text("# the kit is adopted and no run has started" + NL,
                                        encoding="utf-8", newline=NL)
    run_commit("chore: adopt the unattended kit, with no run yet")
    dead = read_signal()
    check("run records: the conf with no record reads DEAD, not NOT ASKED",
          dead["live"] is False and not dead.get("not_asked"), f"{dead}")

    early = run(["git", "rev-list", "--max-parents=0", "main"], r).stdout.strip()
    tip = run(["git", "rev-parse", "main"], r).stdout.strip()
    side = run(["git", "rev-parse", "sidework"], r).stdout.strip()
    check("run records: the fixture has a merged tip, its root and an unmerged side commit",
          len({early, tip, side}) == 3 and all(len(s) == 40 for s in (early, tip, side)),
          f"early={early!r} tip={tip!r} side={side!r}")

    # ---- AC3, the S3 table. Every counted record has its witness AHEAD of its base on `main`, so only
    # its last parked row decides its sub-class. One fixture per alternative, not per row: a table row
    # listing four kinds is four ways to be wrong.
    counted: dict = {}

    def add_counted(slug: str, subclass: str, rows=(), phase: str = "BUILDING") -> None:
        rel = _write_run_record(r, f"{B}/{slug}/RUN.md",
                                {"phase": phase, "witness": tip, "base": early}, rows)
        counted[rel] = (phase, subclass)

    add_counted("tRetire", "retired-unit", [P("rescope", "retire TOOL-tRun-1")])
    add_counted("tSupersede", "retired-unit", [P("rescope", "supersede TOOL-tRun-2 -> TOOL-tRun-3")])
    # `defer` joined the owed acts in TOOL-dUnstuckLanding-18: declared scope set aside, like the two above.
    add_counted("tDefer", "retired-unit", [P("rescope", "defer TOOL-tRun-5")])
    add_counted("tRescopeAdd", "other", [P("rescope", "add TOOL-tRun-4")])
    # The act is the item's FIRST word. A reader matching `retire` anywhere in the item reads this one
    # as a retirement.
    add_counted("tSecondWord", "other", [P("rescope", "add retire")])
    for kind in ("decision", "abort", "override", "waiver", "handoff"):
        add_counted("tOwed" + kind.capitalize(), "surfaced-park", [P(kind, "a question refused")])
    add_counted("tNoRows", "no-rows")
    for kind in ("review", "dispatch", "brief", "proposal"):
        add_counted("tHistory" + kind.capitalize(), "other", [P(kind, "a declaration")])
    # LAST, not ANY: the same two rows in both orders, so a reader that asks "is there an owed row"
    # passes one of these and fails the other.
    add_counted("tOwedThenReview", "other", [P("decision", "asked first"), P("review", "then this")])
    add_counted("tReviewThenOwed", "surfaced-park", [P("review", "this first"), P("decision", "then asked")])
    # A kind the driver does not declare is not a parked row, so it cannot be the last one.
    add_counted("tUndeclaredKind", "surfaced-park",
                [P("decision", "asked"), P("heartbeat", "no driver writes this kind")])
    # ---- TOOL-aMendedFleet-47, derived LANDED: a `LANDING` record whose landing commit is on `main`
    # is neither counted nor unjudgeable, whatever its witness says. Without the derivation these
    # three read as a counted row and as the two witness-at-or-behind-base rows below, which is what
    # makes them discriminate.
    derived = [
        _write_run_record(r, f"{B}/tLanding/RUN.md", {"phase": "LANDING", "witness": tip, "base": early},
                          [P("decision", "asked")]),
        _write_run_record(r, f"{B}/tLandingAtBase/RUN.md", {"phase": "LANDING", "witness": tip, "base": tip}),
        _write_run_record(r, f"{B}/tLandingBehind/RUN.md", {"phase": "LANDING", "witness": early, "base": tip}),
    ]

    # ---- AC3, the unjudgeable half: counted apart with the reason, never scored clean, never counted.
    # The two stale-witness rows are BUILDING, since a LANDING one on `main` now derives LANDED.
    stale: dict = {}

    def add_stale(slug: str, facts: dict, relation: str, why: str) -> None:
        stale[_write_run_record(r, f"{B}/{slug}/RUN.md", facts)] = (relation, why)

    add_stale("tClosedAtBase", {"phase": "BUILDING", "witness": tip, "base": tip},
              "equal", "witness not re-written since preflight")
    add_stale("tBehindBase", {"phase": "BUILDING", "witness": early, "base": tip},
              "behind", "witness not re-written since preflight")
    add_stale("tNoPhase", {"witness": tip, "base": early}, "unknown", "no phase: fact")
    add_stale("tNoWitness", {"phase": "BUILDING", "base": early}, "unknown", "no witness: fact")
    add_stale("tNamedWitness", {"phase": "BUILDING", "witness": "main", "base": early},
              "unknown", "witness is not a sha")
    add_stale("tGhostWitness", {"phase": "BUILDING", "witness": "0" * 40, "base": early},
              "unknown", "witness does not resolve")
    add_stale("tNoBase", {"phase": "BUILDING", "witness": tip}, "unknown", "no base: fact")
    add_stale("tGhostBase", {"phase": "BUILDING", "witness": tip, "base": "f" * 40},
              "unknown", "base does not resolve")
    # Its witness IS behind this base in truth, which is exactly what one walk of `main` cannot see.
    add_stale("tBaseOffMain", {"phase": "BUILDING", "witness": early, "base": side},
              "unknown", "base is not on main")

    # ---- Neither counted nor listed: terminal, archived, and unmerged.
    quiet = [
        _write_run_record(r, f"{B}/tLanded/RUN.md", {"phase": "LANDED", "witness": tip, "base": early},
                          [P("decision", "asked")]),
        _write_run_record(r, f"{B}/tArchived/RUN.ABORTED.0123abcd.md",
                          {"phase": "ABORTED", "witness": tip, "base": early}),
        _write_run_record(r, f"{B}/tUnmerged/RUN.md", {"phase": "BUILDING", "witness": side, "base": early}),
        # AC1's HEAD-not-worktree pair, committed terminal here and edited live below.
        _write_run_record(r, f"{B}/tWorktreeLive/RUN.md", {"phase": "LANDED", "witness": tip, "base": early}),
    ]
    # ...and its mirror, committed live here and edited terminal below.
    add_counted("tWorktreeDone", "no-rows")
    run_commit("chore: run records")

    # ...and a LANDING record whose landing commit is NOT on `main`: committed on a branch HEAD now
    # sits on, so the derivation must read the base ref and never HEAD. It stays counted.
    run(["git", "checkout", "-q", "-b", "landing-ahead"], r)
    add_counted("tLandingAhead", "surfaced-park", [P("decision", "asked")], phase="LANDING")
    run(["git", "add", "--", f"{B}/tLandingAhead/RUN.md"], r)
    run(["git", "commit", "-q", "-m", "chore: a landing not yet on main", "--no-verify"], r)

    # AFTER the commit the working tree contradicts HEAD for two records, and a third record exists in
    # the working tree alone. Every one of these is read at HEAD or not at all.
    _write_run_record(r, f"{B}/tWorktreeLive/RUN.md", {"phase": "BUILDING", "witness": tip, "base": early})
    _write_run_record(r, f"{B}/tWorktreeDone/RUN.md", {"phase": "LANDED", "witness": tip, "base": early})
    untracked = _write_run_record(r, f"{B}/tUntracked/RUN.md",
                                  {"phase": "BUILDING", "witness": tip, "base": early})

    got = read_signal()
    rows = {d.split(" ", 1)[0]: d for d in got["detail"] if not d.startswith("note")}
    tracked = len(counted) + len(stale) + len(quiet) + len(derived)
    check("run records: the population is every TRACKED record, the archive in and the untracked out",
          got["of"] == tracked, f"of {got['of']}, wanted {tracked}")
    check("run records: live over a non-empty population", got["live"] is True, f"live={got['live']}")
    check("run records: the value is the counted fixtures and nothing else",
          got["value"] == len(counted), f"value {got['value']}, wanted {len(counted)}: {got['detail']}")
    check("run records: every unjudgeable fixture is counted apart",
          got["unjudgeable"] == len(stale), f"unjudgeable {got['unjudgeable']}, wanted {len(stale)}")
    for rel, (phase, sub) in sorted(counted.items()):
        want = f"{rel} {phase} {tip[:8]} ahead {sub}"
        check(f"run records: {rel.split('/')[2]} reads {sub}",
              rows.get(rel) == want, f"got {rows.get(rel)!r}, wanted {want!r}")
    for rel, (relation, why) in sorted(stale.items()):
        row = rows.get(rel, "")
        check(f"run records: {rel.split('/')[2]} is unjudgeable, {relation}, with its reason",
              f" {relation} unjudgeable \u2014 {why}" in row, f"got {row!r}")
    for rel in quiet + derived + [untracked]:
        check(f"run records: {rel.split('/')[2]} is neither counted nor listed",
              rel not in rows, f"got {rows.get(rel)!r}")
    check("run records: every LANDING record landed on main reads derived LANDED, and only those",
          got.get("derived_landed") == len(derived), f"derived_landed {got.get('derived_landed')}")
    want_sum = f"derived \u2014 {len(derived)} of {len(derived) + 1} LANDING records read LANDED"
    check("run records: the derived summary line sits just before the closing note",
          got["detail"][-2].startswith(want_sum), f"got {got['detail'][-2]!r}, wanted {want_sum!r}")
    check("run records: the refused-landing note closes the detail",
          got["detail"][-1].startswith("note \u2014 a refused landing"), f"last {got['detail'][-1]!r}")

    # ---- AC2, through the CLI: registered in SIGNALS, and `--check` exits 0 with the value above its
    # pin, because nothing gates on a report-only signal. The premise is asserted first.
    rep = report(r)
    check("run records: the report registers the signal", _RUN_SIG in rep, f"signals {sorted(rep)}")
    check("run records: the CLI reads what the in-process call read",
          rep.get(_RUN_SIG, {}).get("value") == got["value"], f"cli {rep.get(_RUN_SIG)}")
    chk = run([sys.executable, REPORT_REL, "--check"], r)
    check("run records: --check exits 0 with the signal over its pin, because it is report-only",
          chk.returncode == 0 and got["value"] > 0,
          f"rc={chk.returncode} value={got['value']} stderr={chk.stderr.strip()[:200]}")

    # ---- A walk that cannot happen is DEAD with its stage named, never a clean zero.
    blind = read_signal("no-such-branch")
    check("run records: a base ref the rev-list cannot walk reads DEAD, not a clean zero",
          blind["live"] is False and blind["value"] == 0 and "rev-list" in str(blind["detail"]),
          f"{blind}")

    # ---- AC4, three git calls for five records and for fifty, four once LANDING records exist. A
    # separate minimal repo, so the count
    # is over a population the arm sets rather than over whatever the fixture above accumulated.
    small = tmp / "runcalls"
    small.mkdir()
    run(["git", "init", "-q", "-b", "main"], small)
    run(["git", "config", "user.email", "selftest@example.com"], small)
    run(["git", "config", "user.name", "selftest"], small)
    for name in ("base", "witness"):
        (small / f"{name}.txt").write_text(name + NL, encoding="utf-8", newline=NL)
        run(["git", "add", "-A"], small)
        run(["git", "commit", "-q", "-m", name, "--no-verify"], small)
    wit = run(["git", "rev-parse", "HEAD"], small).stdout.strip()
    bas = run(["git", "rev-parse", "HEAD~1"], small).stdout.strip()
    # TOOL-aMendedFleet-47: the third size adds FIVE `LANDING` records, each derived LANDED, so one
    # batched `log` costs a fourth call where a per-record lookup would cost eight.
    per_size = {}
    for lo, hi, phase in ((0, 5, "BUILDING"), (5, 50, "BUILDING"), (50, 55, "LANDING")):
        for i in range(lo, hi):
            _write_run_record(small, f"{B}/tCall{i}/RUN.md",
                              {"phase": phase, "witness": wit, "base": bas}, [P("decision", "x")])
        run(["git", "add", "-A"], small)
        run(["git", "commit", "-q", "-m", f"{hi} records", "--no-verify"], small)
        seen = dr.build_nonterminal_merged_runs(_build_run_ctx(dr, small))
        per_size[hi] = (_measure_git_calls(dr, small), seen["value"], seen.get("derived_landed"))
    for size, (calls, value, got_derived) in sorted(per_size.items()):
        landings = max(0, size - 50)
        check(f"run records: {size} records are all read, {landings} derived LANDED (the premise)",
              value == size - landings and got_derived == landings,
              f"value {value} derived_landed {got_derived}")
        want_calls = 4 if landings else 3
        check(f"run records: {size} records cost {want_calls} git calls", calls == want_calls,
              f"{calls} calls")


def _extract_driver_set(text: str, name: str):
    """The members of one space-separated declaration in the driver, or None where it is absent."""
    m = re.search(r"^" + name + r'="([^"]*)"', text, re.M)
    return set(m.group(1).split()) if m else None


def test_park_sets_match_the_driver(tmp: pathlib.Path) -> None:
    """TOOL-dLoggedFlight-13 AC6: the engine's copies of the driver's four sets, held to the driver.

    The engine SPELLS them because drift-audit runs in trees with no unattended kit; this arm is what
    keeps a spelling from becoming a second vocabulary. The driver is reached by a path derived from
    this kit's own directory, as the recall and workflow arms above reach theirs.
    """
    print("run-record sets vs the unattended driver's own declarations")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    try:
        driver = resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"
    except LookupError:
        driver = None
    if driver is None or not driver.exists():
        skip("run-record sets equal the driver's", "no unattended driver beside this kit")
        return
    text = driver.read_text(encoding="utf-8", errors="replace")
    pairs = (("PHASES_TERMINAL", dr._RUN_PHASES_TERMINAL), ("PARK_KINDS", dr._RUN_PARK_KINDS),
             ("PARK_KINDS_OWED", dr._RUN_PARK_KINDS_OWED), ("PARK_ACTS_OWED", dr._RUN_PARK_ACTS_OWED))
    for name, mine in pairs:
        theirs = _extract_driver_set(text, name)
        check(f"driver sets: {name} is declared where this arm reads it", bool(theirs),
              "the declaration moved or emptied, so nothing below would compare anything")
        if not theirs:
            continue
        check(f"driver sets: every {name} member the driver declares is in the engine",
              not (theirs - set(mine)), f"engine lacks {sorted(theirs - set(mine))}")
        check(f"driver sets: every {name} member the engine spells is the driver's",
              not (set(mine) - theirs), f"driver lacks {sorted(set(mine) - theirs)}")

    # THE CONTROL, so the comparison is seen to discriminate: the driver as it would read after gaining
    # an owed kind the table lacks. The doctored copy is the real file with one member added, never a
    # synthetic declaration, so the extraction it exercises is the one the checks above rely on.
    doctored = re.sub(r'^PARK_KINDS_OWED="([^"]*)"', r'PARK_KINDS_OWED="\1 heartbeat"', text,
                      count=1, flags=re.M)
    grown = _extract_driver_set(doctored, "PARK_KINDS_OWED") or set()
    check("driver sets: control — a driver that gains an owed kind reads unequal",
          "heartbeat" in grown - set(dr._RUN_PARK_KINDS_OWED), f"extracted {sorted(grown)}")


def test_drift_history(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-48 S7: `--check` appends one group per run to the common dir's history,
    the other modes write nothing, the key hash sees a member swap, and a failed write is no verdict."""
    print("drift history (--check appends a group; other modes never write; a failed write is no verdict)")
    import json
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    r = make_repo(tmp, name="history")
    hist = r / ".git" / dr.HISTORY_FILE
    n = len(json.loads(run([sys.executable, REPORT_REL, "--json"], r).stdout))
    first = run([sys.executable, REPORT_REL, "--check"], r)
    run([sys.executable, REPORT_REL, "--check"], r)
    lines = hist.read_text(encoding="utf-8").splitlines() if hist.is_file() else []
    check("history: two --check runs write one header and two groups of one row per record",
          len(lines) == 1 + 2 * n and lines[0] == "\t".join(dr.HISTORY_COLUMNS)
          and sum(ln.startswith("#") for ln in lines) == 1, f"{len(lines)} lines for {n} records")
    check("history: every row carries nine fields and a state in the four-state set",
          all(len(ln.split("\t")) == 9 and ln.split("\t")[5] in ("live", "dead", "not-asked", "declared-empty")
              for ln in lines[1:]) and bool(lines[1:]), lines[1] if len(lines) > 1 else "")
    run([sys.executable, REPORT_REL, "--offenders"], r)
    run([sys.executable, REPORT_REL, "--json"], r)
    run([sys.executable, REPORT_REL, "--json", "--check"], r)
    after = hist.read_text(encoding="utf-8").splitlines() if hist.is_file() else []
    check("history: --offenders, --json and --json --check write nothing", after == lines,
          f"{len(lines)} -> {len(after)} lines")

    def measure_key_hash(detail):
        rec = {"signal": "s", "value": len(detail), "of": 9, "live": True, "detail": detail}
        return dr.build_history_rows([rec], set(), "t", "h", "b", "bs")[0].split("\t")[8]

    one = measure_key_hash([{"path": "a.md"}, {"path": "b.md"}])
    check("history: a member swap at an equal count moves key_hash",
          one != measure_key_hash([{"path": "a.md"}, {"path": "c.md"}]), one)
    check("history: a moved line locator does not move key_hash",
          measure_key_hash([{"path": "a.md:3"}, {"path": "b.md", "line": 4}])
          == measure_key_hash([{"path": "a.md:7"}, {"path": "b.md", "line": 9}]), one)

    hist.unlink()
    hist.mkdir()
    squat = run([sys.executable, REPORT_REL, "--check"], r)
    check("history: a directory on the file's name leaves the exit status unchanged",
          squat.returncode == first.returncode, f"{first.returncode} -> {squat.returncode}")
    check("history: ...and stderr names the path it could not write",
          "history NOT written to" in squat.stderr and dr.HISTORY_FILE in squat.stderr, squat.stderr[-300:])


def test_drift_delta(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-49: `--delta` prints a moved, a hash-only and no unchanged signal between a
    reading at BASE and one at HEAD, and each of the four no-delta cases is one `skipped` line at 0."""
    print("drift delta (--delta reads the history; every miss is one skipped line, never a zero delta)")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    r = make_repo(tmp, name="delta")
    for i in range(3):
        run(["git", "commit", "-q", "--allow-empty", "-m", f"delta {i}", "--no-verify"], r)
    base = run(["git", "rev-parse", "HEAD~3"], r).stdout.strip()
    head = run(["git", "rev-parse", "HEAD"], r).stdout.strip()
    hist = r / ".git" / dr.HISTORY_FILE
    header = "\t".join(dr.HISTORY_COLUMNS) + "\n"

    def build_group(utc, sha, moved, hashed):
        return "".join("\t".join((utc, sha, "b", "bs", sig, "live", val, "9", kh)) + "\n" for sig, val, kh in
                       (("moved", moved, "aa"), ("hashed", "4", hashed), ("same", "5", "cc")))

    at_base, at_head = build_group("t1", base, "7", "bb"), build_group("t2", head, "2", "dd")

    def measure_delta(text, *args):
        if text is None:
            hist.unlink(missing_ok=True)
        else:
            hist.write_text(text, encoding="utf-8", newline="\n")
        return run([sys.executable, REPORT_REL, "--delta", *(args or ("HEAD~3", "HEAD"))], r)

    out = measure_delta(header + at_base + at_head)
    lines = out.stdout.splitlines()
    check("delta: both readings are named equal to their ends",
          bool(lines) and lines[0].count("(equal)") == 2, out.stdout + out.stderr)
    check("delta: a moved value prints one line", any(ln.endswith("moved 7 -> 2") for ln in lines), out.stdout)
    check("delta: a hash-only move prints `members changed`",
          any(ln.endswith("hashed 4 -> 4 (members changed)") for ln in lines), out.stdout)
    check("delta: an unchanged signal prints nothing", not any(" same " in ln for ln in lines), out.stdout)
    for label, text, why in (("no history file", None, "no drift history"),
                             ("a foreign header", "utc\tsha\n" + at_base + at_head, "header"),
                             ("no reading at BASE", header + at_head, "at or before BASE"),
                             ("no reading inside BASE..HEAD", header + at_base, "inside BASE..HEAD")):
        out = measure_delta(text)
        check(f"delta: {label} is one skipped line at exit 0",
              out.returncode == 0 and out.stdout.splitlines() == [out.stdout.strip()]
              and "skipped" in out.stdout and why in out.stdout, f"{out.returncode} {out.stdout!r}")
    out = measure_delta(header + at_base + at_head, "0000000", "HEAD")
    check("delta: an argument that is not a commit exits 2", out.returncode == 2, f"{out.returncode}")


def test_dead_streaks(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-90 S8: `derive_dead_streaks` counts READINGS, not groups, by header, with
    absence ending a streak; the report names a report-only probe dead past the limit, and a stale
    `DEAD_FILED` entry, and neither moves `--check`'s exit."""
    print("dead streaks (readings by sha, columns by header, the limit names retirement, report only)")
    import json
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    cols = list(dr.HISTORY_COLUMNS)

    def write_hist(path, readings, order=cols):
        # `readings` is a list of (sha, {signal: state}); one group per entry, utc unique per entry.
        text = "\t".join(order) + "\n"
        for i, (sha, states) in enumerate(readings):
            for sig, state in states.items():
                row = {"#utc": f"t{i}", "sha": sha, "base_ref": "b", "base_sha": "bs", "signal": sig,
                       "state": state, "value": "0", "of": "0", "key_hash": "-"}
                text += "\t".join(row[c] for c in order) + "\n"
        path.write_text(text, encoding="utf-8", newline="\n")

    hist = tmp / "streaks.tsv"
    seq = [("s0", {"d3": "live", "back": "dead", "gone": "dead"})] + [
        (f"s{i}", {"d3": "dead", "back": "dead", "gone": "dead"}) for i in (1, 2)] + [
        ("s3", {"d3": "dead", "back": "live"})]
    write_hist(hist, seq)
    got = dr.derive_dead_streaks(hist)
    check("streaks: dead in the last three readings counts 3; live or absent newest counts 0",
          got is not None and got[0] == {"d3": 3, "back": 0, "gone": 0} and got[1] == 4, f"{got}")
    write_hist(hist, seq[:3] + [("s2", {"d3": "dead", "back": "dead", "gone": "dead"})] + seq[3:])
    again = dr.derive_dead_streaks(hist)
    check("streaks: a repeated-sha group is one reading, so it ages nothing",
          again == got, f"{again} vs {got}")
    write_hist(hist, seq, order=list(reversed(cols)))
    check("streaks: a reordered header reads the same", dr.derive_dead_streaks(hist) == got,
          f"{dr.derive_dead_streaks(hist)}")
    write_hist(hist, [(f"s{i}", {"d": "dead"}) for i in range(10)])
    check("streaks: ten dead readings count 10, the limit's default",
          dr.derive_dead_streaks(hist) == ({"d": 10}, 10) and dr.DEFAULT_DEAD_READINGS_LIMIT == 10,
          f"{dr.derive_dead_streaks(hist)}")
    check("streaks: a missing file is None, never zero streaks",
          dr.derive_dead_streaks(tmp / "no-such.tsv") is None)
    hist.write_text("utc\tsha\n", encoding="utf-8", newline="\n")
    check("streaks: a foreign header is None", dr.derive_dead_streaks(hist) is None)

    r = make_repo(tmp, name="streaks")
    recs = json.loads(run([sys.executable, REPORT_REL, "--json"], r).stdout)
    check("streaks: with no history every record's dead_readings is null",
          bool(recs) and all(s.get("dead_readings", "x") is None for s in recs), "")
    human = run([sys.executable, REPORT_REL], r).stdout
    check("streaks: no history prints the no-history liveness line",
          "# dead-for-N: no history at" in human, human[:400])
    rc_absent = run([sys.executable, REPORT_REL, "--check"], r).returncode
    (r / ".git" / dr.HISTORY_FILE).unlink(missing_ok=True)
    dead = [s["signal"] for s in recs if not s["live"] and not s["gateable"] and not s.get("not_asked")
            and s["signal"] != "handkept_inventories_disagreeing_with_source"]
    if not dead:
        skip("streaks: the limit's status line", "the fixture reads no report-only signal DEAD")
    else:
        sig = dead[0]
        write_hist(r / ".git" / dr.HISTORY_FILE, [(f"{i:040x}", {sig: "dead"}) for i in range(10)])
        human = run([sys.executable, REPORT_REL], r).stdout
        row = next((ln for ln in human.splitlines() if ln.strip().startswith(sig)), "")
        check("streaks: a report-only probe dead for the limit names SIGNALS and DEAD_FILED",
              "DEAD PROBE for 10 readings" in row and "DEAD_FILED" in row, row)
        check("streaks: the liveness line counts the readings it found",
              "# dead-for-N: 10 readings recorded at" in human, human[:400])
        check("streaks: --json carries dead_readings 10 for it",
              next(s for s in json.loads(run([sys.executable, REPORT_REL, "--json"], r).stdout)
                   if s["signal"] == sig)["dead_readings"] == 10, "")
        rc_present = run([sys.executable, REPORT_REL, "--check"], r).returncode
        check("streaks: --check exits the same with the history present and absent",
              rc_present == rc_absent, f"{rc_absent} -> {rc_present}")
        write_hist(r / ".git" / dr.HISTORY_FILE, [(f"{i:040x}", {sig: "dead"}) for i in range(10)])
    layer = r / KIT_NAME / "drift_signals.py"
    filed = {"no_such_signal": "X-1", **({dead[0]: "X-2"} if dead else {})}
    layer.write_text(layer.read_text(encoding="utf-8") + f"DEAD_FILED = {filed!r}\n",
                     encoding="utf-8", newline="\n")
    human = run([sys.executable, REPORT_REL], r).stdout
    check("streaks: a DEAD_FILED entry for a signal not in the report is named in the header",
          any(ln.startswith("# dead-for-N: DEAD_FILED names no_such_signal") and "take the entry out" in ln
              for ln in human.splitlines()), human[:600])
    if dead:
        row = next((ln for ln in human.splitlines() if ln.strip().startswith(dead[0])), "")
        check("streaks: a filed dead probe prints the filed id", "filed X-2" in row, row)


def test_escape_ratio(tmp: pathlib.Path) -> None:
    """TOOL-aMendedFleet-50 S9: `--escape-ratio` over a fixture month holding a merge-landed contained
    fix, a merge-landed escaped fix, a direct fix, a stamp-only fix and a fix touching no product path."""
    print("escape ratio (landings by first parent, blame in the parent, stamps out, DIRECT named)")
    import json

    r = make_repo(tmp, name="escape")
    # Every commit of the arm is dated into one month; make_repo's own commits are dated now, so the
    # month's landings are exactly the ones made here.
    when = {"GIT_AUTHOR_DATE": "2026-03-15T12:00:00Z", "GIT_COMMITTER_DATE": "2026-03-15T12:00:00Z"}

    def build_commit(subject: str, files: dict) -> str:
        for rel, text in files.items():
            (r / rel).write_text(text, encoding="utf-8", newline="\n")
        run(["git", "add", "-A"], r)
        run(["git", "commit", "-qm", subject, "--no-verify"], r, env=when)
        return run(["git", "rev-parse", "HEAD"], r).stdout.strip()

    build_commit("feat: the library", {"src/lib.py": "one\ntwo\nthree\n", "conf/kit.toml": 'version = "1.0"\n'})
    run(["git", "checkout", "-q", "-b", "topic"], r)
    build_commit("feat: branch-local code", {"src/branch.py": "x\ny\n"})
    contained = build_commit("fix(topic): repair branch-local code", {"src/branch.py": "x\nY\n"})
    escaped = build_commit("fix(topic): repair code main already had", {"src/lib.py": "ONE\ntwo\nthree\n"})
    run(["git", "checkout", "-q", "main"], r)
    run(["git", "merge", "-q", "--no-ff", "--no-verify", "-m", "merge topic", "topic"], r, env=when)
    merge = run(["git", "rev-parse", "HEAD"], r).stdout.strip()
    direct = build_commit("fix: repair on the first-parent line", {"src/lib.py": "ONE\ntwo\nTHREE\n"})
    stamp = build_commit("fix: bump the stamp", {"conf/kit.toml": 'version = "1.1"\n'})
    other = build_commit("fix: a file outside the product", {"notes.txt": "n\n"})

    out = run([sys.executable, REPORT_REL, "--escape-ratio", "2026-03", "--json"], r)
    res = json.loads(out.stdout) if out.returncode == 0 and out.stdout.strip() else {}
    by = {f["sha"]: f for f in res.get("fixes", [])}
    check("escape: n counts the contained, the escaped and the direct fix, two of them escaped",
          res.get("n") == 3 and res.get("escaped") == 2, f"rc {out.returncode} {out.stderr[-300:]} {res}")
    got = by.get(contained, {})
    check("escape: a merge-landed fix blaming only its own branch is contained",
          got.get("class") == "contained" and got.get("landing") == merge
          and got.get("blamed_landings") == [merge] and got.get("direct") is False, str(got))
    got = by.get(escaped, {})
    check("escape: a merge-landed fix blaming code already on main is escaped",
          got.get("class") == "escaped" and got.get("landing") == merge and merge not in got.get("blamed_landings", [merge]),
          str(got))
    got = by.get(direct, {})
    check("escape: a direct fix is its own landing, named DIRECT, and escaped",
          got.get("class") == "escaped" and got.get("landing") == direct and got.get("direct") is True
          and res.get("direct") == 1, str(got))
    check("escape: a stamp-only fix is unclassified and outside n",
          by.get(stamp, {}).get("class") == "stamp-only" and res.get("unclassified") == {"stamp-only": 1},
          str(res.get("unclassified")))
    check("escape: a fix touching no product path is never read", other not in by and len(by) == 4,
          str(sorted(f["class"] for f in by.values())))
    text = run([sys.executable, REPORT_REL, "--escape-ratio", "2026-03"], r)
    check("escape: the text form prints the ratio with its interval and the caveat line",
          "Wilson interval" in text.stdout and text.stdout.rstrip().endswith("not evidence of an effect"),
          text.stdout[-400:])
    empty = run([sys.executable, REPORT_REL, "--escape-ratio", "2020-01"], r)
    lines = empty.stdout.splitlines()
    check("escape: an empty month prints n 0, says it is empty, and prints no ratio",
          empty.returncode == 0 and any(ln.startswith("n ") and "empty" in ln for ln in lines)
          and not any(ln.startswith("ratio") for ln in lines), empty.stdout)
    bad = run([sys.executable, REPORT_REL, "--escape-ratio", "2026-3"], r)
    clash = run([sys.executable, REPORT_REL, "--escape-ratio", "2026-03", "--check"], r)
    check("escape: a malformed month and a --check beside the mode each exit 2",
          bad.returncode == 2 and clash.returncode == 2 and "YYYY-MM" in bad.stderr and "--check" in clash.stderr,
          f"{bad.returncode} {clash.returncode}")


# ---------------------------------------------------------------------------------------------
# TOOL-dUnstuckLanding-15 — ABORTED run records whose work landed anyway
# ---------------------------------------------------------------------------------------------

_AWL_SIG = "aborted_work_landed"
_DWL_SIG = "discarded_work_landed"
_AWL_CUTOFF = "2026-02-01"
# What each fixture record must read, with a dated cutoff and the base ref `main`: the four AC3 shapes,
# an archive and a floored live record that are both negative, and one post-cutoff positive. The
# implementation review's round 1 added three: a run whose --no-ff landing merge `git revert -m 1`
# backed out (M4), a run never merged (M11, the one shape only clause (ii) decides), and a run based
# off the base ref's graph, which the engine places as the library does (L4).
_AWL_WANT = {"tEqBase": "not-landed (i)", "tForeign": "not-landed (i)", "tReverted": "not-landed (iii)",
             "tPos": "landed", "tArch": "not-landed (i)", "tFloor": "not-landed (i)", "tLate": "landed",
             "tMergeRev": "not-landed (iii)", "tUnmerged": "not-landed (ii)", "tOffRef": "not-landed (ii)"}


def _run_dated(r: pathlib.Path, day: str, *cmd: str) -> subprocess.CompletedProcess:
    """One git command whose commit, where it makes one, is dated `day` as author AND committer: the
    dating rule reads `%cs`, the committer's day, so a fixture that set the author alone dates nothing."""
    stamp = f"{day}T12:00:00+0000"
    return run(["git", *cmd], r, env={"GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp})


def _build_aborted_fixture(tmp: pathlib.Path, name: str):
    """A fixture repo holding one ABORTED record per shape the content predicate decides.

    Every commit is dated, so each record's first commit falls where the arm needs it against
    `_AWL_CUTOFF`. `unreverted` is a ref at the tip before tReverted's revert and tMergeRev's merge
    revert, which is how AC4 reads the same records with both removed. Returns `(repo, shas)`, the shas
    keyed by role.
    """
    NL = chr(10)
    B = f"{FIXTURE_MEMORY_ROOT}/builds"
    r = make_repo(tmp, name=name)
    shas: dict = {}

    def run_commit(day: str, msg: str) -> str:
        _run_dated(r, day, "add", "-A")
        out = _run_dated(r, day, "commit", "-q", "-m", msg, "--no-verify")
        assert out.returncode == 0, f"fixture commit {msg!r} failed: {out.stderr.strip()[:200]}"
        return run(["git", "rev-parse", "HEAD"], r).stdout.strip()

    def add_merged_work(day: str, slug: str, path: str, msg: str) -> tuple:
        """`(base, witness)`: a run branch cut from main, one commit on it, merged --no-ff."""
        base = run(["git", "rev-parse", "main"], r).stdout.strip()
        run(["git", "checkout", "-q", "-b", "w" + slug], r)
        (r / path).parent.mkdir(parents=True, exist_ok=True)
        (r / path).write_text(slug + NL, encoding="utf-8", newline=NL)
        witness = run_commit(day, msg)
        run(["git", "checkout", "-q", "main"], r)
        out = _run_dated(r, day, "merge", "-q", "--no-ff", "-m", f"merge the {slug} run", "w" + slug)
        assert out.returncode == 0, f"fixture merge of {slug} failed: {out.stderr.strip()[:200]}"
        return base, witness

    (r / ".unattended.conf").write_text(f'HANDOFF_CUTOFF="{_AWL_CUTOFF}"' + NL, encoding="utf-8", newline=NL)
    shas["root"] = run_commit("2026-01-02", "chore: adopt the unattended kit")
    (r / "src" / "other.txt").write_text("other" + NL, encoding="utf-8", newline=NL)
    shas["foreign"] = run_commit("2026-01-03", "chore: unrelated work")
    shas["pos"] = add_merged_work("2026-01-04", "tPos", "src/pos.txt", "feat(tPos): the work")
    shas["rev"] = add_merged_work("2026-01-05", "tReverted", "src/rev.txt", "feat(tReverted): the work")
    # Attributable by PATH alone: its subject does not name the slug.
    shas["late"] = add_merged_work("2026-01-06", "tLate", f"{B}/tLate/notes.md", "feat: the late work")
    shas["mrev"] = add_merged_work("2026-01-07", "tMergeRev", "src/mrev.txt", "feat(tMergeRev): the work")
    shas["mrev_merge"] = run(["git", "rev-parse", "main"], r).stdout.strip()
    # Never merged: its run branch keeps the one commit, and main never takes it.
    shas["gone_base"] = shas["mrev_merge"]
    run(["git", "checkout", "-q", "-b", "wtUnmerged"], r)
    (r / "src" / "gone.txt").write_text("gone" + NL, encoding="utf-8", newline=NL)
    shas["gone"] = run_commit("2026-01-07", "feat(tUnmerged): the work")
    # Based OFF main's graph: a side line from the root that main never takes, and the run cut from it.
    run(["git", "checkout", "-q", "-b", "wside", shas["root"]], r)
    (r / "src" / "side.txt").write_text("side" + NL, encoding="utf-8", newline=NL)
    shas["side"] = run_commit("2026-01-07", "chore: side work")
    (r / "src" / "off.txt").write_text("off" + NL, encoding="utf-8", newline=NL)
    shas["off"] = run_commit("2026-01-07", "feat(tOffRef): the work")
    run(["git", "checkout", "-q", "main"], r)
    run(["git", "branch", "unreverted", "main"], r)
    out = _run_dated(r, "2026-01-08", "revert", "--no-edit", shas["rev"][1])
    assert out.returncode == 0, f"fixture revert failed: {out.stderr.strip()[:200]}"
    out = _run_dated(r, "2026-01-08", "revert", "-m", "1", "--no-edit", shas["mrev_merge"])
    assert out.returncode == 0, f"fixture merge revert failed: {out.stderr.strip()[:200]}"

    root = shas["root"]

    def write_aborted(slug: str, base: str, witness: str, rows=()) -> str:
        facts = {"phase": "ABORTED", "witness": witness, "base": base, "halt-code": "fork-unresolvable"}
        return _write_run_record(r, f"{B}/{slug}/RUN.md", facts, rows)

    write_aborted("tEqBase", root, root)
    write_aborted("tForeign", root, shas["foreign"])
    write_aborted("tReverted", *shas["rev"])
    write_aborted("tPos", *shas["pos"])
    write_aborted("tMergeRev", *shas["mrev"])
    write_aborted("tUnmerged", shas["gone_base"], shas["gone"])
    write_aborted("tOffRef", shas["side"], shas["off"])
    write_aborted("tArch", root, root)
    _write_run_record(r, f"{B}/tFloor/RUN.md", {"phase": "LANDED", "witness": root, "base": root})
    run_commit("2026-01-10", "records: the legacy run records")
    # tArch rotates to an archive name and must still date to its first add; tFloor's earlier run
    # rotates out and a new run takes RUN.md, whose tenancy begins at the rotation.
    run(["git", "mv", f"{B}/tArch/RUN.md", f"{B}/tArch/RUN.ABORTED.0123abcd.md"], r)
    run(["git", "mv", f"{B}/tFloor/RUN.md", f"{B}/tFloor/RUN.LANDED.abcd1234.md"], r)
    write_aborted("tFloor", root, root)
    run_commit("2026-01-20", "records: rotate two run records")
    # Rows of its own, so it shares under half its lines with any older record. `--follow` follows
    # COPIES from unmodified files, so a record this small and this alike would date to a sibling's
    # add - the library's stated limit, which errs toward grandfathering, and both readers share it.
    write_aborted("tLate", *shas["late"], rows=[_build_park_row("review", f"late row {i}") for i in range(20)])
    run_commit("2026-03-01", "records: the post-cutoff run record")
    return r, shas


def _read_aborted_rows(dr, r: pathlib.Path, base_ref: str = "main") -> tuple:
    """`(aborted signal, discarded signal, {slug: verdict field})` over one fresh context."""
    ctx = _build_run_ctx(dr, r, base_ref)
    awl, dwl = dr.build_aborted_work_landed(ctx), dr.build_discarded_work_landed(ctx)
    rows = {}
    for d in awl["detail"] + dwl["detail"]:
        if not isinstance(d, str) or d.startswith(("note", "DEAD")):
            continue                          # a NOT ASKED detail is a dict, a note or DEAD a string
        bits = d.split(" ", 5)
        rows[bits[0].split("/")[2]] = bits[5] if len(bits) > 5 else ""
    return awl, dwl, rows


def test_aborted_work_landed(tmp: pathlib.Path) -> None:
    """TOOL-dUnstuckLanding-15 AC2 to AC7 and AC9: each negative shape, the revert removed, the facts
    that do and do not clear a record, an archive, a post-cutoff record, a blank cutoff, misread
    controls, both empty states, and the call count. Ancestry is git's own answer throughout: every
    witness and base is a real commit in a fixture repo."""
    print("ABORTED run records whose work landed anyway")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    NL = chr(10)
    B = f"{FIXTURE_MEMORY_ROOT}/builds"
    r, shas = _build_aborted_fixture(tmp, "abortedwork")
    tip = run(["git", "rev-parse", "main"], r).stdout.strip()

    def run_commit(day: str, msg: str) -> None:
        _run_dated(r, day, "add", "-A")
        _run_dated(r, day, "commit", "-q", "-m", msg, "--no-verify")

    def write_record(slug: str, base: str, witness: str, wla: str = "") -> None:
        facts = {"phase": "ABORTED", "witness": witness, "base": base, "halt-code": "fork-unresolvable"}
        if wla:
            facts["work-landed-at"] = wla
        _write_run_record(r, f"{B}/{slug}/RUN.md", facts)

    # ---- AC3 and AC5, the shapes as built. Each verdict field is asserted whole, so a record read as
    # the wrong clause is caught as surely as one read the wrong way.
    awl, dwl, rows = _read_aborted_rows(dr, r)
    for slug, want in sorted(_AWL_WANT.items()):
        check(f"aborted work: {slug} reads {want}", rows.get(slug) == want, f"got {rows.get(slug)!r}")
    check("aborted work: live over the legacy population, the archive included in `of`",
          awl["live"] is True and awl["of"] == 9, f"live={awl['live']} of={awl['of']} {awl['detail']}")
    check("aborted work: only the legacy positive is counted", awl["value"] == 1, f"{awl['detail']}")
    check("aborted work: the post-cutoff positive counts in discarded and not in aborted",
          dwl["live"] is True and dwl["value"] == 1 and dwl["of"] == 1
          and not any("/tLate/" in d for d in awl["detail"]), f"{dwl} {awl['detail']}")
    row = next((d for d in awl["detail"] if "/tFloor/RUN.md " in d), "")
    check("aborted work: a row is <record> <halt-code> <witness8> <date> <class> <verdict>",
          row == f"{B}/tFloor/RUN.md fork-unresolvable {shas['root'][:8]} 2026-01-20 legacy not-landed (i)",
          f"got {row!r}")

    # ---- AC4, the same records with the revert removed: the revert clause is what decided tReverted.
    awl4, _d, rows4 = _read_aborted_rows(dr, r, "unreverted")
    check("aborted work: with its revert removed, the merged-then-reverted record is listed",
          rows4.get("tReverted") == "landed" and awl4["value"] == 3,
          f"got {rows4.get('tReverted')!r} value {awl4['value']}")
    check("aborted work: with its merge's revert removed, the merge-reverted record is listed (M4)",
          rows4.get("tMergeRev") == "landed", f"got {rows4.get('tMergeRev')!r}")

    # ---- AC2, through the CLI: both registered, both non-zero, and `--check` still exits 0.
    rep = report(r)
    check("aborted work: the report registers both signals, both non-zero and report-only",
          all(rep.get(n, {}).get("value", 0) > 0 and rep.get(n, {}).get("gateable") is False
              for n in (_AWL_SIG, _DWL_SIG)), f"{[rep.get(n) for n in (_AWL_SIG, _DWL_SIG)]}")
    chk = run([sys.executable, REPORT_REL, "--check"], r)
    check("aborted work: --check exits 0 with both signals over their pins",
          chk.returncode == 0, f"rc={chk.returncode} stderr={chk.stderr.strip()[:200]}")

    # ---- AC5, a blank cutoff: the post-cutoff record turns LEGACY and is counted, with the note, and
    # the discarded signal is NOT ASKED rather than a clean zero. Restored after.
    (r / ".unattended.conf").write_text('HANDOFF_CUTOFF=""' + NL, encoding="utf-8", newline=NL)
    run_commit("2026-03-02", "chore: blank the cutoff")
    awl5, dwl5, rows5 = _read_aborted_rows(dr, r)
    check("aborted work: a blank cutoff reads the post-cutoff record LEGACY and counts it",
          rows5.get("tLate") == "landed" and awl5["value"] == 2, f"{awl5['detail']}")
    check("aborted work: a blank cutoff carries the note naming the blank key",
          any(d.startswith("note") and "HANDOFF_CUTOFF is blank" in d for d in awl5["detail"]),
          f"{awl5['detail']}")
    check("aborted work: a blank cutoff reads discarded NOT ASKED, never a clean zero",
          dwl5.get("not_asked") is True and "HANDOFF_CUTOFF is blank" in str(dwl5["detail"]), f"{dwl5}")
    (r / ".unattended.conf").write_text(f'HANDOFF_CUTOFF="{_AWL_CUTOFF}"' + NL, encoding="utf-8", newline=NL)
    run_commit("2026-03-03", "chore: date the cutoff again")

    # ---- AC3 and AC5, the facts. An upheld fact clears a legacy record and never a post-cutoff one.
    write_record("tPos", *shas["pos"], wla=f"{shas['pos'][1]} {tip}")
    write_record("tLate", *shas["late"], wla=f"{shas['late'][1]} {tip}")
    run_commit("2026-03-04", "records: settle tPos and tLate")
    awl, dwl, rows = _read_aborted_rows(dr, r)
    check("aborted work: an upheld work-landed-at moves the legacy positive to settled",
          rows.get("tPos") == "settled" and awl["value"] == 0, f"{awl['detail']}")
    check("aborted work: an upheld work-landed-at does not clear a post-cutoff record",
          rows.get("tLate") == "landed" and dwl["value"] == 1, f"{dwl['detail']}")
    # A fact naming another witness is not this record's, so it clears nothing.
    write_record("tPos", *shas["pos"], wla=f"{shas['foreign']} {tip}")
    write_record("tForeign", shas["root"], shas["foreign"], wla=f"{shas['foreign']} {tip}")
    run_commit("2026-03-05", "records: two facts that prove nothing")
    awl, _d, rows = _read_aborted_rows(dr, r)
    check("aborted work: a work-landed-at naming another witness leaves the record counted",
          rows.get("tPos") == "landed" and awl["value"] == 1, f"{awl['detail']}")
    check("aborted work: the fact on a negative record reads fact-not-upheld and is not counted",
          rows.get("tForeign") == "fact-not-upheld", f"got {rows.get('tForeign')!r}")
    # An archive no verb can edit is listed with its verdict and counted nowhere.
    run(["git", "mv", f"{B}/tPos/RUN.md", f"{B}/tPos/RUN.ABORTED.0123abcd.md"], r)
    run_commit("2026-03-06", "records: rotate tPos")
    awl, _d, rows = _read_aborted_rows(dr, r)
    check("aborted work: the positive rotated to an archive reads landed (archived), uncounted",
          rows.get("tPos") == "landed (archived)" and awl["value"] == 0, f"{awl['detail']}")

    # ---- AC6, controls that cannot say no, and a positive control that cannot say yes.
    saved = dr._WORK_LANDED_CONTROLS
    try:
        landed = dict(saved[3][1])
        dr._WORK_LANDED_CONTROLS = tuple((label, dict(landed)) for label, _f in saved)
        awl6, dwl6, _r = _read_aborted_rows(dr, r)
        check("aborted work: controls that all describe landed work read both signals DEAD, naming "
              "the first", all(s["live"] is False and not s.get("not_asked")
                               and s["detail"][0].startswith("DEAD PROBE")
                               and saved[0][0] in s["detail"][0] for s in (awl6, dwl6)), f"{awl6} {dwl6}")
        reverted = dict(saved[3][1], reverted=saved[3][1]["on_base_ref"])
        dr._WORK_LANDED_CONTROLS = saved[:3] + ((saved[3][0], reverted),) + saved[4:]
        awl6, dwl6, _r = _read_aborted_rows(dr, r)
        check("aborted work: a positive control pointed at reverted work reads both DEAD, naming it",
              all(s["live"] is False and saved[3][0] in s["detail"][0] for s in (awl6, dwl6)),
              f"{awl6} {dwl6}")
    finally:
        dr._WORK_LANDED_CONTROLS = saved
    awl, _d, _r = _read_aborted_rows(dr, r)
    check("aborted work: the shipped controls restored read live again", awl["live"] is True, f"{awl}")

    # ---- AC7, the two empty states. Neither prints a clean zero.
    e = make_repo(tmp, name="abortedempty")
    for sig in (dr.build_aborted_work_landed(_build_run_ctx(dr, e)),
                dr.build_discarded_work_landed(_build_run_ctx(dr, e))):
        check(f"aborted work: {sig['signal']} with no record and no conf reads NOT ASKED",
              sig.get("not_asked") is True and sig["live"] is False, f"{sig}")
    (e / ".unattended.conf").write_text(f'HANDOFF_CUTOFF="{_AWL_CUTOFF}"' + NL, encoding="utf-8", newline=NL)
    _write_run_record(e, f"{B}/tDone/RUN.md", {"phase": "LANDED", "witness": "0" * 40, "base": "0" * 40})
    run(["git", "add", "-A"], e)
    run(["git", "commit", "-q", "-m", "chore: the kit with no ABORTED record", "--no-verify"], e)
    for sig in (dr.build_aborted_work_landed(_build_run_ctx(dr, e)),
                dr.build_discarded_work_landed(_build_run_ctx(dr, e))):
        check(f"aborted work: {sig['signal']} with the conf and no ABORTED record reads DEAD, naming "
              "the empty population", sig["live"] is False and not sig.get("not_asked")
              and "reads phase ABORTED" in str(sig["detail"]), f"{sig}")

    # ---- AC9, the call count: four shared calls and two per record, whatever the history's length.
    small = tmp / "abortedcalls"
    small.mkdir()
    run(["git", "init", "-q", "-b", "main"], small)
    run(["git", "config", "user.email", "selftest@example.com"], small)
    run(["git", "config", "user.name", "selftest"], small)
    (small / "seed.txt").write_text("seed" + NL, encoding="utf-8", newline=NL)
    run(["git", "add", "-A"], small)
    run(["git", "commit", "-q", "-m", "seed", "--no-verify"], small)
    per_record = 2
    seen = {}
    for lo, hi in ((0, 3), (3, 6)):
        for i in range(lo, hi):
            (small / f"work{i}.txt").write_text(f"{i}" + NL, encoding="utf-8", newline=NL)
            run(["git", "add", "-A"], small)
            run(["git", "commit", "-q", "-m", f"feat(tCall{i}): the work", "--no-verify"], small)
            wit = run(["git", "rev-parse", "HEAD"], small).stdout.strip()
            bas = run(["git", "rev-parse", "HEAD~1"], small).stdout.strip()
            _write_run_record(small, f"{B}/tCall{i}/RUN.md", {"phase": "ABORTED", "witness": wit, "base": bas})
        run(["git", "add", "-A"], small)
        run(["git", "commit", "-q", "-m", f"{hi} records", "--no-verify"], small)
        landed = dr.build_aborted_work_landed(_build_run_ctx(dr, small))
        check(f"aborted work: {hi} records are all read and counted (the premise)",
              landed["value"] == hi and landed["of"] == hi, f"{landed}")
        seen[hi] = _measure_git_calls(dr, small, dr.read_aborted_verdicts)
    check("aborted work: three more records cost three times the per-record constant",
          seen[6] - seen[3] == 3 * per_record, f"{seen}")
    check("aborted work: the shared calls are four", seen[3] - 3 * per_record == 4, f"{seen}")
    for i in range(50):
        (small / "noise.txt").write_text(f"{i}" + NL, encoding="utf-8", newline=NL)
        run(["git", "add", "-A"], small)
        run(["git", "commit", "-q", "-m", f"chore: noise {i}", "--no-verify"], small)
    check("aborted work: fifty unrelated commits on the base ref move no count",
          _measure_git_calls(dr, small, dr.read_aborted_verdicts) == seen[6], f"{seen}")


def resolve_bash_shell(probe_dir: pathlib.Path) -> str | None:
    """A shell that runs the kit library as bash runs it: `[[ ]]` and process substitution, both of
    which the library uses. `sh` on MSYS is bash in POSIX mode, so the probe leaves that mode first."""
    marker = probe_dir / ".bashprobe"
    marker.write_text("PROBE=works\n", encoding="utf-8", newline="\n")
    probe = ('set +o posix 2>/dev/null; . ./.bashprobe; y=$(cat < <(printf %s "$PROBE")); '
             '[[ "$y" == works ]] && printf %s "$y"')
    try:
        for cand in ("bash", "sh", "/usr/bin/bash", "/bin/bash"):
            try:
                out = subprocess.run([cand, "-c", probe], cwd=str(probe_dir), capture_output=True,
                                     text=True, encoding="utf-8", errors="replace")
            except (OSError, FileNotFoundError):
                continue
            if out.returncode == 0 and out.stdout.strip() == "works":
                return cand
        return None
    finally:
        marker.unlink(missing_ok=True)


def test_work_landed_matches_the_driver(tmp: pathlib.Path) -> None:
    """TOOL-dUnstuckLanding-15 AC8: the engine's content predicate and first-commit dating, held to the
    unattended kit library's own `check_work_landed` and `read_first_commit_date` over the same fixture
    records, the base ref standing for the tip. Both directions: a record either reads differently in
    is a red here, whichever side moved. The library is reached by a path derived from this kit's own
    directory, as the driver-set arm above reaches the driver."""
    print("content predicate and dating vs the unattended kit library")
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    try:
        lib = resolve_kit_dir("unattended", "lib-unattended.sh", KIT) / "lib-unattended.sh"
    except LookupError:
        lib = None
    if lib is None or not lib.exists():
        skip("work-landed parity with the driver", "no unattended kit library beside this kit")
        return
    shell = resolve_bash_shell(tmp)
    if shell is None:
        skip("work-landed parity with the driver", "no bash that runs the kit library here")
        return
    r, shas = _build_aborted_fixture(tmp, "abortedparity")
    tip = run(["git", "rev-parse", "main"], r).stdout.strip()
    got = dr.read_aborted_verdicts(_build_run_ctx(dr, r))
    mine = {row["path"]: ({"landed": "0", "not-landed": "1"}.get(row["verdict"], "2"), row["date"])
            for row in got["rows"]}
    check("parity: the engine read every fixture record", len(mine) == len(_AWL_WANT), f"{sorted(mine)}")
    script = ('set +o posix 2>/dev/null; . "$1" || exit 9; t=$2; shift 2; for p in "$@"; do '
              'check_work_landed "$p" "$t"; rc=$?; d=$(read_first_commit_date "$p"); '
              'printf "%s|%s|%s\\n" "$p" "$rc" "$d"; done')
    out = run([shell, "-c", script, "parity", lib.as_posix(), tip, *sorted(mine)], r)
    theirs = {}
    for line in out.stdout.split("\n"):
        bits = line.strip().split("|")
        if len(bits) == 3:
            theirs[bits[0]] = (bits[1], bits[2])
    check("parity: the library answered for every record", set(theirs) == set(mine),
          f"rc={out.returncode} stderr={out.stderr.strip()[:200]} got {sorted(theirs)}")
    check("parity: the fixture holds a landed and a not-landed record (the premise)",
          {"0", "1"} <= {v[0] for v in mine.values()}, f"{mine}")
    for path in sorted(mine):
        check(f"parity: {path.split('/')[2]} {path.rpartition('/')[2]} reads the same verdict and date "
              "in both", mine[path] == theirs.get(path), f"engine {mine[path]} library {theirs.get(path)}")
    arch = next((p for p in mine if "/tArch/" in p), "")
    floor = next((p for p in mine if "/tFloor/RUN.md" in p), "")
    check("parity: a rotated archive is dated by its first add, not by the rotation",
          mine.get(arch, ("", ""))[1] == "2026-01-10" == theirs.get(arch, ("", ""))[1], f"{arch}")
    check("parity: a live RUN.md is floored at its archived sibling",
          mine.get(floor, ("", ""))[1] == "2026-01-20" == theirs.get(floor, ("", ""))[1], f"{floor}")
    # No hand-flipped "control" here (implementation review round 1, L3): a flipped copy of the
    # engine's own verdict differs from the library's exactly when the per-record checks above have
    # already redded, so it could not fail on its own. The premise check above, a landed and a
    # not-landed record both present, is what shows the comparison is not over a constant.

    # ---- L6: ONE fixture fed to both graders of `work-landed-at`. tPos's fact names its witness and the
    # tip; tLate's names another run's commit. The engine's `upheld` reading and the library's
    # `check_work_landed_fact`, which the leg's check 15 calls, must agree on each.
    B = f"{FIXTURE_MEMORY_ROOT}/builds"
    facts = {"phase": "ABORTED", "halt-code": "fork-unresolvable"}
    _write_run_record(r, f"{B}/tPos/RUN.md", dict(facts, witness=shas["pos"][1], base=shas["pos"][0],
                                                  **{"work-landed-at": f"{shas['pos'][1]} {tip}"}))
    _write_run_record(r, f"{B}/tLate/RUN.md", dict(facts, witness=shas["late"][1], base=shas["late"][0],
                                                   **{"work-landed-at": f"{shas['foreign']} {tip}"}),
                      [_build_park_row("review", f"late row {i}") for i in range(20)])
    _run_dated(r, "2026-03-10", "add", "-A")
    _run_dated(r, "2026-03-10", "commit", "-q", "-m", "records: two facts, one upheld", "--no-verify")
    tip = run(["git", "rev-parse", "main"], r).stdout.strip()
    got = dr.read_aborted_verdicts(_build_run_ctx(dr, r))
    held = {row["path"]: row["upheld"] for row in got["rows"] if row.get("wla")}
    script = ('set +o posix 2>/dev/null; . "$1" || exit 9; t=$2; shift 2; for p in "$@"; do '
              'check_work_landed_fact "$p" "$t"; printf "%s|%s\\n" "$p" "$?"; done')
    out = run([shell, "-c", script, "parity", lib.as_posix(), tip, *sorted(held)], r)
    graded = {}
    for line in out.stdout.split("\n"):
        bits = line.strip().split("|")
        if len(bits) == 2:
            graded[bits[0]] = bits[1] == "0"
    check("parity: both graders read the same work-landed-at facts (L6)",
          len(held) == 2 and set(graded) == set(held),
          f"engine {sorted(held)} library {sorted(graded)} stderr={out.stderr.strip()[:200]}")
    check("parity: the facts hold one upheld and one not (the premise)",
          set(held.values()) == {True, False}, f"{held}")
    for path in sorted(held):
        check(f"parity: {path.split('/')[2]} work-landed-at reads the same upheld verdict in both",
              held[path] == graded.get(path), f"engine {held[path]} library {graded.get(path)}")

    # ---- Implementation review round 2, L5: the tip-on-base-ref clause, armed. Both facts above name a
    # tip on main, so the engine's `resolved.get(wla-tip) in parents` conjunct could be deleted with
    # every check green. tPos's fact is rewritten to name the side branch's tip, which main does not
    # carry, and both graders must refuse it: the engine's `upheld` False, the library's rc 1.
    pos = f"{B}/tPos/RUN.md"
    _write_run_record(r, pos, dict(facts, witness=shas["pos"][1], base=shas["pos"][0],
                                   **{"work-landed-at": f"{shas['pos'][1]} {shas['side']}"}))
    _run_dated(r, "2026-03-11", "add", "-A")
    _run_dated(r, "2026-03-11", "commit", "-q", "-m", "records: tPos names an off-ref tip", "--no-verify")
    tip = run(["git", "rev-parse", "main"], r).stdout.strip()
    got = dr.read_aborted_verdicts(_build_run_ctx(dr, r))
    off = [row["upheld"] for row in got["rows"] if row.get("wla") and row["path"] == pos]
    check("parity: the engine does not uphold a fact whose tip is off the base ref (L5)",
          off == [False], f"{off}")
    out = run([shell, "-c", script, "parity", lib.as_posix(), tip, pos], r)
    check("parity: the library does not uphold a fact whose tip is off the base ref (L5)",
          out.stdout.strip() == f"{pos}|1", f"{out.stdout.strip()} stderr={out.stderr.strip()[:200]}")


def test_version_carriers_agree(tmp: pathlib.Path) -> None:
    """TOOL-dLoggedFlight-13 S6: every carrier of this kit's version agrees with the engine's constant.

    The population is DERIVED: every file in this kit's directory that carries the marker, plus the
    out-of-kit carriers its descriptor declares. A carrier that forgets the marker entirely drops out
    of the first half, which is why the descriptor's declared list is required to resolve too.
    """
    print("drift-audit version carriers agree with the engine")
    import tomllib
    sys.path.insert(0, str(KIT))
    import drift_report as dr

    want = dr.KIT_DRIFT_AUDIT_VERSION
    marker = re.compile(r"gov:kit drift-audit@([0-9][0-9.]*[0-9])")
    in_kit = sorted(p for p in KIT.iterdir()
                    if p.is_file() and marker.search(p.read_text(encoding="utf-8", errors="replace")))
    desc = tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8"))
    declared = [KIT.parent / c.split("/", 1)[1] for c in desc.get("marker_carriers", [])
                if c.startswith("{prefix}/")]
    check("versions: the kit dir holds carriers beyond the engine", len(in_kit) > 1,
          f"found {[p.name for p in in_kit]}")
    check("versions: the descriptor declares its out-of-kit carriers", bool(declared),
          "marker_carriers is empty or no longer spelled with {prefix}")
    for p in in_kit + declared:
        text = p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""
        found = marker.findall(text)
        check(f"versions: {p.name} carries the marker at {want}", bool(found) and set(found) == {want},
              f"found {found}")

def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        test_conf_parser_matches_bash(tmp)
        # FOREIGN_PREFIX_PROBE (TOOL-aRepatriatedFork-52 S1): the arm above ran the subject, and a probe stops here.
        if os.environ.get("FOREIGN_PREFIX_PROBE") == "1":
            print("foreign-prefix-probe: stopped after 1 arm")
            print("FAIL (1 assertions)" if (FAILS) else "PASS (1 assertions)")
            return 1 if (FAILS) else 0
        test_harness_liveness_note_is_derived(tmp)
        test_signals_can_move(tmp)
        test_lexicon_signals(tmp)
        test_lexicon_marginal_rate(tmp)
        test_no_signal_hardcodes_live(tmp)
        test_live_backlog_rows(tmp)
        test_backlog_ask_signals(tmp)
        test_asks_disposed_overrides(tmp)
        test_legs_retried_after_timeout(tmp)
        test_fleet_over_budget(tmp)
        test_remote_ci_red_streak(tmp)
        test_auto_memory_pointers(tmp)
        test_cutoff_keys_armed(tmp)
        test_stale_dossiers(tmp)
        test_live_builds_without_activity(tmp)
        test_backlog_stragglers(tmp)
        test_readme_mechanism_drift(tmp)
        test_declared_empty(tmp)
        test_handkept_name_sets(tmp)
        test_ratchet_guard(tmp)
        test_baselines(tmp)
        test_shrink_low_water(tmp)
        test_base_is_remote_tracking(tmp)
        test_ratchet_lookback(tmp)
        test_ratchet_message_states_its_window(tmp)
        test_lang_mode_ratchet(tmp)
        test_evidence_oracle(tmp)
        test_local_grammar_matches_the_extractor(tmp)
        test_source_cited_ids(tmp)
        test_report_only_signal_is_judged_against_its_pin(tmp)
        test_evidence_globs_exclude_test_templates(tmp)
        test_nonterminal_merged_runs(tmp)
        test_park_sets_match_the_driver(tmp)
        test_drift_history(tmp)
        test_drift_delta(tmp)
        test_dead_streaks(tmp)
        test_escape_ratio(tmp)
        test_aborted_work_landed(tmp)
        test_work_landed_matches_the_driver(tmp)
        test_version_carriers_agree(tmp)
    print()
    if SKIPS:
        print(f"drift-audit selftest: {len(SKIPS)} SKIPPED — {', '.join(SKIPS)}")
        print(f"drift-audit selftest: floor {CHECK_FLOOR} NOT compared — a skipped arm's checks are "
              f"absent for a reason the floor cannot see")
    elif len(EXECUTED) < CHECK_FLOOR:
        FAILS.append("check floor")
        print(f"drift-audit selftest: FAIL executed {len(EXECUTED)} checks, under the floor of "
              f"{CHECK_FLOOR} — an arm went missing")
    if FAILS:
        print(f"drift-audit selftest: {len(FAILS)} FAILED — {', '.join(FAILS)}")
        return 1
    print(f"drift-audit selftest: all checks passed ({len(EXECUTED)} executed, floor {CHECK_FLOOR})"
          + (f" ({len(SKIPS)} skipped, see above)" if SKIPS else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
