"""Count the processes a traced bash run created, and attribute its wall time, from one xtrace file.

usage: python trace_spawns.py <trace> <script> [<script> ...]

The trace is written with
    env SHELLOPTS=xtrace BASH_XTRACEFD=9 PS4='+${EPOCHREALTIME} ${BASHPID} ${BASH_SOURCE##*/}:${LINENO} ' \
        bash <script> <args> 9>><trace>
so every bash process in the tree, child scripts included, writes its own rows into the one file.

Two counts, both independent of how loaded the host is:
- forks: distinct BASHPID values, less the first. A subshell, a `$(...)` and a child bash script
  each traced at least one row from a new process id. A fork that traced nothing is not seen.
- execs: rows whose first word is neither a bash builtin, a keyword, an assignment nor a function
  defined in one of the scripts named. Each one is a program the shell started.
The wall-clock figures are the gap from each row to the next, so an untraced child (git, python,
node, sed) is charged to the row that started it. Concurrent processes interleave, so the per-row
attribution is only exact for a run that does one thing at a time; the two counts are exact either way.

WHAT IT DOES NOT COUNT: a program started by a program that is not bash (git running its hooks,
python's subprocess calls), and a fork that never ran a traced command.
"""
import re
import sys
from collections import defaultdict

BUILTINS = set('''. : [ alias bg bind break builtin caller cd command compgen complete compopt continue
declare dirs disown echo enable eval exec exit export false fc fg getopts hash help history jobs kill
let local logout mapfile popd printf pushd pwd read readarray readonly return set shift shopt source
suspend test times trap true type typeset ulimit umask unalias unset wait
if then else elif fi case esac for select while until do done in function time { } ! [[ ]] coproc
(( ))'''.split())
ROW = re.compile(r'^(\++)(\d+\.\d+) (\d+) ([^ :]*):(\d+) (.*)$')
DEF = re.compile(r'^\s*(?:function\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*\(\)\s*\{?')
ASSIGN = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*(\[[^]]*\])?\+?=')


def parse_rows(path):
    rows = []
    with open(path, encoding='utf-8', errors='replace') as f:
        for line in f:
            m = ROW.match(line.rstrip('\n'))
            if m:
                rows.append((float(m.group(2)), m.group(3), m.group(4), int(m.group(5)), m.group(6)))
    return rows


def load_spans(scripts):
    """basename -> sorted [(line, function)], and the set of every function name defined."""
    spans, names = {}, set()
    for s in scripts:
        starts = []
        with open(s, encoding='utf-8', errors='replace') as f:
            for i, line in enumerate(f, 1):
                m = DEF.match(line)
                if m and '()' in line:
                    starts.append((i, m.group(1)))
                    names.add(m.group(1))
        spans[s.replace('\\', '/').rsplit('/', 1)[-1]] = starts
    return spans, names


def resolve_func(spans, src, n):
    name = '(top level)'
    for s, nm in spans.get(src, []):
        if s > n:
            break
        name = nm
    return name


def check_exec(cmd, funcs):
    word = cmd.split(' ', 1)[0].strip("'")
    if not word or ASSIGN.match(word) or word in BUILTINS or word in funcs:
        return False
    return True


def measure_trace(rows, spans, funcs):
    pids, execs = [], defaultdict(int)
    seen = set()
    by_func, by_line, n_line = defaultdict(float), defaultdict(float), defaultdict(int)
    for i, (ts, pid, src, n, cmd) in enumerate(rows):
        if pid not in seen:
            seen.add(pid)
            pids.append(pid)
        gap = rows[i + 1][0] - ts if i + 1 < len(rows) else 0.0
        key = '%s:%d' % (src, n)
        by_func['%s %s' % (src, resolve_func(spans, src, n))] += gap
        by_line[key] += gap
        n_line[key] += 1
        if check_exec(cmd, funcs):
            execs[cmd.split(' ', 1)[0].strip("'")] += 1
    return pids, execs, by_func, by_line, n_line


def print_report(rows, pids, execs, by_func, by_line, n_line, sample):
    wall = rows[-1][0] - rows[0][0]
    print('trace rows %d, wall %.1fs, forks %d, execs %d' % (len(rows), wall, len(pids) - 1, sum(execs.values())))
    print('\n## execs by program')
    for k, v in sorted(execs.items(), key=lambda kv: -kv[1])[:25]:
        print('%7d  %s' % (v, k))
    print('\n## wall by function (s)')
    for k, v in sorted(by_func.items(), key=lambda kv: -kv[1])[:25]:
        print('%9.1f  %s' % (v, k))
    print('\n## wall by line (s, executions, sample)')
    for k, v in sorted(by_line.items(), key=lambda kv: -kv[1])[:25]:
        print('%9.1f %6d  %s  %s' % (v, n_line[k], k, sample[k][:110]))


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    rows = parse_rows(sys.argv[1])
    if len(rows) < 2:
        sys.exit('too few trace rows: %d -- was PS4 the shape the docstring names?' % len(rows))
    spans, funcs = load_spans(sys.argv[2:])
    sample = {}
    for _, _, src, n, cmd in rows:
        sample.setdefault('%s:%d' % (src, n), cmd)
    print_report(rows, *measure_trace(rows, spans, funcs), sample)


if __name__ == '__main__':
    main()
