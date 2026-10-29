**Serves:** journal TOOL-dSafePassage-15

# TOOL-dSafePassage-15 — acceptance ledger

The unit as built, at spec rev-2. In `tools/govkit/upgrade_steps.py`: `run_step_walk`'s `persist`
asks `test_steps_recordable` on the in-memory receipt before each of the walk's five records and,
where it does not hold, makes no `set_step_state` call and writes nothing, returning the suffix
`NOT_RECORDED_SUFFIX`, `(not recorded: receipt below schema 4)`, which the step line carries (S1,
S2); the schema step's `applied` row lands at move 5, after the post-spawn re-read brought schema 4
into memory, with no case for its id (S3). The `walk` family gains the plants `schema-3`,
`schema-3-fail` and `schema-3-kill` (`WALK_SCHEMA_PLANTS`) and the `update` family `schema-3-update`
(S5). A helper the inventory does not name, the second instance of the same copy in the two
families' scratch govs: `write_fixture_schema_step`, which copies `steps/receipt_schema_4.py` with
`FIXTURE_SCHEMA_STEP_PLANTS` applied (`schema.fail` exits the up 1 before any write; `schema.block`
blocks after the temporary file is written and before its rename) and returns the checkout's own
`govkit/receipt-schema-4` row, refusing where the anchors or the row are gone. `build_walk_target`
and `build_update_gov` gain `schema3`, which forces the receipt to schema 3 with `steps` taken out.
`tools/govkit/selftest.py`'s `check_step_walk` gains the four plants' rows, labelled `[dSP-15]`: the
`New arm:` line's arm.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by
running `python tools/govkit/upgrade_steps.py fixture <family> --plant <case>` on node d (Windows,
Python 3.14); its repositories sit under `%TEMP%`.

**Evidences:** TOOL-dSafePassage-15
- **AC1** — `fixture walk --plant schema-3` exited 0 and printed `step govkit/receipt-schema-4 ·
  applied` then `step fx/s1` to `fx/s4 · applied`, and `walk: the receipt reads schema 4 · first row
  govkit/receipt-schema-4 applied`.
- **AC2** — `fixture walk --plant schema-3-fail` exited 1 and printed `step govkit/receipt-schema-4 ·
  failed · exit 1: fx: schema up fails by its plant (not recorded: receipt below schema 4)` and `walk:
  the receipt's bytes equal their bytes before the run`.
- **AC3** — `fixture walk --plant schema-3-kill` exited 0 and printed `walk: after the kill · the
  receipt reads schema 3 whole · the up's temporary file present`, the re-run's five `applied` lines,
  and `walk: the re-run's target and receipt equal an uninterrupted walk's`.
- **AC4** — `fixture update --plant schema-3-update` exited 0 and printed `update: the receipt reads
  schema 4 · steps [('govkit/receipt-schema-4', 'applied'), ('fx/s1', 'applied'), ('fx/s2',
  'applied')]` and `update: the killed target's re-run exits 0 · its receipt, carry aside, equals the
  uninterrupted run's`; the comparison parses both receipts and drops `carry` from every `files` row,
  per rev-2.
- **The predicate's red** — with `persist`'s test replaced by `if False:` in the working copy,
  `fixture walk --plant schema-3` exited 1 on `Refusal: a receipt at schema 3 has no steps to record
  'govkit/receipt-schema-4' in`, printing three `walk: FAILED` lines; the file was restored from its
  copy.
- **The arm's needles** — an AST read of `check_step_walk`'s table matched every needle of the four
  new rows against the four fixture outputs above, with no `<family>: FAILED` in any.

Owed at the close: `govkit selftest` (with `check_step_walk`'s four `[dSP-15]` rows and their
RED-first observation, staged by a walk copy that skips the predicate), `govkit refusal join`,
`govkit acceptance matrix`, `govkit selfcheck`, `recall floor arms`, `encoding posture`, `spec tokens`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: `check_step_walk`, cut to `walk schema-3`, `walk schema-3-fail` and `update schema-3-update`. Break: the walk's `persist` skips `test_steps_recordable`. RED, all three arms: `FAIL [dSP-15] fixture walk schema-3 exits 0 and names step govkit/receipt-schema-4 · applied`, with `upgrade_steps.Refusal: a receipt at schema 3 has no `steps` to record 'govkit/receipt-schema-4' in` and `walk: FAILED · the walk exited 1`. GREEN restored: all 3 ok. The only remaining failures are the three dSP-2 S2 arms that fail at HEAD (see unit 2).
