# Is the union parent graph sound? Three questions, measured before any code

**Serves:** research TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3

Node `a`, 2026-09-08, over 337 CIM rows and 334 `ps -W` rows, 330 overlaid. The rev-3 architecture
rests on a UNION of two parent graphs; these are the three things that could make it unsound, asked
of the real table rather than reasoned about.

## Q1 — the two graphs disagree, on 7 of 330 overlaid rows

| winpid | image | `win_ppid` | MSYS parent, as a winpid |
|---|---|---|---|
| 29956 | `bash.exe` | 14912 | 45828 |
| 48256 | `bash.exe` | 35296 | 29956 |
| 48424 | `bash.exe` | 46524 | 49528 |
| 40860 | `bash.exe` | 43636 | 44004 |
| 30444 | `bash.exe` | 30308 | 49160 |
| 47320 | `head.exe` | 33492 | 19880 |
| 40828 | `python.exe` | 28004 | 19880 |

MSYS's `fork` emulation spawns through a stub, so an MSYS process's WINDOWS parent is not its MSYS
parent. **This is not an error in either graph — both are true, about different things.**

**What it means for the closure.** The union has strictly more edges than either graph alone, so
the in-scope set is an OVER-approximation: a row can be pulled into a tree by a Windows edge that
MSYS would not recognise, and vice versa. For a REAPER that is the safe direction only because the
roots are attributable — the closure can reach further down a tree we own, never sideways into one
we do not, since every path still starts at a declared root. Stating it because the opposite
intuition (that a union is riskier) is the natural one, and because the start-time corroboration in
unit 2 §4 is what bounds the over-approximation.

## Q2 — the union contains at least one cycle

**1 row of 337 sits on a cycle.** The detector here is coarse and the exact count is not the point;
the existence is. A depth-unbounded walk over this graph without a visited-set does not terminate.

Unit 4 §8 F3 resolved to a visited-set rather than inheriting `run-gates.sh:429`'s depth-8 cap, on
the argument that it gives the same termination guarantee without discarding a deep tree. That
argument was made before this measurement and is now evidenced: the cycle guard is load-bearing on
this host, not defensive programming.

## Q3 — PARENTLESS has a large false-positive population, and the age ceiling does NOT save it

**24 of 337 rows have a `win_ppid` naming no census row. Eighteen are older than one hour.**

```
csrss.exe          86.9h        explorer.exe     86.9h
csrss.exe          86.9h        Lightshot.exe    86.9h
wininit.exe        86.9h        cmd.exe          86.9h
winlogon.exe       86.9h        msedge.exe       86.8h
vmmemCmZygote      86.8h        GitHubDesktop    79.9h
Spotify.exe        78.2h        tail.exe -f …    63.1h
```

On Windows a parent exiting does not reparent its children and does not clear the field, so
"`win_ppid` names no live process" is the ORDINARY state of every long-lived desktop process. It is
not evidence of abandonment.

**So PARENTLESS must never authorize a kill on its own, and no ceiling makes it safe** — these rows
are 78 to 87 hours old and every candidate ceiling is far below that. The only thing standing
between `reap-orphans` and `explorer.exe` is the SCOPE FENCE. That is already the design — unit 2
runs before unit 3, and unit 3 grades only members of the in-scope set — but the ordering was a
tidiness argument before this measurement and is now a safety requirement with a named casualty
list.

Two consequences taken into the round-3 fold rather than left as prose:

1. **Unit 3's spec must say that PARENTLESS is a LABEL and never a licence**, with this population
   as the evidence, so a later reader cannot reasonably read `reap-orphans` as "kill anything
   parentless".
2. **Unit 2's frozen-corpus arm (AC1) must include at least one of these rows** — a genuinely
   parentless, genuinely ancient, genuinely NOT-OURS process — and assert it is out of scope. A
   fixture of only in-scope rows cannot fail in the direction that matters.

And the last row of that table is the reason the kit exists: `tail.exe -f /tmp/revert-harness.txt`
at 63.1 hours, parentless, still holding a pipe, and genuinely abandoned. The predicate finds it.
The fence is what tells it apart from `explorer.exe`.
