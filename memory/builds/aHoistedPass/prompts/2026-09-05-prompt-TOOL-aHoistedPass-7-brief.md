**Serves:** journal TOOL-aHoistedPass-7

# Brief — TOOL-aHoistedPass-7, a brief on disk before the code that cites it

*The last unit of `aHoistedPass`. Read this, then read the spec whole. The spec is the design; this
says what the spec cannot — what the run around you already decided, and where this unit's own
history has been wrong twice.*

## The one thing to get right, because this spec has been wrong about it twice

**S2 lifts `_find_build_commit` out of `tools/unattended/check-pass-order.sh` into
`tools/unattended/lib-unattended.sh`, and the lift is REAL work, not bookkeeping.**

rev-3 of this spec resolved fork F2 as MOOT, on the ground that the extraction had already landed —
`_find_build_commit` is right there at `check-pass-order.sh:337` with call sites at `:378` and `:395`.
That resolution was wrong, and round 1's audit found why: **that file has no top-level function
definitions at all.** `_find_build_commit` and `_report` are both INDENTED inside an enclosing block,
so neither exists until the block runs, and no sibling script can source the file and call them. The
symbol had landed; the seam had not. A grep for the name cannot see the difference.

rev-4 re-opened F2 and took the lift. rev-5 then folded round 2's BLOCKER: every
`check-pass-order.sh:<span>` this spec built on was a `c4fcf5ad` address naming unrelated code at
BASE — `:172-215`, described as the build-commit selection, is the waiver-registry prose and the
`PREANCHOR_CAP` range validation at BASE, so a literal reading would have shipped an exemption
registry inside a pass-order leg. Every address is now re-cited BY NAME. **Trust the names, re-open
them at BASE before you cut, and if a third caller has appeared since, S3 says to re-derive S2 rather
than lift blind.**

**AC14 is the criterion that proves the lift rather than the symbol**: source `lib-unattended.sh` from
a scratch script and invoke `build_commit` with its five arguments. The same test against the old
nested definition FAILS at BASE, which is exactly the fact rev-3 missed.

## What verification is owed, and what is not

- **Do not run the full bar.** M6 charges a build pass the DIFF-SCOPED gates for what it touched; the
  full bar runs ONCE, at the push boundary, and the parent run owns that.
- **S3 touches a GREEN merge-bar leg whose own suite is on no bar.** That is this unit's real blast
  radius and it was priced in F2's option (b). So: take a BEFORE reading first —
  `bash tools/unattended/check-pass-order.sh` on the live tree, capturing the four liveness counts —
  then do the lift, then re-run and assert the counts are byte-identical. A post-only reading proves
  nothing about a move. AC7 is written that way on purpose.
- **Hand-run both suites and report their exit codes**:
  `bash tools/unattended/check-pass-order.test.sh` (the regression check for S3, which must stay green
  without an edit to a single arm) and your own `tools/unattended/check-brief-recorded.test.sh`.
  Nothing standing re-checks either.
- **`python3 tools/memory-tree/check-arms.py --check`** must exit 0. A new leg means new `fail`
  branches, and a stranded arm is silent.

## The bounds

- **Declare the write set first**: `--dispatch aHoistedPass --pass TOOL-aHoistedPass-7 --writes <path>`,
  one `--writes` per path. Widen before the commit; narrowing is refused.
- **S8's bump half IS SPENT** — `DEPL-aHoistedPass-1` took `unattended` 1.17 to 1.18 at order 2. What
  survives is real and easy to miss: your NEW script is a new carrier, so it must carry
  `KIT_UNATTENDED_VERSION` and a same-line `gov:kit unattended@` marker at that same value, AND join
  the script list at `check-kit-versions.sh:169`. The loop reds without it.
- **This unit is NOT an owner turn.** rev-4 re-derived that from the carriers it edits, none on ruling
  D1's veto-2 list. Do not reintroduce the bump-derived classification.
- **F1 is resolved at option (a): date `BRIEF_RECORDED_CUTOFF` at the landing and accept `graded 0`.**
  The day-one population is empty and the evidential weight sits in the staged-break arms observed
  RED before the leg lands. Do not back-date it and do not invent a waiver registry — an exemption is
  not coverage.
- **A leg that cannot move must SAY so.** S6's `DEAD PROBE` grammar assertion is the liveness half:
  when the driver no longer spells the row shape the leg matches, it refuses rather than reporting a
  reassuring zero. Exercise that branch; a probe you have only ever seen pass is an assertion about
  nothing.
- **Flip the spec status header to `CLOSED` in the SAME COMMIT as the code**, and write the acceptance
  ledger a closed Tier-2 unit owes — one line per numbered criterion, `**Serves:** journal`, under
  `memory/builds/aHoistedPass/build/`.
- **Run `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` after the commit** and act on
  what it names before you stop. Committed range only.
- Commit. Do not merge and do not push — the landing is the parent run's act.
