"""churn.py <s> — a measure-legs fixture leg: silent, spawning `-c pass` children back to back for s seconds.

TOOL-dRedressedBar-18, AC7. Each child lives far shorter than one census scan, so the census walk of
this tree sees little CPU, while the job's exact accounting sees every child's. The job veto is what
keeps this leg from reading STALLED.
"""
import subprocess
import sys
import time

exe = getattr(sys, "_base_executable", None) or sys.executable
end = time.monotonic() + float(sys.argv[1])
while time.monotonic() < end:
    subprocess.run([exe, "-I", "-c", "pass"], check=False)
sys.exit(0)
