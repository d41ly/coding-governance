# **Serves:** research PLAY-dClosedLoop-1
"""Derive dClosedLoop's review debt: every design commit after the whole-design shape audit that no closing review's
range covers.

A closing review names its range as `<base>...<head>` with the base excluded, and its commits are those after the base
up to the head. The floor is the newest commit whose v2 blob is the one the shape audit's run A names as its subject,
since that audit read the whole design there. A design commit touches a record under the build folder that is not a
research return, an instruments record, the session log, a comparison of review runs, or a generator or its output.

Usage: python -X utf8 review_debt.py [<head>]   (from the worktree root); prints the floor, the ranges and one row per
uncovered commit, and writes nothing.

Promoted from the session's scratchpad (`cloud/review_debt.py`) for the whole-design audit's Stage 0, which runs it in any tree;
byte for byte its scratch original but for this note and the Serves line.
"""
import pathlib
import re
import subprocess
import sys

HEAD = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
B = "memory/builds/dClosedLoop/"
V2 = B + "build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
NOT_DESIGN = re.compile(r"-research-|-instruments\.md$|-session-log\.md$|-compared\.md$|-reviews-|\.(py|html|svg|json|txt)$")


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, encoding="utf-8", check=True).stdout


audit = pathlib.Path(B + "reviews/2026-10-18-review-PLAY-dClosedLoop-1-shape-audit-a.md").read_text(encoding="utf-8")
blob = re.search(re.escape(V2) + r"@([0-9a-f]{40})", audit).group(1)
floor = next(c for c in git("log", "--format=%H", HEAD, "--", V2).split()
             if git("rev-parse", f"{c}:{V2}").strip() == blob)
print(f"floor: {floor[:9]}, the commit whose v2 blob the shape audit read ({blob[:9]})")

ranges = []
for rec in sorted(pathlib.Path(B + "reviews").glob("*.md")):
    m = re.search(r"\b([0-9a-f]{40})\.\.\.([0-9a-f]{40})\b", rec.read_text(encoding="utf-8"))
    if m:
        ranges.append((rec.name, m.group(1), m.group(2)))
covered = {}
for name, base, head in ranges:
    for c in git("rev-list", f"{base}..{head}").split():
        covered.setdefault(c, name)
print(f"closing-review ranges read: {len(ranges)}, commits they cover: {len(covered)}")

rows = []
for c in git("rev-list", "--reverse", f"{floor}..{HEAD}").split():
    files = [f for f in git("diff-tree", "--no-commit-id", "--name-only", "-r", c).split()
             if f.startswith(B + "build/") and not NOT_DESIGN.search(f)]
    if files and c not in covered:
        subject = git("log", "-1", "--format=%s", c).strip()
        rows.append((c[:9], subject, len(files)))
print(f"design commits after the floor that no closing review covers: {len(rows)}")
for sha, subject, n in rows:
    print(f"  {sha}  {n} design record(s)  {subject[:110]}")
