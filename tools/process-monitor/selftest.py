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


if __name__ == "__main__":
    sys.exit(main())
