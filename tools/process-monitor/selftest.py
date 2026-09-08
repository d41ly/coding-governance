#!/usr/bin/env python3
"""selftest.py — the process-monitor engine's arms.

gov:kit process-monitor@0.1

Two kinds of arm and the split is deliberate. PARSING arms run over captured fixtures, so they grade
column contracts without a live table. LIVENESS arms run over a live read, because a property like
"this row answers a signal probe" cannot be observed on a fixture whose rows are all long dead — a
criterion aimed at a frozen fixture for a live property can neither pass nor fail.

    python tools/process-monitor/selftest.py

Exit 0 = every arm passed · 1 = an arm failed.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import census  # noqa: E402

PASS = []
FAIL = []


def check(name, got, want):
    if got == want:
        PASS.append(name)
        print("  ok   %s" % name)
    else:
        FAIL.append(name)
        print("  FAIL %s (got %r, wanted %r)" % (name, got, want), file=sys.stderr)


def check_true(name, cond, why=""):
    check(name, bool(cond), True) if cond else (
        FAIL.append(name), print("  FAIL %s %s" % (name, why), file=sys.stderr))


def build_cim_fixture():
    """Two well-formed rows, one with no command line, plus a CONTINUATION row.

    The continuation row is the shape run-gates.sh:432-436 records: a command line containing a
    newline splits one process across rows whose leading fields are prose. Its first token here is
    NOT a number, which is what the guard tests.
    """
    s = census._CIM_SEP
    return "\n".join([
        s.join(["4242", "1000", "12.5", "3600", "C:/x/bash.exe -c sleep"]),
        s.join(["4243", "4242", "0.0", "60", ""]),
        "  && export TEMP='C:/tmp' && echo hi",          # continuation: no numeric head
        s.join(["notanumber", "4242", "1.0", "10", "x"]),  # non-numeric id
    ])


def build_ps_w_fixture():
    """`ps -W`: a header, one REAL msys row, one SYNTHETIC row carrying the 0x400000 bit."""
    return "\n".join([
        "      PID    PPID    PGID     WINPID   TTY         UID    STIME COMMAND",
        "     5000    4999    4999       4242   ?         197609 01:00:00 /usr/bin/bash",
        "  4198485       0       0       4243   ?              0 01:00:00 /c/x/python.exe",
    ])


# ---------------------------------------------------------------- parsing arms

def test_row_contract_is_complete():
    cim, _ = census.parse_cim(build_cim_fixture())
    psw, _ = census.parse_ps_w(build_ps_w_fixture())
    rows = census.build_windows_rows(cim, psw)
    check("test_row_contract_is_complete",
          all(sorted(r) == sorted(census.FIELDS) for r in rows) and
          all(r["winpid"] is not None for r in rows) and
          all(r["win_ppid"] is not None for r in rows),
          True)


def test_both_kinds_are_present_and_distinguished():
    cim, _ = census.parse_cim(build_cim_fixture())
    psw, _ = census.parse_ps_w(build_ps_w_fixture())
    rows = {r["winpid"]: r for r in census.build_windows_rows(cim, psw)}
    # 4242's ps -W PID (5000) carries no synthetic bit -> a real MSYS row
    # 4243's ps -W PID (4198485) carries the bit    -> native, msys ids withheld
    check("test_both_kinds_are_present_and_distinguished",
          (rows[4242]["kind"], rows[4242]["msys_pid"], rows[4242]["msys_ppid"],
           rows[4243]["kind"], rows[4243]["msys_pid"], rows[4243]["msys_ppid"]),
          ("msys", 5000, 4999, "native", None, None))


def test_native_is_the_majority_on_this_node():
    """The PARTITION's shape, not the non-emptiness of each part.

    "At least one of each" passes on a table labelled entirely one way, which is precisely the
    defect this arm replaced: without the 0x400000 discriminator every row grades `msys`.
    """
    if not sys.platform.startswith("win"):
        print("  SKIP test_native_is_the_majority_on_this_node "
              "(measured on the Windows join; no live table here)")
        return
    rows, counts = census.scan_processes()
    check_true("test_native_is_the_majority_on_this_node",
               counts["native"] > counts["msys"],
               "(native %d, msys %d — a table labelled entirely one way reds here)"
               % (counts["native"], counts["msys"]))


def test_continuation_rows_are_rejected_and_counted():
    cim, rejected = census.parse_cim(build_cim_fixture())
    check("test_continuation_rows_are_rejected_and_counted", (len(cim), rejected), (2, 2))


def test_partial_rows_survive_and_are_counted_apart():
    cim, _ = census.parse_cim(build_cim_fixture())
    psw, _ = census.parse_ps_w(build_ps_w_fixture())
    rows = census.build_windows_rows(cim, psw)
    counts = census.measure_rows(rows, 0, "windows-join")
    # 4243 reports no command line; it SURVIVES with None and is counted, never dropped.
    check("test_partial_rows_survive_and_are_counted_apart",
          (counts["total"], counts["no_command"],
           {r["winpid"]: r["command"] for r in rows}[4243]),
          (2, 1, None))


def test_unjoined_row_keeps_native_kind():
    """A CIM row with no `ps -W` overlay at all is native with both msys fields None."""
    cim, _ = census.parse_cim(build_cim_fixture())
    rows = {r["winpid"]: r for r in census.build_windows_rows(cim, {})}
    check("test_unjoined_row_keeps_native_kind",
          (rows[4242]["kind"], rows[4242]["msys_pid"], rows[4242]["msys_ppid"]),
          ("native", None, None))


def test_posix_fixture_collapses_both_namespaces():
    """UNEXERCISED LIVE on this node: MSYS `ps` rejects `-o` outright, so this is fixture-only and
    says so rather than implying coverage of the live POSIX path."""
    fixture = "\n".join([
        "  PID  PPID ELAPSED     TIME COMMAND",
        " 4242  1000    3600 00:00:12 /bin/bash -c sleep",
        " 4243  4242      60 01:02:03 /usr/bin/python3 -c pass",
        " junk  4242      60 00:00:01 not a row",
    ])
    rows, rejected = census.parse_posix(fixture)
    by = {r["winpid"]: r for r in rows}
    check("test_posix_fixture_collapses_both_namespaces",
          (len(rows), rejected,
           by[4242]["winpid"] == by[4242]["msys_pid"],
           by[4242]["win_ppid"] == by[4242]["msys_ppid"],
           by[4242]["age_s"], by[4242]["cpu_s"], by[4243]["cpu_s"], by[4243]["kind"]),
          (2, 1, True, True, 3600.0, 12.0, 3723.0, "msys"))


def test_cpu_clock_parses_every_shape():
    check("test_cpu_clock_parses_every_shape",
          (census.parse_cpu_clock("00:00:12"), census.parse_cpu_clock("01:02:03"),
           census.parse_cpu_clock("2-03:00:00"), census.parse_cpu_clock("12"),
           census.parse_cpu_clock("nonsense")),
          (12.0, 3723.0, 183600.0, 12.0, None))


def test_non_utf8_backend_output_survives():
    """A CP1252 byte in a command line must not kill the read.

    Measured on the real table: `subprocess.run(..., text=True)` died with a UnicodeDecodeError at
    byte 66732, on a READER THREAD, leaving `.stdout` as None.
    """
    raw = (b"4242" + census._CIM_SEP.encode() + b"1000" + census._CIM_SEP.encode()
           + b"1.0" + census._CIM_SEP.encode() + b"60" + census._CIM_SEP.encode()
           + b"caf\xe7 /x/y")
    cim, rejected = census.parse_cim(raw.decode("utf-8", "replace"))
    check("test_non_utf8_backend_output_survives", (len(cim), rejected), (1, 0))


def test_summary_counts_are_derived():
    cim, rej = census.parse_cim(build_cim_fixture())
    psw, _ = census.parse_ps_w(build_ps_w_fixture())
    rows = census.build_windows_rows(cim, psw)
    counts = census.measure_rows(rows, rej, "windows-join")
    text = census.render_rows(rows, counts)
    check("test_summary_counts_are_derived",
          (counts["total"] == len(rows),
           counts["msys"] + counts["native"] == len(rows),
           str(len(rows)) in text.splitlines()[-1],
           text.splitlines()[0] == "\t".join(census.FIELDS)),
          (True, True, True, True))


# ---------------------------------------------------------------- refusal arms

def test_no_backend_refuses():
    got = "no refusal"
    try:
        census.scan_processes("nonesuch")
    except census.CensusRefused as exc:
        got = "refused" if "nonesuch" in str(exc) else "refused without naming it"
    check("test_no_backend_refuses", got, "refused")


def test_empty_read_refuses_rather_than_reporting_zero():
    """The green-by-absence guard, staged: a backend answering nothing must RAISE."""
    saved = census.run_bounded
    census.run_bounded = lambda argv, timeout=0: ""
    try:
        census.scan_processes("windows-join")
        got = "returned an empty table"
    except census.CensusRefused:
        got = "refused"
    finally:
        census.run_bounded = saved
    check("test_empty_read_refuses_rather_than_reporting_zero", got, "refused")


def test_hung_backend_is_bounded():
    """The bound is on the CHILD, so a hung reader raises rather than blocking forever.

    Staged with a real sleeping child and a 2s bound. A bound applied around a pipeline would bound
    the verdict and not the clock, which is the class selected for these paths.
    """
    import time
    started = time.time()
    got = "did not refuse"
    try:
        census.run_bounded([sys.executable, "-c", "import time; time.sleep(30)"], timeout=2)
    except census.CensusRefused as exc:
        got = "refused" if "did not answer" in str(exc) else "refused for the wrong reason"
    elapsed = time.time() - started
    check("test_hung_backend_is_bounded", (got, elapsed < 20), ("refused", True))


# ---------------------------------------------------------------- liveness arms

def test_live_read_sees_itself():
    if not sys.platform.startswith("win"):
        print("  SKIP test_live_read_sees_itself (windows-join backend only)")
        return
    rows, counts = census.scan_processes()
    mine = os.getpid()
    check("test_live_read_sees_itself",
          (counts["total"] > 1, any(r["winpid"] == mine for r in rows)),
          (True, True))


def test_every_live_row_answers_its_own_liveness_probe():
    """A row the reaper's own signal path cannot see is a row the census must not claim.

    LIVE, not the fixture: the fixture's rows are all long dead, so this criterion could neither
    pass nor fail there. A row that exits between the scan and the probe is re-read once.
    """
    if not sys.platform.startswith("win"):
        print("  SKIP test_every_live_row_answers_its_own_liveness_probe (windows-join only)")
        return
    rows, _ = census.scan_processes()
    msys_rows = [r for r in rows if r["kind"] == "msys"][:6]
    if not msys_rows:
        FAIL.append("test_every_live_row_answers_its_own_liveness_probe")
        print("  FAIL test_every_live_row_answers_its_own_liveness_probe "
              "(no msys rows to probe — a skip here is indistinguishable from coverage)",
              file=sys.stderr)
        return
    unanswered = []
    for r in msys_rows:
        done = subprocess.run(["kill", "-0", str(r["msys_pid"])], capture_output=True)
        if done.returncode != 0:
            fresh, _ = census.scan_processes()          # re-read once: it may simply have exited
            if any(x["winpid"] == r["winpid"] for x in fresh):
                unanswered.append(r["msys_pid"])
    check_true("test_every_live_row_answers_its_own_liveness_probe", not unanswered,
               "(these msys rows are still present but do not answer kill -0: %r)" % unanswered)


def main():
    print("process-monitor census: arms")
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print("\nprocess-monitor census: %d passed, %d failed (%d assertions)"
          % (len(PASS), len(FAIL), len(PASS) + len(FAIL)))
    return 1 if FAIL else 0




# ================================================================ scope (unit 2)

import scope  # noqa: E402

ROOTS = ["/c/projects/gov"]


def build_row(winpid, win_ppid, command, age=100.0, msys_pid=None, msys_ppid=None, cpu=1.0):
    return {"winpid": winpid, "msys_pid": msys_pid, "win_ppid": win_ppid,
            "msys_ppid": msys_ppid, "kind": "msys" if msys_pid else "native",
            "age_s": age, "cpu_s": cpu, "command": command, "backend": "windows-join"}


def build_corpus():
    """A tree we own, a native grandchild, a no-command descendant, and NOT-OURS rows.

    The not-ours rows are the point: a fixture holding only in-scope rows cannot fail in the
    direction that matters. `explorer.exe` here is parentless and ancient, exactly the shape the
    live table carries 18 of.
    """
    return [
        build_row(10, 1, "/c/projects/gov/x/bash.exe -c 'run'", age=500.0),   # ROOT
        build_row(11, 10, "bash -c ./relative.sh", age=400.0),                # relative argv
        build_row(12, 11, "/usr/bin/sleep 900", age=300.0),                   # bare argv
        build_row(13, 12, "python.exe -c pass", age=200.0),                   # native grandchild
        build_row(14, 13, None, age=100.0),                                   # no command
        build_row(90, 1, "C:/Windows/explorer.exe", age=300000.0),            # NOT ours, ancient
        build_row(91, 90, "C:/Windows/system32/lsass.exe", age=300000.0),     # NOT ours
        build_row(92, 1, "bash -c \"export TEMP='/c/projects/gov' && echo hi\"", age=50.0),
    ]


def test_scope_over_the_frozen_corpus_is_exact():
    sc, counts = scope.derive_scope(build_corpus(), ROOTS)
    check("test_scope_over_the_frozen_corpus_is_exact",
          (sorted(sc), 90 in sc, 91 in sc, 92 in sc),
          ([10, 11, 12, 13, 14], False, False, False))


def test_declared_root_admits_and_names_it():
    sc, _ = scope.derive_scope(build_corpus(), ROOTS)
    check("test_declared_root_admits_and_names_it", sc[10]["root"], "/c/projects/gov")


def test_closure_reaches_bare_argv_and_native_descendants():
    """rev-2 refused three of these four. It is D9, D20 and D22 in one fixture."""
    sc, _ = scope.derive_scope(build_corpus(), ROOTS)
    check("test_closure_reaches_bare_argv_and_native_descendants",
          (11 in sc, 12 in sc, 13 in sc), (True, True, True))


def test_self_chain_is_in_scope_but_not_killable():
    sc, _ = scope.derive_scope(build_corpus(), ROOTS, self_chain={10, 11})
    check("test_self_chain_is_in_scope_but_not_killable",
          (10 in sc, sc[10]["killable"], sc[11]["killable"], sc[12]["killable"]),
          (True, False, False, True))


def test_blank_roots_refuses():
    got = "no refusal"
    try:
        scope.derive_scope(build_corpus(), [])
    except scope.ScopeRefused:
        got = "refused"
    check("test_blank_roots_refuses", got, "refused")


def test_root_that_claims_everything_refuses():
    outcomes = []
    for bad in ("/", "c:", "/c/x"):
        try:
            scope.derive_scope(build_corpus(), [bad])
            outcomes.append("admitted")
        except scope.ScopeRefused:
            outcomes.append("refused")
    check("test_root_that_claims_everything_refuses", outcomes, ["refused"] * 3)


def test_prefix_is_separator_anchored():
    rows = [build_row(20, 1, "/c/projects/gov-scratch/x/bash.exe"),
            build_row(21, 1, "/c/projects/gov/x/bash.exe")]
    sc, _ = scope.derive_scope(rows, ROOTS)
    check("test_prefix_is_separator_anchored", (20 in sc, 21 in sc), (False, True))


def test_assignment_inside_a_dash_c_body_does_not_admit():
    """CONSTRUCTED, and stated as such: checked against the live table, in zero of the nine rows
    carrying `export TEMP=` is the assignment the ONLY occurrence of the root. The vector is real,
    the isolated instance is not, so the fixture is built rather than claimed to be captured."""
    rows = [build_row(30, 1, "bash -c \"source /x/y && export TEMP='/c/projects/gov' && echo\"")]
    sc, _ = scope.derive_scope(rows, ROOTS)
    check("test_assignment_inside_a_dash_c_body_does_not_admit", 30 in sc, False)


def test_a_real_path_inside_a_dash_c_body_does_admit():
    """The other direction: the tokenizer must not simply discard `-c` bodies."""
    rows = [build_row(31, 1, "bash -c \"/c/projects/gov/tools/run.sh --flag\"")]
    sc, _ = scope.derive_scope(rows, ROOTS)
    check("test_a_real_path_inside_a_dash_c_body_does_admit", 31 in sc, True)


def test_recycled_parent_edge_is_dropped_and_counted():
    rows = build_corpus() + [build_row(40, 10, "/usr/bin/other", age=900.0)]  # older than its parent
    sc, counts = scope.derive_scope(rows, ROOTS)
    check("test_recycled_parent_edge_is_dropped_and_counted",
          (40 in sc, counts["dropped_edges"] > 0), (False, True))


def test_no_command_row_can_be_a_descendant_but_not_a_root():
    sc, _ = scope.derive_scope([build_row(50, 1, None)], ROOTS)
    sc2, _ = scope.derive_scope(build_corpus(), ROOTS)
    check("test_no_command_row_can_be_a_descendant_but_not_a_root",
          (50 in sc, 14 in sc2), (False, True))


def test_msys_edges_are_translated_before_the_union():
    """The MSYS parent names an MSYS id, which must be joined to a winpid first. An untranslated
    union looks up 7000 in the winpid map and finds nothing — or worse, finds an unrelated row."""
    rows = [build_row(60, 1, "/c/projects/gov/x/bash.exe", msys_pid=7000, msys_ppid=1),
            build_row(61, 999, "/usr/bin/sleep 900", msys_pid=7001, msys_ppid=7000)]
    sc, counts = scope.derive_scope(rows, ROOTS)
    check("test_msys_edges_are_translated_before_the_union",
          (60 in sc, 61 in sc), (True, True))


def test_cyclic_graph_terminates():
    rows = [build_row(70, 71, "/c/projects/gov/x/a", age=100.0),
            build_row(71, 70, "/usr/bin/b", age=100.0)]
    sc, _ = scope.derive_scope(rows, ROOTS)
    check("test_cyclic_graph_terminates", 70 in sc, True)


def test_tokenizer_strips_assignments_everywhere():
    check("test_tokenizer_strips_assignments_everywhere",
          (scope.parse_tokens("export A=/c/x B=/c/y prog /c/z"),
           scope.parse_tokens("A=/c/x prog")),
          (["prog", "/c/z"], ["prog"]))


def test_live_scope_is_not_empty():
    """The fence, invoked the way the PRODUCT invokes it. Every fence defect across three audit
    rounds was invisible because the fence was only ever exercised over planted fixtures."""
    if not sys.platform.startswith("win"):
        print("  SKIP test_live_scope_is_not_empty (windows-join backend only)")
        return
    root_dir = os.environ.get("PROCMON_ROOT") or subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True,
        text=True).stdout.strip()
    rows, _ = census.scan_processes()
    sc, _ = scope.derive_scope(rows, scope.load_conf(root_dir),
                               scope.build_self_chain(rows, os.getpid()))
    check_true("test_live_scope_is_not_empty", len(sc) > 0,
               "(the shipped conf admits NOTHING on this machine)")


# ================================================================ classify (unit 3)

import classify  # noqa: E402

CEIL, RATE = 100.0, 0.5


def build_graded(**kw):
    r = build_row(kw.pop("winpid", 1), kw.pop("win_ppid", 999), kw.pop("command", "/x"),
                  age=kw.pop("age", 200.0), cpu=kw.pop("cpu", 1.0), **kw)
    return r


def test_every_verdict_member_has_a_producing_fixture():
    """Counting members is not coverage; PRODUCING them is. rev-3 carried an OVERAGE member no
    input could emit, and the closed-set arm passed on the spelling of the enum."""
    live = {999}
    produced = {
        classify.derive_verdict(build_graded(age=50.0), CEIL, RATE, live),
        classify.derive_verdict(build_graded(cpu=None), CEIL, RATE, live),
        classify.derive_verdict(build_graded(win_ppid=4242), CEIL, RATE, live),
        classify.derive_verdict(build_graded(cpu=180.0), CEIL, RATE, live),
        classify.derive_verdict(build_graded(cpu=1.0), CEIL, RATE, live),
    }
    check("test_every_verdict_member_has_a_producing_fixture",
          (sorted(produced), sorted(classify.VERDICTS)),
          (sorted(classify.VERDICTS), sorted(classify.VERDICTS)))


def test_ceiling_decides_before_any_label():
    """A young row is OK even at rate 1.0 with no live parent — otherwise every healthy gate leg
    and every fresh shell on the box reds."""
    check("test_ceiling_decides_before_any_label",
          (classify.derive_verdict(build_graded(age=99.0, cpu=99.0, win_ppid=4242), CEIL, RATE, {999}),
           classify.derive_verdict(build_graded(age=101.0, cpu=101.0, win_ppid=4242), CEIL, RATE, {999})),
          ("OK", "ORPHAN"))


def test_native_parentless_row_is_orphan_and_reaped():
    """`msys_ppid` absent is the NATIVE majority. It must not make the row UNKNOWN — that was
    rev-3's defect and it made reap-orphans inert over the whole target population."""
    r = build_graded(win_ppid=4242, msys_pid=None, msys_ppid=None)
    check("test_native_parentless_row_is_orphan_and_reaped",
          classify.derive_verdict(r, CEIL, RATE, {999}), "ORPHAN")


