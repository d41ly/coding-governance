# **Serves:** research PLAY-dClosedLoop-1
"""Find every [chain] row whose planned-units cell holds "; " inside parentheses, backticks or double quotes, where the
unit count's split on "; " cuts one clause into several.

Usage: python -X utf8 paren_semis.py   (from the worktree root); exit 1 when any is found

Promoted from the session's scratchpad (`walk/paren_semis.py`) for the whole-design audit's Stage 0, which runs it in any tree;
byte for byte its scratch original but for this note and the Serves line.
"""
import re
import sys

v2 = open("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md", encoding="utf-8").read()
chain = v2.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
found = 0
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| [^|]+ \| (.+) \| [^|]+ \|$", ln)
    if not m:
        continue
    depth, tick, quote, at = 0, False, False, []
    cell = m.group(2)
    for i, ch in enumerate(cell):
        if ch == "`" and not quote:
            tick = not tick
        elif ch == '"' and not tick:
            quote = not quote
        elif not tick and ch == "(":
            depth += 1
        elif not tick and ch == ")":
            depth = max(0, depth - 1)
        elif cell.startswith("; ", i) and (depth or tick or quote):
            at.append(i)
    for i in at:
        found += 1
        print(f"{m.group(1)}: ...{cell[max(0, i - 70):i + 50]}...")
print(f"splits inside a clause: {found}")
sys.exit(1 if found else 0)
