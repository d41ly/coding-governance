"""Split one traced check-wiring.sh run into its arm windows, and sum each candidate's cost.

usage: python 2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py <trace> <check-wiring.sh>

The trace is the one 2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh writes, and <script> is
the check-wiring.sh that run executed: its line numbers must be the ones the trace carries.

The run list is DERIVED from the script: every column-0 line that is exactly a name beginning
`check_`. A window opens at the first process's row for one of those lines and runs to the row
before the next; `(prelude)` precedes the first and the last closes at the trace's final row. Per
window: wall (first row to the next window's first row), forks (process ids first seen in it, the
first process excluded) and execs, by the counter's own parser and exec rule, loaded from the file
beside this one and never restated here.

Two guards, each exiting 1 with a line naming what failed: every run-list line must match exactly
one row of the first process, else the trace was not taken from this script; and the TOTAL must
equal the counter's whole-trace figures, else a row fell outside every window.

WHAT IT DOES NOT DO: decide which arms a caller needs. The candidate sets below are named
constants, derived from the verdict reading in 2026-10-11-build-TOOL-aBriskPreflight-3-wiring-scope.md;
an arm added to the script lands in C1 and C2 and in no other candidate without an edit here.
"""
import importlib.util
import os
import re
import sys

COUNTER = '2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py'
RUN_LIST_LINE = re.compile(r'^check_[a-z_]*$')
PRELUDE = '(prelude)'
# The two arms that cannot raise `unwired` under --check (the record's verdict reading).
REPORT_ONLY = ('check_eol', 'check_backlog_stragglers')
# ponytail: C3 is the prelude and check_hooks only; its blob and mode helpers run inside that window.
C3_ARMS = (PRELUDE, 'check_hooks')


def load_trace_spawns():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), COUNTER)
    spec = importlib.util.spec_from_file_location('trace_spawns', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def derive_run_list(script):
    out = []
    with open(script, encoding='utf-8', errors='replace') as f:
        for n, line in enumerate(f, 1):
            line = line.rstrip('\r\n')
            if RUN_LIST_LINE.match(line):
                out.append((n, line))
    return out


def measure_arm_windows(ts, rows, script):
    """[(name, wall, forks, execs)], or exits 1 when a run-list line does not match the trace."""
    base = script.replace('\\', '/').rsplit('/', 1)[-1]
    _, funcs = ts.load_spans([script])
    first = rows[0][1]
    run_list = derive_run_list(script)
    if not run_list:
        sys.exit('arm-windows: %s has no run-list line (a column-0 `check_*` call), so it is not check-wiring.sh' % script)
    starts = [(0, PRELUDE)]
    for n, name in run_list:
        hits = [i for i, (_, pid, src, ln, cmd) in enumerate(rows)
                if pid == first and src == base and ln == n and cmd.strip() == name]
        if len(hits) != 1:
            sys.exit('arm-windows: run-list line %s:%d `%s` matched %d rows of the first process, not 1 -- '
                     'the trace was not taken from this script' % (base, n, name, len(hits)))
        if hits[0] <= starts[-1][0]:
            sys.exit('arm-windows: run-list line %s:%d `%s` traced before the window it should follow' % (base, n, name))
        starts.append((hits[0], name))
    seen, out = set(), []
    for k, (i, name) in enumerate(starts):
        j = starts[k + 1][0] if k + 1 < len(starts) else len(rows)
        end_ts = rows[j][0] if j < len(rows) else rows[-1][0]
        forks = execs = 0
        for _, pid, _, _, cmd in rows[i:j]:
            if pid not in seen:
                seen.add(pid)
                forks += pid != first
            execs += ts.check_exec(cmd, funcs)
        out.append((name, end_ts - rows[i][0], forks, execs))
    pids, ex, _, _, _ = ts.measure_trace(rows, *ts.load_spans([script]))
    want = (round(rows[-1][0] - rows[0][0], 6), len(pids) - 1, sum(ex.values()))
    got = (round(sum(w[1] for w in out), 6), sum(w[2] for w in out), sum(w[3] for w in out))
    if got != want:
        sys.exit('arm-windows: TOTAL %r is not the counter\'s %r (wall, forks, execs) -- a row fell outside every window'
                 % (got, want))
    return out


def print_arm_windows(windows):
    names = [w[0] for w in windows]
    candidates = (
        ('C1 whole --check', names),
        ('C2 all but %s' % '+'.join(REPORT_ONLY), [n for n in names if n not in REPORT_ONLY]),
        ('C3 prelude+check_hooks', list(C3_ARMS)),
    )
    row = '%-50s %9s %6s %6s'
    print(row % ('window', 'wall_s', 'forks', 'execs'))
    for name, wall, forks, execs in windows:
        print('%-50s %9.1f %6d %6d' % (name, wall, forks, execs))
    by = {w[0]: w for w in windows}
    print('%-50s %9.1f %6d %6d' % ('TOTAL', sum(w[1] for w in windows), sum(w[2] for w in windows),
                                   sum(w[3] for w in windows)))
    print()
    for label, arms in candidates:
        picked = [by[a] for a in arms if a in by]
        print('%-50s %9.1f %6d %6d' % (label, sum(w[1] for w in picked), sum(w[2] for w in picked),
                                       sum(w[3] for w in picked)))


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    ts = load_trace_spawns()
    rows = ts.parse_rows(sys.argv[1])
    if len(rows) < 2:
        sys.exit('arm-windows: too few trace rows: %d' % len(rows))
    print_arm_windows(measure_arm_windows(ts, rows, sys.argv[2]))


if __name__ == '__main__':
    main()
