# **Serves:** research TOOL-aBriskPreflight-1
"""Attribute wall time in a bash xtrace (PS4='+${EPOCHREALTIME} ${LINENO} ') to lines and functions.

usage: python trace_gaps.py <trace> <script>
Each trace line's cost is the gap to the NEXT trace line, so a slow external command (git, python,
a child script) is charged to the line that ran it.
"""
import re
import sys
from collections import defaultdict

trace, script = sys.argv[1], sys.argv[2]
rx = re.compile(r'^\++(\d+\.\d+) (\d+) (.*)$')
rows = []
with open(trace, encoding='utf-8', errors='replace') as f:
    for line in f:
        m = rx.match(line.rstrip('\n'))
        if m:
            rows.append((float(m.group(1)), int(m.group(2)), m.group(3)))
if len(rows) < 2:
    sys.exit('too few trace rows: %d' % len(rows))

# Function spans: a definition line `name() {` opens a span that runs to the next definition.
starts = []
with open(script, encoding='utf-8', errors='replace') as f:
    for i, line in enumerate(f, 1):
        m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\(\)\s*\{', line)
        if m:
            starts.append((i, m.group(1)))


def resolve_func(n):
    name = '(top level)'
    for s, nm in starts:
        if s > n:
            break
        name = nm
    return name


by_line = defaultdict(float)
cnt_line = defaultdict(int)
by_func = defaultdict(float)
cnt_func = defaultdict(int)
sample = {}
gaps = []
for (t, n, cmd), (t2, _, _) in zip(rows, rows[1:]):
    d = t2 - t
    by_line[n] += d
    cnt_line[n] += 1
    fn = resolve_func(n)
    by_func[fn] += d
    cnt_func[fn] += 1
    sample.setdefault(n, cmd[:110])
    gaps.append((d, n, cmd[:110]))

total = rows[-1][0] - rows[0][0]
print('trace rows %d, wall %.1fs' % (len(rows), total))
print('\n## by function (wall s, trace rows)')
for fn, s in sorted(by_func.items(), key=lambda x: -x[1])[:20]:
    print('%8.1f  %6d  %s' % (s, cnt_func[fn], fn))
print('\n## by line (wall s, executions, sample)')
for n, s in sorted(by_line.items(), key=lambda x: -x[1])[:25]:
    print('%8.1f  %6d  L%-6d %s' % (s, cnt_line[n], n, sample[n]))
print('\n## single largest gaps')
for d, n, c in sorted(gaps, reverse=True)[:15]:
    print('%8.1f  L%-6d %s' % (d, n, c))
