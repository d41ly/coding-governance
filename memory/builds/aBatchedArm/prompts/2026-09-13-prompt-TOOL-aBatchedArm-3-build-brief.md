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

## The order, because six of the runs cost twenty minutes to two hours each

Every long run goes on a FROZEN clone — `git clone --local` into a SHORT path under `$TEMP`
(a clone into the scratchpad hits MAX_PATH) — with its stdout redirected to a file. Never read a
result through `tail`; grep the file. The Bash tool's ceiling is ten minutes, so start each long
run with `run_in_background` and wait for its completion notification; do not poll it with sleep
loops, which spawn and contaminate the timing. Before each TIMED run, `ps` the box for another
`run-gates`/`run-selftests`/`check-unattended` and record the answer; a timing taken beside another
bar is NO READING.

1. **AC4 arm one, at BASE, first.** On the frozen clone, two concurrent direct invocations
   `bash tools/unattended/check-unattended.test.sh --shard 1/2` and `--shard 2/2`, each wrapped in
   `date +%s` before and after, each captured to its own file. A reading exists only if its file
   carries the trailer `(this leg ran shard k/2 only …)`; a red-but-complete run prints NO `PASS`
   and NO `FAIL executed`, so neither is the witness. Record both walls and the longest.
2. **The unsharded run at BASE**, same clone, captured whole: it yields AC12's baseline `FAIL` set
   and AC6's pre-split floor-graded count (`$n` as the floor grade reads it — the PASS line, if any,
   is 2 higher). It is not a timing, so it may overlap your editing, but not step 1 or step 8.
3. **Commit one — the leak delete alone** (S5's `reset_tree` change, AC12). Derive the leaked set
   from BOTH stores, delete the origin half through ONE extra spawn
   `git --git-dir="$ORIGIN" update-ref --stdin` and the local half through the clone-side batch
   that already exists. Then the unsharded run again on a fresh frozen clone at that commit: its
   `FAIL` set must be byte-identical to step 2's, and `git ls-remote --heads "$ORIGIN"` plus
   `git for-each-ref refs/heads` after a reset must show the fresh set. Both facts in the ledger.
4. **Commit two — S1, S3, the replays and S6 together.** The cut, the hoist (derive the population:
   every `name() {` between `:299` and the floor line; write the count into the HOIST SET note from
   that derivation), eight floors, the per-boundary topology capture and replay, and the `MUT`
   counter. The capture is ENV-GATED and inert by default — it must add no assertion and change no
   verdict; set the variable only for the AC8 runs. Expect the derived leaked set to be EMPTY at
   every boundary once commit one is in: seven skip lines naming the boundary is then the correct
   AC8 record, and the ANCESTRY half of the capture (`git merge-base --is-ancestor unit main` and
   whatever else a later arm depends on) is where the replays are actually owed. Do not manufacture
   a plant to make a negative non-vacuous.
5. **The staged breaks**, each against ONE shard run, each observed RED then unstaged: a mis-cut
   region (AC2), a removed replay (AC8), the separated control (AC9), one un-hoisted helper (AC10),
   a block stranded past an `exit` (AC11).
6. **The serial readings, and the re-balance.** The rows need readings and the `--serial` pass
   needs rows, so stage the eight rows with the OLD row's budget as a placeholder, run
   `bash tools/run-gates/run-selftests.sh --serial --kit tools/unattended/check-unattended.test.sh`
   on a frozen clone of the staged tree, and read the eight walls from the runner's own rows. Those
   same eight outputs are AC1's eight floor-graded counts and AC6's eight `FAIL` sets; ONE unsharded
   run at the same tree gives the ninth count and the unsharded `FAIL` set. If `max(shard)` is
   outside your DECLARED tolerance of `sum / 8`, move whole `reset_tree`-led blocks across the
   nearest boundary and take one more serial pass; every candidate's readings go in the ledger
   beside the one chosen. Each iteration costs a whole serial pass, so declare the tolerance before
   the first reading and stop when it holds.
7. **Commit three — S2 and S4**: the eight rows with their serial readings as budgets,
   the `install-prefix-carried.txt` count raised by hand with a fourth-column reason naming the eight
   literals, the ported join inside `run-selftests.sh --check`, its new arm in
   `run-selftests.test.sh` (a deleted shard row reds naming the index; `unattended.test.sh` does not
   red), and the two whole-suite notes retargeted.
8. **AC4 arm two, at HEAD, on a fresh frozen clone, no other bar on the box:**
   `bash tools/run-gates/run-selftests.sh --pooled --kit tools/unattended/check-unattended.test.sh`,
   captured whole. The `SWEEP of 8 suite(s), width 8 (outer 8, inner 1)` line is the fixture
   assertion; the eight walls come from the runner's own rows, each a reading only if that row's
   output carries its trailer. Then compute: max, mean, the 20-minute verdict, and the ratio
   max(eight) / longest(two-shard). At or above 0.5 the arity is LOWERED with both readings beside
   it — that is F2's fallback and it is a finding, not a failure — and the lowering is a further
   commit that re-cuts, re-floors and re-rows, not a note.

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
- Three commits in the Rollout's order, a fourth if F2's fallback fires, each with the unit id in
  its subject; the spec's status header set to CLOSED in the last one, with a rev-8 §9 line if
  anything diverged from rev-7.
- `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` run after each commit and acted on.

Do NOT run `run-unattended-gates.sh` in any mode, the driver suite `unattended.test.sh`, or the
bar's full self-test population as verification; the unit's measurement is the runs above and nothing
else is owed.
