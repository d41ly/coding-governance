"""hog.py <s> — a measure-legs fixture leg: one busy child per logical core for s seconds. TOOL-dRedressedBar-18.

It holds host CPU above the concurrent mode's 80% cap, so the next leg must wait for a sample at
or under it (AC4). On a host where it cannot, the arm's liveness half fails rather than passing.
"""
import os
import subprocess
import sys

s = float(sys.argv[1])
exe = getattr(sys, "_base_executable", None) or sys.executable
code = "import time\nend = time.monotonic() + %r\nwhile time.monotonic() < end:\n    pass\n" % s
kids = [subprocess.Popen([exe, "-I", "-c", code]) for _ in range(os.cpu_count() or 1)]
sys.exit(max(k.wait() for k in kids))
