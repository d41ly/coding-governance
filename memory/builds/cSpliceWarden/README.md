---
slug: cSpliceWarden
node: c
opened: 2026-09-12
streams: tooling+playbook
roster: TOOL
ids: TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-5 TOOL-cSpliceWarden-6 TOOL-cSpliceWarden-7 TOOL-cSpliceWarden-8
---

# cSpliceWarden — the archive that contradicted itself, and the rotation nobody declared

Node `c` · opened 2026-09-12 · streams tooling+playbook.

`memory/archive/TOOL.2026-08-17.md` says in its own header that it holds "Terminal rows only …
deduplicated by id". It holds 90 rows. Twenty-four are terminal. Sixty-six are not, forty-nine of
its ids are also live in `memory/backlog/TOOL.md`, seven of those disagree about status, and two ids
appear in it twice. Seventeen of its ids exist in no other backlog shard or archive at all, and for
fifteen of those the only surviving row says OPEN about work that closed a month ago.

No gate sees any of this, and the reason is not an oversight in one check. It is that **this repo
never declared what a rotation MEANS**, so nothing could grade the result. `memory/HYGIENE.md` says
both things at once — `git mv` the whole index, AND carry every non-terminal row forward — and taken
together those two sentences duplicate every live row into a frozen file. That duplication is not an
accident of this one archive. It is what the documented procedure produces.

This README is the master overview and the owner decision menu, per `memory/TEMPLATE-SPEC.md`.

## Start here

**The root cause, established from git rather than inferred.** The 2026-08-17 rotation happened
twice, on two branches, on the same day, to the same filename. The branch that wrote
`memory/archive/TOOL.2026-08-17.md` had never seen the commits that closed those rows.

`TOOL-cBriefedPilot-1` is the clean specimen. Its spec
(`memory/builds/cBriefedPilot/spec/2026-08-14-spec-cBriefedPilot-1.md`) has read
`**Status:** CLOSED` since rev-3 on 2026-08-16. Commit `c32161be` flipped its backlog row OPEN →
CLOSED on 2026-08-15. Walking `origin/main`'s ancestry, the row's status then alternates between
CLOSED and OPEN nine times across three days — every reversion arriving with a merge from a branch
that carried the older token — before going absent entirely. `9d41abb1`, the commit whose branch
created the archive, is **not** a descendant of `c32161be`: the two sat on parallel branches, and the
one that rotated was the one that still believed the row was open.

The row-keyed merge driver was failing during exactly this window. `c1af5dd2`'s own commit message
records it: *"The row-keyed merge driver had failed (the known linked-worktree ConfError), so both
index stages were row-only and gave no structure to merge against."* With the driver down, a backlog
merge resolves by taking a side, and taking a side is how a closure gets un-closed.

**Why `cut` is the answer and not merely the tidier option.** Under whole-file-snapshot rotation a
live row exists in two files, one of which can never be updated. A status disagreement is then
structural — not a thing that went wrong, but the steady state. All seven disagreements here are
that. Under `cut` the two files partition the family, every id lives in exactly one of them, and the
disagreement has nowhere to form.

Both disciplines are coherent, which is why this build declares the mode rather than hardcoding it.
inCMS deliberately practises the snapshot form (`ARCH-aTemperedLoom-19`, its `scripts/rotate_index.py`
R1-R6 invariants and `carry_backlog.py`). A kit shipped to both projects must let each say which it
runs, and must refuse to grade a tree that has said neither.

## The measured state, all of it derived

Every figure below is DERIVED at writing time by reading the files, never carried from prose.
Re-derive with `python tools/memory-tree/row_grammar.py --report` and the queries in unit 4's spec.

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

The seventeen are the whole of the damage: `TOOL-aBranchedMandate-2`, `-3`, `TOOL-aStandingWrit-3`,
`TOOL-cFinalBerth-3`, and `TOOL-cBriefedPilot-1`, `-4`, `-5`, `-6`, `-11`, `-12`, `-15`, `-16`, `-17`,
`-18`, `-19`, `-20`, `-21`. Each one's terminal row text was recovered from `origin/main`'s own
history, because the closing commit rewrote the BODY as well as the token — the archive preserves the
pre-close prose, and re-homing its text verbatim would re-assert claims the tree refutes. Four of the
fifteen differ that way.

