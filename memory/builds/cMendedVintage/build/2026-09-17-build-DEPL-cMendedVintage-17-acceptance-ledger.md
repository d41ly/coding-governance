# cMendedVintage — the acceptance ledger for unit 17

**Serves:** journal DEPL-cMendedVintage-17

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every observation below was taken by running the real engine against
scratch fixture targets at the shell — once before the change and once after — so every criterion
here is answered by a fixture and none by a suite.*

## The one thing worth reading twice

**The defect is live, it was reproduced, and the spec's account of what it does was wrong in two
rows of three.** rev-1's §4 table reasoned about the three shapes a target's
`.gitattributes`
can take and predicted a splice of foreign bytes at an arbitrary blank line. Measurement disagreed.
The missing term is that any file these writers produce ends with a newline, so
`split("\n")`
always yields a trailing empty field, and every such file already holds one blank line before the
target adds any of its own.

**What BASE actually did, per shape, measured at `d719bca7`:**

- A file with only that trailing blank line. The empty-marker locator found exactly one pair, and
  because an empty block renders as exactly one empty line, the splice replaced an empty line with an
  empty line. **The bytes did not move and the run exited 0.** What moved was the receipt: the row
  came out claiming
  `mode: spliced`
  with
  `patterns: []`
  and
  `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
  — the sha256 of the empty string — while gov's real block sat on disk claimed by nothing. This
  happens on every run, silently, at exit 0.
- A file carrying one further blank line of the target's own. Two pairs, and the run died mid-write
  with
  `govkit: expected exactly one marker pair, found 2 open and 2 close`
  at exit 2, after the verdict table and after the snapshot, so the receipt was never re-stamped.
  Three blank lines gave the same refusal at three pairs.
- A file with no trailing newline. **Unreachable.** Both writers end their write with a newline, so
  the append row rev-1 listed cannot be produced by any target this tool has installed into.

So the red is not bytes landing where they do not belong. The splice really does fire at an arbitrary
blank line; the bytes it lands there are the bytes already there. The damage is the RECEIPT, and the
loud half is an aborted update — which is worse than rev-1 claimed in the common shape, because an
exit code cannot see it.

**rev-2 records all of that and adds AC5**, because a suite watching exit codes alone reports the
silent shape clean. AC2 was reworded in the same revision: it asked for "two blank lines outside
gov's block", and one of those two is supplied by the file's own trailing newline, so the fixture it
described was not the fixture it meant.

**The fix is two exits and one deletion, and the write gate is structural rather than nominal.** The
empty pin set leaves the arm above every line that builds a marker, so the write carrier is assigned
only below a non-empty set and the block builder over a non-empty set always emits both markers.
Renaming the verdict cannot reopen the empty-marker call — which is exactly what AC2 reds on. The
withdrawal then removes the marked region and drops the receipt row through
`withdrawn_rows`
together, reusing the removal channel this verb already owns rather than minting a second one, which
is also what makes the rollback's un-drop one line instead of a new branch.

**One thing the spec asked for and this unit deliberately did not do.** §3 refuses a renormalize on
the withdrawal path. The flag the renormalize keys on is the one the pin WRITE sets, so the removal
carries its own second flag for the rollback's path set alone. Folding the two would renormalize a
population the target no longer pins — and it would bite precisely on a target that keeps eol rules
of its own outside gov's block, which is the target this whole unit is about.

**Evidences:** DEPL-cMendedVintage-17

- AC1 — OBSERVED —
  `pins-moved`
  — before the change all three fixture shapes printed it; after, all three print
  `pins-withdrawn     [attributes   ] .gitattributes`
  and the tally reads
  `pins-withdrawn 1`.
  A read-only run of the same fixture prints the verdict and then the sentence naming the block as
  REMOVED rather than rewritten, and writes nothing.
- AC2 — OBSERVED —
  `.gitattributes`
  — the fixture whose own rules carry a blank line exited 2 before the change with the marker-pair
  refusal and exits 0 after it, with no refusal in the output. AMENDED in the same revision: the
  criterion asked for two blank lines outside gov's block when one of the two is the file's own
  trailing newline, logged at §9 rev-2.
- AC3 — OBSERVED —
  `attributes`
  — after the run gov's marked region is absent from the file, the surviving text equals the pre-run
  bytes minus that region computed by the same locator, and the receipt's row list filtered on role
  `attributes`
  is empty. Measured on all three shapes.
- AC4 — OBSERVED —
  `.gitattributes`
  — a fixture built from a gov declaring no pin at all writes no
  `.gitattributes`
  at apply, and the following
  `update --write`
  exits 0, prints neither pin verdict, and still leaves no such file. Liveness: that run reports
  `wrote 1,`
  so it is not a report on an update that never happened.
- AC5 — OBSERVED —
  `patterns`
  — the fixture with no blank line of its own is the one BASE completed at exit 0 over. After the
  change its receipt carries no attributes row at all, so the empty
  `patterns`
  list and the sha256 of the empty string are both unreachable rather than merely unlikely.

## OWED

- **The gate-side encoding of AC1 through AC5.** The arms landed in this unit's write set are
  `[-17]`
  arms and only the govkit self-test suite can execute them. That suite is a merge-bar leg and no
  gate, suite or bar ran in this pass, so the arms are asserted here by construction — they replay
  the same fixture sequence the shell observations used, through the builders
  `build_verify_gov`
  and
  `build_verify_target`
  that
  `DEPL-cMendedVintage-15`
  already ships — and OWED to the bar the main loop runs once every unit is terminal. Nothing in
  section 6 is owed: every criterion was observed directly.
- **No other unit's owed criterion is discharged here.** This unit found none open against it.
