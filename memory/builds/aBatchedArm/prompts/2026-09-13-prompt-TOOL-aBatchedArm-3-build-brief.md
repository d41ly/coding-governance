**Serves:** journal TOOL-aBatchedArm-3

# Build brief — TOOL-aBatchedArm-3, the gate self-test graded as eight declared shards

The spec is `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-3.md` at rev-7. It
survived five adversarial audit rounds and its loop exited NON-CONVERGENT with disposition FOLD, so
it is not re-reviewed: **build what it says**, and where it names a line number, that line is the
edit. Every anchor below was re-read against the tree at `205a58e0`, whose `tools/` is byte-identical
to the spec's BASE `0422ea2e` (`git diff --stat 0422ea2e HEAD -- tools/` is empty). This brief carries
what a builder oriented in the spec alone would still have to re-derive, and the order that keeps
the expensive runs from being paid twice.

## The one sentence

`tools/unattended/check-unattended.test.sh` goes from two shards to eight, cut only at
`reset_tree`-led block edges, with every cross-shard helper hoisted, every boundary's topology
replayed, the one accumulation control instrumented, and the two leaked heads deleted on reset —
then the split is MEASURED on this host against a two-shard reading, and the ratio decides the arity.
No arm's verdict changes. The suite is RED at BASE and stays RED; that is not yours.

## Read these before the first edit, in this order

1. The spec, whole. §2 is the edit list, §4 Rollout is the commit order, §6 is what proves it.
2. `tools/unattended/check-unattended.test.sh`: `:29` (`SHARD_ARITY=2`), `:44-52` (the shard
   parser and `in_shard`), `:57-59` (`hit`/`miss`/`same` — each is one `n` increment), `:177-189`
   (the bare origin, `ORIGIN`, `ANCHOR0`; the FRESH head set is `main` on origin, `main` and `unit`
   locally), `:240-246` (`reset_tree`: its `update-ref --stdin` runs on the CLONE, not the origin),
   `:268-298` (the already-hoisted helpers, `anchor_break`/`anchor_restore`), `:299` (`if in_shard 1`),
   `:1238-1245` (the `ahead` push — leak one, origin side), `:1276-1293` (the seam, and the `SH_I = 2`
   replay you generalise), `:1404-1513` (the nine-arms block and its `still clean after nine
   mutations` control), `:3045-3047` (`trunk` — leak two, created LOCALLY then pushed), `:3145`
   (`FLOOR_ASSERTIONS=392`), `:3161-3168` (the floor case and the grade), `:3169-3175` (the
   whole-suite note S4 retargets), `:3186` (the C21 pair, AFTER the grade), `:3227-3229` (the
   trailer and the PASS line — AC4's completion witness).
3. `tools/run-gates/run-selftests.sh`: `:97,:116` (`--kit` is a SUBSTRING filter on argv, so
   `--kit tools/unattended/check-unattended.test.sh` selects the eight rows), `:370-378` (the row
   checker; `^[0-9]+/[0-9]+$` already admits `1/8`), `:308-330` (width: node a is profile `capable`,
   width 8, so `--pooled` gives outer 8), `:454-503` (`sweep-ceiling-factor` and `SWEEP_WALL`).
4. `tools/run-gates/selftest-budgets.txt:114` — the one row you replace with eight; columns are
   TAB-separated `name · budget · argv · reason`.
5. `tools/run-gates/run-gates.gov.test.sh:365-395` — the shard-contract predicate you PORT (the
   forward half only: one arity per script, indices `1..n` complete). Its REVERSE half — "declares
   `SHARD_ARITY` but is called whole" — is exactly what would red `unattended.test.sh`, and AC5
   forbids that: scope the port to scripts a budget row calls WITH `--shard`.
6. `tools/unattended/run-unattended-gates.sh:175-176` — the `run UNSHARDED on purpose` note.

## The write set, declared before any edit

`tools/unattended/check-unattended.test.sh` · `tools/run-gates/selftest-budgets.txt` ·
`tools/install-prefix-carried.txt` · `tools/run-gates/run-selftests.sh` ·
`tools/run-gates/run-selftests.test.sh` · `tools/unattended/run-unattended-gates.sh` ·
`memory/builds/aBatchedArm/` (records). Declare all seven with `--dispatch` before the first edit;
if building uncovers an eighth, re-declare WIDER before the commit, never narrower.

## OWNER RULING 2026-09-13 — no self-test runs during the build; ONE verification pass at the end

The first pass of this unit was stopped after three hours with ten suites running concurrently on a
box that was also carrying this session's own orphaned A/B runs; every timed reading it took was NO
READING by its own ledger, and its untimed runs were still going. The owner ruled: **the build
agents do not run self-tests on every step. Build everything first, then run the verification
once, when the build is complete.** This supersedes the spec's §4 Rollout where that section grades
each commit by a suite run — AC12's "own commit, graded alone" is satisfied by the final pass's
unsharded `FAIL` set at HEAD equalling the one at BASE, since an unsharded run executes every arm
whatever the arity; if that equality fails, bisect THEN, not before. Write a rev-8 §9 line recording
the ruling and this reading of AC12.

**Where the tree stands.** Commit one (`94a6b677`, the leak delete) and a CHECKPOINT (`cbf8ebce`)
are on the branch. The checkpoint carries the stopped pass's edits UNVERIFIED: `SHARD_ARITY=8` cut
at `reset_tree`-led edges, 27 helpers hoisted (derived, the spec's 28 counted a string inside a
loop), `topo_capture` at every boundary with `replay_landed_main` at the boundary whose unsharded
capture carries `unit<main`, the `MUT`/`MUT_EXPECTED` counter (13 cycles, block-declared), eight
placeholder floors of `1`, the shard join in `run-selftests.sh --check` with two arms in its test,
and both whole-suite notes retargeted. Its acceptance ledger at
`memory/builds/aBatchedArm/build/2026-09-13-build-TOOL-aBatchedArm-3-1-acceptance-ledger.md` holds
AC5 and AC12's head-set half already observed, and the trace-based per-line cost method it used.
Read the checkpoint's diff (`git show cbf8ebce --stat`, then the suite file's diff against
`94a6b677`) before editing: it is yours to keep, correct or redo, and nothing in it has been graded.

