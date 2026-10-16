"""steady.py <s> — a measure-legs fixture leg: silent and busy for s seconds. TOOL-dRedressedBar-18.

Its log never grows and its one process burns CPU the whole time, so the stall test's CPU half must
keep it from reading STALLED however long the window (AC6), and it is the leg a held host turnstile
runs beside (AC15).
"""
import sys
import time

end = time.monotonic() + float(sys.argv[1])
n = 0
while time.monotonic() < end:
    n += 1
sys.exit(0)
