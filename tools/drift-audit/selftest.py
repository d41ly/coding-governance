#!/usr/bin/env python3
"""selftest.py — the drift-audit kit's own falsifiability test.

gov:kit drift-audit@1.0

    python drift-audit/selftest.py

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
import pathlib
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
FAILS: list[str] = []
SKIPS: list[str] = []


def check(label: str, cond: bool, detail: str = "") -> None:
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
    body = (
        '# a comment with an = sign\n'
        'MEMORY_ROOT=memory\n'
        'DISCIPLINES="one two three"\n'
        "QUOTED_SINGLE='x y'\n"
        '\n'
        'TRAILING=spaced   \n'
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
    for key in ("MEMORY_ROOT", "DISCIPLINES", "QUOTED_SINGLE", "TRAILING"):
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
    (r / "drift-audit").mkdir(parents=True)

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

    for f in ("drift_report.py", "drift_signals.template.py"):
        (r / "drift-audit" / f).write_bytes((KIT / f).read_bytes())
    (r / "drift-audit" / "drift_signals.py").write_text(
        "PRODUCT_GLOBS = ['src']\n"
        "SHRINK_ONLY = {'shrinkme.txt': 'a list that promises to shrink'}\n"
        "HANDKEPT = []\n"
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
    return r


def report(r: pathlib.Path, *extra: str) -> dict:
    import json

    out = run([sys.executable, "drift-audit/drift_report.py", "--json", *extra], r)
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

    # --- 3 — --check honours the pin in BOTH directions -------------------------------------
    print("--check pin semantics")
    sig = r / "drift-audit" / "drift_signals.py"
    over = run([sys.executable, "drift-audit/drift_report.py", "--check"], r)
    check("--check reds while a gateable signal is over its (default 0) pin", over.returncode == 1,
          f"rc={over.returncode}")
    sig.write_text(sig.read_text(encoding="utf-8").replace(
        "PINS = {}", "PINS = {'non_terminal_specs_cited_by_product_source': 1}"),
        encoding="utf-8", newline="\n")
    at = run([sys.executable, "drift-audit/drift_report.py", "--check"], r)
    check("--check greens once the pin is seeded at the measured value", at.returncode == 0,
          f"rc={at.returncode} stderr={at.stderr.strip()[:200]}")

    # --- a missing project layer is a REFUSAL, never a default ------------------------------
    sig.unlink()
    gone = run([sys.executable, "drift-audit/drift_report.py"], r)
    check("a missing project layer refuses with rc 2", gone.returncode == 2, f"rc={gone.returncode}")


# ---------------------------------------------------------------------------------------------
# 4 — DECLARED_EMPTY relabels a drained probe WITHOUT muzzling it (both directions)
# ---------------------------------------------------------------------------------------------


def test_declared_empty(tmp: pathlib.Path) -> None:
    """A declaration must stay LIFTABLE, or it is the DEAD PROBE defect wearing a nicer label.

    Direction one on its own — drain the population, declare it, watch `--check` go quiet — is
    indistinguishable from a probe that has simply gone blind, because that is exactly what a blind
    probe looks like too. Only direction two, putting one row back and watching the same signal score
    again, separates "empty on purpose" from "cannot see". Both directions run over ONE fixture, so
    the ledger row and the declaration are the only variables between them.
    """
    print("DECLARED_EMPTY (a drained probe reports declared, and still LIFTS)")
    r = make_repo(tmp, name="declared")
    sig = r / "drift-audit" / "drift_signals.py"
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
    quiet = run([sys.executable, "drift-audit/drift_report.py", "--check"], r)
    check("drained + declared: --check stays green", quiet.returncode == 0,
          f"rc={quiet.returncode} stderr={quiet.stderr.strip()[:200]}")

    # THE DISCRIMINATING ASSERTION of direction one. The three above hold just as well for a signal
    # `--check` is merely ignoring; only the PRINTED status tells a reader "empty on purpose" from
    # "blind", and that line is the one a human acts on.
    human = run([sys.executable, "drift-audit/drift_report.py"], r)
    row = next((ln for ln in human.stdout.splitlines()
                if "ledger_rows_contradicting_git" in ln), "")
    check("drained + declared: the printed row reads 'empty by declaration'",
          "empty by declaration" in row, f"row={row.strip()!r}")
    check("drained + declared: and NOT 'DEAD PROBE'",
          bool(row) and "DEAD PROBE" not in row, f"row={row.strip()!r}")

    # --- direction two: one row returns, the declaration is dropped, the probe must SCORE ------
    sha = run(["git", "rev-parse", "--short", "HEAD"], r).stdout.strip()
    assert len(sha) >= 7, f"fixture HEAD sha not produced: {sha!r}"
    ledger_dir.mkdir(parents=True)
    # The row shape `make_repo` already writes. `BASESHA` is deliberately NOT hex, so `_SHA` finds
    # exactly one sha in the line and the arm isolates the oracle rather than the row's wording.
    (ledger_dir / "a.md").write_text(
        "| slug | branch | status |\n|---|---|---|\n"
        f"| `aThing` | `feature/x` off `BASESHA` | in-flight — NOT merged, work at `{sha}` |\n",
        encoding="utf-8", newline="\n")
    sig.write_text(sig.read_text(encoding="utf-8").replace(
        ", 'ledger_rows_contradicting_git'", ""), encoding="utf-8", newline="\n")
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "a ledger row returns", "--no-verify"], r)

    back = report(r)["ledger_rows_contradicting_git"]
    check("a row returns: the probe is LIVE again — the declaration was not a muzzle",
          back["live"] is True, f"live={back['live']}")
    check("a row returns: and it scores the contradiction", back["value"] == 1,
          f"got {back['value']}")
    fires = run([sys.executable, "drift-audit/drift_report.py", "--check"], r)
    check("a row returns: --check reds again", fires.returncode == 1, f"rc={fires.returncode}")
    check("a row returns: ...and names the signal on stderr",
          "ledger_rows_contradicting_git" in fires.stderr,
          f"stderr={fires.stderr.strip()[:200]}")


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        test_conf_parser_matches_bash(tmp)
        test_signals_can_move(tmp)
        test_declared_empty(tmp)
    print()
    if SKIPS:
        print(f"drift-audit selftest: {len(SKIPS)} SKIPPED — {', '.join(SKIPS)}")
    if FAILS:
        print(f"drift-audit selftest: {len(FAILS)} FAILED — {', '.join(FAILS)}")
        return 1
    print(f"drift-audit selftest: all checks passed"
          + (f" ({len(SKIPS)} skipped, see above)" if SKIPS else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
