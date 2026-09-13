#!/usr/bin/env python3
"""runlog.py — the runlog kit's command line. gov:kit runlog@1.0

    python <this kit>/runlog.py journal --producer driver|gates|pushes

`journal` prints one producer file's parsed lines to stdout, one JSON object per line whose keys are
exactly the line's keys, and puts everything a human reads on stderr: the resolved path, the line
count and the bad-line count, which is ALWAYS printed for a file that exists, so a writer emitting
garbage is loud rather than filtered out. The journal root is the git common dir of the clone the
command runs IN, so every worktree of one clone reads the same file.

Exit 0 = the file was read, or is absent (a named state: no producer has written yet) · 2 = no
journal root resolves, or the file exists and cannot be read.
"""
import argparse
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import runlog_lib as rl  # noqa: E402

# How many refusal reasons are printed under the count. The COUNT is never capped; only the list is,
# so a journal of a million torn lines prints a bounded stderr and still says a million.
REFUSALS_SHOWN = 5


def cmd_journal(args) -> int:
    try:
        root = rl.resolve_journal_root()
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    path = root / rl.PRODUCER_FILES[args.producer]
    journal = rl.read_journal(path)
    shown = journal.path
    if journal.state == "absent":
        print(f"runlog: {shown} absent", file=sys.stderr)
        return 0
    if journal.state == "unreadable":
        print(f"runlog: {shown} unreadable — {journal.note}", file=sys.stderr)
        return 2
    for line in journal.lines:
        sys.stdout.write(json.dumps(line.fields) + "\n")
    sys.stdout.flush()
    empty = " empty" if journal.state == "empty" else ""
    print(f"runlog: {shown}{empty} lines={len(journal.lines)} bad={journal.bad}", file=sys.stderr)
    for lineno, why in journal.refusals[:REFUSALS_SHOWN]:
        print(f"runlog: {shown}:{lineno} refused — {why}", file=sys.stderr)
    if journal.bad > REFUSALS_SHOWN:
        print(f"runlog: {journal.bad - REFUSALS_SHOWN} more refusal(s) not listed", file=sys.stderr)
    return 0


def main(argv=None) -> int:
    # A path or a refusal reason can carry a character the console's code page lacks, and a print
    # that raises on it would turn a report into a traceback.
    sys.stderr.reconfigure(errors="backslashreplace")
    ap = argparse.ArgumentParser(prog="runlog.py", description="Read a run log in the runlog grammar.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pj = sub.add_parser("journal", help="print one producer file's lines as JSON, counts on stderr")
    pj.add_argument("--producer", required=True, choices=sorted(rl.PRODUCER_FILES))
    args = ap.parse_args(argv)
    return cmd_journal(args)


if __name__ == "__main__":
    sys.exit(main())
