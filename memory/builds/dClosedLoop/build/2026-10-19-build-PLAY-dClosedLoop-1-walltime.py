# **Serves:** research PLAY-dClosedLoop-1
"""Wall time for the whole-design audit's stages, read from the agents' own transcripts: each agent's first and last
timestamp and its wall, and each stage's span from its first agent's start to its last agent's end. No review had
recorded its wall time (`gap-rt-26`; research-final-audit `[1a]`), so the audit records its own.

Usage: python walltime.py <transcripts dir> <stage>=<agent id>[,<agent id>...] ...
  e.g. walltime.py <dir> walk-A=<id>,<id>,<id>,<id>,<id> skeptics-A=<id>,<id>,<id>,<id> synthesis-A=<id>
An agent's transcript is `<dir>/agent-<id>.jsonl`, one JSON object a line, each with its `timestamp`.
Exit 0, or 2 on a transcript that is missing or holds no timestamp.

What it does not measure: time the main loop spent between stages, which the stages' spans leave out and the total's
first start and last end include; and an agent the harness restarted, whose transcript holds both runs.
"""
import json
import sys
from datetime import datetime
from pathlib import Path


def span(path):
    stamps = []
    for ln in path.read_text(encoding="utf-8").splitlines():
        try:
            t = json.loads(ln).get("timestamp")
        except ValueError:
            continue
        if t:
            stamps.append(datetime.fromisoformat(t.replace("Z", "+00:00")))
    return (min(stamps), max(stamps)) if stamps else None


def wall(seconds):
    m, s = divmod(int(round(seconds)), 60)
    h, m = divmod(m, 60)
    return f"{h}h{m:02d}m{s:02d}s" if h else f"{m}m{s:02d}s"


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    folder, starts, ends = Path(argv[0]), [], []
    for arg in argv[1:]:
        stage, ids = arg.split("=", 1)
        spans = []
        for aid in ids.split(","):
            p = folder / f"agent-{aid}.jsonl"
            s = span(p) if p.exists() else None
            if s is None:
                print(f"walltime: {stage}: no timestamps for agent {aid} at {p.as_posix()}")
                return 2
            spans.append((aid, *s))
        first, last = min(s[1] for s in spans), max(s[2] for s in spans)
        starts.append(first)
        ends.append(last)
        total = sum((s[2] - s[1]).total_seconds() for s in spans)
        print(f"{stage}: agents {len(spans)}, from {first:%H:%M:%S} to {last:%H:%M:%S} UTC, span "
              f"{wall((last - first).total_seconds())}, agent walls summed {wall(total)}")
        for aid, a, b in spans:
            print(f"  {aid}: {a:%H:%M:%S} to {b:%H:%M:%S}, {wall((b - a).total_seconds())}")
    print(f"total: from {min(starts):%Y-%m-%d %H:%M:%S} to {max(ends):%Y-%m-%d %H:%M:%S} UTC, "
          f"{wall((max(ends) - min(starts)).total_seconds())}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
