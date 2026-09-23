**Serves:** journal TOOL-aBatchedArm-2

# Build brief — TOOL-aBatchedArm-2, the structural group linter over the batched self-test

The spec is `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-2.md` at rev-2. Its
loop exited NON-CONVERGENT with disposition FOLD, so it is not re-reviewed: **build what it says.**
Its base `e9ed269b` predates the units that shaped the file it grades, so your FIRST act is a rev-3
§9 line bumping the base to `e8da0a54` and recording the facts below; every line number the spec
types is stale and every anchor is re-derived by TEXT.

## THE OWNER RULINGS, which bind this unit before the spec does

- 2026-09-13: build agents run NO self-test on every step — build first, verify once when the
  build is complete.
- 2026-09-14: land as it stands, and **run no gate until every unit of the build is built.**

This unit's product IS a static linter: a single pass over one text file, seconds, no subprocess
per group, no suite executed. Running it over the tracked suite and over scratch copies with a
planted violation is the same class as the static scans the previous units observed with, and it
is how AC1 through AC5 are observed — so RUN THE LINTER, and run its `.test.sh` sibling, which
is a handful of linter invocations over scratch copies. What you do NOT run: the suite it grades
(`check-unattended.test.sh`, in any mode or shard), the bar, `run-unattended-gates.sh`. AC6 (the
leg appears on the bar) is ledgered AMENDED — owed at the build's final gate pass by
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`.

## The facts the spec does not know (rev-3 records them)

1. **`emitted` exists and its grammar is fixed** (`TOOL-aBatchedArm-1`, CLOSED at rev-7):
   `emitted "<sig>|<sig>" "$out"` at `check-unattended.test.sh:93`, the `|`-separated
   interpolation-stripped signatures; and the SENTINEL `emitted "?" "$out"`, which the helper
   refuses by name, is what every one of the FOURTEEN converted groups carries until the build's
   final pass pastes the observed sets. Rule A reads the helper NAME of the arms (`miss`, `same`),
   never the set, so the sentinel is not rule A's business; but the linter's header says it saw
   `n` sentinels, because a file whose every group is unobserved is a fact the final pass reads.
2. **The delimiter call set at this base** is `reset_tree`, `anchor_break` (`:358`),
   `anchor_restore` (`:368`), `wreset` (`:431`), `seed_ros` (`:469`), `replay_landed_main` (`:520`),
   plus the eight `if in_shard k` seams and every `; reset_tree` mid-line. Resolve it FROM THE FILE
   (every function whose body calls `reset_tree`, transitively) and assert it non-empty; print the
   boundary count and the group count on every run, as S4 says.
3. **Fourteen groups, not nineteen**: the first pass's ledger
   (`build/2026-09-14-build-TOOL-aBatchedArm-1-2-acceptance-ledger.md`) has the ranges and the
   refusals. Rule A, B and C's starting figures over the tracked file are DERIVED by your first run
   and pasted, never typed — including any pre-existing rule-C hit on `_f1_clean=$(run)` (the
   equality baseline, a solo block), which is reported, never waived, exactly as §3 says.
4. **`check-arms.py`** (`tools/memory-tree/check-arms.py`) is the normaliser rev-2's rule A no
   longer needs; F1 resolves by deletion. Do not invoke it from the linter.

## Read these before the first edit, in this order

1. The spec, whole. §2 S1–S5 is the edit list, §4 the rules table and the delimiter, §6 the five
   static ACs you observe and the one you ledger.
2. `tools/unattended/check-unattended.test.sh`: `:62-64` (`hit`/`miss`/`same`), `:65-93` (the
   `emitted` header and helper), the six delimiter helpers above, one converted group (grep
   `emitted "?"` — fourteen hits — and read one whole, from its `reset_tree` to its last `hit`).
3. `tools/memory-tree/check-arms.py` — its `--selftest` shape and its gate-legs row are the
   pattern for yours: `tools/gate-legs.json`'s `check-arms selftest` row (`chunk: selftests`,
   `subject: kit`, `guard`, `ceiling`) and `tools/run-gates/selftest-budgets.txt:55` (its budget
   row: name, seconds, argv, reason).
4. `tools/unattended/check-pass-order.test.sh:29-31` — the fork-free `case` spelling of the three
   helpers, the shape for your `.test.sh`.

## The write set, declared before any edit

`tools/unattended/check-arms-groups.sh` (new) · `tools/unattended/check-arms-groups.test.sh`
(new) · `tools/gate-legs.json` (one row, `subject = kit`, `chunk = selftests`, a `guard` of
`tools/unattended/`, a `ceiling`) · `tools/run-gates/selftest-budgets.txt` (one row for the
`.test.sh`, its reading from your own timed run of it — seconds — with the condition named) ·
`tools/install-prefix-carried.txt` (a new kit file that names its own kit dir or a sibling by
literal needs a BAN row — derive `$HERE` instead and add none) · `tools/unattended/kit.toml` (the
`include` list at `:32` names the kit's test files — add yours, or the descriptor's population gate
reds) · `memory/builds/aBatchedArm/` (records). Declare all with `--dispatch` before the first
edit.

## Traps this repo has already recorded, so you do not pay for them again

- **A new gate is not landed until its failing case has been observed.** Each of rules A, B and C
  is staged as a planted violation in a scratch COPY of the suite and observed RED, then the copy
  discarded — that is AC1–AC3 and it is static.
- **The install-prefix leg is a BAN** on `tools/<kit>/` literals in kit files: derive your own
  directory and the suite's path (`$HERE/check-unattended.test.sh`); an empty derivation REFUSES.
- **Every `.sh` is verified at the BYTE level**; LF committed; no backslash escapes through
  heredocs; the Edit tool or binary-mode scripts only.
- **A declared population**: `tools/unattended/kit.toml:32` lists the kit's test files by name;
  `govkit selfcheck` reds a tracked kit file no rule names. Add yours.
- **`every held leg is budgeted, every budget row resolves`** is an unguarded bar leg: a new
  `chunk: selftests` row in `gate-legs.json` with no budget row reds it. Add both in one commit.
- **The liveness line is not optional**: a zero-group parse REFUSES with a non-zero exit (AC4),
  never a clean verdict.

## What done looks like

- rev-3 §9 line first; then the linter, its test, the two manifest rows and the descriptor line;
  one or two commits with the unit id in the subject.
- The ledger at `memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-2-1-acceptance-ledger.md`:
  AC1–AC5 OBSERVED with the linter's own output over the tracked file (group count, boundary
  count, sentinel count, the three starting figures) and over the three planted copies (each RED,
  naming rule, group and line); AC6 AMENDED naming the final-pass command.
- `bash tools/unattended/check-arms-groups.sh` exits 0 or 1 over the tracked suite — whichever the
  starting figures make it — and its header names what it does not grade; `bash
  tools/unattended/check-arms-groups.test.sh` GREEN with its floor declared.
- `bash tools/check-install-prefix.sh`, `bash tools/check-line-length.sh`, `python
  tools/memory-tree/gen_build_index.py --check-format` and the pre-commit hook green on each
  commit; the spec header CLOSED in the last one.
- `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` after each commit and acted on.

Do NOT run `check-unattended.test.sh` in any mode or shard, the bar, or `run-unattended-gates.sh`.
