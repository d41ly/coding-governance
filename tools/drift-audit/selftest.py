#!/usr/bin/env python3
"""selftest.py — the drift-audit kit's own falsifiability test.

gov:kit drift-audit@1.4

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
import shutil
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
    (r / "conf").mkdir(parents=True)
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
        (r / "drift-audit" / f).write_bytes((KIT / f).read_bytes())
    (r / "drift-audit" / "drift_signals.py").write_text(
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
    quiet6 = run([sys.executable, "drift-audit/drift_report.py", "--check"], r)
    check("unset cutoff: --check stays green rather than reding a dead gateable probe",
          quiet6.returncode == 0, f"rc={quiet6.returncode} stderr={quiet6.stderr.strip()[:200]}")
    sig.write_text(keep, encoding="utf-8", newline="\n")

    # --- a missing project layer is a REFUSAL, never a default ------------------------------
    sig.unlink()
    gone = run([sys.executable, "drift-audit/drift_report.py"], r)
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
    # present exactly where an installed kit puts it.
    kit_src = pathlib.Path(__file__).resolve().parent.parent / "lexicon"
    shutil.copytree(kit_src, r / "tools" / "lexicon",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    src = r / "src" / "thing.py"
    src.write_text("def build_thing():\n    pass\n", encoding="utf-8", newline="\n")
    conf = r / ".lexicon.conf"
    conf.write_text(
        'BANNED_SUFFIXES="Manager"\nLANGS="py:python-ast:parser"\n'
        'VERB_OFFENDER_PIN="99"\nSUFFIX_OFFENDER_PIN="0"\nLAYER_OFFENDER_PIN="0"\n'
        'ratified="2999-01-01 node t"\n\nVERBS:\n  build  make a thing\n\nLAYERS:\n  src/* -> vendor/*\n',
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


# ---------------------------------------------------------------------------------------------
# 4 — DECLARED_EMPTY relabels a drained probe WITHOUT muzzling it (three directions)
# ---------------------------------------------------------------------------------------------


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
    muzzle = run([sys.executable, "drift-audit/drift_report.py", "--check"], r)
    check("still declared, a row returns: --check REDS — the declaration was not a muzzle",
          muzzle.returncode == 1, f"rc={muzzle.returncode} stderr={muzzle.stderr.strip()[:200]}")
    check("still declared, a row returns: ...and names the signal on stderr",
          "ledger_rows_contradicting_git" in muzzle.stderr,
          f"stderr={muzzle.stderr.strip()[:200]}")
    # ...and the human-facing print must stop excusing it too. The status ladder reads the same
    # declaration set, so a muzzle can hide there just as easily as in the gate.
    printed = run([sys.executable, "drift-audit/drift_report.py"], r)
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
    fires = run([sys.executable, "drift-audit/drift_report.py", "--check"], r)
    check("declaration lifted: --check reds identically", fires.returncode == 1,
          f"rc={fires.returncode}")
    check("declaration lifted: ...and names the signal on stderr",
          "ledger_rows_contradicting_git" in fires.stderr,
          f"stderr={fires.stderr.strip()[:200]}")


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
    sig = r / "drift-audit" / "drift_signals.py"

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
        return run([sys.executable, str(r / "drift-audit" / "drift_report.py"), "--check"], r)

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


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        test_conf_parser_matches_bash(tmp)
        test_signals_can_move(tmp)
        test_lexicon_signals(tmp)
        test_no_signal_hardcodes_live(tmp)
        test_declared_empty(tmp)
        test_ratchet_guard(tmp)
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
