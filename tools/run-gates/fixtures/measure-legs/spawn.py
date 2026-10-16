"""spawn.py <n> <hold_s> — a measure-legs fixture leg: n children, each sleeping hold_s. TOOL-dRedressedBar-18.

Each child is the BASE interpreter run with `-I -c`, so a launcher shim or a venv redirector adds no
process of its own and the profiler's per-process rows can be told apart by that argv. With n = 0
this process sleeps hold_s itself: it is the zero-child twin whose process count cancels the wrapper
and the interpreter, so the difference of the two counts is n by construction (AC1).
"""
import subprocess
import sys
import time

n, hold = int(sys.argv[1]), float(sys.argv[2])
exe = getattr(sys, "_base_executable", None) or sys.executable
kids = [subprocess.Popen([exe, "-I", "-c", "import time; time.sleep(%r)" % hold]) for _ in range(n)]
if not kids:
    time.sleep(hold)
sys.exit(max([k.wait() for k in kids] or [0]))
