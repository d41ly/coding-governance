"""memio.py <mb> — a measure-legs fixture leg: commit and touch <mb> MiB, then write <mb> MiB. TOOL-dRedressedBar-18.

The job's peak commit must read at least <mb> MiB and its write counters at least <mb> MiB (AC2).
The file goes under TMPDIR, the scratch the profiler gives every leg, and is removed before exit.
"""
import os
import sys
import tempfile

mb = int(sys.argv[1])
block = bytearray(mb * 1024 * 1024)
for off in range(0, len(block), 4096):
    block[off] = 1
fd, path = tempfile.mkstemp(prefix="memio.")
try:
    with os.fdopen(fd, "wb") as fh:
        step = 1024 * 1024
        for off in range(0, len(block), step):
            fh.write(block[off:off + step])
        fh.flush()
        os.fsync(fh.fileno())
finally:
    os.remove(path)
sys.exit(0)
