---
slug: aTrimmedWait
node: a
opened: 2026-11-14
streams: tooling
roster: TOOL
ids: TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 TOOL-aTrimmedWait-8 TOOL-aTrimmedWait-9 TOOL-aTrimmedWait-10 TOOL-aTrimmedWait-11 TOOL-aTrimmedWait-12 TOOL-aTrimmedWait-13 TOOL-aTrimmedWait-14 TOOL-aTrimmedWait-15 TOOL-aTrimmedWait-16 TOOL-aTrimmedWait-17 TOOL-aTrimmedWait-18 TOOL-aTrimmedWait-19
---

# aTrimmedWait — builds stop waiting on checks that grade more than the caller needs, without moving any verdict

## The problem this build exists to solve

Session `db957487` ran dFairHearing and aSmoothedDispatch: 334 agents and 72 h of agent wall time.
Its largest reworkable costs were waits, not work. Units were re-dispatched after `--dispatch`
refused specs it could have refused before the spec commit. Hygiene check 12 graded every spec to
check one. The pre-commit hook refused commits on a stale build index the commit could have
rendered. The idle-wake `--resume` re-ran the whole audit when nothing had moved. Builders polled
their own background work. `handoff.py agents` re-parsed a 51 MB transcript on every call. The <!-- PINNED 2026-11-14 -->
measurements and their scripts are recorded in the brief under `prompts/`.

## Expected improvements

- A spec defect `--dispatch` would refuse is refused before the spec commit.
- One spec or one build is graded by check 12 in seconds, not 376 s. <!-- PINNED 2026-11-14 -->
- A commit renders its own index instead of being refused on check 9.
- An idle-wake `--resume` tick hashes every brief in one git call, not one per brief.
- A role agent cannot poll; it waits on the notification.
- `handoff.py agents` reads only a transcript's appended bytes.

## Detriments if this is not built

- Every build keeps paying for re-dispatched units: about 30 h in the measured session.
- Spec writers keep spending 4-6 min per hygiene run, and commits keep costing 66-110 s.
- The main loop keeps blocking for 51 s per idle tick, and builders keep idling on `tail -f`. <!-- PINNED 2026-11-14 -->

## Build-level rules

- **No verdict moves.** Each unit's acceptance is one command timed before and after on node a,
  plus a fixture showing the same refusals, reds and greens. A speed-up that moves a verdict is out. The two owner-accepted moves are refusals: a role agent's polling wait (unit 6) and a suite whose only admitting word sits in a shell comment (unit 9).
- **Reuse the owner's predicates** ([one-fact]): a pre-check calls the driver's own reader, never a copy.
- **The full run and the bar keep grading everything**; only the caller-scoped paths narrow.
- **Re-verified at open, against main `846d51d39`**: R4 shrank to `--resume`, because a refused
  `--release-task` took 4.7 s, not 47 s. R5 shrank to the polling refusal and the `-eo pipefail` <!-- PINNED 2026-11-14 -->
  option gap, because G3 already refuses every plain suite launch the probe tried.
- No spec audit: the owner declined it at kickoff.
- Kit versions move once, after the last code move.

## Parked decisions

None.

<!-- roster:units -->

