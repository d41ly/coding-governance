# **Serves:** research PLAY-dClosedLoop-1
"""The chain's critical path: the longest chain of builds by planned units, over v2's [chain] after relation, and
what each candidate edge would add to it.

Usage: python critical_path.py [--edge <child>:<parent> ...]   (from the worktree root)

A build's units are its planned-units cell's clauses, counted as the map counts them (split on "; "). A build
starts when every parent has landed, so the path's length is the largest sum of units along a parent chain.

Promoted from the session's scratchpad (`order/critical_path.py`) for the whole-design audit's Stage 0, which runs it in any tree;
byte for byte its scratch original but for this note and the Serves line.
"""
import re
import sys

V = "memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md"
text = open(V, encoding="utf-8").read()
chain = text.split("\n## [chain]", 1)[1].split("\n## ", 1)[0]
units, parents = {}, {}
for ln in chain.split("\n"):
    m = re.match(r"^\| (d[A-Z]\w+) \| [^|]+ \| ([^|]+) \| (.+) \| [^|]+ \|$", ln)
    if m:
        units[m.group(1)] = len([u for u in m.group(3).split("; ") if u.strip()])
        parents[m.group(1)] = [p.strip() for p in m.group(2).split(",") if p.strip() in
                               re.findall(r"^\| (d[A-Z]\w+) \|", chain, flags=re.M)]
assert len(units) == 22, len(units)   # 21 until the owner's FQ-4 opened the chain with dTrueNorth, 2026-10-19; 16 until SP-1, 18 until WK-4 split dTotalRecall and dBoundRoles, 20 until
#                                       AP-25 gave the upgrade-step kind its own build, dSafePassage, 2026-10-18


def longest(par):
    memo, via = {}, {}

    def f(b, seen=()):
        if b in seen:
            sys.exit(f"cycle through {b}")
        if b not in memo:
            best, arg = 0, None
            for p in par[b]:
                v = f(p, seen + (b,))
                if v > best:
                    best, arg = v, p
            memo[b], via[b] = best + units[b], arg
        return memo[b]

    for b in par:
        f(b)
    end = max(memo, key=memo.get)
    path, b = [], end
    while b:
        path.append(b)
        b = via[b]
    return memo[end], list(reversed(path)), memo


base, path, memo = longest(parents)
print(f"critical path: {base} units, {' > '.join(path)}")
print("each build's earliest finish, in units: " + ", ".join(f"{b} {memo[b]}" for b in sorted(memo, key=memo.get)))
for arg in [a for a in sys.argv[1:] if ":" in a]:
    child, parent = arg.split(":")
    par = {b: list(ps) for b, ps in parents.items()}
    par[child] = par[child] + [parent]
    length, p, _ = longest(par)
    print(f"with {child} after {parent}: {length} units ({length - base:+d}), {' > '.join(p)}")
