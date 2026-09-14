# Acceptance ledger — TOOL-dLoggedFlight-9

**Serves:** journal TOOL-dLoggedFlight-9

Tier-2 · node d · 2026-09-14 · the build pass of the committed record, against spec rev-5. The pass
bumped the spec from rev-4 to rev-5 in its own commit before any code, and its section 9 line names
each change. Every criterion line is OBSERVED, and what a gate leg observes is written as owed.
`<suite>` is `tools/runlog/selftest.py`, run directly and never through the gate runner. Its three
timed runs at the closing commit printed `902 passed, 0 failed (902 assertions, floor 902)` in 26.5 to
26.6 s. No gate leg was run, per the owner's instruction of 2026-09-13, and no suite that existed under
`tools/unattended/` before this build ran. Every history an arm reads is a scratch repository built
through one `git fast-import`, and every journal, extract and store is scratch. Every fixture model is
a real `build_run_model` over a scratch history, or one such model lengthened by copying its own
entries.

## The criteria

**Evidences:** TOOL-dLoggedFlight-9

- AC1 — `write_record` (`test_record_ac1_names`) — a build rotated the way the driver rotates, whose
  first run dispatched unit 1 and aborted with no journal line and whose live run dispatched unit 2
  under a driver journal of its own, wrote two records on one date. Each name ended in the run key
  `derive_run_starts` gave that run, and the two keys differ. The journal-less record commits `none`.
  Each name passed the check 5 grammar and the check 21 projection, both typed from the hygiene doc,
  and each graded near miss failed: a name with no family, a name claiming an unserved id and a free
  name. A garbled record re-rendered on a later date was rewritten in place, and the folder still held
  two records. A never-committed run-state file exited 2 with a line naming it. With
  `MEMORY_ROOT=docs/mem` the record landed under `docs/mem/builds/` and nothing under the default
  root. RED seen with the key dropped from the name, with the lookup keyed on the date, with the root
  spelled `memory`, and with the refusal's exit swallowed. The real gate's verdict over a committed
  record is OWED to the `memory hygiene` leg of the bar that grades this run's own record, which
  `TOOL-dLoggedFlight-11` renders.
- AC2 — `derive_serves` (`test_record_ac2_serves`) — a run that dispatched units 2, 3 and 5 of a build
  whose specs define 1 to 5, and an undefined 9, served `X-xFixtureRun-2..3 X-xFixtureRun-5`, and the
  head bound exactly those three as check 21 reads it. A unit closed and named by the run's own commit
  was served, one closed with no commit of the run naming it was not. A run whose one dispatched id no
  spec defines exited 0 with a `no spec-defined unit` line and wrote nothing. RED seen with dispatched
  ids read off the parked rows, which served 9, with closed units ignored, and with the unbound run
  given an id.
- AC3 — `render_record` (`test_record_ac3_shape`) — the landed run's record carried S3's eight headings
  in order. Every table row led with a UTC time or an ordinal, over a population holding both. No line
  matched any of the four id-anchor shapes typed from the recall kit's extractor, and a row led by a
  unit id fails both graders. The twin's facts and tables equalled the markdown read back by line
  shape. RED seen with the units row led by its id, and with the twin dropping a row of every table.
- AC4 — `RECORD_SCHEMA` (`test_record_ac4_classes`) — a real model given one value of every shaped
  class and every member of every closed vocabulary a table carries rendered each of them, and the
  window's openers and closers each reached the file on their own render. Four intruders sat in fields
  the renderer reads: a command in a verb, a session id in a unit, an absolute path in a ledger ref and
  free text in a workflow label. None reached the file, raw or escaped, and the summary counted
  `values withheld: 4`. Free text in the evidence, the sessions, the worktrees and the facts never
  reached it either, and an owner turn's clock time appears nowhere. A vocabulary short one member
  withholds that value, which the arm counts. The driver-source arm found the first six ledger
  sources equal to the driver's owed kinds and acts in both directions. RED seen with cells rendered
  unvalidated, with owner turns kept on the timeline, and with the ledger sources reordered.