| # | Unit | Mechanism |
|---|---|---|
| 1 | `TOOL-aTrimmedWait-1` | R1: one pre-commit spec validation that runs `--dispatch`'s cheap refusals through the driver's own predicates, wired into the spec stage and the writer's instructions |
| 2 | `TOOL-aTrimmedWait-2` | R2: hygiene check 12 graded over one named spec or build, with the writer told to use it |
| 3 | `TOOL-aTrimmedWait-3` | R3: when check 9 refuses a commit, the pre-commit hook renders the moved index, stages it into the hook's index and grades again (`--write-staged`, opt-in by `STAGED_RENDER`) |
| 4 | `TOOL-aTrimmedWait-4` | R3: `gen_build_index.py --write` writes only the artifacts whose rendered bytes moved (owner, 2026-11-14) |
| 5 | `TOOL-aTrimmedWait-5` | R4: `--resume` and `--status` hash every brief in one `git hash-object --stdin-paths` call, every line byte-identical (owner, 2026-11-14) |
| 6 | `TOOL-aTrimmedWait-6` | R5: the scratch guard refuses a role agent's polling wait, and G3 reads past `-o pipefail` |
| 7 | `TOOL-aTrimmedWait-7` | R6: `handoff.py agents` caches parsed calls per transcript and parses only appended bytes |
| 8 | `TOOL-aTrimmedWait-8` | Closing-review repair, memory-tree: `--write-staged` declines before it writes or stages, its index and decline arms tested, the scoped hygiene fixture arms its edge cutoff, and the branch-guard leg names the hygiene producer (review M1 M3 M4 M5 M6 L1) |
| 9 | `TOOL-aTrimmedWait-9` | Closing-review repair, hooks and roles: the polling rows read no shell comment as a duration and are tested at the floor, and arm 23 tells a resumed read from a cold re-parse (review M2 L2 M7) |
| 10 | `TOOL-aTrimmedWait-10` | Close-bar repair: the commit-render switch moves from `.memory-tree.conf` to a policy catalogue key, and the fork sites the shell-hygiene leg names are converted (owner, 2026-11-15) |
| 11 | `TOOL-aTrimmedWait-11` | Close repair, inherited: the hygiene suite's partition arm stops reading check 26's cache-hit count, so a cold clone reads it green (owner, 2026-11-15) |
| 12 | `TOOL-aTrimmedWait-12` | Reconcile with local main at `5d48501da` before the landing merge: eight conflicts resolved, `derive_partition_lines` kept over main's `extract_hs_lines` (owner, 2026-11-16) |
| 13 | `TOOL-aTrimmedWait-13` | Close repair: the driver suite's parity table gains the `--check-specs` row unit 1 owed (owner, 2026-11-16) |
| 14 | `TOOL-aTrimmedWait-18` | Reconcile with local main at `8eda4a5a0` before the landing merge: five conflicts resolved, the summed floors restored where both sides read one number (owner, 2026-11-17) |
| 15 | `TOOL-aTrimmedWait-19` | Landing repair: the hygiene suite's partition helper takes back main's name `extract_hs_lines`, so the push's merge-loss check clears (owner, 2026-11-18) |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 15 unit(s) · node a · opened 2026-11-14 · streams tooling
ids TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 TOOL-aTrimmedWait-8 TOOL-aTrimmedWait-9 TOOL-aTrimmedWait-10 TOOL-aTrimmedWait-11 TOOL-aTrimmedWait-12 TOOL-aTrimmedWait-13 TOOL-aTrimmedWait-14
ids TOOL-aTrimmedWait-15 TOOL-aTrimmedWait-16 TOOL-aTrimmedWait-17 TOOL-aTrimmedWait-18 TOOL-aTrimmedWait-19

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aTrimmedWait-1 — `unattended.sh --check-specs` refuses, before the spec commit and through `--dispatch`'s own predicates, every spec defect `--dispatch` refuses from the spec files alone](spec/2026-11-14-spec-TOOL-aTrimmedWait-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aTrimmedWait-2 — hygiene check 12 grades one named spec or one build on request, and the spec writer is told to run it that way](spec/2026-11-14-spec-TOOL-aTrimmedWait-2.md) | 2 | 2 | CLOSED | rev-4 | 2026-11-14 |
| [TOOL-aTrimmedWait-3 — a commit refused on build-index drift renders its own index, stages it and is graded again](spec/2026-11-14-spec-TOOL-aTrimmedWait-3.md) | 3 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aTrimmedWait-4 — `gen_build_index.py --write` writes only the artifacts whose bytes moved](spec/2026-11-14-spec-TOOL-aTrimmedWait-4.md) | 4 | 2 | CLOSED | rev-3 | 2026-11-14 |
| [TOOL-aTrimmedWait-5 — the holder's idle-wake `--resume` stops paying one git process per briefed unit](spec/2026-11-14-spec-TOOL-aTrimmedWait-5.md) | 5 | 2 | CLOSED | rev-3 | 2026-11-14 |
| [TOOL-aTrimmedWait-6 — the role gate refuses a role agent's polling wait, and steps past an option cluster such as `-eo pipefail`](spec/2026-11-14-spec-TOOL-aTrimmedWait-6.md) | 6 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aTrimmedWait-7 — `handoff.py agents` keeps its parsed session calls per transcript and parses only the bytes appended since](spec/2026-11-14-spec-TOOL-aTrimmedWait-7.md) | 7 | 2 | CLOSED | rev-3 | 2026-11-14 |
| [TOOL-aTrimmedWait-8 — a declined staged render leaves the tree as it found it, and the paths the closing review found untested are armed](spec/2026-11-14-spec-TOOL-aTrimmedWait-8.md) | 8 | 2 | CLOSED | rev-2 | 2026-11-14 |
| [TOOL-aTrimmedWait-9 — closing-review repair, hooks and roles: the role gate reads no shell comment as words, the P3 rows are tested at the floor, and arm 23 tells a resumed read from a cold re-parse](spec/2026-11-14-spec-TOOL-aTrimmedWait-9.md) | 8 | 2 | CLOSED | rev-3 | 2026-11-15 |
| [TOOL-aTrimmedWait-10 — close-bar repair: the commit-render switch becomes the policy key `memory.staged-render`, and the fork sites the shell-hygiene leg names are converted](spec/2026-11-15-spec-TOOL-aTrimmedWait-10.md) | 9 | 2 | CLOSED | rev-2 | 2026-11-15 |
| [TOOL-aTrimmedWait-11 — close repair, inherited: the hygiene suite's partition arm sets aside check 26's cache-hit count](spec/2026-11-15-spec-TOOL-aTrimmedWait-11.md) | 10 | 2 | CLOSED | rev-5 | 2026-11-15 |
| [TOOL-aTrimmedWait-12 — the reconcile with local main at 5d48501da: its eight conflicts resolved so the landing merge is clean](spec/2026-11-16-spec-TOOL-aTrimmedWait-12.md) | 11 | 2 | CLOSED | rev-2 | 2026-11-16 |
| [TOOL-aTrimmedWait-13 — close repair: the driver suite's parity table gains the `--check-specs` row unit 1 owed](spec/2026-11-16-spec-TOOL-aTrimmedWait-13.md) | 12 | 1 | CLOSED | rev-1 | 2026-11-16 |
| [TOOL-aTrimmedWait-18 — the reconcile with local main at 8eda4a5a0: its five conflicts resolved and the coincident floor summed, so the landing merge is clean](spec/2026-11-17-spec-TOOL-aTrimmedWait-18.md) | 13 | 2 | CLOSED | rev-2 | 2026-11-17 |
| [TOOL-aTrimmedWait-19 — the hygiene suite's partition helper takes back main's name, so the landing's merge-loss check clears](spec/2026-11-18-spec-TOOL-aTrimmedWait-19.md) | 14 | 1 | CLOSED | rev-1 | 2026-11-18 |
<!-- /gen:build-units -->

Records: 75 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aTrimmedWait-1 TOOL-aTrimmedWait-2 TOOL-aTrimmedWait-3 TOOL-aTrimmedWait-4 TOOL-aTrimmedWait-5 TOOL-aTrimmedWait-6 TOOL-aTrimmedWait-7 TOOL-aTrimmedWait-8 TOOL-aTrimmedWait-9 TOOL-aTrimmedWait-10 TOOL-aTrimmedWait-11 TOOL-aTrimmedWait-12
TOOL-aTrimmedWait-13 TOOL-aTrimmedWait-18 TOOL-aTrimmedWait-19.

Ids whose spec moved past its audited revision: none — 0 of 15 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aTrimmedWait-1` | no |
| 2 | `TOOL-aTrimmedWait-2` | no |
| 3 | `TOOL-aTrimmedWait-3` | no |
| 4 | `TOOL-aTrimmedWait-4` | no |
| 5 | `TOOL-aTrimmedWait-5` | no |
| 6 | `TOOL-aTrimmedWait-6` | no |
| 7 | `TOOL-aTrimmedWait-7` | no |
| 8 | `TOOL-aTrimmedWait-8`, `TOOL-aTrimmedWait-9` | yes |
| 9 | `TOOL-aTrimmedWait-10` | no |
| 10 | `TOOL-aTrimmedWait-11` | no |
| 11 | `TOOL-aTrimmedWait-12` | no |
| 12 | `TOOL-aTrimmedWait-13` | no |
| 13 | `TOOL-aTrimmedWait-18` | no |
| 14 | `TOOL-aTrimmedWait-19` | no |

A step's `Parallel` yes means its units share an order; `doc.build-method#m6-passes-commits-parallelism` still sequences two of them whose write sets intersect at dispatch.
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-routes -->

| Purpose | Read |
|---|---|
| the units | the units table above |
| briefs | `2026-11-18-prompt-TOOL-aTrimmedWait-19-brief.md`, `2026-11-18-prompt-TOOL-aTrimmedWait-19-1-spec-writer.md` and 56 more under prompts/ |
| reviews | `2026-11-14-review-TOOL-aTrimmedWait-1-diff-review-round1.md` (CLEAN WITH FIXES) |
| logs | `2026-11-18-build-TOOL-aTrimmedWait-19-1-acceptance-ledger.md`, `2026-11-17-build-TOOL-aTrimmedWait-18-1-acceptance-ledger.md` and 14 more under build/ |
| open asks | `BACKLOG.md`, 4 open |
| card ref | `refs/gov/builds/aTrimmedWait/card` |
<!-- /gen:build-routes -->
