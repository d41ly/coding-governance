# cMendedVintage — the acceptance ledger for unit 13

**Serves:** journal DEPL-cMendedVintage-13

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar, no self-test suite and
no `*.test.sh` ran in this pass. Every observation below was taken by running the real engine against
scratch fixture targets at the shell — the whole matrix once against the PRE-change engine and once
after — so every criterion is answered by a fixture and none by a suite.*

## The one thing worth reading twice

**The verb nobody asked me to touch is byte-identical, and that was measured rather than argued.**
The extraction's whole risk is `apply` changing. Three fixture shapes were taken through
`apply` against a copy of the engine at `a47c286b` and then against the engine this unit leaves —
the manifest write path, the silenced-leg WITHHELD path, and the non-manifest order path — capturing
stdout, the resulting runner file, the receipt's `gate_runner` block and its stamp, with paths and
shas normalised. All three diffs are EMPTY. The comparison is the only way to answer AC6 at all,
because a suite has no pre-extraction engine to run.

**The defect is live and it was reproduced before a line was written.** A fixture applied, then
stripped of one leg row by hand, then taken through `update --target <fixture> --write` against the
pre-change engine came out with the row still missing and no line anywhere about gate legs. Against
the engine this unit leaves, the same fixture comes out with the row restored and the run printing
`gate legs: emitted 2`, in a run whose own tally reads `wrote 1,` — one file, belonging to the OTHER
kit. That is S3's whole claim: a leg is a DECLARATION, not a file.

**The spec proposed a function name the naming declaration refuses, and the declaration was asked
rather than reasoned with.** `--suggest emit_gate_legs --as py.function` answers `print_gate_legs`,
because `emit` is in no row of the table and the nearest canon cluster is the stdout verb — which is
wrong for a function whose job is a file. `--suggest write_gate_legs --as py.function` answers OK.
The name is amended at rev-3; rev-1's claim that `emit` "is the verb both call sites already spell"
was true of the prose and irrelevant to the gate.

**S4's union is caller-selected, and that is a divergence from rev-2 rather than a detail.** The
union is unconditional in the spec's wording, and applying it unconditionally CHANGES `apply`: that
verb rewrites its receipt's `kits` and `files` to its own selection, so carrying `emitted` rows for
kits the receipt no longer claims would make one field name kits another field does not. `update`
narrows only which rows it classifies and leaves `kits` whole, so there the carry is required. The
rule lives in one function and the caller passes a flag. Amended at rev-3.

**`update` never validated the target's `[gate_runner]` and now must.** The declared file is a
TARGET-supplied path the emission joins onto the target root and WRITES — the escape the validator's
own header records, and which `apply` closes in its pre-write pass. A fixture whose `deploy.toml`
was edited by hand to `file = "../../ESCAPED.json"` and taken through `update --write` exits 1
naming `[gate_runner].file`, writes no file outside the target, keeps the bytes it had already
landed, and raises no traceback. Amended at rev-3.

**S5 was written against one branch and its sibling was live.** The shared function raises a second
`Refusal` the spec never named — a leg whose NAME the target's runner carries and this receipt does
not claim — which any hand-edit made after the install can produce. In `apply` that raise is correct
for exactly S5's own reason; on the update path it is the identical wedge, one branch over from the
branch the spec asked for. A fixture whose receipt had its claim on one leg dropped by hand and was
then taken through `update --write` aborted after its writes against the first cut of this unit, and
now reports it, keeps the bytes, leaves the row the target holds alone, and does not re-stamp. S5 is
widened to its class at rev-3 and the branch is armed.

**`TOOL-dRetiredFork-27` did not fire in any fixture and was not widened.** The duplicate-row
behaviour needs the receipt to claim a name the target also carries; no fixture here produced a
duplicate row, and the dedupe is the same `by_name` index in the one shared function, so the second
caller reaches exactly the behaviour the first one had. The row stays open.

**Evidences:** DEPL-cMendedVintage-13

*Every token below sits on its own bullet's FIRST physical line, deliberately: hygiene check 23
joins an answer's backticked tokens to the criterion's per PHYSICAL line, so a token pushed onto a
continuation belongs to no line and its criterion grades as answered by nothing.*

- AC1 — OBSERVED — `update --target <fixture> --write` — a fixture installed with two kits, each
  declaring one `[[gate_leg]]`, has one leg's row deleted from its runner by hand and committed; the
  run afterwards restores it. The RED-WHEN was staged and read: with the population keyed on the
  kits whose bytes MOVED rather than on the selected kits' descriptors, the same run leaves the row
  missing and four other arms fall with it. Against the pre-change engine the run prints no
  gate-legs line at all.
- AC2 — OBSERVED — `--kits` — the same fixture taken through a run scoped to one kit restores that
  kit's leg, leaves the other kit's leg standing in the runner, and still claims it in the receipt's
  `gate_runner.emitted` as `("demo2 leg", "demo2")`. The RED-WHEN was staged and read: with the
  caller passing no carry set the same run's `emitted` is `[('demo leg', 'demo')]` alone, which is
  the revocation that wedges the target at the run after.