def test_live_windows_parent_is_not_an_orphan():
    check("test_live_windows_parent_is_not_an_orphan",
          classify.derive_verdict(build_graded(win_ppid=999), CEIL, RATE, {999}), "IDLE")


def test_no_cpu_row_is_unknown():
    check("test_no_cpu_row_is_unknown",
          classify.derive_verdict(build_graded(cpu=None, win_ppid=4242), CEIL, RATE, {999}),
          "UNKNOWN")


def test_rate_boundary_is_inclusive():
    check("test_rate_boundary_is_inclusive",
          (classify.derive_verdict(build_graded(age=200.0, cpu=100.0), CEIL, RATE, {999}),
           classify.derive_verdict(build_graded(age=200.0, cpu=99.0), CEIL, RATE, {999})),
          ("SPIN", "IDLE"))


def test_msys_ppid_participates_in_no_predicate():
    """Two rows identical but for msys_ppid must grade the same."""
    a = build_graded(winpid=1, win_ppid=999, msys_pid=None, msys_ppid=None)
    b = build_graded(winpid=2, win_ppid=999, msys_pid=50, msys_ppid=51)
    check("test_msys_ppid_participates_in_no_predicate",
          classify.derive_verdict(a, CEIL, RATE, {999}) ==
          classify.derive_verdict(b, CEIL, RATE, {999}), True)


def test_summary_counts_are_derived_from_the_run():
    rows = [build_row(1, 999, "/c/projects/gov/a", age=200.0, cpu=1.0),
            build_row(2, 4242, "/c/projects/gov/b", age=200.0, cpu=1.0),
            build_row(999, 1, "/c/projects/gov/parent", age=500.0, cpu=1.0)]
    graded, counts = classify.scan_verdicts(rows, {1: {}, 2: {}, 999: {}}, CEIL, RATE)
    text = classify.render_report(graded, counts)
    check("test_summary_counts_are_derived_from_the_run",
          (counts["census"], counts["scoped"], counts["flagged"] == len(graded),
           str(len(graded)) in text.splitlines()[-1]),
          (3, 3, True, True))


def test_out_of_scope_rows_are_never_graded():
    """The ordering that keeps explorer.exe alive: an unadmitted row is not graded at all."""
    rows = [build_row(90, 4242, "C:/Windows/explorer.exe", age=300000.0, cpu=1.0)]
    graded, counts = classify.scan_verdicts(rows, {}, CEIL, RATE)
    check("test_out_of_scope_rows_are_never_graded", (len(graded), counts["flagged"]), (0, 0))


if __name__ == "__main__":
    sys.exit(main())
