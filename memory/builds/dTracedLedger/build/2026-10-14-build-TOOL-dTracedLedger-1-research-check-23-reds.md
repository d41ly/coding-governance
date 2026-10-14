# Check 23 at origin/main ebce889c7 — reproduction, bisect, attribution and owners

**Serves:** research TOOL-dTracedLedger-1

The finding came from session 1799cb98 (build dClosedLoop, instrument 4): `memory hygiene` exits 1
at origin/main `ebce889c7` on two check-23 failures. This record reproduces it, finds why the merge
bar did not stop it, and names who owns each row. Node `d`, 2026-10-14. Every command ran in a
detached worktree at `%TEMP%/c23`, never in the primary tree.

## Reproduction

`bash tools/memory-tree/check-memory-hygiene.sh` at `ebce889c7` exits 1 with two check-23 lines:
8 rows in neither legal form and 30 that share no token with their criterion, 37 distinct because
aSparedSpawn unit 11 AC10 is in both. The same run prints check 17, the stale
`memory/gotchas/INDEX.md`, which dRedressedBar's unit 7 already owns.

The first run was starved: commit charge stood at 34.3 of 36.5 GB, Cygwin forks failed with
`child_copy` and check 26 reported `WinError 1455`. That run omitted check 17's line silently and
still exited 1. A clean re-run printed check 17, and its check-23 set was byte-identical.

## Bisect, first parent from 6081d92e4

| Commit | Check 23 | Landing |
|---|---|---|
| `6081d92e4` | green | aOrientedCast's build onto node a's local main |
| `190cbc2dd` | 36 rows | aSparedSpawn onto local main, "the run stays HELD, unpushed" |
| `53b258844` | 36 rows | aHeardState, "the bar was skipped by the owner's order" |
| `106bf6e92` | 36 rows | aSweptBar |
| `39ed3d035` | 37 rows | aOrientedCast's addenda; adds aOrientedCast unit 22 AC7 |
| `cf7c64519` | 37 rows | the aOrientedCast hand-off record |
| `ebce889c7` | 37 rows | origin/main 2a9d8191 merged in, then pushed |

## Why the bar did not stop it

- Not a guard: `memory hygiene` in `tools/gate-legs.json` has no `guard`, so a scoped bar runs it.
- Not a scoped push: `.githooks/pre-push --decide` for the tip over `2a9d8191` answers `full`.
- Not the inherited-red landing: at `2a9d8191` the leg is green and `--offenders` prints nothing.
  At the tip it prints three keys, all new, so every red is OWN by signature. `GATE_ATTRIBUTE` on
  the one leg also reads OWN, through KF3, because the diff edits `run-gates.sh`.
- The bar was bypassed. aSparedSpawn's hold reason says the owner deferred the gates until "the
  fully reconciled tree", and aOrientedCast's says "The owner ordered a push with the bar
  bypassed". `ebce889c7` was pushed from node `a`. This node's `.git/runlog/pushes.log` has no line
  for it, so the push's own record is on node `a` and was not read.
- The first full bar after the push did see it: node `d`, 2026-10-13 19:11, worktree
  `gov-bar-profile-failures-b80cc3`. Its `memory_hygiene.log` carries the two check-23 lines and
  no check 17. dRedressedBar's red table traces that leg to check 17 alone, so check 23 is
  untraced there.

## Owners

Both builds are live. aSparedSpawn's `RUN.md` reads `phase: HELD`, held from VERIFYING until the
owner, and its remote claim `refs/gov/runs/aSparedSpawn` is `held` by node `a`. aOrientedCast's
`RUN.md` is HELD until the owner too. Their ledger lines are not edited here. Each owner gets one
ask, filed in this build's `BACKLOG.md` with a pointer to the owner's folder: the backlog grammar
admits an ask only in its own slug's folder, and the generator refused the first attempt to file
them in the owners' folders with verdict `V1`.

## The rows, classed

| Class | Rows | Remedy |
|---|---|---|
| a backticked token wrapped across a line break | aSparedSpawn 10 AC9, 8 AC6, 8 AC10 | rewrap |
| every token on a continuation line | aSparedSpawn 6 AC8, 32 AC12 | rewrap |
| no observation: `not run`, `OWED at VERIFYING` | aSparedSpawn 6 AC6, 11 AC10, 13 AC11 | observe, or amend |
| answer names its instrument, not the criterion's token | 26 aSparedSpawn rows | owner, per row |
| answer ran a variant of the criterion's command | aSparedSpawn 32 AC1, 34 AC1 | observe, or amend |
| a token beside the words "owed … not observable" | aOrientedCast 22 AC7 | observe, or amend |

32 AC1's answer diffs to `6e8f8b1da` where its criterion names `37200355d`, so it observed a
different range. 34 AC1 differs from its criterion only by `-U0`. aOrientedCast 22 AC7 is the
sharpest: `PreToolUse` satisfies the form arm, and the text says nothing was observed.

## Observations not filed

- A fork-starved run dropped check 17's line with no notice while check 26 announced itself. One
  observation, mechanism unproven.
- The token arm joins by containment, so a one-letter token such as node `a` joins nearly any
  criterion that also carries one; aSparedSpawn 13 AC11 shares only `a` with its criterion.

## Instruments

```
bash tools/memory-tree/check-memory-hygiene.sh                # at each bisect commit
bash tools/memory-tree/check-memory-hygiene.sh --offenders    # at ebce889c7 and at 2a9d8191
bash .githooks/pre-push --decide ebce889c7d71… 2a9d8191da18… origin
GATE_REGEN_CHECK=0 GATE_LEGS=<memory hygiene alone> GATE_ATTRIBUTE=2a9d8191… \
  bash tools/run-gates/run-gates.sh
python -I memory/builds/dTracedLedger/build/2026-10-14-build-TOOL-dTracedLedger-1-pairs.py . <row>…
```

`GATE_REGEN_CHECK=0` was set only so the probe would reach the leg past the stale INDEX. The pairs
instrument mirrors check 23's two extractors and prints each row's criterion tokens beside its
answer's. It joins tokens per bullet where the gate's form arm reads the first line only, so it
classes and does not grade.