- AC3 — OBSERVED — `silenced_legs` — a kit whose leg argv names an engine gov does not ship is
  reported by `update` with the same sentence `apply` prints, the defective leg is absent from the
  runner, the healthy sibling IS written, and the run exits 1. One defective leg does not take the
  healthy ones with it, which is the shape this step already had once.
- AC4 — OBSERVED — `update --target <fixture> --write` — a fixture whose runner file is replaced
  with non-JSON bytes and committed comes out of that run with the file named in an `r.fail`
  finding, exit 1, NO traceback, the engine bytes this run wrote still on disk, and `gov_commit`
  still at the pre-run stamp. The RED-WHEN was staged and read: with the caller asking for `apply`'s
  disposition the same run aborts and that arm reds.
- AC5 — OBSERVED — `ROLLED BACK` — a kit whose own `[check]` is staged green-to-red is reverted by
  the verify pass, and its leg is NOT written by the run that reverted it, while the kit whose
  writes stood keeps its leg. The RED-WHEN was staged and read: with the rolled-back set out of the
  population the reverted kit's leg appears in the runner beside the surviving one.
- AC6 — OBSERVED — `apply --target <fixture>` — the runner file this engine produces is
  byte-identical to the one the pre-change engine produced from the same fixture, over three shapes:
  the manifest write path, the silenced-leg withheld path, and the non-manifest order path. The
  stdout of all three is identical too, after path and sha normalisation. A second, weaker half is
  gradeable in-suite and is written as an arm: a re-`apply` leaves the runner byte-identical, which
  reds on the same class of regression.
- AC7 — OBSERVED — `gate-legs.md` — a fixture whose `[gate_runner].kind` is `none` is applied, then
  gov renames the leg's engine in its next vintage; `update --write` refreshes the order to the new
  argv, prints `ORDERED, not emitted`, and leaves the receipt's `orders` list holding exactly the one
  row `apply` recorded. Against the pre-change engine the same fixture's order still names the
  vintage-A engine afterwards.

## OWED

- **AC6's atomic write has no failing case here and is not claimed.** S6 is implemented — the
  write-back is `write_text` to a sibling temp path followed by `os.replace` — but nothing in this
  pass fails when it is absent, so the byte-identity arms above would pass over a plain `write_text`
  too. `DEPL-cMendedVintage-21` is the unit that makes the atomic write one helper with something
  that fails when it is not used, and it is later in this roster. Recorded OWED rather than claimed.
  **Discharged 2026-09-17 by `DEPL-cMendedVintage-21`**, whose ledger carries the `**Evidences:**`
  block: that unit extracts this write-back into `write_atomic` and stages a raise between the temp
  write and the replace, so the mitigation now has a failing case. AC6 itself is unchanged and was
  not re-graded — this note records the second half arriving, not a criterion moving.
- **The gate-side encoding of every criterion.** Thirty-one arms tagged `[-13]` land in this
  unit's write set and only the govkit self-test suite can execute them in place. That suite is a
  merge-bar leg and no gate, suite or bar ran in this pass. They are NOT asserted by construction:
  the block's source was taken verbatim from the shipped file, wrapped in a standalone harness
  binding the suite's own `check`, `git` and `settle` and a real temp root, and run against the real
  engine — all thirty-one reported `ok`. It was then re-run against five staged breaks of the
  engine, one per scope item plus one for the refusal class, and each break redded the arms written
  against it and nothing else.
  What is owed is the suite RUN: that the block still holds in the suite's own scope, with the
  suite's own `tmp`, and that the arms it sits beside are still green.
- **The merge bar is owed whole.** `govkit selftest`, `govkit selfcheck`, `govkit refusal join`,
  `govkit acceptance matrix` and `run-gates canary` are this unit's declared gates and none ran as a
  bar leg here. Four checkers that are not suites DID run directly and are not owed: `govkit
  selfcheck` exits 0 over gov's own descriptors, `refusal_join.py` enumerates 254 branches with its
  raised pin holding, the naming checker exits 0 with its verb-offender pin unmoved, and the
  carried-prefix scan reports `carried-prefix clean` with no row rising.
- **`BRANCH_PIN` was raised from a measurement, not a prediction.** 252 at this unit's base
  `a47c286b`, read off a clean export of that tree, and 255 on the tree this unit leaves. The net is
  three and the sites are five — four new refusal branches, every one of them the same rule applied
  on the update path, and one removed by merging `apply`'s two spellings of the malformed-runner
  refusal into a single message the update path needs as a value. All four new sites are armed.
- **`check_runbook_parity.py` is red at HEAD and is red here, identically.** Eighteen problems on
  both sides, naming registry entries with no anchored runbook section. It is not a leg in the
  manifest and this unit neither caused nor cleared it; recorded so a later reader does not attribute
  it to this diff.
- **No read-only preview of the emission was built, and §3 was corrected rather than left standing.**
  rev-2's non-goal said the preview "prints what it would emit"; the read-only run RETURNS hundreds
  of lines above this step, so printing that would mean resolving every leg on a path that writes
  nothing, for no criterion. The clause is withdrawn at rev-3 — an amendment that leaves its other
  half in place is one rule returning two verdicts. The absence of an `if write:` guard at the call
  site is a measurement of that same return rather than an assumption about it.