**Phase A — finish every edit, run nothing.** What is left: the eight budget rows (S2) with a
PLACEHOLDER budget equal to the old row's, the `install-prefix-carried.txt` count raised by hand
with its fourth-column reason, any `--check`-visible defect in the join, and the `--check` and
`--list` gates themselves (those are seconds, not suites, and are not what the ruling forbids).
Commit as `TOOL-aBatchedArm-3 S1-S6: …`. The floors and the budgets stay placeholders until Phase B
has readings; they are re-set in the closing commit.

**Phase B — ONE verification pass, on an idle box.** Before it starts: `ps -ef` for any
`check-unattended`, `run-selftests`, `run-gates` or `unattended.test` process; if any exists, it is
an orphan of a dead turn or another session's run — record it, and do not start until the box is
clear (kill only what `ps` shows descends from a dead ancestor; never another session's). Every run
goes on a frozen `git clone --local` under a SHORT `$TEMP` path, stdout to a file, started with
`run_in_background` and awaited through the completion notification — no sleep loops, no `tail`.
The runs, in this order, each SERIAL with respect to the others unless stated:

1. On a clone at BASE `0422ea2e`: the unsharded run (AC12's baseline `FAIL` set and AC6's
   pre-split floor-graded count), then the two-shard reading as two CONCURRENT direct invocations
   `--shard 1/2` and `--shard 2/2` stamped with `date +%s` (AC4 arm one). A reading exists only if
   its output carries the trailer `(this leg ran shard k/2 only …)`.
2. On a clone at HEAD (the Phase A commit): the eight shards through
   `bash tools/run-gates/run-selftests.sh --serial --kit tools/unattended/check-unattended.test.sh`
   — one pass, eight rows one after another. It yields the eight serial walls (S2's budgets), the
   eight floor-graded counts (AC1, S3's floors) and the eight `FAIL` sets (AC6). Then the
   unsharded run at HEAD: the ninth count, the unsharded `FAIL` set (AC6, and AC12 against run 1).
   With `CHECK_UNATTENDED_TOPO=1` (the checkpoint's env gate, `:467`) set on BOTH the unsharded
   run and the eight, the captures are AC8's; the same outputs, no extra run.
3. The staged breaks, batched into ONE concurrent batch of shard runs on a scratch copy: a mis-cut
   region (AC2), a removed replay (AC8), the separated control (AC9), one un-hoisted helper (AC10),
   a block stranded past an `exit` (AC11) — five breaks staged in five DIFFERENT shard indices of
   one copy, the five shards run concurrently, each observed RED for its own reason, then the copy
   discarded. One batch, not five runs.
4. `bash tools/run-gates/run-selftests.sh --pooled --kit tools/unattended/check-unattended.test.sh`
   on a fresh clone at HEAD with the box otherwise idle (AC4 arm two). The
   `SWEEP of 8 suite(s), width 8 (outer 8, inner 1)` line is the fixture assertion; the eight walls
   from the runner's rows; then max, mean, the 20-minute verdict, and max(eight) / longest(two).
5. `bash tools/run-gates/run-selftests.test.sh` once, and `--check` and `--list` on the real tree
   (AC3, AC5, AC7).

If the balance is outside the tolerance you DECLARE before run 2 (`max(shard)` against `sum / 8`),
re-cut using the per-line costs the checkpoint's trace method gives you and re-run ONLY run 2's
eight rows — that is the one permitted repeat, and it is recorded as a candidate beside the chosen.

**Phase C — the closing commit.** Floors from run 2's counts within ~3 % headroom, budgets from
run 2's walls, the arity decision from run 4 (at or above 0.5 the arity is LOWERED with both
readings beside it, a further re-cut commit, and run 2 and run 4 taken again for the new arity —
the ruling's one-pass rule yields to F2's fallback, which is the spec's own repeat), every reading
in the ledger with its witness, the spec header CLOSED with the rev-8 line.

## Traps this repo has already recorded, so you do not pay for them again

- **Every `.sh` edit is verified at the BYTE level.** `core.autocrlf=true` here: the working copy is
  CRLF, committed bytes are LF, `git show rev:path` smudges. Trust `git cat-file -p <oid>`. Edit
  with the Edit tool, never with a Python `open()` in text mode — that eats the bare CRs four of
  this file's awk regexes depend on. Never pass a backslash escape through a bash heredoc.
- **`check-arms.py` reads this file by LINE and skips comments.** Region bodies are deliberately NOT
  reindented so every arm signature stays byte-identical; keep it that way when you wrap a region.
- **The install-prefix leg is a BAN in both directions.** `selftest-budgets.txt` is pinned at 14
  carried literals (`tools/install-prefix-carried.txt:111`); eight rows replacing one makes 21, and
  S2 says raise it BY HAND with a fourth-column reason in the same commit. `check-unattended.test.sh`
  itself is pinned at 3 — hoisting and re-cutting must add no path literal. Run
  `bash tools/check-install-prefix.sh` before every commit.
- **The floor-graded count EXCLUDES the C21 pair.** `PROLOGUE_ARMS` is 0 for that figure and the
  comment at `:3153` is TRUE — rev-3 said to correct it and was wrong. Every `FLOOR_SHARD_i` is
  measured from `$n` at the grade, discounted ~3 %, both figures beside the constant. The existing
  note says the two floors summing to `FLOOR_ASSERTIONS` is a COINCIDENCE, not an invariant; do not
  assert it for eight either.
- **`--only 28` is broken** (`TOOL-aHoistedPass-37`) and is not yours. The suite's pre-existing red
  (`TOOL-aQuenchedHarness-9`, `TOOL-aHoistedPass-38`) is not yours. AC6 compares `FAIL` sets, not
  exit codes, for exactly that reason.
- **A skip must announce itself.** AC4's `O < 8` branch and AC8's empty-set branch both SKIP by
  name; a skip that looks like a pass is the class §7 bans.
- **Orphaned processes contaminate the next timing.** After every background run finishes, check
  for stragglers (`python tools/process-monitor/reap.py --sweep` exists) before the next timed one.

## What done looks like

- Every AC in §6 observed, each with the command that observed it in the acceptance ledger at
  `memory/builds/aBatchedArm/build/2026-09-13-build-TOOL-aBatchedArm-3-1-acceptance-ledger.md`,
  shaped like unit 4's ledger beside it. AC4's ten readings each carry their trailer witness or the
  words NO READING. The two ratios and the arity decision are written there, whichever way they fell.
- `bash tools/run-gates/run-selftests.sh --check` GREEN with the eight rows and the ported join.
- `bash tools/run-gates/run-selftests.sh --kit tools/unattended/check-unattended.test.sh --list`
  names exactly eight rows.
- `bash tools/run-gates/run-selftests.test.sh` GREEN with the join arm and its floor moved.
- `bash tools/run-gates/run-gates.gov.test.sh` still GREEN (its shard-contract half reads
  `gate-legs.json`, which you do not touch).
- The install-prefix, memory-hygiene and line-length gates green on each staged diff.
- Two commits after the checkpoint — Phase A and Phase C — a third if F2's fallback fires, each
  with the unit id in its subject; the spec's status header set to CLOSED in the last one, with the
  rev-8 §9 line recording the owner ruling and anything else that diverged from rev-7.
- `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` run after each commit and acted on.

Do NOT run `run-unattended-gates.sh` in any mode, the driver suite `unattended.test.sh`, or the
bar's full self-test population as verification, and do NOT run any suite before Phase B; the
unit's measurement is Phase B and nothing else is owed.
