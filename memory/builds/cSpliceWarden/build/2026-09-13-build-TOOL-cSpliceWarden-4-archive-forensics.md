# How the 2026-08-17 TOOL archive came to contradict itself

**Serves:** journal TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-1

The build README carries the canon's five slots and cannot hold this. It is the evidence behind
them, established from git rather than inferred, and it is what a future session should read before
touching a rotated archive.

## The measured state, all of it derived

Every figure was derived by reading the files at base `09a22d2b` on 2026-09-12, never carried from
prose. They describe the file AS FOUND, not as written: it was created on 2026-08-17 holding 13
rows, and merges that day and after appended to it — 17 at `c1af5dd2`, 29 at `b7e49c99`, 34 at
`0bea5595`. The 90-row state is where this repair found it, a month later.
Re-derive with `python tools/memory-tree/row_grammar.py --report` and the partition query below.

| fact | value |
|---|---|
| rows in `archive/TOOL.2026-08-17.md` | 90 |
| terminal (CLOSED) | 24 |
| non-terminal | 66 — 60 OPEN, 5 SPECCED, 1 DEFERRED |
| ids also live in `backlog/TOOL.md` | 49 |
| of those, disagreeing on status | 7 |
| ids duplicated inside the archive | 2 (`TOOL-aBranchedMandate-2`, `-3`) |
| ids shared with `archive/TOOL.2026-08-17b.md` | 17 |
| archive-only ids carrying a non-terminal row | 17 |
| of those, ROWS needing a new home | 15 |
| true status of all 17, from git and their specs | CLOSED |
| `archive/TOOL.2026-08-14.md` | 48 rows, 48 terminal — clean under `cut` |
| `archive/TOOL.2026-08-17b.md` | 23 rows, 23 terminal — clean under `cut` |

## The root cause

The 2026-08-17 rotation happened TWICE, on two branches, on one day, to one filename. The branch
that wrote `memory/archive/TOOL.2026-08-17.md` had never seen the commits that closed the rows it
froze.

`TOOL-cBriefedPilot-1` is the clean specimen. Its spec has read `**Status:** CLOSED` since rev-3 on
2026-08-16, and commit `c32161be` flipped its backlog row OPEN → CLOSED on 2026-08-15. Walking
`origin/main`'s ancestry, the row's status then alternates between CLOSED and OPEN nine times across
three days before going absent entirely. `9d41abb1`, the commit whose branch created the archive, is
**not** a descendant of `c32161be` — the two sat on parallel branches, and the one that rotated was
the one that still believed the row was open.

The row-keyed merge driver was failing during exactly that window. `c1af5dd2`'s own message records
it: *"The row-keyed merge driver had failed (the known linked-worktree ConfError), so both index
stages were row-only and gave no structure to merge against."* With the driver down, a backlog merge
resolves by taking a side, and taking a side is how a closure gets un-closed.

## Why `cut` and not merely the tidier option

Under whole-file-snapshot rotation a live row exists in two files, one of which can never be
updated. A status disagreement is then STRUCTURAL — not a thing that went wrong, but the steady
state. All seven disagreements here are that. Under `cut` the two files partition the family, every
id lives in exactly one of them, and the disagreement has nowhere to form.

Both disciplines are coherent, which is why the mode is DECLARED rather than hardcoded. inCMS
deliberately practises the snapshot form (`ARCH-aTemperedLoom-19`, its `scripts/rotate_index.py`
R1-R6 invariants and `carry_backlog.py`). A kit shipping to both projects must let each say which it
runs.

## Seventeen ids, fifteen rows

The gap between those two numbers is a defect this build had to find, and it is the one place the
brief was wrong. `TOOL-aBranchedMandate-2` and `-3` carry TWO rows each in the archive — SPECCED at
lines 86-87 and CLOSED at 94-95 — so they are at once "archive-only and non-terminal" and "the stale
duplicate pair". Re-homing them on the first reading would have written two SPECCED rows into the
live shard while their CLOSED rows stayed in the archive: two brand-new cross-file status
contradictions, in the build that exists to remove cross-file status contradictions, and invisible to
check 20 because it is per-file.

The partition, verified exact before it was applied — every row in exactly one set, none in two and
none in none:

| set | rows | disposition |
|---|---|---|
| live shard already owns the id | 49 | deleted from the archive |
| archive-only, non-terminal, no terminal twin | 15 | re-homed to `memory/backlog/TOOL.md` |
| stale half of an in-file duplicate pair | 2 | dropped; the CLOSED twin survives |
| terminal survivors | 24 | kept |

49 + 15 + 2 + 24 = 90. After the repair, a re-check found all 90 original rows still accounted for —
surviving in the archive, present in the live shard, or quoted verbatim in the supersession note —
and no id gone from the memory tree at all.

## The re-homed rows carry a recovered body, not the archive's

All 15 grade CLOSED, established twice over: from each id's spec status header, and from the closing
commit on `origin/main`'s ancestry. The two agree in every case. The archive preserves the PRE-close
body, because a closing commit often rewrote the sentence as well as the token — **4 of the 15
differ**. Re-homing the archive text verbatim would have re-asserted claims the tree refutes:
`TOOL-aStandingWrit-3`'s archive body says the unattended instruction layer "is unowned in this
tree", and `BUILD-METHOD.md` has existed since.

Each row was therefore written with the body from its closing commit, not the one the archive froze.

## What is left, and deliberately

17 of the 24 surviving rows are still byte-identical rows of `TOOL.2026-08-17b.md`; only 6 of that
file's 23 rows are unique to it. The archive PAIR therefore does not partition the family even after
this repair, which is why the corrected header does not claim exclusivity. Filed, not fixed.
