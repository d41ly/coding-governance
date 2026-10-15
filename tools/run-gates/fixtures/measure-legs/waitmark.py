"""waitmark.py <path> <bound_s> — a measure-legs fixture leg that ends on a mark, not on a clock.
TOOL-dRedressedBar-25 S18.

It polls every 0.1 s, exits 0 once <path> exists and exits 1 once <bound_s> seconds pass without it,
printing nothing. `test_legs_table` runs it after `orphan.sh 2 <mark>`, whose background subshell
creates the mark only once it has printed `late` and closed its stdout and stderr, so a `hold` that
exits 0 ends after the orphan's last write and its last handle on the capture, and a mark that never
comes is a failed `hold`.
"""
import os
import sys
import time

path, end = sys.argv[1], time.monotonic() + float(sys.argv[2])
while not os.path.exists(path):
    if time.monotonic() >= end:
        sys.exit(1)
    time.sleep(0.1)
sys.exit(0)