**Seventeen ids, fifteen rows, and the gap between those two numbers is a defect this build had to
find.** `TOOL-aBranchedMandate-2` and `-3` carry TWO rows each in the archive — SPECCED at lines 86-87
and CLOSED at 94-95 — so they are at once "archive-only and non-terminal" and "the stale duplicate
pair". Re-homing them on the first reading would have written two SPECCED rows into the live shard
while their CLOSED rows stayed in the archive: two brand-new cross-file status contradictions, in the
build that exists to remove cross-file status contradictions, and invisible to check 20 because it is
per-file. Their CLOSED rows are correct and terminal, so under `cut` they belong where they already
are. Unit 4's §4 carries the full four-way partition and its arithmetic.

## Units

| id | tier | mechanism | order |
|---|---|---|---|
| `TOOL-cSpliceWarden-1` | 2 | `ROTATION_MODE` declared in `.memory-tree.conf`, and the one rotation semantics written into the HYGIENE pair and the charter template | 1 |
| `TOOL-cSpliceWarden-2` | 2 | hygiene check 10 reaches backlog archives — four defects, not the two filed | 2 |
| `TOOL-cSpliceWarden-3` | 2 | hygiene check 20 reaches backlog archives | 4 |
| `TOOL-cSpliceWarden-4` | 1 | the archive repair: supersession note, evacuation, the fifteen re-homed | 3 |
| `TOOL-cSpliceWarden-5` | 1 | the records: two duplicate rows consolidated, one false retirement superseded | 5 |

**The order is load-bearing and is not a preference.** Unit 4 runs BEFORE unit 3. Widening check 20
to backlog archives while the two stale duplicate rows are still in the file raises the measured
duplicate count from 3 to 5, and `ROW_DUPLICATE_PIN` is shrink-only and exact-match — so building in
the other order forces a wrong-way pin move and then a second commit to undo it. Evacuate first and
the pin never moves. Measured, not reasoned: `row_grammar.scan` over the widened file set returns 5
duplicates today and 3 after the evacuation.

## BUILD-LEVEL RULES

- Classification per `BUILD-METHOD.md` M2 is recorded per unit in its own spec §9 on first pass.
- The archive is a ratified record. Unit 4 does not silently rewrite it: the supersession note states
  every false claim verbatim and quotes every removed row, and the removal is the owner's ratified
  decision of 2026-09-12, not the run's judgment.
- No figure in this build's prose is authored where a command can derive it.

<!-- gen:build-index -->
**Build status:** CLOSED · 5 unit(s) · node c · opened 2026-09-12 · streams tooling+playbook
ids TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-5 TOOL-cSpliceWarden-6 TOOL-cSpliceWarden-7 TOOL-cSpliceWarden-8

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-cSpliceWarden-1 — rotation becomes a DECLARED mode, and one semantics replaces two](spec/2026-09-12-spec-TOOL-cSpliceWarden-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-cSpliceWarden-2 — hygiene check 10 reaches a backlog archive, and stops reporting a reassuring zero](spec/2026-09-12-spec-TOOL-cSpliceWarden-2.md) | 2 | 2 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-cSpliceWarden-4 — the archive repair: superseded, evacuated, and fifteen rows re-homed](spec/2026-09-12-spec-TOOL-cSpliceWarden-4.md) | 3 | 1 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-cSpliceWarden-3 — hygiene check 20 scans a rotated backlog shard](spec/2026-09-12-spec-TOOL-cSpliceWarden-3.md) | 4 | 2 | CLOSED | rev-2 | 2026-09-13 |
| [TOOL-cSpliceWarden-5 — two rows filing one gap become one, and a false retirement is superseded](spec/2026-09-12-spec-TOOL-cSpliceWarden-5.md) | 5 | 1 | CLOSED | rev-2 | 2026-09-13 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-cSpliceWarden-1 TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-5.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-cSpliceWarden-1` | no |
| 2 | `TOOL-cSpliceWarden-2` | no |
| 3 | `TOOL-cSpliceWarden-4` | no |
| 4 | `TOOL-cSpliceWarden-3` | no |
| 5 | `TOOL-cSpliceWarden-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
