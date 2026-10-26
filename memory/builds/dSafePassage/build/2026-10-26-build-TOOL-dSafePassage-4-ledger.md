**Serves:** journal TOOL-dSafePassage-4

# TOOL-dSafePassage-4 — acceptance ledger

The unit as built. In `tools/govkit/upgrade_steps.py`: `derive_reverse_steps` (S3), `run_reverse_walk`
with its five moves (S4), `write_rollback_record` (S6), and `fixture rollback|rollback-update
[--plant <case>]` with every plant of §4 "Inventory". Helpers the inventory does not name, each the
second instance of something `run_step_walk` held inline, lifted so both walks share one copy:
`write_step_record` (set the row, write the receipt atomically), `run_step_reread` (spawn, then
re-read `schema` and `steps`, now also dropping a key the step took away, which only a down does),
`read_image_paths` and `write_step_staged` (the S11 staging); and for the fixtures
`build_walk_target`, `run_fixture_child`, `run_fixture_govkit` and `build_update_gov`, lifted out of
the `walk` and `update` families, plus `read_reverse_walk_callers` and `run_callers_probe` for AC7.
The fixture step `fx.py` gains `<slug>.block-after`, `<slug>.down-fails`, `<slug>.down-keeps` and
the `<slug>.down-saw` view of the tree. In `tools/govkit/govkit.py`: `check_rollback_vintage` beside
`demand_forward_vintage`, whose remedy now names `update --rollback --to <rev>` (S2); the
`--rollback` flag, live only with an explicit `--to`, and the USAGE line and sentence (S1); the
`--rollback --kits` refusal; `would roll back <id>` in the read-only preview; the reverse walk and
the record after the preview and before the pre-write snapshot, a stop ending the run with its
finding (S5, S6); no forward walk under `--rollback`; the stamp keeping the `schema` the downs left;
and `_rb_finish` writing the record at each of the run's three returns. `help/upgrade-steps.md` gains
"Rolling back" (S8), and its receipt paragraph, with the module docstring, now says an `applied` row
carries a stopped down's `failure` (TOOL-dSafePassage-43's two leftover texts).
`tools/govkit/selftest.py` gains `check_step_rollback`, the `New arm:` line's arm.
`refusal_join.py`'s `BRANCH_PIN` moves 314 -> 319 by the measured delta (384 -> 389).

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed by
running `python tools/govkit/upgrade_steps.py fixture <family> [--plant <case>]` on node d (Windows,
Python 3.14); its repositories sit under `%TEMP%`. The lifted helpers were re-observed through the
families they came from: `fixture walk` (0), `walk fail-k` (1), `walk kill-step` (0), `walk attended`
(1), `update` (0), `update update-fail` (1), `update kill-walk` (0), `update read-only` (0), each
with no `FAILED` line, and a scratch probe of `run_step_walk` printed its three refusals unchanged
(`does not read back after the spawn`, `refused the step's writes`, `'../x.txt' is not a path inside
the target`). Reds were staged in a scratch copy of `tools/govkit` and `tools/process-monitor`, one
edit per case, the fixture run from the copy. The arm itself was not run: the role hook refuses a
run that loads `selftest.py`.

A FOLLOW-UP COMMIT acted on the M6 checklist. `two-answers-to-one-question`: the attended stop's
text was spelled in both walks and the `walk` fixture; all three read `ATTENDED_STOP` now, and
`fixture walk --plant attended` and `fixture rollback` re-ran clean.
`test-oracle-read-from-a-historical-sha` and `suite-invalidated-by-a-commit-under-it`: the arm's in-process probe of
`check_rollback_vintage` read gov's own `HEAD` and `HEAD~1`, which a shallow clone or a commit made
mid-suite moves; it now builds a scratch repository of two commits, and a probe of the same five
cases over one printed the three refusals and the two passes.

