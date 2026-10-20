# **Serves:** research PLAY-dClosedLoop-1
"""Which lines of dClosedLoop's design records no Tier-2 review has read, line by line.

Usage: python coverage_v2.py [--plant-uncover <review-stem>]   (from the worktree root)

Each report's "Reviewed:", "Range:" or "Subjects (round N):" line is a blob set (an audit that read named records whole at those
blobs) or a range (a diff review over (base, head]). `git blame HEAD` gives every current line the commit that
last wrote it. A line is reviewed when an audit read its record at a blob whose commit descends from that
commit, or when that commit lies inside a reviewed range. Anything else is unreviewed.
--plant-uncover drops one report, to see the lines it covered turn unreviewed.

Promoted from the session's scratchpad (`the state record's [revisit-instrument], coverage_v2.py`) for the whole-design audit's Stage 0, which runs it in any tree;
byte for byte its scratch original but for this note and the Serves line.
"""
import collections
import pathlib
import re
import subprocess
import sys

REV = pathlib.Path("memory/builds/dClosedLoop/reviews")
BUILD = pathlib.Path("memory/builds/dClosedLoop/build")
SKIP = re.compile(r"-1-(research-|session-log|compaction-)|compared|instruments")


def git(*a):
    r = subprocess.run(["git", *a], capture_output=True, text=True, encoding="utf-8")
    return r.stdout


drop = sys.argv[sys.argv.index("--plant-uncover") + 1] if "--plant-uncover" in sys.argv else None
audits, ranges = [], {}
for p in sorted(REV.glob("*.md")):
    stem = p.stem.split("PLAY-dClosedLoop-1-")[1]
    if stem == drop:
        continue
    m = re.search(r"^(?:Reviewed|Range|Range reviewed|Subjects \(round \d+\)): (.+)$", p.read_text(encoding="utf-8"), re.M)
    if not m:
        sys.exit(f"{p.name}: no Reviewed or Range line")
    r = re.match(r"([0-9a-f]{40})\.\.\.?([0-9a-f]{40})", m.group(1))
    if r:
        ranges[stem] = set(git("rev-list", f"{r.group(1)}..{r.group(2)}").split())
        continue
    pairs = re.findall(r"(memory/builds/dClosedLoop/build/[^@,\s]+\.md)@([0-9a-f]{40})", m.group(1))
    if not pairs:
        sys.exit(f"{p.name}: a Reviewed line that is neither a range nor a blob set")
    audits += [(stem, path, blob) for path, blob in pairs]
print(f"reports read: {len(set(a[0] for a in audits))} audits over {len(audits)} record blobs, {len(ranges)} diff ranges")

# For each audited (record, blob): the commits touching the record that the audit point descends from.
# `audited` is kept apart, since a lookup in the defaultdict would add every record to it.
covered_by_audit = collections.defaultdict(set)
audited = {path for _, path, _ in audits}
for stem, path, blob in audits:
    cands = git("log", "--format=%H", f"--find-object={blob}", "--", path).split()
    points = [c for c in cands if git("rev-parse", f"{c}:{path}").strip() == blob]
    if not points:
        sys.exit(f"{stem}: blob {blob[:9]} of {path} matches no commit")
    covered_by_audit[path] |= set(git("rev-list", points[0], "--", path).split())

subject = {}
rows = []
for p in sorted(BUILD.glob("*.md")):
    if SKIP.search(p.name):
        continue
    path = p.as_posix()
    blame = git("blame", "--line-porcelain", "HEAD", "--", path)
    commits = [ln.split()[0] for ln in blame.split("\n") if re.match(r"^[0-9a-f]{40} \d+ \d+", ln)]
    unrev = collections.Counter()
    for c in commits:
        if c in covered_by_audit[path] or any(c in s for s in ranges.values()):
            continue
        unrev[c] += 1
    for c in unrev:
        if c not in subject:
            subject[c] = git("log", "-1", "--format=%h %s", c).strip()
    rows.append((p.stem.split("PLAY-dClosedLoop-1-")[1], len(commits), sum(unrev.values()),
                 path in audited, unrev))

total = sum(r[1] for r in rows)
unrev_total = sum(r[2] for r in rows)
print(f"design records {len(rows)} · lines {total} · unreviewed {unrev_total} ({100 * unrev_total / total:.0f}%)")
print()
print(f"{'record':<34} {'lines':>6} {'unrev':>6} {'share':>6}  read whole")
for name, n, u, whole, _ in sorted(rows, key=lambda r: -r[2]):
    print(f"{name:<34} {n:>6} {u:>6} {100 * u / n if n else 0:>5.0f}%  {'yes' if whole else 'no'}")
print()
by_commit = collections.Counter()
for *_, unrev in rows:
    by_commit.update(unrev)
print("unreviewed lines by the commit that wrote them, the largest 25:")
for c, n in by_commit.most_common(25):
    print(f"  {n:>5}  {subject[c][:150]}")
