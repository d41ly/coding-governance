**Serves:** journal TOOL-aBatchedArm-1

# Build brief — TOOL-aBatchedArm-1, batching the gate self-test's arms by tree state

The spec is `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-1.md` at rev-4. Its
loop exited at rev-3 NON-CONVERGENT with disposition FOLD, so it is not re-reviewed: **build what it
says.** But its base `e9ed269b` predates three units that changed the file it converts, so your FIRST
act is a rev-5 §9 line that bumps the base to `46b12b93` and records the four facts below; every
line number the spec types is stale and every anchor is re-derived by TEXT.

## THE OWNER RULINGS, which bind this unit before the spec does

- 2026-09-13: build agents run NO self-test on every step — build first, verify once when the
  build is complete.
- 2026-09-14: land as it stands, and **run no gate until every unit of the build is built.**

So this unit runs NO suite, NO shard, NO bar, NO `run-unattended-gates.sh`. You convert the file
and you do not run it. What you MAY run, because it executes no suite and costs seconds: `bash -n`
over the file; your own STATIC scans of the converted file (AC4 and AC7 are static scans by their
own wording — observe them with a script over the text and paste its output); `grep -c` counts;
the record gates the pre-commit hook runs on `git commit`. AC1, AC2, AC3, AC5 and AC6 need the suite
to run and are ledgered AMENDED — `- ACn — amended rev-5 — NOT OBSERVED under the 2026-09-14
ruling; owed at the build's final gate pass by `<the exact command>`` — naming the command. AC3 is
the safety property of this whole unit and it is the FIRST thing the final pass reads, so write its
amended line with the exact recipe: the `FAIL` set and the floor-graded `$n` of the unsharded run
at `46b12b93` (unit 3's ledger already holds them: 21 `FAIL` lines, count 555) against the same two
figures after conversion, `n` allowed to move by exactly the number of `emitted` calls you added,
which you paste beside it.

## The four facts the spec does not know (rev-5 records them)

1. **The file is EIGHT shards now** (`TOOL-aBatchedArm-3`, CLOSED): `if in_shard 1` at `:492`
   through `if in_shard 8` at `:2769`, 27 helpers hoisted to the prologue, `topo_capture <k>` at
   each region's first line and `replay_landed_main` at region 4's. A group NEVER spans a region
   seam (the spec's own edge), and the `topo_capture`/replay lines are not arms and are not
   grouped.
2. **The nine-arms block is a counted block** (`TOOL-aBatchedArm-3` S6): `MUT=0; MUT_EXPECTED=13`
   at `:1574`, every `reset_tree`-led cycle in it increments `MUT`, and the `same` at `:1657`
   asserts the count. Batching any arm in that block lowers the cycle count and reds the control.
   That block stays EXACTLY as it is — it is S3's "control without a witness" class — and the
   rev-5 line says so.
3. **The floors are set** (`FLOOR_ASSERTIONS=538` at `:3250`, `FLOOR_SHARD_1..8` beneath): your
   conversion adds one `emitted` assertion per group and removes none, so every count rises and
   every floor stays valid. S4's re-measure is NOT done here — it is owed at the final pass from
   that pass's counts — and the rev-5 line says so. Same for S5's budget rows.
4. **`reset_tree` now deletes two leaked heads in both stores** (`TOOL-aBatchedArm-3` S5,
   `:261`); one `reset_tree` per group is still the group's whole reset.

## Read these before the first edit, in this order

1. The spec, whole. §2 S1–S3 is the edit, §3's BINDING PRIOR is the rule you must not bend, §4's
   data model is the group shape, §6 AC4 and AC7 are the two static checks you observe.
2. `tools/unattended/check-unattended.test.sh`: `:62-64` (the three helpers — `emitted` is a
   fourth beside them, same counter, same failure idiom), `:261` (`reset_tree`), `:492` and every
   `if in_shard k` (the eight seams), `:553` (`_f1_clean=$(run)` — the baseline the equality arms
   read; the whole-run EQUALITY arms and this capture stay solo), `:1566-1658` (the counted block —
   untouched), the sites that run with `GOV_UNATTENDED_REPORT=1` (`:1917-1995`, `:2917-3163` — the
   skip-line detector in `emitted` must not be fooled by arms that ASSERT skip lines; those arms
   stay solo).
3. `tools/unattended/check-unattended.sh`: `:93` (`fail()` — the SOLE emitter of
   `UNATTENDED check N FAILED — <text>`; the interpolation-stripped `<text>` is the signature
   `emitted` keys on), `:761` (`report()` — every skip line, gated on `GOV_UNATTENDED_REPORT`), the
   three check-1 `exit` sites (find them by text under check 1 — the spec's `:114`, `:198`, `:385`
   are stale) — the arms that reach them stay solo.
4. `tools/memory-tree/check-arms.py` — its signature normaliser is the one `emitted` must agree
   with (first-interpolation truncation: the `arm-literal-strands-on-message-edit` class). Reuse
   its rule; do not invent a second normaliser.

## The write set, declared before any edit

`tools/unattended/check-unattended.test.sh` · `memory/builds/aBatchedArm/` (records). NOT
`selftest-budgets.txt` (S5 is owed at the final pass), NOT the floors. Declare with `--dispatch`
before the first edit.

## How to convert without running

- **Classify first, convert second.** Write a scratch script that walks the file's arms between
  `reset_tree`-led boundaries — the delimiter is the CALL SET, `reset_tree` and every helper that
  calls it (`anchor_break`, `anchor_restore`, `seed_ros`, `wreset`, `replay_landed_main`), plus the
  eight seams — and tags each block: SOLO (any `miss`, any `same`, any exit-code-only or
  empty-output assertion, any anchor/PATH-stub/remote-rewriting arm, any equality arm, the counted
  block, any `GOV_UNATTENDED_REPORT=1` arm) or BATCHABLE (only `hit`s against one `$(run)`). Paste
  the classification counts in the ledger; that is F1's "measured distribution".
- **A group is contiguous BATCHABLE blocks inside one region whose breaks do not touch the same
  file or ref.** Two arms carrying one assertion text never share a group (rule B of the linter
  unit 2 will grade). Start with groups of at most FIVE blocks; the spec's F1 says widen until it
  reds, and you cannot observe a red, so five is the size and the rev-5 line says why.
- **Every existing `hit` line stays BYTE-IDENTICAL.** The conversion changes only the lines around
  them: one `reset_tree`, the mutations in sequence, one `out=$(run)`, one `emitted "<sig> <sig>"
  "$out"`, then the untouched `hit "$out" …` lines. This is what keeps AC3's equivalence readable
  as a diff, and what the spec's §4 rejected the table rewrite to preserve.
- **`emitted`'s expected set is DERIVED from the arms, not typed by hand**: for each group, the
  signature is the `fail N "…"` text the arm's `hit` literal matches, resolved through the
  `check-arms.py` normaliser; an arm whose literal resolves to no signature makes its block SOLO,
  never a guess.
- **`check-arms.py --check` reads this file by line and skips comments; the armed-branch pin must
  not move.** Run it (seconds, static) after the conversion and before the commit.

## Traps this repo has already recorded, so you do not pay for them again

- **Every `.sh` edit is verified at the BYTE level.** `core.autocrlf=true` here; trust
  `git cat-file -p <oid>`. Edit with the Edit tool or a BINARY-mode script, never a Python `open()`
  in text mode — that eats the bare CRs four of this file's awk regexes depend on. Never pass a
  backslash escape through a bash heredoc.
- **The install-prefix leg is a BAN.** This file is pinned at 3 carried literals; add none.
- **`TOOL-dScriptedRepeat-15` S3 is ratified and flat**: no `miss`, no `same`, ever, in a group.
  128 assertions stay solo and the spec says the unit alone lands at 40 to 44 minutes; that is the
  design, not a failure.
- **`--only 28` is broken** (`TOOL-aHoistedPass-37`) and is not yours.

## What done looks like

- rev-5 §9 line first, then the conversion in tranches of one region each, each tranche a commit
  with the unit id in its subject (eight regions, so up to eight commits; a region with nothing
  batchable is stated, not committed).
- AC4 and AC7 observed by your static scan over the final file, the scan's output pasted in the
  ledger at `memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-1-1-acceptance-ledger.md`;
  AC1, AC2, AC3, AC5, AC6 ledgered AMENDED with their final-pass commands.
- The ledger carries: the classification counts, the group count and size distribution, the
  number of `emitted` calls added (AC3's allowed `n` delta), the invocation count before and after
  (`grep -c '\$(run)'` — 285 at BASE, paste both).
- `bash -n` clean; `python tools/memory-tree/check-arms.py --check` green; install-prefix and
  line-length green; the spec header CLOSED in the last commit.
- `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` run after each commit and acted on.

Do NOT run the suite in any mode, any shard, the bar, or `run-unattended-gates.sh`. The unit's
observation is the build's final pass and nothing else is owed now.