Owed at the close: the `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`govkit selfcheck`, `recall floor arms`, `encoding posture`, `lexicon naming predicates` and
`spec tokens` legs, and the RED-first observation of `check_step_rollback`.

**Evidences:** TOOL-dSafePassage-4
- AC1 — `fixture rollback`, rc 0: the walk applied `s1` to `s4`, then `step fx/s4 · rolled-back`, `s3`, `s2`, `s1` in that order, every row `rolled-back`, `rollback: the target's bytes equal their bytes before the walk` (receipt and staging journal left out). `--plant partial-to`, rc 0: only `s4` and `s3` rolled back, `s1` and `s2` `applied`, `rollback: s1.txt and s2.txt present`. Red staged: `derive_reverse_steps` returning walk order printed `rollback: FAILED · the reverse walk's lines are not ['step fx/s4 · rolled-back', ...]`.
- AC2 — `--plant after-kill`, rc 0: `rollback: after the kill · fx/s3 failed · s3.txt present`; then `step fx/s4 · skipped (nothing applied)`, `s3`, `s2`, `s1` rolled back, bytes equal before the walk.
- AC3 — `--plant after-fail`, rc 0: `step fx/s3 · failed · exit 1: fx: s3 up fails by its plant`, `rollback: down canaries before the reverse walk: none`; then `s4` skipped and `s3`, `s2`, `s1` rolled back, bytes equal.
- AC4 — `--plant down-fails`, rc 1: `step fx/s4 · rolled-back`, `step fx/s3 · STOPPED · down exit 1: fx: s3 down fails by its plant`, `fx/s3` `('applied', 'down exit 1: ...')`, no `s2.down` or `s1.down`, no traceback; the repaired re-run printed `s3`, `s2`, `s1` rolled back, `s4 downed 1 time(s) in all · bytes equal`. `--plant witness-stays`, rc 1: `step fx/s2 · STOPPED · witness still holds after down`, `fx/s2` `('applied', 'witness still holds after down')`, no `s1.down`. Both print `stop text opens with an entry of DOWN_STOP_PREFIXES: yes`, and `python -c` over `upgrade_steps.DOWN_STOP_PREFIXES` read `[True, True, True]` for the two texts and the `down interrupted:` one (TOOL-dSafePassage-43 AC3, TOOL-dSafePassage-49 S2). `--plant unrecorded`, rc 0: `s2`'s row blanked with `s2.txt` present, all four rolled back, `s2.down` present. Red staged: move 4 continuing past a failed down printed `rollback: FAILED · the reverse walk went on past the stop` and `... did not resume at s3`.
- AC5 — `fixture rollback-update`, rc 0: a first run with `s1.down-fails` exited 1 with `the rollback's reverse walk stopped at fx/s1`, `file rows and gov_commit held at B`, the record ending `gov_commit: not moved, the reverse walk stopped at fx/s1`; the repaired run printed `step fx/s1 · rolled-back`, `s1's down found tools/demo/one.txt at B, before the write loop moved it`, `tools/demo/one.txt b'v1\n' · gov_commit A · schema 4`, and the record `down fx/s1: rolled-back`, `files: wrote 1 · moved 0 · deleted 0 · withheld 0 · conflicts 0`, `gov_commit: moved to <A8>`, `finished <utc>`. `--plant read-only`, rc 0: `govkit update —   would roll back fx/s1` alone, `step spawns during the read-only run: none`. NOT OBSERVED: the red "the stamp re-sets RECEIPT_SCHEMA", since this fixture holds no schema step and its downs leave schema 4, which equals `RECEIPT_SCHEMA`; TOOL-dSafePassage-19 and TOOL-dSafePassage-5 carry the rollback past the schema step.
- AC6 — `--plant refused`, `descendant`, `scoped`, `no-base`, rc 1 each, `update exits 2 · receipt unchanged · step spawns none`, naming respectively `roll back deliberately with \`update --rollback --to <A>\``, `which is not an ancestor of`, `so it takes no --kits`, `records no gov_commit`. A probe of `check_rollback_vintage` refused no base, a descendant and the receipt's own commit with no row, and passed an ancestor and its own commit with a row. Red staged: `demand_forward_vintage` dropped printed `rollback-update: FAILED · update did not refuse naming \`update --rollback --to\``.
- AC7 — `--plant callers`, rc 0: `a call of run_reverse_walk at govkit.py:<n>, in _cmd_update`, `one caller, update's _cmd_update`; over a planted second caller `in planted_caller` and `RED · 2 call(s)`.
- AC8 — `git grep -n -e "update --rollback" -e "update-reverted" -e "never rolls back" -- "help/upgrade-steps.md"` names all three inside "Rolling back"; `python tools/govkit/govkit.py --help` prints `govkit.py update --target <path> [--to <rev>] [--write] [--write-withdrawals] [--accept-role-moves] [--rollback]`.