- AC5 — `python tools/runlog/runlog.py verify` (`test_record_ac5_verify`) — the live run's record
  commits its six journal lines, never nothing. `verify` exited 0 on the untouched journal, and 0 again
  after the run appended two lines, which the rebuilt model does attribute, so the committed count is
  what kept it green. After one attributed line's `rc` was edited it exited 1 naming the `sha256`
  mismatch. On the journal-less record it read `commitment=none` and exited 0 with its
  nothing-to-verify line. With no journal of the run on the machine it exited 2. RED seen with the
  digest left out of the comparison, with every current line hashed, with `none` reported as a
  mismatch, and with the commitment computed over no line.
- AC6 — `render_record` (`test_record_ac6_cap`) — 500 timeline rows, 60 units, 200 anomalies and 300
  ledger entries rendered 16,474 bytes, stating `500 · shown 60 · elided 440` and each aggregation. All
  twelve anomaly kinds were kept with their 200 counted. The `Data` twin carried the same facts and the
  same rows, and a row from the elided middle, present in the model, is in neither copy. The widest
  model, every list at its bound with its widest values, measured 36,139 bytes at the nominal bounds
  and fitted after halving, saying how many rows it now shows. RED seen with the halving removed, with
  an anomaly kind dropped from its aggregate, and with the twin carrying each row twice.
- AC7 — `record --write` (`test_record_ac7_cli`) — without `--write` the command printed the record and
  wrote nothing. With it the command exited 0, wrote one record, and printed on stdout the
  `gen_build_index.py --write` command it found beside the kit and the subject
  `records(xFixtureRun): the run record`, which carries no unit id, and its wall time as report-only.
  RED seen with the index line removed.
- AC8 — `subprocess` patched (`test_record_ac8_cost`) — rendering the 500-row model made no subprocess
  call, and the patched counter saw the one git call made under it afterwards. The render took 0.003 s,
  printed and not graded. RED seen with one git call added to the render.

## What else the pass carried

- **Three model fields, each through `build_run_model`** (`test_record_model_fields`). `journal_lines`
  equalled the line numbers read off the journal files by bytes, leaving out another slug's lines and
  another worktree's bar. A workflow run inside the window reached the timeline with its label and one
  outside it did not. An out-of-band edit carried its START's time, and the record showed both. RED
  seen with the workflow runs dropped, with their window test dropped, with a joined bar's line and a
  joined push's lines left out, with the driver's lines taken for every slug, and with the time left
  off.
- **The CLI's source resolution** moved out of `cmd_model` into `resolve_model_sources`, which `record`
  shares, so the two commands resolve journals, store and transcripts one way.

## Staged RED

Twenty-seven breaks, each an edit applied to the file by a harness kept outside the tree, run against
the arm that owns it and restored byte for byte. Each turned its arm red and the restored file passed.
One more break, dropping `derive_serves`'s intersection with the defined ids, stayed green: the
model's unit list holds only spec-defined ids, so the intersection cannot change the answer. It was
replaced by the break that reads dispatched ids off the parked rows, which serves the undefined id and
turned the arm red. The breaks are named per criterion above.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `memory hygiene`, including AC1's check 5 and check 21 over this run's own committed record;
- `lexicon naming predicates`, `install-prefix (shipped surface)` and `govkit selfcheck`;
- `codebase-map coverage + freshness`;
- `runlog selftest`, the leg that runs `<suite>`, and
  `every held leg is budgeted, every budget row resolves`, whose row this pass re-measured.

## Residue

- The spec status tokens are a copy of the memory tree's list, and nothing holds them to it, since that
  arm would need a second carried path literal. A status outside the copy is withheld, not rendered.
- The record's timeline carries idle gaps, whose end is an event's time, and that event can be an owner
  turn. The kit README names it.
- `verify` cannot see a line inserted before the committed first time. The model attributes none there
  except a bar a joined push pinned, and the kit README names it.
- The runlog kit stays at 1.0, as the brief sets it, and no leg, fixture file or pin moved. The budget
  row reads 27 s, still under the 60 s floor.
