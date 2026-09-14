# Acceptance ledger — TOOL-dLoggedFlight-13

**Serves:** journal TOOL-dLoggedFlight-13

Tier-2 · node d · 2026-09-14 · the build pass of the drift-audit run-record signal, against spec
rev-5. The pass moved the spec from rev-4 to rev-5 in its own commits, `ddc0b675` and `d99edec6`,
before any code, and its section 9 line names each change. The code landed in `454b9016`. The suite,
`tools/drift-audit/selftest.py`, ran directly and never through the gate runner. At the closing
bytes it printed `all checks passed (259 executed, floor 259)` in 66.6 s, against 188 checks and
60.8 s before this unit. The report ran over this tree once, as AC1's own observation. No gate leg
ran, per the owner's instruction of 2026-09-13, and no suite that existed under `tools/unattended/`
before this build ran.

Every staged break below edited the real engine, the real README or the real suite, ran the arm, and
restored the file from its own bytes, checked by hash. The eighteen engine and README breaks were run
twice, the second time with the kit's bytecode cache cleared and the interpreter at `-B`, and each
failed the check it aims at both times.

## The criteria

**Evidences:** TOOL-dLoggedFlight-13

- AC1 — `python tools/drift-audit/drift_report.py --json` — run once over this tree, it exited 0.
  The signal read value 5, `of` 57, `live` true, one unjudgeable and pin 5. The population is the 51
  tracked `RUN.md` files and the 6 rotated archives, measured with `git ls-tree` over the build
  folders. Every detail row prints the witness's relation to its base. aClosedDocket reads `ahead
  retired-unit`, aCollapsedScan `ahead other`, and aUnblockedFleet, dRetiredFork and dSealedTally
  `ahead surfaced-park`. dRatifiedSeam reads `equal unjudgeable — witness not re-written since
  preflight`, and the refused-landing note closes the list. The suite's `test_nonterminal_merged_runs`
  commits a record terminal and then edits it live in the working tree, which is not counted. Its
  mirror, committed live and edited terminal, is counted, and a record present only in the working
  tree is absent from `of`. RED seen: the working tree read in place of the blob listed the first and
  dropped the second. A population selector naming no file read DEAD, and every value check failed.
- AC2 — `python tools/drift-audit/drift_report.py --check` — over this tree it is the `drift-audit
  records` leg, and its verdict is owed to the post-build gate run. The suite ran `--check` over its
  own fixture with the signal at 18 against pin 0, and it exited 0. RED seen: the signal made gateable
  turned that exit to 1, naming the signal over its pin.
- AC3 — `python tools/drift-audit/selftest.py` (`test_nonterminal_merged_runs`) — each alternative of
  each S3 row is its own fixture, and each reads its sub-class. Rescope retire and supersede read
  `retired-unit`, and rescope add and the item whose second word is `retire` read `other`. Decision,
  abort, override and waiver read `surfaced-park`, the record with no row reads `no-rows`, and review,
  dispatch, brief and proposal read `other`. A decision then a review reads `other` and the reverse
  reads `surfaced-park`, so the LAST row decides. A row of a kind the driver does not declare after a
  decision leaves it `surfaced-park`. A witness equal to its base reads `equal` and one behind it
  reads `behind`, each unjudgeable with the reason and not counted. So do a missing phase, witness or
  base, a witness named `main`, an unresolvable witness or base, and a base off `main`. A LANDED
  record, a rotated ABORTED archive and a witness on an unmerged side branch are neither counted nor
  listed. RED seen, each failing the fixture it aims at: retirement never matched, `waiver` dropped
  from the owed set, the empty record read `other`, and `review` or `add` joined an owed set. So did
  `retire` matched anywhere in the item, the first row deciding, and an undeclared kind taken as
  parked. The equal branch removed read the equal fixture as `behind`, and the behind branch removed
  counted the behind fixture. LANDED dropped from the terminal set counted the LANDED records, the
  merge test skipped counted the unmerged witness, and the sha shape relaxed counted the witness named
  `main`.
- AC4 — `python tools/drift-audit/selftest.py` (`test_nonterminal_merged_runs`) — the signal's git
  processes are counted at the report module's own `subprocess` binding over a separate repository.
  Five records cost 3, fifty cost 3, and each size was first read and counted whole. RED seen: one
  git call added per record made those 8 and 53.
- AC5 — `bash tools/check-kit-versions.sh` — the `kit version markers` leg's verdict at 1.11 is owed
  to the post-build gate run, and so is the `drift-audit selftest` leg's. Every carrier moved: the
  constant and marker in `drift_report.py`, the markers in the README, the adopter, the project
  layer, its template and the suite, and both drift workflow harnesses' marker and `meta.version`. The
  suite's `test_version_carriers_agree` reads the markers of every file in the kit directory. It adds
  the descriptor's `marker_carriers`, and all eight agree with `KIT_DRIFT_AUDIT_VERSION`. RED seen:
  the README's marker put back to 1.10 failed its check. The suite ran directly and passed, as the
  opening paragraph records.
- AC6 — `python tools/drift-audit/selftest.py` (`test_park_sets_match_the_driver`) — the driver is
  present here. `PHASES_TERMINAL`, `PARK_KINDS`, `PARK_KINDS_OWED` and `PARK_ACTS_OWED` each equal the
  engine's copy in both directions, and each is first asserted to be declared where the arm reads it.
  A control dopes the real driver text with one more owed kind and reads it unequal. RED seen:
  `waiver` dropped from the engine read `engine lacks ['waiver']`, which is the driver holding an
  owed kind the table lacks. `review` and `add` added read `driver lacks`, and LANDED dropped from the
  terminal set read `engine lacks ['LANDED']`.

## What else the pass carried

- The suite had no assertion floor, so it gained one. `check` now counts every executed check, and
  the closing line prints the count against `CHECK_FLOOR`, set at the measured 259. A run with a SKIP
  says the floor was not compared rather than comparing it. RED seen: the version arm's call removed
  from `main` printed `executed 249 checks, under the floor of 259` and exited 1.
- A repo with no run record and no `.unattended.conf` reads NOT ASKED, and one with the conf and no
  record reads DEAD. A base ref the rev-list cannot walk reads DEAD with the stage named. Each has its
  arm.
- `tools/drift-audit/drift_signals.py` pins the signal at the measured 5 with no RATCHETS row, for
  the reason spec section 4 gives.
- The README gained the 1.10 to 1.11 migration note, the signal's table row and a short section. The
  section names the four sub-classes and points at `_derive_run_subclass` for the table.
- The map was regenerated. `symbols.json` gained the new public function and the three arms. No
  dossier claims a drift-audit key, and no inventory key moved.
- No carried-prefix row moved. With the gate's own two patterns, every file this pass touched carries
  the same count it carried at the base. The suite reaches the driver, the recall kit and the
  harnesses by paths derived from its own directory.

## The checklist over the build

`gotchas.py --for-diff HEAD~1..HEAD` over the spec commit selected eight classes, and over the code
commit twelve.

- `amendment-leaves-its-other-half-standing`: spec section 5's testing line still said `no-progress`,
  rev-3's name for what rev-4 made unjudgeable. `d99edec6` rewrote it before any code.
- `two-answers-to-one-question`: the engine spells four driver sets, held to the driver both ways by
  AC6's arm. The README had restated the S3 table, a third copy, and now points at the function.
- `staged-break-runs-stale-bytecode`: the kit's `__pycache__` held three files from an earlier run.
  Every break was re-run with it cleared before each run and the interpreter at `-B`, with the same
  eighteen REDs.
- `fixture-passes-by-finding-nothing`: each negative check sits beside a positive one in the same
  arm. The checklist asked for three more breaks, the unmerged witness, a non-terminal LANDED and a
  relaxed sha shape, and each went RED.
- `naming-leg-grades-what-python-named`: every definition, nested ones included, was asked of
  `lexicon.py --suggest` and leads with a declared verb. There is no class and no dunder. The leg
  itself was not run, since its argv is a gate row.
- `heredoc-escape-reaches-the-regex`: the edit tool decoded the unicode escapes this unit wrote for
  the middle dot and the em dash into the literal characters. The regex and the three fixture strings
  were written back as escapes by a byte-level script, and the committed blobs hold no control byte.
- `staged-break-substitutes-a-synthetic-value`: every break edits the shipped engine against real
  commits. AC6's control adds one member to the real driver's text.
- `degradation-known-but-unreported`: every stage that can fail returns DEAD with its note. An
  unjudgeable record carries its reason in its own row.
- `inline-fence-swallows-the-rest-of-the-file`, `trailing-comma-counted-as-an-element`,
  `empty-field-collapses-unless-it-is-last` and `one-value-field-records-a-mixed-outcome`: no fence,
  comma counter, TAB read or one-value field is in this diff.
- `suite-invalidated-by-a-commit-under-it`: no commit was made while the suite ran.
- `fold-text-is-unreviewed-surface`: rev-5 and this pass's prose are unreviewed. The build's closing
  diff review reads them.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it: `drift-audit records`,
which is AC2 over this tree, `drift-audit selftest`, `drift-audit wiring`, `kit version markers`,
`lexicon naming predicates`, `codebase-map coverage + freshness` and `memory hygiene`. The legs
outside section 7 that this pass's files reach are owed the same way. They are `install-prefix
(shipped surface)`, over the unchanged carried counts, and `govkit selfcheck`, over the moved version
marker.
