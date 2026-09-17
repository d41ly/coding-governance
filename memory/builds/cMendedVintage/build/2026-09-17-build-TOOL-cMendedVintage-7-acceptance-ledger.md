# cMendedVintage — the acceptance ledger for unit 7

**Serves:** journal TOOL-cMendedVintage-7

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh` suite
ran in this pass. Every line below was taken by running the edited checker, or the named gate script,
at the shell in the worktree, and every red was STAGED into a scratchpad copy and then discarded
rather than described.*

## Read this before you read the green arms

**The loop this unit adds is INERT on every gov bar, exactly as the loop it lives beside is.** This
tree holds no receipt, so a bare run takes the announced `SKIP` path and the new note has nothing to
count. The only thing any gov bar grades here is the built-in arm harness, which is why the fifth and
sixth arms went into that harness rather than into a suite. A green row for this leg is evidence that
the value comparison and the silence-on-zero branch behave; it is not evidence that any receipt in
this repository was read, because there is none.

**Silence on zero is a designed behaviour and not an unannounced skip, and the distinction is the
unit.** The preceding unit was held to the rule that a skipped arm must say so. This loop is not a
skipped arm: it runs on every invocation with rows in hand, and printing nothing is its answer when
the answer is zero. A line that appears on every run carries no information and trains a reader past
the one run where it says something. The header sentence added by S5 states the same thing for a
reader who finds the silence and wonders whether it is a bug.

**The count printed is the fixture's own, derived at print time.** The spec's goal section cites 47
of inCMS's 95 rows from `DEPL-dGaugedVintage-8`. That is a historical measurement of another
repository at another time, it is carried into no message, no comment and no assertion in this unit,
and the only number this unit's code can print is the one it just counted.

**The remedy this note prints is live in this release, and the note stays a note anyway.** Checked
rather than assumed: `DEPL-cMendedVintage-4` has already landed and the withheld-re-stamp message in
the deployer carries the `--pin` spelling at
`govkit.py:8723`
today. So the argument for keeping this advisory is NOT that the remedy is broken — it is that an
adopter pulling this release has had no earlier release in which to clear their rows, and the release
that fixes a remedy should not also be the release that starts redding on it. The follow-up that
turns the note into a leg failure is named in the script header and in the spec's Edges section, and
nobody in this build carries it.

**Three citations in the spec were stale by roughly nine hundred lines and one claim was false.**
Logged as rev-2 with its section 9 lines. The substance of all three re-verified as written; only the
addresses had moved, because the deployer grew underneath the spec between Tuesday and Wednesday. The
false claim was §4's "both print today" sentence about the bare remedy form, which stopped being true
when `DEPL-cMendedVintage-4` landed at order 5 of this same build.

**Evidences:** TOOL-cMendedVintage-7

- AC1 — OBSERVED. Run with
  `--selftest`
  the fifth arm reports
  `ARM ok`
  against the label naming two unattributed rows counting 2, and the run exits 0. That arm's fixture
  receipt carries two rows whose `evidence` is
  `unattributed`
  plus one row set to `apply` and one row with the field ABSENT, and it asserts the printed line
  names
  `2 row(s)`
  Observed RED four ways on scratchpad copies, none of them left in the tree: with
  the predicate rewritten to `"evidence" in row` the arm fails, with it rewritten to bare
  `row.get("evidence")` it fails, with the silence branch disabled it survives but the sixth arm
  fails, and with the remedy reduced to the no-op form it fails. The first two are the exact
  substitution the brief names as the class that already bit two units in this build, and the arm
  discriminates against both.
  figure: DERIVED — the 2 is the fixture's own row count, read out of the printed line by the arm
  rather than asserted anywhere.
- AC2 — OBSERVED. In the same
  `--selftest`
  run the sixth arm reports
  `ARM ok`
  against the label saying no unattributed row prints anything at all, over a fixture receipt
  holding one `apply` row and one row with no `evidence` field. The arm's
  assertion is that the captured stdout is the EMPTY STRING, so a zero-valued
  `NOTE`
  line would fail it and not merely look odd. Observed RED by disabling the silence branch on a
  scratchpad copy, which drops the harness to 5 of 6.
- AC3 — OBSERVED. The line the populated case prints is
  `check-receipt: NOTE - clear them with: govkit adopt --re-adopt --pin <path>=<rev> --write`
  which contains `--pin` and does not contain `--re-adopt --write` as a contiguous string. The fifth
  arm asserts both halves, so this is a graded property and not a read one. Observed RED by
  substituting the bare form into a scratchpad copy, which fails that arm alone.
- AC4 — OBSERVED, and the figure is DERIVED at both ends as the criterion demands. Run with
  `--selftest`
  the harness now prints
  `fixtures: 6/6 arm(s) ok`
  against the
  `fixtures: 4/4 arm(s) ok`
  the preceding unit's AC2 recorded. Two higher, and the count is printed from the length of the
  results list, so an arm written but never appended would leave the number where it was.
- AC5 — OBSERVED. The head of the file carries, inside the section that says out loud what this
  checker does NOT check, a bullet reading "No VERDICT on the `evidence` state, though it is now
  READ", which states that such rows are counted and printed as a
  `NOTE`
  whose count never moves the exit status, gives the reason, and names the condition that ends it:
  the release AFTER adopters have had one in which to clear their rows. It closes with the sentence
  that this arm only reports and the integrity arm above it is the only one that decides, which is
  the qualification the criterion's red-when clause asks for.

Nothing is OWED among the five criteria: all five were observed against the edited checker. Two gate
legs named in §7 could not be observed in this pass and are OWED to the main loop's bar.

## What did not run, and why

`bash tools/run-gates/run-gates.sh` in every form, and every `*.test.sh` suite, were withheld by this
pass's own mandate. The gate scripts that DO grade this unit's new bytes were run individually, which
is the direct-check substitution the mandate asks for, and all of them are green:

| gate script run directly | what it says about this unit | result |
|---|---|---|
| `python tools/run-gates/check-receipt.py --selftest` | the six arms, which are the unit | exit 0, 6/6 |
| `python tools/lexicon/lexicon.py` | the new function leads with a declared verb | exit 0, `.py` graded in parser mode |
| `bash tools/check-install-prefix.sh` | the new prose spells no kit path | exit 0, 269 shipped files |
| `bash tools/check-dead-paths.sh` | the rev-2 edits name no deleted file | exit 0, 24 derived needles |
| `bash tools/check-line-length.sh` | the header and ledger prose stay under their limits | exit 0 |
| `python tools/check-spec-tokens.py` | rev-2's backticked citations still resolve | exit 0, 849 tokens graded |
| `python tools/govkit/govkit.py selfcheck` | no declaration moved, and none needed to | exit 0, 0 unclaimed |

`python tools/codebase-map/gen_map.py --write` was run after the edit and rewrote exactly one of the
three generated artifacts: the new function is a symbol key and the other two artifacts came back
byte-identical. No dossier claim was owed, which is the difference between this unit and the
preceding one — a new leg NAME is an inventory key and a new function is not.

**OWED to the bar, two legs.** `run-gates gov canary` is a `*.test.sh` suite and is banned in this
pass; it is the leg that would confirm the manifest row still dispatches the way the runner expects
after the file grew. The memory-hygiene ledger arms are HELD under `--staged`, so no commit hook
graded this document's own shape and the push-boundary run is where it binds.

**The name follows a refusal rather than a first instinct.** The spec records that
`python tools/lexicon/lexicon.py --suggest report_unattributed --as py.function`
refused `report` and named `print`, on the ground that print writes to stdout for a human and never
returns a value in disguise. The shipped function is `print_unattributed` and it returns None, so the
verb and the signature agree; the two new arms capture stdout to grade it, which is the shape a print
verb forces and is why they do not read a return value.

**The arms grade a rows list that went through the receipt on disk.** Both new arms build their
fixture with the harness's own writer and then read the rows back out of the written JSON, so a row
shape that `json` would never round-trip cannot pass them. That is deliberate consistency with the
four arms already there and not decoration: the field this loop keys on is a string that has to
survive serialisation to reach the checker in an adopter's tree.
