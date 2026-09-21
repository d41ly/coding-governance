# cMendedVintage — the acceptance ledger for unit 12

**Serves:** journal TOOL-cMendedVintage-12

*Node `c`, 2026-09-18, written by the pass that built the unit. No merge bar and no `*.test.sh` suite
ran in this pass. Every line below was taken at the shell in this worktree, by running the repaired
function and the repaired checker directly; the one red was staged against a scratch copy of the
pre-repair file rather than described.*

## Read this before you read the green arms

**The path set was captured BEFORE anything was edited, which is the only way AC1 could not be
faked.** A fixture over three commits and six units — including one unit with no brief row and one id
that does not exist — was run against the unmodified library and kept. The same fixture was re-run
against the repaired one and the two outputs are byte-identical. The disjointness verdict rests on
those paths, so a repair that quietly returned a different set would have moved a safety answer while
claiming to fix a stall.

**One property the heredoc gave free had to be paid for explicitly.** Command substitution strips
trailing newlines and the heredoc put exactly one back, so every line the old loop read was
terminated. A file need not be, and a bare `read` drops an unterminated last line. Without the
`|| [ -n ... ]` guard the repair would have returned a SMALLER set on any run-state file whose last
line is a brief row and which ends without a newline — the one way this change could have moved a
verdict quietly. It is in the diff and its reason is in the comment above it.

**The measurement adjudicates between two live diagnoses, and it was not designed to.** This run's
own parked decision attributes the failure to accumulated cost: roughly fifty dispatch rows times a
hundred-odd commits of `git show`, tens of milliseconds a spawn on this platform, with the parent
showing no CPU because the work sits in short-lived children. The spec attributes it to the reader
waiting on a grandchild's write end. The repair does not REDUCE the spawn count — it adds a `mktemp`
per call and removes a subshell, which is a wash or slightly worse — and the same verb went from
exiting on a one-hour bound having written nothing to completing in 2m26s. Cost alone does not
explain a change of that size when the spawn count did not fall. Both diagnoses are partly right and
the order matters: the stall was the blocker, and the residual 2m26s IS the cost the parked decision
describes, still growing with rows, commits and file size. That cost is section 3's explicit non-goal
and remains somebody's next unit.

**What is OWED, and why it is not a bullet below.** Section 7 originally declared a permanent arm
over this function in the kit's own suite. This pass is forbidden to run any suite, so it could not
watch that arm fail, and an arm whose failing case nobody has observed is an assertion about nothing.
It is recorded OWED in the spec at rev-2 rather than written blind. The arms that DID land are the
checker's own, where the failing case was observed in the same session.

**The write set grew by one file beyond what the brief listed, and this is that disclosure.** The
brief allowed the library, the shell-hygiene checker, its registry, the spec and this ledger. The
dispatch row for `DEPL-cMendedVintage-26` also wrote the run-state file, because declaring one is how
AC1's second half is proved and the verb stages its own record. Nothing else was touched.

**A dispatch was declared for another unit, deliberately, and the main loop should not declare it
twice.** `DEPL-cMendedVintage-26` now carries the row at `2026-09-18T20:40:31Z`, naming the two
govkit files its own spec's section 6 table lists, its spec and its acceptance ledger. Its brief tells
its builder to re-declare if the set grows.

**Evidences:** TOOL-cMendedVintage-12

- AC1 — `read_brief_paths` — OBSERVED, both halves. The captured path set over three commits and six
  units is byte-identical before and after the repair; `diff` of the two captures is empty. For the
  second half, a bounded
  `bash tools/unattended/unattended.sh --dispatch cMendedVintage --pass DEPL-cMendedVintage-26 --writes ...`
  exited 0 in
  `real 2m26.343s`
  and wrote its row into the run-state file, where it is now the last dispatch row. The before-state
  is this run's own record rather than my claim: four attempts are logged, at 2h14m, at a 420 s
  bound, at a 300 s traced bound and at a 11350 s bound, none of which wrote a row. Liveness for the
  first half: the same fixture asks for a unit with no brief row and for an id no row carries, and
  both answer empty in both captures, so a capture that returned nothing at all could not have
  passed as agreement.
- AC2 — `lib-unattended.sh` — OBSERVED in both directions, and the RED half was staged. The widened
  predicate over the PRE-repair text of the file names
  `[(138, 'RBP')]`
  and over the repaired text names nothing in any gated class. The pre-repair text was taken from
  `git show HEAD:...` rather than edited into the tree, because the file is the one the driver sources
  on every verb and a half-written copy of it voids whatever invocation reads it next. The rest of the
  tracked tree was then measured: the widening moves sites in more than twenty files out of the near
  miss it used to sit in, and every one of them was checked against the assignment it follows. The
  four whose assignment is furthest away — up to 749 lines, and each behind a function close — are
  file-level values read by a loop below, not names re-used across a scope. The scan prints all six
  populations on every run, green included, so the near misses stay visible rather than becoming
  coverage.
- AC3 — `read_brief_paths` — OBSERVED. With `TMPDIR` pointed at a directory that does not exist, the
  function exits 2, prints nothing on stdout, and stderr carries
  `lib-unattended: read_brief_paths cannot create a scratch file`
  naming itself. The paired control is the same call with a working scratch root in the same session,
  which returns the path set of AC1 — so a function that could not read anything at all would have
  failed that companion first. This is the state an empty answer would otherwise be
  indistinguishable from, because a pass that declared no brief paths is legitimate and common.
