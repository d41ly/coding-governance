"""printenv.py — a measure-legs fixture leg: every environment NAME it sees, then one planted credential.

TOOL-dRedressedBar-18, AC9 and AC11. Names only, never values: the log is a durable record. Then a
URL whose userinfo the profiler's redaction must mask before the log is kept. TOOL-dRedressedBar-19,
AC39: then the byte 0xe7 and, after a CRLF, a second planted credential, written to the binary
stdout, so a redaction that decodes, or drops a CR, loses a byte the log must keep.
"""
import os
import sys

for name in sorted(os.environ):
    print(name)
print("https://u:s3cret@example.invalid/x")
sys.stdout.flush()
sys.stdout.buffer.write(b"\xe7\r\nhttps://v:s3cret@example.invalid/y\n")
sys.stdout.buffer.flush()
