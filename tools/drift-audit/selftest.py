#!/usr/bin/env python3
"""selftest.py — the drift-audit kit's own falsifiability test.

gov:kit drift-audit@1.9

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
import io
import pathlib
import shutil
import re
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
    for key in ("MEMORY_ROOT", "DISCIPLINES", "QUOTED_SINGLE", "TRAILING",
                "EXPORTED", "INLINE"):
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

    # --- DEPL-dGaugedVintage-13: a backlog row that outlived its own CLOSED spec ---
    print("backlog rows outliving closed specs (dGV-13)")
    b13 = report(r)["backlog_rows_outliving_closed_specs"]
    check("[dGV-13] a spec whose id is in NO backlog row is not a finding",
          b13["value"] == 0, f"got {b13['value']} detail={b13['detail']}")
    check("[dGV-13] ...and the signal is LIVE, so a zero means it looked",
          b13["live"] is True and b13["of"] >= 1, f"live={b13['live']} of={b13['of']}")
    _shard = r / "memory" / "backlog"
    _shard.mkdir(parents=True, exist_ok=True)
    _ids = [x["id"] for x in report(r)["spec_status_terminal_ids"]["detail"]] \
        if "spec_status_terminal_ids" in report(r) else []
    _sp = sorted((r / SPEC_DIR_FOR_FIXTURE).glob("*.md"))
    _own = None
    for _f in _sp:
        _m = re.search(r"^#\s+([A-Z]+-[a-zA-Z]+-\d+)\b", _f.read_text(encoding="utf-8"), re.M)
        _s = re.search(r"^\*\*Status:\*\*\s*([A-Za-z]+)", _f.read_text(encoding="utf-8"), re.M)
        if _m and _s and _s.group(1).upper() in ("CLOSED", "WONTDO"):
            _own = _m.group(1)
            break
    if _own is None:
        skip("[dGV-13] the row arms", "this fixture carries no terminal spec to key a row on")
    else:
        _fam = _own.split("-", 1)[0]
        _row = _shard / f"{_fam}.md"
        _row.write_text(f"# fixture backlog\n\n- {_own} \u00b7 OPEN \u00b7 a row that outlived its spec\n",
                        encoding="utf-8", newline="\n")
        run(["git", "add", "-A"], r); run(["git", "commit", "-qm", "dgv13 open row"], r)
        b13o = report(r)["backlog_rows_outliving_closed_specs"]
        check("[dGV-13] a NON-terminal row under a CLOSED spec is counted",
              b13o["value"] == 1, f"got {b13o['value']} detail={b13o['detail']}")
        check("[dGV-13] ...and the detail names the id, the row's token and the spec's",
              bool(b13o["detail"]) and b13o["detail"][0]["id"] == _own
              and b13o["detail"][0]["row_status"] == "OPEN",
              str(b13o["detail"][:1]))
        _row.write_text(f"# fixture backlog\n\n- {_own} \u00b7 CLOSED \u00b7 reconciled\n",
                        encoding="utf-8", newline="\n")
        run(["git", "add", "-A"], r); run(["git", "commit", "-qm", "dgv13 closed row"], r)
        b13c = report(r)["backlog_rows_outliving_closed_specs"]
        check("[dGV-13] a TERMINAL row under the same spec is not counted",
              b13c["value"] == 0, f"got {b13c['value']} detail={b13c['detail']}")

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

    kit_src = pathlib.Path(__file__).resolve().parent.parent / "lexicon"
    shutil.copytree(kit_src, r / "tools" / "lexicon",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (r / ".lexicon.conf").write_text(
        'BANNED_SUFFIXES="Manager"\nLANGS="py:python-ast:parser"\n'
        'VERB_OFFENDER_PIN="99"\nSUFFIX_OFFENDER_PIN="0"\nLAYER_OFFENDER_PIN="0"\n'
        'ratified="2999-01-01 node t"\n\nVERBS:\n  build  make a thing\n\nLAYERS:\n  src/* -> vendor/*\n',
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
    shutil.copytree(kit_src, b / "tools" / "lexicon",
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    (b / ".lexicon.conf").write_text(
        'BANNED_SUFFIXES="Manager"' + chr(10) + 'LANGS="py:python-ast:parser"' + chr(10)
        + 'VERB_OFFENDER_PIN="99"' + chr(10) + 'SUFFIX_OFFENDER_PIN="0"' + chr(10)
        + 'LAYER_OFFENDER_PIN="0"' + chr(10) + 'ratified="2999-01-01 node t"' + chr(10) + chr(10)
        + "VERBS:" + chr(10) + "  build  make a thing" + chr(10) + chr(10)
        + "LAYERS:" + chr(10) + "  src/* -> vendor/*" + chr(10),
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
        "**Status:** CLOSED - rev-2 - 2026-01-05 - node a - Tier-2 - base 0000000",
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
        src = (KIT.parent / "workflows" / harness).read_text(encoding="utf-8")
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
    proj = r / "drift-audit" / "drift_signals.py"
    conf = r / ".memory-tree.conf"
    spec_dir = r / SPEC_DIR_FOR_FIXTURE

    def add(rel: str, body: str, msg: str) -> None:
        p = r / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8", newline="\n")
        run(["git", "add", "-A"], r)
        run(["git", "commit", "-q", "-m", msg, "--no-verify"], r)

    def sig(*extra: str) -> dict:
        return report(r, *extra)["non_terminal_specs_cited_by_product_source"]

    # ---- ARM 1: the correction-form id. Its seq carries a trailing lowercase letter, which the
    # hand-typed digits-then-boundary pattern could not match at all -- so the spec scored UNKEYED
    # and the probe declined to judge it, silently. Observed RED against that pattern: the spec was
    # absent from the judgeable population entirely.
    before = sig()["of"]
    add(str(pathlib.Path(SPEC_DIR_FOR_FIXTURE) / "2026-01-02-spec-aFixed-1b.md").replace("\\", "/"),
        "# TOOL-aFixed-1b \u2014 a ratified correction\n\n"
        "**Status:** SPECCED \u00b7 rev-1 \u00b7 2026-01-02 \u00b7 node a \u00b7 Tier-2 \u00b7 base 0000000\n",
        "spec(aFixed): a correction-form id")
    check("evidence: a correction-form id is JUDGED, not silently unkeyed",
          sig()["of"] == before + 1,
          f"population {before} -> {sig()['of']}, wanted +1")

    # ---- ARM 2: a citation from a TEST file is the house's own bookkeeping certifying the
    # bookkeeping, so it must not count as evidence a unit shipped. The same id cited from a
    # PRODUCT file must count. Both halves, because only the pair discriminates.
    add("src/thing.test.sh", "# cites TOOL-aThing-1 from a test file\n",
        "test: cite a spec id from a test file")
    check("evidence: a test-file citation is not evidence a unit shipped",
          all(row["id"] != "TOOL-aThing-1" for row in sig()["detail"]),
          f"detail: {[row['id'] for row in sig()['detail']]}")
    add("src/thing.py", "# cites TOOL-aThing-1 from product source\n",
        "feat: cite the same id from product source")
    check("evidence: a product-file citation IS evidence a unit shipped",
          any(row["id"] == "TOOL-aThing-1" for row in sig()["detail"]),
          f"detail: {[row['id'] for row in sig()['detail']]}")

    # ---- ARM 3: the drain. Remove every remaining product citation and the VALUE reaches zero,
    # while the judgeable population does NOT -- they are different fields, and an arm asserting on
    # the population would be green whatever the citations did.
    (r / "src" / "thing.py").unlink()
    run(["git", "add", "-A"], r)
    run(["git", "commit", "-q", "-m", "chore: drop the product citation", "--no-verify"], r)
    drained = sig()
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
    dead = sig()
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
          any(row["id"] == "WDGT-aWidget-1" for row in sig()["detail"]),
          f"detail: {[row['id'] for row in sig()['detail']]}")


def test_local_grammar_matches_the_extractor(tmp: pathlib.Path) -> None:
    """The local fallback is not a second grammar, and this is what keeps it honest.

    The report falls back to a local copy of the id alternation when the recall extractor is not
    importable, which is the only way a copy-installed kit can run in a tree without it. A copy
    nobody compares is a second grammar with extra steps, so compare it -- here, where this repo
    HAS the extractor, against what the extractor itself produces for this same tree.
    """
    import importlib.util

    extractor = KIT.parent / "memory-recall" / "extract.py"
    if not extractor.exists():
        skip("local grammar equals the extractor's", "no memory-recall kit beside this one")
        return
    spec = importlib.util.spec_from_file_location("_drift_report_probe", KIT / "drift_report.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    root = KIT.parent.parent
    families = mod._families_of(mod.load_conf(root))
    check("local grammar equals the extractor's for this tree",
          mod._local_ident(families) == mod._grammar_ident(root, families),
          "the local fallback has diverged from the shipped alternation")

def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        test_conf_parser_matches_bash(tmp)
        test_harness_liveness_note_is_derived(tmp)
        test_signals_can_move(tmp)
        test_lexicon_signals(tmp)
        test_lexicon_marginal_rate(tmp)
        test_no_signal_hardcodes_live(tmp)
        test_live_backlog_rows(tmp)
        test_readme_mechanism_drift(tmp)
        test_declared_empty(tmp)
        test_ratchet_guard(tmp)
        test_ratchet_lookback(tmp)
        test_ratchet_message_states_its_window(tmp)
        test_lang_mode_ratchet(tmp)
        test_evidence_oracle(tmp)
        test_local_grammar_matches_the_extractor(tmp)
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
