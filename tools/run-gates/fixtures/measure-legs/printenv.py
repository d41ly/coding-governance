"""printenv.py — a measure-legs fixture leg: every environment NAME it sees, then one planted credential.

TOOL-dRedressedBar-18, AC9 and AC11. Names only, never values: the log is a durable record. The last
line is a URL whose userinfo the profiler's redaction must mask before the log is kept.
"""
import os

for name in sorted(os.environ):
    print(name)
print("https://u:s3cret@example.invalid/x")
